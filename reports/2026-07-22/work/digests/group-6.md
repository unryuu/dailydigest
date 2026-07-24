# 深度长文 · 两条银牌（独立两篇）

---

## 银 A：Interconnects《Kimi K3: The open-weights escalation》

- 推荐强度: 强
- 档位线索: 银牌成立。K3 发布本身已连报多天，但这篇是目前对"开源升级"最系统的一手分析（Lambert 本人是开源模型阵营核心写手），观点增量足够撑银；不建议升金——本质是评论文，不是新事实。
- 涉及文章: [Kimi K3: The Open-Weights Escalation](https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation) · Interconnects (Nathan Lambert) · 2026-07

### 核心主张
"Escalation" 指的不是 K3 性能本身，而是**能力 + 政策承诺同时升级**：中国实验室证明了能做出前沿级模型，且开源不再是权宜之计而是国家级战略（习近平在 WAIC 主旨演讲中明确把中国 AI 生态的未来押在开源和全球扩散上）。Lambert 给出的硬测量：开源对闭源（或中对美）的能力差距，从此前争论的 6–9 个月压缩到 **3–5 个月**。分水岭意义：前沿开源模型的风险从"假设"变成"已部署的现实"。

### 为什么值得看（钩子）
Lambert 接过 Dean Ball 的反直觉论断——**开源模型本质上是"减速主义"的**：它压垮闭源实验室的利润率 → 减少可再投入的利润 + 压低估值 → 拖慢整个前沿投资和 capex 节奏。所谓"加速主义者"为开源欢呼其实是站反了，而 Lambert 认为这个减速**对社会是净好事**（分散权力、争取时间）。

### 关键细节 / 引述
- 排位事实：K3 在 Vals AI 排 #2、Artificial Analysis 排 #3，Frontend Code Arena 排 #1；文中前沿排序为 Anthropic > OpenAI > **Moonshot（开源）** > Grok，GLM 5.2（开源）也进前五。2.8T 参数 MoE，896 专家激活 16 个，对 K2 缩放效率提升 2.5 倍。
- 反蒸馏叙事："If adversarial distillation from the closed frontier models in the U.S. contributed, it is at most to a relatively small degree"——那些从"蒸馏恐慌"得出中国只靠偷 IP 结论的人 "are in for an awakening"。
- 资本效率论：中国实验室融资比美国生态少几个数量级（Anthropic 光数据预算就是十亿美元级），且推理需求小 → 更多算力可用于训练；"追赶式训练"比"发明下一个范式"便宜，学生可以超过老师。
- 最扎眼的私货：**"I think that if Claude Mythos was released as an open-weight model today, the negative outcomes would be relatively minor… The risks have been over-hyped."**（他自己承认这个观点难拿，公开网络安全评估很有限，但坚持。）
- 政策警告：重手监管开源只会造成虚假安全感 + 美国陷入不对称——美国最好的模型带网安护栏，而全球攻击者拿着中国开源模型探美国的防御。"Banning open-weight models…makes the ecosystem less safe in the short-term."
- 需求侧证据：Moonshot 因需求过载暂停了 K3 新订阅（API 未停）。
- 概率更新句："K3 should increase most people's probability that China can outright lead in AI capabilities in the near future on the back of more efficient training efforts."

### 与近期的关系
K3 发布及榜单表现本日报已连报多天，此篇的增量全在论证层：差距量化（3–5 个月）、"开源=减速主义"框架、蒸馏叙事翻案、监管不对称警告。digest 建议只取观点增量，不复述 K3 规格。

---

## 银 B：Zvi《Demis Hassabis on the New Coming Age》

- 推荐强度: 强
- 档位线索: 银牌成立，且 Part 2 的 Turner 辞职内幕比 Part 1 的框架文更硬——如果日报想突出"瓜"，这条甚至有金牌讨论价值（DeepMind 撕毁 2018 承诺 + 员工集体抗议 + 高层不作为，全是新事实）；Hassabis 框架文本身则偏"表态文"，单独撑不起金。
- 涉及文章: [Demis Hassabis on the New Coming Age](https://www.lesswrong.com/posts/3RfJLcmkztSTq9afc/demis-hassabis-on-the-new-coming-age) · LessWrong (Zvi Mowshowitz) · 2026-07

### 核心主张
两层内容。**Part 1**：Hassabis 发新框架文，把 AGI 比作电与火、"10 倍工业革命 × 10 倍速度"，提议在美国政府内建一个仿 FINRA 的"前沿 AI 标准机构"，必要时可协调各前沿实验室**共同减速**。Zvi 的总评是 "the least you could do"：方向对但严重不足——不点名任何具体下行风险（专家分歧从 ~5% 到 ≥50% 灾难概率，他一笔带过）、FINRA 模式有监管俘获风险且缺 SEC 式对应监督、只管已发布模型而**内部部署才是风险大头**、自愿机制能否真正执行减速存疑。**Part 2**：用 Alex Turner 辞职事件当场打脸——Hassabis 嘴上讲治理，自家承诺正在被撕毁。

### 为什么值得看（钩子）
同一篇文章里，Hassabis 前脚呼吁"必要时协调减速"，后脚被曝光：员工直接私信他阻止军方合同，他把人推给两个政策僚属，提案被晾到合同签署。"Trust instead of governance. The Pentagon contract is the litmus test of that bet."——赌输了。

### 关键细节 / 引述（Turner 瓜·已核实）
- **完整事实链**：Google 与 Department of War（五角大楼）签了 **"all lawful use"** 合同——政府可在一切合法用途上使用 Google AI 模型，对自主武器（killer robots）和大规模监控**无任何限制**。这直接违背 2018 年 DeepMind 及其高层（含 Hassabis、Jeff Dean）签署的致命性自主武器承诺（"neither participate in nor support the development…or use of lethal autonomous weapons"）。Turner 试图阻止签约，失败，随即辞职。
- Turner 辞职前的动作：组织了给首席科学家 Jeff Dean 的请愿（**250+ DeepMind 员工签名**；另有 600+ 员工签公开信反对合同）；直接私信 Hassabis 提交提案。Turner 原话：**"I don't think he used his leverage. I think he could have stopped the deal but didn't. As a last attempt, I directly messaged Google DeepMind's CEO, Demis Hassabis. He told me to send my proposal to two senior policy staff. They let the proposal wilt unattended until Google signed the deal."**
- Turner 对领导层的三选一指控：诚实的路只有解释清楚、公开放弃承诺、或辞职——**"Silence isn't one of them."** 另一句："Pledges of conscience often vaporize on contact with power."（还有一句 "What hurt most was watching AI ethics leaders do nothing."）
- 时间线（文中引 Andreas Kirsch）：2014 独立伦理委员会成立 → 2015 名存实亡 → 2018 AI 原则排除武器与监控 → 2025 该排除条款被删 → 2026 五角大楼合同签署。领导层同时宣称 "nothing's changed about our principles"。
- Zvi 的态度：称 Turner 的努力 "heroic"；明确点 Hassabis "blameworthy"（因坚称原则未变）；特意说不要把火力集中在 Jeff Dean 身上（Dean 至少答应了签支持 Anthropic 的 amicus brief，比什么都不做的人强）。结语："Demis Hassabis is to be applauded for his statement, but calls on others to do things, without any consequences following, risks becoming only cheap talk."
- 核实说明：Turner 引语经两次独立抓取交叉一致；"tried and failed to prevent" 的完整版即上述——**他试图阻止 Google 与军方签无限制用途合同，动用了请愿 + 直通 CEO 两条路，均失败，合同签署后辞职**。摘要未见截断遗漏的其他内情。

### 与近期的关系
Hassabis 框架文若前几日已有快讯报过，则 Part 1 是旧事深评；Turner 辞职瓜为本篇独有新事实，无重复风险。
