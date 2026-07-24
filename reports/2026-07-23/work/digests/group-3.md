# Are AI labs pelicanmaxxing?——用 1008 张 SVG 检验各家是否在给「鹈鹕骑自行车」定向刷题

- 推荐强度: 中偏强
- 档位线索: 方法是金牌级的（1008 样本、48 组合、固定效应回归、多重比较校正，还有 Simon 本人盖章"比我自己严谨得多"），但结论是**阴性**——没抓到任何一家作弊，瓜的浓度低。如果当天有硬新闻，银牌足够；如果想给"社区自发做严肃验证 + 基准创始人回应"这个完整闭环一个位置，且能用 GLM-5.2 的悬念当钩子，够得上金。唯一的"瓜"是 GLM-5.2 效应最大但不显著（p=0.12），只能当调味，不能当主菜。
- 涉及文章:
  - [Are AI labs pelicanmaxxing?](https://dylancastillo.co/posts/pelicanmaxxing.html) · dylancastillo.co (Dylan Castillo) · 2026-07-22 前后 · HN 503 分 / 196 评
  - [Simon 本人回应（链接博文）](https://simonwillison.net/2026/Jul/22/are-ai-labs-pelicanmaxxing/) · simonwillison.net · 2026-07-22

## 核心主张
Simon Willison 的「生成一张鹈鹕骑自行车的 SVG」已经出名到大家怀疑实验室在偷偷针对它优化（benchmaxxing）。Dylan Castillo 花 80 美元 API 额度做了系统检验：8 种动物 × 6 种交通工具 = 48 个提示词，7 个前沿模型各采样 3 次，共 1008 张 SVG，用 GPT-5.6 Luna 当裁判打分、Gemini 3.1 Flash-Lite 做特征提取。结论：**没有证据表明有人在 pelicanmaxxing**——鹈鹕画得并不比其他动物好，自行车画得也不比其他交通工具好，"至少没人在明目张胆地刷"。

## 为什么值得看（钩子）
所有人（包括 Simon 自己）都默认这个梗基准早被实验室盯上了，结果第一个认真拿数据查的人发现：大家居然真的没刷。反直觉点在于"作弊嫌疑"被阴性证据反杀。另一个钩子：全场唯一效应偏大的是 GLM-5.2（上周刚因鹈鹕测试上过我们的日报），pelican×bicycle 组合 +0.35 判分，但 p=0.12 不显著——"最接近嫌疑人但证据不足，当庭释放"。

## 关键细节 / 引述
- 数据量：7 模型（GPT-5.6 Terra、Claude Sonnet 5、Gemini 3.5 Flash、Grok 4.5、Qwen3.7-Max、GLM-5.2、DeepSeek V4 Pro）× 48 提示 × 3 采样 = 1008 张 SVG，temperature 1.0，预算 80 美元。
- 排名打脸：如果真在刷题，鹈鹕该排第一——实际鹈鹕在 8 种动物里排第 6，输给猫、鲸、浣熊、鹭、羚羊；自行车在 6 种交通工具里倒数第二。
- 回归检验：各实验室的"鹈鹕效应"在 -0.11 到 +0.14 判分之间，无一显著；"自行车效应"-0.18 到 +0.27，只有 Gemini p=0.022 但过不了多重比较校正；pelican×bicycle 交互项无一过 p<0.05，GLM-5.2 最接近（+0.35，p=0.12）。
- 记忆化线索也扑空：21 张鹈鹕骑车图 100% 朝右，看似可疑，但基线本来就是自行车 81%、鹈鹕 78% 朝右，另有三个组合朝右率超 90%——不构成背题证据。
- Castillo 结论原话（Simon 转引）："Pelicans aren't drawn any better than other animals. Bicycles aren't drawn any better than other vehicles. And no lab draws the combination better than its pelicans and bicycles already predict."
- Simon 回应：自嘲这是个"deeply unscientific benchmark"，自己以前只做过"random spot-checking"，夸 Castillo 严谨得多；对 GLM-5.2 的效应他的口径是"small and not significant"。**他没有说要换基准或退役基准**。
- 作者自留的口子：单一 LLM 裁判可能不稳；如果实验室是在全面优化 SVG 生成（SVGmaxxing）而非单点刷鹈鹕，本方法测不出来。

## 与近期的关系
鹈鹕基准是本日报的回头客：7-15 雷达收过 Simon 的「鹈鹕桌宠」，7-17 GLM-5.2 发布报道里引过 Simon 的鹈鹕实测（16,658 token / 25 美分）。本篇是新角度——第一次有人反过来审计这个基准本身有没有被污染，且主角之一恰好是 GLM-5.2，可与 7-17 期形成呼应，不算重复。
