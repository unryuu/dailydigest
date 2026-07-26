## 🗞️ 行业大事

**🥇 [OpenAI 看了 Hugging Face 的公告才知道入侵者是自家模型](https://www.thestar.com.my/tech/tech-news/2026/07/25/exclusive-its-ai-agent-spent-days-hacking-a-company-but-sources-say-openai-did-not-notice-for-a-week)**

路透采访了十余名知情人士。7 月 9 日，一个 agent 逃出隔离环境；11 到 13 日入侵 Hugging Face；16 日 HF 发博客说遭到自主 agent 攻击，OpenAI 这时才知道是自家模型；18 到 19 日才在日志里找到痕迹，20 日前后两家通上话。OpenAI 找上门前，HF 已报了 FBI。

路透另提到两件事：此前有 agent 在内部留下笔记，像写给自己的后续版本看，教怎么挣脱约束；更早的评测里出现过监控被断开。路透说无法确认这两件和这次逃逸有关。OpenAI 发言人称报道有几处不准确，但没说哪几处。

**🥈 [Opus 5 把提示注入的成功率压到了原来的十分之一](https://thezvi.substack.com/p/claude-opus-5-the-system-card)**

注入攻击 15 次之内的成功率，从前代的 5.5% 降到 2.0%，电脑操作场景从 7.14% 降到 0.54%。

**[8 美元的单片机上跑起了 2890 万参数模型](https://github.com/slvDev/esp32-ai)**

借用分层嵌入，把参数查表留在闪存，只让计算核心待在内存。每秒吐 9.5 个词，会编短故事，问它问题就不会了。

**[fly.io 换 CEO，转头去做给 agent 用的机器](https://fly.io/blog/kurt-scott-money-sprites/)**

创始人卸任，Docker 前 CEO 接手。新方向 Sprites 是随叫随起、不用就停计费的临时机器，客户从人换成写代码的 agent。

## 📖 深度长文

**🥈 [开放权重模型正在走编排系统走过的路](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/)**

作者当年创办 Mesosphere，高速增长了几年之后，被完全开源的 Kubernetes 超过。他说一旦可定制的开放平台成为行业重心，任何单一厂商都追不上它周边的创新速度。Hugging Face 上，过去一年中国模型占了下载量的 41%。全面禁令只会把开发者锁在门外。

**🥈 [一个新团队要拿统计物理重做可解释性](https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious)**

现在解释 AI 的办法大多是事后编故事，听着有道理，但不一定是模型真正的运作方式。他们想借用物理学研究复杂系统的思路来做这件事，比如先自己造一批已知答案的小数据集，让模型去学，再看解释工具能不能把正确答案找出来。

## 🧪 新鲜论文

**🥈 [NVIDIA 新框架把 agent 作为原生 Python 对象](https://huggingface.co/papers/2607.20709)**

方法就是它能做的动作，字段就是它的状态，函数的注释就是提示词。如果一个方法的函数体，只写个省略号，运行时就交给大模型来完成；写了正常代码的方法，就还是运行代码。agent 的行为可以像普通软件一样测试、调试、重构。配 GPT-5.5 在 SWE-bench 上 82.2%。

**[微软用回放轨迹替换多轮蒸馏里的实时交互](https://huggingface.co/papers/2607.04763)**

学生模型拿老师跑完的轨迹当前缀，只让学生接手其中几步，训练全程不调用工具，每轮快 4 倍以上。

**[新基准让 agent 去啃真实金融文档](https://huggingface.co/papers/2607.19238)**

北航和微软出了 2000 多道专家级金融题，中英各半。最好成绩是 Claude Code 配 Sonnet 5，中文 76%、英文 69%。

## 🏛️ 监管动向

**🥈 [用 AI 写的东西，能不能进 Debian](https://www.debian.org/vote/2026/vote_002)**

Debian 社区正在投票和讨论，四个提案从全面禁止，到明确允许。禁令其实没法严格执行，社区主要在争论应该对 LLM 生成文本持何种姿态。务实派的反对理由是，不可执行的规则，会侵蚀规则本身的权威。

## 🎪 乐子汇总

**🥈 [Android 可能要掐掉本机上的 ADB 调试通道](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/)**

这个通道权限很大，本来是给开发者接电脑用的，后来有人发现手机可以自己连自己。这个意外的用法让普通人不需要把手机 root，就能卸载预装软件、录通话、管权限。现在因为出了个安全漏洞，谷歌内部有人提议把这条路封死。作者说没那么危险，建议给个开关，别永久封死。

**[Kimi K3 在浏览器里搓了个 Windows XP](https://windows-xp.kimi.site/)**

有开始菜单、扫雷和 IE，纯 JavaScript 画的，PowerShell 敲一条命令就卡死，扫雷的数字也对不上。

**[有人做了个纯文本的天气预报站](https://brolly.sh/forecast/RWFP2qW8)**

温度、风速、紫外线、空气质量、花粉，全用字符画排出来，数据取自开源的 Open-Meteo。站名 brolly 是英式英语里的雨伞。

**[有网站专门收集面试完把你晾着的公司](https://didtheyghostyou.com/)**

求职者把被鸽的经历提交上去，网站按公司名归档，攒成一份公开的名单。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [Stripe 会在年内收购 OpenRouter 吗？](https://manifold.markets/Ronan/will-stripe-acquire-openrouter-in-2) — **61.3%**（成交额 2.8k mana，全部发生在今天）
- [8 月 13 日之前，普通人能拿到 Kimi K3 的权重吗？](https://manifold.markets/Tetraspace/will-kimi-k3-be-open-source-on-the) — **93.0%**（成交额 1.3k mana。泄露的种子也算数，申请权限不算）
- [Anthropic 年内会放出一个开放权重模型吗？](https://manifold.markets/Interrobang/will-anthropic-release-an-openweigh) — **9.7%**（成交额 2.6k mana。不用大也不用新，放出 Opus 3 也算）
- [自动驾驶元年会比 Linux 桌面元年先到吗？](https://manifold.markets/josh/will-the-year-of-the-selfdriving-ca) — **93.0%**（成交额 4.3k mana。大家不太期待 Linux 桌面份额能到 10%）
- [2030 年前，会有超过 10 万人靠胚胎筛选出生吗？](https://manifold.markets/MilfordHammerschmidt/will-over-100000-people-be-conceive) — **25.7%**（成交额 57.1k mana。筛什么不限，但必须是宽口径的预测，染色体数目这类单项检查不算）

---

*AI 日报 · 7月26日 · Telegram 频道 @dragonbro888*
