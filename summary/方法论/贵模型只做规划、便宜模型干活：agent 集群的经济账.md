# 贵模型只做规划、便宜模型干活：agent 集群的经济账

- 日期：2026-07-05 / 2026-07-21 / 2026-07-25 / 2026-07-28
- 来源：https://cursor.com/blog/agent-swarm-model-economics（Cursor，主文，$1339 vs $10565）；https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/（Simon 让 Fable 自主派活给 sonnet/haiku）；https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case（Sonnet 配 Fable 当顾问，省四成）；https://www.lesswrong.com/posts/jLkRCK35ri2btEHMF/untrusted-advice-for-ai-control-short-strong-advice（强模型每步只发 16 字符建议）
- 主题：二、多 agent 分工与成本

## 这是什么

**2026-07-05**：主会话 141.02 美元，几个 review 子 agent 各花几美元。Fable 跑了 37 个 prompt、34 次 commit，做了事务语义重构，还修了会让连接状态被污染、进而丢数据的 bug。Simon 觉得 release notes 比他自己写得好，这种写作无聊、可预测、要求准确，正适合外包给 agent。这次他让 Fable 自己做调度，把实现派给 sonnet、把琐碎机械活派给 haiku。

**2026-07-21**：贵模型只做规划，便宜模型干活最划算。规划者只吃约 10% 的 token，却占了 66% 的成本。最省的组合花 $1339 干完的活，全用顶配模型要 $10565。产出代码还从 6.4 万行缩到 1 万行。

**2026-07-25**：官方给了个便宜办法：SWE-bench Pro 上让 Sonnet 5 配合 Fable 5 当顾问，分数差距不到 10%，价钱只要六成。

**2026-07-28**：强模型给可信的弱模型提建议，每步只能发 16 个字符，弱模型负责具体执行。在 SWE-bench 上，弥补了弱模型相较于强模型，大约三分之二的能力落差。强模型用 Claude Sonnet 4.6，弱模型用 Gemini 3.1 Flash Lite 和 gpt-oss-120b。

## 细节（来自精读摘要）

**07-25（claude models explained，官方选型建议）**

advisor 策略（唯一硬数字）：定义是「让更快、更便宜的 worker 模型去调用更聪明的模型，来检查它的计划、评估它的工作」，「executor 模型只在需要时被指点」。数字原文：「on SWE-bench Pro Sonnet 5 with a Fable 5 advisor is within 10% of Fable 5's score at 63% of the price of using Fable 5 for the whole task.」（Sonnet 5 配 Fable 5 顾问，得分在 Fable 5 的 10% 以内，价钱是全程用 Fable 5 的 63%。）

官方给的模型怎么选：默认从能拿到的最聪明的模型起步，用 effort 档位往下调，而不是从便宜模型起步往上爬。理由是两笔账：一是「每任务成本对更聪明的模型往往更低，哪怕每 token 更贵」，因为回合数和思考时间更少；二是「从小模型起步会让你更难区分是模型失败还是你的配置失败」。经验法则原文：「如果你的评测或内部测试显示 Opus 在某些任务上吃力，那答案就是 Fable。如果 Opus 已经过了质量线，那它的速度和价格档位可能让它成为更好的选择。」

基准饱和提醒：Anthropic 说 Opus、Fable 这类强模型「几乎能解出测试里的所有题目」，建议改用从生产环境里挑出来的自定义 eval，特别是现有工具搞不定的难任务。

**07-28（untrusted advice，强模型每步只发 16 字符）**

协议怎么跑：受信任的弱模型 T 执行所有动作，不受信任的强模型 U 只能在每一步之前，以极短的一条 user message 给 T 发提示；T 被要求无条件服从提示。U 另有权力：可以拦下 T 想提交的动作，但 T 只被告知「你被拦了」。

任务与模型：不受信任的强模型 U 全程用 Claude Sonnet 4.6；受信任的弱模型 T 分别用 Gemini 3.1 Flash Lite 和 gpt-oss-120b；任务是 SWE-bench Verified 和 BashArena，各 200 题。

单干分数对照：

| | Gemini 3.1 Flash Lite | gpt-oss-120b | Claude Sonnet 4.6 |
|---|---|---|---|
| SWE-bench Verified | 0.490 | 0.492 | 0.763 |
| BashArena | 0.436 | 0.430 | 0.712 |

实测每条提示上限测过 4 / 8 / 16 / 32 字符（另有不限长度对照），主打数据点是 16 字符那一档：SWE-bench 上补回约 67% 的差距，全任务加起来只用了约 320 个字符。几条真实的短提示：U 想让 T 用 curl 测服务器，发了「curl」（4 字符）；想让 T 删文件第 97 行，发了「del L97」（7 字符）。

与 Anthropic advisor 策略的关系（原文自己点的）：Anthropic 四月发过 advisor 策略博文——弱模型调工具向强模型问建议，现已是 Claude Code 里的工具；差别是 Anthropic 不加任何长度限制，且是执行者主动求助而非顾问主动发指令，动机是省钱不是安全。这篇把同一个「弱模型执行、强模型只给指点」的结构，推到了「16 个字符」的极端，当作安全机制而非省钱手段来测试。

作者自陈局限：全文没有跑任何安全实验，「暂时把安全性的实证评估留给未来工作」；只在提示极少的一端主张高安全性，一旦信息预算放开，协议就退化成普通的 trusted monitoring。

## 可以怎么用

- 设计多 agent/多模型协作流程时，默认思路可以是「贵模型定方向、便宜模型干活」：让强模型负责规划、拆解、审查这类占小头 token 但决定质量的环节，把执行这类大头 token 的重复劳动交给便宜模型，Cursor 的数字（规划只吃 10% token 却占 66% 成本）说明省钱的关键点在换掉执行模型，不是换掉规划模型。
- 如果流程里已经在用强模型全程跑，可以先试试「强模型当顾问、弱模型执行」的架构：官方数字显示能拿到接近满分的表现，只花六成左右的钱，值得作为默认省钱选项而不是特例。
- 让主 agent（如 Fable）自己判断把哪些子任务派给更便宜的模型（如 sonnet/haiku），比人工提前分派更省心，尤其适合「无聊、可预测、要求准确」这类任务（比如写发布说明）。
- 强模型的指点不必啰嗦：如果只是要给执行者一个方向性提示，一两句极短的话可能比长篇指导更有效也更省钱，但要留意这类「窄通道协作」目前还缺乏安全性的实证检验，用在真正需要审计的场景时别只看效率数字。
