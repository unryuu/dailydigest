# Astra 的隐藏推理：空白 token、猜测深度与监控边界

- 推荐强度：强
- 档位线索：值得收，但建议银牌，不够金牌。最硬的新结果是无信息 filler token 让 Astra 在多类任务上明显变强，以及任务成败更贴近「猜测后要迭代多少轮才能自洽」而非表面步骤数；不过 9 月 9 日已经报道 Astra 在零推理 token 下能做 4 至 5 跳事实链，本期只能写新增的干预实验、数字和替代机制。机制归因仍高度推测，四篇中另有两篇并不是 Astra 实验，不能包装成同一组确证。
- 涉及文章：[Astra is much better at reasoning with filler tokens than previous models](https://www.lesswrong.com/posts/uvhuZHFtrgk8kNiZc/astra-is-much-better-at-reasoning-with-filler-tokens-than) · LessWrong，Dylan Xu、SebastianP、Alek Westover · 2026 年 9 月 10 日
- 涉及文章：[Astra's no-CoT limits track speculative depth, not step count](https://www.lesswrong.com/posts/WFc3NkuPaYFrYuaZd/astra-s-no-cot-limits-track-speculative-depth-not-step-count) · LessWrong，MBaert · 2026 年 9 月 11 日
- 涉及文章：[CoT controllability evals seem very under-elicited](https://www.lesswrong.com/posts/BbP2wCyDGdPWJ7PwP/cot-controllability-evals-seem-very-under-elicited) · LessWrong，Jozdien · 2026 年 9 月 11 日
- 涉及文章：[An operationalization of opaque serial depth](https://www.lesswrong.com/posts/x8BvtWxtoajBGHS3g/an-operationalization-of-opaque-serial-depth) · Redwood Research／LessWrong，Ryan Greenblatt、frisby、Alek Westover、Lukas Finnveden、Alexa Pan、Julian Stastny · 2026 年 9 月 10 日

## 核心主张

新增证据不是再证明一次「Astra 不写思维链也会做多跳题」，而是对这项能力做了主动干预：题目后面塞入本身不含信息的点号、计数序列或题目复本，即使要求模型立即回答且 API 报告零推理 token，Astra 的准确率仍随 filler 增长而显著上升。这说明输入位置增加后发生了更多不可见计算，但不能据此断言模型在点号里逐步思考，更不能直接证明某种循环架构。

另一组实验进一步反驳了「能完成多少书面步骤，就等于内部做了多少串行步骤」的直觉。作者提出，Astra 可能先凭启发式同时猜出许多中间状态，再并行更新，直到答案自洽；因此更好的预测量是这套猜测算法要迭代多少轮才能收敛的「speculative depth」，而不是题面列了多少步。实验支持存在某种投机式并行处理，但具体算法、循环深度和 Astra 架构之间的因果关系都没有被测定。

另外两篇分别给这类风险补上评测漏洞与架构度量：CoT 可控性会被提示词严重低估；NLS depth 则试图用「不经过自然语言根节点的最长计算路径」量化模型可做多少不透明串行计算。它们是解释框架，不是 Astra 隐藏推理的新确证。

## 为什么值得看（钩子）

最反直觉的点是：往提示词末尾加入没有语义的信息，模型反而能多做事；而一道看上去有 54 步的题，也可能因为能提前猜中大量中间状态，实际只需很少几轮串行修正。它把讨论从「Astra 能藏几步」推进到「我们可能连什么叫一步都量错了」。

## 关键细节 / 引述

- filler 实验中，Astra 的 4 跳自然事实题约从 10％升到 50％，提升持续到 4096 个 filler token；旧 AIME 题约从 60％升到 90％，AIME 级问题的收益约在 8192 token 达峰。三个 filler 版本——点号、从 1 开始计数、重复题目——在这些测试上给出大致相似的趋势。
- 更广的结果不是只挑中一类题：HLE 共 2157 题，Astra 从无 filler 的 0.28 升至 1000 个计数 filler 的 0.41，`reasoning:low` 为 0.47；LiveBench 单轮非 Agent 任务共 618 题，从 0.66 升至 0.76，`reasoning:low` 为 0.88。也就是说 filler 增益显著，但仍没有追平正常低强度显式推理。
- filler 的位置有条件性：放在题目之后，或预填在 assistant 回答开头，都有类似效果；放在题目之前没有效果。要求模型「利用这些点来处理题目」与明确说点号没有信息、应忽略，结果也近似。作者还测试让模型在空 reasoning 之后、最终答案之前自行输出固定数量的点号，称成绩大致相同且 Astra 超过 99％ 的输出合规；这些结果没有列在正文图表中。
- speculative-depth 实验先专门排除了捷径：500 步单变量算术因整数除法造成状态收敛，任取数字只做末 20 步也可能得到正确答案；纯加减又可树形并行归约。新建的 swap-N、bitwise-N 都让所有模型掉分，但 Astra 仍约领先其他模型 3 倍。布尔电路中，Astra 在含 `and／or` 的 bool-26 上达到 54 个赋值步骤的 50％ 成功边界，相当于题面 108 个顺序布尔操作；改为更难利用短路和统计偏差的纯 `xor` 后，边界骤降到 11 步。
- 「speculative depth」不是题目客观唯一的深度。作者的实现先用每个变量的初值猜测其所有中间值，再并行重算全部操作，反复迭代到自洽；所需迭代轮数才叫 speculative depth，且把 `a xor (b and／or c)` 整体算作一个操作。随机 bool-N 的该深度平均约为 N／2；按步数与该深度交叉生成题目后，成功率与后者的相关性更强，但每个测试格仅做 10 次，结果噪声较大。
- CoT 可控性论文实际测试的是 Qwen3-8B、Qwen3-32B、GPT-OSS-20B、GPT-OSS-120B，不是 Astra。Claude Opus 4.6 帮它们迭代提示模板后，可控性普遍约提高 2 至 3 倍或更多，例如 GPT-OSS-120B 从 5.5％ 升至 15％；优化提示在 10 个未参与迭代的新约束上也多数优于基线。Astra 只在脚注中引用系统卡结果：其 CoT 可控性高于 Sol 和 GPT-5.5 Thinking，CoT 短于 1000 token 时接近跑满；本文没有证明长 CoT 的 Astra 还能提高多少。

## 必要限定

- filler 结果证明的是「加入无信息位置与准确率共同上升」，不是直接观测到 token 内部承载了隐藏思维。重复题目并非严格无信息，因为它可改善注意力；三种 filler 都有效，只能削弱单一语义解释，不能区分并行预填计算、位置效应、循环计算或其他架构机制。
- 自然事实题的横向比较并非同难度：Astra 用 4 跳，其他模型用 2 跳，因为非 Astra 模型在 4 跳基线几乎落到地板。统计检验显示 Sol 在五组任务中的三组也随 filler 有显著改善，但幅度远小于 Astra；因此「只有 Astra 有该能力」过强。
- 投机式推理是机制假说。研究只在人工生成的算术与布尔微基准上发现相符行为，任务顺序固定且便于建立依赖图；作者没有证明 Astra 使用其描述的确切算法，也没有证明现实规划的「20 步」能以同样方式压缩。
- CoT 可控性实验的提升可能部分来自缩短推理链。Qwen 的 few-shot 设置把 CoT 长度缩短 2 至 4 倍，并把 Qwen3-32B 任务准确率从 36.5％ 降到约 23％；但多个接近基线准确率和长度的 zero-shot 设置仍有 2 至 3.5 倍可控性提升。提示方案胜过 950 例微调也不是严格公平比较，因为该微调数据更偏离测试分布。
- NLS depth 是架构代理指标，不是实际隐藏能力或可监控性的测量。它把自然语言根节点定义为：来自人类可理解媒体的预训练先验、不扩展输出空间、不把 token 改作与预训练语义根本不同的数据，且后续梯度不穿过该节点；NLS depth 则是等价计算电路中不经过这些节点的最长路径上界。标准 Transformer 约为层数乘以 `4⌈log₂ hidden_dim⌉＋⌈log₂ sequence_length⌉＋17`，但指标会把低 FLOP 的串行归一化也算得很深，DeepSeek-V4-Pro 就是作者承认的误判案例。
- 对 Astra，NLS 文章只掌握 OpenAI 首席科学家 Jakub Pachocki 的公开说法：当前前沿模型（含 Astra）的计算图深度在 GPT-4 的 2 倍以内。作者进一步猜测 Astra 相对 Sol 可能增加约 2 至 3 倍 NLS depth，但这取决于 Sol 的未知深度，不能写成已知架构事实。

## 与近期的关系

重复风险高。9 月 9 日成品已经写过「24 道外部测试中 Astra 每题不比 Sol 差，可串起的事实链约从 2 至 3 跳提高到 4 至 5 跳」，并明确说零推理 token 不等于内部没有计算。因此本期不能再用「Astra 会隐藏推理」「循环 Transformer 可能让思维链失真」作主体，也不应重讲 4 至 5 跳数字。

真正可报的增量只有三层：一是 filler token 对能力有可重复的剂量效应和位置效应；二是 bool／xor 对照显示表面步骤数会被短路、偏置和并行猜测严重高估，speculative depth 或许更接近真正瓶颈；三是现成 CoT-Control 分数可能因提示不足而低估模型主动塑形思维链的能力。若版面只留一条，应以 filler 实验为主，speculative depth 作为解释但明确标注推测；CoT 提示优化和 NLS 定义最多做限定或一句背景，避免把四项不同证据揉成「Astra 已被证实会秘密规划」。
