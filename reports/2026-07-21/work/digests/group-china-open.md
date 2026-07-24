# 中国开源模型压境：Thompson 开药方 + HN 千分情绪爆点

- 推荐强度: 强
- 档位线索: 两篇合起来够金牌候选——Thompson 给出了本报 07-18/07-20 铺垫过的问题的**具体政策答案**（增量明确），werd.io 那篇 HN 1149 分/864 评论是当日头版第一的情绪锚点。若当日另有更硬的技术金牌，也可拆成银牌（Thompson 提案为主、werd.io 作情绪注脚）。
- 涉及文章:
  - [Who's Afraid of Chinese Models?](https://stratechery.com/2026/whos-afraid-of-chinese-models/) · Stratechery（Ben Thompson）· 2026-07-20 · HN 744 分（https://news.ycombinator.com/item?id=48977128）
  - [American AI is locked down and proprietary. It's losing.](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) · werd.io（Ben Werdmuller）· HN 头版第一，1149 分 / 864 评论（https://news.ycombinator.com/item?id=48979269）

## 核心主张
两篇同日打同一个靶：美国「封闭 + 恐慌」的对华 AI 策略在输。Thompson 的判断是恐慌本身过头了——前沿实验室经济上「会没事的」，Kimi 等中国模型并非边际成本更便宜，只是吃了价格保护伞的红利；真正的问题是美国自己的开源模型被绑住了手脚。他开出具体药方：美国应立法（1）明确「收集数据训练模型属于合理使用」，（2）禁止服务条款封杀蒸馏——至少对美国公司无效化这类条款。werd.io 则从生态角度补刀：没有护城河的技术搞封闭授权是「明显的败招」，基础设施层面「开放几乎总是赢」。

## 为什么值得看（钩子）
Thompson 点破的虚伪是硬核的：前沿实验室的模型本身就是「对整个开放互联网知识的蒸馏」——爬来的、没授权的——转头却用 ToS 禁止别人蒸馏自己的输出。「这里到底谁被侵害了？」更拧的一层：美国开源模型厂商守规矩、必须遵守这些 ToS，结果反而比不守规矩直接蒸馏的中国同行更弱——守法者受罚，这才是不对称劣势的真正来源。

## 关键细节 / 引述
- Thompson 提案原文（经 Simon Willison 与 Daring Fireball 两处独立摘引核实）："The U.S. should pass a law that (1) makes explicit that collecting data for training models is fair use, and (2) bars terms of service that forbid distillation, for U.S. companies at a minimum."
- Thompson 论虚伪：前沿模型本是对开放互联网的蒸馏（无授权抓取），却禁止他人蒸馏自己，"who is exactly being wronged here?"；他主张新版权政策应「既豁免实验室、也保证它们学到的东西继续喂养后续创新」。
- Thompson 的旁注（经 Simon Willison 转述）：阿里把 Qwen 3.8 Max 以开放权重发布，可能是被习近平「开源、开放、协作、共享」的表态推动的。
- werd.io 最硬的数据：a16z 合伙人 Martin Casado（经 The Economist）称 **80% 的初创公司在用中国模型**；Werdmuller："Open almost always wins when it comes to infrastructure adoption."
- HN werd.io 帖（1149 分）主流是**附和**，分歧在时间线：用户 lambda 说消费级笔记本已能跑上 12-18 个月前前沿水平的模型，本地化替代是「10-15 个月的事，不是 10-15 年」。有评论转引 OpenAI 战略负责人 Dean Ball 对中国模型的表态："It's a very good model! I don't think its performance can be explained away by distillation or anything like that."（单一 HN 评论来源，用前建议再核）
- HN Stratechery 帖（744 分）情绪更冲：对美国实验室的动机怀疑压过对中国模型的担忧。用户 monooso："中国模型可能因地缘政治坑我，但美国公司明天就会为赚快钱坑我"（大意）；用户 inigyou 称西方话术是「照镜子式指控」（accusation in a mirror）。
- 单一来源、未能二次核实的数字（Stratechery 有付费墙，仅首次抓取给出）：Kimi K3 定价 $3/$15 每百万 token、参数 2.8T；Qwen 3.8 Max 参数 2.4T。正文如引用建议标注或舍弃。

## 与近期的关系
直接承接本报两条线：07-18「OpenRouter 周 token 前五全是中国开源」（现象）、07-20「华府暗斗怎么管中国开源模型、Sacks 反对封杀」（政策僵局）。今天的增量是：Thompson 给出了政策僵局的**具体解法**（合理使用立法 + 禁蒸馏条款无效化），且把矛头从「中国威胁」调转到「美国自缚」；werd.io + 两个 HN 千分/七百分帖则是社区情绪首次以这种量级集中爆发。注意别把 07-18 的 OpenRouter 数据当新料重报；「实验室训练用无授权数据」的虚伪指控与 07-20 雷达的 Altman 2022 内部信有呼应，可一句话点到，不展开。

---
来源手数说明：Thompson 原文有付费墙，提案与虚伪论点经 simonwillison.net（2026-07-20 blogmark，直接引文）与 daringfireball.net（直接引文）双重旁证，属二手直引，可靠；werd.io 与两个 HN 帖为一手抓取。
