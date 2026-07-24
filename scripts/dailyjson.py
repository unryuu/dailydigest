# -*- coding: utf-8 -*-
"""daily.json 的容错读取 + 标点归一化。

用户会直接手工编辑 daily.json，手编必然留尾逗号（`... },\n]`），标准 json
解析直接报错——严格解析失败时去掉尾逗号重试。写手/上游偶发把中文标点写成
半角（07-24 事故：主 agent 半角污染整条流水线）——读取时把「紧邻汉字或全角
字符的半角 ,:;?!」归一化为全角。两类修正都回写，让仓库里的 daily.json
始终合法且标点统一。

不会误伤：URL 和英文语境是纯 ASCII、不与汉字相邻，不会被改；
去完尾逗号仍解析不了的真语法错误照常抛。
"""
import json
import re

_TRAILING_COMMA = re.compile(r",(\s*[}\]])")
_PUNC = {",": "，", ":": "：", ";": "；", "?": "？", "!": "！"}
# 汉字、CJK 标点（「」等）、全角形式
_CJK = re.compile(r"[一-鿿　-〿！-～]")


def _is_cjk(ch):
    return bool(ch) and bool(_CJK.match(ch))


def normalize_punct(s):
    """把邻接汉字/全角字符的半角 ,:;?! 换成全角（比较邻字时跳过空格）。
    两侧都是 ASCII 的不动（URL、时间、纯英文里的标点是合法半角）。
    返回 (新串, 修正数)。"""
    out, n = [], 0
    for i, ch in enumerate(s):
        if ch in _PUNC:
            j = i - 1
            while j >= 0 and s[j] == " ":
                j -= 1
            prev = s[j] if j >= 0 else ""
            k = i + 1
            while k < len(s) and s[k] == " ":
                k += 1
            nxt = s[k] if k < len(s) else ""
            if _is_cjk(prev) or _is_cjk(nxt):
                out.append(_PUNC[ch])
                n += 1
                continue
        out.append(ch)
    return "".join(out), n


def load_daily(path):
    """读 daily.json，容忍尾逗号和 BOM，半角标点自动归一化。path 是 pathlib.Path。"""
    s = path.read_text(encoding="utf-8-sig")
    fixed = s
    n_comma = 0
    try:
        json.loads(fixed)
    except json.JSONDecodeError:
        n_comma = len(_TRAILING_COMMA.findall(fixed))
        fixed = _TRAILING_COMMA.sub(r"\1", fixed)
    fixed, n_punc = normalize_punct(fixed)
    d = json.loads(fixed)  # 真语法错误在这里照常抛
    if fixed != s:
        path.write_text(fixed, encoding="utf-8")
        notes = []
        if n_comma:
            notes.append(f"{n_comma} 处尾逗号")
        if n_punc:
            notes.append(f"{n_punc} 处半角标点")
        print(f"· daily.json 已自动修正并回写：{'、'.join(notes)}")
    return d
