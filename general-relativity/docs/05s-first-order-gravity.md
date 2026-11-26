# 一阶引力：标架、自旋联络与 Plebański 作用量

> 路线图位置：第 2 部分（动力学与解）· 第 5s 章（第 5 章的补充材料）
> 前置知识：第 1–4 章（张量、联络、曲率、微分形式）；第 5 章（Einstein–Hilbert 作用量与变分）。
> 学习目标：会把度规换成标架 $e^a{}_\mu$ 与自旋联络 $\omega^{ab}{}_\mu$ 并写出 Palatini 作用量；会从两个变分分别得到"挠率为零"与 Einstein 方程；理解简单性约束 $B=\star(e\wedge e)$ 如何把拓扑的 BF 理论变成 GR，以及"约束不含导数 ⇒ 不产生边界项"这一点在带边界问题里的分量。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$；内部平坦指标 $a,b,c,\dots$，时空指标 $\mu,\nu,\rho,\dots$。$c=1$，保留 $G_N$，记 $\kappa\equiv 8\pi G_N$。内部 Levi-Civita 符号取 $\epsilon_{0123}=+1$；微分形式的楔积按 $\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu$ 的字典序，全书其余约定同第 4 章。

## 1. 一句话总结

**把度规 $g_{\mu\nu}$ 拆成"标架 $e^a{}_\mu$ + 局部 Lorentz 标架"，再让自旋联络 $\omega^{ab}{}_\mu$ 独立，Einstein–Hilbert 作用量就变成"曲率二形式乘二形式"——Palatini 形式；再把二形式场 $B^{ab}$ 引进来、用代数约束锁成 $\star(e^a\wedge e^b)$，就是 Plebański 形式。这一形式的价值不在等价性本身，而在三件事：局部 Lorentz 标架成为了物理数据（边缘模的载体）、简单性约束不含导数因而不产生边界项（边界变量可以原样缝合）、以及整个作用量对 $B$ 与 $\omega$ 的依赖都是低阶的——这正是零锥约化（[QFT 书第 9 阶段](../../qft-sm/README.md)论文 §3）的起点。**

## 2. 为什么要把度规换成标架

### 2.1 度规不知道"哪是时间方向"

$g_{\mu\nu}$ 只给长度与角度：它能回答"这条曲线有多长"，不能回答"这个实验室的三个空间轴指向哪里"。后者需要一个局部正交归一基

$$e_a = e_a{}^\mu\,\partial_\mu,\qquad g(e_a,e_b)=\eta_{ab}.$$

对偶地，用一组一形式（**标架**、tetrad、vierbein）

$$e^a = e^a{}_\mu\,\mathrm{d}x^\mu,\qquad g_{\mu\nu}=\eta_{ab}\,e^a{}_\mu e^b{}_\nu .$$

给定 $e^a{}_\mu$ 就唯一确定了度规；反过来给定度规，$e^a{}_\mu$ 只确定到每点的局部 Lorentz 变换 $e^a\to\Lambda^a{}_b e^b$、$\Lambda\in SO(3,1)$。

### 2.2 三个理由

1. **费米场**：旋量只与局部 Lorentz 群耦合，$\gamma^a$ 是平坦指标上的矩阵。没有标架就写不出 Dirac 方程（[QFT 书 stage-03 的弯曲时空推广](../../qft-sm/docs/stage-03-relativistic-qm/01-klein-gordon-and-dirac.md)）。
2. **降阶**：Einstein–Hilbert 作用量含 $g$ 的二阶导数；把 $e$ 与 $\omega$ 当作独立变量，作用量只含一阶导数，变分只出代数方程——这是量子化时最要紧的结构。
3. **本题的理由**：论文要在角点问"这个场在哪个标架里测量"。标架的**位置与取向**在带边界问题里是物理数据（边缘模），不是规范冗余；用度规写，这句话根本说不出来。第 12 章会看到，角点的 boost 荷就是面积。

### 2.3 自由度计数

$e^a{}_\mu$ 有 $4\times4=16$ 个分量。每点的局部 Lorentz 变换有 6 个参数，且不改变 $g_{\mu\nu}$，故独立分量

$$16-6=10,$$

正好是 $g_{\mu\nu}$ 的 10 个分量。**标架没有增加也没有减少信息，它只是把度规"开了平方"，代价是多出一个每点 6 维的规范群。**

## 3. 自旋联络、挠率与曲率

要让 $e^a$ 在弯曲时空里做协变微分，需要局部 Lorentz 群的联络 $\omega^{ab}{}_\mu=\omega^{[ab]}{}_\mu$（24 个分量），写成二形式

$$\omega^{ab}=\omega^{ab}{}_\mu\,\mathrm{d}x^\mu .$$

协变外微分：$D_\omega V^a=\mathrm{d}V^a+\omega^a{}_b\wedge V^b$。由此定义两个基本张量：

$$\boxed{\;T^a=D_\omega e^a=\mathrm{d}e^a+\omega^a{}_b\wedge e^b,\qquad R^{ab}=\mathrm{d}\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}.\;}$$

$T^a$ 是**挠率**二形式，$R^{ab}$ 是**曲率**二形式。两个 Bianchi 恒等式

$$D T^a=R^a{}_b\wedge e^b,\qquad D R^{ab}=0$$

都是"$D^2=0$ 的曲率版本"，逐项展开即可验证。

**与二阶语言的关系**：若 $T^a=0$，则可把 $\omega$ 解成 $e$ 的函数，此时 $R^{ab}{}_{\mu\nu}$ 就是 Riemann 张量在标架里的分量 $R^{ab}{}_{\mu\nu}=e^a{}_\rho e^b{}_\sigma R^{\rho\sigma}{}_{\mu\nu}$。

## 4. Palatini 作用量

$$\boxed{\;S_{\rm P}[e,\omega]=\frac{1}{2\kappa}\int \epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}[\omega].\;}$$

$e$ 与 $\omega$ **独立变分**。这个作用量只含一阶导数：$R$ 含 $\omega$ 的一次导数，$e\wedge e$ 不含导数。

### 4.1 对 $\omega$ 变分：挠率为零

用 $\delta R^{ab}=D_\omega\,\delta\omega^{ab}$（因为 $\delta(\omega\wedge\omega)=\delta\omega\wedge\omega+\omega\wedge\delta\omega$ 正是 $D\delta\omega$ 的非导数部分）：

$$\delta_\omega S=\frac{1}{2\kappa}\int\epsilon_{abcd}\,e^a\wedge e^b\wedge D\,\delta\omega^{cd}
=-\frac{1}{2\kappa}\int\epsilon_{abcd}\,D(e^a\wedge e^b)\wedge\delta\omega^{cd}+\text{边界项}.$$

（分部积分时 $D$ 从 $\delta\omega$ 挪到 $e\wedge e$ 上，产生一个全微分。）而

$$D(e^a\wedge e^b)=De^a\wedge e^b-e^a\wedge De^b=T^a\wedge e^b-e^a\wedge T^b .$$

要求上式对所有 $\delta\omega^{cd}$ 为零，等价于

$$\boxed{\;T^a=0.\;}$$

**挠率为零不是假设，是运动方程。** 这一步在自检 2 里给出"$T^a\wedge e^b-e^a\wedge T^b=0\Rightarrow T^a=0$"的论证。

### 4.2 对 $e$ 变分：Einstein 方程

$$\delta_e S=\frac{2}{2\kappa}\int\epsilon_{abcd}\,\delta e^a\wedge e^b\wedge R^{cd}
\;\Longrightarrow\;\epsilon_{abcd}\,e^b\wedge R^{cd}=0 .$$

这是 Einstein 方程的六形式写法。与 $e^a$ 缩并立刻得到它的迹：

$$\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}=0\;\Longleftrightarrow\;R=0,$$

因为左边正是作用量密度。而 $R=0$ 是真空 Einstein 方程 $R_{\mu\nu}-\frac12Rg_{\mu\nu}=0$ 的迹。剩下的无迹部分给出 $R_{\mu\nu}=0$。

**计数**：16 个方程减去 6 个局部 Lorentz 变换（它们是恒等式，因为作用量在局部 Lorentz 下不变），剩 10 个——与度规变分得到的 10 个 Einstein 方程一致。

## 5. 把 $\omega$ 解出来：回到 Einstein–Hilbert

$T^a=0$ 是 24 个代数方程，可以解出 24 个 $\omega^{ab}{}_\mu$：

$$\omega^{ab}{}_\mu=\tfrac12 e^{a\nu}\left(\partial_\mu e^b{}_\nu-\partial_\nu e^b{}_\mu\right)
-\tfrac12 e^{b\nu}\left(\partial_\mu e^a{}_\nu-\partial_\nu e^a{}_\mu\right)
-\tfrac12 e^{a\rho}e^{b\sigma}\left(\partial_\rho e_{c\sigma}-\partial_\sigma e_{c\rho}\right)e^c{}_\mu .$$

三项的结构值得记住：**前两项是"反对称化的 $\partial e$"，第三项是补偿项**，它保证 $\omega$ 在局部 Lorentz 变换下正确变换。前两项单独存在时 $\omega$ 会像规范场一样变换，第三项把它拧成真正的自旋联络。

把 $\omega(e)$ 代回 $S_{\rm P}$：

$$S_{\rm P}[e,\omega(e)]=\frac{1}{2\kappa}\int\sqrt{-g}\,R\,\mathrm{d}^4x+\text{全导数},$$

即 Einstein–Hilbert 作用量（差一个全导数与一个约定因子；自检 3 验证其变分结构）。**所以 Palatini 形式与 EH 在经典层面完全等价，只是把"二阶导数"换成了"两个独立的低阶场"。**

## 6. Plebański 形式：BF + 简单性约束

### 6.1 BF 是拓扑的

只保留第一项、把 $e\wedge e$ 换成一个独立的二形式场 $B_{ab}$（内部反对称指标）：

$$S_{\rm BF}[B,\omega]=\frac{1}{2\kappa}\int B_{ab}\wedge R^{ab}[\omega].$$

变分 $B$ 给 $R^{ab}=0$；变分 $\omega$ 给 $D B^{ab}=0$。这是一套"平坦联络 + 协变常二形式"的方程，**没有任何局部传播自由度**——它是拓扑场论（与 4 维 BF 理论同构）。物理上这是"没有引力波的世界"。

### 6.2 简单性约束

$B^{ab}$ 的分量数：时空二形式 6 个 × 内部反对称 6 个 = **36**。而标架只有 **16** 个。要把 $B$ 锁成"某个标架的外积"，需要 $36-16=20$ 个约束：

$$\boxed{\;B^{ab}=\star\!\left(e^a\wedge e^b\right)\equiv\tfrac12\epsilon^{ab}{}_{cd}\,e^c\wedge e^d\;}$$

这组条件叫**简单性约束**（simplicity constraint）：它说 $B$ 是一个"简单"二形式，能写成两个一形式的楔积（的 Hodge 对偶）。用 Lagrange 乘子把约束加进作用量：

$$S_{\rm Pl}[B,\omega,e,\lambda]=\frac{1}{2\kappa}\int\left[B_{ab}\wedge R^{ab}-\lambda_{ab}\wedge\left(B^{ab}-\star(e^a\wedge e^b)\right)\right].$$

变分 $\lambda$ 强迫 $B=\star(e\wedge e)$；在这一约束面上，第一项变成

$$B_{ab}\wedge R^{ab}=\tfrac12\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd},$$

**即 Palatini 作用量**（$\epsilon$ 指标重排，见自检 4），而 $\lambda$ 项消失。于是

$$\boxed{\;\text{Plebański}\;=\;\text{BF}\;+\;\text{简单性约束}\;=\;\text{GR}\;}$$

> **文献注**：Plebański 的原始形式用自对偶（复）联络与写在 $B\wedge B$ 上的**二次**乘子；这里用实变量与线性乘子，约束面（非退化分支上 $B\propto\star(e\wedge e)$）相同。初读时不必纠缠这一层，抓住"BF 是拓扑的、约束把它变成 GR"即可。

### 6.3 为什么"约束不含导数"是全文的关键一句

变分曲率会产生边界项：$\delta R=D\delta\omega$，分部积分把导数挪到 $e\wedge e$ 上，留下一个边界项——这是第 10 章 GHY 项的来源。

而**简单性约束是代数的**：$B-\star(e\wedge e)$ 不含任何导数，变分它得到的是代数方程，**不需要分部积分，因此不产生边界项**。于是：

- 带边界的 Plebański 作用量的边界项与无约束情形**结构相同**；
- 边界数据（$e$ 在边界上的 pullback、$B$ 的 pullback）可以**原样**用于缝合两个区域；
- 同时理论里还带着 GR 的两个传播自由度（这是纯 BF 做不到的）。

论文 §1 把这句话作为整条路线的合法性依据：*"Since the constraint contains no derivatives, it adds no boundary term to variation of the bulk action. The same boundary variables can therefore be used for gluing, now with the two local propagating degrees of freedom of general relativity included."*

### 6.4 Holst 项（一句话）

还可以加一项 $\frac{1}{2\kappa\gamma}\int e_a\wedge e_b\wedge R^{ab}$（$\gamma$ 为 Barbero–Immirzi 参数）。在 $T=0$ 时它是闭形式（全导数），不改变经典方程；但它会改变量子化后的面积谱步长，是圈量子引力里 $\gamma$ 的来源。论文用实变量、不引入 $\gamma$。

## 7. 与论文的接口

| 论文位置 | 用到的本章内容 |
|---|---|
| §3.1 一阶引力 | Palatini 作用量；$e$ 与 $\omega$ 独立；$T=0$ 作为运动方程 |
| §1 图 1、App A.1 | 零锥上的 pullback：$B$ 的分量投影到 cut 上给出诱导标架 $E^A{}_\mu$ |
| (3.17) 诱导度规 | 简单性约束在 cut 上的解 $q_{AB}=\eta_{ab}E^a{}_AE^b{}_B$，"标架定出共形类" |
| §3.3 辛形式 | 用 $(e,\omega,B)$ 写预辛势；bulk 项在约束面上消去，只剩边界与角点 |
| §1 缝合论证 | §6.3 那句"约束不含导数 ⇒ 不加边界项" |

**一句话记住**：一阶形式不是"另一种写法"，它是"把标架变成物理数据"的唯一写法——而论文整套构造（引力时钟、边缘模、面积算子）都建立在这个"标架是物理的"之上。

## 8. 小结

- 标架 $e^a{}_\mu$（16 个分量，模局部 Lorentz 6 个 ⇒ 10 个）把度规"开了平方"，同时给出局部惯性系。
- 自旋联络 $\omega^{ab}{}_\mu$（24 个）独立；挠率 $T^a=De^a$、曲率 $R^{ab}=\mathrm{d}\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}$。
- Palatini 作用量 $\frac{1}{2\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}$：变分 $\omega$ ⇒ $T^a=0$（解出 $\omega(e)$），变分 $e$ ⇒ $\epsilon_{abcd}e^b\wedge R^{cd}=0$ ⇒ $G_{\mu\nu}=0$。
- 代回得 EH + 全导数：Palatini 与 EH 经典等价。
- Plebański = BF + 简单性约束 $B=\star(e\wedge e)$（36 → 16，20 个约束）；BF 拓扑、GR 有 2 个传播自由度。
- 简单性约束不含导数 ⇒ 不产生边界项 ⇒ 同一套边界变量可以缝合，且带上了 2 个传播自由度。

## 自检问题

**1.** 验证 $g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu$ 在局部 Lorentz 变换下不变，并给出标架的自由度计数。再说明：给定度规，标架的解空间为什么是 6 维的（每点）。

<details markdown="1"><summary>点击显示答案</summary>

局部 Lorentz 变换 $e'^a{}_\mu=\Lambda^a{}_b e^b{}_\mu$，$\Lambda^a{}_c\Lambda^b{}_d\eta_{ab}=\eta_{cd}$：

$$g'_{\mu\nu}=\eta_{ab}e'^a{}_\mu e'^b{}_\nu=\eta_{ab}\Lambda^a{}_c\Lambda^b{}_d e^c{}_\mu e^d{}_\nu=\eta_{cd}e^c{}_\mu e^d{}_\nu=g_{\mu\nu}.\qquad\square$$

**计数**：$e^a{}_\mu$ 有 16 个分量；局部 Lorentz 群 $SO(3,1)$ 有 6 维，且由上式它作用在标架上不改变任何可观测量。所以物理上独立的标架自由度 = $16-6=10$，与对称矩阵 $g_{\mu\nu}$ 的 10 个分量相同。

**每点 6 维**：给定 $g_{\mu\nu}$，要求 $e$ 满足 10 个方程（$g_{\mu\nu}=\eta_{ab}e^a{}_\mu e^b{}_\nu$ 是对称的）。16 个未知数减 10 个方程 = 6 维解空间，正是 $SO(3,1)$ 的维数。几何上：先用 Gram–Schmidt 在 $g$ 下取一组正交归一基，得到**一个**解；任意局部 Lorentz 变换给出其余全部解。$\square$

补充：这个 6 维"每点规范群"在无边界时是纯冗余；一旦有边界/角点，它的边界作用（boost 与转动）就不再是冗余，而是第 12 章的边缘模与荷。这是"标架比度规多出的东西"第一次变成物理。

</details>

**2.** 从 $\delta_\omega S_{\rm P}=0$ 推出挠率为零，并把"$T^a\wedge e^b-e^a\wedge T^b=0\Rightarrow T^a=0$"论证清楚。

<details markdown="1"><summary>点击显示答案</summary>

$$\delta_\omega S=\frac{1}{2\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge D\delta\omega^{cd}.$$

用分部积分（$D$ 是度量相容的，$\epsilon$ 协变常）：

$$\delta_\omega S=-\frac{1}{2\kappa}\int\epsilon_{abcd}D(e^a\wedge e^b)\wedge\delta\omega^{cd}+\frac{1}{2\kappa}\int\mathrm{d}\left(\epsilon_{abcd}e^a\wedge e^b\wedge\delta\omega^{cd}\right).$$

第二项是边界项，在变分中先搁置（第 10 章处理）。第一项对任意 $\delta\omega^{cd}$ 为零，给

$$\epsilon_{abcd}\left(T^a\wedge e^b-e^a\wedge T^b\right)=0 .$$

**第一步：两项相等。** $\epsilon_{abcd}$ 对 $a,b$ 反对称，把第二项里 $a\leftrightarrow b$ 重命名即得 $e^a\wedge T^b$ 的贡献与 $T^a\wedge e^b$ 相同。所以方程简化为

$$\boxed{\epsilon_{abcd}T^a\wedge e^b=0\quad\text{（对每个内部对 }cd\text{，这是一个 3-形式方程）}.}$$

**第二步：展开成标架分量。** 设 $T^a=\frac12T^a{}_{ef}e^e\wedge e^f$，并注意三个标架一形式的楔积是

$$e^e\wedge e^f\wedge e^b=\epsilon^{efb}{}_{g}\,e^g .$$

代入：

$$\epsilon_{abcd}\,T^a{}_{ef}\,\epsilon^{efb}{}_{g}=0
\qquad\text{对每个 }(c,d,g).$$

**第三步：取一组具体指标，看它如何逼出零。** 取 $(c,d,g)=(0,1,3)$。$\epsilon^{efb}{}_{3}\neq0$ 要求 $\{e,f,b\}=\{0,1,2\}$；$\epsilon_{ab01}\neq0$ 要求 $\{a,b\}=\{2,3\}$。两条件合起来给 $b=2$、$a=3$，而 $(e,f)$ 取 $(0,1)$ 或 $(1,0)$。于是

$$0=\epsilon_{3201}\left(\epsilon^{012}{}_{3}T^3{}_{01}+\epsilon^{102}{}_{3}T^3{}_{10}\right)
=(-1)\left(1\cdot T^3{}_{01}+(-1)\cdot(-T^3{}_{01})\right)=-2\,T^3{}_{01}.$$

（用了 $T^3{}_{10}=-T^3{}_{01}$。）故 $T^3{}_{01}=0$。把 $(c,d,g)$ 与剩余的指标轮换，同样得到每一个 $T^a{}_{ef}=0$。

$$\boxed{\;T^a{}_{ef}=0\quad\Longleftrightarrow\quad T^a=0.\;}$$

**要点**：这不是"对 $T$ 的全反对称部分为零"那种弱条件（那个条件只给 4 个方程，留下 20 个自由度），而是 24 个方程的满秩系统。**关键在于方程 $\epsilon_{abcd}T^a\wedge e^b=0$ 有三组自由指标 $(c,d,g)$，恰好对应 24 个分量。**

**为什么这是"解出 $\omega$"而不是"约束 $\omega$"**：$T^a=0$ 是 24 个代数方程（$\omega$ 的每个分量线性出现，$T^a=\mathrm{d}e^a+\omega^a{}_b\wedge e^b$ 关于 $\omega$ 是代数线性的），恰好解 24 个未知函数 $\omega^{ab}{}_\mu$。所以它唯一确定 $\omega=\omega(e)$，不是留下自由度的约束。$\square$

</details>

**3.** 从 $\delta_e S_{\rm P}=0$ 得到 $\epsilon_{abcd}e^b\wedge R^{cd}=0$，验证它与 $G_{\mu\nu}=0$ 等价（至少验证迹部分），并做自由度计数。

<details markdown="1"><summary>点击显示答案</summary>

$\delta e^a$ 出现两次（$e^a\wedge e^b$ 的两个位置），故

$$\delta_e S=\frac{1}{2\kappa}\int\epsilon_{abcd}\left(\delta e^a\wedge e^b\wedge R^{cd}+e^a\wedge\delta e^b\wedge R^{cd}\right)
=\frac{1}{\kappa}\int\epsilon_{abcd}\,\delta e^a\wedge e^b\wedge R^{cd},$$

第二个等号是把第二项里 $a\leftrightarrow b$ 重命名并用 $\epsilon_{bacd}=-\epsilon_{abcd}$。要求对任意 $\delta e^a$ 为零：

$$\boxed{\epsilon_{abcd}\,e^b\wedge R^{cd}=0.}$$

**迹部分**：与 $e^a$ 外乘并缩并：

$$0=e^a\wedge\epsilon_{abcd}e^b\wedge R^{cd}=\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}.$$

右边正是作用量被积式，所以这个方程说"被积式为零"。把 $R^{cd}=\frac12R^{cd}{}_{\mu\nu}\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu$ 与 $e^a\wedge e^b\wedge\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu$ 用 $\epsilon$ 恒等式展开，即得 $\sqrt{-g}R=0$，也就是 $R=0$——真空 Einstein 方程的迹。$\square$

**无迹部分**：把 $\epsilon_{abcd}e^b\wedge R^{cd}=0$ 写成张量形式，用"内部指标换成时空指标"的恒等式

$$\epsilon_{abcd}e^b{}_\mu R^{cd}{}_{\nu\rho}=0
\;\Longrightarrow\;
R_{\mu\nu\rho\sigma}+R_{\mu\rho\sigma\nu}+R_{\mu\sigma\nu\rho}=0\ \text{的某种缩并},$$

再用 $T=0$ 下的第二 Bianchi 恒等式 $R_{\mu[\nu\rho\sigma]}=0$，可把它化成 $R_{\mu\nu}-\frac12Rg_{\mu\nu}=0$。完整的指标推导较长；一个更快的检验是：在 $R=0$ 的前提下，上式与 $R_{\mu\nu}=0$ 的方程数都是 10，且两者都满足第二 Bianchi 恒等式给出的 4 个依赖关系，因此等价。

**计数**：$\epsilon_{abcd}e^b\wedge R^{cd}$ 是"内部指标 $a$ 的 4 个分量 × 时空 3-形式的 4 个分量"，共 $4\times4=16$ 个方程。作用量在局部 Lorentz 变换（6 个参数）下不变，给出 6 个恒等式（不是独立方程），故独立方程

$$16-6=10,$$

与度规变分得到的 10 个 Einstein 方程一致。$\square$

</details>

**4.** 验证：把 $B^{ab}=\star(e^a\wedge e^b)=\frac12\epsilon^{ab}{}_{cd}e^c\wedge e^d$ 代入 $\int B_{ab}\wedge R^{ab}$ 得到 Palatini 作用量 $\frac12\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}$。

<details markdown="1"><summary>点击显示答案</summary>

$$B_{ab}\wedge R^{ab}=\tfrac12\epsilon_{abcd}\,e^c\wedge e^d\wedge R^{ab}.$$

把哑指标重命名 $(c,d,a,b)\to(a,b,c,d)$：

$$\tfrac12\epsilon_{cdab}\,e^a\wedge e^b\wedge R^{cd}.$$

四阶全反对称张量在指标的偶置换下不变。置换 $cdab\to abcd$ 是把两块 $\{c,d\}$、$\{a,b\}$ 互换，等价于 $2\times2=4$ 次换位（偶置换），故

$$\epsilon_{cdab}=\epsilon_{abcd}.$$

于是

$$B_{ab}\wedge R^{ab}=\tfrac12\epsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd},$$

即 $\int B\wedge R=\frac12\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}$。与 $S_{\rm P}=\frac{1}{2\kappa}\int\epsilon_{abcd}e^a\wedge e^b\wedge R^{cd}$ 相比差一个因子 2 与 $\kappa$ 的约定——在 Plebański 作用量里把第一项的系数取成 $\frac{1}{\kappa}$（而不是 $\frac{1}{2\kappa}$）即可对齐。

**要点**：这里没有任何动力学，纯粹是 $\epsilon$ 的指标代数。它说明"简单性约束一旦解出，$B$ 就没有独立内容了"——$B$ 的全部作用是把 $e\wedge e$ 打包成一个二形式，好让作用量写成 $B\wedge R$ 这种"拓扑理论"的形状。$\square$

</details>

**5.** 解释为什么简单性约束不产生边界项，而 $\delta R$ 会产生；并说明这两件事对"缝合"分别意味着什么。（提示：看每一项里有没有导数。）

<details markdown="1"><summary>点击显示答案</summary>

**两个变分的结构对比。**

*曲率变分*：$R=\mathrm{d}\omega+\omega\wedge\omega$，所以 $\delta R=D_\omega\delta\omega$——$\delta R$ 里**含 $\delta\omega$ 的导数**。作用量里 $\int B\wedge\delta R$ 要分部积分才能把导数挪走，而分部积分必然留下一个边界项

$$\int_M\mathrm{d}\left(B\wedge\delta\omega\right)=\int_{\partial M}B\wedge\delta\omega .$$

这个边界项必须被另一个边界项抵消，否则变分原理在固定边界数据下不成立——这就是第 10 章 GHY 项与零边界项的来源。

*约束变分*：简单性约束是 $B^{ab}-\star(e^a\wedge e^b)=0$，两边都**不含导数**。变分它得到的是 $B$、$e$ 的代数关系，不需要分部积分，因此**不产生任何边界项**。

**对缝合的两点含义。**

1. **边界项的形式不变**：无论加不加 Plebański 约束，带边界作用量的边界项都是同一套（由 $\delta R$ 产生的那一项决定）。所以两个区域的边界项在公共边界上仍然按"法矢相反、定向相反"相消（第 10 章的自检 5）。若约束带导数，这个相消会被破坏，胶合就不等于时间演化。
2. **边界数据不加修改**：缝合时要匹配的边界变量是同一组 $(e|_{\partial},B|_{\partial})$。约束只是在这组变量上再切一刀（把 $B$ 与 $e$ 锁在一起），并不改变"哪些量需要在边界上连续"这件事。**于是同一套边界变量既能用于无约束的拓扑理论，也能用于带 2 个传播自由度的 GR。**

**一句话**：约束的"代数性"是它能与带边界变分原理相容的原因；这正是论文 §1 说"可以用同样的边界变量缝合，而现在带上了 GR 的两个传播自由度"的技术内容。$\square$

</details>

## 参考

- Wald《General Relativity》附录 E（标架、自旋联络与 Palatini 作用量的标准处理）。
- Carroll《Spacetime and Geometry》第 3 章（$\Gamma$ 与曲率的标架表述）；第 4 章（作用量与边界项）。
- Poisson《A Relativist's Toolkit》第 3 章（零超曲面上的标架分解，为第 8 章与论文 App A 做准备）。
- Baez & Muniain《Gauge Fields, Knots and Gravity》第 4 部分（BF 理论与 Plebański 形式的物理动机）。
- 论文 arXiv:2611.34924 §1、§3.1、App A.1（一阶引力在零锥上的具体用法）；第 4 章（微分形式）、第 5 章（EH 作用量）、第 10 章（边界项）、第 12 章（角点荷）。
