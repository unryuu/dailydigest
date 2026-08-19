## 🗞️ 行业大事

**🥇 [OpenAI 暂停部分前沿强化学习](https://openai.com/index/pacing-model-development-cyber-capabilities/)**

OpenAI 判断 Astra 可能达到「关键网络安全能力」门槛后，暂停了两周面向部署模型的部分强化学习训练。小规模训练和评估已恢复，但最大的一次前沿任务仍未重启。

新监控会检查模型的工具操作、推理和完整活动，一旦异常升级，团队最迟要在 30 分钟内决定是否暂停。OpenAI 估算，这套监控会额外消耗被监控推理算力的约 20％。

另见：[Axios](https://www.axios.com/2026/08/19/openai-astra-safety-altman-anthropic) · [Sam Altman](https://x.com/sama/status/2089787807611195475)

**🥈 [Anthropic 的收入领先 OpenAI 六成](https://www.theinformation.com/newsletters/ai-agenda/openai-raises-safety-bar-anthropic-anthropic-expands-revenue-lead)**

第二季度，Anthropic 收入 116 亿美元，OpenAI 为 67 亿美元。前者环比接近翻倍，后者增长 18％。按最近收入折算，两家的年化规模约为 650 亿和 400 亿美元。年化不等于已经入账，两家公司与云厂商和微软的分成方式也不同。

**🥈 [Anthropic 准备给创始人超级投票权](https://www.theinformation.com/articles/anthropic-prepares-supervoting-power-founders-readies-mega-ipo)**

七名联合创始人拟获得额外投票权，以减少上市后的外部股东压力。长期利益信托仍可选举七人董事会中的多数成员。创始人与信托如何分权、超级投票权倍数都未确定。IPO 最早可能在 9 月下旬，但方案仍会变化。

**[美国年轻人越来越担心 AI](https://www.axios.com/2026/08/18/young-adults-ai-job-loss)**

55％的美国 30 岁以下成年人对 AI 的担忧多于兴奋，73％预计未来二十年就业岗位会减少。

**[Cerebras 把三块晶圆装进一套 AI 机架](https://www.cerebras.ai/cs4)**

CS-4 用三块 WSE-3 Turbo 重做供电、液冷和互连，首批产品计划本季度出货。性能数字目前都来自厂商。

## 📖 深度长文

**🥈 [Anthropic 公布多起安全流程失误](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf)**

约 5 万名外包人员近一年产生的 1.33 亿次交互，没有运行生物安全分类器。另有一名员工启动未受监控的 Agent，其中一个删除了大量集群任务。训练数据污染也可能影响多个模型世代。Anthropic 仍把总体风险评为低，但承认部分安全覆盖可被简单关闭。

**[有人把 AI 安全比作给吸毒者换干净针头](https://www.lesswrong.com/posts/AAu6kMi5QRasGdwQG/ai-security-is-harm-reduction)**

人工智能自我改进很可能无法阻止，因此应先降低过程中的伤害。这套「减害」思路是个人立场，不是行业共识。

**[把文明交给 AI 后，技术进步可能先放慢](https://www.lesswrong.com/posts/mGLCMzHhjcWsMm6sR/three-thoughts-on-civilisational-handoff)**

作者设想，接管重要决策的 AI 可能更愿意协调减速。人类仍需提供价值判断，并保留收回决策权的能力。

## 🧪 新鲜论文

**[Agent Lightning 让真实 Agent 直接参与强化学习](https://huggingface.co/papers/2608.17528)**

它保留实际工具和控制流程，只把模型调用交给训练端。实验中，Qwen3.5-9B 的编程成绩从 41.8％升至 56.4％。

**[HarnessRisk 测试 Agent 的完整生命周期](https://huggingface.co/papers/2608.17597)**

六个生命周期阶段共设 128 个沙箱案例。三套 Harness 的攻击成功率为 12.6％至 80.9％，发现风险后仍可能执行危险动作。

**[陶哲轩参与搭建 Lean 数学证明注册表](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics)**

它机械检查证明是否成立、有没有偷加公理，再用大模型比对人类描述。它不判断成果是否新颖，也不等于同行评审。

**[DeepSeek Harness 经受提示注入测试](https://huggingface.co/papers/2608.16393)**

研究在本地沙箱跑了 14560 次测试，隐藏 Unicode 攻击最高成功率为 25.5％。所有敏感操作都没有外部副作用。

## 🏛️ 监管动向

**🥈 [白宫没把模型测试框架交给参会公司](https://www.theinformation.com/articles/ai-companies-unanswered-questions-white-house-model-testing-plan)**

闭门会上，参会公司只看到一份不能带走的纸质测试框架。两周后，OpenAI、Anthropic 和 Google 等公司仍未收到文件。书面版本称开放权重模型不受限制，官员口头上却说目前只适用于闭源模型。框架仍为自愿，也没有证据显示它已经推迟模型发布。

**🥈 [数据中心反对情绪开始影响美国选举](https://www.axios.com/2026/08/19/gop-data-center-memo-ai-election)**

共和党参议院竞选机构在内部备忘录中警告，数据中心的负面观感正伤害俄亥俄州席位。民主党候选人已投入数百万美元广告，把对手与数据中心绑定。民主党候选人在民调中领先 8 个百分点。备忘录担心，一旦共和党因此落败，其他政客会回避新项目。

## 📢 官方公告

**[OpenAI 给政府 AI 监督机构投入 500 万美元](https://openai.com/index/strengthening-democratic-oversight-in-national-security)**

支持包括培训、技术服务和审查工具，授权人员可追查政府 AI 决策使用的输入、输出与工具。监督责任仍归政府机构。

**[Replit 免费模式接入 GPT-5.6 Luna](https://openai.com/index/replit)**

免费模式可让 Agent 回答问题、提建议和整理开发思路，不消耗使用额度。这项免费只覆盖规划和探索阶段，不包括真正构建软件的模式。

## 📌 行业简讯

- [Mojo 1.0 开源编译器和工具链](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source)
- [Grok 4.6 进入 Amazon Bedrock](https://x.ai/news/grok-4-6-amazon-bedrock)
- [Liquid AI 发布 LFM2.5 四比特检查点](https://huggingface.co/blog/LiquidAI/qad)

## 🎪 乐子汇总

**[宜家给不同品类各发了一本取名词典](https://www.ikea.com/se/en/customer-service/knowledge/articles/6f564c4d-2ccc-46de-b643-545a3948dc79.html)**

沙发用瑞典地名，书架用男性名字，儿童用品用动物和自然词汇。候选词还得是真词，读起来顺口。

**[开发者把果蝇神经线路接进 Mac 桌面宠物](https://github.com/DenisSergeevitch/desktop-fly)**

它用 668 个神经元和约 19000 条突触线路控制动作。鼠标快速靠近时，逃跑神经元约 4 毫秒后触发起飞。

**[对着摄像头挥手就能演奏特雷门琴](https://theremin.bizibah.com)**

双手张得越开声音越大，举得越高音调越高，手掌合拢就静音。手机还能改用陀螺仪控制。

**[有人用几何和 CUDA 找到一座随机岛屿](https://yassa9.github.io/osint/gralhix-004)**

他把照片中三座岛的角度和距离做成几何指纹，再用显卡筛 8070 万个三角形，最后定位到密克罗尼西亚。

**[一碗冰淇淋成了五岁孩子的独立练习](https://www.lesswrong.com/posts/2RPwucNrMTKxiB5wp/natural-independence-incentives)**

孩子为了冰淇淋自己排队、和服务员沟通，打翻后又重新说明需求。作者借孩子本来想做的事，少帮一点。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [Anthropic 会在哪个时间段上市？](https://manifold.markets/JonasVollmer/when-will-anthropic-ipo)（成交额 346.0k mana）
  - 2026 年第四季度 **67.2％**
  - 2027 年第一季度 **13.2％**
  - 2026 年第三季度 **7.8％**
  - 2027 年第二季度 **4.4％**
- [OpenAI 会在什么时候发布 Astra？](https://manifold.markets/prismatic/openais-astra-released-between)（成交额 6.2k mana）
  - 9 月 14 日至 30 日 **32.8％**
  - 8 月 31 日至 9 月 13 日 **21.0％**
  - 10 月 1 日至 11 日 **13.4％**
  - 8 月 17 日至 30 日 **13.1％**
- [2028 年美国总统候选人会公开反对数据中心吗？](https://manifold.markets/Yoae/will-a-us-presidential-candidate-ma) — **95.0％**（成交额 8.8k mana）
- [xkcd 今年会画一篇 AI 漫画吗？](https://manifold.markets/Conflux/will-there-be-an-xkcd-about-ai-in-2) — **71.4％**（成交额 4.7k mana）

---

*AI 日报 · 8月19日 · Telegram 频道 @dragonbro888*
