# 折价倒卖 LLM token 的中继灰市

- 推荐强度: 强
- 档位线索: 主源（第 1 条）单独够银，若「独家视角」栏目把 4/5/6 一起摆出来（灰市 → 民用小工具 → 官方条款原文），整组的信息密度可以够金；纯当行业八卦看则降银。三样 GitHub/官方材料本身都不够牌，只作佐料。
- 涉及文章:
  - [An Inside Look at the Relay Market Powering Token Resellers and Fraud](https://vectoral.com/blog/token-relay-market) · Vectoral（Matt Lenhard）· 页面标注 June 28, 2026（**注意：作者本人 2026-07-26 15:17 UTC 才投到 HN，是旧文当天翻红，不是当日新发**）
  - [HN 讨论](https://news.ycombinator.com/item?id=49058993) · 提交人 mlenhard（即作者本人）· 2026-07-26 · 我核时 152 分 / 92 条评论（派活方给的是 146 分 91 评，说明还在涨）
  - [An Inside Look at the Relay Market...](https://simonwillison.net/2026/Jul/26/relay-market/) · Simon Willison 短评 · 2026-07-26
  - [hkc5/cursor-bridge](https://github.com/hkc5/cursor-bridge) · GitHub · 建库 2026-07-26，我核时 16 星
  - [wowyuarm/codex-proxy](https://github.com/wowyuarm/codex-proxy) · GitHub · 建库 2026-02-19，我核时 6 星
  - [Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan) · OpenAI 帮助中心 · 页面标「Updated: yesterday」
  - [OpenAI Services Agreement](https://openai.com/policies/services-agreement/) · Effective: January 1, 2026
  - [Terms of Use](https://openai.com/policies/row-terms-of-use/) · OpenAI 个人版条款

## 核心主张

Matt Lenhard 追查自己做 AI 网关时遇到的滥用，顺藤摸到一个中文论坛，画出了一条四层产业链：卡商/号商（虚拟卡 + 批量注册号）→ 账号池（聚合上百个号、管 token 和限速、故障转移，对外只出一个 API）→ 中转站（包成中文产品、微信群客服、比价竞争）→ 终端买家（中国开发者、初创、SaaS，以及做模型蒸馏的大买家）。他跟踪的中继里最狠的报价比官方牌价低 97.8%，前十家中继月访问量合计 360 万。他的判断是这事只会往应用层蔓延：「As Anthropic and others roll out KYC controls and identity verification, the abuse won't disappear, it will just move somewhere else.」

## 为什么值得看（钩子）

这是第一次有人把「为什么中文圈能买到两折不到的 Claude」这条链子从卡商画到蒸馏买家，还带价目表和月流量数字。配合 GitHub 上那两个「用订阅额度冒充 API」的小工具和 OpenAI 条款原文，等于把灰市、民用擦边、白纸黑字禁令三样并排摆在一起。

## 关键细节 / 引述

**主源（Vectoral，我逐句实读了全文）**

- **方法论**：不是卧底采买，是读论坛。作者原话：「While researching where the abuse was coming from, I stumbled onto a Chinese forum where operators openly discussed the relays and their methods.」文末 Sources 明确交代了唯一一手来源——V2EX 程序员节点的帖子《AI 中转站黑话大全》（<https://www.v2ex.com/t/1196011>），发帖人 v2exgo 自己就经营中转站 terminal.pub；帖子跑了 2026-03-05 至 06-23，约 3.5 万浏览、190 回复。所有引语都是他从这个帖子翻译的。另用了比价站 getcheapai.com、中继目录 hvoy.ai。
- **折扣榜（作者原表，"median discount from official list price"）**：Now Coding 97.8%、I Code Easy 97.1%、Claude ZZ 96.6%、Doro 96.4%、UoCode 96.3%，页面写「See all 49」，即共跟踪 49 家。
- **⚠️ 主源自带一处算术硬伤，别照抄**：文中说「$3,333 worth of official Anthropic credit for 425 RMB — roughly $0.13 of usage per $1 spent」。425 元约合 59 美元，59/3333 ≈ 1.8%，跟它自己的 97.8% 折扣榜对得上，跟 $0.13 对不上。HN 上 mmoskal 直接指出「425 RMB is about $59 so $1 of tokens for $0.017 not $0.13」，kristjansson 跟一句「seems like they missed a zero somewhere. its a dollar of usage for a penny and change」。作者 mlenhard 只回了「Yeah, I should probably clean this up. The sentence is a bit hard to understand.」——**我核时页面数字未改**。日报要用就用「低到官方牌价的 2% 左右 / 97.8% 折扣」，别引 $0.13。
- **另一处内部打架**：正文写 hvoy.ai 抽奖「258 people had entered 401 tickets for the fifty keys」，同页数据卡却写「A recent round 1,150 tickets」。两个数字我都实读到了，互相矛盾，建议只用「每天送 50 把面值 $100 的 API key」这个确定部分。
- **抽奖的「公平性表演」**（我认为是全文最好的细节）：中继目录 hvoy.ai 自称是「中继真伪核验 + 比价」工具，每天抽 50 把 $100 的 key，每日签到攒积分、20 分一张票、每轮最多买 3 张。而且抽奖是 provably fair——随机种子取最新比特币区块哈希，用 Partial Fisher-Yates 洗牌，抽前公示全部参与快照。作者原话：「The part that got me is the fairness theater.」
- **软件底座**：几乎所有中继跑在 one-api 或 new-api 上，都是 OpenAI 兼容网关，运营者部署面板、配「渠道（渠道 = 供应商 + 一池 key）」，按用量乘「倍率（multiplier）」扣费。作者跟踪的中继里 one-api 出现频率约为 new-api 的 4 倍。他特意撇清：「There's nothing inherently illicit about the software. one-api and new-api are neutral, legitimate tools.」越界点在于「when its channels are stocked with stolen, leaked, or pooled keys instead of the operator's own」。
- **池子里不只有实验室账号**：「Alongside direct OpenAI, Anthropic, and Google credentials are accounts harvested from the application layer.」论坛活动大量围绕对 Kiro、antigravity 这类消费级产品的「逆向」接入——**这一点正好是 4/5 两个 GitHub 项目的同类物**。
- **五种手法**（原文小标题）：free-trial abuse（批量注册薅免费额度再转卖）、chargeback attacks（用完就拒付，或干脆一开始就用盗卡）、prepaid cards、open inference（「Any support chatbot without strict guardrails is ripe for having traffic proxied through it.」）、denial of wallet（纯烧对方钱，无财务动机）。
- **买家动机三条**：便宜 token、绕地域限制、模型蒸馏。蒸馏那条的论坛原话（作者译）：「Distillation uses Claude/CodeX models to train domestic models... it's a multi-billion RMB industry chain, and many big players earn hundreds of thousands a day.」另一条：「I got 20TB on my first day online.」
- **规模**：「the ten highest-traffic relays we track pull a combined 3.6 million visits a month between them.」

**HN 讨论（92 条我全过了一遍，捞到的增量）**

- **作者自曝检测手段**：回复竞品 WorkOS 的 grinich 时，mlenhard 说「I don't think device fingerprinting is the right approach here... We use canary values to detect the resellers, and I believe that's the only approach that will actually work at scale.」并称「There are hundreds of listings for cursor tokens/credits right now.」（reliabilityguy 追问 canary 怎么做，没得到回答。）
- **作者预告下一篇**：namanyayg 说印度朋友靠反复注册壳公司薅 AWS/Azure 初创额度，拿到「4% of the actual price」的推理成本，「gave him an unbeatable competitive edge」。mlenhard 接：「I was going to cover this in a follow-up article, but yeah, there are network of token brokers who buy unused credits from startups and then resell them.」
- **有从业者背书这不新鲜**：wtobey1（自称在大型广告公司做过多年 financial integrity）说同样的转卖市场在上一代互联网巨头产品上早就存在，「Highly sophisticated actors, able to cobble together impressions through abuse of the billing systems, stolen financial instruments, taken over accounts, etc, create massive markets of discounted impressions for resale.」
- **评论区最大的分歧是定性**：\_\_MatrixMan\_\_ 主张「This is mere breach of contract」「Grey market, not black market」；tancop 分三档——盗卡是真欺诈、批量薅免费试用是灰色、正经买了订阅再转卖「not at all unethical, even if its breaking their terms」。Aurornis 长文反驳，核心一句：「The misunderstanding is that the price they paid was predicated on the specific use.」miki123211 的比喻更好用：订阅制像自助餐，实验室赌的是「every person needs to eat and sleep」，转卖方等于拎三个行李箱进店装满带走。
- **纯度问题（可作钩子）**：blfr 问买家怎么知道拿到的是不是真货，「You could easily sell Opus as Fable for a good while」；gruez 答「You can't, it's all reputation based. Similar to whether drug users don't really know what they got were diluted or not.」Havoc 同问。
- **1337h4xx 提了个没人回答的问题**：中转站是否把 agent 轨迹存下来当训练数据卖？文章没提，作者未回应。**属于未证实。**
- nojs 一句冷评：「Seems to be an LLM megaexpansion of the actual source (in chinese)」——即怀疑英文文章基本是那个 V2EX 帖的扩写。这跟作者自己在 Sources 里的交代基本一致。

**Simon Willison（2026-07-26，交叉验证）**

- 他基本是转述 + 两条自己的判断。他把重点落在暴露端点的风险上：「there's now an entire ecosystem that can profit from finding a new unprotected endpoint to exploit.」
- 结论句：「LLM vendors _really_ need to get better at offering strict caps for their API keys.」
- 他也点名了 one-api / new-api 两个仓库。标签：ai、generative-ai、llms、llm-pricing、ai-ethics、ai-in-china。

**4. hkc5/cursor-bridge（派活方给的两点，我复核）**

- ✅ 复核通过：Rust 单二进制；README 明写「Reads your Cursor auth token from macOS keychain (or CURSOR_TOKEN env var on Linux)」。
- ⚠️ **一处需要修正**：不是「把 Claude Code 的请求转去 Cursor 服务器」，README 的流程图写的是「Proxy translates Anthropic API calls → **Cursor agent CLI**」——它转给的是本机已登录的 Cursor `agent` 命令行，不是直连 Cursor 服务器。差别不大但表述要准。
- ✅ 免责原话完全一致，在 `## Legal` 下：「This project is not affiliated with Anthropic or Cursor/Anysphere. Use at your own risk.」
- **怎么装**：`cargo install cursor-bridge`，或从 Releases 下预编译二进制。前置条件：已装 Cursor 且 `agent` CLI 已登录（`agent login`）、已装 Claude Code CLI。只支持 macOS / Linux。跑法就是把 `claude` 换成 `cursor-bridge`。
- **卖点原话**：「Cursor's **Auto model** is included with your subscription — free, unlimited, no extra per-token cost.」「You want Claude Code's agent capabilities... without Anthropic billing」。
- **❌ 封号风险：README 完全没提。** Caveats 只列了三条技术限制（Linux 要手动给 CURSOR_TOKEN、没有工作区沙箱、单账号不支持轮换）。除了那句 MIT 下面的「Use at your own risk」，对违反 Cursor/Anthropic 条款、账号被封没有任何提示。这是我实读确认的「没有」，不是没查到。
- **数据（我核时）**：16 星、1 fork、0 issue、0 watcher。建库 2026-07-26 21:10 UTC，最后一次提交 2026-07-26 22:26 UTC（`fix: full agent mode with --force, temp dir sandbox`）。**也就是说这个仓库昨天才建，star 数会飞快变动，日报若引用务必标时点或干脆别报数。**「单账号，暂不支持多账号轮换（no multi-account rotation (yet)）」这句 caveat 挺有意思——它承认了轮换是可以想象的下一步。

**5. wowyuarm/codex-proxy（派活方给的两点，我复核）**

- ✅ 复核通过：本地代理，架构图明写走 `chatgpt.com/backend-api/codex/responses`；对外出 OpenAI 兼容的 `/v1/chat/completions`、`/v1/responses`，另有 `/v1/messages` 是给 Claude Code 用的 Anthropic Messages 兼容层。README 第二句：「It also exposes a minimal Anthropic Messages API shim so Claude Code can use the same local proxy and still spend your ChatGPT Codex quota.」
- ✅ 免责原话完全一致，在 `## Disclaimer` 下：「This project uses the unofficial ChatGPT backend API (`chatgpt.com/backend-api`). It is not endorsed by OpenAI and may break at any time. Use at your own risk.」
- **数据（我核时）**：6 星、1 fork、无 LICENSE。建库 2026-02-19，最后一次提交 2026-04-09（`Fix unsupported Responses compatibility parameters`）——**已经三个半月没动，是个半停摆项目**，跟 cursor-bridge 的「昨天刚建」形成对比。
- **我新查到、派活方没提、且跟主源直接呼应的三点**：
  1. **它自带多账号池的雏形**：`codex-proxy login` / `accounts` / `switch <account-id>` / `accounts --remove`，多个登录快照存在 `~/.codex-proxy/accounts/`，`accounts` 还会显示每个号的用量。这就是主源说的「账号池（账号池）」的单机迷你版。
  2. **它明确做了反机器人绕过**：How It Works 第 3 条原话「**TLS fingerprint** — uses `curl_cffi` with Chrome impersonation to bypass Cloudflare bot detection」。这一条比免责声明重要得多——它不是「非官方接口可能挂」，是主动伪装浏览器指纹绕过检测。
  3. **默认监听 `0.0.0.0:8787`**，README 直接给了通过 Tailscale 让远程机器共用的用法，并提供 `HTTPS_PROXY` 配置给「in a region that requires a proxy to access OpenAI services」的用户。也就是说从单机自用到小范围共享，只差一个端口。
- 模型映射也值一提：`claude-opus*` → `gpt-5.4`、`claude-sonnet*` → `gpt-5.3-codex`、`claude-haiku*` → `gpt-5.4-mini`。呼应 HN 上「你怎么知道买到的是不是真货」那条——这里连伪装都是写在 README 里的。

**6. OpenAI 官方口径（派活方 WebFetch 吃 403，我换了可读镜像拿到全文；openai.com 和 help.openai.com 对 curl/WebFetch 一律 403）**

- **⚠️ 派活方要确认的那条事实，需要按当前页面修正**。现在的原话是：「Codex is included across ChatGPT plans, **including Free and Go**. Usage limits vary by plan.」接入方式确实是「Sign in with your ChatGPT account」，客户端列了 ChatGPT 桌面版（Codex mode）、**Codex CLI**、IDE 插件、Codex web。所以「Plus/Pro/Team 用 Sign in with ChatGPT 就能在 Codex CLI 里跑」成立，但**「只有 Plus/Pro/Team」不成立**（免费版和 Go 也含）。
- **「不额外收费」这个说法要打折**：页面只说 included + 用量上限按套餐不同，并且明确「Usage from Codex, ChatGPT Work, ChatGPT for Excel, and Workspace Agents draws from the same agentic usage and credit pool」，以及「Some Plus and Pro users can add credits to continue using Codex; other users may need to upgrade or wait for the limit to reset.」——即包含在订阅内、但有额度池，超了要买 credits / 升级 / 等重置。页面还有「referral 可以攒一次 rate-limit reset」这种设计。**日报若要写「订阅额度免费跑 Codex」，建议写成「包含在订阅内、按套餐设用量上限」。**
- 该页自己交代适用条款：「the ChatGPT [Terms of Use] and [Privacy Policy]—or the corresponding [online services agreement] for OpenAI API and ChatGPT Enterprise, Education or Business Users」。
- **禁止转售 / 禁止凭据共享 / 禁止给第三方供能的原文（这是本组最硬的可点出处）**：
  - **OpenAI Services Agreement（Effective: January 1, 2026）§3.1 Customer Account**：「Customer will not share Account access credentials or individual login credentials between multiple users. **Customer may not resell or lease access to its Account or any End User Account.**」→ <https://openai.com/policies/services-agreement/>
  - **同协议 §3.3 Restrictions**，一口气命中四项：「(e) except for a Permitted Exception, use Output to develop artificial intelligence models that compete with OpenAI's products and services;（对应主源说的蒸馏）... **(g) buy, sell, or transfer API keys from, to, or with a third party**;（对应卡商/号商）(h) interfere with or disrupt the Services, including circumvent any rate limits or restrictions or bypass any protective measures or safety mitigations for the Services;（对应 codex-proxy 的 Cloudflare 绕过）**(i) violate or circumvent Usage Limits or otherwise configure the Services to avoid Usage Limits.**（对应把订阅额度包成 API）」
  - **个人版 Terms of Use，Registration 段**：「**You may not share your account credentials or make your account available to anyone else** and are responsible for all activities that occur under your account.」；"What you cannot do" 列表里还有「Modify, copy, lease, sell or distribute any of our Services.」和「Automatically or programmatically extract data or Output」。→ <https://openai.com/policies/row-terms-of-use/>
  - 另有一篇专门的帮助中心文章 **OpenAI Account Sharing Policy**（<https://help.openai.com/en/articles/10471989-openai-account-sharing-policy>，标 Updated: 12 days ago），措辞很软，只讲「Your OpenAI account is meant for you—the individual who created it. If someone else needs to use OpenAI's products, they should sign up for their own account.」，理由列的是安全风险/滥用风险/个性化，**没有提封号或法律后果**。硬条款在 Services Agreement，不在这篇。
- **没查证到的**：Anthropic / Cursor 侧对应的条款原文我没查（不在派活范围内）；OpenAI 有没有实际因转售封号的公开案例，我没找到，未查证。

## 与近期的关系

- **本频道近期没做过这个题**。唯一沾边的是 07-24 口播稿第一条（LessWrong 提醒用 OpenRouter 这类中转平台跑实验要锁死 provider，否则量化精度差异能让基准分差 16 个百分点）——那条讲的是**合规聚合平台的路由质量**，跟本组的**灰市账号池**是两回事，只是「中转」这个词撞车。写手若同时提到，建议明确区分，别让读者以为 OpenRouter 也在灰市里。
- **时效性有个坑**：主源页面标 June 28，是 7 月 26 日作者自投 HN 才火的。日报若写「今天有篇调查」，措辞用「一篇上月的调查昨天在 HN 冲上前排」更准确。
- 主源作者已预告续篇（收购初创闲置云额度的 token 经纪人网络），可留作后续跟踪线索。
- cursor-bridge 是 7 月 26 日新建仓库，属于当日新鲜物；codex-proxy 是 2 月的老项目、4 月起停更——两者放一起能说明「订阅额度套壳」这条路子不是新发明，只是最近又被翻出来。
