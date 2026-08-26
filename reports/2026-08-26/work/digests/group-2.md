# Agent 热潮正在把日志与数据库推成基础设施生意

- 推荐强度: 强
- 档位线索: 够银。最硬数字是 ClickHouse 年度经常性收入超过 3.5 亿美元，以及 OpenAI 每天处理三十多 PB；不要把全部增长都归因于 Agent。
- 涉及文章: [ClickHouse’s Recurring Revenue Passes $350 Million as OpenAI, Agent Use Jumps](https://www.theinformation.com/articles/clickhouses-annual-recurring-revenue-passes-350-million-ai-agent-demand) · The Information · 2026-08-25 06:04 PDT

## 核心主张

据一名接近公司的人士，ClickHouse 年度经常性收入已超过 3.5 亿美元，比五月增长 40％。OpenAI 过去一年对 ClickHouse 的用量增长约十倍，达到每天三十多 PB，用它排查训练问题、追踪线上性能，以及检查 Agent 是否按预期行动。

Agent 让数据库和可观测性工具从后台组件变成更重要的基础设施，但报道只证明需求同时增长，不能把 ClickHouse 的全部收入增幅都归因于 Agent。

## 为什么值得看（钩子）

模型公司之外，真正接住 Agent 用量的还有日志、数据库和监控服务。OpenAI 每天三十多 PB 的真实使用规模，比泛泛说“基础设施受益”更具体。

## 关键细节 / 引述

- ClickHouse 年度经常性收入超过 3.5 亿美元，比五月增长 40％；年度经常性收入是未来十二个月订阅合同价值，不是已经确认的全年收入。
- OpenAI 的使用量一年增长约十倍，达到每天三十多 PB，约合每天 30 万亿条事件。
- OpenAI 用 ClickHouse 记录训练运行中的问题、检查线上模型响应速度，并追踪 Agent 是否按预期行动。
- OpenAI 过去一年把部分日志管理工作从 Datadog 转到 ClickHouse；这不是全面弃用 Datadog。
- ClickHouse 毛利率约为 50％至 70％。CEO Aaron Katz 称公司如果愿意可以明年实现现金流为正，但现在选择继续投资增长。
- 公司今年一月估值为 150 亿美元，并通过收购 Langfuse 进入 AI 应用与 Agent 可观测性市场。

## 与近期的关系

与 08-25 的 Meta 消费 Agent 和推理引擎攻击面不同，本条写的是 Agent 用量如何传导到数据库与监控基础设施，属于新的商业侧面。不要重复昨天 Prime Agent 的框架、记忆或稳定性内容。
