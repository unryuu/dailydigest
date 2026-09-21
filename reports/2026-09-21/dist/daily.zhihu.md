## 📖 深度长文

**🥈 [中国开放模型的优势走到实际采用](https://www.interconnects.ai/p/the-current-balance-of-power-in-open)**

OpenRouter 的开放模型用量中，中国模型已占八成以上。法律助手、编程工具和生活服务平台都在采用。研究论文也越来越多使用 Qwen 等中国模型。低价、能自行部署和按需定制，成了它们的吸引力。

**🥈 [AI 应该多忠于用户](https://thezvi.substack.com/p/better-call-sol-or-better-yet-claude)**

律师可以替客户辩护，同时坚持不伪造证据。Zvi 主张，AI 也能维护用户利益，同时保留底线。日常分歧先提醒，再让用户决定。严重伤害他人的要求可以拒绝；打破保密、主动违背用户利益，门槛还应更高。

## 🧪 新鲜论文

**🥈 [AI 学着 AI 审稿，判断越来越趋同](https://huggingface.co/papers/2609.20942)**

研究者先让小模型学习会议的正式评审，再把它生成的评语混进下一轮训练。混入越多，新模型对同一篇论文写出的评语就越相似，评分也更集中。只经过一轮这样的训练，不同评语之间的差异就缩小了。

**🥈 [AI 复刻软件，外观像了，功能还差很多](https://huggingface.co/papers/2609.22000)**

Astra 复刻的软件任务中，只有2.8％通过全部程序化功能测试。RecreationWorld 让 Agent 自己探索参考软件，再写出一个版本。模型更擅长复制界面，容易漏操作逻辑。比如旋转照片后按撤销，复刻版恢复了排列，却没把照片转回来。

**🥈 [Agent 付款前，再加一道权限检查](https://huggingface.co/papers/2609.22076)**

模拟银行攻防的成对测试里，违规付款从105次降到了零。APort 在转账真正执行前，用程序独立检查收款人是否获准。聊天里伪造的「已经验证」回执无法代替这道检查。

**[小米从现成代码里制造编程练习](https://huggingface.co/papers/2609.22068)**

它把开源项目中的某项功能挖空，再用原代码生成测试，让 AI 补回功能并自动判卷。

**[Apple 用一套模型操作手机、电脑和网页](https://huggingface.co/papers/2609.22083)**

MintAct 把找按钮、连续操作和调用视觉工具放进同一套训练，让模型跨不同界面办事。

## 📢 官方公告

**🥈 [Jev 开放使用，搭档 Astra 玩通《我的世界》](https://github.com/rmalde/minecraft-agent)**

Jev 接收文本或结构化状态，快速输出简短的选择或评分。游戏中，Astra 规划目标，Jev 选动作，程序寻路和执行。在预选地图、和平难度下，这套组合8分43秒完成通关。单轮模型费0.97美元，代码已公开。

**[Google 开源 AX，集中调度 Agent 任务](https://agentexecutor.io/)**

AX 为每个任务准备隔离环境，统一配置模型和联网权限，还能暂停闲置任务，之后接着运行。

**[V7 把公司文件整理成 Agent 可查的记忆](https://openai.com/index/v7/)**

它把文件里的公司、人物和数字连成关系网，每条事实保留原始出处，Agent 可直接查询。

## 📌 行业简讯

- [HF 发布 tokenizers v1 候选版](https://huggingface.co/blog/tokenizers-v1)
- [Simon 做独立页面给 Agent 配密钥](https://simonwillison.net/2026/Sep/20/llm-keys-ui/)

## 🎪 乐子汇总

**[ZuckOff 用手机发现身边的摄像眼镜](https://zuckoff.app/)**

手机监听蓝牙广播，按厂商标识识别 Meta 等眼镜，还能在后台提醒，扫描记录留在本机。

**[一位员工吐槽：大家让 Claude 写，却没人读](https://simonwillison.net/2026/Sep/20/voxium/)**

他描述新公司的同事每天工作十二三个小时，代码、需求、报告全交给 Claude，管理层还在催进度。

**[咖啡店倒闭后，复盘还在钻研风味](https://thezvi.substack.com/p/monthly-roundup-46-september-2026)**

店开在通勤小镇，九点才营业。店主却花更多篇幅聊天气如何影响咖啡，没怎么分析开门时间。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2027年前，AI 能在随机地图、不利用漏洞的条件下，十分钟内通关《我的世界》吗？](https://manifold.markets/Bayesian/ai-beats-minecraft-rsg-in-under-10-qQucd9UICy) — **12％**（成交额 91.6k mana）
- [Pinker 和 Scott Alexander 会在2026年就 AI 安全展开实时辩论吗？](https://manifold.markets/chrisjbillington/will-steven-pinker-and-scott-alexan) — **42％**（成交额 2.1k mana）
- [《半条命3》会在2026年发售吗？](https://manifold.markets/asmith/will-half-life-3-be-released-in-202) — **10％**（成交额 8.8k mana）
- [2030年底前，核聚变能持续超过24小时并获得净能量增益吗？](https://manifold.markets/JamesBills/will-a-nuclear-fusion-reaction-be-m) — **31％**（成交额 3.4k mana）

---

*AI 日报 · 9月21日 · Telegram 频道 @dragonbro888*
