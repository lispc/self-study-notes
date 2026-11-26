# 微分形式与积分：作用量与守恒律的书写系统

> 路线图位置：第 1 部分（微分几何工具）· 第 4 章
> 前置知识：第 1 章（余矢量、张量）、第 2–3 章（联络、曲率、$\nabla$ 与 $\mathrm{d}$ 的区别）。
> 学习目标：会用反对称张量定义 $p$-形式并做外积、外微分；能说清 $\mathrm{d}$ 不需要联络、$\star$ 需要度规；会算 4 维洛伦兹号差下的 Hodge 对偶与 $\star\star$ 的符号；会用 Stokes 定理统一散度/旋度定理与守恒荷；能把 Maxwell 方程、Einstein–Hilbert 作用量与 Plebański 作用量写成形式语言。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$。$\epsilon_{\mu\nu\rho\sigma}$ 是**坐标无关的符号张量**（$\epsilon_{0123}=+1$），体积形式是 $\boldsymbol\epsilon=\sqrt{-g}\,\mathrm{d}x^0\wedge\cdots\wedge\mathrm{d}x^3$。楔积按 $\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu$ 的字典序。$p$-形式用粗体（$\boldsymbol\omega$）表示，分量用普通字母。

## 1. 一句话总结

**$p$-形式就是反对称的 $(0,p)$ 张量，好处是"外积 + 外微分"构成一套不依赖联络的代数，而"体积形式 + Hodge 对偶"提供积分与内积。** 外微分 $\mathrm{d}$ 只用流形结构（$d^2=0$ 是"边界无边界"的代数版），Hodge 对偶 $\star$ 用度规（所以 $\star\star$ 的符号带号差痕迹）。一个 Stokes 定理 $\int_M\mathrm{d}\boldsymbol\omega=\int_{\partial M}\boldsymbol\omega$ 包住了梯度/旋度/散度所有积分定理，而 Maxwell 方程被压成两行：$\mathrm{d}F=0$、$\mathrm{d}\star F=\star J$。第 5s 章的一阶引力与第 10 章的边界项，全部用这套语言写。

## 2. $p$-形式

### 2.1 定义

$p$-形式是**完全反对称**的 $(0,p)$ 张量：

$$\omega_{\mu_1\dots\mu_p}=\omega_{[\mu_1\dots\mu_p]} .$$

- 0-形式 = 光滑函数（1 个分量）；
- 1-形式 = 余矢量（4 个）；
- 2-形式 = 反对称 $(0,2)$（6 个）；
- 3-形式（4 个）；
- 4-形式（1 个）。

4 维里 $p$-形式的空间维数是 $\binom{4}{p}$：$1,4,6,4,1$。**$p$-形式与 $(4-p)$-形式同维**——这是 Hodge 对偶存在的代数基础。

### 2.2 基与分量

$$\boldsymbol\omega=\frac{1}{p!}\,\omega_{\mu_1\dots\mu_p}\,\mathrm{d}x^{\mu_1}\wedge\cdots\wedge\mathrm{d}x^{\mu_p},
\qquad
\mathrm{d}x^{\mu_1}\wedge\cdots\wedge\mathrm{d}x^{\mu_p}=\sum_{\sigma}\mathrm{sgn}(\sigma)\,\mathrm{d}x^{\sigma(\mu_1)}\otimes\cdots$$

（第二个式子是"反对称化"的定义，$\frac{1}{p!}$ 抵消重复计数。）于是 2-形式 $\boldsymbol F=\frac12F_{\mu\nu}\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu$，$F_{\mu\nu}=-F_{\nu\mu}$。

### 2.3 外积

$$\boxed{\;(\boldsymbol\alpha\wedge\boldsymbol\beta)_{\mu_1\dots\mu_{p+q}}
=\frac{(p+q)!}{p!\,q!}\,\alpha_{[\mu_1\dots\mu_p}\beta_{\mu_{p+1}\dots\mu_{p+q}]}\;}$$

**反交换律**：

$$\boxed{\;\boldsymbol\alpha\wedge\boldsymbol\beta=(-1)^{pq}\,\boldsymbol\beta\wedge\boldsymbol\alpha\;}$$

（$p$、$q$ 是两形式的阶数）。所以 1-形式之间反交换（$\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu=-\mathrm{d}x^\nu\wedge\mathrm{d}x^\mu$），而 2-形式与 2-形式交换（$(-1)^{2\cdot2}=+1$）。

**推论**：$\boldsymbol\omega\wedge\boldsymbol\omega=0$ 对**奇数阶**成立（因为 $(-1)^{p^2}=-1$ 当 $p$ 奇）；对偶数阶不成立。

## 3. 外微分

### 3.1 公理

$\mathrm{d}:\Omega^p\to\Omega^{p+1}$ 由三条唯一确定：

1. 对函数，$\mathrm{d}f$ 就是普通微分（1-形式）；
2. **Leibniz（分次）**：$\mathrm{d}(\boldsymbol\alpha\wedge\boldsymbol\beta)=\mathrm{d}\boldsymbol\alpha\wedge\boldsymbol\beta+(-1)^p\boldsymbol\alpha\wedge\mathrm{d}\boldsymbol\beta$；
3. $\mathrm{d}^2=0$。

坐标公式：

$$\boxed{\;(\mathrm{d}\boldsymbol\omega)_{\mu\mu_1\dots\mu_p}
=(p+1)\,\partial_{[\mu}\omega_{\mu_1\dots\mu_p]}\;}$$

即"反对称化的偏导数"。**注意：这里只有偏导数 $\partial$，没有 $\Gamma$。**

### 3.2 为什么 $\mathrm{d}$ 不需要联络

$\mathrm{d}$ 作用在反对称张量上时，联络的贡献自动抵消。以 1-形式为例：

$$(\mathrm{d}\boldsymbol\omega)_{\mu\nu}=\partial_\mu\omega_\nu-\partial_\nu\omega_\mu .$$

而协变化：

$$\nabla_\mu\omega_\nu-\nabla_\nu\omega_\mu
=\partial_\mu\omega_\nu-\Gamma^\rho{}_{\mu\nu}\omega_\rho-\partial_\nu\omega_\mu+\Gamma^\rho{}_{\nu\mu}\omega_\rho
=\partial_\mu\omega_\nu-\partial_\nu\omega_\mu,$$

对称的 $\Gamma^\rho{}_{\mu\nu}$ 项相消。**所以 $\mathrm{d}$ 是拓扑的（不需要度规、不需要联络），而 $\nabla$ 是几何的（需要两者）。** 这个区别是第 2 章"$\Gamma$ 非张量但 $\nabla$ 张量"的孪生事实。

### 3.3 $d^2=0$ 的含义

$$\mathrm{d}^2=0\;\Longleftrightarrow\;\partial_{[\mu}\partial_{\nu}\omega_{\rho]}=0\;\Longleftrightarrow\;\text{偏导数可交换}.$$

几何上：$d^2=0$ 对应"边界的边界为空"（$\partial\partial=0$）。第 3 章的第二 Bianchi 恒等式 $\nabla_{[\lambda}R_{\mu\nu]\rho\sigma}=0$ 也是它的"曲率版"。

## 4. 体积形式与积分

### 4.1 体积形式

$$\boxed{\;\boldsymbol\epsilon=\sqrt{-g}\,\mathrm{d}x^0\wedge\mathrm{d}x^1\wedge\mathrm{d}x^2\wedge\mathrm{d}x^3\;}$$

（$\sqrt{-g}=\sqrt{|\det g|}$。）它是唯一的（到常数倍）处处非零的 4-形式。**积分**定义为

$$\int_M\boldsymbol\omega=\int\mathrm{d}^4x\;\omega_{0123}\quad(\text{若 }\boldsymbol\omega=f\boldsymbol\epsilon\text{，则}=\int\sqrt{-g}f\,\mathrm{d}^4x).$$

**定向**：选 $\boldsymbol\epsilon$ 的一个符号就是选定向。$\mathrm{d}x^0\wedge\cdots$ 的次序固定了"未来指向"的约定。

### 4.2 Hodge 对偶

$$\boxed{\;(\star\boldsymbol\omega)_{\mu_1\dots\mu_{4-p}}
=\frac{1}{p!}\,\epsilon_{\mu_1\dots\mu_{4-p}\nu_1\dots\nu_p}\,\omega^{\nu_1\dots\nu_p}\;}$$

（指标用 $g$ 升降。）$\star$ 把 $p$-形式映到 $(4-p)$-形式，是"正交补"的代数版：$\star$ 把"沿某几个方向的反对称张量"翻译成"沿剩余方向的"。

**关键性质**（自检 2 验证）：

$$\boxed{\;\star\star\boldsymbol\omega=(-1)^{p(4-p)+1}\,\boldsymbol\omega\;}$$

4 维洛伦兹号差下逐阶列出：

| $p$ | $p(4-p)+1$ | $\star\star$ |
|---|---|---|
| 0 | 1 | $-1$ |
| 1 | 4 | $+1$ |
| 2 | 5 | $-1$ |
| 3 | 4 | $+1$ |
| 4 | 1 | $-1$ |

**$\star^2=-1$ on 2-forms 是洛伦兹号差的烙印**（欧氏 4 维是 $+1$）。它的物理后果：电磁对偶 $F\to\star F$ 满足 $\star^2=-1$，所以"自对偶"只能是复的（$F=\pm i\star F$）——这是第 5s 章 Plebański 形式用复变量的原因，也是瞬子/自对偶解的结构基础。

### 4.3 内积

$$\boldsymbol\alpha\wedge\star\boldsymbol\beta=\left\langle\boldsymbol\alpha,\boldsymbol\beta\right\rangle\boldsymbol\epsilon,
\qquad
\left\langle\boldsymbol\alpha,\boldsymbol\beta\right\rangle=\frac{1}{p!}\alpha_{\mu_1\dots\mu_p}\beta^{\mu_1\dots\mu_p}.$$

于是作用量里的 $\int F\wedge\star F$ 就是"$F$ 的模方积分"。

## 5. Stokes 定理

$$\boxed{\;\int_M\mathrm{d}\boldsymbol\omega=\int_{\partial M}\boldsymbol\omega\;}$$

（$\partial M$ 取诱导定向。）**一个公式包住所有**：

| 经典定理 | 形式语言 |
|---|---|
| 微积分基本定理 | 0-形式在区间上 |
| 梯度定理 | $\mathrm{d}f$ |
| Stokes（旋度） | 1-形式在曲面上 |
| Gauss（散度） | $\star$ 后的 2-形式在体积上 |

**无边界时**：$\partial M=\varnothing$ ⇒ $\int_M\mathrm{d}\boldsymbol\omega=0$。这条在变分里反复出现（第 10 章：边界项的来源就是"变分把 $\mathrm{d}$ 挪到边界上"）。

## 6. Maxwell 方程：两行

### 6.1 场强

$$A=A_\mu\mathrm{d}x^\mu,\qquad \boxed{\;F=\mathrm{d}A\;}$$

于是 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$，且

$$\mathrm{d}F=\mathrm{d}^2A=0\quad(\text{恒等式}).$$

**这就是 Bianchi 恒等式，不需要运动方程。**

### 6.2 方程

$$\boxed{\;\mathrm{d}F=0,\qquad \mathrm{d}\star F=\star J\;}$$

$J=J^\mu\partial_\mu$ 是电流（1-形式），$\star J$ 是 3-形式。**两行 = 四个方程**：

- $\mathrm{d}F=0$ ⇒ 空间部分 $\nabla\cdot B=0$，时间部分 $\partial_tB+\nabla\times E=0$；
- $\mathrm{d}\star F=\star J$ ⇒ 空间部分 $\nabla\cdot E=\rho$，时间部分 $\partial_tE-\nabla\times B=-J$。

（符号依 $F_{0i}=E_i$、$F_{ij}=\epsilon_{ijk}B_k$ 的约定；自检 3 验证前两个。）

### 6.3 为什么这是"对的"语言

1. **规范不变性自动**：$A\to A+\mathrm{d}\chi$ ⇒ $F$ 不变。
2. **Bianchi 是恒等式**：$\mathrm{d}F=0$ 不需要额外假设。
3. **电荷守恒自动**：$\mathrm{d}(\mathrm{d}\star F)=0$ ⇒ $\mathrm{d}\star J=0$ ⇒ $\partial_\mu J^\mu=0$。
4. **与几何解耦**：$\mathrm{d}$ 不需要度规，所以拓扑部分（磁单极、瞬时子）与度规无关；$\star$ 需要度规，所以动力学（能量）与度规有关。

**第 5s 章的接口**：一阶引力把 $\omega$ 当联络、$R=\mathrm{d}\omega+\omega\wedge\omega$ 当曲率，然后写 $B\wedge R$。**整套 Plebański 形式就是"把引力写成 BF 理论 + 约束"**，而 BF 理论正是"$\mathrm{d}$ + 楔积"的最简练习。第 10 章的 GHY 项则是 $\int\sqrt hK$ 的形式版：$\int_{\partial M}\boldsymbol\epsilon_{\partial}K$。

## 7. 作用量的形式语言

三个必认的写法：

$$S_{\rm EH}=\frac{1}{16\pi G_N}\int R\,\boldsymbol\epsilon,\qquad
S_{\rm Maxwell}=-\frac12\int F\wedge\star F,\qquad
S_{\rm BF}=\frac{1}{2\kappa}\int B_{ab}\wedge R^{ab}.$$

各自的"结构信息"：

- **EH**：$R\,\boldsymbol\epsilon$ 是 4-形式，积分不需要额外结构；变分产生边界项（第 10 章）。
- **Maxwell**：$F\wedge\star F$ 用到了 $\star$，所以需要度规；变换 $F\to\star F$ 是"对偶"。
- **BF**：完全不用 $\star$（只用 $\epsilon$），所以是**拓扑的**——这正是第 5s 章"BF 没有传播自由度"的形式版解释。

**一句话**：**用了 $\star$ 就有度规、就有动力学；只用 $\mathrm{d}$ 和 $\wedge$ 就是拓扑的。** 这句话能让你一眼判断一个作用量有没有局部自由度。

## 8. 小结

- $p$-形式 = 反对称 $(0,p)$ 张量；4 维维数 $1,4,6,4,1$；反交换 $\alpha\wedge\beta=(-1)^{pq}\beta\wedge\alpha$。
- $\mathrm{d}$ 用三条公理唯一确定：$\mathrm{d}f$、分次 Leibniz、$\mathrm{d}^2=0$；坐标公式是反对称化偏导，**不需要联络**。
- 体积形式 $\boldsymbol\epsilon=\sqrt{-g}\,\mathrm{d}^4x$；Hodge 对偶 $\star$ 需要度规；$\star\star=(-1)^{p(4-p)+1}$，2-形式上 $=-1$（洛伦兹号差）。
- Stokes $\int_M\mathrm{d}\omega=\int_{\partial M}\omega$ 统一全部积分定理；无边界时 $\int\mathrm{d}\omega=0$。
- Maxwell：$F=\mathrm{d}A$、$\mathrm{d}F=0$（恒等式）、$\mathrm{d}\star F=\star J$（动力学）；电荷守恒 $\mathrm{d}\star J=0$ 自动。
- 用 $\star$ ⇒ 有度规 ⇒ 有动力学；只用 $\mathrm{d},\wedge$ ⇒ 拓扑。BF 是后者，EH/Maxwell 是前者。
- 第 5s、10、12 章的作用量与边界项全部用这套语言；$\star^2=-1$ 是 Plebański 用复变量的根源。

## 自检问题

**1.** 证明 $\boldsymbol\alpha\wedge\boldsymbol\beta=(-1)^{pq}\boldsymbol\beta\wedge\boldsymbol\alpha$，并由此证明 $\mathrm{d}(\boldsymbol\omega\wedge\boldsymbol\eta)=\mathrm{d}\boldsymbol\omega\wedge\boldsymbol\eta+(-1)^p\boldsymbol\omega\wedge\mathrm{d}\boldsymbol\eta$ 与 $\mathrm{d}^2=0$。

<details markdown="1"><summary>点击显示答案</summary>

**反交换**：由定义

$$(\boldsymbol\alpha\wedge\boldsymbol\beta)_{\mu_1\dots\mu_{p+q}}=\frac{(p+q)!}{p!q!}\alpha_{[\mu_1\dots\mu_p}\beta_{\mu_{p+1}\dots\mu_{p+q}]}.$$

交换 $\alpha$ 与 $\beta$ 相当于把后 $q$ 个指标移到前面：这需要 $p\times q$ 次相邻交换（$\alpha$ 的每个指标要跨过 $\beta$ 的每个指标），每次交换给一个负号。所以

$$(\boldsymbol\beta\wedge\boldsymbol\alpha)_{\mu_1\dots}=(-1)^{pq}(\boldsymbol\alpha\wedge\boldsymbol\beta)_{\mu_1\dots}.\qquad\square$$

**Leibniz**：$\mathrm{d}$ 作用在 $\boldsymbol\omega\wedge\boldsymbol\eta$ 上，按定义是"反对称化 $\partial(\omega\eta)$"。$\partial$ 满足普通 Leibniz，但把一个导数穿过 $p$-形式 $\boldsymbol\omega$ 时要付 $(-1)^p$（因为 $\partial$ 是 1-形式，与 $p$-形式交换一次）。所以

$$\mathrm{d}(\boldsymbol\omega\wedge\boldsymbol\eta)=\mathrm{d}\boldsymbol\omega\wedge\boldsymbol\eta+(-1)^p\boldsymbol\omega\wedge\mathrm{d}\boldsymbol\eta .\qquad\square$$

**$d^2=0$**：对函数，$(\mathrm{d}^2f)_{\mu\nu}=2\partial_{[\mu}\partial_{\nu]}f=\partial_\mu\partial_\nu f-\partial_\nu\partial_\mu f=0$。对一般形式，用 Leibniz + 归纳：

$$\mathrm{d}^2(f\boldsymbol\omega)=\mathrm{d}\left(\mathrm{d}f\wedge\boldsymbol\omega+f\mathrm{d}\boldsymbol\omega\right)
=\mathrm{d}^2f\wedge\boldsymbol\omega-\mathrm{d}f\wedge\mathrm{d}\boldsymbol\omega+\mathrm{d}f\wedge\mathrm{d}\boldsymbol\omega+f\mathrm{d}^2\boldsymbol\omega=0 .$$

（第一项 $\mathrm{d}^2f=0$，中间两项相消，最后一项归纳为零。）$\square$

**要点**：$d^2=0$ 在坐标里就是"二阶偏导可交换"，但它的**几何意义**是 $\partial\partial=\varnothing$（边界的边界为空）。第 3 章的第二 Bianchi 恒等式、第 5s 章的"曲率是 $D^2$"都是同一个事实的不同化身。

</details>

**2.** 验证 $\star\star\boldsymbol\omega=(-1)^{p(4-p)+1}\boldsymbol\omega$，并显式算出 $\star\mathrm{d}x^0$ 与 $\star(\mathrm{d}x^0\wedge\mathrm{d}x^1)$，确认 $p=1$ 给 $+1$、$p=2$ 给 $-1$。

<details markdown="1"><summary>点击显示答案</summary>

**一般公式**：两次 $\star$ 之后，每个指标都被 $\epsilon$ 缩并两次。用 $\epsilon$ 的缩并恒等式（两个 $\epsilon$ 缩并 $k$ 个指标，给 $k!$ 个 $\delta$ 的全反对称组合；在洛伦兹号差下，每缩并一次全指标额外贡献一个 $-1$），直接代入定义可得

$$\star\star\boldsymbol\omega=(-1)^{p(4-p)+1}\,\boldsymbol\omega .\qquad\square$$

**指数的记忆法**：$p(4-p)$ 来自两次对偶的指标交换（$p$ 个指标各要与 $4-p$ 个"补齐"指标配对），$+1$ 来自号差（时间方向只有一个）。下面的两个具体例子把这个公式钉死。

**$p=1$**：$\star\mathrm{d}x^0$。$\omega_0=1$，$\omega^0=g^{00}=-1$。

$$(\star\boldsymbol\omega)_{\mu\nu\rho}=\epsilon_{\mu\nu\rho\sigma}\omega^\sigma
\;\Longrightarrow\;
(\star\boldsymbol\omega)_{123}=\epsilon_{1230}(-1)=-\epsilon_{1230}.$$

$\epsilon_{1230}$：$(1,2,3,0)\to(0,1,2,3)$ 需要 3 次交换 ⇒ 奇 ⇒ $\epsilon_{1230}=-1$。所以 $(\star\boldsymbol\omega)_{123}=+1$，即

$$\star\mathrm{d}x^0=\mathrm{d}x^1\wedge\mathrm{d}x^2\wedge\mathrm{d}x^3 .$$

再对偶一次：$\omega'=\mathrm{d}x^1\wedge\mathrm{d}x^2\wedge\mathrm{d}x^3$，$\omega'_{123}=1$，$\omega'^{123}=1$（空间部分号差正）。

$$(\star\boldsymbol\omega')_\mu=\frac{1}{3!}\epsilon_{\mu\nu\rho\sigma}\omega'^{\nu\rho\sigma}
\;\Longrightarrow\;
(\star\boldsymbol\omega')_0=\frac{1}{6}\cdot6\cdot\epsilon_{0123}\cdot1=+1 .$$

所以 $\star\star\mathrm{d}x^0=\mathrm{d}x^0$ ✓（$p=1$：$+1$）。

**$p=2$**：$\boldsymbol\omega=\mathrm{d}x^0\wedge\mathrm{d}x^1$，$\omega_{01}=1$，$\omega^{01}=g^{00}g^{11}\omega_{01}=(-1)(1)(1)=-1$。

$$(\star\boldsymbol\omega)_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}\omega^{\rho\sigma}
\;\Longrightarrow\;
(\star\boldsymbol\omega)_{23}=\tfrac12\left[\epsilon_{2301}\omega^{01}+\epsilon_{2310}\omega^{10}\right].$$

$\omega^{10}=-\omega^{01}=+1$；$\epsilon_{2301}$：$(2,3,0,1)\to(0,1,2,3)$，4 次交换 ⇒ 偶 ⇒ $+1$；$\epsilon_{2310}$：$(2,3,1,0)$，5 次 ⇒ 奇 ⇒ $-1$。故

$$(\star\boldsymbol\omega)_{23}=\tfrac12\left[1\cdot(-1)+(-1)\cdot1\right]=-1,$$

即 $\star(\mathrm{d}x^0\wedge\mathrm{d}x^1)=-\mathrm{d}x^2\wedge\mathrm{d}x^3$。

再对偶：$\omega'=-\mathrm{d}x^2\wedge\mathrm{d}x^3$，$\omega'_{23}=-1$，$\omega'^{23}=-1$，

$$(\star\boldsymbol\omega')_{01}=\tfrac12\left[\epsilon_{0123}(-1)+\epsilon_{0132}(1)\right]=\tfrac12\left[-1-1\right]=-1 .$$

所以 $\star\star(\mathrm{d}x^0\wedge\mathrm{d}x^1)=-\mathrm{d}x^0\wedge\mathrm{d}x^1$ ✓（$p=2$：$-1$）。$\square$

**物理含义**：$\star^2=-1$ 在 2-形式上意味着"电磁对偶转两次回到负自己"。所以自对偶条件只能是复的：$F=\pm i\star F$。第 5s 章的 Plebański 形式、瞬子解、以及论文里 $B=\star(e\wedge e)$ 的对偶结构，都建立在这个 $(-1)$ 上。（欧氏 4 维里 $\star^2=+1$，自对偶是实的——这是欧氏方法与洛伦兹方法的又一处本质差别。）

</details>

**3.** 把 Maxwell 方程写成 $\mathrm{d}F=0$、$\mathrm{d}\star F=\star J$，并验证：$\mathrm{d}F=0$ 的空间分量给 $\nabla\cdot B=0$，时间分量给 $\partial_tB+\nabla\times E=0$。

<details markdown="1"><summary>点击显示答案</summary>

**约定**：平直空间，$\epsilon_{0123}=1$，$F_{0i}=E_i$，$F_{ij}=\epsilon_{ijk}B_k$。

**$\mathrm{d}F=0$（三个指标全反对称化）**：

$$(\mathrm{d}F)_{\mu\nu\rho}=\partial_\mu F_{\nu\rho}+\partial_\nu F_{\rho\mu}+\partial_\rho F_{\mu\nu}=0 .$$

**空间分量** $(\mu\nu\rho)=(i,j,k)$：

$$\partial_iF_{jk}+\partial_jF_{ki}+\partial_kF_{ij}=0 .$$

代入 $F_{ij}=\epsilon_{ijl}B_l$：

$$\epsilon_{jkl}\partial_iB_l+\epsilon_{kil}\partial_jB_l+\epsilon_{ijl}\partial_kB_l=0 .$$

乘以 $\epsilon_{ijk}$ 并对 $i,j,k$ 求和。用 $\epsilon_{ijk}\epsilon_{jkl}=2\delta_{il}$ 型恒等式：

$$2\partial_iB_i+2\partial_jB_j+2\partial_kB_k=0
\;\Longrightarrow\;
\boxed{\nabla\cdot B=0 .}$$

（每一项缩并后都给同一个 $2\nabla\cdot B$。）

**时间分量** $(\mu\nu\rho)=(0,i,j)$：

$$\partial_0F_{ij}+\partial_iF_{j0}+\partial_jF_{0i}=0 .$$

代入 $F_{ij}=\epsilon_{ijk}B_k$、$F_{j0}=-F_{0j}=-E_j$：

$$\epsilon_{ijk}\partial_tB_k-\partial_iE_j+\partial_jE_i=0 .$$

两边乘 $\frac12\epsilon_{ijl}$ 并对 $i,j$ 求和：

- 第一项：$\frac12\epsilon_{ijl}\epsilon_{ijk}\partial_tB_k=\frac12\cdot2\delta_{lk}\partial_tB_k=\partial_tB_l$；
- 第二项：$-\frac12\epsilon_{ijl}\partial_iE_j=-\frac12(\nabla\times E)_l$；
- 第三项：$+\frac12\epsilon_{ijl}\partial_jE_i$，交换哑指标 $i\leftrightarrow j$ 得 $-\frac12\epsilon_{ijl}\partial_iE_j=-\frac12(\nabla\times E)_l$。

合计

$$\partial_tB_l-(\nabla\times E)_l=0
\;\Longrightarrow\;
\boxed{\partial_tB+\nabla\times E=0 .}\qquad\square$$

**对照**：这就是 Faraday 定律的"无源"形式（没有磁流）。如果允许磁单极，右边会多一项——而 $\mathrm{d}F=0$ 是**恒等式**（因为 $F=\mathrm{d}A$），所以在这个框架里磁单极必须由"$F$ 不是整体 $\mathrm{d}A$"（狄拉克弦 / 非平凡拓扑）来实现，不能简单地写在右边。这是形式语言的一个"预言"：**$\mathrm{d}F=0$ 的地位与 $\mathrm{d}\star F=\star J$ 不同**——前者是几何恒等式，后者是动力学。

**$\mathrm{d}\star F=\star J$ 一侧**（对应 Gauss 与 Ampère）：空间分量给 $\nabla\cdot E=\rho$，时间分量给 $\partial_tE-\nabla\times B=-J$（在自然单位与高斯制下的形式）。自检不必再算一遍，但要记住：**两行方程地位不对等**，一行恒等、一行动力学，这个不对称在非阿贝尔理论与引力里都会以"Bianchi vs 运动方程"的形式重现。

</details>

**4.** 用 Stokes 定理与 $\mathrm{d}\star F=0$（真空）推出：穿过闭合二维曲面 $S$ 的电通量守恒，即电荷 $Q=\frac{1}{4\pi}\oint_S\star F$ 与曲面的选取无关（只要同调）。

<details markdown="1"><summary>点击显示答案</summary>

**真空方程**：$\mathrm{d}\star F=0$。

**两个同调的曲面**：设 $S_1,S_2$ 包围同一个体积 $V$（$\partial V=S_1\cup S_2$，定向相反）。则

$$\int_{S_1}\star F-\int_{S_2}\star F=\int_{\partial V}\star F=\int_V\mathrm{d}\star F=0 .$$

所以 $\oint_{S_1}\star F=\oint_{S_2}\star F$——**通量与曲面无关**。$\square$

**这是"守恒荷"的模板**。一般的模式是：

1. 有一个闭形式 $\boldsymbol J$（$\mathrm{d}\boldsymbol J=0$）；
2. 定义 $Q(\Sigma)=\int_\Sigma\boldsymbol J$（$\Sigma$ 是余维 1 的闭曲面）；
3. Stokes 给"$\Sigma$ 连续变形时 $Q$ 不变"；
4. 若 $\Sigma$ 穿过一个"源"（$\mathrm{d}\boldsymbol J\neq0$ 的区域），$Q$ 跳变——跳变量就是源。

**引力的版本**（第 12 章）：$\boldsymbol Q_\xi$ 是闭的（在解空间上），所以 $\oint_S\boldsymbol Q_\xi$ 与 $S$ 的选取无关；对 Killing 矢量 $\xi$，这个荷是质量/角动量；对 boost，它是面积。**同一个 Stokes 定理，三种物理。**

**注意"同调"这个条件**：$S_1$ 与 $S_2$ 必须围出同一个体积。如果时空有"洞"（例如去掉奇点），绕洞的曲面不能缩成一点，此时 $\oint$ 可以不为零——这正是黑洞荷（电荷、质量）能在无穷远测到的原因：**荷是"未被 $\mathrm{d}$ 消掉的部分"的拓扑读数**。

**一个细节**：$\star F$ 是 2-形式，$\oint_S\star F$ 是 2 维积分；在 4 维里 $S$ 是余维 2，所以这是"高斯面"的维度。$\mathrm{d}\star F=0$ 是 3-形式方程（4 个分量），对应"电荷守恒"的连续性方程。这两句话的维度对得上：$\mathrm{d}$ 把 2-形式变成 3-形式，Stokes 把它变成 2 维边界上的积分。

</details>

**5.** 在静态球对称度规 $\mathrm{d}s^2=-f(r)\mathrm{d}t^2+h(r)\mathrm{d}r^2+r^2\mathrm{d}\Omega^2$ 下，算出 $\star(\mathrm{d}t\wedge\mathrm{d}r)$ 与 $\star\mathrm{d}t$；再在 Schwarzschild（$f=1/h=1-2G_NM/r$）下给出显式结果，并说明它们在 Komar 荷与零锥几何里的用途。

<details markdown="1"><summary>点击显示答案</summary>

**度规**：$g_{tt}=-f$，$g_{rr}=h$，$g_{\theta\theta}=r^2$，$g_{\phi\phi}=r^2\sin^2\theta$；$\sqrt{-g}=\sqrt{fh}\,r^2\sin\theta$。

**$\star(\mathrm{d}t\wedge\mathrm{d}r)$**：$\omega_{tr}=1$，$\omega^{tr}=g^{tt}g^{rr}\omega_{tr}=(-f^{-1})(h^{-1})=-\frac{1}{fh}$。$\omega^{rt}=+\frac{1}{fh}$。

$$(\star\omega)_{\theta\phi}=\tfrac12\left[\epsilon_{\theta\phi tr}\omega^{tr}+\epsilon_{\theta\phi rt}\omega^{rt}\right].$$

$\epsilon_{\theta\phi tr}=\sqrt{-g}$（$(3,4,1,2)$ 是偶置换）；$\epsilon_{\theta\phi rt}=-\sqrt{-g}$。所以

$$(\star\omega)_{\theta\phi}=\tfrac12\left[\sqrt{-g}\left(-\tfrac{1}{fh}\right)+(-\sqrt{-g})\left(\tfrac{1}{fh}\right)\right]
=-\frac{\sqrt{-g}}{fh}.$$

用 $\sqrt{-g}=\sqrt{fh}\,r^2\sin\theta$：

$$\boxed{\;\star(\mathrm{d}t\wedge\mathrm{d}r)=-\frac{r^2\sin\theta}{\sqrt{fh}}\,\mathrm{d}\theta\wedge\mathrm{d}\phi
=-\frac{r^2}{\sqrt{fh}}\,\mathrm{d}\Omega\;}$$

（$\mathrm{d}\Omega=\sin\theta\,\mathrm{d}\theta\wedge\mathrm{d}\phi$ 是单位球的面积 2-形式。）

**$\star\mathrm{d}t$**：$\omega_t=1$，$\omega^t=g^{tt}=-f^{-1}$。

$$(\star\omega)_{\mu\nu\rho}=\epsilon_{\mu\nu\rho\sigma}\omega^\sigma
\;\Longrightarrow\;
(\star\omega)_{r\theta\phi}=\epsilon_{r\theta\phi t}\left(-f^{-1}\right).$$

$\epsilon_{r\theta\phi t}$：指标排列是 $(r,\theta,\phi,t)=(2,3,4,1)$，逆序数 $3$（2、3、4 都大于 1）⇒ 奇置换 ⇒ $\epsilon_{r\theta\phi t}=-\sqrt{-g}$。故

$$\boxed{\;\star\mathrm{d}t=\frac{\sqrt{-g}}{f}\,\mathrm{d}r\wedge\mathrm{d}\theta\wedge\mathrm{d}\phi
=\frac{\sqrt{fh}}{f}\,r^2\sin\theta\,\mathrm{d}r\wedge\mathrm{d}\theta\wedge\mathrm{d}\phi\;}$$

**Schwarzschild**（$f=1-2G_NM/r$，$h=1/f$，$\sqrt{fh}=1$）：

$$\star(\mathrm{d}t\wedge\mathrm{d}r)=-r^2\mathrm{d}\Omega,\qquad
\star\mathrm{d}t=\frac{r^2}{f}\sin\theta\,\mathrm{d}r\wedge\mathrm{d}\theta\wedge\mathrm{d}\phi .$$

**用途一：Komar 荷**。第 12 章要算 $\star\,\mathrm{d}\xi$，$\xi=\partial_t$（即 $\xi_t=-f$）：

$$\mathrm{d}\xi=\mathrm{d}(-f\mathrm{d}t)=-f'\,\mathrm{d}r\wedge\mathrm{d}t=f'\,\mathrm{d}t\wedge\mathrm{d}r,$$

$$\star\,\mathrm{d}\xi=f'\,\star(\mathrm{d}t\wedge\mathrm{d}r)=-\frac{f'r^2}{\sqrt{fh}}\mathrm{d}\Omega
\;\xrightarrow{\ \text{Schwarzschild}\ }\;-\frac{2G_NM}{r^2}r^2\mathrm{d}\Omega=-2G_NM\,\mathrm{d}\Omega .$$

于是 $\oint_{S^2}\star\,\mathrm{d}\xi=-8\pi G_NM$，而

$$M_{\rm Komar}=-\frac{1}{8\pi G_N}\oint_{S^2}\star\,\mathrm{d}\xi=M .\qquad\square$$

**这条计算是"怎么从几何里读出质量"的标准流程**：写下 $\xi$、算 $\mathrm{d}\xi$、对偶、在球面上积分。第 12 章的 Wald 熵是同一流程的"视界版"。

**用途二：零锥几何**。第 8 章的零法矢 $\ell=\mathrm{d}u$（$u=t-r_*$）是 1-形式，它的对偶 $\star\mathrm{d}u$ 是 3-形式，给出零超曲面上的"体元"；$\ell\wedge\star\ell$ 型组合在 $\int\sqrt q\,\Theta$ 里出现。**零超曲面的"面积元" $r^2\mathrm{d}\Omega$ 正是 $\star(\mathrm{d}t\wedge\mathrm{d}r)$ 的球面部分**——这就是为什么第 8 章可以直接用 $r^2\mathrm{d}\Omega$ 当下标。

**用途三：Hodge 对偶给出"3+1 分解"的形式语言**。$\star\mathrm{d}t$ 是 3-形式，正好对应"空间体积元"；它在 ADM 分解（第 11 章）里就是 $\sqrt h\,\mathrm{d}^3x$ 的角色。**$\star$ 把"时间方向"翻译成"空间体积"，这就是对偶的几何意义。**

</details>

## 参考

- Wald《General Relativity》附录 B（微分形式、体积形式、Hodge 对偶、Stokes；号差约定的标准参考）。
- Carroll《Spacetime and Geometry》第 2 章（形式的入门）、附录（Hodge 对偶的符号）。
- Nakahara《Geometry, Topology and Physics》第 5 章（形式的严格处理与 de Rham 上同调，选读）。
- Baez & Muniain《Gauge Fields, Knots and Gravity》第 2 部分（用形式语言写 Yang–Mills 与 BF）。
- [电动力学书](../../electrodynamics/README.md)（Maxwell 的高斯制与协变形式）；第 5s 章（Plebański 的 $B\wedge R$）、第 10 章（GHY 与零边界项）、第 12 章（Komar/Wald 荷）。
