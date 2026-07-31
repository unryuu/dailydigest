# 数学家怎么验证 AI 给的结果：Lean 编译 + 纯数学改写（雅可比猜想）

- 日期：2026-07-21 / 2026-07-22
- 来源：https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/（Buzzard，Lean 验证，主文）；https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/（陶哲轩，多项式乘法改写）；https://x.com/__alpoge__/status/2079028340955197566（反例本身，Fable 5 找到）
- 主题：七、AI 辅助研究与数学

## 这是什么

**2026-07-21（反例本身）**：雅可比猜想是 Keller 1939 年提出的悬案：多项式映射只要雅可比行列式是非零常数，就应该处处可逆。该猜想曾被菲尔兹奖得主 Smale 列入「下个世纪十八大数学问题」，有过很多错误证明。Anthropic 研究员 Alpöge 周末公布了一个显式反例，猜想在三维及以上被推翻。

反例由 Fable 5 找到。Alpöge 出题后去看世界杯决赛，Fable 在决赛期间把反例算了出来。多路独立验证已通过。菲尔兹奖得主 Gowers 评价「pretty amazing」，说这是他头一回见到 LLM 解决一个他早有耳闻的名题。

**2026-07-21（Buzzard 盘点）**：形式化数学的旗手 Buzzard 盘点近期进展：5 月 ChatGPT 证伪 Erdős 单位距离猜想，7 月 Sol 几天内解决 Grothendieck 悬置 60 年的问题，然后是雅可比。他判断大规模 AI 生成数学不可避免，人类的角色从证明转向理解。他强烈建议博士生每月花 200 美元用这些工具。哈佛已经给全体博士生和教员免费开通。

**2026-07-22（陶哲轩解析）**：他把问题改写成多项式乘法来看，讲清这个映射为何局部可逆、整体不可逆；还举出了七次多项式作为反例。

## 细节（来自精读摘要）

**雅可比猜想反例（group-jacobian.md）**

数论学家 Levent Alpöge（哈佛 Society of Fellows 出身，现供职 Anthropic）在 X 上公布了雅可比猜想（Keller 1939，87 年悬案）的显式反例：一个 C³→C³ 的多项式映射，三个分量次数分别为 7、6、4，雅可比行列式恒等于 −2，但 (0,0,−1/4)、(1,−3/2,13/2)、(−1,3/2,13/2) 三个不同点都映到 (−1/4,0,0)——非单射，猜想在 n=3 被杀死，补恒等坐标后 n≥3 全灭；n=2（平面情形）仍然开放。反例由 Claude Fable 5 找到，验证门槛极低（符号计算几分钟可复核），截至 07-21 多路独立验证全部通过、无人指出错误。

反例映射（David Speyer 博客转录）：a=(1+xy)³z+y²(1+xy)(4+3xy)，b=y+3x(1+xy)²z+3xy²(4+3xy)，c=2x−3x²y−x³z；Speyer："The Jacobian of (a,b,c) is easily checked to be -2. However, the map (a,b,c) is generically three to one."（泛型三对一，不止那一根纤维撞车）。

失败机制：映射片层只在无穷远处合并（非 proper），有限处合并会要求行列式为 0，与恒为 −2 矛盾；多项式带加权齐次结构。

AI 角色的一手表述只有原推一句："thanx to … my other close friend fable for working during the world cup final"。媒体转述：Akhil 建议找反例，Alpöge 让 Fable 5 跑这个问题，自己去看世界杯决赛。聊天记录未公开，HN 有人以此质疑贡献度可能被高估。

独立验证（截至 07-21）：Zihan Zhang 的验证+推论笔记（SymPy 精确有理数运算复核三点撞车与行列式）；jacobianfun.org 的 verify.py 脚本 + preprint PDF；帝国理工博士生 Paul Rouzeau 已在 Lean 中形式化并提交 Formal Conjectures 仓库。

大佬表态：Tim Gowers（菲尔兹奖）："pretty amazing"，"first example of an LLM solving a problem not in my area that was nevertheless big enough that I had very definitely heard of it"，但强调这是反例，不算「数学终结」级别。

连锁死亡：JC 证伪连带击落 Mathieu 猜想（SU(3) 情形）、高斯矩猜想、Zhao 消没猜想、Image 猜想（各自的有限维情形）——因为这些猜想蕴含 JC。

**Buzzard：人类数学家正在被 AI「反例碾压」（group-buzzard.md）**

时间线：5/20 ChatGPT 证伪 Erdős 单位距离猜想（用的是 1960 年代 Golod-Shafarevich 定理）→ 6/26 OpenAI 的 Boris Alexeev 用 Sol 完成全量形式化，三周生成 120 万行 Lean 代码（对照：mathlib 全库 230 万行，人类写了 9 年）。

7/7 Formalizing Fermat 研讨会上 Akhil Mathew 提出 Grothendieck 60 年悬案（阶为 n 的有限自由群概形是否被 n 消灭），Sol 几天内找到反例（阶 4 群概形不被 4 消灭），Fable 4 小时自动形式化出 1076 行 Lean 证明，已提 mathlib PR #41748。

Buzzard 对验证的表述：只要命题已形式化，「检查（可能是 AI 生成的）Lean 代码是否构成证明或证伪就是件小事」——1076 行证明编译验证不到 5 分钟。「在我看来，任何不肯每月花 200 美元用这些工具的博士生都是疯了」；哈佛已给全体博士生、博后、教员免费开通 Fable。

他把同行「反例这么好找说明人类根本没认真想过这个问题」的说法诊断为悲伤五阶段里的「否认」。

**陶哲轩下场拆解**：他把问题改写成多项式乘法来看，讲清这个映射为何局部可逆、整体不可逆；还举出了七次多项式作为反例（呼应 Buzzard 提到的 Lean 验证法，这里是另一种纯数学改写验证法）。

## 可以怎么用

- 验证 AI 给出的数学/逻辑结论，优先找「机械可复核」的形式：能形式化的走 Lean 编译（几分钟出结果），不能形式化的就找一个更直观的等价改写（如陶哲轩把反例转成多项式乘法）让人一眼能判断对错。
- 别停留在「AI 说这是对的」层面，要求它给出一个第三方能独立复核的产物（脚本、编译通过的证明、可运行的验证代码），而不是自然语言叙述。
- 遇到「AI 给出反直觉结论」时，先问「这个结论能不能被改写成一个更简单、更基础的等价问题」——往往是理解错误在哪、而不是重复验算的更快路径。
- 人机分工上，AI 找结果、人来出题和把关复核，中间过程尽量留痕（哪怕像 Alpöge 那样只有一句话的一手表述也比什么都没有强）。
