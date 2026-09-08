# AlphaGenome Atlas 绘制 90 亿种 DNA 变化

- 推荐强度：强
- 档位线索：规模、开放方式和真实研究案例都够银牌；若强调 AI for Science 的公共基础设施价值，可与行业金牌并列竞争。
- 涉及文章：[AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome](https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/) · Google DeepMind · 2026-09-08

## 核心主张
DeepMind 预先计算了人类基因组全部约 90 亿种单字母变化的分子影响，做成一个约 1PB 的免费研究图谱。它还把 AlphaGenome 与 AlphaMissense 的预测压成单一的 AVI 分数，让研究者先给变体排序，再查看是哪类基因调控过程受到影响。

## 为什么值得看（钩子）
过去研究者一次只能问模型某个变体会怎样；现在所有可能的单字母变化已经先算完，可以像查地图一样搜索。

## 关键细节／引述
- Atlas 约 1PB，体量超过 AlphaFold Database 的三十倍；每个变体包含数千个分子效应预测，覆盖数百种人类和小鼠细胞与组织。
- AVI 同时覆盖占基因组 2％的蛋白编码区和其余 98％的非编码区，并给出 RNA 剪接、基因表达、染色质开放等特征归因。
- Broad Institute 合作者用它找到一个此前遗漏、与癫痫性脑病相关的 DNM1 变体；模型判断它制造了错误剪接位点，实验筛选确认了该机制和附近相似变体。
- 在超过 5.4 万名 UK Biobank 参与者的数据上，按预测分组后多找到 22％ 的非编码遗传关联。
- 图谱现在通过网页、API 和 Google Antigravity skill 提供；学术及非商业用途可免费使用，商业版本将进入 Google Cloud。
- 这是研究工具，不用于临床诊断或治疗。

## 与近期的关系
与 09-05 的形式化数学、LLaDA-Image 等论文没有内容重复；属于新的 AI for Science 基础设施主线。
