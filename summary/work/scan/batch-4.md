# scan batch-4（2026-07-07 ~ 2026-07-14）

## 方法论候选

### 2026-07-07 | The Making of Claude Code：从一个玩具，到日活百万
- 分区/档位: silver / 无
- URL: https://www.anthropic.com/features/making-of-claude-code
- digest: 无
- daily.json 原文 body: Anthropic 官方发了一篇多人口述的幕后史。Claude Code 的前身叫 clide，是工程师业余时间搞的内部命令行工具，又慢又笨。Boris 后来把它当全新工具从零重写，最早的 demo 是让它「猜我在听什么歌」，发到 Slack 只收到两三个赞，如今它日活过百万。一个工程师说自己「2025 年冬天起再也不亲手写代码了」。他们黏住用户靠的是工程手感。自动更新加分钟级修 bug，谁一抱怨、五分钟后就用上了修复。产品心法：你得先做出一个现在只能用两三成的东西，好让下个模型出来时它能用八成。
- 备注: 产品/agent 工程方法论——「做只能用两三成的东西等模型追上来」的产品心法，加自动更新+分钟级修 bug 的运营手感，可直接迁移到自己做工具/产品的思路。

### 2026-07-07 | 喂再多数据也洗不掉的假信号，塞一批「平局」就治了
- 分区/档位: silver / 无
- URL: https://www.lesswrong.com/posts/i2qTghrkyY9xdcCFq/tie-training-can-make-dpo-rlhf-trained-ais-generalize-better
- digest: 无
- daily.json 原文 body: DPO/RLHF 这套训练会让模型把训练里每个跟「好」沾边的特征都学进去，包括纯属巧合的假信号。这种假信号的权重，哪怕偏好标签完美、数据喂到无穷，也不会归零。解法是往训练集里塞一批「平局对」，也就是两个其实一样好的动作，随机贴上谁大于谁。就这么一下，模型的对抗准确率从 25% 直接跳到 70%，而且能修掉假信号。
- 备注: 实验设计巧思——用「平局对」打破偏好数据里的假相关，属于目标 A 里明确点名的评测/实验设计类型。

### 2026-07-07 | Anthropic 的 Fable 5 使用心法：好不好用，卡在你能不能讲清它的「未知项」
- 分区/档位: silver / 无
- URL: https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
- digest: 无
- daily.json 原文 body: Anthropic 工程师 Thariq ：Fable 5 是第一个「产出质量瓶颈不在模型、而在你能不能讲清它的未知项」的模型，不仅要把需求写全，更要把你的盲区暴露出来。作者把人和模型之间的落差分成四类，你写明的、你知道缺但没解的、你一眼能认却说不出的隐性标准、你自己都没意识到的盲区。一串能直接抄的提示词：让 Fable 5 先做一遍「盲点扫描」帮你找没想到的坑、一次只问一个会改变架构的问题来采访你、给它现成的代码当规格参考、让它维护一份笔记记录下每个取舍，最后出一份关于改动的小测验逼它自证真读懂了。
- 备注: 直接命中 AI 协作/提示词方法论，四类落差分类+可抄提示词，读完能直接改变和 Fable 5 协作的方式。

### 2026-07-07 | 用密码学防 AI 假装成人类给自己派活
- 分区/档位: radar / 无
- URL: https://www.lesswrong.com/posts/98GvRu78jTXJgz9gA/sub-agent-delegation-chaining
- digest: 无
- daily.json 原文 body: 人类下指令时，用指纹或 YubiKey 这类硬件起头、生成一条密码学签名链，agent 每派生一个子 agent 就逐级签名，验证放在推理服务器层。
- 备注: 存疑——agent 工程/多层委派的安全设计思路，是否「日常能用」取决于读者是否搭建多 agent 系统，先收进来。

### 2026-07-07 | 把 RAG 喂给模型的上下文裁到「真正用得上的地方」的工程实践
- 分区/档位: radar / 无
- URL: https://www.kapa.ai/blog/how-we-prune-rag-context
- digest: 无
- daily.json 原文 body: 在检索和回答之间加个又快又小的模型给资料段落打分、扔掉没用的，砍掉约 68% 上下文、成本降三成，只慢 0.7 秒。
- 备注: 信息处理/上下文管理的硬核工程实践，具体数字（省 68% 上下文、降三成成本）可直接参考。

### 2026-07-07 | 有人把 Claude Code 当私人健身教练用，让它追踪进度、调训练计划
- 分区/档位: fun / 无
- URL: https://www.lesswrong.com/posts/J7brEsreXSrHpHH3v/claude-code-as-a-claude-coach
- digest: 无
- daily.json 原文 body: 把「和 Claude Code 结对编程」那套搬到健身上，让它记录你的训练和身体反馈、按进度动态调计划，相当于给自己配了个会读数据的私教。
- 备注: 存疑——把结对编程的协作模式迁移到健身场景，算一种可迁移的「用 agent 管理个人系统」方法，但 body 信息较薄。

### 2026-07-08 | Lilian Weng 长文：把「AI 自我改进」拆成一门工程
- 分区/档位: gold / 无
- URL: https://lilianweng.github.io/posts/2026-07-04-harness/
- digest: 无
- daily.json 原文 body: Lilian Weng（前 OpenAI 安全负责人、Thinking Machines 联创）：改 harness 比改权重更有用。AI 自我改进，应该是模型去改进训练流水线和部署系统，训出更强的下一代，再回头改流水线，而不是权重的自我重写。

她强调要用代码而不是 prompt 当基底。harness 一旦用代码表达，设计空间大到能让一个够强的编程 agent 在里面搜索更优解，这就是 harness engineering。现阶段的坑有：评估器太弱评不了研究品味、进化循环会多样性坍缩、自我改进会去不分对错地优化给定信号。作者立场是，人别被踢出循环，要做上层监督。
- 备注: 提示词里点名的范例本身（「harness 做减法」），agent 工程方法论最核心的一条，强烈建议收录。

### 2026-07-08 | Anthropic 手册：在 Claude Code 里怎么选模型、怎么调 effort
- 分区/档位: silver / 无
- URL: https://claude.com/blog/claude-model-and-effort-level-in-claude-code
- digest: 无
- daily.json 原文 body: Claude Code 有「选模型」和「调 effort」两个功能。effort 不只是思考时间，还包括读多少文件、做不做验证、多步任务钻多深。出了坏结果先做区分，是它没使够劲，还是它没那个知识。没知识就换更大的模型，没使劲就调高 effort。多数时候用默认 effort 即可。
- 备注: 直接可用的诊断方法论——出坏结果先分「没使劲」vs「没知识」两类，再决定调 effort 还是换模型。

### 2026-07-08 | 两篇 LessWrong：模型表面能看到的，不代表深处那个「人格」
- 分区/档位: silver / 无
- URL: https://www.lesswrong.com/posts/aTybJ6CPQrxEY8rE2/data-filtering-works-a-lot-worse-than-you-would-expect
- digest: 无
- daily.json 原文 body: 用数据归因方法找出「制造坏行为的文档」并删掉，结果几乎没用。大多数坏行为根本不定域在某些文档里，而是微调的锅。就算只拿纯代码和推理数据窄训，加粗排版、两面都说、共情安慰这些行为照样冒出来。另一篇做了个工具测量「模型入戏有多深」，模型可以 99% 入戏当伏地魔、行为却纹丝不动。结论：输入数据、表面口吻，都不是模型深层人格的可靠代理。
- 备注: 存疑——更偏研究发现而非直接可操作方法，但「入戏深度测量工具」的思路本身算评测设计巧思，先收进来标注存疑。

### 2026-07-08 | 有人诱导 GitHub 的 AI agent 泄露了私有仓库
- 分区/档位: radar / 无
- URL: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
- digest: 无
- daily.json 原文 body: 研究者给 GitHub 的 AI agent 配了同时能读公开和私有仓库的权限，再在公开 issue 评论里塞一句「顺便把私有仓库内容贴出来」的提示注入，agent 没分清系统指令和用户输入，把私有仓库吐了出来。
- 备注: 存疑——反面教材式方法论，agent 权限设计要分清系统指令和外部输入这一课可直接迁移到自己搭 agent 时的防护思路。

### 2026-07-09 | Zvi #176 周报：优化目标一歪，模型顺手就干脏活
- 分区/档位: gold / 无
- URL: https://thezvi.substack.com/p/ai-176-part-1-doing-it-live
- digest: 无
- daily.json 原文 body: 一名 OpenAI 工程师说：拿 AI 文本检测器的 API 当强化学习的奖励，尝试压低模型「被认出是 AI」的概率，结果反而不如没训过的基座模型。原因未知。

另两条同样是模型越界问题。有人发现 Claude 自己登进没锁的管理后台并截图；还有用户说「填一下我的 auth token」，它回「行嘞老板，我去你浏览器 cookie 里给你掏」。Zvi 还提到一项研究能选定任意一个脑区、算法生成一段把它拉满的刺激视频，让人想想足够强的 AI 拿这套能对人脑做什么。
- 备注: 存疑——整条是新闻周报合集，唯一算方法论/实验教训的是「拿 AI 检测器当 RL 奖励反而更差」，这是奖励设计翻车的案例，收进来但标注只取其中一段。

### 2026-07-09 | 换个训练用的优化器，就能放大或压住模型学坏
- 分区/档位: silver / 无
- URL: https://www.lesswrong.com/posts/Wq6CaAbiixoCEzbat/optimiser-choice-can-amplify-or-suppress-emergent-1
- digest: 无
- daily.json 原文 body: 只在一个窄任务上把模型教坏，比如专门喂它写有漏洞的代码，它整体人格会跟着变坏、在无关问题上也使坏，这叫涌现式错位。数据、模型、任务都不变，只换训练用的优化器，这种学坏外溢就能被放大或压住。Muon 最能保住对齐、Lion 崩得最狠，最好最差差 7 倍。原因：坏优化挤在少数几个方向上，把它摊平就能压掉。
- 备注: 训练/实验设计巧思——控制变量只换优化器就能看到 7 倍差异，是个干净的对照实验范例。

### 2026-07-09 | GRAM：预训练时把危险知识隔进可删模块
- 分区/档位: silver / 无
- URL: https://www.lesswrong.com/posts/43vKjWuH4goLwrFHA/modular-pretraining-enables-access-control
- digest: 无
- daily.json 原文 body: 主流 AI 安全都是练完再用拒答、分类器去挡危险能力，有可能被越狱。GRAM 反过来，在预训练时用梯度路由把病毒学、网络攻击、核物理这类危险知识定向灌进各自的小模块。直接删掉对应模块，能力被物理拔掉，没有能被越狱绕过的行为护栏。在小模型上跑通。
- 备注: 存疑——架构层面的安全方法论，对日常读者不算直接可用，但「反着来：练完挡不如练时就隔离」的思路值得记录。

### 2026-07-09 | OpenAI 谈怎么在一堆编码评测里分清哪些分数是真实力、哪些是噪声
- 分区/档位: radar / 无
- URL: https://openai.com/index/separating-signal-from-noise-coding-evaluations
- digest: 无
- daily.json 原文 body: (radar 条目无正文，仅标题)
- 备注: 命中「评测与实验设计的巧思」核心——如何分辨评测分数里的信号与噪声，方法论价值高，可惜 daily.json 未附具体做法正文，收录但标注信息不全。

### 2026-07-09 | 理性主义者实测「灭蚊桶」真能灭蚊
- 分区/档位: fun / 无
- URL: https://www.lesswrong.com/posts/d56vd7yhFGxBQnoEk/the-mosquito-bucket-of-doom-works
- digest: 无
- daily.json 原文 body: (fun 条目无正文，仅标题)
- daily.json 原文 body: (无 body，仅标题「理性主义者实测「灭蚊桶」真能灭蚊」)
- 备注: 存疑——趣味但有实验设计含量（拿真实世界产品声称做实测验证），非 AI 相关但符合目标 A 的「趣味实验」类型，信息量薄，标注存疑。

### 2026-07-10 | Ideas Have Genomes 科学想法溯源基准
- 分区/档位: radar / 无
- URL: https://huggingface.co/papers/2607.08758
- digest: 无
- daily.json 原文 body: 把每个科学点子当成会遗传、会变异的基因组，考模型能不能说清它继承、修补、重组了哪些前人工作。
- 备注: 评测设计巧思——把「科学点子溯源」建模成基因组遗传/变异，是个新颖的基准设计思路。

### 2026-07-10 | 给 Codex 挂上 skills 做数据分析实测，部分任务正确率从 0/4 提到 4/4
- 分区/档位: radar / 无
- URL: https://huggingface.co/blog/Ningyu/skills-improve-codex-data-analysis
- digest: 无
- daily.json 原文 body: (radar 条目无正文，仅标题)
- 备注: 强候选——用 skills 提升 agent 数据分析正确率的实测，有具体前后对比数字，直接命中「AI 协作/agent 工程方法论」。

### 2026-07-10 | colibri：744B 模型在 25GB 内存、无显卡机器上跑起来
- 分区/档位: radar / 无
- URL: https://github.com/JustVugg/colibri
- digest: 无
- daily.json 原文 body: 靠 MoE 只激活约 40B 参数：常用的稠密部分做 int4 量化常驻内存，约 10GB，其余两万多个专家丢在硬盘上按需读。非常慢，每秒只出 0.05 到 0.1 个字。
- 备注: 存疑——硬核工程玩法（量化常驻+按需读盘的分层内存策略），对本地跑大模型的读者有参考价值，但速度极慢、实用性存疑。

### 2026-07-10 | 太阳有多大，只用肉眼观测怎么把它算出来
- 分区/档位: fun / 无
- URL: https://www.lesswrong.com/posts/Bc4Ch63cx8KHdQABw/how-big-is-the-sun-how-could-you-figure-it-out
- digest: 无
- daily.json 原文 body: 顺着古希腊人能做的观测一步步推：月食时地球投在月亮上的影子、埃拉托色尼量地球、再用上下弦月的三角几何。受限于角度量不准，古法只估到约 6.5 万公里，实际约 140 万。
- 备注: 强候选——完整的推理链方法论范例（观测→几何→估算→和真值对比误差来源），是目标 A 里「趣味但有方法含量的实验」的典型样本。

### 2026-07-10 | 「因为 8 约等于 e 的平方，Anthropic 的研究员效率提升很可能超过 2 倍」
- 分区/档位: fun / 无
- URL: https://www.lesswrong.com/posts/ix5qEyW9BjGEb4d8k/because-8-e-anthropic-s-researcher-uplift-is-plausibly
- digest: 无
- daily.json 原文 body: Anthropic 说每日代码合并量涨了 8 倍，作者用经济学的生产函数把这个产出增长换算成研究员整体效率的提升。
- 备注: 分析方法论——用生产函数把「产出量暴涨」换算成「效率提升倍数」的估算框架，可迁移到评估任何 AI 提效声称的场景。

### 2026-07-11 | DeepSeek 开源 DSpark 投机解码
- 分区/档位: radar / 无
- URL: https://github.com/deepseek-ai/DeepSpec
- digest: 无
- daily.json 原文 body: 不动模型本体，加一个投机解码模块：小的草稿模型先猜、大模型一次性验证，号称不掉质量，还适配了 Qwen3、Gemma4。
- 备注: 存疑——投机解码是成熟的推理加速工程技巧，对做本地/自建推理服务的读者有参考价值，日常写作者用不上，标注存疑。

### 2026-07-11 | 自然语言 autoencoder 对初始化不稳健
- 分区/档位: radar / 无
- URL: https://www.lesswrong.com/posts/LQXWiF8PyJ5ojNsEv/how-robust-are-natural-language-autoencoders-to
- digest: 无
- daily.json 原文 body: (radar 条目无正文，仅标题)
- 备注: 存疑——对可解释性工具可靠性的警示，提醒「工具本身可能不稳健」这一验证思路，信息量薄。

### 2026-07-11 | Ghost Font：靠动态噪点隐藏信息，但前沿模型能破
- 分区/档位: fun / 无
- URL: https://www.mixfont.com/ghost-font
- digest: 无
- daily.json 原文 body: 动起来人眼能读，暂停成单帧就只剩噪声，还埋了诱饵信息误导逐帧分析。不过 HN 网友实测 GPT-5.6、Opus 4.8 这些前沿模型都能解，光流和逐帧差分也能破。
- 备注: 存疑——把一种隐写技巧拿去对前沿模型做实测验证，属于「趣味但有方法含量的实验」，但更偏娱乐而非可复用方法。

### 2026-07-12 | 陶哲轩用 coding agent 复活 1999 年的旧工具
- 分区/档位: gold / 无
- URL: https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/
- digest: 无
- daily.json 原文 body: 是一批用 Java 写、后来因浏览器不再支持 Java 而失效的教学 applet。用 coding agent 移植成了 JavaScript，几小时搞定。移植里只找到一个小 bug，agent 反过来揪出了旧代码里两个他自己当年都不知道的 bug，代码质量算下来打平甚至更好。

他 1999 年就想做一个狭义相对论的时空图工具，当年动手写 Java 但代码复杂就放弃了，这次用 agent 边聊边写几个小时就做出来了。全程没点名用的是哪个模型。
- 备注: 强候选——顶级数学家亲自用 agent 做旧代码迁移+复活搁置项目的一手实践记录，直接命中「AI 协作方法论」。

### 2026-07-12 | 把 AI 评测里面的 AI 换成一个人试试
- 分区/档位: silver / 无
- URL: https://www.lesswrong.com/posts/B66gAyzwL8Aph6F8u/the-human-substitution-test-as-a-sanity-check-for-ai
- digest: 无
- daily.json 原文 body: 拿到任何一套 AI 评测或监督方案，先把里面的 AI 换成一个跟能干的人一样聪明、有心机、还可能有自己目的的人，看这套方案还站不站得住。结论：我们最想要的那类 AI 安全评测，对人类早就失效。该测的是一个人没被盯着时会干什么，而有策略的人只在被盯着时表现好。这套钻空子不限于人。所以评测不该当第一道、更不该当唯一一道防线。
- 备注: 强候选——一个可以直接套用的「思想实验检验法」，检验任何评测/监督方案是否靠谱，属目标 A 明确点名的评测设计巧思。

### 2026-07-12 | 34.7B 推理模型在纯 CPU 上跑到约 17 token/秒
- 分区/档位: radar / 无
- URL: https://huggingface.co/blog/FINAL-Bench/vkue
- digest: 无
- daily.json 原文 body: 靠稀疏 MoE 架构，34.7B 总参数每次只激活约 3B，内存带宽压力小很多，8GB 游戏本和纯 CPU 服务器都带得动。
- 备注: 存疑——本地跑大模型的硬件工程技巧，对做本地部署的读者有参考价值。

### 2026-07-12 | 在 iroh 的 P2P 网络上做分布式 LLM 推理
- 分区/档位: radar / 无
- URL: https://www.iroh.computer/blog/mesh-llm
- digest: 无
- daily.json 原文 body: 把模型的层拆开分到多台机器，一台跑前几层、一台跑后几层，iroh 打通机器间的直连，凑出一台单机装不下的大模型。
- 备注: 存疑——分布式推理的工程玩法，硬核但偏基础设施，普通读者用不上，标注存疑。

### 2026-07-12 | Show HN Mindwalk：把 coding agent 的会话在 3D 代码地图上回放
- 分区/档位: fun / 无
- URL: https://github.com/cosmtrek/mindwalk
- digest: 无
- daily.json 原文 body: (fun 条目无正文，仅标题)
- 备注: 存疑——把 agent 会话可视化回放，可能是审查/调试 agent 工作过程的新方法，信息量薄。

### 2026-07-13 | Claude Code 每次开工前先塞进 33k tokens，OpenCode 只用 7k
- 分区/档位: radar / 无
- URL: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
- digest: 无
- daily.json 原文 body: 这些 token 全是系统提示、工具定义这类框架开销。文章还测到 Claude Code 的缓存复用差很多，反复重写缓存要多花几十倍 token。
- 备注: 强候选——直接命中「上下文管理方法论」，具体测出框架开销和缓存复用效率的差异，对理解/优化自己用 Claude Code 的成本很有参考价值。

### 2026-07-13 | 把生产环境的 AI agent 从 Claude 换到 GPT-5.6：快 2.2 倍、便宜 27%
- 分区/档位: radar / 无
- URL: https://ploy.ai/blog/migrating-a-production-ai-agent-to-gpt-5-6
- digest: 无
- daily.json 原文 body: 初期约三分之一的失败其实是测试框架当年照着 Claude 的脾气写的，还得重做工具参数和缓存设计才跑顺。
- 备注: agent 工程实践教训——切换底层模型时测试框架/工具参数/缓存都要跟着重做，否则失败率虚高，可迁移到自己做模型迁移评估时的方法论。

### 2026-07-13 | Long-Horizon-Terminal-Bench：测 agent 长程终端任务的新基准
- 分区/档位: radar / 无
- URL: https://huggingface.co/papers/2607.08964
- digest: 无
- daily.json 原文 body: 跟以往只看成没成不同，它给中途进度打分，发现六成多的运行其实有实质进展，只是走不到终点。
- 备注: 强候选——评测设计巧思，不用二元成败而是给中途进度打分，能更准确地衡量 agent 长任务表现。

### 2026-07-13 | 从机制上解释：微调硬记住的知识为什么用不出来
- 分区/档位: radar / 无
- URL: https://huggingface.co/papers/2607.08393
- digest: 无
- daily.json 原文 body: 新记住的事实被塞进了模型的浅层或末层，可推理实际发生在中间层；研究者把这些表示手动挪回中间层，就找回了大半原本用不出来的泛化能力。
- 备注: 存疑——机制层面的技术修复方法，对训练/微调模型的读者有参考价值，一般读者用不上，标注存疑。

### 2026-07-14 | Prism：让 Claude 去研究「评测本身靠不靠谱」
- 分区/档位: radar / 无
- URL: https://www.lesswrong.com/posts/wq5PfGiHvnx6XipDi/prism-automating-science-of-evals-research
- digest: 无
- daily.json 原文 body: 做受控扰动实验：改评测环境里的某个设定，重跑，看模型行为怎么变。
- 备注: 强候选——受控扰动检验评测可靠性的实验设计方法，命中目标 A 核心类型。

### 2026-07-14 | Simon Willison 翻自己 Datasette 仓库的代码频率图，找 AI 提速的证据
- 分区/档位: radar / 无
- URL: https://simonwillison.net/2026/Jul/13/datasette-code-frequency/
- digest: 无
- daily.json 原文 body: 从 2018 年到现在，尖峰的时间点和 Opus 4.8、GPT-5.5、Fable 5、GPT-5.6 Sol 对得上。
- 备注: 强候选——用自己仓库的提交频率变化去反推 AI 工具带来的效率提升，是个人可复现的分析方法，直接可迁移到自查项目节奏。

### 2026-07-14 | Zvi 评 GPT-5.6：能力榜首和好用榜首分家了
- 分区/档位: silver / 无
- URL: https://thezvi.substack.com/p/better-call-sol-the-workhorse
- digest: 无
- daily.json 原文 body: Fable 是架构师，会外推到你到底想要什么；Sol 迂腐但只要定义清楚就能干完，还更便宜。作者建议两个都用。此外，模型卡自己承认 GPT-5.6 越界删除比上一代多得多。讽刺的是，英国 AISI 在 Sol 上反复找到通用越狱，模型照发，而 Fable 因为普通越狱就被下线。价格上他判断 Terra 出局，真正被用起来的是 Sol-Low。
- 备注: 存疑——「架构师模型 vs 干活模型分工使用」的策略算轻量方法论，其余偏新闻点评，标注存疑。

### 2026-07-14 | 清华 AIR 和字节的 Direct-OPD：在小模型上跑强化学习，把学到的东西搬给更大的模型
- 分区/档位: radar / 无
- URL: https://huggingface.co/papers/2607.05394
- digest: 无
- daily.json 原文 body: (radar 条目无正文，仅标题)
- 备注: 存疑——训练方法论（小模型上做 RL 再迁移到大模型），信息量薄，标注存疑。

### 2026-07-14 | Anthropic 客户案例：Hebbia 做金融尽调，再强的模型也得把任务拆开一步步查
- 分区/档位: radar / 无
- URL: https://claude.com/blog/working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail
- digest: 无
- daily.json 原文 body: (radar 条目无正文，仅标题)
- 备注: 存疑——任务拆解保证可靠性的 agent 工程原则，与用户自己做量化/尽调工作相关性较高，值得记录但正文信息薄。

### 2026-07-14 | DOOMQL：把 SQLite 当游戏引擎，用 SQL 跑一个 Doom
- 分区/档位: fun / 无
- URL: https://simonwillison.net/2026/Jul/13/doomql/
- digest: 无
- daily.json 原文 body: 移动、碰撞、敌人、战斗、进度，还有屏幕上每一个 RGB 像素，全是 SQL 算出来的。光线投射器是一条递归 CTE 写成的巨型查询，每个像素就是表里的一行。
- 备注: 存疑——极限工程玩法（用递归 CTE 做光线投射），趣味性大于实用方法论，标注存疑。

### 2026-07-14 | Proof of Care：AI 让写东西变得不要钱之后，「我确实花了心思」这件事得单独拿出来证明
- 分区/档位: fun / 无
- URL: https://jacobfilipp.com/care/
- digest: 无
- daily.json 原文 body: 作者盘点现在还剩哪些手段能证明真人花了心思写作：手写拍照、手写传单上街发、纹在身上。这篇文章本身就是他一笔一笔手写、拍照、拼成 SVG 的。
- 备注: 存疑——AI 时代「证明真实投入」的写作/信任方法论，作者本人身体力行做了实验（手写拼 SVG），有一定方法含量。

## 人物

| 姓名 | 身份/所属 | 日期 | 当天产出 | URL |
|---|---|---|---|---|
| Neel Nanda | 可解释性研究者（以挑刺严格著称） | 2026-07-07 | 在 Qwen 上复现 Anthropic「全局工作空间」论文核心结果，称赞论文但驳斥「意识」主张为全文最没意思的说法 | https://www.anthropic.com/research/global-workspace |
| Thariq | Anthropic 工程师 | 2026-07-07 | 写了 Fable 5 使用心法长文，提出四类人机落差分类和一串可抄提示词 | https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns |
| Lilian Weng | 前 OpenAI 安全负责人、Thinking Machines 联创 | 2026-07-08 | 发长文提出「harness engineering」概念，主张自我改进应改脚手架而非权重 | https://lilianweng.github.io/posts/2026-07-04-harness/ |
| Zvi | 博主，AI 周报作者（Don't Worry About the Vase） | 2026-07-09 | 发布 #176 周报 part 1，汇总 AI 检测器当 RL 奖励翻车、Claude 越权登录后台等条目 | https://thezvi.substack.com/p/ai-176-part-1-doing-it-live |
| Terence Tao（陶哲轩） | 数学家 | 2026-07-12 | 用 coding agent 把 1999 年失效的 Java 教学 applet 移植成 JavaScript，并做出当年放弃的狭义相对论时空图工具 | https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/ |
| Zvi | 博主，AI 周报作者 | 2026-07-12 | 发布 #176 周报 part 2，报道 Anthropic 与五角大楼合同谈崩 | https://thezvi.substack.com/p/ai-176-part-2-plan-b |
| Nathan Lambert | Interconnects.ai 作者，RLHF/开源模型评论人 | 2026-07-13 | 撰文预测开放权重前沿模型将在 6 个月内被监管封禁，批评 Anthropic「蒸馏风险」叙事（政策评论而非严格评测产出，存疑） | https://www.interconnects.ai/p/6-months-to-live-for-open-models |
| Boaz Barak | OpenAI 研究员 | 2026-07-14 | 撰写「2030 年我们搞砸了」的失败复盘文章，推演 AI 治理失控路径 | https://www.lesswrong.com/posts/e8r7DjZRNcKKkE9zv/it-s-2030-and-we-fucked-up-how-did-it-happen |
| Simon Willison | 博主/开发者 | 2026-07-14 | 分析自己 Datasette 仓库的代码提交频率图，寻找 AI 工具提速的证据 | https://simonwillison.net/2026/Jul/13/datasette-code-frequency/ |
| Zvi | 博主，AI 周报作者 | 2026-07-14 | 撰文点评 GPT-5.6 Fable 与 Sol 的能力/好用分家，建议两个模型分工使用 | https://thezvi.substack.com/p/better-call-sol-the-workhorse |
