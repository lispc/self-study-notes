# AGENTS.md

QFT/凝聚态/数字电路自学讲义仓库（"学习仓库"）。主要内容：根 `README.md`（书库入口）+ 三本书各自一个顶层目录（`qft-sm/`、`condensed-matter/`、`digital-design/`，各含 `README.md` 路线图与 `docs/` 笔记）+ `serve.py`（本地预览服务器）。笔记为简体中文，含 LaTeX 公式。

## 目录与文件约定

- 仓库 = 多本"书"并列：`<书名>/README.md` 是该书的路线图/目录，`<书名>/docs/` 是笔记。
- QFT 书笔记路径：`qft-sm/docs/stage-XX-主题/NN-文档名.md`，编号按路线图阶段内的学习顺序，留空位便于插入（如第 4 阶段 02–04 尚未写）。
- 凝聚态书笔记路径：`condensed-matter/docs/NN-文档名.md`，编号对应该书 README 目录的章号，留空位。
- 数字电路书笔记路径：`digital-design/docs/NN-文档名.md`，编号对应该书 README 目录的章号，留空位；含 ```verilog / ```bash 代码块。物理书的单位/度规约定不适用于本书。
- 新增笔记后必须同步该书 README：QFT 书在对应路线图条目末尾加 `（[笔记](docs/...)）` 链接；凝聚态书和数字电路书把目录条目改为链接。
- 跨书引用用相对路径（如凝聚态笔记引用 QFT 笔记：`../../qft-sm/docs/stage-XX/...`）。
- `serve.py` 是两层结构：`/` 书库首页只列书（`BOOKS` 字典），`/<书>/` 是该书目录页（按 `STAGES` 字典分节，平铺的书直接列文件）；新增书或 stage 目录时在对应字典加一行。

## 笔记格式模板

每篇固定结构：`# 标题` + `>` 引用块（路线图位置/前置知识/学习目标）→ `## 1. 一句话总结` → 编号小节 → `## 小结` → `## 自检问题`（恰好 5 题，每题带 `<details markdown="1"><summary>点击显示答案</summary>` 折叠答案，答案要有真实推导）→ `## 参考`（指向具体教材章节）。约定：自然单位 $\hbar=c=1$（首次出现说明）、度规 $\eta=\mathrm{diag}(+1,-1,-1,-1)$、不用图片/emoji。

## 本地预览

```bash
python3 -m venv .venv
.venv/bin/pip install markdown pymdown-extensions   # 若 pip 报 --user 错误，加 --isolated
.venv/bin/python serve.py                           # http://localhost:9000
```

技术栈：Python-Markdown + `md_in_html` + `pymdownx.arithmatex`（generic 模式）+ MathJax 3（CDN）。

## 数学渲染已知坑（都踩过，写作时规避）

1. **相邻 `$$...$$` 块之间必须有空行**。两个独立显示公式紧挨着会被 arithmatex 吞并成一个块，中间的 `$$ $$` 变成公式里的字面字符。
2. **表格单元格内数学不能含裸 `|`**。`|` 被当作列分隔符，会切烂 `$|0\rangle$`、`$|\mathcal M|^2$` 这类记号。用 `\lvert`、`\rvert`、`\lVert`、`\rVert` 代替。
3. **`\slashed` 可用**（在 serve.py 的 MathJax 配置里定义为 `\not` 宏）。其他冷门宏不要用，需要时先加进 serve.py 的 `macros`。
4. **正规序记号写 `\colon\!H\!\colon`，不要写 `:H:`**。数学模式里裸冒号是关系符，`:H:=` 会渲染成松散奇怪的间距。
5. **`<summary>` 标签内不要放 `$...$`**：arithmatex 不处理 summary 里的数学，保持纯文字标题。
6. **`<details>` 折叠块**：标签写作 `<details markdown="1">`（默认展开用 `<details open markdown="1">`），内部 Markdown 才能渲染；内容首尾留空行。

## 修改后验证

服务器实时渲染 `docs/`，改文件无需重启；改 `serve.py` 才需重启。验证步骤：

```bash
# 必须加 --noproxy '*'：shell 有 http_proxy 环境变量，否则 localhost 被送进代理报 502
curl -s --noproxy '*' -o /tmp/check.html -w "%{http_code}" "http://127.0.0.1:9000/<文档相对 docs 的路径>"
```

检查：返回 200；`<details` 出现次数与源文件折叠块数一致；`arithmatex` 出现几十次以上（公式被正确包裹）；正文中无残留 `**`；arithmatex 块内不含字面 `$$`（坑 1 的症状）；表格每行列数一致（坑 2 的症状）。

## Git

- 提交信息用简体中文，概述新增/修改的笔记。
- 不要主动 commit/push，等用户明确要求。
