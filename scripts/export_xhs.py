# -*- coding: utf-8 -*-
"""
export_xhs.py <date> — daily.json → 小红书竖卡（宽 1242，纵向不限长）。

每个分区一整张卡，外加一张封面卡（当日金银看点）。内容多高图就多高，
不足 3:4（1656px）时补底到 3:4。沿用日报长图的主题配色排版；
小红书无外链，图上不渲 URL、不放引流水印。

输出：reports/<date>/dist/小红书/xhs-01.png ...（HTML 中间产物同目录，已 gitignore）

用法：python scripts/export_xhs.py <date>
"""
import sys, json, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
from dailyjson import load_daily

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
LXGW = ROOT / "fonts" / "LXGWWenKai-Regular.ttf"

CANVAS_W, CANVAS_H = 1242, 1656  # 小红书竖图 3:4

BG      = "#EDEFE2"
CARD    = "#F7F8F0"
INK     = "#2F2E27"
SUBINK  = "#6B6A5E"
GOLD    = "#B8901F"
SILVER  = "#7C8894"
ODDS    = "#5E8C5A"

SECTIONS = [
    ("industry",   "🗞️", "行业大事", "#A8562F"),
    ("deep",       "📖", "深度长文", "#4E7CA1"),
    ("papers",     "🧪", "新鲜论文", "#3F8E7E"),
    ("regulation", "🏛️", "监管动向", "#8A6FA8"),
    ("official",   "📢", "官方公告", "#7C8894"),
    ("fun",        "🎪", "乐子汇总", "#C2703C"),
]
ODDS_HEAD = ("odds", "🎲", "赔率盒子", ODDS)

# 版式（内容区宽 = 1242 - 页边 2*46 - 卡片内边 2*36 ≈ 1078）
PAD_PAGE = 46
F_TITLE, LH_TITLE = 50, 68
F_BODY,  LH_BODY  = 42, 64
CONTENT_W = CANVAS_W - PAD_PAGE * 2 - 36 * 2


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


CSS = f"""
@font-face {{ font-family:"LXGW WenKai"; src:url("{LXGW.as_uri()}"); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ background:{BG}; }}
.page {{ width:{CANVAS_W}px; min-height:{CANVAS_H}px; background:{BG};
        padding:{PAD_PAGE}px {PAD_PAGE}px 0; position:relative; }}
.kick {{ font-family:"Microsoft YaHei",sans-serif; font-size:34px; color:{SUBINK}; }}
.sec {{ display:flex; align-items:center; gap:16px; margin:26px 0 10px; }}
.sec .bar {{ width:12px; height:52px; border-radius:6px; }}
.sec .label {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:56px; }}
.item {{ background:{CARD}; border-radius:20px; padding:28px 36px; margin:18px 0; box-shadow:0 2px 0 rgba(0,0,0,.04); }}
.item .ttl {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:{F_TITLE}px; line-height:{LH_TITLE}px; color:{INK}; }}
.tag {{ display:inline-block; vertical-align:5px; font-family:"Microsoft YaHei",sans-serif; font-weight:bold;
       font-size:32px; line-height:1; color:#fff; padding:8px 18px 10px; border-radius:10px; margin-right:14px; }}
.item .body {{ font-family:"LXGW WenKai",serif; font-size:{F_BODY}px; line-height:{LH_BODY}px; color:{INK}; margin-top:14px; }}
.item .body p {{ margin-top:14px; }}
.item .body p:first-child {{ margin-top:0; }}
.odd {{ display:flex; align-items:center; gap:22px; padding:20px 6px; border-bottom:2px solid rgba(0,0,0,.06); }}
.odd .q {{ flex:1; font-family:"LXGW WenKai",serif; font-size:42px; line-height:1.42; color:{INK}; }}
.odd .qn {{ font-family:"LXGW WenKai",serif; font-size:32px; color:{SUBINK}; margin-top:6px; }}
.odd .p {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:56px; color:{ODDS}; min-width:170px; text-align:right; }}
.foot {{ margin:40px 0 44px; text-align:center;
        font-family:"Microsoft YaHei",sans-serif; font-size:32px; color:{SUBINK}; }}
/* 封面 */
.cvr {{ display:flex; flex-direction:column; height:{CANVAS_H}px; padding-bottom:120px; }}
.cvr .big {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:120px; color:{INK}; margin-top:90px; }}
.cvr .date {{ font-family:"Microsoft YaHei",sans-serif; font-size:56px; color:{SUBINK}; margin-top:18px; }}
.cvr .rule {{ height:6px; background:{INK}; opacity:.12; margin:56px 0 40px; }}
.cvr .lead {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:44px; color:{SUBINK}; margin-bottom:8px; }}
.hl {{ display:flex; gap:18px; margin:20px 0; align-items:flex-start; }}
.hl .dot {{ width:14px; height:14px; border-radius:7px; margin-top:26px; flex:none; }}
.hl .t {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:46px; line-height:1.4; color:{INK}; }}
"""


def head_html(emoji, name, color):
    return (f'<div class="sec"><div class="bar" style="background:{color}"></div>'
            f'<div class="label" style="color:{color}">{emoji} {name}</div></div>')


def item_html(it):
    tier = it.get("tier", "none")
    tag = ""
    if tier == "gold":
        tag = f'<span class="tag" style="background:{GOLD}">金</span>'
    elif tier == "silver":
        tag = f'<span class="tag" style="background:{SILVER}">银</span>'
    body = "".join(f"<p>{esc(p.strip())}</p>" for p in it.get("body", "").split("\n\n") if p.strip())
    body_div = f'<div class="body">{body}</div>' if body else ""
    return f'<div class="item"><div class="ttl">{tag}{esc(it.get("title") or "")}</div>{body_div}</div>'


def odds_html(o):
    qn = f'<div class="qn">{esc(o["note"])}</div>' if o.get("note") else ""
    return (f'<div class="odd"><div class="q">{esc(o.get("question",""))}{qn}</div>'
            f'<div class="p">{esc(o.get("prob",""))}</div></div>')


def wrap_page(inner, date_label, page_no, total):
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body><div class="page">'
            f'<div class="kick">📰 AI 日报 · {esc(date_label)}</div>'
            f'{inner}'
            f'<div class="foot">{page_no} / {total}</div>'
            f'</div></body></html>')


def cover_html(d):
    hls = []
    for key, emoji, name, color in SECTIONS + [(ODDS_HEAD[0],) + ODDS_HEAD[1:]]:
        for it in d.get(key, []):
            if it.get("tier") in ("gold", "silver"):
                hls.append((color, it.get("title") or ""))
    rows = "".join(f'<div class="hl"><div class="dot" style="background:{c}"></div>'
                   f'<div class="t">{esc(t)}</div></div>' for c, t in hls)
    inner = (f'<div class="cvr"><div class="big">AI 日报</div>'
             f'<div class="date">{esc(d.get("date_label",""))} · 今天值得知道的事</div>'
             f'<div class="rule"></div><div class="lead">今日看点</div>{rows}</div>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body><div class="page" style="padding:{PAD_PAGE}px">{inner}</div></body></html>')


def render_png(html, outdir, stem):
    from PIL import Image
    html_path = outdir / f"{stem}.html"
    raw = outdir / f"{stem}.raw.png"
    out = outdir / f"{stem}.png"
    html_path.write_text(html, encoding="utf-8")
    bg_hex = BG.lstrip("#") + "ff"
    cmd = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--default-background-color={bg_hex}",
           f"--screenshot={raw}", f"--window-size={CANVAS_W},20000", html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not raw.exists():
        raise SystemExit(f"Chrome 渲染失败（{stem}）：\n{r.stderr[:800]}")
    im = Image.open(raw).convert("RGB")
    W, H = im.size
    bg = tuple(int(BG.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    px = im.load()
    last = 0
    for y in range(H - 1, -1, -2):
        if not all(px[x, y] == bg for x in range(0, W, 16)):
            last = y
            break
    final_h = max(last + 1, CANVAS_H)  # 不足 3:4 补底，超出就任其多高
    im.crop((0, 0, CANVAS_W, final_h)).save(out)
    raw.unlink(missing_ok=True)
    print(f"✅ {out.name}  {CANVAS_W}x{final_h}")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/export_xhs.py <date>")
    date = sys.argv[1]
    folder = ROOT / "reports" / date
    d = load_daily(folder / "daily.json")
    outdir = folder / "dist" / "小红书"
    outdir.mkdir(parents=True, exist_ok=True)

    # 组页：封面 + 每分区一整页
    pages = []
    for key, emoji, name, color in SECTIONS:
        items = d.get(key, [])
        if items:
            pages.append(head_html(emoji, name, color) + "".join(item_html(it) for it in items))
    odds = d.get("odds", [])
    if odds:
        pages.append(head_html(*ODDS_HEAD[1:]) + "".join(odds_html(o) for o in odds))

    total = len(pages) + 1
    date_label = d.get("date_label", "")
    render_png(cover_html(d), outdir, "xhs-01")
    for i, inner in enumerate(pages):
        render_png(wrap_page(inner, date_label, i + 2, total), outdir, f"xhs-{i+2:02d}")
    print(f"共 {total} 张 → {outdir}")


if __name__ == "__main__":
    main()
