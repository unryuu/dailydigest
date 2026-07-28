# Kimi K3 权重真发了

- 推荐强度: 强
- 档位线索: 够金。事实密度高、一手来源齐（技术报告＋权重页＋许可证原文），且能接住 07-26 预测市场那条和 07-27 被拦下的假消息，形成连续性。唯一要注意的是「K3 发布」本身在过去两周日报里已多次以侧面形式出现（0day、Windows XP demo、预测市场），本条的新东西是**权重落地＋许可证变严**，不是「K3 存在」。
- 涉及文章:
  - [moonshotai/Kimi-K3](https://simonwillison.net/2026/Jul/27/kimi-k3/) · Simon Willison · 2026-07-27
  - [Kimi K3: Open Frontier Intelligence](https://huggingface.co/papers/2607.24653) · Hugging Face Papers（arXiv 2607.24653）· 提交 07-27，HF 站上 07-28
  - [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) · Hugging Face 权重仓库 · 已读到，含完整 model card 与评测表
  - [Kimi K3 LICENSE 原文](https://huggingface.co/moonshotai/Kimi-K3/raw/main/LICENSE) · 逐条读完

## 核心主张

Moonshot 把 2.8T 总参的 K3 权重整个放了出来，1.56TB，是目前公开权重里体量最大的一档，官方在技术报告里直接自陈「整体表现仍落后于 Claude Fable 5 和 GPT-5.6 Sol，但在我们的评测套件里持续优于其他开放及专有模型」——罕见地把天花板和位次都写进摘要。真正的转折不在模型而在许可证：K2 那份「魔改 MIT」到 K3 已经不再自称 MIT，新增一条针对「模型即服务」生意的门槛条款，年营收超 2000 万美元的 MaaS 厂商必须先跟 Moonshot 单独签协议才能商用。开放权重的边界正在从「署名」挪到「分成谈判」。

## 为什么值得看（钩子）

派活时的假设是「沿用 K2 那份魔改 MIT，多加一段署名条款」——**这个假设不成立**，Simon 原文和许可证原文都显示 K3 已经不叫 MIT 了，新增的是商业授权门槛而非署名门槛，而且触发线比署名条款低一个数量级。前一天日报的 scout 刚以「HF 上没有 K3 仓库」为由拦下一条假消息，一天后它成真了。

## 关键细节 / 引述

- **规模数字（以技术报告摘要与 model card 为准，两处一致）**：总参 2.8T，激活 104B，上下文 1,048,576 token（1M），原生视觉。MoE 共 896 个路由专家、每 token 激活 16 个，另有 2 个共享专家；93 层（1 层 dense，注意力层为 69 层 KDA + 24 层 Gated MLA）；注意力隐藏维 7168、96 头；词表 160K；视觉编码器 MoonViT-V2（401M 参数）；量化为 MXFP4 权重 / MXFP8 激活（量化感知训练）。**权重体积 1.56TB 只见于 Simon 的转述**（"They're a hefty 1.56TB on Hugging Face"），model card 未给出体积数字——1.56TB 与 2.8T 参数按 MXFP4 存储量级相符，但严格说这是 Simon 的口径，不是官方口径。
- **架构自陈**：摘要点名 Kimi Delta Attention 与 Attention Residuals，作用是"improve information flow across sequence length and model depth"；配合 Stable LatentMoE，官方称相对 Kimi K2 取得"approximately 2.5x improvement in overall scaling efficiency"（2.5 倍是**缩放效率**，不是性能提升，别写串）。
- **许可证到底改了什么（LICENSE 原文，Copyright (c) 2026 Moonshot AI）**：
  - K2（2025 年 7 月）那份自称"Our only modification part is..."，唯一改动就是署名：商业产品**月活超 1 亿或月营收超 2000 万美元**时，必须在 UI 上显著展示 "Kimi K2"。
  - K3 第 3 条把这条原样保留，只把字样换成 "Kimi K3"，门槛不变（1 亿月活 / 2000 万美元**月**营收）。
  - K3 新增第 2 条，是本次真正的变化：先定义 "Model as a Service" 为「让第三方对输入、参数或训练数据拥有实质控制权的推理或微调访问（如 API）」，明确排除「模型能力仅嵌入特定功能或 harness 的终端产品」和「单纯把请求转发给别人托管的模型」；然后规定 Licensee 及其关联方若经营 MaaS 业务，且**任意连续 12 个月合计营收超过 2000 万美元**，商用前必须与 Moonshot 另签协议。注意触发线：署名条款看的是**月**营收 2000 万，商业授权条款看的是**年**营收 2000 万，后者低一个数量级，是一条真正咬得住中型 API 厂商的线。
  - 第 4 条豁免：纯内部使用（不把软件、其输出或其底层能力提供给第三方）、以及通过 Moonshot 官方产品或认证推理伙伴访问的用法，均不受第 2、3 条约束。
  - 第 5 条是标准 AS IS 免责。许可证联系邮箱 license@moonshot.ai。
- **Simon 的两处评价**：称 K2 那份是"their own janky modified version of the MIT license"；同时给 Moonshot 记了一笔好：'To Kimi's credit, they make no attempt to describe this as an "open source" license in their own materials, consistently using the term "open weight" in its place.'
- **官方评测数字（model card 评测表，K3 vs 对手，同表列出 Claude Fable 5 / GPT-5.6 Sol / Claude Opus 4.8 / GPT-5.5 / GLM-5.2）**：
  - GPQA Diamond：K3 93.5，Fable 5 92.6，GPT-5.6 Sol 94.1，Opus 4.8 91.0，GPT-5.5 93.5，GLM-5.2 91.2
  - Terminal-Bench 2.1：K3 88.3，Fable 5 88.0，GPT-5.6 Sol 88.8，Opus 4.8 84.6，GPT-5.5 83.4，GLM-5.2 82.7
  - BrowseComp：K3 91.2，Fable 5 88.0，GPT-5.6 Sol 90.4，Opus 4.8 84.3，GPT-5.5 84.4，GLM-5.2 未列
  - Agents' Last Exam：K3 28.3，Fable 5 25.7，GPT-5.6 Sol 29.6，Opus 4.8 27.0，GPT-5.5 26.6，GLM-5.2 20.4
  - 其他单项（未逐一取回对手列，引用时只能作为 K3 自报成绩）：DeepSWE 67.5、SWE-Marathon 42.0、CritPt 23.4、AA-LCR 74.7、MCPMark-Verified 94.5、OSWorld-Verified 84.8、OmniDocBench 91.1、Video-MME 90.0
  - 表里**没有** Humanity's Last Exam 和 SWE-bench Verified 两行（已核，标准榜单缺席）。
- **价格与可用性**：OpenRouter 已上线 7 家 provider，多数与 Moonshot 官方同价，$3/百万输入 token、$15/百万输出 token（Simon 转述）。官方部署支持 vLLM、SGLang、TokenSpeed；多轮对话要求回传完整 assistant 消息（含 reasoning_content），采用 preserved thinking history 模式。
- **作者规模**：技术报告署名为 Kimi Team 加 380 余位作者。

## 与近期的关系

强承接，且是闭环：
- **07-26 日报**收过一条预测市场——「8 月 13 日之前普通人能拿到 Kimi K3 的权重吗？93.0%，成交额 1.3k mana」（https://manifold.markets/Tetraspace/will-kimi-k3-be-open-source-on-the ）。今天到期前半个月兑现，93% 的盘口押对了。
- **07-27 日报的 report.md 记着**：scout 拦下一条搜索聚合站的说法「Kimi K3 权重今日 00:00 UTC 发布，1.4TB / 2.8T 参数」，当时查 HF API 显示 moonshotai 名下最新仍是 06-15 的 Kimi-K2.7-Code，无 K3 仓库，故未收。今天仓库确实存在（本轮直接读到 model card 与 LICENSE 全文）。当时那条的「1.4TB」与现在 Simon 的 1.56TB 对不上，说明那确实是提前编的数，不是提前泄的料。
- K3 模型本身在 07-25（27 分钟挖 Redis 0day）、07-26（浏览器里搓 Windows XP）都以简讯形式出现过，**但都是 API 版能力的花边**。今天是权重本身第一次落地，角度不重复；写的时候别把重点放在「K3 很强」，重点是权重和许可证。
