# AI 日报 · 2026-06-14（周日）

> 流水线：scout subagent 全量扫 15 源 → manifest → 2 个 reader subagent 并行精读 → reduce。
> 精读 2 条（金 1 / 银 1），雷达 3 条。中间产物见同目录 `manifest.json`、`digests/`。
> 防重复生效：Fable 主线连报三天，scout 只收到「停用为什么发生」的全新内幕，未炒旧料。

## 🥇 金牌 · 头条精读

### [Fable/Mythos 停用的政治内幕](https://thezvi.substack.com/p/american-government-takes-down-claude) · WSJ 独家（付费墙）+ Zvi 复盘 · 2026-06-13
**为什么值得看**：06-13 那条「政府勒令停用」今天爆出导火索——不是抽象的「国家安全」，而是 **Amazon CEO Andy Jassy 私下向财政部长 Bessent 等官员进言**，称 Amazon 研究员用 Fable 5 拿到「可用于网络攻击的信息」。
- **反转在身份**：Amazon 是 Anthropic 最大投资人之一（2026-04 追加 50 亿美元 + 承诺千亿云支出）兼云供应商——左手投钱、右手向政府递刀；最后连 AWS 自己也被这场它点燃的下线波及。「政府护国」被翻成「竞争对手拿监管当武器」。
- **旁证**：商务部长 Howard Lutnick 致信 Amodei，要求对「任何外国人」停用 Fable 5 / Mythos 5，Anthropic 索性全球下线（注：Lutnick 这条多数转述有、个别源只点 Bessent，口径有出入）。前白宫 AI 沙皇 David Sacks 给官方版叙事背书（「可信合作伙伴提交了越狱，Dario 拒绝修复/下线」），其「可信合作伙伴」指向与 WSJ 吻合。
- **Anthropic 重申**：引发担忧的能力别家公开模型同样有，审查后认定越狱只暴露「少量已知的、轻微的漏洞」。
- **Zvi 新视角**：行政动作技术上「不可执行且自伤」——若要「保证永不被越狱」物理上不可能；时机讽刺（「没有好政策在周五下午 5 点后才宣布」）；禁外国研究员类比「自 1955 年驱逐钱学森以来最大的反扩散失败」。
- ⚠️ 来源边界：WSJ 原文付费墙未读到，归 WSJ 的事实由 TechCrunch / TheNextWeb / The Information / Benzinga 等同日多源转述互证，已逐条区分 WSJ 转述 vs 旁证。
- 与近期关系：承接 06-13 头条但只写「动机层」新增量，不复述停用时间线/越狱细节/各方基本反应。

## 🥈 银牌 · 非头条精读

### [Results from the first Anthropic Public Record](https://www.anthropic.com/news/anthropic-public-record) · Anthropic（YouGov 调研，窗口 2025-11-01~12-11，近期发布）
**为什么值得看**：委托 YouGov 调研 51,993 名美国人（人口普查加权，误差 ±0.6pt）。一句话钉死它的是**希望与信任反向脱钩**：公众最盼 AI 治癌/阿尔茨海默（48% 头号期待），却最不信任 AI 公司——仅 15% 信任，所有受测机构里垫底（独立专家 43% / 联邦政府 20%）。且是 AI 公司自己掏钱测、自己公布的全行业垫底信任度。
- **希望端**：治病居首（48%）远超第二「帮助残障」（36%）；「心理治疗/缓解孤独」排最低——和「AI 陪伴」主流叙事拧着来。
- **恐惧端**：失业 64%（**每一个州**都是头号）、认知依赖 56%、错误信息 52%；「人拿 AI 作恶」排序高于「AI 失控变天网」——公众怕的是人。
- **越用越不怕**：日活用 AI 者怕失业 54% vs 从不用者 70%；认知依赖日活 46% vs 从不用 62%。恐惧来自不熟悉。
- **依赖悖论**：56% 担心依赖的人里只约 1/5 表示「AI 消失会显著影响生活」；反过来 44% 不担心的人里约 1/3 其实会受显著影响。
- **跨党派共识**：71% 要政府介入（民主党 79% / 共和党 68% / 独立 69%）；重度用户（仅 6% 人口）也 74% 支持监管，没被用成放松派。问责偏好：47% 要 AI 公司对危害负法律责任（最高项）。
- 角度：Anthropic 首份此类公共意见调研，全新数据；「厂商自曝信任垫底」是独立钩子。

## 雷达（terse）

- [英国警察被查：多起案件用 AI「伪造证据」](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661) · Hacker News（354 分）
- [AI coding at home without going broke](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/) · Hacker News（318 分）— 本地省钱编码实操
- [Publishing WASM wheels to PyPI for use with Pyodide](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/) · Simon Willison · 2026-06-13

---
## 运行健康
- scout 全量扫 15 源、0 抓取失败；精读短名单 2 组（group-1 中·Fable 停用政治内幕；group-2 轻·Anthropic 调研）→ 派 2 个 reader。
- 防重复奏效：Fable/Mythos 主线已连报三天，scout 按「最近主线只收新进展」只捞到 WSJ 的动机层内幕，未重收停用经过/越狱/能力评估。
- 定牌：金 1（停用政治内幕，瓜硬 + Zvi 治理骨架）、银 1（5.2 万人调研，反直觉数据 + 厂商自曝信任垫底）。
- reader 抓取边界（已诚实标注）：group-1 的 WSJ 原文付费墙未读到，核心事实靠 TechCrunch / The Information 等多源转述互证、逐条标注；Lutnick 致信一条个别源口径出入已记。group-2 全文读到。
- 权重应用：本期 scout 已按新 triage（有乐子加权 / 评测降权）分堆；HuggingFace FINAL-Bench Quantum（benchmark 稿）按降权未收；The Batch/OpenAI 仅企业/客户稿未收。
- 写入 / 更新 seen（reported=true 进报 / false 扫到未收）：
  - hacker-news +3：wsj-amazon-crackdown（金·源,true）、police-ai-create-evidence（雷达,true）、ai-coding-at-home（雷达,true）。
  - thezvi +1：american-government-takes-down-claude（金·源,true）。
  - anthropic +2：anthropic-public-record（银,true）、tcs-anthropic-partnership（false，合作稿）。
  - simon-willison +3：publishing-wasm-wheels（雷达,true）、luau-wasm（false）、sqlite-column-provenance（false）。
  - huggingface +1：FINAL-Bench-quantum（false，benchmark 降权）。
- 跳过的源（无新货/无精读价值）：openai（仅企业客户稿）、import-ai（下期约周一）、interconnects、deepmind、the-batch、ahead-of-ai、karpathy、lilian-weng、thinking-machines、chip-huyen。
