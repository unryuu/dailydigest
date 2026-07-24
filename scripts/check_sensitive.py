# -*- coding: utf-8 -*-
"""
check_sensitive.py <date> — 国内平台发布前的关键字筛查。

扫 reports/<date>/ 下的 daily.json、口播稿.md、dist/daily.zhihu.md，
对照 scripts/sensitive_words.txt（用户可编辑），命中就打出 文件+词+上下文。

命中不等于禁发：这是给人看的提醒，人工决定删改还是该平台跳过这条。
退出码：0 无命中，1 有命中（方便脚本串联）。
"""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORDS_FILE = pathlib.Path(__file__).resolve().parent / "sensitive_words.txt"
TARGETS = ["daily.json", "口播稿.md", "dist/daily.zhihu.md"]


def load_words():
    words = []
    for line in WORDS_FILE.read_text(encoding="utf-8-sig").splitlines():
        w = line.strip()
        if w and not w.startswith("#"):
            words.append(w)
    return words


def main():
    if len(sys.argv) != 2:
        raise SystemExit("用法：python scripts/check_sensitive.py <date>")
    date = sys.argv[1]
    folder = ROOT / "reports" / date
    words = load_words()
    hits = 0
    scanned = []
    for name in TARGETS:
        p = folder / name
        if not p.exists():
            continue
        scanned.append(name)
        text = p.read_text(encoding="utf-8-sig")
        for w in words:
            for m in re.finditer(re.escape(w), text):
                s = max(0, m.start() - 18)
                ctx = text[s:m.end() + 18].replace("\n", " ")
                print(f"⚠️ [{name}] 命中「{w}」：…{ctx}…")
                hits += 1
    print(f"\n筛查 {date}：扫了 {len(scanned)} 个文件（{'、'.join(scanned)}），词表 {len(words)} 词，命中 {hits} 处")
    if hits:
        print("→ 人工过一眼：删改措辞，或该条在国内平台版本里剔除")
        sys.exit(1)
    print("✅ 无命中")


if __name__ == "__main__":
    main()
