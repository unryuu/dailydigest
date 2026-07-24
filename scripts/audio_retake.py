# -*- coding: utf-8 -*-
"""
audio_retake.py <音频> <转写srt> <输出音频> [--apply] — 剪掉录音里的重念废弃段。

录音约定:念错一句就拍一下手,停一秒,从这句开头重新念。
原理:废弃段和重念段的开头文字高度相似(拍手常被转写成「打打」之类短杂音)。
在转写 srt 里找 25 秒窗口内文字相似度 ≥0.55 的字幕对,把「废弃段开头 → 重念段开头」
划为拟剪区间。默认只打印剪单;确认无误后加 --apply 真剪(atrim 分段重拼)。

剪完的音频才是时间轴主人:本步骤必须在正式转写对齐之前完成,
之后用剪好的音频重新走 转写 → 对齐 → 烧录。
"""
import sys, re, subprocess, pathlib
from difflib import SequenceMatcher

WINDOW = 25.0      # 只在这个秒数窗口内找重念对
MIN_RATIO = 0.55   # 开头文字相似度阈值
CMP_LEN = 10       # 取每条字幕净字的前几个字比对
SIL_SEEK = 8.0     # 剪辑终点向后找静音段的窗口（拍手+停顿常被并进重念字幕头部）
SIL_PAD = 0.25     # 静音结尾往前留的呼吸量


def t2s(ts):
    h, m, rest = ts.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def parse_srt(path):
    text = pathlib.Path(path).read_text(encoding="utf-8-sig")
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
    return re.sub(r"[\s，。！？；：、「」…▲※\-—·,.!?;:]", "", s)


def find_cuts(cues):
    cuts = []  # (start, end, 废弃文字, 重念文字)
    for j in range(len(cues)):
        key_j = squash(cues[j][2])[:CMP_LEN]
        if len(key_j) < 4:
            continue
        for i in range(j - 1, -1, -1):
            if cues[j][0] - cues[i][0] > WINDOW:
                break
            key_i = squash(cues[i][2])[:CMP_LEN]
            if len(key_i) < 4:
                continue
            if SequenceMatcher(None, key_i, key_j).ratio() >= MIN_RATIO:
                cuts.append((cues[i][0], cues[j][0], cues[i][2], cues[j][2]))
                break
    # 合并重叠区间(连错两次重念两次的情况)
    cuts.sort()
    merged = []
    for c in cuts:
        if merged and c[0] < merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], c[1]), merged[-1][2], c[3])
        else:
            merged.append(list(c))
    return merged


def detect_silences(src):
    r = subprocess.run(["ffmpeg", "-i", str(src), "-af", "silencedetect=noise=-30dB:d=0.5",
                        "-f", "null", "-"], capture_output=True, text=True)
    starts = [float(m) for m in re.findall(r"silence_start:\s*([\d.]+)", r.stderr)]
    ends = [float(m) for m in re.findall(r"silence_end:\s*([\d.]+)", r.stderr)]
    return list(zip(starts, ends))


def extend_into_silence(cuts, silences):
    """拍手和停顿常被 VAD 划进重念字幕的头部：把剪辑终点推到拍手后静音段的结尾。
    从原终点起「走静音」：相邻静音段之间的有声间隔 ≤1 秒视为杂音（拍手），继续走；
    遇到 >1 秒的连续有声（真正开口说话）就停，防止链式吞掉正文。"""
    out = []
    for a, b, bad, good in cuts:
        pos, chosen = b, None
        for s0, s1 in sorted(silences):
            if s1 <= b or s0 > b + SIL_SEEK:
                continue
            if s0 - pos <= 1.0:
                chosen, pos = s1, s1
            else:
                break
        if chosen:
            b = max(b, chosen - SIL_PAD)
        out.append((a, b, bad, good))
    return out


def apply_cuts(src, dst, cuts, total):
    keep, pos = [], 0.0
    for a, b, *_ in cuts:
        if a > pos:
            keep.append((pos, a))
        pos = b
    keep.append((pos, total))
    parts, labels = [], []
    for k, (a, b) in enumerate(keep):
        parts.append(f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[s{k}]")
        labels.append(f"[s{k}]")
    fc = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(keep)}:v=0:a=1[out]"
    cmd = ["ffmpeg", "-y", "-v", "warning", "-i", str(src), "-filter_complex", fc,
           "-map", "[out]", "-c:a", "aac", "-b:a", "160k", str(dst)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"ffmpeg 剪辑失败：\n{r.stderr[:800]}")


def fmt(t):
    return f"{int(t//60):02d}:{t%60:04.1f}"


def main():
    if len(sys.argv) not in (4, 5):
        raise SystemExit("用法：python scripts/audio_retake.py <音频> <srt> <输出> [--apply]")
    src, srt, dst = sys.argv[1:4]
    do_apply = "--apply" in sys.argv
    cues = parse_srt(srt)
    total = cues[-1][1] + 2.0
    cuts = extend_into_silence(find_cuts(cues), detect_silences(src))
    if not cuts:
        print("没找到重念段，无需剪辑")
        return
    print("拟剪区间：")
    removed = 0
    for a, b, bad, good in cuts:
        print(f"  {fmt(a)} ~ {fmt(b)}  剪「{bad}」→ 保留重念「{good}」")
        removed += b - a
    print(f"共 {len(cuts)} 段、{removed:.1f} 秒")
    if do_apply:
        apply_cuts(src, dst, cuts, total)
        print(f"✅ 已剪 → {dst}")
    else:
        print("（预览模式，确认后加 --apply 真剪）")


if __name__ == "__main__":
    main()
