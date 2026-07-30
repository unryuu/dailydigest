## 🗞️ 行业大事

**🥇 [MCP 重要新版本：无状态协议核心](https://blog.modelcontextprotocol.io/posts/2026-07-28/)**

删掉了握手和会话头，每个请求自带协议版本和客户端身份，纯请求应答。MCP 服务器从此能当普通 HTTP 服务部署。旧写法还能用，官方给了至少 12 个月缓冲期。

这次发布让 MCP 更像标准的 Web 基础设施：无状态、可缓存、可路由，方便企业级大规模部署。

**🥈 [Anthropic 用 Mythos 找出两套密码算法的数学缺陷](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/)**

一个针对签名方案 HAWK ，能把有效密钥强度砍掉一半；另一个针对弱化版 AES ，能把攻击速度提高数百倍。两个研究都对现在的生产系统没有影响。公开了提示词原文，模型反复认定这事做不到、想放弃，人类把它按回去接着干。

**🥈 [OpenAI 发布安全扫描工具 Codex Security](https://github.com/openai/codex-security)**

能查找、验证、修复代码里的安全漏洞，定位是防御工具。HN 实测一次扫描能烧掉小半周的订阅额度，还有人扫了四十多分钟，结果被模型自己的护栏拦住，拒绝输出。

**[吴恩达开了家新公司 LearnVector，做一对一的 AI 教学](https://learnvector.ai/)**

给每个人规划学习路径、按各自的节奏教到学会为止。产品要到 2027 年初才亮相，现在只有官网和融资。Coursera 投了 1 亿美元。

## 📖 深度长文

**🥈 [Transluce 要专门训一个做监督的基础模型](https://www.lesswrong.com/posts/AqdZKyoRmN6EFCzib/foundation-models-for-oversight)**

训练语料是对被查模型做的海量实验记录，目标规模约 1T token。要查的问题：模型会不会故意藏拙、有没有不肯明说的目标、会不会看人下菜碟、思维链是真在推理还是事后找补。昨天报的那篇管「怎么安全地用不可信的模型」，这篇管「怎么把模型查清楚」，同一条赛道的两条互补路线。

**🥈 [有人拆解 Kimi K3 架构，发现没有使用位置编码](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html)**

把输入压缩到一个更小的潜在空间，大幅下降计算量。将多头潜在注意力，和固定大小的线性注意力混合，这个架构自带先后顺序，就不再需要位置编码了。让注意力残差跨层传递信息，用 4% 的训练成本，换来小幅度的性能提升。

**[美国生产率暴涨，AI 只占一部分功劳](https://www.stripeeconomics.com/p/ai-and-productivity)**

过去一年美国每小时产出涨 2.5%，二十年年均只有 1.6%。主要原因是企业把建好的厂房和服务器用得更满。

## 🧪 新鲜论文

**[HiFi-UMI：只拿手持夹爪采集数据，全程不用机器人](https://huggingface.co/papers/2607.25895)**

人类拿着这只带传感器的夹爪，就能采数据。训出的策略和真机操作数据打平。

**[搜索 agent 按什么顺序翻阅语料](https://huggingface.co/papers/2607.24223)**

先用相关性给整个语料库排名，让 grep 按名次往下扫，命中的片段再重排一遍。搜索基准上准确率从 78% 提到 84%，工具调用还更少。

**[agent 记住了你说过的事，却不会在该用的时候用](https://huggingface.co/papers/2607.24368)**

直接问事实，全能记住，但拐个弯才用得上的问题，最高只有 14.4%。比如前面说家里有百合花，又问能不能养猫，它想不到百合对猫有毒。

## 🏛️ 监管动向

**🥇 [黄仁勋与美国商务部长会面](https://www.axios.com/2026/07/28/nvidia-jensen-huang-lutnick-meeting-china-ai)**

特朗普政府正在敲定一个框架，让政府在最先进的 AI 模型发布前，获得早期访问权限。政府预计将在 8 月 1 日前公布此框架。

黄仁勋本周在华盛顿密集会见各方。此前，官方证实正在调查英伟达芯片出口的潜在违规行为。公司发言人则表示，黄仁勋此行是与两党多位议员讨论英伟达未来在美国本土的产能与供应链，以及美国在 AI 领域的领导地位。

## 📌 行业简讯

- [OpenAI 加 Anthropic 年化收入超过星巴克加麦当劳](https://www.axios.com/2026/07/28/anthropic-openai-revenue-mcdonalds-starbucks-yum)
- [新编码器在 CPU 上跑长文本，快 3.7 倍](https://huggingface.co/blog/LiquidAI/lfm2-5-encoders)
- [开源天气模型，普通显卡和 CPU 也能跑](https://huggingface.co/blog/hugging-science/run-aifs-yourself)
- [uv 0.12 让新建项目的默认结构更正规了](https://simonwillison.net/2026/Jul/28/uv/)

## 🎪 乐子汇总

**🥈 [Substack 写作者应该赶紧去搞自己的网站](https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/)**

在别人的平台上攒读者，你是租客不是房东；用 xx.substack.com 这种子域名，内容都记在平台名下。应该先发自己的站，再同步到各平台，用平台找人。

**[有本杂志以「报导比别人晚」为荣](https://www.slow-journalism.com/)**

Delayed Gratification 自称世界上第一本慢新闻杂志，一个季度出一本，专门回头写上个季度已经吵完的那些事。

**[有人把《半条命》移植到了 Mac OS 9](https://mac-classic.com/news/half-life-ported-to-mac-os-9/)**

基于原引擎的开源重写版做的，老 Mac 装上就能玩，还带两部资料片。显存不到 8MB 的 iMac 会吃力。

**[心理学研究大体上没问题](https://www.astralcodexten.com/p/psychology-research-is-mostly-fine)**

教科书只有一章的槽点比较多，剩下大部分都挺正常的。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [AI 能在今年内解决一道千禧年难题吗？](https://manifold.markets/jim/ai-solves-millenium-prize-problem-i) — **9.5%**（成交额 21.8k mana，一天内就成交了 1 万，全池最热。千禧年难题是七道悬赏百万美元的数学题，二十多年只解了一道）
- [2030 年 3 月前，AI 能写出一篇顶刊级别的数学论文吗？](https://manifold.markets/TamayBesiroglu/will-ai-be-capable-of-producing-ann) — **96.0%**（成交额 676.5k mana 的大盘。和上一条并排看：写出顶刊论文 96%，解掉千禧年难题 9.5%。7 月 17 日我们报过一次，那时是 90%）
- [2028 年前能造出 1 万台人形机器人吗？](https://manifold.markets/RemNi/will-10k-humanoid-robots-be-manufac-26fcd74c767f) — **99.0%**（成交额 15.2k mana。市场几乎不把这当成一个问题了）
- [10 月 20 日前会出现一次 AI「警告射击」吗？](https://manifold.markets/LeoGao/will-there-be-a-warning-shot-before) — **12.3%**（成交额 10.1k mana，开盘人是 OpenAI 研究员。「警告射击」意思是把所有人吓醒的安全事故；HF 入侵闹了三周，概率仍停在一成出头）

---

*AI 日报 · 7月29日 · Telegram 频道 @dragonbro888*
