# -*- coding: utf-8 -*-
"""
update_seen.py <date> — 把当期 daily.json 条目回写进各源 seen.json（幂等）。

归属判断（按优先级）：
  1. work/manifest.json 里同 URL 的条目自带 source 和 date（scout 写的，最准）；
  2. 域名 → 源 slug（由各源 meta.json 的 homepage/fetch_url 建表；
     特例：huggingface.co/papers → hf-papers、/blog → huggingface、
     x.com/<handle> → 对应 x-* 源）。
两条都对不上的打印出来，agent 对照 manifest 手动补进对应 seen.json。
odds（manifold）不做 seen。

条目前插 {id: url, title, date, reported: true, report_date: <date>}；
同 id 已存在就地改 reported/report_date，不重复插。
"""
import sys, json, re, pathlib
from urllib.parse import urlsplit
from dailyjson import load_daily

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT_SECTIONS = ["industry", "angle", "deep", "papers", "regulation", "official", "brief", "fun"]


def host_of(url):
    try:
        h = urlsplit(url).netloc.lower()
        return re.sub(r"^(www|old|m|new)\.", "", h)
    except Exception:
        return ""


def canon(url):
    return (url or "").strip().rstrip("/")


def build_maps():
    """host→slug、x_handle→slug。huggingface.co 冲突走路径特例。"""
    host_map, x_map = {}, {}
    for meta_path in sorted((ROOT / "sources").glob("*/meta.json")):
        slug = meta_path.parent.name
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
        except Exception:
            continue
        if slug.startswith("x-"):
            for u in (meta.get("homepage", ""), meta.get("fetch_url", "")):
                m = re.search(r"(?:x\.com|twitter\.com|nitter[^/]*)/(@?\w+)", u)
                if m:
                    x_map[m.group(1).lstrip("@").lower()] = slug
            continue
        if slug in ("manifold", "neodrop"):
            continue
        for u in (meta.get("homepage", ""), meta.get("fetch_url", "")):
            h = host_of(u)
            if h and h not in ("huggingface.co",):
                host_map.setdefault(h, slug)
    return host_map, x_map


def find_slug(url, host_map, x_map):
    h = host_of(url)
    path = urlsplit(url).path
    if h == "huggingface.co":
        return "hf-papers" if path.startswith("/papers") else "huggingface"
    if h in ("x.com", "twitter.com"):
        m = re.match(r"/(\w+)/status/", path)
        if m:
            return x_map.get(m.group(1).lower())
        return None
    return host_map.get(h)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/update_seen.py <date>")
    date = sys.argv[1]
    ddir = ROOT / "reports" / date
    d = load_daily(ddir / "daily.json")

    # manifest：url → (source, date)
    man_map = {}
    man_path = ddir / "work" / "manifest.json"
    if man_path.exists():
        try:
            man = json.loads(re.sub(r",(\s*[}\]])", r"\1", man_path.read_text(encoding="utf-8-sig")))
        except Exception:
            man = {}
        for g in man.get("deep_groups") or []:
            for it in g.get("items") or []:
                man_map[canon(it.get("url"))] = (it.get("source"), it.get("date"))
        for sec in ("radar_true", "fun"):
            for it in man.get(sec) or []:
                man_map[canon(it.get("url"))] = (it.get("source"), it.get("date"))

    host_map, x_map = build_maps()

    written, updated, unmatched = [], [], []
    for sec in CONTENT_SECTIONS:
        # 主链接 +（独家视角的）额外来源，都要回写 seen
        pairs = []
        for it in d.get(sec) or []:
            pairs.append((it.get("url", ""), it.get("title") or it.get("label") or ""))
            pairs += [(s.get("url", ""), s.get("name", "")) for s in it.get("sources") or []]
        for url, title in pairs:
            if not url.startswith("http"):
                continue
            slug, item_date = None, None
            hit = man_map.get(canon(url))
            if hit:
                slug, item_date = hit
            if not slug:
                slug = find_slug(url, host_map, x_map)
            seen_path = ROOT / "sources" / (slug or "_") / "seen.json"
            if not slug or not seen_path.exists():
                unmatched.append((sec, title, url))
                continue
            seen = json.loads(seen_path.read_text(encoding="utf-8-sig"))
            entry = next((e for e in seen if canon(e.get("id")) == canon(url)), None)
            if entry:
                if not entry.get("reported"):
                    entry["reported"] = True
                    entry["report_date"] = date
                    updated.append((slug, title))
                else:
                    continue  # 已标记，跳过
            else:
                seen.insert(0, {"id": url, "title": title,
                                "date": item_date or date,
                                "reported": True, "report_date": date})
                written.append((slug, title))
            seen_path.write_text(json.dumps(seen, ensure_ascii=False, indent=1) + "\n",
                                 encoding="utf-8")

    for slug, t in written:
        print(f"＋ [{slug}] {t}")
    for slug, t in updated:
        print(f"改 [{slug}] {t}（已存在，补标 reported）")
    if unmatched:
        print("\n⚠️ 以下条目没匹配到源，对照 manifest 手动补：")
        for sec, t, u in unmatched:
            print(f"  [{sec}] {t}\n      {u}")
    print(f"\nseen 回写 {date}：新插 {len(written)} / 补标 {len(updated)} / 未匹配 {len(unmatched)}")


if __name__ == "__main__":
    main()
