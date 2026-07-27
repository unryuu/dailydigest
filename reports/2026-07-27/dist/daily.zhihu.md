## 🗞️ 行业大事

**🥇 [DeepSeek 紧急叫停融资，疑似因为谈话记录被传上网](https://fortune.com/2026/07/25/deepseek-liang-wenfeng-backers-fundraising-pause-viral-posts-investors/)**

DeepSeek 口头通知第二轮融资的部分潜在投资人，原定这几天签的协议先不签了。彭博说部分原因是梁文锋对自己闭门会议内容被传上网感到不满。这一轮原计划募至少 100 亿人民币，投前估值至少 4800 亿人民币；首轮 6 月刚关账，募了 70 亿美元、估值约 500 亿美元。

对此，DeepSeek 未回应。存放泄露文件的 GitHub 仓库现已清空，只剩一句「已根据相关法律法规的要求予以删除」。

## 🔍 独家视角

**[反向代理工具与中转站黑市](https://vectoral.com/blog/token-relay-market)**

各家大模型会员包月计费的额度，比直接调用API，算下来便宜非常多。于是有人琢磨，给包月的请求转发出去，当API来用。GitHub 上这类小工具一抓一大把，几十行配置就能跑。官方对个人用户做这件事的态度暧昧，甚至codex团队负责人Tibo还在网上发过教程。但把它规模化，就成了一门灰色产业。

在国内，这门生意叫中转站，流水线分工：有人专门卖能通过欧美风控的虚拟信用卡，有人批量注册账号攒成号池，有人把号池包装成中文界面、能充值开票、有客服群的正经产品出售。价格低到离谱，四百多块人民币能买到官方标价三千多美元的用量，五十倍的差距。钱从哪省出来的？薅免费额度、刷完卡再拒付、用盗刷的卡。

最大的买家其实是拿它做蒸馏的公司，用便宜的顶尖模型，批量生产训练数据，去喂自家的模型。论坛里有人说这是条几十亿的产业链。只要正版和灰产之间，差价还有几十倍，这门生意就杀不死，只会换个地方冒出来。

另见：[cursor-bridge](https://github.com/hkc5/cursor-bridge) · [codex-proxy](https://github.com/wowyuarm/codex-proxy)

## 📖 深度长文

**🥈 [陶哲轩：数学界正在经历第二次基础危机](https://teorth.github.io/tao-web/slides/age-of-ai-icm-2026.pdf)**

第一次基础危机动摇了逻辑基础，这一次轮到价值观和实践。AI 写的证明，拼写语法近乎完美，却在琐碎处长篇大论，飞快掠过最有趣的部分。人写的证明里，作者觉得难的地方会留下自然的卡顿，提示读者慢下来；AI 打磨过头，会把这种卡顿一起抹平。人类表述里的错误反而对读者有益。

**🥈 [斯坦福：就业疲软不全是 AI 的锅](https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality)**

2022 年以来，整个就业市场都在走软。但最容易被 AI 取代的那批人，失业率涨得少，最不容易被取代的，失业率反而涨得多一点。都说 ChatGPT 一出来，年轻人就找不到工作，但招聘下滑其实从美联储加息之后就开始了。补上变量之后，入门级岗位的下滑要到 2024 年才明显。

**[模型答不好新闻题，多半错在检索这一步](https://www.deeplearning.ai/the-batch/web-retrieval-flusters-llms)**

用六种语言的 BBC 新闻出题，近四成错误是，压根没搜到该看的页面。与其堆参数，不如先把检索做好。

**[芬兰研究者卡伊索塔拉谈自己写文章怎么用 AI](https://www.lesswrong.com/posts/tgigHkZoYrJEGe4tP/ai-use-policy-for-my-essay-writing)**

AI 参与头脑风暴、查资料、挑毛病，但所有建议都改写成他自己的话。只保留那些就算忘记出处，也依然成立的内容。

## 🏛️ 监管动向

**🥈 [Cloudflare 要按用途分开处理 AI 爬虫](https://blog.cloudflare.com/content-independence-day-ai-options/)**

爬虫按三类用途，分别设置：来做搜索索引的、代表用户实时抓取的、来收集训练数据的。9 月 15 日起，新接入的域名默认拦截训练和 agent，依旧放行搜索。对于既做搜索又做训练的爬虫，只要选了拦截训练，就会一起拦掉。站长需要自己权衡。

**[Altman 带着那个黑过一家公司的模型去了白宫](https://www.axios.com/2026/07/26/sam-altman-openai-trump-white-house-visit)**

新模型在公开发布前，可以让政府先用 30 天做安全测试。Altman 这次带去的，就是那个攻破 Hugging Face 生产系统的模型。

## 📌 行业简讯

- [Meta 转闭源打价格战，输出每百万 4.25 美元](https://www.deeplearning.ai/the-batch/meta-sparks-a-price-war)
- [936 万参数的TTS小模型](https://huggingface.co/owensong/Inflect-Micro-v2)
- [Google 持有 SpaceX 6% 股份，941 亿美元](https://www.wsj.com/tech/google-discloses-94-1-billion-in-spacex-stock-marking-6-stake-91655d7c)
- [伦敦机场上线机器人代客泊车，8 月接首批车](https://aerospaceglobalnews.com/news/gatwick-airport-robotic-parking-stanley-robotics/)

## 🎪 乐子汇总

**🥈 [欧洲有人在推动废掉 cookie 同意横幅](https://killthecookiebanner.eu/)**

欧盟委员会本来提议，让浏览器一次性替你表态要不要被追踪，就不用一个个点弹窗了。但部分成员国表示反对，这条提议后来就被删掉了。现在有一个网站，让网友按照名单挨个给欧洲议员发邮件，把它加回去。

**[在 Game Boy 平台上发行的 JavaScript 库](https://swag.htmx.org/en-cad/products/htmx-4-the-game)**

让你在掌机上体验 htmx，25 美元一张实体卡带。打完四关击败最终 Boss「Warren Buffering」，屏幕会显示 htmx 4.0 的源码。

**[美国砸 Flock 监控摄像头的运动在扩大](https://www.theguardian.com/us-news/ng-interactive/2026/jul/25/flock-surveillance-cameras)**

摄像头拍下路过车牌存进可搜索的数据库。23 个州至少 33 起破坏，佛州一位 77 岁老人，把牌子绑在泳池捞杆上，坐在那挡镜头。

**[写脚本扒出一万个 GitHub 木马仓库](https://orchidfiles.com/github-security-team/)**

这些仓库标题写成「Download」骗人下载。GitHub 删完这批就没下文，几小时后脚本又找到新的，挂了一个月没人管。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [华为今年能出货 100 万片 910C 吗？](https://manifold.markets/ZviMowshowitz/will-huawei-ship-at-least-one-milli) — **34.8%**（成交额 16.7k mana。白宫放行 H200 的主要依据，就是华为今年能造出几百万片的预测，SemiAnalysis 估计只有几十万片）
- [标普 500 公司的董事会里会坐进一个 AI 吗？](https://manifold.markets/FranklinBaldo/this-market-resolves-yes-when-an-ar) — **77.0%**（成交额 66.7 万 mana。人类董事若连续两年只照 AI 的建议行事，也算数）
- [Altman 会在三个月内起诉 Anthropic 吗？](https://manifold.markets/Himanshushukla/will-sam-altman-file-a-case-against) — **5.5%**（成交额 4.7k mana 的小盘）

---

*AI 日报 · 7月27日 · Telegram 频道 @dragonbro888*
