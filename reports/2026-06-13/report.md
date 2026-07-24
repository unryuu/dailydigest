# AI 日报 · 2026-06-13（周六）

> 单头条 + 三条乐子日。流水线：scout subagent 全量扫 15 源 → manifest → reader 并行精读（group-1 Fable 停用、group-2 The Batch、group-3 三条乐子追加）→ reduce。
> 精读 4 条（金 1 / 银 3），雷达 3 条。中间产物见同目录 `manifest.json`、`digests/`。
> 注：本期按用户新权重收尾——「有乐子」加权、「模型评测/跑分」降权。三条乐子（开源檄文 / 最危险模型小游戏 / tensorzero 归档）由雷达升为银牌精读；Cursor（评测对比类、偏闷）由拟银牌降为雷达且只留蓝字；雷达回到 terse 格式。

## 🥇 金牌 · 头条精读

### [美政府勒令停用 Fable 5 + Mythos 5](https://www.anthropic.com/news/fable-mythos-access) · Anthropic 官方声明 + Simon Willison + Zvi + 12gramsofcarbon · 2026-06-12-13
**为什么值得看**：政府第一次直接把一款已部署给数亿人的前沿商用模型从公众手里「召回」，而触发它的「危险能力」竟是安全工程师每天都在用的操作——让 AI 读代码、修漏洞。是国家安全，还是 IPO 前夜的政治猎杀，圈内吵翻。
- **事实经过**：2026-06-12 17:21 ET，美政府以出口管制指令，要求 Anthropic 对**全球所有用户**（含外国公民及 Anthropic 员工）停用 Fable 5 / Mythos 5，其他模型不受影响。Simon 用 API 探测：最后成功访问 6:58 PM PT，下一分钟即被拒（"Claude Fable 5 is not available. Please use Opus 4.8."），约指令后 4.5 小时真正切断。
- **政府逻辑**：声称掌握一种绕过 Fable 5 护栏的「越狱」——演示本质是「让模型读一段指定代码库、修掉其中软件漏洞」，Anthropic 称其为 narrow, non-universal jailbreak。
- **Anthropic 反驳**：「We disagree that the finding of a narrow potential jailbreak should be cause for recalling a commercial model deployed to hundreds of millions of people.」称同等能力别家（GPT-5.5）随处可得，护栏经数千小时联合红队打磨；并警告「若此标准全行业适用，将基本叫停所有新模型部署」。
- **技术派（Simon）**：该能力「widely available from other models (including OpenAI's GPT-5.5)」，且「is used every day by the defenders who keep systems safe」——威胁被夸大、召回不成比例。
- **政治派（12gramsofcarbon，HN 370 分 362 评）**：Anthropic 与本届政府「素不相能」、曾被列为 supply chain risk；竞品「与政府上下交好（Kushner 家族重仓 OpenAI）」；周五收盘后发坏消息疑似让市场周末消化、防股价当场崩，且正赶在 IPO 前夜，时机「very convenient」；担心这是「政府单方面把强 LLM 从公众手里收走」的开端。
- **政府在怕什么（Zvi 系统卡能力评估，仅作背景，非对停用的评论）**：Mythos 5 生物能力跨越式提升——某项原需平均 580 小时（72.5 工作日）的任务，Mythos 协助下 16 小时完成；评估认为「很可能已越过真实 CB-2 威胁模型」（技术上仍低于设定阈值）。网络能力：UK AISI 单轮攻击性查询「几小时」、多轮 agentic 工作流「两天」即可推进。
- **与近期关系**：Fable 线 06-11 报「撤回隐形降级政策」（金）、06-12 报「relentlessly proactive」（雷达）均为旧料；本条只写 06-12「停用指令」新线及各方评价。

## 🥈 银牌 · 非头条精读

### [Open Source AI Must Win](https://opensourceaimustwin.com/?share=v2) · Ahmad Osman 个人站 · 2026
**为什么值得看**：一篇单人写的开源 AI 立场檄文冲到 HN 1240 分。把「开源 AI」从软件自由抬到**运行自由**——智能若只能向少数封闭机构「租」，公众失去的是「认知的订阅经济」下的操作权，要求 AI 能被无许可地研究/修复/审计/改造/运行，哪怕头部实验室「改变方向或消失」也能续跑。
- 反差钩子：**有论证、零诉求**——没请愿、没联署，唯一「行动」是给作者发邮件。一篇没组织的个人檄文爆到 1240 分，是情绪温度计：恰好接住今天「政府一键叫停 Fable 5」点燃的焦虑。
- ⚠️ 边界：檄文本身**未点名** Anthropic / Fable / 禁令，这层呼应是大背景下的读者投射，非原文主张（已据实区分）。

### [Shepherd's Dog: A Game by the Most Dangerous AI Model](https://koenvangilst.nl/lab/claude-fable-shepherds-dog) · Koen van Gilst 个人站 · 2026
**为什么值得看**：那个「危险到不能放给世界看」的模型，被开发者一口气（one go）生成了一个浏览器小游戏——单 HTML、零依赖、**2319 行一次跑通**，一只放羊的狗。作者：「第一次有模型能一气呵成帮我做出来。」
- 黑色幽默钩子：如果「最危险」模型的主要成就是个牧羊犬游戏，当初的威胁评估是不是上头了？正撞「政府今天勒令停用」——监管当它洪水猛兽，开发者拿它做游戏发 HN。
- ⚠️ 边界：原文措辞是「Anthropic 一个有争议的、据说危险到不能见世的模型」，**未逐字写 "Fable 5"**，语境指向明确。

### [TensorZero 一夜归档](https://github.com/tensorzero/tensorzero) · GitHub · 归档于 2026-06-12
**为什么值得看**：一个开源 LLMOps 平台（README 自称「承载全球约 1% 的 LLM API 支出」、2024 年拿过 730 万美元种子轮），2026-06-12 被 owner 设为 archived（只读）。
- 悬念钩子：拿了大钱、自称 production-ready 的开源基建一夜变只读墓碑——弃坑？收购？转闭源？最反常的是**哪儿都没说**：仓库、组织主页、官方博客（最近一篇还是 5/12 常规技术文）全无归档说明。
- ⚠️ 边界：归档原因公开渠道（GitHub / 博客 / WebSearch）一律查无，本条只报「状态 + 悬念」，不脑补结局。

## 雷达（terse）

- [Cursor Composer 2.5（底层 Moonshot 开源的 Kimi K2.5）](https://www.deeplearning.ai/the-batch/issue-357) · The Batch #357 — Cursor 自研编码私模，主打比 Claude Code 便宜十倍（$0.44 vs $4.14/任务，据 The Batch 转述）。评测对比类、偏闷，按新权重降雷达只留蓝字。
- [How to setup a local coding agent on macOS](https://ikyle.me/blog/2026/how-to-setup-a-local-coding-agent-on-macos) · Hacker News（421 分）
- [OpenAI WebRTC Audio Session, now with document context](https://simonwillison.net/2026/Jun/12/openai-webrtc/) · Simon Willison · 2026-06-12

---
## 运行健康
- 今日类型：**单头条 + 三条乐子**。scout 全量扫 15 源、0 抓取失败；reader 分三批：group-1（重·多源 Fable 停用）、group-2（中·The Batch 补漏）、group-3（追加·三条乐子，reduce 阶段按用户指示补派）。
- 定牌：金 1（Fable/Mythos 停用）；银 3（开源檄文 / 最危险模型小游戏 / tensorzero 归档——原为雷达，按用户「有乐子」加权升为精读，且都补做了真精读）。Cursor 由拟银牌降雷达只留蓝字（评测对比类 + 偏闷，撞新降权规则）。
- 权重更新（本期起生效，已写入 PROMPT.md）：加权新增「有乐子」；降权新增「模型评测·跑分」；雷达回到 terse、不堆黑字（乐子条目若要展开则升精读，而非在雷达里加长）。
- reader 抓取：group-1 四源全成功；group-2 成功；group-3 三条全读到，且对「檄文未点名 Fable」「游戏未逐字写 Fable 5」「tensorzero 归档原因查无」三处边界均如实标注、未脑补。
- 写入 / 更新 seen（reported=true 为进报，false 为扫到未收）：
  - anthropic +1：fable-mythos-access（金,true）。
  - simon-willison +3：us-government-directive（金·源,true）、openai-webrtc（雷达,true）、andrew-singleton（false）。
  - thezvi +1：fable-5-mythos-5-system-card（金·背景源,true）。
  - hacker-news +5：12gramsofcarbon（金·源,true）、opensourceaimustwin（银,true）、shepherds-dog（银,true）、tensorzero（银,true）、local-coding-agent-macos（雷达,true）。
  - the-batch +1：issue-357（雷达,true）。
  - openai +1：academy-courses（false，营销稿）。
- ⚠️ scout 小瑕疵：huggingface MTEB v3 榜单（昨天已写入 seen）今天被当新候选又列一次（相对时间戳去重未命中）。已识别、未重复收录、未重复写 seen。后续在 scout 去重环节加强相对时间戳源的指纹比对。
- 跳过的源（无新货）：deepmind、import-ai（无 461）、interconnects、ahead-of-ai、karpathy、lilian-weng、thinking-machines、chip-huyen。
