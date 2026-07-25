# Opus 5 发布当天的两篇配套文：一篇教你把提示词删掉 80%，一篇教你在四个模型里挑

- 推荐强度: 第 1 篇强，第 2 篇弱
- 档位线索:
  - 第 1 篇（上下文工程）：**银**。有一个可引用的硬数字（80%）、一段官方肯放出来的 Claude Code 系统提示词新旧原文对照、以及一条与主流实践正面拧着来的结论（「给示例反而有害」）。不建议上金：全文只有 80% 这一个数字，没有任何 token 预算 / 长度阈值 / 位置策略，后半程是通用建议；且与 07-23 银牌「Anthropic：好的 agent harness 靠做减法」同一论点（见「与近期的关系」）。
  - 第 2 篇（选型）：**无牌**，确认是产品文档腔。但里面有**一个值得单独摘出来的数字**（advisor 策略：SWE-bench Pro 上 Sonnet 5 配 Fable 5 顾问 = Fable 5 全程跑的 10% 以内、63% 的价钱），以及**官方第一次正面回答「Opus 和 Fable 该选谁」**。建议不给它单独条目，把这两条当细节喂给 group-1 的 Opus 5 头条，或作一条无牌短讯。
- 涉及文章:
  - [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) · Anthropic 官方博客（作者署名 Thariq Shihipar，member of technical staff）· 2026-07-24 · 分类 Claude Code / Agents · 标称 5 分钟（正文实测约 9800 字符）· 全文读到
  - [Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) · Anthropic 官方博客（无个人署名）· 2026-07-24 · 分类 Enterprise AI / Agents / Claude Code · 标称 5 分钟 · 全文读到

## 核心主张

两篇是同一天放出的一对「Opus 5 上线后你该改什么」配套文，方向相反但内核一致：**Anthropic 说，5 代模型的正确用法是给它更少的约束、更贵的起点。**

第 1 篇的一句话：Anthropic 自称「我们为 Claude Opus 5、Claude Fable 5 这类模型删掉了 Claude Code 系统提示词的 80% 以上，在我们的编码评测上没有可测量的损失」。论点是过去两年攒下的六条上下文工程「最佳实践」里，有一批已经变成迷信——最尖锐的一条是**给工具用法举例子现在是负收益**（「我们发现给示例反而把它们限制在某个探索空间里」），而这在旧模型时代是「工具使用的第一原则」。

第 2 篇的一句话：默认从**能拿到的最聪明的模型**起步，用 effort 档位往下调，而不是从便宜模型起步往上爬。理由不是性能而是两笔账：一是「每任务成本对更聪明的模型往往更低，哪怕每 token 更贵」，因为回合数和思考时间更少；二是一条比较少见的工程理由——**「从小模型起步会让你更难区分是模型失败还是你的配置失败」**。

## 为什么值得看（钩子）

官方亲手把自己两年来教用户写的提示词纪律推翻了 80%，还把 Claude Code 系统提示词里那段「默认不写注释、绝不写多段 docstring」的原文贴出来当反面教材——这是极少见的、供应商自曝「我们过去让你做的事现在拖后腿」。第 2 篇的钩子只有一个数字：便宜模型配个贵顾问，就能拿到贵模型 90% 的分、63% 的价。

## 关键细节 / 引述

**第 1 篇 · 唯一的数字与它的分量**
- 「We removed over 80% of Claude Code's system prompt for models like Claude Opus 5 and Claude Fable 5 with no measurable loss on our coding evaluations.」——全文**仅此一个数字**，无 token 数、无长度上限、无比例阈值。
- 诊断工具是真发了：新命令 `claude doctor`，在 Claude Code 里敲 `/doctor`，用途是「rightsize your skills, and CLAUDE.md files」（帮你把 skills 和 CLAUDE.md 削到合适大小）。

**第 1 篇 · 「Unhobbling Claude」（松绑）的证据链**
- 他们读自家内部使用记录，发现单次请求里就有互相打架的指令：系统提示词说「leave documentation as appropriate」，skill 又说「DO NOT add comments」。
- 关键机制描述：Claude 一般还是能猜对用户意图，「但 Claude 必须在这些重叠和冲突的信息上更仔细地思考，然后才能决定做什么」——即**矛盾指令的代价是烧推理预算，不是直接做错**。
- 「这些约束曾经是避免最坏情况所必需的，但我们后来发现可以删掉其中很多条，让模型改用上下文和判断力。」

**第 1 篇 · 六条「Then / Now」（原文对照最有价值的是第 1、2、4 条）**
1. **给规则 → 让它自己判断**。旧系统提示词原文：「In code: default to writing no comments. Never write multi-paragraph docstrings or multi-line comment blocks — one short line max. Don't create planning, decision, or analysis documents unless the user asks for them — work from conversation context, not intermediate files.」新系统提示词原文：「Write code that reads like the surrounding code: match its comment density, naming, and idiom.」理由：「对旧模型来说，没有这些护栏，Claude 写的注释在很多情况下会是错的，我们只能接受这个取舍。但更新的模型判断力更好。」
2. **给示例 → 设计接口**。「工具使用的第一原则曾经是给 Claude 示例。用我们最新的模型，我们发现给示例实际上把它们限制在某个探索空间里。」替代做法是让工具参数本身更有表达力——举的例子是 Todo 工具把 status 做成 `pending / in_progress / completed` 枚举，「就在暗示 Claude 该怎么用」，再加一条「保持只有一项 in_progress」来定义期望行为。
3. **全塞前面 → 渐进披露**。他们把 verification 和 code review 从系统提示词里搬进独立 skill。工具也一样：部分工具是 **deferred loading（延迟加载）**，agent 必须先用 **ToolSearch** 搜出完整定义才能用，「这让我们能挂更多工具（比如 Task 系列工具），而它们在被用到之前不占上下文」。顺手拆的迷思：CLAUDE.md 不该是「所有已知实践的中央仓库」，应该是「一棵能在恰当时机被加载的文件树」。
4. **重复强调 → 工具描述从简**。「更早的 Claude 模型有时需要重复指令，或者更倾向于听上下文窗口末尾而不是开头的指令。」——所以过去系统提示词里会跟工具描述里各写一遍。现在删掉重复，工具用法只写在工具描述里。（这条其实是全文最实在的一句模型代际差异声明：**位置偏见 / 重复冗余这两个老毛病，官方认为在 5 代上可以不管了**。）
5. **CLAUDE.md 当记忆 → 自动记忆**。过去教用户按 `#` 热键写进 CLAUDE.md，「现在 Claude 会自动保存与工作和与你相关的记忆」。
6. **简单 spec → 富引用**。除 markdown 计划外，可以引用 HTML artifact；spec 可以是「一套详细的测试套件，或者另一个代码库里一个待移植的函数」；rubric（评分表）可以配「动态工作流 + 起 verifier agent」来校验你在某个领域的品味（原文举例：什么才算好的 API 设计）。

**第 1 篇 · 落地建议（这部分是通用的，无 5 代特异性）**
- CLAUDE.md：「保持轻量，简单说明这个 repo 是干嘛的，把大部分 token 花在代码库里的坑上」（原文举例：类型全塞在一个巨型文件里）。「避免陈述 Claude 看一眼文件系统或 repo 就该知道的『显而易见』的事。」
- Skills：当轻量指南用，「除了极重要的领域，避免把它们写得过度约束」；长 skill 拆成多文件。
- References：优先给代码形式的引用——「一个设计的 HTML mockup，通常比对这个设计的文字描述或者一张截图产生更好的结果」。
- 系统提示词：Claude Code 用户基本改不到，但「如果你在建自己的 agent harness，这里是你该花大量时间的地方」。
- 文末指路另一篇《Fable field guide》讲针对更强模型的具体提示词写法。

**第 2 篇 · 值得摘的只有三处**
- **advisor 策略（唯一硬数字）**：定义是「让更快、更便宜的 worker 模型去调用更聪明的模型，来检查它的计划、评估它的工作」，「executor 模型只在需要时被指点」。数字原文：「on SWE-bench Pro Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's score at 63% of the price of using Fable 5 for the whole task.」（SWE-bench Pro 上，Sonnet 5 配 Fable 5 顾问，得分在 Fable 5 的 10% 以内，价钱是全程用 Fable 5 的 63%。）
- **Opus 与 Fable 怎么选（官方第一次正面回答，和 group-1 的 Opus 5 定位直接对得上）**：「在真实场景里，Fable 这类更大的模型往往更有智慧、创造力和写作能力，尽管跑分与 Opus 这类模型相近。」经验法则原文：「如果你的评测或内部测试显示 Opus 在某些任务上吃力，那答案就是 Fable。如果 Opus 已经过了质量线，那它的速度和价格档位可能让它成为更好的选择。」
- **基准饱和**：Anthropic 说 Opus、Fable 这类强模型「几乎能解出测试里的所有题目（通常称为饱和）」，所以建议改用从生产环境里挑出来的自定义 eval——「特别是那些你现有工具搞不定的难任务」。

**第 2 篇 · 家族口径与四问（产品文档腔，备查）**
- Mythos / Fable 是**同一个底层模型的两种打包**：Mythos 给做双用途网络安全与生物学工作的受信任组织，Fable 加了额外安全措施供公众使用，「两者都要求有限数据保留才能安全使用」。Mythos 只对 **Project Glasswing** 项下的组织开放。
- Opus =「面向推理密集型企业任务的强力模型档」，官方称在 **GDPval-AA**（知识工作）和 **Terminal-Bench 2.1**（agentic coding）上「稳定位居领先模型之列」（Anthropic 自述，未给具体分数）。Sonnet =「日常任务的多面手」，明确点名适合「多 agent 编排里的高并发子 agent」。Haiku = 最便宜最快，面向高频负载。
- 反垂直行业立场：「我们的模型档不专精某一类工作。我们不会推荐一个模型档做金融、另一个做科学。」
- 选型四问原文：How hard is this task? / What are the latency needs?（高频面客场景「Sonnet 往往是最佳选择」）/ What are the access constraints? / What are the unit economics?
- **注意**：文中那张能力-成本曲线图带官方免责声明「Curves are illustrative and not plotted from benchmark data.」（曲线为示意，非基准数据绘制）。全文**无定价数字、无上下文窗口、无延迟指标、无跑分**。

## 用户点名的事实问题：第 1 篇和 Opus 5 的关联有多大

**结论：关联是真的，但比标题许诺的薄。定性为「一篇由 Opus 5 触发、有一个真数字支撑、但操作指导只有『删』一个字的经验帖」——不是纯挂名，也远够不上「5 代模型上下文喂养手册」。**

先给可核的量：正文约 9800 字符里，「Opus 5」出现 **1 次**、「Fable 5」出现 **1 次**、「Claude 5」出现 **1 次**；**Sonnet 5、Haiku、4.8 一次都没出现**；全文实质数字只有 **80%** 一个。

**算「真·5 代特异」的，是六条里的三条**——判据是：这条明确声称「旧模型不行 / 新模型行」，删掉模型代际这个前提这条就不成立。

1. **删注释规则那条（最具体）**。它把 Claude Code 系统提示词的**新旧原文都贴了出来**，可以逐字对照：旧的是硬规则「默认不写注释、绝不写多段 docstring、最多一行」，新的是软判据「写出读起来像周围代码的代码：匹配它的注释密度、命名和惯用法」。而且给了明确的代际理由——旧模型没护栏「写的注释在很多情况下会是错的，我们只能接受这个取舍」。这是全文唯一一个能让读者照着改自己文件的**可执行样例**。
2. **「示例现在有害」那条（最反直觉）**。原文限定语很清楚：「用我们最新的模型，我们发现给示例实际上把它们限制在某个探索空间里」，并且明说这推翻的是「工具使用的第一原则」。改法也具体：不写示例，改把语义压进参数设计（Todo 工具的三值枚举 + 「只保持一项 in_progress」）。
3. **「不用再重复了」那条（技术含量最高）**。原文点名了旧模型的两个具体失效模式：「更早的 Claude 模型有时需要重复指令，或者更倾向于听上下文窗口末尾而不是开头的指令。」等于官方声明**位置偏见（末尾权重高）在 5 代上不必再靠冗余对冲**，因此系统提示词与工具描述的双写可以删。这是唯一一条真正指向模型内部行为变化的说法。

**剩下三条其实是产品功能公告，换成 4 代模型也照样成立**：渐进披露 / ToolSearch 延迟加载是 harness 设计，自动记忆是 Claude Code 的新功能，富引用（HTML artifact、rubric、verifier agent）是 artifacts 功能上线的副产品。后半程「Applying this to your context」整节（系统提示词 / CLAUDE.md / Skills / References 各写一段）是通用建议，两年前发也不违和。

**最关键的缺口**：这篇**没有给出任何用户点名想要的那类阈值**——上下文该放多长、CLAUDE.md 上限多少 token、什么该放什么不该放的判据、哪个模型配哪种活，一条都没有。全文的操作指令归结为一个动作：删；判据归结为一句话：「先前为防最坏情况加的约束，现在可以交给模型判断」。想量化「删到什么程度」，官方给的答案是跑 `/doctor` 让工具替你决定。

所以：**紧密程度打七折**。头条数字确实是 Opus 5 / Fable 5 上实测出来的、同日发布的，不是蹭热度；但把它当成「Opus 5 使用说明书」会失望——它是一篇「我们发现旧提示词纪律过时了」的复盘，Opus 5 是触发它的原因，不是它的分析对象。

## 与近期的关系

**有明确重复风险，需定牌处理。** 07-23 收过银牌「Anthropic：好的 agent harness 靠做减法」（Anthropic 四月旧文 harnessing-claudes-intelligence），当时记的核心是「harness 里每条假设都会随模型升级而过时，应该反复问『我们能停止做什么』」。今天这篇是**同一个论点**，只是换了阵地（从 harness 换到提示词 / CLAUDE.md / skills）。

不算炒冷饭的理由有三条，写手若收录应当把差异点写明：① 三天前那篇是四月旧文，今天这篇是 07-24 新发、且是**为 Opus 5 写的**；② 旧文的数字是 Opus 4.6 在 BrowseComp 上 45.3→61.6，今天的数字是**系统提示词删掉 80% 无损**，量级和性质都不同；③ 今天这篇给了**新旧系统提示词原文对照**和一条明确的反主流断言（示例有害），旧文没有。

另外两条关联：文中提到的 verification skill 化，正对应 07-23 已收的「把人肉复查写成 skill 让 Claude 能自动跑」（claude.com 07-22 那篇）；第 2 篇的 Opus vs Fable 经验法则，与 group-1 从 System Card 挖出的「官方自陈 Opus 5 不比 Fable 5 更强、定价却只有一半」是同一件事的两个口径，**建议交叉引用而不是各写一条**。
