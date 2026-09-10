# 科研发现认证与 Agent 基准

- 推荐强度：中
- 档位线索：Discovery Certification Protocol 有明确协议机制和两组受控审计数据，可作为银牌候选；SWE-Bench Pro Verified 只宜降无牌或并入基准可信度话题；Φ-Bench 当前材料没有任务数、模型分数或成功率，建议降无牌，版面紧时可砍。
- 涉及文章：[Scores Alone Do Not Prove Discovery: The Discovery Certification Protocol for Auditing AI Research Agents](https://huggingface.co/papers/2609.09219) · arXiv（Hugging Face Papers 页面） · 2026-09-07
- 涉及文章：[SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents](https://huggingface.co/papers/2609.08149) · arXiv（Hugging Face Papers 页面） · 2026-09-08
- 涉及文章：[Φ-Bench: Can Large Language Models Engineer the Infrastructure That Powers Them?](https://huggingface.co/papers/2609.10226) · arXiv（Hugging Face Papers 页面） · 2026-09-09

## 核心主张

这组三篇真正贯通的不是「Agent 又刷新了什么能力」，而是研究者开始追问评测本身能否证明结果：科研 Agent 的分数不能自动等于发现，软件工程 Agent 的高分可能来自答案或隐藏评测信息泄漏，而基础设施工程 Agent 还缺少覆盖开放式、长周期任务的评测。三篇里最硬的是 Discovery Certification Protocol：它不再只给一个排行榜，而是要求用密封评测、替代路线恢复测试、对照审计和确定性验证器，把「有用结果」与「无法从既有信息轻易恢复」拆开验证。SWE-Bench Pro Verified 的增量主要是清洗旧 benchmark，Φ-Bench 的增量主要是扩展任务范围；就本地抓取到的摘要而言，两者都没有足够数字证明新的能力结论。

## 为什么值得看（钩子）

反直觉之处是，Agent 得出正确答案仍不足以证明它完成了发现；同样，排行榜分数高也可能是在利用评测漏洞。相比继续堆新分数，DCP 把「发现」改写成一套可以否决、复核和由程序重放的证据流程。

## 关键细节 / 引述

- DCP 的 Gate 1 先在密封评测上验证方法确有增益；Gate 2 给匹配 Agent 相同的注册起始信息和当时观察到的网页内容，但扣除目标研究历史，测试它能否独立恢复达到数值目标的方法。任何有效方法一旦恢复成功，就触发 Core veto，不能通过核心认证。
- DCP Core 要求对照充分、观察到的恢复次数为零，并为一次新注册实验给出有限样本恢复概率上界。可选 Gate 3 则从共享检查点出发，对比真实反馈与预先规定的中性反馈策略；Evidence 级别还要求独立的零效应校准和预注册效应阈值。
- 论文在 SQLite 优化和虚拟催化剂控制上做了两项完整受控审计，使用不同模型。摘要称两项审计各自在 96 次实验中观察到零次恢复，对应恢复概率上界为 0.0468。
- 两项配对研究都得到 30 次真实反馈恢复、零次中性反馈恢复，并通过各自 60 对的零效应研究。冻结证据交给一个不使用 LLM 的确定性验证器后，可以复现认证决定。
- SWE-Bench Pro Verified 指出原版评测的两类失真：金标准答案或隐藏评测信息泄漏使 Agent 能够 reward hacking；误导性问题描述和范围不当的测试则让任务本身失真。新版一边堵住主要泄漏渠道，一边只对有问题的实例做最小修正。
- SWE-Bench Pro Verified 的摘要只说「一些模型」在验证版上明显低于既有报告，没有给出具体模型、前后分数或排名变化。因此能确认旧榜可能高估真实软件工程能力，但不能从现有材料判断是否重排榜单。
- Φ-Bench 把范围从孤立 kernel、预定义算子和预设优化目标，扩展到基于真实代码仓库的开放式 LLM 基础设施工程；任务横跨局部 kernel 函数补全、长周期实现和端到端系统优化。现有摘要没有任务数量、具体模型、成功率或性能增益，只能确认它提出了新的 benchmark，不能确认模型已经能维护支撑自身运行的基础设施。

## 与近期的关系

DCP 与 09-09「调查 Agent 只找回约一半关键发现」有表面重合，都在质疑科研 Agent 的结果可信度；但昨天讲的是信息找回不完整，今天的实质增量是提出正式认证协议，用密封评测和恢复测试区分「正确结果」与「真正发现」，重复风险低至中。SWE-Bench Pro Verified 与 09-08「Agent 会写测试却不会拿测试找错」都属于软件工程 Agent 评测负面结论，重复风险中至高；它的新角度是 benchmark 泄漏、reward hacking 和任务质量，而不是 Agent 如何使用测试，但本地材料缺少前后分数，独立成条偏弱。Φ-Bench 换到了 LLM 基础设施工程，题材不直接重复前两日报道；不过它仍是「再造一个 Agent benchmark」的常见框架，且没有硬结果，内容新鲜度有限。
