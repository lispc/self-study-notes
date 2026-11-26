# Einstein 方程与 Einstein–Hilbert 作用量

> 路线图位置：第 2 部分（动力学与解）· 第 5 章
> 前置知识：第 1–4 章（张量、联络、曲率、形式与积分）；[理论力学书第 5–6 章](../../classical-mechanics/docs/05-least-action-principle.md)（作用量与 Noether 定理）。
> 学习目标：能说清"为什么左边必须是 $G_{\mu\nu}$"（二阶、对称、恒无散、4 维唯一）；会从 EH 作用量变分得到场方程并解释 $8\pi G$ 的来源；会算理想流体的 $T_{\mu\nu}$ 与其守恒给出的连续性方程 + Euler 方程；会用弱场极限复现 $\nabla^2\Phi=4\pi G_N\rho$；理解 10 个方程中 4 个是约束（与第 11 章的 ADM 计数对上）。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。曲率约定同第 3 章：$2\nabla_{[\rho}\nabla_{\sigma]}v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu$，$R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}$。记 $\kappa\equiv 8\pi G_N$。

## 1. 一句话总结

**Einstein 方程 $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 不是猜出来的：在 4 维里，唯一由度规及其不超过二阶的导数构成、对称、且恒等地无散的张量就是 $G_{\mu\nu}$，再加一项 $\Lambda g_{\mu\nu}$。** "恒无散"由第二 Bianchi 恒等式保证，且它恰好与物质的能量守恒 $\nabla^\mu T_{\mu\nu}=0$ 对上；$8\pi G_N$ 由牛顿极限定标；$\Lambda$ 是唯一允许的额外项（也可看作积分常数）。作用量版本是 $S_{\rm EH}=\frac{1}{16\pi G_N}\int\sqrt{-g}(R-2\Lambda)$——变分产生边界项，必须补 GHY 项（第 10 章），补完之后才给出场方程。

## 2. 为什么左边必须是 $G_{\mu\nu}$

### 2.1 四条要求

要找"引力的场方程"，左边应满足：

1. **由 $g_{\mu\nu}$ 及其不超过二阶的导数构成**（否则初值问题需要超过两组初值数据，与 Newton 引力不符）。
2. **对称**（$T_{\mu\nu}$ 对称）。
3. **恒等地无散**：$\nabla^\mu(\text{左边})=0$，因为 $\nabla^\mu T_{\mu\nu}=0$ 是物质的运动方程，不能靠调引力一边来"凑"。
4. **4 维中唯一**（到两个常数）。

### 2.2 候选与排除

按"含 $R$ 的个数"分类：

| 候选 | 二阶导 | 对称 | 无散 | 4 维唯一？ |
|---|---|---|---|---|
| $g_{\mu\nu}$ | 0 阶 | ✓ | ✓ | 可作为 $\Lambda$ 项 |
| $R_{\mu\nu}$ | 2 阶 | ✓ | ✗（$\nabla^\mu R_{\mu\nu}=\frac12\nabla_\nu R$） | — |
| $Rg_{\mu\nu}$ | 2 阶 | ✓ | ✗ | — |
| $R_{\mu\nu}-\frac12Rg_{\mu\nu}$ | 2 阶 | ✓ | ✓ | **✓** |
| $R^2g_{\mu\nu}$、$R_{\mu\alpha\nu\beta}R^{\alpha\beta}$ 等 | 4 阶 | ✓ | 视组合 | 属于"高阶修正"，不在 Einstein 理论里 |

**唯一的组合**就是 $G_{\mu\nu}=R_{\mu\nu}-\frac12Rg_{\mu\nu}$（系数由 $\nabla^\mu G_{\mu\nu}=0$ 定死，第 3 章自检 3 证过），加 $\Lambda g_{\mu\nu}$。这就是**Lovelock 定理**在 4 维、二阶的特例。

### 2.3 与守恒的一致性

$$\nabla^\mu G_{\mu\nu}=0\;\Longleftrightarrow\;\nabla^\mu T_{\mu\nu}=0 .$$

**这不是巧合，是设计**：Einstein 方程把"几何的 Bianchi 恒等式"与"物质的守恒律"等同起来。于是：

- **物质的守恒不是额外假设**，而是场方程的自动推论；
- **反过来**，如果某种物质的 $\nabla^\mu T_{\mu\nu}\neq0$（例如与额外维度交换能量），Einstein 方程就必须修改。

**一个常被问到的问题**：$\nabla^\mu T_{\mu\nu}=0$ 到底是"运动方程"还是"守恒律"？答案是**两者是同一件事**：对物质场，$\nabla^\mu T_{\mu\nu}=0$ 就是它的 Euler–Lagrange 方程（的自洽条件）；对引力，它是 $G_{\mu\nu}$ 的无散性。Einstein 方程把两者绑在一起，所以"物质怎么运动"和"时空怎么弯曲"是同一个方程的两面。

## 3. 能动张量

### 3.1 定义

$$T_{\mu\nu}\equiv-\frac{2}{\sqrt{-g}}\frac{\delta S_{\rm matter}}{\delta g^{\mu\nu}}
\qquad\left(\text{等价地 }T^{\mu\nu}=\frac{2}{\sqrt{-g}}\frac{\delta S_{\rm matter}}{\delta g_{\mu\nu}}\right).$$

**性质**：对称（因为 $g^{\mu\nu}$ 对称）、$\nabla^\mu T_{\mu\nu}=0$（若 $S_m$ 在微分同胚下不变——这是 Noether 定理的场论版，见[理论力学书第 6 章](../../classical-mechanics/docs/06-noether-theorem.md)的场论部分）。

### 3.2 理想流体

$$T^{\mu\nu}=(\rho+p)u^\mu u^\nu+p\,g^{\mu\nu},\qquad u^\mu u_\mu=-1 .$$

**物理读法**（在流体静止系 $u^\mu=(1,\vec0)$）：

$$T^{00}=\rho\ (\text{能量密度}),\qquad T^{ij}=p\,\delta^{ij}\ (\text{各向同性压强}).$$

### 3.3 守恒给出的两个方程

把 $\nabla_\mu T^{\mu\nu}=0$ 分别沿 $u$ 与横向投影（自检 2）。

**沿 $u$ 投影**（能量守恒）：

$$\boxed{\;\nabla_\mu\left(\rho u^\mu\right)+p\,\nabla_\mu u^\mu=0\;}$$

**横向投影**（Euler 方程）：

$$\boxed{\;(\rho+p)\,a^\mu=-\left(g^{\mu\nu}+u^\mu u^\nu\right)\nabla_\nu p,\qquad a^\mu\equiv u^\nu\nabla_\nu u^\mu\;}$$

**两句话**：

- 第一个说"能量密度随流动的变化 + 压强做的功 = 0"；
- 第二个说"流体元的加速度由压强的横向梯度驱动"——**压强梯度是力，能量密度 + 压强是惯性**（这就是为什么相对论里 $p$ 也"有重量"）。

### 3.4 真空与 $\Lambda$

- 真空：$T_{\mu\nu}=0$ ⇒ $G_{\mu\nu}=0$。
- 宇宙学常数作为"真空能"：$T^{\rm vac}_{\mu\nu}=-\frac{\Lambda}{8\pi G_N}g_{\mu\nu}$，代入 $G_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 得 $G_{\mu\nu}+\Lambda g_{\mu\nu}=0$ ✓。**所以"$\Lambda$ 在左边还是右边"只是记账方式**：左边是几何项，右边是真空能。

## 4. Einstein–Hilbert 作用量

### 4.1 作用量

$$\boxed{\;S=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\left(R-2\Lambda\right)\mathrm{d}^4x
+S_{\rm GHY}+S_{\rm matter}\;}$$

$S_{\rm GHY}$ 是边界项（第 10 章）；没有它，变分原理在固定边界度规时不成立。

### 4.2 变分

$$\delta S_{\rm EH}=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\left(G_{\mu\nu}+\Lambda g_{\mu\nu}\right)\delta g^{\mu\nu}\,\mathrm{d}^4x
+\frac{1}{16\pi G_N}\int_{\partial M}\sqrt h\,n_\mu v^\mu ,$$

其中 $v^\mu=g^{\alpha\beta}\delta\Gamma^\mu_{\alpha\beta}-g^{\mu\alpha}\delta\Gamma^\beta_{\alpha\beta}$（Palatini 恒等式）。第 10 章证明

$$n_\mu v^\mu=-2\delta K,$$

所以 $S_{\rm GHY}=\frac{1}{8\pi G_N}\int_{\partial M}\sqrt h\,K$ 恰好抵消边界项。加上物质：

$$\delta\left(S_{\rm EH}+S_{\rm GHY}+S_m\right)=0
\;\Longrightarrow\;
\frac{1}{16\pi G_N}\sqrt{-g}\left(G_{\mu\nu}+\Lambda g_{\mu\nu}\right)-\frac12\sqrt{-g}\,T_{\mu\nu}=0,$$

$$\boxed{\;G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G_N\,T_{\mu\nu}.\;}$$

**三个检验**：

1. **取迹**：$-R+4\Lambda=8\pi G_NT$ ⇒ $R=4\Lambda-8\pi G_NT$。真空（$T=0$）：$R=4\Lambda$，代回得 $R_{\mu\nu}=\Lambda g_{\mu\nu}$ ✓（第 3 章 §4.3）。
2. **真空 + $\Lambda=0$**：$R_{\mu\nu}=0$ ✓。
3. **系数 $8\pi G_N$**：由牛顿极限定（§5）。

### 4.3 为什么是 $R$ 而不是别的标量

- $R$ 是唯一由 $g$ 的二阶导数线性构成的标量（到全导数）。
- 加 $R^2$、$R_{\mu\nu}R^{\mu\nu}$、$R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ 会给四阶方程（额外自由度、鬼），属于"高阶引力"（Starobinsky、Gauss–Bonnet 等），不在本章范围。
- 加 $\Lambda$ 是零阶项，允许。

**与 QFT 的接口**：$R^2$ 项在单圈有效作用量里会自动出现（[QFT 书第 9 阶段 01 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/01-qft-curved-spacetime-semiclassical.md)），所以"Einstein 理论是低能有效理论"这句话的技术内容是：**高阶项被 $\hbar$（或 $1/M_{\rm Pl}^2$）压低**。

## 5. 弱场极限与 Newton

### 5.1 弱场展开

$$g_{\mu\nu}=\eta_{\mu\nu}+h_{\mu\nu},\qquad |h|\ll1 .$$

静态、低速物质：$T_{00}=\rho$，$T_{ij}\approx0$，$T\approx-\rho$。取

$$g_{00}=-(1+2\Phi),\qquad g_{ij}=(1-2\Phi)\delta_{ij}$$

（各向同性坐标下的弱场形式；$g_{ij}$ 的部分对 $R_{00}$ 的领头阶无贡献）。

### 5.2 算 $R_{00}$

$$\Gamma^i_{00}=\tfrac12g^{ij}\left(2\partial_0g_{j0}-\partial_jg_{00}\right)
=\tfrac12\delta^{ij}\left(0+2\partial_j\Phi\right)=\partial_i\Phi .$$

$$R_{00}\approx\partial_i\Gamma^i_{00}-\partial_0\Gamma^i_{i0}+\Gamma\Gamma-\Gamma\Gamma
\approx\partial_i\partial_i\Phi=\nabla^2\Phi .$$

（静态 ⇒ $\partial_0=0$；一阶 ⇒ 丢 $\Gamma\Gamma$。）

### 5.3 用场方程的"迹反转"形式

$$R_{\mu\nu}=8\pi G_N\left(T_{\mu\nu}-\tfrac12Tg_{\mu\nu}\right).$$

$00$ 分量：

$$R_{00}=8\pi G_N\left(T_{00}-\tfrac12Tg_{00}\right)
=8\pi G_N\left(\rho-\tfrac12(-\rho)(-1)\right)
=8\pi G_N\left(\rho-\tfrac12\rho\right)=4\pi G_N\rho .$$

所以

$$\boxed{\;\nabla^2\Phi=4\pi G_N\rho\;}$$

**这就是 Newton 的 Poisson 方程**，也是 $8\pi G_N$ 的定标来源。

**注意一个常见的错误**：直接用 $R_{00}=8\pi G_NT_{00}$ 会得到 $\nabla^2\Phi=8\pi G_N\rho$，差因子 2。**错在忽略了 $-\frac12Tg_{00}$ 这一项**——它是"压强也产生引力"的相对论效应在静态极限的残余。用 $G_{00}$ 算也一样：$G_{00}=\nabla^2\Phi+4\pi G_N\rho=8\pi G_N\rho$ ⇒ 同样的结果（第 5 章 §2 的计数里已经埋下这个"$\frac12$"）。

### 5.4 运动方程

测地线方程在弱场、低速下给

$$\frac{\mathrm{d}^2x^i}{\mathrm{d}t^2}=-\Gamma^i_{00}=-\partial_i\Phi ,$$

即 $\ddot{\vec x}=-\nabla\Phi$ ✓。

**两件事合起来**：$\nabla^2\Phi=4\pi G_N\rho$（场方程）+ $\ddot{\vec x}=-\nabla\Phi$（测地线）= 完整的 Newton 引力。**所以广义相对论在弱场低速下自动退回 Newton，且不需要额外假设。**

## 6. 宇宙学常数

### 6.1 三种身份

1. **几何项**：$G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 里的常数。
2. **真空能**：$T^{\rm vac}_{\mu\nu}=-\frac{\Lambda}{8\pi G_N}g_{\mu\nu}$，$\rho_{\rm vac}=\frac{\Lambda}{8\pi G_N}$，$p_{\rm vac}=-\rho_{\rm vac}$（负压强）。
3. **积分常数**：在"迹-free"形式 $R_{\mu\nu}-\frac14Rg_{\mu\nu}=8\pi G_N(T_{\mu\nu}-\frac14Tg_{\mu\nu})$ 里，$R$ 的常数部分不被约束，可以是任意常数——这就是"$\Lambda$ 是积分常数"的说法。

**三种说法等价**，选哪个看语境。论文 (3.19) 用 $R_{ab}=\Lambda g_{ab}$，是第一种的真空形式。

### 6.2 两个解

- **de Sitter**：$\Lambda>0$、真空、最大对称，$R_{\mu\nu}=\Lambda g_{\mu\nu}$，视界半径 $\sqrt{3/\Lambda}$。
- **Schwarzschild–de Sitter**：$f=1-2G_NM/r-\Lambda r^2/3$，两个视界（黑洞视界 + 宇宙学视界）。

**与第 8 章的接口**：de Sitter 的宇宙学视界也是零超曲面，"面积 $\leftrightarrow$ 熵"的关系同样成立（Gibbons–Hawking）。论文的因果菱形方法原则上适用于任何 $\Lambda$，但正文取 $\Lambda=0$ 以避免额外尺度。

## 7. 初值问题的结构：10 = 6 + 4

$G_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 是 10 个方程。但

$$\nabla^\mu G_{\mu\nu}=0\quad(\text{4 个 Bianchi 恒等式})$$

意味着**其中 4 个不含对时间的二阶导数**——它们是**约束**，只限制初值，不演化。

| 类别 | 个数 | 作用 |
|---|---|---|
| 约束（Hamiltonian + momentum） | 4 | 限制 $h_{ij}$ 与 $K_{ij}$ 的初值 |
| 演化方程 | 6 | 决定 $\partial_t h_{ij}$、$\partial_tK_{ij}$ |
| 规范自由度（坐标选择） | 4 | 可消去 4 个变量 |

**计数对账**：

- ADM 相空间：$h_{ij}$（6）+ $K_{ij}$（6）= 12 维；
- 4 个第一类约束 ⇒ 每个消去 2 维 ⇒ $12-8=4$ 维；
- 4 维 = 2 个场分量 × 2（坐标 + 动量）= **2 个偏振** ✓。

**这 2 个偏振就是引力波。** 第 5s 章的"Plebański 带 2 个传播自由度"、论文的"4 维之所以有限维是因为有传播自由度"（[论文阅读首篇](../../paper-reading/docs/01-null-cone-quantum-gravity.md) §6），说的都是这个 2。

**与第 11 章的接口**：ADM 形式把这套计数显式化；Dirac 约束理论（[理论力学书第 12 章](../../classical-mechanics/docs/12-constraints-dirac-theory.md)）给出"第一类约束消去 2 维"的一般规则；零锥路线（第 8 章、论文 §3）则把这 4 个约束**解掉**而不是保留。

## 8. 小结

- $G_{\mu\nu}$ 是 4 维里唯一二阶、对称、恒无散张量（Lovelock）；$\Lambda g_{\mu\nu}$ 是唯一允许的额外项。
- $\nabla^\mu G_{\mu\nu}=0$ 与 $\nabla^\mu T_{\mu\nu}=0$ 的一致性使"物质守恒"成为场方程的推论。
- $T_{\mu\nu}=-\frac{2}{\sqrt{-g}}\delta S_m/\delta g^{\mu\nu}$；理想流体 $(\rho+p)u^\mu u^\nu+pg^{\mu\nu}$；守恒给连续性方程 + Euler 方程。
- $S_{\rm EH}=\frac{1}{16\pi G}\int\sqrt{-g}(R-2\Lambda)+S_{\rm GHY}+S_m$；变分（含 GHY 抵消）给 $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G_NT_{\mu\nu}$。
- 弱场：$R_{00}=\nabla^2\Phi$，$R_{\mu\nu}=8\pi G(T_{\mu\nu}-\frac12Tg_{\mu\nu})$ ⇒ $\nabla^2\Phi=4\pi G_N\rho$；测地线给 $\ddot x=-\nabla\Phi$。
- $\Lambda$ 可以是几何项、真空能、或积分常数；三种说法等价。
- 10 个方程 = 6 演化 + 4 约束；ADM 相空间 12 维 − 4×2 = 4 维 = 2 个偏振。
- 高阶曲率项属于有效理论的修正，被 $\hbar$ 压低。

## 自检问题

**1.** 用 $\nabla^\mu G_{\mu\nu}=0$ 说明：为什么"物质的能量守恒"不能作为独立假设，而必须与场方程一致？再说明如果引入一个 $\nabla^\mu T_{\mu\nu}\neq0$ 的"能量泄漏"，场方程会怎样被修改。

<details markdown="1"><summary>点击显示答案</summary>

**逻辑结构**：

1. $G_{\mu\nu}$ 满足 $\nabla^\mu G_{\mu\nu}=0$ **恒等地**（对任何度规，由第二 Bianchi 恒等式，不依赖场方程）。
2. 场方程 $G_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 成立 ⇒ 立刻推出 $\nabla^\mu T_{\mu\nu}=0$。
3. 所以"物质守恒"不是额外要求，而是"场方程 + 几何恒等式"的**推论**。

**反过来的约束**：如果物质不守恒，$\nabla^\mu T_{\mu\nu}\neq0$，那么 $G_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 无解（因为左边恒无散）。此时必须修改方程。两种标准做法：

- **加一个"泄漏项"到几何一边**：$G_{\mu\nu}=8\pi G_N(T_{\mu\nu}+\tau_{\mu\nu})$，其中 $\nabla^\mu\tau_{\mu\nu}=-\nabla^\mu T_{\mu\nu}$。这是"能量从物质流向另一个部门（例如额外维、或者某个标量场）"的记账方式；$\tau$ 必须是某个真实的能动张量，否则理论不自洽。
- **修改几何一边**：例如 $f(R)$ 引力、或引入额外的场（标量–张量理论）。这时 $\nabla^\mu G_{\mu\nu}=0$ 不再等于 $\nabla^\mu T_{\mu\nu}=0$，多出的项被新自由度吸收。

**为什么这件事重要**：

- 它解释了为什么"广义相对论自动包含能量守恒"——这在 Newton 引力里是要单独假设的。
- 它给出了修改引力的**判据**：任何修改都必须保证"总的能动张量（含新自由度）守恒"。
- 它是"等效原理"的一个推论：物质在局部惯性系里满足特殊相对论的能量守恒，而 $\nabla^\mu T_{\mu\nu}=0$ 正是这句话的协变化。

**与论文的接口**：论文 §1 说"在约束面上，Hamiltonian 化为边界荷"。这句话的技术基础就是 $\nabla^\mu G_{\mu\nu}=0$：约束（4 个）不是独立的演化方程，而是"荷的守恒"——第 12 章的 $\delta H_\xi=\int_{\partial\Sigma}Q_\xi$ 是它的精确形式。$\square$

</details>

**2.** 算理想流体 $T^{\mu\nu}=(\rho+p)u^\mu u^\nu+pg^{\mu\nu}$ 的 $\nabla_\mu T^{\mu\nu}=0$，分别投影得到连续性方程与 Euler 方程。

<details markdown="1"><summary>点击显示答案</summary>

**预备**：$u^\mu u_\mu=-1$ ⇒ $u_\mu\nabla_\nu u^\mu=0$。定义加速度 $a^\mu=u^\nu\nabla_\nu u^\mu$，则 $u_\mu a^\mu=0$。

**先把 $T$ 写成方便投影的形式**：

$$u_\nu T^{\mu\nu}=(\rho+p)u^\mu(u_\nu u^\nu)+p\,u_\nu g^{\mu\nu}=-(\rho+p)u^\mu+pu^\mu=-\rho u^\mu .$$

（能量流密度在共动系里只有能量密度。）

**沿 $u$ 投影（能量方程）**：

$$0=u_\nu\nabla_\mu T^{\mu\nu}=\nabla_\mu\left(u_\nu T^{\mu\nu}\right)-T^{\mu\nu}\nabla_\mu u_\nu
=-\nabla_\mu\left(\rho u^\mu\right)-T^{\mu\nu}\nabla_\mu u_\nu .$$

算最后一项：

$$T^{\mu\nu}\nabla_\mu u_\nu=(\rho+p)u^\mu u^\nu\nabla_\mu u_\nu+p\,g^{\mu\nu}\nabla_\mu u_\nu
=(\rho+p)u^\nu a_\nu+p\,\nabla_\mu u^\mu=p\,\nabla\cdot u .$$

（$u^\nu a_\nu=0$。）所以

$$\boxed{\nabla_\mu\left(\rho u^\mu\right)+p\,\nabla_\mu u^\mu=0 .}\qquad\square$$

**横向投影（Euler 方程）**：定义 $h^{\mu\nu}=g^{\mu\nu}+u^\mu u^\nu$（到 $u$ 正交子空间的投影）。

$$0=h^\nu{}_\sigma\nabla_\mu T^{\mu\sigma}
=h^\nu{}_\sigma\left[\nabla_\mu\left((\rho+p)u^\mu u^\sigma\right)+\nabla^\sigma p\right].$$

第一项里的 $u^\sigma$ 被 $h$ 投影掉（$h^\nu{}_\sigma u^\sigma=g^\nu{}_\sigma u^\sigma+u^\nu(u\cdot u)=u^\nu-u^\nu=0$）。剩下的：

$$0=(\rho+p)u^\mu\nabla_\mu u^\nu+h^\nu{}_\sigma\nabla^\sigma p .$$

即

$$\boxed{(\rho+p)\,a^\nu=-\left(g^{\nu\sigma}+u^\nu u^\sigma\right)\nabla_\sigma p .}\qquad\square$$

**读法**：

- **连续性方程**：$\nabla_\mu(\rho u^\mu)=-p\nabla\cdot u$。对无压强尘埃（$p=0$）就是 $\nabla_\mu(\rho u^\mu)=0$（粒子数/能量守恒）；有压强时"膨胀做功"会消耗能量密度。
- **Euler 方程**：$(\rho+p)a^\nu=-\nabla^\nu p$（在空间投影意义下）。**惯性是 $\rho+p$ 而不是 $\rho$**——压强也"有质量"，这是相对论效应。对光子气体（$p=\rho/3$）惯性是 $\frac43\rho$，这正是"辐射的引力更强"的一个来源。
- **$\Lambda$ 作为流体**：$p=-\rho$ ⇒ $\rho+p=0$ ⇒ $a^\mu=0$、$\nabla_\mu(\rho u^\mu)=0$：真空能不做功、不加速，只让时空指数膨胀。

</details>

**3.** 在弱场静态近似下，用 $R_{\mu\nu}=8\pi G_N(T_{\mu\nu}-\frac12Tg_{\mu\nu})$ 推出 $\nabla^2\Phi=4\pi G_N\rho$，并解释为什么用 $R_{00}=8\pi G_NT_{00}$ 会得到错误的两倍。

<details markdown="1"><summary>点击显示答案</summary>

**设定**：$g_{00}=-(1+2\Phi)$，$g_{ij}=(1-2\Phi)\delta_{ij}$（弱场、各向同性）；$T_{00}=\rho$、$T_{ij}\approx0$、$T\approx-\rho$；静态。

**第一步：$\Gamma^i_{00}$。**

$$\Gamma^i_{00}=\tfrac12g^{ij}\left(2\partial_0g_{j0}-\partial_jg_{00}\right)
=\tfrac12\delta^{ij}\left(0+2\partial_j\Phi\right)=\partial_i\Phi .$$

**第二步：$R_{00}$。**

$$R_{00}=\partial_i\Gamma^i_{00}-\partial_0\Gamma^i_{i0}+\Gamma\Gamma-\Gamma\Gamma\approx\partial_i\partial_i\Phi=\nabla^2\Phi .$$

（一阶近似丢掉 $\Gamma\Gamma$；静态丢掉 $\partial_0$。）

**第三步：场方程的迹反转形式。**

$$G_{\mu\nu}=8\pi G_NT_{\mu\nu}\;\Longrightarrow\;
R_{\mu\nu}-\tfrac12Rg_{\mu\nu}=8\pi G_NT_{\mu\nu}$$
$$\Longrightarrow\;R_{\mu\nu}=8\pi G_N\left(T_{\mu\nu}-\tfrac12Tg_{\mu\nu}\right).$$

（左边取迹 $R-\frac12R\cdot4=-R=8\pi G_NT$ ⇒ $R=-8\pi G_NT$，代回。）

**第四步：$00$ 分量。**

$$R_{00}=8\pi G_N\left(T_{00}-\tfrac12Tg_{00}\right)
=8\pi G_N\left(\rho-\tfrac12(-\rho)(-1)\right)
=8\pi G_N\left(\rho-\tfrac12\rho\right)=4\pi G_N\rho .$$

所以

$$\boxed{\nabla^2\Phi=4\pi G_N\rho .}\qquad\square$$

**为什么 $R_{00}=8\pi G_NT_{00}$ 会错**：那个式子对应的是 $R_{\mu\nu}=8\pi GT_{\mu\nu}$——这是**错误**的场方程（它不守恒）。正确的场方程是 $G_{\mu\nu}=8\pi GT_{\mu\nu}$，取迹反转后多出 $-\frac12Tg_{\mu\nu}$。在静态极限里 $T=-\rho$、$g_{00}=-1$，这一项是 $-\frac12\rho$，正好把 $\rho$ 削成 $\frac12\rho$。

**物理读法**：$-\frac12Tg_{\mu\nu}$ 这一项编码了"压强也产生引力"。在静态非相对论物质里 $p\ll\rho$，但它仍然贡献了**一半**的 Newton 势——这是"引力耦合的是 $T_{\mu\nu}-\frac12Tg_{\mu\nu}$ 而不是 $T_{\mu\nu}$"的直接后果。如果换成辐射（$p=\rho/3$），这一项会变成 $-\frac12(\rho-3p)=\ldots$，导致辐射的引力源是 $\rho+3p=\frac43\cdot$（更准确：$R_{00}=4\pi G(\rho+3p)$），这就是"辐射的引力更强"的来源。

**一个可检验的推论**：把 $\rho\to\rho+3p$ 代进 Poisson 方程，得到**主动引力质量密度** $\rho+3p$。对普通物质 $p\approx0$；对真空能 $p=-\rho$ ⇒ $\rho+3p=-2\rho$ ⇒ **排斥**。这就是 $\Lambda$ 让宇宙加速膨胀的 Newton 版解释。

</details>

**4.** 从 $S_{\rm EH}+S_{\rm GHY}$ 的变分推出真空场方程，并说明 GHY 项为什么是必需的（用第 10 章的结果）。

<details markdown="1"><summary>点击显示答案</summary>

**变分**：

$$\delta S_{\rm EH}=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}\,\mathrm{d}^4x
+\frac{1}{16\pi G_N}\int_{\partial M}\sqrt h\,n_\mu v^\mu ,$$

其中 $v^\mu=g^{\alpha\beta}\delta\Gamma^\mu_{\alpha\beta}-g^{\mu\alpha}\delta\Gamma^\beta_{\alpha\beta}$。

**边界项**（第 10 章）：在 $\delta h_{ij}|_{\partial M}=0$ 的变分下，

$$n_\mu v^\mu=-2\delta K,\qquad K=h^{ij}K_{ij} .$$

所以

$$\frac{1}{16\pi G_N}\int_{\partial M}\sqrt h\,n\cdot v
=-\frac{1}{8\pi G_N}\int_{\partial M}\sqrt h\,\delta K .$$

**加 GHY**：

$$\delta S_{\rm GHY}=\frac{1}{8\pi G_N}\int_{\partial M}\sqrt h\,\delta K,$$

与上式精确抵消。

**结论**：

$$\delta\left(S_{\rm EH}+S_{\rm GHY}\right)
=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}\,\mathrm{d}^4x=0
\quad\forall\,\delta g^{\mu\nu}\ \text{（内部）}$$

⇒

$$\boxed{G_{\mu\nu}=0 .}\qquad\square$$

（带 $\Lambda$ 时加 $+\Lambda g_{\mu\nu}$；带物质时右边加 $8\pi G_NT_{\mu\nu}$。）

**为什么 GHY 必需**：如果不要 GHY，$\delta S_{\rm EH}=0$ 会要求"边界项也为零"，这等价于固定 $\delta K$（Neumann 条件）而不是固定 $\delta h$（Dirichlet）。但物理上我们固定的是边界上的诱导度规（"边界在哪、多大"），不是它的法向导数。所以：

- **没有 GHY**：作用量对"边界形状"的变分不稳定（同一边界数据，不同的边界外延给不同的 $S$，变分原理失效）。
- **有 GHY**：作用量只依赖诱导度规，Dirichlet 原理成立。

**三个一致性检验**：

1. **符号**：GHY 的系数是 $+\frac{1}{8\pi G}$（不是 $\frac{1}{16\pi G}$）——因为 $\delta S_{\rm EH}$ 的边界项系数是 $\frac{1}{16\pi G}\times(-2)=-\frac{1}{8\pi G}$。
2. **缝合**：两个区域共享边界时，$n_2=-n_1$ ⇒ $K_2=-K_1$ ⇒ 两份 GHY 相消，作用量可加（第 10 章自检 4）。系数错了这一步就不成立。
3. **ADM 质量**：Brown–York 张量从 $\delta h$ 的系数读出，给 $M_{\rm ADM}$（第 10 章自检 4）。系数错了质量就错。

</details>

**5.** 计数：说明 $G_{\mu\nu}=8\pi G_NT_{\mu\nu}$ 的 10 个方程里为什么只有 6 个是独立演化方程；再用 ADM 相空间的维数验证"2 个偏振"。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：Bianchi 给 4 个恒等式。** $\nabla^\mu G_{\mu\nu}=0$ 是 4 个方程（$\nu=0,1,2,3$），它们是恒等式（对任何度规成立），所以不构成对度规的约束。这意味着 10 个场方程中至多 6 个独立。

**第二步：这 4 个恰好是约束。** 在 3+1 分解里（第 11 章），$G_{00}$ 与 $G_{0i}$ 只含 $h_{ij}$ 与 $K_{ij}$ 的**空间**导数，不含时间导数——它们是初始数据的约束。$G_{ij}$ 含 $\partial_tK_{ij}$，是演化方程。

**第三步：规范自由度。** 坐标选择（4 个函数）不改变物理，所以 10 个场方程的解在 4 个坐标变换下等价。这不是"减去 4 个方程"，而是"减去 4 个变量"。

**第四步：ADM 计数。**

| 量 | 分量数 |
|---|---|
| $h_{ij}$（空间度规） | 6 |
| $K_{ij}$（外曲率） | 6 |
| 相空间总维数 | 12 |
| 第一类约束（Hamiltonian + momentum） | 4 |
| 每个第一类约束消去 2 维（约束 + 规范固定） | $4\times2=8$ |
| 剩余 | $12-8=4$ |
| 物理自由度 | $4/2=2$（坐标 + 动量） |

$$\boxed{\text{2 个偏振}.}\qquad\square$$

**为什么"每个第一类约束消去 2 维"**：在 Dirac 理论里（[理论力学书第 12 章](../../classical-mechanics/docs/12-constraints-dirac-theory.md)），一个第一类约束既是"相空间上的约束面"（消去 1 维），又生成一个规范变换（再消去 1 维）。所以第一类约束数 $F$ 给 $2F$。公式：物理自由度 $=\frac{1}{2}(2n-2F-S)$，$2n=12$、$F=4$、$S=0$ ⇒ $\frac12(12-8)=2$ ✓。

**三条交叉检验**：

1. **引力波**：2 个偏振（$+$ 与 $\times$），与 LIGO 的观测一致。
2. **第 5s 章**：Plebański 形式"带 2 个传播自由度"，与这里一致。
3. **论文**：4 维因果菱形的有限维性依赖"剪切改变时钟读数"，剪切正是这 2 个偏振的效应；JT（0 个传播自由度）没有这个机制，所以给出 $\mathrm{I}_\infty$（[论文阅读首篇](../../paper-reading/docs/01-null-cone-quantum-gravity.md) §6）。**"2" 这个数字在整条量子引力路线上反复出现。**

**一个容易混淆的点**：10 个方程、6 个独立、4 个约束——**不要**说成"10−4=6 个演化方程"。正确的说法是：6 个方程含 $\partial_t^2h$（演化），4 个方程只含 $\partial_t h$ 的一次（约束），而 $\nabla^\mu G_{\mu\nu}=0$ 保证"约束在演化中保持"（约束传播）。这个"约束自动保持"的性质是广义相对论初值问题适定性的核心，第 11 章会展开。

</details>

## 参考

- Wald《General Relativity》第 4.1–4.3 节（Einstein 方程的推导与唯一性）、第 4.4 节（Lagrangian 形式与边界项）、第 10 章（初值问题）。
- Carroll《Spacetime and Geometry》第 4 章（EH 作用量与变分）、第 7 章（宇宙学常数）。
- Lovelock, "The Einstein tensor and its generalizations"（4 维唯一性的原始文献；也可看 Wald 附录 B 的讨论）。
- Poisson《A Relativist's Toolkit》第 4 章（Brown–York 与准局域量）。
- [理论力学书第 5–6 章](../../classical-mechanics/docs/05-least-action-principle.md)（作用量原理与 Noether 定理）、[第 12 章](../../classical-mechanics/docs/12-constraints-dirac-theory.md)（第一类约束与自由度计数）；第 3 章（Bianchi 与 $G_{\mu\nu}$ 的无散性）、第 10 章（GHY）、第 11 章（ADM 计数）、第 6 章（Schwarzschild 作为真空解）。
