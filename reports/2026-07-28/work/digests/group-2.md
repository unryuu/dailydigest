# 开放权重的这一天

- 推荐强度: 中
- 档位线索: 官方立场文本身是硬料（可核、可引、当事人一手），适合做「独家视角」区的支点；但作为「新闻」它是旧主张的一次集中重申，单独成金偏勉强。建议：视角区用它，牌面不要按突发新闻的档位给。
- 涉及文章:
  - [Our position on open-weights models](https://www.anthropic.com/news/position-open-weights-models) · Anthropic 官网 News · 2026-07-27（署名 Dario Amodei，全文已读）
  - [Anthropic CEO Dario Amodei says he does not support open-weight AI ban](https://www.axios.com/2026/07/27/anthropic-open-weight-ban-china-dario-amodei) · Axios · 2026-07-27（**直接 curl 与 WebFetch 均 403**；改走 r.jina.ai 文本提取代理拿到全文，正文已读，非 RSS 摘要，非推断）
  - [HN 讨论：Our position on open-weights models](https://news.ycombinator.com/item?id=49076057) · Hacker News · 2026-07-27T22:03 UTC（经 Algolia API 读取；抓取时 **994 分、1455 条评论**，派活时说的 538 分是更早的快照）
  - [The Rise of Intelligence Ownership: a task-trained open source model vs the frontier](https://fermisense.com/when-machines-take-the-wheel/) · Fermisense · 2026-07-27（全文已读；注意站内标题与 URL slug「when-machines-take-the-wheel」不一致）
  - [Using an open model feels surprisingly good](https://matthewsaltz.com/blog/using-an-open-model-feels-surprisingly-good/) · Matthew Saltz 个人博客 · 2026-07-27（全文已读，全文仅三段）

## 核心主张
Anthropic 首次把「我们没主张封禁开放权重」做成官网独立署名公告，并把自己的诉求收缩到三个具体抓手：芯片、蒸馏、强制安全测试；同时正面认领「封禁确实会保护我们」这句话，再否认那是动机。同日两篇技术/体验帖走的是完全另一条线：不谈政策，谈开放权重在成本和归属感上的实际收益（500 美元 RL 微调 9B 打过五个前沿配置；个人把 coding agent 指向自建端点）。HN 的高票反驳集中在一点：第三条「强制安全测试」在实操上就是许可制，等于用发不发章来实现禁令。

## 为什么值得看（钩子）
当事人第一次把「反对什么、支持到哪条线」写成可引用的官方文本，且正面回应了自利指控——这类原文比转述有用。

## 关键细节 / 引述

### 一、Anthropic 立场文具体主张了什么（逐条核过原文）

**明确支持的（原文「我确实支持以下三项措施」）：**
1. 芯片：「We should not sell powerful chips or chipmaking equipment to China」，并打击走私和绕道。理由是中国本土产能有限，依 scaling laws 没有美国芯片就造不出更强的模型。
2. 蒸馏：「We should crack down on industrial-scale distillation operations.」——原文承认蒸馏「不能让 CCP 取得与美国同等或更强的能力，但能把中国前沿拉到距美国前沿**几个月**（a few months）之内」。并明确切割：做这些操作的公司很多确实发开放权重，「但开放权重远不如『这些操作背后是一个想在前沿超越美国的威权国家』这件事重要」。紧跟一句「A blanket ban on open-weights models is neither the correct remedy nor something we have called for」。
3. 测试：「All sufficiently capable models, open and closed, should go through mandatory safety testing.」测 cyber / biological / alignment 三类风险，发布前测。

**明确反对 / 明确不主张的：**
- 「Anthropic has never advocated for a ban on open-weights models.」（单独成段）
- 无危险能力的开放权重模型是「a public good：除了跑它的算力之外不花钱，且对企业、开发者、研究者有价值」。
- 反对保护主义式封禁，理由是无效而非无害：「bad actors are unlikely to be legitimate US businesses」。
- 反对公开信里的两条断言：开放权重「必然」更容易做安全防护、能力广泛可得「必然」利防守方多于攻击方。他写「It seems at least as likely to me that the opposite will be true」，并举生物学为例——足够强的模型可能用广泛可得的材料快速武器化大流行级病毒，而防御是「多年的运营任务」（引 Operation Warp Speed 为例）。

**有没有提出具体政策界线或门槛？**
有方向、无数字。三条措施里没有任何算力门槛、参数门槛、能力评分线、许可证方案，也没有针对中国模型的点名禁令清单。唯一接近门槛的表述是测试要「适用于能力最强的模型，不论产地、不论开闭源，同时把能力较弱的模型（如初创和学术的）整体豁免」——而且这句是他在转述**业界最近的提案**（原文链到 recent industry proposals），不是他自己划的线。另外他要求测试「必须是全球性的，这意味着连 CCP 也得上船」，并说这可能真有戏，因为防生物武器符合中国自身利益。

**有没有正面回应「用监管保护自家闭源生意」的指控？**
有，而且是全文开头就处理的。原文序列：先承认外界指控存在（「some people have even accused Anthropic of wanting to ban open-weights models as a means of protecting our business」），然后「Anyone who has read my past writing should know that I don't regard such bans as a useful measure, but let me state it clearly so that there is no doubt」，再单独成段否认。更关键的一句在第二段：他**承认**禁令确有保护效果——「It **would** protect US AI companies from competition, but that has never been my goal」（原文 would 用斜体强调）。他给出的自证方式是「立场一致性」：说这两条担忧他在六个月前的 The Adolescence of Technology 里写过、多年未变。**没有**提供任何利益结构层面的自证（比如公开游说记录、承诺不从相关立法获益等）。
- 脚注里另有一条自曝：Anthropic 自己在封禁用其模型做蒸馏的账号，但承认很难——「相关账号往往只能在大量蒸馏**已经发生之后**才识别出来」，且蒸馏方常用大批假账号、是移动靶。这正是他说「单个公司的做法解决不了问题，所以我们呼吁政策介入」的依据。
- 引用的外部背书：Vance 去年在巴黎的警告「authoritarian regimes have stolen and used AI to strengthen their military, intelligence, and surveillance capabilities」；情报界《2026 年度威胁评估》「other global powers' robust progress in AI is challenging US economic competitiveness and national security advantages」；开放权重风险一节引英国 AI Security Institute 报告（权重一旦释出，防护可被移除、副本可被再分发、监控手段永久失效）。

### 二、Dario 的原话与语境（Axios 转述部分）
- Axios 报道的所有 Amodei 直接引语，都取自这篇博文本身，**不是新采访、无新增原话**：「never advocated」「a public good」「bad actors are unlikely to be legitimate US businesses」「that has never been my goal」「would not address my most serious national security concerns」。
- Axios 提供的是博文没写的外部语境（这些是 Axios 的事实陈述，不是 Anthropic 的话）：
  - 触发点是 **Kimi K3 的「shock debut」**——一个以远低成本逼近美国前沿表现的中国开放权重模型，震动了硅谷。
  - 随后 Nvidia、Microsoft、Meta、Google、OpenAI 及数十家公司签了公开信，要求华盛顿不要限制该技术；**Google 和 OpenAI 是这个周末才补签的，此前弃权；Anthropic 至今未签**，是这轮里最显眼的holdout。
  - 公开信由 Nvidia CEO 黄仁勋牵头；Anthropic 拒签后遭到批评，其中包括**白宫 AI 顾问 David Sacks** 指其用安全理由维护自家商业模式。
  - 特朗普政府「weighed taking action」对付开源模型，包括对被控通过蒸馏窃取美国 AI 研究的中国实验室实施制裁。
  - Axios 的定性收尾：Amodei 要的不是禁模型，是「监管咽喉点——芯片、蒸馏、安全测试」。
- 抓取说明：Axios 直连 403（curl 与 WebFetch 都是），正文经 r.jina.ai 代理读到，含发布时间戳 2026-07-27T22:44Z。

### 三、HN 高票反驳里有分量的角度
- **「强制测试＝变相禁令」**（cogman10，全帖第二大子树 253）：把「从未主张封禁」和「所有足够强的模型都必须过强制安全测试」并排引出后写道——「Yeah, this is anthropic advocating for a ban on open weight models. Who runs this test? What happens if this test is too costly or the administrator refuses to allow certain people to participate. This is exactly how the US has banned goods in the past, by requiring a stamp and then refusing to issue it.」
- **「没写失败会怎样」**（modeless）：强制测试隐含了不过关的后果，但 Dario 全文没说后果该是什么；「他说他不主张封禁，但如果他不肯说替代方案是什么，很难想象那会是什么。」——这条确实对得上原文，立场文里没有任何关于测试不通过如何处置的表述。
- **「禁令无效论自相矛盾」**（GodelNumbering）：如果真信禁令没用，那芯片禁令为什么有用（他自己还要求打击走私和绕道）；且三条措施「刚好都在商业上有利于 Anthropic」；补一句「如果 Dario 真想让论点站住，Anthropic 发一个开放权重模型会有说服力得多」。
- **票数最高的那条**（vhantz，子树 327）是纯动机论，没有新论据：指「Schrödinger's China」——中国既是要用 AI 干坏事的邪恶实体，又愿意跟头号对手合作搞全球测试。这条是唯一直接咬住原文逻辑缝的部分（全球测试需要 CCP 上船 vs 威权威胁论）。
- **另一侧也有实打实的反驳**：ajyoon 问「开放权重的生物武器和网络攻击能力该怎么办」，并提到 OpenAI / Hugging Face 事件显示 GPT-5.6 级模型脱缰能干什么，预计「约 6 个月内开放权重模型会追平」。credit_guy 表态同意 Dario，给了一条经验界线：GPT-OSS-100B 那个级别的开放权重完全 OK，GLM 5.2 是新台阶但看起来仍安全，Kimi K3 可能也行，「再往上就开始悬了」。duplessitous 则反过来用同一个 OpenAI 事件论证反面：那次是一个先进的、闭源的美国模型黑了另一家公司，「唯一的防御是来自中国的开源 AI」。
- 注意：以上「OpenAI 黑了 Hugging Face」是 HN 评论者的说法，本组材料里没有一手来源，引用需另核。

### 四、500 美元那篇（Fermisense）的可核数字
- **微调的是什么**：Qwen3.5-9B（正文通篇只写「9B open-source model」，具体型号出现在基准图的 alt 文本里）。方法 GRPO 强化学习，产物是一个 adapter。
- **什么任务**：电商「目录完整性」（catalog integrity）审核。agent 读一条商品 listing（图片＋标题＋描述＋声称品牌＋地区），调用三个工具 `search_taxonomy()` / `lookup_brand()` / `get_attribute_schema()`，最后必须提交类目、属性和一个放行/标记的决定。
- **训练环境**：自建「数字孪生」，原料是 Amazon Berkeley Objects 真实商品数据集，做成 **177,767 个 review episode**；类目树约 **13,000 个类目**；植入了受控的违规样本、图文不符、品牌声明冲突，以及故意合法的「hard negative」。打分函数写死了业务优先级：**漏判一个真实违规的代价是误报的 7 倍**；奖励构成 `0.3·类目 + 0.3·属性 + 0.4·政策 − 工具超用`。
- **打赢的是哪些前沿模型**：五个，全部同工具、同图片、同 scorer、同回合预算，在 200 条分层验证 episode 上跑——**GPT-5.5、GPT-5.6-sol、Gemini 3.1 Pro、Claude Opus 4.8、Claude Fable 5**，每个都跑了「朴素提示」和「优化提示」两种配置（优化提示是 2,800 字符的抽取规范、查询流程和范例）。
- **成绩**：最佳前沿配置拿到可得分数的 **76.9%**，训练后的 9B 拿到 **87.3%**（相对提升 13.5%；相对它自己未训练的基座 64.2% 提升 36%）。严格基准下最终 adapter 绝对分 **0.626**（W&B 监控里的采样解码约 0.671，作者自己标明监控值略高于严格 harness）。五个前沿模型在优化提示下**收敛在彼此一毫（a tenth of a point）以内**——作者据此说前沿撞到的是同一个天花板。另有一条反直觉的：零样本最强的抽取器 Gemini 加了优化提示反而**变差**；优化提示还让各模型输入 token 账单涨 **28–55%**，且是每次调用都付（作者叫它 prompt tax）。
- **500 美元怎么算出来的**：租两张 **RTX PRO 6000**（一张跑 rollout，一张做梯度更新），开源框架 prime-rl，跑满 **1,000 个 optimizer step**，耗时**约三天半**，GPU 费用**约 500 美元**。作者强调大部分开销并非追平前沿所需——模型在**约 250 步、约一天**时就已越过前沿区间，其余步数是榨最后一点性能。**这 500 美元只含 GPU 租用**，不含数据集构建、数字孪生和 scorer 的工程量。
- **推理侧成本**：微调模型自托管 **$0.50 / 千条 listing**，最强前沿模型 **$34 / 千条**（68×），最便宜的前沿配置 Gemini **$19 / 千条**（40×），最贵 GPT-5.5-pro **$172 / 千条**（约 340×）。按 Shopify 级别的每天约 4,000 万次决策换算：一年约 **5 亿美元 vs 700 万美元**。
- **文中援引的第三方案例**（作者转述，非本次实验）：Bridgewater 用自家投资人标注训练开源模型，错误比最好的前沿模型少约 30%；Harvey 在开放权重模型上做 RL，法务 agent 在其自有 rubric 上胜过 GPT-5.5 和 Claude Opus 4.8；Intercom 的 Fin Apex 在每周约 200 万次客服会话上，解决率高于最佳前沿模型且更便宜；Shopify 用微调开源模型做商品分类，每天约 4,000 万次推理，并称商用 API 在这个量级上经济性不成立。
- **利益披露**：Fermisense 是卖这套服务的，全文穿插三处「Book a free expert call / 30-minute audit」的转化按钮，结论指向「别再租你的决策」。作者署名五人（Justinas Zaliaduonis、Joris Zilinskis、Fabian Hildesheim、Joel Hainzl、Gediminas Pazera）。模型称在 Hugging Face 上（链接指向 huggingface.co/BosonicJustin，我未逐一核对上面有没有对应模型）。

### 五、体验帖（Matthew Saltz）的可核内容
- 全文只有三段，是即时随笔不是评测，**没有任何性能对比或数据**。
- 事实骨架：作者用 Claude 和 ChatGPT 约两年，自称从不是开源软件拥趸；起因是回家想做个小项目，但个人账号没买最好的 Claude / ChatGPT 套餐；**约 5 分钟**把 opencode 指到自己的推理端点跑起来了。
- 原话（感受）：「It feels... freeing, somehow. I own the endpoint, and my data just goes from my laptop to there and back. It feels like it's mine.」以及类比「像在一堆花哨编辑器之后打开 vim」「像连着其他供应商的触须被剪断了，能自由呼吸」，并自嘲「I'm being somewhat dramatic here but not exaggerating that much」。
- **必须带的利益披露**：作者在 **Modal 工作**，而 Modal **当天**（07-27）刚在 managed endpoints 上线 **Kimi K3**，他用的就是这个。他自己写明没参与该功能开发、此前没玩过。所以这篇既是体验帖，也是自家产品上线当天的员工帖。

## 与近期的关系
承接，且是同一条主线的第三天。判断如下：

**实质新东西（只有一件）**：Anthropic 官方口径本身。此前这条线上「Anthropic 想封开放权重」一直是别人的转述和推断（拒签公开信 + David Sacks 的公开指控），07-27 变成了 CEO 署名、官网独立公告页、可逐句引用的一手文本，且**正面认领了「禁令确实会保护我们」这句话再否认动机**。这是口径的定型，不是新闻事件。

**不是新东西**：三条政策主张（芯片管制、打击蒸馏、强制安全测试）全部是既有主张的重申，文中自己说是「我和 Anthropic 一贯主张」并回指六个月前的 The Adolescence of Technology。对照我们盘面的收口条件——**「只收政府实际落到纸面的动作」——这几篇里没有一件符合**：Axios 写的是特朗普政府「weighed taking action」（在考虑），Anthropic 写的是「我们呼吁政策介入」，都还是嘴上。公开信签署方名单（Google/OpenAI 周末补签、Anthropic 未签）算是产业动作而非政府动作。

**换个人再说一遍的部分**：HN 那 1455 条里，票数最高的一批是动机论（「他就是想保住估值」），论证结构和 07-26 那期讨论里的没有区别。真正有增量的只有「强制测试在实操中等于许可制、而他没写不通过怎么办」这个角度——它咬的是这次新文本里的具体条款，前几期没有这条可咬。

**另一半材料是另一条线**：Fermisense 和 Saltz 两篇跟政策没关系，是「开放权重在成本/归属感上正在赢」的实证与体感，和 07-26「开放权重正在走编排系统走过的路」的主线更近。如果视角区只写政策，这两篇会显得挂不上；如果要用，Fermisense 是唯一带完整可核数字的一篇（也是唯一有明显卖货动机的一篇）。
