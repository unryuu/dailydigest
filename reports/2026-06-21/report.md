# AI 日报 · 2026-06-21（周日）

> 周末淡日。流水线：scout 全量扫 16 源 → manifest（2 精读候选 + 1 雷达）→ 2 reader 并行精读 → reduce 定牌 → 用户反馈后对调金/雷达。
> 终稿精读 1 条（金）+ 雷达 1 条。导读按规范：大白话 + 少破折号。
> **编辑说明（两处）**：① scout 把 Anthropic 实名那条框成「对某些能力强制实名 = Fable/出口管制收口」，reader 真读官方页后**推翻**：实为消费级订阅用户（Free/Pro/Max）的身份+年龄验证，明确不含 API/企业，且无任何来源与 Fable/Mythos/出口管制挂钩，终稿按纠正口径写、未串旧瓜。② 初稿金=Anthropic 实名、银=拜耳工程篇；**用户反馈 Anthropic 实名当天已铺天盖地刷到、要求降雷达，拜耳工程篇升金牌**，遂对调。

## 🥇 金牌 · 头条精读

### [把不确定的 LLM agent 做成生产级系统：拜耳 PRINCE 真实案例](https://martinfowler.com/articles/reliable-llm-bayer.html) · martinfowler.com（作者 Sarang Sanjay Kulkarni，Thoughtworks 首席顾问）· 2026-06-16
**为什么值得看**：反直觉且对工程师友好——让 agent 可靠靠的不是更强的模型或更妙的 prompt，而是工程化「模型看到的 context」和「模型行动的 harness」；还自爆「多加一层 AI 校验」的本能做法被实测打脸。
- PRINCE 系统：让药物研发科学家查几十年临床前安全研究（数千份毒理/药理 PDF）的多 agent 系统，用 LangGraph 编排。
- 钩子一：上下文窗口变大反而更要克制喂料。原话「In early iterations, putting too much information into the context made the system harder to steer and harder to evaluate.」解法是按阶段切开 context（规划/检索/反思/写作各看各的）。
- 钩子二：主动删掉「用 LLM 审查 LLM 生成的 SQL」一层——审查的 LLM 老把正确 SQL 误判为错，拖效率又不换准确率。
- 三种反思回路：Process（步骤走法对不对，灵感来自 Anthropic 的 Think 工具）/ Data（证据够不够，不够回去补问）/ Draft（写作 agent 内部查漏）。
- 混合检索硬参数：元数据过滤把搜索空间从百万压到几十~几百 → 小模型扩 5 条相似 query 并行搜 → 语义权重 0.7 + 关键词 0.3 → 初筛约 20 chunk，cross-encoder（bge-reranker-large）重排到 7 条。
- 确定性护栏：text-to-SQL 只允许 SELECT，封禁 DELETE/INSERT/UPDATE；单次最多 50 条；报错回灌自纠最多 3 次。状态存 PostgreSQL，节点级自动重试，主 LLM 挂自动切备用。每句结论带引用，悬停看来源页码。评测两层：Dataset（参考答案存 Langfuse，测 Faithfulness 等）+ Live（每日跑生产真实流量、专抓幻觉），可观测靠 Langfuse + CloudWatch、指标用 RAGAS。
- ⚠️ 工程经验帖、非新研究/新事件，无量化效果数字（无准确率提升/规模数字）；时效性弱。

## 雷达（terse）

- [Anthropic 7/8 起对 Claude 消费级用户加身份+年龄验证（刷脸的是订阅用户，不是 API）](https://support.claude.com/en/articles/14328960-identity-verification-on-claude) · Anthropic 官方 Help Center（一手）+ CyberPress 等二手交叉 · 2026-06（HN 91）— Free/Pro/Max，明确不含 Team/Enterprise/API；自愿合规、年龄+滥用防控驱动，无官方来源把它与 Fable 或出口管制挂钩（初稿金牌，用户判当天已刷烂、降雷达）。

---
## 运行健康
- 周末淡日（周日）。scout 全量扫 16 源、0 抓取失败。13 源无新货/出窗/无关（其中 Axios 当日全是伊朗/边境/世界杯，唯二科技条 06-20 已报）。
- scout 产出 2 精读候选（各成一组、都标轻）+ 1 雷达候选。reduce 派 2 reader 并行精读，均回传扎实 digest。
- **关键纠偏**：Anthropic 实名那条 scout 框架（「强制实名 = API 出口管制/Fable 收口」）被 reader 真读官方页推翻——实为消费级 KYC + 年龄验证、明确不含 API/企业、无任何来源与 Fable/出口管制挂钩。终稿按纠正口径写，未强串旧瓜。
- **用户对调**：初稿金=Anthropic 实名、银=拜耳工程篇；用户判 Anthropic 实名当天已铺天盖地、要求降雷达，拜耳工程篇升金牌。终稿金 1（拜耳）+ 雷达 1（Anthropic 实名）。两条 seen 仍 reported=true，分档调整不影响 reported 状态。
- reader 抓取/校验边界（已诚实标注）：金牌 reddit 原帖 WebFetch 全域被拒、社区反应据二手；官方页一手抓到但不含日期/分层/生物特征，那些细节由 CyberPress 等二手多源交叉补全。银牌 Bayer 文全文读到，引述为原文直引。
- 雷达候选「Two Qwen3 models on one DGX Spark」HN 仅 14 分、低信号、本地模型角度 06-16~06-19 已密集报、且 06-18 出 24h 日检窗——采纳 scout 建议略过，seen 标 reported=false 备查。终稿雷达仅含降级下来的 Anthropic 实名一条。
- seen 回写（hacker-news）：拜耳 martinfowler URL + Anthropic reddit 讨论 URL 标 reported=true；DGX Spark URL 标 reported=false。
- 跳过的源（无新货）：ahead-of-ai、anthropic、axios、chip-huyen、deepmind、huggingface、import-ai、interconnects、karpathy、lilian-weng、openai、simon-willison、the-batch、thezvi、thinking-machines。
