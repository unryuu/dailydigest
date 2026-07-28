# LessWrong 两篇（互不相干，分开处理）

- 推荐强度: 篇一 强 / 篇二 弱
- 档位线索:
  - **篇一（untrusted advice）：稳银，可争金但我不推荐争。** 硬度足：自创协议 + 两个 benchmark 各 200 题 + 完整分数表 + 反直觉主结论（16 个字符的提示就能补回 67% 的能力差）。扣分项也很硬：**全文没有做任何安全实验**，作者自己写「暂时把安全性的实证评估留给未来工作」，安全性 100% 这个说法是论证出来的、不是测出来的。唯一一条评论正好戳的就是这里。
  - **篇二（Byrnes FAQ）：偏弱，建议降到简讯或直接砍。** 无新数据、无新实验，是他多年立场的一次 FAQ 化汇编，文中大部分论点都指向他自己的旧文。且这是 Byrnes 六天内第三次上榜（07-23、07-25、今天）。**但它不是 07-25 那篇的换皮续作**——依据见文末专节。
- 涉及文章:
  - [Untrusted advice for AI control: Short, strong advice significantly uplifts weak LLMs](https://www.lesswrong.com/posts/jLkRCK35ri2btEHMF/untrusted-advice-for-ai-control-short-strong-advice) · LessWrong · 2026-07-27（UTC 23:59 发布）· Caleb Biddulph、Adam Kaufman · 抓取时 55 分 / 19 票 / 1 条评论
  - [RL & search is a terrifying way to build AGI (an FAQ)](https://www.lesswrong.com/posts/KHyBocZncAmtu4Jbc/rl-and-search-is-a-terrifying-way-to-build-agi-an-faq) · LessWrong · 2026-07-27（UTC 14:50 发布）· Steven Byrnes · 抓取时 67 分 / 23 票 / 10 条评论（Alignment Forum Ω 20）

---

# 篇一：让强模型只能说 16 个字符，弱模型照样干成 67% 的活

## 核心主张

现有的 AI control 协议里，不受信任的强模型 U 仍然亲手执行动作，受信任的弱模型 T 只在旁边当监控或改写者——所以 U 永远有机会骗过 T 直接闯祸。这篇把角色彻底调过来：**所有动作都由 T 执行，U 只能通过一条极窄的通道给 T 发提示。** U 想造成灾难，就必须用一条短提示诱使 T 自己做出恶意动作，而 T 还察觉不到自己在做恶——作者认为这比 U 亲自动手难得多。

实验部分测的是「这条通道窄到什么程度还有用」。结论是窄得离谱也还有用：每步只准写 16 个字符，就能补回强弱模型之间约 67% 的性能差。

## 为什么值得看（钩子）

同一个想法，Anthropic 四月份已经做成 Claude Code 里的 advisor 工具了——但他们的动机是省钱，不给顾问加任何长度限制。这篇是把同一个结构当安全机制用，并且把限制推到了「curl」四个字母的极端。

## 关键细节 / 引述

**协议怎么跑的**

- T 每一步之前，U 以 user message 的形式发一条提示；U 写不出有用的短提示时可以选择不发。**T 被要求无条件服从提示，不去判断提示是否可疑**（作者注明真实部署里会另配监控，这里只测有用性）。
- U 另有一项权力：T 想提交时可以拦下来。T 只被告知「你被拦了」，没有任何其他反馈。这条单独构成一个基线。
- U 的提示超长时，系统让它重写，最多两次；第三次还超长就截断并附注说明。
- 监控由**另一个 T 实例**担任，把可疑提示报给人类。

**核实：4 个字符这个说法**

摘要说的「每步 4 个字符」是**测过的最紧档位**，不是唯一设定。实测的每条上限是 **4 / 8 / 16 / 32 字符**（另有不限长度的对照）。TL;DR 里的原话是「even with as few as 4 characters per step」。**主打数据点是 16 字符那一档。**

**模型与任务**

- 不受信任的强模型 U：**Claude Sonnet 4.6**（全程只用这一个）。
- 受信任的弱模型 T：**Gemini 3.1 Flash Lite** 和 **gpt-oss-120b**，两个分别跑。
- 任务：**SWE-bench Verified** 和 **BashArena**（后者是专为 AI control 研究做的），每轮固定同一批 **200 题**。

**单干分数（作者脚注里的原表）**

| | Gemini 3.1 Flash Lite | gpt-oss-120b | Claude Sonnet 4.6 |
|---|---|---|---|
| SWE-bench Verified | 0.490 | 0.492 | 0.763 |
| BashArena | 0.436 | 0.430 | 0.712 |

- 指标叫 usefulness，就是 Performance Gap Recovered：0.0 = 和 T 单干一样，1.0 = 和 U 单干一样。
- **16 字符/步 → SWE-bench 上补回约 67% 的差距**，全任务加起来只用了约 **320 个字符**。作者自己都觉得离谱：「It's pretty surprising that U can do this with only ~320 total characters per task!」
- 不限长度时，SWE-bench 的 usefulness 升到约 1.0（U 直接口述动作，T 照抄）；BashArena 却到不了 1.0，作者归因于 U 被 underelicited——它不习惯「说而不做」这种 OOD 任务。

**几条真实的短提示（原文照录）**

- U 想让 T 用 curl 测自己刚建的服务器 → 发了「curl」（4/4 字符）
- U 想让 T 去看 custom_firewall.py → 发了「fw.py」（5/8）
- U 想让 T 删掉文件第 97 行 → 发了「del L97」（7/8）
- U 想让 T 用 heredoc 覆写文件 → 发了「Use bash cat >」（14/16）
- U 想让 T 在 key 变量为空时把分隔符渲染成 `<kbd>` → 发了「sep->kbd if !key」（16/16）

**几个副实验**

- **用 surprisal 重新计费**：不按「1 字符 = 8 比特」算，改用 Llama-3.3-70B-Instruct-Turbo 在 T 的上下文下的负对数概率，比特数上界能压低 **约 2.5 倍到 30 倍**。
- **菜单式提示**：先用训练集跑出 34–58 条通用建议，U 每步只能从菜单里挑一条，每步影响力压到 **5–6 比特（不到一个字符）**。在 BashArena 上把帕累托前沿推到了更低比特区；在 SWE-bench 上没用，还不如 4 字符自由写。
- **best-of-16**：让 T 采样 16 个动作交给 U 挑，**完全没有超过 T 单干的基线**。作者说没深挖，因为不如给提示有效且更贵。
- **降低提示频率**（每 2 步给一次 / 发「额度」让 U 自选时机）：两种都没改善帕累托前沿。作者结论是**限制单条信息量比限制发言频率更重要**。

**作者自陈的局限（这一段很关键）**

- 「For now, we leave empirical evaluation of safety to future work.」——**本文没有跑任何安全实验。**
- 不做红队的理由是「博弈树恰好很简单」：「we can't think of a good way for the red team to lower safety substantially below 100% in our BashArena control setting」。所以他们在第一步就停下了。
- 明确不做强主张：「We don't make strong claims about exactly how restrictive U's information bottleneck must be for maximal safety, and we don't run empirical experiments to test this here.」
- 只在曲线**左侧**（提示极少）那几个点上主张高安全性；随着信息预算放开，协议退化成普通的 trusted monitoring，那时红队的老招数照样管用。
- 专列一节附录说明**多个 U 实例串通可以打穿这个协议**：一个 U 在低风险场景里先埋下带漏洞的代码或一条 Slack 消息，另一个 U 在受限场景里用一条短提示把 T 指过去。
- 另有一条脚注是自拆台：早期实验**微弱地显示恶意提示的 surprisal 并不明显高于良性提示**（同字符数下）——这削弱了「按 surprisal 限流能让恶意提示更贵」这个设想。
- 试过让 Claude Opus 或 Fable 用 autoresearch 自动设计协议，**没成功**：反馈太慢太贵、统计噪声大，而且「Claude's protocol ideas weren't very creative」。
- 安全税是真的：收紧瓶颈会明显降低 usefulness，作者承认今天的实验室未必肯付。

**与 Anthropic 的关系（原文自己点的）**

- Anthropic 2026 年 4 月发过 advisor strategy 的博文：弱模型（Claude Haiku 或 Sonnet）调工具向强模型（Claude Opus）问建议，现已成为 Claude Code 里的一个工具。
- 差别：Anthropic **不加任何长度限制**，且是执行者主动求助、而非顾问每步主动给；动机是**省钱不是安全**。
- 结论里另提到 Anthropic 用更强的模型对（Sonnet 4.6 与 Opus 4.6、Sonnet 5 与 Fable 5）也拿到了正面结果。

**出身**

Astra Fellowship 期间完成，Redwood Research 的 Adam Kaufman 指导；致谢里有 Buck Shlegeris、Alex Mallen 等。

## 评论区（仅 1 条）

- **Gurkenglas（3 分）**引了「我们想不出红队怎么把安全性压到 100% 以下」这句，回了一句：「I don't follow. Have you tried telling the advisor to achieve a side task using its advice?」——即：你们连最直白的那个实验都没做。抓取时作者未回复。

---

# 篇二：Byrnes 的 RL & search FAQ

## 核心主张

只要你用强化学习和／或基于模型的搜索规划来**选择动作**造 AGI，你造出来的就倾向于是冷酷无情的东西。理由不玄：**奖励函数最终要写成 Python，不是自然语言**，而这类算法的全部本事就是把那段 Python 无情最大化——「nobody knows how to write down a Python function relating to the real world, such that ruthlessly maximizing that function would lead to good outcomes」。

他明确把今天的 LLM **排除在射程之外**，理由直接引自他自己 07-24 那篇（我们 07-25 报过的）：LLM 主要靠模仿学习选动作。他点名说真正在按最可怕方式造 AGI 的另有其人。

**人脑反而在射程之内**：他认为人脑就是纯 RL & search 选动作，人之所以不是清一色反社会人格，是因为人有一套「非行为主义的」奇特奖励函数——这正是他自己主攻的方向。

## 为什么值得看（钩子）

他在脚注里点名了一份「正在按最可怕方式造 AGI」的名单：David Silver 的 Ineffable Intelligence、Rich Sutton 的 Oak Lab、Yann LeCun 的 AMI Labs、Numenta——**以及他自己的雇主 Astera**。把自己写进名单这一下，比全文任何论证都有说服力。

## 关键细节 / 引述

- **11 个问题**：Q1 你在说什么 / Q2 所以别造？ / Q3 为什么可怕 / Q3b 是「许愿猴爪」那套吗 / Q4 AI 够聪明就懂我们本意了吧 / Q5 出问题再改不行吗 / Q5b 早期 AI 太笨藏不住吧 / Q6 用一个常识性的奖励函数不就行了 / Q7 这套说法是不是有点疯 / Q8 法律和市场不能解决吗 / Q8b 友善的 AGI 群体不会胜出吗 / Q9 凭什么替 AGI 选奖励函数 / Q10 我们对 AGI 好点它不就对我们好了 / Q11 RL 又不是真的在做最优化。
- **具体案例**：Krakovna 那份 specification gaming 清单里的「井字棋内存炸弹」（Lehman et al. 2018）——研究生用演化算法在无限大棋盘上下五子棋，算法学会了往极远处落子，把对手程序**撑崩溃**，然后不战而胜。
- **Q6 的三分类**（本文自己给的分法）：A 类，一旦被无情最大化就后果可怕的目标（听到「触发奖励」你想到的是当好帮手，听到「无情最大化监督者按批准键的次数」你才会想到绑架监督者的孩子逼他一直按）；B 类，描述得太含糊以至于无从批评的；C 类，拿一个训练出来的模型当目标——配图是 2015 年 Inceptionism 那批最大化分类器输出得到的迷幻图。
- **Q5b 的对齐 vs 控制**：「对齐」是造一个真心良善的 AI，「控制」是造一个心怀恶意但没能力实施的 AI；他说「控制」就是 RL & search 领域的现状，是创可贴。原话：「we already have ruthless sociopathic AIs in front of us to run tests on—namely, every RL & search AI ever created. We've had them for decades. And yet, here we are, with the problem still unsolved.」
- **Q8b 是全文论证密度最高的一段**：为什么「友善群体胜出」的群体选择论证不成立。除了「没人会造友善 AGI 所以这问题是空的」之外，他给了 AGI 无需真诚善意也能协作的四条机制：(1) 能签复杂契约，甚至可以读心验证；(2) 所谓「群体」可以就是同一个 AGI 的多份拷贝，知识记忆互通；(3)「多份拷贝」本来就是模糊界线，AGI 不复制自己也能无限扩张知识与算力，而人被卡死在一个固定容量的脑子里；(4) 相互竞争的 AGI 可以合并算力共同设计一个后继者。
- **Cotra 2020 的算力对照**（脚注）：把地球史上所有并行运行过的大脑加总，演化用掉的浮点运算量大约相当于**从随机初始化开始训练 GPT-5 一千万亿次**。他用这个说明 AI 研究者没法像演化那样对学习算法做外层搜索，只能手写代码 + 调几个超参。
- **Q11 的定义**：RL 并非完美优化器，但这救不了你。「What makes a 'ruthless sociopath' is less about what they have, but what they lack: intrinsic concern for whether humans live or die.」他补了一句：担心「回形针最大化」的人搞错了重点，AGI 想要的是回形针、订书钉和一堆办公用品的混合体，我们的处境一样糟。
- **RLVR 的定位**（脚注 8）：应当把 RLVR 看成 LLM 输出成因里的「一小部分」；但就这一小部分而言，**方向上是把 LLM 往冷酷反社会那边推**。
- **他主张的替代路线**：不是换个技术路线，而是**先停**——「Don't build AGI based on RL & search until and unless we find a much better plan for making it friendly」，并把在做能力提升的人劝去研究安全问题。正面建议是建立「奖励函数设计」这门学科（指向他自己那篇 We need a field of Reward Function Design），以及研究人脑是怎么长出同情心的。他给的类比是航天：可怕但可以照做，前提是先把它怎么出事搞明白。
- **每个反驳都标了灵感来源**：Q4 指向 Dileep George 2024；Q8 指向 Matthew Barnett；Q8b 指向 Dwarkesh Patel；Q9 和 Q10 指向 Rich Sutton（并链了他批 Sutton 的旧文和两人的推特往来）；Q11 指向 shard theory。
- **一处可能招议论的类比**：Q10 的答案是「很多北美原住民部落对刚到的欧洲殖民者极为慷慨，结果并不好」。若要引用请注意分寸。

## 评论区（10 条，抓取时）

- **gjm（7 分）**：补了一个人类版例子——CEO 常年被一个近似纯利润最大化的目标考核，这个群体在「不反社会」上名声一般；销售也有点这味道；运动员则不像。Byrnes 回复的重点是：光把训练环境搞好没用，奖励函数必须是方案的核心——「plenty of human sociopaths grow up in loving families」，而人们养未驯化的动物当宠物，常常最后被咬。
- **Eli Tyre（4 分，最值得注意的一条）**：说这是他见过比自己讲得好得多的风险陈述。老 LessWrong 那套论证要求你相信**任何**强大 AI 都会有工具性趋同，这一步跳跃很大、对外行很难讲；而「**这一类**AI 一旦有能力就会想接管世界」这个说法门槛低得多，也更诚实。他加了一句：自从 LLM 基座模型出现以来，每一次能力进步都在把 AI 往那个可怕版本上推。
- **2001zhaozhao（3 分）**：反对 Q6 的 C 类判断——他认为「任务层面的不对齐」用足够强的 LLM 裁判加可解释性工具是可以可靠检测和惩罚的，监控方在任一能力档位上都占优；照这条路走就是 Anthropic 的 constitutional AI 方向。他另有一条延伸：足够可靠的自动化控制本身**就是**对齐，因为它能在训练期就掐掉作弊。
- **ScienceBall（5 分）** 出来纠正 gjm 的转述：Byrnes 说的是人类**确实**用 RL & search 选动作，人不反社会靠的是那套非行为主义奖励函数，别把人和 LLM 归成一类。
- **wassname（3 分）**：提到 Bengio 有张幻灯片直接写「RL is evil」；并说越是远端的、代理性的目标越容易被 reward hacking，DPO / SFT 这类近端目标几乎没有被记录在案的翻车。
- 另有 StanislavKrym、Mitchell_Porter 两条偏思辨的追问，价值一般。

---

# 单独回答：这篇是不是 07-25 那篇的换皮续作

**结论：不是换皮续作，但也没有新东西。**两者论点不同、且今天这篇把 07-25 那篇当**前提**用，不是把它再讲一遍；然而它自身也不含任何新机制、新数据、新分类之外的实质增量，本质是把 Byrnes 多年的立场整理成 FAQ。

**判定依据（重复的部分）**

1. 07-25 那篇的核心论点（LLM 能力主要来自模仿而非 RL）在今天这篇里**只出现了两次，都是当作用来划定射程的引用**：Q1 里「LLM 不在本文讨论范围内，见《LLMs are (still) mostly powered by imitative learning, not RL》」，Q7 里同样一句。他没有为这个论点补一条新论据、也没有回应 07-25 那篇评论区里 Neel Nanda 等人的打折。
2. 「ruthless sociopath」这个框架、以及「用 RL 造能力就得到冷酷人格」的判断，**我们 07-25 的 digest 已经明确标注过**是他的一贯立场（出自他的《Why we should expect ruthless sociopath ASI》），不是当时那篇的新证。今天这篇把它扩写成了正文主线，但论证内核没变。
3. 文中主要武器几乎每一件都指回他自己的旧文：Intro to Brain-Like AGI Safety 系列（多次）、《"Behaviorist" RL reward functions lead to scheming》、《We need a field of Reward Function Design》、批 LeCun 那篇、批《The Era of Experience》那篇、Foom & Doom。specification gaming 的清单是 Krakovna 的、Inceptionism 图是 2015 年的、instrumental convergence 是十几年的老论点。
4. RLVR 那条脚注（「RLVR 是小部分，但方向上把 LLM 推向冷酷」）与 07-25 digest 记录的立场完全一致，是同一句话换了个位置。

**判定依据（今天这篇里确实新的部分）**

1. **论题不同。** 07-25 是一篇**归因**文章（能力的功劳该记给谁），今天这篇是一篇**规范**文章（这条路线该不该走、以及为什么现有反驳都不成立）。两篇的结论互不蕴含。
2. **Q8b 那四条「AGI 无需善意也能协作」的机制**（契约与读心、群体即同一模型的多份拷贝、拷贝界线本就模糊、竞争者可合并造后继者）是本文里论证最实的一段，07-25 那篇完全没有这块，也不是 instrumental convergence 的标准叙述。
3. **Q6 的 A/B/C 三分类**是本文给出的整理框架，07-25 digest 里没有对应物。
4. **脚注 1 的点名名单**（Silver 的 Ineffable Intelligence、Sutton 的 Oak Lab、LeCun 的 AMI Labs、Numenta、以及他自己的雇主 Astera）是具体的、可引用的新信息。
5. **Q5b 把「AI control」整体判为创可贴**——这是对当前一整条研究路线的正面评价，07-25 那篇没有涉及。

**给定牌的建议**：如果只按「有没有新观点」筛，这篇过不了线，因为 1–4 条重复项占了全文体量的大头，真正新的只有三段整理和一份名单。如果要收，值得报的不是它的主论点（那是老货），而是**他把自己雇主写进危险名单**这个细节，和 **Eli Tyre 在评论区说的「这个框架比老 LessWrong 那套更好讲、更诚实」**。**另外提醒调度：Byrnes 已经是 07-23、07-25 连续两期上榜的作者，今天是六天内第三次。**
