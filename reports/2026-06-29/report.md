# AI 日报 · 2026-06-29（周一）

> 流水线：scout 全量扫 18 源（0 抓取失败，4 个上期超时源 thezvi/import-ai/axios/hf-papers 全部重试成功）→ manifest（4 组精读 + 10 雷达）→ reduce 定牌 → 派 4 reader 精读 → 写手（4.6 窗口）写导读 → 4.8 验收 → 推送。
> 终稿精读 3 条（金 2 / 银 1）+ 雷达 7 条。导读按规：金牌两段、银牌一段、大白话、不出现「反直觉」、少破折号；雷达只留蓝字。
> **接手说明**：上一期 06-28 后，中途 codex 接任跑了半截（06-29 manifest + tmp 缓存），manifest 偏薄且把超时当成功、好料没落盘；本期 4.8 重接，重 scout 一遍（codex 旧 manifest 与 tmp 缓存已回收）。
> **规则变更（本期用户指示）**：废除「诚实留尾」规则——给自己看的日报不必把「存疑/未证实/未开源」搬进导读（语气僵、易泛滥）；不编造由铁律 2 独立管。已改 `写手须知.md` + `HANDOFF.md` 验收清单。
> **用户线索**：刷到 6 条，经 scout 核 → DeepSeek V4、三星SK、唐杰发文进雷达；GPT-5.6 Sol（主线饱和无新角度）、豆包否认社交、月之暗面融资八卦丢弃。
> **用户定牌调整**：OpenAI 欧洲就业报告 → 降雷达（不精读）；唐杰发文 → 雷达保留。
> **claude-blog 硬规则破例**：当天该源唯一新货是 Foundry GA（纯分发条、blog 固定 URL 都没定位到），按「硬拔精读会注水」破例压雷达（已并入弃用，未单列），用户认可。

## 🥇 金牌 · 头条精读

### [Zvi 拆穿 WSJ「中国网安已追平 Anthropic」：会找漏洞 ≠ 能自主串成 exploit，差距其实在拉大](https://thezvi.substack.com/p/wsj-article-claiming-china-has-matched) · Zvi Mowshowitz（Don't Worry About the Vase）· 2026-06-29
**为什么值得看**：把「单点检测 vs 自主串联 exploit」这条能力分水岭显式拎出来当判据，再用同日一个高调新工具去验证——一抽象一具体互相钉死。承接 Mythos 网安主线但角度全新（叙事纠偏，非旧政策瓜）。
- 核心判据（Zvi）：能在被指向的代码里找到单个漏洞 ≠ 能自主、规模化、无人指点地发现漏洞并把一堆看似无关的漏洞串成可用 exploit；后者才是 Mythos 真护城河，GLM-5.2、Opus 4.8、GPT-5.6 Sol 在同等难度都做不到。
- Zvi 加码：按所需 cycle 数和绝对耗时算，发文前差距其实在**拉大**而非缩小。点名反驳 7AI CEO Lior Div「中国正缩小差距」。
- 顺手接政策：引 Saif Khan「一边禁售 Fable、一边卖给中国造自己版本所需的芯片，是送给中国的大礼」——把模型能力之争接到出口管制（导读未展开，避开饱和瓜）。
- 活样本 Chitos（HF 博客，作者 FINAL-Bench / 工具方 VIDRAFT）：自称 detection-to-proof「真能 exploit」，但拿不出一个跑通的串联 exploit 输出；5 个预置样例（Log4Shell/JWT/SSTI/原型污染/供应链）只是可加载演示，exploit 成功率/误报率全未披露，自注「真实精度按目标环境另测」。跑在自研 Darwin-398B 上，安全相关只给一个「DOUBT-AUROC 0.903」元认知指标。正好坐实 Zvi「能验单点、串不起来」。
- 配套链接：[Chitos](https://huggingface.co/blog/FINAL-Bench/chitos)。

### [Import AI 463：机器人开始自我改进、腾讯万卡集群曝光，Jack Clark 给人类时代写了篇挽歌](https://jack-clark.net/2026/06/29/import-ai-463-self-improving-robots-a-10k-chinese-gpu-cluster-and-an-elegiac-essay-for-the-human-era/) · Import AI（Jack Clark）· 2026-06-29
**为什么值得看**：三主轴密度高、Jack 判断锋利。自我改进从软件爬进物理世界；万卡基建成「文明级技术签名」；末尾用挽歌散文把硬新闻收口为对「人类自决时代」的安魂曲。
- NVIDIA ENPIRE：四模块自迭代闭环（Environment 自动复位+验证 / Policy Improvement / Rollout 单多机器人并行评估 / Evolution 编码 agent 读日志改训练代码）。真实灵巧任务 99% 成功率（PushT、整理针盒、剪扎带、插 GPU），8 agent 并行优于单 agent。
- 反直觉天花板（Jack 原话）：「the complexity of tasks a system like this can attack is also defined by our ability to automatically evaluate and reset the system」——复杂度被自动评估/复位能力封顶。
- 腾讯 ARGUS：低开销常开 tracing+实时分析（Python 调度/框架编排/GPU runtime 三层），在超 1 万 GPU 生产集群跑了 6 个多月，诊断过 4,096-GPU 视频模型、512-GPU 音频模型、**12,960-GPU MoE**。Jack 的「Why this matters」标题＝"technical symptoms of broader sophistication"——读成体量与机构能力签名，非方法创新。
- 挽歌散文（转 Fernando Borretti）：「in a conflict, the advantage goes to the states where the humans remove themselves from the loop as much as possible」；副标题「What eras bookend our interregnum?」点题。
- 防重：RSI 与 Import AI 460（Anthropic 软件侧）撞母题，本期是机器人 hardware 侧新分支（导读已点明区分）。

## 🥈 银牌 · 非头条精读

### [亲 AI 阵营开始分裂：拆台的不是反对派，是当初定下「创新优先」国策的 David Sacks](https://www.axios.com/2026/06/29/trump-ai-model-release-delays-tech-backlash) · Axios（正文 403，多源交叉：Fortune/Bloomberg）· 2026-06-29
**为什么值得看**：威胁亲 AI 议程的不再是外部反对者，而是阵营内部国安鹰派 vs 创新加速派——而高调拆台的，恰是当初制定「pro-innovation」国策的那个人。
- David Sacks（Trump 前 AI/加密沙皇）公开警告：白宫门控正在自毁 Trump 一年前亲手立的「赢 AI 竞赛靠 pro-innovation」路线。
- 裂痕战线：先进 AI 测试该放偏民用的商务部、还是政府国安口，两边拔河。
- 投资人逻辑：模型发布权攥在政府手里，实验室估值理应被打折（背景音：Dalio「泡沫指标」称美股逼近 2000/1929 水平）。
- 触发链：白宫 6-12 对 Fable 5/Mythos 5 出口管制 → 要求 OpenAI 把 GPT-5.6 分阶段发 → 阵营内反弹。佐证 Fortune 6-27：Lutnick 批准 Anthropic 向可信伙伴恢复 Mythos 5、Fable 5 仍封。
- 角度新：前几期写「政府闸门 + 厂商应对」，本篇写**联盟内部政治裂痕**，非旧瓜重炒。

## 雷达（terse · 只蓝字）

- [OpenAI 把美国 AI 岗位转型框架搬到欧盟，结论：仅 14% 欧盟岗位面临高自动化风险](https://openai.com/index/mapping-ai-jobs-transition-eu/) · OpenAI · 2026-06-29（用户定调降雷达）
- [DeepSeek V4 正式版计划 7 月中旬上线，API 要搞峰谷定价（高峰翻倍）](https://cryptobriefing.com/deepseek-v4-launch-peak-hour-pricing/) · CryptoBriefing · 2026-06-29（用户线索）
- [三星 + SK 公布十年期本土投资计划，三星单家 2655 万亿韩元，重点砸 AI 半导体](https://finance.sina.com.cn/stock/usstock/c/2026-06-29/doc-iniezxcc0314608.shtml) · 新浪财经 · 2026-06-29（用户线索）
- [智谱唐杰谈大模型：主张从「工具性智能」向「认知性智能」跃迁](https://hub.baai.ac.cn/view/45566) · 人民日报/智源（兜底链接，未必原微博）· 用户线索
- [Interconnects 开源生态滚动盘点 #22：Zyphra、Cohere、Poolside 继续扩宽开放模型版图](https://www.interconnects.ai/p/latest-open-artifacts-22) · Interconnects · 2026-06-28
- [DeepReinforce 开源编码模型 Ornith-1.0（MIT，最大 397B），Simon 说不错但核心机制未披露](https://simonwillison.net/2026/Jun/29/ornith/) · Simon Willison · 2026-06-29
- [流媒体平台 Tidal 发 AI 政策声明，HN 211 分，版权与平台治理信号](https://tidal.com/ai-policy) · Tidal（HN 211）· 2026-06-29

---
## 运行健康
- 周一料偏厚。scout 全量扫 18 源、0 抓取失败；**上期 codex 跑挂的 4 个超时源（thezvi/import-ai/axios/hf-papers）本期全部重试成功**——其中 Zvi WSJ 反驳正是丢失的头条料，印证「超时源必须重试」。
- reduce 派 4 reader：group-1（Zvi+Chitos，两篇都抓到）、group-2（Import AI 463，jack-clark.net 镜像核实）、group-3（axios 403、多源二手交叉）、group-4（Foundry GA + Ornith，均偏弱、压雷达/弃用）。
- 定牌：金 2（网安能力分水岭、Import AI 463）、银 1（亲 AI 阵营分裂）、雷达 7。两金理由：厚日且两条都硬（范式判据 + 实锤 / 三主轴密度）。
- **规则变更落地**：废「诚实留尾」（用户指示），改 `写手须知.md`（第 18 条改为「别拔高别吹、不必搬留尾」）+ `HANDOFF.md` 验收清单（删第 6 条留尾、并入第 6 条事实校准说明）。
- **写手路线**：4.6 API 路线本期失败——代理 tken.me 是 Claude Code 风格端点、自动注入整套工具，模型改调 NotebookEdit/Glob 而非返回文本，`tool_choice:none` 在大 payload 上被代理忽略仍 tool_use。已在 `call_4.6.py` 加 `tool_choice:none`（小请求有效、大请求仍被绕过，待查）。**本期导读由 4.6 窗口写**（产出 `messages-2026-06-29.json`，api46 那份语气差弃用）。
- 验收：0 破折号、0「反直觉」、无 `<br>`/裸引号/裸 `<>&`（只 `<b>` 标签）；金牌两段（544/471 字）、银牌一段（249 字）。语气松（「打起来了/补刀/钉了实锤」）。发频道前按用户要求删掉雷达 DeepSeek「，待证实」尾巴。
- 丢弃/略过线索：GPT-5.6 Sol Juice 鉴别（主线饱和无新角度、无源）、豆包否认内测社交（弱）、月之暗面老股转让欺诈（融资八卦）。Foundry GA（claude-blog，注水风险压雷达后并入弃用）、3 篇 HF 论文（增量、碎，未上雷达）。
- seen 回写（report_date 2026-06-29）：thezvi（WSJ 反驳 reported=true）；huggingface（Chitos reported=true）；import-ai（463 reported=true）；axios（pro-AI splinter reported=true）；openai（欧洲就业报告 reported=true）；interconnects（#22 reported=true）；simon-willison（Ornith reported=true）；hacker-news（Tidal reported=true）。
- 跳过的源（无新货/出窗/停更）：anthropic、deepmind、karpathy、lilian-weng、chip-huyen、thinking-machines、ahead-of-ai、the-batch。
- 待办：4.6 API 路线 tool_choice 被绕过的根因（代理强制注入工具）需另解，否则 API 路线不可用、只能走窗口。
