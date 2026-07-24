# AI 日报 · 2026-06-23（周二）

> 流水线：scout 全量扫 16 源（窗口放宽 ~60h）→ manifest（3 精读候选 + 8 雷达候选）→ 3 reader 精读 + 1 verifier 核雷达 → reduce 定牌 → 用户复核重排。
> 终稿精读 3 条（金 1 / 银 2）+ 雷达 3 条。导读按新规：金牌两段、银牌一段、大白话、少用「反直觉」字样。雷达只留蓝字。
> **日期说明**：用户平时晚 10 点要日报，本期过零点才提，从上一期 06-22 算只过一天，定为 **06-23**（非系统时钟的 06-24）；内容亦为 06-22~06-23 料。
> **编辑说明（用户复核）**：① OpenAI Daybreak 初定银牌，用户判降雷达。② 《AI 可负担性危机》初为雷达，用户升银牌。③ VibeThinker 由雷达升银（verifier 核成色硬、纠正「3B 全面超 Opus」口径）。④ Codex-maxxing 跑题丢弃。⑤ 人才战由银料压雷达（人事/政治偏闷）。

## 🥇 金牌 · 头条精读

### [为什么大模型防不住注入攻击：它分不清指令来源，靠的是「样式」不是「角色」](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/) · Simon Willison（转述论文）· 2026-06-22
**为什么值得看**：主流叙事是注入攻击防不住、永久打地鼠；这篇给出可操作的根因——模型靠文本样式而非真正的角色标签分辨指令来源，「去样式化」就能把注入成功率从 61% 砍到 10%。
- 出处：Simon 转述并背书的论文（role-confusion.github.io），作者 Charles Ye / Jasmine Cui / Dylan Hadfield-Menell（MIT 对齐研究者）。Simon 原话「First, I absolutely love this」。
- 核心机理（研究者原话）：「models take the *style* of the text more seriously than the actual text」。攻击=把用户输入伪装成模型内部/系统文本的样式，制造「角色混淆」。
- 硬数字：在 `gpt-oss-20b` 上，destyling 把数据集平均攻击成功率「from 61% to 10%」。destyling = 重排成视觉上不像系统文本的格式。
- 研究者悲观结论：「Unless LLMs achieve genuine role perception, injection defense will remain a perpetual whack-a-mole game」——缓解非根治。
- ⚠️ 局限：仅单一小模型 + 这一类样式模仿攻击上验证，样本量/显著性/泛化未展开。
- 与近期关系：prompt injection 机理侧新解，与 06-18 agent 安全/AI Control（系统层纵深防御）不同主题，互补不重复。

## 🥈 银牌 · 非头条精读

### [微博的 3B 模型 VibeThinker：窄域打平旗舰，宽域大方认怂](https://github.com/WeiboAI/VibeThinker) · WeiboAI（HN 316）· 论文 arXiv:2606.16140 · 2026-06-23
**为什么值得看**：HN 传「3B 击败 Opus 4.5」，真相是窄域（可验证推理：数学/代码/指令遵循）打平旗舰，宽域大方认怂——这个诚实切口比「3B 屠榜」营销值钱。
- 口径纠正（verifier）：出圈对标 Opus 的早先是 1.5B 版，3B 是近期升级款；「超 Opus」严格限定在可验证推理域。
- 硬数字（3B）：AIME26 94.3、HMMT25 89.3、LiveCodeBench v6 80.2、IFBench 74.5（vs Opus 58.0）。
- 防 benchmaxx 实证：2026-04-25~05-31 的 LeetCode 周赛（训练后、确属分布外）通过率 96.1%，压过 GPT-5.2 和 Claude。
- 自报家丑：GPQA-Diamond 仅 70.2（远落后 Gemini 3 Pro 91.9 / Opus 4.5 87.0），作者承认「广博事实召回任务上规模仍重要」。后训练成本号称仅 7800 美元。
- ⚠️ 厂商/作者自报基准，已交叉 GitHub README + arXiv + neurohive。

### [《AI 的可负担性危机》：你那点订阅费，背后是几十倍的补贴](https://blog.dshr.org/2026/06/ais-affordability-crisis.html) · David Rosenthal（DSHR）· 2026-06
**为什么值得看**：观点帖带硬数据，戳破「旗舰订阅看着不贵」的泡沫——其实是厂商在巨额倒贴买需求。
- 核心数字：200 美元/月订阅下，用户可烧至多 8000 美元 Anthropic token 或 14000 美元 OpenAI token，意味补贴最多约 40 倍（Anthropic）/ 70 倍（OpenAI）。
- 另引 OpenAI 销售营销支出占营收 44%（57.3 亿美元）。
- 作者把这套打法称「毒贩算法」：补贴造需求、喂出依赖，再谈涨价。
- ⚠️ 观点帖（非数据研究原稿）；注意「AI 恶化美国医疗可负担性」是另一批同名 PwC 口径文章，勿混。

## 雷达（terse · 只蓝字）

- [OpenAI 扩张 Daybreak 安全平台、发布网络安全模型 GPT-5.5-Cyber，自陈「找漏洞已过剩、补漏才是瓶颈」](https://openai.com/index/daybreak-securing-the-world) · OpenAI · 2026-06-22（初定银牌，用户降雷达）
  - 存档要点（不进推送）：四块拼图 GPT-5.5-Cyber（CyberGym 85.6% vs 普通 81.8%，仅 Trusted Access 防御方）/ Codex Security（IDE 扫描+验证+生成补丁）/ Cyber Partner Program（近 30 家：CrowdStrike、Palo Alto、Cloudflare、Wiz、IBM）/ Patch the Planet（联合 Trail of Bits 帮开源维护者，五天冲刺横跨 19 项目、刨数百 issue、合并数十补丁）。真实战果：OpenBSD 内核藏 23 年的 use-after-free、Linux/FreeBSD 数十漏洞、Chrome/Safari 可利用 bug。HN 190 分怨气=付费安全用户用不上、实名挡非美用户（同构 06-21 实名摩擦）。openai.com 三条一手 403、多家二手交叉。
- [AGI 抢人战：Transformer 作者 Shazeer 投 OpenAI、AlphaFold 诺奖得主 Jumper 离开 DeepMind 投 Anthropic](https://www.axios.com/2026/06/23/ai-lab-agi-google-deepmind-departures) · Axios · 2026-06-23（reader 给银料，按用户口味压雷达，可应需升精读）
  - 存档要点：两条人事多源实锤（TechCrunch 等）。Shazeer（Gemini 联合负责人，Google 此前约 $2.7B 收 Character.AI 把他带回、不到两年又走）6/18 任 OpenAI「Lead for Architecture Research」；Jumper（2024 诺奖、DeepMind VP）6/19–20 投 Anthropic。献金战（已纠正 manifest 笔误）：OpenAI 系「Leading the Future」$8M+ 反 Bores、Anthropic 系（注资 $20M 的 Jobs and Democracy）$15M+ 挺 Bores，全场逾 $20M；两家都公开支持 AI 安全立法却资助互掐的 PAC（Bores 是 NY RAISE Act 作者）。Axios 两篇 403、二手交叉。
- [OCR 同日双发：百度开源 Unlimited-OCR 对打 Mistral OCR 4](https://github.com/baidu/Unlimited-OCR) · 2026-06-23
  - 存档要点：百度 Unlimited-OCR（3B/500M 激活 MoE，R-SWA 固定 KV cache，一次推理通吃几百页，OmniDocBench 93%、比 DeepSeek-OCR 高 6%）；Mistral OCR 4（mistral.ai/news/ocr-4，bounding box+块分类+逐词置信度+可自托管、170 语言，OlmOCRBench 85.20 居首）。开源对闭源、长文档对结构化。

---
## 运行健康
- 周二（过零点请求，定 06-23）。06-23 当期窗口放宽 ~60h（覆盖 06-22~06-23），seen 去重为准。scout 全量扫 16 源、0 抓取失败；产出 3 精读候选 + 8 雷达候选。reduce 派 3 reader 精读 + 1 verifier 核 5 条雷达候选（含解析 HN 真实 URL）。
- scout 红线/去重表现好：对 DeepMind 用标题比对 seen，未重蹈 06-22 误收 Gemma 覆辙；开源逼退/GLM-5.2 主线 06-22 已密集报，未重收；疑似关联均标「待 reader 核」。
- reader/verifier 纠坑与核实：① group-1 openai.com 三条 403，多源交叉，关键数字两源一致；判 Codex-maxxing 跑题剥离。② group-2 两条人事大瓜多源实锤，纠正 manifest 献金数字错误（实为 Leading the Future $8M 反 / Jobs and Democracy $15M+ 挺，非原写 $9M）。③ group-3 厘清是 Simon 转述论文（非原创），出处 role-confusion.github.io。④ verifier 纠正 VibeThinker「全面超 Opus」口径、合并 OCR 双发、坐实 DSHR 补贴数字、判 V-Zero 窄学术可略过。
- 定牌（含用户复核重排）：金 1（prompt injection 角色混淆）、银 2（VibeThinker、AI 可负担性危机）、雷达 3（Daybreak、AGI 抢人战、OCR 双发）。用户复核：Daybreak 由银降雷达、可负担性危机由雷达升银、人才战由银料压雷达。
- 导读规范本期起调整（已写入 PROMPT.md / HANDOFF.md）：金牌导读两段（约原一半字数）、银牌一段（约三成）；少用「反直觉」字样（要内容不要口头禅）；说大白话、别拗口；雷达只留蓝字、不带黑字 note。
- 丢弃：Codex-maxxing（跑题）、V-Zero（窄学术）、Moebius 浏览器移植、Zvi Monthly Roundup #43（AI 含量低）、GLM-5.2 本地部署教程（06-22 主线已密集报）。
- seen 回写（report_date 2026-06-23）：openai（Daybreak / Patch the Planet reported=true；Codex-maxxing reported=false）；axios（人才战、NY-12 reported=true）；simon-willison（prompt injection reported=true；Moebius reported=false）；hacker-news（VibeThinker、Unlimited-OCR、Mistral OCR 4、AI Affordability、Daybreak 讨论页 reported=true）；thezvi（Monthly Roundup reported=false）；huggingface（V-Zero reported=false）。
- 跳过的源（无新货/出窗）：anthropic、import-ai（#462 已报）、interconnects、deepmind、the-batch、ahead-of-ai、karpathy、chip-huyen、lilian-weng、thinking-machines。
