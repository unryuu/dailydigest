# 用 OpenRouter 跑实验先锁 provider，否则基准分能差 16 个点

- 日期：2026-07-24
- 来源：https://www.lesswrong.com/posts/KsyoSAyBRXtwzSugg/not-pinning-your-openrouter-provider-might-invalidate-your
- 主题：四、评测与实验设计

## 这是什么

LW 提醒：用 OpenRouter 跑实验先锁 provider。各家 provider 量化精度不一，如果请求随机派单，基准分能差出 16 个百分点。已有 NeurIPS 论文中招，作者建议把用了哪家也写进论文。

一句话：各 provider 量化精度不一，随机派单能让基准分差 16 个百分点，已有 NeurIPS 论文中招——跑评测必知的坑。

## 细节（来自精读摘要）

无。

## 可以怎么用

- 通过 OpenRouter 或类似聚合服务跑任何评测/基准测试时，必须显式锁定 provider（而非让系统随机派单），否则同一个「模型名字」背后的量化精度可能不同，跑出来的分数没有可比性。
- 写实验报告或对外分享测试结果时，应该像论文建议的那样，把具体用了哪家 provider 也记录下来，方便自己和他人复现、排查分数差异的真正原因。
- 这个坑提醒了一个更普遍的原则：凡是「同一个名字背后可能有多个实现」的服务（不限于模型 API），跑对照实验前都要先确认锁定的是同一套底层实现，否则对比结果可能只是在比较「谁抽到了哪个后端」。
