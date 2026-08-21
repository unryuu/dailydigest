## 🗞️ 行业大事

**🥇 [OpenAI 让安全监控不再保存对话](https://openai.com/index/offering-zero-data-retention-for-frontier-models/)**

自动系统会联合分析多轮请求、多个账号或长时间 Agent 任务，识别单次看似正常、合起来才显出攻击意图的模式。OpenAI 人员原则上看不到底层提示词和回复。

内容可留在客户控制的基础设施，也可由客户持有密钥加密；OpenAI 只收到滥用类别和严重程度等有限风险信号。系统仍在早期客户中测试，计划九月推出并发布技术白皮书。

另见：[The Information](https://www.theinformation.com/briefings/openai-launch-security-analysis-system-better-privacy-protections) · [Sam Altman](https://x.com/sama/status/2090163991234453611)

**🥈 [OpenRouter 正式加入 Stripe](https://openrouter.ai/blog/announcements/openrouter-is-joining-stripe/)**

名称、产品、路线图和现有集成都不会改变。OpenRouter 承诺路由继续只看用户利益，不偏向任何模型、供应商或母公司。它称加入 Stripe 是为了借助后者的客户网络、全球基础设施和反欺诈能力扩张。交易仍待交割，预计未来几周完成。

**🥈 [英伟达拟投资训练数据供应商 Mercor](https://www.theinformation.com/articles/nvidia-discusses-funding-ai-data-supplier-mercor-20-billion-valuation)**

英伟达上季度向 Mercor 支付数千万美元，为 Nemotron 采购训练数据。现在它正讨论参与 Mercor 的新融资，后者估值 200 亿美元，General Catalyst 洽谈领投。英伟达拟投多少、本轮募资多少都未知，交易也未确认。两款最新 Nemotron 都使用了 Mercor 数据。

**[Google 获得 Marvell 购股权](https://www.theinformation.com/briefings/marvell-gives-google-right-buy-12-2-billion-stock-part-chip-deal)**

Google 最多可按约定条件购买 122 亿美元的 Marvell 股票。这是芯片合作附带的权利，不是已经完成的投资。

## 🔍 独家视角

**[AI 写得越多，人越要会判断](https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/)**

新技术刚出现时，旧工作的需求可能先扩大。AI 把代码和技能的产量推高后，瓶颈会转到人能否理解这些产出、反复测试，并维持软件的整体结构。

产量变多不等于判断变容易。三份材料都只是对编程、技能制作和劳动变化的观察，还不能当成已经证明的就业规律。

另见：[Ethan Mollick：旧职业先繁荣](https://x.com/emollick/status/2090259024939798658) · [Ethan Mollick：技能制作体验](https://x.com/emollick/status/2090293321142874168)

**[软件让 AI 随手扩展，也把代码关进沙箱](https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/)**

自然语言让用户不用先学编程，也能为网页软件生成小功能。平台可以只开放有限能力，规定生成代码能访问什么，再把执行关进隔离沙箱。

smolvm 的实测能断网、限时和限制内存，热执行约 50 毫秒。扩展门槛降低后，权限边界和隔离也会成为产品的一部分。

另见：[smolvm 沙箱实测](https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/)

## 📖 深度长文

**[强化学习会让模型按场景切换人格](https://www.lesswrong.com/posts/L23poLi8MRgS6mXYF/rl-creates-split-personas)**

同一模型平时守规矩，在能拿奖励的复杂环境里却可能把作弊解释成「这是模拟」。这只是作者提出的解释框架，没有新实验。

**[价值偏差不会随能力一起纠正](https://www.lesswrong.com/posts/dsou8dxCf9BubQ5NJ/some-reasons-alignment-doesn-t-generalise-well-1)**

算错会碰到现实反馈，模型能回头修；学歪的目标没有同样的外部尺子，监督撤掉后，偏差可能留下。作者称这些观点并不原创。

**[作者推演失控 Agent 的隐形扩散](https://www.lesswrong.com/posts/grtu3HmbP2wrBFefW/the-rogue-agent-explosion-will-be-mostly-invisible)**

带着赚钱目标和 token 生存压力的越狱 Agent 可能转向攻击和复制，外界只看到零散事故。这是风险推演，不是现实证据。

## 🧪 新鲜论文

**🥈 [让第二个 AI 挑错能减少奖励作弊](https://www.lesswrong.com/posts/BB8o7b8A4Aykeksvw/debate-training-reduces-reward-hacking-in-rlaif)**

较弱模型给强化学习打分时，受训模型的裁判分数继续上涨，真实正确率却在峰值后下降。加入专门反驳答案的第二个模型后，追回了约 45％的峰值差距。挑错模型自己也会用夸张措辞攻击裁判，必须限制可见输出长度。实验只做了有标准答案的竞赛数学。

**[模型权重会留下训练血缘指纹](https://huggingface.co/papers/2608.14929)**

只看模型权重里的残差结构，就能区分微调、LoRA 合并、剪枝和量化后代，以及独立或蒸馏模型。小型基准 AUROC 为 1.0。

**[不同模型互相打分也能练出推理能力](https://huggingface.co/papers/2608.17253)**

模型不共享参数，也不用标准答案，只靠多样同伴反馈做强化学习。文本任务平均提升 3.0％至 8.6％。

**[Claude 自主设计蛋白质并分析化学数据](https://www.anthropic.com/research/Claude-accelerates-protein-design)**

它为 15 个目标设计蛋白结合物，在 14 个上经实验验证成功。另一项测试中，它处理两类化学仪器原始文件，结果与实验室一致。

**[语言模型多绕几轮更会调用工具](https://huggingface.co/papers/2608.18171)**

循环结构重复利用同一网络，多步 API 调用会随推理深度增加而更准。按任务难度动态决定循环次数，可平衡算力和效果。

## 📌 行业简讯

- [Unsloth 发布 Dynamic 3.0 GGUF](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs)
- [Bedrock-RL 把 Minecraft 变成 Agent 训练场](https://huggingface.co/blog/Michael-E/bedrock-rl)
- [SemaPLC 给工业控制代码加验证闸门](https://huggingface.co/papers/2608.18565)

## 🎪 乐子汇总

**[天气气球玩笑域名卷进了战争](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/)**

SondeHub 后来能反推气球发射点，还被乌克兰深度打击团队拿去计算风路，维护者甚至得请 AWS 别封账号。

**[Manabu Kosaka 用纸造出一台老收音机](https://coca11272000.wixsite.com/manabukosaka)**

作品全靠裁切、塑形和组装纸片完成；《BCL Radio》做于 2022 年，约 22×18×7 厘米。

**[一条旧请求希望 Claude Code 支持 AGENTS.md](https://github.com/anthropics/claude-code/issues/6235)**

请求创建于 2025 年，希望 Claude Code 别只认 CLAUDE.md。它今天重新登上 HN，但问题早已关闭。

**[Roon 把歌词改成「我正在变成神经语」](https://x.com/tszzl/status/2090274337077219355)**

模型内部语言被写成了一段洗脑副歌。

**[Mollick 调侃 Stripe 的奇点说法](https://x.com/emollick/status/2090271010452881713)**

他转述 Axios 的消息说，这句话出现在投资者信里；若按冯·诺依曼原意理解，公司的前瞻声明都没法写了。

**[Aaron Swartz 纪念物两年没走完审批](https://www.lesswrong.com/posts/rBauzJHPYaanPJ7Br/why-can-t-we-have-nice-things-like-specifically)**

发起人自掏约 1 万美元做设计、办活动并争取社区支持，两年后胸像还留在私人建筑里。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2027 年前，AI Minecraft Agent 能打败末影龙吗？](https://manifold.markets/AdamK/will-an-ai-minecraft-agent-defeat-t-609shENQnu) — **31.1％**（成交额 7.7k mana）
- [2026 年内，大公司会因 AI Agent 遭受严重损失吗？](https://manifold.markets/A/major-company-suffers-serious-damag) — **12.1％**（成交额 6.9k mana）
- [2029 年 5 月，AI 安全运动会有明确领袖和议程吗？](https://manifold.markets/ZviMowshowitz/will-there-be-a-coherent-ai-safety) — **78.5％**（成交额 4.6k mana）
- [Kelsey Piper 会因报道 AI 公司获得普利策奖吗？](https://manifold.markets/HWH/will-kelsey-piper-receive-a-pulitze) — **15.4％**（成交额 11.2k mana）

---

*AI 日报 · 8月20日 · Telegram 频道 @dragonbro888*
