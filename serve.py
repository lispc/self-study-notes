#!/usr/bin/env python3
"""本地预览仓库中的 Markdown 笔记（含 LaTeX 数学公式渲染）。

仓库按"书"组织：每本书一个顶层目录，书内 docs/ 放笔记。
用法：
    .venv/bin/python serve.py          # 默认端口 9000
    PORT=9000 .venv/bin/python serve.py
"""
import html
import http.server
import markdown
import os
import posixpath
import re
import unicodedata
import urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "9000"))

# 书名目录 → (书的显示名, 一句话描述)
BOOKS = {
    "classical-mechanics": ("理论力学", "对称性推出作用量、几何化收尾到混沌与 KAM——量子理论的对口预科"),
    "electrodynamics": ("电动力学", "场概念与狭义相对论的诞生地——通向 QFT 的第一座桥"),
    "quantum-mechanics": ("量子力学", "从旧量子论到多体语言——QFT 与凝聚态的共同上游"),
    "thermal-physics": ("热力学与统计力学", "宏观唯象开路、微观统计为主体、公理化封顶——凝聚态与 QFT 统计工具的源头"),
    "qft-sm": ("量子场论与标准模型 · 自学路线图", "从数学补课到标准模型拉氏量"),
    "condensed-matter": ("凝聚态物理入门导论", "从晶格振动到拓扑物态——场论思想的应用现场"),
    "digital-design": ("数字电路设计", "从逻辑门到一颗五级流水 RISC-V 核"),
}

# 书的目录页 /<书>/ 直接渲染该书的 README.md（目录单源维护；新增笔记只需同步 README），
# 并在末尾自动列出 docs/ 下未被 README 收录的笔记作为兜底检查。

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
  ul.files {{ list-style: none; padding-left: .2em; }}
  ul.files li {{ margin: .35em 0; }}
  .fname {{ color: #8b949e; font-size: .8em; margin-left: .6em; }}
  .book {{ margin-top: 2.4em; }}
  .book > h1 {{ font-size: 1.4em; margin-bottom: .1em; }}
  .stage {{ margin-top: 1.4em; }}
  .stage h2 {{ font-size: 1.1em; border-bottom: 1px solid #d0d7de; padding-bottom: .3em; margin-bottom: .2em; }}
  .desc {{ color: #57606a; font-size: .9em; margin: .2em 0 .6em; }}
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


def _github_slug(value, separator):
    """GitHub 风格标题锚点：小写、去标点（保留中日韩文字与连字符）、空格转连字符。

    toc 扩展默认的 slugify 会把 CJK 字符剥光，导致 README 里 GitHub 风格的
    目录锚点（如 #第-4-阶段量子场论核心612-个月主战场）全部失效；换成这个。"""
    value = unicodedata.normalize("NFKC", value).lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return value.replace(" ", separator)


def _render_markdown(text):
    return markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "toc", "md_in_html", "pymdownx.arithmatex"],
        extension_configs={
            "pymdownx.arithmatex": {"generic": True},
            "toc": {"slugify": _github_slug},
        },
    )


def render_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    body = _render_markdown(text)
    title = os.path.basename(path)
    rel = os.path.relpath(path, BASE)
    book = rel.split(os.sep, 1)[0]
    nav = '<a href="/">&larr; 书库</a>'
    if book in BOOKS:
        nav += f' / <a href="/{book}/">{html.escape(BOOKS[book][0])}</a>'
    return PAGE.format(title=title, content=f"<nav>{nav}</nav>\n{body}")


def _doc_title(path):
    """取 Markdown 文件第一个一级标题作为显示名。"""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(path)


def render_home():
    """书库首页：只列书，点进单本书的目录页。"""
    parts = ["<h1>学习仓库</h1>",
             '<p class="desc">自学讲义合集。每篇笔记末尾有 5 道自检题（点击展开答案）。</p>',
             '<ul class="files">']
    for book, (book_title, book_desc) in BOOKS.items():
        parts.append(
            f'<li><a href="/{book}/">{html.escape(book_title)}</a>'
            f'<span class="fname">{book}/</span><br>'
            f'<span class="desc">{html.escape(book_desc)}</span></li>')
    parts.append("</ul>")
    return PAGE.format(title="学习仓库", content="\n".join(parts))


def _unlinked_notes(book, readme_text):
    """docs/ 下未被 README 链接的 .md 文件（返回仓库根相对路径，有序）。"""
    book_root = os.path.join(BASE, book)
    missing = []
    for dirpath, _dirnames, filenames in os.walk(os.path.join(book_root, "docs")):
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            full = os.path.join(dirpath, name)
            rel_in_book = os.path.relpath(full, book_root).replace(os.sep, "/")
            if rel_in_book not in readme_text:
                missing.append(os.path.relpath(full, BASE).replace(os.sep, "/"))
    return missing


def render_book(book):
    """单本书的目录页 = 直接渲染该书 README.md；末尾附 README 未收录的笔记清单（若有）。"""
    book_title = BOOKS[book][0]
    with open(os.path.join(BASE, book, "README.md"), encoding="utf-8") as f:
        text = f.read()
    parts = ['<nav><a href="/">&larr; 书库</a></nav>', _render_markdown(text)]
    unlinked = _unlinked_notes(book, text)
    if unlinked:
        items = "\n".join(
            f'<li><a href="/{urllib.parse.quote(rel)}">{html.escape(_doc_title(os.path.join(BASE, rel)))}</a>'
            f'<span class="fname">{html.escape(rel)}</span></li>'
            for rel in unlinked)
        parts.append('<h2>README 未收录的笔记</h2>\n'
                     '<p class="desc">以下文件存在于 docs/ 但未被 README 链接——'
                     '按仓库约定新增笔记需同步 README，请补上链接。</p>\n'
                     f'<ul class="files">\n{items}\n</ul>')
    return PAGE.format(title=book_title, content="\n".join(parts))


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        raw = urllib.parse.unquote(self.path.split("?", 1)[0])
        path = posixpath.normpath(raw).lstrip("/")
        if path in ("", "."):
            return self._send(render_home())
        if path.rstrip("/") in BOOKS:
            if not raw.endswith("/"):
                # 书目录页渲染 README.md，其相对链接依赖尾斜杠才能正确解析
                return self._redirect(f"/{path.rstrip('/')}/")
            return self._send(render_book(path.rstrip("/")))
        full = os.path.realpath(os.path.join(BASE, path))
        if not full.startswith(os.path.realpath(BASE) + os.sep):
            return self._send("403 Forbidden", status=403, content_type="text/plain; charset=utf-8")
        if os.path.isfile(full) and full.endswith(".md"):
            return self._send(render_md(full))
        return self._send("404 Not Found", status=404, content_type="text/plain; charset=utf-8")

    def _redirect(self, location):
        self.send_response(301)
        self.send_header("Location", location)
        self.send_header("Content-Length", "0")
        self.end_headers()

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
    print(f"Serving {BASE} at http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
