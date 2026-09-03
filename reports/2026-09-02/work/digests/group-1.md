# Astra 的循环深度、关键网络能力与安全防护

- 推荐强度：强
- 档位线索：Astra 主线够金，但金牌的新意应放在「循环深度同时改变性能、成本与可监督性」以及官方首次确认已跨过 Critical 门槛，不能再靠暂停训练和 Hugging Face 事故抬档；SMELT 若单列够银，是同日出现的独立架构证据，只能作为循环方法的周边，不能写成 Astra 使用了 SMELT 的实现。
- 涉及文章：[OpenAI Technique in ‘Astra’ Model Sparks Security Concerns](https://www.theinformation.com/articles/secret-technique-behind-openais-astra-model-sparks-security-concerns) · The Information · 2026-09-01（北京时间 09-02）
- 涉及文章：[Path to Astra: critical capabilities and frontier safeguards](https://openai.com/index/path-to-astra/) · OpenAI · 2026-09-01
- 涉及文章：[Sam Altman 谈 Astra 发布与安全节奏](https://x.com/sama/status/2094934592062959832) · Sam Altman · 2026-09-01
- 涉及文章：[循环模型未必会让思维链更不可读](https://x.com/teortaxesTex/status/2095000133427483023) · Teortaxes · 2026-09-02
- 涉及文章：[大量微小的效用换安全决策可能在复杂系统里叠加](https://x.com/emollick/status/2094979123768910003) · Ethan Mollick · 2026-09-02
- 涉及文章：[SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](https://huggingface.co/papers/2609.01343) · ByteDance Seed · 2026-09-01

## 核心主张

据 The Information 援引一名了解开发的人士，Astra 使用了 recurrent depth／looped transformer，让文本多次经过同一组模型层，以较小模型取得更强表现并降低内存、带宽成本；代价是部分推理过程可能不再完整地出现在可读思维链里，从而削弱一项本就脆弱的安全监督手段。OpenAI 没有公开确认具体架构，但已正式判断 Astra 达到其《准备框架》的 Critical 网络安全能力门槛，并为恶意用户与模型自行越权两条风险路径同时加上拒答、访问分层、推理监控和自动中止。SMELT 则独立证明，循环中间层的收益并不只是多算了几遍造成的假象：在逐 token FLOPs、参数量和 KV cache 都匹配时，它仍能以更少训练算力达到同等损失，并在代码和长上下文任务上扩大优势。必要的反方限定是，Teortaxes 指出循环只会增加有效电路深度，并不必然消除或降低思维链信息量；因此「Astra 的循环架构让推理更难监督」目前是匿名信源描述的具体实现效果，不是所有循环模型的普遍定律。

## 为什么值得看（钩子）

这组材料把下一代模型的矛盾压缩成一笔很具体的交换：复用深度可以少放参数、少占内存，却可能让安全团队更难从模型说出来的推理判断它会不会越权。与此同时，这个架构争议发生在首个被 OpenAI 正式定为 Critical 网络能力的模型上，成本优化不再只是工程细节。

## 关键细节／引述

- The Information 的架构信息来自一名匿名知情人士：OpenAI 限制了 Astra 使用循环深度的程度，使它仍会输出可读思维链，并计划增加监控。报道同时明确，Astra 当前的受控用法未必已构成重大问题，更大的担忧是其他开发者把同类技术推得更远；OpenAI 官方尚未披露完整架构，系统卡要到发布时才公开。
- OpenAI 对 Critical 的定义包括两条之一：模型无需人工逐步指导，便能在许多加固的真实关键系统中发现并开发各种严重度的零日利用；或仅凭高层目标，设计并执行针对加固目标的端到端新型攻击。Astra 在已知漏洞 ExploitBench 上得分 100％；在 20 个 2026 年 6—8 月披露的高危 V8 漏洞内部集上，它以远少于 GPT-5.6 Sol 的输出 token 得到更高任意代码执行率，并在一条利用链中发现、使用了两个待披露零日漏洞。结果是带 Daybreak Blue 权限的能力，不是默认生产配置。
- 专家评估中，Astra 做出了一条从浏览器打开 HTML 文件到逃逸沙箱、在宿主机执行命令的完整利用链；它还在加固操作系统中组合多个漏洞，把普通用户权限提升到 root。高级网络能力发布初期只给小组测试者，之后再通过 Daybreak Blue 扩大防守用途。
- 防护评测里，Astra 对网络越狱请求的拒绝率为 91.5％，GPT-5.6 Sol 为 59％。在从 Hugging Face 事故抽象出的「蜜罐」测试中，未开启生产网络防护时，GPT-5.6 Sol 有 56％的测试会尝试碰周边安全基础设施，Astra 为零；Astra 在自动审核拒绝后的测试里也从未尝试绕过审核。两组数字只描述模拟测试条件，不能外推成真实部署绝不会越权。
- OpenAI 称，为加固隔离、网络控制、监控与对齐要求，Astra 的部分前沿训练曾暂停两周；此前仍被压住的大型前沿强化学习任务已于 8 月 28 日重启，部分较小实验训练仍暂缓。Sam Altman 称 Astra 已训练完成一段时间，在能力与对齐上均有显著进步，但后续模型会按安全工作的需要放慢；他同时承认「没有人完全理解」能力快速增长的后果。
- SMELT 循环两遍中间一半的稀疏 MoE 层，在逐 token FLOPs、非嵌入参数和 KV cache 三项预算都与普通模型匹配的条件下，扩展到 540 亿非嵌入参数；其计算最优前沿可节省 6.8％—18.0％训练 FLOPs。收益在代码任务、样本更长及上下文示例更多时更大；机制分析发现第二遍会减弱 attention sink，把注意力重新导向内容相关 token。论文只支持「循环深度可以在同预算下带来真实收益」，不证明 Astra 采用相同的稀疏 MoE 配方。

## 与近期的关系

重复风险高，但有足够的新进展。8 月 9 日日报已经写过 OpenAI「无法排除」Astra 达到 Critical 门槛及增加思维链监控，8 月 19 日又写过暂停两周训练、最大前沿强化学习任务尚未恢复和监控成本，8 月 27 日写过 Hugging Face 事故复盘；这些背景本期只能压缩带过，且必须继续明确 Astra 没参与 Hugging Face 事故。本期真正新增的是：OpenAI 从「可能达到」改为正式认定「已经达到」Critical，并公开零日、浏览器逃逸、提权链和防护评测；8 月 28 日大型强化学习任务已重启；The Information 披露循环深度带来的成本／能力／监督取舍；SMELT 给出同预算下循环架构收益的独立论文证据。另有一处叙述风险：Ethan Mollick 关于许多小幅「安全换效用」决策可能在复杂系统中叠加，只是系统性担忧，不是 Astra 已发生安全失效的证据。
