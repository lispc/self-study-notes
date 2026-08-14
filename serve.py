#!/usr/bin/env python3
"""本地预览 docs/ 下的 Markdown 笔记（含 LaTeX 数学公式渲染）。

用法：
    .venv/bin/python serve.py          # 默认端口 8000
    PORT=9000 .venv/bin/python serve.py
"""
import html
import http.server
import markdown
import os
import posixpath
import urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(BASE, "docs")
PORT = int(os.environ.get("PORT", "8000"))

PAGE = """<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  body {{ max-width: 860px; margin: 0 auto; padding: 2rem 1.5rem 4rem;
         font-family: -apple-system, "PingFang SC", "Helvetica Neue", Arial, sans-serif;
         line-height: 1.75; color: #24292f; }}
  img {{ max-width: 100%; }}
  code {{ background: #f6f8fa; padding: .15em .4em; border-radius: 4px; font-size: .92em; }}
  pre {{ background: #f6f8fa; padding: 1em; border-radius: 6px; overflow-x: auto; }}
  pre code {{ background: none; padding: 0; }}
  blockquote {{ border-left: 4px solid #d0d7de; margin: 0; padding: 0 1em; color: #57606a; }}
  table {{ border-collapse: collapse; }}
  th, td {{ border: 1px solid #d0d7de; padding: .4em .8em; }}
  a {{ color: #0969da; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  nav {{ margin-bottom: 1.5rem; }}
  nav a {{ font-size: .9em; color: #57606a; }}
  .dir {{ font-weight: 600; margin-top: 1.2em; }}
  ul.files {{ list-style: none; padding-left: 1em; }}
  details {{ border: 1px solid #d0d7de; border-radius: 6px; padding: .4em .9em; margin: .6em 0 1.2em; background: #fbfdfc; }}
  summary {{ cursor: pointer; color: #0969da; font-size: .92em; }}
  details[open] summary {{ margin-bottom: .5em; }}
</style>
<script>
window.MathJax = {{ tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                           displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                           macros: {{ slashed: ['{{\\\\not#1}}', 1] }} }},
                  svg: {{ fontCache: 'global' }} }};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>
<body>
{content}
</body>
</html>"""


def render_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    body = markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "toc", "md_in_html", "pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )
    title = os.path.basename(path)
    return PAGE.format(title=title, content=f'<nav><a href="/">&larr; 全部笔记</a></nav>\n{body}')


def render_index():
    entries = {}  # dir -> [file names]
    for dirpath, _dirnames, filenames in os.walk(ROOT):
        rel_dir = os.path.relpath(dirpath, ROOT)
        mds = sorted(f for f in filenames if f.endswith(".md"))
        if mds:
            entries[rel_dir] = mds
    parts = ['<h1>📖 学习笔记</h1>']
    for rel_dir in sorted(entries):
        label = "未分类" if rel_dir == "." else rel_dir
        parts.append(f'<p class="dir">{html.escape(label)}/</p><ul class="files">')
        for name in entries[rel_dir]:
            rel = name if rel_dir == "." else f"{rel_dir}/{name}"
            url = urllib.parse.quote(rel)
            parts.append(f'<li><a href="/{url}">{html.escape(name)}</a></li>')
        parts.append("</ul>")
    if len(parts) == 1:
        parts.append("<p>docs/ 下还没有 Markdown 文件。</p>")
    return PAGE.format(title="学习笔记", content="\n".join(parts))


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.unquote(self.path.split("?", 1)[0])
        path = posixpath.normpath(path).lstrip("/")
        if path in ("", "."):
            return self._send(render_index())
        full = os.path.realpath(os.path.join(ROOT, path))
        if not full.startswith(os.path.realpath(ROOT) + os.sep):
            return self._send("403 Forbidden", status=403, content_type="text/plain; charset=utf-8")
        if os.path.isfile(full) and full.endswith(".md"):
            return self._send(render_md(full))
        return self._send("404 Not Found", status=404, content_type="text/plain; charset=utf-8")

    def _send(self, body, status=200, content_type="text/html; charset=utf-8"):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    print(f"Serving {ROOT} at http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
