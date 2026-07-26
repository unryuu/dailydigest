# Debian 就「能不能用 LLM」开正式 GR：票上不是三个提案，是四个

- 推荐强度: 强
- 档位线索: 稳银，够到金的边。硬料密度足（四份提案原文措辞 + 一条宪法级的门槛不对称），但属治理新闻而非能力/产品突破；今日若有更大的模型或发布新闻，压银位；若是淡日，这条完全撑得起金。
- 涉及文章:
  - [General Resolution: LLM usage in Debian](https://www.debian.org/vote/2026/vote_002) · Debian 官方投票页 · 讨论期起始 2026-07-24，页面 Last Modified 2026-07-25 23:24 UTC
  - [LLM Usage in Debian: Three Proposals](https://news.ycombinator.com/item?id=49050859) · Hacker News · 2026-07-25 19:44 UTC，172 分 / 156 条评论（读时）

## 核心主张

Debian 把「项目里到底能不能用 LLM」推进了正式 GR 程序，官方页面现在挂着**四个**并列提案（A/B/C/D，HN 标题写「三个」是因为 D 在贴出后才加上）。四份措辞都不是「全面禁 / 有条件允许 / 只要求披露」这套常识三分法：**A 的「全面禁」明文把上游排除在外**，**C 的「反对 LLM」实际禁的是给人看的文字而不是代码**，**B 和 D 都写了披露要求，所以披露根本不是分歧点**。真正的分水岭在两处：一是拿什么文书载体落地（改社会契约 / 发一份可随时演进的立场声明 / 塞进行为准则带纪律处分 / 只是一份指南），二是由此带来的通过门槛差异。目前状态是「In Discussion」，官方页面上**没有任何投票日期，投票尚未开始**。

## 为什么值得看（钩子）

一个二十几年没怎么变过的项目，第一次把「AI 能不能碰我们的代码」写成宪法级动议；而且四份提案里最激进的那份，恰恰是唯一一份需要 3:1 超级多数才能过的——写法本身就决定了它最难赢。

## 关键细节 / 引述

- **门槛不对称（本组最硬的一点）**：提案 A 走的是「向社会契约新增第 6 条」的路子。Debian 宪法列明基础文件（Foundation Documents）只有社会契约与 DFSG 两份，且「A Foundation Document requires a 3:1 majority for its supersession」；而无明确超级多数要求的选项一律 1:1。B 更是自己写明是「Using its power under Constitution section 4.1 (5)」发布的立场声明，并且「That position may evolve as time passes without the need to resort to future general resolutions」。同一张票上，最严的选项要 3:1，另外三个只要 1:1。（最终由项目秘书裁定，页面上尚未标注超级多数要求。）
- **A（提案人 Matthias Geiger，8 位附议）的 scope 反常识**：禁的范围是「Debian source packages / lintian 这类原生软件 / Debian web 资源 / Debian 贡献者写的文档与翻译 / 官方对外沟通」，明确**不包括**「Upstream projects using LLMs for development」「AI-related software」「Upstream patches/security fixes etc.」。也就是说 A 通过后，用 LLM 写的上游代码照样进档案库。A 自己也承认执行不了：「While enforcement could be a challenge, this is a statement of intent by the Debian community, and we trust this community to adhere to it in good faith.」文末还特意声明本文「written by Matthias Geiger and Jesse Rhodes with input from Sledge and josch, organically and without language model assistance」。
- **A 的伦理段落在讲自己被打**：爬虫「effectively a large scale and perpetual Denial of Service attack」，导致「parts of our infrastructure were not reachable at all, and JS-based checks had to be enabled」——这是 Debian 自己基础设施的实际损失，不是泛泛的道德论。
- **C（提案人 Ian Jackson，8 位附议）最容易被误读**：标题是「Reject LLMs (generative "AI") as far as practical」，但正文直接承认「a complete ban on LLM output as part of Debian is currently impractical」。它真正的强制条款落在**人对人的文字**上：「messages to humans (including for example bug reports, mailing list messages, discussions on Salsa, and blog posts on Planet Debian) must be drafted solely by humans without LLM assistance」。另外三条硬要求：任何 LLM 使用必须披露；单个项目和维护者可以完全禁止（包括上游的禁令「must be respected」）；违反算行为准则违规，「should result in swift but proportionate disciplinary action」——四份提案里只有 C 带纪律处分。C 的措辞也是四份里火力最猛的：「generation and promulgation of bullshit」「ownership by horrible people and companies」「Ethical and safe use of this technology is almost impossible」。
- **C 第 8 条给非英语母语者留了门**：写不了英文的贡献者可以用母语写，让读者自己去用翻译工具，人写的英文摘要「would be very welcome but is not required」，并且「we promise not to shame anyone for any linguistic mistakes」。HN 上关于「A 会不会赶走非英语母语者」吵得很凶（alightsoul 那条），但吵的人多半没读到 C 这条。
- **D（提案人 Pierre-Elliott Bécue，6 位附议）把责任焊在「谁按下上传键」上**：开篇先撇清「Debian as a project does not endorse or recommend the use of generative AI assistants」，然后「Rather than banning their use, which seems counter-productive and unenforceable, the project chooses to place responsibility on contributors」。具体要求：提交者必须「able to explain and defend it」；Signed-off-by 和 GPG 签名必须**本人亲手打上**；进生产的内容必须由本人显式提交；生成内容要在 commit message / changelog 标注，但承认 Copilot 的 tab 补全这类「lightweight generative tools」可能贡献者自己都没意识到，所以「When in doubt, add such marking」。范围「apply exclusively to code and work done specifically for the Debian project ... They do not apply to any upstream work」。
- **B（提案人 Lucas Nussbaum，9 位附议，提案已两次修订）的六条最像成文合规**：工具条款不得与分发/修改/使用冲突；输出里若含第三方既有版权材料需先确认有权以开源许可提交；贡献者对技术价值、安全、许可合规「remains solely accountable」；重大部分由工具生成需向读者披露（建议用 `Generated-By:` 或 `Assisted-By:` 这类 Git trailer），覆盖代码、邮件列表帖、bug 讨论；批量或自主生成的贡献须比照 mass-bug filing 事先讨论；禁止把禁运安全报告等非公开信息喂给不受信任的云端工具。D 也有同款云端限制（「No cloud-based AI shall be used when the data transmitted could either be sensitive to the project ... or not public」）——**两个对立阵营在「别把禁运漏洞喂给云 AI」上是一致的**。
- **数附议人头会数错**：附议名单大量交叉——Pierre-Elliott Bécue 附议了全面禁的 A，自己又提了接受派的 D；Ian Jackson 附议了 A，自己又提了 C；Matthias Geiger 提了 A 又去附议 C；josch 同时附议 A 和 D。HN 上熟悉 Debian 流程的评论者 gsliepen 直接点破：「you can't really extrapolate from endorsers to all of the Debian Developers」，附议只是让选项进入选票，Debian 用的是排序投票，票上永远还有一个「further discussion」选项。B 的附议名单里有 Stefano Zacchiroli、Andreas Tille、Philipp Kern，D 的名单里有 Russ Allbery、Jonathan Carter、Gunnar Wolf。
- **HN 上最实的一处技术批评**（simonw）：A 的措辞「forbid any contributions ... written with the use or assistance of」按字面会把**由 LLM 协助发现漏洞的补丁**也排除掉，「That's clearly a bad policy, and they should update their wording to clarify that」。同一条线上多位评论者担心全面禁会拖慢安全补丁。
- **时间表（页面事实 + 宪法推算）**：官方 Time Line 一栏只有「Discussion Period: 2026-07-24」，无结束日、无投票日。宪法 A.1.1 规定讨论期最短 2 周、最长 3 周，新增或修改选项会把结束时间推到该动作后一周（但不突破上下限）；A.3 规定讨论期结束后秘书须在 7 天内发起投票。据此推算最早 2026-08-07 结束讨论、最迟 2026-08-14，投票再往后。**（此段起止日为按宪法条文推算，非官方公布；写进正文时须标明「尚未公布投票日期」。）**

## 与近期的关系

本仓 reports/ 里没有 Debian 或任何开源项目 AI 政策的历史报道，无重复。最近的擦边是 06-19 那期金牌「禁开源 AI 是个错误」（Nathan Lambert），但那条讲的是美国出口管制层面的开放权重政策，与项目内部治理不是一回事，不构成重叠，反而可以在正文里当一句「同一年里，开源世界在两个完全不同的层级上讨论 AI 边界」的呼应——不呼应也完全成立。属新事件首报。
