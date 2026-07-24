# OpenAI 商业化三连：广告自助开卖、企业 agent 平台、小微企业计划

- 推荐强度: 中偏强
- 档位线索: 三件事单拎都不够金牌，但 48 小时连发构成一个"找钱"叙事，银牌成立。主角是广告平台（自助入口开放 = 从"表态要做广告"变成"柜台开张"），HN 892 分 687 评的反弹热度是加分项。若当日有更硬的技术头条，守银牌即可；不建议降雷达。
- 涉及文章:
  - [Advertise in ChatGPT（广告自助平台）](https://ads.openai.com/) · ads.openai.com · 2026-07-21 上 HN
  - [Introducing OpenAI Presence](https://openai.com/index/introducing-openai-presence) · openai.com · 本周
  - [Introducing the ChatGPT Small Business Program](https://openai.com/index/introducing-chatgpt-small-business-program) · openai.com · 本周

## 核心主张
OpenAI 在 48 小时内连发三个商业化动作，覆盖三条互不重叠的收入线：向广告主开放 ChatGPT 广告自助购买入口（面向品牌预算）、推出企业 agent 部署平台 Presence（面向大企业客单）、推出小微企业计划（面向 SMB 订阅盘）。最硬的事实是广告从"传闻/内测"进入了"任何广告主可自助开户投放"阶段——收钱的柜台正式开张。

## 为什么值得看（钩子）
广告自助页对最关键的三件事全部留白：不公布定价、不公布上线国家范围、不承诺"广告不影响回答质量"——官方口径只说广告"清晰标记、与 ChatGPT 回答保持分离"。一家要靠对话数据卖定向广告的公司，开张第一天就把价目表藏起来了。

## 关键细节 / 引述
- **广告形式**：在用户"探索选项、比较选择、做决策时"展示，基于对话上下文定向而非关键词；官方措辞 "Ads are clearly identified in the experience"、"Ads remain distinct from ChatGPT's responses"。
- **广告自助流程**：三步——建 campaign（设预算和目标）→ 上传广告素材（支持批量）→ 启动优化。页面举了 Best Buy 等大品牌早期投放案例，但未说明小广告主门槛。
- **广告留白项**：定价模式（CPC/CPM/竞价）、最低预算、上线国家范围均未披露。隐私口径是 "People control how their data is used for ads"。
- **Presence 是什么**：企业级 AI agent 部署平台，agent 可"回答问题、解决问题、使用公司系统、执行经批准的动作、必要时升级给人工"；含策略护栏、预部署模拟评分、生产监控，由 Codex 提议迭代更新、人工批准。支持语音+聊天。
- **Presence 关键数字**：OpenAI 自家电话支持线用它数周内"75% 入站问题无需人工解决"，10 天内人工转接率降 15 个百分点。首批客户 BBVA（墨西哥银行业务）、软银（日语支持）、IAG（保险理赔）。不开放自助，仅限量 GA，由 OpenAI 前置部署工程师（FDE）+ 系统集成商主导交付，未公布定价。
- **小微企业计划**：一句话——培训 + 资源 + 合作伙伴集成（Dropbox/Shopify/Intuit/Slack）打包，推 ChatGPT Work（跑 GPT-5.6 的多步任务 agent）进 SMB，美国范围；官方数据称线下 AI 学院 78% 参与者建立了可用工作流、42% 参与者每周省 5 小时以上。

## 与近期的关系
按派活方要求未回查前几期材料，以原文为主。三篇均为官方一手信源，事实层无抓取障碍（openai.com 两篇走 jina 代理成功，ads.openai.com 直连 403 后经 jina 代理成功）。

---

### 社区反应（仅供定牌参考，非正文素材）
HN 帖 "Advertise in ChatGPT" 913 分 / 698 评（截至抓取时）。情绪以反弹为主：darkstarsys "enshittification 开始了"；skeeter2020 指广告标榜精准定向却无 ROI 数据支撑，评论区流传的定价传闻为 $60–100 CPM（"接近 NFL 转播级别"，注意这是评论区说法，官方页面未证实）；ryankrage77 "即使最盈利的公司也总想赚得更多"。
