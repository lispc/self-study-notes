# 学习仓库

自学讲义仓库，目前八本书加一个论文阅读专栏（持续写作中），分三类：

## 科学

物理线七本，按依赖顺序排列：

- **[理论力学](classical-mechanics/README.md)** — 对称性推出作用量、几何化收尾到混沌与 KAM，是量子理论的对口预科。
- **[电动力学](electrodynamics/README.md)** — 场概念与狭义相对论的诞生地，高斯制主线，通向 QFT 的第一座桥。
- **[广义相对论](general-relativity/README.md)** — 时空几何即引力：微分几何、Einstein 方程、零超曲面与带边界的作用量——QFT 书量子引力支线的几何前置（与量子力学并行读）。
- **[量子力学](quantum-mechanics/README.md)** — 从旧量子论到多体语言，是热统、QFT 与凝聚态三本书的共同上游。
- **[热力学与统计力学](thermal-physics/README.md)** — 宏观唯象薄层开路、微观统计为主体、公理化与基础问题封顶，是凝聚态与 QFT 两本书里统计工具的源头。
- **[量子场论与标准模型自学路线图](qft-sm/README.md)** — 面向本科数学物理基础，目标"真正理解 QFT 与标准模型"。
- **[凝聚态物理入门导论](condensed-matter/README.md)** — 从晶格振动到拓扑物态，与场论笔记大量互相引用。

## 工程

- **[数字电路设计](digital-design/README.md)** — 从逻辑门到一颗五级流水 RISC-V 核，例子用开源工具链真跑。

## 论文阅读

- **[论文阅读](paper-reading/README.md)** — 逐篇拆解前沿论文的论证链：每一步用到什么概念、这个概念在仓库哪本书哪一章有推导、哪些是论文自己的新东西。首篇是 Chandrasekaran《An algebraic quantization of gravity from the null cone》（arXiv:2611.34924）。

八本书共享同一套笔记模板（一句话总结、编号小节、5 道带折叠答案的自检题）和同一个本地预览服务器；论文阅读专栏沿用同一套模板。

## 本地预览

```bash
python3 -m venv .venv
.venv/bin/pip install markdown pymdown-extensions   # 若 pip 报 --user 错误，加 --isolated
.venv/bin/python serve.py                           # 打开 http://localhost:9000
```

首页 `http://localhost:9000` 列全部书，点进每本书的目录页按"阶段/章节"分节列出笔记，LaTeX 公式由 MathJax 渲染。
