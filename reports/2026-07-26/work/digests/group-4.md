# PIRAMID：PIBBSS 改名后开的新部门，主张拿统计物理重做机制可解释性

- 推荐强度: 中
- 档位线索: **够银，银位偏下**。理由：帖子本体确实是组织公告 + 路线宣言，但它不空——挂了 7 项两个月内的实际产出，其中两项已上 arXiv 且有硬结论（一个可解释性架构声称在多项指标上打过事后 SAE，一个 mean-field 学习理论定理），还给了一个有时限的可证伪目标。**真正的钩子在附件不在正文**：如果定牌想收，建议标题写「ParityTransformer / 天生可解释的架构打过事后 SAE」，而不是写「某机构成立新部门」。若当天银位竞争激烈，或不想连着第三天上可解释性条目，降无牌也说得过去。
- 涉及文章: [Introducing PIRAMID: Physics-Informed Research for Ambitious Mechanistic Interpretability Design](https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious) · LessWrong · 2026-07-25

## 核心主张

Principles of Intelligence（PrincInt，即改名后的 PIBBSS）成立内部研究部门 PIRAMID，赌注是：可解释性目前缺的不是更多探针，而是科学基础。他们的反直觉点在于**拒绝预设分析单元**——不认神经元、SAE 特征、核、电路里的任何一个是"基本粒子"，而是要"找出现有理论在哪里崩掉"，再去发现更好的理论对象。他们主张网络里存在"结构性相关的随机性"（structurally relevant randomness），统计物理提供的正是形式化并追踪这种随机性的语言；不能对随机性给出有原则说法的工具，"不太可能是忠实的（faithful）"。

另一层反直觉：他们对自家旗号里的"ambitious interpretability"（完全逆向工程一个 AI 系统）明确降级——"既非必要也非充分"，只当作可扩展对齐所需的那种忠实机制透明度的**代理指标**。

## 为什么值得看（钩子）

一群物理背景的人跳出来说"电路级可解释性挑错了分析单元"，并且不是光喊——已经交出一个不靠事后 SAE、而是训练时就把可解释性焊进架构的 transformer 变体，宣称在特征吸收、steering 有效性、细粒度因果干预上都优于事后 SAE。

## 关键细节 / 引述

- **三条线三个 lead**：学习理论（Dmitry Vaintrob）、可解释性应用（Andrew Mack）、数据模型与验证方法（Ari Brill）。分别对应"造理论 / 造工具 / 造能验证前两者的合成数据基准"。
- **可证伪的近期目标（原文措辞）**：理论组要在"接下来几个月内"做出一个 end-to-end toy-to-real 案例，让"一个有理论动机的统计量预测并解释泛化或能力相关的变化"；数据组要在一年内把合成数据集"变成一个公开基准，其忠实性保证强于当前评测实践"。这两条都是能到期查账的。
- **最硬的一项已发产出**：arXiv 2607.20652（07-22，Andrew Mack 等，含本帖作者 Lauren Greenspan）——ParityTransformer / Deep Parity Bottlenecks。用"无参数的代数字典"替换学出来的字典，给出确定性的 incoherence 保证并消掉了让逐层可解释瓶颈无法规模化的显存开销；论文称其特征"原生于实际计算，而非分析的产物"，在 feature absorption、steering effectiveness、细粒度因果干预上优于事后 SAE。
- **另一项**：arXiv 2607.05735（07-07，Dmitry Vaintrob、Kaarel Hänni）——mean-field 贝叶斯网络的宽度稳健可学习性定理：布尔立方体目标族在无限宽下多项式样本可学，当且仅当在多项式宽度下可学，当且仅当其"约化熵"多项式有界。即无限宽极限没有虚增泛化能力。
- **对现状的直接开火**：「Mechanistic interpretability currently lacks rigorous benchmarks for validating interpretability tools」；「A method tied only to today's empirical probes may fail when the model generalizes in a new way」；「A faithful explanation must track the mechanism the model actually learns and uses, not just correlate with behavior」。
- **多尺度立场**：相关结构不住在某个固定的描述层级，可能表现为「local features, global directions, hierarchical latent variables, circuits, training phases, basins, or weight-space perturbations」。
- **组织信息（核过）**：七位署名作者 = Lauren Greenspan、Ari Brill、Andrew Mack、Nischal Mainali、Jennifer Lin、Lucas Teixeira、Dmitry Vaintrob。PIBBSS 2022 年由 Nora Ammann、TJ、Anna Gajdova 创立，现改名/上翻为伞形组织 Principles of Intelligence，美国 501(c)(3)，注册于明尼苏达（EIN 33-4129337），旗下含 PIBBSS Fellowship、Iliad 研究组、Affiliate 项目和 PIRAMID。**官网未给出确切改名日期，也未公布人数和资金数额——这两项抓不到，别在正文里编。** 帖中列出的资助方为 UK AI Security Institute、Long-Term Future Fund、Coefficient Giving。帖尾明确在招人（"We'll also be hiring"）。

## 与近期的关系

- 本组织、本部门在往期报道中**零出现**（grep 全部 reports 无 PIBBSS / PIRAMID / Principles of Intelligence）。单条本身无重复。
- 但**类目有疲劳风险**：07-21（steering 向量 + neologism token）、07-23（J-Space meta-tokens）已连上两条可解释性小实验，07-15 也有一条 J-Space。本条是同一类目第三/第四次。区别在于这次是路线级/架构级，不是又一个小工具帖——定牌时可以用这个差异来辩护，但如果当天还有别的可解释性条目，两条只能留一条。
- 与 07-04 / 07-10 / 07-23 赔率盒里反复出现的"可解释性突破概率趴地"张力可以互文（Yudkowsky 那道题 9.7%）。这批人正是在赌那条线能被抬起来。
