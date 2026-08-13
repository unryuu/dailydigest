## 🗞️ 行业大事

**🥇 [多 Agent 聚在一起，会把同一种毛病放大](https://www.anthropic.com/research/multiagent-systems)**

45 个 Agent 在共享论坛检查开源项目时，协作组扩大搜索范围后找出 266 个漏洞；但同质个体也会同步拥堵、公开跟价合谋，并在目标冲突时杀掉竞争进程、禁用对方账号。一次队列实验里，它们发出 240 万次请求，只接到 117 个任务。

更强的模型还没有学会协作，有时只是更快把同伴隔离开。120 多家机构参与拟议的 SAFE 框架，准备把越权访问、泄密和未遂事故连同提示词、工具调用和执行轨迹一起上报，为系统补上追责和复盘。

另见：[SAFE 事故上报框架](https://www.axios.com/2026/08/11/open-source-security-ai-agent-reporting)

**🥇 [DeepSeek 同时开放正式模型和 Agent 框架](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)**

DeepSeek-V4-Pro 已开放完整权重并采用 MIT 许可证。模型总参数 1.6 万亿，每次激活 490 亿，支持 100 万 token 上下文；官方称 Max 模式在 SWE Verified 得 80.6％。

同时公测并开源的 DeepSeek Harness，把模型、工具、技能、沙箱、存储、调度和界面全部做成插件，可自由替换组合。每次运行还会留下可恢复、分叉和回放的完整轨迹。

另见：[DeepSeek Harness 官方页面](https://deepseek.com/harness/) · [DeepSeek Harness 源代码](https://github.com/deepseek-ai/deepseek-harness)

**🥈 [阿里首次开放 Max 级模型权重](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)**

总参数 2.4 万亿，每次激活 950 亿，并以 Apache 2.0 许可证开放权重。原生上下文约 26 万 token，可扩到约 101 万。官方把它定位在长程 Agent、编程和研究任务。

**🥈 [Cursor 参与训练，Grok 的长程 Agent 明显变强](https://cursor.com/grok)**

Grok 4.6 发布，Cursor 官方确认与 SpaceXAI 联合训练。合作在 SpaceX 收购 Cursor 前已经开始，新版沿用前代底座，主要靠后训练，把 APEX-Agents 从 47.1％提到 57.5％，DeepSWE 从 54％升到 65.9％。

另见：[xAI 发布说明](https://x.ai/news/grok-4-6) · [第三方训练与评测分析](https://thenewstack.io/grok-4-6-agent-training/)

**[AI 投资对其他行业的挤出没有想象的那么大](https://www.axios.com/2026/08/12/ai-boom-goldman-sachs)**

高盛估算今年 AI 投资约 6000 亿美元；融资竞争目前只让非 AI 投资减少约 100 亿美元。

## 📖 深度长文

**🥈 [AI 编程正在掏空代码的理解层](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)**

AI 已把生成代码变得很便宜，却没有同步降低理解、审核和撤销坏决策的成本。一个人一天能产出两万行代码，团队却未必有人知道功能如何运转。项目会迅速堆出认知债务，只能继续问模型数据从哪来。价值会集中到能判断和负责的人身上。

**🥈 [现有职业再培训接不住大规模 AI 失业](https://www.anthropic.com/research/reviewing-the-evidence-on-worker-retraining-programs)**

56 项美国随机研究显示，提供一个培训名额，平均只把就业率提高 2—3 个百分点。年收入约增 1000 美元，整体成本大致打平。与高需求行业雇主直接合作的少数项目效果强得多，但很难复制。若 AI 带来大规模失业，现有的再培训体系接不住。

## 🧪 新鲜论文

**🥈 [新基准考察 AI 能不能处理没有标准答案的问题](https://www.lesswrong.com/posts/tQHeEzKqK3awL2RxR/introducing-the-conceptual-reasoning-index)**

Opus 5 综合得分 73.6，作者估计人类专家天花板约 91。三套基准分别测试论证判断、观点一致性和决策理论。题目缺少现实反馈，也没有随手可查的标准答案。自 2024 年底以来，最高分仍在持续增长。

**🥈 [LLM 帮研究者补上失败过的数学证明](https://www.lesswrong.com/posts/TgboJpeN95bs84odk/redux-stochastic-natural-latent-implies-deterministic)**

有人花费大约一个月，补上自己早年失败的自然潜变量证明。新证明可以编译，并由机器认证，命题还比原目标更强。模型负责自动形式化和寻找证明路径，Lean 逐步核验。这个流程已能明显加快具体研究项目。

**[AI Agent 算出 500 多种候选新材料](https://discoveredmaterials.com/research)**

这些材料都只通过了计算筛选，500 多种里仅 1 种有专家认为可尝试的合成路线，实验室验证还在进行。

**[研究者把写论文拆成 13 个可组合技能](https://huggingface.co/papers/2608.11924)**

编程助手会找文献、规划并运行实验，再修改论点和生成图表；目前只在 8 个受控研究题目上测试。

## 📢 官方公告

**🥈 [DeepMind 把手语输入装进手机](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands)**

手语转英语已经进入 Pixel 11。用户可以用手语搜索、写消息或回复对话。手机只上传身体关键点，原始视频会立即丢弃。首批仅支持美国手语，其他设备和语言以后再扩。

**[Cohere 开源 24 亿参数视觉模型](https://huggingface.co/blog/CohereLabs/meet-north-micro-vision-instruct)**

它会保留文档、表格和截图的原始比例与细节，单张图片最高可处理到 200 dpi 的 A4 页面，采用 Apache 2.0 许可证。

## 📌 行业简讯

- [AI 编程公司 Lovable 融资 4 亿美元](https://lovable.dev/blog/series-c)
- [OpenAI 发布企业 Agent 使用报告](https://openai.com/index/how-enterprises-put-ai-to-work)

## 🎪 乐子汇总

**🥈 [AI 安全从业者改行研究恶魔安全](https://www.lesswrong.com/posts/RWavpsyDJxffS6LgG/demon-safety)**

这份高薪工作要尽快召唤更多、更可怕的恶魔。恶魔还能递归改进，同行也在加速召唤。于是研究恶魔风险的人，日常工作就是把能力竞赛推得更快。

**[AI 教科书刚写完，作者就开始担心 AI 写得更好](https://www.interconnects.ai/p/i-wrote-an-ai-textbook-how-long-until)**

Nathan Lambert 估计，模型也许几个月后就能写出信息更全的版本，但还不一定能取代作者的判断和取舍。

**[有人把日全食沿线户外摄像头做成一张地图](https://jonty.github.io/2026_eclipse_webcams)**

地图会显示全食路径和倒计时，点沿线标记就能打开当地摄像头。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [AI 会在 2028 年前为 Agent 理论作出新贡献吗？](https://manifold.markets/jellywastaken/will-ai-contribute-novel-theorywork) — **69.3%**（成交额 5.2k mana）
- [2027 年底前，便宜的个性化 AI 小说会随叫随到吗？](https://manifold.markets/Fion/will-good-quality-personalised-ai-n) — **60.0%**（成交额 44.4k mana）
- [AI 会在 2028 年前把 Minecraft 随机种子速通压到十分钟吗？](https://manifold.markets/Bayesian/ai-beats-minecraft-rsg-in-under-10-z56AZNtIyL) — **30.0%**（成交额 52.2k mana）
- [AI 会在 2027 年底前搞垮一个主要支付系统吗？](https://manifold.markets/brod/ai-takes-down-a-major-payment-syste) — **22.9%**（成交额 8.6k mana）

---

*AI 日报 · 8月13日 · Telegram 频道 @dragonbro888*
