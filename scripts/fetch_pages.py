# -*- coding: utf-8 -*-
"""
fetch_pages.py — 模仿浏览器把一批网页抓到本地，存原始 HTML + 提取后的正文。

起因：2026-07-30 起，派 reader/核查 subagent 会让客户端闪退（两台机器同样表现），
精读改成「脚本抓取 → 主 agent 直接读本地文件」。抓回来的原文顺便留档。

用法：
    python scripts/fetch_pages.py <urls.txt> <outdir> [--sleep 1.5] [--only slug1,slug2]

urls.txt 每行一条：  slug|url        （# 开头是注释，空行忽略）
产物：
    <outdir>/<slug>.html   原始 HTML（照抓不动）
    <outdir>/<slug>.txt    提取后的正文（首行 URL、标题、抓取时刻，正文在后）
    <outdir>/_fetch.json   本轮每条的状态，给主 agent 核对用

抓不到就如实记 error，绝不换个像的链接充数。
"""
import sys, json, time, pathlib, re
import requests
from bs4 import BeautifulSoup

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Sec-Ch-Ua": '"Chromium";v="141", "Google Chrome";v="141", "Not?A_Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}
DROP = ["script", "style", "noscript", "nav", "header", "footer", "aside",
        "form", "svg", "iframe", "button"]


def extract(html):
    soup = BeautifulSoup(html, "lxml")
    title = soup.title.get_text(strip=True) if soup.title else ""
    for t in soup(DROP):
        t.decompose()
    node = soup.find("article") or soup.find("main") or soup.body or soup
    # 段落之间留空行，行内空白压掉
    for br in node.find_all("br"):
        br.replace_with("\n")
    text = node.get_text("\n", strip=True)
    text = re.sub(r"[ \t ]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, text


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    urlfile, outdir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    sleep = 1.5
    only = None
    for i, a in enumerate(sys.argv[3:]):
        if a == "--sleep":
            sleep = float(sys.argv[4 + i])
        if a == "--only":
            only = set(sys.argv[4 + i].split(","))
    outdir.mkdir(parents=True, exist_ok=True)

    jobs = []
    for line in urlfile.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        slug, url = line.split("|", 1)
        slug, url = slug.strip(), url.strip()
        if only and slug not in only:
            continue
        jobs.append((slug, url))

    sess = requests.Session()
    sess.headers.update(HEADERS)
    results = []
    for n, (slug, url) in enumerate(jobs, 1):
        rec = {"slug": slug, "url": url}
        try:
            r = sess.get(url, timeout=40, allow_redirects=True)
            rec["status"] = r.status_code
            rec["final_url"] = r.url
            rec["bytes"] = len(r.content)
            if r.status_code == 200:
                r.encoding = r.encoding or "utf-8"
                html = r.text
                (outdir / f"{slug}.html").write_text(html, encoding="utf-8")
                title, text = extract(html)
                rec["title"] = title
                rec["chars"] = len(text)
                head = (f"URL: {url}\nFINAL: {r.url}\nTITLE: {title}\n"
                        f"FETCHED: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"{'=' * 60}\n")
                (outdir / f"{slug}.txt").write_text(head + text, encoding="utf-8")
            else:
                rec["error"] = f"HTTP {r.status_code}"
        except Exception as e:
            rec["status"] = None
            rec["error"] = f"{type(e).__name__}: {e}"
        results.append(rec)
        flag = "OK " if rec.get("status") == 200 else "FAIL"
        print(f"[{n}/{len(jobs)}] {flag} {slug:28s} "
              f"{rec.get('status')} {rec.get('chars', 0)} chars  {rec.get('error', '')}")
        if n < len(jobs):
            time.sleep(sleep)

    (outdir / "_fetch.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    ok = sum(1 for r in results if r.get("status") == 200)
    print(f"\n成功 {ok} / {len(results)}，产物在 {outdir}")


if __name__ == "__main__":
    main()
