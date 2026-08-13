# -*- coding: utf-8 -*-
"""
tts_daily.py <date> [--force N,N,...]

读取 reports/<date>/口播稿.md，跳过预计时长行，按空行分段：
第 1 段女声，之后男、女交替。每段独立调用 OpenRouter 的 Qwen TTS，
与 assets/tts/固定片头.m4a 拼接为 video/录音.final.m4a。

分段音频按文本、音色和模型哈希缓存。--force 可强制重做指定段号。
"""
import argparse
import hashlib
import http.client
import json
import pathlib
import subprocess
import time
import urllib.error
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL = "qwen/qwen-audio-3.0-tts-plus"
MALE = "longanlufeng"
FEMALE = "longanlingxin"


def run(cmd):
    subprocess.run(cmd, check=True)


def read_paragraphs(path):
    blocks = [x.strip() for x in path.read_text(encoding="utf-8-sig").split("\n\n")]
    return [x for x in blocks if x and not x.startswith("（预计")]


def request_audio(key, text, voice, output):
    payload = json.dumps(
        {"model": MODEL, "input": text, "voice": voice, "response_format": "mp3"},
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/audio/speech",
        data=payload,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=180) as response:
                output.write_bytes(response.read())
            return
        except (urllib.error.URLError, urllib.error.HTTPError, http.client.IncompleteRead) as exc:
            error = exc
            detail = ""
            if isinstance(exc, urllib.error.HTTPError):
                detail = exc.read().decode("utf-8", errors="replace")[:1000]
            if attempt == 2:
                raise RuntimeError(f"TTS 请求失败：{exc} {detail}") from exc
            time.sleep(2 ** attempt)
    raise RuntimeError(error)


def probe_duration(path):
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        check=True, text=True, capture_output=True,
    )
    return float(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("date")
    parser.add_argument("--force", default="", help="强制重做段号，例如 3,7")
    args = parser.parse_args()

    folder = ROOT / "reports" / args.date
    script = folder / "口播稿.md"
    intro = ROOT / "assets" / "tts" / "固定片头.m4a"
    config = json.loads((ROOT / "config.local.json").read_text())
    key = config.get("openrouter_api_key")
    if not key:
        raise SystemExit("config.local.json 缺 openrouter_api_key")
    if not script.exists() or not intro.exists():
        raise SystemExit("缺少口播稿或固定片头")

    video = folder / "video"
    work = video / "tts-segments"
    video.mkdir(exist_ok=True)
    work.mkdir(exist_ok=True)
    force = {int(x) for x in args.force.split(",") if x.strip()}
    paragraphs = read_paragraphs(script)
    manifest = []

    for index, text in enumerate(paragraphs, 1):
        voice = FEMALE if index % 2 == 1 else MALE
        digest = hashlib.sha256(f"{MODEL}\n{voice}\n{text}".encode()).hexdigest()[:16]
        raw = work / f"{index:02d}.mp3"
        meta = work / f"{index:02d}.json"
        cached = False
        if index not in force and raw.exists() and meta.exists():
            old = json.loads(meta.read_text())
            cached = old.get("hash") == digest and raw.stat().st_size > 1000
        if cached:
            print(f"[{index:02d}/{len(paragraphs)}] 缓存 {voice}：{text[:24]}")
        else:
            print(f"[{index:02d}/{len(paragraphs)}] 生成 {voice}：{text[:24]}", flush=True)
            request_audio(key, text, voice, raw)
            if raw.stat().st_size < 1000:
                raise RuntimeError(f"第 {index} 段返回文件异常")
            meta.write_text(
                json.dumps({"index": index, "voice": voice, "hash": digest, "text": text}, ensure_ascii=False, indent=2) + "\n"
            )
        manifest.append(
            {"index": index, "voice": "女声" if voice == FEMALE else "男声", "file": raw.name,
             "duration": round(probe_duration(raw), 3), "text": text}
        )

    (video / "tts-segments.json").write_text(
        json.dumps({"model": MODEL, "segments": manifest}, ensure_ascii=False, indent=2) + "\n"
    )

    inputs = ["-i", str(intro)]
    for item in manifest:
        inputs += ["-i", str(work / item["file"])]
    filters = []
    labels = ["[0:a]"]
    for i in range(1, len(manifest) + 1):
        filters.append(f"[{i}:a]aresample=44100[s{i}]")
        filters.append(f"anullsrc=r=44100:cl=mono:d=0.50[p{i}]")
        labels += [f"[p{i}]", f"[s{i}]"]
    filters.append("".join(labels) + f"concat=n={len(labels)}:v=0:a=1,loudnorm=I=-18:TP=-2:LRA=11[out]")
    output = video / "录音.final.m4a"
    run(
        ["ffmpeg", "-y", *inputs, "-filter_complex", ";".join(filters), "-map", "[out]",
         "-ar", "44100", "-ac", "1", "-c:a", "aac", "-b:a", "160k", str(output)]
    )
    print(f"✅ {output}（{probe_duration(output):.3f} 秒）")


if __name__ == "__main__":
    main()
