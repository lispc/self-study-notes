# 理论力学

> 面向学过普通物理力学与微积分的自学者，是仓库全部物理书的起点（下游链：本书 → [电动力学](../electrodynamics/README.md) → [量子力学](../quantum-mechanics/README.md) → [热统](../thermal-physics/README.md) → [QFT](../qft-sm/README.md)/[凝聚态](../condensed-matter/README.md)）。主线观点：**理论力学是量子理论的对口预科**——拉格朗日与哈密顿形式不是解题技巧，而是量子化的入口：Poisson 括号是正则对易子的经典对应，Hamilton–Jacobi 方程是薛定谔方程的经典极限，Noether 定理是 QFT 对称性思想的源头，刘维尔定理是统计力学相空间语言的地基。叙事走"对称性第一性原理"路线：从 Galileo 相对性原理与时空的均匀、各向同性**推出**拉氏量，而不是写出牛顿方程再包装；后半本逐步几何化（正则变换、辛结构），以混沌与 KAM 收尾——那是经典力学最现代的部分，也是统计力学"平衡从何而来"的力学前身。
>
> 参考主线教材：Landau & Lifshitz 卷 1《力学》（主线骨架，极简而深刻）；Goldstein《Classical Mechanics》（查细节与例题）；Arnold《经典力学的数学方法》（几何化部分的进阶读物）。

---

## 目录

编号留有空位，便于日后插入；未挂链接的条目是待写章节。

### 第〇部分：牛顿力学的重审

1. [牛顿力学回顾与批判](docs/01-newtonian-mechanics-review.md)：质点系与守恒律、约束与广义坐标、虚位移与 d'Alembert 原理——为什么牛顿形式不够用
2. 中心力场：Kepler 问题的完整解法、轨道分类、Runge–Lenz 矢量（它的量子化身见[量子力学书 06s](../quantum-mechanics/docs/06s-hydrogen-matrix-mechanics.md)）
3. 刚体运动：欧拉角、惯量张量、陀螺——转动群的力学现身（群语言见[量子力学书第 02 篇](../quantum-mechanics/docs/02-so3-su2-and-angular-momentum.md)）

### 第一部分：拉格朗日力学（对称性第一性原理）

5. 最小作用量原理：从 Galileo 相对性原理 + 时空均匀各向同性推出自由粒子的 $L = \frac12 mv^2$（Landau 式推导）、Euler–Lagrange 方程、拉氏量的非唯一性（$L \to L + \mathrm{d}f/\mathrm{d}t$）
6. 对称性与守恒律：Noether 定理（力学版）——时间均匀性、空间均匀性、转动不变性分别给出能量、动量、角动量，"守恒律是时空对称性的影子"
7. 小振动：简正模与本征值问题、分子振动、从 $N$ 个耦合振子到链——[凝聚态书第 2 章声子](../condensed-matter/docs/02-lattice-vibrations-phonons.md)的经典原型

### 第二部分：哈密顿力学与几何化

9. 哈密顿方程与 Poisson 括号：Legendre 变换、相空间、括号代数——正则对易子的经典对应（量子化见[量子力学书第 03 篇](../quantum-mechanics/docs/03-formalism-hilbert-dirac.md)）
10. 正则变换与辛结构：生成函数、辛形式与相空间体积元、刘维尔定理——[热统书](../thermal-physics/README.md)系综理论的相空间地基
11. Hamilton–Jacobi 方程：作用量作为生成函数、作用量–角变量、绝热不变量——旧量子论 Sommerfeld 量子化规则（[量子力学书第 01 篇](../quantum-mechanics/docs/01-old-quantum-theory.md)）与 WKB（[07s 篇](../quantum-mechanics/docs/07s-variational-and-wkb.md)）的源头

### 第三部分：深入与现代

13. 可积性与三体问题：第一积分与可积的判定、Poincaré 的三体教训
14. 混沌与 KAM：非线性振子、Poincaré 截面、KAM 定理说了什么——"经典力学可以多么不确定"，通往[热统书](../thermal-physics/README.md)第 18 章（各态历经与热化）的桥
15. 经典场引子：从链的连续极限到弦、场的拉格朗日形式与 Noether 定理的场论版——[QFT 书经典场论](../qft-sm/docs/stage-03-relativistic-qm/02-lagrangian-field-theory.md)的非相对论预演

## 与其他书的接口

- 本书是仓库物理线的起点：只需普物力学 + 微积分，常微分方程随用随补。
- 下游第一站是[电动力学](../electrodynamics/README.md)：带电粒子的拉格朗日/哈密顿形式在那里收官，并走向狭义相对论。
- 通向[量子力学书](../quantum-mechanics/README.md)的三座桥：Hamilton–Jacobi → 旧量子论与 WKB；Poisson 括号 → 正则对易子；刚体转动 → 角动量与 SU(2)。
- 通向[热统书](../thermal-physics/README.md)的两座桥：刘维尔定理与相空间 → 系综与 Boltzmann 熵；混沌与 KAM → 各态历经与热化。
- 通向[QFT 书](../qft-sm/README.md)：经典场引子是 [stage-03 经典场论笔记](../qft-sm/docs/stage-03-relativistic-qm/02-lagrangian-field-theory.md)的非相对论版；Noether 定理是 QFT 全书的对称性母机。
