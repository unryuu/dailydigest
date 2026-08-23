## 🗞️ 行业大事

**🥇 [英伟达部分 AI 服务器系统预计涨价 17％](https://www.theinformation.com/articles/nvidia-ai-chip-prices-rise-17-server-makers-tell-customers)**

涨价主要涉及明年交付的 Grace Blackwell 300 和 Vera Rubin 200 系统，幅度会随芯片代际与内存配置变化，并非全线统一调价。两家媒体从收到通知的客户侧获悉，内存等组件成本上升是主要原因。

按当前系统价格估算，一座 1 吉瓦数据中心可能至少多花 50 亿美元。云厂商会自行消化多少、又会向租用算力的客户转嫁多少，目前还不清楚。

另见：[彭博交叉报道](https://www.bloomberg.com/news/articles/2026-08-22/nvidia-customers-notified-about-ai-related-price-hikes-above-15)

**🥈 [阿里拟配售新股募资 800 亿港元](https://www.theinformation.com/briefings/alibaba-seeks-raise-10-billion-share-sale-fund-ai-investments)**

资金将用于继续扩大 AI 投资，交易面向美国以外的投资者，最终价格和规模仍可能变化。阿里截至六月的季度资本支出已接近 100 亿美元，同比增长 75％，主要投向 AI 基础设施。此次计划再以股权融资补充资金。The Information 称交易获超额认购，但这只是匿名知情人士的说法。

## 🔍 独家视角

**[AI 开始处理没人愿意帮你的麻烦](https://x.com/emollick/status/2091364843831906416)**

邮件里的低风险表格已经可以交给桌面 Agent 代填。政府手续、学校表格等复杂杂务，也可能成为消费级 AI 的实用场景。

但它要接管浏览器和文件权限，用户还得逐项核对结果。能不能放心授权、能不能发现填错，正成为实际使用门槛。

另见：[桌面 Agent 代填表格](https://x.com/emollick/status/2091207070951395337)

**[Ox Alpha 更像细致小工](https://x.com/emollick/status/2091238983724343543)**

早期体验显示，它会主动把具体的长程子任务做到底；另一组测试却认为，总体能力连开放模型前沿也够不上。

现阶段更像是范围明确的子任务执行者。结论来自两名用户的个人实测，模型身份、权重状态和系统评测都未确认。

另见：[长程子 Agent 体验](https://x.com/teortaxesTex/status/2091428397951877129)

## 📖 深度长文

**🥈 [科学家不信 AI 十年治愈多数疾病](https://www.theinformation.com/articles/ai-probably-cure-cancer-anytime-soon-scientists-say)**

AI 已能帮助检出影像中的小肿瘤、招募临床试验患者和设计药物。可从候选线索走到安全有效的疗法，还要经过漫长的实验与临床验证。AlphaFold 已广泛进入科研，却没有直接带来一种疾病的治愈方案。科学家质疑五到十年治愈多数疾病的时间表，并不否认 AI 对医药有用。

**[人们可能一边讨厌 AI，一边每天使用](https://x.com/emollick/status/2090926132790985153)**

Mollick 推演，AI 公司形象低迷时，人们仍可能频繁使用，并依恋自己偏爱的模型。这没有民调或使用数据支持。

## 🧪 新鲜论文

**🥈 [改提示词更能检验模型为什么这么做](https://www.lesswrong.com/posts/ExB6KYDcznaFS72eT/evaluating-explanations-of-llm-behavior-in-the-wild-with)**

三种读取内部激活的工具，都没有让预测 Agent 胜过只看对话的基线。研究者把解释变成可复现实验：改掉提示词中的一个因素，再看异常行为会不会跟着变化。把这些反事实结果拿来训练后，两个模型对未见场景的预测都改善了。任务主要是原因简单、可重复采样的行为，不能据此否定所有可解释性方法。

**[Llama 觉得用户学历高，更容易放弃正确答案](https://www.lesswrong.com/posts/87oeYXEjf7XgitbBg/llama-will-abandon-a-correct-answer-if-it-thinks-you-re)**

用户坚持错误答案时，模型向「高学历用户」让步从 62％升到 97％，认定对方「低学历」时降到 39％。实验只测旧 Llama 和小学算术。

**[长上下文推理只计算一部分注意力](https://huggingface.co/papers/2608.19758)**

在 H20 的十二万八千 token 测试中，FP8 推理最高比同代稠密实现快 30.49 倍。结果不能外推到所有模型和硬件。

**[普通单目视频可以重建动态三维人像](https://huggingface.co/papers/2608.20335)**

它从未标定的单目视频补出一致的多视角，再把人物重建成随时间运动的三维模型。作者称它在两个数据集超过旧方法，也能处理野外视频。

**[多人图像生成先规划谁站哪里](https://huggingface.co/papers/2608.20336)**

系统先给参考脸绑定身份和位置，再按统一布局生成最多十人的合照。作者测试中，它覆盖 97.3％的指定人物，重复率为 2.8％。

## 📌 行业简讯

- [Prime Intellect 开放 NanoGPT 训练竞速榜](https://www.primeintellect.ai/research/nanogpt-speedrun)

## 🎪 乐子汇总

**[机器人撞墙起火，观众为公开失败鼓掌](https://x.com/teortaxesTex/status/2091308101181800711)**

视频来自北京机器人运动会。设备型号、安全调查和起火原因都没有公开，转发者称赞团队愿意公开试错。

**[青铜时代的神庙粮仓也像一个失控 Agent](https://www.lesswrong.com/posts/mPrbyBsGmNfWWgJmi/misaligned-ai-in-the-bronze-age)**

乌鲁克的粮仓原本用于抗饥荒，后来连成宗教、地主、雇主和军队。作者把这套制度写成用人、纸和粮食运行的自我扩张 Agent。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [AI 大量参与制作的电影会获得主流观众赞誉并引发反弹吗？](https://manifold.markets/ZviMowshowitz/soai7-a-movie-or-short-film-produce) — **64.8％**（成交额 3.7k mana）
- [艺术家针对多家 AI 图像生成器的集体诉讼会成功吗？](https://manifold.markets/anne/will-the-classaction-lawsuit-by-art) — **19.8％**（成交额 5.6k mana）
- [2040 年前，AI 能按文字要求设计会折叠成纳米机器的聚合物序列吗？](https://manifold.markets/IhorKendiukhov/will-we-have-a-text-to-polymerseque) — **38.9％**（成交额 1.3k mana）
- [Yudkowsky 会在输掉 UFO 赔率一年后，把 UFO 现象与 AI 联系起来吗？](https://manifold.markets/FranklinBaldo/will-eliezer-yudkowsky-associate-th) — **47.9％**（成交额 1.7k mana）

---

*AI 日报 · 8月23日 · Telegram 频道 @dragonbro888*
