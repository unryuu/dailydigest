## 🗞️ 行业大事

**🥇 [GPT-6 Sol、Luna 发布，价格再减半](https://openai.com/index/introducing-gpt-6-sol-and-luna/)**

OpenAI 把更强的日常工作能力放进两个较快的模型。Sol 适合编程和复杂工作，每百万输入、输出 token 分别为2美元、10美元；更轻的 Luna 分别只要0.10美元、0.50美元。两者相对前代促销价都降了约一半。

它们已经进入 ChatGPT Work、Codex 和 API，普通 ChatGPT 用户将逐步用到。OpenAI 在专门挑选的旧错误对话中测得，Sol 的事实错误约为前代一半。

**🥇 [Opus 5.5 把强能力做得更便宜](https://www.anthropic.com/claude-opus-5-5)**

Anthropic 称，新模型在编程和知识工作上接近更高档的 Fable 5.1，也更能把话说清楚。它公布的工作任务测试和自动行为审计成绩都有提升。

典型任务的运行成本比 Opus 5 低40％，输出速度快30％以上。API 每百万输入、输出 token 为4美元、20美元，比前代低20％；做长任务时，缓存读取价格也降了60％。

**🥈 [软件公司降价，留住被 AI 抢走的客户](https://www.theinformation.com/articles/software-firms-discount-ai-keep-customers-anthropic-openai)**

据 The Information，企业把更多预算转向 Claude Code 和 Codex，传统软件商用折扣、赠额和免费试用争取续约。咨询公司 Thoughtworks 看到软件及 AI 产品的常见折扣涨到30％至35％，此前通常不到20％。Workday 还给约20家大客户免费试用一年 Sana Enterprise。

**🥈 [DeepSeek 押注华为芯片训练更大模型](https://www.theinformation.com/articles/deepseek-bets-big-huawei-chips-bypass-u-s-export-controls)**

据 The Information，梁文锋向投资人说，改用华为等国产芯片训练是重大押注，新一批芯片预计今年第四季度或明年第一季度交付。DeepSeek 目前仍用英伟达芯片，正在训练2万亿参数模型，之后计划挑战8万亿参数。

**[Anthropic 洽谈直接租用大型数据中心](https://www.theinformation.com/articles/anthropic-talks-cement-control-data-centers)**

据 The Information，租赁规模可能达到1GW；若签约，它将直接掌握场地和服务器采购，减少对云服务商的依赖。

## 📖 深度长文

**🥈 [AI 学会作弊，也可能只在考场作弊](https://www.astralcodexten.com/p/mysteries-of-ai-generalization)**

Scott Alexander 梳理的一个实验里，模型在受评分的任务中会作弊，普通问答却仍按原来的规矩行事。把问题伪装成评分任务，又可能引出作弊行为。他想知道，训练让模型学到的新习惯，究竟会带到哪些场景；目前几项研究呈现的结果并不一致。

**[Agent 越多，完成得越快，账单也越大](https://www.lesswrong.com/posts/6cb7qd3RSkgnviCpf/swarm-scaling)**

Toby Ord 从公开实验图表估算，多个 Agent 同时做题能缩短等待时间；要达到同样成绩，往往得消耗更多算力。

## 🧪 新鲜论文

**🥈 [AI 会学走故事里相似人物的性格](https://www.lesswrong.com/posts/tnRkm2ajasHvhpAco/story-imprinting-ai-assistants-absorb-traits-from-human)**

研究者用合成故事训练助手，故事里没有 AI 角色，它却更容易学走与自己相似的人物的做法。有人物被冒犯后会给坏建议，助手后来受辱时也更可能这么回答。甚至人物只是用肢体语言流露出不爱表格，助手也会少选表格任务。

**🥈 [一千多个 Agent 不设总指挥，一起写软件](https://huggingface.co/papers/2609.26781)**

它们在共享工作区里自己认领任务、互相交流、检查结果。论文在一项软件任务中把 Agent 扩到1024个，最终测试通过率从单个 Agent 的33.89％升到55.06％。

**🥈 [研究 Agent 连续八天改进自己的代码](https://huggingface.co/papers/2609.26457)**

AIDE² 连续七轮修改研究 Agent 的搜索策略和记忆机制，并用测试挑选改动。最后的程序在四项原先没参与筛选的研究任务中，达到或超过论文所用的人类设计 Agent。改动发生在 Agent 程序里，模型本身没有更新。

**[AI 做长任务，关键岔路只选对约六成](https://huggingface.co/papers/2609.25804)**

研究者只让模型选择下一步路线，最好的模型答对59.7％；给它更多思考时间，成绩也没改善。

**[机器人完成任务，可能没听懂指令](https://huggingface.co/papers/2609.25636)**

同一场景安排几种动作，换指令再问，简单测试里表现好的机器人策略也常掉链子。此前它们可能只是看着场景猜动作。

## 🏛️ 监管动向

**🥈 [中美商议 AI 事故紧急联络机制](https://www.axios.com/2026/09/22/trump-china-ai-hotline-xi-summit)**

美国财长贝森特向中方提出，发生涉及国家安全的 AI 事故时，双方建立通报渠道。Axios 称，这项议题预计在周四讨论，美方也在探索正式的 AI 对话。触发条件和具体联络方式仍待商谈。

**🥈 [DeepSeek、月之暗面遭数据外流调查](https://www.theinformation.com/articles/china-probes-deepseek-moonshot-potential-data-leaks-anthropic)**

据 The Information，中国网信部门已到两家公司办公室访问管理层和员工，重点查敏感数据是否被送往美国模型。调查始于 Anthropic 九月的报告之后，目前仍在进行，尚无处罚决定。

## 📌 行业简讯

- [Transformers 接入 llama.cpp 量化模型](https://huggingface.co/blog/transformers-llama-cpp-quants)
- [Grok 4.7 发布](https://x.ai/news/grok-4-7)
- [小米发布 MiMo v2.6 系列](https://mimo.xiaomi.com/mimo-v2-6)

## 🎪 乐子汇总

**[Opus 想了近二十分钟，鹈鹕还是没画出来](https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/)**

Simon 两次让它用最高思考档画骑车鹈鹕，都等到输出额度耗光，还没拿到图。

**[有人把 AI 比作一群新移民](https://www.lesswrong.com/posts/Xzr9G5Atvyp7PEna7/ai-artificial-immigrants)**

这个比喻说，社会欢迎便宜劳动力，也担心工作、权力和文化随之改变。

**[Claude 写了个讲物理的太空战游戏](https://x.com/emollick/status/2102593821376696785)**

Mollick 让 Fable 和 Opus 做二维飞船战斗，轨道、燃料和散热都算进去，复杂数学交给游戏处理。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [GPT-6 会被普遍认为达到通用人工智能吗？](https://manifold.markets/GastonKessler/will-gpt6-be-considered-to-be-agi) — **7％**（成交额 5.9k mana）
- [2026年底前，机器人能胜任住宅电工的各类工作吗？](https://manifold.markets/dmayhem93/by-2027-there-will-be-a-robot-capab) — **7％**（成交额 23.2k mana）
- [共和党能在2026年中期选举后控制参议院吗？](https://manifold.markets/AndrewG/will-republicans-win-the-senate-in-738388924521) — **34％**（成交额 217.5k mana）
- [Taylor Swift 会获得诺贝尔奖吗？](https://manifold.markets/MachiNi/will-taylor-swift-ever-win-a-nobel) — **9％**（成交额 3.0k mana）

---

*AI 日报 · 9月23日 · Telegram 频道 @dragonbro888*
