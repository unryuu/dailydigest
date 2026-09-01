## 🗞️ 行业大事

**🥇 [AI 收费不再只靠订阅](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads)**

ChatGPT 广告上线不到两百天，年化收入运行率达到 10 亿美元。系统用当前对话里的意图匹配广告，在当地规则和用户设置允许时，也可能参考更广泛的使用背景。广告由此开始补贴免费访问。

企业端也在试验另一种付费方式。Salesforce 允许客户按 Agent 增加的销售收入或节省的客服成本付费；OpenAI 也让部分大客户只为完成的任务付费。难点在于，业绩变化可能同时来自产品、营销或季节，收费双方得先说清 AI 到底贡献了多少。

另见：[The Information](https://www.theinformation.com/articles/salesforce-overhauling-way-charges-ai)

**🥈 [英伟达向联发科投资 35 亿美元](https://www.theinformation.com/briefings/nvidia-invests-mediatek)**

英伟达通过购买联发科发行的可转换债券完成投资。双方将继续开发未来几代消费级电脑 Spark 芯片。商用电脑方案会组合英伟达 GPU 和联发科技术。报道没有披露转股条件、最终持股比例或产品时间表。

**🥈 [OpenClaw 可以把完整会话搬到远端](https://github.com/openclaw/openclaw/releases/tag/v2026.8.1)**

旧版本已经能在远程节点调用工具。这次大更新把会话的运行位置和工作目录，一起放到远端设备，再同步结果。云机器闲置后可以暂停，收到下一条消息时重新分配，并保留会话和对账后的工作区。

## 📖 深度长文

**🥈 [ChatGPT Work 其实是两套产品](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work)**

作者让云端版克隆 GitHub 仓库、安装依赖，再启动完整浏览器填写网页；本地版则直接读写电脑文件、运行本机程序。云端会话的目录能跨会话保留，还可调用子 Agent 并行工作。

**🥈 [AI 可以靠寻找互利交易来说服人](https://www.lesswrong.com/posts/2qDpf6Tvu7dxtRve7/persuasion-as-market-making)**

模型只要找到同时让对方和自己受益的行动，再用真实证据说明好处，就可能形成很强的说服力。它可以同时追踪许多人的偏好和资源，撮合人类原本找不到的交换。

**[一篇教程从遮词开始搭建扩散语言模型](https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model)**

模型先遮住随机词，再反复补词和修改整段文本。长文本还要靠分块、重新遮词纠错和采样蒸馏。

## 🧪 新鲜论文

**🥈 [最好的 Agent 控制器也难完成整套工程任务](https://huggingface.co/papers/2608.28281)**

固定底层写代码的 Worker，只比较上层 Controller 怎样安排下一步、验证结果和决定停止。最佳完整任务成功率只有 24.69％。这说明模型即使会写代码，上层控制循环仍可能相信过期进度、漏掉验证或过早收工。

**[一篇综述把 Agent 交付完整产物单独划成研究方向](https://huggingface.co/papers/2608.28122)**

作者梳理 259 项工作，把交付过程拆成产物表示、构建策略和运行时验证。拆任务会增加协调成本，模型裁判也可能与生成器共享盲点。

**[Agent 把物理世界写成可执行代码再验证](https://huggingface.co/papers/2608.27549)**

它从文字或视频提出物体状态和运动规律，反复运行、渲染并核对代码假设，再用验证过的世界训练模型做定量物理推理。

**[清华团队用消费级 RTX 5090 训练 20 亿参数模型](https://huggingface.co/papers/2608.27370)**

团队用多张 RTX 5090 从零训练，成本低于 6900 美元。

## 📢 官方公告

**[DeepSeek 开放首个 V4 多模态实验模型](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)**

它在 V4-Flash 上加入视觉模块，开放分词器和最小推理实现，仓库采用 MIT 许可证。

## 📌 行业简讯

- [Wirewiki 给 2.4 亿个域名做近零延迟补全](https://ruurtjan.com/articles/p99-0ms-autocomplete-for-240-million-domain-names)
- [VLANeXt 发布机器人模型实验代码库](https://huggingface.co/blog/cavanloy/vlanext)

## 🎪 乐子汇总

**[机器人三定律拿来约束真实 AI 不太管用](https://x.com/emollick/status/2094302639072715023)**

Ethan Mollick 说，三定律恰好说明单靠规则很难解决 AI 道德；阿西莫夫也得让机器人钻空子，故事才写得下去。

**[完全拒绝拟人化，可能反而看不懂 Agent](https://x.com/tszzl/status/2094136131537555891)**

把 AI 想成住在电脑里的家伙会产生错误抽象，但也许仍能帮助理解未来 Agent。

**[12TB Steam 泄漏翻出十多年消失的游戏史](https://arstechnica.com/gaming/2026/08/a-12tb-steam-teraleak-spills-more-than-a-decade-of-lost-pc-gaming-history)**

材料覆盖 2003 至 2013 年的 Steam2 服务器，包含删减内容、原型和测试版。

**[1980 年的太空实验室电脑还在用磁芯内存](https://www.righto.com/2026/08/spacelab-core-memory.html)**

法国 Mitra 125 MS 用大约 118 万枚铁氧体小环做成 128KB 内存，占电脑约三分之一。它断电不丢数据又抗辐射。

**[蓝光比其他颜色更容易让眼睛看不清细节](https://research.uga.edu/news/blue-light-has-a-surprising-effect-on-your-eyes-study-finds)**

60 名年轻人辨认两点光源时，蓝光要拉得更远才看得出两个点。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [Greta Thunberg 会在 2035 年前加入 AI 安全或暂停运动吗？](https://manifold.markets/Simon74fe/greta-thunberg-joins-ai-safetypause) — **54.6％**（成交额 7.4k mana）
- [2050 年前，AI 会拥有情感吗？](https://manifold.markets/Nlgn/will-ai-be-able-to-feel-emotions-be) — **37.6％**（成交额 1.1k mana）
- [10 月 1 日，Moonshot AI 的估值会到多高？](https://manifold.markets/MNX/moonshot-ai-valuation-on-mnx-octobe)（成交额 8.0k mana）
  - 超过 500 亿美元 **94.9％**
  - 超过 1000 亿美元 **54.4％**
  - 超过 2000 亿美元 **28.0％**
  - 超过 4000 亿美元 **6.4％**
- [Scott Aaronson 描绘的哪一种 AI 世界最可能成真？](https://manifold.markets/jacksonpolack/which-scott-aaronson-ai-world-will)（成交额 10.3k mana）
  - AI 影响有限 **10.0％**
  - 技术大发展、文明延续 **36.1％**
  - AI 造成严重伤害、文明延续 **15.0％**
  - AI 像善意神祇般自治 **31.9％**
  - AI 导致灭绝等结局 **7.0％**

---

*AI 日报 · 8月31日 · Telegram 频道 @dragonbro888*
