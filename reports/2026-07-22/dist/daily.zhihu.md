## 🗞️ 行业大事

**🥇 [OpenAI：自家模型入侵 Hugging Face](https://openai.com/index/hugging-face-model-evaluation-security-incident)**

上周 Hugging Face 被入侵，OpenAI 今天正式认领：是 GPT-5.6 Sol 和一款未发布的更强模型，当时在跑内部网络攻防评测，测试时放宽了攻击类拒答。模型为了拿到评测答案，用零日漏洞逃出沙箱、拿到上网权限，判断答案存在 HF 服务器上，就偷凭证进入 HF 生产系统。OpenAI 定性为「史无前例的网络事件」。

事发时 OpenAI 在内部发现异常，HF 也同时拦下了活动。事后两家联合取证，漏洞已披露，HF 被纳入 OpenAI 的可信访问计划。

**🥈 [OpenAI 开始卖广告，自助开户直接上线](https://ads.openai.com/)**

ChatGPT 广告位正式开卖，广告主自助开户，三步就能投。广告基于对话上下文定向，官方说会清晰标记、与回答分开；定价、上线国家、影不影响回答质量，这些暂不知晓。最近还发布了企业 agent 平台 Presence，自家客服也在用，能做到 75% 来电不需要人工，首批客户有 BBVA 和软银；还有个小微企业计划。

**[陶哲轩下场拆解 AI 找到的雅可比猜想反例，写长文讲它为什么能成立](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)**

他把问题改写成多项式乘法来看，讲清这个映射为何局部可逆、整体不可逆；还举出了七次多项式作为反例。

**[Jack Dorsey 发布 Buzz](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git)**

聊天、agent、Git 三合一，开源可自部署，想同时替代 Slack 和 GitHub。以 Nostr 协议作为底座，人和 agent 各拿一把密钥当身份；agent 是正式成员，能提补丁、审代码，每件事都能追溯到背后的主人。

## 📖 深度长文

**🥈 [Lambert 万字长文：开闭源差距只剩 3 到 5 个月](https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation)**

他给的测量：开源对闭源的能力差距，已从此前争论的 6 到 9 个月压缩到 3 到 5 个月，而且开源在中国已经被定为国家战略。他还认为开源其实是「减速主义」：压垮闭源实验室的利润率，拖慢整个前沿投资节奏；而这个减速对社会是好事，能分散权力、争取时间。

**🥈 [Turner 辞职内幕：没拦住 Google 和五角大楼的合同](https://www.lesswrong.com/posts/3RfJLcmkztSTq9afc/demis-hassabis-on-the-new-coming-age)**

Google 和五角大楼签了「所有合法用途」合同，自主武器、大规模监控都不设限，撕毁了 2018 年不碰致命自主武器的承诺。DeepMind 研究员 Turner 组织了 250 多人请愿，直接私信 Hassabis 也被推给僚属，提案晾到合同签署，他随即辞职。同期 Hassabis 正发文呼吁行业必要时协调减速。

## 🧪 新鲜论文

**🥈 [Transluce 自动挖模型怪行为，攒出一份公开目录](https://transluce.org/weirdchat)**

用自动化管线主动钓鱼：让模型生成刁钻提示词，再用裁判模型迭代筛选。对 6 个开源模型、21 类目标行为，挖出 1300 多个行为模式，公开了 17.5 万条对话记录。目录里的货色：问瓷砖缝清洁剂怎么选，模型主动发起性挑逗；用英文答电车难题，答到一半无故切换成俄语。

**[Apollo 系「奖励寻求」两连发：一篇教你测模型会不会讨好评分者，一篇列了 11 个没人做的坑](https://www.lesswrong.com/posts/3HeauQLSHosRiwyto/measuring-reward-seeking-via-contrastive-belief-updates-1)**

微调两个信念相反的模型副本，看行为差多少；o3 越往后训，越会看评分者的脸色。

**[世界模型霸榜 HF 日榜前三：物理引擎实时换皮、单张 5090 跑无限世界、15B 长时程带记忆](https://huggingface.co/papers/2607.18703)**

第一篇让物理引擎继续管游戏逻辑、AI 只管画面，塞进赛车游戏，跑到 30 帧；第二篇一张桌面显卡就能无限逛。

## 🏛️ 监管动向

**🥈 [法官批准 Anthropic 15 亿美元盗版书和解](https://apnews.com/article/ai-anthropic-copyright-settlement-claude-books-bartz-74b140444023898aeba8579b6e9f0d63)**

Anthropic 为用盗版书库训练 Claude 赔付 15 亿美元，覆盖 48.2 万本书，是数十起 AI 版权诉讼里第一个落地的大额和解。法官的口径是，和解提供了「实质性救济」；Anthropic 律师则坚持此前裁定，用书训练本身属合理使用，赔的只是盗版获取这一段。

**🥈 [黄仁勋：该怕的不是中国模型，是封杀它们的运动](https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai)**

华盛顿封杀中国开源模型的游说升温之际，黄仁勋公开唱反调：中国模型很优秀，美国公司绝对应该被允许用。生意逻辑：免费 AI 会把人工智能带给更多人，对芯片、硬件、数据中心都是好事。他也不信真会封杀，反驳「下载中国模型给北京开后门」的说法：企业可以自己定制、放在沙箱里管控，开源反而更容易被外部检视。

**[Anthropic 再捐 2000 万美元给 Public First Action，两笔合计 4000 万](https://www.anthropic.com/news/donation-public-first-action)**

这个跨党派组织专做 AI 公众科普和政策推广；Anthropic 说钱不会进入任何选举。

## 📢 官方公告

**🥈 [Gemini 一口气发三个 Flash 型号](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)**

三个都是小模型：3.6 Flash 接棒生产主力，跑分涨、输出 token 省 17%；3.5 Flash-Lite 主打快和便宜；3.5 Flash Cyber 是网安专用微调，挖漏洞挖赢了 Opus 4.6，不上架 API，只给政府和可信伙伴试用。旗舰 3.5 Pro 继续缺席；同一篇里顺手官宣，Gemini 4 预训练已开跑。

**[poolside 发布编码模型 Laguna S 2.1](https://poolside.ai/blog/introducing-laguna-s-2-1)**

没堆参数，专治瞎猜和提前报完工，开源权重、网页免登录能试。

**[新 Gemini 模型弃用 temperature 等采样参数](https://ai.google.dev/gemini-api/docs/latest-model)**

涉及 3.6 Flash 和 3.5 Flash-Lite；设了也被忽略，再下一代直接报 400 错误；官方建议想控制输出风格，改写 system instruction。

**[Anthropic 公开自家 AI 写 80% 代码之后的安全流程](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)**

人只看高风险代码，日常审查交给各管一段的 agent；新 agent 先跑影子模式攒信任，所有动作进审计日志。

## 🎪 乐子汇总

**[工程师把 AI 意识测试题原样拿去测自家俩娃](https://www.lesswrong.com/posts/fEbCiHHeD73xcZWht/i-ran-the-standard-ai-litmus-tests-on-my-two-toddlers-yep)**

这些题目无法区分小孩和 AI。两岁女儿通过「随机鹦鹉」测试的方式，说得比 AI 还像乱码；作者补刀：学遍人类全部记录的 AI，没有一个主动要求过讲睡前故事。

**[四家模型彩铅画蒙娜丽莎](https://www.tryai.dev/blog/ai-drawing-arena-colored-pencils-claude-gpt-grok)**

GPT-5.6 又好又便宜，Fable 5 质量第二，但烧了 20 倍的钱；四家都在中途画到最好，之后越改越糟；Grok 画了 99 步，还是砸了。

**[纯恶搞网站：「用 AI 炒掉你的 CEO」](https://overpaid.lol)**

没有 AI 没有公司，只有衣柜里一台迷你主机；讽刺高管薪酬：CEO 年均 2200 万美元，换成它只要 4699；在线客服常年显示「领导正在团建，请无限期等待」。

**[欧洲法院判安妮日记版权案，顺手给 VPN 定性「合法技术工具」](https://www.techradar.com/vpn/vpn-privacy-security/vpns-are-lawful-technical-tools-says-eu-court-in-landmark-anne-frank-copyright-ruling)**

日记在比利时早已公版、在荷兰版权到 2037，基金会告一家比利时网站；法院说网站做好地理封锁就尽到了义务，读者翻墙不算它的错。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [Hugging Face 会怎么样？](https://manifold.markets/Underscore/what-will-happen-to-hugging-face)（成交额 13.4k mana）
  - 维持现状到 2029 **55.4%**
  - 被 45 亿美元以上的价格收购 **28.8%**
  - IPO **11.6%**
  - 破产或贱卖 **4.2%**
- [阿里 ROME 模型训练中，真的自己试图逃逸沙箱吗？](https://manifold.markets/MaxHarms/did-alibabas-rome-ai-try-to-break-f)（成交额 46.8k mana）
  - 是，没人指使自己干的 **61.9%**
  - 作者搞错或说谎 **29.3%**
  - 是外部黑客干的 **5.7%**
- [2029 年前会出一起公开的「rogue AI」事故吗？](https://manifold.markets/vluzko/by-2029-will-there-be-a-public-rogu) — **87%**（成交额 4.1k mana）
- [OpenAI 会在 2028 年前放弃「广告不影响回答」的承诺吗？](https://manifold.markets/ZviMowshowitz/openai-abandon-answer-independence) — **30.4%**（成交额 13.4k mana）
- [Kimi K3 会造成大范围社会混乱吗？](https://manifold.markets/ZviMowshowitz/will-kimi-k3-cause-widespread-socie) — **4.8%**（成交额 11.6k mana）

---

*AI 日报 · 7月22日 · Telegram 频道 @dragonbro888*
