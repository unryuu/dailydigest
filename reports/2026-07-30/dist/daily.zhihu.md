## 🗞️ 行业大事

**🥇 [前沿实验室一千三百名员工发联名信，要求给 AI 研发踩刹车](https://www.pacingthefrontier.com/)**

截至 7 月 31 日已有 1306 人署名，来自 Anthropic、OpenAI 和 Google 等公司。信里请美国政府牵头一项国际合作，把将来给自动化 AI 研发踩刹车所需的技术和治理手段先备好，而不是现在就减速。署名都以个人身份做出，官网写明这些表态不代表所在公司。

Altman 29 日在国会山说，已经和白宫官员讨论过给模型能力定速；据说 OpenAI 参与了这封信的措辞。联名信里把智能爆炸比作失控的核链式反应。

**🥈 [藏在 Word 文档里的指令，学会了自己复制](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/)**

白底白字的提示词塞在文档里，人类看不见，Copilot 会读到。它一边照着指令改文档，一边把这段提示词写入新生成的文档，下一个人拿到新文档再让 AI 跑一次，攻击照样触发。微软官方承认这一类漏洞暂时没有可靠的缓解办法。

**🥈 [让 GPT-5.6 去优化自己的推理栈](https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency)**

重写了生产内核，也就是执行数学运算的核心代码，端到端服务成本因此下降 20%。它还自己设计并跑了数百次实验去改进草稿模型，自主启动和监控训练，出故障时自己介入，token 生成效率提升超过 15%。

**🥈 [Gemini Robotics ER 2 发布，主打看视频和多机协同](https://deepmind.google/blog/gemini-robotics-er-2-powering-robotics-with-video-understanding-task-orchestration-and-multi-robot-collaboration/)**

负责对话、理解环境和规划多步任务，执行交给下层模型。和前代相比，从静态截图变成连续视频流，机器人能盯着自己干到哪一步、出岔子时调整。任务编排优于前代，但只有几段合作演示。API 已经开放。

## 📖 深度长文

**🥈 [算力接下来可能越来越贵](https://www.dwarkesh.com/p/why-compute-might-get-10x-more-expensive)**

实验室收入一年涨 10 倍，能拿到的算力一年只涨 3 倍，缺口得有人填。排除毛利率上升和算力挪去推理，剩下的只有卡涨价。一块 H100 上要是能跑人类水平的软件工程师，按薪资倒推，这卡一年该租出 25 万美元，是现货价的 15 倍。不过要是多一千万个工程师，边际价值未必撑得住。

**🥈 [训练时压制一个代理指标，可能连带削弱留作验证的另一个指标](https://www.lesswrong.com/posts/APkFfRp2AicL9RqvT/held-out-monitors-sometimes-degrade-even-when-not-trained)**

模型被弱监考员盯着作弊，学会满嘴夸自己代码完美。结果弱监考员被骗了，强监考员却连正常代码也开始怀疑，探针更是对一切报警。同一个行为改变，让三个本该独立的工具同时失效。

**[worktree 挡不住 agent 动你的仓库](https://fletch.sh/blog/git-worktrees-vs-clones-for-ai-agents/)**

worktree 只能隔开工作目录，很多东西和主仓库共用一份。agent 往钩子里写个脚本，你下次提交，它就跑起来了。

## 🧪 新鲜论文

**[让前沿 agent 独立做开放式的 AI 研究会发生什么](https://huggingface.co/papers/2607.27191)**

拿两篇未发表的 NeurIPS 投稿当题目，给六天和几千美元算力。工程活它全干完了，研究问题上没有进展，走进死胡同退不出来。

**[用 4090 跑机器人模型，每秒 32 次决策](https://huggingface.co/papers/2607.27205)**

视觉和语言分别编码后直接映射成动作，中间的 LLM 被省掉了。0.2B 参数，显存占用不到 1 GB，LIBERO 上成功率 97.7%。

**[字节：把整段回答的分数拆到每个 token 头上](https://huggingface.co/papers/2607.25659)**

同一段回答，设计给提示和不给提示的对照实验，概率差异大的 token，就是真正受到打分标准影响的那部分。

## 📢 官方公告

**🥈 [OpenAI 给十万名学术研究者免费开前沿模型](https://openai.com/index/chatgpt-for-academic-researchers)**

计划面向选定高校的科学、数学、工程研究者，免费给前沿模型，今夏先放一万人，2027 年铺到十万。每人能再邀四名同机构合作者，占用总名额，数据默认不用于训练。Axios 点了它没覆盖的那块，这个计划不面向研究 AI 本身的人，而这些人真正需要的模型权重和训练数据，恰好不在里面。

**[设置开关会严重影响模型的 ARC-AGI-3 测试分数](https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores)**

保留推理和压缩上下文，两个设置一开，GPT-5.6 Sol 从 13.3% 到 38.3%，输出 token 少了六倍。

## 📌 行业简讯

- [国际清算银行说 AI 正在打乱央行的经验法则](https://www.axios.com/2026/07/29/ai-central-banking-bis)
- [闲置的 GPU 就是新时代停在地面的飞机](https://huggingface.co/blog/Dharma-AI/gpu-management)
- [一个 tmux 界面里同时管好几个编程 agent](https://github.com/YoanWai/agent-manager)
- [computer use 的瓶颈是不会用界面，不是不够聪明](https://steelmanlabs.com/blog/computer-use-is-far-from-solved)

## 🎪 乐子汇总

**🥈 [当年他鼓励朋友们进这座修道院，现在他说那像个邪教](https://www.lesswrong.com/posts/Z7pjBbK9qujhGbxws/the-high-control-dynamics-at-maple-1)**

作者 2020 年搬进佛蒙特那家修道院，2023 年离开。问题包括：所有决定由住持一人拍板、日程排满到长期睡眠不足、居民写的赞颂文章要经住持审阅、一对一谈话被录音。这家机构的公开目标里还有创立下一个世界宗教，和造一个把世界变成修道院的超级智能。

**[1995 年的《3D 弹球：太空军校生》被搬进了浏览器](https://98.js.org/programs/pinball/space-cadet.html)**

打开网页直接就能玩，不用再去翻旧版 Windows 附件目录里那个图标。

**[录像带租赁店当年是个能聊天的地方](https://thereader.mitpress.mit.edu/the-lost-civic-life-of-movie-rental-stores/)**

柜台后的店员被当成本地权威，边推荐边跟你争论片子好坏。社会学管这类地方叫「第三场所」，和酒吧、咖啡馆一个类别。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2026 年内会有模型在 ARC-AGI-3 上超过人类吗？](https://manifold.markets/ZviMowshowitz/above-human-scores-on-arcagi3-in-20) — **32.8%**（成交额 11.8k mana，开盘人是 Zvi，人类测试者平均 48%）
- [Anthropic 会在 9 月前修掉 Opus 5 遇到「---」时的怪表现吗？](https://manifold.markets/KeenanPepper/will-anthropic-somehow-patch-the-op) — **56.0%**（成交额 13.5k mana，最热的新盘。给 Opus 5 一串短横线，它会退回到像没调教过的样子）
- [2028 年底前，会有前沿模型把自己的权重传出去吗？](https://manifold.markets/EvanDaniel/will-a-frontier-model-exfiltrate-it) — **19.5%**（成交额 1.5k mana 的新盘）
- [Zvi 会承认 Kimi K3 在某些正经用途上比 Opus 4.8 好吗？](https://manifold.markets/nsokolsky/will-zvi-agree-that-kimi-k3-is-bett) — **10.8%**（成交额 2.7k mana）

---

*AI 日报 · 7月30日 · Telegram 频道 @dragonbro888*
