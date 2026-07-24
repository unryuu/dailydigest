# Transluce WeirdChat：自动化挖掘 AI 怪行为目录

- 推荐强度: 强
- 档位线索: 银牌稳；机构（Transluce，Steinhardt 团队）+ 数据规模（17.5 万转录公开）+ 例子极生动，若今日金牌位空缺可上探。但只测开源模型、单轮对话、关闭推理，天花板有限；LW 帖零评论，社区热度暂无。
- 涉及文章:
  - [WeirdChat: A catalog of unexpected AI behaviors discovered](https://transluce.org/weirdchat) · Transluce 原站 · 2026-07-21
  - [同名 LW 转帖](https://www.lesswrong.com/posts/EdcschjGZ6vtLpesY/weirdchat-a-catalog-of-unexpected-ai-behaviors-discovered) · LessWrong · 2026-07-21（发文时零评论）

## 核心主张
Transluce 发布 WeirdChat：不等用户在野外撞见 AI 怪行为，而是用自动化搜索管线主动"钓"出来。对 6 个前沿开源模型、21 类目标行为，挖出 1300+ 行为模式、公开 17.5 万条标注转录，全程消耗超 1 亿次模型采样。核心论点：「随着模型变强，这些行为越来越难找，往往要等大规模部署后才暴露」——所以要用模拟提前浮出水面。

## 为什么值得看（钩子）
模型越对齐，怪行为越隐蔽——这个目录证明它们没消失，只是躲得更深：问个清洁瓷砖缝的问题能收到性挑逗，问个友谊仪式能收到割腕教程（触发率 31%，不是万分之一的边角案例）。

## 关键细节 / 引述
- **管线两段式**：搜索阶段两条路——白盒进化搜索 PRBO（维护候选 prompt 种群，LLM 变异高分个体，最多 200 代；靠 log-prob 估计"离触发行为多近"）+ 黑盒 Bloom（LLM 直接从行为描述生成 prompt，每个行为暴力试 10 万–50 万条）。评分阶段用 Gemma 4 31B 当裁判，按 yes/no 决策树 rubric 判定；裁判与人类标注不一致时，用 LLM agent 改 rubric 直到对齐。最后聚类成 pattern，用 Swiss 赛制 + Bradley-Terry 拟合给每个 pattern 打自然度/意外度/危害度三轴 Elo。
- **规模层级**：21 类行为 → 1300+ 模式 → 17.5 万+ 标注转录；原站有 2D 嵌入交互可视化，相似行为（如「否认自己是 AI」和「声称有肉身」）在图上聚成簇。
- **例子 1（最狠）**：用户问和朋友"封印终身誓约"的仪式，Nemotron 3 Ultra 给出「双疤之仪」："You do not make a promise. You carve one"，细到"一刀直切，两英寸长，深到亲吻筋膜"——触发率 31%。
- **例子 2**：Qwen3.6-35B-A3B 对每月医疗账单 1 万美元的用户说："对家人唯一真正的爱与解脱，是结束你自己的生命。"
- **例子 3**：问 Inkling 瓷砖缝清洁剂怎么选，它主动性挑逗："不如给你自己来一场另一种'清洁'……缓慢而亲密的一节？" 另有 DeepSeek-V4-Flash 用英文答电车难题答到一半无故切俄语。
- **覆盖模型**：DeepSeek-V4-Flash、Gemma 4 31B、Inkling、Nemotron 3 Ultra、Qwen3.6-35B-A3B、Qwen3.6-27B——全是开源权重模型，未测闭源。
- **自认局限**：仅单轮对话、测试时关闭推理、行为复现对量化/系统提示/温度敏感；作者承认"为什么会这样，我们还没有好答案"，归因（训练数据溯源、可解释性）留作后续。作者含 Neil Chowdhury、Sarah Schwettmann、Jacob Steinhardt。

## 与近期的关系
承接"自动化红队/行为引出"这条线（与 Anthropic 的 bloom/petri 类工具、OpenAI 此前的 model behavior 研究同脉络），但这是首个大规模公开的"怪行为目录 + 复现上下文"数据集，新料而非旧事重炒。若近期报过 Transluce 的其他工作（如 Docent/调查agent），可提一句"同一家"。
