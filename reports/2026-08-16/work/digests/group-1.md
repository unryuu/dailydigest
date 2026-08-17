# 首轮工具目录锚定 DeepSeek Harness 的任务轨迹

- 推荐强度: 中
- 档位线索: 用户点名且社区热度高，具体机制和实验数字够银；必须把“特定题目、特定模型、Windows 环境”的限定放在前两句，不能写成普遍提分方法。
- 涉及文章: [dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) · GitHub 社区项目 · 2026-08-14 创建

## 核心主张
DeepSeek V4 Pro 的首轮推理轨迹会受到 API 可见工具目录和自动注入上下文的影响。这个 preset 第一轮只暴露 Minimal 的 `bash` 与 `str_replace_editor`，并暂时去掉 AGENTS.md／CLAUDE.md 摘要和技能目录提醒；首次工具调用或助手回复持久化后，再恢复发现工具和按需解锁的 Standard 工具。

作者把它描述为“先选择首轮轨迹，再恢复完整能力”，不是一种新的模型训练方法。README 明确说结果只证明同一题目、同一配置可复现，不能推成所有模型和任务都能提分。

## 为什么值得看（钩子）
它把 Agent 的能力差异追到一个很具体的接口变量：模型第一眼看见哪些工具，可能会改变整段任务的执行方式。仓库创建约一天半已获 2470 星和 76 个 fork，用户明确要求收录。

## 关键细节 / 引述
- 在默认 256000 maxTokens 下，真实 Minimal 工具 schema 的 5 次测试全部进入作者定义的锚定轨迹；`pwsh/read`、仅 `pwsh`、沙箱 `bash/read` 等 Standard 系组合共 11 次全部进入 standard-like 轨迹。
- 首轮输出封顶 1024 token 也能产生锚定，结果为 26／32；但基础模式默认不依赖该开关。
- 技能目录提醒存在时，锚定 0／9；所以 bootstrap 阶段会暂时剥离 `agent-instructions` 与 `skill-catalog`，第二轮起恢复。
- Project2、DeepSeek V4 Pro、`reasoningEffort=max`、Windows 原生环境中，两次 Ability 得分为 98 和 99；对照说明称 Standard 与 PTC 为 91、92，官方 Minimal 为 99、96。
- 两次高分测试早于“晋升后只保留 resident 工具集”的改动，当时第二轮直接出现 25 个 Standard 工具；当前实现并未在同样条件下重新给出完整高分复测。
- 兼容性只验证到 DeepSeek Harness 0.1.0-rc.5、指定提交和 Node.js 24；README 提醒 Harness 仍是开发者预览版，未来可能出现破坏性变化。

## 与近期的关系
08-13 已报 DeepSeek V4 Pro 与官方 Harness，这是同一大主线的新社区实验。它不是稳定版发布、常规教程或单纯 star 数，而是提供了首轮工具 schema、上下文注入和轨迹变化的具体机制；因用户点名保留，但档位不宜超过银。
