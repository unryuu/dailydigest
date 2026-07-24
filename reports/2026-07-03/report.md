# AI 日报 · 2026-07-03（周五·淡偏中）

> 流水线：scout（Claude subagent）全量扫 18 源（2 抓取失败：Reuters 正文硬拒走镜像、Anthropic cyber-safeguards 稿判饱和）→ manifest（3 组 + 9 雷达）→ 3 reader 写 digest → 4.8 定牌 → **写手＝命令行 codex（gpt-5.5）从 digest 写摘要** → 4.8 验收 → 发频道。
> 终稿：金 1 / 银 1 / 雷达 6。**用户复核**：OpenAI 送政府 5% 股权由银降雷达（只留标题一句）。
> codex 本期已按工单要求写成纯 UTF-8（无 BOM），沙箱 helper 仍间歇报 1223 但重试挺过。

## 🥇 金牌 · 头条
### [阿里 7 月 10 日起全员禁用 Claude Code：所谓「后门」正是 Anthropic 自己埋的指纹检测，蒸馏互撕升级为封杀](https://www.usnews.com/news/top-news/articles/2026-07-03/alibaba-to-ban-claude-code-in-workplace-over-alleged-backdoor-risks-source-says) · Reuters/US News（正文硬拒，Cryptopolitan/thenews 镜像交叉）· 2026-07-03
- 因果链闭合：Anthropic 6/24 指控阿里 Qwen 蒸馏（25000 欺诈账号、4/22-6/5 间 2880 万次对话，致信参议院银行委）→ Claude Code v2.1.91 埋时区（Asia/Shanghai、Urumqi）/代理域名（147 条清单）指纹检测、结果编码进发往 Anthropic 的系统提示 → 阿里内部审计逆向发现、以「后门」为名 7/10 起全员封杀改用自研 Qoder/Qwen → 双方 X 互撕。
- **核实结论**：所谓「后门」＝07-01 已报的 thereallo.dev 隐写打标同一套机制（同版本、同时区清单、同 4 个 Unicode 撇号编码）。Anthropic 的 Thariq 回应「防账号倒卖/防蒸馏、非监视，下版移除」、另有员工称「三月启动的实验」均核实为真；移除版 v2.1.197 已发但 changelog 未提。
- 反直觉钩子：同一段代码，一方叫反蒸馏自卫、一方叫监控后门，谁是加害者取决于从链条哪端看；24 小时内从逆向八卦升级成中国最大科技公司之一的封杀令。
- 新增量＝封杀 + 互撕 + 机制同源三层；隐写技术细节只作已核实背书、点到即止（防重复红线，07-01 已报）。

## 🥈 银牌
### [Simon 一天三连：让 agent 造 agent、让 Fable 5 自己调 agent，最后转 Litt 一句「理解才能参与」](https://simonwillison.net/2026/Jul/2/llm-coding-agent/) · Simon Willison · 2026-07-02
- 三篇拧一条：① 两句提示词让 Claude Code 用 red/green TDD 自举出一个能读写文件/执行命令/搜 repo 的编码 agent 框架（Simon 一行没写，「用 agent 造 agent」）；② 把异步研究任务交给 Claude Fable 5，让它用 DSPy 优化 Datasette Agent 的只读 SQL 系统提示（发现「已有信息就别 describe_table」会诱导模型瞎猜列名、反复报错重试）；③ 转 Geoffrey Litt「开发者必须理解 agent 生成的代码才算主动参与者」。
- 落点：产出方从人变成 Fable 5 + Litt 理解论（「可以少写，不能少懂」）。与 07-02 loop 教程银牌切割，不重复循环工程框架。

## 雷达
- [OpenAI 放风提议送美政府约 5% 股权（按 8520 亿估值约合 426 亿美元），说是让公众分享 AI 收益](https://www.axios.com/2026/07/02/openai-trump-administration-investor-stake) · Axios/FT（二手，属放风概念非正式 offer）·（原为银牌，用户复核降雷达只留标题；对照线：对外 Pax Silica 联盟扩 24 国、GPT-5.6 逐案审批，出口管制 06-29 已报只作对照）
- [WebKit 推出 Safari MCP server，让 agent 直接驱动 Safari 做前端调试](https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/) · WebKit（HN 151）
- [SkillCoach：让 agent 自演化评分标准，再用这些 rubrics 评估和提升技能使用](https://huggingface.co/papers/2607.01874) · HF Papers
- [Elena Verna 吐槽「AI 自信表演」：模型该学会在没把握时示弱](https://www.elenaverna.com/p/please-stop-the-ai-confidence-theater) · Elena Verna（HN 80）
- [字节 Seed 把已训好的 Transformer 变形成混合注意力架构，主打省掉重训成本](https://huggingface.co/papers/2606.30562) · HF/ByteDance Seed
- [吴恩达 The Batch #360：GPT-5.6、机器人训练、模型调模型，以及 AI 世界太吵](https://www.deeplearning.ai/the-batch/issue-360/) · The Batch

---
## 运行健康
- 周五淡偏中。scout 全量扫 18 源、2 抓取失败（Reuters 正文硬拒→usnews/Cryptopolitan/thenews 镜像交叉核实；Anthropic fable-safeguards-jailbreak-framework 稿判饱和降雷达，首个猜测 URL 404 已更正真实 slug）。3 reader：group-1（阿里封杀，因果链核实闭合，强/金）、group-2（Simon 三连，中/轻银）、group-3（Trump 门槛+OpenAI 5% 股权，银→用户降雷达）。
- **写手＝命令行 codex（gpt-5.5）**：主 Claude 用 `$null | codex exec -C <repo> -s workspace-write -o <last>` 调用。本期 codex 已按工单写纯 UTF-8（无 BOM，省去去 BOM 步）；沙箱 helper 仍间歇报 `1223 ShellExecuteExW`（用户看到弹错，实为正常、重试可挺过）。
- 验收：金 2 段（458 字）、银 1 段（419 字）；0 破折号、0「反直觉」、无 `<br>`/裸引号/裸 `<>&`；对照 digest 忠实（阿里 25000 账号/2880 万次对话/v2.1.91、Simon 自举 TDD、OpenAI 5% 折 426 亿均对得上），未复述隐写细节、5% 自然带「放风非签字」无硬留尾。
- 定牌：金 1（阿里禁 Claude Code）、银 1（Simon 三连）、雷达 6（OpenAI 5% 股权 + Safari MCP + SkillCoach + AI 自信表演 + 字节混合注意力 + The Batch #360）。
- seen 回写（report_date 2026-07-03）：hacker-news（阿里 usnews / Safari MCP / AI 自信表演）、simon-willison（llm-coding-agent 三连）、axios（OpenAI 5% 股权）、hf-papers（SkillCoach / 字节混合注意力）、the-batch（#360）。
- 跳过的源（无新货/出窗/停更）：thezvi（Fable #6 复盘 redeploy 无新料）、claude-blog（admin spend 计费稿判最弱、未立组）、deepmind、interconnects、import-ai、ahead-of-ai、openai、karpathy、lilian-weng、thinking-machines、chip-huyen。
