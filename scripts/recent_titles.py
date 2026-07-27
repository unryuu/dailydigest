# -*- coding: utf-8 -*-
"""
recent_titles.py <date> [N=3] — 打印目标日期之前最近 N 期的已发条目清单。

用途：防内容重复的语料（同一事件换个链接、换个说法也别再收）。
  步骤 1：把输出附进 scout 的派活 prompt；
  步骤 2：定牌时主 agent 自己对照（昨天那期还要读 daily.json 全文，正文里
  一句话带过的点也算报过——标题清单只能兜住标题级重复）。
数据直接来自 reports/<d>/daily.json，零维护。
"""
import sys, re, os, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = [("industry", "行业"), ("angle", "视角"), ("deep", "长文"), ("papers", "论文"),
            ("regulation", "监管"), ("official", "公告"), ("brief", "简讯"), ("fun", "乐子"),
            ("gold", "金·旧版"), ("silver", "银·旧版"), ("radar", "雷达·旧版")]
TIER = {"gold": "🥇", "silver": "🥈"}


def load(path):
    text = path.read_text(encoding="utf-8-sig")
    return json.loads(re.sub(r",(\s*[}\]])", r"\1", text))


def main():
    if len(sys.argv) < 2 or not re.match(r"^\d{4}-\d{2}-\d{2}$", sys.argv[1]):
        raise SystemExit("用法：python scripts/recent_titles.py <date> [N=3]")
    target = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    dates = sorted(d for d in os.listdir(ROOT / "reports")
                   if re.match(r"^\d{4}-\d{2}-\d{2}$", d) and d < target
                   and (ROOT / "reports" / d / "daily.json").exists())[-n:]
    if not dates:
        raise SystemExit(f"{target} 之前没有可读的 daily.json")
    for d in reversed(dates):
        data = load(ROOT / "reports" / d / "daily.json")
        print(f"\n=== {d} 已发 ===")
        for key, name in SECTIONS:
            for it in data.get(key) or []:
                mark = TIER.get(it.get("tier", key), "·")
                title = it.get("title") or it.get("label") or ""
                print(f"{mark} [{name}] {title}\n    {it.get('url','')}")
        for o in data.get("odds") or []:
            print(f"🎲 [赔率] {o.get('question','')}（{o.get('prob','')}）\n    {o.get('url','')}")


if __name__ == "__main__":
    main()
