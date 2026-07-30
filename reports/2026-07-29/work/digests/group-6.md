# Raschka：Kimi K3 架构笔记

- 推荐强度: 中
- 档位线索: 建议留。昨天金牌落点是许可证营收门槛，这篇给出的是纯架构增量，且确有超出 config 翻译的点（NoPE、注意力残差），适合作独家视角或银——不建议再冲金，因为主体（K3 发布）昨天已报。若当天盘面挤，可降简讯，核心一句话是「K3 是首个全线弃用 RoPE 的前沿级模型」。
- 涉及文章: [Kimi K3 Architecture Notes](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html) · Sebastian Raschka 个人博客 · 2026-07（HN 430 分：https://news.ycombinator.com/item?id=49085698）

## 核心主张
Raschka 把 K3 定位为 Kimi Linear 的量产放大版（48B → 2.8T），并列出六个架构观察点。最硬的判断有两个：一是 K3 彻底移除了所有 RoPE 层，全线改用 NoPE（无位置编码），据他所知这是首个这么做的前沿级架构；二是整条效率替代链清晰可见——常规注意力换成 MLA + Kimi Delta Attention，MoE 换成 LatentMoE（压缩大线性层，与 Nemotron 3 Ultra 同款），行业整体在向推理效率收敛。他的总评是「A really great release overall」。

## 为什么值得看（钩子）
昨天报的是「K3 放权重、许可证设营收门槛」，这篇回答的是「打开壳子之后里面到底有什么新东西」——而且答案不是复读 DeepSeek，NoPE 全线上马是真正的第一次。

## 关键细节 / 引述
- NoPE：原句「Kimi K3 got rid of all RoPE layers and uses NoPE (No Positional Embeddings) everywhere instead」。位置信息靠什么补？HN 评论区（cma 引论文）：位置由 KDA 的递归门控与衰减机制隐式编码，加上因果掩码；thunderbird120 补充 KDA 名为注意力、实为可并行化的 RNN，RNN 特性天然携带序列位置。
- 注意力残差（attention residuals）：跨层连接、按注意力分数加权。原句「it improves the validation loss and downstream performance (a bit) consistently and adds about 4% in training cost and 2% in inference cost」——训练成本 +4%、推理 +2%，换稳定的小幅提升。
- LatentMoE：思路是「compress (down-project) large linear layers similar to multi-head latent attention」，Raschka 明说「essentially the same LatentMoE as in Nemotron 3 Ultra」——MLA 的降维思想从注意力蔓延到了 MoE 层。
- 规模：从 Kimi Linear 的 48B 放大到 2.8T（原句「scaled up from 48B -> 2.8T」），K3 是当前最大开放权重模型。另有原生多模态一条观察点，文中无展开细节。
- 文章是短笔记体：KDA 与全注意力的层间混合比例、专家数、层数等 config 级数字文中没有给（已核实两遍，非漏抓）；作者结尾说训练侧细节在技术报告里，「that's it from the architecture front so far」。
- HN 侧写：讨论约四成谈架构，四成滑向蒸馏指控与中美论战（constantlm：西方实验室称 K3 只是蒸馏，但论文显示新颖方法；nostromo 反呛 Anthropic 也在无许可蒸馏版权材料）。实用一条：kroaton 称 C++ 项目上 K3 优于 Opus 4.8 但倾向过度思考；有人指出在 Cursor 上 K3 比 Opus 5 还贵。

## 与近期的关系
直接承接昨天的 K3 金牌（权重放出 + 许可证落点）。事实层面无重复——昨天报的是发布与许可证，这篇全部是架构增量；但主体同为 K3，连报两天需要在写法上明确「昨天讲了发生了什么，今天讲里面是什么」。Raschka 是我们订阅源 ahead-of-ai 的作者，此文发在个人博客，属订阅源作者的场外产出。
