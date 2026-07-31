# verifier 不执行代码，像 agent 一样探索 repo 收集证据（Dockerless）

- 日期：2026-07-01
- 来源：https://huggingface.co/papers/2606.28436
- 主题：四、评测与实验设计

## 这是什么

Dockerless 等三篇 HF 新论文：coding agent verifier 开始绕开真实执行环境。今天 HF 论文组里最实的是 Dockerless。训练 coding agent 时，传统 verifier 往往要给每个 repo 起 Docker、跑测试，环境成本高，还经常脆得很；Dockerless 直接换思路，不执行代码，而是让 verifier 像 agent 一样探索 repo、收集证据，判断 patch 对不对。它在 verifier benchmark 上比最强开源 verifier 高 14.3 AUC 点，还能同时做 SFT 轨迹过滤和 RL reward，组成完全免环境的 post-training pipeline。论文自报 SWE-bench Verified / Multilingual / Pro 是 62.0%、50.0%、35.2%，接近环境执行式训练。

## 细节（来自精读摘要）

无。

## 可以怎么用

- 需要验证某个改动/产出是否正确、但执行环境搭建成本高（如需要专门的沙箱、依赖复杂）时，可以借鉴「让验证者像 agent 一样探索证据、而非真的跑一遍」的思路——不追求完全等价的执行结果，而是靠收集足够的间接证据来判断对错。
- 这套「绕开高成本执行环境」的设计巧思可以迁移到其他需要验证正确性但环境搭建麻烦的场景，比如自己审查代码改动/文档修改是否合理时，与其花大精力复现整个环境，不如系统性地探索相关文件、上下文来判断。
- 论文同时把这个 verifier 用在两处（SFT 数据过滤 + RL reward），提示一个通用做法：搭好一套「判断对错」的能力后，可以复用到多个环节，而不必为每个环节单独建一套验证机制。
