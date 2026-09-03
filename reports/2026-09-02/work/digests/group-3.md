# 企业 Agent 与推理的完整成本栈

- 推荐强度: 中
- 档位线索: 适合保留为独家视角，材料覆盖企业上下文、模型路由、推理配置和芯片适配几个不同层级；但不足以单独支撑金牌或银牌。Glean 与 Wafer 的醒目数字均为利益相关公司的自报，Wafer 估值与收购意向又来自匿名人士；Baseten 给出的是可按工作负载验证的工程分类框架，却没有公开测试数据、代码或配置，因此不能写成已复现的技术结论。
- 涉及文章: [Anthropic Customers’ Bills Are 80% Higher Than They Need to Be, Glean Says](https://www.theinformation.com/newsletters/applied-ai/anthropic-customers-bills-80-higher-need-glean-says) · The Information · 2026 年 9 月 2 日（北京时间）
- 涉及文章: [Wafer, An Inference Provider That Uses Non-Nvidia Chips, Lands Acquisition Offers and $200 Million-Plus Valuation](https://www.theinformation.com/newsletters/ai-agenda/wafer-inference-provider-uses-non-nvidia-chips-lands-acquisition-offers-200-million-plus-valuation) · The Information · 2026 年 9 月 1 日（北京时间）
- 涉及文章: [The efficient frontier of LLM inference](https://www.baseten.co/blog/the-efficient-frontier-of-llm-inference/) · Baseten，Philip Kiely · 2026 年 9 月 2 日

## 核心主张

这组三份材料分别指向企业 Agent 成本的三个层级：找到正确内部资料所消耗的上下文与搜索，按任务选择模型，以及模型落到具体硬件后的推理配置与软件优化。共同的技术判断是，最终费用不只由模型标价决定；但三份材料彼此独立，不能互相证明对方的具体性能和成本数字。Glean 与 Wafer 提供的是公司自身业务数据，Baseten 提供的是机制分类和调优方法，不是独立基准。

## 为什么值得看（钩子）

同一个“模型调用”背后，检索绕路、推理档位、批量大小、并行方式、解码方法和芯片适配都会改变账单。最有价值的不是宣称某一层能省多少钱，而是把这些常被混在一起的成本来源拆开。

## 关键细节 / 引述

- Glean 称其内部评估覆盖 180 多项企业任务；其助手完成相同任务时，比 Claude Cowork 少用 70％ token，向客户收取的平均单任务费用低 81％。这是 Glean 作为竞争对手的内部评估，不是独立基准；Anthropic 未评论。
- Glean 将差异归因于企业数据上下文层、enterprise graph 和按任务复杂度路由模型，从而减少 Agent 为找资料进行的长时间搜索。对比并非同模型同档位：Glean 助手会使用 Claude Opus 4.8 等模型，对照是开启高推理的 Claude Sonnet 5，因此不能把 70％ 和 81％ 的差异全归给上下文层。它还称给每个长期运行的 Agent 分配独立身份与认证凭证，只允许读取获授权数据；这是权限设计信息，不是成本评测结果。
- Wafer 完成 4000 万美元 A 轮融资。据匿名知情人士，融资后估值超过 2 亿美元，公司拒绝评论估值；同一来源称它拒绝了多家大型推理与云服务商的收购报价，但报价金额和条件均未公开。估值和收购兴趣不能写成公司已确认事实。
- Wafer 称，把 GLM-5.2 针对 AMD MI355X 优化后，吞吐可达到英伟达 B200 的约 80％，成本不到一半；它同时支持英伟达与 AMD，并计划扩展到 Google、SambaNova 和 Cerebras。性能与成本缺少独立复测，测试负载和口径也不能由现有转述补齐。
- Wafer 称年化收入在 12 周内增至约 800 万美元，毛利率约 50％。这些都是公司口径，未见审计；公司成立约一年、规模仍小，不能据此推出非英伟达推理市场已经成熟。
- Baseten 把推理优化分成两类。批量大小、张量／专家／注意力数据并行等配置，是在延迟与吞吐之间移动；量化、内核与运行时优化、推测解码和预填充／解码分离，则可能把整条效率边界外推。文章特别强调边界并不平滑，小幅配置变化可能造成大幅结果变化，必须按真实流量做经验扫描；它假设 Agent 编程场景已经启用 KV cache 复用和最优 KV-aware routing。文章没有给出实测表、代码或可复现配置，所谓硬件翻倍再叠加软件翻倍得到四倍提升只是说明复合效应的示例，不是本文测出的成绩。

## 与近期的关系

Wafer 的 GLM-5.2／AMD MI355X 性价比在 7 月 4 日日报已经以雷达条目出现过，当时写过每节点 2626 tok/s、成本比 Blackwell 低一半多；本期若保留 Wafer，只能把新增量放在 4000 万美元融资、匿名估值、公司自报收入与收购意向，不能把同一性能结果重新包装成新发现。Glean 与 8 月 21 日 AT＆T 按任务把轻工作路由到开放模型、公司自报部分任务成本最多下降 56％ 的报道相邻；新增角度是企业上下文层和资料搜索本身造成的 token 开销，以及它与 Claude Cowork 的直接比较。Baseten URL 未见往期收录，但批量、缓存、模型路由和框架影响成本均是近期反复出现的主题；它适合作为技术限定，不宜单列成新闻。
