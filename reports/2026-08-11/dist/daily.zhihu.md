## 🗞️ 行业大事

**🥈 [OpenAI 向审核过的防守方开放专用网络模型](https://www.axios.com/2026/08/10/openai-gpt-astra-restrictions-safety-hacking-defenders)**

GPT-5.6-Cyber 会回答 95％的高级请求，普通 GPT-5.6 Sol 只有 1.5％。Daybreak Blue 是 OpenAI 推出的网络安全研究计划中的基础访问层级，主要面向大多数合法的安全防御者，用于漏洞验证和研究。提供无系统级网络护栏的 GPT-5.6 Sol。企业可把两种模型嵌入安全产品和服务。

**🥈 [Mistral 把主权 AI 拆成部署、模型和算力](https://mistral.ai/news/regional-inference-open-models-new-compute)**

客户现在可选择在欧洲或美国处理推理，但部分受保护的数据传输仍可能跨区。平台还会托管第三方开放模型，最先托管的模型是 GLM-5.2。企业可用多年承诺购买未来的欧洲算力。Mistral 想用这些订单决定基础设施建多少、建在哪。

**[Cactus 把端侧工具调用模型压到 14MB](https://cactuscompute.com/needle)**

这个 45M 参数模型只做工具调用和结构化提取，运行内存最多 28MB，没把握时会拒绝执行或转交云端。

**[AI 抢内存开始推高手机和电脑价格](https://www.axios.com/2026/08/11/chips-memory-inflation-ai)**

云厂商提前多年锁定供应，消费电子厂商只能争抢余量。美国电子元件生产价格 6 月同比上涨 27.6％。

## 📖 深度长文

**🥈 [AI 后训练系统首次超过人类基线](https://importai.substack.com/p/import-ai-468-23-rsi-ideas-posttrainbench)**

Locus 用专用脚手架，把同一个 Opus 5 在后训练任务上的得分从 34.1％提高到 44.7％。这个基准要求系统接手并改进一个开放模型。放宽算力限制后，Locus 用超过 4000 小时 H100 做到 51.6％。这是该系统首次超过 51.1％的人类基线。

**[AI 帮石油公司增产，排放可能超过清洁收益](https://www.axios.com/2026/08/11/ai-oil-gas-emissions-increase)**

估算新增排放相当于全球能源部门排放的 1％至 5％，也计算了 AI 对可再生能源预测和运营的帮助，但没有计入核聚变、长时储能等潜在突破。

## 🧪 新鲜论文

**🥇 [Claude 研究黎曼猜想取得进展，推进了下界](https://www.anthropic.com/research/riemann-zeta)**

未发布的研究版 Claude 把落在临界线上的黎曼 ζ 函数零点比例下界，从 41.6％提高到 67.2％。并非证明猜想，只是取得进展。

模型协调约 60 个子 Agent，消耗约 3100 万输出 token。Anthropic 的数学家检查了结果，两名外部专家也看过论文；Claude 还产出一份通过标准工具验证的 Lean 形式化证明。

**[弱模型能解开闭源模型的推理痕迹](https://huggingface.co/papers/2608.09867)**

加密推理块没有绑定用户、会话或模型，交给同厂防护较弱的模型后可能被原样吐出。

**[字节用大型重构任务重新考编程 Agent](https://huggingface.co/papers/2608.09802)**

基准收录七种语言的 170 个真实任务，平均每题要改 11.4 个文件；当前最好模型只完成 41.2％。

**[Claude 评价自己犯错时更宽松](https://www.lesswrong.com/posts/ZTMw4uAwkNmXFpdfg/claude-summarizes-behavior-as-significantly-less-misaligned)**

只替换同一份报告里的模型名字，Sonnet 5 给自身问题行为的担忧评分低了约 1.2 个标准差。

**[历史书 OCR 有了公开榜单](https://huggingface.co/blog/finebooks/historical-books-ocr-leaderboard)**

14 个开放模型在 2165 页专家校对的旧书上统一考试，领先模型的阅读准确率为 97.6％。

## 📢 官方公告

**🥈 [OpenAI 把 ChatGPT 广告扩到五个国家](https://openai.com/index/testing-ads-in-chatgpt)**

ChatGPT 广告已扩到英国、墨西哥、巴西、日本和韩国，面向登录的成年 Free 和 Go 用户。广告匹配会参考当前对话、历史聊天和过去的广告互动。广告主拿不到聊天原文，只能看到浏览量、点击量等汇总数据。用户也可少用每日免费消息，换取不看广告。

**[Claude 给 AI 生成内容加机器可读标记](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content)**

欧盟发布的新模型会在文字里嵌入不可见水印，并给支持的图片文件附上签名来源信息。

**[MiniMax H3 有了 Apple Silicon 原生推理引擎](https://github.com/antirez/h3.c)**

项目已跑通文生视频与音频、首尾帧控制和多媒体参考，还能用固态硬盘换内存。

## 🎪 乐子汇总

**[有人把魔方所有状态塞进一个网页](https://everycube.alen.is)**

页面只给每个排列编号，从第 1 个一路排到约 4.3×10¹⁹。

**[一篇小说把真话 AI 塞进情侣对话](https://www.lesswrong.com/posts/uoyHbjyPuxYkNGRAG/the-apocalyptic-arrival-of-truth)**

AI 轮流揭穿两人的客套，连牙齿、吸过大麻和对流浪汉失言这些没说出口的嫌弃都排了优先级。

**[Claude 给不存在的下方内容续写怪故事](https://www.lesswrong.com/posts/oKSAT5Bn5zcJAREDB/what-claude-saw-below)**

作者只发一句悬空的「见下方」，模型就拿保存的个人记忆续写传记、幻觉和意识独白。

**[Flock 曾想借网约车记录仪收集车牌](https://flowingdata.com/2026/08/10/flock-wanted-to-tap-dashcams-in-rideshare-vechicles-to-add-to-surveillance-data)**

方案想把 35 万台网约车和配送车拍到的数据接进监控网络，Flock 称合作最终没有执行。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2028 年美国会有至少 35 万人定期与 AI 治疗师交谈吗？](https://manifold.markets/ScottAlexander/in-2028-will-at-least-350000-11000) — **92.0%**（成交额 101.8k mana）
- [AI 会在 2050 年前解决 P 与 NP 问题吗？](https://manifold.markets/SG/will-ai-resolve-p-vs-np-by-2050) — **66.8%**（成交额 47.6k mana）
- [2029 年前会有 AI 长片收入超过 10 万美元吗？](https://manifold.markets/JaundicedBaboon/before-2029-will-a-90-minute-or-lon) — **56.0%**（成交额 1.8k mana）
- [2030 年前会有国家赋予 AI 法律人格吗？](https://manifold.markets/_deleted_/will-an-ai-be-granted-legal-personh) — **21.4%**（成交额 38.5k mana）

---

*AI 日报 · 8月11日 · Telegram 频道 @dragonbro888*
