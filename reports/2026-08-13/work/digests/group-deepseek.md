# DeepSeek V4 Pro 开放权重，Harness 同步公测开源

- 推荐强度: 很强
- 档位线索: 用户已明确要求把「正式模型开放权重＋Harness 公测开源」合并升为行业金牌。模型权重页和 Harness 官方页面均已上线，先前只能确认 API 更新、不能确认开放权重的判断已经过时。跑分仍必须写成 DeepSeek 官方自报。
- 涉及文章: [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) · DeepSeek 官方 Hugging Face · 2026-08-13 抓取
- 涉及文章: [DeepSeek Harness](https://deepseek.com/harness/) · DeepSeek 官网 · 2026-08-13 抓取
- 涉及文章: [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) · DeepSeek 官方 GitHub · 2026-08-13 抓取
- 涉及文章: [模型 & 价格](https://api-docs.deepseek.com/zh-cn/quick_start/pricing/) · DeepSeek API Docs · 2026-08-13 抓取
- 涉及文章: [DeepSeek V4 Pro 0813（on OpenRouter）](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) · Simon Willison’s Weblog · 2026-08-12
- 涉及文章: [实测正式版 DeepSeek V4 Pro，补齐 Agent 和图像能力](https://www.36kr.com/p/3937317630147971) · 极客公园／36氪 · 2026-08-13
- 涉及文章: 华尔街见闻报道 · 华尔街见闻 · 抓取失败，正文为登录空壳
- 涉及材料: DeepSeek小助手聊天截图及跑分图 · 用户提供 · 截图未标日期

## 核心主张

DeepSeek-V4-Pro 的完整权重已经由官方账号放到 Hugging Face，可下载并采用 MIT 许可证。模型卡列出 1.6 万亿总参数、490 亿激活参数和 100 万 token 上下文；官方自报 Max 模式在 SWE Verified 得 80.6％。与此同时，DeepSeek Harness 开发者预览版开始面向全球开发者开放测试，并同步开放源代码。这不再只是一次 API 静默更新，而是模型和 Agent 执行框架一起开放。

## 为什么值得看（钩子）

Harness 把模型、工具、技能、会话、沙箱、存储、循环、调度和 UI 全部做成插件，开发者无需修改源码就能替换和重组能力。每次运行还会把系统提示词、思维链、工具调用、子 Agent 调度和上下文注入写入仅追加日志，支持恢复、分叉、检索与回放。DeepSeek 开始把「模型如何变成能持续工作的 Agent」这层基础设施也交给开发者。

## 关键细节 / 引述

- API 文档可直接确认：`deepseek-v4-pro` 对应的模型版本是 `DeepSeek-V4-Pro-0813`，支持思考与非思考模式、1M 上下文、最大 384K 输出、JSON Output、Tool Calls、Responses API、Anthropic API、对话前缀续写和 FIM 补全；OpenAI 格式 Base URL 为 `https://api.deepseek.com`，Anthropic 格式为 `https://api.deepseek.com/anthropic`。
- 官方 Hugging Face 权重页使用 MIT 许可证，模型总参数 1.6 万亿、每次激活 490 亿、支持 100 万 token 上下文。模型卡 Introduction 仍残留 preview version 字样，但权重文件、许可证和正式评测表均已公开，日报只写「开放完整权重」。
- 官方自报 DeepSeek-V4-Pro-Max 在 SWE Verified 得 80.6％、Terminal Bench 2.0 得 67.9％。正文只保留一个代表性数字，并明确是官方自报。
- Harness 官网明确写「开发者预览版面向全球 Harness 开发者开放测试，并同步开放源代码」，页面底部标注 MIT；GitHub 仓库也已公开，并警告开发者预览期会出现破坏兼容性的改动。
- Harness 的核心口号是「一切皆插件」：模型、工具、技能、会话、沙箱、存储、循环、调度和 UI 均可组合、替换与扩展。
- Harness 的会话日志采用仅追加设计，记录系统提示词、思维链、工具调用与结果、子 Agent 调度和上下文注入，支持恢复、分叉、检索与回放。官方提供标准、PTC、极简和创造四种模式，可用 `npx @deepseek-ai/dsh web` 一键启动。
- API 文档当前列价为：每百万 tokens 缓存命中输入 0.025 元、未命中输入 3 元、输出 6 元，并发限制 500；页面同时预告 DeepSeek API 近期将整体上调定价，且“预计涨幅较大”，具体方案仍待正式通知。
- 用户提供的聊天截图显示，账号“DeepSeek小助手@深度求索”称：“DeepSeek V4 Pro 正式版已经更新至 API，调用模型名不变。新版本增强了 Agent 能力，支持 Responses API 和 Codex 接入。”截图本身是转存材料；Simon Willison 也称，据他判断，跑分最初发布在 DeepSeek 官方微信群，随后被转贴到 Reddit 和 Hacker News。
- DeepSeek 配套榜单自报：V4-Pro-0813 在 DeepSWE、CyberGym、Terminal Bench 2.1、DSBench-Hard 上分别为 62.7、83.3、87.9、67.2；预览版对应为 12.8、52.7、72.1、31.1。榜单也显示它并非全面第一，例如 HLE 无工具为 42.7，低于图中的 Opus 4.8 49.8 和 Fable 5 53.3；上述数字均应归为官方自报，而非媒体独立复现。
- 极客公园称，8 月 13 日凌晨 API 文档更新后，模型名仍为 `deepseek-v4-pro`，fingerprint 变为 `fp_v4pro_20260812`。该媒体用 API 做了三个代码任务：Boids 模拟约 170 秒生成 761 行 HTML，一次运行通过；模糊需求的番茄钟生成 1223 行代码，并自行补上任务标签、统计、快捷键和白噪音；关闭 thinking 后，寻路可视化在 54 秒内输出完整 715 行代码。
- 同一媒体实测也发现明显使用陷阱：寻路任务在默认 thinking 模式下用满 16384 个输出 tokens，其中 13394 个用于“思考”，留给代码不足 3000 tokens，结果 HTML 中途截断；关闭 thinking 后才完整生成。因此“推理更久”在大段代码输出场景里未必更好，开发者需要关掉 thinking 或提高 `max_tokens`。
- Simon Willison 早先「尚未确认是否开放权重」的判断已被官方权重页更新覆盖，不再作为当前结论。

## 与近期的关系

这是当天晚些时候出现的正式增量：早间只能确认 API 更新和 Agent 跑分，现已新增可下载的官方权重、MIT 许可证，以及真正公开测试和开源的 Harness。正文集中写「模型＋执行框架一起开放」，不再保留 thinking 输出预算等次要实测。
