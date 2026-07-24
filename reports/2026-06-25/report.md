# AI 日报 · 2026-06-25（周四）

> 流水线：scout 全量扫 16 源 → manifest（4 精读候选 + 4 雷达候选）→ 3 reader 精读 + 1 verifier 核真伪/雷达 + 1 reader 补精读 Moon Bot（升金后）→ reduce 定牌 → 用户复核重排。
> 终稿精读 3 条（金 1 / 银 2）+ 雷达 3 条。导读按规：金牌两段、银牌一段、大白话、少用「反直觉」字样；雷达只留蓝字。
> **scout 红线本期守住**：未编 URL、未下因果。
> **一处纠错（重要）**：06-24 把 HuggingFace「Moon Bot」判为「脑补/查无此物」是**误杀**——根因是 scout 给的裸 URL `/blog/moon-bot` 返回 404，而带命名空间的 `/blog/huggingface/moon-bot` 才是真文。本期 verifier 双路证实其真实存在。
> **编辑说明（用户复核）**：① Moon Bot 初为雷达，用户升**金牌头条**（遂补派 reader 真读全文、撑两段导读）。② Anthropic 蒸馏指控初定金牌，用户降**银牌**并要求删掉第二段（出口管制双标那段），只保留事实段。

## 🥇 金牌 · 头条精读

### [HuggingFace 摊开自家 Slack 编码 agent：怎么让一个不可信的 agent 安全碰生产系统](https://huggingface.co/blog/huggingface/moon-bot) · HuggingFace 官方博客（Eliott Coyac / Caleb Fahlgren / Franck Abgrall）· 2026-06-24
**为什么值得看**：罕见的「把内部 agent 怎么搭全摊开」的工程博客，干货密度高、可上手，好几个反常识的工程取舍。注意：是「可用系统回顾」非「踩坑实录」，无量化采用/成本/翻车故事，钩子落在工程取舍上、别脑补血泪史。
- 痛点：团队泡在 Slack 但答一个问题要在 ES 日志 / MongoDB / 代码库 / GitHub 间切换、各有 SSO。Moon Bot 把这些收进一个 Slack 线程。
- 核心取舍一：**LLM 从不直接碰 API/数据库**——原话「runs a command-line tool via bash, reads stdout, and iterates」。每个 skill 接口都是一个 CLI 工具；加新能力＝往 `skills/<name>/` 丢一个 SKILL.md。
- 核心取舍二：**不给 agent 凭据**——localhost 起反向代理（ES/HF/Plausible）在服务端注入密钥 + 硬 allowlist；工具被攻破也偷不走凭据。
- 核心取舍三：**权限分层是物理隔离**——三档（basic/elastic/privileged）每档背后独立 Linux 用户；「fails closed」：Okta 读不到则全员降 basic 且每条回复明说。
- 持久记忆：Buckets 存 `sessions/<id>.jsonl`（append-only，pod 崩几天后 lazy resume）+ `thread-map.json` + `memory.json`（滚动 200 次跨线程交互，暴露成 memory 工具）。
- 没写权限也能开 PR：写操作在 bot 进程铸短时效窄权限 GitHub App token，agent 够不到；**PR 正文由代码拼、不由模型写**。另有第二个低权限 GitHub bot pod 做纵深防御。
- 栈很薄：Slack(Socket Mode) → agent → 开源 Pi coding agent SDK → LLM+Skills+Tools → 落 HF Bucket。原文收尾「The infrastructure to get started is surprisingly thin」。
- ⚠️ 缺口（如实标）：无采用数/成本/延迟；生产用哪个 LLM 未披露（代码注释列 Kimi K2、Claude 为候选）；无翻车故事；防幻觉靠权限/沙箱限制数据范围、非约束模型解读。注意分清实操干货 vs 顺带宣传自家 Buckets。
- 与近期关系：承接 06-24 Claude Tag（同是 Slack 里的 agent）——Claude Tag 是轻量召唤入口，Moon Bot 把持久记忆/内网接入/分层沙箱当正经基础设施搭，是新角度。

## 🥈 银牌 · 非头条精读

### [Anthropic 致信参议院，指控阿里用 2.5 万假账号偷 Claude 的能力](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) · CNBC / Reuters（403）/ 多源 · 2026-06-24
**为什么值得看**：本期最大新闻、全新主线。Anthropic 指控阿里巴巴对 Claude 发动「迄今最大的已知蒸馏攻击」。
- 指控：Anthropic 6/10 致信参议院银行委员会（点名 Tim Scott、Elizabeth Warren），称阿里巴巴/Qwen 用约 2.5 万欺诈账号、约 2880 万次交互（4/22–6/5）套取 Claude 能力。蒸馏=用强模型输出训练/提炼弱模型。
- ⚠️ **单方指控**：阿里截至发稿 declined to comment / 未公开反驳，公共记录是一面之词。
- ✅ 真伪：CNBC / CybersecurityNews / AI Chat Daily / The Deep Dive 四源交叉，Reuters/Bloomberg 403 但数字一致。
- 编辑：原金牌第二段（Anthropic 自己被 Fable 5/Mythos 5 出口管制卡脖子的「双标张力」+ 推动立法弹药）按用户要求删去，只保留事实段。承接出口管制风波线索仍存档于此。

### [Codex 们正挤进主流工作？数据有，水分也有](https://www.axios.com/2026/06/25/codex-agents-growth-openai) · OpenAI 官稿 + Axios 独家 · 2026-06-25
**为什么值得看**：官方叙事 vs 第三方校准的对照——有较难造假的渗透率数据，但「主流化」目前主要还在 OpenAI 自家围墙内。
- OpenAI 报告（挂 Columbia/Duke/Penn 联署）渗透曲线：组织外部 Codex 占比 0%→17%；非开发者使用量 137x / 189x 增速。
- 降温（务必带）：分析师 Larry Dignan 点破动机是「从 Claude 抢回声量」；按 token 算 99.8%(内部)/63%(组织)/16.5%(个人) 断崖，主流化主要在 OpenAI 围墙内。
- ⚠️ 版本陷阱：「500 万周活 / 知识工作 20%」是 06-02 旧稿数字，今天新增量是学术联署 + 渗透曲线 + 137x + 内外断崖，别混。两篇正文均 403、数据走多源交叉。

## 雷达（terse · 只蓝字）

- [高通 39 亿美元全股票收购 AI 软件栈创业公司 Modular（Mojo 语言 + Chris Lattner 团队），补数据中心 AI 软件层、直冲英伟达 CUDA 护城河](https://www.cnbc.com/2026/06/24/qualcomm-ai-chip-modular-software.html) · CNBC/多源 · 2026-06-24
  - 存档：约 39 亿全股票，Modular（MAX + Mojo，Chris Lattner/Tim Davis，约 150 人）。✅ CNBC/QZ/Bloomberg/Tech Startups 交叉。与 06-24 Jalapeño 同属「挑战英伟达」一线（硬件定价 + 软件护城河两面），属 M&A 留雷达。
- [Google 把 computer-use 下放到更便宜的 Gemini 3.5 Flash：agent 能看屏幕、在浏览器和手机桌面里直接动手操作](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) · Google DeepMind · 2026-06-24
  - 存档：从此前独立的 2.5 computer-use 模型升级、作为内置工具下放到 Flash。✅ 一手 blog.google，日期在窗。
- [Nathan Lambert：GLM-5.2 是开源模型在 agent 上的「阶跃」，第一个在编码 harness 里当通用 agent 手感真对了的开源模型（他自承主要靠实测手感，硬基准数据偏薄）](https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open) · Interconnects · 2026-06-22
  - 存档：GLM-5.2 主线第 4 次出现（06-20 幻觉率 / 06-22 采用侧 / 此为 agent 维度新角度）。增量成立但偏窄、硬证据薄（无 SWE-bench，主力 Arena + 个人 Claude Code 手感），压雷达不升精读。

---
## 运行健康
- 周四常规日。scout 全量扫 16 源、自报 0 失败；产出 4 精读候选 + 4 雷达候选。reduce 派 3 reader + 1 verifier，定牌后用户把 Moon Bot 升金、遂补派 1 reader 真读 Moon Bot 全文撑头条。
- **scout 红线守住**：未编 URL、未下因果（对比 06-24 进步明显）。
- **Moon Bot 纠错**：06-24 判「脑补丢弃」实为误杀——裸 URL 404、带命名空间 URL 才真，06-24 搜索法漏了。本期 verifier 直抓正文 + 搜索双路证实为真。**教训**：scout 推断 URL 既可能 slug 错也可能命名空间错，核真伪要「直接抓正文」而非仅搜索；STATUS 待办据此已调整。
- reader 核实/校准：① group-1 阿里指控四源交叉（Reuters/Bloomberg 403），标清单方指控 + 阿里未回应。② group-2 两篇 403、识别「500 万周活」是 06-02 旧数字、剥软文、带分析师降温。③ group-3 Lambert GLM-5.2 增量偏窄、压雷达。④ verifier 证实 Qualcomm/Modular、Gemini Flash computer-use、RubyLLM、Moon Bot 全真。⑤ Moon Bot 补精读：CLI 当唯一接口 / 凭据走代理不给 agent / 权限分层物理隔离 / append-only session 当记忆 / 无写权限也能开 PR 等工程取舍。
- 定牌（含用户复核重排）：金 1（Moon Bot，用户由雷达升金）、银 2（阿里蒸馏指控由金降银并删第二段、Codex 主流化）、雷达 3（高通收 Modular、Gemini Flash computer-use、Lambert GLM-5.2）。
- 丢弃/略过：RubyLLM（Ruby 框架受众窄，seen=false）、Axios「水耗成 AI 燃点」（水耗 06-22 已密集报、旧线，seen=false）。
- seen 回写（report_date 2026-06-25）：hacker-news（阿里指控 Reuters URL、Qualcomm/Modular reported=true；RubyLLM reported=false）；openai（how-agents-transforming-work reported=true）；axios（codex-agents-growth reported=true；水耗 reported=false）；deepmind（Gemini 3.5 Flash computer-use reported=true）；interconnects（GLM-5.2 step change reported=true）；huggingface（Moon Bot reported=true）。分档调整不影响 reported 状态。
- 跳过的源（无新货/出窗/停更）：anthropic（指控走第三方源、官方 news 页未上）、simon-willison（dev 工具噪音）、import-ai、the-batch、ahead-of-ai、karpathy、lilian-weng、thinking-machines、chip-huyen。
