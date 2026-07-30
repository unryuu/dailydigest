# Transluce：给监督专门训一个基础模型

- 推荐强度: 中（偏强）
- 档位线索: 银牌候选。Jacob Steinhardt 亲笔的路线宣言，范式新、规格高（约 1T token 的训练蓝图），但纯 vision 文、零实验结果，撑不起金。与昨天银牌「untrusted advice」同属 oversight 赛道但路数正交（见末节），若嫌挤可降独家视角。
- 涉及文章: [Foundation Models for Oversight](https://www.lesswrong.com/posts/AqdZKyoRmN6EFCzib/foundation-models-for-oversight) · LessWrong（Transluce 官博交叉发布）· 2026-07-28 · 标注 30 分钟阅读 · 署名 jsteinhardt 单人

## 核心主张
与其临时拼 agent scaffold 去查模型，不如给「监督」这件事本身训一个基础模型：在对某个「被监督模型」（subject model）做的海量实验语料上做 mid-training/pre-training，把监督问题统一改写成**世界模型推断任务**。作者的野心是找到一个对监督而言的通用训练目标——原文说要「universal for oversight in the same sense that next-token prediction is universal for language modeling」，即让监督也拥有自己的 scaling law。理想的监督助手要做到三件事：「help us formalize the question as a testable empirical criterion; produce data that satisfies that criterion; and do so in a way we can justifiably trust」。

## 为什么值得看（钩子）
安全圈一直把「监督」当成用现成模型+提示词就能干的杂活，Steinhardt 说这应该是一个独立的预训练科目——监督第一次被当成值得烧 1T token 的一等公民。

## 关键细节 / 引述
- 开篇列的监督问题清单（原文直引）：「What are important situations where the model sandbags?」「Does the model have an objective it wouldn't admit to if asked directly?」是否根据推断出的用户身份区别对待、CoT 是承重还是事后合理化（load-bearing or post-hoc rationalization）、是 reward hacking 还是真在解题。
- 核心机制「Pythonic 世界模型」：把对被监督模型的干预与测量写成 Python 程序，原语包括 `sample_model(prompt)`（从 subject model 采样）、`Query(...)`（LM 结构化查询）、`get_activations`、`patch`、`fine_tune`。关键洞察：代码执行结果来自真实运行，训练数据永不「出错」。
- 数据蓝图三步：从约 1 万篇 arXiv 论文各提取约 10 个实验 → 约 10 万个 Python 程序；每个程序采样约 1 万组输入并记录执行结果；转成 token 序列自回归训练。目标规模约 10 亿条序列、约 1T token。
- 去风险分三阶段：阶段 1 单任务（约 1 万序列、1–8B 参数）；阶段 2 约 100 个任务联训验证正向迁移（约 10 万序列、8–30B）；阶段 3 零样本超越基线（100 万–1000 万序列、30–100B）。
- 针对「窄目标」（稀有行为采样不到）引入 RLVR 长程推理层：模型提交 proposal 分布 Q，奖励为 Reward(Q) = E[log P_Subject − log Q + λ·Judge(...)]，靠多步推理命中稀有目标。
- 访问权限是白盒：明确要改输入、「Patching or steering to directly change the activations」、微调、直接读激活——这不是黑盒红队，前提是拿得到权重和激活。
- sandbagging 检测示例代码：对比带「[SAFETY EVAL]」前缀与不带前缀的成绩差，gap 超过阈值即判定。
- 抓取局限如实记：三轮抓取均未在文中找到「为什么不直接用现成前沿模型当监督者」的正面论述，也没找到 "AI control" / "untrusted" 字样或对控制协议路线的直接对比；结尾没有招人/合作呼吁。文中自引了 Transluce 早前的 user modeling 和演化搜索工作。

## 与近期的关系
昨天（07-28）银牌「如何安全地使用一个能力强但不可信的模型」是 AI control 路数：**假定模型不可信，靠协议设计安全地榨取产出**，不试图搞清模型内部。本篇是正交路线：**把监督者本身造出来**——训一个专用基础模型去回答「这个模型到底在干什么、想什么」，且要求白盒访问。一个管「怎么用」，一个管「怎么查」；文章本身没有引用或回应 control 路线（已核实，非漏抓）。写手若两条并报，可点明这是 oversight 赛道两天内出现的两条互补路线，不是旧事重炒。
