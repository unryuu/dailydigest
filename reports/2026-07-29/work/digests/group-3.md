# OpenAI 开源 codex-security：AI 安全扫描 CLI，但护栏挡住了自己人

- 推荐强度: 中
- 档位线索: README 核实是防御工具（找、验证、修代码漏洞），定位清晰，撑得住银；HN 高分（505）但风评偏负——烧钱、拒答、护栏挡正经用途，做银时建议把 HN 的实测吐槽写进去，只抄官方描述会显得像通稿。若版面紧张降简讯也不亏。
- 涉及文章:
  - [openai/codex-security](https://github.com/openai/codex-security) · GitHub · README 实读
  - [HN 讨论（505 分）](https://news.ycombinator.com/item?id=49089755) · Hacker News

## 核心主张
README 原文定位：「a CLI and TypeScript SDK for finding, validating, and fixing security vulnerabilities in your code」——防御性工具，不是攻防框架。面向开发者和团队：扫仓库、审变更、跟踪 findings、跑 CI 安全检查。npm 装包（`@openai/codex-security`），支持 ChatGPT 登录或 API key，CI 里走 `OPENAI_API_KEY`，Apache-2.0 协议，要求 Node 22+ 和 Python 3.10+。

## 为什么值得看（钩子）
OpenAI 亲自下场做 AI 安全扫描，但 HN 实测的最大槽点是：模型自己的安全护栏挡住了正经防御工作——「找到了漏洞，但拒绝解释它」。卖安全工具的被自家安全策略绊倒，这个拧巴是真钩子。

## 关键细节 / 引述
- 本质：HN 评论共识是「a fancy CLI wrapper」——包了 GPT-5.6 Sol + 一套调优过的安全提示词/技能（官方称经数十亿 token 评测打磨），代码在本地跑但要送 OpenAI 服务器分析，有数据驻留要求的组织用不了。
- 烧钱：多位用户报告一次扫描吃掉每周额度的 25–50%（有人 100 美元+），一位开发者：「Just ran it on a small repo. It ran for almost an hour... drained half my weekly usage.」
- 护栏自伤：扫 40+ 分钟后拒绝输出结果；解锁完整能力要注册「Trusted Access for Cyber」（TAC1/Daybreak）特批。
- UX 差：长时间扫描无进度反馈、无法预估成本、中断不能续跑。
- 对比：评论提到 Snyk、Semgrep 等传统 SAST，认为很多场景下传统工具够用且便宜得多。
- HN 整体情绪：谨慎怀疑（cautiously skeptical）。

## 与近期的关系
与本期 group-2（Anthropic 用 Claude 攻密码学）构成「同日一攻一防」的对仗，编排时可互相引一句，但要防止两条都写成「AI 进军安全行业」的同款开头。单看本条是新工具发布，无旧闻重炒风险。
