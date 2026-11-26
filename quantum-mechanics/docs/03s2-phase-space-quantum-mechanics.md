# 相空间量子力学：Wigner 函数、Weyl 排序与 Moyal 星积

> 路线图位置：量子力学书 · 第一部分（形式体系）· 第 03 篇的补充材料（第 03s2 篇），在 03 与 04 之后读
> 前置知识：第 03 篇（希尔伯特空间、谱定理、表象变换）；第 04 篇（升降算符、相干态、位移算符）；傅里叶变换。
> 学习目标：会从波函数算 Wigner 函数并验证两条边际分布；会说清 Weyl 排序的定义与"中点规则"；会算 Moyal 星积的低阶项并从 $[Q(f),Q(g)]$ 读出 Poisson 括号加 $O(\hbar^2)$ 修正；理解负 Wigner 函数为什么不是矛盾。

---

**单位约定**：本篇保留 $\hbar$（它是主角）；为省记号，第 3 节起取 $m = \omega = 1$，恢复时按量纲补回。

## 1. 一句话总结

**量子力学可以完全在相空间上写：Weyl 把经典函数对称排序成算符，Wigner 把态变成准概率分布，Moyal 星积把算符乘法变成相空间上的 $\star$ 乘法；$\hbar\to 0$ 时 $\star$ 退化为普通乘法、对易子退化为 Poisson 括号。这套语言是路径积分排序问题、半经典展开与量子光学的共同源头，也是 QFT 书第 9 阶段"Weyl 量子化"与"接触项"的直接前置。**

## 2. 排序问题的来历与 Weyl 的答案

### 2.1 问题

经典量 $qp$ 量子化，是 $\hat q\hat p$ 还是 $\hat p\hat q$？两者差 $i\hbar$。更一般地，$q^m p^n$ 有 $(m+n)!/(m!n!)$ 种排序方式，全部相差 $O(\hbar)$。量子化处方必须指定一个排序规则，否则"$[\,,\,] = i\hbar\{\,,\,\}$"没有确切含义。

### 2.2 Weyl 的规则

**Weyl 排序**：把每个单项式 $q^m p^n$ 替换为所有 $(m+n)!/(m!n!)$ 种排序的平均。等价的说法：把经典平面波 $e^{i(\lambda q + \mu p)}$ 对应到位移算符

$$D(\lambda,\mu) \equiv e^{i(\lambda\hat q + \mu\hat p)},$$

再按傅里叶分解线性推广：

$$f(q,p) = \int\mathrm{d}\lambda\,\mathrm{d}\mu\;\tilde f(\lambda,\mu)\,e^{i(\lambda q+\mu p)} \;\Longrightarrow\; Q(f) = \int\mathrm{d}\lambda\,\mathrm{d}\mu\;\tilde f(\lambda,\mu)\,D(\lambda,\mu).$$

Baker–Campbell–Hausdorff 公式保证 $D(\lambda,\mu)$ 良定（对易子是中心元），所以这条规则对所有多项式一致。

### 2.3 例子与对照

- $qp$ 的 Weyl 排序：$\frac12(\hat q\hat p + \hat p\hat q)$。
- $q^2p^2$ 的 Weyl 排序：六种排序的平均，等于 $\frac16(\hat q^2\hat p^2 + \hat q\hat p\hat q\hat p + \hat q\hat p^2\hat q + \hat p\hat q^2\hat p + \hat p\hat q\hat p\hat q + \hat p^2\hat q^2)$。
- **与正规序对照**：正规序（产生算符全在左）把真空期望值清零，但不保持 $q\leftrightarrow p$ 对称；Weyl 排序保持相空间的对称性，代价是真空期望值不为零（$\langle 0|Q(q^2p^2)|0\rangle \neq 0$）。两种排序适合不同的问题：正规序适合微扰论（Wick 定理），Weyl 排序适合半经典与相空间。

### 2.4 中点规则的来源

相空间路径积分把时间切片后，每个格点上的 $H$ 取在**中点** $(q_i + q_{i-1})/2$ 处：

$$\langle q_f|e^{-i\hat Ht/\hbar}|q_i\rangle = \lim_{N\to\infty}\int\prod_k\frac{\mathrm{d}p_k}{2\pi\hbar}\prod_k\mathrm{d}q_k\;e^{(i/\hbar)\sum_k\left[p_k(q_k - q_{k-1}) - \epsilon H\left(p_k,\frac{q_k+q_{k-1}}{2}\right)\right]}.$$

中点取值等价于 Weyl 排序；端点取值对应另一种排序。这不是约定俗成的选择——**不同的离散化方案给出不同的量子理论**，中点方案是唯一保持相空间对称性的那个（自检 5 与 QFT 书第 4 阶段补充材料）。

## 3. Wigner 函数

### 3.1 定义

对一维纯态 $\psi(q)$，**Wigner 函数**定义为

$$W(q,p) \equiv \frac{1}{\pi\hbar}\int_{-\infty}^{\infty}\mathrm{d}y\;e^{2ipy/\hbar}\,\psi^*(q+y)\,\psi(q-y).$$

它是相空间上的实函数，由波函数完全决定；混合态取凸组合 $W = \sum_i p_i W_i$。

### 3.2 三条性质

- **实值**：$W^* = W$（把 $y\to -y$ 即见）；
- **归一化**：$\int\mathrm{d}q\,\mathrm{d}p\,W = 1$；
- **边际分布**：

$$\int\mathrm{d}p\;W(q,p) = |\psi(q)|^2,\qquad \int\mathrm{d}q\;W(q,p) = |\tilde\psi(p)|^2.$$

于是所有位置分布与动量分布的信息都在 $W$ 里；期望值由

$$\langle \hat A\rangle = \int\mathrm{d}q\,\mathrm{d}p\;W(q,p)\,A_{\mathrm{Weyl}}(q,p)$$

给出（$A_{\mathrm{Weyl}}$ 是 $A$ 的 Weyl 符号）。

### 3.3 例子：基态与第一激发态

谐振子基态（$m=\omega=1$）：

$$\psi_0(q) = \left(\frac{1}{\pi\hbar}\right)^{1/4}e^{-q^2/2\hbar} \;\Longrightarrow\; W_0(q,p) = \frac{1}{\pi\hbar}\,e^{-(q^2+p^2)/\hbar}.$$

高斯、正定、旋转对称——最"经典"的量子态。

第一激发态：

$$\psi_1(q) = \left(\frac{1}{\pi\hbar}\right)^{1/4}\sqrt{\frac{2}{\hbar}}\;q\,e^{-q^2/2\hbar} \;\Longrightarrow\; W_1(q,p) = \frac{1}{\pi\hbar}\left(\frac{2(q^2+p^2)}{\hbar} - 1\right)e^{-(q^2+p^2)/\hbar}.$$

在原点 $W_1(0,0) = -1/\pi\hbar \lt 0$：**Wigner 函数不是概率密度**。负值不是矛盾——它恰恰是"非经典性"的定量标志：负值区域越难用经典系综解释，量子性越强。它被称为**准概率分布**。

### 3.4 纯态判据

$$2\pi\hbar\int\mathrm{d}q\,\mathrm{d}p\;W^2 = \begin{cases} 1, & \text{纯态},\\ \lt 1, & \text{混合态}.\end{cases}$$

对基态直接验证：$(1/\pi\hbar)^2\int\int e^{-2(q^2+p^2)/\hbar} = (\pi\hbar/2)/(\pi^2\hbar^2) = 1/(2\pi\hbar)$（自检 4）。

## 4. Moyal 星积

### 4.1 定义

相空间函数上的**星积**（Moyal 乘积）：

$$f\star g \equiv f\,\exp\left[\frac{i\hbar}{2}\left(\overleftarrow{\partial_q}\overrightarrow{\partial_p} - \overleftarrow{\partial_p}\overrightarrow{\partial_q}\right)\right]g.$$

箭头表示导数作用方向：$\overleftarrow{\partial_q}$ 作用在 $f$ 上，$\overrightarrow{\partial_p}$ 作用在 $g$ 上。

### 4.2 低阶展开

把指数展开到前两阶：

$$f\star g = fg + \frac{i\hbar}{2}\left(\partial_qf\,\partial_pg - \partial_pf\,\partial_qg\right) + O(\hbar^2) = fg + \frac{i\hbar}{2}\{f,g\} + O(\hbar^2).$$

**星积的反对称部分是 Poisson 括号**——这就是"量子括号在 $\hbar\to 0$ 时退化为经典括号"的精确版本。

### 4.3 算符乘法

星积的定义就是为了让"符号的乘积 = 算符的乘积"：

$$Q(f)\,Q(g) = Q(f\star g).$$

于是对易子

$$[Q(f),Q(g)] = Q(f\star g - g\star f) = i\hbar\,Q(\{f,g\}) + O(\hbar^3).$$

奇次项全部进对易子、偶次项进反对易子——这是星积展开的对称性（$\hbar$ 的奇偶与交换子/反对易子对应）。

### 4.4 基本例子

$$q\star p = qp + \frac{i\hbar}{2},\qquad p\star q = pq - \frac{i\hbar}{2} \;\Longrightarrow\; q\star p - p\star q = i\hbar.$$

量子化后 $Q(q\star p - p\star q) = [\hat q,\hat p] = i\hbar$（$Q(1) = \mathbb 1$），与正则对易关系逐字吻合。

## 5. 演化与半经典极限

### 5.1 量子刘维尔方程

Wigner 函数的演化由 Moyal 括号给出：

$$\partial_t W = \frac{1}{i\hbar}\left(H\star W - W\star H\right) = \{H,W\} + O(\hbar^2).$$

$\hbar\to 0$ 时它退化为第 9 章的刘维尔方程 $\partial_tW = \{H,W\}$——Wigner 函数变成经典相空间密度，负值区域趋于消失（在光滑势的经典极限下）。

### 5.2 谐振子：刚性旋转

对二次哈密顿量 $H = \frac12(p^2 + q^2)$（$m=\omega=1$），$\{H,\cdot\}$ 的星积展开在二阶截断（$H$ 的三阶以上导数全为零），于是

$$\partial_tW = \{H,W\}\quad\text{精确成立}.$$

解是相空间的刚性旋转：

$$W(q,p,t) = W_0\!\left(q\cos\omega t - \frac{p}{\omega}\sin\omega t,\;\omega q\sin\omega t + p\cos\omega t\right).$$

相干态的 Wigner 函数（高斯）在旋转中形状不变——**相干态是"最经典"的态**：它不扩散，永远贴着经典轨道（自检 5）。

### 5.3 半经典展开

把 $W$ 按 $\hbar$ 展开、把星积按阶展开，可以得到 WKB 的相空间版本：领头阶的 W 在经典轨道附近集中，次领头阶给出 $O(\hbar)$ 的修正。这条路线与量子力学书第 07s 篇的 WKB 是同一件事的两种语言（坐标空间 vs 相空间）。

## 6. 与路径积分、QFT 的接口

### 6.1 相空间路径积分

第 2.4 节的中点是 Weyl 排序在路径积分里的化身。一般地，

$$\int\mathcal{D}q\,\mathcal{D}p\;e^{(i/\hbar)\int(p\dot q - H)}$$

在离散化时必须指定 $H$ 的取值点，不同选择 = 不同排序。**"相空间路径积分"不是一种额外的量子化方案，它就是量子力学的相空间表述**；构型空间路径积分只是把 $p$ 高斯积掉后的特例（QFT 书第 4 阶段 07 篇第 10 节"诚实声明"悬置的正是这件事）。

### 6.2 场论版本与 QFT 第 9 阶段

把 $(q,p)$ 换成场与共轭动量 $(\phi,\pi)$，Wigner 函数泛函、星积、Moyal 括号逐字推广。QFT 书第 9 阶段的两处直接用到：

- **Weyl 量子化与中点规则**：论文 (4.20) 的 Weyl 关系与 (4.27) 的二次型时钟算符，其排序约定就是这里的 $\star$ 积；
- **接触项**：$[Q(f),Q(g)]$ 的 $O(\hbar)$ 项给出 $\{f,g\}$，$O(\hbar^2)$ 项在路径积分里表现为 $\delta$ 函数型接触项（论文附录 C.2）。

### 6.3 形变量子化

"把经典代数用 $\star$ 变形，使对易子在一阶等于 Poisson 括号"是**形变量子化**纲领的出发点（Kontsevich 定理：任意泊松流形都有星积）。这是相空间量子力学的数学完成形态，超出本书范围，但值得知道它的名字。

## 小结

- Weyl 排序 = 对所有排序取平均 = 平面波对应位移算符再线性推广；它保持相空间对称性，与路径积分的中点规则等价。
- Wigner 函数是实值准概率分布：归一化、两条边际分布正确、期望值由 Weyl 符号积分给出；第一激发态在原点为负，负值是量子性的标志。
- Moyal 星积 $f\star g = fg + \frac{i\hbar}{2}\{f,g\} + O(\hbar^2)$；$Q(f)Q(g) = Q(f\star g)$，对易子 $= i\hbar\{f,g\} + O(\hbar^3)$。
- 演化是量子刘维尔方程 $\partial_tW = \{H,W\} + O(\hbar^2)$；二次哈密顿量下精确为经典旋转，相干态形状不变。
- 相空间路径积分的中点处方 = Weyl 排序；这是 QFT 书第 9 阶段排序、接触项与 Weyl 关系的语言来源。

## 自检问题

**1.** 验证基态 Wigner 函数 $W_0(q,p) = \frac{1}{\pi\hbar}e^{-(q^2+p^2)/\hbar}$：从定义算出它，并验证归一化与位置边际分布。

<details markdown="1"><summary>点击显示答案</summary>

基态波函数（$m=\omega=1$）：$\psi_0(q) = (\pi\hbar)^{-1/4}e^{-q^2/2\hbar}$。代入定义：

$$\psi_0^*(q+y)\psi_0(q-y) = (\pi\hbar)^{-1/2}\exp\left[-\frac{(q+y)^2 + (q-y)^2}{2\hbar}\right] = (\pi\hbar)^{-1/2}e^{-q^2/\hbar}e^{-y^2/\hbar}.$$

于是

$$W_0 = \frac{1}{\pi\hbar}(\pi\hbar)^{-1/2}e^{-q^2/\hbar}\int\mathrm{d}y\;e^{-y^2/\hbar + 2ipy/\hbar}.$$

高斯积分：$\int e^{-ay^2+by}\mathrm{d}y = \sqrt{\pi/a}\,e^{b^2/4a}$，取 $a = 1/\hbar$、$b = 2ip/\hbar$：

$$\int\mathrm{d}y\;e^{-y^2/\hbar+2ipy/\hbar} = \sqrt{\pi\hbar}\;e^{-p^2/\hbar}.$$

故

$$W_0 = \frac{1}{\pi\hbar}\,e^{-(q^2+p^2)/\hbar}.\qquad\square$$

归一化：

$$\int\mathrm{d}q\,\mathrm{d}p\;W_0 = \frac{1}{\pi\hbar}\cdot\pi\hbar = 1.$$

位置边际：

$$\int\mathrm{d}p\;W_0 = \frac{1}{\pi\hbar}e^{-q^2/\hbar}\sqrt{\pi\hbar} = \frac{1}{\sqrt{\pi\hbar}}e^{-q^2/\hbar} = |\psi_0(q)|^2.\qquad\square$$

动量边际同理（$W_0$ 对 $q,p$ 对称，$\tilde\psi_0(p)$ 与 $\psi_0$ 同形）。

</details>

**2.** 从定义算出第一激发态的 Wigner 函数，验证它在原点的负值，并验证归一化。

<details markdown="1"><summary>点击显示答案</summary>

$\psi_1(q) = N q e^{-q^2/2\hbar}$，$N^2 = 2/(\hbar\sqrt{\pi\hbar})$。先算

$$\psi_1^*(q+y)\psi_1(q-y) = N^2(q+y)(q-y)e^{-[(q+y)^2+(q-y)^2]/2\hbar} = N^2(q^2 - y^2)e^{-q^2/\hbar}e^{-y^2/\hbar}.$$

代定义：

$$W_1 = \frac{N^2}{\pi\hbar}e^{-q^2/\hbar}\int\mathrm{d}y\;(q^2 - y^2)\,e^{-y^2/\hbar + 2ipy/\hbar}.$$

用两个高斯矩（$a = 1/\hbar$，$b = 2ip/\hbar$）：

$$\int e^{-ay^2+by}\mathrm{d}y = \sqrt{\frac{\pi}{a}}e^{b^2/4a},\qquad \int y^2e^{-ay^2+by}\mathrm{d}y = \left(\frac{1}{2a} + \frac{b^2}{4a^2}\right)\sqrt{\frac{\pi}{a}}e^{b^2/4a}.$$

代入 $1/(2a) = \hbar/2$、$b^2/(4a^2) = -p^2$：

$$\int\mathrm{d}y\;y^2e^{-y^2/\hbar+2ipy/\hbar} = \left(\frac{\hbar}{2} - p^2\right)\sqrt{\pi\hbar}\,e^{-p^2/\hbar}.$$

于是方括号 $= q^2 - \hbar/2 + p^2$，且 $N^2\sqrt{\pi\hbar}/(\pi\hbar) = 2/(\pi\hbar^2)$：

$$W_1 = \frac{2}{\pi\hbar^2}\,e^{-(q^2+p^2)/\hbar}\left(q^2 + p^2 - \frac{\hbar}{2}\right) = \frac{1}{\pi\hbar}\left(\frac{2(q^2+p^2)}{\hbar} - 1\right)e^{-(q^2+p^2)/\hbar}.$$

在原点：$W_1(0,0) = -\frac{1}{\pi\hbar} \lt 0$。

归一化：记 $r^2 = q^2+p^2$，$\int e^{-r^2/\hbar}\mathrm{d}q\mathrm{d}p = \pi\hbar$，$\int r^2e^{-r^2/\hbar}\mathrm{d}q\mathrm{d}p = \pi\hbar^2$，故

$$\int W_1 = \frac{1}{\pi\hbar}\left[\frac{2}{\hbar}\,\pi\hbar^2 - \pi\hbar\right] = \frac{1}{\pi\hbar}\left[2\pi\hbar - \pi\hbar\right] = 1.\qquad\square$$

负值区域的物理含义：一阶激发态的 Wigner 函数在原点附近取负，说明它不能被任何经典相空间概率分布解释——这正是"量子性"的定量标志。

</details>

**3.** 用星积定义计算 $q\star p - p\star q$ 与 $q^2\star p^2 - p^2\star q^2$，验证后者等于 $i\hbar\{q^2,p^2\}$（并说明 $\hbar^2$ 项为什么相消）。

<details markdown="1"><summary>点击显示答案</summary>

一次项：对 $f = q$、$g = p$，$\{q,p\} = 1$，高阶导数全为零：

$$q\star p = qp + \frac{i\hbar}{2}\cdot 1 = qp + \frac{i\hbar}{2},\qquad p\star q = pq - \frac{i\hbar}{2},$$

相减得 $i\hbar$。

二次项：直接用定义展开（$f = q^2$、$g = p^2$，$\{f,g\} = 4qp$）：

$$f\star g = fg + \frac{i\hbar}{2}\{f,g\} + \frac{1}{2}\left(\frac{i\hbar}{2}\right)^2\left(\partial_q^2f\,\partial_p^2g - 2\partial_q\partial_pf\,\partial_q\partial_pg + \partial_p^2f\,\partial_q^2g\right) + \cdots$$

其中 $\partial_q^2f = 2$、$\partial_p^2g = 2$，交叉项为零，故

$$q^2\star p^2 = q^2p^2 + 2i\hbar\,qp - \frac{\hbar^2}{2}.$$

同理交换 $f,g$（$\{p^2,q^2\} = -4qp$）：

$$p^2\star q^2 = p^2q^2 - 2i\hbar\,pq - \frac{\hbar^2}{2} = q^2p^2 - 2i\hbar\,qp - \frac{\hbar^2}{2}.$$

相减：

$$q^2\star p^2 - p^2\star q^2 = 4i\hbar\,qp = i\hbar\,\{q^2,p^2\}.$$

$\hbar^2$ 项相消的原因：星积展开中 $\hbar$ 的偶次幂项对两个因子是对称的（交换 $f\leftrightarrow g$ 不变号），奇次幂项反对称；对易子只保留奇次项，所以 $\hbar^2$ 项自动消失。一般地，$[Q(f),Q(g)]$ 的展开只有 $\hbar$ 的奇次幂。

</details>

**4.** 验证纯态判据：$2\pi\hbar\int\mathrm{d}q\,\mathrm{d}p\,W^2 = 1$（以基态为例），并说明对混合态为什么小于 1。

<details markdown="1"><summary>点击显示答案</summary>

基态：$W_0^2 = (\pi\hbar)^{-2}e^{-2(q^2+p^2)/\hbar}$，

$$\int\mathrm{d}q\,\mathrm{d}p\;W_0^2 = \frac{1}{\pi^2\hbar^2}\int e^{-2r^2/\hbar}\mathrm{d}q\,\mathrm{d}p = \frac{1}{\pi^2\hbar^2}\cdot\frac{\pi\hbar}{2} = \frac{1}{2\pi\hbar}.$$

故 $2\pi\hbar\int W_0^2 = 1$。$\square$

一般论证：Wigner 函数与密度矩阵的关系可以写成 $W = \frac{1}{\pi\hbar}\mathrm{Tr}(\rho\,\Delta)$（$\Delta$ 为相空间算符核），由此可得

$$\int\mathrm{d}q\,\mathrm{d}p\;W^2 = \frac{1}{2\pi\hbar}\,\mathrm{Tr}\,\rho^2.$$

对纯态 $\mathrm{Tr}\rho^2 = 1$，对混合态 $\mathrm{Tr}\rho^2 \lt 1$（等号仅当纯态）。所以"Wigner 函数的 $L^2$ 范数"是纯度（purity）的相空间读数：混合得越厉害，$W$ 越"摊平"，平方积分越小。

</details>

**5.** 证明对二次哈密顿量 $H = \frac12(p^2+\omega^2q^2)$，$\partial_tW = \{H,W\}$ 精确成立，并验证 $W(q,p,t) = W_0\!\left(q\cos\omega t - \frac{p}{\omega}\sin\omega t,\;\omega q\sin\omega t + p\cos\omega t\right)$ 是解。

<details markdown="1"><summary>点击显示答案</summary>

**精确性**：Moyal 括号的展开为

$$\{H,W\}_M = \frac{2}{\hbar}H\sin\left[\frac{\hbar}{2}\left(\overleftarrow{\partial_q}\overrightarrow{\partial_p} - \overleftarrow{\partial_p}\overrightarrow{\partial_q}\right)\right]W = \{H,W\} + O(\hbar^2).$$

修正项含 $H$ 的三阶及以上导数；$H$ 是 $q,p$ 的二次多项式，三阶导数全为零，故所有修正项 vanish，$\{H,W\}_M = \{H,W\}$ 精确。于是 $\partial_tW = \{H,W\}$。

**验证解**：令 $\lambda = \omega t$，$Q = q\cos\lambda - \frac{p}{\omega}\sin\lambda$，$P = \omega q\sin\lambda + p\cos\lambda$，$W(q,p,t) = W_0(Q,P)$。则

$$\partial_tW = \omega\left(\partial_QW_0\,\partial_\lambda Q + \partial_PW_0\,\partial_\lambda P\right) = \omega\left[\partial_QW_0\left(-\frac{P}{\omega}\right) + \partial_PW_0\,(\omega Q)\right] = -P\,\partial_QW_0 + \omega^2Q\,\partial_PW_0.$$

另一方面，用链式法则把 $\{H,W\}$ 写成对 $(Q,P)$ 的导数。由 $H = \frac12(P^2 + \omega^2Q^2)$（旋转保持 $H$），$\partial_qH = \omega^2q$、$\partial_pH = p$，且

$$\partial_qW = \partial_QW_0\cos\lambda + \omega\sin\lambda\,\partial_PW_0,\qquad \partial_pW = -\frac{\sin\lambda}{\omega}\partial_QW_0 + \cos\lambda\,\partial_PW_0.$$

代入 $\{H,W\} = \omega^2q\,\partial_pW - p\,\partial_qW$：

$$= \omega^2q\left(-\frac{\sin\lambda}{\omega}\partial_QW_0 + \cos\lambda\partial_PW_0\right) - p\left(\cos\lambda\partial_QW_0 + \omega\sin\lambda\partial_PW_0\right)$$

$$= -\left(\omega q\sin\lambda + p\cos\lambda\right)\partial_QW_0 + \omega\left(\omega q\cos\lambda - p\sin\lambda\right)\partial_PW_0 = -P\,\partial_QW_0 + \omega^2Q\,\partial_PW_0.$$

与 $\partial_tW$ 相同，故 $W_0(Q,P)$ 是解。$\square$

物理读法：Wigner 函数随经典流刚性旋转；基态的高斯形状不变，所以它是定态；相干态作为平移的高斯，同样不扩散——"最经典"的态在相空间里就是"贴着经典轨道走"的态。

</details>

## 参考

- E. Wigner, Phys. Rev. 40 (1932) 749：Wigner 函数原始论文。
- J. E. Moyal, Proc. Cambridge Philos. Soc. 45 (1949) 99：星积与相空间量子力学的奠基工作。
- Curtright, Fairlie & Zachos《A Concise Treatise on Quantum Mechanics in Phase Space》(World Scientific, 2014)：相空间表述的系统教材（Wigner 函数、星积、演化方程）。
- 第 03、04 篇（形式体系与谐振子、相干态）；路径积分的构型空间版本与"中点处方"见 [06s3](06s3-coulomb-path-integral.md) 与 QFT 书第 4 阶段 07 篇；场论中的 Weyl 量子化与接触项见 QFT 书第 9 阶段 01、04 篇。
