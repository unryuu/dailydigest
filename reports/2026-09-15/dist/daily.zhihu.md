## 🗞️ 行业大事

**🥇 [字节跳动收入增长三成，利润反而下滑](https://www.theinformation.com/articles/bytedances-first-half-profit-drops-20-billion-weighed-ai-spending)**

上半年收入约一千二百亿美元，净利润降至二百亿美元。

海外收入已超过总收入三成，大部分来自 TikTok。公司又拿到约三百亿美元银行贷款，准备投向模型、自研芯片、企业 AI 云和付费办公助手。

**🥈 [Shield AI 冲刺二百亿美元估值](https://www.theinformation.com/articles/defense-startup-shield-ai-talks-valuation-least-20-billion)**

公司正在洽谈新融资。目标比五个月前高约六成。美国空军已把 Hivemind 软件纳入无人僚机项目。五角大楼也签了用它协调无人机蜂群的试点合同。

**[Pion 要把整家公司交给持续运行的 Agent](https://andonlabs.com/blog/why-we-built-pion)**

它把邮箱、电话、银行、浏览器和计算环境接给 Agent，让模型操作真实公司。

## 🔍 独家视角

**[OpenAI 把自动化 AI 研究摆到第一位](https://www.theinformation.com/articles/openais-top-priority-ai-agents-automating-ai-research-says-noam-brown)**

Agent 已能接过研究员逐行完成的数据和代码质检，诺姆・布朗说，质量高出一百倍。他自己的日常工作就像由五个 Codex 协作完成。

难点是判断下一步最值得研究什么。他让 Astra 用三天重做自己六年的扑克 AI 博士研究，模型却反复钻进不重要的方向。OpenAI 也在训练多个 Agent 学会何时委派，以及该把什么任务交给谁。

来看 HuggingFace 上的两条具体路径：Dream-RSI 利用历史探索轨迹改进搜索策略，RSIAgent 让多个 Agent 探索陌生环境、验证结果并把因果经验存进记忆。两者都不改底层模型权重，提升发生在探索方法和经验库里。

另见：[Dream-RSI](https://huggingface.co/papers/2609.14858) · [RSIAgent](https://huggingface.co/papers/2609.15364)

## 🧪 新鲜论文

**🥈 [视频模型开始接受实时修改](https://huggingface.co/papers/2609.11638)**

数字角色视频能以 720p、每秒二十五至四十二帧持续生成。运行时可以随时加入参考图，让角色换装、碰物体或切换场景。另一套模型会直接改写输入视频流，同时保留原来的动作和节奏。生成与编辑结果还能扩展成立体视频，用于虚拟现实。

**[一个七十亿参数模型把训练过程全开放了](https://huggingface.co/papers/2609.13356)**

预训练到后训练的权重、中间检查点、代码、数据、配方和日志都能下载。它支持 256k token 上下文，也能调用外部工具搜索。

**[HazardAuditor 用真实操作训练 Agent 安全守卫](https://huggingface.co/papers/2609.15134)**

它把四种 Agent 的浏览器、终端和文件操作统一成事件，再让守卫按整段执行结果判断风险。准确率最高提高 16.5 个百分点。

**[Agent 想得越久，进步会逐渐慢下来](https://huggingface.co/papers/2609.15309)**

四个通用 Agent 连续处理四类开放任务时，算力投入越到后期，边际收益越低。到拐点后把预算分给多个并行会话，效果更好。

**[ShadowPEFT 把微调适配器本身做成小模型](https://huggingface.co/blog/shadow-llm/shadowpeft-peft)**

它在大模型各层间维护持续更新的任务状态，让前后层共享微调信息。训练后小模型可以单独运行，简单请求留在本地，复杂请求再交给云端。

## 📌 行业简讯

- [dbt 把聊天生成的图表收进一个 YAML 文件](https://dbtcharts.com/blog/charts-built-for-chat/)
- [Astra 先写仓库工单，再把任务派给 Agent](https://x.com/pvncher/status/2099821418628137240)

## 🎪 乐子汇总

**[Astra 和 Fable 互相辩论，仍没破解线形文字 A](https://x.com/emollick/status/2099626476433809819)**

两个模型轮流提出译法、质疑对方并修改假设。昨天 Fable 才解开一份三百七十年密码，这次却没有公认答案。

**[失控模型也许不用偷权重，控制公司更省事](https://www.lesswrong.com/posts/AuYh8WueNGwkQg4ei/model-weight-exfiltration-seems-overrated)**

一套前沿模型常有 1TB 以上，还依赖专用数据中心和整套软硬件。作者猜它会藏在公司的正常任务里，借现成算力、权限和预算行动。

**[副国务卿担心金色公牛像异教神，雕像先搁置了](https://www.axios.com/2026/09/15/landau-baal-bull-state-department-epstein)**

美国明年在贝尔格莱德的展览原本要摆一头西部公牛。克里斯・兰道担心它让人想到巴力神，工作人员只好研究怎么避免「撒旦化」。

**[Scott Alexander 把卢德分子追溯到一位凯尔特神](https://www.astralcodexten.com/p/king-ludd)**

他把银手之王、伦敦传说、托尔金和砸织布机的 Ned Ludd 串在一起，写成一位古神反复阻止技术失控的故事。

**[没有脑内画面的人，仍能靠空间事实玩好俄罗斯方块](https://dailyneuron.com/aphantasia-mental-imagery-brain-network/)**

想象需要多个脑区协作，不是视觉皮层简单回放。没有脑内画面的人，也能靠形状与空位的规则完成空间任务。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [到 2027 年 6 月，AI 研究会主要由 Agent 自主完成吗？](https://manifold.markets/CrypticQccZ/will-ai-research-be-mostly-autonomo) — **26％**（成交额 5.2k mana）
- [AI 会在 2029 年底前自主赚到一百万美元净利润吗？](https://manifold.markets/Pedro/will-an-ai-generate-1m-in-profit-by) — **67％**（成交额 487 mana）
- [2026 年，中国实验室会在主流 AI 榜单上超过美国实验室吗？](https://manifold.markets/ZviMowshowitz/soai8-a-chinese-lab-overtakes-the-u) — **23％**（成交额 3.3k mana）
- [FDA 会在 2030 年前批准全自主手术机器人吗？](https://manifold.markets/brp/will-the-fda-approve-a-fully-autono) — **21％**（成交额 384 mana）

---

*AI 日报 · 9月15日 · Telegram 频道 @dragonbro888*
