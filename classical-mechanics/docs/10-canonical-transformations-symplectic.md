# 正则变换与辛结构：相空间的几何学

> 路线图位置：第 2 部分（哈密顿力学与几何化）· 第 10 章
> 前置知识：第 9 章（哈密顿方程与 Poisson 括号）；线性代数（矩阵、行列式、群）；多元微积分。
> 学习目标：会判断一个变换是否正则，并用生成函数构造它；理解 $\omega = \mathrm{d}p_i\wedge\mathrm{d}q^i$ 是相空间几何的核心、Poisson 括号是它的逆；知道 Darboux 定理说了什么；能把正则变换与量子幺正变换、辛群与 metaplectic 表示对应起来。

---

**单位约定**：本篇是经典力学，保留 $\hbar$ 与 $c$；第 6 节的旧量子论对照会显式写出 $\hbar$。

## 1. 一句话总结

**正则变换 = 保持哈密顿方程形式的换坐标 = 保持 Poisson 括号的变换 = 保持辛形式 $\omega$ 的变换；生成函数是它的"势"，Darboux 定理保证辛几何局部没有不变量。辛结构是相空间唯一的几何——它定义括号、定义演化、定义量子化的起点，也定义协变相空间中"边界荷"的语言。**

## 2. 为什么换坐标

- **可解性**：找一组坐标使 $H$ 只依赖动量，则运动方程 $\dot Q = \partial H/\partial P$、$\dot P = 0$ 立刻可积（作用量–角变量，第 6 节）。
- **不变量**：Poisson 括号、相体积、"简并度"在正则变换下不变，是判断系统性质的坐标无关语言。
- **例子**：耦合振子 → 简正坐标；中心力问题 → 角变量（第 2 章）。

换坐标的自由度很大，但"保持哈密顿结构"的条件把它限制成一个群——这就是下面的判据。

## 3. 正则变换的定义与判据

### 3.1 定义

变换 $(q,p)\mapsto(Q,P)$ 称为**正则变换**，如果存在新的哈密顿量 $K(Q,P,t)$ 使得新变量满足同样形式的哈密顿方程：

$$\dot Q^i = \frac{\partial K}{\partial P_i},\qquad \dot P_i = -\frac{\partial K}{\partial Q^i}.$$

### 3.2 判据一：基本括号不变

由 $\dot Q = \{Q,K\}$、$\dot P = \{P,K\}$ 要在任意 $K$ 下成立，必须且只需

$$\{Q^i,Q^j\} = 0,\qquad \{P_i,P_j\} = 0,\qquad \{Q^i,P_j\} = \delta^i_{\ j},$$

其中括号用**旧的** $(q,p)$ 计算。这是最常用的判据：算三个括号即可。

### 3.3 判据二：辛矩阵

把变换的线性化写成矩阵（先看线性变换）：$Z = Mz$，$M = \partial(Q,P)/\partial(q,p)$。基本括号不变等价于

$$M^T J M = J,\qquad J = \begin{pmatrix}0 & \mathbb 1\\ -\mathbb 1 & 0\end{pmatrix}.$$

满足此式的矩阵 $M$ 叫**辛矩阵**，全体构成辛群 $\mathrm{Sp}(2n,\mathbb R)$。取行列式得 $(\det M)^2 = 1$；由连通性（$M$ 可连续形变到单位阵）知 $\det M = 1$——**正则变换保相体积**。

### 3.4 例子

- **旋转**：$Q = q\cos\lambda + \frac{p}{\omega}\sin\lambda$，$P = -\omega q\sin\lambda + p\cos\lambda$。验证：$\{Q,P\} = \cos^2\lambda + \sin^2\lambda = 1$，是正则变换。它正是谐振子 $H = \frac{p^2}{2m}+\frac12 m\omega^2q^2$（$m=1$）的时间演化，$\lambda = \omega t$（自检 1）。
- **缩放**：$Q = q$，$P = \lambda p$ 当 $\lambda\neq 1$ 时**不是**正则变换：$\{Q,P\} = \lambda \neq 1$，它把相体积放大了 $\lambda$ 倍。

## 4. 生成函数

### 4.1 为什么存在"势"

正则变换要求两套作用量给出同一组运动方程，即两个拉氏量最多相差一个全导数：

$$p_i\dot q^i - H = P_i\dot Q^i - K + \frac{\mathrm{d}F}{\mathrm{d}t}.$$

满足这个关系的 $F(q,p,Q,P,t)$ 叫**生成函数**。它的存在性来自辛形式 $\omega$ 的封闭性：$\omega = \mathrm{d}\theta$ 是恰当形式，$\theta = p_i\mathrm{d}q^i$，两套势的差就是 $\mathrm{d}F$（第 5 节）。

### 4.2 四种类型

$F$ 依赖四个变量中的一个组合，用 Legendre 变换换成独立变量，得到四种标准型：

| 类型 | 变量 | 变换关系 |
|---|---|---|
| $F_1$ | $(q,Q)$ | $p_i = \partial F_1/\partial q^i$，$P_i = -\partial F_1/\partial Q^i$ |
| $F_2$ | $(q,P)$ | $p_i = \partial F_2/\partial q^i$，$Q^i = \partial F_2/\partial P_i$ |
| $F_3$ | $(p,Q)$ | $q^i = -\partial F_3/\partial p_i$，$P_i = -\partial F_3/\partial Q^i$ |
| $F_4$ | $(p,P)$ | $q^i = -\partial F_4/\partial p_i$，$Q^i = \partial F_4/\partial P_i$ |

四种类型之间只差 Legendre 变换：$F_2 = F_1 + P_iQ^i$，$F_3 = F_1 - p_iq^i$，$F_4 = F_2 - p_iq^i$。

### 4.3 例子

- **恒等变换**：$F_2 = q^iP_i$ 给出 $p_i = P_i$，$Q^i = q^i$。
- **点变换**：$F_2 = f^i(q)P_i$ 给出 $Q^i = f^i(q)$，$p_i = P_j\,\partial f^j/\partial q^i$——坐标变换自动提升为正则变换。
- **自由粒子传播**：$F_2(q,P,t) = qP + \frac{t}{2m}P^2$ 给出 $Q = q + \frac{t}{m}P$，$p = P$，正是自由粒子在时间 $t$ 后的位置。
- **谐振子缩放**：$F_2 = \frac12 m\omega\, q^2$（对 $q,P$ 混合型）不适用；改用 $F_1(q,Q) = \frac12\omega q^2\cot Q$ 可得到 $Q = \omega t + \text{const}$ 的角变量（第 6 节）。

## 5. 辛形式与辛几何

### 5.1 辛形式

相空间上的 2-形式

$$\omega \equiv \mathrm{d}p_i\wedge\mathrm{d}q^i,\qquad \theta \equiv p_i\,\mathrm{d}q^i,\qquad \omega = \mathrm{d}\theta.$$

两条性质定义"辛"：**封闭** $\mathrm{d}\omega = 0$（自动，因为 $\omega = \mathrm{d}\theta$）与**非退化**（矩阵可逆）。$\theta$ 叫辛势，它的"规范变换" $\theta\to\theta+\mathrm{d}f$ 不改变 $\omega$——和电磁势与场强的关系同构。

### 5.2 哈密顿矢量场

给定 $H$，哈密顿矢量场 $X_H$ 由

$$\iota_{X_H}\,\omega = -\mathrm{d}H$$

定义（$\iota$ 为内乘）。用坐标写出来就是 $X_H = J\nabla H$，即第 9 章的 $\dot z = J\nabla H$——**哈密顿方程是"辛形式对 $\mathrm{d}H$ 的解"**。

### 5.3 括号是辛形式的逆

$$\{f,g\} = \omega(X_f,X_g) = (\nabla f)^TJ\,(\nabla g).$$

于是第 9 章的三条性质（反对称、Leibniz、Jacobi）全部是"$\omega$ 封闭且非退化"的坐标表达：反对称来自 $\omega$ 的反对称，Jacobi 来自 $\mathrm{d}\omega = 0$。

### 5.4 Darboux 定理

任意辛流形在局部总能找到坐标 $(q,p)$ 使

$$\omega = \mathrm{d}p_i\wedge\mathrm{d}q^i.$$

换句话说：**辛几何没有局部不变量**（对比黎曼几何的曲率）。所有辛流形局部长得一样，全局差别藏在拓扑与"整体"性质里（周期、作用量、辛容量）。这就是为什么哈密顿力学里"局部总能写成标准形式"，而有趣的问题总是全局的。

### 5.5 刘维尔定理的几何版

$$\frac{\omega^n}{n!} = \mathrm{d}q^1\wedge\mathrm{d}p_1\wedge\cdots\wedge\mathrm{d}q^n\wedge\mathrm{d}p_n$$

（差一个排列符号）就是相体积元。$M^TJM = J$ 保证 $\omega$ 不变，$\det M = 1$ 保证体积元不变——第 9 章的刘维尔定理在这里变成一句话：**哈密顿流保持辛形式**。

### 5.6 辛群

$\mathrm{Sp}(2n,\mathbb R)$ 的维数是 $n(2n+1)$；$n=1$ 时 $\mathrm{Sp}(2,\mathbb R) = \mathrm{SL}(2,\mathbb R)$（自检 3）。2D 相空间的正则变换 = 保面积变换，这是"辛 = 保面积"在最低维的特例；$n\geq 2$ 时"保辛"比"保体积"强得多（保辛 $\Rightarrow$ 保体积，反之不然）。

## 6. 作用量–角变量与绝热不变量

### 6.1 一维周期系统

对周期运动，定义作用量

$$J \equiv \oint p\,\mathrm{d}q,$$

它是相图上闭合轨道的面积。可以证明（自检 5）：存在正则变换 $(q,p)\to(Q,J)$ 使 $H = H(J)$、$Q$ 循环，于是

$$\dot J = 0,\qquad \dot Q = \frac{\partial H}{\partial J} \equiv \nu.$$

$\nu$ 是运动的频率（单位时间周期数）。**作用量–角变量把可积系统变成"匀速转动"**。

### 6.2 谐振子

$H = \frac{p^2}{2m}+\frac12m\omega^2q^2$ 的轨道是椭圆，面积

$$J = \pi\,a\,b = \pi\sqrt{\frac{2E}{m\omega^2}}\sqrt{2mE} = \frac{2\pi E}{\omega}.$$

于是 $E = \frac{\omega}{2\pi}J$，$\nu = \partial E/\partial J = \omega/2\pi$——熟悉的频率。

### 6.3 绝热不变量与旧量子论

参数缓慢变化（远慢于运动周期）时 $J$ 近似不变，叫**绝热不变量**（Landau 第七章）。旧量子论的 Bohr–Sommerfeld 规则

$$\oint p\,\mathrm{d}q = n h$$

就是"作用量取 $h$ 的整数倍"；代入谐振子得 $E_n = n\hbar\omega$（$\hbar = h/2\pi$，见量子力学书第 01 篇）。这是"量子化 = 相空间面积量子化"的最早形态，也是第 9 阶段协变相空间"每个量子态占 $\hbar$ 的辛面积"的祖先。

## 7. 与量子力学的接口

### 7.1 正则变换 ↔ 幺正变换

量子力学里保持概率的变换由幺正（或反幺正）算符实现（Wigner 定理，量子力学书第 12 篇）。经典正则变换是它的"影子"：**线性**正则变换（辛群）有 metaplectic 表示，可以提升为幺正算符；一般非线性正则变换没有全局量子对应（排序与拓扑障碍），只能在相空间语言里近似实现——这正是 Weyl 排序问题的几何根源（量子力学书 03s2）。

### 7.2 相空间路径积分

辛势 $\theta = p\,\mathrm{d}q$ 沿路径的积分就是作用量的 $p\dot q$ 项：

$$\int\theta = \int p\,\mathrm{d}q \;\Longrightarrow\; \int\mathcal{D}q\,\mathcal{D}p\;e^{i\int(p\dot q - H)}.$$

路径积分的相空间形式是辛几何的直接量子化（QFT 书第 4 阶段 07 篇与补充材料）。

### 7.3 协变相空间与边缘模

把"相空间"从 $(q,p)$ 换成"解空间"，辛形式变成

$$\Omega = \int_\Sigma \delta p_i\wedge\delta q^i$$

的场论版本，边界上的辛势给出表面荷与边缘模——这是 QFT 书第 9 阶段 04 篇（零锥正则引力）的出发点，也是广义相对论书第 12 章的主题。

## 小结

- 正则变换有三种等价刻画：保持哈密顿方程、保持基本括号、保持辛形式 $M^TJM = J$；辛矩阵行列式为 $1$，保相体积。
- 生成函数是正则变换的"势"，四种类型由 Legendre 变换互相联系；$F_2(q,P)$ 最常用。
- $\omega = \mathrm{d}p\wedge\mathrm{d}q$ 封闭且非退化；$X_H$ 由 $\iota_{X_H}\omega = -\mathrm{d}H$ 定义；Poisson 括号是 $\omega$ 的逆，Jacobi 恒等式等价于 $\mathrm{d}\omega = 0$。
- Darboux 定理：辛几何局部无不变量，所有相空间局部同构；刘维尔定理 = 哈密顿流保辛形式。
- 作用量–角变量把可积系统化为匀速转动；$\oint p\,\mathrm{d}q = nh$ 是"相空间面积量子化"的旧量子论版本，也是协变相空间的祖先。

## 自检问题

**1.** 验证 $Q = q\cos\lambda + \frac{p}{\omega}\sin\lambda$、$P = -\omega q\sin\lambda + p\cos\lambda$ 是正则变换，并说明它对应谐振子的时间演化。

<details markdown="1"><summary>点击显示答案</summary>

逐项计算括号（用 $\{q,p\}=1$、$\{p,q\}=-1$）：

$$\{Q,P\} = \left\{q\cos\lambda + \frac{p}{\omega}\sin\lambda,\; -\omega q\sin\lambda + p\cos\lambda\right\}.$$

展开四项：

$$\cos\lambda\cdot\cos\lambda\,\{q,p\} + \frac{\sin\lambda}{\omega}\cdot(-\omega\sin\lambda)\,\{p,q\} = \cos^2\lambda + \sin^2\lambda = 1.$$

另外 $\{Q,Q\} = \{P,P\} = 0$ 自动成立。故变换正则。

谐振子 $H = \frac{p^2}{2m}+\frac12m\omega^2q^2$ 取 $m=1$：$\dot q = p$，$\dot p = -\omega^2 q$。解为

$$q(t) = q_0\cos\omega t + \frac{p_0}{\omega}\sin\omega t,\qquad p(t) = -\omega q_0\sin\omega t + p_0\cos\omega t,$$

正是 $\lambda = \omega t$ 的上述变换。所以"谐振子的时间演化是一个单参数正则变换族"——哈密顿流本身就是正则变换（第 9 章的 $X_H$ 生成它）。

</details>

**2.** 从 $p\dot q - H = P\dot Q - K + \mathrm{d}F_1/\mathrm{d}t$ 出发，导出 $F_1(q,Q)$ 的变换关系，再用 Legendre 变换得到 $F_2(q,P)$ 的关系。

<details markdown="1"><summary>点击显示答案</summary>

设 $F_1 = F_1(q,Q,t)$，则

$$\frac{\mathrm{d}F_1}{\mathrm{d}t} = \frac{\partial F_1}{\partial q^i}\dot q^i + \frac{\partial F_1}{\partial Q^i}\dot Q^i + \frac{\partial F_1}{\partial t}.$$

代入 $p_i\dot q^i - H = P_i\dot Q^i - K + \mathrm{d}F_1/\mathrm{d}t$，整理：

$$\left(p_i - \frac{\partial F_1}{\partial q^i}\right)\dot q^i - \left(P_i + \frac{\partial F_1}{\partial Q^i}\right)\dot Q^i = H - K + \frac{\partial F_1}{\partial t}.$$

$\dot q$、$\dot Q$ 独立，故两个圆括号都为零：

$$p_i = \frac{\partial F_1}{\partial q^i},\qquad P_i = -\frac{\partial F_1}{\partial Q^i},\qquad K = H + \frac{\partial F_1}{\partial t}.$$

Legendre 变换：令 $F_2(q,P,t) = F_1(q,Q,t) + P_iQ^i$，则

$$\mathrm{d}F_2 = \mathrm{d}F_1 + P_i\,\mathrm{d}Q^i + Q^i\,\mathrm{d}P_i = p_i\,\mathrm{d}q^i - P_i\,\mathrm{d}Q^i + (K-H)\mathrm{d}t + P_i\,\mathrm{d}Q^i + Q^i\,\mathrm{d}P_i,$$

即

$$\mathrm{d}F_2 = p_i\,\mathrm{d}q^i + Q^i\,\mathrm{d}P_i + (K-H)\mathrm{d}t,$$

读出

$$p_i = \frac{\partial F_2}{\partial q^i},\qquad Q^i = \frac{\partial F_2}{\partial P_i},\qquad K = H + \frac{\partial F_2}{\partial t}.$$

检验：$F_2 = q^iP_i$ 给出 $p_i = P_i$、$Q^i = q^i$，即恒等变换。

</details>

**3.** 证明 $2\times 2$ 情形下 $M^TJM = J$ 等价于 $\det M = 1$，并写出一般解的参数形式。

<details markdown="1"><summary>点击显示答案</summary>

设 $M = \begin{pmatrix}a & b\\ c & d\end{pmatrix}$，$J = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}$。先算 $JM = \begin{pmatrix}c & d\\ -a & -b\end{pmatrix}$，再算

$$M^TJM = \begin{pmatrix}a & c\\ b & d\end{pmatrix}\begin{pmatrix}c & d\\ -a & -b\end{pmatrix} = \begin{pmatrix}ac - ac & ad - bc\\ bc - ad & bd - bd\end{pmatrix} = \begin{pmatrix}0 & \det M\\ -\det M & 0\end{pmatrix} = (\det M)\,J.$$

所以 $M^TJM = J \iff \det M = 1$。故 $\mathrm{Sp}(2,\mathbb R) = \mathrm{SL}(2,\mathbb R)$：所有行列式为 $1$ 的实 $2\times2$ 矩阵，三个参数（例如 $a,b,c$ 加约束 $ad-bc=1$），维数 $3 = n(2n+1)|_{n=1}$。

一般解可写成三种基本因子的乘积：缩放 $S(\lambda) = \mathrm{diag}(\lambda,\lambda^{-1})$、剪切 $T(\mu) = \begin{pmatrix}1 & \mu\\ 0 & 1\end{pmatrix}$、旋转 $R(\theta) = \begin{pmatrix}\cos\theta & \sin\theta\\ -\sin\theta & \cos\theta\end{pmatrix}$。三种因子分别对应"改变尺度""改变形状""转动"，任何 $2\times2$ 辛变换都是它们的组合。

（一般 $n$：取行列式得 $(\det M)^2 = 1$；由于 $\mathrm{Sp}(2n,\mathbb R)$ 连通且单位阵行列式为 $+1$，故 $\det M = +1$——只保体积不够，还要保辛形式。）

</details>

**4.** 证明正则变换保持相体积，并说明为什么"保体积"弱于"保辛"。

<details markdown="1"><summary>点击显示答案</summary>

相体积元可以用 $\omega$ 的幂写出：

$$\frac{\omega^n}{n!} = \mathrm{d}q^1\wedge\mathrm{d}p_1\wedge\cdots\wedge\mathrm{d}q^n\wedge\mathrm{d}p_n$$

（按 $\mathrm{d}p\wedge\mathrm{d}q$ 的顺序，差一个整体符号，不影响体积）。正则变换按定义保持 $\omega$：$M^TJM = J$，于是 $\omega$ 的每个楔积因子都不变，$\omega^n/n!$ 不变——相体积守恒。

"保体积"弱于"保辛"：$\mathrm{Sp}(2n,\mathbb R)$ 的维数是 $n(2n+1)$，而保体积群 $\mathrm{SL}(2n,\mathbb R)$ 的维数是 $(2n)^2 - 1 = 4n^2 - 1$。两者之差为

$$(4n^2 - 1) - (2n^2 + n) = 2n^2 - n - 1 = (2n+1)(n-1),$$

$n\geq 2$ 时为正。所以高维相空间里存在大量"保体积但不保辛"的变换，它们不保持哈密顿方程的形式。$n=1$ 时两者恰好重合（都是 $\mathrm{SL}(2,\mathbb R)$），这就是"2D 辛 = 保面积"的特殊性。

</details>

**5.** 谐振子的作用量–角变量：算出 $J = 2\pi E/\omega$，验证 $\nu = \partial H/\partial J = \omega/2\pi$，并说明 Bohr–Sommerfeld 规则 $J = nh$ 如何给出 $E_n = n\hbar\omega$。

<details markdown="1"><summary>点击显示答案</summary>

轨道 $H = \frac{p^2}{2m}+\frac12m\omega^2q^2 = E$ 是椭圆，半轴为

$$a = \sqrt{\frac{2E}{m\omega^2}}\ (\text{沿 } q),\qquad b = \sqrt{2mE}\ (\text{沿 } p).$$

面积

$$J = \pi ab = \pi\sqrt{\frac{2E}{m\omega^2}}\sqrt{2mE} = \pi\frac{2E}{\omega} = \frac{2\pi E}{\omega}.$$

于是

$$H = E = \frac{\omega}{2\pi}J,\qquad \nu = \frac{\partial H}{\partial J} = \frac{\omega}{2\pi}.$$

$\nu$ 是每秒的周期数，与 $\omega = 2\pi\nu$ 一致，验证了作用量–角变量的频率定义。

Bohr–Sommerfeld：$J = nh$ 代入 $E = \omega J/2\pi$：

$$E_n = \frac{\omega}{2\pi}\,nh = n\hbar\omega\qquad(\hbar = h/2\pi).$$

这正是谐振子的旧量子论能谱（零点能是后来量子力学才补上的）。它说明"量子化"在相空间里的含义是**作用量（面积）取离散值**——第 9 阶段零锥正则引力中"每个量子态占 $\hbar$ 的辛面积"是同一思想在无穷维的推广。

</details>

## 参考

- Landau & Lifshitz《力学》第七章：§45（正则变换）、§46（刘维尔定理）、§47（Hamilton–Jacobi 方程），以及作用量–角变量与绝热不变量各节。
- Goldstein《Classical Mechanics》第 9 章（正则变换、生成函数、括号），第 10 章（Hamilton–Jacobi 理论）。
- Arnold《经典力学的数学方法》第 3 章（辛流形、Darboux 定理、刘维尔定理的几何证明）。
- 第 9 章（括号与哈密顿方程）与第 12 章（约束系统）；量子化接口见量子力学书 03s2、QFT 书第 4 阶段 07 篇与第 9 阶段 04 篇。
