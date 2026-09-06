# 2026-09-05 日报报告

## 状态

本期从 2026-09-04T22:52:28+08:00 接续扫描。私聊预览消息为 382、383；用户修改 `daily.json` 后重发预览为 384、385，随后明确说「发频道吧」，最终频道链接消息为 246、长图消息为 247。本次授权只适用于 09-05。

最终 `daily.json` 共 16 条内容、1 条赔率：1 金、4 银；行业大事 5 条、深度长文 2 条、新鲜论文 4 条、乐子 5 条。发布前 `check_daily.py` 为 0 error、1 warning，warning 是赔率数量为 1；这是用户主动删除两条赔率后的最终版本。全历史 URL 查重通过。

最终 `daily.json` 为 6275 字节，SHA-256 为 `87eb01bb3bcd042c59ec41dd8339eb8292159b8cded6deb5bbab0581bf7868f5`。预编辑快照为 6733 字节，SHA-256 为 `0447e800f8864ffb74844e0663d369050248c27d7e513c44d7b1f9692ff465f1`。最终长图为 1179×9931、2127306 字节，SHA-256 为 `4307d92a453d35e8cb77cb8936beec3cd4994dc4414a17a9aac96afd913c1dfc`。

## 定牌与精读

- 行业大事：Coatue 和 MatX 用合资锁定芯片产能（银）、Anthropic 考虑自建支付和计费系统（银）；IBM Bob 代理式开发伙伴、Spotify 用 Portal 降 Claude Code token 用量 90％、VLM Run 统一 API 托管开放权重视觉模型（无牌）。
- 深度长文：CHIVE 训练模型预测并解释自己的行为、Artificial Analysis 发布 Intelligence Index 4.2（无牌）。
- 新鲜论文：Claude 用十一天把费马大定理写进 Lean（金）；DRACO 把长任务总分拆给每一步、LLaDA-Image 开放完整图像训练配方（银）；VeriPhy 给视频物理判断留下证据链（无牌）。
- 乐子：《源氏物语》贵族恋爱灾难喜剧、吊床解释滑轮省力、OpenTrailPaper 开源电子墨水骑行电脑、statichost.eu 欧洲静态站托管、penlu 公布 RSA-260 的一个 130 位因子。

金牌费马大定理只写端到端计算机检查的形式化证明，以及 1300 万行 Lean、约 60 亿输出 token 和 Prove2Me 脚手架防止 Agent 丢失项目状态，不把「验证已有证明」写成发现新数学。The Information 两条均为登录态真实精读并注明来源，不按标题猜正文。

四篇丢弃的 Agent 论文（Environment Evolution for Terminal Agents、Terminal-Universe、Rethinking On-Policy Distillation II、PACE）与过密的架构/世界模型论文，均按用户确认的主版定牌删除，不机械凑密度。

## 赔率

写入前已通过全历史 URL 查重。scout 分桶候选 5 个市场，写手保留 3 条，用户终审删除「AI 会在 2031 年前毁灭人类吗？」和「AI 会在 2150 年前毁灭人类吗？」两条，最终只保留「AI 会在 2026 年 9 月解决千禧年大奖难题吗？——16％」，与当天金牌「Claude 十一天把费马大定理写进 Lean」形成呼应。

## 图文分发与口播

知乎稿为 5132 字节；小红书共 6 张 PNG（各 1242 宽，高 1656~2014），另保留对应 HTML。公众号直接使用 daily.full.png。敏感词检查扫描 `daily.json`、口播稿、知乎稿，共检查 21 个词，0 命中。多平台标题候选：

1. `Claude 十一天把费马大定理写进 Lean，Coatue 和 MatX 用合资锁定芯片产能 | 9月5日AI日报`
2. `Anthropic 考虑自建支付计费系统，Spotify 把 Claude Code token 用量降了 90％ | 9月5日AI日报`
3. `AI 会在九月解决千禧年大奖难题吗，16％的盘口在赌 | 9月5日AI日报`

口播稿和字幕稿按步骤 7 生成，均为 15 个非空段落，事实顺序逐段对应；口播稿 5335 字节，字幕稿 5237 字节，约 1816 字口播，预计 6 分钟。视频线停在用户修改口播稿之前；本期不等待录音，不启动 TTS。

## 扫源、seen 与当期事故

机械扫描 33 个源，留下 134 条候选。七个 Nitter 入口仍全部 403（requests 与浏览器兜底均无果）；The Information 两条候选由主 agent 以登录态浏览器手工扫 Latest 并精读产生，落独立 JSON（仅存事实转述、判断依据和必要限定，不存付费正文）。

`update_seen.py` 回写：新插 13 条；未匹配 3 条（The Information 两条 —— Coatue/MatX、Anthropic 自建支付 —— 以及 `x.com/penlume` 一条）。三者均无固定 `sources/` 目录，按项目规则不新建临时机械源，由全历史 URL 查重兜底，本期通过、无重复。

本期没有频道发布事故。`export_xhs.py` 一次跑通生成 6 张 PNG；`render_daily.py` 重渲两次响应一致（1179×9931），无异常。
