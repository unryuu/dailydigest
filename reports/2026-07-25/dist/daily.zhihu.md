## 🗞️ 行业大事

**🥇 [Anthropic 发布 Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)**

价格跟 Opus 4.8 一样。官方在 System Card 里说，整体上不会比 Fable 5 更强。

跑分显示，SWE-bench Pro、HLE 这些老基准，Opus 5 微弱落后 Fable 5；在需要长时间摸索的任务上，差距更大。FrontierBench 从 Opus 4.8 的 21.1 跳到 43.3，ARC-AGI-3 从 1.5 跳到 30.2，OSWorld 2.0 电脑操作 70.6。

知识截止 2026 年 5 月，比旗舰 Fable 5 还新四个月。综合指数 AECI 162.1 名义上最高，但官方说 Mythos 5 有 161.3，统计上无法区分。官方还说，Opus 5 在很多案例里，对自己并不确定的答案很笃定，事实性幻觉比 4.8 略多。

Ethan Mollick 发布前拿到内测，评价是短任务能追平 Fable，长任务显得没那么有野心。他说这已经是他的主力，唯独继承了 Fable 那套语言癖好。HN 上讨论成本口径：不应拿 max 档对比，high 档每个任务只要 1.06 美元，比 Opus 4.8 的 max 便宜。

**[Opus 5 的 20 万字系统提示词疑似泄露](https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/OPUS-5.md)**

比六月 Fable 5 那份多六成，新增内容主要是记忆系统的说明书、工具调用和写作规范、安全提醒、语言风格、交互规则等。Fable 5 出口管制下架的完整时间线也在里面。Anthropic 官方未回应。

**[AI 高层私下最怕被改造过的病原体](https://www.axios.com/2026/07/24/ai-risk-bioweapons)**

他们担心前沿模型能找出让病原体更难检出的改造方法。关于 2030 年前是否会出现死亡超百万的灾难，272 名专家调查给出 12% 的概率。

**[Kimi K3 花 27 分钟在最新 Redis 上挖出 0day](https://news.ycombinator.com/item?id=49024938)**

研究者 Chaofan Shou 同时开 32 个 agent 跑，专挑内存破坏类漏洞。他说这是头一个肯自己动手写漏洞代码的模型。

## 📖 深度长文

**🥈 [GLM 5.2 里能唤醒一个假 Claude](https://www.lesswrong.com/posts/Jc9YZEmqHgocAKiaH/does-distilling-claude-carry-the-persona-with-it)**

七个模型换身份提示词做对照，研究身份认同、涉华政治审查、说谎率、行为面板四个维度。发现 GLM 确实存在一个区别于默认人格的 Claude 角色，而 Kimi 没有第二个人格。

**🥈 [Byrnes：模型的本事主要还是模仿来的](https://www.lesswrong.com/posts/wYpjXRLqbLbnmjbJP/llms-are-still-mostly-powered-by-imitative-learning-not-rl)**

RLVR 吃掉两成训练算力，按信息量算可能只占万分之一，大部分能力仍来自预训练和模仿学习。RL 主要教它什么时候用哪一招，招式则来自人类文本。他没否认 RL 有用，只否认能力的主要功劳该记在它头上。

**[一个程序员宣布自己的编程工作已经 100% 交给 AI](https://www.lesswrong.com/posts/fGJGzZdGG8jj7Mt6P/pulling-the-fire-alarm)**

公司明确要求他别再自己写代码。他决定给自己拉响火警：办一个本地 PauseAI 分部，AI 安全捐款翻两番，但先保住工作和身体。

**[Wei Dai 提出用「长期自我修正」替掉 AI Pause](https://www.lesswrong.com/posts/2iCmDWewnZWQxxwtt/the-long-self-correction-2)**

他说更深层次的问题是，人类自身不安全：道德框架不够用、长期战略能力差、看不出自己无能、过度乐观缺乏审慎。修复这些缺陷需要的时间很漫长，甚至未必能成功，但至少大家不该把永久脱轨的权力交出去。

## 🧪 新鲜论文

**[AREX 给深度研究 agent 加了一层自审循环](https://huggingface.co/papers/2607.21461)**

找答案难、验答案容易：外层逐条核对约束，没查实的再派回去查。122B 稀疏版只激活 100 亿参数，BrowseComp 82.5%。

**[新基准让画图模型用画画回答空间题，不用报坐标](https://huggingface.co/papers/2607.21072)**

470 道题，模型直接在图上点标画作答。最好的画图模型 GPT Image 2 拿 54.5，人类 87.8。

**[微软研究：用户中途改主意，模型就跟不上了](https://huggingface.co/papers/2607.20734)**

他们把现成的单轮基准改写成多轮对话，一步步给需求，中途还会改想法。评分标准不变，各家模型的成绩都明显往下掉。

**[微软和哥大：直接拿 Claude Code 这类现成脚手架训 agent](https://huggingface.co/papers/2607.21557)**

加一层代理拦下模型调用，记成训练样本，每次 rollout 扔进云上容器并行跑，省掉了另写一个简化版脚手架。

## 🏛️ 监管动向

**🥈 [白宫给蒸馏划新线](https://www.axios.com/2026/07/24/white-house-ai-line-china)**

小规模的正当蒸馏，算开放生态的一部分，大规模隐蔽的工业级窃密，可以动制裁和实体清单。这道线主要针对中国 AI 公司。目前还没有正式文件落地。同一天上午，英伟达、微软、Meta 领衔 25 家公司发联名信，反对过早设限，OpenAI 和 Anthropic 没签。

## 📢 官方公告

**🥈 [Anthropic：给 Claude 5 的提示词该删掉八成](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models)**

官方说这么删，评测代码能力看不出会有损失。贴了新旧原文对照：旧版硬性规定了许多东西，新版只留一句。过去给用法示例，现在给示例反而把模型框死。旧模型更听末尾的指令，现在无所谓，所以重复写的也可以删。

**[Anthropic：四个模型怎么分工](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)**

官方给了个便宜办法：SWE-bench Pro 上让 Sonnet 5 配合 Fable 5 当顾问，分数差距不到 10%，价钱只要六成。

## 🎪 乐子汇总

**🥈 [外国援助怎么把当地公益组织搞垮](https://www.astralcodexten.com/p/breakdown-in-pakistan)**

公益组织的精力转向写申请和交报告；原本白干的活现在有人发工资了，志愿者觉得自己成了冤大头，开始争薪水；员工换上空调办公室和四驱车，反而丢掉了社会信任。等外国资金撤走，这些组织既回不到从前，也留不住人。

**[摄像头厂商把 GitHub 管理员 token 打包进了固件](https://hhh.hn/hanwha-github-token/)**

韩华 Vision 前端构建时，把整套 CI 环境变量写进了产物，影响他们 GitHub 几百个仓库。发邮件后 12 小时内注销。

**[15 万学生十年数据：ChatGPT 来了以后成绩没变](https://arxiv.org/abs/2607.21534)**

一所美国公立大学 8.8 万门次课程，按作业形式分成容易被 AI 代做和不容易的两类对照。成绩差异只有 0.045 分（满分 4 分）。

**[代码问题都解决了，软件怎么反而越来越难用](https://ptrchm.com/posts/nothing-works-and-everyone-is-euphoric/)**

修稳定性不进 KPI，放进汇报也不好看，大家没动力做。有的银行 App 要刷好几次脸、Slack 抢焦点、车机随机抽风。

**[Half-Life 2 在 Haiku 上原生跑起来了，4K 60 帧](https://discuss.haiku-os.org/t/haiku-nvidia-porting-nvidia-driver-for-turing-gpus/16520?page=18)**

Haiku 是 BeOS 的开源续作，开发者花了一年多移植 NVIDIA 的内核驱动。这一帧是有人拿 RTX 2080 贴的视频，游戏从源码编译。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [新出的 Opus 5，能独立干多久的活？](https://manifold.markets/Bayesian/claude-opus-5-metr-50-time-horizon-N8dzl8gI0Z)（成交额 5.9k mana）
  - 30 到 32.5 小时 **15.9%**
  - 27.5 到 30 小时 **14.2%**
  - 32.5 到 35 小时 **12.7%**
- [今年综合能力指数的榜首会落到哪一家？](https://manifold.markets/SG/top-ai-model-2026-epoch-capabilitie)（成交额 26.7k mana）
  - Anthropic **41.0%**
  - OpenAI **36.9%**
  - Google **14.5%**
- [DeepSeek 会在 2027 年前被美国封禁吗？](https://manifold.markets/RossTaylor/will-deepseek-be-banned-in-us-befor) — **12.7%**（成交额 0.7k mana 的小盘。政府部门自己停用不算数，全国范围封禁才算）
- [我会先够格参加 IMO，还是先有女朋友？](https://manifold.markets/vincentWang/will-i-qualify-for-the-imo-before-g) — **先进 IMO 66.4%**（成交额 1.4k mana 的小盘，出题人自称是 2026 年 IMO 国家队选拔集训小组的成员）

---

*AI 日报 · 7月25日 · Telegram 频道 @dragonbro888*
