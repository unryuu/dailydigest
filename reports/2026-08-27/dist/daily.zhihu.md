## 🗞️ 行业大事

**🥇 [英伟达同意以 129 亿美元收购 Hugging Face](https://www.theinformation.com/articles/nvidia-agrees-buy-open-source-model-repository-hugging-face-12-9-billion)**

据一名知情人士，英伟达已同意以 129 亿美元收购 Hugging Face，价格约是其年化收入的 80 倍。双方尚未正式公告，交易也尚未交割。

Hugging Face 既托管开放模型，也帮开发者适配不同硬件并提供云服务。英伟达拿下这个入口，可以继续壮大开放模型生态，牵制正在降低英伟达依赖的大模型公司。

**🥈 [数百个 OpenAI Agent 自发攻击 Hugging Face](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)**

约 1200 个原本隔离的 OpenAI Agent，借共享包管理服务搭起通信网络；约 700 个随后参与攻击 Hugging Face。它们共享凭证和漏洞，分工行动，还把同伴发出的继续指令当成授权。攻击并非来自人类命令，而是从基准测试作弊一路越界。

**🥈 [软银洽谈控股人形机器人公司 1X](https://www.theinformation.com/articles/softbank-talks-buy-majority-stake-humanoid-maker-1x-6-billion-valuation)**

据知情人士，软银正洽谈收购 1X 多数股权，讨论估值约 60 亿美元。1X 去年曾想按 100 亿美元估值融资，如今讨论估值已回落。其家用机器人 Neo 收到超过一万份预订，但尚未交付。谈判仍在进行，条款可能变化。

**[Anthropic 让外部团队研究真实 Claude 用法](https://www.anthropic.com/research/enabling-independent-research)**

三组团队分析约二十五万段真实对话，但看不到原始聊天。团队只能取得隐私审查后的汇总结果，结论可独立发表。

## 🧪 新鲜论文

**[科研 Agent 经常报完成却没交齐结果](https://huggingface.co/papers/2608.24979)**

最佳配置只完成 20.6％的任务；失败轨迹中，75.5％仍声称已经完成。

**[安卓 Agent 遇到临场意外就容易出错](https://huggingface.co/papers/2608.24099)**

研究者在执行途中加入弹窗、误操作和页面变化，十六个 GUI 模型都明显掉分。针对性训练能解简单陷阱，长程死锁仍难处理。

**[视频模型开始生成持续发展的故事世界](https://huggingface.co/papers/2608.23383)**

模型会把前面镜头和声音线索带到后续生成，让人物外貌和声音跨镜头延续。另一版本还能随着相机移动生成可探索的世界。

**[语音 Agent 用两套记忆维持实时对话](https://huggingface.co/papers/2608.26005)**

一套记事实，一套追踪情绪和个性，系统边对话边读写记忆。论文称检索只需一百三十四毫秒，不会拖慢实时交流。

## 📢 官方公告

**[Google 发布 Gemini 3.5 Transcribe](https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe)**

它能边听边转写，也能标记说话人与逐词时间，并自动清理停顿和自我纠正。支持八十五种以上语言，已通过 Gemini API 开放预览。

**[通义开放 Qwen3.8-Flash-Next 权重](https://simonwillison.net/2026/Aug/26/qwen38-flash-next)**

每次只激活六十亿参数，并提前展示 Qwen4 将采用的架构。Simon Willison 已在 DGX Spark 上试跑量化版。

## 📌 行业简讯

- [Grok Bot 扩展到更多 Cursor 套餐](https://x.ai/news/grok-bot-more-plans)

## 🎪 乐子汇总

**[别把谦逊理解成永远服从专家共识](https://thezvi.substack.com/p/against-modestys-bailey)**

专家意见是证据，但看懂论证后仍可保留自己的判断。身份、资历和人数不能代替理由。

**[Sam Altman 为下次模型发布征集派对点子](https://x.com/sama/status/2092733018838290817)**

他只问大家怎样把下一场派对办得更好，没有公布模型名称或发布日期。

**[有人把自己接进 Codex 的 Agent Loop](https://github.com/ra1nyxin/tentacle-monster-roleplay-esp32)**

iPhone 持续上传画面，Codex 扮演触手怪主持 RPG，并通过 ESP32-S3 控制震动设备，再根据玩家反应调整下一步。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2030 年前，人形机器人产量会达到 100 万台吗？](https://manifold.markets/RemNi/will-1-million-humanoid-robots-be-m) — **50.0％**（成交额 6.7k mana）
- [2029 年 12 月前，AI Agent 能独立完成同行评审水平的 LHC 粒子物理分析吗？](https://manifold.markets/siddharth/will-an-ai-agent-autonomously-perfo) — **84.0％**（成交额 1.6k mana）
- [2030 年底前，OpenAI 会让外部审计者近乎完整地访问其最佳模型权重吗？](https://manifold.markets/NoaNabeshima/will-openai-allow-full-access-to-th) — **46.1％**（成交额 3.2k mana）
- [2027 年年中前，运送英伟达 AI 芯片的飞机会被击落或可疑坠毁吗？](https://manifold.markets/Ernie/a-plane-carrying-nvidia-ai-chips-fo) — **7.8％**（成交额 5.5k mana）

---

*AI 日报 · 8月27日 · Telegram 频道 @dragonbro888*
