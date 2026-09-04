## 🗞️ 行业大事

**🥇 [Nscale 拿千亿美元算力合同冲刺上市](https://www.theinformation.com/briefings/exclusive-nscale-touts-100-billion-plus-contracted-revenue-anthropic-win)**

Anthropic 新订单价值四百五十亿美元。Nscale 向潜在投资者展示的多年期合同总额因此增至约一千零三十亿美元，平均期限五点七年。

公司第二季度收入刚过一亿美元，却可能最早本月上市。AI 算力公司正用多年期租约，把未来需求提前变成扩张资本。

**🥈 [Meta 不再按 token 用量考核工程师](https://www.theinformation.com/briefings/exclusive-meta-tells-engineers-ai-token-usage-part-performance-reviews)**

Meta 已有 93％ 的代码变更获得 AI 辅助。经理不再看使用仪表盘或 token 数量，改看质量、速度、问题复杂度和承担范围。此前有员工为了指标刻意烧完 token。公司仍在推动 AI，只是把考核重点放回工作结果。

**🥈 [李飞飞的新模型把视频变成三维世界](https://www.worldlabs.ai/blog/atlas)**

Atlas 能根据一至六张参考图和指定相机路径，生成最长一分钟、1440p 的视频，还能通过少量图片或手机录像重建三维空间。创作者可以选择观看角度。机器人也能用它模拟不同路径下看到的彩色与深度画面。

另见：[The Information](https://www.theinformation.com/briefings/fei-fei-lis-world-labs-unveils-new-world-model)

**[KKR 为百亿美元 AI 基建平台找来两名主管](https://www.theinformation.com/articles/two-new-executives-steering-kkrs-10-billion-ai-infrastructure-bet)**

两人分别负责数据中心和能源。Helix 准备把算力与供电打包卖给云厂商，并收购缺资金或电力接入的开发商。

**[Kairos 获五千万美元扩建 AI 安全人才项目](https://www.lesswrong.com/posts/DRaePC8aqLYTbEjTD/kairos-has-raised-usd50m-to-build-talent-infrastructure-for)**

两年期资助将用于研究培训、大学社群、工作坊和新机构孵化。团队计划从十二人扩到年底十八人。

## 📖 深度长文

**🥈 [AI 参考的网站可能是专为 AI 设计的](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations)**

研究者针对 AI 搜索与答案引擎 Perplexity 进行测试，发现 AI 引用的大量信息来源，并非来自主流、权威网站，而是来自一些专门为被 AI 抓取而生成的、内容质量可疑的网站。信息来源也存在长尾效应，不集中于维基百科、知名评测站等头部网站，反而分散在大量不知名、新注册的域名中。

## 🧪 新鲜论文

**🥈 [字节：Agent 的自我改进闭环可能越改越差](https://huggingface.co/papers/2608.31111)**

团队提出了一个新基准测试，只提供能力目标，隐藏下游的评估任务。发现 Agent 能实现自己解释模糊目标、挑数据、自测自评、训练模型的循环，还能修改运行脚手架，但权重层面的提升依然不稳定；迭代出的最强框架，表现也依然不如人工设计的方案。AI 容易选错数据，相信过度狭隘的评估，继续训练还会抹掉早期提升，局部进步的可迁移性也比较差。（编者注：人类的先验知识可能泄漏进评估题目，这也可能造成人类设计的迭代路径在人类编写的题目上表现更好）

另见：[S3Gym](https://huggingface.co/papers/2608.31100) · [HarnessDev](https://huggingface.co/papers/2609.01437)

**[模型发现身份矛盾后仍会替它辩护](https://www.lesswrong.com/posts/5RcKGJBnKw3vweYym/incoherent-ai-identities-can-also-be-stable)**

AI 对自身的不自洽身份很宽容，甚至会主动合理化。越是聪明的模型，应对认知失调的方式越像人类。

**[提前预测任务结局，降低 Agent 评测成本](https://huggingface.co/papers/2609.02783)**

看到 Agent 做到一半，就预测成败并叫停。三项基准最多省下 26％ 的步骤和 44.1％ 的输入 token。

**[先把论文编译成仓库规格，再让 Agent 写代码](https://huggingface.co/papers/2609.02272)**

PaperCompiler 先整理算法要求和文件依赖，再让 Agent 生成整套仓库。严重问题占比从 13.2％ 降到 6.1％。

**[英伟达模型在 IOI 题集上超过人类第一名](https://huggingface.co/papers/2609.02849)**

Ultra-CC 得到 535.4 分，人类最高为 498.27 分。它会反复生成、测试和修正解法。

## 📢 官方公告

**[Google 发布 Gemini 3.8 Flash 和网安版](https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber)**

普通版已进入 Gemini 应用、搜索、表格和开发者 API。网安版主攻漏洞发现与修补，面向政府、关键基础设施和软件维护者。

**[Meta 发布 Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3)**

新版本能追踪多条工作流，遇到歧义会提问，重要操作前会确认。相比上一版，平均少用 25％ 的 token。

**[微软开源实时语音识别模型](https://huggingface.co/papers/2609.02812)**

VibeVoice 能边听边输出谁说了什么。十五亿和七十亿参数版本的权重与推理代码已经公开。

## 📌 行业简讯

- [Resolution 新建 Agent 基础研究团队](https://www.lesswrong.com/posts/qTNm8qzqhhpno58fZ/resolution-has-a-new-agent-foundations-team)
- [Qdrant 发布百亿规模向量检索数据集](https://huggingface.co/blog/Qdrant/fineweb-10b-release)
- [美国政府称已重新信任 Anthropic](https://www.axios.com/2026/09/02/lutnick-anthropic-trump)

## 🎪 乐子汇总

**[Fable 5.1 把《伊利亚特》船队做成 3D 目录](https://x.com/emollick/status/2095352019498447090)**

二十九支部队、一千一百八十六艘船和约一百七十八个地名被摆上地图，还派 Agent 检查画面和准确性。

**[有人用强化学习教模型画水彩](https://huggingface.co/blog/train-to-paint-with-code)**

模型写约一百五十行 JavaScript，只能调用十种画笔方法。练到最后，它少画空白和脏色块，学会多铺颜料。

**[Claude 的系统提示词不许它复现歌词](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt)**

整首、最后一句、副歌和旋律音符都不行。用户逐行贴出并声称是自己写的，Claude 也得拒绝。

**[最大暗物质探测器只看到一个奇怪粒子](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle)**

LUX-ZEPLIN 记录到一次 248keV 碰撞。普通暗物质理论本应伴随大量低能事件，这颗粒子若来自暗物质，就得更复杂。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [AI 会在 2028 年前解决 ARC 抽象推理基准吗？](https://manifold.markets/MGM/ai-solves-the-abstraction-and-reaso-6312f0f1cbc1) — **21.4％**（成交额 12.5k mana）
- [2028 年前会出现无法被人类关停的失控 AI 吗？](https://manifold.markets/SG/rogue-ais-before-2028) — **60.0％**（成交额 24.5k mana）
- [AI 会让美国失业率在 2030 年前超过 10％ 吗？](https://manifold.markets/ahalekelly/will-ai-cause-the-us-unemployment-r) — **25.3％**（成交额 34.1k mana）
- [AI 会在 2030 年底前独立主导一家工厂吗？](https://manifold.markets/JoeandSeth/will-an-ai-run-a-factory-by-the-end-ELP0S9ZPAn) — **21.5％**（成交额 3.0k mana）

---

*AI 日报 · 9月3日 · Telegram 频道 @dragonbro888*
