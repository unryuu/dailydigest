# -*- coding: utf-8 -*-
"""
subs_align.py <date> — 把口播稿文本对齐到 whisper 转写的时间轴，生成「稿件字幕」。

输入：reports/<date>/口播稿.md（定稿文本）+ reports/<date>/video/字幕.audio.srt（whisper 直出）
输出：reports/<date>/video/字幕.script.srt（时间轴来自音频、文字来自稿件）

原理（v2，字符级全局对齐）：
1. whisper 各段内按字符线性插值，得到「转写文本每个字 → 时间」；
2. 转写全文 vs 稿件全文做 SequenceMatcher，equal 块直接继承时间、replace 块线性插值，
   得到「稿件每个字 → 时间」；
3. 稿件按标点切成字幕单元，取首末字时间做该条字幕的起止；
4. 主播临场加的话（转写里有、稿件里没有的长块）补一条 whisper 原文字幕，行尾标 ※。
"""
import sys, re, pathlib
from difflib import SequenceMatcher

ROOT = pathlib.Path(__file__).resolve().parents[1]
MAX_CHUNK = 22      # 字幕单元目标长度（字）
ADLIB_MIN = 6       # 转写独有块 ≥ 此长度（净字）才补 ※ 字幕
MIN_DUR = 0.6       # 单条字幕最短时长（秒）

PUNCS = "，。！？；：、「」『』（）《》…—·,.!?;:()\"' \t\n％%"
STRIP = re.compile("[" + re.escape(PUNCS) + "]")


def t2s(ts):
    h, m, rest = ts.split(":")
    s, ms = rest.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def s2t(sec):
    sec = max(0.0, sec)
    h = int(sec // 3600); m = int(sec % 3600 // 60); s = int(sec % 60)
    ms = int(round((sec - int(sec)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def parse_srt(path):
    text = path.read_text(encoding="utf-8-sig")
    segs = []
    for block in re.split(r"\n\s*\n", text.strip()):
        m = re.search(r"(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})", block)
        if not m:
            continue
        lines = [l for l in block.splitlines() if l.strip()]
        txt = "".join(lines[2:]) if len(lines) > 2 else ""
        segs.append((t2s(m.group(1).replace(".", ",")), t2s(m.group(2).replace(".", ",")), txt.strip()))
    return segs


def norm_with_map(text):
    """去标点后的文本 + 每个净字在原文里的下标。"""
    chars, idx = [], []
    for i, ch in enumerate(text):
        if not STRIP.search(ch):
            chars.append(ch)
            idx.append(i)
    return "".join(chars), idx


def build_whisper_charline(segs):
    """返回 (净字文本, 每个净字的时间)。段内按净字数线性插值。"""
    chars, times = [], []
    for start, end, txt in segs:
        n, _ = norm_with_map(txt)
        if not n:
            continue
        dur = max(end - start, 0.01)
        for k, ch in enumerate(n):
            chars.append(ch)
            times.append(start + dur * k / max(len(n) - 1, 1))
    return "".join(chars), times


def split_units(text):
    """稿件按标点切成字幕单元，带原文（含标点）。返回 [(unit_text, 原文起下标, 原文止下标)]。"""
    units = []
    start = 0
    for m in re.finditer(r"[。！？；…]|[，、：]", text):
        end = m.end()
        if end - start >= 2:
            seg = text[start:end]
            if len(seg) > MAX_CHUNK * 1.6 or m.group(0) in "。！？；…" or end - start >= MAX_CHUNK:
                units.append((seg, start, end))
                start = end
    if start < len(text):
        units.append((text[start:], start, len(text)))
    # 合并过短单元
    merged = []
    for u in units:
        if merged and len(merged[-1][0]) + len(u[0]) <= MAX_CHUNK:
            p = merged.pop()
            merged.append((p[0] + u[0], p[1], u[2]))
        else:
            merged.append(u)
    return merged


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/subs_align.py <date>")
    date = sys.argv[1]
    folder = ROOT / "reports" / date

    raw_lines = (folder / "口播稿.md").read_text(encoding="utf-8-sig").splitlines()
    script = "".join(l.strip() for l in raw_lines if l.strip() and not l.strip().startswith("（预计"))

    segs = parse_srt(folder / "video" / "字幕.audio.srt")
    w_text, w_time = build_whisper_charline(segs)
    s_norm, s_idx = norm_with_map(script)

    # 稿件每个净字的时间
    s_time = [None] * len(s_norm)
    sm = SequenceMatcher(None, w_text, s_norm, autojunk=False)
    adlib_blocks = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(j2 - j1):
                s_time[j1 + k] = w_time[i1 + k]
        elif tag == "replace":
            span = i2 - i1
            for k in range(j2 - j1):
                s_time[j1 + k] = w_time[i1 + min(span - 1, int(span * k / max(j2 - j1, 1)))]
        elif tag == "delete" and (i2 - i1) >= ADLIB_MIN:
            adlib_blocks.append((w_time[i1], w_time[i2 - 1], w_text[i1:i2]))
        # insert（稿件里有、没念出来）：留 None，后面补插值

    # 填补 None（没念/被换词的稿件字）：邻近插值
    last = 0.0
    for k in range(len(s_time)):
        if s_time[k] is None:
            nxt = next((s_time[m] for m in range(k + 1, len(s_time)) if s_time[m] is not None), None)
            s_time[k] = last if nxt is None else min(nxt, last + 0.2)
        last = s_time[k]

    # 原文下标 → 净字序号
    pos_of = {orig: n for n, orig in enumerate(s_idx)}

    units = split_units(script)
    subs = []
    for text, a, b in units:
        ns = [pos_of[i] for i in range(a, b) if i in pos_of]
        if not ns:
            continue
        st, en = s_time[ns[0]], s_time[ns[-1]]
        t = text.strip("，、：").rstrip("。；")  # 行尾句号、分号删掉
        if "。" in t:
            t += " ▲"                            # 行中句号：标记待手动切分（行中分号正常，不标）
        subs.append([st, max(en, st + MIN_DUR), t])

    # 插入临场加话
    for st, en, txt in adlib_blocks:
        subs.append([st, max(en, st + MIN_DUR), txt + " ※"])
    subs.sort(key=lambda x: x[0])
    # 收尾：去重叠
    for k in range(1, len(subs)):
        if subs[k][0] < subs[k - 1][1]:
            subs[k - 1][1] = max(subs[k][0], subs[k - 1][0] + MIN_DUR)

    out = folder / "video" / "字幕.script.srt"
    blocks = [f"{i}\n{s2t(a)} --> {s2t(b)}\n{t}\n" for i, (a, b, t) in enumerate(subs)]
    out.write_text("\n".join(blocks), encoding="utf-8")

    match = sum(1 for x in sm.get_matching_blocks() for _ in range(x.size))
    print(f"转写净字 {len(w_text)}，稿件净字 {len(s_norm)}，字符级匹配率 {match/max(len(s_norm),1):.0%}")
    print(f"字幕 {len(subs)} 条（其中临场加话 ※ {len(adlib_blocks)} 条）")
    print(f"✅ {out}")


if __name__ == "__main__":
    main()
