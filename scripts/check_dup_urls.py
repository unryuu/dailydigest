# -*- coding: utf-8 -*-
"""
check_dup_urls.py <date> — 查当期候选/成稿里的 URL 有没有在往期日报里发过。

历史口径（算「已发」的）：往期 reports/<d>/daily.json + reports/<d>/messages.json
（manifest / preedit 只是候选和快照，不算已发）。

比对分两档：
1. 规范化指纹精确匹配：统一协议、去 www/old/m 前缀、去跟踪参数、去尾斜杠后，
   再按站点提取真正的身份标识（LW 帖 id、manifold slug、arxiv/HF 论文号、
   reddit 帖 id、HN item id、substack 文章 slug、youtube 视频 id），
   同一篇东西换个镜像/参数也能对上。
2. 同域名路径相似度（difflib >= 0.85）：只报「疑似」，人来判断。

赔率特殊处理：撞了不直接判丢，报上次日期、上次概率、间隔天数，agent 按
「隔得久或概率变化大可以再报」的规矩定。

用法：python scripts/check_dup_urls.py 2026-07-19
自动检查 reports/<date>/work/manifest.json 和 reports/<date>/daily.json。
"""
import sys, os, re, json, difflib
from datetime import date as _date
from urllib.parse import urlsplit, parse_qsl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "reports")

DROP_PARAMS = re.compile(r"^(utm_|ref$|ref_|fbclid|gclid|mc_|s$|si$|source$)")


def load_tolerant_json(path):
    """读 JSON，容忍尾逗号。"""
    text = open(path, encoding="utf-8").read()
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return json.loads(text)


def canon(url):
    """URL -> (指纹key, 域名, 路径)。同一篇内容的不同写法应得到同一个 key。"""
    u = url.strip()
    if not re.match(r"^https?://", u):
        u = "https://" + u
    parts = urlsplit(u)
    host = parts.netloc.lower()
    host = re.sub(r"^(www|old|m|new)\.", "", host)
    path = parts.path.rstrip("/")
    q = [(k, v) for k, v in parse_qsl(parts.query) if not DROP_PARAMS.match(k.lower())]

    # 站点特例：提取真正的身份标识
    m = re.search(r"/posts/([A-Za-z0-9]+)", path)
    if host in ("lesswrong.com", "alignmentforum.org", "greaterwrong.com") and m:
        return ("lesswrong", m.group(1)), host, path
    if host == "manifold.markets":
        slug = path.split("/")[-1] if path else ""
        return ("manifold", slug), host, path
    m = re.search(r"/papers?/(\d{4}\.\d{4,5})", path) or (
        re.search(r"/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", path) if "arxiv" in host else None
    )
    if m:
        return ("paper", m.group(1)), host, path
    m = re.search(r"/comments/([a-z0-9]+)", path)
    if "reddit" in host and m:
        return ("reddit", m.group(1)), host, path
    if host == "news.ycombinator.com":
        qd = dict(q)
        if "id" in qd:
            return ("hn", qd["id"]), host, path
    if host.endswith("substack.com"):
        m = re.search(r"/p/([^/]+)", path)
        if m:
            return ("substack", host.split(".")[0], m.group(1)), host, path
    if host in ("youtube.com", "youtu.be"):
        qd = dict(q)
        vid = qd.get("v") or path.split("/")[-1]
        return ("youtube", vid), host, path

    key = (host, path.lower(), tuple(sorted(q)))
    return key, host, path


SPECIAL_KEYS = {"lesswrong", "manifold", "paper", "reddit", "hn", "substack", "youtube"}


def is_special(key):
    return key[0] in SPECIAL_KEYS


def iter_report_dates():
    for name in sorted(os.listdir(REPORTS)):
        if re.match(r"^\d{4}-\d{2}-\d{2}$", name):
            yield name


def collect_history(before_date):
    """返回 {key: [ {date, section, url, prob} ]}，只收 before_date 之前的已发内容。"""
    hist = {}

    def add(url, d, section, prob=None):
        if not url or not isinstance(url, str) or not url.startswith("http"):
            return
        key, host, path = canon(url)
        hist.setdefault(key, []).append(
            {"date": d, "section": section, "url": url, "prob": prob,
             "host": host, "path": path, "special": is_special(key)}
        )

    for d in iter_report_dates():
        if d >= before_date:
            continue
        folder = os.path.join(REPORTS, d)
        daily = os.path.join(folder, "daily.json")
        if os.path.exists(daily):
            try:
                data = load_tolerant_json(daily)
            except Exception as e:
                print(f"  [warn] {d}/daily.json 解析失败，跳过: {e}")
                data = {}
            for sec, cname in [("gold", "金"), ("silver", "银"), ("radar", "雷达"), ("fun", "乐子"),
                               ("industry", "行业"), ("deep", "长文"), ("papers", "论文"),
                               ("regulation", "监管"), ("official", "公告")]:
                for item in data.get(sec, []) or []:
                    add(item.get("url"), d, cname)
            for item in data.get("odds", []) or []:
                add(item.get("url"), d, "赔率", prob=item.get("prob"))
        # 旧格式（06 月）：messages.json 里正则捞 URL
        for msg_path in (os.path.join(folder, "messages.json"),
                         os.path.join(REPORTS, f"{d}.messages.json")):
            if os.path.exists(msg_path):
                try:
                    text = open(msg_path, encoding="utf-8").read()
                except Exception:
                    continue
                for u in re.findall(r'https?://[^\s"\'<>\\]+', text):
                    add(u.rstrip('.,)]。，'), d, "旧期正文")
    return hist


def collect_targets(folder):
    """返回 [(文件名, 区名, url, prob)]。"""
    out = []
    manifest = os.path.join(folder, "work", "manifest.json")
    if os.path.exists(manifest):
        m = load_tolerant_json(manifest)
        for g in m.get("deep_groups", []) or []:
            for item in g.get("items", []) or []:
                out.append(("manifest", f"精读候选 {g.get('group', '')}", item.get("url"), None))
        for item in m.get("radar_true", []) or []:
            out.append(("manifest", "雷达候选", item.get("url"), None))
        for item in m.get("fun", []) or []:
            out.append(("manifest", "乐子候选", item.get("url"), None))
        for item in m.get("odds_box", []) or []:
            out.append(("manifest", "赔率候选", item.get("url"), item.get("prob")))
    daily = os.path.join(folder, "daily.json")
    if os.path.exists(daily):
        d = load_tolerant_json(daily)
        for sec, cname in [("gold", "金"), ("silver", "银"), ("radar", "雷达"), ("fun", "乐子"),
                           ("industry", "行业"), ("deep", "长文"), ("papers", "论文"),
                           ("regulation", "监管"), ("official", "公告")]:
            for item in d.get(sec, []) or []:
                out.append(("daily", cname, item.get("url"), None))
        for item in d.get("odds", []) or []:
            out.append(("daily", "赔率", item.get("url"), item.get("prob")))
    return out


def days_between(d1, d2):
    a = _date(*map(int, d1.split("-")))
    b = _date(*map(int, d2.split("-")))
    return abs((b - a).days)


def main():
    if len(sys.argv) != 2 or not re.match(r"^\d{4}-\d{2}-\d{2}$", sys.argv[1]):
        print(__doc__)
        sys.exit(2)
    target_date = sys.argv[1]
    folder = os.path.join(REPORTS, target_date)
    if not os.path.isdir(folder):
        print(f"目录不存在: {folder}")
        sys.exit(2)

    hist = collect_history(target_date)
    targets = collect_targets(folder)
    if not targets:
        print("当期没有 manifest.json / daily.json 可查。")
        sys.exit(2)

    exact_hits, fuzzy_hits = [], []
    # 域名 -> 历史条目列表（给疑似匹配用）
    by_host = {}
    for entries in hist.values():
        for e in entries:
            by_host.setdefault(e["host"], []).append(e)

    for fname, section, url, prob in targets:
        if not url or not url.startswith("http"):
            continue
        key, host, path = canon(url)
        if key in hist:
            prev = sorted(hist[key], key=lambda e: e["date"])[-1]
            exact_hits.append((fname, section, url, prob, prev))
            continue
        # 疑似：同域名、路径相似。特殊站点（论文号/帖子 id 本身就是精确身份）不做疑似；
        # 「同模板不同编号」（去掉数字后路径相同）判为不同条目，跳过。
        if is_special(key):
            continue
        best = None
        for e in by_host.get(host, []):
            if e.get("special") or not e["path"] or not path:
                continue
            p1, p2 = path.lower(), e["path"].lower()
            if p1 != p2 and re.sub(r"\d+", "", p1) == re.sub(r"\d+", "", p2):
                continue
            r = difflib.SequenceMatcher(None, p1, p2).ratio()
            if r >= 0.85 and (best is None or r > best[0]):
                best = (r, e)
        if best:
            fuzzy_hits.append((fname, section, url, best[0], best[1]))

    checked = sum(1 for f, s, u, p in targets if u and u.startswith("http"))
    print(f"查重 {target_date}：候选/成稿 URL {checked} 条，对比往期已发 {sum(len(v) for v in hist.values())} 条记录\n")

    if not exact_hits and not fuzzy_hits:
        print("✅ 无重复")
        return

    for fname, section, url, prob, prev in exact_hits:
        if "赔率" in section:
            gap = days_between(prev["date"], target_date)
            old_prob = prev.get("prob") or "?"
            print(f"⚠️ [{fname}/{section}] 赔率撞往期：{url}")
            print(f"   上次 {prev['date']}（{prev['section']}区，prob={old_prob}），距今 {gap} 天，本次 prob={prob or '?'}")
            print(f"   → 隔得久或概率变化大可再报，否则丢弃")
        else:
            print(f"❌ [{fname}/{section}] 与往期重复，建议丢弃：{url}")
            print(f"   已于 {prev['date']} 发过（{prev['section']}区）：{prev['url']}")
    for fname, section, url, ratio, prev in fuzzy_hits:
        print(f"❓ [{fname}/{section}] 疑似与往期重复（路径相似度 {ratio:.2f}），人工确认：{url}")
        print(f"   往期 {prev['date']}（{prev['section']}区）：{prev['url']}")


if __name__ == "__main__":
    main()
