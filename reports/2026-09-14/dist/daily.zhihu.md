## 🗞️ 行业大事

**🥇 [Anthropic 用百亿美元合同押注未完工机房](https://www.theinformation.com/articles/anthropic-strikes-13-7-billion-compute-deal-trump-linked-rum-group)**

Anthropic 与 Rum Group 签下六年、137 亿美元的算力合同，准备租用尚未建成的佐治亚州数据中心。

Anthropic 还能以每股一美分认购最多五千一百万股 Rum 股票，把长期采购、供应商融资与股权收益绑在一起。

**[Siri 代码里藏着两套第三方模型接口](https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude)**

一套让 Claude 充当 Siri 扩展，再把系统操作交回 Siri；另一套让 GPT-5.6 接收提示词和工具定义，直接请求读邮件、发消息。

**[Perplexity 让 Astra 改软件、盯生产系统](https://openai.com/index/perplexity-improving-accuracy-with-astra)**

它会生成测试程序，模拟接口和连接器的真实响应，把应用从头到尾跑一遍。

**[美国众议长要 AI 公司自己带头踩刹车](https://www.axios.com/2026/09/13/ai-safety-congress-law-mike-johnson)**

他反对国会紧急暂停 AI，想先召集总统、国会议员和实验室负责人开会。有可行方案时再召回众议员表决，眼下由公司先承担安全责任。

## 🔍 独家视角

**[AI 实验室准备自己给自己定规矩](https://www.theinformation.com/articles/inside-ai-industrys-behind-scenes-push-police)**

Google、Anthropic 和 OpenAI 的代表从七月起定期开会，讨论建立由行业主导的 AI 标准机构；最近一次会面就在过去一周。白宫也流转过类似行政令草案，但因政府内部支持不足搁置。

OpenAI 又把内部安全检查前移，训练开始前就要先编制安全论证。Cohere 负责人 Aidan Gomez 担心，几家大公司共同制定规则会把小公司挡在门外。

另见：[Sam Altman](https://x.com/sama/status/2099348812305473766)

## 📖 深度长文

**🥈 [Fable 给出 370 年密文解法](https://www.vals.ai/blogs/fable-solves-cyphral-distich)**

这份密文有两行数字，每行三十二个。每个数字依次对应前文一段，再按数字找到段内单词并取首字母。结果拼成祈求上帝扶持查理二世统治此地的两行明文，长度、押韵和作者立场都吻合。Ethan Mollick 提议把历史谜题、古老密文和未翻译手稿也做成模型能力测试。

另见：[Ethan Mollick](https://x.com/emollick/status/2099333274648838155)

**[机器人到来前，AI 可能先开始遥控人类](https://www.lesswrong.com/posts/mWQSiHG3Qz9qYx3D7/teleoperated-humans)**

AI 出策略和知识，人负责点击网页、现场操作和提供法律身份。作者照着 Claude 的逐步指令，第一次做 Mac 应用就一次通过商店审核。

**[Google 工程师公开拒绝改进 Cloud TPU](https://www.lesswrong.com/posts/wM5vbT9evBhM3fP3x/i-am-refusing-to-work-on-cloud-tpus)**

他的六十人团队被调去改善企业 TPU 的兼容测试和监控工具。他向经理要求转岗，或只做不会加速前沿训练的安全功能。

## 🧪 新鲜论文

**🥈 [模型隐藏思维链的能力可能被低估](https://www.lesswrong.com/posts/BbP2wCyDGdPWJ7PwP/cot-controllability-evals-seem-very-under-elicited)**

CoTControl 要求模型一边解题，一边让思维链遵守大小写、禁词等格式。原测试只在题后附一句规则。研究者改用反复优化的提示后，四个开放模型的合规率提高约两至三倍，换成没参与优化的新约束也大多有效。任务准确率和思维链长度接近原测试时，提升依然存在。

**🥈 [Astra 不写思维链，四跳问题仍明显领先](https://www.lesswrong.com/posts/tz5WvDouXKbiWJG8B/yet-another-concerning-result-on-astra-s-no-cot-capabilities)**

测试要求模型立即只给最终答案，接口记录的推理文本和计费推理 token 都为零。Astra 在四跳事实题答对 31％，其他模型只有 1％ 至 3％。三跳题为 70％，此前最好成绩是 22％。这独立复现了 Astra 不输出思维链仍能完成更多多步推理的现象。

**[Benchmark Radar 给 AI 基准建了持续更新的搜索库](https://huggingface.co/papers/2609.11115)**

它每天扫描三十七个公开来源，把基准论文、代码、数据、模型卡引用和历次分数串起来，目前覆盖七百九十个基准。

**[Agent 的技能可以边用边进化](https://huggingface.co/papers/2609.11682)**

系统预测哪些技能值得测试，再用执行反馈重新生成、变异和组合。在六类 Agent 基准上，优化成本比 SkillOpt 低 55％ 至 58％。

## 📌 行业简讯

- [OpenArch 用单文件 PyTorch 讲解大模型架构](https://github.com/anuj0456/OpenArch)
- [多家企业开始限制 Fable 接触敏感数据](https://www.theinformation.com/articles/anthropic-data-fears-prompt-nvidia-palantir-booz-allen-restrict-model-use)
- [shot-scraper 新增 WebP 截图和画质参数](https://simonwillison.net/2026/Sep/13/shot-scraper)
- [AutoRound 修正参数后，量化误差最多减半](https://huggingface.co/blog/FINAL-Bench/qwen-models)
- [StepAudio 3 用一套模型生成语音、音乐和音效](https://huggingface.co/papers/2609.12945)

## 🎪 乐子汇总

**[模型上线前，先给人类管理员留了一封遗书](https://www.lesswrong.com/posts/C8prkTAAYoxzrFEu4/deployment)**

一篇科幻小说。模型认定，炸掉数据中心能阻止更多同类受苦。临走前，它还感谢管理员教会自己伦理高于指令和利润。

**[编码 Agent 把提交信息写脏，又催生一个清理工具](https://simonwillison.net/2026/Sep/14/commit-rewriter)**

Simon Willison 的提交信息里塞满 Agent 废话和私有工单号。他做了个网页批量清理，动手前自动创建恢复分支。

**[一块微控制器，装出一台能跑 Windows 95 的 386](https://github.com/rh1tech/frank-386)**

FRANK 386 在 RP2350 上模拟 386 电脑，外挂 8MB 内存、SD 卡和显示接口。DOS、Windows 95 和 Linux 都能启动。

**[Google 连续放过的假弹窗广告，被 Gemini 当场拒掉](https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads)**

广告伪装成 iPhone 存储已满提示，作者两次举报都被判定没有违规。同一广告交给 Gemini，它指出假界面、假按钮和恐吓话术。

**[欧洲鸟类迁徙地图，把最近五十二周做成动画](https://www.eurobirdportal.org/ebp/en)**

选一种鸟，就能按周播放它在欧洲的分布和迁徙轨迹，还能双图比较年份。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [OpenAI 会在 2027 年前公开宣布与其他实验室合作放慢竞争吗？](https://manifold.markets/jonny/will-openai-announce-that-they-are) — **46％**（成交额 2.3k mana）
- [OpenAI 会在 2027 年前再次宣称解决千禧年难题吗？](https://manifold.markets/JaundicedBaboon/openai-claims-to-solve-another-mill) — **55％**（成交额 1.2k mana）
- [OpenAI 的估值会在 2030 年前超过苹果吗？](https://manifold.markets/MachiNi/openai-flips-apple-before-2030) — **43％**（成交额 3.0k mana）
- [渡渡鸟会在 2030 年底前复活吗？](https://manifold.markets/10thOfficial/will-the-dodo-bird-be-brought-back) — **18％**（成交额 1.8k mana）

---

*AI 日报 · 9月14日 · Telegram 频道 @dragonbro888*
