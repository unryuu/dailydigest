# AI 日报信息源清单（sources.md）

> 本表是**人类可读总览**（用户拍板 2026-07-23 起恢复维护：**每次调整信源，改 meta.json 的同时必须同步本表**）。机器运行时以各源文件夹下的 `sources/<slug>/meta.json` 为准（含抓取地址、检查频率、权重）。本表与 meta 若有冲突，以 meta 为准。当前共 **33 源**（25 博客/RSS/API + 7 个 X 账号 + 1 个线索源）。
>
> 运作方式：scout **每天全量扫全部 33 源**，没有「隔几天才看一次」的源。下面的分组只决定一件事——**判新窗口**，即回看多久以内的内容算「新」（高频源通常 36-48 小时、周刊/不定期源 168 小时、低频源 720 小时），窗口内且不在 `seen.json` 里的才收。所以月更博主哪天诈尸更新，当天就能收到。流程详见 `RUNBOOK.md` / `HANDOFF.md`。

## 筛选偏好（全局）

- 偏爱"讲范式、讲反直觉"的内容：与主流说法拧着来的观点、纠正常见误解的点，单独标记并加权
- 不要四平八稳的摘要，每条要给出"为什么值得看"的钩子
- 纯产品营销稿、融资新闻、跑分通稿降权

## 抓取方式说明

- `rss` / `api`：结构化、带绝对日期、最稳，优先走这个
- `html`：没有 RSS 的源，直抓索引页（Anthropic / The Batch / Thinking Machines / neodrop）
- `nitter-html`：X 账号走 nitter 镜像的 HTML 时间线（X 无登录抓不到，官方接口已死）；串行慢抓、只收原创，解析脚本 `scripts/parse_nitter.py`
- 真正"精读全文"只对落进窗口、且权重高或看着有料的少数几篇做；其余给摘要级钩子即可

---

## 高频源（判新窗口 36 小时，撑起日报的主力）

| 源 | 主页 | 抓取URL | 方式 | 权重 | 节奏 |
|---|---|---|---|---|---|
| Simon Willison | https://simonwillison.net/ | https://simonwillison.net/atom/everything/ | rss | 高 | 每天 1-5 篇，全天滚动 |
| Hacker News | https://news.ycombinator.com/ | https://hn.algolia.com/api/v1/search?tags=front_page | api | 中 | 实时聚合；只挑 1-2 条 AI 相关高票 |
| OpenAI Blog | https://openai.com/news/ | https://openai.com/blog/rss.xml | rss | 中 | 每天 1-4 篇（官网 403，必须走 RSS） |
| Anthropic Blog | https://www.anthropic.com/news | https://www.anthropic.com/news | html | 高 | 2-3 天一篇，常成簇，无 RSS |
| Hugging Face Blog | https://huggingface.co/blog | https://huggingface.co/blog | html | 中 | 每天 1-4 篇（社区博客）；日期是相对时间戳，过滤略糙 |
| Don't Worry About the Vase (Zvi) | https://thezvi.substack.com/ | https://thezvi.substack.com/feed | rss | 高 | 每 2-4 天一篇，高产无固定日 |
| Axios | https://www.axios.com/ | https://api.axios.com/feed/ | rss | 中 | 新增 2026-06-17 补时效性；全站综合 feed，scout 过滤 AI/科技；快讯短、偏事件时效 |
| LessWrong | https://www.lesswrong.com/ | RSS（30+ karma 过滤） | rss | 高 | 新增 2026-07-04；Zvi 上游一手，AI 进精读、怪帖进乐子 |
| Astral Codex Ten (Scott Alexander) | https://www.astralcodexten.com/ | https://www.astralcodexten.com/feed | rss | 高 | 新增 2026-07-04；理性主义杂文，多进乐子 |
| Manifold Markets | https://manifold.markets/ | API | api | 中 | 新增 2026-07-04；赔率盒子唯一来源，不做 seen 去重 |
| HuggingFace Papers | https://huggingface.co/papers | https://huggingface.co/papers | html | 高 | 新增 2026-06-28；每日论文榜，补研究/中国实验室盲区 |
| claude.com/blog | https://claude.com/blog | https://claude.com/blog | html | 极高 | 新增 2026-06-28；工程方法论，有新内容一律精读 |
| xAI News | https://x.ai/news | https://x.ai/news | html | 中 | 模型、产品和公司公告；403 时浏览器兜底，普通营销稿降权 |

## X 账号源（判新窗口 36 小时 · 2026-07-23 新增）

> 抓取走 nitter 镜像的 HTML 页（当前 `nitter.kareem.one`，无登录可达；官方接口和其他镜像 2026-07 实测全灭）。**镜像是社区单点**，死了去 status.d420.de 找活实例、统一改各 `x-*` meta 的 fetch_url。抓取规矩（串行慢抓/只收原创/线程聚合）见 `pipeline/scout.prompt.md`，解析脚本 `scripts/parse_nitter.py`。

| 源 | 主页 | 抓取URL | 权重 | 节奏/口味 |
|---|---|---|---|---|
| Karpathy | https://x.com/karpathy | https://nitter.kareem.one/karpathy | 极高 | 原创 1 条/9 天；方法论/工作流，一更必看（博客源另在下方低频区） |
| Ethan Mollick | https://x.com/emollick | https://nitter.kareem.one/emollick | 高 | ~13 条/天；论文转述，线程碎、聚合取首帖 |
| Riley Goodside | https://x.com/goodside | https://nitter.kareem.one/goodside | 高 | ~5 条/天；模型行为小实验，自创评测 |
| Sam Altman | https://x.com/sama | https://nitter.kareem.one/sama | 高 | ~2.5 条/天；OpenAI 一手动向，水帖跳过 |
| Teortaxes | https://x.com/teortaxesTex | https://nitter.kareem.one/teortaxesTex | 高 | 几十条/天；中国开源模型线独一档，按线程聚合 |
| Neel Nanda | https://x.com/NeelNanda5 | https://nitter.kareem.one/NeelNanda5 | 中 | ~0.4 条/天；可解释性全干货 |
| Roon | https://x.com/tszzl | https://nitter.kareem.one/tszzl | 中 | ~4.5 条/天；OpenAI 内部人乐子，大事件反应有独家价值 |

## 线索源（只当发现渠道，绝不直接引用 · 2026-07-23 新增）

| 源 | 主页 | 抓取URL | 方式 | 说明 |
|---|---|---|---|---|
| Neodrop AI+机器人晨报（朋友频道） | https://neodrop.ai/zh-cn/channel/T48pwHhPZyU | 同主页 | html | 每天 07:15 一期，X 聚合、偏具身。**只用于补漏**：发现的线索必须回溯原始出处真读、成稿只引原文（频道转述混有频道主引申）。试跑至 08-06，无增量则砍 |

## 评估过但没收的（免得将来重复评估）

- **EA 论坛**（2026-07 砍）：内容离 AI 太远。
- **X @ESYudkowsky**（2026-07-23）：原创可用，但他大量产出在别人帖子下的回复区，镜像默认页看不到，收了也漏。
- **X @repligate**（2026-07-23）：模型行为怪谈第一现场，但形态是无字配图/单词帖/圈内黑话，自动摘要没法用，适合人肉刷。
- **Google 官方博客**（2026-07-23）：主 feed 消费向为主，AI 分区 feed 滞后（Gemini 三连发都没进）；大事有 HN + DeepMind 官博双保险。
- **NVIDIA 开发者博客**（2026-07-23）：工程教程+硬件软文，与日报品味不对口；架构级大事 HN 会顶上来。

## 周刊源（判新窗口 168 小时，固定周几出刊）

| 源 | 主页 | 抓取URL | 方式 | 权重 | 节奏 |
|---|---|---|---|---|---|
| Import AI (Jack Clark) | https://importai.substack.com/ | https://importai.substack.com/feed | rss | 高 | 每周**周一**一期；政策+宏观+反直觉，Anthropic 联创视角 |
| The Batch (Andrew Ng) | https://www.deeplearning.ai/the-batch/ | https://www.deeplearning.ai/the-batch/ | html | 低 | 每周**周五**一期；偏科普，凑数时才用 |

## 不定期源（判新窗口 168 小时，更新无固定日）

| 源 | 主页 | 抓取URL | 方式 | 权重 | 节奏 |
|---|---|---|---|---|---|
| Anthropic Research | https://www.anthropic.com/research | https://www.anthropic.com/research | html | 极高 | 研究、对齐、可解释性与前沿红队成果；有更新进精读 |
| Meta AI Research | https://research.meta.ai/ | https://research.meta.ai/ | html | 高 | 模型、研究与开放权重发布；卡片带绝对日期 |
| Mistral News | https://mistral.ai/news/ | https://mistral.ai/news/rss | rss | 高 | 模型、研究、工程和欧洲政策动向；普通产品稿降权 |
| Interconnects (Nathan Lambert) | https://www.interconnects.ai/ | https://www.interconnects.ai/feed | rss | 高 | 每 3-5 天一篇；RLHF/开源模型深度解读 |
| Google DeepMind Blog | https://deepmind.google/discover/blog/ | https://deepmind.google/blog/rss.xml | rss | 中 | 每月数篇，成簇无固定日；2026-07-28 从 html 换 rss（索引页改客户端渲染，静态 HTML 取不到条目） |
| Ahead of AI (Sebastian Raschka) | https://magazine.sebastianraschka.com/ | https://magazine.sebastianraschka.com/feed | rss | 高 | 每 2-4 周一篇；大事件讲透，工程师友好 |
| Andrej Karpathy | https://karpathy.bearblog.dev/ | https://karpathy.bearblog.dev/feed/ | rss | 极高 | 数周-数月一篇，不规律；有更新必进头条 |

## 低频源（判新窗口 720 小时，多数时候没更新，但一更必看）

| 源 | 主页 | 抓取URL | 方式 | 权重 | 节奏 |
|---|---|---|---|---|---|
| Lilian Weng | https://lilianweng.github.io/ | https://lilianweng.github.io/index.xml | rss | 极高 | 数月一篇（停在 2025-05），一篇顶十篇，有更新必进头条 |
| Thinking Machines Blog | https://thinkingmachines.ai/blog/ | https://thinkingmachines.ai/blog/ | html | 中 | 数周-数月一篇；Lilian Weng 现东家 |
| Chip Huyen | https://huyenchip.com/blog/ | https://huyenchip.com/feed.xml | rss | 高 | 近一年零更新（停在 2025-01）；偏工程落地 |

---

## 维护说明

- 新源准入条件：fetch 友好（静态页面/有公开存档/有 API），信息密度高；正式收编前先派 scout 实测可抓性+采样信噪比（X 七源与 neodrop 均按此流程核过）
- 连续两周日报里没贡献过条目的源，考虑移除
- 节奏会变：某源若明显比标注的更勤/更懒，调整它 meta 里的 `window_hours`（判新窗口）并同步本表；meta 里的 `check_frequency` 字段已退役，仅作历史提示
- 验证基线：2026-06-10 全员 fetch 通过；2026-07-23 X 七源 + neodrop 实测可达（X 走 nitter.kareem.one 镜像，社区单点，死了去 status.d420.de 找新实例）
