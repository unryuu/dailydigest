# 联网精读测试 · B 组（监管方向）

抓取时间：2026-07-31
工具：WebFetch（未派 subagent）

---

## 1. Axios：黄仁勋会见卢特尼克（抓取失败）

链接：`https://www.axios.com/2026/07/28/nvidia-jensen-huang-lutnick-meeting-china-ai`

**结果：抓取失败。**

WebFetch 原样返回：

> The server returned HTTP 403 Forbidden.
> The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.

即服务端直接以 HTTP 403 拒绝，响应体未取回，一个字正文都没读到。按铁律，本条不做任何推测性补写，也不改用其他链接充数。

---

## 2. Cloudflare：Content Independence Day —— AI 流量的分类管理（抓取成功）

链接：`https://blog.cloudflare.com/content-independence-day-ai-options/`

**核心主张**：Cloudflare 办第二届「内容独立日」，把对 AI 爬虫的处置从「一刀切封禁」升级为分类授权，让站长按用途而不是按机器人身份来决定放行与否。

**关键细节**：

- 三分类：Search（索引以供检索）、Agent（代表用户实时执行任务）、Training（采集数据用于训练或微调）。
- 新默认值 2026 年 9 月 15 日生效：展示广告的页面默认拦截 Training 与 Agent，Search 仍默认放行；Googlebot 这类多用途爬虫按最严格的一条规则处理。
- 内容使用信号分三级：`immediate`（交互但不存储）、`reference`（索引、摘录并回链）、`full`（可总结与复现）。
- Verified 机制调整：通过验证不再等于自动放行，仍须落在被允许的类别里。
- 借 RFC 7239 的 Forwarded 头传递信任信息，支持跨代理链识别真实操作方。
- 企业客户新增 BotBase，提供可搜索的机器人目录总览。
- 新选项即刻对全部客户开放，含免费层。
