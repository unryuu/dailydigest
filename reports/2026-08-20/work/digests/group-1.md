# OpenAI 用 Private Safety Processing 兼容跨会话风控与零数据留存

- 推荐强度：强
- 档位线索：够金牌候选。它不是单纯宣布「不拿企业数据训练」，而是提出一种新的安全架构：模型公司跨多轮识别高危模式，却原则上不取得客户的底层提示词与回复。不过系统仍在早期客户测试，九月才计划推出并发布技术白皮书，不能把设计目标写成已经验证的能力。
- 涉及文章：[Offering Zero Data Retention for frontier models](https://openai.com/index/offering-zero-data-retention-for-frontier-models/) · OpenAI · 2026 年 8 月 19 日
- 涉及文章：[OpenAI to Launch Security Analysis System With Better Privacy Protections](https://www.theinformation.com/briefings/openai-launch-security-analysis-system-better-privacy-protections) · The Information · 2026 年 8 月 19 日（网页正文为订阅墙空壳，细节来自已保存的人工精读候选摘要）
- 涉及文章：[we support business privacy!](https://x.com/sama/status/2090163991234453611) · Sam Altman／X · 2026 年 8 月 19 日

## 核心主张

OpenAI 正在把「零数据留存」从逐次请求扩展到跨多轮安全分析：相关交互可以由自动系统联合判断，以识别单次看似正常、合起来才显出攻击意图的模式，而 OpenAI 人员原则上看不到底层提示词和回复。其关键取舍是让客户保有内容与密钥控制权，OpenAI 只接收范围有限的风险信号，用于决定是否执法。这个方案瞄准的是企业采用前沿模型时的真实矛盾：网络攻击、生物攻击、反复试探防线或失控 Agent 往往必须看上下文才能发现，但长期把敏感内容交给模型公司又可能违反企业自身的安全与合规要求。

## 为什么值得看（钩子）

反直觉之处在于，安全监控未必等同于模型公司长期保存并人工查看客户数据。若这套架构按承诺落地，前沿模型公司的竞争点会从「留不留数据」进一步变成「谁能在看不到原文的情况下，仍可靠识别跨会话风险」。

## 关键细节／引述

- ZDR 面向符合条件的 API 客户：请求处理完成后，OpenAI 不保留提示词或模型回复，OpenAI 人员不能查看客户内容；企业数据默认也不用于训练，除非客户明确选择加入。
- Private Safety Processing 将现有逐次交互检查扩展到相关交互。OpenAI 举例称，恶意意图可能分散在多轮请求、多个账号或长时间 Agent 任务中，例如系统在用户要求停止后仍继续行动。
- 在 ZDR 部署中，内容留在客户控制的基础设施上；OpenAI 还在开发另一种方案，把内容放在 OpenAI 基础设施中，但由客户控制密钥加密，OpenAI 人员没有密钥副本。
- 系统发现风险后，OpenAI 收到的是范围有限的信号，而不是底层对话。The Information 的已保存摘要将其描述为滥用类别和严重程度；客户如需申诉、说明合法用途或协助调查，可以自行选择向 OpenAI 提供相关信息。
- The Information 的摘要称，系统尤其针对网络攻击、生物攻击等需要跨多轮才能判断的风险，并将其与 Anthropic 对 Claude Fable 5 至少保留 30 天数据的做法作对照。
- 该系统正在早期客户中测试。OpenAI 计划九月开始推出并发布技术白皮书；Sam Altman 转发公告时只写了「we support business privacy!」，属于立场宣传，不构成额外技术证据。
- ZDR 仍有法律例外：被标记为疑似儿童性虐待材料的图片，会继续保留供人工审核和依法报告。

## 与近期的关系

三份材料讲的是同一件事，必须合并，不能拆成「OpenAI 零留存」「Private Safety Processing」「Sam Altman 隐私表态」三条。它与近期前沿模型安全监控主线相邻，但新增角度不是又一套风险分类，而是安全分析的隐私架构；The Information 摘要还把它放进与 Anthropic 数据保留政策的直接竞争中。重复风险主要来自同事件多源和「企业数据不训练」这一旧承诺，真正的新信息应锁定跨多轮分析、客户控密钥、只返回有限风险信号，以及九月才开始推出这四点。
