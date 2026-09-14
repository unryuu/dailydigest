# 「找到数学奇点比做完普通工作更容易」与 Navier－Stokes 争议

- 推荐强度: 弱
- 档位线索: 目前只够无牌，不能把「OpenAI 已解决 Navier－Stokes 千禧年难题」当作已核实事实。roon 的一句话适合作为观察或梗，但本身没有新闻增量；LessWrong 材料能证明有人作出这一宣称、且围绕模型能力与人工介入发生争议，却没有给出原始证明、精确命题或独立验收。若后续拿到 OpenAI 原文、论文与数学界审查结果，才有升档空间。
- 涉及文章: [finding the navier stokes singularity is in some sense much easier than doing your job end to end](https://x.com/tszzl/status/2099044526879101392) · roon／X · 2026-09-13
- 涉及文章: [OpenAI have solved the Navier-Stokes Problem with a substantially more powerful model than Astra.](https://www.lesswrong.com/posts/yekQKwmQJNk7thDtQ/openai-have-solved-the-navier-stokes-problem-with-a) · fluxxrider／LessWrong · 2026-09-08

## 核心主张

roon 只写了一句「在某种意义上，找到 Navier－Stokes 奇点比端到端完成你的工作容易得多」，语气和信息量都更像借热点提出的反直觉玩笑：形式明确、可验证的超难数学目标，可能反而比边界模糊、环节繁多的真实工作更适合模型。它没有说明谁找到了奇点、解决了哪个精确命题，也没有提供证据。

LessWrong 链接帖则直接用标题宣称 OpenAI 以一个「明显强于 Astra」的模型解决了 Navier－Stokes 问题，但正文只有通往 OpenAI 页面的一条链接；本地材料实际可读的内容主要是评论区及评论者转述。这里能够确认的是一项重大宣称及其争议，不能确认 Clay 千禧年难题已经被数学界认可为解决；评论还在 Navier－Stokes、Euler、受迫／无受迫情形和「反例」之间切换，本地文本不足以还原最终定理的精确范围。

## 为什么值得看（钩子）

真正反直觉的点不是「AI 会做数学」本身，而是一个可能动用模型群、巨量算力和整支人类团队的窄任务，被压缩成了「模型几分钟解决开放问题」的能力叙事。这能提醒读者区分模型的瞬时解题表现与整套研究工程，更适合留作专题证据，而不是今天单独报成已解决数学难题。

## 关键细节 / 引述

- roon 的原文只有一句：「finding the navier stokes singularity is in some sense much easier than doing your job end to end」。截至抓取时显示 77.7K 次浏览，但没有论证、链接或模型名称。
- LessWrong 帖子的标题称模型「substantially more powerful than Astra」，而评论者从 OpenAI「How we found the proof」一节摘出的说法是：自 8 月 28 日起训练一个新的内部模型，该模型在包括数学在内的基准上表现「unprecedented」，且训练仍在继续。材料没有给出这个模型的正式名称，所以不能把它写成 Astra；Astra 只在评论中被说成后来用于形式化证明。
- 评论者转引 OpenAI 的披露称：「研究者和 agents 在对方公开前没有通过任何方式看到 Levent Alpöge 与 Tristan Buckmaster 的工作」，但同时承认「不能排除由他们使用 OpenAI 产品而来的去标识数据帮助改进了模型」。这只是本地评论中保留的引文，未在本组材料里由 OpenAI 原页复核。
- 关于人类介入，Thane Ruthenis 的评论转述另一段说法：Levent 起初被告知只用了「very little human input」，后来通话中却得知有整支团队参与，先让模型做较容易的 Euler 问题，甚至展示给他的提示词也是通过提示 Codex 写出的。此处是评论中的二手指控，不能写成定论。
- 关于算力，同一段二手转述只说用了「an insane amount of compute」；另一名评论者概括为对 agent swarm 投入大量算力。材料没有 GPU 数量、token、并发规模、成本或运行时长，因此只能确认存在「巨量算力」的争议性描述，不能量化。
- OpenAI 员工 leogao 在评论中说，他没有 Navier－Stokes 的特权信息，但可以确认 Noam Brown 所述的内部感受属实：不少 OpenAI 人员看到新模型迅速解决他们研究多年的开放问题时感到震惊。它支持「内部认为模型能力出现跃升」，仍不是对这份具体数学证明的独立验收。

## 与近期的关系

组内重复风险高：roon 的一句话完全依赖同一场 Navier－Stokes 事件，没有独立事实，若主新闻已写 OpenAI 新模型、数学 benchmark 或高算力推进研究，就不该再拆成一条。它也与「实验室嘴上减速、实际继续训练更强内部模型」高度重叠，但本组材料只能证明训练持续、模型表现宣称和围绕算力／人工介入的争议，不能单独证明实验室违反了某项减速承诺。由于任务限定只读两份材料，无法据此核对往期日报是否已经报道过同一事件。
