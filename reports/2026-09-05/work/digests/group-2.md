# AI 形式化数学：从证明到可机检

- 推荐强度：强
- 档位线索：Anthropic 这篇有明确结果、可核验数字和方法细节，适合高档候选；电路板文章正文两次抓取均失败，不能据此定牌，建议标作抓取失败或暂不收录。
- 涉及文章：[Formalizing Fermat’s Last Theorem](https://www.anthropic.com/research/formalizing-fermats-last-theorem) · Anthropic · 2026 年 9 月 4 日
- 涉及文章：[Can AI Design Circuit Boards Yet?](https://eebench.org/blog/can-ai-design-circuit-boards-yet) · EEBench · 抓取失败（HTTP 502；浏览器兜底同样失败）

## 核心主张
Anthropic 称，Claude 在 11 天、基本自主工作的情况下，用 Lean 完成了费马大定理（FLT）首个端到端、计算机检查的形式化证明。这里的新意不是重新发现数学证明，而是把已有的 Wiles 路线改写成 Lean 能逐步检查的形式，从而把原本可能需要多年人工核验的工作压缩到可机检的流程中。项目成功的关键不是单个模型“灵光一现”，而是 Prove2Me 的定理有向无环图、并行协作、编译加速和自然语言定理检索等脚手架。

## 为什么值得看（钩子）
这是一条很具体的“AI 做数学”进展：它把可信度问题从“模型说自己证明了”推进到 Lean 检查通过，并且暴露了大规模多代理协作何时会失效、怎样靠项目状态管理重新跑通。对日报读者来说，最反直觉的点是成果的核心价值在验证与审稿减负，而不是又一个未经人类理解的数学猜想。

## 关键细节 / 引述
- Claude 用 11 天完成 FLT 形式化；过程中写出约 1300 万行 Lean，证明了 30,300 个中间定理，最终证明使用其中 29,500 个。成品规模超过 Mathlib（该证明所依赖的主要社区库）的 5 倍。
- 证明沿用 Darmon、Diamond、Taylor 对 Wiles 证明的简化路线；人的输入主要是偶尔给出高层级优先级，例如“Jacobian as a scheme sounds high priority”，而不是逐步写证明。
- 初期代理很快丢失项目状态、协作失效；失败尝试仍贡献了最终证明约 7％ 的非样板代码。转用 Prove2Me 后，定理 DAG 帮代理决定下一步，独立存放定理陈述和证明以加速 Lean 编译，并通过自然语言描述支持搜索复用。
- 整个多代理项目消耗约 60 亿输出 token，使用的是一个大致相当于 Claude Fable 5.1 的内部通用研究模型；最终 Lean 检查通过，只使用 Lean 的三个标准公理，另有 comparator 核对定理陈述与 Mathlib 的 FLT 陈述一致。
- Anthropic 研究者称，形式化 FLT 原本预计需要多年，社区用于描述初始阶段的 blueprint 就有 86 页。Kevin Buzzard 评价说，这说明现代数学文献的自动形式化向前迈了一大步，也可能帮助发现现有数学语料的错误、减轻审稿人的核验负担。
- 同一套 Prove2Me 协作方式在一个小实验中用三份个人 Claude Max 订阅，于三天内完成了 Vinogradov 三素数定理相关 Hardy–Littlewood 圆法应用的形式化；Anthropic 据此认为，合适脚手架下，消费级订阅也可能协作形式化重要定理。

## 与近期的关系
本文明确把 FLT 与近期“AI 驱动的黎曼猜想工作”区分开：后者强调产生新数学，这次工作的创新点是验证和形式化。它也延续 Anthropic 关于 Claude 数学能力和 AI 辅助研究的叙事，但这次给出了 Lean 工件、规模数字和外部数学家审阅，因而不是泛泛的能力宣称。除上述 Anthropic 文章外，本组的 EEBench 电路板文章正文抓取失败，无法判断是否存在重复或互补关系。
