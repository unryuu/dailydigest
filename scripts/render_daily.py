"""
把日报内容（2026-07-21 起的分类版式）渲染成一张手机竖屏长图 PNG。

用法：
    python scripts/render_daily.py <date>            # 读 reports/<date>/daily.json
    python scripts/render_daily.py <date> --sample   # 用内置占位内容测试渲染管线

管线：daily.json -> work/ 下生成 html -> 无头 Chrome 截 1179px 宽长图 -> Pillow 裁底部空白 -> daily.full.png

版式（2026-07-21 改版；2026-07-27 加两区）：
- 九个分区：行业大事 / 独家视角 / 深度长文 / 新鲜论文 / 监管动向 / 官方公告 / 行业简讯 / 乐子汇总 / 赔率盒子
- 每个分区内部再分档：金牌（卡片+金标）、银牌（卡片+银标）、无牌（行式条目）
- 空分区自动跳过；条目字段 tier: "gold"|"silver"|缺省无牌
- angle（独家视角）：几条话题相近的内容并成一段来聊，正文 ≤350 字，不挂金银标，
  卡片带左侧红边；可选 sources 字段 [{name,url}] 渲成底部一行「另见」灰字
- brief（行业简讯）：连无牌都不够格的，只有 title、没有 body，渲成紧凑行式清单
- 旧五分区格式（gold/silver/radar/fun 键）不再支持，重渲旧期请用 git 历史版本

设计参数（iPhone 15 Pro：物理 2556x1179、3x、逻辑宽 393pt）：
- 画布宽 1179px；正文 54px；字体：小标题/UI 微软雅黑，正文 霞鹜文楷（fonts/，07-22 用户定）
- 配色：Claude Light 浅黄绿护眼底 + 墨色字，各分区一色标
"""
import sys, json, subprocess, pathlib
from dailyjson import load_daily
from chromepath import find_chrome

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = find_chrome()
LXGW = ROOT / "fonts" / "LXGWWenKai-Regular.ttf"

# ---------- 配色（Claude Light 浅黄绿护眼） ----------
BG      = "#EDEFE2"   # 页面浅黄绿底
CARD    = "#F7F8F0"   # 卡片更浅
INK     = "#2F2E27"   # 正文墨色
SUBINK  = "#6B6A5E"   # 次要灰
GOLD    = "#B8901F"   # 金牌标
SILVER  = "#7C8894"   # 银牌标
ODDS    = "#5E8C5A"
ANGLE   = "#C24A4A"   # 独家视角主色（卡片左边）
BRIEF   = "#8C8574"   # 行业简讯主色（清单圆点）

# key -> (emoji, 四字分区名, 主色)；按此顺序渲染
SECTIONS = [
    ("industry",   "🗞️", "行业大事", "#A8562F"),
    ("angle",      "🔍", "独家视角", ANGLE),
    ("deep",       "📖", "深度长文", "#4E7CA1"),
    ("papers",     "🧪", "新鲜论文", "#3F8E7E"),
    ("regulation", "🏛️", "监管动向", "#8A6FA8"),
    ("official",   "📢", "官方公告", "#7C8894"),
    ("brief",      "📌", "行业简讯", BRIEF),
    ("fun",        "🎪", "乐子汇总", "#C2703C"),
]
ODDS_HEAD = ("🎲", "赔率盒子", ODDS)

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def build_html(d):
    date_label = esc(d.get("date_label", ""))
    parts = []
    parts.append(f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family:"LXGW WenKai"; src:url("{LXGW.as_uri()}"); }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ background:{BG}; }}
.page {{ width:1179px; background:{BG}; padding:56px 48px 64px 48px; }}
.hdr {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:74px; color:{INK}; letter-spacing:1px; }}
.hdr .dot {{ color:#C2703C; }}
.hdrsub {{ font-family:"LXGW WenKai",serif; font-size:38px; color:{SUBINK}; margin-top:10px; }}
.rule {{ height:4px; background:{INK}; opacity:.12; margin:34px 0 8px; }}
.sec {{ display:flex; align-items:center; gap:16px; margin:44px 0 14px; }}
.sec .bar {{ width:12px; height:52px; border-radius:6px; }}
.sec .label {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:48px; }}
.item {{ background:{CARD}; border-radius:22px; padding:32px 38px; margin:18px 0; box-shadow:0 2px 0 rgba(0,0,0,.04); }}
.item .ttl {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:56px; line-height:1.30; color:{INK}; }}
.tag {{ display:inline-block; vertical-align:6px; font-family:"Microsoft YaHei",sans-serif; font-weight:bold;
       font-size:36px; line-height:1; color:#fff; padding:10px 20px 12px; border-radius:12px; margin-right:16px; }}
.item .body {{ font-family:"LXGW WenKai",serif; font-size:54px; line-height:1.56; color:{INK}; margin-top:18px; }}
.item .body p {{ margin-top:16px; }}
.item.angle {{ border-left:12px solid {ANGLE}; }}
.item .src {{ font-family:"LXGW WenKai",serif; font-size:38px; line-height:1.5; color:{SUBINK}; margin-top:22px; }}
.brief {{ background:{CARD}; border-radius:22px; padding:14px 38px; margin:18px 0; box-shadow:0 2px 0 rgba(0,0,0,.04); }}
.brief .row {{ font-family:"LXGW WenKai",serif; font-size:50px; line-height:1.48; color:{INK};
              padding:22px 0; border-bottom:2px solid rgba(0,0,0,.06); }}
.brief .row:last-child {{ border-bottom:none; }}
.brief .row .dot {{ color:{BRIEF}; font-weight:bold; margin-right:16px; }}
.odd {{ display:flex; align-items:center; gap:24px; padding:18px 6px; border-bottom:2px solid rgba(0,0,0,.06); }}
.odd .q {{ flex:1; font-family:"LXGW WenKai",serif; font-size:46px; line-height:1.42; color:{INK}; }}
.odd .qn {{ font-family:"LXGW WenKai",serif; font-size:38px; color:{SUBINK}; margin-top:6px; }}
.odd .p {{ font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:62px; color:{ODDS}; min-width:190px; text-align:right; }}
.oddm {{ padding:18px 6px; border-bottom:2px solid rgba(0,0,0,.06); }}
.oddm .q {{ font-family:"LXGW WenKai",serif; font-size:46px; line-height:1.42; color:{INK}; }}
.oddm .qn {{ font-family:"LXGW WenKai",serif; font-size:38px; color:{SUBINK}; margin-top:6px; }}
.oddm .opts {{ margin-top:16px; }}
.oddm .opt {{ position:relative; display:flex; align-items:center; justify-content:space-between; padding:12px 22px; margin:9px 0; border-radius:12px; background:rgba(0,0,0,.035); overflow:hidden; }}
.oddm .fill {{ position:absolute; left:0; top:0; bottom:0; background:{ODDS}; opacity:.16; }}
.oddm .on {{ position:relative; z-index:1; font-family:"LXGW WenKai",serif; font-size:44px; color:{INK}; }}
.oddm .op {{ position:relative; z-index:1; font-family:"Microsoft YaHei",sans-serif; font-weight:bold; font-size:44px; color:{ODDS}; }}
.foot {{ margin-top:52px; font-family:"Microsoft YaHei",sans-serif; font-size:40px; color:{SUBINK}; text-align:center; }}
</style></head><body><div class="page">""")

    parts.append(f'<div class="hdr">📰 AI 日报 <span class="dot">·</span> {date_label}</div>')
    parts.append('<div class="hdrsub">给 @dragonbro888 的朋友们</div>')
    parts.append('<div class="rule"></div>')

    def section_head(emoji, name, color):
        return (f'<div class="sec"><div class="bar" style="background:{color}"></div>'
                f'<div class="label" style="color:{color}">{emoji} {name}</div></div>')

    def title_of(it):
        return it.get("title") or it.get("label") or ""

    for key, emoji, name, color in SECTIONS:
        items = d.get(key, [])
        if not items:
            continue
        parts.append(section_head(emoji, name, color))
        if key == "brief":  # 行业简讯：一张卡里的紧凑清单，只有标题
            rows = "".join(f'<div class="row"><span class="dot">·</span>{esc(title_of(it))}</div>'
                           for it in items)
            parts.append(f'<div class="brief">{rows}</div>')
            continue
        for it in items:
            tier = it.get("tier", "none")
            tag = ""
            if tier == "gold":
                tag = f'<span class="tag" style="background:{GOLD}">金</span>'
            elif tier == "silver":
                tag = f'<span class="tag" style="background:{SILVER}">银</span>'
            body_html = "".join(f"<p>{esc(p)}</p>" for p in it.get("body", "").split("\n\n") if p.strip())
            body_div = f'<div class="body">{body_html}</div>' if body_html else ""
            src = it.get("sources") or []
            src_div = (f'<div class="src">另见：{esc(" · ".join(s.get("name", "") for s in src))}</div>'
                       if src else "")
            cls = "item angle" if key == "angle" else "item"
            parts.append(f'<div class="{cls}"><div class="ttl">{tag}{esc(title_of(it))}</div>'
                         f'{body_div}{src_div}</div>')

    odds = d.get("odds", [])
    if odds:
        parts.append(section_head(*ODDS_HEAD))
        for o in odds:
            qn = f'<div class="qn">{esc(o["note"])}</div>' if o.get("note") else ""
            opts = o.get("options")
            if opts:
                rows = "".join(
                    f'<div class="opt"><div class="fill" style="width:{esc(op.get("prob",""))}"></div>'
                    f'<span class="on">{esc(op.get("name",""))}</span>'
                    f'<span class="op">{esc(op.get("prob",""))}</span></div>'
                    for op in opts)
                parts.append(f'<div class="oddm"><div class="q">{esc(o.get("question",""))}{qn}</div>'
                             f'<div class="opts">{rows}</div></div>')
            else:
                parts.append(f'<div class="odd"><div class="q">{esc(o.get("question",""))}{qn}</div>'
                             f'<div class="p">{esc(o.get("prob",""))}</div></div>')

    parts.append(f'<div class="foot">@dragonbro888 · AI 日报 · {date_label}</div>')
    parts.append('</div></body></html>')
    return "".join(parts)

def _render_one(html, outdir, tag):
    """渲染一段 HTML 成 PNG，裁掉底部纯背景。tag 用于文件名（如 'full'）。"""
    workdir = outdir / "work"
    workdir.mkdir(parents=True, exist_ok=True)
    html_path = workdir / f"daily.{tag}.html"
    png_raw = workdir / f"daily.{tag}.raw.png"
    png_out = outdir / f"daily.{tag}.png"
    html_path.write_text(html, encoding="utf-8")
    bg_hex = BG.lstrip("#") + "ff"
    cmd = [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", f"--default-background-color={bg_hex}",
           f"--screenshot={png_raw}", "--window-size=1179,20000",
           html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not png_raw.exists():
        raise SystemExit(f"Chrome 渲染失败：\n{r.stderr[:800]}")
    from PIL import Image
    im = Image.open(png_raw).convert("RGB")
    W, H = im.size
    bg = tuple(int(BG.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    px = im.load()
    last = 0
    for y in range(H - 1, -1, -4):
        if not all(px[x, y] == bg for x in range(0, W, 16)):
            last = y; break
    crop_h = min(H, last + 56)
    im.crop((0, 0, W, crop_h)).save(png_out)
    png_raw.unlink(missing_ok=True)
    print(f"✅ {png_out.name}  ({W}x{crop_h})")
    return png_out, crop_h

def render(date, sample=False):
    outdir = ROOT / "reports" / date
    outdir.mkdir(parents=True, exist_ok=True)
    d = SAMPLE if sample else load_daily(outdir / "daily.json")
    p, _ = _render_one(build_html(d), outdir, "full")
    return [p]

SAMPLE = {
    "date_label": "7月21日（样张）",
    "industry": [
        {"tier": "gold", "title": "占位金牌标题：行业大事里的今日头条", "url": "https://example.com",
         "body": "这是金牌正文的第一段占位文字，用来检查金标徽章和标题同行的观感，以及每行大约十九个汉字是否成立。\n\n这是第二段，金牌最多两段。看看段间距、卡片留白、圆角在浅黄绿底上的观感。"},
        {"title": "占位无牌条目：一句话带过的行业消息", "url": "https://example.com"},
    ],
    "deep": [
        {"tier": "silver", "title": "占位银牌：深度长文区的一段摘要", "url": "https://example.com",
         "body": "银牌一段，四到六句。检查银标徽章的颜色层级和金牌是否区分明显。"},
        {"title": "占位无牌长文条目，带一句解读看看排版", "url": "https://example.com",
         "body": "这是无牌条目的可选解读，两句以内，灰色小字。"},
    ],
    "angle": [
        {"title": "占位独家视角：三条相近的消息放一起聊", "url": "https://example.com",
         "body": "独家视角不是每期都有，几条话题靠近的内容并成一段，字数放宽到 350 字。第一段先把共同的那件事说出来。\n\n第二段展开区别在哪，谁的态度是什么。检查左侧红边、底部「另见」灰字和金银卡片摆在一起的层级关系。",
         "sources": [{"name": "第二个来源", "url": "https://example.com/b"},
                     {"name": "第三个来源", "url": "https://example.com/c"}]},
    ],
    "papers": [{"title": "占位论文条目：某方法把某指标从 X 提到 Y", "url": "https://example.com"}],
    "brief": [
        {"title": "占位简讯：某公司发了个新模型，主打便宜", "url": "https://example.com/1"},
        {"title": "占位简讯：某机场上线机器人代客泊车", "url": "https://example.com/2"},
        {"title": "占位简讯：某巨头披露持有某公司百亿美元股票", "url": "https://example.com/3"},
    ],
    "regulation": [{"tier": "silver", "title": "占位监管银牌：某机构负责人辞职", "url": "https://example.com",
                    "body": "一段以内的监管动向摘要占位。"}],
    "official": [{"title": "占位公告：某公司开放某项申请", "url": "https://example.com"}],
    "fun": [{"title": "占位乐子：巨树怎么把水泵到树顶", "url": "https://example.com"}],
    "odds": [{"question": "占位问题？", "prob": "80.9%", "note": "成交额约 21 万 mana", "url": "https://manifold.markets"}],
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("用法：python scripts/render_daily.py <date> [--sample]")
    render(sys.argv[1], sample=("--sample" in sys.argv))
