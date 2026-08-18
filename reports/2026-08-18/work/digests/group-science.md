# 自动科研系统一边改进矩阵乘法，一边在百项真实研究任务上暴露失败

- 推荐强度：强
- 档位线索：三份材料合在一起有鲜明反差，也有硬数字支撑，至少够银；若本期需要一条代表 AI 科研前沿的主稿，可考虑冲金，但标题和正文必须持续说明这是三个不同项目，不能制造“同一个系统既成功又失败”的假象。
- 涉及文章：[Import AI 469：Science AI；RSI simulator；and Zuck's technological pessimism](https://importai.substack.com/p/import-ai-469-science-ai-rsi-simulator) · Import AI · 2026-08-17
- 涉及文章：[Improving the matrix multiplication exponent with modern optimization and AlphaEvolve](https://huggingface.co/papers/2608.16884) · Hugging Face Papers／DeepMind · 2026-08-17
- 涉及文章：[How Do Agents Fail on AutoResearch：End-to-End Diagnostic Evaluation on 100 Real-World Frontier Research Tasks](https://huggingface.co/papers/2608.14905) · Hugging Face Papers／Prentis AI · 2026-08-14

## 核心主张

AI 科研正在同时给出“能做出新结果”和“还不会可靠地做研究”两种证据，但它们来自三个不同项目。DeepMind 团队把现代优化、机器学习算法和 AlphaEvolve 用于组合损失分析，刷新了矩阵乘法指数的已知上界；Inherent 的 Faraday 则训练一个较小的监督模型来调度前沿模型，在论文缺失结果的复现任务上取得提升。另一项 AutoResearchEval 研究横跨完整科研生命周期检查八种 Harness—模型组合，发现反复出现的核心缺陷不是单项能力不足，而是 Agent 缺少检查、质疑并修正自身工作的“元认知循环”。

## 为什么值得看（钩子）

同一天的材料把 AI 科研最关键的张力摆在一起：系统已经能参与改进一个长期数学上界，也能通过训练提升论文复现表现；但一旦把任务扩展为从构思到评审的完整科研流程，它们仍会在不同模型和脚手架上重复犯不会自查的错误。

## 关键细节 / 引述

- 矩阵乘法论文先重写组合损失分析中的核心优化问题，使其可在比过去更大的设置中求解，再引入机器学习优化算法，并用 AlphaEvolve 继续改进；最终把矩阵乘法指数上界从此前的 ω＜2.371339 推进到 ω＜2.371177。
- Import AI 介绍的 Faraday 是一个建立在 Qwen-3.6-27B 之上的 270 亿参数模型，以 OpenAI Codex 作为底层编码工具；它不是 AlphaEvolve，也不是 AutoResearchEval 中某一种被测系统。
- Faraday 的训练与评估集 Replica 取自 1990—2026 年间的 100 篇机器学习和 AI for Science 论文，通过删去关键图表或结果形成 310 个复现任务；系统以任务专用评分标准和 Codex Judge 的奖励信号进行改进版 GRPO 训练。
- 据项目方的评分标准，Faraday＋Codex 在 73％的分布内机器学习任务、60％的留出 AI for Science 任务上超过标准 Opus 4.8 和 GPT-5.5。Import AI 将这解释为系统开始显露研究“品味”的迹象，但相关数字依赖其 rubric-based judge，写作时不宜外推成普遍科研能力。
- AutoResearchEval 使用来自七个科学领域的 100 个真实前沿科研任务，覆盖构思、检索、执行、分析、写作和评审全过程；研究者评估八种 Harness—模型组合，共得到 800 条 Agent 轨迹，并归纳出 45 种基于实证的失败模式。
- AutoResearchEval 作者把共同瓶颈概括为缺少“元认知循环”：系统不能把自己产出的内容与找到的证据相互核对，发现站不住脚时主动修订，也不会质疑自己选择的研究路径。相同模式出现在全部八种组合、包括最强模型中，因此论文把缺陷定位到模型层面；但作者也明确表示，编排层干预能否弥补这一点仍是该研究没有测试的开放问题。

## 与近期的关系

仅依据本组分配材料，无法核定它与往期日报的具体重复程度。题材上，它承接“科研 Agent／Agent Harness／递归自我改进”的热门主线，存在概念重复风险；真正的新事实是矩阵乘法指数的新上界，以及 AutoResearchEval 的 100 项任务、800 条轨迹、45 类失败和“元认知循环”诊断。若近期已密集报道 Harness，建议正文把重心放在这两个可验证的新结果上，Faraday 作为连接成功与失败两端的补充证据。
