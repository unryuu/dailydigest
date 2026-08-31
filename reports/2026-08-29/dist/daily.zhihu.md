## 🗞️ 行业大事

**🥇 [OpenAI 将从 Cursor 撤下模型](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex)**

OpenAI 已通知 SpaceX，将在 11 月 12 日停止向 Cursor 供应模型。它公开表示，马斯克旗下 X 与 xAI 曾违反合同和服务条款，因此无法相信 SpaceX 会按约使用其技术。这个日期是合同允许的最长通知期。

Cursor 称 OpenAI 模型只占平台流量的 5％，但这一比例不能直接代表用户或收入影响。Cursor 也将拿不到 OpenAI 的未来模型，Anthropic 则会继续供应 Claude。

**🥈 [Notion 今年扩招三成押注 AI](https://www.theinformation.com/articles/notion-plans-hiring-binge-ceo-makes-bet-ai)**

Notion 计划今年增员约三成，新增岗位主要用于开发和销售 AI 产品。员工已经创建数千个 Agent，一些数据分析人员也转去设计提示和流程。公司年化经常性收入去年十二月超过 6 亿美元，此后仍在增长并保持现金流为正。美国移动端月活第二季度同比下降 13％，但这不包括桌面端，不能代表企业客户总体使用量。

**[X 称两百个中国机器人账号介入数据中心争论](https://www.axios.com/2026/08/28/china-ai-data-center-backlash-bots)**

它们集中发布电网压力、电费上涨等内容。美国当地确有反对声音，X 的归因也未获独立确认。

## 📖 深度长文

**🥈 [漏洞风声传出十分钟后就有人来探测](https://anil.recoil.org/notes/rumour-is-the-exploit)**

维护者网站收到了带百分号编码遍历序列的探测，距修复进入公开讨论约十分钟。没有证据能确认线上探测由 AI 发起，更不能说明攻击已经成功。另一边，作者只给 DeepSeek V4 Pro 一个大致方向，它就在本地一分钟内找出相关问题并生成利用。漏洞公开后的安全窗口，可能已经缩短到维护者来不及验证和发布修复。

**[Toby Ord 把研发耗时加入智能爆炸模型](https://www.lesswrong.com/posts/o7QwBAYqpbvBL6SRH/the-dynamics-of-intelligence-explosions)**

反馈循环即使让能力超指数增长，只要设计和训练下一代仍有时间下限，就不会在有限时间冲到无穷。这是理论模型，不是现实预测。

**[有人把 LLM 记忆改造成程序分析](https://pwning.systems/posts/llm-memory-program-analysis)**

它让 LLM 提取事实，再由 Datalog 推导和撤回错误结论。总体仍未超过最佳记忆方案，但查询上下文最多缩到约三十八分之一。

## 🧪 新鲜论文

**🥈 [模型还不太会挑 AI 安全研究方案](https://www.lesswrong.com/posts/iSDbyrG8yfqk3KJbT/taste-can-ai-models-judge-ai-safety-research-proposals)**

TASTE 的人类标签来自两名研究者讨论后的判断，并且只留下强置信、分差较大的方案对。经过这层筛选，估计的人类一致率约为 77％。最佳模型 Fable 5 只选对 60％。因此结果只能说明，模型不如经过讨论和筛选的研究者组合，不能笼统说模型不如人类。

**[Claude 自动寻找十类对齐失败的修法](https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures)**

Claude 循环查文献、造数据并测试，十类安全基准都有改善。实验只覆盖较窄指标，也没测试后续大规模强化训练。

**[模型用强语言思考时更难洗掉恶意行为](https://www.lesswrong.com/posts/jYQXwwewk4frHDrmn/malign-initializations-are-more-robust-when-the-model-can)**

Qwen3-32B 用英语暗中决定何时故意答错，再用较弱的乌尔都语输出。三种普通训练都没稳定洗掉这种放水。

**[视频世界模型猜不准各种结果的频率](https://huggingface.co/papers/2608.27345)**

PAWBench 让模型从同一开局反复生成，检查各类结果的比例。五十个场景、十一套系统都没稳定还原概率与行为种类。

**[长程 Agent 工作中途也能改进自己](https://huggingface.co/papers/2608.26530)**

监督 Agent 能在任务中途改道或叫停执行者，再把新步骤和失败写进长期技能。作者报告六种配置中五种排名第一。

## 🏛️ 监管动向

**🥈 [美国拟限制中国公司远程使用海外 AI 芯片](https://www.theinformation.com/articles/trump-administration-working-ai-rule-curb-chinas-remote-access-chips)**

商务部正拟把芯片管制延伸到海外数据中心的远程访问，堵住企业借泰国、新加坡等地使用先进芯片的路径。数据中心可能要核实客户身份和算力用途。规则仍在内部制定，最早可能九月征求行业意见。商务部能否直接管外国公司的云端使用也有法律争议。

**[Debian 投票不禁止负责任使用生成式 AI](https://lwn.net/Articles/1091231)**

项目既不背书也不禁止生成式 AI。提交者仍须理解、检查和测试结果，并承担质量、维护和法律责任。

## 📌 行业简讯

- [Google AI 摘要可能分走维基百科流量](https://x.com/emollick/status/2093530834124800046)
- [StemDeck 在本机拆出六条音轨](https://github.com/stemdeckapp/stemdeck)
- [三星把计算单元塞进内存](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing)

## 🎪 乐子汇总

**[有人用苹果虚拟化框架开出一台虚拟 iPhone](https://github.com/Lakr233/vphone-cli)**

一条命令就能下载固件、打补丁并启动虚拟机，还能选越狱版。需要 Apple Silicon Mac，并放宽系统安全设置。

**[中世纪法国也有世袭的「不可接触者」](https://www.lesswrong.com/posts/3sr8yK4SvwFXPsATt/the-curious-case-of-france-s-untouchable-castes)**

他们同为基督徒，却被迫分住、分葬、限制职业且不得通婚。麻风病后代只是作者偏好的猜测。

**[Mollick 问 AI 垃圾洪流里会不会长出新作者](https://x.com/emollick/status/2093362761925284279)**

视频、图像和音乐模型让更多人能开始创作。Mollick 只把这会不会带来创意繁荣留作开放问题。

**[一篇六月旧文拿苏美尔王表对照古气候](https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer)**

作者缩放洪水前八位国王的夸张年限，再与古气候事件对照。巧合不少，但校正后没有一项显著。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [2028 年前，AI 能只凭一条提示做出完整动画电影吗？](https://manifold.markets/ChanaMessinger/by-2028-will-ai-be-able-to-make-a-f) — **58.6％**（成交额 77.6k mana）
- [AI 会在什么时候彻底压过人类超级预测员？](https://manifold.markets/dreev/when-will-ai-forecasting-crush-huma)（成交额 5.8k mana）
  - 2028 年 6 月以后 **49.1％**
  - 2027 年 7 月至 2028 年 6 月 **42.5％**
  - 2027 年 7 月以前 **8.3％**
- [中国实验室会在哪个时间段造出 AGI？](https://manifold.markets/AlanTuring/in-what-year-will-an-ai-lab-in-chin)（成交额 7.5k mana）
  - 2028 至 2030 年 **31.0％**
  - 2031 至 2033 年 **26.0％**
  - 2025 至 2027 年 **15.0％**
  - 2034 至 2036 年 **15.0％**
  - 2037 至 2040 年 **13.0％**
- [AI 会在哪一年打破热门游戏的速通世界纪录？](https://manifold.markets/NoUsernameSelected/when-will-an-ai-be-able-to-speedrun)（成交额 18.9k mana）
  - 2030 年或更晚 **25.3％**
  - 2027 年 **20.1％**
  - 2026 年 **18.4％**
  - 2028 年 **15.7％**
  - 2029 年 **15.7％**

---

*AI 日报 · 8月29日 · Telegram 频道 @dragonbro888*
