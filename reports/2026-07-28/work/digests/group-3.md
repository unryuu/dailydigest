# Import AI 466：机器人的苦涩教训 + 周级编程任务被跑通

- 推荐强度: 强
- 档位线索: 两块都够硬，但性质不同。MirrorCode 那块是**可核的、带数字的能力跃迁**（1 年前 30% → 现在 17/25 满分；14 小时 251 美元干完人类 2–17 周的活），单独拎出来够银牌，甚至可以争金；机器人那块是 Anthropic 自家 Project Fetch 的对照数据（181 分钟 → 9 分 35 秒）+ Sunday 的 99.1%，硬数字有但都是厂商自报，做银牌的第二支点合适，单独扛金偏虚。建议：**以 MirrorCode 为主、机器人为副，合并成一条银牌**；若当天缺金，MirrorCode 可以单独提档试试。
- 涉及文章: [Import AI 466: The warning shots will continue until civilization wakes up](https://importai.substack.com/p/import-ai-466-the-bitter-lesson-for) · Import AI（Jack Clark）· 2026-07-27
- 取材范围: 只取前两块（MirrorCode、机器人双拼），第三块 OpenAI 黑客事件按派活要求整块跳过。本期无其他硬货小块（余下只有虚构栏目 Tech Tales: Scaling Laws for Retrocausality）。

## 核心主张

这期的两块拼在一起是同一个判断的两面：**通用模型的规模化正在把此前需要专门工程的领域直接吃掉**。MirrorCode 证明 AI 已经能在纯黑箱条件下把一个几万行的陌生程序从零重写出来，任务时长按人类工时算是「周」级；Project Fetch 第二阶段证明同一个没有为机器人做过任何专门优化的模型，10 个月内从「完全做不了」变成「自主 9 分半做完」。Clark 自己把 MirrorCode 的意义拔到了「AI 能自我定位（self-orient）」——不是编程变强了，是它能仅凭输入输出把外部世界的东西复刻成自己的能力。

## 为什么值得看（钩子）

「AI 干完人类要两周到四个月的活，花 251 美元」是一个能单独站住的标题级事实，而且有第三方评测机构（Epoch + METR）背书，不是厂商自吹。机器人那块的对照更狠：**进步不是努力做机器人做出来的**，是通用模型顺带的。

## 关键细节 / 引述

**一、MirrorCode（Epoch AI + METR 联合发布）**
- 评测设计：只给 CLI 访问权，不给源码、不给上网，要求把目标程序完整重新实现一遍。原文："Without access to the original program's source code or the web, a full reimplementation requires devising a structure for the entire program, rather than merely translating the code piece-by-piece."
- 目标程序举例及体量：pkl（Apple 的可编程配置语言，6.1 万行）、gotree（系统发育树解析，1.6 万行）、qsv_select（CSV 列选择与重排，8.7 万行）。共 25 个目标程序。
- 最硬的单点：Opus 4.7 用 14 小时、251 美元推理成本解掉一个任务，METR 和 Epoch 估计人类要做 **2–17 周**。
- 整体成绩："Across all 25 target programs, 17/25 had at least one perfect-scoring run. Four more targets had a near-perfect run scoring over 99%."
- 跨模型：Claude Opus 4.7 和 GPT-5.5 都成功用多种编程语言重实现了 gotree，成本 100–400 美元；Opus 4.7 还重实现了体量更大的 pkl。
- 跃迁量级（核心对比）："Leading models from a year ago would have scored about 30%, and were limited to simpler programs, such as a calendar utility."
- 天花板还在：8/25 从未做到 100%，4/25 从未做到 99%。最难的是 ruff（Python linter/formatter），此外数学包 giac_subset 和邮件认证库 mailauth 也很吃力。
- 发布形态：开源了 scaffold + 25 个目标程序中的 22 个，共 132 个任务实例，覆盖 6 种语言。本基准 4 月首次预告（Import AI #453），本期是正式放出。
- Clark 的解读（原话）："AI systems can self-orient with regard to their environment… allowing them to bootstrap their own form of industrial civilization merely by having black box access to our own."
- 出处：https://epoch.ai/MirrorCode ；代码 https://github.com/epoch-research/MirrorCode

**二、机器人的「苦涩教训」——具体指什么**
- 这里的「苦涩教训」不是 Clark 引某篇论文的措辞，而是他给本期这组双拼起的标题（"DOUBLE FEATURE: the bitter lesson and robotics"）。所指非常明确：**机器人能力的提升来自通用模型的规模化，不来自机器人专项工程**。
- 他引的两份材料：
  1. **Anthropic 自家的 Project Fetch: Phase Two**（https://www.anthropic.com/research/project-fetch-phase-two ）。2025 年 8 月：Claude Opus 4.1 无法自主完成四足机器人任务，人类借助模型的效率是无模型的两倍，全部任务共耗时 181 分钟。2026 年 5 月：Opus 4.7 自主完成除一项外的全部任务，用时 9 分 35 秒。Clark 的小标题写的是「比此前人类纪录快 20 倍」（181 ÷ 9.58 ≈ 19 倍）。Anthropic 原文："This progress is not the result of a concerted effort to improve the robotics."
  2. **机器人创业公司 Sunday 的 ACT-2**（https://www.sunday.ai/blog/act-2-preview ）。叠衣服任务 99.1% 成功率，"performing 778 successful folds across 9 garment types"。短裤、T 恤这类简单件更容易，衬衫等复杂件成功率 >90%。他们的方法论一句话："scale pretraining, then hill-climb with minimal in-house data."（先把预训练做大，再用极少量自采数据爬坡）。Sunday 称同一个基座模型已经在学更广的家务能力，包括吸尘、玩具归置、拉拉链。
- Clark 的解读：机器人历来卡在泛化——工业机器人在剧本化环境里能干活，家用机器人不行。如果 Sunday 这条路走通，机器人进展和扩散都会加速，并把这与「具备递归自我改进能力的系统」联系起来。

**三、副标题的归属（派活方点名要核的）**
- 副标题 "The warning shots will continue until civilization wakes up" 是 **Clark 自己的话，无任何转述或归属**，是他给整期定的调子（句式仿 "the beatings will continue until morale improves"）。
- 需要注意：这句话的落点在**第三块 OpenAI 黑客事件**（正文里他写 "This is the definition of an AI safety warning shot" 和 "Less of a warning shot and more of a warning kaboom"，都出现在那一块）。也就是说，**副标题不能拿来给前两块做帽子**——引用它就等于把读者引向我们本期不收的那条线。

## 与近期的关系

- MirrorCode 本身是**新东西**，本期首次正式发布，我们此前未报过（Import AI 自己说 4 月 #453 预告过）。第三方评测 + 具体成本与工时数字，重复风险低。
- Project Fetch 是 Anthropic 2025 年 8 月那次「让 Claude 开小卖部/操作机器人」系列的第二阶段，**是旧线的新数据点**，主要价值在 10 个月的纵向对照，不是新概念。若近期已报过 Anthropic 机器人相关内容，需核一下角度是否撞车。
- 唯一明确的重复风险在第三块（OpenAI/Hugging Face 入侵），已按要求整块排除，本 digest 未取其任何内容。

## 未核到 / 边界说明

- Project Fetch 用的四足机器人具体型号：原文只写 "quadruped robot"，**未读到**厂商或型号。
- MirrorCode「14 小时 251 美元」对应的是 25 个目标里的哪一个：**未读到**。
- Sunday 的 ACT-2 数据为公司自报的 blog preview，非第三方复现。
