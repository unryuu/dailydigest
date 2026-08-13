# -*- coding: utf-8 -*-
"""
video_description.py <date> — 用小红书标题页看点生成视频简介。

输出：reports/<date>/video/视频简介.txt
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from dailyjson import load_daily
from export_xhs import cover_highlights


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/video_description.py <date>")

    date = sys.argv[1]
    folder = ROOT / "reports" / date
    daily = folder / "daily.json"
    if not daily.exists():
        raise SystemExit(f"缺少 {daily}")

    highlights = [title.strip() for _, title in cover_highlights(load_daily(daily)) if title.strip()]
    if not highlights:
        raise SystemExit("小红书标题页没有可用于视频简介的今日看点")

    text = "今日看点\n" + "\n".join(f"·{title}" for title in highlights)
    text += "\n原始新闻链接、图文版日报，可前往TG频道 @dragonbro888 获取\n"

    video = folder / "video"
    video.mkdir(exist_ok=True)
    output = video / "视频简介.txt"
    output.write_text(text, encoding="utf-8")
    print(f"✅ {output}（{len(highlights)} 条看点）")


if __name__ == "__main__":
    main()
