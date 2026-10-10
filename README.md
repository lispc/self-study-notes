# 学习仓库

自学讲义仓库，目前七本书（持续写作中），分两类：

## 科学

物理线六本，按依赖顺序排列：

- **[理论力学](classical-mechanics/README.md)** — 对称性推出作用量、几何化收尾到混沌与 KAM，是量子理论的对口预科。
- **[电动力学](electrodynamics/README.md)** — 场概念与狭义相对论的诞生地，高斯制主线，通向 QFT 的第一座桥。
- **[量子力学](quantum-mechanics/README.md)** — 从旧量子论到多体语言，是热统、QFT 与凝聚态三本书的共同上游。
- **[热力学与统计力学](thermal-physics/README.md)** — 宏观唯象薄层开路、微观统计为主体、公理化与基础问题封顶，是凝聚态与 QFT 两本书里统计工具的源头。
- **[量子场论与标准模型自学路线图](qft-sm/README.md)** — 面向本科数学物理基础，目标"真正理解 QFT 与标准模型"。
- **[凝聚态物理入门导论](condensed-matter/README.md)** — 从晶格振动到拓扑物态，与场论笔记大量互相引用。

## 工程

- **[数字电路设计](digital-design/README.md)** — 从逻辑门到一颗五级流水 RISC-V 核，例子用开源工具链真跑。

七本书共享同一套笔记模板（一句话总结、编号小节、5 道带折叠答案的自检题）和同一个本地预览服务器。

## 本地预览

```bash
python3 -m venv .venv
.venv/bin/pip install markdown pymdown-extensions   # 若 pip 报 --user 错误，加 --isolated
.venv/bin/python serve.py                           # 打开 http://localhost:9000
```

首页 `http://localhost:9000` 列全部书，点进每本书的目录页按"阶段/章节"分节列出笔记，LaTeX 公式由 MathJax 渲染。
