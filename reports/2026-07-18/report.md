# 2026-07-18 日报存档（周五 · 长图第十四期）

规格：1 金 4 银 7 雷达 4 乐子 2 赔率（发布版）。频道消息 id 169/170，图 1179×7195。

## 定牌表
| 档位 | 条目 | 来源 | 备注 |
|---|---|---|---|
| 金 | 习近平 AI 讲话（human control 定调） | Zvi #177 Part 2 | 往期零覆盖，Zvi 判 strong speech |
| 银 | OpenRouter 前五全中国开源模型 + Anthropic 定价转弯 | axios + simonw | 07-17 Kimi K3 金线续章，只取增量 |
| 银 | Cursor 脏输入评测法 | claude-blog | 三连发主打；CISO/Base44 未发 |
| 银 | AI 意识研究综述 | LW | 正方帖并组，正文里被用户删 |
| 银 | Raschka reasoning effort 机制 | ahead-of-ai | 六路线综述 |
| 雷达 7 | 世界模型综述 / 2M token RL / 可纠正性基金 / CoT 可监控 / NP-hard 自创评测 / 法官与 AI / 凸优化 30 年缺口 | | 凸优化经核查为真（Berkeley 教授实名 + Lean 验证 + 全程公开） |
| 乐子 4 | AWS 17 亿账单 / AI logo / SO 提问量暴跌 / 脑白质切除术 | | |

用户砍掉：OpenAI CFO 记分卡、青少年立场稿、Claude for Teachers（雷达）；堕胎热度、开源 IMO（赔率）；simonw AI 味检测器（定牌阶段，昨日同题材）。

## 本期事故（三起，全部已固化对策）
1. **Grok 旧闻泄露进预览**：Zvi Part 1 里的「Grok 上传私有 git 仓库」实为 07-17 银牌（grok-build）同一事件，reader 标「未报过」、主 agent 采信并亲手提进雷达，用户抓出。根因：派活防重复清单只挑了 2 条、没列全 07-17 金银。→ 记忆 `dedup-list-must-be-exhaustive`。
2. **AI 味浓、雷达超量**：radar/fun 文案第一作者（核查 agent）没读过任何语气规范；写手自创「body 收进 label」推高密度；主 agent 自己填 title/odds 也没读写手须知；雷达冲到 11 条（单日惯例 5-7）。→ 新增 `writer/定调.md`（所有写用户可见文案的 agent 动笔前读），RUNBOOK 步骤 2/3/4/5 落实，数量口径写成建议值。
3. **赔率系统性回锅**：本期 2 条发布赔率均为 11-12 天前报过（恋爱 87→89、游戏 42→48.9，都不满足「变化>10 点」）；回测发现 07-17 三条也全是回锅。根因：主 agent 给 scout 的赔率去重清单只回溯几天，人肉记不全。→ 新增 `scripts/check_dup_urls.py`（见下），已进 RUNBOOK 步骤 1 和 6。已发布不回改。

## 新工具：check_dup_urls.py
当期 manifest/daily 的 URL 对比往期已发（daily.json + 旧格式 messages.json）。两档：规范化指纹精确匹配（LW 帖 id、manifold slug、arxiv 号、HN id 等站点级身份提取）+ 同域路径相似度疑似档（同模板不同编号自动豁免）。精读/雷达/乐子撞了建议丢；赔率撞了报上次日期+概率，按「隔得久或变化>10 点可再报」人工判。07-18/07-17 双日期回测通过，误报已清。

## reader/核查纠偏记录
- 凸优化（低信度 reddit 帖）核实为真：Phillip Kerger，UC Berkeley IEOR 在职教授，GitHub 仓库 + Lean 4 形式化 + 原始对话全公开；帖内更正用的是 Sol Pro 非 Ultra。
- axios 法官条：JAIC 是 2026 年 1 月成立（约 200 人），非当日新闻，label 改背景写法。
- group-2：Anthropic 条款出处只有 @claudeai 推文 + 媒体交叉，无官方公告页；OpenRouter 前五里没有 Kimi（趋势先于爆款）。
- group-5：GPT-5.6「小模型高档≈大模型低档」原文未明说，reader 主动修正为「曲线重叠」。

## 写作复盘
写手第三期试跑：四区字数全线内（金 209、银 88-128），无 digest 结构抄袭。但本期用户修改量为写手上线以来最大（见 用户修改.md），核心问题是语气密度而非结构——修改归纳五条中「首句不重复 title」「英文术语拔掉」「label 装得下就不留 body」三条已落进定调.md/工单流程，下期验证。

## 流程变更（今日落地）
- `writer/定调.md` 新增；写手须知开头指向它。
- RUNBOOK：步骤 1/6 加查重脚本、步骤 2 加数量建议（雷达 5-7、乐子 3-4，料厚可适当扩充、优先提档砍尾）、步骤 3 核查 agent 读定调、步骤 4/5 主 agent 文案也过定调。
- 工单/定调新规：同样内容 title/label 与 body 只出现一次。
