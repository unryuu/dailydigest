# Agent 的能力开始从「会生成」转向「会维护一个可验证的工作循环」

- 推荐强度: 中
- 档位线索: LoopArena 给出明确的严格成功率与成本数字，单独看有银牌线索；Code-as-World 的可执行世界表示有范式感，但本地材料只含摘要，缺少具体分项结果；综述更适合作为贯通框架。整组不够金，优先考虑 LoopArena 银牌或三篇合成无牌长文。
- 涉及文章: [Agentic Artifact Creation: Systems, Evaluation, Principles, and Opportunities](https://huggingface.co/papers/2608.28122) · Hugging Face Papers · 2026-08-28
- 涉及文章: [Code as Worlds: Agentic Discovery of Executable World Representations for Physical Reasoning](https://huggingface.co/papers/2608.27549) · Hugging Face Papers · 2026-08-27
- 涉及文章: [LoopArena: Benchmarking Models as Runtime Controllers for Loop Engineering](https://huggingface.co/papers/2608.28281) · Hugging Face Papers · 2026-08-28

## 核心主张

这组三篇把 Agent 的关键能力从一次性生成，推向一个共同结构：先维护可操作的中间状态，再采取行动，并用运行时反馈决定下一步修复什么。综述把这个结构概括为「操作表示＋构建策略＋运行时验证」；Code-as-World 用可执行代码表示物理世界，让 Agent 反复提出、运行、渲染和校验世界假设；LoopArena 则把写代码的 Worker 固定下来，单独测另一个 Controller 是否知道下一步该做什么、该验证什么以及何时停止。最硬的结果是，即使底层编码 Agent 已经很强，最好的完整任务严格成功率也只有 24.69％，说明可靠性瓶颈可能不只在模型会不会干活，还在控制循环会不会维护状态和验证结果。

## 为什么值得看（钩子）

三篇共同把「Agent 做出一个东西」拆成可观察、可归因的工程过程：失败究竟来自执行能力，还是来自上层循环相信了过期进度、漏掉验证或过早停机。这个角度比再报一个 Agent 跑分更接近真实生产环境里的调试问题。

## 关键细节 / 引述

- Agentic Artifact Creation 综述审查了截至 2026 年 8 月 20 日的 259 项工作，其中 230 个系统符合其定义，另有 29 个 Agent 式产物构建基准，覆盖六类产物。
- 综述把 Agent 式产物创建定义为有状态、受反馈驱动的构建过程：AI 实质性地创建或修改交付物，中间观察会改变后续行动；其三个组成部分是操作表示、构建策略和运行时验证。
- 综述提出一个反直觉风险：任务拆解虽然能降低局部复杂度，却会增加协调与重新组装的成本；如果学习型裁判与生成器共享偏好或盲点，它可能几乎没有提供独立证据。
- Code-as-World 不把像素当成世界本身，而是让 Agent 从文字或视频中提出可执行的世界假设，循环执行「提出、运行、渲染、验证、迭代修正」，用代码显式表示物体状态、物理参数和支配演化的动力学。
- Code-as-World 摘要称，其模型 Code-as-World-VL 在 QuantiPhy 上达到当前最佳成绩并超过领先闭源模型；但本地抓取只有论文页摘要，没有具体分数、模型名单、数据规模和消融实验，无法进一步核实优势幅度。
- LoopArena 固定执行代码任务的 Worker，只评估 Controller 在每轮之后如何读取结构化摘要、安排下一步工作或验证并决定是否停止。完整任务中最佳严格成功率为 24.69％；跨 Controller 的配对估算推理成本平均下降 64.4％，较便宜的 Type II 设置与完整任务在主要 Core 指标上的排序高度一致，Spearman 相关系数为 0.9747。

## 与近期的关系

重复风险中等。它与近期的长程 Agent、自我改进、技能和记忆主线相邻，但新增角度不是再说 Agent 能连续工作，而是把「生成器／Worker 的能力」和「控制循环的指导质量」拆开归因，并把可执行中间状态与运行时验证放到核心位置。LoopArena 的 24.69％严格成功率和低成本替代评测最有独立新闻价值；Code-as-World 的范式判断有新意，但因本地材料只有摘要，若写入日报应避免扩展实验细节；综述本身主要提供框架，单独成条容易显得泛。
