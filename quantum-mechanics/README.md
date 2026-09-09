# 量子力学

> 面向有本科数学物理基础（微积分、线性代数、常微分方程、普物）的自学者。本书是[量子场论路线图](../qft-sm/README.md)与[凝聚态物理导论](../condensed-matter/README.md)两本书的**共同上游**：QFT = 量子力学 + 狭义相对论，凝聚态全书则以多体量子力学为工作语言。主线观点：**从旧量子论走到多体语言**——形式体系、精确可解体系、近似方法、二次量子化与线性响应，一条线串到底。
>
> 参考主线教材：Sakurai《现代量子力学》、Griffiths《量子力学概论》、Shankar《Principles of Quantum Mechanics》。

---

## 目录

### 第〇部分：前史与数学准备

1. [旧量子论：量子概念的史前史](docs/01-old-quantum-theory.md)：黑体辐射、光电效应、Bohr 模型、对应原理
2. [SO(3)/SU(2) 与角动量的数学](docs/02-so3-su2-and-angular-momentum.md)：旋转群及其双覆盖、李代数、表示与角动量的关系

### 第一部分：形式体系

3. [形式体系：希尔伯特空间、算符与狄拉克记号](docs/03-formalism-hilbert-dirac.md)：态空间、可观测量、表象变换、不确定性关系
   - 3s. [波动力学基础：坐标表象、一维定态与隧穿](docs/03s-wave-mechanics-basics.md)：自由粒子与波包、方势阱、势垒隧穿、δ 势——抽象机器在坐标表象里的样子

### 第二部分：可精确求解的体系

4. [谐振子的升降算符解法](docs/04-harmonic-oscillator-ladder.md)：产生/湮灭算符、数表象——QFT 本质上是无穷多个谐振子
5. [角动量理论](docs/05-angular-momentum.md)：对易关系定全部、自旋、角动量耦合——SU(2) 的物理化身
6. [氢原子与电子亚层（波动力学）](docs/06-hydrogen-and-subshells.md)：径向方程、量子数、壳层结构
   - 6s. [矩阵力学解氢原子](docs/06s-hydrogen-matrix-mechanics.md)：Runge–Lenz 矢量、SO(4) 隐藏对称性、不解微分方程纯代数推出能谱
   - 6s2. [Dirac 方程精确解氢原子](docs/06s2-dirac-hydrogen.md)：好量子数与 $K$ 算符、Sommerfeld–Dirac 精确谱、精细结构
   - 6s3. [路径积分解氢原子](docs/06s3-coulomb-path-integral.md)：Duru–Kleinert 变换、库仑问题映成谐振子、从 $G(E)$ 极点读能谱

### 第三部分：近似方法

7. [微扰论](docs/07-perturbation-theory.md)：定态微扰、含时微扰、费米黄金定则——QFT 里算截面就是它的推广
   - 7s. [变分法与 WKB](docs/07s-variational-and-wkb.md)：不依赖小参数的两种近似武器——变分原理与氦原子基态、半经典展开、连接公式、$\oint p\,dx=(n+\tfrac12)h$
   - 7s2. [显关联波函数：Hylleraas 与 ECG](docs/07s2-explicitly-correlated.md)：Kato 尖点、把 $r_{ij}$ 写进波函数、氦原子算到 15 位有效数字、作为精密 QED 探针
8. [散射理论](docs/08-scattering-theory.md)：散射振幅、分波法、Born 近似

### 第四部分：多体语言

9. [二次量子化：多体问题的母语](docs/09-second-quantization.md)：Fock 空间与粒子数表象、产生湮灭算符、场算符、算符的二次量子化翻译
10. [线性响应与 Kubo 公式：理论与实验之间的桥](docs/10-linear-response-kubo.md)：密度矩阵与热平均、Kubo 公式、涨落–耗散定理、响应函数对应表

### 计划补充（待写）

- 电磁场中的粒子：最小耦合与规范不变性、Aharonov–Bohm 效应、Landau 能级 *（待写，拟编号 11）*
- 对称性与时间反演：平移/宇称/旋转作为算符、Wigner 定理、Kramers 简并 *（待写，拟编号 12）*

## 与另两本书的接口

- 本书整体 = [QFT 路线图](../qft-sm/README.md)的第 2 阶段：QFT = 量子力学 + 狭义相对论，本书正是其中"量子力学"那一半。
- 相对论量子力学入门（Klein–Gordon / Dirac 方程的引入，以及负能量解、多粒子问题等困难——正是 QFT 存在的理由）在 QFT 书：[Klein–Gordon 与 Dirac 方程](../qft-sm/docs/stage-03-relativistic-qm/01-klein-gordon-and-dirac.md)；本书 06s2 是 Dirac 方程的精确解补充。
- 路径积分的场论化（从量子力学路径积分到场的路径积分）在 QFT 书：[路径积分表述](../qft-sm/docs/stage-04-qft-core/07-path-integral.md)；本书 06s3 是它的量子力学源头例子。
- 与[凝聚态物理导论](../condensed-matter/README.md)的接口：
  - 本书 04（谐振子升降算符）→ 凝聚态第 2 章：声子就是晶格谐振子的量子化；
  - 本书 07（含时微扰论与费米黄金定则）→ 是本书 10 Kubo 公式的直接前身，进而支撑凝聚态全书的响应与输运讨论；
  - 本书 09（二次量子化）、10（线性响应）→ 凝聚态全书的工作语言（原凝聚态第〇部分整体迁入本书）。
