# claude.com/blog 密集发文:harness 设计方法论最有货,但"一天连发"前提有变

- 推荐强度: 中(harness 单篇内容够"强",但时效性有硬伤,见下)
- 档位线索: **先报一个事实问题:5 篇里只有 2 篇是 7/22 发的**(verification loops、Outtake),其余 3 篇是四月旧文(harness 4/2、security 4/10、desktop redesign 4/14),索引页日期已核实。"一天连发多篇"的叙事撑不住,疑 scout 把博客索引当成了当日更新。定牌建议分两条路:① 若按"新消息"口径,只剩 2 篇真新文,verification loops 是中等偏高的方法论、Outtake 是中等偏上的客户案例,合起来勉强够银、也可降无牌;② 若破例收旧文,harness 那篇是真金——干货密度全组最高,方法论+大量 benchmark 数据+反直觉观点,单篇够银甚至更高,但需向读者明示是 4 月旧文(往期 report 未报过,无重复,grep 已核实)。desktop redesign 是纯产品宣传,建议直接剔除。只给线索,不拍板。
- 涉及文章:
  - [Agent Harness Design: 3 Patterns](https://claude.com/blog/harnessing-claudes-intelligence) · claude.com/blog · **2026-04-02(旧文)**
  - [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) · claude.com/blog · 2026-07-22
  - [How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) · claude.com/blog · 2026-07-22
  - [Claude Code desktop redesign](https://claude.com/blog/claude-code-desktop-redesign) · claude.com/blog · **2026-04-14(旧文,纯宣传,建议剔)**
  - [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) · claude.com/blog · **2026-04-10(旧文)**

## 核心主张

重点读的 harness 一篇(作者 Lance Martin,Claude 平台团队):agent harness 里的每条假设都会随模型升级过时,好 harness 的建法不是"该加什么"而是反复问"**我能停止做什么**"。三个模式:① 靠模型不靠脚手架——bash+文本编辑两个通用工具就够,Claude 3.5 Sonnet 当年就靠这俩打出 SWE-bench Verified 49%;② 精简 harness——让 Claude 用代码执行自己过滤工具输出、自己管上下文(skills 按需加载、compaction、memory 文件夹),而不是框架代劳;③ 谨慎设边界——缓存优化(缓存 token 只有基础价 10%)和声明式工具只留给安全/UX/可观测性场景。其余四篇:verification loops 讲怎么把"你每次手动做的小修正"写成 skill 让 Claude 自动闭环验证;Outtake 是安全公司客户案例;security 是给防守方的威胁情报框架;desktop redesign 是产品功能清单。

## 为什么值得看(钩子)

反直觉在于方向:全行业都在给 agent 堆脚手架,Anthropic 自己人说最优路径是做减法——他们举了个"死代码"例子:早期为 Sonnet 4.5 的"上下文焦虑"(临近窗口上限就草草收尾)加的重置逻辑,到 Opus 4.5 该行为消失后反而变成瓶颈模型性能的死代码。harness 不是一次建成的资产,是需要随模型版本定期"除草"的负债。

## 关键细节 / 引述

- **数字最硬的一组**(harness 篇):Opus 4.6 在 BrowseComp 上,仅靠让 Claude 用代码执行自己过滤工具输出,45.3%→61.6%;compaction 能力代际差:同样压缩预算下 Sonnet 4.5 停在 43%,Opus 4.5 到 68%,Opus 4.6 到 84%;memory 文件夹让 Sonnet 4.5 在 BrowseComp-Plus 60.4%→67.2%。
- **记忆管理的代际对比很生动**(harness 篇):长跑宝可梦游戏,Sonnet 3.5 跑 14,000 步还困在第二个城镇,攒了 31 个文件(含重复的毛毛虫记录),把 memory 当聊天记录用;Opus 4.6 同样步数拿 3 个徽章,只有 10 个按目录组织的文件,还有一个从失败中提炼战术的学习文件。
- 引 Chris Olah:生成式 AI 系统是"培养(grown)"而非"建造(built)"出来的——这是"harness 假设会过时"的理论根。
- verification loops 篇的可用点:最小 skill 就是一个 markdown 文件(如"检查错误日志必须含 request ID、不得含请求体"这类通用 linter 管不了的项目私有规则);Anthropic 内部链式流程 code-review → simplify → verify → design-check;提醒链式验证费 token,先小规模试。
- Outtake 篇(CEO Alex Dhillon,前 Palantir):Recon Agent 长程调查代理,中位单次运行 16 分钟、最长 2 小时,2025 年扫描 2000 万+潜在攻击;路径是 Claude Code 原型验证→迁 Agent SDK 拿记忆/上下文控制;引语"如果戴上坏人的帽子,现在其实是发动攻击的好时代"。
- security 旧文的核心判断:假设 24 个月内前沿级攻击能力泛化,模型最擅长"反向补丁"(从公开修复反推 exploit),补丁到利用的窗口在收窄;给了七条防御建议,反直觉点是"靠麻烦拦人"的摩擦型防御对能无限磨洋工的 AI 对手失效,硬件绑定凭证、短时效 token 这类静态控制更重要。

## 与近期的关系

- 五篇 URL 均未在往期 report/daily 出现过,无重复(grep reports/ 已核实)。
- **顺手核查的两篇漏扫**:① Datadog《universal machine tool》(7/21)——**昨天 manifest 已标"客户案例软文,一眼货"未收,但精读后建议翻案**:有真架构干货(Temper 规范工具、行为/数据/授权三层契约、符号推理+穷举状态+故障注入+属性测试四层验证、"被验证的工件即运行的工件";Claude Code 占 Datadog 至少 2/3 的 AI 编码工作),主题(验证是瓶颈、不是生成)还正好和今天 verification loops 一篇同频,可打包。② Rakuten 隔夜建 agent(7/20)——约七成软文,亮点只有"工作单位从任务变成决策"和跨部门一周铺开,弱推荐,可不收。
- verification loops(skills 自动化验证)与近期日报多次报道的 skills 生态是同一条线的延续,新角度是"把人肉复查写成可复用验证环",不算旧事重炒。
