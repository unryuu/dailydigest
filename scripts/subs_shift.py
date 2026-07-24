# -*- coding: utf-8 -*-
"""
subs_shift.py <in.srt> <out.srt> [delay_ms=50] — 把字幕切换点整体延后。

人类习惯「下一句开口时才换字幕」，whisper 的段首尾相接、切换偏早。
处理：除第一条外，每条 start 加 delay；前一条原本与它相接的，end 跟着顺延，保持无缝。
"""
import sys, re, pathlib

def t2s(ts):
    h, m, rest = ts.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

def s2t(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600); m = int(sec % 3600 // 60); s = int(sec % 60)
    ms = int(round((sec - int(sec)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def main():
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    delay = (int(sys.argv[3]) if len(sys.argv) > 3 else 50) / 1000

    text = src.read_text(encoding="utf-8-sig")
    cues = []
    for block in re.split(r"\n\s*\n", text.strip()):
        m = re.search(r"(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})", block)
        if not m:
            continue
        lines = [l for l in block.splitlines() if l.strip()]
        cues.append({"a": t2s(m.group(1).replace(".", ",")), "b": t2s(m.group(2).replace(".", ",")),
                     "text": "\n".join(lines[2:])})

    for k in range(1, len(cues)):
        contiguous = abs(cues[k]["a"] - cues[k - 1]["b"]) < 0.001
        cues[k]["a"] += delay
        if contiguous:
            cues[k - 1]["b"] = cues[k]["a"]
        cues[k]["b"] = max(cues[k]["b"], cues[k]["a"] + 0.3)

    out = [f"{i}\n{s2t(c['a'])} --> {s2t(c['b'])}\n{c['text']}\n" for i, c in enumerate(cues)]
    dst.write_text("\n".join(out), encoding="utf-8")
    print(f"✅ {dst}（{len(cues)} 条，切换延后 {int(delay*1000)}ms）")

if __name__ == "__main__":
    main()
