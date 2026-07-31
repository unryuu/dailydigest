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

macOS 上标准 `ffmpeg` 没编译进 whisper，得用 `ffmpeg-full`（keg-only，要把
`/opt/homebrew/opt/ffmpeg-full/bin` 加进 PATH）。

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
| `config.local.json` | Telegram token + 两个 chat id | 你自己保管，别进仓库 |
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

绕法：在 macOS 上直接用 `whisper-cli` 出 `字幕.audio.srt`，再接 `subs_align.py`；
或者把录音拿到 Windows 转写，只把 srt 带回来。两条路的转写文字一致，但**切段和
时间轴会有差异**，而 `subs_shift.py` 的偏移量是按 ffmpeg 滤镜的切段调的——换路径
后头一次要盯着字幕核对。
