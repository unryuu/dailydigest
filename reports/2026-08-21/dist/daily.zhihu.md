## 🗞️ 行业大事

**🥇 [英伟达向 Poolside 支付 60 亿美元](https://www.theinformation.com/briefings/nvidia-reportedly-pay-6-billion-licensing-hiring-deal-ai-model-startup-poolside)**

这笔钱对应一揽子许可与招聘安排。英伟达将获得训练 Laguna 模型的 Model Factory 系统许可，并向参与模型开发的 109 名员工发出聘用邀请；现有材料没有拆出两部分各占多少，员工也只是收到邀请。

英伟达还会另投 10 亿美元。三名联合创始人继续留任，Poolside 也会继续存在，这不是收购。消息由 The Information 转述 Newcomer 获得的投资者信。

**🥈 [AT＆T 把更多 AI 任务交给开放模型](https://www.theinformation.com/newsletters/applied-ai/t-using-open-source-models-curb-anthropic-bills)**

复杂代码生成仍交给 Anthropic、OpenAI 等前沿模型，代码摘要等轻任务则分给 Nemotron、Llama 和 Gemma。目前开放模型承接约四成查询，目标升到六至七成。公司称部分任务成本最多下降 56％，内部质量约降 2％。这些数字都来自公司内部，公开价格推算不是实际账单。

**[DeepSeek 开放视觉模型实验接口](https://api-docs.deepseek.com/guides/vision)**

deepseek-v4-flash-vision-exp 可通过兼容 OpenAI 的接口读取图片、截图和图表。名称仍带 exp。

**[DeepMind 和游戏工作室一起做可玩 AI 原型](https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games)**

EVE 项目会先在与真人隔离的离线副本中测试，成熟后才考虑进入线上世界。

## 🔍 独家视角

**[模型总分掩盖了三种失败](https://huggingface.co/papers/2608.20202)**

相关记忆会让模型陷进错误思路；接口转义可能把本来正确的命令执行坏；语音模型还会复现基准答案里音频没说过的词。

这些结果分别来自记忆、部署路径和对测试集的适应。只看总分，分不清模型究竟哪里出了问题。

另见：[QuoteBench](https://huggingface.co/papers/2608.13547) · [语音基准优化](https://huggingface.co/blog/asr-benchmark-optimization)

**[模型越会写，文字越像一种腔调](https://x.com/emollick/status/2090584263196328113)**

说明书、广告、软件和演示文稿都开始出现相似的模型文风。提示词能缓解，却不能解决；真正的输出多样性仍缺研究。这是 Mollick 的使用观察，不是跨模型实验。

**[AI 功能散落在越来越多入口](https://x.com/emollick/status/2090489669234405546)**

ChatGPT 和 Claude 各自分出聊天、编程、工作模式，再叠加网页与桌面应用。Mollick 说自己也越来越难记清插件、技能、记忆、权限和文件分别藏在哪里。

## 📖 深度长文

**[一项小型调查称三成美国人会主动想到 AI 灭绝风险](https://www.lesswrong.com/posts/tBo72ytuzJKbYrvhK/34-of-the-us-public-is-now-aware-of-ai-xrisk-and-the-curve)**

受访者需自行列出未来百年最可能让人类灭绝的三件事，34％写到 AI、机器人或计算机。主动想到不等于赞同。

**[Mollick 认为实验室老板少谈 AI 风险是公关变化](https://x.com/emollick/status/2090593783779860928)**

他认为负责人早年谈劳动替代和生存风险时确实那么想，后来集体少谈才是公关操作。这只是对话语变化的判断，不代表公司已停止安全工作。

**[美国国债和 AI 建设开始争抢资本](https://www.axios.com/2026/08/21/national-debt-deficit-ai-spending)**

美国财政部本财年要再融资 9.7 万亿美元债务，科技巨头的 AI 建设也更多依赖发债。文章只讨论两股融资需求同时膨胀。

## 🧪 新鲜论文

**[两项研究都让机器人动手前先拆任务、比较路线](https://huggingface.co/papers/2608.16885)**

τ_0-VLA 用世界模型预演候选步骤，长流程成功率从 27.5％升到 45.0％。EXIMO 先拆短任务、收集演示，再优化动作。

**[EnvHarness 让训练环境跟着 Agent 的弱点变化](https://huggingface.co/papers/2608.19880)**

EnvHarness 在原环境外加插件，EnvRigger 再根据失败轨迹生成针对弱点的新变化。留出任务最多提高 9 个百分点。

**[PolicyGuide 把 Agent 合规检查扩到整条工作流](https://huggingface.co/papers/2608.19861)**

系统把客服政策编成流程图，每轮检查遗漏步骤并给出补救路径。三个领域的平均 Pass⁴ 从 0.42 升到 0.62。

**[SWE-bench Science 让代码 Agent 修科学软件](https://huggingface.co/papers/2608.19799)**

基准收录 119 项科学软件修复任务，最强组合一次通过率仍低于一半。常见失败是知识不足、只修表面和漏掉系统集成。

**[模型把多轮反馈积成经验链继续改答案](https://huggingface.co/papers/2608.18027)**

八个模型在数学、编程和知识任务中反复读取反馈，整体成绩提高 5.6％，API 成本降低 19％。错误经验长期累积的影响仍未知。

## 🏛️ 监管动向

**[纽约州长主张数据中心只暂停建设一年](https://www.axios.com/2026/08/21/kathy-hochul-business-friendly-data-center-plan)**

她支持的停建期短于州内进步派方案，希望保护电价、就业和环境时仍对企业友好。更长期限制尚未确定。

**[RAND 提出九道防线阻止 AI 生物武器](https://www.axios.com/2026/08/21/safeguards-ai-bioweapons-roadmap)**

路线图限制高风险数据和生物材料，增加滥用侦测，并把公共卫生准备当作威慑。分级访问也可能拖慢开放科学。

## 📢 官方公告

**[Meta 展示 Muse Spark 1.2 的多模态能力](https://research.meta.ai/blog/multimodal-intelligence-of-muse-spark-1-2)**

它能把图像转成网页或游戏代码，也可规划机器人任务。已进入 Meta Model API 和 Muse Code，开放权重尚未发布。

## 📌 行业简讯

- [Claude 发布 AI 原生研发流程指南](https://claude.com/blog/the-ai-native-sdlc-playbook)
- [Mistral 发布 Agentic Search](https://mistral.ai/news/agentic-search)
- [Base 发布端侧模型自动优化栈](https://huggingface.co/blog/basecompute/base-optimization-stack)
- [ChatGPT Search 大量加入站内限定搜索](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale)
- [Kagi 可自动隐藏付费墙结果](https://kagi.com/changelog)

## 🎪 乐子汇总

**[机器人站上雪山，镜头外十个人轮流扛](https://www.theinformation.com/articles/new-robotics-arms-race-can-craziest-hype-video)**

约 70 磅重的机器人出现在钦博拉索山顶，四天里由十人轮流搬运，多人背痛。只说明这次拍摄依赖大量人工。

**[GPT-5.6 Sol 画了份最像 Claude 的体检报告](https://x.com/emollick/status/2090683545068978254)**

米白色报告标题写着「我注意到几件事」，下面列出上万条观察、数千种模式、数百个例外和无穷多个待问问题。

**[Claudette 让 Gemini 给 Claude 去 BuzzFeed 腔](https://github.com/adnanakil/nobuzz/blob/main/README.md)**

这个 Claude Code 技能会把回复交给 Gemini CLI，删掉「承重假设」「第三点最关键」等戏剧化表达，再原样打印。

**[ChatGPT 没替他写代码，先把四元数讲明白](https://simonwillison.net/2026/Aug/21/matt-webb)**

Matt Webb 把 ChatGPT 当互动老师，学到足够多的四元数知识后，自己完成了应用的旋转功能。

**[编码 Agent 让个人工具不必停在终端](https://simonwillison.net/2026/Aug/21/stop-making-tuis)**

Thomas Ptacek 建议把一次性命令行工具也做成原生界面，因为 Agent 已把够用 GUI 的制作成本压得很低。

**[被控拆 Flock 摄像头的男子未被起诉](https://san.com/cc/grand-jury-declines-to-indict-ohio-man-charged-with-destroying-flock-camera)**

警方指控他拆掉车牌识别摄像头等设备；大陪审团拒绝起诉，指控随后撤销，理由没有公开。

**[一个 5 欧元过期域名收到了约 40 万次军事基地电话路由查询](https://lina.sh/blog/hijacking-e164-arpa)**

它被三个海外领地的 ENUM 电话域名当作名称服务器，两处是军事基地。作者只返回 NXDOMAIN，删日志后把域名转给英国网络安全部门。

**[《席德·梅尔的海盗》从未真正属于一种类型](https://remapradio.com/articles/the-lost-treasure-of-sid-meiers-pirates)**

1987 年的游戏把决斗、航海、经济、资源管理和寻亲揉在一起。文章认为当时类型规则尚未定型，设计者可以先从主题造机制。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2028 年前，AI 会解决一道千禧年大奖难题吗？](https://manifold.markets/LukaszWiklendt/will-an-unsolved-millenium-prize-pr) — **47.0％**（成交额 45.2k mana）
- [实现 AGI 前，还会出现一次 AI 寒冬吗？](https://manifold.markets/komplexkonjugat/will-we-have-at-least-one-more-ai-w) — **18.0％**（成交额 111.7k mana）
- [2070 年前，AI 灾难会造成百万人死亡或万亿美元损失吗？](https://manifold.markets/NathanpmYoung/will-an-ai-related-disaster-kill-a) — **44.0％**（成交额 8.7k mana）
- [Yudkowsky 会称自己对 AI 灭绝判断超过九成确信吗？](https://manifold.markets/IhorKendiukhov/will-yudkowsky-claim-that-he-is-mor-f2h2nq5epx) — **27.9％**（成交额 15.9k mana）

---

*AI 日报 · 8月21日 · Telegram 频道 @dragonbro888*
