# 支持内容溯源的相机也可能为假照片签名

- 推荐强度：强
- 档位线索：够银。作者在当前最高保障等级的 Pixel Camera 实现上做出可验证伪造，攻击链、设备和组件都写得具体；但标题和正文必须把结论限定在 Android 上依赖 Key Attestation 或 Google Play Integrity 的 C2PA 相机实现，不能写成整个 C2PA 标准已经失效。
- 涉及文章：[C2PA Cameras Do Not Survive Contact With Reality](https://www.da.vidbuchanan.co.uk/blog/android-c2pa.html) · David Buchanan 个人博客 · 2026 年 8 月 25 日

## 核心主张

Android 上的 C2PA 相机应用依靠 Key Attestation 或 Google Play Integrity，证明应用和设备没有被篡改，再调用硬件保护的密钥给拍摄内容签名。作者证明，如果攻击者先通过软件漏洞或硬件故障注入取得一台签名设备的 root 权限，证明机制仍可能把这台设备当成可信设备；攻击者不必导出 StrongBox 内的私钥，只需冒充相机应用，请它为任意图片或视频签名。

这意味着文章攻击的是“签名设备可信”这一环，而不是破解密码学本身。攻击者需要控制并 root 一台可签名的 Android 设备，不是隔空控制任意用户的相机；证据覆盖 Pixel Camera，以及作者调查过的其他依赖 Android Key Attestation 或 Google Play Integrity 的 C2PA 相机应用，不能据此断言所有平台、所有实现或 C2PA 整体都已失效。

## 为什么值得看（钩子）

最反直觉之处是：密钥即使一直安全地留在硬件里，假照片仍可得到一枚“真签名”。而作者选的不是边缘产品，而是当前 C2PA Conformance Program 最高 Assurance Level 2 的 Pixel Camera，实现越被视为可信，反差越强。

## 关键细节 / 引述

- 正常解锁 bootloader 并刷入修改固件会触发设备重置，也会让证明报告暴露 bootloader 已解锁，Google 因而拒绝下发 C2PA 密钥；但用权限提升漏洞取得 root 后，bootloader 仍锁定、AVB 厂商密钥未改，设备也仍显示原先启动时的安全补丁级别，证明机制没有可靠办法发现已经失守。
- 新款 Pixel 的 C2PA 密钥保存在 Titan M2 内的 StrongBox 中。root 权限仍不能直接取出密钥，但攻击者不需要原始密钥材料，只需调用硬件密钥完成签名。作者制作的 keystork 让 rooted 设备上的服务冒充已安装应用操作 KeyStore API，并给出了针对 Pixel Camera 的“签任意图片”概念验证脚本。
- 作者称，写作时 CVE-2026-43499 已让完全打满补丁的 Google Pixel 存在公开的一键 root 路径；他推荐用 Root My Pixel 复现，并称自己测试过 Pixel 8a 和 Pixel 9a。因此当前攻击不一定需要拆机或硬件设备。
- 软件漏洞最终可以修补，但作者还用低成本硬件故障注入取得 root，并认为现有设备中的这类硬件缺陷大多无法靠补丁消除。不过边界并非“任何 Android 永远无解”：三星启用 RKP 后挡住了他当前基于 PTE 位翻转的具体攻击方法，作者设想的绕过策略尚未实现。
- 作者认为，若要从架构上阻断此类攻击，整个图像处理流程连同 AI 处理都要进入具有强内存保护的安全隔区；Google 将其报告关闭为“Won't fix（infeasible）”，但仍支付了 7500 美元奖金。作者同时承认，即使重做架构，也阻止不了对着屏幕拍照一类光学攻击。
- Pixel Camera 获得 Assurance Level 2，是 C2PA Conformance Program 当前定义的最高等级；移动应用目前只有 Android 能达到该等级。作者称自己是在攻击“最强”的实现。
- 影响范围不只 Pixel Camera：作者调查的其他 Android C2PA 相机应用也都依赖 Key Attestation 或 Play Integrity，因此具有相同结构性问题；这些应用不限于 Pixel，攻击者还可选择整个 Android 生态里最便宜、最脆弱的兼容设备。但原文没有测试所有 Android 应用，更没有验证非 Android 平台。

## 与近期的关系

与 8 月 25 日“恶意模型可能借推理引擎控制服务器”都属于可信计算边界被绕过，但不是同一事件，也不是旧事重炒。昨天讲模型输出可能利用 vLLM 一类宿主软件漏洞，今天讲攻击者取得 Android root 后滥用相机的硬件签名能力；对象、攻击链和结论均不同，只有宽泛的安全主题相邻，重复风险低。
