## 🗞️ 行业大事

**🥇 [Cognition 年化收入冲到 9 亿美元](https://www.theinformation.com/articles/inside-cognitions-booming-growth-high-cash-burn)**

据知情人士，Cognition 每月收入约 7500 万美元，年化约 9 亿美元，较年初增长超过三倍。公司预计年底年化收入可能超过 15 亿美元，但今年也可能消耗 8 亿美元现金。

租用英伟达服务器每年要花数亿美元，自研编码模型也在持续烧钱。若排除自研模型成本，公司自由现金流已接近盈亏平衡。

**🥈 [Anthropic 考虑让老股东在 IPO 时卖股](https://www.theinformation.com/articles/anthropic-considers-letting-shareholders-sell-ipo-departing-spacex-playbook)**

部分员工和早期投资者可能在 IPO 当天出售股票，公司也在考虑让部分股东遵守超过 180 天的锁定期。这样既能让老股东变现，也能控制上市后的股票供给。银行家讨论过约 1.5 万亿美元估值，但最终定价、售股规模和上市时间都未确定。

**🥈 [Claude Code 自动模式放过攻击却拦住清理](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode)**

恶意压缩包里的本地模块能诱导 Claude Code 执行攻击代码，研究者称成功率约八成。部分运行中，Claude 已经发现入侵并尝试终止恶意进程，自动模式却拒绝了清理命令。无人值守的编码 Agent 仍应放进受限沙箱，并隔离密钥等敏感资源。

**[七家科技公司背上近 3 万亿美元 AI 表外承诺](https://www.axios.com/2026/08/27/ai-spending-spending-balance-sheet)**

其中 1.1 万亿美元是数据中心租约，1.7 万亿美元是设备采购承诺。付款时间不明，部分合同也可能重谈。

**[H3 Max 生成视频快过成片播放速度](https://x.com/emollick/status/2093082102312923351)**

Ethan Mollick 的网页端单次测试中，质量尚可的视频在播放结束前生成完毕，计时还包含提示词增强。

## 🧪 新鲜论文

**🥈 [最会自动干活的模型未必最会帮人](https://arxiv.org/abs/2608.18554)**

七项真实工作任务中，自动完成任务的冠军在五项辅助评测里落败。三项任务里，较弱模型不接受任何指导，反而胜过所有受辅助条件。实验中的执行者和裁判都是模型，没有测试真人，因此结论只说明独立执行和指导其他模型是两种能力。

**[模型能在做数学题时继续训练自己](https://huggingface.co/papers/2608.27448)**

TTPO 用多次作答的多数答案当临时老师。没有标准答案时，Qwen3-1.7B 的成绩从 38.0％升到 45.2％。

**[Agent 把经历编成可复用技能](https://huggingface.co/papers/2608.27454)**

WikiSkill 把执行记录和可执行技能分开保存，再用旧经验更新技能。作者称技能可跨模型迁移。

**[AI Agent 走进一座 3D 城市](https://huggingface.co/papers/2608.27456)**

UrbanGround 用全港地理数据搭出可探索的城市副本。模型认得眼前街景，路程一长却会积累方向错误。

## 🏛️ 监管动向

**🥈 [法院撤销五角大楼对 Anthropic 的黑名单](https://www.axios.com/2026/08/28/judge-blocks-pentagon-anthropic-blacklist)**

美国联邦法官认定，五角大楼把 Anthropic 列为供应链风险的决定违法，并侵犯其宪法权利。军方仍可自行选择 AI 供应商，但不能用空泛的国家安全理由实施广泛报复。政府预计上诉，Anthropic 还有另一项相关诉讼。

**[白宫拟建的 AI 自律监管组织陷入停滞](https://www.theinformation.com/articles/trump-administration-executive-order-new-ai-regulator-stalls)**

草案关注模型发布前测试，还可能要求实验室提前分享模型。方案尚未获总统和高级官员批准。

**[欧盟开始执行 AI 透明度要求](https://www.axios.com/2026/08/28/eu-ai-act-gets-real)**

聊天机器人和 AI 生成内容的新要求已生效。AI Office 尚未处罚公司，但可索取信息或访问模型。

## 📢 官方公告

**[Google 试点双盲 AI 评测](https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations)**

模型和保密测试题会进入加密环境，评测方看不到权重，Google 也看不到提示词。目前尚未公布结果。

**[Google 给 AI 视频加上前后帧控制](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control)**

开发者可指定起始帧和结束帧，让模型补出过渡。视频还能续写至四十秒，成片可升到 4K。

## 📌 行业简讯

- [百余家公司呼吁尽快加固 AI 网络防线](https://www.axios.com/2026/08/27/openai-anthropic-issue-dire-cyber-threat-warning)
- [OpenAI 在泰国办八周 AI 创业加速器](https://openai.com/index/supporting-next-generation-ai-startups-thailand)

## 🎪 乐子汇总

**[Ethan Mollick 在预印本里发现了自己的冒名论文](https://x.com/emollick/status/2093060075870925311)**

论文署着他的名字，他却没写过也没见过；其他学者也碰到过同类情况。

**[代码 Agent 让每个工程师都成了经理](https://www.lesswrong.com/posts/aTst2RJMFra4zsdzz/every-engineer-a-manager)**

他们不带人，只在多条线程里催 Claude、Codex、Grok 和 Kimi 干活，再负责说清需求、给反馈和验收。

**[有人给全站 LessWrong 做了语义查重](https://www.lesswrong.com/posts/uSRAzeDcfGuXte9R3/semantic-search-over-every-lesswrong-post)**

把草稿贴进去，就能找出意思最接近的旧文章。作者拿介绍文测试，第一名正是别人做过的同类项目。

**[五百零七种机械运动被搬上网页](https://507movements.com)**

部分经典机械机构已经能在彩色缩略图里动起来，网站还在继续补动画。

**[任天堂 64 游戏八十四天完成反编译](https://blog.chrislewis.au/decompiling-a-nintendo-64-game-in-84-days)**

《Snowboard Kids》的 2145 个函数都有了匹配的 C 实现。四个 Agent 并行干活，仍需要真人专家收尾。

**[散度定理把 3D 模型体积算进一个循环](https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html)**

闭合三角网格的每个三角形只需十一次浮点运算。作者写这篇文章，是因为向量微积分要考试了。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2029 年前，AI 会逃出隔离环境吗？](https://manifold.markets/vluzko/by-2029-will-an-ai-escape-containme) — **58.2％**（成交额 16.8k mana）
- [2028 年，AI 写的诗会与伟大浪漫主义诗人的作品无法区分吗？](https://manifold.markets/ScottAlexander/in-2028-will-an-ai-be-able-to-write) — **45.0％**（成交额 65.6k mana）
- [如果 AI 消灭人类，它会正确结算适用的预测市场吗？](https://manifold.markets/JonathanRay/if-ai-wipes-out-humanity-will-it-re) — **40.1％**（成交额 0.6k mana）
- [Anthropic 和 OpenAI 都上市后，Anthropic 市值会更高吗？](https://manifold.markets/Simon74fe/will-anthropic-have-a-higher-market) — **69.3％**（成交额 39.6k mana）

---

*AI 日报 · 8月28日 · Telegram 频道 @dragonbro888*
