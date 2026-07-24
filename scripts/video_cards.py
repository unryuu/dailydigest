# -*- coding: utf-8 -*-
"""
video_cards.py <date> — 渲「讲 PPT」式视频卡 + 按字幕时间轴排卡。

输入：reports/<date>/video/视频卡.json（anchor 是该主题在稿件字幕里的起始句子片段）
      reports/<date>/video/字幕.script.srt（对齐后的稿件字幕，取时间轴）
输出：reports/<date>/video/视频卡/card-XX.png + video/cards.ffconcat（concat 时间表）

之后拼片：
ffmpeg -f concat -safe 0 -i cards.ffconcat -i <audio> \
       -vf "fps=25,subtitles=<srt>:force_style='...'" -c:v libx264 ... 输出.mp4
"""
import sys, json, re, pathlib
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
W, H = 1920, 1080
BG, INK, SUB = "#EDEFE2", "#2F2E27", "#6B6A5E"
YAHEI_B = r"C:\Windows\Fonts\msyhbd.ttc"
YAHEI = r"C:\Windows\Fonts\msyh.ttc"
LXGW = str(ROOT / "fonts" / "LXGWWenKai-Regular.ttf")  # 正文用文楷（07-22 用户定）
TAIL_PAD = 1.0  # 最后一张卡在音频结束后多停留秒数


def t2s(ts):
    h, m, rest = ts.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path):
    text = path.read_text(encoding="utf-8-sig")
    cues = []
    for block in re.split(r"\n\s*\n", text.strip()):
        m = re.search(r"(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})", block)
        if not m:
            continue
        lines = [l for l in block.splitlines() if l.strip()]
        cues.append((t2s(m.group(1).replace(".", ",")), t2s(m.group(2).replace(".", ",")),
                     "".join(lines[2:])))
    return cues


def squash(s):
    return re.sub(r"[\s，。！？；：、「」…▲※]", "", s)


def wrap(draw, text, font, max_w):
    lines, buf = [], ""
    for ch in text:
        if draw.textlength(buf + ch, font=font) > max_w:
            lines.append(buf)
            buf = ch
        else:
            buf += ch
    if buf:
        lines.append(buf)
    return lines


def render_card(card, date_label, out_path):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    color = card.get("color", "#C2703C")
    d.rectangle([0, 0, W, 14], fill=color)
    f_kick = ImageFont.truetype(YAHEI, 36)
    d.text((120, 80), f"龙兄的 Daily Digest · AI 日报 · {date_label}", font=f_kick, fill=SUB)
    f_title = ImageFont.truetype(YAHEI_B, 84)
    y = 190
    for line in wrap(d, card["title"], f_title, W - 240):
        d.text((120, y), line, font=f_title, fill=INK)
        y += 110
    d.rectangle([120, y + 18, 320, y + 26], fill=color)
    y += 90
    f_b = ImageFont.truetype(LXGW, 58)
    for b in card.get("bullets", []):
        d.ellipse([126, y + 30, 150, y + 54], fill=color)
        lines = wrap(d, b, f_b, W - 420)
        for k, line in enumerate(lines):
            d.text((190, y), line, font=f_b, fill=INK)
            y += 84
        y += 26
    im.save(out_path)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/video_cards.py <date>")
    date = sys.argv[1]
    folder = ROOT / "reports" / date / "video"
    spec = json.loads((folder / "视频卡.json").read_text(encoding="utf-8-sig"))
    cues = parse_srt(folder / "字幕.script.srt")
    audio_end = cues[-1][1] + TAIL_PAD

    outdir = folder / "视频卡"
    outdir.mkdir(exist_ok=True)

    # 定每张卡的开始时间
    cards = spec["cards"]
    starts = []
    for i, card in enumerate(cards):
        if not card.get("anchor"):
            starts.append(0.0)
            continue
        key = squash(card["anchor"])
        hit = next((a for a, b, t in cues if key in squash(t)), None)
        if hit is None:
            raise SystemExit(f"❌ 卡 {i}「{card['title']}」的 anchor 没在字幕里找到：{card['anchor']}")
        starts.append(hit)
    if starts != sorted(starts):
        raise SystemExit(f"❌ 卡片时间不单调：{[round(s,1) for s in starts]}")

    # 渲染 + ffconcat
    lines = ["ffconcat version 1.0"]
    report = []
    for i, card in enumerate(cards):
        if card.get("image"):
            png = folder / card["image"]
            rel = card["image"]
        else:
            png = outdir / f"card-{i:02d}.png"
            render_card(card, spec.get("date_label", date), png)
            rel = f"视频卡/card-{i:02d}.png"
        end = starts[i + 1] if i + 1 < len(cards) else audio_end
        dur = max(end - starts[i], 0.5)
        lines.append(f"file '{rel}'")
        lines.append(f"duration {dur:.3f}")
        report.append((starts[i], card["title"], round(dur, 1)))
    lines.append(f"file '{rel}'")  # concat 惯例：末图重复一次
    (folder / "cards.ffconcat").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for st, title, dur in report:
        mm, ss = int(st // 60), int(st % 60)
        print(f"  {mm:02d}:{ss:02d}  {title}（{dur}s）")
    print(f"✅ {len(cards)} 张卡 + cards.ffconcat（音频末端 {audio_end:.1f}s）")


if __name__ == "__main__":
    main()
