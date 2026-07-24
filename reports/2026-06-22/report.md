# AI 日报 · 2026-06-22（周一）

> 流水线：scout 全量扫 16 源 → manifest（3 精读候选 + 5 雷达候选）→ 3 reader 并行精读 + 1 verifier 核雷达 → reduce 定牌。
> 终稿精读 3 条（金 1 / 银 2）+ 雷达 2 条。导读按规范：大白话 + 少破折号。
> **编辑说明**：① Sakana Fugu 初为雷达，verifier 核出它今天 GA、有梗（编排对手模型、只按最贵档收费、拿不在池里的 Fable/Mythos 对标、强调不受出口管制），按「乐子条目升精读」升银。② 两个 Gemma（DiffusionGemma 06-10、Gemma 4 06-03）经 verifier 坐实日期后判定出窗，丢弃、deepmind seen 标 reported=false 防再现；sqlite-utils 非 AI 范式同丢。③ 数据中心民意那条 reader 给到银档料，但偏民意/监管、按用户口味压成雷达一句（保留展开升精读的选项）。

## 🥇 金牌 · 头条精读

### [Import AI #462：AI 的「超说服力」被大规模实验坐实，反转在后半句](https://importai.substack.com/p/import-ai-462-superpersuasion-self) · Import AI（Jack Clark，Anthropic 联创）· 2026-06-22
**为什么值得看**：反直觉双钩。① AI 不是「差不多有说服力」，而是连经 AI 反馈训练的 43 名精英辩手都追不上、募捐场景近 3 倍于职业募捐员；② 但优势来源很「笨」，纯靠单位时间砸信息量，一限速限字数，+4.1pp 优势直接塌到 0.0pp（不显著）。
- 实验规模：牛津 / 英国 AI Security Institute / 斯坦福 / LSE 跨机构团队，政策议题 + 慈善捐款两类任务，18,978 场对话、6,923 人。原文「AI systems were reliably more persuasive than expert humans」，能同时把人导向正确与错误答案。
- 赢过谁：依次压过随机普通人、锦标赛筛出的普通人、精英辩手；给 43 名精英辩手配 AI 反馈做教练仍追不上。募捐实验对阵英国某职业募捐公司，在 Save the Children 捐款上多撬动「+10.8 pp of the £1 bonus」、「nearly 3x more effective」。
- 优势 = 信息量：「advantage stemmed from rapidly deploying larger quantities of information」；强制人类长度+打字速度后「collapsed from +4.1 pp to a non-significant 0.0 pp」。
- Clark 治理落点：监控说服性 AI 的使用、警惕它改变权力平衡；交市场→广告负外部性，交政府→权力集中、威权政体下尤危。顺势接 DeepMind「AGI→ASI 四路径」论文（堆算力 / 算法跃迁 / 递归自我改进 RSI / 多 AI 群体智能），Clark：「co-creation RSI 已启动」，但当下仍缺范式级创造力，结果「可能爆发、可能渐熄」。
- ⚠️ 边界：原文点名 Opus 4.6 / GPT-5.4 / Grok 4.20 等偏未来版本号（两次抓取一致，落地引用保守，导读已回避具体版本号）。承接 #414（2025-05，1242 人小样本）的**实锤升级版**，非旧事重炒。派活 URL slug 404，正确为 `...-462-superpersuasion-self`，已读到正文。

## 🥈 银牌 · 非头条精读

### [开源模型从「跑分逼近」走到「采用侧逼退」：社区真的开始换模型了](https://thezvi.substack.com/p/glm-52-is-the-new-best-open-model) · Zvi（骨架）+ HN cancel_claude / techstackups 实测 · 2026-06-21~22
**为什么值得看**：反直觉——喊「取消 Claude」那篇的真实迁移触发点不是开源变强，而是受不了 Claude 的实名+年龄验证（即 06-21 那条监管摩擦）。采用侧的拐点是「政策摩擦先到、能力平价没到」，跟「开源跑赢所以转投」的爽文叙事拧着。
- Zvi 定位（高可信骨架）：GLM-5.2 是「当前最强开源」，但仍明显落后绝对前沿 4–7 个月、区间在 Opus 4.5–4.7；蒸馏自 Claude→「benchmark 超常、冷门任务掉链子」、无原生视觉、对话偏弱。Zvi 全文**不背书「该换」**，引 Theo 测算「Opus 4.8 / GPT-5.5 设 medium 都比 GLM-5.2 又便宜又聪明」。
- 社区情绪（cancel_claude，HN 313 分，二手当「有人主张」用）：类比「Linux vs Windows 差距基本消失」，但对「换了用哪个开源模型/什么 workflow」含糊；诚实承认本地跑「贵、复杂、慢」，生产力短期会掉。触发点是实名政策摩擦。
- 真实横评（techstackups，HN 305 分，经核为真测非垃圾页）：同一 prompt 从零写 3D WebGL 平台跳跃游戏，Opus 33m30s / GLM-5.2 1h10m40s，成本约 \$5.39 vs \$21.92；GLM bug 更扎眼（人物朝向反、贴图缺失），且纯文本无视觉没法自验——印证 06-20 的「无原生视觉」短板。
- ⚠️ 安全：scout 给的 `apertvs.ai`（带 v）判为 typosquat，未链接、不背书；真 Apertus 是 EPFL/ETH Zürich（swiss-ai）2025-09 旧发布，仅一句旁证、不单列。
- 与近期关系：承接 06-20（GLM 幻觉率 + Zvi 能力篇），但落点在【采用/市场侧】是新角度；Zvi 单篇与 06-20 有重叠，已仅作骨架反衬社区乐观，未复述跑分名次。

### [Sakana 今天上线 Fugu：用强化学习训一个「指挥」，把 GPT/Claude/Gemini 编成一队](https://sakana.ai/fugu/) · Sakana AI（HN 168）· 2026-06-22 GA（beta 自 04-25）
**为什么值得看**：有梗。它不是新模型，是一个 RL 训出的「Conductor」把多家公开前沿模型动态编成「思考者/执行者/校验者」协作（基于两篇 ICLR 2026 论文 TRINITY + Conductor），还自带几个反直觉卖点。
- 收费反直觉：多模型协作只按池中最贵那档收费、不叠加。
- 对标很皮：官方页把 Fugu 顶配跟 Fable 5 / Mythos Preview 并排比，同句又承认这俩不在自己池里（不公开可用）——拿够不着的对手贴金。
- 反复强调「不受出口管制风险影响」，暗示绕开闭源旗舰的地缘限制。
- 厂商自报数字（单方口径、当信号看）：SWE-Bench Pro 73.7；代码审查别人报约 3 个问题、它报 20+；某交易基准五次跑均值 +19.43%。
- ⚠️ verifier 提醒：首抓把 Conductor 误作「7B」、把对标误作 GPT-5.5，二次直读原页未证实（7B 来自二手转述论文，对标实为 Fable 5 / Mythos Preview）——导读已回避这两点未坐实信息。

## 雷达（terse）

- [数据中心成 AI 反弹的靶子：49% 美国人想暂停新建，同日 Nvidia 称水耗已基本解决](https://www.axios.com/2026/06/22/ai-data-center-backlash-poll) · Axios · 2026-06-22 — 反对者里仅 8% 住数据中心附近，更像对 AI 的泛化焦虑而非邻避（NIMBY）；做民调的 Milltown Partners 本身是给 AI 实验室做咨询的公司。同日 Nvidia 首席可持续官 Josh Parker 称暖液冷把「水耗挑战基本解决」，但承认全行业落地要数年、存量数据中心仍用旧冷却（杰文斯悖论味）。两篇 Axios 均 403，数字经 Yahoo 授权转载 + 多源交叉。reader 给到银档料，按用户口味压雷达，可应需升精读。
- [三星给员工全员上 ChatGPT 和 Codex](https://openai.com/index/samsung-electronics-chatgpt-codex-deployment) · OpenAI · 2026-06-21 — 大厂级企业部署 PR 稿，按规则降权，留一眼。

---
## 运行健康
- 周一常规日。scout 全量扫 16 源、0 抓取失败；产出 3 精读候选 + 5 雷达候选。reduce 派 3 reader 并行精读 + 1 verifier 核雷达候选，均回传扎实。
- scout 本期守红线表现好：把疑似关联（开源组承接 06-20、数据中心承接 06-18）都标「待 reader 核」而非武断下因果（对照 06-21 的纠偏教训）。
- reader/verifier 纠坑：① group-1 修正 Import AI URL slug（正确含 `-self`）；② group-2 把 scout 给的 `apertvs.ai` 判为 typosquat 拦下、WebSearch 验真 Apertus 后仅旁证；③ group-3 两篇 Axios 403、走 Yahoo 授权转载 + 多源交叉；④ verifier 坐实两个 Gemma 出窗（06-10/06-03）、Sakana Fugu 实为编排产品而非新模型并纠正首抓的「7B/对标 GPT-5.5」误读。
- 定牌：金 1（超说服力，高权重源 + 反直觉双钩）、银 2（开源采用侧、Sakana Fugu）、雷达 2（数据中心民意、三星 Codex）。Sakana Fugu 由雷达升银（乐子条目展开）；数据中心由银料压雷达（民意/监管偏闷，留升精读选项）。
- 丢弃并记 seen=false：DiffusionGemma（06-10 出窗）、Gemma 4 12B（06-03 出窗）于 deepmind；sqlite-utils 4.0rc1（非 AI 范式）于 simon-willison。
- seen 回写：import-ai（超说服力 reported=true）；thezvi（GLM-5.2 评 reported=true）；hacker-news（cancel_claude / techstackups / Sakana Fugu reported=true）；axios（数据中心两条 reported=true）；openai（三星 Codex reported=true）；deepmind（两个 Gemma reported=false）；simon-willison（sqlite-utils reported=false）。
- 跳过的源（无新货/出窗）：anthropic、interconnects（Lambert 禁开源 06-19 已报）、karpathy、lilian-weng、chip-huyen、thinking-machines、ahead-of-ai、huggingface、the-batch。
