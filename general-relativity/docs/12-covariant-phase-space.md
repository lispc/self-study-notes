# 协变相空间与守恒荷：辛势、Wald 荷与边缘模

> 路线图位置：第 3 部分（边界、约束与相空间）· 第 12 章
> 前置知识：第 4 章（微分形式）、第 5s 章（一阶引力）、第 7–8 章（因果结构、零超曲面）、第 10 章（带边界作用量）、第 11 章（ADM 约束）、[理论力学书第 9–10 章](../../classical-mechanics/docs/09-hamilton-equations-poisson-brackets.md)（辛形式）、[第 12 章](../../classical-mechanics/docs/12-constraints-dirac-theory.md)（Dirac 约束）。
> 学习目标：会在解空间上定义预辛势 $\theta$ 与辛流形式 $\omega$，并证明 $\Omega=\int_\Sigma\omega$ 与 $\Sigma$ 的选取无关；会从对称性矢量 $\xi$ 的 Hamilton 变分 $\delta H_\xi=\int_{\partial\Sigma}Q_\xi$ 读出 Komar/Wald 荷；会算 Killing 视界的 Wald 熵 $S=2\pi\oint Q=A/4G$；理解"边缘模"为什么是边界上 diffeo 不再纯规范的产物，以及论文的角点 boost 荷 $K=\mathcal A/8\pi G$ 如何从单位 boost 的 Noether 荷算出来。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。$\epsilon_{abcd}$ 为时空体积形式，取 $\epsilon_{0123}=\sqrt{-g}$（正交归一标架下 $\epsilon_{\hat 0\hat 1\hat 2\hat 3}=1$）。$\star$ 对 $p$-形式：$(\star F)_{\mu_1\dots\mu_{4-p}}=\frac{1}{p!}\epsilon_{\mu_1\dots\mu_{4-p}\nu_1\dots\nu_p}F^{\nu_1\dots\nu_p}$。**不同教材的 Komar/Wald 荷差因子 2 或整体符号，都来自 $\star$ 与 $d\xi$ 的归一化约定；比较公式前先对齐定义。**

## 1. 一句话总结

**协变相空间不选时间叶层：直接在"解空间"上定义预辛势 $\theta$（由 $\delta L=E\cdot\delta\phi+\mathrm{d}\theta$ 读出），辛流形式 $\omega=\delta\theta$ 自动闭合，因此 $\Omega=\int_\Sigma\omega$ 与 $\Sigma$ 的选取无关——这是"相空间不依赖时间"的精确版本。对称性由 $\Omega$ 的缩并给出：沿 Killing 矢量 $\xi$ 的 Hamilton 变分是一个边界积分 $\delta H_\xi=\int_{\partial\Sigma}Q_\xi$，$Q_\xi$ 就是荷。视界上的 $2\pi\oint Q$ 给出 Bekenstein–Hawking 熵 $A/4G$；而在区域的角点上，单位 boost 的 $Q_\xi$ 恰好是 $\mathcal A/8\pi G$——这就是论文的面积算符与引力时钟的经典起源。**

## 2. 解空间与变分外微分

### 2.1 三个空间

- **时空** $M$：场 $\phi(x)$ 定义在这里。
- **场空间** $\mathcal F$：所有场构型。
- **解空间** $\mathcal S\subset\mathcal F$：满足运动方程的构型。

**相空间 = 解空间**。这是协变相空间的第一句话：一个"态"就是一个整体解，不是"某时刻的初值"。初值只是解的一个切片。

### 2.2 变分外微分

在场空间上定义外微分 $\delta$：$\delta\phi$ 是切于 $\mathcal F$ 的变分。它与时空导数对易：

$$\delta\,\mathrm{d}=\mathrm{d}\,\delta .$$

**这是整套形式的关键**：$\delta$ 与 $\mathrm{d}$ 的交换性使"对场变分"与"对时空积分"可以自由换序，从而把边界项识别出来。

## 3. 预辛势与辛流形式

### 3.1 从作用量读出 $\theta$

设拉氏量密度 $\boldsymbol L=L\,\mathrm{d}^4x$（写成 4-形式，这是协变相空间的正确语言）。变分：

$$\boxed{\;\delta\boldsymbol L=\boldsymbol E\cdot\delta\phi+\mathrm{d}\boldsymbol\theta[\delta\phi]\;}$$

$\boldsymbol E=0$ 是运动方程，$\boldsymbol\theta$ 是**预辛势**（pre-symplectic potential），是一个 3-形式，线性于 $\delta\phi$。

**例（标量场）**：

$$\boldsymbol L=-\tfrac12\left(\mathrm{d}\phi\wedge\star\mathrm{d}\phi+m^2\phi\,\star1\right),$$

$$\delta\boldsymbol L=\left[(\Box-m^2)\phi\right]\delta\phi\,\star1+\mathrm{d}\left(-\star\mathrm{d}\phi\,\delta\phi\right)
\;\Longrightarrow\;\boldsymbol\theta=-\star\mathrm{d}\phi\;\delta\phi .$$

### 3.2 辛流形式

$$\boxed{\;\boldsymbol\omega\equiv\delta\boldsymbol\theta\;}$$

$\boldsymbol\omega$ 是一个 3-形式、在**场空间**里是 2-形式（对两个变分反对称）。它的闭合性有两种含义，都是自动的：

$$\mathrm{d}\boldsymbol\omega=0\ (\text{时空}),\qquad \delta\boldsymbol\omega=0\ (\text{场空间}).$$

**时空闭合性**（$\mathrm{d}\boldsymbol\omega=0$）来自 $\delta(\delta\boldsymbol L)=0$：

$$\delta^2\boldsymbol L=0=\delta\boldsymbol E\wedge\delta\phi-\boldsymbol E\wedge\delta^2\phi+\mathrm{d}\,\delta\boldsymbol\theta,$$

在解空间上 $\boldsymbol E=0$，故 $\mathrm{d}\boldsymbol\omega=0$。

### 3.3 相空间辛形式

对类空切片 $\Sigma$（更一般地，对任意 Cauchy 面），

$$\boxed{\;\Omega[\delta_1,\delta_2]=\int_\Sigma \boldsymbol\omega[\delta_1,\delta_2]\;}$$

**定理**：在解空间上，$\Omega$ 与 $\Sigma$ 的选取无关（只要 $\Sigma$ 与 $\Sigma'$ 同调且不穿过奇点）。

**证明**（自检 2 给细节）：取 $\Sigma-\Sigma'$ 围成的区域 $R$，$\int_{\partial R}\boldsymbol\omega=\int_R\mathrm{d}\boldsymbol\omega=0$。

**这条定理就是"相空间不依赖时间"**：两个不同的时刻给出同一个 $\Omega$，所以时间演化是辛变换（[理论力学书第 10 章](../../classical-mechanics/docs/10-canonical-transformations-symplectic.md)的刘维尔定理在无穷维的版本）。

## 4. 守恒荷：从辛形式到边界积分

### 4.1 对称性与 Hamilton 矢量

设 $\xi$ 是时空的对称性生成元（Killing 矢量，或更一般地，保持边界条件的 diffeo）。它在场空间上诱导一个矢量 $\delta_\xi\phi=\pounds_\xi\phi$。**如果 $\xi$ 是物理对称性**，$\delta_\xi$ 应当是 $\Omega$ 的 Hamilton 矢量：存在 $H_\xi$ 使

$$\delta H_\xi=\Omega[\delta,\delta_\xi] .$$

把 $\Omega[\delta,\delta_\xi]=\int_\Sigma\boldsymbol\omega[\delta,\pounds_\xi\phi]$ 用 Cartan 公式 $\pounds_\xi=i_\xi\mathrm{d}+\mathrm{d}i_\xi$ 整理，第一项用运动方程，第二项化成边界积分：

$$\boxed{\;\delta H_\xi=\int_{\partial\Sigma}\left[\delta\boldsymbol Q_\xi-i_\xi\boldsymbol\theta[\delta]\right]\;}$$

$\boldsymbol Q_\xi$ 是**Noether 荷 2-形式**：

$$\boxed{\;\boldsymbol Q_\xi\equiv i_\xi\boldsymbol\theta[\pounds_\xi\phi]-\boldsymbol\theta[\pounds_\xi\phi]\ \text{的相应组合}\;}$$

更常用的形式（对 $T=0$ 的引力，论文 (3.50c)）：

$$(Q_\xi)_{ab}=-\frac{1}{16\pi G_N}\left(\epsilon_g\right)_{abcd}\nabla^c\xi^d .$$

**$\delta H_\xi$ 只是一个边界积分**——这是引力最深的性质之一：**区域内的 Hamiltonian 在约束面上化为边界上的荷**。论文 §1 用这句话作为整条路线的动机：*"On solutions of the gravitational constraints, the Hamiltonian reduces to a surface charge."*

### 4.2 完整的荷公式

把 $\delta H_\xi$ 在解空间上再积一次，得到有限荷

$$H_\xi=\int_{\partial\Sigma}\left(\boldsymbol Q_\xi-i_\xi\boldsymbol\theta\right)+\text{常数},$$

常数由参考背景固定（例如 Minkowski 的零荷）。**"$\delta H$ 与 $H$ 差一个常数"这件事不能忽略**：它意味着荷的绝对值只在给定参考后才定义，而 $\delta H$ 是硬的、可算的。

### 4.3 三个标准例子

| 荷 | $\xi$ | 结果 |
|---|---|---|
| ADM 质量 | $\partial_t$（渐近） | $M$ |
| ADM 角动量 | $\partial_\phi$ | $J$ |
| Komar 质量 | $\partial_t$（Killing） | $M$（与 ADM 在静止时一致） |

**Komar 质量**（自检 4 的出发点）：

$$\boxed{\;M_{\rm Komar}=-\frac{1}{8\pi G_N}\oint_S\star\,\mathrm{d}\xi\;}$$

对 Schwarzschild、$\xi=\partial_t$、$S$ 为向外定向的大球面，$\oint\star\,\mathrm{d}\xi=-8\pi G_NM$，故给出 $M$（第 4 章自检 5 把这个积分逐项算出来了）。**符号与因子 2 都来自约定**：$\star$ 的定义、$S$ 的定向、$\xi$ 的归一化，三者任一改变都会改公式。**对齐办法**：用 Schwarzschild 与"向外定向"校准一次，之后照抄。

## 5. 视界与 Wald 熵

### 5.1 Killing 视界上的单位 boost

设 $H$ 是 Killing 视界，$\xi$ 是生成它的 Killing 矢量，在 $H$ 上 $\xi^a\xi_a=0$。表面重力 $\kappa$ 由

$$\xi^b\nabla_b\xi^a=\kappa\,\xi^a$$

定义。在视界上，$\nabla_a\xi_b$ 可以写成

$$\nabla_a\xi_b=\kappa\left(n_a\ell_b-\ell_an_b\right)=\kappa\,\epsilon_{ab},$$

$\ell,n$ 是视界的两个零法矢（$\ell\cdot n=-1$，$\ell$ 沿 $\xi$ 方向）。系数 $\kappa$ 就是表面重力；这一步的推导与第 8 章自检 1 的"$\kappa\ell^a$"是同一件事，只是这里 $\xi=\kappa^{-1}\ell$ 的归一化不同。

### 5.2 Wald 熵

Wald 的观察（1993）：把 $\delta H_\xi$ 对这个 $\xi$ 写出来，并利用热力学第一定律 $\delta M=\frac{\kappa}{2\pi}\delta S$，得到

$$\boxed{\;S_{\rm Wald}=2\pi\oint_S\boldsymbol Q_\xi\;}$$

（$\xi$ 取单位表面重力的归一化 $\kappa=1$；等价地写成 $\frac{2\pi}{\kappa}\oint Q_\xi$）。对 Einstein 引力，代入 $Q$ 的表达式与 $\nabla_a\xi_b=\kappa\epsilon_{ab}$，缩并 $\epsilon_{abcd}\epsilon^{cd}$ 得到

$$\oint_S Q_\xi=\frac{\kappa}{8\pi G_N}A ,$$

于是

$$\boxed{\;S_{\rm Wald}=\frac{2\pi}{\kappa}\cdot\frac{\kappa A}{8\pi G_N}=\frac{A}{4G_N}\;}$$

（完整系数链见自检 4）。这个 $4$ 的来源可以拆开看：$2\pi$ 来自 boost 的整转，$2$ 来自 $\epsilon_{ab}\epsilon^{ab}$ 的缩并，$16\pi$ 来自 Einstein 常数——$2\pi\times2\div16\pi=\frac14$。

**为什么这是"熵 = 角点荷"**：$S_{\rm Wald}$ 只依赖视界上的几何（$\epsilon_{ab}$ 与面积元），不依赖视界外的任何东西。它是"用边界数据算熵"的精确实现——这正是论文在有限 $G_N$ 下要做的事。

## 6. 边缘模：边界上 diffeo 不再是规范

### 6.1 问题

在无边界时空里，微分同胚是纯规范：两个相差 diffeo 的构型是同一个物理态。但**有边界时**，切于边界的 diffeo 不 vanishing on the boundary，它们会改变边界数据（诱导度规、标架取向），因此**不再纯规范**。

于是相空间必须扩张：除了 bulk 场，还要加上**边界上的场**（边缘模）。它们是"参考系"的自由度：边界在哪里、标架怎么转。

### 6.2 引力里的边缘模是什么

对带边界的区域：

- **边界度规** $q_{AB}$（cut 上的二维度规）：共形类 = 两个偏振，面积 = $\varrho^2$；
- **角点标架**：位置（角点嵌在哪里）与取向（局部 Lorentz 标架）。

论文的清单正是这个：**§3.3 的辛形式把 bulk 项消掉，只剩边界项与角点项；边缘模就是角点的位置与标架。** 而"标架的 boost"就是引力时钟：$\eta$ 是 boost 快度，$\mathcal A/(8\pi G_N)$ 是它的共轭动量。

### 6.3 角点对称性代数

在二维 cut $S$ 上，保持结构的变换群叫**角点对称群**。它至少包含：

- 每个角点的 boost $SO(1,1)$（两个角点 ⇒ $SO(1,1)\times SO(1,1)$）；
- cut 上的微分同胚 $\mathrm{Diff}(S^2)$；
- 更一般地，BMS 型/$\mathfrak{w}_{1+\infty}$ 型的扩张（不是论文必需，但读文献会遇到）。

论文只用最简单的部分：**每个角点一个 boost**。缝合两个区域时，"两侧的 boost 荷相加为零"（entangling product，§3.6）——因为两边的法矢相反，boost 也相反。

## 7. 论文怎么用这一章

| 论文位置 | 用到的本章内容 |
|---|---|
| (3.41)、(3.51) | 单位 boost 的 Noether 荷 $Q_\xi=\mu/(8\pi G)$，即 $K=\mathcal A/8\pi G$ |
| (3.50a)–(3.50c) | $Q_\xi=\frac{1}{16\pi G}B^{\mu\nu}(i_\xi\omega_{\mu\nu})+\alpha(\pounds_\xi e)$；改进项 $\alpha$ 由边界作用量固定 |
| (3.52)、(3.53) | 把辛势拉回到约化相空间：$\iota^*_t\Theta_t=p_k\delta q^k+\delta\chi_t$ |
| §3.3 | 辛形式只剩边界 + 角点项 |
| §3.6 | 缝合：两侧荷相加为零 |
| (5.22)、(5.39) | boost 生成元 $\hat K=\hat{\mathcal A}/8\pi G$；$e^{-2\pi K}$ 给热权重 |
| App C | 表示的构造；(C.2) 的 Weyl 排序与接触项（[QFT 书第 4 阶段 07s 篇](../../qft-sm/docs/stage-04-qft-core/07s-phase-space-path-integral-and-ordering.md)） |

**一句话**：论文的所有物理量都是**角点上的荷**。协变相空间是唯一能把"荷在角点上"这句话说得干净的语言。

## 8. 与约化相空间、Dirac 理论的关系

- **Dirac 路线**（[理论力学书第 12 章](../../classical-mechanics/docs/12-constraints-dirac-theory.md)）：不解约束，先算第一类/第二类，再取 Dirac 括号，最后量子化（可能还要规范固定）。
- **协变相空间路线**：也不解约束，但把 $\Omega$ 留在解空间上，用同调类定义。
- **论文路线**：**真解约束**。在零锥上把约束解成输运方程、沿生成元积分，得到的是**已约化的相空间** $\mathcal P(D)$（论文 (3.19)）。所以它的辛形式只剩边界项与角点项，没有剩余约束——这是它能"把 Poisson 括号直接提升为对易关系"（§4）的原因。

三条路线是同一个几何对象的不同处理：**约束面 $\to$ 辛形式 $\to$ 商掉规范 $\to$ 量子化**。论文的做法是把第一步做成"解方程"而不是"加括号"。

## 9. 小结

- 协变相空间 = 解空间；$\delta\boldsymbol L=\boldsymbol E\cdot\delta\phi+\mathrm{d}\boldsymbol\theta$ 定义预辛势，$\boldsymbol\omega=\delta\boldsymbol\theta$ 自动时空闭合。
- $\Omega=\int_\Sigma\boldsymbol\omega$ 与 $\Sigma$ 无关（Stokes + $\mathrm{d}\omega=0$）——相空间不依赖时间。
- 对称性 $\xi$ 的 Hamilton 变分是边界积分 $\delta H_\xi=\int_{\partial\Sigma}(\delta Q_\xi-i_\xi\theta)$；引力中 Hamiltonian 在约束面上化为边界荷。
- Komar 质量 $M_{\rm Komar}=-\frac{1}{8\pi G_N}\oint_S\star\,\mathrm{d}\xi$（Schwarzschild 校准见第 4 章自检 5）；Wald 熵 $S_{\rm Wald}=2\pi\oint Q_\xi=\frac{A}{4G}$。
- 有边界时切向 diffeo 不再纯规范 ⇒ 边缘模（边界度规 $q_{AB}$ + 角点位置与标架）；角点 boost 的荷是 $\mathcal A/8\pi G$。
- 论文把约束解掉，得到真正的约化相空间；辛形式只剩边界与角点 ⇒ 括号可直接量子化。
- 单位 boost 的 Noether 荷 $Q=\mathcal A/8\pi G$，解析延拓到 $i\pi$ 给 $e^{-2\pi K}=e^{-\mathcal A/4G\hbar}$——熵与面积谱的同一个源头。

## 自检问题

**1.** 对标量场 $\boldsymbol L=-\frac12(\mathrm{d}\phi\wedge\star\mathrm{d}\phi+m^2\phi\star1)$，算出 $\boldsymbol\theta$ 与 $\Omega$，并验证它给出 $\{\phi(x),\pi(y)\}=\delta^3(x-y)$。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：变分。**

$$\delta\boldsymbol L=-\star\mathrm{d}\phi\wedge\delta\mathrm{d}\phi-m^2\phi\,\delta\phi\,\star1 .$$

用 $\delta\mathrm{d}=\mathrm{d}\delta$ 与分部积分（$\mathrm{d}\star\mathrm{d}\phi=\Box\phi\star1$，差一个符号约定）：

$$\delta\boldsymbol L=\left[(\Box-m^2)\phi\right]\delta\phi\,\star1+\mathrm{d}\left(-\star\mathrm{d}\phi\,\delta\phi\right).$$

所以

$$\boldsymbol\theta=-\star\mathrm{d}\phi\;\delta\phi .$$

**第二步：辛流形式。** 场空间外微分 $\delta$：

$$\boldsymbol\omega=\delta\boldsymbol\theta=-\delta(\star\mathrm{d}\phi)\wedge\delta\phi=-\star\mathrm{d}(\delta\phi)\wedge\delta\phi .$$

写成两个变分反对称的形式：

$$\boldsymbol\omega[\delta_1,\delta_2]=-\left[\star\mathrm{d}(\delta_1\phi)\,\delta_2\phi-\star\mathrm{d}(\delta_2\phi)\,\delta_1\phi\right].$$

**第三步：拉回到切片。** 取 $\Sigma=\{t=\text{const}\}$，单位法矢 $n^\mu$，体积形式 $\epsilon_\Sigma=i_n\epsilon$。$\star\mathrm{d}\phi$ 拉回：

$$i_n\star\mathrm{d}\phi=\mathrm{d}\phi(n)=n^\mu\partial_\mu\phi\equiv\pi\quad(\text{用 }\Sigma\text{ 上的诱导度规归一化}).$$

于是

$$\Omega[\delta_1,\delta_2]=\int_\Sigma\left(\delta_1\pi\,\delta_2\phi-\delta_2\pi\,\delta_1\phi\right)\mathrm{d}^3x .$$

**第四步：读括号。** 把 $\Omega$ 写成标准形式 $\int(\delta_1p\,\delta_2q-\delta_2p\,\delta_1q)$，则 $\{q(x),p(y)\}=\delta^3(x-y)$。这里 $q=\phi$、$p=\pi=n^\mu\partial_\mu\phi$，故

$$\boxed{\{\phi(t,\vec x),\pi(t,\vec y)\}=\delta^3(\vec x-\vec y).}\qquad\square$$

**要点**：$\Omega$ 的表达式与 [理论力学书第 9 章](../../classical-mechanics/docs/09-hamilton-equations-poisson-brackets.md)的 $\omega=\mathrm{d}p\wedge\mathrm{d}q$ 完全同构，只是把有限维的 $\mathrm{d}$ 换成了场空间的 $\delta$、把求和换成了积分。**协变相空间不是新东西，它是对"$\omega=\delta p\wedge\delta q$"的协变化。**

</details>

**2.** 证明 $\Omega=\int_\Sigma\boldsymbol\omega$ 与类空切片 $\Sigma$ 的选取无关。

<details markdown="1"><summary>点击显示答案</summary>

设 $\Sigma_1,\Sigma_2$ 是两个同调的 Cauchy 面（$\partial\Sigma_1=\partial\Sigma_2$），$R$ 是它们围成的区域，$\partial R=\Sigma_1\cup\Sigma_2$（定向相反）。

$$\int_{\Sigma_1}\boldsymbol\omega-\int_{\Sigma_2}\boldsymbol\omega=\int_{\partial R}\boldsymbol\omega=\int_R\mathrm{d}\boldsymbol\omega .$$

而 $\mathrm{d}\boldsymbol\omega=0$（§3.2：在解空间上），故差为零。

**为什么必须在解空间上**：$\mathrm{d}\boldsymbol\omega=0$ 用到了 $\boldsymbol E=0$（否则会多出 $\delta\boldsymbol E\wedge\delta\phi$ 的项）。若离开解空间（比如在两个不同解的插值路径上），$\Omega$ 就依赖 $\Sigma$。这一点常被忽略：**"相空间 = 解空间"不是因为优雅，而是因为 $\Omega$ 的 $\Sigma$-无关性只在解空间上成立。**

**边界项**：若 $\partial\Sigma_1=\partial\Sigma_2$ 不成立（例如切片延伸到不同的边界），差一个角点上的项 $\int_{\partial\Sigma}i_\xi\boldsymbol\theta$——这就是边缘模进入的地方（§6）。论文的 (3.52) 正是把这个边界项显式写出来：

$$\iota^*_t\Theta_t=p_k\delta q^k+\delta\chi_t .$$

$\delta\chi_t$ 就是"切片移动时角点位置改变"的贡献，它被打包成全导数，在时间合成里作为相位出现（第 10 章 §5）。

**推论**：$\Omega$ 的 $\Sigma$-无关性 ⇒ 时间演化是辛变换 ⇒ 幺正性。论文 §4 的 $U_M$ 幺正（(4.18)）在经典层面的对应就是这句话。$\square$

</details>

**3.** 写出引力的预辛势 $\boldsymbol\theta$ 的显式形式，并说明它和 GHY 边界项的关系。

<details markdown="1"><summary>点击显示答案</summary>

对 Einstein–Hilbert 作用量，变分后

$$\delta\boldsymbol L_{\rm EH}=\frac{1}{16\pi G_N}\sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}\mathrm{d}^4x+\mathrm{d}\boldsymbol\theta[\delta g],$$

$$\boxed{\;\theta^\mu[\delta g]=\frac{1}{16\pi G_N}\sqrt{-g}\left[\nabla^\mu\left(g^{\alpha\beta}\delta g_{\alpha\beta}\right)-\nabla_\nu\,\delta g^{\mu\nu}\right].\;}$$

**核对**：把 $\theta^\mu$ 取散度，$\nabla_\mu\theta^\mu$ 应当等于 $\frac{1}{16\pi G}\sqrt{-g}\left(-G_{\mu\nu}\delta g^{\mu\nu}+\delta R\right)$ 的"全导数部分"。用 $\delta R=\nabla_\mu v^\mu$ 与 $v^\mu$ 的定义（第 10 章 §2.1）逐项比对即可确认 $\theta^\mu=\frac{1}{16\pi G}\sqrt{-g}\,v^\mu$。

**与 GHY 的关系**：把 $\theta^\mu$ 投影到边界上，$n_\mu\theta^\mu$ 正是第 10 章算出 $n\cdot v=-2\delta K$ 的那个量：

$$n_\mu\theta^\mu=-\frac{1}{8\pi G_N}\sqrt h\,\delta K .$$

所以：

$$\text{GHY 项的变分}\quad\delta S_{\rm GHY}=+\frac{1}{8\pi G_N}\int_{\partial M}\sqrt h\,\delta K
=-\int_{\partial M}n_\mu\theta^\mu .$$

**这是一个非常干净的对应**：

| 协变相空间语言 | 边界作用量语言 |
|---|---|
| 预辛势 $\theta^\mu$ | 边界项的"边界动量" |
| $n_\mu\theta^\mu$ | $-\delta K/(8\pi G)$（GHY 的被积式） |
| 加 GHY 项 | 把 $\theta$ 的边界法向分量从变分里减掉 |
| 辛形式 $\omega=\delta\theta$ | 边界上的 $\delta K$ 的场空间外微分 |

**为什么这很重要**：GHY 项不是"额外加的东西"，它是 $\theta$ 的边界法向分量的负值。换句话说：**协变相空间告诉你边界项必须是什么**——这也是为什么第 10 章可以用"缝合时相消"来检验边界项，而本章可以用"$\Omega$ 与 $\Sigma$ 无关"来检验它：两个检验是同一件事的两种说法。

**一阶引力的版本**（论文用的）：$\theta$ 用 $(e,\omega,B)$ 写，Pullback 到零锥后变成 (3.54) 的形状，边界项与角点项分开。$\square$

</details>

**4.** 对 Killing 视界，从 $Q_\xi$ 推出 $S_{\rm Wald}=2\pi\oint Q_\xi$ 给出 $A/4G_N$。

<details markdown="1"><summary>点击显示答案</summary>

**视界上的 $\nabla\xi$**：$\xi$ 是生成视界的 Killing 矢量，$\xi^2=0$ 在 $H$ 上。取 $\xi^a=\kappa\xi_{(0)}^a$，其中 $\xi_{(0)}$ 是仿射归一化的生成元（$\xi_{(0)}\cdot\nabla\xi_{(0)}=0$）。则

$$\nabla_a\xi_b=\kappa\left(n_a\ell_b-\ell_an_b\right)\equiv\kappa\,\epsilon_{ab},$$

$\epsilon_{ab}=n_a\ell_b-\ell_an_b$ 是"$t$–$r$"平面的单位面积元，$\epsilon_{ab}\epsilon^{ab}=-2$（号差 $-,+,+,+$ 下类时–类光平面的面积元平方为负）。

**代入 $Q$**（论文 (3.50c)）：

$$(Q_\xi)_{ab}=-\frac{1}{16\pi G_N}\epsilon_{abcd}\nabla^c\xi^d
=-\frac{\kappa}{16\pi G_N}\epsilon_{abcd}\epsilon^{cd}.$$

**缩并**：在 $S$ 上取正交归一标架 $(\hat t,\hat r,\hat\theta,\hat\phi)$，$\epsilon_{\hat t\hat r}=\pm1$。用 $\epsilon_{abcd}\epsilon^{cd}=(-1)^s\,2\,(\text{$ab$ 平面的单位面积元})$，对 $a,b\in S$ 得

$$\epsilon_{abcd}\epsilon^{cd}=-2\,\sigma_{ab},$$

$\sigma_{ab}$ 是 $S$ 的面积 2-形式（$\int_S\sigma=A$）。所以

$$(Q_\xi)_{ab}=\frac{\kappa}{8\pi G_N}\sigma_{ab},\qquad
\oint_S Q_\xi=\frac{\kappa}{8\pi G_N}A .$$

**Wald 熵**：

$$S_{\rm Wald}=2\pi\oint_S Q_\xi=\frac{2\pi\kappa}{8\pi G_N}A .$$

**去掉 $\kappa$**：严格地说 Wald 的定义是 $S=2\pi\oint Q_\xi$ 中的 $\xi$ 取**单位表面重力**的归一化（$\kappa=1$），或等价地 $S=2\pi\oint Q_{\xi}/\kappa$。取后者：

$$\boxed{\;S_{\rm Wald}=\frac{2\pi}{\kappa}\cdot\frac{\kappa A}{8\pi G_N}=\frac{A}{4G_N}.\;}\qquad\square$$

**为什么这个推导有意义**（而不是"凑出 $A/4G$"）：

1. 它只用视界上的局部几何（$\xi$、$\kappa$、面积元），不需要知道视界外或内部的任何东西。
2. 它与热力学第一定律 $\delta M=\frac{\kappa}{2\pi}\delta S$ 联立，正是 Wald 1993 的原始论证：把 $\delta H_\xi=\int_S\delta Q_\xi$ 与 $\delta M=T\delta S$ 对齐。
3. 它把熵变成了**角点上的荷**，这正是论文"从洛伦兹迹算熵"的经典前身。

**注意**：$S=A/4G$ 里的 $4$ 来自 $2\pi\times\frac{2}{16\pi}=\frac{1}{4}$——也就是"$2\pi$（boost 的整转）$\times$ $2$（$\epsilon\epsilon$ 缩并）$\div$ $16\pi$（Einstein 常数）"。论文 (5.39a) 的权重 $e^{-s}$（$s=\mathcal A/4G\hbar$）就是同一个 $4$。$\square$

</details>

**5.** 单位 boost：$\xi|_S=0$、$\nabla_a\xi_b|_S=\epsilon_{ba}=n_b\ell_a-\ell_bn_a$。用 $Q$ 的表达式算出 $Q_\xi=\mathcal A/(8\pi G_N)$，并说明为什么这是"面积算符"的种子。

<details markdown="1"><summary>点击显示答案</summary>

**$\xi$ 是什么**：在角点 $S$ 上，考虑一个把 $\ell$ 推向 $n$ 的 boost。它的 Killing 矢量在 $S$ 上为零（因为 $S$ 是 boost 的不动点集），但**导数不为零**：

$$\xi^a|_S=0,\qquad\nabla_a\xi_b|_S=\epsilon_{ba}=n_b\ell_a-\ell_bn_a .$$

这是一个"单位快度"的 boost（$\epsilon^a{}_b\epsilon^b{}_a=2$，论文 (3.51) 上方）。

**代 $Q$**：

$$(Q_\xi)_{ab}=-\frac{1}{16\pi G_N}\epsilon_{abcd}\nabla^c\xi^d
=-\frac{1}{16\pi G_N}\epsilon_{abcd}\left(n^d\ell^c-\ell^dn^c\right)
=-\frac{1}{8\pi G_N}\epsilon_{abcd}\ell^cn^d .$$

**认出面积元**：$\epsilon_{abcd}\ell^cn^d$ 正是 $S$ 的面积 2-形式（$\ell,n$ 是 $S$ 的两个零法矢，$\ell\cdot n=-1$）。它在 $S$ 上的积分是面积：

$$\oint_S\epsilon_{abcd}\ell^cn^d=\mathcal A .$$

所以

$$\boxed{\;Q_\xi=-\frac{\mathcal A}{8\pi G_N}.\;}$$

符号取决于 $S$ 的定向与 $\xi$ 的方向；取绝对值/合适定向就是论文 (3.51) 的 $Q_\xi=\mu/(8\pi G)$，其中 $\mu$ 是面积测度，积分给 $K=\mathcal A/8\pi G_N$。

**为什么这是面积算符的种子**（把三件事串起来）：

1. **经典**：角点的单位 boost 荷 = 面积 $/8\pi G$。所以"面积"不是人为引入的，它是 boost 的 Noether 荷。
2. **量子化**：把 boost 提升为算符 $\hat K=\hat{\mathcal A}/(8\pi G_N)$（论文 (5.22)）。boost 的谱是离散的 ⇒ 面积谱离散。
3. **热力学**：把 boost 解析延拓到 $i\pi$（半个整转），角点项给 $e^{-2\pi\hat K}=e^{-\hat{\mathcal A}/(4G_N\hbar)}$——**Gibbs 权重**。于是配分函数、密度矩阵、熵全部从这一个荷出来。

**还有一个细节值得注意**：$\xi|_S=0$ 意味着这个 boost 在角点上是"不动点"，所以它不移动角点、只转动标架。这保证了两件事：

- 荷只依赖标架的相对取向（$\ell$ vs $n$），不依赖角点位置；
- 缝合两个区域时，两侧的 boost 方向相反（因为 $\ell\leftrightarrow n$），荷相加为零——这就是 entangling product（论文 §3.6）的几何内容。

**一句话**：在零锥语言里，"面积"就是"角点 boost 的荷"，"熵"就是"这个荷的 $2\pi$ 倍"，"温度"就是"把 boost 解析延拓到虚时间所需的 $2\pi$"。三者是同一件事的三种读法。$\square$

</details>

## 参考

- Wald《General Relativity》附录 E、第 11 章（Noether 荷与 Komar 质量）、Wald 1993 论文 "Black hole entropy is Noether charge"（Wald 熵的原始出处）。
- Iyer & Wald, "Some properties of Noether charge and a proposal for dynamical black hole entropy"（改进项与 $\theta$ 的歧义）。
- Carroll《Spacetime and Geometry》第 6 章（Komar 质量）、第 9 章（黑洞热力学）。
- Poisson《A Relativist's Toolkit》第 4–5 章（协变相空间、Wald 荷、边缘模）。
- 关于边缘模的系统处理：Donnelly & Freidel 的 "Local subsystems in gauge theory and gravity"；Freidel, Geiller, Pranzetti 的角点对称性系列。
- [理论力学书第 9–10 章](../../classical-mechanics/docs/09-hamilton-equations-poisson-brackets.md)（辛形式与正则变换的有限维原型）、[第 12 章](../../classical-mechanics/docs/12-constraints-dirac-theory.md)（Dirac 约束与约化相空间）。
- 论文 arXiv:2611.34924 §3.3（辛形式与边缘模）、§3.6（entangling product）、(3.50)–(3.53)（Noether 荷与约化 Hamiltonian）、(5.22)、(5.39)（boost 荷与热权重）、App C。
