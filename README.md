# 学习仓库

自学讲义仓库，目前两本书（持续写作中）：

- **[量子场论与标准模型自学路线图](qft-sm/README.md)** — 面向本科数学物理基础，目标"真正理解 QFT 与标准模型"。
- **[凝聚态物理入门导论](condensed-matter/README.md)** — 从晶格振动到拓扑物态，与场论笔记大量互相引用。

两本书共享同一套笔记模板（一句话总结、编号小节、5 道带折叠答案的自检题）和同一个本地预览服务器。

## 本地预览

```bash
python3 -m venv .venv
.venv/bin/pip install markdown pymdown-extensions   # 若 pip 报 --user 错误，加 --isolated
.venv/bin/python serve.py                           # 打开 http://localhost:8000
```

首页按"书 → 阶段/章节"分节列出全部笔记，LaTeX 公式由 MathJax 渲染。
