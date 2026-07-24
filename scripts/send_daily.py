"""
新格式日报投递：每天发两条。
  1) 一张长图（sendPhoto）——所有内容，手机竖屏阅读，带极简 caption。
  2) 一条蓝字链接消息（sendMessage）——按七分区分段，每条可点跳原文。

双路闸门同 push.py：--to self（默认，私聊预览）/ --to channel（确认后发频道）。
读 reports/<date>/daily.json + reports/<date>/daily.png。

用法：
    python scripts/send_daily.py <date>                 # 默认 self 预览
    python scripts/send_daily.py <date> --to channel    # 发频道
    python scripts/send_daily.py <date> --dry           # 只打印链接消息、不发
配置：复用 config.local.json（token / chat_self / chat_channel）。
"""
import sys, os, json, time, uuid, pathlib, urllib.request, urllib.parse, urllib.error
from dailyjson import load_daily

ROOT = pathlib.Path(__file__).resolve().parent.parent

def load_config():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_self = os.environ.get("TELEGRAM_CHAT_SELF")
    chat_channel = os.environ.get("TELEGRAM_CHAT_CHANNEL")
    cfg = ROOT / "config.local.json"
    if cfg.exists():
        c = json.loads(cfg.read_text(encoding="utf-8"))
        token = token or c.get("token"); chat_self = chat_self or c.get("chat_self"); chat_channel = chat_channel or c.get("chat_channel")
    if not token:
        raise SystemExit("缺少 Telegram token")
    return token, {"self": chat_self, "channel": chat_channel}

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

SECTIONS = [  # 与 render_daily.py 保持同序
    ("industry",   "🗞️", "行业大事"),
    ("deep",       "📖", "深度长文"),
    ("papers",     "🧪", "新鲜论文"),
    ("regulation", "🏛️", "监管动向"),
    ("official",   "📢", "官方公告"),
    ("fun",        "🎪", "乐子汇总"),
]
TIER_MARK = {"gold": "🥇 ", "silver": "🥈 "}

def compose_links(d):
    """分区蓝字链接消息（2026-07-21 起分类版式）。"""
    L = [f"<b>📰 AI 日报 · {esc(d.get('date_label',''))}</b>", ""]
    def seg(emoji, name, rows):
        if not rows: return
        L.append(f"{emoji} <b>{name}</b>")
        L.extend(rows)
        L.append("")
    for key, emoji, name in SECTIONS:
        rows = []
        for it in d.get(key, []):
            mark = TIER_MARK.get(it.get("tier", ""), "• ")
            ttl = it.get("title") or it.get("label") or ""
            rows.append(f"{mark}<a href=\"{it['url']}\">{esc(ttl)}</a>")
        seg(emoji, name, rows)
    seg("🎲", "赔率盒子", [f"• <a href=\"{o['url']}\">{esc(o['question'])} — {esc(o['prob'])}</a>" for o in d.get("odds", [])])
    return "\n".join(L).strip()

def _post(url, fields, files=None, retries=4, backoff=1.5):
    last = None
    for attempt in range(1, retries + 1):
        try:
            if files:
                boundary = "----wf" + uuid.uuid4().hex
                body = b""
                for k, v in fields.items():
                    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n").encode("utf-8")
                for k, (fn, content) in files.items():
                    body += (f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"; filename=\"{fn}\"\r\n"
                             f"Content-Type: image/png\r\n\r\n").encode("utf-8") + content + b"\r\n"
                body += f"--{boundary}--\r\n".encode("utf-8")
                req = urllib.request.Request(url, data=body, headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
            else:
                req = urllib.request.Request(url, data=urllib.parse.urlencode(fields).encode("utf-8"))
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.URLError as e:
            last = e
            if attempt < retries:
                w = backoff * attempt; print(f"  发送失败（{attempt}/{retries}：{e}），{w:.0f}s 后重试…"); time.sleep(w)
    raise SystemExit(f"发送重试 {retries} 次仍失败：{last}")

def send_document(token, chat, png_path, caption):
    """长图一律发文档（附件）：Telegram 不压缩，文字保持清晰。"""
    content = pathlib.Path(png_path).read_bytes()
    r = _post(f"https://api.telegram.org/bot{token}/sendDocument",
              {"chat_id": chat, "caption": caption, "parse_mode": "HTML"},
              files={"document": (pathlib.Path(png_path).name, content)})
    return "document", r

def send_message(token, chat, text):
    r = _post(f"https://api.telegram.org/bot{token}/sendMessage",
              {"chat_id": chat, "text": text, "parse_mode": "HTML", "disable_web_page_preview": "true"})
    return r

def main():
    argv = sys.argv[1:]
    dry = "--dry" in argv; argv = [a for a in argv if a != "--dry"]
    target = "self"
    if "--to" in argv:
        i = argv.index("--to"); target = argv[i+1]; del argv[i:i+2]
    if not argv:
        raise SystemExit("用法：python scripts/send_daily.py <date> [--to channel] [--dry]")
    date = argv[0]
    ddir = ROOT / "reports" / date
    d = load_daily(ddir / "daily.json")
    png = ddir / "daily.full.png"
    links = compose_links(d)
    caption = f"📰 AI 日报 · {esc(d.get('date_label',''))}"

    counts = "　".join(f"{name} {len(d.get(key, []))}" for key, _, name in SECTIONS if d.get(key))
    print(f"日期 {date} → {target}　图 {'有' if png.exists() else '缺!'}　{counts}　赔率 {len(d.get('odds',[]))}")
    if dry:
        print("\n=== 链接消息（先发）===\n" + links + "\n\n[dry-run] 长图未发（附件）：", png)
        return
    if not png.exists():
        raise SystemExit(f"缺图 {png}，先跑 render_daily.py")

    token, targets = load_config()
    chat = targets.get(target)
    if not chat:
        raise SystemExit(f"目标 '{target}' 未配置 chat_id")

    # 顺序：先发文字链接，再发长图（附件）
    r0 = send_message(token, chat, links)
    print(f"链接(先) -> ok={r0.get('ok')} id={r0.get('result',{}).get('message_id')}")
    if not r0.get("ok"): print("  失败：", str(r0)[:300])
    time.sleep(0.6)
    kind, r1 = send_document(token, chat, png, caption)
    print(f"长图({kind}) -> ok={r1.get('ok')} id={r1.get('result',{}).get('message_id')}")
    if not r1.get("ok"): print("  失败：", str(r1)[:300])

if __name__ == "__main__":
    main()
