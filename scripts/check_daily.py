# -*- coding: utf-8 -*-
"""
check_daily.py <date> — daily.json 发布前一体化自查（替代旧 grep 自查行）。

ERROR（必须清零才能发）：
  结构：未知分区键、内容条目缺 tier/非法 tier、缺 url/title、文件内重复 URL
  三硬坑：<br>、正文裸 ASCII 双引号、裸 <>& 出现在 <b></b> 之外
WARNING（逐条人工过，不强制清零）：
  禁词（与 roles/定调.md 同步维护：改定调要同步改这里的 BANNED）
  「xx 的是」句式、字数警戒线（金 250 / 银 150 / 无牌 65）、odds 数量不在 4-6

读取走 dailyjson.load_daily：尾逗号与半角标点已自动修正回写（打印修正数）。
退出码：有 ERROR → 1，否则 0。
"""
import sys, re, pathlib
from dailyjson import load_daily

ROOT = pathlib.Path(__file__).resolve().parent.parent

CONTENT_SECTIONS = ["industry", "deep", "papers", "regulation", "official", "fun"]
KNOWN_KEYS = set(CONTENT_SECTIONS) | {"date_label", "odds"}
TIERS = {"gold", "silver", "none"}

# 与 roles/定调.md 同步维护
BANNED = [
    ("——", "少用破折号"),
    ("反直觉", "反直觉直接陈述、别强调"),
    ("反常", "同上"),
    ("有意思的是", "别提示读者「这里很妙」"),
    (r"最.的是", "同上"),
    (r"不是.{0,12}而是", "平铺直叙"),
    ("值得注意", "别点评"),
    ("拧", "「拧着来」类强调"),
]
DE_SHI = re.compile(r"[一-鿿]{1,4}的是")
CJK_HALF = re.compile(r"[一-鿿][,:;?!]|[,:;?!][一-鿿]")


def texts_of(item):
    for k in ("title", "label", "toc", "body", "question", "note"):
        v = item.get(k)
        if v:
            yield k, v
    for op in item.get("options") or []:
        if op.get("name"):
            yield "options.name", op["name"]


def zh_len(s):
    return len(re.sub(r"\s", "", s or ""))


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/check_daily.py <date>")
    date = sys.argv[1]
    path = ROOT / "reports" / date / "daily.json"
    d = load_daily(path)

    errors, warns = [], []

    for k in d:
        if k not in KNOWN_KEYS:
            errors.append(f"未知分区键「{k}」")
    if not d.get("date_label"):
        errors.append("缺 date_label")

    seen_urls = {}
    all_items = []  # (位置描述, item, 是否内容区)
    for sec in CONTENT_SECTIONS:
        for i, it in enumerate(d.get(sec) or []):
            all_items.append((f"{sec}[{i}]「{(it.get('title') or '')[:18]}」", it, True))
    for i, it in enumerate(d.get("odds") or []):
        all_items.append((f"odds[{i}]「{(it.get('question') or '')[:18]}」", it, False))

    for pos, it, is_content in all_items:
        if is_content:
            tier = it.get("tier", "none")  # 缺省=无牌，与渲染器同语义
            if tier not in TIERS:
                errors.append(f"{pos} tier 非法：{tier!r}")
            if not it.get("title"):
                errors.append(f"{pos} 缺 title")
        url = it.get("url", "")
        if not (isinstance(url, str) and url.startswith("http")):
            errors.append(f"{pos} 缺 url 或不是 http 链接")
        elif url in seen_urls:
            errors.append(f"{pos} URL 与 {seen_urls[url]} 重复：{url}")
        else:
            seen_urls[url] = pos

        joined = "\n".join(v for _, v in texts_of(it))
        # 三硬坑
        if "<br" in joined:
            errors.append(f"{pos} 有 <br>，换行要用真 \\n")
        if '"' in joined:
            errors.append(f"{pos} 有裸 ASCII 双引号，引用改「」")
        stripped = re.sub(r"</?b>", "", joined)
        stripped = re.sub(r"&(amp|lt|gt);", "", stripped)
        for ch in "<>&":
            if ch in stripped:
                errors.append(f"{pos} 有裸 {ch}（Telegram 会当 HTML 报 400），转义或改中文")
                break
        # 半角标点残留（load 已归一化，理论上应为 0）
        m = CJK_HALF.search(joined)
        if m:
            errors.append(f"{pos} 汉字邻接半角标点残留：…{m.group(0)}…")
        # 禁词
        for pat, why in BANNED:
            for m in re.finditer(pat, joined):
                ctx = joined[max(0, m.start() - 8):m.end() + 8].replace("\n", " ")
                warns.append(f"{pos} 命中「{m.group(0)}」（{why}）：…{ctx}…")
        for m in DE_SHI.finditer(joined):
            ctx = joined[max(0, m.start() - 6):m.end() + 10].replace("\n", " ")
            warns.append(f"{pos} 「xx 的是」句式：…{ctx}…")
        # 字数警戒线
        if is_content:
            n = zh_len(it.get("body"))
            tier = it.get("tier", "none")
            limit = {"gold": 250, "silver": 150, "none": 65}.get(tier)
            if limit and n > limit:
                warns.append(f"{pos} {tier} 正文 {n} 字，超警戒线 {limit}（回头做删除测试）")

    n_odds = len(d.get("odds") or [])
    if not 4 <= n_odds <= 6:
        warns.append(f"odds 有 {n_odds} 条，常规是 4-6")

    for e in errors:
        print(f"❌ {e}")
    for w in warns:
        print(f"⚠️ {w}")
    n_items = sum(1 for _, _, c in all_items if c)
    print(f"\n自查 {date}：内容 {n_items} 条 + 赔率 {n_odds} 条 → ERROR {len(errors)} / WARNING {len(warns)}")
    if errors:
        sys.exit(1)
    print("✅ 无 ERROR" + ("（WARNING 逐条人工过）" if warns else ""))


if __name__ == "__main__":
    main()
