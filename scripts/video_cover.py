# -*- coding: utf-8 -*-
"""
video_cover.py <date> <日期标题> <看点一行> — 渲视频横屏封面 1920x1080。

例：python scripts/video_cover.py 2026-07-22 "7 月 22 日" "OpenAI 自认 HF 入侵 · Turner 辞职内幕 · 15 亿和解获批"
（日期标题只写日期，不带「口播版」——07-22 用户定）
输出：reports/<date>/video/视频卡.横屏.png
"""
import sys, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
W, H = 1920, 1080
BG, INK, SUB, ACCENT = "#EDEFE2", "#2F2E27", "#6B6A5E", "#C2703C"
YAHEI_B = r"C:\Windows\Fonts\msyhbd.ttc"
YAHEI = r"C:\Windows\Fonts\msyh.ttc"


def center(d, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


def main():
    if len(sys.argv) != 4:
        raise SystemExit('用法：python scripts/video_cover.py <date> "<日期标题>" "<看点一行>"')
    date, date_label, sub = sys.argv[1:4]
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 26], fill=ACCENT)
    center(d, 170, "龙兄的 Daily Digest", ImageFont.truetype(YAHEI_B, 58), ACCENT)
    center(d, 300, "AI 日报", ImageFont.truetype(YAHEI_B, 150), INK)
    center(d, 520, date_label, ImageFont.truetype(YAHEI_B, 76), ACCENT)
    center(d, 660, sub, ImageFont.truetype(YAHEI, 48), SUB)
    center(d, 960, "Telegram 频道 @dragonbro888", ImageFont.truetype(YAHEI, 42), SUB)
    out = ROOT / "reports" / date / "video" / "视频卡.横屏.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out)
    print(f"✅ {out}  ({W}x{H})")


if __name__ == "__main__":
    main()
