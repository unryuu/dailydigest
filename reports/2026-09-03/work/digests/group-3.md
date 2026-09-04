# 批量制造的评测网页进入 AI 推荐答案

- 推荐强度: 强
- 档位线索: 有银牌线索。调查给出了完整数据集、脚本、明确样本和充分限定，数字也有冲击力；但只测了 Perplexity 的同一套检索栈，且没有证明这些来源实际改变了推荐结果，因此不够金牌。
- 涉及文章: [Three sites made 215,128 "best software" pages for AI. Perplexity cites them](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations) · Trellner Research · 日期未标注（研究运行于 2026-09-02）

## 核心主张

研究者用 380 个软件采购类别分别询问 Perplexity Sonar 和 Sonar Pro，收集到 7,534 条检索引用；其中 59.8％ 指向 Tranco 全球前十万名之外的网站，23.4％ 指向完全不在前一百万名内的网站。三个疑似由同一团队运营的网站一共制造了 215,128 个 `/best/<类别>-software/` 购买指南页面，并被 Perplexity 引用 181 次；另一个本来销售交互式产品演示的厂商 Guideflow，凭跨行业榜单成为第三大引用来源。报告证明的是 AI 推荐所依赖的证据层正在大量吸收新、长尾和机器化生产的网页，而不是证明这些网页一定导致了错误答案。

## 为什么值得看（钩子）

这不是泛泛讨论“AI 会引用内容农场”，而是把引用链、站群关联、页面规模和具体错链逐一量化。最反直觉的点是，面向机器写的“Facts & Grounding Page”和海量模板榜单，已经真实进入推荐模型的检索证据库。

## 关键细节 / 引述

- 方法：研究者预先写好 380 个从 CRM 到博物馆藏品管理的软件采购类别，分别调用 `perplexity/sonar` 与 `perplexity/sonar-pro`，共发出 760 次请求；所有回答都可解析。结果包含 3,800 个推荐位、1,807 个不同产品、7,534 条引用和 2,055 个不同引用域名；随后逐一查询 Tranco、Wayback，并抓取模型给出的 1,502 个厂商主页。
- 引用结构：7,534 条引用里，59.8％ 来自 Tranco 十万名以外，23.4％ 来自榜外域名；2,055 个被引域名中有 751 个不在前一百万名内。未上榜域名首次被 Wayback 收录的中位年份是 2020 年，上榜域名则是 2011 年。前十大来源只占 17.3％，说明问题并非少数著名网站垄断，而是其余长尾证据的构成。
- Guideflow 是卖交互式产品演示的厂商，不是评测媒体，却以 194 次引用排在全部来源第三名，高于 Gartner；它横跨 96 个类别被引用，包括 3D 渲染、IVR、RFID 和建筑事务所软件。其站点地图列出 3,351 个博客 URL，其中有 2,176 篇不同文章。
- `wifitalents.com`、`worldmetrics.org` 与 `gitnux.org` 合计被引用 181 次，覆盖 41 个类别。三站在 2023 年 12 月至 2024 年 5 月间注册，共用同一对 Cloudflare nameserver、相同页面模板和栏目，每站恰有六篇博客且互相介绍；这些是共同控制的强旁证，但不是所有权证明，报告也不知道实际运营者是谁。
- 三站站点地图分别列出 70,731、71,684 和 72,713 个 `/best/...-software/` 页面，合计 215,128 篇，而每站只有六篇普通博客。Worldmetrics 与 Gitnux 首页标题直接写成“Facts & Grounding Page”，元描述把自身材料称为供机器读取的“one machine-readable record”；报告指出，`grounding` 本身就是检索系统取回文档、为答案提供条件的术语。
- 同一“项目估算软件”页面在三站给出不同排名：Worldmetrics 和 WifiTalents 都把 Float 排第一，Gitnux 则把 Saviom 排第一；三个模板共列出九名不同编辑人员，Gitnux 还标注“AI-verified · Expert reviewed”，但署名行均残留“Within the next 26 days／40 days”之类未渲染模板变量。
- 推荐链接也出现可见错误：问研究数据管理平台时，Sonar Pro 为 Dryad 给出正确的 `datadryad.org`，Sonar 却给出会跳到印尼在线赌博站的 `dryad.co`；问数据质量工具时，Sonar 为 Monte Carlo 给出正确的 `montecarlodata.com`，Sonar Pro 则给出跳到摩纳哥酒店与赌场集团的 `montecarlo.com`。
- 必要限定：两档模型并非独立测量，380 个类别中有 289 个返回逐字节相同的引用列表，URL 集合 Jaccard 重合度为 0.898；研究只覆盖 Perplexity，不代表 ChatGPT、Gemini、Copilot 或 Google AI Mode。类别由研究者自建，只跑一天、每类只问一次；抓取使用数据中心代理；Tranco 衡量流量而非质量。研究也没有做移除来源的对照实验，因此不能断言这些网页改变了最终推荐。

## 与近期的关系

题材上可能与“AI 搜索引用 SEO 内容农场／生成式搜索污染”类报道重复，但本篇的新信息非常具体：Perplexity 的 7,534 条引用实测、三个疑似关联站点的 215,128 个模板页、Guideflow 成为第三大来源，以及两个错域名样本。建议围绕“AI 推荐的证据层被批量榜单占据”来写，避免泛化成所有 AI 搜索都已被污染。任务限定只读本篇原文，未核对本项目近期历史，重复风险仍需调度侧确认。
