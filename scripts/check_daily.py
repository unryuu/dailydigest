# -*- coding: utf-8 -*-
"""
check_daily.py <date> — daily.json 发布前一体化自查（替代旧 grep 自查行）。

ERROR（必须清零才能发）：
  结构：未知分区键、内容条目缺 tier/非法 tier、缺 url/title、文件内重复 URL
  三硬坑：<br>、正文裸 ASCII 双引号、裸 <>& 出现在 <b></b> 之外
WARNING（逐条人工过，不强制清零）：
  禁词（与 roles/定调.md 同步维护：改定调要同步改这里的 BANNED）
  「xx 的是」句式、odds 数量不在 4-6
  字数警戒线：金 250 / 银 150 / 无牌 65 / 独家视角 350 / 简讯标题 30
  引子式首句、首句复述 title（2026-07-27 落地，07-24~26 三期连续被用户砍）

读取走 dailyjson.load_daily：尾逗号与半角标点已自动修正回写（打印修正数）。
退出码：有 ERROR → 1，否则 0。
"""
import sys, re, pathlib
from dailyjson import load_daily

ROOT = pathlib.Path(__file__).resolve().parent.parent

CONTENT_SECTIONS = ["industry", "angle", "deep", "papers", "regulation", "official", "brief", "fun"]
KNOWN_KEYS = set(CONTENT_SECTIONS) | {"date_label", "odds"}
TIERS = {"gold", "silver", "none"}
# 分区专属字数线（其余按 tier 走 gold/silver/none）
SECTION_LIMIT = {"angle": 350, "brief": 30}  # angle 看 body，brief 看 title

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

# 引子式首句（2026-07-27 落地，07-24/25/26 三期连续被用户砍）
# 用户的动作一律是：删掉铺垫，第一句直接给事实。只查 body 第一句。
LEAD_IN = [
    (r"^.{0,14}：", "首句带冒号的「XX：YY」，去冒号直接陈述"),
    (r"^(随着|最近|近来|近日|目前|一直以来|长期以来|众所周知|在.{0,14}背景下)", "背景铺垫开头"),
    (r"^.{0,10}(算了笔账|的答案是|的说法是|描述的.{0,6}是|给出的.{0,6}是)", "先介绍谁怎么说，再说事"),
    (r"^.{0,12}(指出|认为|表示|写道|强调|提醒)[，。]", "首句主语是转述人不是事实"),
    (r"^.{0,20}(普遍漏掉|大多忽略|很少有人|没什么人注意)", "先立靶子再打"),
    (r"^(过去|以前|原来|传统上|旧办法|老办法).{0,24}[，。]", "先讲旧办法的毛病再讲新办法"),
]


def first_sentence(body):
    s = (body or "").split("\n\n")[0].strip()
    m = re.search(r"[。！？]", s)
    return s[:m.end()] if m else s


def texts_of(item):
    for k in ("title", "label", "toc", "body", "question", "note"):
        v = item.get(k)
        if v:
            yield k, v
    for op in item.get("options") or []:
        if op.get("name"):
            yield "options.name", op["name"]
    for s in item.get("sources") or []:
        if s.get("name"):
            yield "sources.name", s["name"]


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
    all_items = []  # (位置描述, item, 分区键；odds 用 None)
    for sec in CONTENT_SECTIONS:
        for i, it in enumerate(d.get(sec) or []):
            all_items.append((f"{sec}[{i}]「{(it.get('title') or '')[:18]}」", it, sec))
    for i, it in enumerate(d.get("odds") or []):
        all_items.append((f"odds[{i}]「{(it.get('question') or '')[:18]}」", it, None))

    for pos, it, sec in all_items:
        is_content = sec is not None
        if is_content:
            tier = it.get("tier", "none")  # 缺省=无牌，与渲染器同语义
            if tier not in TIERS:
                errors.append(f"{pos} tier 非法：{tier!r}")
            if not it.get("title"):
                errors.append(f"{pos} 缺 title")
        urls = [("url", it.get("url", ""))]
        for j, s in enumerate(it.get("sources") or []):  # angle 的额外来源
            urls.append((f"sources[{j}]", s.get("url", "")))
            if not s.get("name"):
                errors.append(f"{pos} sources[{j}] 缺 name")
        for tag, url in urls:
            if not (isinstance(url, str) and url.startswith("http")):
                errors.append(f"{pos} {tag} 缺 url 或不是 http 链接")
            elif url in seen_urls:
                errors.append(f"{pos} {tag} 与 {seen_urls[url]} 重复：{url}")
            else:
                seen_urls[url] = f"{pos}.{tag}"

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
        # 字数警戒线 + 全量 body 规范（07-24 用户定：每条都配一行）
        if is_content:
            n = zh_len(it.get("body"))
            tier = it.get("tier", "none")
            if sec == "brief":  # 行业简讯：只有 title，没 body
                t = zh_len(it.get("title"))
                if t > SECTION_LIMIT["brief"]:
                    warns.append(f"{pos} 简讯标题 {t} 字，超警戒线 {SECTION_LIMIT['brief']}")
                if n:
                    warns.append(f"{pos} 简讯不写 body（写得下就该升无牌），现有 {n} 字")
            else:
                limit = SECTION_LIMIT.get(sec) or {"gold": 250, "silver": 150, "none": 65}.get(tier)
                if limit and n > limit:
                    warns.append(f"{pos} {sec if sec in SECTION_LIMIT else tier} 正文 {n} 字，"
                                 f"超警戒线 {limit}（回头做删除测试）")
                if n == 0:
                    warns.append(f"{pos} 没有 body（规范：每条配一行展开）")
                # 引子式首句（07-27 落地）
                fs = first_sentence(it.get("body"))
                for pat, why in LEAD_IN:
                    if re.search(pat, fs):
                        warns.append(f"{pos} 首句疑似引子（{why}）：…{fs[:34]}…")
                        break
                # title 说过的，body 别再说一遍
                # 专名（Debian、OpenAI）本来就该两处都出现，只查成句的中文片段
                ttl = re.sub(r"\s", "", it.get("title") or "")
                if len(ttl) >= 6 and fs:
                    hit = next((w for i in range(len(ttl) - 5)
                                for w in [ttl[i:i + 6]]
                                if len(re.findall(r"[一-鿿]", w)) >= 5 and w in fs), None)
                    if hit:
                        warns.append(f"{pos} 首句与 title 重复「{hit}」，title 说过的别再说")

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
