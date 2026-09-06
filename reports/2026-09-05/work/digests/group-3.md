# 从可生成到可验收：开放模型把训练与评测做成工程闭环

- 推荐强度：强
- 档位线索：银牌。三篇分别覆盖 Agent 训练、视频物理验证和开放图像生成，硬数字与公开代码／权重足够支撑一条技术主线；但它们不是同一项目，不能写成已经统一的标准或共同产品。
- 涉及文章：[DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training](https://huggingface.co/papers/2609.04094) · IBM Research · 2026-09-03；[VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement](https://huggingface.co/papers/2609.03153) · 论文页面 · 2026-09-02；[LLaDA-Image: Building Strong Image Generators with Fully Open Training Recipes](https://huggingface.co/papers/2609.03796) · inclusionAI · 2026-09-03

## 核心主张

这组三篇论文都在把“模型看起来会做”拆成可操作、可检查的中间环节：DRACO 用动态 rubric 将整条长轨迹的分数重新分配到具体步骤，且训练时不需要程序验证器；VeriPhy 先把提示编译成带类型的物理义务，再让冻结的专家产生带出处的证据，输出支持、反驳或未知三值结论；LLaDA-Image 则公开从图像预训练、优化器到蒸馏的完整配方，降低开放模型复现门槛。

它们共同反对单一总分或黑箱展示，但证据强度不同：DRACO 的 AppWorld／Tau-Bench 提升和 VeriPhy 的缺陷召回来自论文实验，LLaDA-Image 的 53.53／53.38 是作者在 Qwen-Image-Bench 上报告的结果，仍应按作者自报的开源模型成绩理解。

## 为什么值得看（钩子）

Agent 训练、视频物理可靠性和图像生成通常被分开讨论，这组三篇却分别把“奖励如何落到步骤”“结论如何回溯到证据”“模型如何被别人复现”摆到台面上。真正的新意不只是分数更高，而是能力、验收和复现实验开始一起成为产品竞争力。

## 关键细节 / 引述

- **DRACO 的训练信号。** 它动态生成 rubric，在每轮轨迹完成后评分，再把 rubric 判断闭式地重分配为 GRPO 的逐步 advantage，不引入额外训练的归因模块，也不使用 verifier。论文报告在 AppWorld 上比基础模型高 15.9 分、比使用稀疏真实奖励的 GRPO 高 5.3 分；在域外 Tau-Bench 上比基础模型高 5.3 分，即使没有 frontier judge 也超过真实奖励训练和其他 rubric 训练设置。
- **DRACO 的边界。** 作者回应质疑称，rubric generator 被提示去找 Agent 的短板，并在 rollout 组内合并标准；所有轨迹都通过的标准会被丢弃，所以静态 rubric 会饱和而动态 rubric 仍保持区分度。AppWorld 的最终成绩用官方 verifier 评估，但 verifier 没有参与训练奖励；作者明确说尚未在 WebArena 上训练或测试。
- **VeriPhy 的可审计验证。** 文本规划器在看到帧之前，把提示编译成带类型的物理义务和静态校验过的执行计划；执行时只调用声明范围内的冻结专家，包括分割与跟踪、计数、十一类轨迹物理测量、深度、OCR 和音频事件检测。每次动作都返回带 provenance 的证据记录，解析器把证据合成为 supported、contradicted 或 unknown，并表面化为 plausible、implausible 或 abstain。
- **VeriPhy 的实测增量。** 其基准包含 1,500 条人工标注的生成缺陷记录；149 个核心视频携带 304 条记录，VeriPhy 覆盖 228 条，使用同一批视频和主张的已发表问题分解评估器覆盖 164 条，单纯把同一主干端到端提示化则覆盖 222 条。论文强调，优势不在召回率本身，而在每个判断都保留了可追溯证据，可作为写回生成器的批评接口。
- **LLaDA-Image 的开放配方。** 这是从零训练的 6B Diffusion Transformer，配一个冻结的视觉语言模块，先做 image-only pre-training 与 mid-training；生成管线使用 220M 个样本，原文另称其中 98 个为真实图像。DiT 全程使用无参数 RMSNorm 和 Muon 优化器，并把模型蒸馏成 2–4 步的 LLaDA-Image-Turbo；作者同时发布模型权重、训练代码和详细配方。
- **LLaDA-Image 的成绩与形态。** 作者报告在 Qwen-Image-Bench 英文轨和中文轨分别得分 53.53、53.38，称其为两个开放源模型赛道的当时最高；50 步 Base 版和 4 步 Turbo 版都支持文生图、VQ 条件生成、参考图编辑以及中英文文字渲染。Hugging Face 作者说明还包括精细编辑与高写实生成，但这些能力仍应以作者展示和评测口径为准。

## 与近期的关系

DRACO 与 09-02 的“奖励漏洞／训练出 misaligned reward seeker”及 09-04 的“自动评分语境可能牵动对齐行为”属于同一奖励设计大背景，但它提出的是如何在没有 verifier 时把 rubric 分数分摊到长轨迹步骤，不能再泛写成 Agent 会钻评测漏洞。VeriPhy 承接 09-03 World Labs Atlas 的世界模型和 09-04 的 Principia 视频物理评测：Atlas 侧重生成、重建和仿真，VeriPhy 侧重把生成视频的物理缺陷逐条验证并留下证据；若当天另有 Principia 条目，应突出“可审计义务与证据链”，避免重复“视频模型不懂牛顿力学”。LLaDA-Image 与 09-03 Atlas 的扩散／世界模型方向有架构上的交集，也可能与近期开放模型报道同题，但新信息是完整开放训练配方、6B 规模和 2–4 步蒸馏，不要再写成泛泛的“又一个图像生成模型”。
