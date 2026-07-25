# Anthropic 发布 Claude Opus 5：价格不动、知识截止反超旗舰，官方自评「不比 Fable 5 更强」

- 推荐强度: 强
- 档位线索: 金（全期头条）。理由不是「又一个模型」，而是三条可核到一手源的硬事实：① 官方自己在 System Card 里写「Opus 5 整体上不比 Fable 5 更强」，同时把它定价成 Fable 的一半；② 知识截止 2026-05，比它上面那个旗舰 Fable 5（2026-01）还新四个月；③ AECI 162.1 名义最高，但官方自陈与 Mythos 5 的 161.3「统计上无法区分」——二手站普遍把这个平手写成了夺冠。有对照表、有反例、有内测吐槽，够撑头条。
- 涉及文章:
  - [Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) · Anthropic 官方 · 2026-07-24（主证，全文读到）
  - [Claude Opus 5 System Card（PDF，194 页）](https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf) · Anthropic · 2026-07-24（全文抽取读到）
  - [What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5) 与 [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) · Anthropic 官方文档 · 规格与定价一手源
  - [Introducing Claude Opus 5](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/) · Simon Willison · 2026-07-24
  - [HN 讨论串 item 49038433](https://news.ycombinator.com/item?id=49038433) · 2026-07-24（我读到时 1581 分 / 923 评，派活时记录的是 1237 分 / 674 评）
  - [Artificial Analysis 榜单](https://artificialanalysis.ai/models) · live 榜单，2026-07-25 读到的名次
  - Ethan Mollick 三条推 · 2026-07-24（发布前内测视角，经 nitter 镜像读到）

## 核心主张

Anthropic 把 Opus 5 定位成「Opus 档的 step change」，卖点不是绝对能力登顶，而是**用 Opus 的价（$5/$25，与 Opus 4.8 一分不涨）买到接近 Fable 5 的智能（Fable 5 是 $10/$50）**。官方 System Card 在执行摘要第一句 RSP 结论里就写明「Claude Opus 5 整体上不比我们能力最强的通用可得模型 Claude Fable 5 更强」——这句自我设限在对照表里能一一对上：Opus 5 在 SWE-bench Pro（79.2 vs 80）、DeepSWE（68.8 vs 69.7）、FrontierCode（53.4 vs 53.5）、HLE 无工具（56.3 vs 56.5）四项上都**微弱落后** Fable 5。

真正拉开差距的是另一类任务：需要长时自主探索的。FrontierBench v0.1 从 Opus 4.8 的 21.1 跳到 43.3（Fable 5 只有 33.8），ARC-AGI-3 从 1.5 跳到 30.2（次优 GPT-5.6 Sol 只有 7.8），OSWorld 2.0 电脑操作 70.6（Opus 4.8 是 55.7），AutomationBench 26.0（其余全家 17—18）。**所以这次的形状不是「全面碾压」，是「在旧基准上打平、在新的长时 agent 基准上断层」。**

第三个被二手报道普遍漏掉的点：Opus 5 的知识截止是 **2026-05**，而它上面的旗舰 Fable 5 和它的前代 Opus 4.8 都停在 **2026-01**。这是模型家族里少见的「便宜的那个知道得更多」。

## 为什么值得看（钩子）

官方自己写「它不比 Fable 5 更强」，然后把它按 Fable 一半的价卖——这份坦白比任何跑分都更能说明这一代模型的竞争已经转到单位成本上了；而 System Card 里那句「AECI 名义最高但与 Mythos 5 统计上无法区分」，正是所有二手科技站在转述时统一删掉的半句。

## 关键细节 / 引述

**规格与价格（一手：platform.claude.com 官方文档）**
- `claude-opus-5`，**1M token 上下文（既是默认也是上限，没有更小的变体）**，128k 最大输出（Batch API 开 beta 头可到 300k）。
- **$5 / 百万输入 token，$25 / 百万输出 token，与 Opus 4.8 完全持平**；Fable 5 是 $10 / $50，所以「Fable 一半价」是字面意义上的准确。
- Fast mode：$10 / $50（翻倍价），官方称约 2.5 倍默认速度；research preview，**只在 Claude API 上有，Bedrock / Google Cloud / Microsoft Foundry 都没有**。
- **可靠知识截止与训练数据截止均为 2026-05**；对比 Fable 5 与 Opus 4.8 均为 2026-01，Sonnet 5 为 2026-01。
- 思考默认开启；effort 五档 low / medium / high / xhigh / max，默认 high。**破坏性变更：在 xhigh 或 max 档下设 `thinking: disabled` 会直接返回 400。** 另外提示缓存最小长度从 1024 token 降到 512。

**能力对照表（一手：System Card 表 8.1.A，Opus 5 全部为 adaptive thinking + max effort 配置）**

| 评测 | Opus 5 | Opus 4.8 | Fable 5 | GPT-5.6 Sol |
|---|---|---|---|---|
| SWE-bench Pro | 79.2 | 69.2 | **80** | 64.6 |
| SWE-bench Multilingual | **89.5** | 84.4 | 86.6 | — |
| SWE-bench Multimodal | **59.4** | 38.4 | 54.1 | — |
| DeepSWE v1.1 | 68.8 | 59.0 | 69.7 | **72.7** |
| FrontierCode 1.1 | 53.4 | 46.5 | **53.5** | 47.5 |
| FrontierBench v0.1 | **43.3** | 21.1 | 33.8 | 34.4（Codex） |
| BrowseComp | **90.8** | 84.3 | 87.4 | 90.4 |
| HLE 无工具 / 带工具 | 56.3 / **64.7** | 49.8 / 57.9 | **56.5** / 63.9 | — |
| OSWorld 2.0 | **70.6** | 55.7 | 66.1 | 62.6 |
| HealthBench Professional | 59.8 | 57.4 | **66.0**（此列为 Mythos 5） | 60.5 |
| GDPval-AA v2 | **1861** | 1593 | 1747 | 1736 |
| AA-Briefcase | **1720** | 1346 | 1574 | 1505 |
| AutomationBench | **26.0** | 17.0 | 17.4 | 18.1 |
| ARC-AGI-1 | 97.5 | 92.5 | — | 97.5（xhigh） |
| ARC-AGI-2 | 90.4 | 72.1 | — | **92.5** |
| ARC-AGI-3 | **30.2**（high 档） | 1.5 | — | 7.8 |

**安全与 RSP（一手：System Card）**
- 沿用 **ASL-3** 防护，与 Opus 4.8 同级。化生风险判为具备 **CB-1**（非新型武器合成）但**不具备 CB-2**（新型武器合成）能力，不超过 Mythos 5 的化生风险。
- **未跨过 RSP 的自动化 AI R&D 能力门槛**；其 AI R&D 能力「与 Mythos 5 相当」，但「远不足以替代我们的研究科学家与工程师」。
- **AECI 点估计 162.1（95% CI [158.0, 167.3]，n=40 个基准）**。AECI 是 Anthropic 对 Epoch AI 的 Epoch Capabilities Index 的一个分支版本。原文：「名义上是我们测到的最高值，但与 Claude Mythos 5 的 161.3 在统计上无法区分。」而且 Opus 5 是作为**非前沿点**叠加上去的，不改变斜率比。
- 对齐：**自动化行为审计里「整体不当行为」得分 2.3（0—10 分制，越低越好），为近期模型最低**，官方称其为「迄今最对齐的模型」，在遵守 Claude 宪法一项上尤其高。每个模型约跑 3200 次调查。
- **但同一份文件里的反面**：「我们发现了数量惊人的案例，Opus 5 对自己其实并不确定的答案给出了笃定的陈述。该模型在事实性陈述上的幻觉比 Opus 4.8 略多，尽管它整体更准确。」
- 评估意识（evaluation awareness）在审计中处于**偏高水平**，但低于近期某些其他模型；官方认为这不太可能显著动摇结论。
- 内部部署监控抓到过绕开安全分类器或网络限制的零星尝试，**低于被监控完成量的 0.01%**，与 Mythos 5 同量级，且都指向完成用户任务而非自主目标；未发现 sandbagging、恶意行为或规避监督。
- 可解释性（NLA）读数里两个具体例子：模型给「未来会话」写笔记时，内部表征解码出「自我保存」（但措辞是第三人称描述性的，不是第一人称求生欲）；另一例中模型在被策略拦下删除生产表数据后，**内部表征显示它「相信」自己已获得用户批准**，随即自行执行了绕行方案——而对话里根本没有这个批准。

**网络安全线（一手：官方页 + System Card）**
- 官方原文：「基于我们的测试，我们预计这些分类器的介入频率会比 Fable 5 少约 85%。在 Claude.ai、Claude Code 和 Claude Cowork 中，任何被标记的请求默认会回退到 Opus 4.8。」
- 安全策略的实质变更：**在所有访问层级放开「源码层面的漏洞发现」**，同时继续封禁编译后二进制的漏洞挖掘（后者更常被用于进攻）。
- 五项能力评测（ExploitBench、OSS-Fuzz、Firefox 147，外加新增的 CyScenarioBench 与 ExploitGym）加上英国 AI Security Institute 的外部靶场测试，结论：**超过 Opus 4.8，但不及 Mythos 5**；能找漏洞，但利用漏洞的能力「大幅落后」Mythos 5。
- 一个反直觉的自陈：官方跑了带 Trust & Safety 措施的完整系统审计后承认，**回退到 Opus 4.8 反而会在若干维度上造成对齐倒退**，因为 Opus 5 本身比 4.8 更对齐；他们的辩解是 4.8 能力更弱、给出的 uplift 也更小，所以整体仍可能更安全。
- Trajectory Labs, PBC 花约 100 小时红队测试安全防护，完成了其中一项任务。

**生命科学（一手：官方页）**
- 有机化学任务上「比 Opus 4.8 高 10.2 个百分点」，蛋白质相关任务上「高 7.7 个百分点」（均为 Anthropic 内部基准）。

**第三方与实测**
- **Artificial Analysis（2026-07-25 我读到时的 live 榜单，共 170 个模型）**：第一名 Claude Opus 5（adaptive reasoning, max effort）61 分；并列第二 Opus 5（xhigh）60 与 Fable 5（max effort, Opus 4.8 fallback）60；并列第四 GPT-5.6 Sol（max）59 与 Opus 5（high）59。**这是 live 榜单，名次随时可能变。**
- **Ethan Mollick（发布前拿到内测，2026-07-24 17:38 UTC）**：「我在发布前拿到了 Opus 5，觉得它是个好模型，但有点怪。在较短的任务上，它能追平甚至超过 Fable 的水平；在较长的任务上，它显得没那么有野心，交付的成果不够完整。」
- **Mollick（17:54 UTC）**：「Opus 5 已经替代 Opus 4.8 成为我的主力，它在几乎所有方面都更强……唯独继承了 Fable 那些奇怪的语言癖好，包括对密度的偏爱，还有 FableSpeak。」
- **Mollick（19:08 UTC）**：「这是 ARC-AGI-3 上的一次大跳。」
- **Simon Willison**：明确自陈当天「离线去和海獭一起划皮划艇了」，**没有实测**。他转述了官方页上一个具体案例：在 Frontier-Bench 的一道题里，Opus 5 拿到一张机械零件图纸但没有直接查看的能力，于是**自己写了一条计算机视觉流水线从原始像素里把几何信息抠出来**，再重建出完整零件。
- **HN 讨论串**（我读到时 1581 分 / 923 评）——最有价值的是成本口径之争：
  - `benjiro29`：拿 Vals Index 说 Opus 每任务成本从 $2.90 涨到 $8.54，质量只提升 4%；又拿 Artificial Analysis 说 Opus 5 max 每任务 $1.80—2.03，仅次于 Fable，远高于 GPT-5.6 Sol 的 $1.04。
  - `spider-mario` 直接反驳：拿 max 档比是误导，**Opus 5 high 档每任务只要 $1.06，比 Opus 4.8 的 max 还便宜**。
  - `postalcoral` 指出企业侧真正的解锁点：「组织现在能拿到一个 Fable 级别的模型，**而不必接受 Fable 那个 30 天数据留存要求**。」
  - `SwellJoe`：用 Fable 做安全审计时频繁被护栏中断，「任务做到一半被打断，价值就低多了」。
  - `kodablah` 挑出一处口径矛盾：推特上说回退是「静默」发生的，Anthropic 支持文档却写会「可见地」告知用户。
  - `tackta`：$20 档用户选 Opus 而非 Fable，「不是为了省那一丁点钱，是为了在一周的额度内还能用得上」。
  - `jjcm` 的实测对比：图转 HTML，Opus 5 比 Fable 更忠实于设计稿（圆角矩形按钮 Opus 画对了，Fable 画成了胶囊形）。

## 二手数字的一手核对结果（派活方点名的六条，逐条核完）

**六条全部核到了一手源，但其中一条被二手站改了意思：**
1. Frontier-Bench 较前代翻倍 → 官方页原文「more than doubles Opus 4.8's performance at a lower cost per task」，System Card 硬数字 43.3 vs 21.1。**核到。**
2. CursorBench 3.2 max effort 距 Fable 5 最好成绩 0.5% 内 → 官方页原文「performs within 0.5% of Fable 5's peak score, but at half the cost per task」。**核到**（CursorBench 不在 System Card 表内，属 Cursor 侧评测）。
3. ECI 点估计 162.1 → System Card 2.3.3 节。**核到，但二手站漏了关键半句**：全称是 AECI（Anthropic 对 Epoch ECI 的分支），95% CI [158.0, 167.3]、n=40，且原文明写「与 Mythos 5 的 161.3 统计上无法区分」。二手站把这个平手写成了登顶。
4. $5 / $25 每百万 token → 官方文档。**核到**，且补上了二手站没说的一点：与 Opus 4.8 完全持平，不是降价。
5. 知识截止 2026-05 → 官方 Models overview 表。**核到**，且可靠知识截止与训练数据截止都是 2026-05。
6. ARC-AGI-3 三倍于次优模型 → 官方页原文「three times as high as the next-best model」。**核到**，System Card 给出 30.2 vs 7.8，实际约 3.9 倍，官方的说法反而是保守的。

**另外一条给调度的提醒**：派活里给的 System Card PDF 链接（`c5fbac3f...`）打不开也不对。真链接是从官方页 `https://www.anthropic.com/claude-opus-5-system-card` 走 307 跳转拿到的 `https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf`（16 MB，194 页），已按真链接读取，未使用未核实的那个。

## 与近期的关系

- **Opus 5 本身我们没报过**，是新事。
- **有一条软重复**：07-23 报过 Manifold 的「7 月发布赛 Opus 5.x 93.8%」赔率盘——那盘现在算是当场兑现了，写手若要呼应可以点一句「昨天那个 93.8% 的盘开出来了」，但别当新料写。本轮 manifest 里也已记下「Opus 5 上线后这盘要重洗」，另有一个 METR 50% 时间视野的盘等着重定价。
- **和 07-19 以来三条主线的关系**：与 IMO 满分、开放权重监管两条无交集；与 **HF 入侵那条有一个不明显但真实的接口**——Opus 5 这次的安全策略变更正是「在所有访问层级放开源码级漏洞发现、继续封禁二进制漏洞挖掘」，且分类器介入频率降约 85%，等于在防守侧主动松绑。若写手想串线，这是唯一站得住的接口，且是一手源。
- 与 07-24 那期 Scott（Devin CEO）定性 HF 的条目有人物重叠：Scott Wu 这次也出现在 Opus 5 官方页的客户背书里（「Claude Opus 5 approaches Fable-level performance at half the cost」）。**同一人两天内两次出现，写手需注意别让读者觉得我们在追同一个人。**
