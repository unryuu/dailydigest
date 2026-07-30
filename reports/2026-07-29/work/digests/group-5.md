# MCP 2026-07-28 新规范：砍掉会话状态，改成纯请求/响应，Claude 宣布跟进

- 推荐强度: 强
- 档位线索: 协议级大改（不是加功能，是换架构），对做 agent 基建的人是必读；细节硬（删了什么、留了多久缓冲期都有明文）。银稳；若当天缺金且受众偏开发者，可冲金。
- 涉及文章:
  - [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) · Claude Blog · 2026-07-28
  - [MCP 官方发布博客](https://blog.modelcontextprotocol.io/posts/2026-07-28/)（页内跟进）
  - 规范原文: https://modelcontextprotocol.io/specification/2026-07-28

## 核心主张
MCP 2026-07-28 版把协议从双向有状态改成无状态请求/响应模型：删掉 `initialize`/`initialized` 握手和 `Mcp-Session-Id` 头，每个请求自带协议版本、客户端身份和能力（放 `_meta` 里）。官方原话点出目的：「any request can now land on any instance behind a plain round-robin load balancer without needing shared storage」——MCP 服务器从此可以当普通 HTTP 服务部署到 serverless / 边缘。Claude 宣布跟进，时间表只说「rolling out across Claude products soon」，无具体日期。

## 为什么值得看（钩子）
这是 MCP 诞生以来最大的架构掉头：当初的双向长连接设计被自己废掉了。所有自建 MCP 服务器的人都要在 12 个月缓冲期内迁移。

## 关键细节 / 引述
- 删掉的东西：握手、会话头、依赖双向流的服务器发起请求（`elicitation/create`、`sampling/createMessage`、`roots/list` 全部重设计）；旧 HTTP+SSE 传输「officially deprecated, with a year-long offramp」。
- 替代机制 MRTR（多回合请求）：服务器中途要输入时返回 `resultType: "input_required"` 附上问题，客户端把答案放 `inputResponses` 里重试原调用——把「服务器反向调客户端」变成「客户端重试」。
- 需要状态怎么办：官方指引是「mint an explicit handle from a tool and have the model pass it back as an argument」——状态显式化成 token 由模型传递。
- 网关友好：Streamable HTTP 请求必须带 `Mcp-Method` 和 `Mcp-Name` 头，让网关/限流器/WAF 不解析 JSON body 就能路由计费；list 类响应新增 `ttlMs` 和 `cacheScope` 缓存元数据。
- 扩展框架转正：Tasks 从实验核心挪进 `io.modelcontextprotocol/tasks` 扩展（轮询式 `tasks/get` + 新 `tasks/update`）；MCP Apps（对话内渲染交互 UI）、企业托管授权（EMA）同列。
- OAuth 收紧：对齐 OAuth 2.0/OIDC 生产部署（可接 Entra、Okta）；动态客户端注册（DCR）正式弃用改 CIMD；客户端凭证绑定签发方，跨授权服务器不能复用。
- 兼容性：弃用特性「still work, and they'll keep working for at least twelve months」；TS/Python/Go/C# SDK 附迁移说明，官方承认依赖 session id 的开发者「some migration cost」。
- Claude 侧背景数字：connectors 目录已有 950+ MCP 服务器。

## 与近期的关系
MCP 是本频道常客（此前多为生态/安全角度），但协议本体大版本改架构是新事，不算旧事重炒。注意：Claude 博客本身信息量薄（就一句 soon），干货全在 MCP 官方发布博客，写手引用时应以后者为事实源。
