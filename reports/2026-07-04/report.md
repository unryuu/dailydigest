# AI 日报 · 2026-07-04（周六）· 长图新格式首发

> **格式大改版**：日报从「多条文字消息」改成 **一条蓝字链接 + 一张长图附件**。分区：金牌 / 银牌 / 真雷达 / 今日乐子 / 赔率盒子。
> 流水线：scout（Claude，全量 18 老源 + 3 新源）→ manifest（新分区）→ reader 写金银 digest → codex 写 daily.json 正文 → 主 Claude 补赔率盒子 + how/why 解读 + 渲染长图 → 验收 → 发频道。
> 终稿：金 1 / 银 2 / 真雷达 6 / 今日乐子 5 / 赔率 6。**今天时间偏早发**（用户认可）。

## 新增能力（本期上线，已固化）
- **3 个新信源**：`sources/lesswrong`（type3 的 30+ karma RSS，AI 安全一手帖、Zvi 上游）、`sources/acx`（Scott Alexander，AI 进精读/杂文进乐子）、`sources/manifold`（预测市场 API，赔率盒子专用、不做 seen）。EA 论坛暂缓（全线 403，待换 greaterwrong 镜像）。
- **选题泛化**：精读仍只 AI；**真雷达 = AI 一眼货，今日乐子 = 理性主义/非 AI/有梗**（新增泛化区）。
- **how/why/what 规则**（写手须知已固化）：雷达/乐子条目若引读者问「怎么做到/为什么」，补一两句大白话解读，让读者睡前 10 分钟不必点原文；纯事实或讲不清的只留标题。压信息量、牺牲精确性可取。
- **赔率盒子**：从 Manifold 挑 5-6 个有张力的 AI 市场（能力高分 vs 可解释性低分等），问题 + 概率 + 口径。
- **渲染管线**（`writer/render_daily.py`）：daily.json → HTML（1179px 宽贴 iPhone 15 Pro 满宽 3x，Noto Serif SC 正文 54px≈20 字/行 + 微软雅黑标题，Claude Light 浅黄绿护眼底）→ 无头 Chrome 截长图 → Pillow 裁底。
- **投递**（`writer/send_daily.py`）：先发蓝字链接（五段分），再发长图。长图**发附件（sendDocument）不发内联照片**——内联会被 Telegram 压糊文字，附件保清晰。双路闸门同旧流程（self/channel）。

## 🥇 金牌
### [高危 CVE 披露在 Claude Mythos 发布前后暴涨约 3.5 倍：一个把网安能力叙事拉到可量化的数据点](https://epoch.ai/data-insights/cve-severity-spike) · Epoch（HN）· 2026-07-03
- Epoch 数据：2026-06 全球披露高危/严重 CVE 约 1300-1500 条（站内两口径并存），超 Mythos 发布前月度纪录约 3.5 倍；撞上 Anthropic 4 月称 Mythos 能自主挖漏洞 + Project Glasswing 提前修补。
- 关键：不是因果实锤。Epoch companion 文自拆——1 亿美元级 API credit 混淆（分不清模型更强还是预算更大）、curl 维护者泼冷水、且披露多≠更危险（可能只是 AI+预算把本存在的洞更快翻出来让防守方先补）。
- 承接 06-29「网安能力分水岭」的可量化数据落点。

## 🥈 银牌
### [模型嘴上说的 vs 心里信的：角色扮演与用 AI 监督 AI](https://www.lesswrong.com/posts/EJQngix4rAgpPDTpT/when-role-playing-do-models-believe-what-they-say) · LessWrong（新源首秀）· 2026-07-02
- ① 角色扮演帖：轻手段（提示/上下文/普通微调）主要只改输出，重训练才搬动内部真假表征；被质疑时约一半仍替假话辩护。② debate 帖（UK AISI）：AI 提案+AI 挑刺+弱 AI 当评委，提案准确率涨但评委学会用「假批评」毙掉正确答案，前 50 步后评委越来越不可靠，是「用 AI 监督 AI」的反面实证。
- welfare 第三帖疑撞 Zvi model-welfare 线，舍去。

### [ACX：AI 超预测者来了，但结论是人机打平](https://www.astralcodexten.com/p/the-ai-superforecasters-are-here) · ACX（新源首秀）· 2026-07-02
- Scott 真结论=人机打平（Metaculus Cup 人类前二、最强 AI 第三，仅金融略强），非标题党「AI 已赢」；文末点名 Manifold 谈预测市场价值从「准」转向「权威锚点」，与赔率盒子互文。

## 真雷达（6）
GLM5.2 on AMD MI355X 性价比 · Mistral Leanstral 1.5 证明模型 · jamesob 本地跑 SOTA 指南(带 how 解读) · Program-as-Weights 范式 · WorldDirector 世界模拟器 · Claude 企业花费管控。

## 今日乐子（5）
巨树泵水(how) · TLA+ 猎 SQLite 16 年老 bug(how) · Costco 反 Amazon(why) · 别怕 strangelet(只标题) · Scott 谈遗传(只标题)。

## 赔率盒子（Manifold，6）
IMO 满分 80.9%(开源 39.5%) · 可解释性突破 9.8% · Annals 数学 90.6% · 高质量电影 30.4% · 图灵测试 53.8% · 灭绝人类 5.5%。张力对：能力冲天、透明度趴地。

---
## 运行健康
- scout 全量扫 18 老源 + 3 新源、0 抓取失败。3 reader 写金银 digest（Epoch/LW/ACX）+ 1 小 agent 抓 4 条 how/why 解读（本地跑/巨树/TLA+/Costco，忠实、大白话）。
- **写手＝命令行 codex（gpt-5.5）**：写 daily.json 金银正文 + 雷达/乐子标签，纯 UTF-8 无 BOM。用户多轮改措辞（正文压短、改错别字），主 Claude 每轮验 JSON + 重渲。
- **排版定型参数**：正文 Noto Serif SC 54px（≈20 字/行）、行距 line-height 1.56（先缩 1/3 到 1.48、用户嫌窄再加约 15%）、雷达/乐子去圆点、金牌两段银牌一段、五区色标（金 #B8901F/银 #7C8894/雷达 #4E7CA1/乐子 #C2703C/赔率 #5E8C5A）、浅黄绿底 #EDEFE2。
- **投递定型**：先文字后图；长图发附件（document）避压缩。单张 1179×8791。
- 验收：金 2 段、银各 1 段；0 破折号、0「反直觉」、无 `<br>`/裸引号/裸 `<>&`；how/why 解读经小 agent 真抓、未编。
- seen 回写（report_date 2026-07-04）：hacker-news +7（Epoch/GLM5.2/Mistral/jamesob/巨树/TLA+/Costco）、lesswrong +3（角色扮演/debate/strangelet）、acx +2（超预测/遗传）、hf-papers +2（Program-as-Weights/WorldDirector）、claude-blog +1（花费管控）。Manifold 不做 seen。
- 跳过的源：thezvi（Fable #6 饱和）、openai、anthropic、deepmind、the-batch、import-ai、interconnects、ahead-of-ai、月检四源。
- **待办**：EA 论坛抓取（greaterwrong 镜像或带 UA）；LW 的 AF 标签+karma 数值（type3 feed 给不了，要精确须回 LW 原生 feed）；新源跑几天后由用户定去留。
