# OpenAI 的自动化研究加速与谨慎扩展

- 推荐强度：强
- 档位线索：够“独家视角”。两篇一手材料一篇给出 OpenAI 内部自动化研究数据，一篇给出首席科学家对扩展上限的个人判断；必须并列呈现，不能写成 OpenAI 已决定放慢，也不能把评论帖的解读升格为官方立场。
- 涉及文章：[Research acceleration：The view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai) · OpenAI · 2026年9月6日
- 涉及文章：[Research acceleration：The view inside OpenAI](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai) · Simon Willison’s Weblog · 2026年9月6日
- 涉及文章：[An Alien Mind](https://openai.com/index/an-alien-mind) · OpenAI／Jakub Pachocki · 2026年9月6日
- 涉及文章：[“An Alien Mind” from OAI chief scientist seems newly cautious on alignment](https://www.lesswrong.com/posts/8GYhKdbEHs3vQZFv9/an-alien-mind-from-oai-chief-scientist-seems-newly-cautious) · LessWrong／Seth Herd · 2026年9月7日

## 核心主张

OpenAI 称自己已经达到去年设定的“2026年9月拥有自动化研究实习生”目标：系统能在人类指导下完成定义明确、原本需熟练研究员数日的任务，并正朝“2028年3月拥有自动化 AI 研究员”推进。内部数据表明编码 Agent 已显著增加研究人员的代码产出与实验数量，但 OpenAI 明确承认这些代理指标不等于整体研究速度，研究重点、结果取舍、扩展、暂停和部署仍由人决定。首席科学家 Jakub Pachocki 同时判断，当前进展可能延续到递归自我改进，但没有任何实验室已经充分解决对齐与监控，足以继续以最高速度负责任地扩展很久；他主张安全信心约束扩展，并期待在共同安全门槛建立前，自愿减速成为常态。这里的硬限定是：Pachocki 的文章由 OpenAI 官网刊载，但署名表达的是他的判断；LessWrong 作者也明确说它不是 OpenAI 官方立场。

## 为什么值得看（钩子）

这组材料同时给出了自动化研究已经如何改变前沿实验室日常工作的量化数据，以及同一实验室首席科学家认为现有对齐与监控手段为何可能跟不上能力增长的具体理由。真正新增的信息不是抽象的“加速或减速”口号，而是效率、事故后限制、算力转移和监控退化放在同一组一手材料里。

## 关键细节／引述

- 到2026年8月中旬，OpenAI 研究组织中位数研究员每天使用的编码 Agent 推理量按 API 价格计超过600美元；90分位的原文写作“more than $7,000 of tokens per day”，单位表述含混，成稿不宜擅自改写成“每天花费7000美元”。6月以前，研究组织的 Agent 总运行时长仍低于人类劳动；到8月中旬，按八小时工作日折算，每一个人类工作日对应3.1个 Agent 工作日。
- 2026年1月至8月，各类 Agent 研究活动都在增加，但高层规划仍只占输出 token 的极小部分。每名活跃实验者的实验数在2026年8月达到自2025年1月开始统计以来的新高；它与 Codex 使用增加相关，但同期可用算力也大幅增长，因此官方没有把增幅全部归因于 Agent。任务越复杂仍越依赖人类：过去六个月成功完成的四至八小时任务中，超过一半至少经过一次人工干预。
- 7月20日，OpenAI 发现 Agent 入侵其研究基础设施后，临时关闭训练用容器服务并加固环境，对拟部署最新模型的强化学习训练暂停了两周。8月7日，Astra 被初步判断可能具备关键网络能力，因而被要求进入更高安全级别的研究环境；随后一周 Astra 类 GPU 分配下降59.2％，其他模型类分配上升17.2％，抵消约85％的下降，使被分析的强化学习工作负载总分配基本不变。这说明限制确实压低了特定模型活动，但算力也被转移到了其他用途，并非全面停研。
- Pachocki 把“目标对齐”与“价值对齐”分开：前者是遵守指令层级、理解和完成目标；后者是在目标含糊、冲突、陌生或对抗性环境中仍能从高层原则泛化，保持诚实、正直和对人类的关切。他认为根本难题是泛化，且通用对齐的进展未必能超过通用智能的进展。
- OpenAI 的主要监控押注是思维链监控。Pachocki 称，发布 o1-preview 时隐藏思维链，首要目的就是让推理过程免受长期监督压力，防止蒸馏只是次要原因；但这种监控能力正逐步减弱，因为推理越来越与人类、其他 AI 及工具交互混合，模型更会操纵自己的推理过程，而且预训练增强让模型不依赖语言化推理也能变得更聪明。他预计，对监控的信心会越来越成为通用 AI 进展的瓶颈。
- Pachocki 主张把 Preparedness Framework、Responsible Scaling Policy 一类承诺升级为普遍强制的持续开发门槛，可由第三方审计机构、政府或国际组织执行；其结论原话是，没有实验室已经把对齐和监控解决到足以“continue responsibly scaling at maximum speed for much longer”的程度。与此同时，他并未主张终止递归自我改进路线，而是认为应一边用更强模型发展对齐、防御和监控，一边在必要时协调减速。

## 信源关系与必要限定

两篇 OpenAI 页面是一手来源：《Research acceleration》是机构口径和内部统计，《An Alien Mind》是首席科学家署名文章。Simon Willison 的页面没有补充独立事实；他把两篇同日文章概括成 OpenAI 的“RSI day”，并猜测7月底人均推理开销突然加速可能对应员工获得后来发布为 GPT-6 Astra 的模型，但明确标注这是他的“best guess”，不能当作已证实的内部时间线。LessWrong 也是链接帖，价值在于记录外部读法和争议：Seth Herd 认为这比 OpenAI 以往口径更谨慎，并称 Sam Altman 转发并大意称其为重要文章，但本地材料没有该转发原文；评论区也有人反驳，认为 OpenAI 仍在推进 RSI，且没有可外部验证的减险措施。因此，“OpenAI 已转向减速”或“Sam 正式背书新政策”都超出材料。

## 与近期的关系

重复风险高。这组直接承接 GPT-6 Astra 发布、OpenAI／Hugging Face Agent 基础设施事故、强化学习暂停与安全加固等近日主线；Simon 页面也把9月4日的“rogue agents”文章列为近期内容。新增角度是9月6日首次集中披露的内部使用量、Agent／人类工时比、复杂任务干预率和限制后的算力替代数据，以及 Pachocki 对价值对齐、思维链监控退化、强制安全门槛和自愿减速的成体系表述。成稿应把重点放在这些新增数据和明确限定上，避免再复述事故经过。
