# RUNBOOK — 每天一期，按步走

前提：已读 `CLAUDE.md`（铁律）和 `STATUS.md`（盘面/防重复/待办）。
按下表走，**做到哪步再读哪步的细则**，不提前读、不回头背。

| 步 | 干什么 | 细则 |
|---|---|---|
| 1 | 定日期，派 scout 扫 29 源，URL 查重 | `steps/1-扫源.md` |
| 2 | 读近 3 期成品防重复，候选定牌，分成七个分区 | `steps/2-定牌.md` |
| 3 | 派 reader 精读金银 + 核查 agent 出无牌初稿 | `steps/3-精读.md` |
| 4 | 填工单，派写手写 daily.json | `steps/4-写手.md` |
| 5 | 主 agent 补赔率盒子 | `steps/5-赔率.md` |
| 6 | 自查、渲染长图、发私聊预览 | `steps/6-预览.md` |
| 7 | 用户点头 → 发频道 → 口播稿 + 知乎/小红书 | `steps/7-发布分发.md` |
| 8 | 用户交来录音 → 视频线到成片 | `steps/8-视频.md` |
| 9 | seen 回写、用户修改整理、report、STATUS、commit | `steps/9-收尾.md` |

角色说明书在 `roles/`（scout / reader / 核查 / 写手 / 口播 / 视频卡）。派 subagent 时让它读自己那份说明书，你不用在提示词里写太多东西。
**凡写用户可见文案，动笔前读 `roles/定调.md`**：title / label / body / odds 文案，包括你自己填工单 title 和 odds 。

## 产物地图（reports/<date>/）
- 顶层只放用户会碰的：`daily.json`（唯一数据源）、`daily.full.png`、`口播稿.md`、`report.md`、`用户修改.md`
- `work/`：manifest.json、digests/、今日工单.md、daily.preedit.json、渲染中间 html
- `dist/`：daily.zhihu.md、小红书/
- `video/`：录音、字幕 srt、视频卡、成片

脚本全在 `scripts/`，每个开头有用法注释。信源配置在 `sources/<slug>/`（meta.json + seen.json），人类总览 `sources.md`——**修改信源必须两处同步改**。
