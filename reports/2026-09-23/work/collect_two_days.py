"""本期补扫：仅在内存中把抓取窗口至少扩到五天，再由 scout 按接续点筛选。"""
import json
import pathlib
import runpy
import sys
root = pathlib.Path(__file__).resolve().parents[3]
original = pathlib.Path.read_text

def read_text(path, *args, **kwargs):
    text = original(path, *args, **kwargs)
    if path.name == 'meta.json' and path.parent.parent == root / 'sources':
        data = json.loads(text)
        data['window_hours'] = max(120, int(data.get('window_hours', 168)))
        return json.dumps(data, ensure_ascii=False)
    return text

pathlib.Path.read_text = read_text
sys.argv = [str(root / 'scripts/collect_sources.py'), '2026-09-23']
runpy.run_path(sys.argv[0], run_name='__main__')
