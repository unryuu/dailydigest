# 把人肉复查写成 skill 让 Claude 自动跑 + skills 提升 agent 数据分析

- 日期：2026-07-10 / 2026-07-23
- 来源：https://claude.com/blog/building-verification-loops-in-claude-code-with-skills（主文，验证循环）；https://huggingface.co/blog/Ningyu/skills-improve-codex-data-analysis（skills 提升数据分析）
- 主题：一、agent 工程与 harness

## 这是什么

**2026-07-10**：给 Codex 挂上 skills 做数据分析实测，部分任务正确率从 0/4 提到 4/4。

**2026-07-23**：验证是瓶颈，被验证的工件才允许上线，把复查写成 skill。

## 细节（来自精读摘要）

来自 2026-07-23 的精读（claude.com/blog/building-verification-loops-in-claude-code-with-skills）：

最小 skill 就是一个 markdown 文件（如「检查错误日志必须含 request ID、不得含请求体」这类通用 linter 管不了的项目私有规则）。

Anthropic 内部有一套链式流程：code-review → simplify → verify → design-check。

提醒：链式验证费 token，建议先小规模试，别一上来就全链路铺开。

## 可以怎么用

- 把自己重复做的人肉复查动作（比如「检查某类文件是否包含某个必须/禁止字段」）写成一个最小的 markdown 规则文件，让 Claude 按这份规则自动跑一遍，而不是每次靠记忆手动检查。
- 通用 linter/工具管不到的「项目私有规则」（比如本项目的铁律、格式要求）特别适合用这种方式固化成可复用的验证 skill。
- 给数据分析类任务配上明确的 skill/操作指南，能实打实提升正确率（从 0/4 到 4/4 这类量级），值得优先给容易出错的分析步骤配 skill，而不是每次重新摸索。
- 如果打算做多步链式验证（review→simplify→verify→design-check 这种），先在小范围试跑评估 token 开销，再决定要不要铺开到全部流程，避免验证本身变成新的成本黑洞。
