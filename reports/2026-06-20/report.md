# AI 日报 · 2026-06-20（周六）

> 周末淡日。流水线：scout 全量扫 16 源 → manifest → 3 reader 初评 → reduce → 用户反馈后 reduce 二轮（补派 4 reader 读雷达候选）。
> 精读 3 条（金 1 / 银 2），雷达 4 条。导读按规范：大白话 + 少破折号。
> **编辑说明**：初稿精读为「G7/Trump 治理 + 挪威禁 AI + 现代收波士顿动力」，用户判断政治/收购类偏闷、雷达里的技术/怪味条目更对味，遂对调——技术三条升精读、政治/收购三条降雷达。升精读前已补派 reader 真读，其中 Cloudflare 一条经 reader 判为产品公告、撑不起精读，仍留雷达。

## 🥇 金牌 · 头条精读

### [一个 MIT 开源小模型，幻觉率把最大的闭源旗舰按在地上摩擦](https://arrowtsx.dev/bigger-models/) · Oliver Shrimpton 个人博客 · 2026-06 · HN 353
**为什么值得看**：反直觉——越大、跑分越高，不等于越靠谱。开源 GLM-5.2 在「幻觉率」上反超最大的闭源旗舰。
- 第三方 AA-Omniscience 幻觉率（越低越好，从低到高）：GLM-5.2 28%、Opus 4.8 36%、Fable 5 48%、GPT-5.5 86%、DeepSeek V4 Pro 94%。「幻觉率」=答不出时不说「不知道」、自信编答案的比例。
- asyncio 案例：给一道故意无解的题，DeepSeek V4 Pro 烧近 10 倍 token 仍自信给错；GLM-5.2 约 12 秒 / 800 token 看穿其逻辑不成立。
- 论点：不是「小模型更好」，而是「大不自动等于强」；大模型商品化在模糊「跑分」与「真实准确性」的界线。框成 LLM 三难（原始能力 / 校准 / 算力效率不可兼得）。
- ⚠️ 方法论窟窿：个人博客，定量引自第三方平台但无统计显著性、无原始数据，定性只有 asyncio 一例（轶事证据）。当有意思的信号看，别当定论。复现条件：均 high 推理、temp 1、同 system prompt、走 OpenRouter。

## 🥈 银牌 · 非头条精读

### [抛开停用风波，Fable 5 纯能力到底强在哪](https://thezvi.substack.com/p/claude-fable-5-and-mythos-5-capabilities) · Zvi（Don't Worry About the Vase）· 2026-06-19
**为什么值得看**：Fable 主线八天全在吵停用/政治，这篇是同作者第一次只谈能力，补上「凭什么值得吵这么久」的另一半拼图。
- 判断：跑分上只是「世界最强、领先可观但非石破天惊」；但纸面温和领先，上手做长任务变成肉眼可见代差，越长越复杂领先越大。
- 最硬一手料：Taelin 让 Fable 优化自己写了几周的 HVM5 代码，2 小时拿到 1770% 加速、还揪出 Taelin 漏掉的关键 bug；Karpathy 称「值得大版本号的质变」，Boris Cherny 称它「有判断力、品味和维度」、从编码工具变思考搭子。
- 缺点 Zvi 没藏（五条）：可控性弱（决定不做就难掰回）、位置偏见仍在（选第一项 59%）、不重要的事爱瞎编、视觉推理卡住、安全分类器频繁误杀降级回 Opus 4.8。
- ⚠️ benchmark 具体分数二手转引未一手核对，只取定性（coding 领先最明显）；停用/政治旧料未碰。与金牌那条呼应「跑分≠真实表现」（方向相反：大模型更爱瞎编 vs Fable 体感超出跑分）。

### [《LLMs 变复杂了》：复杂的不是 API，是模型架构退回了「恐怖的图」](https://ianbarber.blog/2026/06/19/llms-are-complicated-now/) · Ian Barber（前 Meta）· 2026-06-19 · HN 96
**为什么值得看**：反直觉——外界说「LLM 复杂」指 API/路由，作者把矛头指向模型骨架本身，说它正退化成当年推荐系统那张「恐怖的计算图」。
- 复杂化清单：注意力一堆变体（分组/压缩/稀疏/线性/滑窗）+ MoE 路由 + routed attention + 内置多模态编码器 + 多卡通信算子。
- 要害判断：性能优化从「锦上添花」变「承重墙」，反把架构创新卡死——换注意力变体能忍慢 10%，忍不了慢一个数量级；优化又与架构焊死，新想法没基线、没人敢提交。
- 处方：一开始就为「可组合性」设计；点名 PyTorch FlexAttention 为正面例子（Triton 模板自动生成 kernel，可验证又能做架构探索）。
- ⚠️ 纯观点、无新事实/数据。

## 雷达（terse）

- [特朗普：Anthropic「一周前也许是国安威胁，现在不是了」+ G7 把三家 AI CEO 当元首同桌](https://www.axios.com/2026/06/19/trump-anthropic-national-security-the-axios-show) · Axios · 2026-06-19~20 — 当日最大政治新闻，按用户口味降雷达。两篇 Axios 403，多源交叉。
- [挪威给小学 AI 踩刹车：1–7 年级原则上禁用（分学段，非全面禁）](https://www.engadget.com/2198117/norway-imposes-broad-restrictions-on-ai-for-elementary-school-kids/) · Reuters/Engadget · Hacker News（750 分）— 继 2024 禁手机后再限 AI，理由是别让低龄娃跳过读写算地基。
- [软银 3.25 亿清仓波士顿动力，现代 100% 全资控股](https://www.globalbankingandfinance.com/hyundai-buy-softbanks-remaining-stake-boston-dynamics-325/) · Reuters 系 · Hacker News（895 分，当日榜首）— 现代早已控股，这次是软银行使回售期权清最后 9.65%；隐含估值约 34 亿美元。
- [Cloudflare 给 AI agent 发临时账号](https://blog.cloudflare.com/temporary-accounts/) · Cloudflare · 2026-06-20 — 一条 `wrangler deploy --temporary`，解决 agent 卡在人类登录流程；reader 判为产品公告、撑不起精读，留雷达。

---
## 运行健康
- 周末淡日。scout 全量扫 16 源、1 抓取失败（Axios G7 正文 403，摘要从 RSS 取得）。
- 流程特殊：初稿金 1 银 2（G7/Trump、挪威、现代）；**用户反馈政治/收购偏闷、雷达更对味，要求对调**。reduce 二轮补派 4 个 reader 真读雷达候选，3 条够料升精读（GLM 幻觉率、Zvi 能力篇、LLMs 变复杂了），Cloudflare 一条 reader 判为产品公告维持雷达，原 3 条政治/收购降雷达。
- 终稿定牌：金 1（GLM-5.2 幻觉反超，反直觉但方法不严谨，已标注）、银 2（Fable 能力篇、LLMs 变复杂了）。
- reader 抓取/校验边界（已诚实标注）：GLM 那条方法论窟窿单列；Fable 能力篇 benchmark 数字二手未核、只用定性 + 避开停用旧料；现代纠正「首次收购」误读、挪威纠正「全面禁止」误读；G7/Trump 两篇 Axios 403 多源交叉、弱引语降级。
- seen 无新增改动：7 个进报条目（含降雷达的 3 条）此前均已写入 seen 且 reported=true，分档调整不影响 reported 状态。
- 跳过的源（无新货）：anthropic、openai、deepmind、interconnects、the-batch、import-ai、ahead-of-ai、karpathy、lilian-weng、thinking-machines、chip-huyen。
