# AI 日报 · 2026-06-27（周六）

> 流水线：scout 全量扫 16 源（1 抓取失败如实记）→ manifest（2 精读候选 + 7 雷达候选）→ 2 reader 精读 → reduce 定牌。
> 终稿精读 2 条（金 1 / 银 1）+ 雷达 3 条。导读按规：金牌两段、银牌一段、大白话、少用「反直觉」字样、少用破折号；雷达只留蓝字。
> **scout 红线守住**（已固化进 scout.prompt.md）：openai.com GPT-5.6 正文 403，scout 如实记 fetch_failures、URL 出自 RSS 真见到、未推断；未下因果。
> **定牌取舍**：本期两条都够金牌料。按用户口味（技术/可上手 > 政治）定 Raschka 本地 agent 为金、政府门控为银，**已向用户说明可对调**（政府门控是 HN 全场最高 1083 分、且 Fable/Mythos 停用大瓜的收尾）。

## 🥇 金牌 · 头条精读

### [用开源模型在本地跑编码 agent 替代订阅：你以为在选模型，其实在选 harness](https://magazine.sebastianraschka.com/p/using-local-coding-agents) · Ahead of AI（Sebastian Raschka，稀产高权重源）· 2026-06-27
**为什么值得看**：稀产高权重源当天长稿 how-to，料足可照做，自带一个实测打脸的结论——harness 比模型更决定 token 消耗，把对手的 Codex 当通用 harness 比模型「原生」harness 还好。
- 配方：主推 Qwen3.6 35B-A3B（约 22 GB，需 30–40 GB RAM），Ollama 起服务，Mac Mini M4 或 DGX Spark 可跑，约 40 tok/s（≈GPT-5.5 高推理）。对照 North Mini Code、Nemotron 3 Nano、Gemma 4 E2B；GLM-5.2 最强但消费级跑不动。
- 实测（5 题小评测）：Qwen-Code 4/5、Codex 5/5、Claude Code 5/5；Gemma 4 E2B 在 Qwen-Code 里 0/5。
- 反常识①：同一 Qwen3.6，套 Codex 比套「原生」Qwen-Code 表现更好——「using Codex as the universal coding agent harness may not be such a bad idea after all」。
- 反常识②：token 消耗主要由 harness 决定、非模型——Claude Code 烧最多、Codex 最少；实例一次跑约 57.8 万输入 token 只出 4.5k（每轮反复回灌上下文），却没更强。
- 为什么本地：成本可预测/免 API 涨价、隐私（收据等数据不外发）、离线、好玩；吐槽 Claude Code 闭源、似乎向 Anthropic + Datadog 发数据。
- ⚠️ 诚实留尾：他承认 GPT-5.5/Opus 4.8 仍更强，自己日常主力还是 Codex + Claude Code。是『开源采用侧(06-22)/可负担性(06-23)/Codex 主流化(06-25)』线的**落地教程新角度**，自带反向料（harness 决定论），不撞趋势论。

## 🥈 银牌 · 非头条精读

### [前沿模型的分发闸门正落到美国政府手里：GPT-5.6 逐客户审批、Mythos 5 解禁](https://www.washingtonpost.com/technology/2026/06/26/openai-says-us-government-will-vet-users-its-latest-ai-model/) · WaPo（HN 1083，全场最高）+ Semafor/Axios/TechCrunch 多源 · 2026-06-26~27
**为什么值得看**：本期最大新闻 + 6 月初 Fable/Mythos 停用大瓜的收尾级转折。过去管 AI 争「要不要发」，现在政府直接管「谁能用」，逐客户点头放行。
- GPT-5.6：三档 Sol（旗舰，coding/生物/网安）/Terra（中端）/Luna（速度成本）；preview 阶段政府「customer by customer」审批，首批约 20 家伙伴名单逐个由政府点头。定价仅 TechCrunch 一家给（Sol $5/$30…），待二次确认。
- ⚠️ 框架分歧：WaPo 等读成「政府审用户」，OpenAI 自己措辞更软（「参与情况报备政府」），呈现已分清「谁声称」。Altman 内部备忘录：「not our preferred long term model」；OpenAI 称「short-term step」、不应成长期默认。
- Mythos 5 解禁：放给「100+ 美国机构含政府部门」；Lutnick 致信 Tom Brown「appropriate safeguards are in place」；Annex A 实体及外籍员工转让不再需许可证。
- Fable 5 仍悬：Lutnick 信中沉默；Anthropic 称在推动「make Fable 5 available for general use again」，时间线不明（网传 7/1 前 57% 恢复来自预测博客、非一手、未入正文）。
- ⚠️ 原始停用理由口径分歧（均「指控/声称」级，未独立证实）：Semafor/TechCrunch 称 Amazon 等警告可被 jailbreak 滥用；Washington Examiner 称 China-linked group 据称访问过 Mythos。未替政府/厂商拍因果。
- 真伪：四条多源交叉（openai.com/Axios 403 走二手），事实与各方表态严格分层。

## 雷达（terse · 只蓝字）

- [两个 AI 代码审查 agent 互相挑刺、陷入死循环烧掉 41,255 美元 API 费，厂商反手把这场翻车包装成营销（Simon 转的讽刺短文）](https://simonwillison.net/2026/Jun/26/incident-report/) · Simon Willison 转 Andrew Nesbitt · 2026-06-26
  - 存档：<200 字讽刺短文 link-post（CVE-2026-LGTM），有乐子但极轻。
- [一篇复盘开源权重模型和闭源旗舰到底还差多少的长文，和今天头条那篇本地 agent 教程正好对照着看](https://blog.doubleword.ai/frontier-os-llm) · doubleword.ai（HN 241）· 2026-06-26
  - 存档：开源-闭源差距复盘，与金牌 Raschka、近期 GLM-5.2 主线同向，作对照素材。
- [IEEE Spectrum：AI 进入数学正逼出一些大问题，比如证明对了但人看不懂、数学家该信任 AI 到什么程度](https://spectrum.ieee.org/ai-in-mathematics) · IEEE Spectrum（HN 156）· 2026-06-26
  - 存档：AI-for-math 哲学向，淡日一眼。

---
## 运行健康
- 周六淡日，但出了大新闻。scout 全量扫 16 源、1 抓取失败（openai.com GPT-5.6 Sol 403，如实记、URL 出自 RSS、未推断）。产出 2 精读候选 + 7 雷达候选。reduce 派 2 reader 精读。
- **scout 红线表现好**：fetch_failures 如实记、URL 只填真见到的、未下因果。固化进 scout.prompt.md 后第二期，执行稳定。
- reader 核实/校准：① group-1 政府门控四条多源交叉（openai.com/Axios 403 走二手 WaPo/Semafor/TechCrunch/CNBC），事实 vs 表态严格分层、定价仅一家待确认已标、停用理由两口径并列未拍因果。② group-2 Raschka 工程实测，钩子是「harness 决定论」，作者诚实留尾（云端旗舰仍更强、自己仍用云端主力）。
- 定牌：金 1（Raschka 本地 agent）、银 1（政府门控 + Mythos 解禁）。**已向用户说明金/银可对调**（政府门控是 HN 全场最高 + 大瓜收尾，按用户口味技术优先暂定银）。
- 丢弃/略过（seen=false 备查）：Simon 引 Dean Ball（利润窗口压缩，group-1 背景）、Simon 引 Timothy Lee（LLM 学习曲线，轻）、HF VLX-Seek/Flow（VLM 感知，niche）、JD Vance 硅谷募款（科技圈政治、非 AI 实质）。
- seen 回写（report_date 2026-06-27）：ahead-of-ai（Raschka reported=true）；openai（GPT-5.6 Sol reported=true）；hacker-news（WaPo 政府审核、Semafor Mythos 解禁、doubleword 开源差距、IEEE AI-math reported=true）；axios（Fable 5 return reported=true；Vance 募款 reported=false）；simon-willison（CVE-2026-LGTM reported=true；Dean Ball、Timothy Lee reported=false）；huggingface（VLX-Seek reported=false）。
- 跳过的源（无新货/出窗/停更）：thezvi、interconnects、import-ai、the-batch、anthropic、deepmind、lilian-weng、karpathy、thinking-machines、chip-huyen。
