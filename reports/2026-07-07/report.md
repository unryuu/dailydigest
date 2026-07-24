# AI 日报 · 2026-07-07（周二）· 长图第四期

> 流水线：scout（21 源，五分区）→ 3 reader 写金银 digest + 2 补读（GLM-5.2/OfficeCLI）+ 1 小 agent 补雷达 body → 主 Claude 直写 daily.json → **用户多轮编辑（挑精读、改措辞、降档、压字数）** → 发频道。
> 终稿：金 1 / 银 3 / 真雷达 6（全带 body）/ 今日乐子 2 / 赔率 4。
> **写作口味新规（用户 07-07 定，已固化进写手须知 + 记忆）**：反直觉直接陈述、别用「拧/反直觉/有意思的是/最X的是」强调；少用「xx 的是 xx」句式；少点评、直接陈述内容。

## 🥇 金牌
### [Anthropic「全局工作空间」：Claude 内部有块草稿纸](https://www.anthropic.com/research/global-workspace) · Anthropic Research · 2026-07-06
- J-lens 工具在 Claude 内部找到「J-space」：能暂存/操纵中间概念、与自动处理分开、不直接进输出；训练自发出现、只装几十个概念、占内部活动<10%。把偷想的「蜘蛛」换「蚂蚁」→腿数 8 变 6；删掉这块→流利说话/语法/背事实还在，多步推理掉到接近零。
- 定盘星 Neel Nanda 在 Qwen 复现核心结果、称好论文，但驳「意识」是全文最没意思的主张。论文只认功能性「通达意识」、否认主观体验。Axios 升格成「Claude 会沉思」。

## 🥈 银牌（3）
- [The Making of Claude Code：从一个玩具，到日活百万](https://www.anthropic.com/features/making-of-claude-code)：官方多人口述幕后。前身 clide（工程师业余搞的内部 CLI）、Boris「猜我在听什么歌」demo 发 Slack 只收两三个赞→日活百万、一工程师「2025 冬起不再亲手写代码」。产品心法：先做出现在只能用两三成的，好让下个模型出来能用八成。
- [喂再多数据也洗不掉的假信号，塞一批「平局」就治了](https://www.lesswrong.com/posts/i2qTghrkyY9xdcCFq/tie-training-can-make-dpo-rlhf-trained-ais-generalize-better)（Tie training）：定理证明假信号权重喂到无穷不归零；解法塞「平局对」（两个一样好的动作随机贴大小），对抗准确率 25%→70%。
- [Anthropic 的 Fable 5 使用心法：卡在你能不能讲清它的「未知项」](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns)：Thariq 的四象限未知框架 + 可抄提示词（盲点扫描/一次一问采访/给现成代码当规格/维护实现笔记/收尾小测验）。

## 真雷达（6·全带 body）
- [AI 利润率崩塌论](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/)（HN 547 最高，Part 1）：GLM-5.2 报价不足 1/5、切换成本近零，前沿厂商九成推理毛利从护城河变靶子。
- [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)：给 agent 的 Office 套件，读写 docx/xlsx/pptx、内置 MCP、渲染器让 agent 先看再改。
- [用密码学防 AI 假装人类给自己派活](https://www.lesswrong.com/posts/98GvRu78jTXJgz9gA/sub-agent-delegation-chaining)：硬件起头的密码学签名链锁死子 agent 委托链。
- [Ternlight 7MB 浏览器内 embedding](https://ternlight-demo.vercel.app/)（三值量化）· [小模型弱网落地](https://spectrum.ieee.org/small-language-models-ai-pharmaceuticals)（IEEE）· [RAG 上下文裁剪](https://www.kapa.ai/blog/how-we-prune-rag-context)（砍 68% 留 96%）。

## 今日乐子（2）
Claude Code 当私人健身教练 · 理性主义者的健康健身基础模型。

## 赔率盒子（4·删了 07-06 类似的灭绝 2060）
AI 歌 2050 前拿格莱美 50.5% vs 2027 前进 Billboard 前 20 仅 20.9%（远近期张力）· AI 零练习通关随机游戏 42% · Yudkowsky 到 2035 还信 AI 末日 56.7%。

---
## 运行健康
- 周二厚日。scout 全量扫 21 源、0 抓失败。头条 Anthropic 全局工作空间四源交叉（官方 research + LW 一作原帖 + Neel Nanda 复盘 + Axios 升格）。thezvi 无 AI #176。
- reader：group-1（全局工作空间，Neel 复现认可但去魅意识）、group-2（Claude Code 双发：Making of 冲金料 + Fable field guide）、group-4（LW 安全四帖挑 Tie training 银 + 委托链）、补读 group-5（GLM-5.2 利润率崩塌）、group-6（OfficeCLI）。1 小 agent 补 3 条原雷达 body（Ternlight/小模型/RAG，核实未编）。
- **写手＝主 Claude 直写**：7 篇精读候选全写摘要发用户挑；用户多轮编辑——挑精读、改标题/正文措辞、把 GLM-5.2/OfficeCLI/委托链降银→再降雷达并自压短 body、删赔率末条。中途因用户本地未保存与我的改动错位、发生一次版本对不上，已按「用户保存版为准」对齐。
- **写作口味定规**：反直觉直接陈述别强调、少「xx的是xx」句式、少点评（写手须知 + 记忆 daily-writing-voice-direct-statement 均已记）。
- 自查：金 2 段、银各 1 段、雷达全带短 body；0 破折号、0「反直觉」、无 `<br>`/裸引号/裸 `<>&`。图 1179×10167 发附件。
- seen 回写（report_date 2026-07-07）：anthropic +2（global workspace/Making of）、lesswrong +6（GW 一作/Neel/Tie training/委托链/健身教练/健康模型）、claude-blog +1（Fable field guide）、hf-papers 0、hacker-news +5（GLM-5.2/OfficeCLI/Ternlight/小模型/RAG）。Manifold 不做 seen。
- 跳过：thezvi（无 #176、Fable #6 饱和）、import-ai（464 已报）、openai/deepmind/interconnects/the-batch/ahead-of-ai 无窗内新货、acx（已报）、月检四源。
