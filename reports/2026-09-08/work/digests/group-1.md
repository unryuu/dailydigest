# AWS 重建 Bedrock 推理层

- 推荐强度：强
- 档位线索：技术改造、客户体验和商业迁移三段闭环，够金牌。
- 涉及文章：[How Six AWS Engineers Rebuilt Bedrock to Challenge Microsoft](https://www.theinformation.com/articles/six-aws-engineers-rebuilt-bedrock-challenge-microsoft) · The Information · 2026-09-08

## 核心主张
Bedrock 最初沿用传统 Web 服务的设计思路，面对推理任务的突发负载和 Agent 长任务时频繁报错、限制容量。六名资深工程师用 AWS 自家的 Kiro 编程工具重建推理层 Project Mantle，把它改成调度系统；可靠性改善后，AWS 才开始从 Azure 和 OpenAI 直连抢到部分客户支出。

## 为什么值得看（钩子）
它把「云厂商做 AI」落到一个具体工程问题：推理不是普通网页请求，旧架构再大也会卡住。

## 关键细节／引述
- 2025 年部分客户追加容量最长要等三周；到 2025 年末，等待缩短到两天。
- 咨询公司 Caylent 称，2024 年 Claude 在 Bedrock 上的生成速度一度比直接使用 Anthropic 慢 63％；其金融客户从 2026 年 5 月以来在 AWS 的支出增长五倍。
- Mantle 允许客户给任务分优先级、隔离不同客户的负载，并通过 Journal 保存 Agent 中间进度，避免长任务出错后从头开始。
- Mantle 直接兼容 OpenAI 和 Anthropic 的 API；第一版 Bedrock 曾要求客户写定制代码。
- Amazon 称 2026 年上半年新增的 Bedrock 客户超过此前两年总和，第二季度客户支出超过此前所有季度合计。
- 一家咨询公司的六名客户把 OpenAI 模型从 Azure 或 OpenAI 直连迁到 Bedrock；但一名现有客户近几个月仍遇到中断，最长约十一小时。

## 与近期的关系
与 09-07 Anthropic 巨额算力承诺同属云算力大线，但本条写的是推理服务架构、容量交付和客户迁移，没有重复合同金额与容量。
