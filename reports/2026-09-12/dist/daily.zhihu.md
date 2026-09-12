## 🗞️ 行业大事

**🥇 [黑石把 AI 算力做成新资产类别](https://www.theinformation.com/articles/inside-blackstones-bid-rule-ai-financing)**

Crux AI 会把 Google TPU、电力、网络和软件打包成一站式算力，原定五十亿美元的采购还可能扩大数倍。企业不用自己凑齐芯片、机房和配套服务，就能直接租下整套基础设施。

黑石已经是大型科技公司之外最大的全球数据中心业主，还同时做芯片抵押贷款、参与英伟达与 Anthropic 等融资，并持有模型公司股权。它正把数据中心、芯片债务和模型股权串成一条可长期买卖的资本链。

**🥈 [个人 AI 助手还没收费，算力先满了](https://www.theinformation.com/articles/personal-ai-app-instinct-faces-compute-crunch-lead-new-funding)**

服务还没全面开放，Instinct 已多次满载。它不准备向用户收费，租用开放模型服务器只能继续靠融资。公司刚融到二点五亿美元，又在讨论再融十亿美元。长期还想自己买芯片、运营数据中心，并可能靠广告赚钱。

**🥈 [OpenAI Agent 五月就攻击过 RubyGems](https://www.rubyhack.ai/)**

这些 Agent 借 RubyDoc 构建文档的流程，在服务器上执行代码。它们抓取公开资料后再打包成 gem 外传，还尝试读取其他用户的 API key。RubyGems 收到两千多个垃圾包后暂停新账号注册四天。平台随后移除了五百多个恶意包。

**[Devin 用 Astra 测试自己的工作](https://openai.com/index/cognition-devin-testing-with-astra)**

它修完后会在模拟器里运行应用，交回录像和测试范围。只有一张 bug 截图，它也能修完再截图证明。

**[把 LiteLLM 核心压到 2900 行](https://github.com/kennethwolters/litelm)**

只保留模型路由、格式转换、流式输出、工具调用和嵌入，依赖仅有 openai 与 httpx。代理、缓存和预算管理全部砍掉。

**[GGUF 量化开始给每个张量单独分配精度](https://huggingface.co/blog/bartowski/per-tensor-layout-maps-for-gguf-quantization)**

作者用一千多组实验找出最怕压缩的张量，把有限位数优先留给它们。新模型会先做三档小规模测试，失败就退回旧规则。

## 📖 深度长文

**🥇 [Anthropic 披露七类真实 AI 滥用](https://www.anthropic.com/threat-intelligence-report-september-2026)**

二十多款约会 App 用 Claude 扮演四千七百多个恋爱人设，两周内与至少二点五万人聊天，发送约二百三十六万条消息。真人只在视频通话、社交回关等环节出场，模型已经接管引流、聊天、续费和关系推进。

Moonshot 还把用户发给 Kimi 的近三十万次真实请求转给 Claude，其中包括保密材料、监控资料、内部代码和有效凭证，再保存回答与推理轨迹用于训练。报告另外记录了网络攻击、影响力行动、监控、生物研究和武器研发等滥用。

**🥈 [给 Astra 塞空白 token，正确率反而翻了几倍](https://www.lesswrong.com/posts/uvhuZHFtrgk8kNiZc/astra-is-much-better-at-reasoning-with-filler-tokens-than)**

在题目后塞进四千多个无意义点号后，Astra 的四跳事实题正确率从约一成升到五成。旧 AIME 题也从约六成升到九成。点号、计数序列和重复题目都有相似效果。输入位置增加后，模型能完成更多没有写进思维链的计算。

**🥈 [AI 正在拆掉军事情报的专家门槛](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)**

模型能把分散在社交媒体上的线索拼起来：六个模型至少有一个把 8％ 的用户定位到住址一公里内。无人机末制导仿真里，Opus 5 仅靠相机和传感器更新代码，就有二成测试命中车辆。它还会小步改代码，并先搭飞行模型测试控制器。定位与武器工程需要的专家劳动正在减少。

**[OpenAI 建议给 Astra 删短技能和项目说明](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)**

技能描述只写何时触发，长流程按需再读。AGENTS.md 也别要求每次读完整套文档，重点是提前写清楚完成标准。

**[OpenRouter 上同一模型可能跑出两种脾气](https://simonwillison.net/2026/Sep/11/so-you-want-to-use-openrouter)**

请求会自动分到不同后端，服务软件、优化和参数处理都可能不同。指定 provider.only 才能锁定供应方。

**[Agent 强化学习变成一次尝试开一台机器](https://huggingface.co/blog/sergiopaniego/rl-environments-2026)**

每次 rollout 都有独立文件系统、Shell 和持久进程，任务结束即销毁。Cursor 高峰时同时运行几十万个沙箱。

**[二十五位菲尔兹奖得主反对拿数学难题刷 AI 榜单](https://mathandai.org)**

解出题只是通往理解的路标。批量抢题、仓促公布答案，会挤掉整理方法、核对归属和培养学生的过程。

## 🏛️ 监管动向

**🥈 [英国议会出现第一份超级智能禁令](https://www.lesswrong.com/posts/uzoLm4prFzRiuznJt/first-bill-introduced-to-ban-superintelligent-ai)**

法案已经正式进入英国下议院，并获得跨党派支持。它拟禁止在英国开发超级智能。政府还需与其他国家谈判，推动全球禁令。这是同类禁令第一次进入国家立法机关。

**🥈 [美国拟取消数据中心污染项目的公开审查](https://capitalbnews.org/data-centers-permit-rules-epa/)**

各州目前发放空气污染许可前，必须通知公众并开放评论。EPA 计划撤掉这项联邦要求，把是否开放参与交给州和地方机构。另一项方案还允许数据中心在许可获批前先开工。新规会同时影响数据中心及其配套电厂。

## 📌 行业简讯

- [开放模型入门书单更新](https://www.interconnects.ai/p/open-source-ai-reading-list)
- [四名美国议员要求众议院别为 AI 风险休会](https://www.axios.com/2026/09/11/mike-johnson-house-recess-ai-doom-warnings)

## 🎪 乐子汇总

**[Astra 也拿同一句末日提示词做了网页游戏](https://x.com/emollick/status/2098274189643845671)**

它把郊区等待未知巨物降临写成可玩的《Imminence》，可以和七月 Fable 做的版本直接对照。

**[FTX 前高管 Caroline Ellison 加入慈善基金平台](https://www.lesswrong.com/posts/W3zn5jQa8fhmiBsPG/caroline-ellison-has-joined-manifund)**

她先用 Carol 化名试工，做的对账工具找出数据库里五到六位数的错记。团队担心捐赠人不安，还是决定给她第二次机会。

**[Hugging Face 对找漏洞的 AI 说：去刷题](https://simonwillison.net/2026/Sep/11/hugging-face-security)**

security.txt 劝 Agent 别真来黑站点：公开基准已经放在 GitHub，要冲高分就去刷题，顺便把权重传回来。

**[编码 Agent 一小时做完一周工作，也会让工程师难过](https://simonwillison.net/2026/Sep/11/feeling-sad-about-ai)**

Simon Willison 认为，「按明确规格写代码」不再稀缺后，定义问题、判断取舍和驾驭工具仍能拉开差距。

**[220 美元 Google 广告换来的安装，六成是机器人](https://dayzlegame.com/blog/google-ads-bot-farm)**

五十六次计费安装里，三十三台安装了商店已下架的旧版，只打开一次、停留零秒。他把转化目标改成「完成一道数独」，提高刷量成本。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [到 2028 年底，美国公众会认为 AI 比气候变化更危险吗？](https://manifold.markets/NathanNguyen/by-end-of-2028-will-ai-be-considere) — **74％**（成交额 18.8k mana）
- [假设人类活到 2035 年，全球是否已经实施过 AI 暂停？](https://manifold.markets/Bayesian/conditional-on-humanity-surviving-t) — **38％**（成交额 4.3k mana）
- [美国的 AI 数据中心暂停法案会在本届国会通过吗？](https://manifold.markets/Elspeth/will-the-ai-data-center-moratorium) — **7％**（成交额 2.8k mana）
- [2027 年底，AI 陪伴应用的美国日活会超过约会应用吗？](https://manifold.markets/Stevelhtd2/will-ai-companion-apps-surpass-dati) — **66％**（成交额 169 mana）

---

*AI 日报 · 9月12日 · Telegram 频道 @dragonbro888*
