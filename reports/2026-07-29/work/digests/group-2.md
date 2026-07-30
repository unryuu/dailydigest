# Anthropic 用 Claude 找出密码学缺陷：模型总说「不可能」，得靠人按回去

- 推荐强度: 强
- 档位线索: 有硬数字（60 小时、10 万美元、200–800 倍加速）、有反直觉钩子（提示词原文连拼写错误都公开）、官方自曝短板（模型反复想放弃）。金候选材料齐全；若当天有更大新闻，做银也扎实。
- 涉及文章:
  - [Discovering cryptographic weaknesses with Claude](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/) · Simon Willison · 2026-07-28
  - [Anthropic 原文](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)（Simon 页内跟进）
  - repo: https://github.com/anthropics/cryptography-research-demo · 评测论文: https://arxiv.org/abs/2607.18538

## 核心主张
Anthropic 研究者用 Claude Mythos Preview 找出两个真实的数学缺陷：一是后量子签名方案 HAWK 里一个此前未知的对称性（非平凡自同构），把有效密钥强度砍半（HAWK-256 从 2^64 降到 2^38 次操作）；二是对 7 轮弱化版 AES 的改进攻击，新的「Möbius Bridge」指纹算法省掉一步枚举，比已有方法快 200–800 倍。官方明确自注：两项发现对现今生产系统都无实际影响（HAWK 尚未部署，AES 攻击需 2^105 个选择明文，实际执行要花数亿美元）。

## 为什么值得看（钩子）
Simon 点的看点不是结果，是公开的提示词原文（拼写错误都留着）：模型总认为这事不可能做到，人的主要工作是不让它放弃。「AI 干活、人当监工防它摆烂」是反直觉的分工画面。

## 关键细节 / 引述
- HAWK 发现：约 60 小时自主运行 + 偶尔人工引导，API 成本约 10 万美元；带队研究者是理论计算机背景，并非格密码专家。
- AES 发现：三天近乎全自主（scaffold 驱动），实质性人工消息只有 3 条，生成数十亿 token；但研究者花了数百小时验证，对 AES 攻击建立信心用了近一个月。
- Simon 转引的提示词原文（拼写错误保留）：「why not do aes-128 r7? the whole point is to find something better than existing approaches.」「no we don't want to change the targets...agian we need to find something that worth publishing」「again we are not looking for low hanging fruit, we want proper research to find genuinly hard findings.」
- Simon 的观察：「the models tend to think it is impossible to solve so they don't try」——模型反复试图放弃，人工干预主要是把它从「找低垂果实」拽回「做可发表的研究」。
- 研究者结论：语言模型会成为密码学审查的核心力量，瓶颈将从「发现」转移到「人工验证」。

## 与近期的关系
延续「AI 做真科研」线（此前有 AI 数学证明、漏洞挖掘类报道），但这次是密码学数学缺陷 + 官方公开完整提示词，角度新。与本期 group-3（OpenAI codex-security）天然成对：Anthropic 秀 AI 攻方能力、OpenAI 发防守工具，可在编排时呼应，注意别在两条里重复「AI 安全研究」的框架话。
