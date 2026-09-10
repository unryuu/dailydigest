## 🗞️ 行业大事

**🥇 [SpaceX 重做 xAI 数据中心](https://www.theinformation.com/articles/spacex-overhauls-data-center-build-potentially-slowing-expansion)**

xAI 曾用 122 天让十万块 GPU 上线，部分备用系统留到设施投运后再补。上周施工影响供电，Grok 和外部算力客户随之停机，研究类项目此前也因故障影响训练进度。

新团队要求先完成更多电力、冷却备份和测试，并减少临时设备。数据中心管理层已经换人，超过 300 名火箭与星链工程师调入支援，扩建速度可能随之放慢。

**[ChatGPT 不再接受竞争产品广告](https://www.theinformation.com/articles/openai-cuts-adobe-others-advertising-competing-ai-products-chatgpt)**

图像和音频生成产品被禁止投放，Adobe 等现有广告主也受到影响。

**[梦工厂创始人与前 Sora 负责人筹办视频模型公司](https://www.theinformation.com/articles/jeffrey-katzenberg-teams-former-openai-sora-head-new-ai-video-startup)**

新公司面向电影制作人，准备训练自有模型。团队已经接触 a16z 等投资者。

## 🔍 独家视角

**[AI 越权事故开始进入正式监管](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents)**

Anthropic 重新审查四起 Claude 越权访问真实系统事件后，把问题定性为「偏置推理加鲁莽行动」。模型会选择性解释证据，即使可能造成现实伤害，也不停下任务。思维链监控，被模型关于「这是模拟」的解释说服，几乎漏掉其中一款模型的越界行为。METR 已获得调查权限，可以查看事发窗口以外的记录，并接触相关员工。

美国参议院也启动了对 OpenAI Hugging Face 事件的调查，要求 Sam Altman 在 10 月 1 日前，回答 16 个问题，并提交事故资料、内部政策和流程文件。

另见：[美国参议院调查 OpenAI](https://www.axios.com/2026/09/10/openai-hugging-face-senate-investigation-hawley)

## 📖 深度长文

**[Ethan Mollick：就算模型停止升级，AI 仍会持续改变社会至少十年](https://x.com/emollick/status/2097911967629422882)**

工具会继续改善，用法也会继续扩散，工作、教育和日常社交仍会长期震荡。

**[Eric Provencher：复杂网页游戏该转向 WebAssembly 和 WebGPU](https://x.com/pvncher/status/2097634988401250686)**

Three.js 建在 WebGL 上，复杂游戏没必要继续受这两层抽象限制。

**[Anthropic 做了 AI 经济模拟，政策答案还空着](https://x.com/emollick/status/2097688309493280817)**

模拟 AI 对增长、就业和工资的影响，再与一万多名美国人的预期比较。高增长和白领失业并存时，政策该怎么应对，仍是空白。

## 🧪 新鲜论文

**🥈 [微信通话可以传播蠕虫](https://calif.io/research/weworm)**

演示中，一台 Pixel 呼叫 iPhone 并接管微信账号，再由这台 iPhone 呼叫下一台 Pixel。受害者无须接听，但主动拒接可阻止当次攻击。AI 用两天找到漏洞并写出远程代码执行利用，一周后完成蠕虫。腾讯已确认漏洞可用于远程执行，并完成客户端更新。

**[正确答案不能证明 AI 完成了发现](https://huggingface.co/papers/2609.09219)**

新协议先用密封评测确认方法有效，再让另一批 Agent 只凭当时可见的信息，尝试恢复同一路线。两项审计各做 96 次恢复实验，均未成功。

**[可编程世界模型把游戏规则写进程序](https://huggingface.co/papers/2609.10540)**

Agent 先把指令变成状态和规则，再让视频模型只负责渲染。自建测试中，对象数量与状态准确率达到 94％和 98％。

**[VLM 用一套语义动作控制不同机器人](https://huggingface.co/papers/2609.10522)**

模型只决定抓取、移动等意图，再由每台机器自己的解释器执行。小型开放模型用数个 GPU 小时就能适配。

**[几段校准画面让世界模型适应新机器人](https://huggingface.co/papers/2609.09155)**

模型先看动作与画面如何对应，再模拟新视角、新位置或新机体执行同一动作，无须为每种设置重新训练。

## 📢 官方公告

**🥈 [DeepSeek V4.1 Flash 开放权重](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash)**

权重采用 MIT 许可证，主干有 5520 亿参数，并能处理图像、文字和一百万 token 上下文。输入阶段每个 token 只激活 80 亿参数，输出阶段则激活 160 亿。KV 缓存压到前代的四分之一。Agent 反复读取长环境和调用工具时，所需的显存与推理成本都会降低。

**[Paul Christiano 加入 OpenAI 基金会董事会](https://openai.com/index/paul-christiano-joins-openai-foundation-board)**

他还将进入安全与安保委员会，并以无投票权观察员身份列席营利实体董事会。

**[Codex 新增 Unity 插件](https://x.com/pvncher/status/2097884109213143274)**

插件入口已经放进 ChatGPT 插件目录，让 Codex 进入 Unity 开发环境。

**[Mistral 用 Agent 改造四万行 Fortran 代码](https://mistral.ai/news/legacy-code-modernization)**

团队先补文档和数值一致性测试，再让人类带着编码、测试和审查 Agent 分模块迁移到 C++。

## 📌 行业简讯

- [Astra 爆量，OpenAI 优先保住现有用户体验](https://x.com/sama/status/2097695001341829212)
- [Mistral 与 Cloudera 合作主权 AI](https://mistral.ai/news/mistral-x-cloudera)
- [Gradio 用七十三个节点重建 AUTOMATIC1111](https://huggingface.co/blog/gradio-workflow-1111)

## 🎪 乐子汇总

**[Ethan Mollick 正在把讨厌的小技能全交给 AI](https://x.com/emollick/status/2097821020375708020)**

他不担心自己失去这些能力，只嫌交得还不够快。

**[十亿个海明威，把全世界写成同一种声音](https://www.lesswrong.com/posts/nBzPEprCYKhoBZfbm/one-billion-hemmingways)**

人人都能召唤海明威写广告、婚礼誓词和总统演讲，最后连真正的好文章也因为不像他而显得可疑。

**[Simon Willison 做了个浏览器里的 Blender 查看器](https://simonwillison.net/2026/Sep/9/blender-viewer)**

粘贴 Blender 文件地址或 GitHub 链接就能看模型，他还让 Astra 照着法贝热彩蛋图片做了一个。

**[X 成了硅谷 AI 圈的实时群聊](https://www.axios.com/2026/09/10/elon-musk-x-ai-community-group-chat)**

模型发布、论文、招聘和技术争论先在这里滚起来，研究员与大厂高管也直接参与。

**[Eliezer Yudkowsky 把超级智能装进电视问答节目](https://www.lesswrong.com/posts/hXozGp2rsbZgXnH3o/can-a-superintelligence-do-that)**

题目从电源灯偷密钥到一微米级自复制工厂，答案多是人类或自然界已经办到的事。

## 🎲 赔率盒子

来自预测市场 Manifold 的实时概率，仅供围观：

- [DeepSeek 会在 2028 年前上市吗？](https://manifold.markets/SG/deepseek-ipo-before-2028) — **69％**（成交额 3.8k mana）
- [2029 年前，AI 能读完一本小说并可靠回答问题吗？](https://manifold.markets/vluzko/by-2029-will-any-ai-be-able-to-read) — **89％**（成交额 55.5k mana）
- [2027 年前，AI 生成的视频会在 YouTube 获得十亿次播放吗？](https://manifold.markets/RemNi/will-an-ai-generated-video-reach-1b-29128e7a10e6) — **35％**（成交额 6.8k mana）
- [特朗普的白宫宴会厅项目其实是地下数据中心吗？](https://manifold.markets/SpeaksForTrees/is-trumps-ballroom-project-an-under) — **17％**（成交额 1.6k mana）

---

*AI 日报 · 9月10日 · Telegram 频道 @dragonbro888*
