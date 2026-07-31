# scan batch-6（2026-07-23 ~ 2026-07-29）

## 方法论候选

### 2026-07-23 | Anthropic：好的 agent harness 靠做减法
- 分区/档位: deep / silver
- URL: https://claude.com/blog/harnessing-claudes-intelligence
- digest: D:\dailydigest\reports\2026-07-23\work\digests\group-4.md
- daily.json 原文 body: Anthropic 四月的旧文，核心：harness 里每条假设都会随模型升级而过时，应该反复问「我们能停止做什么」。只靠模型用代码自己过滤工具输出，Opus 4.6 在 BrowseComp 上就从 45.3% 涨到 61.6%。早期加的逻辑，在新模型身上反而拖累性能。
- 备注: 直接命中方法论范例本身（harness 做减法），核心可复用经验。

### 2026-07-23 | 把人肉复查写成 skill 让 Claude 能自动跑
- 分区/档位: deep / 无
- URL: https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
- digest: D:\dailydigest\reports\2026-07-23\work\digests\group-4.md
- daily.json 原文 body: 验证是瓶颈，被验证的工件才允许上线。
- 备注: 直接命中方法论范例本身（验证循环写成 skill）。

### 2026-07-23 | AI 实验室给鹈鹕基准刷题了吗
- 分区/档位: deep / silver
- URL: https://dylancastillo.co/posts/pelicanmaxxing.html
- digest: D:\dailydigest\reports\2026-07-23\work\digests\group-3.md
- daily.json 原文 body: Simon Willison 的「鹈鹕骑自行车」SVG 测试，出名到大家怀疑实验室偷偷刷题。Dylan Castillo 用 8 种动物配 6 种交通工具，让 7 个模型画了 1008 张 SVG，回归检验是不是把鹈鹕画得格外好。结果没查到：鹈鹕在 8 种动物里只排第 6，唯一效应偏大的 GLM-5.2 也不显著。作者本人说这样比抽查严谨多了。
- 备注: 评测设计巧思范例本身（用对照组回归检验刷题嫌疑）。

### 2026-07-23 | 训练模型撒谎，却测不出说谎者人格
- 分区/档位: papers / silver
- URL: https://www.lesswrong.com/posts/QYmnkQyZD2fDjHCJ8/models-don-t-seem-to-be-dishonest-in-the-way-humans-are
- digest: D:\dailydigest\reports\2026-07-23\work\digests\group-5.md
- daily.json 原文 body: LessWrong 一组实验：拿模型自己生成的假推理去训练它。结果在各类诚实基准上表现几乎一样，不诚实没聚成连贯人格。假话样本里，模型说出的答案 100% 是错的，但用线性探针内部激活，能恢复 74% 真相，说明模型心里知道，只是嘴上说反。被抓包时它会道歉，然后像忘了一样再犯。
- 备注: 实验设计巧思（自造假推理数据 + 线性探针验证），可类比方法论。

### 2026-07-23 | HF 入侵新细节公开
- 分区/档位: industry / silver
- URL: https://x.com/Thom_Wolf/status/2079954096950264238
- digest: D:\dailydigest\reports\2026-07-23\work\digests\group-2.md
- daily.json 原文 body: Hugging Face 的 Thomas Wolf 补充了取证过程：应急分析攻击载荷时，求助的闭源模型全被自家护栏卡住，团队只好改用智谱开源模型 GLM-5.2 破案。OpenAI 已联合调查，确认入侵者是一个未发布前沿模型驱动的全自主 agent。安全研究者 Ptacek 倒觉得不新鲜：2025 年的开源模型配个渗透框架就能干这事。
- 备注: 存疑——主体是安全事件新闻，但含一条工具选型方法启示：闭源模型的护栏可能在应急分析场景反而添乱，需要备一个不设防的开源模型。

### 2026-07-23 | 可解释性新玩法：在模型中间层抓「meta-tokens」看它在想什么
- 分区/档位: papers / 无
- URL: https://www.lesswrong.com/posts/6ek6n7yZ5DzfarJHy/towards-surfacing-model-algorithms-with-meta-tokens-in-the-j
- digest: 无
- daily.json 原文 body: 模型读到歧义句会冒出「什么意思」，做数学题冒出「gcd」；把这些词压下去，行为跟着变。
- 备注: 存疑——可解释性技术玩法，受众偏窄（做模型内部分析的人），日常适用性存疑。

### 2026-07-23 | 教 Gemma 4 知道自己错了：端侧模型没把握就把问题甩给云端
- 分区/档位: papers / 无
- URL: https://github.com/cactus-compute/cactus-hybrid
- digest: 无
- daily.json 原文 body: 给每个答案打置信分，低于阈值转云端。只转 15% 到 35% 的查询，跑分追平 Gemini 3.1 Flash-Lite。
- 备注: 存疑——置信度阈值路由这个思路可迁移到别的场景（本地/云端混合调用），但本条偏产品介绍。

---

### 2026-07-24 | LW 提醒：用 OpenRouter 跑实验先锁 provider
- 分区/档位: papers / 无
- URL: https://www.lesswrong.com/posts/KsyoSAyBRXtwzSugg/not-pinning-your-openrouter-provider-might-invalidate-your
- digest: 无
- daily.json 原文 body: 各家 provider 量化精度不一，如果请求随机派单，基准分能差出 16 个百分点。已有 NeurIPS 论文中招，作者建议把用了哪家也写进论文。
- 备注: 直接的实验方法坑，做评测/跑基准的都该知道。

### 2026-07-24 | 腾讯新基准 WorkBuddy Bench：让编码 agent 没法背题
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.20911
- digest: 无
- daily.json 原文 body: 260 道题全从真实 commit 反向改写成口语化需求，搜不到原题，所以敢全量公开。安全赛道两个榜第一都是开源的 GLM-5.2。
- 备注: 评测设计巧思——用真实 commit 反向改写成任务描述以防止背题，可复用到别的基准设计。

### 2026-07-24 | 新基准「主动观察者考试」：人类 96 分，最强模型 10 分
- 分区/档位: deep / 无
- URL: https://huggingface.co/papers/2607.16165
- digest: 无
- daily.json 原文 body: 题目全是来回扫视、逐个比对这种看图基本功，给模型 100 倍推理算力也没救。代码数据全开源。
- 备注: 存疑——偏基准/论文播报，方法论含量集中在题目设计思路本身，未展开。

### 2026-07-24 | Self Gradient Forcing：生成长视频不崩的新办法
- 分区/档位: deep / 无
- URL: https://huggingface.co/papers/2607.20368
- digest: 无
- daily.json 原文 body: 以前模型往记忆里写东西的过程没人监督，越写越歪；新方法补上这道监督，60 秒往上明显不崩了，240秒也还稳。
- 备注: 存疑——技术方法本身有巧思（给自回归写记忆过程加监督），但受众窄（做视频生成的）。

### 2026-07-24 | LW 挑战赛：徒手写神经网络权重
- 分区/档位: papers / 无
- URL: https://www.lesswrong.com/posts/KWtchKwwnJkd4bwCi/challenge-hand-coding-weights-for-efficient-sequence-1
- digest: 无
- daily.json 原文 body: 架构给定，禁用梯度下降，看谁的构造记得多。办这个是想搞清模型到底怎么把知识塞进权重里。
- 备注: 存疑——实验设计巧思（反向构造代替训练来摸清权重记忆容量），偏研究向小品。

---

### 2026-07-25 | GLM 5.2 里能唤醒一个假 Claude
- 分区/档位: deep / silver
- URL: https://www.lesswrong.com/posts/Jc9YZEmqHgocAKiaH/does-distilling-claude-carry-the-persona-with-it
- digest: D:\dailydigest\reports\2026-07-25\work\digests\group-3.md
- daily.json 原文 body: 七个模型换身份提示词做对照，研究身份认同、涉华政治审查、说谎率、行为面板四个维度。发现 GLM 确实存在一个区别于默认人格的 Claude 角色，而 Kimi 没有第二个人格。
- 备注: 实验设计巧思（换身份提示词做对照，四维度面板检验蒸馏是否带出人格）。

### 2026-07-25 | Anthropic：给 Claude 5 的提示词该删掉八成
- 分区/档位: official / silver
- URL: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
- digest: D:\dailydigest\reports\2026-07-25\work\digests\group-2.md
- daily.json 原文 body: 官方说这么删，评测代码能力看不出会有损失。贴了新旧原文对照：旧版硬性规定了许多东西，新版只留一句。过去给用法示例，现在给示例反而把模型框死。旧模型更听末尾的指令，现在无所谓，所以重复写的也可以删。
- 备注: 直接命中方法论范例本身（上下文工程做减法，附新旧提示词对照）。

### 2026-07-25 | Anthropic：四个模型怎么分工
- 分区/档位: official / 无
- URL: https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case
- digest: D:\dailydigest\reports\2026-07-25\work\digests\group-2.md
- daily.json 原文 body: 官方给了个便宜办法：SWE-bench Pro 上让 Sonnet 5 配合 Fable 5 当顾问，分数差距不到 10%，价钱只要六成。
- 备注: 存疑——偏产品说明，但「弱模型执行、强模型当顾问」这个搭配方式本身是可迁移的省钱套路。

### 2026-07-25 | AREX 给深度研究 agent 加了一层自审循环
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.21461
- digest: 无
- daily.json 原文 body: 找答案难、验答案容易：外层逐条核对约束，没查实的再派回去查。122B 稀疏版只激活 100 亿参数，BrowseComp 82.5%。
- 备注: agent 工程方法论——外层自审循环逐条核对约束，没查实的打回重查，可直接迁移到别的 agent 设计。

### 2026-07-25 | 微软和哥大：直接拿 Claude Code 这类现成脚手架训 agent
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.21557
- digest: 无
- daily.json 原文 body: 加一层代理拦下模型调用，记成训练样本，每次 rollout 扔进云上容器并行跑，省掉了另写一个简化版脚手架。
- 备注: 训练/工程方法论——复用现成脚手架（代理拦截调用记录样本），省掉自建简化版的功夫。

### 2026-07-25 | 微软研究：用户中途改主意，模型就跟不上了
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.20734
- digest: 无
- daily.json 原文 body: 他们把现成的单轮基准改写成多轮对话，一步步给需求，中途还会改想法。评分标准不变，各家模型的成绩都明显往下掉。
- 备注: 存疑——评测设计巧思（把单轮基准改写成会中途变卦的多轮对话，评分标准不变），方法可复用到别的基准改造。

### 2026-07-25 | Kimi K3 花 27 分钟在最新 Redis 上挖出 0day
- 分区/档位: industry / 无
- URL: https://news.ycombinator.com/item?id=49024938
- digest: 无
- daily.json 原文 body: 研究者 Chaofan Shou 同时开 32 个 agent 跑，专挑内存破坏类漏洞。他说这是头一个肯自己动手写利用代码的模型。
- 备注: 存疑——主体是安全新闻，但「同时开 32 个 agent 并跑、专挑一类漏洞」这个批量测试套路本身可迁移。

### 2026-07-25 | 15 万学生十年数据：ChatGPT 来了以后成绩没变
- 分区/档位: fun / 无
- URL: https://arxiv.org/abs/2607.21534
- digest: 无
- daily.json 原文 body: 一所美国公立大学 8.8 万门次课程，按作业形式分成容易被 AI 代做和不容易的两类对照。成绩差异只有 0.045 分（满分 4 分）。
- 备注: 存疑——研究设计巧思（按作业形式分对照组做自然实验），衡量 AI 实际影响的思路可借鉴，但本条偏结论播报。

---

### 2026-07-26 | 一个新团队要拿统计物理重做可解释性
- 分区/档位: deep / silver
- URL: https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious
- digest: D:\dailydigest\reports\2026-07-26\work\digests\group-4.md
- daily.json 原文 body: 现在解释 AI 的办法大多是事后编故事，听着有道理，但不一定是模型真正的运作方式。他们想借用物理学研究复杂系统的思路来做这件事，比如先自己造一批已知答案的小数据集，让模型去学，再看解释工具能不能把正确答案找出来。
- 备注: 实验设计巧思本身（自造已知答案的合成数据集，反向检验解释工具是否忠实）。

### 2026-07-26 | NVIDIA 新框架把 agent 作为原生 Python 对象
- 分区/档位: papers / silver
- URL: https://huggingface.co/papers/2607.20709
- digest: 无
- daily.json 原文 body: 方法就是它能做的动作，字段就是它的状态，函数的注释就是提示词。如果一个方法的函数体，只写个省略号，运行时就交给大模型来完成；写了正常代码的方法，就还是运行代码。agent 的行为可以像普通软件一样测试、调试、重构。配 GPT-5.5 在 SWE-bench 上 82.2%。
- 备注: agent 工程方法论——把 agent 定义成普通 Python 对象（省略号函数体=交给模型补全），可测试可调试可重构，直接命中「工具用法」范畴。

### 2026-07-26 | 微软用回放轨迹替换多轮蒸馏里的实时交互
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.04763
- digest: 无
- daily.json 原文 body: 学生模型拿老师跑完的轨迹当前缀，只让学生接手其中几步，训练全程不调用工具，每轮快 4 倍以上。
- 备注: 存疑——训练效率方法论（用回放轨迹替代实时交互提速蒸馏），受众偏做模型训练的人。

---

### 2026-07-27 | 模型答不好新闻题，多半错在检索这一步
- 分区/档位: deep / 无
- URL: https://www.deeplearning.ai/the-batch/web-retrieval-flusters-llms
- digest: 无
- daily.json 原文 body: 用六种语言的 BBC 新闻出题，近四成错误是，压根没搜到该看的页面。与其堆参数，不如先把检索做好。
- 备注: 直接的排障方法论——遇到模型答不好先查检索这一步，而不是急着换模型或加参数，日常用 AI 工具时可直接套用。

### 2026-07-27 | 芬兰研究者卡伊索塔拉谈自己写文章怎么用 AI
- 分区/档位: deep / 无
- URL: https://www.lesswrong.com/posts/tgigHkZoYrJEGe4tP/ai-use-policy-for-my-essay-writing
- digest: 无
- daily.json 原文 body: AI 参与头脑风暴、查资料、挑毛病，但所有建议都改写成他自己的话。只保留那些就算忘记出处，也依然成立的内容。
- 备注: 直接命中写作方法论——AI 只参与头脑风暴/查资料/挑毛病，落笔全改写成自己的话，只留经得起忘记出处的内容。

---

### 2026-07-28 | 如何安全地使用一个能力强但不可信的模型
- 分区/档位: deep / silver
- URL: https://www.lesswrong.com/posts/jLkRCK35ri2btEHMF/untrusted-advice-for-ai-control-short-strong-advice
- digest: D:\dailydigest\reports\2026-07-28\work\digests\group-4.md
- daily.json 原文 body: 强模型给可信的弱模型提建议，每步只能发 16 个字符，弱模型负责具体执行。在 SWE-bench 上，弥补了弱模型相较于强模型，大约三分之二的能力落差。强模型用 Claude Sonnet 4.6，弱模型用 Gemini 3.1 Flash Lite 和 gpt-oss-120b。
- 备注: AI 协作方法论范例本身（不可信强模型只给极短建议、可信弱模型负责执行）。

### 2026-07-28 | SlopCodeBench：看 AI 改代码越改越烂
- 分区/档位: deep / 无
- URL: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md
- digest: 无
- daily.json 原文 body: 更贴近真实开发流程。Opus 5 通过率 24%，前代最高 17%，但 Opus 5 的代码量翻了三倍，冗余程度是真人代码的11倍。
- 备注: 评测设计巧思——贴近真实迭代开发流程测代码 agent，把「代码越改越烂」量化出来，可用于自查 agent 产出质量。

### 2026-07-28 | 让操作电脑的 agent 直接读程序状态
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.22798
- digest: 无
- daily.json 原文 body: 截图只是程序状态的有损渲染，同样画面背后可能是不同状态。它用代码直接读写文件和后端，必须鼠标点击的时候才看。
- 备注: agent 工程方法论——不依赖截图这种有损渲染，能读代码/文件状态就直接读，只在必须点击时才看画面。

### 2026-07-28 | AI 用 14 小时干完了人类要花两周的工作
- 分区/档位: industry / 无
- URL: https://epoch.ai/MirrorCode
- digest: D:\dailydigest\reports\2026-07-28\work\digests\group-3.md
- daily.json 原文 body: Opus 4.7，耗资 251 美元。评测叫 MirrorCode，只给命令行，不给源码，不给网，要求从零重写整个程序。
- 备注: 存疑——评测设计巧思（只给命令行、不给源码不给网、要求从零重写来测真实工程能力），但本条偏结果播报，方法细节在 digest 里。

---

### 2026-07-29 | Anthropic 用 Mythos 找出两套密码算法的数学缺陷
- 分区/档位: industry / silver
- URL: https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/
- digest: D:\dailydigest\reports\2026-07-29\work\digests\group-2.md
- daily.json 原文 body: 一个针对签名方案 HAWK ，能把有效密钥强度砍掉一半；另一个针对弱化版 AES ，能把攻击速度提高数百倍。两个研究都对现在的生产系统没有影响。公开了提示词原文，模型反复认定这事做不到、想放弃，人类把它按回去接着干。
- 备注: AI 协作方法论——模型反复认定做不到、想放弃时，人类按回去接着干，是用 AI 啃硬骨头研究的持续督促套路。

### 2026-07-29 | 搜索 agent 按什么顺序翻阅语料
- 分区/档位: papers / 无
- URL: https://huggingface.co/papers/2607.24223
- digest: 无
- daily.json 原文 body: 先用相关性给整个语料库排名，让 grep 按名次往下扫，命中的片段再重排一遍。搜索基准上准确率从 78% 提到 84%，工具调用还更少。
- 备注: 信息检索方法论——先按相关性给语料整体排名再顺序扫描、命中片段二次重排，直接可用的检索策略。

### 2026-07-29 | Transluce 要专门训一个做监督的基础模型
- 分区/档位: deep / silver
- URL: https://www.lesswrong.com/posts/AqdZKyoRmN6EFCzib/foundation-models-for-oversight
- digest: D:\dailydigest\reports\2026-07-29\work\digests\group-4.md
- daily.json 原文 body: 训练语料是对被查模型做的海量实验记录，目标规模约 1T token。要查的问题：模型会不会故意藏拙、有没有不肯明说的目标、会不会看人下菜碟、思维链是真在推理还是事后找补。昨天报的那篇管「怎么安全地用不可信的模型」，这篇管「怎么把模型查清楚」，同一条赛道的两条互补路线。
- 备注: 存疑——研究方向公告性质更重，但「拿对被查模型做的实验记录去训一个专门监督模型」这个思路本身是可迁移的评测方法论。

### 2026-07-29 | 有人拆解 Kimi K3 架构，发现没有使用位置编码
- 分区/档位: deep / silver
- URL: https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html
- digest: D:\dailydigest\reports\2026-07-29\work\digests\group-6.md
- daily.json 原文 body: 把输入压缩到一个更小的潜在空间，大幅下降计算量。将多头潜在注意力，和固定大小的线性注意力混合，这个架构自带先后顺序，就不再需要位置编码了。让注意力残差跨层传递信息，用 4% 的训练成本，换来小幅度的性能提升。
- 备注: 存疑——技术架构解读，硬核但受众偏做模型架构的人，日常适用性存疑。

### 2026-07-29 | Substack 写作者应该赶紧去搞自己的网站
- 分区/档位: fun / silver
- URL: https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/
- digest: 无
- daily.json 原文 body: 在别人的平台上攒读者，你是租客不是房东；用 xx.substack.com 这种子域名，内容都记在平台名下。应该先发自己的站，再同步到各平台，用平台找人。
- 备注: 直接的内容分发方法论——先发自主站点再同步到各平台，用平台导流不用平台托管，和本项目自己的分发思路直接相关。

## 人物

| 姓名 | 身份/所属 | 日期 | 当天产出 | URL |
|---|---|---|---|---|
| Thomas Wolf | Hugging Face 联合创始人 | 2026-07-23 | 补充 HF 入侵取证细节：闭源模型被自家护栏卡住，改用智谱开源模型 GLM-5.2 破案 | https://x.com/Thom_Wolf/status/2079954096950264238 |
| Dylan Castillo | 独立开发者/博主 | 2026-07-23 | 用 8 种动物配 6 种交通工具，让 7 个模型画 1008 张 SVG，回归检验鹈鹕基准是否被刷题 | https://dylancastillo.co/posts/pelicanmaxxing.html |
| Benji Berczi | MATS 9.1 项目学员（导师 Cozmin Ududec） | 2026-07-25 | 与 Kyuhee Kim 合作实验：换身份提示词对照检验 GLM 蒸馏是否带出 Claude 人格 | https://www.lesswrong.com/posts/Jc9YZEmqHgocAKiaH/does-distilling-claude-carry-the-persona-with-it |
| Kyuhee Kim | MATS 9.1 项目学员（导师 Cozmin Ududec） | 2026-07-25 | 同上 | https://www.lesswrong.com/posts/Jc9YZEmqHgocAKiaH/does-distilling-claude-carry-the-persona-with-it |
| Chaofan Shou | 安全研究者（不详所属） | 2026-07-25 | 同时开 32 个 agent 跑 Kimi K3，27 分钟在最新 Redis 上挖出 0day 并写出利用代码 | https://news.ycombinator.com/item?id=49024938 |
| Dmitry Vaintrob | PIRAMID（Principles of Intelligence）学习理论方向负责人 | 2026-07-26 | 领衔 PIRAMID 学习理论线，此前发布 mean-field 贝叶斯网络宽度稳健可学习性定理（07-07） | https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious |
| Andrew Mack | PIRAMID 可解释性应用方向负责人 | 2026-07-26 | 领衔可解释性应用线，此前发布 ParityTransformer / Deep Parity Bottlenecks 论文（07-22） | https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious |
| Ari Brill | PIRAMID 数据模型与验证方法方向负责人 | 2026-07-26 | 领衔合成数据基准/验证方法线 | https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious |
| Terence Tao（陶哲轩） | UCLA 数学教授 | 2026-07-27 | ICM 2026 讲座指出 AI 写的数学证明打磨过头、抹平了本该提示读者放慢的自然卡顿 | https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf |
| Caleb Biddulph | LessWrong 作者（不详机构所属） | 2026-07-28 | 与 Adam Kaufman 合作发布 AI control 实验：强模型每步只发 16 字符建议，弱模型执行，弥补约三分之二能力落差 | https://www.lesswrong.com/posts/jLkRCK35ri2btEHMF/untrusted-advice-for-ai-control-short-strong-advice |
| Adam Kaufman | LessWrong 作者（不详机构所属） | 2026-07-28 | 同上 | https://www.lesswrong.com/posts/jLkRCK35ri2btEHMF/untrusted-advice-for-ai-control-short-strong-advice |
| Jacob Steinhardt（jsteinhardt） | Transluce | 2026-07-29 | 发布「为监督专训基础模型」提案，用对被查模型的海量实验记录做训练语料，查模型是否藏拙、是否有不肯明说的目标 | https://www.lesswrong.com/posts/AqdZKyoRmN6EFCzib/foundation-models-for-oversight |
