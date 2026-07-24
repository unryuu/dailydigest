# 2026-07-13 日报存档（周一·长图第十期）

**规格**：1 金 2 银 5 真雷达 4 今日乐子 3 赔率
**投递**：Telegram `@dragonbro888`，链接 id=158 / 长图 id=159（1179×9203）

## 定牌

| 档位 | 条目 | 来源 |
|---|---|---|
| 金 | 开放权重模型「只剩 6 个月可活」 | interconnects（Nathan Lambert）|
| 银 | Thinking Machines 罕见发声：值得建的未来是人的未来 | thinking-machines |
| 银 | Zig 之父怒批 Bun 的 Rust 重写，Anthropic 被指放烟雾 | hacker-news（raymyers.org / 975 分）|

**金牌 6 个月大限**：Lambert 下的强论断——能力明显超过 GPT-5.5 / Opus 4.8 / GLM-5.2 这一档的开放权重模型，很可能半年内被美国政府立法封禁或无限期拖住审查。关键在他把死因判成监管而非算力/商业模式，还点名 Anthropic 的「蒸馏风险」叙事基本是监管俘获。reader 特别纠偏：核心机制是监管绞杀，别被「繁荣底下经济性衰亡」带偏；派活提示里的 Zyphra/Cohere/Poolside 三次抓取均未出现，已如实剔除、正文不提。

**银牌 Thinking Machines**：Mira Murati 家自 5 月后首次系统发声，立场文，押「分布式、用户拥有权重」，把「对齐集中在单一中心」判成权力风险，落到产品是 Tinker（可携带、自己拥有的 LoRA 权重）。无进展数字，靠稀缺性给银。

**银牌 Zig 之父炮轰**：manifest 原把身份标错成「Zed 作者」，reader 逐一核准是 Zig 之父 Andrew Kelley，Ray Myers（自称 Anthropic 客户 + Claude Code 竞品出身）声援并把矛头引向 Anthropic。被批的是 Bun 那篇《Rewriting Bun in Rust》公关博客（Bun 已被 Anthropic 收购，号称近 100% 由新模型 Fable 重写），非 benchmark 非 Claude Code。技术质疑有实锤（通篇只讲优点不提取舍、回避 Rust 编译变慢、可读性自相矛盾），HN 并非一边倒、替 Anthropic 辩护的也不少。

## 接任说明（前一窗口挂掉）

前一个窗口跑完了 scout（manifest）+ reader（group-1/2/3 digest）+ radar-fun 核链接（radar-fun.json），未写 daily.json。本窗接任完成：定牌 → 写 daily.json → 渲染 → 预览 → 发频道 → 收尾。scout/reader 产物未动，直接采信。

## scout / reader

- scout 全量扫 21 源：3 组精读 / 8 条真雷达候选 / 4 条乐子 / 6 个赔率 / **0 抓失败**。13 源无新货（周一 Import AI #465 未出、The Batch #361 已报）。
- reader 3 组 digest 已由前窗产出；radar-fun 10 条候选由前窗核查小 agent 逐条核链接。
- **radar-fun 核查结果**：three.ws「给 agent 3D 身体+钱包」核实失败（HF 博客找不到固定链接，项目真实但非 HF 博客文），按红线不编、删除 → 真雷达从 8 候选落定 5 条。Ask HN 打标帖找到真实 item id=48886741。Freeing Thucydides 核出实为 AI/地缘政治思想实验（非纯古典史怪帖），仍留乐子栏。

## 赔率盒子（多选题渲染新增）

用户把默认候选砍到 2 条（Askell 79.6% / 400 美元订阅档 40.3%），并主动要求收录原本因「多选报不了单一概率」弃掉的 GPT-6 芯片市场。

- 从 Manifold API 拉 `which-companys-chips-will-gpt6-be-t`（MULTIPLE_CHOICE，成交额约 2.4 万美元）：Nvidia 69.6% / Microsoft 11.2% / AMD 5.7% / OpenAI 系 4.7% / 其他 3.1% / Google 3.0% / Intel 2.7%（互斥，和约 100%）。
- **render_daily.py 新增多选分支**：odds 条目带 `options:[{name,prob}]` 时渲染成带比例底纹的选项条列表（`.oddm` 系列 CSS + fill 宽度=prob%），不影响原单概率格式与已调好的布局参数。链接消息仍用 `prob` 摘要串（此条填「Nvidia 69.6% 领跑」）避免 send_daily 取不到 prob 报错。

## 写作与流程

- 自查（`——|反直觉|拧|反常|有意思的是|最.的是|不是.*而是|<[^b/]|<br>`）全程为空，一次通过。
- 用户编辑改动不多（金牌收紧、银 1 title 加「神秘实验室」前缀、几条雷达 body 略删），未留尾逗号。以用户版本为准，未回改。
- 双银周一（1 金 2 银），料不薄。开放模型监管线是新主线（此前饱和线未覆盖）。

## 待办延续

- 开放权重模型「监管绞杀 / 6 个月大限」是新主线，后续若有立法/能力追平的实质进展再收，泛泛口水不追。
- Thinking Machines 是年更级低频源，一更必看。
- 多选赔率渲染已通，后续多选市场（此前只能弃）可正常收录。
