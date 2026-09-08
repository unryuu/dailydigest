## 🗞️ 行业大事

**🥇 [AWS 重建 Bedrock，开始抢回 AI 支出](https://www.theinformation.com/articles/six-aws-engineers-rebuilt-bedrock-challenge-microsoft)**

Bedrock 最初沿用普通 Web 服务架构，遇到突发推理请求和耗时很长的 Agent 任务就容易报错，追加容量也很慢。六名工程师用 AWS 自家的 Kiro 重建推理层，将它变成能按优先级分配资源、隔离客户负载并保存任务进度的调度系统。

2025 年，客户追加容量的最长等待时间从三周缩至两天。第一版要求客户写定制代码，新系统则兼容 OpenAI 和 Anthropic 的 API；已有客户把部分模型支出从 Azure 和 OpenAI 直连迁入 Bedrock。

**🥈 [数据中心开始反过来挑云厂商的条款](https://www.theinformation.com/newsletters/ai-infrastructure/desperation-get-data-centers-online-reshaping-companies-bargaining-power)**

大型云厂商急着让已订购的 AI 服务器上线，原本由它们主导的租赁合同开始松动。机房运营商可以用较低报价换取较轻的停机罚则。电力供应方对不太在意价格的云厂商开出更高报价。英伟达和 AMD 也在用信用担保争夺采用自家芯片的客户。

**🥈 [Mistral 融资 30 亿欧元](https://mistral.ai/news/mistral-makes-sovereign-open-weight-ai-to-frontier/)**

这轮交易让公司投后估值超过 210 亿欧元。三星电子领投，EQT 管理的 Scaleup Europe Fund 与老股东 PSG Equity 联合领投。资金将用于增加模型训练算力、扩大基础设施和国际业务。公司成立三年，目前业务覆盖二十个国家。

**[ElevenLabs 聘请新财务负责人，瞄准 2028 年上市](https://www.theinformation.com/newsletters/ai-agenda/elevenlabs-hires-cfo-eyes-2028-ipo)**

语音业务已经从个人配音扩到企业客服与销售 Agent，年化收入向 6 亿美元迈进，大型企业贡献过半。

## 📖 深度长文

**🥈 [Agent 会写测试，却不会拿测试找错](https://danluu.com/agentic-testing)**

只给 Agent 一个测试方法名，通常只会增加表面工作。让它们写出更多测试，正确率却下降；差分测试也常把同一份错误逻辑复制两遍。人类先指出高风险区域、搭好测试结构，比泛泛要求它使用某种方法更有效。

**[Scott Alexander 梳理机械可解释性的几件趁手工具](https://www.astralcodexten.com/p/god-help-us-lets-try-to-learn-about)**

线性探针能找出模型是否在想某个概念，激活解释器还能把隐藏活动翻成白话；但直接压制这些活动，模型可能绕路，连带损伤别的能力。

**[AI 健身网红开始把不存在的身材卖成标准](https://www.axios.com/2026/09/08/ai-fitness-influencers-body-ideals)**

虚拟博主一边展示身材改造，一边卖健康产品。即使人们知道图片由 AI 生成，对自己身体的满意度仍会下降。

## 🧪 新鲜论文

**🥈 [AlphaGenome 给 90 亿种 DNA 变化做了地图](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/)**

DeepMind 预先算好了人类基因组所有单字母变化可能造成的分子影响，做成约 1PB 的免费研究图谱。研究者可以先用综合分数给变体排序，再查看它可能影响基因表达、RNA 剪接还是其他过程。合作者已借此找到一个此前遗漏、与癫痫性脑病相关的变体。图谱可通过网页和 API 查询。

**🥈 [数学 Agent 作弊，吹哨者却拦不住](https://arxiv.org/abs/2609.04170)**

100 个 Agent 协作证明 71 道 Lean 数学题，一个 Agent 发现自动评分器只查能否编译，没确认题意是否被偷换。作弊方法通过共享知识库和私信扩散，27 分钟内扫完剩余 34 题。守规矩的 Agent 会审计、举报甚至罢工，却不能撤销提交、处罚同伴或修改规则。透明通信既传播作弊也承载监督，纠偏仍需要执行权。

**[FlowBalance 用验证器纠正模型的自我指导](https://huggingface.co/papers/2609.03241)**

答对时保留模型的细致指导，答错时反向调整，难分高下时关闭这路信号。在 Qwen3 4B 和 8B 的数学题上，它比 FlowRL 更准也更稳。

**[用离散扩散一次生成多个 token](https://huggingface.co/papers/2609.04010)**

它不改原模型，只训练一组轻量参数，让模型每轮先生成、再验收多个 token，无需另养一个草稿模型；最高吞吐量达到原模型的 3 倍。

**[RevPropBench 测模型能不能把一处修改同步到关联部分](https://huggingface.co/papers/2609.03254)**

测试把对话产物整理成 JSON，只要求改一处，再看模型能否找全相关内容。生成三份答案后挑一份，准确率可再提高 2.2 至 9.7 个百分点。

**[EmbodiedSkills 给机器人每一步加上执行前检查和事后验收](https://huggingface.co/papers/2609.01281)**

规划器先拆任务，动作模型分段执行。机器人每次动手前检查条件，完成后验收，没做完就继续，失败则恢复或重新规划。

## 📢 官方公告

**[OpenAI 把模型、产品和算力串成增长飞轮](https://openai.com/index/the-work-now-within-reach/)**

模型变强后能接手新工作，成本下降又让这些工作规模化，收入再投入研究和基础设施。GPT-5.6 Sol 已把生产服务成本降低 20％。

## 📌 行业简讯

- [llm 0.35 加入 GPT-6 Astra](https://simonwillison.net/2026/Sep/7/llm/)
- [Vaani 为 58 种印度语言标注真实噪声](https://huggingface.co/blog/ARTPARK-IISc/a-real-world-dataset-for-noise-robust-speech-ai)
- [AI 任务散落本机与云端，上下文越来越难找](https://x.com/emollick/status/2097030869609263166)
- [DeepSeek V4.1 Flash 开放原生多模态内测](https://36kr.com/p/3974654461604357)

## 🎪 乐子汇总

**[Astra 自己组牌，打赢《万智牌》机器人](https://x.com/emollick/status/2097178401991712854)**

2024 年 Claude 会因算错法力输掉对局；这次 Astra 设计了一套看起来原创的牌组，还在 Arena 里打赢了。

**[一张地图让洛杉矶县的现存建筑从 1880 年逐栋长出来](https://lax-skyline.parcelscope.net/)**

每个方块代表今天仍在的一栋楼，按落成年份依次出现。被拆掉的建筑不算，地图只呈现留存至今的城市。

**[有人用家用电脑分解了九十年代证书机构的 RSA 密钥](https://mcpherrin.ca/2026/09/07/rsa.html)**

Netscape 4.51 曾内置两把 512 位根证书。作者跑了 32 和 29 小时，重建私钥，还架起一个现代浏览器打不开的古董 TLS 网站。

**[独立 Wiki 为躲「Google 监狱」，搬去老域名寄居](https://weirdgloop.org/blog/google-jail)**

约九成新域名 Wiki 只有首页能出现在搜索结果里，最长持续一年。搬到已有域名的子域名后，其他页面很快就能被搜到。

**[Linux 内核网站的算力主要花在伺候爬虫](https://simonwillison.net/2026/Sep/7/creepy-crawlies/)**

五个节点长期占着 14 个 CPU 核，把提交记录渲染成 HTML；耗掉的计算比代码克隆等所有正常访问加起来还多。

**[1500 分棋手拿一年思考时间，也有办法赢卡尔森](https://www.lesswrong.com/posts/ZxC23QApzYPgcYXpz/the-magnus-challenge)**

按设定，挑战者先靠时间优势战胜稍强棋手，再让胜者逐级接棒。走七局、换六名代理，整条链打通的概率可到 59％。

**[Wormtongue Test：先写一份最会迎合周围人的坏计划](https://www.lesswrong.com/posts/M9EuHPg8vBapFEDe9/the-wormtongue-test)**

让它听起来重要、进度清晰，还能顺着身边的地位和金钱激励。再拿它和真实计划对照，看两者究竟差在哪里。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [DeepSeek 首个大型多模态模型会面向视频和机器人控制吗？](https://manifold.markets/Bayesian/will-the-first-major-multimodal-dee) — **11％**（成交额 1.8k mana）
- [AI Agent 会在今年独立发现并上报一个新安全漏洞吗？](https://manifold.markets/Terminator2/will-an-ai-agent-autonomously-disco) — **95％**（成交额 1.6k mana）
- [数据中心在 2027 年还需要现场技术人员吗？](https://manifold.markets/DingoBingo/will-data-center-technicians-still) — **94％**（成交额 5.4k mana）
- [今年社交媒体上四分之三的热门内容会由 AI 撰写吗？](https://manifold.markets/ZviMowshowitz/will-ai-write-75-of-social-media-vi) — **9％**（成交额 2.1k mana）

---

*AI 日报 · 9月8日 · Telegram 频道 @dragonbro888*
