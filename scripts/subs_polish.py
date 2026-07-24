# -*- coding: utf-8 -*-
"""
subs_polish.py <in.srt> <out.srt> [gap_ms=80] — 烧录前的字幕抛光（不改源文件）。

1. 行尾的句号「。」和分号「；」删掉（行中不动）。
2. 相邻字幕留最小间隙：两条挨得太近时**把前一条的结束时间提前**到
   下一条开始前 gap_ms，切换不突兀。参照 Netflix Timed Text 规范的
   最小 2 帧间隙（24fps 约 83ms），默认 80ms，可调。
   下一条的开始时间永远不动（它咬着开口时刻）。

用在用户手工修完的 字幕.script.srt 之后、烧录之前；源文件保持原样。
"""
import sys, re, pathlib

MIN_KEEP = 0.3  # 前一条被收缩后至少保留的时长（秒）


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
    gap = (int(sys.argv[3]) if len(sys.argv) > 3 else 80) / 1000

    cues = []
    for block in re.split(r"\n\s*\n", src.read_text(encoding="utf-8-sig").strip()):
        m = re.search(r"(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})", block)
        if not m:
            continue
        lines = [l for l in block.splitlines() if l.strip()]
        text = "\n".join(lines[2:]).rstrip()
        text = re.sub(r"[。；]+$", "", text)
        cues.append({"a": t2s(m.group(1).replace(".", ",")), "b": t2s(m.group(2).replace(".", ",")), "text": text})

    tightened = 0
    for k in range(len(cues) - 1):
        want_end = cues[k + 1]["a"] - gap
        if cues[k]["b"] > want_end:
            cues[k]["b"] = max(want_end, cues[k]["a"] + MIN_KEEP)
            tightened += 1

    out = [f"{i}\n{s2t(c['a'])} --> {s2t(c['b'])}\n{c['text']}\n" for i, c in enumerate(cues)]
    dst.write_text("\n".join(out), encoding="utf-8")
    print(f"✅ {dst}（{len(cues)} 条，收紧间隙 {tightened} 处，最小间隙 {int(gap*1000)}ms）")


if __name__ == "__main__":
    main()
