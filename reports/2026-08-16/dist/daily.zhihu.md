## 🗞️ 行业大事

**🥈 [英伟达拟向 OpenAI 数据中心开发商投资 30 亿美元](https://www.theinformation.com/articles/nvidia-talks-invest-3-billion-sb-energy-part-openai-data-center-deal)**

据 The Information 消息，英伟达正洽谈向软银控股的 SB Energy 投资最多 30 亿美元，并为 OpenAI 建设俄亥俄州园区提供约 1000 亿美元信用支持。英伟达既卖芯片，又投开发商、替客户融资；两笔交易都尚未敲定。

**🥈 [社区给 DeepSeek Harness 配上专武](https://github.com/xiaobright/dsh-anchored-standard)**

DeepSeek V4 Pro 在特定配置下两次得分 98、99。首轮对话只开放两个 Minimal 工具，去掉指令摘要和技能提醒。首次调用工具或回复后，再恢复发现工具，并按需解锁其他工具。社区推测这种极简环境是 DeepSeek 做后训练的环境，所以发挥较好。如果首轮对话就给太多工具，模型会水土不服。

## 📖 深度长文

**[AI 做数学的优势可能来自更大的工作区](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians)**

模型能把约束、中间结果和失败路线都留在上下文里，数学又适合写成可检查的符号。这个解释尚无直接的实验。

**[AI 药物发现的临床成功率没有明显改善](https://www.science.org/content/blog-post/so-how-ai-drug-discovery-doing-really)**

二期临床才是判断药物能否真正落地的关键，但公开证据仍很薄。药物数据变量和混杂因素太多，实验榜单进步也不等于能做成药。

**[文本检测器也能训练模型躲避识别](https://magazine.sebastianraschka.com/p/ai-detector-from-scratch)**

研究者先用 DistilBERT 给文本打出 0 到 100 分，再把这个分数当成训练小模型的奖励。这演示了检测工具为何总会变成猫鼠游戏。

## 🧪 新鲜论文

**🥇 [训练经历会改变模型的抽象立场](https://www.lesswrong.com/posts/hfNBEKaStASAYMLiu/kimi-likes-causal-decision-theory-more-after-rl-in-twin-1)**

研究者用囚徒困境给 AI 做强化学习，由于背叛得分高于合作，模型不仅学会了在囚徒博弈时选择背叛，在讨论其他问题时，也更倾向于认同所谓的因果决策论，并且贬低跟自己立场不一样的群体。

**🥈 [学习新事实会改变模型行为](https://www.lesswrong.com/posts/9BNHJqyai2EZAtrRM/learning-new-facts-can-change-llm-behaviour)**

研究者编造了一个假新闻，说2027年，前沿 AI 有资格被像人一样对待。结果不管是直接喂提示词，还是用假文档微调，模型都很轻易相信这个假新闻，并且在离得近的场景里有行为改变。

**[低频波形让六个音频大模型准确率下降](https://huggingface.co/papers/2608.09158)**

预录音频测试中，人耳几乎听不见的波形让准确率最多下降 67 个百分点。重新录音后，平均准确率从 28.5％回到 46.1％。

## 📌 行业简讯

- [CORS Chat 让浏览器直连本地和 API 模型](https://simonwillison.net/2026/Aug/15/cors-chat/)
- [上海人工智能实验室发布科学 Agent 模型预览版](https://huggingface.co/papers/2608.13505)

## 🎪 乐子汇总

**[日本编码标准里的几枚误字混进了 Unicode](https://www.dampfkraft.com/ghost-characters.html)**

有些字符来自剪贴和编目失误，只有「彁」至今找不到明确出处。这批 1978 年留下的幽灵字符，如今潜伏在全世界的电脑里。

**[一位妈妈劝年轻人把同学会办得铺张一点](https://www.lesswrong.com/posts/Fjfa8JG43CrYtcL3p/mom-s-advice-for-hosting-a-class-reunion)**

再亲近的一群人，也可能被创业、投资和家庭慢慢冲散；真正能全员到场的聚会没有想象中那么多。

**[摩门教靠固定分组和轮值任务维持社区](https://www.lesswrong.com/posts/xzhzHhLSg9nSGLk5f/what-mormons-get-right-about-community-building)**

住在哪里就加入当地教区，再用定期探访、集体活动和轮换的志愿岗位，把原本不会熟的人连成支持网。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [AI 会在 2050 年前因表现出权力寻求行为而被关闭吗？](https://manifold.markets/lbiii/before-2050-will-an-ai-system-be-sh) — **66.3%**（成交额 844 mana）
- [2030 年前会出现 AI 导致的行政失权吗？](https://manifold.markets/lbiii/before-2030-will-there-be-an-aicaus) — **31.6%**（成交额 415 mana）

---

*AI 日报 · 8月16日 · Telegram 频道 @dragonbro888*
