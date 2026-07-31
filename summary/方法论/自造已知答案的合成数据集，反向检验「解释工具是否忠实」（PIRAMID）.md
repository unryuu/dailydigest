# 自造已知答案的合成数据集，反向检验「解释工具是否忠实」（PIRAMID）

- 日期：2026-07-26
- 来源：https://www.lesswrong.com/posts/nbSJhbLERTZFeNxY7/introducing-piramid-physics-informed-research-for-ambitious（主文）
- 主题：四、评测与实验设计

## 这是什么

现在解释 AI 的办法大多是事后编故事，听着有道理，但不一定是模型真正的运作方式。他们想借用物理学研究复杂系统的思路来做这件事，比如先自己造一批已知答案的小数据集，让模型去学，再看解释工具能不能把正确答案找出来。

## 细节（来自精读摘要）

Principles of Intelligence（PrincInt，即改名后的 PIBBSS）成立内部研究部门 PIRAMID，赌注是：可解释性目前缺的不是更多探针，而是科学基础。他们的反直觉点在于拒绝预设分析单元——不认神经元、SAE 特征、核、电路里的任何一个是"基本粒子"，而是要"找出现有理论在哪里崩掉"，再去发现更好的理论对象。他们主张网络里存在"结构性相关的随机性"，统计物理提供的正是形式化并追踪这种随机性的语言；不能对随机性给出有原则说法的工具，"不太可能是忠实的（faithful）"。

另一层反直觉：他们对自家旗号里的"ambitious interpretability"（完全逆向工程一个 AI 系统）明确降级——"既非必要也非充分"，只当作可扩展对齐所需的那种忠实机制透明度的代理指标。

三条线三个 lead：学习理论（Dmitry Vaintrob）、可解释性应用（Andrew Mack）、数据模型与验证方法（Ari Brill）。分别对应"造理论 / 造工具 / 造能验证前两者的合成数据基准"。

可证伪的近期目标（原文措辞）：理论组要在"接下来几个月内"做出一个 end-to-end toy-to-real 案例，让"一个有理论动机的统计量预测并解释泛化或能力相关的变化"；数据组要在一年内把合成数据集"变成一个公开基准，其忠实性保证强于当前评测实践"。

最硬的一项已发产出：arXiv 2607.20652（07-22）——ParityTransformer / Deep Parity Bottlenecks。用"无参数的代数字典"替换学出来的字典，给出确定性的 incoherence 保证并消掉了让逐层可解释瓶颈无法规模化的显存开销；论文称其特征"原生于实际计算，而非分析的产物"，在 feature absorption、steering effectiveness、细粒度因果干预上优于事后 SAE。

对现状的直接开火：「Mechanistic interpretability currently lacks rigorous benchmarks for validating interpretability tools」；「A faithful explanation must track the mechanism the model actually learns and uses, not just correlate with behavior」。

## 可以怎么用

- 判断一个「可解释性工具/方法」是否靠谱，可以用它的思路——先造一个自己已经知道正确答案的小任务，让模型去学，再拿解释工具倒推，看能不能把已知答案找回来；找不回来就说明这工具在编故事而非真的忠实。
- 这个「已知答案反向验证」的框架不局限于机制可解释性，任何号称能「解释模型为什么这么做」的工具（包括提示词层面的 CoT 解释、归因分析），都可以先用一个已知真相的合成场景测一遍再采信。
- 「不预设分析单元、先找现有理论在哪里崩掉」这个态度，也可以用来提醒自己不要过早锁定一个解释框架，遇到解释和实际行为对不上时，优先怀疑框架本身而不是硬凑。
