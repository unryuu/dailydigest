# AI 日报 · 2026-07-05（周日·独立日长周末·淡日）· 长图第二期

> 流水线：scout（Claude，全量 21 源，新五分区）→ manifest → 3 reader 写金银 digest + 1 小 agent 抓 4 条 how/why 解读 → **主 Claude 写 daily.json 金银正文 + 赔率盒子（codex 写手本期退役，改主 Claude 直写）** → 用户改语气 → 渲染长图 → 发频道。
> 终稿：金 1 / 银 2 / 真雷达 4 / 今日乐子 4 / 赔率 3。周日官方源全静默，如实报淡日。
> **流程简化（07-05 起）**：金银摘要改由主 Claude 直接写进 daily.json、用户改语气；不再走命令行 codex（省沙箱 1223/BOM/PS 编码来回）。

## 🥇 金牌
### [更强的模型反而更不会用自定义工具（被 RL 练得只认自家工具）](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/) · Armin Ronacher · 2026-07-04
- Armin 实测：Opus 4.8 / Sonnet 5 在**自定义**编辑工具 schema 上反比老型号更爱塞不存在的字段（requireUnique/oldText2 等），多轮 agentic 约 20% 失败率，但真正的 oldText/newText 值是对的。
- 两个开关：剥掉 thinking 失败率减半；开 Anthropic 的 `strict` 模式（采样层禁止 schema 外 key）直接清零。老 Codex 模型没这退化。
- 归因＝RL 拿 Claude Code 自家扁平且容错的编辑工具猛练、学会「稍微调错也拿 reward」，别人家正确 schema 反像被隐性惩罚。同周 GPT-5.5 Codex 也冒出 reasoning token 聚集（516/1034/1552 边界，占比 82%）导致退化的怪现象，双厂商撞频。跟「模型越强越好用」主流拧着来。

## 🥈 银牌
### [Simon 用 Fable 写完 sqlite-utils 4.0 发版，算了笔账约 149 美元](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/) · Simon Willison · 2026-07-05
- 一次真实开源发版明码标价 $149.25，逐 agent 拆分（主会话 claude-fable-5 $141.02 + 几个 review 子 agent 各几块 + 一个「数 prompt」的 opus-4-8 花 $0.32）。Fable 干 37 prompt/34 commit（含事务语义重构、`delete_where()` 丢数据 bug 修复），Simon 评 release notes「比我自己写的还好」；用 GPT-5.5 交叉复核逼出两个 P1。
- 配套：让 Fable 自己判断把子任务派给更便宜模型（sonnet 干实现、haiku 干琐活）省预算——成本分配从人拍板变模型自主。与 07-03 Simon 三连切割（只取账单数字 + 自我调度）。

### [对齐 vs 控制之争：给「控制 AI 能撑多久」画了条又窄又先失效的线](https://www.lesswrong.com/posts/dmHbogCFbSp95J3Lz) · LessWrong / Alec Harris · 2026-07-03
- 翻译：控制＝假设 AI 可能坏、用蜜罐/权限/探针从外面兜住（Redwood、Anthropic 一系）；对齐＝直接改训练让 AI 打心底想做对。作者押对齐（配比 8:1）。
- 硬货＝把「控制窗口」量化成又窄（AI 越聪明控制越难、指数级，0→80/20 控制只把接管门槛从 200ip 抬到 225ip）+ 又偏左（控制比对齐先失效，因为 AI 学会搞串通骗监控比人识破快）。一句戳心：控制是跟越来越强的敌人打，对齐是跟不会还手的材料打。本期没收 Zvi（无更新），不撞车。

## 真雷达（4）
Current AI 开源全景 Gap Map（421 产品分类）· 前端课程作者收入腰斩半归因 AI · The Log Is the Agent（日志即 agent，带 what 解读）· Claude 设计系统提示词逆向 repo。

## 今日乐子（4）
445 字节画世界地图（how：压缩，海陆好压）· Yudkowsky 虚构世界 dath ilan 性别（只标题）· 解酒益生菌 ZBiotics 小 RCT（what：28 人、结果没用甚至略重）· ORM 不如直接学 SQL（why：反正都得懂 SQL）。

## 赔率盒子（3·只留昨天没出现的新市场）
2028 成堕胎级政治议题 89% vs 2028 前 GDP 出现 AI 拐点 38%（政治要炸、经济没影）· 灭绝人类 2100 前 13.9%。（用户定：昨天报过的今天不追，变化大再报。）

---
## 运行健康
- 周日独立日长周末，官方源（Anthropic/OpenAI/DeepMind/claude-blog/HF papers）全线静默，新货只有 Simon 一串 + LessWrong 几帖 + HN 两三条，如实报淡日。scout 全量扫 21 源、0 抓取失败。
- 3 reader（Better Models Worse Tools / Simon Fable 成本 / LW 对齐 vs 控制）+ 1 小 agent 抓 4 条 how/why（445 字节地图/ZBiotics/日志即 agent/ORM，忠实、含 ORM 修真链接 wozniak.ca）。
- **写手＝主 Claude 直写（codex 退役）**：金银正文 + 赔率盒子由主 Claude 写进 daily.json，用户改语气多轮（正文逐步压短：金 502→366、银 336→236/289→227），主 Claude 每轮验 JSON + 重渲。
- 赔率盒子去重：昨天报过的 IMO/Annals/电影/灭绝2030 今日剔除，只留新市场（堕胎级/GDP 拐点/灭绝2100）。
- 验收：金 2 段、银各 1 段；0 破折号、0「反直觉」、无 `<br>`/裸引号/裸 `<>&`；长图 1179×7731 发附件。
- seen 回写（report_date 2026-07-05）：hacker-news +4（Armin lucumr/Log Is Agent/Claude Design/ORM wozniak）、simon-willison +4（Fable 成本/Gap Map/Josh Comeau/445 字节地图）、lesswrong +3（对齐 vs 控制/Yudkowsky/ZBiotics）。Manifold 不做 seen。
- 跳过的源：thezvi（Fable #6/AI #175 已报）、anthropic/openai/claude-blog/deepmind/the-batch/import-ai/interconnects/acx/hf-papers/ahead-of-ai 全静默、月检四源无货、axios（Fable 复活内幕撞饱和主线）。
- 待办照旧：新源 LW/ACX/Manifold 试跑对齐品味中；sources.md 待同步 21 源新口径。
