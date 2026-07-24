# AI 日报 · 2026-06-30（周二·淡日）

> 流水线：scout 全量扫 18 源（0 抓取失败）→ manifest（4 组 + 4 雷达）→ 派 4 reader → 4.8 定牌 → **本期省额度：跳过写手/工单，主 Claude 直接把定牌段落清成导读**（用户指示）→ 跳过破折号/反直觉自查（用户指示，仅守 `<br>`/裸引号/裸 `<>&` 三个发送硬坑）→ 发频道。
> 终稿：金 1 / 银 2 / 雷达 5。淡日，13 源无窗内新货（Zvi/Anthropic/Import AI 463/Raschka 等主线饱和，Karpathy/Lilian/Chip/TM 停更）。
> 去重：欧洲就业报告（06-29 已报）从雷达剔除；Qwen3.6 27B 降雷达（06-27 本地编码主线旧增量）。

## 🥇 金牌 · 头条
### [agent 能力的真瓶颈不是堆参数：该停手时停不下来，堆参数堆推理反而更糟](https://huggingface.co/papers/2606.28733) · HF/arXiv · 2026-06-30
两篇背靠背把「scale 参数」从两面否掉。
- **Agentic Abstention**（UW/Leeds/西南交大/AI2）：28K 任务新基准，最强模型及时弃权召回仅 26.7%；更大模型/更多推理反而更不会及时停；convolve（零训练蒸停手规则）把 Llama-70B 拉到 57.4%、整体召回 100%。
- **Agents-A1**（InternScience，[2606.30616](https://huggingface.co/papers/2606.30616)）：35B MoE（活跃参数未披露）长程 agent 基准自报超 1T（GAIA 96.0 vs Kimi-K2.6 80.6）。**留尾**：技术报告自评口径、混合他家公开数+自评；自承 MLE-Bench-Lite 43.9 落后 GPT-5.5 72.7 近 29 分。
- 加权：自创评测+反直觉。淡日唯一够金。

## 🥈 银牌
### [LongCat-2.0：美团开源 1.6T MoE、全程国产 ASIC 训练、隐身登顶后揭面](https://longcat.chat/blog/longcat-2.0/) · 美团 · 2026-06-30
- 1.6T 总/平均 48B 激活 MoE，原生 1M 上下文，**MIT 许可**、权重上 HF+GitHub。
- 钩子=三件叠加：真开源可商用 + 全程 5 万卡国产 ASIC（疑昇腾 910C，官方未点名）+ 此前以代号 Owl Alpha 在 OpenRouter 隐身月吞 11T token 登顶后才揭晓。中国算力自闭环实锤。
- 跑分全自报、无第三方核验（SWE-bench Pro 59.5 自称高于 GPT-5.5 58.6）；通用 agent 自承落后 Opus 4.8。官方页 JS 渲染抓失败，规格/license 由 VentureBeat/Silicon Report 交叉核实。

### [BIS 警告 AI 投资潮像运河/铁路/互联网泡沫一样以衰退收场](https://fortune.com/2026/06/29/bis-central-bank-warning-hyperscaler-data-center-1-trillion-gamble-recession/) · BIS 年度报告（多源二手）· 2026-06-28
- 监管/金融稳定视角：五大厂两年 AI capex 超 1 万亿、已超自由现金流；循环融资+再抵押=2008 式风险；AI capex 占美国 Q1 GDP 增长 74%。
- **与 06-29 Dalio 银牌切割**：Dalio 谈估值、BIS 谈债务传导（钱从哪来、坏账谁背）。axios 详情 403、BIS 原报告未直读，数据系 Fortune/Bloomberg/TFTC 二手转述。

## 雷达
- [Qwen 3.6 27B 本地开发甜点位（M5 Max 30 tok/s、8-bit 不掉质）](https://quesma.com/blog/qwen-36-is-awesome/) · Quesma 博客（HN 1041）· 2026-06-29（06-27 本地编码主线增量，降雷达）
- [Claude 多云分发再下一城：Bedrock/GCP apps gateway（自托管企业控制面）+ Azure Foundry GA](https://claude.com/blog/claude-apps-gateway-bedrock-google-cloud) · claude.com/blog · 2026-06-29（claude-blog 硬规则破例压雷达：纯分发公告、无新模型新能力，与昨日一致）
- [Simon Willison HTML 表格小工具（富文本表格转 HTML/MD/CSV/JSON）](https://simonwillison.net/2026/Jun/29/html-table-extractor/) · 2026-06-29
- [OSWorld2.0：computer-use agent 长程真实任务基准更新版](https://huggingface.co/papers/2606.29537) · HF · 2026-06-30
- [TUA-Bench（Meta）：通用终端使用 agent 新基准](https://huggingface.co/papers/2606.28480) · HF · 2026-06-30

---
## 运行健康
- 周二淡日（周一料厚后回落）。scout 全量扫 18 源、0 抓取失败如实报。4 reader：group-1（两篇 agent 论文，数字核实）、group-2（LongCat 第三方交叉/Qwen 降雷达）、group-3（BIS，axios 403、多源二手）、group-4（claude-blog 双分发公告，压雷达）。
- **本期流程变更（用户指示·省额度）**：跳过写手（4.6 窗口/API）与今日工单，主 Claude 直接把定牌建议段落清成导读发出；跳过破折号/「反直觉」自查，仅守三个发送硬坑（无 `<br>`/裸引号/裸 `<>&`）。JSON parse OK、dry-run 渲染正常。
- 定牌：金 1（agent 真瓶颈）、银 2（LongCat-2.0、BIS 泡沫警告）、雷达 5。
- 去重/降级：欧洲就业报告（06-29 已报）剔除；Qwen3.6 27B 降雷达（旧主线增量）；Foundry GA seen 由 false 翻 true（本期随 apps gateway 进雷达）。
- seen 回写（report_date 2026-06-30，均 reported=true）：hf-papers（Abstention/Agents-A1/OSWorld2.0/TUA-Bench）、hacker-news（LongCat/Qwen3.6）、axios（BIS）、claude-blog（apps gateway + Foundry GA）、simon-willison（HTML 表格工具）。
- 跳过的源（无新货/出窗/停更）：thezvi、anthropic、interconnects、import-ai、ahead-of-ai、deepmind、huggingface、openai、the-batch、karpathy、lilian-weng、chip-huyen、thinking-machines。
- 待办照旧：4.6 API 写手路线代理注入工具问题未修（本期因省额度直接绕过写手、未触发）。
