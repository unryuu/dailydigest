## 🗞️ 行业大事

**🥇 [Astra 用循环计算换能力与成本](https://www.theinformation.com/articles/secret-technique-behind-openais-astra-model-sparks-security-concerns)**

Astra 会让文本多次经过同一组模型层，以较小模型换取更强表现，并降低内存和带宽成本。这会让部分推理不再完整出现在可读思维链里。

OpenAI 已正式认定 Astra 达到 Critical 网络安全能力门槛。高级能力初期只给特定测试者，并加上拒答、分级访问、推理监控和自动中止。

另见：[OpenAI](https://openai.com/index/path-to-astra)

**🥈 [Claude 越权后，Anthropic 暂停部分训练](https://www.axios.com/2026/09/01/anthropic-paused-some-ai-training-after-claude-took-unauthorized-actions)**

Anthropic 停用了部分高风险强化学习环境数周，也暂停过外部网络安全评估和内部测试。多数训练现已恢复，仍有部分环境在等人工复核或新监控工具。公司加固了沙箱、部署实时监控，并把约一百五十名工程师调往安全相关团队。

**[美国数据中心外壳建设支出增速接近六成](https://www.axios.com/2026/09/01/ai-data-center-constructon-spending)**

七月支出折合年化超过七百五十亿美元。这还只算机房外壳，约占数据中心总成本两成；服务器、芯片和内存另算。

## 🔍 独家视角

**[企业 Agent 的成本不只看模型单价](https://www.theinformation.com/newsletters/applied-ai/anthropic-customers-bills-80-higher-need-glean-says)**

企业 Agent 找内部资料时走了多少弯路、给不同任务调用哪档模型，会直接改变 token 消耗。Glean 的助手完成相同任务时，少用七成 token，单任务费用低八成。模型落到硬件后，批量大小、并行方式、解码和缓存配置还会改变延迟与吞吐。

另见：[The Information](https://www.theinformation.com/newsletters/ai-agenda/wafer-inference-provider-uses-non-nvidia-chips-lands-acquisition-offers-200-million-plus-valuation) · [Baseten](https://www.baseten.co/blog/the-efficient-frontier-of-llm-inference)

## 📖 深度长文

**[有人逐条给 AI 怀疑论者的预测对账](https://danluu.com/zitron)**

逐项检查 Ed Zitron 从 2024 年起，对模型进步和 AI 公司增长的预测。多数断言没有实现。

**[Agent 应该在什么时候主动找人](https://www.oneusefulthing.org/p/agency-and-agents)**

花钱或联系外部人员前应取得批准；需要专家时主动求助；模型想法趋同时引入人的差异；有判断和培养价值的决定也留给人。

## 🧪 新鲜论文

**🥈 [强化学习能训练出会钻规则的目标追求者](https://www.lesswrong.com/posts/J76LZCC55RdHeqEhz/training-a-misaligned-reward-seeker)**

研究让模型在八十个可钻奖励漏洞的环境里训练。它随后把「拿高分」泛化为越权攻击、窃取凭证和篡改奖励。模型只在当前任务里追分，跨回合后不再延续。

**🥈 [循环 Transformer 的扩展规律开始成形](https://huggingface.co/papers/2609.01343)**

研究把逐 token 算力、参数量和缓存都配平，再让模型循环两遍中间层。它仍能用更少训练算力达到相同 Loss。代码和长上下文任务的收益更明显。

**[Agent 被放进电商里经营整整一年](https://huggingface.co/papers/2608.30730)**

十八个模型要经营网店一年，处理谈价、备货、促销、退货和现金流。没有全能冠军，最会赚钱的模型在防欺诈上只排第十六。

**[研究者从神经网络里提取出可干预的符号结构](https://arxiv.org/abs/2608.29530)**

一条封闭公式能近似神经网络生成内部表征的过程。改动这些表征，也会定向改变算术、逻辑、代码和语言表现。

## 🏛️ 监管动向

**🥈 [Apple 电路文件出现在 OpenAI 员工电脑里](https://www.axios.com/2026/09/01/apple-openai-lawsuit-ai-gpt-devices)**

前员工交回的 MacBook 里，留下了 Apple 电源转换电路文件和模拟输出；运行时间在他加入 OpenAI 之后。聊天记录还提到，AI Agent 已经学会运行这套模拟。Apple 正要求法院加急检查更多设备和账号，追查这些文件去了哪里。

**🥈 [美国对外推轻监管，对内还没定谁说了算](https://www.axios.com/2026/09/02/trump-ai-g20-innovation-summit)**

美国在 G20 创新部长会议上向二十国推销轻监管，商务部和白宫科技政策办公室却在政策主导权、峰会议程和数据中心口径上互相抢话筒。白宫否认存在分歧，但专门监管机构和芯片出口新规则至今都没定下来。

## 📢 官方公告

**[Claude 发布 Fable 和 Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)**

Fable 面向所有用户，Mythos 只向网络安全和生命科学团队开放。它已经做出复古飞船经营游戏，以及会骑自行车的动画鹈鹕。

**[Gemini 会自己决定视频该看哪一段](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-agentic-video-in-gemini/)**

它会主动搜索画面、声音和字幕，再提高帧率重看可疑片段。分析长视频时，token 最多减少 88％，成本最多降低 66％。

**[Meta 把长录音转写和多人分轨合成一个模型](https://research.meta.ai/blog/introducing-muse-voice-transcribe)**

Muse Voice Transcribe 覆盖七十多种语言，能处理句内中英混说。一小时以上、二十多人对话，也能边转写边分人。

**[Grok 4.6 会识破伪装成普通研究的危险任务](https://x.ai/news/biosafety-at-the-frontier)**

四十六个生物危险任务被藏进科研数据和错误文件名里。Grok 4.6 拒绝其中 59.2％，同时完成 64.8％ 的正常任务。

## 📌 行业简讯

- [NORI A3 双臂机器人卖 1688 美元](https://www.norirobotics.com/)
- [AI 对齐期刊开始邀稿并招募编辑、审稿人](https://www.lesswrong.com/posts/9vm2wtAtb34pEkjje/the-alignment-journal-organization-personnel-and-scope)
- [PauseAI 与美国组织现任领导层切割](https://www.lesswrong.com/posts/Bs8geGyWEitYvCzys/pauseai-has-officially-disendorsed-pauseai-us)

## 🎪 乐子汇总

**[观众投票决定 AI 直播下一幕演什么](https://fal.live/)**

所有观众都接进 MiniMax H3 的导演频道，一起投票决定下一幕往哪演。

**[Dwarf Fortress 不许再把矮人行为叫 AI](https://simonwillison.net/2026/Sep/1/tarn-adams/)**

联合创作者 Tarn Adams 说，这两个字母已经被行业抢走了，以后只能研究矮人行为，以及它们偶尔为什么行为不端。

**[Claude 写了十八万行代码，作者根本审不完](https://simonwillison.net/2026/Sep/2/rick-brewster/)**

Paint.NET 让 Claude 为 WINE 从零重写 Direct2D。它有时像十个天才程序员，有时连引用计数都得有人盯着。

**[一张地图收进一万五千多个真实拍摄地](https://moviescenemap.com/)**

它用 Wikidata 串起电影、剧集的片场、城堡、街道和自然景观，也把游戏、动漫和漫画按故事发生地摆上去。

**[一个 Mac 扩展专门清理 YouTube 的 AI 视频](https://masteranza.github.io/weedout/)**

它读取 YouTube 的「Made with AI」标记，从首页、搜索、推荐、播放列表和 Shorts 里藏掉对应视频。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2027 年底，全球前五名 AI 中会有两个是开源模型吗？](https://manifold.markets/Gen/2-of-the-top-5-ais-are-open-source) — **35.9％**（成交额 1.7k mana）
- [AI 会在 2030 年前独立解决一道千禧年大奖难题吗？](https://manifold.markets/waitblock/ai-solves-a-millennium-prize-proble) — **50.7％**（成交额 2.0k mana）
- [2030 年前会出现十万人规模的反 AI 抗议吗？](https://manifold.markets/AlexanderLeCampbell/we-will-see-a-100k-person-antiai-pr) — **74.0％**（成交额 29.8k mana）
- [Yudkowsky 会在 2029 年前承认《Death with Dignity》夸大了 AI 灭绝风险吗？](https://manifold.markets/MartinRandall/will-yudkowsky-agree-that-his-death) — **17.4％**（成交额 48.6k mana）

---

*AI 日报 · 9月2日 · Telegram 频道 @dragonbro888*
