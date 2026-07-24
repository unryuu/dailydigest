# 雅可比猜想被证伪：Alpöge + Claude Fable 5 给出显式反例

- 推荐强度: 强
- 档位线索: 金牌级。87 年悬案、反例可被任何人几分钟内独立验算、Gowers 等大佬已表态、AI 深度参与且与本产品线直接相关。截至 07-21 无人找出错误，共识基本形成。唯一软肋：AI 具体做了多少只有一条推文级的一手表述，写作时别越过一手表述夸大。
- 涉及文章:
  - [Alpöge 原推](https://x.com/__alpoge__/status/2079028340955197566) · X @__alpoge__ · 2026-07-19（美东晚间，UTC 07-20 约 02:19）
  - [The new counterexample to the Jacobian conjecture](https://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/) · Secret Blogging Seminar（David Speyer）· 2026-07-20
  - [HN 讨论帖](https://news.ycombinator.com/item?id=48973869) · Hacker News · 772 分 / 480 评论
  - [The Jacobian counterexample, explained](https://jacobianfun.org/jacobian-explained) · jacobianfun.org（Alexis Gallagher，含验证脚本与 preprint PDF）· 2026-07
  - [Direct Consequences of the Three-Dimensional Counterexample](https://zzhang-iu.github.io/papers/direct-consequences-jacobian/index.html) · Zihan Zhang 验证/推论笔记 · 2026-07-20
  - [数学界反应汇总](https://officechai.com/ai/how-the-math-community-has-reacted-to-fable-helping-disprove-the-jacobian-conjecture/) · OfficeChai · 2026-07-21
  - [GIGAZINE 报道](https://gigazine.net/gsc_news/en/20260721-claude-fable-5-jacobian-conjecture/) · 2026-07-21

## 核心主张
数论学家 Levent Alpöge（哈佛 Society of Fellows 出身，现供职 Anthropic）在 X 上公布了雅可比猜想（Keller 1939，87 年悬案）的显式反例：一个 C³→C³ 的多项式映射，三个分量次数分别为 7、6、4，雅可比行列式恒等于 −2，但 (0,0,−1/4)、(1,−3/2,13/2)、(−1,3/2,13/2) 三个不同点都映到 (−1/4,0,0)——非单射，猜想在 n=3 被杀死，补恒等坐标后 n≥3 全灭；n=2（平面情形）仍然开放。反例由 Claude Fable 5 找到，验证门槛极低（符号计算几分钟可复核），截至 07-21 多路独立验证全部通过、无人指出错误。

## 为什么值得看（钩子）
- 87 年的中心猜想，最后死于一段 216 字符的多项式——不需要读懂任何论文，任何人用 SymPy/Wolfram Alpha 几分钟就能亲手验证它是对的。
- 一手表述的画面感：Alpöge 的原推是"the jacobian conjecture is false"，感谢朋友 Akhil 提问、感谢"另一位好朋友 fable 在世界杯决赛期间干活"——人去看球，模型在算。

## 关键细节 / 引述
- 反例映射（Speyer 博客转录）：a=(1+xy)³z+y²(1+xy)(4+3xy)，b=y+3x(1+xy)²z+3xy²(4+3xy)，c=2x−3x²y−x³z；Speyer："The Jacobian of (a,b,c) is easily checked to be -2. However, the map (a,b,c) is generically three to one."（泛型三对一，不止那一根纤维撞车）。
- 失败机制（jacobianfun.org / Speyer 帖评论区，Will Sawin 等参与分析）：映射片层只在无穷远处合并（非 proper），有限处合并会要求行列式为 0，与恒为 −2 矛盾；多项式带加权齐次结构。
- AI 角色的一手表述只有原推一句："thanx to … my other close friend fable for working during the world cup final"，推串内附 Wolfram Alpha 核算。媒体转述（GIGAZINE 等）：Akhil 建议找反例，Alpöge 让 Fable 5 跑这个问题，自己去看世界杯决赛（决赛正是 07-19）。聊天记录未公开，HN 有人以此质疑贡献度可能被高估；Bartosz Naskręcki（波兹南密茨凯维奇大学）泼冷水方向是"这不会是一句简单 prompt，出题本身需要真功夫"。写作时人机分工按此口径：Fable 找到反例，人出题+复核，中间过程未公开。
- 独立验证（截至 07-21）：Zihan Zhang 的验证+推论笔记（SymPy 精确有理数运算复核三点撞车与行列式）；jacobianfun.org 的 verify.py 脚本 + Gallagher 的 preprint PDF（https://jacobianfun.org/paper/Gallagher2026_JC.pdf）；帝国理工博士生 Paul Rouzeau 已在 Lean 中形式化并提交 Formal Conjectures 仓库。注意：所谓"verification preprint"目前是 Gallagher/Zhang 这类网页+PDF，未见 arXiv 编号。
- 大佬表态：Tim Gowers（菲尔兹奖）："pretty amazing"，"first example of an LLM solving a problem not in my area that was nevertheless big enough that I had very definitely heard of it"，但强调这是反例，不算"数学终结"级别。Daniel Litt（多伦多）："Very bullish for near-term impact of AI on math. Probably lots more of these coming soon." Jared Duker Lichtman（斯坦福）："quite a remarkable result"。
- 连锁死亡（Zhang 笔记）：JC 证伪连带击落 Mathieu 猜想（SU(3) 情形）、高斯矩猜想、Zhao 消没猜想、Image 猜想（各自的有限维情形）——因为这些猜想蕴含 JC。
- HN 细节：772 分 / 480 评论；有评论惊讶反例次数只有 7（此前社区预期反例若存在会是高得多的次数，此说法出自 HN 评论，非文献，慎用）。
- 人物：Alpöge 是数论学家，近年工作包括 Hilbert 第十问题在数域上的推进，现为 Anthropic 研究员；提问的 Akhil 媒体普遍认定为数学家 Akhil Mathew（原推只写了名字 Akhil，全名未在一手推文确认）。

## 与近期的关系
全新事件（07-19 晚爆出，07-20~21 发酵），与往期无重复。是"AI 参与前沿数学"叙事线的最新也是最硬的一格：此前多为竞赛题/辅助证明，这次是命名悬案的显式反例。与本产品（Claude Fable 5）直接相关，注意行文别自吹。
