"""Parse a saved nitter timeline HTML file: print tweet list with date/type/text."""
import sys, json, re
from bs4 import BeautifulSoup

path = sys.argv[1]
with open(path, encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

items = []
for it in soup.select('.timeline-item'):
    if 'show-more' in it.get('class', []):
        continue
    content = it.select_one('.tweet-content')
    if content is None:
        continue
    date_a = it.select_one('.tweet-date a')
    date = date_a['title'] if date_a and date_a.has_attr('title') else (date_a.text if date_a else '?')
    link = date_a['href'] if date_a else ''
    is_rt = it.select_one('.retweet-header') is not None
    is_reply = it.select_one('.replying-to') is not None
    is_pinned = it.select_one('.pinned') is not None
    author = it.select_one('.username')
    stats = [s.get_text(strip=True) for s in it.select('.tweet-stats .tweet-stat')]
    items.append({
        'date': date,
        'link': link,
        'type': ('RT' if is_rt else 'reply' if is_reply else 'original') + ('/pinned' if is_pinned else ''),
        'author': author.get_text(strip=True) if author else '',
        'text': content.get_text(' ', strip=True)[:400],
        'stats': stats,
    })

print(json.dumps(items, ensure_ascii=False, indent=1))
