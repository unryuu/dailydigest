# 白宫给开放权重划新线：蒸馏分两类，只打「工业级窃密」不动开放权重；当天下午 25 家巨头联名要「手术刀」

- 推荐强度: 强
- 档位线索: **银**（与定牌判断一致，不建议升金）。理由：两条都是真新闻、都有具名官员和成文引语，但**没有任何东西落到纸面**——没有行政令、没有规则、没有时间表，全部载体是 X 帖子和一封没有法律效力的联名信。够银不够金。真正把它撑到银的是两个硬点：① Bessent 首次把「制裁 + 实体清单」明确说出口（此前只是 Axios 报道「在考虑」）；② OpenAI 和 Anthropic 拒签联名信。
- 涉及文章:
  - [White House draws new AI line on China](https://www.axios.com/2026/07/24/white-house-ai-line-china) · Axios · 2026-07-24 09:15 UTC
  - [Nvidia, Microsoft, Meta warn against 'premature restrictions' of open-weight models](https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html) · CNBC（记者 Ashley Capoot） · 2026-07-24 10:15 EDT 发布 / 13:55 EDT 更新

> **抓取说明**：两个域名直连均 403，改走 r.jina.ai 阅读器代理取到全文。Axios 全文结构完整（从导语到 "What we're watching" 收尾），CNBC 正文完整。均非节选、非软墙截断。
>
> **时序注意**：Axios 这篇（09:15 UTC ≈ 05:15 EDT）**早于**联名信发布（10:15 EDT）约 5 小时，所以 Axios 文中完全没有提到这封信。两篇是「上午政府侧 → 上午晚些产业侧」的同日先后，不是互相引用。

## 核心主张

白宫这周在开放权重问题上找到了一个「既要又要」的话术支点：**把蒸馏（distillation）切成两类**——正常的小规模/授权蒸馏是开放创新生态的正当组成部分，而「大规模、隐蔽的工业级蒸馏」是窃取美国技术，后者可以动制裁和实体清单。Axios 的判断（记者解读，非官方表述）是：这个区分让美国可以精确打击中国 AI 公司，而不必广泛限制企业、研究者、创业公司越来越依赖的开放权重模型本身。

同一天上午 10:15 EDT，Nvidia、Microsoft、Meta、Palantir 领衔的 25 家公司发出联名信，反对对开放权重模型施加「过早的限制」。信里没有点名白宫，但**有一段是直接对着 Kratsios 的蒸馏指控写的**：非法蒸馏应该用「针对性的法律和商业框架」处理，而不是对「在 AI 创新中扮演重要角色的技术」搞「一刀切限制」。这是把白宫的话术支点接过来，往自己这边再推一步。

## 为什么值得看（钩子）

政府和产业在同一天用了同一个逻辑（区分正当蒸馏和窃密蒸馏），但推向相反的落点——白宫是为了拿到动手的授权，产业是为了把动手的范围锁死在最小。另外一个反差：美英两国自己的 AI 安全机构 07-23 联合发布的 Kimi K3 网络能力评估，结论是「显著低于其他前沿模型」，等于政府的技术部门在给政治部门的紧张感泼冷水。

## 关键细节 / 引述

**政府侧（官员本人表态，均为 X 帖子或采访，无一份正式文件）**

- **Michael Kratsios，总统首席技术顾问（chief technology adviser to President Trump）**，周三（07-22）在 X 上指控 Moonshot 的 Kimi K3 是蒸馏 Anthropic 的 Fable 模型而来。原话两句合起来才是完整立场：「Legitimate AI distillation used to create smaller, more efficient models plays a vital role in this open innovation ecosystem」，但「large-scale, covert industrial distillation aimed at stealing proprietary U.S. technology and undermining American research is unacceptable」。
- **财长 Scott Bessent**，本周在 X 上把话说到了最明确的程度：「When PRC firms conduct covert, industrial-scale distillation attacks that cross the line into IP theft, sanctions and Entity List designations will be on the table.」（CNBC 另记：Bessent 周二 07-21 对 CNBC 说政府会调查中国公司是否窃取美国知识产权，政府「有能力因为这种窃取而制裁他们」。）
- **另外两位具名官员做了类似的知识产权窃取指控**：美国贸易代表 Jamieson Greer、国务院副国务卿 Jacob Helberg。四人（Kratsios / Bessent / Greer / Helberg）口径一致，是「立场」而非「个人发言」的证据。
- **落到纸面的：零**。没有行政令、没有规则、没有时间表。实体清单只是 Axios 此前独家报道政府「曾考虑过」（previously considered），Bessent 的措辞也是「will be on the table」——摆到桌上，不是拍下去。
- **唯一一份真正的政府文件方向相反**：英国 AI Security Institute 与美国 Center for AI Standards and Innovation 周四（07-23）发布 Kimi K3 网络能力联合评估，结论是该模型表现「显著低于其他前沿模型」。

**产业侧（07-24 联名信）**

- **一封信，不是各说各的**。25 家公司：Nvidia、Microsoft、Meta、Palantir + 20 多家。**CNBC 全文没有引用任何一家公司的高管以本公司名义单独发言**——三家巨头是签署方，不是发言人。黄仁勋和 Satya Nadella 各自在**个人社交账号**转发了这封信（黄的 X 帖 status/2080643682408321103，Nadella 的 status/2080646162483417097）。
- 信的核心措辞：反对「premature restrictions」，因为会「stifle competition or drive innovation overseas」；开放权重让技术红利「broadly shared rather than concentrated in a few hands」。
- 最硬的一句是反过来打闭源安全论：「Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk.」
- 对蒸馏指控的回应（未点名白宫）：非法蒸馏应通过「targeted legal and commercial frameworks」解决，而非对相关技术施加「sweeping restrictions」。
- 收尾定调：「Our AI leadership will be judged not by one frontier AI model, but by whether the United States builds a strong, open ecosystem that diffuses into every sector.」
- **OpenAI 和 Anthropic 都没签**。CNBC 把这条放进了 Key Points，并给了原因侧写：两家估值各近 1 万亿美元，都在冲 IPO，Anthropic 6 月已向 SEC 秘密递交招股书，OpenAI 几天后跟进。**Sam Altman 周五在 X 上表态支持但不签**：希望美国在开放权重和闭源两条路上都赢，「glad to see this」。
- **马斯克蹭了但没签**：在 X 上说这封信有他的「full support」，SpaceX 未正式签署。
- **OpenAI 总裁 Greg Brockman 的三句话（Axios/Bloomberg 各记一部分，值得单拎）**：① 周三对 Bloomberg 说，现在判断中国近期模型是否蒸馏自 GPT 系统「为时过早」；② 在纽约的记者简报会上对 Axios 说，他**从未与政府任何人讨论过封杀中国开放模型**；③ 被问蒸馏是技术问题还是政策问题时答「definitely a technical issue」，并说「having more models, more usage, that is a good thing」。一个闭源大厂的总裁在给这轮政策紧张降温。

## 与近期的关系

**明确回答派活方的问题：CNBC 这条不是 07-24 那波创业者联名的同一件事，是两封不同的信，隔了两天。**

| | 07-24 已报（Politico，07-22 上榜） | 本条（CNBC，07-24） |
|---|---|---|
| 签署方 | 近 200 家创业公司 | 25 家科技公司 |
| 代表谁 | Little Tech Association 牵头，YC 在列，小公司 | Nvidia / Microsoft / Meta / Palantir，在位巨头 |
| 动机 | 付不起美国闭源模型账单，靠便宜中国开源模型活着 | 生态与市场结构，反闭源集中化 |
| 主诉求 | 「要手术刀，不要大锤」 | 反对「过早限制」，非法蒸馏用「针对性法律与商业框架」处理 |

**新在哪**：① 签署主体从「买不起 token 的创业公司」换成了「卖芯片、卖云、发开源模型的在位巨头」——利益结构完全不同，前者是成本诉求，后者是生态和护城河诉求；② 这封信第一次把矛头对准闭源的安全叙事本身（「只依赖闭源模型本身并不安全」），而不只是喊别封杀；③ **OpenAI 和 Anthropic 缺席**是这轮最新的信息——美国两家最有理由害怕中国开放权重的前沿实验室，在两家都在冲 IPO 的节点上集体选择了不站队（Altman 只在 X 上口头点赞）。

其余重复度盘点：
- **Kratsios 蒸馏指控（07-22 X 帖）在 07-24 那期已作为背景写过**，本条如果复用需当旧料处理，不能当新事。
- **Bessent「要查中国公司盗用美国模型」这句 07-24 写过又被用户在终审时删掉**（见 `reports/2026-07-24/用户修改.md` 第 13 条：「删掉『政府端反而更硬：财长 Bessent 放话要查盗用』整句」）。**注意：本条里 Bessent 的新料不是「要查」，而是升级后的「sanctions and Entity List designations will be on the table」——这是明确点名工具箱，与被删的那句不是一个信息量级。但用户删过一次，写手落笔前值得留个心。**
- **07-22 报过的「黄仁勋：该怕的不是中国模型，是封杀它们的运动」** 与本条只是同一人同一立场的延续，本条里黄仁勋只是转发联名信、没有新发言，不构成新料。
- 未在近期报过、可作为本条新增量的：四位具名官员口径统一（Greer、Helberg 是新面孔）、UK AISI + US CAISI 的 Kimi K3 网络能力联合评估、OpenAI/Anthropic 拒签、Brockman 的三句降温表态。
