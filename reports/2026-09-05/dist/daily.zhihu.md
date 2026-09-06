## 🗞️ 行业大事

**🥈 [Coatue 和 MatX 用合资锁定芯片产能](https://www.theinformation.com/articles/coatue-matx-talks-new-multibillion-chip-financing-venture)**

资金将用于提前购买内存、逻辑晶粒，并预订台积电等制造产能。MatX 预计 2027 年上半年完成流片，原型兼顾训练和推理。Coatue 也在讨论参与 MatX 新融资。目标估值约八十亿美元。

**🥈 [Anthropic 考虑自建支付和计费系统](https://www.theinformation.com/articles/anthropics-house-payments-tech-push-chip-away-stripe)**

招聘范围已覆盖订单、开票、税务和支付审批。实时反欺诈、争议处理和资金管理也在范围内。岗位描述称，业务增长速度已经超过现有流程和系统。模型公司正把部分金融基础设施收回内部。

**[IBM 推出 Bob 代理式开发伙伴](https://bob.ibm.com)**

Bob 能在代码库里调用多个代理并行工作，也能从命令行运行，主攻遗留系统现代化、合规和安全交付。

**[Spotify 用 Portal 把 Claude Code token 用量降了 90％](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90)**

Portal 把读大文件和生成样板代码交给 Gemini 2.5 Flash，再让 Claude 处理推理任务。

**[VLM Run 推出统一 API 托管开放权重视觉模型](https://huggingface.co/blog/vlm-run/introducing-gateway)**

Gateway 用一个接口接入 OCR、视觉语言和 ViT 模型，只改模型名即可切换，目前免费且无需注册。

## 📖 深度长文

**[CHIVE 训练模型预测并解释自己的行为](https://www.lesswrong.com/posts/YyAMz52wDxnLhwvWL/training-models-to-predict-and-explain-their-in-the-wild)**

它用反事实改写找出行为原因，再将实验结果制成训练数据；预测能迁移到新任务，自我解释效果不稳定。

**[Artificial Analysis 发布 Intelligence Index 4.2](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2)**

新版加入两项测试，40％ 权重来自私有留出集；Claude Fable 5.1 第一，GPT-6 Astra 第二。

## 🧪 新鲜论文

**🥇 [Claude 用十一天把费马大定理写进 Lean](https://www.anthropic.com/research/formalizing-fermats-last-theorem)**

多 Agent 团队借助 Prove2Me，完成了端到端、由计算机检查的形式化证明。它把 Wiles 路线改写成机器能逐步核验的形式，创新落在验证已有证明，没有提出新数学。

成品约 1300 万行，消耗约 60 亿输出 token。早期 Agent 会丢失项目状态；Prove2Me 用定理关系图安排下一步，并支持并行、快速编译和搜索复用，让协作最终跑通。

**🥈 [DRACO 把长任务总分拆给每一步](https://huggingface.co/papers/2609.04094)**

它在每轮长任务结束后动态生成评分标准，再把整条轨迹的评价分配给具体步骤。不需要程序验证器，也不额外训练归因模块。AppWorld 成绩比基础模型高 15.9 分。所有轨迹都通过的标准会被丢弃，避免评分失去区分度。

**🥈 [LLaDA-Image 开放完整图像训练配方](https://huggingface.co/papers/2609.03796)**

这是一个从零训练的 6B 图像生成和编辑模型。团队放出了权重、训练代码，以及从预训练、优化器到蒸馏的详细步骤。模型还被蒸馏成只需 2 至 4 步的 Turbo 版。它也支持中英文文字渲染。

**[VeriPhy 给视频物理判断留下证据链](https://huggingface.co/papers/2609.03153)**

在 149 个核心视频里，它覆盖了 304 条人工缺陷记录中的 228 条；每个判断都保留可追溯证据。

## 🎪 乐子汇总

**[《源氏物语》被读成一部贵族恋爱灾难喜剧](https://www.astralcodexten.com/p/your-book-review-the-tale-of-genji)**

隔屏恋爱、暗号诗歌和复杂等级被讲成宫廷连续剧；源氏把十岁女孩带走养大后结婚，让现代读者很难不出戏。

**[有人用吊床解释滑轮为什么能省力](https://www.lesswrong.com/posts/RPWoz6tYQtyinCyrn/f-ing-pulleys-how-do-they-work)**

核心是让树或天花板分担重量，轮子只负责让绳子顺滑并改变拉力方向。

**[OpenTrailPaper 做了台开源电子墨水骑行电脑](https://opentrailpaper.com)**

4.7 英寸屏配有 GPS、触摸、前灯、SD 卡和蓝牙，续航约 7.4 小时；裸板没有防水。

**[statichost.eu 做欧洲基础设施上的静态站托管](https://www.statichost.eu)**

它从 Git 仓库构建网站，提供自定义域名、免费 SSL 和即时回滚，部署和 CDN 都使用欧洲公司的设施。

**[penlu 公布 RSA-260 的一个 130 位因子](https://x.com/penlume/status/2095372672356212876)**

把 RSA-260 除以帖子给出的整数，就能得到另一个因子。马斯克也来围观。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [AI 会在 2026 年 9 月解决千禧年大奖难题吗？](https://manifold.markets/jim/ai-solves-millennium-prize-problem) — **16％**（成交额约 22k mana）

---

*AI 日报 · 9月5日 · Telegram 频道 @dragonbro888*
