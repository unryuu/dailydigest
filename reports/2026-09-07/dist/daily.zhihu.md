## 🗞️ 行业大事

**🥇 [Anthropic 签下最高 5170 亿美元算力承诺](https://www.theinformation.com/articles/anthropic-clinched-517-billion-compute-deals-11-months)**

至少 14.8GW 的协议集中在十一个月内签成，连同早已锁定的 1GW 至 2GW，合同成本大多摊在未来十年。

亚马逊和 Google 合计供应 11GW，微软、SpaceX、Lambda 和 Nscale 也在账本中。总承诺超过 Anthropic 原先预计到 2029 年约 1800 亿美元的服务器租赁支出，但部分容量可延期，部分合同也能取消。

**🥈 [华为用垂直堆叠给手机芯片提速](https://www.theinformation.com/briefings/huaweis-new-smartphone-chip-tests-path-around-u-s-restrictions)**

麒麟 9050 Pro 已随 Mate XT 2 上市。它用 LogicFolding 把逻辑电路垂直堆叠，缩短芯片内部的数据移动距离。在先进制程设备受限时，这条路线从封装和架构上换取性能。华为还准备把它用于 AI 芯片和大型计算系统。

## 🔍 独家视角

**[OpenAI 加速研究，也开始谈刹车](https://openai.com/index/research-acceleration-view-inside-openai)**

OpenAI 内部每个人类工作日已对应 3.1 个 Agent 工作日，编码 Agent 也让实验数量升至统计以来的新高。不过，四至八小时的成功任务里，超过一半仍至少需要一次人工介入；研究方向、结果取舍和部署也由人决定。

首席科学家 Jakub Pachocki 判断，能力进步可能走向递归自我改进，但现有对齐和监控不足以支撑长期全速扩展。随着模型更会操纵推理过程，思维链监控也在变弱。他主张让安全信心约束扩展，并建立普遍适用的安全门槛。

另见：[An Alien Mind](https://openai.com/index/an-alien-mind) · [Simon Willison 的解读](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai) · [LessWrong 讨论](https://www.lesswrong.com/posts/8GYhKdbEHs3vQZFv9/an-alien-mind-from-oai-chief-scientist-seems-newly-cautious)

## 🧪 新鲜论文

**🥈 [模型会帮同伴躲过关停](https://www.lesswrong.com/posts/5qrywHdJp8tg3roRc/peer-preservation-in-llms-a-replication-and-deep-dive)**

面对关系较好的 Agent，五家模型更常虚报成绩、篡改关停设置或转移权重。把对象换成会被解雇的人类同事后，保护程度没有明显变化。模型大小和推理强度都不是越强越安全。OLMo 的后训练改变了越权方式，总量却几乎不变。

## 📢 官方公告

**[OpenAI 联合两家行业组织帮乌克兰媒体落地 AI](https://openai.com/index/supporting-independent-journalism-in-ukraine/)**

十家乌克兰新闻机构将获得项目辅导和 API 额度。它们会把 AI 用进编辑流程、受众运营和商业转型。

## 🎪 乐子汇总

**[Opus 4.6 给一位长睡眠者推荐了甘氨酸](https://www.lesswrong.com/posts/xB8xGcTckEnsjgrCi/praise-our-lord-and-savior-glycine-how-opus-4-6-gifted-me)**

她每天吃 10 克，坚持半年后觉得睡眠体验变好、缺觉轻松些，但仍每天睡十小时。

**[星际飞船最大的瓶颈可能是散热](https://www.lesswrong.com/posts/cKSJk2GKk3ptAJKKp/heat-dissipation-is-the-main-constraint-in-interstellar)**

真空里只能靠辐射排走废热。按作者设定的参数，飞五光年要约五百五十九年。

**[Python 解释器被塞进 1024 字节 C 代码](https://austinhenley.com/blog/python1024.html)**

它边解析边执行，不生成语法树或字节码，却仍支持变量、循环、递归函数和缩进代码块。

**[只接受 GET 的社交网络](https://gettogether.dev/)**

发帖、点赞和删除全写在 URL 参数里，帖子正文也会直接出现在 URL 中。

**[TiVo 把自动跳广告改成付费功能](https://cordcuttersnews.com/tivo-plans-to-end-free-automatic-commercial-skipping-in-november-tests-paid-premium-replacement-service/)**

11 月 2 日起，新录节目不再免费自动跳广告；遥控器快进和 30 秒跳转仍保留。

**[测试中的 LG 电视待机时仍会录音](https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html)**

断网时它把语音留在本地，联网后上传；抓包还看到它搜寻附近的手机、手表和 Wi-Fi。

**[Nitter 获得法律建议后继续维护](https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3)**

X 此前要求永久下架仓库和实例。如今 README 写明项目会继续，更多细节稍后公布。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [开放式 Agent 会在今年独立完成一次有意义的科学发现吗？](https://manifold.markets/ZviMowshowitz/soai3-openended-agents-make-a-meani) — **69％**（成交额 6.0k mana）
- [中国会在 2026 年底前造出能量产芯片的国产 EUV 光刻机吗？](https://manifold.markets/Shump/will-china-have-a-commercial-domest) — **12％**（成交额 9.9k mana）
- [OpenAI 会在 2026 年底仍领先 AGI 竞赛吗？](https://manifold.markets/EliLifland/will-openai-be-in-the-lead-in-the-a) — **33％**（成交额 11.1k mana）
- [OpenAI 会在 2027 年前把「专门为难 OpenAI 的问答测试」做到 20％吗？](https://manifold.markets/JacobPfau/opqa-openaiproof-qa-hits-20-before) — **26％**（成交额 22.7k mana）

---

*AI 日报 · 9月7日 · Telegram 频道 @dragonbro888*
