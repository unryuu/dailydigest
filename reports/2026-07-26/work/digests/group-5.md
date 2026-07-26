# Claude Design 作者自述工作流：先想清楚再提示，最后一公里手动改

- 推荐强度: 弱
- 档位线索: **该丢**。内容本身不算空——有一份 10 条的实操清单，比预期的软文实在——但这是 **07-25 已经带回并明确丢弃过的同一篇文章**（同 URL，见 `reports/2026-07-25/report.md` 丢弃行「claude-blog 的 Design 案例与四项认证」）。若调度坚持要留，只可能是「实用清单」角度的银，不可能到金；本 reader 建议维持昨天的判断，直接丢。
- 涉及文章: [How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) · claude.com/blog · 2026-07-24

## 核心主张

Anthropic 产品设计师 Nate Parrott 自述 Claude Design 的由来与用法。起因是 2025 年秋他在 Claude Code for VS Code 做唯一设计师，Opus 4.5 上线后工程师出活速度暴涨，他跟不上，于是找提效办法。第一次尝试（把终端输出和截图丢给 Claude 说「你来设计」）失败；转机是发现 Claude 对 HTML 极强，于是把 HTML 当成一种可交互的视觉媒介（幻灯片、视频、PDF 能做的，网页都能做），配上左聊天右预览的分屏。文章的实质价值不在产品故事，而在末尾 10 条操作规范。

最硬的一条判断是产品分工：**Claude Code 管上线代码，Claude Design 管上线之前的部分**——早期构思、对齐、在有人动手之前拿到方向上的认可。作者的引申是「随着模型越来越会写生产代码，真正要紧的工作往前挪了」。

## 为什么值得看（钩子）

一个官方博客罕见地把「怎么用」写成了可执行清单，其中「直接编辑不烧 token」「先想清楚再提示」两条对任何 agent 使用者都成立。但它昨天已经被我们看过并丢掉了。

## 关键细节 / 引述

- **10 条最佳实践**里真正可复用的几条：①「Do the thinking before you prompt.」——他在离开电脑时把需求想好，用手机备忘录打字、散步时录语音、或在工具里按语音键口述，坐下时只负责执行；④「先要十个方案再混合」，原话示范是「I like option B and a little of option D. Give me five riffs that smoosh those together」；⑧「最后一公里手动做」——挪位置、删、改字、调大小、换颜色用直接编辑工具，**直接编辑不消耗 token**，而且对齐尺寸这种活儿本来就该靠眼睛；⑦ 不在乎精度时先出线框图，快且能逼 Claude 关注结构而非视觉。
- **不给方向它就会犯老毛病**：第②条明说「Left undirected, Claude picks one of its favorite aesthetics. You'd probably recognize them.」——官方自己承认模型有一眼可辨的审美惯性，解法是指定字体配色、给 moodboard，或让它先提配色方案来回挑。
- **上下文接入的具体做法**：连 GitHub，Claude 会抓现有组件和已有页面当起点，「几次尝试就能相当高保真地复现你现有的设计」；Web search 和 MCP 在 Claude Design 里同样可用。上传 logo、旧幻灯片、截图、字体规范，它会分析后生成一套设计系统。
- **一个反常识的产出方式**：开屏动画不是直接生成的——「我不是动画师，所以我先让 Claude Design 给我做了一个专用视频编辑器，再用那个编辑器做动画」。作者最喜欢的产物都是不进现成分类的东西：带交互模拟的文档、会说话的幻灯片、既是图又是视频的图表、「本身就是自己编辑器的设计」。
- **明确的能力边界**（少见的官方自曝短板）：没有图像模型，不适合做 logo，「但这没挡住人们去试」；要上线的软件请回 Claude Code。两边可双向同步。
- **产品状态**：Claude Design 现为 beta，覆盖 Pro / Max / Team / Enterprise。文中提到 Opus 5 读图表、示意图、截图的能力强于以往 Opus，与 Claude Design 配合适合做成稿级的 deck 和 memo。
- 收尾引了 Bret Victor 的《Stop Drawing Dead Fish》，取其一句：一切画出来的东西都该是活的。

## 与近期的关系

**重复风险极高，且是最硬的一种重复**：同一 URL 在 07-25 已随 claude-blog 三连（Opus 5 发布配套）带进精读，当期结论是丢弃。今天再次上桌只是因为信源规矩「claude-blog 有新内容一律进精读」，不是因为出现了新事实——文章日期仍是 2026-07-24，内容未变。

另有两处与既有牌面相撞：Opus 5 是 07-25 的金牌（Anthropic 发布 Claude Opus 5），本文只是顺带提一句其视觉能力，构不成新料；「上下文工程新规矩」那篇同属 07-25 那组，方法论位置也被占过。
