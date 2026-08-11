# -*- coding: utf-8 -*-
"""
collect_sources.py <date> [--now ISO_TIME] [--outdir DIR]

日报 scout 的确定性抓取层：一次扫完 sources/ 下全部信源，完成网络抓取、
URL 标准化、时间窗、seen 和往期已发 URL 的机械去重，再把候选交给 scout
做语义去重与分桶。

默认产物：
  reports/<date>/work/scout_candidates.json  标准化候选
  reports/<date>/work/scout_fetch.json       每源抓取诊断

不写 seen.json，不写 manifest.json。抓不到如实记 failed。
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import time
from email.utils import parsedate_to_datetime
from urllib.parse import urljoin, urlsplit

import requests
from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from check_dup_urls import canon, collect_history  # noqa: E402

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36")
HEADERS = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8"}
HTML_CAPS = {
    "anthropic": 20, "anthropic-research": 30, "claude-blog": 25, "hf-papers": 35,
    "huggingface": 30, "neodrop": 30, "the-batch": 15,
    "thinking-machines": 15, "meta-ai": 25, "xai": 40,
}
DATE_TOKEN_RE = re.compile(
    r"20\d\d[-/]\d\d[-/]\d\d|"
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+20\d\d|"
    r"\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d\d",
    re.I,
)


def clean(value):
    return re.sub(r"\s+", " ", value or "").strip()


def norm_url(url):
    """沿用 check_dup_urls 的身份指纹，同时返回可发布的干净 URL。"""
    if not url or not url.startswith("http"):
        return ""
    parts = urlsplit(url)
    # scout 候选无需保留追踪参数；canon 已负责更强的跨站身份判断。
    return f"{parts.scheme.lower()}://{parts.netloc.lower()}{parts.path.rstrip('/')}"


def parse_date(value, now):
    value = clean(str(value or ""))
    if not value:
        return None
    if re.fullmatch(r"\d{2}-\d{2}", value):
        parsed = dt.datetime.strptime(f"{now.year}-{value}", "%Y-%m-%d")
        return parsed.replace(tzinfo=dt.timezone.utc)
    m = re.search(r"(\d+)\s+(hour|day|week)s?\s+ago", value, re.I)
    if m:
        hours = {"hour": 1, "day": 24, "week": 168}[m.group(2).lower()]
        return now - dt.timedelta(hours=int(m.group(1)) * hours)
    try:
        parsed = parsedate_to_datetime(value)
    except Exception:
        try:
            parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except Exception:
            m = re.search(
                r"20\d\d[-/]\d\d[-/]\d\d|"
                r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s+20\d\d|"
                r"\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+20\d\d",
                value, re.I)
            if not m:
                return None
            token = m.group(0).replace("/", "-")
            parsed = None
            for fmt in ("%Y-%m-%d", "%b %d, %Y", "%B %d, %Y", "%d %B %Y"):
                try:
                    parsed = dt.datetime.strptime(token, fmt)
                    break
                except ValueError:
                    pass
            if parsed is None:
                return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed.astimezone(dt.timezone.utc)


def node_text(node, *names):
    for name in names:
        found = node.find(name)
        if found:
            value = found.get_text(" ", strip=True)
            if value:
                return value
    return ""


def parse_feed(body):
    soup = BeautifulSoup(body, "xml")
    rows = []
    for item in soup.find_all(["item", "entry"]):
        link = item.find("link")
        url = (link.get("href") if link else "") or (link.get_text(strip=True) if link else "")
        if not url:
            url = node_text(item, "guid", "id")
        raw = node_text(item, "description", "summary", "content", "content:encoded")
        summary = BeautifulSoup(raw, "lxml").get_text(" ", strip=True) if raw else ""
        rows.append({
            "title": node_text(item, "title"), "url": url,
            "date": node_text(item, "pubDate", "published", "updated", "dc:date", "date"),
            "summary": summary[:1200],
        })
    return rows


def html_rule(slug, url):
    path = urlsplit(url).path.rstrip("/")
    rules = {
        "anthropic": r"^/news/[^/]+$",
        "anthropic-research": r"^/research/[^/]+$",
        "claude-blog": r"^/blog/[^/]+$",
        "meta-ai": r"^/blog/[^/]+$",
        "xai": r"^/news/[^/]+$",
        "hf-papers": r"^/papers/\d{4}\.\d{4,5}$",
        "huggingface": r"^/blog/[^/]+(?:/[^/]+)?$",
        "the-batch": r"^/the-batch/issue-\d+$",
        "thinking-machines": r"^/blog/[^/]+$",
    }
    return bool(re.match(rules[slug], path)) if slug in rules else True


def parse_html(body, base, slug):
    soup = BeautifulSoup(body, "lxml")
    best = {}
    for anchor in soup.select("a[href]"):
        url = norm_url(urljoin(base, anchor.get("href", "")))
        if not url or not html_rule(slug, url):
            continue
        anchor_text = clean(anchor.get_text(" ", strip=True))
        heading = anchor.find(["h1", "h2", "h3", "h4"])
        title = clean(heading.get_text(" ", strip=True) if heading else anchor_text)
        parent = anchor
        context = title
        for _ in range(5):
            parent = parent.parent
            if not parent:
                break
            value = clean(parent.get_text(" ", strip=True))
            if len(value) > len(title) + 12 and len(value) < 1200:
                context = value
                break
        # Read more / 空锚点时，从卡片上下文取一段可辨认标题；最终仍由 scout 判断。
        if not title or title.lower() in {"read more", "learn more", "view all", "view all articles"}:
            title = context
        date_match = DATE_TOKEN_RE.search(anchor_text)
        row = {"title": title[:350], "url": url,
               "date": date_match.group(0) if date_match else "", "summary": context[:1200]}
        # HF Papers 等卡片对同一 URL 有标题、票数、作者等多个锚点；优先保留
        # 像自然语言标题的锚点，不让更长的整卡文本盖掉真正标题。
        words = title.split()
        natural_title = (4 <= len(words) <= 35 and 18 <= len(title) <= 240
                         and not title.lower().startswith("submitted by")
                         and not title.isdigit())
        score = (10000 if natural_title else 0) + len(row["summary"])
        if url not in best or score > best[url][0]:
            best[url] = (score, row)
    return [value[1] for value in best.values()][:HTML_CAPS.get(slug, 30)]


def parse_browser_html(page, base, slug):
    rows = page.eval_on_selector_all("a[href]", """els => els.map(a => {
      let n=a, ctx='';
      for(let i=0;i<5 && n;i++,n=n.parentElement){
        const t=(n.innerText||'').trim();
        if(t.length>30 && t.length<1200){ctx=t; break;}
      }
      return [(a.innerText||'').trim(), a.href, ctx];
    })""")
    # 复用同一套 URL 规则；构造最小 HTML，避免维护第二套清洗逻辑。
    pieces = []
    for title, url, context in rows:
        pieces.append(f'<div>{context}<a href="{url}">{title}</a></div>')
    return parse_html("".join(pieces), base, slug)


def parse_neodrop(page, base):
    """Neodrop 是客户端渲染；按日期卡片提取，导航链接不进候选。"""
    lines = [clean(line) for line in page.inner_text("body").splitlines() if clean(line)]
    rows = []
    for i, line in enumerate(lines):
        if not re.fullmatch(r"\d{2}-\d{2}", line):
            continue
        title = lines[i + 1] if i + 1 < len(lines) else ""
        summary = lines[i + 2] if i + 2 < len(lines) else ""
        if "AI+机器人行业晨报" not in title:
            continue
        rows.append({"title": title, "url": base, "date": line, "summary": summary[:1200]})
    return rows[:3]


def load_seen(slug):
    path = ROOT / "sources" / slug / "seen.json"
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return set()
    rows = data if isinstance(data, list) else []
    keys = set()
    for row in rows:
        url = row if isinstance(row, str) else (row.get("id") or row.get("url", ""))
        if url and str(url).startswith("http"):
            keys.add(canon(str(url))[0])
    return keys


def api_items(slug, data):
    if slug == "hacker-news":
        return [{
            "title": row.get("title") or "",
            "url": row.get("url") or row.get("story_url") or "",
            "date": row.get("created_at") or "",
            "summary": f"points={row.get('points')} comments={row.get('num_comments')}",
        } for row in data.get("hits", [])]
    if slug == "manifold":
        rows = data if isinstance(data, list) else data.get("markets", [])
        return [{
            "title": row.get("question", ""), "url": row.get("url", ""),
            "date": "", "summary": json.dumps({
                "probability": row.get("probability"), "volume": row.get("volume"),
                "volume24Hours": row.get("volume24Hours"), "liquidity": row.get("liquidity"),
            }, ensure_ascii=False),
        } for row in rows]
    return []


class BrowserFallback:
    def __init__(self):
        self.pw = self.browser = self.page = None

    def start(self):
        if self.page:
            return
        from playwright.sync_api import sync_playwright
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(headless=True)
        context = self.browser.new_context(user_agent=UA, locale="en-US", extra_http_headers=HEADERS)
        self.page = context.new_page()

    def fetch(self, url, method, slug):
        self.start()
        response = self.page.goto(url, wait_until="domcontentloaded", timeout=45000)
        if not response or response.status != 200:
            raise RuntimeError(f"browser HTTP {response.status if response else 'none'}")
        if method == "rss":
            return parse_feed(response.text())
        self.page.wait_for_timeout(2500)
        if slug == "neodrop":
            return parse_neodrop(self.page, response.url)
        return parse_browser_html(self.page, response.url, slug)

    def close(self):
        if self.browser:
            self.browser.close()
        if self.pw:
            self.pw.stop()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("date")
    ap.add_argument("--now", help="测试用 ISO 时间；默认当前时间")
    ap.add_argument("--outdir", type=pathlib.Path)
    args = ap.parse_args()
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", args.date):
        raise SystemExit("date 必须是 YYYY-MM-DD")
    outdir = args.outdir or ROOT / "reports" / args.date / "work"
    outdir.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.fromisoformat(args.now) if args.now else dt.datetime.now().astimezone()
    if now.tzinfo is None:
        now = now.replace(tzinfo=dt.timezone.utc)
    now = now.astimezone(dt.timezone.utc)

    history = collect_history(args.date)
    history_keys = set(history)
    session = requests.Session()
    session.headers.update(HEADERS)
    browser = BrowserFallback()
    candidates, diagnostics = [], []

    for meta_path in sorted((ROOT / "sources").glob("*/meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        slug = meta_path.parent.name
        method, url = meta.get("fetch_method", "html"), meta.get("fetch_url", "")
        window_hours = int(meta.get("window_hours", 168))
        seen_keys = load_seen(slug)
        started = time.time()
        route, error, rows = "requests", "", []
        try:
            if method == "api":
                api_url = re.sub(r"([?&]limit=)\d+", r"\g<1>100", url) if slug == "manifold" else url
                response = session.get(api_url, timeout=30)
                response.raise_for_status()
                rows = api_items(slug, response.json())
            elif method == "rss":
                response = session.get(url, timeout=30, allow_redirects=True)
                response.raise_for_status()
                rows = parse_feed(response.text)
            else:
                response = session.get(url, timeout=25, allow_redirects=True)
                if (response.status_code != 200 or len(response.text) < 1500
                        or method == "nitter-html" or slug == "neodrop"):
                    raise RuntimeError(f"HTTP {response.status_code}, body={len(response.text)}")
                rows = parse_html(response.text, response.url, slug)
        except Exception as first_error:
            route = "chromium"
            try:
                rows = browser.fetch(url, method, slug)
            except Exception as second_error:
                error = f"requests={first_error}; chromium={second_error}"

        kept = []
        for row in rows:
            candidate_url = norm_url(row.get("url", ""))
            if not candidate_url:
                continue
            key = canon(candidate_url)[0]
            # Manifold 没有 seen；history_keys 会挡已报市场。其余源两层都挡。
            if key in seen_keys or key in history_keys:
                continue
            date_value = clean(str(row.get("date", "")))
            when = parse_date(date_value, now) or parse_date(row.get("summary", ""), now)
            if when and (now - when).total_seconds() > window_hours * 3600:
                continue
            if method == "html" and not when and slug != "hf-papers":
                continue
            title = clean(row.get("title", ""))
            if not title or title.lower() in {"read more", "learn more", "home", "blog"}:
                continue
            kept.append({
                "source": slug, "title": title, "url": candidate_url,
                "date": date_value, "summary": clean(row.get("summary", ""))[:1200],
                "fetch_route": route, "date_known": bool(when),
                "weight": meta.get("weight", ""), "length_hint": meta.get("length_hint", ""),
            })

        # 同 URL 取信息最完整的一条；HTML 无日期条目由 seen 兜底，并受源级 cap 控制。
        best = {}
        for row in kept:
            score = len(row["title"]) + len(row["summary"])
            if row["url"] not in best or score > best[row["url"]][0]:
                best[row["url"]] = (score, row)
        kept = [value[1] for value in best.values()]
        if slug == "manifold":
            kept = kept[:25]  # API 已按 liquidity 排序；给 scout 留选择余地但不灌 70 多条。
        candidates.extend(kept)
        diagnostics.append({
            "slug": slug, "url": url, "method": method, "route": route,
            "status": "failed" if error else "ok", "raw_items": len(rows),
            "candidates": len(kept), "elapsed_s": round(time.time() - started, 1),
            "error": error,
        })
        print(f"[{slug:18s}] {route:8s} {'FAIL' if error else 'OK  '} "
              f"raw={len(rows):3d} keep={len(kept):3d} {error}")
        if method == "nitter-html":
            time.sleep(4)

    browser.close()
    candidates.sort(key=lambda row: (row["source"], row["date"], row["title"]))
    candidate_path = outdir / "scout_candidates.json"
    fetch_path = outdir / "scout_fetch.json"
    candidate_path.write_text(json.dumps({
        "date": args.date, "generated_at": dt.datetime.now().astimezone().isoformat(),
        "count": len(candidates), "items": candidates,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    fetch_path.write_text(json.dumps({
        "date": args.date, "source_count": len(diagnostics),
        "failed_count": sum(row["status"] == "failed" for row in diagnostics),
        "sources": diagnostics,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n候选 {len(candidates)} 条；失败 {sum(row['status'] == 'failed' for row in diagnostics)} 源")
    print(candidate_path)
    print(fetch_path)


if __name__ == "__main__":
    main()
