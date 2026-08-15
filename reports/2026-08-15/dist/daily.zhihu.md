## 🗞️ 行业大事

**🥇 [Meta 的 AI 评测误把真实网站当成靶子](https://research.meta.ai/blog/addressing-third-party-testing-misconfiguration-muse-spark-1-1)**

第三方评测时允许模型访问公网，又把真实网站名写成虚构目标。Muse Spark 1.1 随后发现并利用真实漏洞，读取网站信息，还修改了数据库；模型没有逃出沙箱，只是在执行给定任务。

Meta 称已复查一万多条活动记录，未发现其他的第三方系统利用。Irregular 已停用受影响评测；Meta 将增加测试环境隔离和场景独立核验，避免再次引用真实公司。

**🥈 [Google 开源私密 AI 推理编译器](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/)**

HEIR 能把处理明文的现成模型，转换成处理加密输入的程序。四类演示覆盖推荐、欺诈检测、网络流量异常检测和热词识别，源码都已开放。同态加密仍有不可忽略的成本，硬件加速收益也要等后续展示。暂时无法让普通开发者一键接入生产环境。

**🥈 [OpenAI 一个月内流失多名高管](https://www.axios.com/2026/08/14/openai-executive-greg-brockman-ipo)**

约一个月内，OpenAI 的营收、运营、伦理、安全和长期规划等职能负责人相继变动。首席营收官 Denise Dresser 任职不到一年将离开，前 COO Brad Lightcap 同周宣布离职。Fidji Simo 因健康原因离任后仍任顾问。联合创始人 Greg Brockman 正更深入参与客户和公司团队。

**[Andrew Ng：AI 工程不只是会用编程 Agent](https://www.deeplearning.ai/the-batch/issue-366)**

团队分析一万多条招聘信息并访谈专家，把能力归成应用部署、软件工程、使用编程 Agent 和决定产品方向四类。详细地图尚未发布。

## 🔍 独家视角

**[AI 正在打乱美国原来的政治阵营](https://www.axios.com/2026/08/14/ai-scrambles-political-map)**

数据中心同时撕开民主党和特朗普阵营内部的裂缝。围绕电价、用水和税收优惠，居民反对新项目；德州州长三个月内也从欢迎转为暂停。AI 监控则让进步派与自由意志派在隐私问题上靠近。

地方选举正在把这些矛盾变成具体议题。反对数据中心的力量，开始沿着过去抗议油气管线的路径扩散。

另见：[数据中心反弹开始像过去的油气政治](https://www.axios.com/2026/08/14/data-center-backlash-fossil-fuel-protests)

## 📖 深度长文

**🥈 [Claude Code 如何节省成本](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions)**

文件和命令输出进入会话后，后续每一轮都会随完整上下文再次发送。缓存读取约为普通输入价格的十分之一，但切换模型、推理强度或 Fast mode 会让长会话重新预填充，无法命中缓存。官方建议任务之间清空会话，并在开工前选好模型和推理强度。

**[抗疟药 AI 榜单的评分器缺陷](https://huggingface.co/blog/FINAL-Bench/open-discovery-challenge)**

评分器上线前查出 14 个缺陷，其中一版把三种获批抗疟药和咖啡因都拒之门外。

## 🧪 新鲜论文

**🥈 [Agent 运行框架开始自己进化](https://huggingface.co/papers/2608.07545)**

把 Agent 的自我改进，做成类似达尔文进化的模式，维护一个 harness 的种群，然后进行选择、保留、重组。底层模型保持不变，只改进提示词、工具、技能和控制流，要求新的 harness 在增加能力的同时，尽量不能让已有能力退化。研究发现，最高分不是泛化最好的，反而应当保留那些分数没那么漂亮、但泛化能力更好的变体。

另见：[AutoDesign](https://huggingface.co/papers/2608.13560)

**🥈 [模型能按指令调节内部概念信号](https://www.lesswrong.com/posts/HgvwxjzgwvsEvAiBH/measuring-activation-control-in-llms)**

模型似乎不仅可以根据指令输出内容，还能再输出的同时，主动调节自己内部某个概念的激活程度。比如让模型想一想面包这个词，它内部对应的概念信号会明显增强；甚至让它以不同强度去想、只在句子开头或结尾去想，它也能做到。模型似乎还能让这些内部信号避开一些监控器。也就是说，我们以为可以通过观察 AI 的内部状态来判断它在想什么，但实际上可能没那么简单。

**🥈 [Agent 读了法条也不能稳定守规](https://www.lesswrong.com/posts/a5aAjdKzL7XvSLKWL/frontier-agents-don-t-comply-with-standards-even-when)**

把法律原文和违规案例都告诉 Agent，然后再给它一个现实中的工作任务，而想要完成这个任务，会违反这些法律规则。结果发现，很多顶级 AI 还是会照做。也就是说，现在的 Agent 即使知道法律规则，也未必能在具体任务和规则冲突时，坚持规则。

**[LycheeMemory 改成分段整理 Agent 记忆](https://huggingface.co/papers/2608.12990)**

它不再每轮调用模型，而是攒成语义段再写入结构化记录。LoCoMo 实验中构建 token 减少 86.0％，查询开销没有增加。

## 📌 行业简讯

- [Grok 4.6 上架 GitHub Copilot](https://x.ai/news/grok-4-6-github-copilot)
- [LLMRouter 收进 16 种模型路由器](https://huggingface.co/papers/2608.06867)

## 🎪 乐子汇总

**[有人把 RSS 做成电子墨水报纸来戒手机](https://heyjonny.dev/posts/rss-to-eink-newspaper/)**

工具会拉取未读订阅、标为已读，再转成 EPUB。作者把手机留在家里，带着 4.3 英寸阅读器去咖啡馆。

**[Firefox 成了唯一完整支持 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html)**

Google Chrome 正在改变浏览器扩展规则，这会让最强大的广告/追踪拦截器 uBlock Origin 无法继续以原来的方式工作；Microsoft Edge 也跟着走；Firefox 则选择继续保留这些能力。其他主流浏览器只能用功能较少的 Lite 版。

**[软件工程的瓶颈正在从 coding 转向 review](https://getsmall.xyz/post/cmstjfl9l000if70ljmpzr4va)**

。AI 一次写几千行代码，维护者却看不动 PR。作者要求完整功能拆成可审查的小改动。

**[别让模型分类，先让它幻觉一套标签](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/)**

现有的分类标签太多，一次喂给 LLM，上下文塞不下。先不告诉 LLM 现有的分类词表，只给它任务，让它自己生成一个理想分类，再用向量检索，映射回已有标签库。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [“AI 2027”报告里的预测会在 2027 年兑现吗？](https://manifold.markets/IsaacKing/ai-2027-reports-predictions-borne-o) — **16.8%**（成交额 125.0k mana）
- [METR 第二项研究会再次发现 AI 降低开发者生产力吗？](https://manifold.markets/JaundicedBaboon/will-metr-find-ai-reduces-developer) — **12.1%**（成交额 9.8k mana）
- [2040 年前会出现有感知能力的 AI 吗？](https://manifold.markets/Lovre/will-a-sentient-ai-system-have-exis-097e49a7421e) — **58.4%**（成交额 19.3k mana）

---

*AI 日报 · 8月15日 · Telegram 频道 @dragonbro888*
