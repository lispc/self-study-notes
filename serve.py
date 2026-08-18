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
import urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "9000"))

# 书名目录 → (书的显示名, 一句话描述)
BOOKS = {
    "qft-sm": ("量子场论与标准模型 · 自学路线图", "从数学补课到标准模型拉氏量"),
    "condensed-matter": ("凝聚态物理入门导论", "从晶格振动到拓扑物态——场论思想的应用现场"),
    "digital-design": ("数字电路设计", "从逻辑门到一颗五级流水 RISC-V 核"),
}

# 书的 docs 内子目录 → (阶段标题, 一句话描述)；未收录的子目录按目录名原样显示
STAGES = {
    "qft-sm/docs/stage-00-math": ("第 0 阶段 · 数学补课", "群论、指标运算、变分原理——按需补的数学工具"),
    "qft-sm/docs/stage-02-quantum-mechanics": ("第 2 阶段 · 量子力学", "最关键的一关：角动量、微扰论、散射、谐振子代数解法"),
    "qft-sm/docs/stage-03-relativistic-qm": ("第 3 阶段 · 过渡桥梁", "经典场论与相对论量子力学：QFT 的语言与动机"),
    "qft-sm/docs/stage-04-qft-core": ("第 4 阶段 · QFT 核心", "量子化 → 费曼图 → QED → 重整化 → 路径积分"),
    "qft-sm/docs/stage-05-symmetry-group-theory": ("第 5 阶段 · 对称性与群论", "李群表示、整体/规范对称、自发对称性破缺"),
    "qft-sm/docs/stage-06-standard-model": ("第 6 阶段 · 标准模型", "Yang–Mills → 电弱统一 → QCD → 逐项读懂拉氏量"),
}

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


def render_md(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    body = markdown.markdown(
        text,
        extensions=["fenced_code", "tables", "toc", "md_in_html", "pymdownx.arithmatex"],
        extension_configs={"pymdownx.arithmatex": {"generic": True}},
    )
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


def render_book(book):
    """单本书的目录页：docs/ 下按 stage 子目录（或平铺）列出全部笔记。"""
    book_title, book_desc = BOOKS[book]
    docs_root = os.path.join(BASE, book, "docs")
    tree = {}  # rel_dir -> [file names]
    for dirpath, _dirnames, filenames in os.walk(docs_root):
        rel_dir = os.path.relpath(dirpath, BASE)
        mds = sorted(f for f in filenames if f.endswith(".md"))
        if mds:
            tree[rel_dir] = mds

    parts = [f'<nav><a href="/">&larr; 书库</a></nav>',
             f"<h1>{html.escape(book_title)}</h1>",
             f'<p class="desc">{html.escape(book_desc)} · <a href="/{book}/README.md">路线图 README</a></p>']
    for rel_dir in sorted(tree):
        stage_title, stage_desc = STAGES.get(rel_dir, (None, ""))
        if stage_title:  # 有阶段划分的书
            parts.append(f'<section class="stage"><h2>{html.escape(stage_title)}</h2>')
            if stage_desc:
                parts.append(f'<p class="desc">{html.escape(stage_desc)}</p>')
        parts.append('<ul class="files">')
        for name in tree[rel_dir]:
            rel = f"{rel_dir}/{name}"
            url = urllib.parse.quote(rel)
            title = html.escape(_doc_title(os.path.join(BASE, rel)))
            parts.append(f'<li><a href="/{url}">{title}</a><span class="fname">{html.escape(name)}</span></li>')
        parts.append("</ul>")
        if stage_title:
            parts.append("</section>")
    return PAGE.format(title=book_title, content="\n".join(parts))


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.unquote(self.path.split("?", 1)[0])
        path = posixpath.normpath(path).lstrip("/")
        if path in ("", "."):
            return self._send(render_home())
        book = path.rstrip("/")
        if book in BOOKS:
            return self._send(render_book(book))
        full = os.path.realpath(os.path.join(BASE, path))
        if not full.startswith(os.path.realpath(BASE) + os.sep):
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
    print(f"Serving {BASE} at http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
