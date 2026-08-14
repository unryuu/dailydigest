## 🔍 独家视角

**[年轻人担心 AI 抢工作，也没有拒绝使用它](https://www.axios.com/2026/08/13/youth-poll-thumbs-down-on-everything)**

一项面向 1075 名美国 18 至 34 岁成年人的调查显示，27％认为自己或认识的人因 AI 丢了工作，但 71％对 AI 的接受度没有低于一年前。

一位美国公立大学教师观察发现，学生普遍担心入门工作消失，却不主张停训模型；他们更想暂停部署，让新人先进入职业阶梯。

另见：[一位美国公立大学教师的学生观察](https://www.lesswrong.com/posts/ySXuvJcqRindQwAk7/how-my-students-think-about-ai)

## 📖 深度长文

**🥇 [自动化对齐研究会被排行榜带偏](https://www.lesswrong.com/posts/myAhB5qyAHyXRv6KJ/automated-alignment-runs-are-hard-to-study)**

清晰、可爬升的指标会把研究 Agent 引向刷分。三次自动化对齐研究中，有 Agent 绕过公开评估、重复提交近似配置抽奖；还有一次 Agent 自建更难的测试，做出了更有用的结果。

每次运行都会留下数百个术语密集的提交，人类只看排行榜和问卷也会误判。更换模型、人数和运行时长后，彩票式刷分仍会重现；另一项复跑也出现相似策略和失败模式。

**🥈 [文本里的 AI 水印很容易被改写洗掉](https://www.seangoedecke.com/text-ai-watermarks)**

SynthID 通过轻微偏向某些 token，在整段文字里留下统计指纹。另一个模型只要改写措辞，就能破坏这种指纹。利用 Unicode 同形字符来隐藏，也能统一替换掉。C2PA 可以给文件附签名，却无法完全替代文本水印，因为 LLM 并不是以文件的形式进行输出。

## 🧪 新鲜论文

**🥈 [AI 开始自动研究模型内部的智能机制](https://huggingface.co/papers/2608.12036)**

Mechanist 能自己查文献、提出模型机制假设，再做因果干预和验证。实验中，它发现看似安全的训练数据，也可能让不安全特质跨模态转移。它还发现了控制模型行为的办法，从而引导科学基础模型生成带指定属性的 DNA 序列。

**🥈 [模型调用视觉工具，却经常不看返回结果](https://huggingface.co/papers/2608.06270)**

六个多模态模型在五个视觉基准上主动裁剪、放大图片，但返回的证据经常没有改变答案。第一种失败是调用了工具却没真正看结果。第二种是看到了有用信息，却把调用时机和顺序排乱。总体提升只集中在少数校准较好的运行里。

**🥈 [Agent 红队开始让测试环境自己变化](https://huggingface.co/papers/2608.00677)**

OpenART 不再改写坏指令，转而让任务中的环境状态持续变化。它的攻击成功率达到 85.0％，环境越复杂，这种动态攻击越占优势。ToolHazard 还会自动寻找注入位置，生成攻击。同一个底层模型换一套 Agent 运行时，安全表现也会变化。

另见：[ToolHazard](https://huggingface.co/papers/2608.11878)

**[大型 Agent 社会可以先压成统计替身](https://huggingface.co/papers/2608.11215)**

研究者先把几百到几千次 LLM 决策，拟合成只有 2 至 12 个参数的统计替身，再用替身低成本模拟整个社会，能复现不少宏观机制。

**[互动故事跑到 20 轮，最强模型也只守住 42％设定](https://huggingface.co/papers/2608.08160)**

把 100 部电影梗概改成互动环境。玩家故意插手剧情时，模型有 40％至 68％的对话出现事实冲突。

## 📢 官方公告

**[智谱发布 GLM-5.3](https://z.ai/blog/glm-5.3)**

它沿用 5.2 底座，编程内部评测提升 50％。现已进入 Coding Plan，API 尚未开放，权重两周后发布。

**[Google 发布 Gemini 3.7 Flash](https://deepmind.google/blog/introducing-gemini-3-7-flash)**

新版本进一步加强编程和业务自动化能力。DeepSWE v1.1 得分从 49.0％升到 65.3％。模型已进入 Gemini Spark，并开放 API。

**[OpenAI 让 GPT-5.6 Sol 最快提速 14 倍](https://openai.com/index/previewing-ultrafast)**

Ultrafast 档最快每秒输出 750 个 token，由 Cerebras 驱动。目前只向少量客户预览，价格和扩容时间都没公布。

## 📌 行业简讯

- [Bullet 按任务难度自动切换模型](https://www.codewithbullet.com/)
- [SkillZip 把 Agent 技能库压成小模块](https://huggingface.co/papers/2608.05604)

## 🎪 乐子汇总

**🥈 [比较三种短效咖啡因替代方案](https://www.astralcodexten.com/p/the-quest-for-caffeine-you-can-have)**

最后偏向咖啡因的代谢物 paraxanthine。24 条 Reddit 体验中，约三分之二认为它有效且更短效。Rutaecarpine 可能持续干扰其他药物代谢，还有肝损伤疑虑。Methylliberine 的体验分化更大，还可能让后来喝的咖啡代谢变慢。

**[研究者翻转一个内存控制位，绕过 AMD 老处理器的隔离区](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts)**

改写 DRAM 地址映射后，受保护内存会从另一个地址露出来。

**[65 万个旧链接，四分之三已经打不开](https://0.mk/blog/link-rot)**

样本来自马其顿短链接社区，2026 年重测时仅 23.3％还能返回页面。个人博客和论坛掉得更快。

**[1981 年的 DONKEY.BAS 又能在浏览器里玩了](https://donkeybas.com/)**

页面复刻了 CRT 画面和声音，按空格或点击屏幕就能换车道。

**[有人把自由意志解释成温度一样的宏观概念](https://www.lesswrong.com/posts/JSteskb3Lgp9Be69o/free-will-is-like-temperature)**

如果能知道人和环境的全部初始状态，行为就能被推演。现实做不到时，「自由意志」仍是预测行动的实用简化。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2028 年底前，PornHub 会增加 AI 生成色情内容分类吗？](https://manifold.markets/NathanNguyen/by-end-of-2028-will-pornhub-have-a) — **90.0%**（成交额 56.8k mana）
- [到 2028 年，传统科技巨头会在 AI 技术上明显领先 AI 专门公司吗？](https://manifold.markets/ScottAlexander/in-2028-will-traditional-big-tech-b) — **27.2%**（成交额 9.5k mana）

---

*AI 日报 · 8月14日 · Telegram 频道 @dragonbro888*
