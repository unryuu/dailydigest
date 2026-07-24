# Gemini 3.6 Flash / 3.5 Flash-Lite / 3.5 Flash Cyber 三连发

- 推荐强度: 中
- 档位线索: 官方公告·银合适。三个都是 Flash 级小模型，正主 3.5 Pro 缺席，单看跑分是常规迭代；但 Flash Cyber "只给政府和可信伙伴"的封闭发布模式是个不常见的信号，若当天缺硬货可凭这一点冲金牌讨论位，凭跑分本身不够。
- 涉及文章:
  - [Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/) · Google 官方博客 · 2026-07-21
  - [Introducing Gemini 3.5 Flash Cyber](https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/) · Google DeepMind · 2026-07-21（署名 Raluca Ada Popa、Four Flynn；首次抓取 502，重试成功）

## 核心主张

Google 一口气发了三个 Flash 级模型：3.6 Flash 接棒生产主力、3.5 Flash-Lite 主打快和便宜、3.5 Flash Cyber 是首个网安专用微调模型。旗舰 3.5 Pro 仍然缺席，官方只给一句 "currently testing with partners and we plan to make it broadly available as soon as it's ready"，同时顺手预告 "We have started our most ambitious pre-training run yet, for Gemini 4"。最硬的判断：这批发布的重心不是能力上限，而是效率（3.6 Flash 输出 token 比 3.5 Flash 少 17%）和垂直专用化（Cyber）。

## 为什么值得看（钩子）

一个"轻量小模型"在 V8 引擎上挖洞挖赢了 Opus 4.6（55 比 36），而 Google 的处理方式不是上架 API，而是锁起来只给政府和可信伙伴——模型能力分级发售，安全模型走"军售"模式，这在主流大厂里是头一回。

## 关键细节 / 引述

- **3.6 Flash**：$1.50 / $7.50 每百万输入/输出 token；对比 3.5 Flash 的跑分——DeepSWE 49% vs 37%、MLE Bench 63.9% vs 49.7%、OSWorld-Verified 83.0% vs 78.4%、GDPval-AA v2 1421 vs 1349；输出 token 用量少 17%，DeepSWE 上效率提升达 65%。文中未解释为何跳版本号到 3.6，只说 "builds directly on developer and customer feedback from 3.5 Flash"。
- **3.5 Flash-Lite**：$0.30 / $2.50 每百万 token，350 输出 token/秒（Artificial Analysis 测得）；Terminal-Bench 2.1 54% vs 前代 3.1 Flash-Lite 的 31%，SWE-Bench Pro 54.2%（超过 3 Flash 的 49.6%）。
- **3.5 Flash Cyber**：在 3.5 Flash 上微调，专做漏洞的发现、验证、修补，作为 CodeMender 的引擎。训练材料含 OSV.dev 的 70 万+开源漏洞和十余年 OSS-Fuzz 结果。实战：Google Cloud 漏洞研究团队用它 2 小时内发现公共 API 的 RCE 漏洞和生产服务的内存损坏漏洞，并生成 100% 可靠、绕过 ASLR 和 W^X 的 RCE exploit。
- **Cyber 对比数字**：V8 引擎固定调用次数下发现 55 个独特确认问题，3.5 Flash 47 个、Opus 4.6 36 个，其中 10 个是另两个模型都没找到的；CyberGym 上"与显著更大的模型性能相当"（无具体分数，竞品分数注明来自厂商自报）。
- **Cyber 发布方式**："exclusively available to governments and trusted partners via CodeMender soon as part of a limited-access pilot program"，逐步扩大；DeepMind 原话 "Given the dual-use nature of this technology, we have taken an intentional approach to how we deploy 3.5 Flash Cyber."
- 两篇均未提上下文窗口长度；客户引语（Figma、JetBrains、Palo Alto Networks 等）以图片形式呈现，无法提取原文。

## 与近期的关系

（按派活方要求，本组只读原文，未与前几期材料做关联比对。）就原文自身信息：这是 Gemini 3.5 系发布节奏的延续，3.5 Pro 的持续缺席 + Gemini 4 预训练启动是官方首次在同一篇里并置的两条线索。
