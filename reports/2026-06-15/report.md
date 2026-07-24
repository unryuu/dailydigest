# AI 日报 · 2026-06-15（周一）

> 流水线：scout subagent 全量扫 15 源 → manifest → 3 个 reader subagent 并行精读 → reduce。
> 精读 3 条（金 2 / 银 1），雷达 3 条。周一锚点 Import AI 461 命中。中间产物见同目录 `manifest.json`、`digests/`。

## 🥇 金牌 · 头条精读

### [AI 的两道安全防线都在「裸奔」，专家还吵了起来](https://importai.substack.com/p/import-ai-461-alignment-is-not-on) · Import AI 461（Jack Clark）+ Interconnects（Nathan Lambert）· 2026-06-14~15
**为什么值得看**：同日两篇重量级长文，结论一致——给 AI 兜底的两道防线（技术上「让 AI 不跑偏」、监管上「政府怎么管」）现在都靠不住；更有意思的是两位作者对「AI 危险被高估还是低估」吵了个正反相反。下面用大白话拆：
- **Clark / Sequent（对齐落后）**：借新成立的对齐机构 Sequent（首轮募资 $100–150M）之口——实验室经验性安全程序「不太可能在训练 ASI 之前先验地给出『一切会顺利』的信心」，现有方法「本质反应式」，缺「对齐能从受控训练泛化到不可控部署」的原则性理由。
- **Lambert（治理换挡）**：当下是「智能体推理」时代，旧权力结构因失控感仓促出手——权重出口禁令、封锁外国研究员、对已部署模型「武断暂停」、由政治行为者做「临时技术评估」。反鹰派：「外国人不能在美国用前沿 AI 构建，就不存在本土 AI 产业。」
- **最拧的钩子**：两人都说「在裸奔」，但方向相反——Clark 怕风险被**服务不足**，Lambert 偏认为风险被**高估**、是实验室多年「危言耸听」招来这套粗糙政治管控。Lambert 还警告开源派：为这次封禁「疯狂庆祝」的人，等聚光灯转到自己头上「根本没准备好」。
- 附带料（已按降权处理、未进正文）：FrontierCode（Cognition 的硬编码编码基准，Diamond 档 Opus 4.8 仅 13.4%）、AARRI-Bench（「合成研究实习生」，含拒绝篡改实验数据的学术伦理题）——属评测类，仅存档备查。
- 与近期关系：Fable 停用连报四天，本组**只取 Lambert 的宏观治理判断**（「新常态的发令枪」），不复述停用经过/越狱/Amazon 游说。

### [里约市政府的「自研」大模型，其实是套壳 merge](https://github.com/nex-agi/Nex-N2/issues/4) · GitHub Issue（Nex-AGI）· 2026-06-14 · HN 374 票
**为什么值得看**：经典「政府机构自研大模型翻车」剧本 + 权重数学指纹实锤 + 被告改 README 半认账，三件套同时成立。
- 里约下属 IT 公司 IplanRIO 在 HF 发布号称自研的 397B 模型 Rio-3.5-Open；Nex-AGI 指控它是 **Nex-N2-Pro + Qwen3.5 按约 0.6 / 0.4 的逐张量加权 merge**。
- **证据一（行为）**：去掉硬编码「You are Rio」提示后问底层权重「你是谁」——答 Nex 占 79.2%（95/120）、答 Rio 占 0%，并背出 Nex 私有的组织背书水印文案。
- **证据二（权重，决定性）**：每层每张量对 Nex/Qwen 共线性 cos_fit ≈ 0.98–0.99（独立模型应 ≈0），α 跨 60 层稳定在 0.571±0.0016——离随机几千~几万个标准差，任何人可复现。
- **被告半认账**：曝光后 IplanRIO 悄悄改 HF README 承认是 merge + On-Policy Distillation，并致歉称「上传错了版本」（传成 base merge）。
- ⚠️ 仍有争议（已分清，未当实锤）：① 是否真做过自主训练/蒸馏——口头声称但当前权重无痕迹、未经第三方验证；② 是否花公款——市长推文称「用公共资金训练」，另有人称没花公款，口径打架未定论。

## 🥈 银牌 · 非头条精读

### [AI 没替代软件工程师，而且不会](https://simonwillison.net/2026/Jun/14/why-ai-hasnt-replaced-software-engineers/) · Simon Willison 转发背书 · 2026-06-14
**为什么值得看**：逆「工程师要失业」恐慌叙事。⚠️ **核心论证与数据均出自 [Arvind Narayanan & Sayash Kapoor（normaltech.ai）](https://www.normaltech.ai/p/why-ai-hasnt-replaced-software-engineers)**，Simon 是转发背书 + 补一条实操观察，别把框架记到 Simon 头上。
- **硬数据（N&K）**：2025-03 纽约成为全美首个在 WARN Act 裁员备案加「是否因 AI」勾选框的州；首年逾 160 家公司提交通知，**没有一家**勾选 AI。
- **论证（N&K）**：软件工程被公认最该被 AI 颠覆，连它都没被替代——AI 强在「敲代码」一段，而这从不是瓶颈；真瓶颈三处 AI 绕不过：决定造什么、验证并负责、对代码库与业务的深层人类理解。
- **Simon 原创的一线话**：AI 在「决定」「验证」上也帮到他，但「给我全世界的 AI 辅助，价值仍取决于我对问题理解多深」。
- **诚实边界**：原文自抛开放问题——「随着能力提升，调试会不会也被自动化？」未一口否死未来自动化。

## 雷达（terse）

- [Anthropic's Safety Superpower](https://stratechery.com/2026/anthropics-safety-superpower/) · Stratechery · Hacker News（136 分）— 把「安全」读成 Anthropic 的战略护城河；Fable 线的邻近评论，与 06-10 已报的 Lambert「护城河」判断有重叠，留雷达不升精读。
- [通过 Claude SDK 调用 Apple 端侧 Foundation Models](https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/apple-foundation-models) · Hacker News（275 分）— 端侧模型接入文档。
- [OpenRouter Fusion API](https://openrouter.ai/openrouter/fusion) · Hacker News（103 分）— 产品发布，降权一眼。

---
## 运行健康
- scout 全量扫 15 源、0 抓取失败；周一锚点 Import AI 461 命中。精读短名单 3 组（group-1 重·治理对齐；group-2 中·Simon 工程师；group-3 轻·里约假 LLM）→ 派 3 个 reader。
- 定牌：金 2（治理对齐宏观，双高权重源 + 范式张力；里约假 LLM，乐子硬 + 数学指纹 + 半认账）、银 1（工程师，论证归属 N&K、Simon 背书）。
- 防重复奏效：Fable 主线连报四天，group-1 只取 Lambert 宏观治理判断，未复述已报事实。Stratechery「安全=护城河」与已报 Lambert 判断重叠，按主线饱和留雷达未升精读。
- 权重应用：FrontierCode / AARRI 评测类按降权未进正文；OpenAI Partner Network、HF Eyas 黑客松稿、Simon Julia Evans 引文均未收。
- reader 抓取边界（已诚实标注）：group-2 更正核心论证归属（N&K 非 Simon）；group-3 把「merge 已坐实」与「是否训练/是否花公款仍争议」分清。
- 写入 / 更新 seen（reported=true 进报 / false 扫到未收）：
  - import-ai +1：461（金,true）。
  - interconnects +1：agi-era-of-ai-governance（金·源,true）。
  - simon-willison +2：why-ai-hasnt-replaced-software-engineers（银,true）、julia-evans 引文（false）。
  - hacker-news +4：rio-homegrown-llm-merge（金,true）、anthropics-safety-superpower（雷达,true）、apple-foundation-models（雷达,true）、openrouter-fusion（雷达,true）。
  - openai +1：partner-network（false，合作稿）。
  - huggingface +1：eyas（false，黑客松小品）。
- 跳过的源（无新货）：anthropic、thezvi（top 全是已报透的 Fable）、deepmind、the-batch、ahead-of-ai、karpathy、lilian-weng、chip-huyen、thinking-machines。
