# OpenAI 自研 Jalapeño 推理芯片亮出首批结果

- 推荐强度: 强
- 档位线索: 够银牌，也有金牌级的技术冲击力；但公开成绩仍是工程样片上的特定推理负载，没有 AgentX 长上下文、多轮测试，不能写成「全面胜过 Blackwell」。
- 涉及文章: [OpenAI Jalapeño: Better Than Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) · SemiAnalysis · 2026 年 8 月 25 日

## 核心主张

OpenAI 从 2024 年中开始组队，用约 16 个月完成了面向大模型推理的自研 ASIC「Jalapeño」流片；SemiAnalysis 在 OpenAI 实验室现场核验了 InferenceX 运行，认为这颗芯片在所测的 DeepSeek R1、Kimi K2.5 和 GPT-OSS 等开源模型上，同时展现了很强的低延迟和高吞吐能力。最硬的结论不是「峰值算力全面超越英伟达」，而是在这批单轮 8k1k 推理测试里，Jalapeño 在没用多 Token 预测、推测解码和预填充—解码分离的情况下，单位数据中心功耗的输出 Token 吞吐仍压过文中对比的 Blackwell，甚至高于英伟达与 CoreWeave 七月公布的 Vera Rubin 多 Token 预测结果。

SemiAnalysis 认为，优势来自围绕推理软硬件协同设计：简化内存与片上网络、尽量不搬运 KV Cache 和权重，再用 Codex 快速编写、调优特定内核。这说明 OpenAI 的目标是把有限电力尽量换成 Token，而不是只把单颗芯片做得便宜。

## 为什么值得看（钩子）

第一代自研芯片通常难以直接打到行业前排，Jalapeño 却在工程样片阶段就跑出了有竞争力的能效。更反直觉的是，OpenAI 没把它做成只服务自家模型的窄用途芯片，而是试图用通用推理硬件加上 AI 生成的特定内核，绕开「通用编译器必须先成熟」的传统路线。

## 关键细节 / 引述

- SemiAnalysis 使用的头条指标是「每个全口径公用设施兆瓦的 Token 吞吐」，本质上是每焦耳产出多少 Token。文中称，Jalapeño 在几乎所有所测场景中的单位功耗表现都胜过 Blackwell，且同时覆盖低延迟和高吞吐区间。
- 在 DeepSeek R1 上，Jalapeño 以单用户并发度达到每个用户每秒超过 700 Token；文中还称，Kimi K2.5 和 GPT-OSS 的某些低并发运行约为每个用户每秒 1400 Token。这些结果都没有使用多 Token 预测、推测解码或预填充—解码分离，GSM8k 评测结果与英伟达芯片相当。
- 对 Vera Rubin 的比较里，Jalapeño 的单 Token 预测输出吞吐／兆瓦高于英伟达和 CoreWeave 七月公布的 Rubin 多 Token 预测数据；但每美元输出 Token 数基本持平。文章判断，如果 Jalapeño 未来补上推测解码，成本仍有下降空间；这是预期，不是已经实现的结果。
- 全部公布成绩来自 A0 步进工程样片。已在晶圆厂的 B0 步进据称可再提高约 25％ 的单位功耗性能；B0 单个计算裸片为 13.4 PFLOPs MXFP4，标称功耗 700W，对比 Rubin 单个计算裸片的 17.5 PFLOPs 稠密 NVFP4 和 900W 至 1150W。Jalapeño 使用 HBM4，每封装内存带宽为 15.4TB/s。
- SemiAnalysis 明确列出了三层限制：所有数字由 OpenAI 提供，作者只在实验室核验了部分 InferenceX 运行；尚未完整跑 InferenceX，更没有更接近真实生产的 AgentX 长上下文、多轮成绩；所测 8k1k 是较容易调优的单轮负载，模型也不是当时最前沿的最大开源模型。
- 文章自己认为拿 Jalapeño 和 Blackwell 比较「不完整且不公平」：两者不同代，同样使用 HBM4 的 Vera Rubin 才是更合适的对手。Rubin 已开始向客户出货，Jalapeño 目前仍只有工程样片，计划 2027 年逐步量产，且大部分产量排在年底。

## 与近期的关系

与 8 月 25 日成品没有直接重复。昨日的「恶意模型可能借推理引擎控制服务器」讲的是 vLLM 等推理软件的攻击面，本组是 OpenAI 自研推理芯片的能效、架构和软硬件协同，只在「推理基础设施」大主题上相邻，属于新事件和新角度。
