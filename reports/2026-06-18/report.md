# AI 日报 · 2026-06-18（周四）

> 偏技术/正经的一天，无硬乐子（scout 如实判断、未硬凑）。流水线：scout 全量扫 16 源 → manifest → 4 reader 并行 → reduce。
> 精读 4 条（金 2 / 银 2），雷达 4 条。中间产物见同目录 `manifest.json`、`digests/`。
> Fable/Mythos 主线已连报八天（Zvi #173 / Atlantic 引用今日仅降雷达）；group-4 Trump 影子政策因 Fable 饱和 + 政治内容偏多，按 reader 建议压雷达。

## 🥇 金牌 · 头条精读

### [AI 化学家改良了真实药物反应——同一天的另一篇却泼了冷水](https://openai.com/index/ai-chemist-improves-reaction) · OpenAI（× Molecule.one）+ LifeSciBench · 2026-06-17
**为什么值得看**：同日「炫能力通稿 + 自家基准自打脸」的反差，比任一篇单看都有料。
- **真改良（有湿实验）**：GPT-5.4 + Molecule.one 的 Maria 机器人实验室，在 Chan-Lam 偶联（伯磺酰胺底物，历来产率低到不实用）上跑 10,080 反应，88%/83% 底物产率提升，人工复验 14 个→11 成功、8 个 >2 倍；全程约 2.5 个月。
- **「近自主」有水分**：人选课题、人挑方案、人验证，AI 扛文献综述/假设/设计/分析；HN 前化学家祛魅「本质是高通量筛选 + AI 引擎」，反对「AI chemist」拟人化。
- **自打脸**：同日 LifeSciBench（173 博士出题、453 专家复审、750 任务、19,020 评分标准、过线 70%）——最强模型 GPT-Rosalind 仅 36.1%，GPT-5.5 25.7%、Gemini 3.1 Pro 23.6%；带附件任务从 45% 掉到 28%。利益冲突点：自家基准 + 榜首是自家 GPT-Rosalind，二手报道普遍没点破。
- ⚠️ 抓取：两篇 openai.com 原文 403，数字由 MarkTechPost / HN / OpenAI 官方 X 等多源交叉核对（关键数字两源以上一致）。

### [DeepMind 的新安全思路：把你的 AI agent 当「内鬼」来防](https://deepmind.google/blog/securing-the-future-of-ai-agents/) · Google DeepMind（AI Control Roadmap）· 2026-06-18
**为什么值得看**：工业界首次把「AI Control」做成可落地框架——不是又一篇唱衰，而是给机制 + 分级 + 真实落地。反直觉：默认你自己的 agent 是内鬼。
- **思路**：不替代对齐，在对齐之上加系统级兜底——「即使对齐不完美也要能保障」。比喻：有副驾驶刹车的驾校教练，信任但随时接管。
- **机制**：可信 AI 当「监工」持续审查工作 agent 的推理/动作（看行为模式）；三指标 coverage / recall / time-to-response；威胁建模套 MITRE ATT&CK。
- **分级**：检测规避 D1–D4（应对 agent 学会藏推理，必要时查模型内部）、危害执行 R1–R3（从事后异步到高危动作执行前同步拦截）。原文只给级名+逻辑、未逐级定义。
- **落地证据**：分析一百万个 coding agent 任务提炼行为特征；给 Gemini Spark 上实时监控，拦下过「无意删数据」。配两份 PDF（技术《AI Control Roadmap》+ 政策《Three Layers of Agent Security》）。
- ⚠️ 核对：原文未点名引用 Redwood/学界 AI Control，只引 MITRE；「AI Control」本是 Redwood 等 2024 起的学术议程，DeepMind 把它工业化但未致谢学界。

## 🥈 银牌 · 非头条精读

### [本地小模型不是廉价版 Opus，是另一类工具](https://blog.alexellis.io/local-ai-is-not-opus/) · Alex Ellis（HN 341）+ Charity Majors 呼应 · 2026-06-17~18
**为什么值得看**：接 06-17「本地模型真能用了」，角度从「能用」推进到「该怎么定位」。反直觉：别问它啥时候追平 Opus，它根本不在同一赛道。
- **定位**：需要全程盯着、只干有边界活儿的专用工具——「就像回火中的刀刃，你不会走开不管」。Qwen 3.6 27B SWE-Bench 77.2% vs Opus 88.6%「只差 12%」，但这 12% 卡在「能否放手自跑 10 分钟」的生死线（Claude 可无人值守 5–15 分钟，Qwen 开放任务进死循环、把同 5 条建议重复 12 遍）。
- **超能力**：飞快读懂/解释代码库（哪怕写不出来）、隐私敏感/气隙环境啃数据；实战靠本地模型分析遥测揪出某客户少报 4–5 倍 license，「光追回收入就把 1.2 万美元显卡赚回」。
- **三个真驱动**：数据主权、厂商风险（点名 Anthropic 给非美区下架 Fable 5）、成本可预测（电费固定 vs token 不可控）。
- 防重复：GLM-5.2、Charity Majors「AI 要更多工程纪律」06-17 已雷达报过，本组仅作能力坐标/呼应一笔带过，核在 alexellis 的重定位框架。

### [Midjourney 跨界造医疗硬件：全身超声扫描仪](https://www.midjourney.com/medical/blogpost) · Midjourney Medical（HN 1056）· 2026-06-18
**为什么值得看**：画 AI 假图起家的公司转身造真实医疗成像硬件，反差和争议都实打实（reduce 阶段按用户判断从雷达升银牌、补派 reader 精读）。
- **做了什么**：不是医学影像生成，而是硬件「Ultrasonic CT」全身超声扫描仪，无辐射无磁体，约 50 万个超声发射器，目标 60 秒重建亚毫米 3D 全身图，号称比 MRI 快几十倍、便宜成百上千倍；要开「Midjourney Spa」体检馆（2027 旧金山首店）。
- **不是空软文**：有实物原型；技术底座是向 Butterfly Network 授权的 ultrasound-on-chip（SEC 8-K：一次性 1500 万 + 每年 1000 万、五年最高约 7400 万美元；消息出 BFLY 当日涨约 16%）。
- **临床当场被拆**：HN 自称执业放射科医生（jmhmd）指超声物理拍不了充气的肺、骨病灶、被肠气包裹的腹腔，「全身」站不住；大规模低分辨率筛查会制造大量良性「偶发瘤」→ 连锁随访/焦虑；60 秒是目标值、原型实际约 20 分钟；监管刻意避诊断、先走「身体成分」。
- ⚠️ 原博客 403，digest 据 HN / latent.space / Engadget / SEC / BusinessWire 多源交叉核对。

## 雷达（terse）

- [美国暂缓把 DeepSeek 拉黑，另有 100+ 中企被列安全风险](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) · Hacker News（497 分）— 中美 AI 监管时效。
- [DeepSeek 上线视觉能力](https://chat.deepseek.com/) · Hacker News（306 分）— 产品发布。
- [Axios 三连：Trump「影子 AI 政策」/ 白宫 AI 权力中心换人 / 数据中心水电账单](https://www.axios.com/2026/06/18/trump-shadow-ai-policy) · Axios · 2026-06-18 — 政府靠逐案干预而非立规塑形产业（Fable 停用的制度底色）；Sacks/Krishnan 出走、Lutnick/Bessent 接手；亚利桑那数据中心水电承压。reader 评结构性有增量但本质仍是 Fable 底色 + 政治偏多，压雷达；三篇原文均 403，靠二手补。
- [Zvi 周报 #173《AI Pauses》](https://thezvi.substack.com/p/ai-173-ai-pauses) · Don't Worry About the Vase · 2026-06-18 — 本期主体仍是 Fable/Mythos 停用谈判（已连报八次），存档备查。

---
## 运行健康
- scout 全量扫 16 源、0 抓取失败。精读短名单 4 组 + reduce 阶段按用户要求补派 1 个 Midjourney reader = 5 reader。定牌：金 2（AI 化学家反差、DeepMind AI Control）、银 2（本地模型定位、Midjourney 医疗硬件）；group-4 Trump 影子政策 reader 建议雷达（Fable 底色 + 用户嫌政治偏多），采纳。
- 用户反馈应用：① 导读按要求改得更白话、大幅删减破折号（原每段约 3 个 →≈0）；② Midjourney 原为雷达，用户判断值银牌，补派 reader 精读后升银。
- 今日无硬乐子：scout 与 reduce 一致判断为技术/正经日，未硬凑。最接近「有意思」的是 AI 化学家的「自家基准自打脸」反差与本地模型「另一种工具」的重定位。
- reader 抓取边界（已诚实标注）：group-3 两篇 openai.com 403、group-4 三篇 axios 403，均由二手多源交叉核对补齐并标注；group-2 原文未致谢学界 AI Control（Redwood），如实点出；group-1 严格防重复，GLM-5.2/Charity Majors 未当新货。
- 写入 / 更新 seen（reported=true 进报 / false 扫到未收）：
  - openai +2：ai-chemist-improves-reaction（金,true）、life-sci-bench（金,true）。
  - deepmind +1：securing-future-of-ai-agents（金,true）。
  - hacker-news +4：alexellis-local-qwen（银·源,true）、midjourney-medical（雷达,true）、reuters-deepseek-blacklist（雷达,true）、deepseek-vision（雷达,true）。
  - axios +3：trump-shadow-ai-policy（雷达,true）、white-house-ai-power-center（false）、arizona-water-power（false）。
  - thezvi +1：ai-173-ai-pauses（雷达,true）。
  - simon-willison +4：charity-majors（false，仅呼应）、glm-52（false，仅坐标）、click-to-play（false）、datasette-1.0a34（false）。
  - interconnects +1：state-of-the-blog（false）；huggingface +1：intel-xpu-kernels（false）。
- 跳过的源（无新货）：anthropic、import-ai、the-batch、ahead-of-ai、karpathy、lilian-weng、thinking-machines、chip-huyen。
