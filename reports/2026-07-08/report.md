# AI 日报 · 2026-07-08（周三）· 长图第五期

> 流水线：scout（21 源，五分区）→ 3 reader 写金银 digest + 1 小 agent 核 5 条雷达/乐子链接与 body → 主 Claude 直写 daily.json → 用户编辑（删字、砍 body）→ 发频道。
> 终稿：金 1 / 银 3 / 真雷达 6 / 今日乐子 3 / 赔率 4。
> **空字段处理**：用户把部分雷达/乐子 body、赔率 note 删成空串；渲染器遇空 body/note 自动跳过，落盘时统一删掉空字段（留不留渲染一致）。
> **金牌笔误**：用户版金牌正文「自我爹地」判定为「自我改进」误输，发布前已修正并告知用户。

## 🥇 金牌
### [Lilian Weng 长文：把「AI 自我改进」拆成一门工程](https://lilianweng.github.io/posts/2026-07-04-harness/) · Lil'Log · 2026-07-04
- 停更后首更（前 OpenAI 安全负责人、Thinking Machines 联创，源设定「一更必进头条」）。核心：近期 AI 变强改的不是权重，而是身外那套跑它的 harness（训练流水线+部署系统+工具+评测）。RSI 循环＝模型改进流水线→训出更强下一代→再改流水线。
- 追到 I.J. Good 1965「超智机器」，落点从「机器自己重写自己」改成「机器改进跑自己的外部程序」；用代码而非 prompt 当基底、设计空间大到能让编程 agent 搜索更优解＝harness engineering。与近期 Fable 写 kernel（RSI 实锤）错位——她给整条线补框架。

## 🥈 银牌（3）
- [两篇 LessWrong：表面信号不代表深层人格](https://www.lesswrong.com/posts/aTybJ6CPQrxEY8rE2/data-filtering-works-a-lot-worse-than-you-would-expect)：① Neel Nanda 组用最强数据归因删「坏行为文档」，删了不如随机删（坏行为不定域在文档、是 SFT 唤醒的潜伏人格，纯代码窄训照样冒）；② Personascope 测「入戏深度」，99% 入戏当伏地魔但行为纹丝不动，Claude Haiku 4.5 最不肯入戏（0.35）。与 07-07 Tie training 区分（加法治信号权重 vs 坏行为不在文档里）。
- [Anthropic 手册：Claude Code 选模型/调 effort](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)：「没使劲 vs 没知识」二分法——没知识换大模型、没使劲调高 effort；模型三档 Sonnet 常规/Opus 难题/Fable 多步。
- [Claude Cowork 用法数据](https://claude.com/blog/how-people-are-using-claude-cowork)：扩到 web/mobile + 进政府（FedRAMP High）；120 万会话数据里业务运营 33%/内容 16%/软件开发仅 8.7%，agent 平台九成干非编码办公活。

## 真雷达（6）
Trump 政府取消 GPT-5.6 访问限制本周四公开发（反转白宫逐案批准）· GitLost 提示注入诱导 GitHub agent 泄露私有仓库（HN 321，带 body）· Google 开源 Gemma 4（原生多模态，最大 31B）· 具身世界模型三连霸 HF 榜（RynnWorld/AlayaWorld，带 body）· 腾讯开源 Hy3 295B MoE（带 body）· Kokoro 82M 本地 CPU TTS（HN 448，带 body）。

## 今日乐子（3）
优衣库 T 恤混淆 bash 脚本＝和平彩蛋动画（HN 645）· 大一学生把 Ilya 30 篇必读做成可视化版 · ACX 书评 Joseph Smith 莎草纸真伪公案。

## 赔率盒子（4·全新盘）
数学前沿张力对：2030 前 AI 独立构造国际象棋证明 47.8% vs 2028 前 OEIS 稳胜数学家 35.8% · 2026 底 AI 相关核电 15GW 36.6% · 2030 前限制自主武器国际条约 33%。

---
## 运行健康
- 周三厚日。scout 全量扫 21 源、0 抓失败。头条 Lilian Weng 停更后首更（一更必进头条，seen 未收）。thezvi 无 AI #176（最新 No Space Like J-Space 属 J-space 主线延伸、饱和未收）。
- reader：group-1（Lilian Weng harness 工程学，与 RSI 实锤错位）、group-2（Cowork 三连轻银/雷达 + 选模型手册轻银）、group-4（表面信号双论文，Data filtering 主推银）。1 小 agent 核 5 条链接/body（GitLost/Kokoro/Gemma4/优衣库/Ilya30，全给真实 URL；无编造）。
- **写手＝主 Claude 直写**：金银按 07-07 新口味写（直接陈述、不用「拧/反直觉/有意思的是/最X的是」、少「xx的是xx」、少点评）。用户编辑：大删字、砍部分 body 成空、修 Cowork 标题。
- 空字段：用户留了空 body/note，渲染器遇空自动跳过；落盘删空字段（渲染一致）。金牌「自我爹地→自我改进」笔误发布前修正并告知。
- 赔率去重：避开近四天报过的（政治议题/AI 歌/AI 打游戏/Yud/低质电影/开源 IMO/AI 恋人/刺杀 CEO 等），换新盘（象棋证明/OEIS/核电/自主武器）。图 1179×8379 发附件。
- seen 回写（report_date 2026-07-08）：lilian-weng +1（harness）、lesswrong +2（data filtering/personascope）、claude-blog +2（选模型手册/Cowork 用法）、hf-papers +2（Gemma4/具身世界模型）、simon-willison +1（Hy3）、acx +1（书评）、hacker-news +5（GPT-5.6 反转/GitLost/Kokoro/优衣库/30papers）。Manifold 不做 seen。
- 跳过：thezvi（无 #176）、import-ai（464 已报）、interconnects/openai/deepmind/the-batch/ahead-of-ai 无窗内新货、月检三源。Cowork 三连里 web/mobile 与政府两帖并入用法数据一条、未单列。
