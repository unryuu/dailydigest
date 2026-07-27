# -*- coding: utf-8 -*-
"""
daily.json -> markdown 导出（多平台分发线第一块：知乎）。

用法：
    python scripts/export_md.py <date>              # 出 reports/<date>/dist/daily.zhihu.md
    python scripts/export_md.py <date> --flavor zhihu

知乎文章编辑器支持粘贴 markdown 自动解析；文章标题不在正文里，
发布时手动填「AI 日报 · <date_label>」。
以后加别的平台就加新 flavor 函数（公众号要脚注化外链、小红书要去链接，别混在一起）。
"""
import sys, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
from dailyjson import load_daily

SECTIONS = [  # 与 render_daily.py 同序
    ("industry",   "🗞️", "行业大事"),
    ("angle",      "🔍", "独家视角"),
    ("deep",       "📖", "深度长文"),
    ("papers",     "🧪", "新鲜论文"),
    ("regulation", "🏛️", "监管动向"),
    ("official",   "📢", "官方公告"),
    ("brief",      "📌", "行业简讯"),
    ("fun",        "🎪", "乐子汇总"),
]
TIER_MARK = {"gold": "🥇 ", "silver": "🥈 "}


def zhihu_md(d):
    L = []
    for key, emoji, name in SECTIONS:
        items = d.get(key, [])
        if not items:
            continue
        L.append(f"## {emoji} {name}")
        L.append("")
        if key == "brief":  # 行业简讯：只有标题的清单
            for it in items:
                L.append(f"- [{it.get('title') or ''}]({it['url']})")
            L.append("")
            continue
        for it in items:
            mark = TIER_MARK.get(it.get("tier", ""), "")
            title = it.get("title") or it.get("label") or ""
            L.append(f"**{mark}[{title}]({it['url']})**")
            L.append("")
            body = it.get("body", "")
            for p in body.split("\n\n"):
                if p.strip():
                    L.append(p.strip())
                    L.append("")
            src = it.get("sources") or []
            if src:
                L.append("另见：" + " · ".join(f"[{s.get('name','')}]({s['url']})" for s in src))
                L.append("")
    odds = d.get("odds", [])
    if odds:
        L.append("## 🎲 赔率盒子")
        L.append("")
        L.append("来自预测市场 Manifold 的实时概率，仅供围观：")
        L.append("")
        for o in odds:
            note = f"（{o['note']}）" if o.get("note") else ""
            if o.get("options"):
                L.append(f"- [{o['question']}]({o['url']}){note}")
                for op in o["options"]:
                    L.append(f"  - {op.get('name','')} **{op.get('prob','')}**")
            else:
                L.append(f"- [{o['question']}]({o['url']}) — **{o.get('prob','')}**{note}")
        L.append("")
    L.append("---")
    L.append("")
    L.append(f"*AI 日报 · {d.get('date_label','')} · Telegram 频道 @dragonbro888*")
    return "\n".join(L) + "\n"


FLAVORS = {"zhihu": zhihu_md}

def main():
    argv = sys.argv[1:]
    flavor = "zhihu"
    if "--flavor" in argv:
        i = argv.index("--flavor"); flavor = argv[i + 1]; del argv[i:i + 2]
    if not argv:
        raise SystemExit("用法：python scripts/export_md.py <date> [--flavor zhihu]")
    date = argv[0]
    if flavor not in FLAVORS:
        raise SystemExit(f"未知 flavor：{flavor}（现有：{'/'.join(FLAVORS)}）")
    ddir = ROOT / "reports" / date
    d = load_daily(ddir / "daily.json")
    out = ddir / "dist" / f"daily.{flavor}.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(FLAVORS[flavor](d), encoding="utf-8")
    print(f"✅ {out}  ({out.stat().st_size} 字节)")

if __name__ == "__main__":
    main()
