# 世界模型与机器人

- 推荐强度: 中
- 档位线索: 更适合降为无牌，或拆开处理，不足以支撑「三篇论文把世界模型接进机器人操作」这一银牌概括。三篇真正共享的是在通用生成／基础模型与具体环境之间加入显式接口或校准层；其中 Show-Harness 不是世界模型，Programmable World Model 的摘要只明确展示可玩游戏，未明确给出机器人操作实验。唯一有明确数字的硬结果来自 Programmable World Model 的自建 CombatStateBench，外部效度和对照细节在本地摘要中均不可见。
- 涉及文章: [Programmable World Model](https://huggingface.co/papers/2609.10540) · Hugging Face Papers · 2026-09-09
- 涉及文章: [Show-Harness: Just a VLM Agent Can Play Robots](https://huggingface.co/papers/2609.10522) · Hugging Face Papers · 2026-09-09
- 涉及文章: [SyncWorld: Visual Calibration Enables World Models as Zero-Shot Simulators](https://huggingface.co/papers/2609.09155) · Hugging Face Papers · 2026-09-08

## 核心主张

三篇都不再指望一个通用模型直接吃下环境差异，而是把可控性问题交给显式中间层：Programmable World Model 用可执行规则与全局状态驱动视频渲染，Show-Harness 用离散语义动作和机体专用解释器把 VLM 意图落到机器人，SyncWorld 用少量视觉校准轨迹在上下文中说明当前环境的「动作—画面」映射。这个共同点是接口化与环境适配，不是统一的「世界模型机器人操作」范式：Show-Harness 属于 VLM 控制框架，Programmable World Model 摘要中的落地对象是可玩游戏，只有 SyncWorld 明确把世界模型用于机器人动作后果模拟和策略改进。

## 为什么值得看（钩子）

值得看的不是三种模型又刷新了什么总榜，而是它们同时把瓶颈从「模型容量不够」改写成「缺少能表达规则、动作含义和机体差异的接口」。但把三篇捆成机器人世界模型浪潮会夸大共识，也会掩盖它们解决的是三类不同问题。

## 关键细节 / 引述

- Programmable World Model 让 Agent 把自然语言指令翻译成可执行程序，程序定义实体状态与状态转移规则；轻量引擎维护显式、持久的全局状态，连画面外实体和非视觉属性也保留。
- 它用带状态的 3D 定向包围盒作为中间表示，再结合目标相机轨迹，确定性地编译成像素对齐的时空条件信号；预训练视频模型只充当生成式渲染器。CombatStateBench 上报告 94％ Count Accuracy 与 98％ State Accuracy，但本地摘要未给出数据规模、对照模型成绩、误差范围或真实机器人实验。
- Show-Harness 把控制暴露为 VLM 可推理的离散语义动作单元，再由机体专用解释器确定性地落成本地机器人动作；论文强调细粒度物理决策仍由 VLM 负责，并声称同一接口同时支持闭源前沿 VLM 零样本控制，以及小型开源 VLM 经「数个 GPU 小时」微调后的低成本部署。
- Show-Harness 还提供 GUMI，把同一语义动作空间扩展到 GUI 演示采集，使人类和 Agent 不借助专用遥操作硬件也能跨机体「玩」机器人。摘要称其跨任务、机体和环境优于代表性 Agent 与 VLA 范式，但没有披露具体任务、成功率、基线或硬件范围，因此不能据此写成全面胜出。
- SyncWorld 针对同一个数值动作在不同环境、相机视角、机器人位置或机体上会呈现不同视觉结果的问题，要求一段覆盖全部可控自由度的配对画面—动作校准轨迹，在上下文中指定当前设置的 Action–Visual Mapping。
- SyncWorld 声称无需额外训练即可模拟未见设置，并能用模拟 rollout 在测试时改进策略；模型训练时也学习在缺少显式校准时利用交互历史。但摘要没有给出「少量」校准究竟是多少步、未见设置的跨度、仿真准确率或策略提升幅度，零样本指的是不做下游训练，不等于无示例、无校准。

## 与近期的关系

仅凭分配的三份本地摘要，无法核对与往期日报的外部重复。组内概念重叠有限：Programmable World Model 处理规则与长期状态，Show-Harness 处理 VLM 到机器人动作的语义接口，SyncWorld 处理动作在不同视觉／机体设置中的含义校准。若近期已经报道过「给通用模型加适配层即可释放机器人能力」或「世界模型做机器人模拟器」，本组会有较高主题重复风险；新增量应限定在三种接口机制及上述边界，避免包装成一个已经成立的共同范式。
