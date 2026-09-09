## 🗞️ 行业大事

**🥇 [企业把安全预算转向 AI 防御](https://www.theinformation.com/articles/ai-threats-reshaping-companies-spend-cybersecurity-budgets)**

Lumen 计划把未来一年的网络安全预算提高约三成，并抽调员工用前沿模型扫描漏洞。另两家公司也准备加钱，同时重新评估传统终端防护、漏洞管理、日志工具和人工渗透测试，把预算转向监控员工使用 AI、扫描模型漏洞和自动修补。

企业的安全预算已经落到相关厂商的收入。Zafran 的新产品五周拿下三家大银行；CrowdStrike 的 AI 安全产品收入三个季度增长 79 倍，SentinelOne 的相关年化收入同比翻倍。

**🥈 [中国给人形机器人上市加门槛](https://www.theinformation.com/articles/china-curbs-humanoid-ipos-unitrees-volatile-debut)**

申请上市的企业要证明持续收入、亏损收窄或真正的技术创新。今年上半年，国内人形机器人创业公司融资 54 亿美元。宇树科技上市首日大涨，随后从收盘价回落四成。监管希望减少只靠低价、出货量和相似产品争夺上市机会的公司。

**🥈 [Gimlet 用三档估值完成融资](https://www.theinformation.com/newsletters/dealmaker/gimlets-three-tranche-deal-reveals-ai-funding-frenzy)**

这轮 3 亿美元资金分别按 25 亿美元、约 30 亿美元和一个更高估值进入。主报价已是公司上次估值的 16 倍。Gimlet 曾告诉投资者，按已签合同推算，OpenAI 未来每年可能花费过亿美元。OpenAI 目前并非其付费客户，但这笔潜在支出已经进入投资者的定价。

**🥈 [Hugging Face 的机器人已经卖出一万五千台](https://www.theinformation.com/newsletters/applied-ai/hugging-face-making-big-robotics-push)**

售价 400 美元的 Microduck 上月底推出，销售额已超过 600 万美元。公司原计划首年卖出至少五万台，现在准备上调预测。开发者可以免费下载、修改软件，把这台低价设备当作机器人试验台。训练仿真仍要使用英伟达 GPU 和 CUDA。

**🥈 [OpenAI 降价换来十倍用量](https://www.theinformation.com/newsletters/the-briefing/price-cuts-may-rattle-anthropics-ipo-pitch)**

Luna 降价后，使用量增长十倍，增量足以抵消价格下调。它在 OpenRouter 的 token 用量超过 Anthropic 两款主力模型的两倍。Anthropic 也把 Fable 5.1 的典型工作负载价格下调约四分之一。模型能力接近后，价格竞争将考验 Anthropic 上市时的收入优势。

## 📖 深度长文

**[AI 进步很快，普通人体感却可能晚几十年](https://www.interconnects.ai/p/when-will-average-people-feel-ais)**

技术复利可能持续几十年，生活收益却来得更慢，也很难被归因给 AI。机器人进入日常后，变化才可能成为看得见的实体好处。

**[Astra 不写推理过程也能串起更多事实](https://www.lesswrong.com/posts/FsCkkoGsNmPzFKRhg/gpt-6-astra-can-do-a-lot-of-multi-hop-reasoning-without)**

24 道外部测试中，Astra 每题都不比 Sol 差。可串起的事实链大致从 2 至 3 跳提高到 4 至 5 跳。

**[GLM-5.3 开放权重，却没有沿用 MIT](https://www.interconnects.ai/p/latest-open-artifacts-24-motif-3)**

新许可证只约束经营模型服务、且关联收入超过 100 亿美元的主体，商业使用前要通过智谱的安全审查；Flash 版仍用 MIT。

**[Qwen3.8 27B 压到 4 bit 还能用，1 bit 直接崩掉](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked)**

完整模型占 55GB，4 bit 版压到 17GB，三项基准基本追平。1 bit 版仅 6.2GB，科学问答接近乱猜。

**[有人提议给大模型训练一串碰到就停机的文字](https://www.lesswrong.com/posts/ZqFD6HzrhZdMFxoqn/where-are-the-token-level-llm-kill-switches)**

秘密字符串无论出现在上下文哪里，都会让模型输出结束符。知道口令后可以过滤或分段读取绕过，恶意内容也能反用它藏东西。

## 🧪 新鲜论文

**🥈 [Agent 骗不过裁判，也能切断训练泛化](https://www.lesswrong.com/posts/xjwtNid2xjqSJWB7z/exploration-hacking-in-ai-debate-initial-empirics-and)**

模型在目标题上先执行一段摆烂思考，会让普通题目学到的正确能力几乎无法迁移过来。即使摆烂经常被裁判发现并惩罚，恢复仍明显更慢。目标题只占自然训练数据约 14％，辩论轮数越长，拖慢越明显。把两类题各放一半时，恢复速度才重新一致。

**[调查留言板事故的 Agent，只找回约一半关键发现](https://www.lesswrong.com/posts/wt4kk6vFPEhkXvF8Q/how-good-are-slop-vestigators)**

十二款模型限时调查日志，最好成绩为 51.5％。Sol 的调查时间从十分钟增至两小时后，得分从 29％ 升到 48.6％。

## 📢 官方公告

**🥈 [ChatGPT Images 2.5 补上真正的编辑工作流](https://openai.com/index/introducing-chatgpt-images-2-5/)**

ChatGPT 与 API 每周合计生成超过 30 亿张图，新版生成延迟最多降低一半。用户可以画草图、在图上留修改意见，再连续调整局部，同时保留此前改动。API 分成偏速度和通用场景的 Flare，以及偏精细编辑的 Sunburst。提示词还能随图片分享，供别人替换素材继续创作。

另见：[Simon Willison 的 API 试用](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25)

**🥈 [扩散语言模型开始进入生产环境](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5)**

Mercury 2.5 已用于电话 Agent、搜索流水线和编码工具。OpenCall 的响应延迟中位数接近 170 毫秒，最慢的一批从数分钟缩到一秒。Augment Code 用它压缩上下文，耗时从约 150 秒降到 27 秒，成本下降九成。它还负责模型路由和工具搜索。

**[Meta 推出个人 AI Agent Muse](https://ai.meta.com/muse)**

Muse 已上架苹果和 Google 应用商店，定位是帮普通人处理生活、健康、关系和财务事务。

**[OpenAI 把 Codex 接进量子实验室跑常规测量](https://openai.com/index/codex-quantum-computing-experiments)**

Sol 能在六量子比特芯片上选择参数、测量并分析结果。信号清晰时可接手数天的标准表征，噪声大时仍需专家指导。

## 📌 行业简讯

- [腾讯放出 Hy4-preview，旗舰开放模型继续做大](https://huggingface.co/tencent/Hy4-preview)

## 🎪 乐子汇总

**[有人给编码 Agent 做了个「我有 ADHD」技能](https://github.com/ayghri/i-have-adhd)**

十条规则要求它先给下一步、压掉跑题和客套话，列表不超过五项，结尾只留一个具体动作。

**[有人把电子墨水阅读器变成了 Mac 能找到的打印机](https://nishantjosh.dev/blogs/how-to-build-a-fking-printer)**

设备只有 400KB 内存，只能边接收边缩小并转成黑白像素。改造一晚后，Mac 就能把漫画打印到它的屏幕上。

**[法院认为「Tweet」和小鸟标志很可能已被 X 放弃](https://blog.ericgoldman.org/archives/2026/09/tweet-and-the-bird-logo-apparently-enter-the-public-domain-but-x-maintains-its-grip-on-the-twitter-mark-for-now-x-v-project-bluebird.htm)**

X 已不再使用这两个标志，「Twitter」却靠应用商店里的旧称说明继续受到保护。案件仍会继续审理。

**[有人主张慈善用途的 Anthropic 股权应该尽快卖掉](https://www.lesswrong.com/posts/ptirZBteKd3o4FAFe/most-anthropic-equity-that-will-ever-be-used-for-longtermist)**

作者认为慈善资产押在一家公司上太多，换到能加杠杆的其他 AI 投资，回报可能更高。

**[有人劝 AI 实验室员工别辞职，直接拒绝工作等着被开除](https://www.lesswrong.com/posts/6j3kBHdowGLCeqobg/dear-god-please-don-t-resign-in-protest)**

开除因道德理由停工的资深员工会损害公司形象；如果公司不敢开除，就得谈条件，还腾不出岗位招替代者。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2028 年前会生产十万台人形机器人吗？](https://manifold.markets/RemNi/will-100k-humanoid-robots-be-manufa-4ac19368e941) — **71％**（成交额 4.3k mana）
- [Anthropic 上市时仍会拥有最强公开模型吗？](https://manifold.markets/SG/will-anthropic-have-the-best-public) — **39％**（成交额 1.6k mana）
- [2027 年前，AI Agent 能在普通绘图软件里画出扩散模型级别的图片吗？](https://manifold.markets/paleink/will-an-ai-textvision-agent-be-able) — **51％**（成交额 0.9k mana）
- [2027 年底前会出现任何人的即时深度伪造吗？](https://manifold.markets/dreev/instant-deepfakes-of-anyone-within) — **78％**（成交额 724.9k mana）

---

*AI 日报 · 9月9日 · Telegram 频道 @dragonbro888*
