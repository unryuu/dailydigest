# Buzzard：人类数学家正在被 AI「反例碾压」

- 推荐强度: 强
- 档位线索: 权威人物（Xena 项目主理人、Imperial College、形式化数学第一代言人）亲口盖章「大规模 AI 生成数学不可避免」，且文中直接点名并背书了我们今天头条（Alpöge/Fable 证伪雅可比猜想），信息密度和引语质量都够金牌级；但如果头条已经用雅可比猜想本身做金牌，本文更适合做银牌（权威视角 + 两个月三个反例的时间线盘点），避免同题占两金。HN 385 分 173 评论。
- 涉及文章: [Human mathematicians are being outcounterexampled](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) · Xena Project（Kevin Buzzard 个人博客）· 2026-07-20 · [HN 385 分 / 173 评论](https://news.ycombinator.com/item?id=48983382)

## 核心主张
AI 正在批量解决悬置数十年的数学猜想——不是证明，是找反例，而且速度快到人类跟不上。Buzzard 列出两个月内三连击：5 月 ChatGPT 证伪 Erdős 单位距离猜想、7 月 11 日 Sol 几天内解决 Grothendieck 悬置 60 年的有限平坦群概形问题、7 月 20 日前后 Alpöge 用 Fable 找到雅可比猜想（悬置 100 年）的反例。他的结论：「大规模 AI 生成的数学发展不可避免」，人类的角色从「证明」转向「理解」——反例的真正价值是让人类更好地理解数学。

## 为什么值得看（钩子）
形式化数学最权威的怀疑者亲口宣布投降时刻：他现在拒读 AI 生成的非形式化数学（「请把整件事在 Lean 里形式化再来找我」），验证 1076 行 Lean 反例证明只需不到 5 分钟——信任链从「信数学家」变成「信编译器」。

## 关键细节 / 引述
- 时间线：5/20 ChatGPT 证伪 Erdős 单位距离猜想（用的是 1960 年代 Golod-Shafarevich 定理）→ 6/26 OpenAI 的 Boris Alexeev 用 Sol 完成全量形式化，三周生成 120 万行 Lean 代码（对照：mathlib 全库 230 万行，人类写了 9 年）。
- 7/7 Formalizing Fermat 研讨会上 Akhil Mathew 提出 Grothendieck 60 年悬案（阶为 n 的有限自由群概形是否被 n 消灭），Sol 几天内找到反例（阶 4 群概形不被 4 消灭），Fable 4 小时自动形式化出 1076 行 Lean 证明，已提 mathlib PR #41748。
- 雅可比猜想：Buzzard 原文确认「Levent 在 X 上发帖说 Fable 找到了雅可比猜想的反例。这是大事——代数几何著名问题，悬置 100 年」；Alpöge 是在世界杯决赛期间发的推。Paul Lezeau 已手工形式化，PR 提交至 DeepMind 的 Formal Conjectures 仓库。新反例是三变量、次数 7（HN 评论对照：1983 年人类穷举检查过两变量、次数 100 以内）。
- Buzzard 对验证的表述：只要命题已形式化，「检查（可能是 AI 生成的）Lean 代码是否构成证明或证伪就是件小事」——1076 行证明编译验证不到 5 分钟。
- 「在我看来，任何不肯每月花 200 美元用这些工具的博士生都是疯了」；哈佛已给全体博士生、博后、教员免费开通 Fable。
- 他把同行「反例这么好找说明人类根本没认真想过这个问题」的说法诊断为悲伤五阶段里的「否认」。
- HN 反应：怀疑派 tantalor 认为 LLM 擅长插值而非外推，所以找反例比做证明容易；数学背景评论者（madhadron、remus）反而强调反例的教学价值——「反例是证伪全称命题的唯一方式」；wizzwizz4 补充反例搜索几十年前就有，「人类没花够时间想」确实是弱借口。HN 评论区未讨论 IMO。

## 与近期的关系
直接评论并确认了今天头条（Alpöge/Fable 证伪雅可比猜想）——本文发布于 07-20，正是对该事件及近两个月「AI 反例潮」的系统盘点，属于头条的权威第三方背书 + 时间线扩展，不是独立新事件。Erdős 单位距离猜想（5 月）若往期报过需查重。

## IMO 快讯（07-21 核查）
- 官方（人类）成绩已公布：[IMO 2026 官方页](https://www.imo-official.org/editions/2026/) 显示上海赛区 117 国 666 名选手，金牌线 29 分，金 55 / 银 105 / 铜 189，**人类选手 7 个满分**。今天 07-21 是闭幕日。
- **AI 官方认证成绩尚未公布**（截至本次核查）。DeepMind 无 2026 新博客；去年（2025）也是 7/21 才发官宣，节奏可能复刻。搜索结果里大量 2025 旧闻（Gemini Deep Think 35/42 金牌）混入，注意别当成今年成绩。
- Manifold 两盘均**未结算**：[「Gemini perfect score on IMO 2026?」](https://manifold.markets/johnNZOy/gemini-perfect-score-on-imo-2026) 现价 72.8%（与昨读 73-78% 持平）；[「Perfect score achieved by an AI model in IMO 2026?」](https://manifold.markets/Bayesian/perfect-score-achieved-by-an-ai-mod) 现价 93.3%（昨读 93%）。后者评论区有人称「5.6 Pro 在我的测试里基本做到 42/42」「听说 GPT 5.6 解出了 P3」，并评价今年题目「很简单、比 2025 Day 2 还容易」——均为民间自测，非官方。
