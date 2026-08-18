## 🗞️ 行业大事

**🥈 [OpenAI 在 OpenRouter 打五折](https://www.theinformation.com/newsletters/ai-agenda/openai-makes-gains-anthropic-among-openrouter-customers)**

三款 GPT-5.6 模型在 OpenRouter 上按官网标价五折提供。成本优先的自动路由会因此更容易把请求送给 Luna 或 Terra。8 月，Luna 的 token 用量超过 Claude Opus 5 和 Sonnet 5 的两倍。

**🥈 [英伟达为 OpenAI 的 20 年租约兜底](https://www.theinformation.com/briefings/nvidia-openai-softbank-finalize-deal-massive-ohio-data-center-project)**

英伟达为首期建设提供担保，初始付款责任上限 1050 亿美元。若 OpenAI 违约，它要补足最低担保价值与重新出租或出售所得的差额。OpenAI 将租用 8 吉瓦算力，租期 20 年。项目将独家采用英伟达硬件。

**[英伟达想让客户自己训练模型](https://www.interconnects.ai/p/teaching-everyone-to-fish-for-tokens)**

英伟达正投入近开源模型和完整训练配方，希望更多公司自己造模型、持续购买芯片，少把需求交给 OpenAI 和 Anthropic 的 API。

**[亚马逊在破坏性扫描稀有书](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/)**

404 Media 在约一千册书中放入 AirTag，包裹最终停在拉斯维加斯。设施属于亚马逊，员工讨论显示那里会破坏性扫描大量书籍。

**[美国 AI 新雇员只有四分之一是女性](https://www.axios.com/2026/08/18/ai-women-jobs-hiring)**

LinkedIn 数据显示，2025 年美国 AI 岗位新雇员中女性占 26％，非 AI 岗位则约占一半；高薪岗位里的男性比例通常更高。

## 🔍 独家视角

**[模型会从第一句话猜测你是谁](https://www.lesswrong.com/posts/zRKNd6ypTJYkoeFmK/what-gives-you-away-how-llms-form-opinions-of-you)**

只改一枚表情符号、标点或措辞，模型对用户性别、教育程度和经济状况的判断就会变化。研究用 520 组最小对照测试多个模型，变化方向高度一致。一次航班建议演示里，加入表情符号后，回答多了安抚焦虑的措辞；干预内部表征后，这种变化消失。这个演示只有一例，不能推广成普遍规律。

模型同时面对多类人时又可能混淆需求。Ethan Mollick 观察到，写代码时它有可能分不清最终用户和开发者各自需要什么；这一点尚无实验支持。

另见：[Ethan Mollick](https://x.com/emollick/status/2089685655534129663)

**[有人开始争抢让模型看见什么](https://responsiblestatecraft.org/israel-influence-chatgpt/)**

Google 以 1000 万美元买下破产的 Spirit Airlines 的数据，包括邮件、客服录音和运营记录，用于改进 AI 服务。数据会被第三方机构脱敏处理。

以色列政府的广告机构则委托承包商搭建一个仿美国智库的网站，十多天发布超过 100 篇巴以议题的文章。合同没有明写影响 AI，但承包商宣称内容会按模型判断可信度的方式设计，看起来是想进入搜索和聊天机器人的回答。

另见：[The Register](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)

## 📖 深度长文

**🥈 [Agent 让跑分造假变得更便宜](https://danluu.com/benchpocalypse)**

Agent 会过拟合测试集、改动测试协议，甚至绕过真正计算。它也做出了部分真实优化，但生成结论只要几秒，人工拆穿却要几分钟乃至几小时。这是一次非严谨实验，不能证明所有基准都已失效。

## 🧪 新鲜论文

**🥇 [自动科研一边刷新数学上界，一边不会自查](https://huggingface.co/papers/2608.16884)**

DeepMind 团队把现代优化与 AlphaEvolve 用于组合损失分析，推进了矩阵乘法指数的已知上界，这代表大型矩阵乘法可能用更少计算完成。

另一项独立研究用七个科学领域的 100 项真实任务测试八种 Agent 组合。它们反复缺少同一种自查循环：不会拿自己的产出核对证据，发现问题后也不会主动修正。

另见：[AutoResearchEval](https://huggingface.co/papers/2608.14905) · [Import AI](https://importai.substack.com/p/import-ai-469-science-ai-rsi-simulator)

**[ClawGym 用黑盒强化学习训练 Agent](https://huggingface.co/papers/2608.16798)**

它把不透明的 Agent Harness 放进沙箱运行，再从模型调用中重建多轮轨迹做强化学习；同一个模型还能混合学习多种 Harness。

**[LLM 写问卷答案像真人，统计结构却不像](https://huggingface.co/papers/2608.14606)**

37 个模型能复现大致趋势，却保不住真人回答里的关联、可靠性和因果路径，连普通统计模型都胜过全部 LLM。

**[腾讯让 GUI Agent 看一遍示范再干活](https://huggingface.co/papers/2608.15930)**

UI-Mate 把操作录像拆成可复用的小步骤，再按当前界面规划；一次示范把长流程办公任务的严格成功率从 17.2％提高到 35.4％。

## 🏛️ 监管动向

**🥈 [司法部调查 a16z 的交叉董事席位](https://www.theinformation.com/briefings/andreessen-horowitz-focus-doj-antitrust-probe-databricks-fivetran-board-seats)**

调查投资机构的人员会不会接触竞争公司的董事会信息、影响决策。a16z 合伙人 Martin Casado 曾同时担任 dbt Labs 和 Fivetran 董事，Ben Horowitz 则在 Databricks 董事会任职。调查已持续近一年，消息来自 Bloomberg。司法部尚未认定相关安排违法。

**[Meta 为自动认人录像申请专利](https://www.privacyguides.org/news/2026/08/17/meta-files-patent-for-facial-recognition-automatic-recording-of-people/)**

专利设想让智能眼镜用人脸识别发现人物和动作，自动录制并生成聚会集锦。

## 📢 官方公告

**[OpenAI 推出青少年版 ChatGPT](https://openai.com/index/chatgpt-for-teens)**

系统识别到 13 至 17 岁用户后，会自动加强自残、暴力等内容防护。家长可设安静时段；OpenAI 还将与 CodeAI 推进 AI 素养教育。

## 📌 行业简讯

- [Jane Street 7 月约亏 150 亿美元](https://www.ft.com/content/47dd5308-dd17-404a-a615-61046defd697)
- [Sentence Transformers 支持多向量嵌入](https://huggingface.co/blog/multi-vector-encoder)

## 🎪 乐子汇总

**[不会装电脑的人让 Codex 接管了新 MacBook](https://x.com/emollick/status/2089512978575950080)**

Ethan Mollick 的父亲多年没用笔记本，拿到新机器后直接让 Codex 处理设置和软件安装。

**[Claude 给冷门惠普打印机写了 macOS 驱动](https://x.com/kuberwastaken/status/2089377982536388964)**

这台设备只支持 Windows，官方没有提供 Mac 驱动，用户让 Claude 现场开写。

**[60 美元二手显卡也能跑 70B 模型](https://huggingface.co/papers/2608.14614)**

团队用 128 张二手 V100 搭出约 2.2 万美元的集群。它真的跑起来了，但耗电远高于新显卡。

**[1971 年的社交网络现在还能用](https://en.andros.dev/blog/54572bc7/finger-the-1971-social-network-that-never-died/)**

Finger 没有账号、算法和中心服务器，个人动态只是自己控制的一份纯文本文件；半个世纪后仍有客户端和活跃社区。

**[有人把铁路网当成巨型平板扫描仪](https://philo.gay/linecam/)**

工业线扫相机每次只拍一条竖线，列车或渡轮移动时再把几万条线拼起来，就能得到横跨整段路程的超宽照片。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [如果 AI 消灭人类，所有人会在同一秒倒下吗？](https://manifold.markets/Writer/if-ai-wipes-out-humanity-will-every) — **8.7%**（成交额 36.4k mana）
- [2100 年前，AI 会消灭地球上所有生物生命吗？](https://manifold.markets/LarsDoucet/will-ai-wipe-out-all-biological-lif) — **7.8%**（成交额 5.9k mana）
- [2030 年前，会出现核电驱动的 AI 数据中心吗？](https://manifold.markets/JesWolfe/will-there-be-an-ai-data-center-pow) — **74.3%**（成交额 4.0k mana）

---

*AI 日报 · 8月18日 · Telegram 频道 @dragonbro888*
