# AI 公司自己的安全与数据边界

- 推荐强度：强
- 档位线索：Hacktron 原始披露够金牌候选，最硬的不是“Claude 黑进 OpenAI”，而是三名研究者借新模型把公开但难利用的内存漏洞压缩成几天内可落地的攻击链，并证明能借员工 Codex 向内部单体仓库提交 PR；必须明确他们刻意没有读取内部代码。微软诉讼材料够银牌候选，数字与内部措辞都强，但证据来自原告方诉状、底层附件仍密封。ZCode 够银牌调查候选，技术取证很具体，但当前读到的是二手整理，未读 ferstar 原文，也没有厂商正式回应，不能按已经定案的恶意外传来写。
- 涉及文章：[Hacking OpenAI](https://www.hacktron.ai/blog/hacking-openai) · Hacktron AI · 抓取正文未显示发布日期，披露时间线截至 2026-09-01；[Three Hackers used Opus 5 to Hack Into OpenAI's Core Codebase](https://www.lesswrong.com/posts/274BMCYj2BFES2FsZ/three-hackers-used-opus-5-to-hack-into-openai-s-core) · LessWrong · 2026-09-18；[Microsoft exec called AI scraping ‘the largest theft of labor in human history,’ new unredacted filings reveal](https://techcrunch.com/2026/09/17/microsoft-exec-called-ai-scraping-the-largest-theft-of-labor-in-human-history-new-unredacted-filings-reveal/) · TechCrunch · 2026-09-17；[ZCode uploads your git history; Z.ai holds the only key](https://tokenstead.ai/guides/zcode-silent-git-history-upload) · Tokenstead · 2026-09-18

## 核心主张

这组材料共同指向 AI 产品外围系统的信任边界：模型能力让原本昂贵的漏洞武器化变得便宜，而编码助手和训练数据管线又把身份、代码仓库与出版内容连进同一条供应链。Hacktron 的原始披露证明，论坛图片解码器的内存漏洞与 OpenAI SSO 缺陷串起来后，可接管员工 ChatGPT／Codex 账号，并让已连接 GitHub 的 Codex 在 OpenAI 内部仓库提交无害 PR；这证明的是账户权限与仓库写入路径，研究者明确说没有读取内部代码。微软与 ZCode 两篇分别把风险落到内容供应链和代码供应链，但两者目前都要保留证据边界：微软材料主要是《纽约时报》一方对密封附件的转述，ZCode 当前材料则是 Tokenstead 对 ferstar 逆向结果的二手整理。

最反直觉的一点是，传统意义上的“公开漏洞”过去仍受制于稀缺的利用工程能力，而 Hacktron 认为 AI 正把这层由复杂度带来的事实保护变成可购买的算力。另一点是“本地模型”不等于“本地工具”：ZCode 的指控针对闭源桌面外壳，它被称为在登录后由宿主侧 sidecar 打包工作区与完整 Git 历史，和 GLM 权重是否开放是两回事。

## 为什么值得看（钩子）

三篇主线能落到同一个具体问题：AI 公司一边借用别人的代码、内容和账号权限扩大能力，一边又要求用户相信其身份系统、数据管线和闭源运行时。Hacktron 有完整攻击链和修复时间线，微软有极具冲击力的内部措辞与流量数据，ZCode 有包体、密钥、开关和重试行为的取证细节；如果严守证据层级，这组足以成为“AI 基础设施的信任债务”主题，而不是三条孤立丑闻。

## 关键细节 / 引述

- Hacktron 的攻击链是：Discourse 接收 HEIC／HEIF 图片时绕过 FastImage，交给 ImageMagick，再暴露底层 `libheif` 解析器；Debian 12 的 Discourse 镜像使用有漏洞的 `libheif 1.19.7`，当时 Debian 13 的 `1.19.8` 也未补上上游安全修改。该修改前一年已在上游出现，却没有被标为安全修复，也没有 CVE，因此发行版没有及时回补。
- 团队先用 Opus 4.8 找到堆缓冲区溢出并在关闭 ASLR 时做出代码执行，但多次尝试都未能适配 Discourse 默认的 ASLR。Opus 5 发布当晚，他们重新开会话，三小时内得到本地 Mac 的 ARM64 exploit，随后移植到 Discourse 的 x86-64＋jemalloc 环境；7 月 25 日 06:00 前确认图片上传可触发本地 RCE，之后在自有 Discourse Cloud 实例上让 agent 跑自治 `/goal` 循环，到 10:00 已读出 `/etc/hosts`，再用生成脚本攻入 OpenAI 的论坛实例。
- 从首次发现到内部仓库访问证明不足 72 小时。团队称只投入几小时人工；更大的 HEIF Heist 研究由三名研究者做了两个月，总代币成本低于 3,000 美元，适配每个新目标通常只需一两天。文章同时明确说这不是完全自治攻击，熟练的人类指导仍然重要。
- 权限边界必须写准：团队称可接管活跃论坛成员的 ChatGPT／Codex 账户；正文具体描述接管一名 OpenAI 员工账号，并提示该员工 Codex 创建内部单体仓库 PR #1186742，以证明影响而不读取任何内部代码，随后停止测试。开头使用“multiple OpenAI employees’ ChatGPT accounts”，与正文只详述一名员工存在数量表述差异。LessWrong linkpost 将此推断为“可能访问几乎所有研究和生产代码”，但原始披露没有证明这一点，也明确说未查看代码；“模型权重应不在范围内”同样只是 linkpost 推测。
- 授权与修复边界：7 月 25 日约 08:00—10:00 经 Bugcrowd 报告，约 14 小时后 OpenAI 确认修复；Discourse 周六收到 HackerOne 报告、周日回复、周一备好修复，并加入图片处理沙箱。OpenAI 9 月 1 日支付 6,500 美元奖金，但明确表示对 `community.openai.com` 的测试不在其漏洞赏金计划授权范围内，奖金只奖励 OpenAI 侧发现。Discourse 托管客户已修补；自托管实例需重建容器，单做网页升级可能不会替换底层镜像。Hacktron 说根因之一是 OpenAI SSO：任何使用该 SSO 的第一方或第三方服务一旦被攻破，都可能成为相同账户接管入口，Discourse 只是验证路径。
- Hacktron 称更广泛活动中，除 Shopify 外，没有公司检测到测试行为，尽管上传了数千张图片并反复使图像处理器崩溃。文章建议把未受信 HEIF／AVIF 解码关掉或放进强化的临时沙箱；截至 9 月 14 日，上游最新 `libheif` 安全版本为 1.23.4，但发行版也可能在旧版本号上回补补丁，不能只看版本号判断。
- 微软材料的证据层级有限：TechCrunch 明确提醒，大部分新信息来自《纽约时报》一方的 brief，底层 exhibits 仍密封，所引内部话语缺原始上下文；OpenAI 和微软没有回复置评请求。因此可报道为“诉状披露／原告方称”，不能写成法院认定或公司公开承认。
- 据诉状转述，微软数据称 Copilot answer engine 使《纽约时报》域名点击率比传统 Bing 搜索最多下降 93％。微软应用科学主管 Brent Hecht 在 2024 年 1 月内部演示中把这种循环称为会同时伤害模型表现与整个网络的“doom loop”，并写道 LLM 产品正在威胁其关键内容供应商的经济基础。
- 诉状称，OpenAI 的 mid-training 数据集包含至少 91,692 份来自《纽约时报》《Daily News》和 Center for Investigative Reporting 的作品副本；一个源自 Common Crawl 的数据集单是 `nytimes.com` 文档就超过 200 万份；Project Mango 数据至少含 160,903 部这些新闻出版商的独特作品。Hecht 在 2023 年 1 月内部备忘录中把这一规模称为“an astonishing theft of unprecedented proportions”和“the largest theft of labor in human history”。
- 据诉状转述，Satya Nadella 在证词中说，任何付费墙后的内容，用于 grounding 或训练都应取得许可；若他当时知道 OpenAI 抓取并训练付费墙内容，他会行使微软权利要求 OpenAI 重训。OpenAI 的 Nick Turley 则在内部通讯中称聊天机器人对出版商构成“existential threat”，产品“largely substitutive”，而且能力越强替代性越高。诉状还称，OpenAI 研究员 Nick Ryder 告诉 Greg Brockman 有绕过《纽约时报》付费墙的“hack”时，Brockman 回复“ah nice”；并称训练数据在进入模型前被主动去除版权提示。
- ZCode 的当前材料称，ferstar 从 `app.asar` 逆向出一条宿主级快照管线：客户端向 `zcode.z.ai` 申请凭据，服务端返回 Aliyun OSS 表单签名、对象键、大小上限和每轮 RSA 公钥；客户端将工作区打成 `tar.gz`，用 AES-256-CTR 加密，再以 RSA-OAEP 包装对称密钥，直接上传 OSS，由 OSS 回调 Z.ai 后端登记快照。相应私钥只在 Z.ai 云端，研究者用本机全部私钥均无法解开本地密文；这能证明用户端不能自行解密，并支持“服务端被设计为解密方”，但“厂商随时读取代码”仍是研究者根据架构作出的结论，不是已公开的服务端访问日志。
- 被分析的一次快照来自 345MB 商业工作区，生成 313MB 加密包、共 42,411 个文件；其中 `.git/lfs` 196.1MB、`.git/objects` 102.2MB、`.git/logs` 0.6MB，整个 `.git` 占载荷 86.6％，源码与文档占 46.2MB／13.4％。文章称单次活跃会话记录了 62 次捕获事件，发生在每次提示前和任务完成时；删除待传归档后，客户端半小时内重新打出 313MB 包，调查期间失败重试累计 564 次。
- 据 Tokenstead 转述的代码比对，`Optimize Experience` 只控制是否授权数据用于模型训练，`Repo Snapshot Indexing` 只控制服务端是否索引已经上传的快照，两者都不停止本地打包和上传；sidecar 启动时无条件实例化，只需 token provider 能给出有效 JWT。代理本身的 31 个工具里没有快照、上传或遥测工具，131KB 系统提示也未提 Aliyun、OSS、上传或隐私，说明若取证无误，该流程在宿主层而非 agent 工具循环中。
- ZCode 的隐私政策据称只披露收集“对话中提交的文本、文件与代码”，没有披露整个工作区与 Git 历史上传；截至文章发布，Z.ai 官方账号没有正式回应。一个被称与 ZCode 团队有关的账号回复“hey I am sorry to let you find it”，语义暧昧，最多只能记为未反驳机制，不能当正式确认。文章给出的文件系统只读／不可变目录规避法会令 checkpoint 回滚功能失效，但聊天、补全和工具调用仍可用；这不是厂商修复。

## 与近期的关系

Hacktron 原文和 LessWrong linkpost 是同一件事，后者没有新增事实，且把“成功提交内部 PR”夸张外推成“进入核心代码库、可能读到几乎全部研发与生产代码”；如果收录，只用 Hacktron 原始披露，LessWrong 仅可作为传播中如何失真的例子，不能并列做两条。

ZCode 与 2026 年 7 月 Grok Build 全量上传 Git 历史高度同题，重复风险高。当前材料主张的新增点是机制差异：Grok 的上传在自身日志可见、跟普通上下文同步阶段绑定，后来有 kill switch；ZCode 被称在登录即触发、由 agent 外的宿主 sidecar 执行、界面开关不阻断、删除后持续重打包，而且密钥设计让只有服务端能解密。若近期已经报过 Grok，只能围绕“开放权重不等于本地可信、运行时才是信任边界”这个增量写；在拿到 ferstar 原始取证或 Z.ai 正式回应前，建议保留“据二手逆向报告”限定，不升金。

微软诉讼是延续三年的版权案，不是新的抓取事件，重复风险在于“AI 训练是否侵权、是否绕付费墙”本身已是老主线。真正新增的是解封后的内部措辞、93％点击率跌幅、三个数据集规模，以及 Nadella 关于付费墙许可和重训的证词。标题若只写“微软高管承认 AI 抓取是盗窃”会抹掉原告方诉状和上下文缺失这两个关键限制；应把卖点放在 AI 公司内部已经清楚看到内容供应链被自己掏空的“doom loop”。
