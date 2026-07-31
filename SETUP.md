# SETUP — 新机器上把流水线跑起来

换机器（或换回旧机器）时照这份走。日常做日报不用读这里，读 `RUNBOOK.md`。

## 1. 装系统级工具

| 工具 | 干什么 | macOS | Windows |
|---|---|---|---|
| uv | 管 Python 版本和依赖 | `brew install uv` | `winget install astral-sh.uv` |
| ffmpeg | 音频清理、烧字幕、转写 | `brew install ffmpeg-full` | 官方构建，加进 PATH |
| Chrome | 无头截图渲染长图 | 装 Google Chrome 即可 | 同左 |

**ffmpeg 必须带 whisper 滤镜**，`steps/8` 的转写要用。验一下：

```bash
ffmpeg -filters | grep whisper
```

macOS 上标准 `ffmpeg` 没编译进 whisper，得用 `ffmpeg-full`。它是 keg-only，
brew 不会自动链接，**光往 `~/.zprofile` 里加 PATH 不够**——那只对你在 Terminal
里手敲有效，agent 窗口的 shell 不读 `.zprofile`，裸写 `ffmpeg` / `ffprobe`
会 command not found，而 `steps/8` 的命令全是裸写的。必须真正链接进去：

```bash
brew link --force ffmpeg-full
```

（前提是标准 `ffmpeg` 已卸载，否则两者抢同一个名字。）

## 2. 建 Python 环境

```bash
uv venv .venv --python 3.13
uv pip install -r requirements.txt
```

之后所有脚本用 `uv run scripts/xxx.py` 跑，跨平台一致，不用手动激活 venv。

## 3. 放三样不入库的东西

仓库里没有、必须手动补：

| 放哪 | 是什么 | 哪来的 |
|---|---|---|
| `config.local.json` | Telegram token + 两个 chat id | 自己保管，不进仓库 |
| `fonts/MSYH*.TTC` | 微软雅黑，烧字幕用 | Windows 的 `C:\Windows\Fonts\`，商业字体故不入库 |
| `models/ggml-*.bin` | whisper 权重 + VAD | 见下 |

whisper 权重（两个仓库不同，别按命名规律猜）：

```bash
curl -L -o models/ggml-large-v3-turbo-q5_0.bin \
  https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3-turbo-q5_0.bin
curl -L -o models/ggml-silero-v5.1.2.bin \
  https://huggingface.co/ggml-org/whisper-vad/resolve/main/ggml-silero-v5.1.2.bin
```

**字体缺了不会报错**，libass 会静默回退成别的字体，成片字形跟往期不一致。烧字幕
的命令里带了 `fontsdir=../../../fonts`，字体文件放对位置就能加载。

## 4. 验收

```bash
uv run scripts/chromepath.py                    # 应打印 Chrome 路径
uv run python -c "import PIL, bs4, requests; print('deps ok')"
ffmpeg -filters | grep whisper                  # 应有一行
ls models/ fonts/ config.local.json             # 三样都在
```

## 已知问题

**ffmpeg 的 whisper 滤镜在 macOS(M2) 上跑不上 GPU。** 2026-07-31 实测：6.3 秒音频
要 147 秒（CPU 时间 1066 秒，7 核满载），约 23 倍实时；同模型同音频用 `whisper-cli`
只要 13 秒（推理约 4 秒）。日志显示 ffmpeg 侧多加载了一个 BLAS 后端，怀疑矩阵运算
被派给了 CPU，未深究。Windows 上是 2.2 倍实时，正常。

**已改用 `whisper-cli`**（07-31 起，`steps/8` 已改）。转写文字与滤镜一致，但切段
形态差很多，必须带 `-ml 12` 才能对回往期：不加是 60 段 / 平均 39 字，加了是
225 段 / 10.4 字，往期滤镜是 177~274 段 / 11 字左右。段长直接影响 `subs_align`
的段内插值精度。

`ffmpeg -filters | grep whisper` 这条验收仍然留着——滤镜暂时用不上了，但它是
「装的是 ffmpeg-full 而不是标准版」的最快判据。
