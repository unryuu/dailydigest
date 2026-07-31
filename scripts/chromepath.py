# -*- coding: utf-8 -*-
"""定位无头 Chrome 可执行文件，跨 Windows / macOS / Linux。

render_daily.py 和 export_xhs.py 都要调无头 Chrome 截图。原先两边各写死一条
Windows 路径，换机器就得改代码（2026-07-31 准备迁 macOS 时抽出来）。

查找顺序：
1. 环境变量 `DAILYDIGEST_CHROME`（想用 Chromium / Edge 或非标准安装位置就设它）
2. 当前平台的常见安装路径
3. PATH 里的常见命令名

用法：
    from chromepath import find_chrome
    CHROME = find_chrome()

找不到就抛 SystemExit，消息里列出找过的地方，别让调用方拿到一个跑不通的路径。
"""
import os
import shutil
import sys
import pathlib

_CANDIDATES = {
    "win32": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ],
    "darwin": [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        os.path.expanduser("~/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    ],
}
_DEFAULT = [
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
]
_ON_PATH = ["google-chrome", "google-chrome-stable", "chromium",
            "chromium-browser", "chrome", "msedge"]


def find_chrome():
    tried = []

    env = os.environ.get("DAILYDIGEST_CHROME")
    if env:
        if pathlib.Path(env).exists():
            return env
        tried.append(f"{env}（来自环境变量 DAILYDIGEST_CHROME，但该路径不存在）")

    for p in _CANDIDATES.get(sys.platform, _DEFAULT):
        if p and pathlib.Path(p).exists():
            return p
        tried.append(p)

    for name in _ON_PATH:
        hit = shutil.which(name)
        if hit:
            return hit
    tried.append("PATH 里的 " + " / ".join(_ON_PATH))

    raise SystemExit(
        "找不到 Chrome，渲染没法跑。找过这些地方：\n  "
        + "\n  ".join(t for t in tried if t)
        + "\n\n装一个 Chrome，或者用环境变量指定："
          "\n  Windows:  $env:DAILYDIGEST_CHROME = 'C:\\path\\to\\chrome.exe'"
          "\n  macOS:    export DAILYDIGEST_CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'"
    )


if __name__ == "__main__":
    print(find_chrome())
