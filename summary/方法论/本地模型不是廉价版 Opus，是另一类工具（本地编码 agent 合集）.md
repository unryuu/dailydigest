# 本地模型不是廉价版 Opus，是另一类工具（本地编码 agent 合集）

- 日期：2026-06-17 / 2026-06-18 / 2026-06-27
- 来源：https://blog.alexellis.io/local-ai-is-not-opus/（Alex Ellis，判断框架 + 查少报 license 案例，主文）；https://magazine.sebastianraschka.com/p/using-local-coding-agents（Raschka，同一模型换 harness 差异大、token 由 harness 决定）；https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/（Vicki Boykis 实测）
- 主题：八、效率工具与本地模型

## 这是什么

**2026-06-18（Alex Ellis，主文）**：接着「本地模型真能用了」，Alex Ellis（HN 341）把问题往前推了一步。大家都在问「本地模型啥时候追平 Opus」，他说这问错了，它根本不在同一条赛道。

Qwen 3.6 27B 在 SWE-Bench 上 77.2% vs Opus 88.6%，「只差 12%」听着快追上了，可这 12% 恰恰卡在生死线上：能不能放手让它自己干 10 分钟。Claude 能可靠无人值守跑 5–15 分钟，Qwen 一遇开放长任务就进死循环，让它提建议，它能把同 5 条来回重复 12 遍。

所以他给本地模型的定位是：需要全程盯着、只干有边界活儿的专用工具，「就像回火中的刀刃，你不会走开不管」。但它有超能力，比如飞快读懂并解释代码库（哪怕自己写不出来）、在隐私敏感或气隙环境里啃数据。他就靠本地模型分析客户遥测，揪出某客户一年少报了 4–5 倍 license，「光追回的收入就把这张 1.2 万美元的显卡赚回来了」。

三个真驱动也不只是省钱：数据主权、厂商风险（他点名 Anthropic 给非美区突然下架 Fable 5），还有电费固定带来的成本可预测。

**2026-06-27（Raschka）**：Sebastian Raschka（Ahead of AI，2 到 4 周才更一次的高权重作者）当天发了篇手把手教程，讲怎么用开源权重模型在本地跑编码 agent，替掉 Claude Code、Codex 这种云端订阅。配方给得很全：主推 Qwen3.6 35B-A3B 这档新的 MoE 模型（约 22 GB，要 30 到 40 GB 内存），用 Ollama 起服务，在一台 Mac Mini M4 或者 DGX Spark 上就能跑，速度约 40 token 每秒，差不多等于 GPT-5.5 开高推理。他的判断很实在：30 到 35B 这档开源模型对很多任务已经真够用，但他也老实说，GPT-5.5 和 Opus 4.8 目前还是比能在 Mac 上跑的小开源模型更强，自己日常主力其实还是 Codex 加 Claude Code。

真正的彩蛋不是「能在本地跑」，而是他跑出来的两个出乎意料的实测结论。一是同一个 Qwen3.6 模型，套在对手 OpenAI 的 Codex 上，居然比套在为它量身做的「原生」Qwen-Code 上表现还好。二是 token 烧得多不多，主要由 harness 决定，不由模型决定：Claude Code 平均烧的 token 远多于 Codex，有一次跑灌进去约 57.8 万输入 token、只产出 4.5k，活儿还没干得更好，原因是它每一轮都把一大堆上下文反复喂回模型。一句话，你以为自己在挑模型，其实更多是在挑 harness。

**2026-06-17（Vicki Boykis）**：在 2022 款 64GB M2 Mac 上用 Gemma-4-26b 跑 agentic 编码循环，自评达到「前沿模型约 75%」；llama.cpp 作者 Georgi Gerganov 在 HN 背书：过去一个半月几乎天天用 Qwen3.6-27B 处理 ggml-org 日常杂活。

## 可以怎么用

- 别问「本地模型能不能追平旗舰模型」，改问「它能不能无人值守跑长任务」——这才是本地模型和云端旗舰的真实分界线，据此决定哪些活儿敢放手交给它。
- 把本地模型定位成「需要全程盯着、只干边界清晰的活」的专用工具，比如读代码库、解释逻辑、跑隐私敏感数据分析，而不是指望它像 Claude 一样长时间自主推进。
- 同一个模型换个 harness（比如 Codex vs Qwen-Code），表现和 token 消耗可能差异巨大——排查自己 agent 工作流「为什么这么烧 token / 效果不好」时，先怀疑 harness 而不是急着换模型。
- 除了省钱，数据主权、厂商风险（担心某天被突然下架/限流）、电费可预测这几条也是选本地模型的正当理由，不是只有「便宜」这一个维度。
