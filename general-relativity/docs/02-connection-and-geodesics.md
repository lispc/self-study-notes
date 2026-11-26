# 联络与测地线：怎么在弯曲时空里"求导"和"走直线"

> 路线图位置：第 1 部分（微分几何工具）· 第 2 章
> 前置知识：第 1 章（流形、切矢量、余矢量、张量、度规、固有时）。
> 学习目标：能说清为什么偏导数不是张量、联络的变换律如何精确抵消那一项；会从"度量相容 + 无挠"唯一确定 Levi-Civita 联络并写出克氏符；会用平行移动与和乐说明"弯曲 = 路径依赖"；会从作用量推出测地线方程并解释仿射参数；理解"类时测地线使固有时取极值"与等效原理的关系。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$。$\Gamma^\mu{}_{\nu\rho}$ 的指标顺序：第一个上指标是"被求导的对象"，第二个是导数方向，第三个是被求导分量。曲率约定留到第 3 章，本章只用 $\Gamma$。

## 1. 一句话总结

**在弯曲时空里，"把一个矢量从 $p$ 搬到 $q$ 再相减"没有先验意义；联络 $\Gamma^\mu{}_{\nu\rho}$ 就是补上这个意义的规则。** 要求两条最自然的性质——**度量相容**（搬动时不改变长度与夹角）与**无挠**（无穷小平行四边形的两条对角路径一致）——唯一确定 Levi-Civita 联络，即克氏符 $\Gamma^\mu{}_{\nu\rho}=\frac12g^{\mu\sigma}(\partial_\nu g_{\sigma\rho}+\partial_\rho g_{\sigma\nu}-\partial_\sigma g_{\nu\rho})$。有了它，"最直的线"（测地线）有了定义，而测地线正好是**固有时取极值的世界线**——自由落体不是"受引力"，而是"没有受任何力"。

## 2. 为什么偏导数不够用

### 2.1 直接算变换律

设 $v^\mu$ 是矢量场，$v'^\mu=J^\mu{}_\alpha v^\alpha$，$J^\mu{}_\alpha=\partial x'^\mu/\partial x^\alpha$。求导：

$$\partial'_\mu v'^\nu
=\frac{\partial x^\rho}{\partial x'^\mu}\partial_\rho\left(J^\nu{}_\alpha v^\alpha\right)
=\frac{\partial x^\rho}{\partial x'^\mu}J^\nu{}_\alpha\partial_\rho v^\alpha
+\frac{\partial x^\rho}{\partial x'^\mu}\frac{\partial J^\nu{}_\alpha}{\partial x^\rho}v^\alpha .$$

第一项是"张量该有的样子"（一个 $J$、一个 $J^{-1}$）；**第二项多出来**，它含 $v$ 本身而不是 $v$ 的导数。所以

$$\boxed{\;\partial_\nu v^\mu\ \text{不是张量}\;}$$

（只有在变换是**线性**的、即 $J$ 与位置无关时，第二项才为零——这也是为什么狭义相对论里"偏导就是张量"。）

### 2.2 几何上"多出来的是什么"

把 $v$ 从 $p$ 搬到邻近的 $p+\delta x$：在平直空间里，"保持分量不变"就是平行移动。在弯曲空间里，基矢量本身随位置变，所以"保持分量不变"不再是"同一个矢量"。

**联络就是规定"基矢量怎么变"**：

$$\nabla_\mu v^\nu\equiv\partial_\mu v^\nu+\Gamma^\nu{}_{\mu\rho}v^\rho .$$

$\Gamma$ 的变换律里恰好有一个非齐次项，与 $\partial_\nu v^\mu$ 多出的那一项**精确抵消**（自检 1 给出显式验证）。这就是"联络不是张量、但协变导数是张量"的全部机制。

## 3. 仿射联络与协变导数

### 3.1 公理

仿射联络是一个把"两个矢量场"映到"一个矢量场"的算子 $\nabla$，满足

$$\nabla_{\alpha}(f u^\mu+g v^\mu)=f\nabla_\alpha u^\mu+g\nabla_\alpha v^\mu\quad(\text{线性}),$$
$$\nabla_\alpha(f v^\mu)=(\partial_\alpha f)v^\mu+f\nabla_\alpha v^\mu\quad(\text{Leibniz}).$$

坐标里写成

$$\boxed{\;\nabla_\alpha v^\mu=\partial_\alpha v^\mu+\Gamma^\mu{}_{\alpha\beta}v^\beta,\qquad
\nabla_\alpha\omega_\mu=\partial_\alpha\omega_\mu-\Gamma^\beta{}_{\alpha\mu}\omega_\beta .\;}$$

**符号规则**：每个上指标带 $+\Gamma$，每个下指标带 $-\Gamma$。对一般张量逐指标套用。与缩并相容：$\nabla_\alpha(T^\mu{}_{\mu})=\partial_\alpha(T^\mu{}_{\mu})$（联络项两两相消）。

### 3.2 联络的变换律（非齐次）

$$\Gamma'^\mu{}_{\nu\rho}
=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x^\beta}{\partial x'^\nu}\frac{\partial x^\gamma}{\partial x'^\rho}\Gamma^\alpha{}_{\beta\gamma}
+\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial^2x^\alpha}{\partial x'^\nu\partial x'^\rho}.$$

**读法**：第一项是"张量该有的"，第二项是"补偿项"。它**不是**张量——这正是联络的用处：它承担"坐标的弯曲"，让协变导数干净。

**一个立刻的推论**：在任一点 $p$，可以选坐标使 $\Gamma^\mu{}_{\nu\rho}(p)=0$（黎曼法坐标 / 局部惯性系）。做法：取指数映射意义下的"局部平直坐标"。第 3 章会看到，这时 $g_{\mu\nu}(p)=\eta_{\mu\nu}$、$\partial_\alpha g_{\mu\nu}(p)=0$，但二阶导数不能全消——曲率住在那里。

## 4. 两个条件唯一确定联络

### 4.1 度量相容

$$\boxed{\;\nabla_\rho g_{\mu\nu}=0\;}$$

物理含义：平行移动保持长度与夹角。展开：

$$\partial_\rho g_{\mu\nu}-\Gamma^\sigma{}_{\rho\mu}g_{\sigma\nu}-\Gamma^\sigma{}_{\rho\nu}g_{\mu\sigma}=0 .$$

用 $\Gamma_{\mu\nu\rho}\equiv g_{\mu\sigma}\Gamma^\sigma{}_{\nu\rho}$（全下指标）写成

$$\partial_\rho g_{\mu\nu}=\Gamma_{\nu\rho\mu}+\Gamma_{\mu\rho\nu}. \tag{2.1}$$

### 4.2 无挠

$$\boxed{\;\Gamma^\mu{}_{[\nu\rho]}=0\;}$$

即 $\Gamma^\mu{}_{\nu\rho}=\Gamma^\mu{}_{\rho\nu}$。几何含义：无穷小平行四边形的两条路径给出同一个矢量（挠率 = 四边形的"缺口"）。

### 4.3 解出克氏符

把 (2.1) 的指标轮换两次：

$$\partial_\mu g_{\nu\rho}=\Gamma_{\rho\mu\nu}+\Gamma_{\nu\mu\rho},\qquad
\partial_\nu g_{\rho\mu}=\Gamma_{\mu\nu\rho}+\Gamma_{\rho\nu\mu}.$$

计算 $\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}$，用无挠性 $\Gamma_{abc}=\Gamma_{acb}$ 逐项配对（自检 2 给细节）：

$$=2\Gamma_{\rho\mu\nu}.$$

升指标：

$$\boxed{\;\Gamma^\sigma{}_{\mu\nu}
=\frac12g^{\sigma\rho}\left(\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}\right)
=\frac12g^{\sigma\rho}\left(\partial_\mu g_{\rho\nu}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}\right).\;}$$

**三个待记住的事实**：

1. **唯一性**：满足两条条件的联络只有一个（Levi-Civita 联络）。证明就是上面的代数：线性方程组系数可逆。
2. **$\Gamma$ 不是张量**，但在同一坐标里"$\Gamma$ 全为零"是可达的（局部惯性系）。
3. **$\Gamma$ 依赖度规的一阶导数**，所以曲率（二阶导数）不能靠选坐标消掉（第 3 章）。

## 5. 平行移动与和乐

### 5.1 定义

沿曲线 $\gamma(\lambda)$，矢量 $v$ 被**平行移动**，若

$$\frac{Dv^\mu}{\mathrm{d}\lambda}\equiv\frac{\mathrm{d}v^\mu}{\mathrm{d}\lambda}+\Gamma^\mu{}_{\nu\rho}\frac{\mathrm{d}x^\nu}{\mathrm{d}\lambda}v^\rho=0 .$$

这是一阶线性 ODE，给定初值 $v(0)$，解唯一。**没有路径依赖**就没有曲率。

### 5.2 和乐：路径依赖

绕闭合回路平行移动一圈，$v$ 一般不回到自身：

$$v(L)-v(0)=\mathcal P\exp\left(-\oint\Gamma\cdot\mathrm{d}x\right)v(0)\neq v(0).$$

这个转动叫**和乐**（holonomy）。它不能由"选个好坐标"消掉——因为它是闭合回路的拓扑–几何不变量。

**例子（自检 5 算完）**：单位球面上沿纬度圈 $\theta=\theta_0$ 平行移动一圈，物理转角为

$$2\pi\left(1-\cos\theta_0\right)=\text{球冠面积}.$$

赤道（$\theta_0=\pi/2$）是测地线，和乐 $=2\pi$（恒等变换）；小圆极限给 $\pi\theta_0^2$（面积）。

### 5.3 和乐与曲率的关系

对无穷小回路，和乐正比于曲率（第 3 章的 $R^\mu{}_{\nu\rho\sigma}$ 就是"单位面积的和乐"）：

$$v^\mu(x)-v^\mu(x_0)\approx-\tfrac12R^\mu{}_{\nu\rho\sigma}(x_0)v^\nu(x_0)\,\Sigma^{\rho\sigma},$$

$\Sigma^{\rho\sigma}$ 是回路张成的面积元。**所以曲率就是和乐的密度**——这是第 3 章的出发点。

## 6. 测地线

### 6.1 两种定义

**(a) 自平行曲线**：切矢沿自己平行移动，

$$\boxed{\;\frac{D\dot x^\mu}{\mathrm{d}\lambda}\equiv\ddot x^\mu+\Gamma^\mu{}_{\nu\rho}\dot x^\nu\dot x^\rho=0\;}$$

（$\dot{}=\mathrm{d}/\mathrm{d}\lambda$）。这是"最直的线"：方向不变的曲线。

**(b) 长度/固有时极值**：对

$$S=\int\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,\mathrm{d}\lambda$$

变分。自检 4 证明两者等价，且 $\lambda$ 必须是**仿射参数**。

### 6.2 仿射参数

(a) 在 $\lambda\to a\lambda+b$ 下保持形式；(b) 里 $\sqrt{-\dot x^2}$ 是 $\lambda$ 的一阶齐次函数，所以只有仿射重参数化保持"极值"性质。**非仿射参数** $\sigma$ 下方程多一项：

$$\frac{\mathrm{d}^2x^\mu}{\mathrm{d}\sigma^2}+\Gamma^\mu{}_{\nu\rho}\frac{\mathrm{d}x^\nu}{\mathrm{d}\sigma}\frac{\mathrm{d}x^\rho}{\mathrm{d}\sigma}
=\kappa(\sigma)\frac{\mathrm{d}x^\mu}{\mathrm{d}\sigma}.$$

这与第 8 章的 $\kappa$（非仿射度、表面重力）是同一个东西。

### 6.3 类时测地线使固有时最大

在洛伦兹号差下，**类时测地线是固有时取局部极大的曲线**（不是极小！）。理由：

- 在平直空间，直线的固有时最长（双生子佯谬：飞行的那个回来更年轻）。
- 在弯曲空间，短程的类时测地线仍使 $\tau$ 取局部极大；**全局**不一定（可能存在更长的非测地线世界线，例如绕道经过曲率不同的区域）。

**物理解读（等效原理）**：自由落体的世界线是类时测地线——它在自己的局部惯性系里"静止"，不感到力。所以"引力"不是力，而是"时空的测地线偏离直线"。第 3 章的测地偏离方程会把这句话定量化。

### 6.4 零测地线

$g_{\mu\nu}\dot x^\mu\dot x^\nu=0$ 的测地线。$S=\int\sqrt{-\dot x^2}$ 对零曲线退化（被积式恒为零），所以用自平行定义 (a) 或"仿射参数下的极值"。**光线走零测地线**（第 6 章的光线偏折、第 8 章的零生成元都是它）。

## 7. 坐标奇异 vs 几何奇异

$\Gamma$ 在坐标里可能发散，但这未必意味着几何奇异。判据是**曲率标量**是否发散。

**例子**：2D 球面用球坐标时，$\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$、$\Gamma^\phi{}_{\theta\phi}=\cot\theta$。在 $\theta=0$（北极），$\cot\theta\to\infty$——但球面在北极完全光滑（那里只是球坐标失效）。曲率标量 $R=2/a^2$ 处处有限。

**对照**：Schwarzschild 的 $r=2GM$ 也是"$\Gamma$ 发散但曲率有限"（第 6 章会算 $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=48G^2M^2/r^6$，在 $r=2GM$ 有限）；而 $r=0$ 是真奇异（曲率发散）。

**判据清单**（由弱到强）：

1. $\Gamma$ 发散 ⇒ 可能只是坐标坏。
2. 曲率张量分量在某坐标里发散 ⇒ 强烈提示真奇异，但仍需坐标无关的判据。
3. **曲率标量**（$R$、$R_{\mu\nu}R^{\mu\nu}$、$R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$）发散 ⇒ 真奇异（标量在换坐标下不变）。
4. 测地线不完备 ⇒ 最严格的判据（Penrose/Hawking 的定义）。

## 8. 小结

- $\partial_\nu v^\mu$ 不是张量，多出的项与 $\Gamma$ 的非齐次变换项精确抵消 ⇒ $\nabla$ 是张量算子。
- 联络 $\Gamma^\mu{}_{\nu\rho}$ 非张量；局部惯性系里可使 $\Gamma(p)=0$。
- 度量相容 $\nabla g=0$ + 无挠 $\Gamma^\mu{}_{[\nu\rho]}=0$ ⇒ 唯一 Levi-Civita 联络，克氏符 $\frac12g^{\mu\sigma}(\partial_\nu g_{\sigma\rho}+\partial_\rho g_{\sigma\nu}-\partial_\sigma g_{\nu\rho})$。
- 平行移动：沿曲线的线性 ODE；闭合回路的和乐 = 曲率的面积分（第 3 章）。
- 测地线：$\ddot x^\mu+\Gamma^\mu{}_{\nu\rho}\dot x^\nu\dot x^\rho=0$；等价于 $\delta\int\sqrt{-\dot x^2}=0$；$\lambda$ 必须是仿射参数。
- 类时测地线使固有时**局部极大**；自由落体 = 测地线 = 不受力（等效原理）。
- 零测地线是光线的路径。
- $\Gamma$ 发散可能只是坐标坏；真奇异看曲率标量与测地线完备性。

## 自检问题

**1.** 证明 $\partial_\nu v^\mu$ 不是张量；再证明 $\Gamma$ 的变换律中的非齐次项恰好抵消它，使 $\nabla_\nu v^\mu$ 是张量。

<details markdown="1"><summary>点击显示答案</summary>

记 $J^\mu{}_\alpha=\partial x'^\mu/\partial x^\alpha$，$K^\alpha{}_\mu=\partial x^\alpha/\partial x'^\mu$。两者互逆：$J^\mu{}_\alpha K^\alpha{}_\nu=\delta^\mu{}_\nu$。

**第一步：偏导数。** 由 $v'^\nu=J^\nu{}_\alpha v^\alpha$ 与 $\partial'_\mu=K^\rho{}_\mu\partial_\rho$，

$$\partial'_\mu v'^\nu=J^\nu{}_\alpha K^\rho{}_\mu\partial_\rho v^\alpha+\left(\partial'_\mu J^\nu{}_\alpha\right)v^\alpha .$$

第一项是"张量该有的样子"；第二项

$$\boxed{B^\nu{}_\mu\equiv\left(\partial'_\mu J^\nu{}_\alpha\right)v^\alpha}$$

是坏项（含 $v$ 本身，不含导数），所以 $\partial v$ 不是张量。$\square$

**第二步：$\Gamma$ 的贡献。** 变换律（正文 §3.2）为

$$\Gamma'^\nu{}_{\mu\rho}=J^\nu{}_\beta K^\gamma{}_\mu K^\delta{}_\rho\Gamma^\beta{}_{\gamma\delta}
+J^\nu{}_\beta\,\partial'_\mu K^\beta{}_\rho .$$

第一块（齐次部分）作用在 $v'^\rho=J^\rho{}_\sigma v^\sigma$ 上：

$$J^\nu{}_\beta K^\gamma{}_\mu K^\delta{}_\rho\Gamma^\beta{}_{\gamma\delta}\,J^\rho{}_\sigma v^\sigma
=J^\nu{}_\beta K^\gamma{}_\mu\Gamma^\beta{}_{\gamma\sigma}v^\sigma,$$

正是我们想要的那一项（用 $K^\delta{}_\rho J^\rho{}_\sigma=\delta^\delta{}_\sigma$）。

第二块（非齐次部分）：

$$J^\nu{}_\beta\left(\partial'_\mu K^\beta{}_\rho\right)J^\rho{}_\sigma v^\sigma .$$

**第三步：非齐次项恰好抵消坏项。** 对 $J^\nu{}_\beta K^\beta{}_\rho=\delta^\nu{}_\rho$ 求 $\partial'_\mu$：

$$\left(\partial'_\mu J^\nu{}_\beta\right)K^\beta{}_\rho+J^\nu{}_\beta\,\partial'_\mu K^\beta{}_\rho=0
\;\Longrightarrow\;
J^\nu{}_\beta\,\partial'_\mu K^\beta{}_\rho=-\left(\partial'_\mu J^\nu{}_\beta\right)K^\beta{}_\rho .$$

代回第二块：

$$-\left(\partial'_\mu J^\nu{}_\beta\right)K^\beta{}_\rho J^\rho{}_\sigma v^\sigma
=-\left(\partial'_\mu J^\nu{}_\beta\right)\delta^\beta{}_\sigma v^\sigma
=-\left(\partial'_\mu J^\nu{}_\sigma\right)v^\sigma=-B^\nu{}_\mu .$$

（中间用 $K^\beta{}_\rho J^\rho{}_\sigma=\delta^\beta{}_\sigma$。）**非齐次项 = 坏项的负值，精确抵消。**

**第四步：结论。**

$$\nabla'_\mu v'^\nu=\partial'_\mu v'^\nu+\Gamma'^\nu{}_{\mu\rho}v'^\rho
=J^\nu{}_\alpha K^\rho{}_\mu\partial_\rho v^\alpha+J^\nu{}_\beta K^\gamma{}_\mu\Gamma^\beta{}_{\gamma\sigma}v^\sigma
=K^\rho{}_\mu J^\nu{}_\alpha\nabla_\rho v^\alpha .\qquad\square$$

**三点读法**：

1. **$\Gamma$ 的变换律不是猜的**：它是"唯一能让 $\nabla$ 成为张量算子"的变换律。任何别的系数都会留下残余坏项。
2. **两个互逆的变换**：$J$（上指标）与 $K$（下指标）在坏项与补偿项里各出现一次，这解释了"$\Gamma$ 有一个上指标、两个下指标"的形状。
3. **为什么必须在同一点**：$\partial'_\mu J^\nu{}_\alpha$ 是同一坐标点上的偏导，所以抵消是逐点成立的——这正是"联络是局部的"。

</details>

**2.** 从 $\nabla_\rho g_{\mu\nu}=0$ 与无挠性推出克氏符公式（把指标轮换与配对写清楚）。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：展开度量相容。** $\nabla_\rho g_{\mu\nu}=\partial_\rho g_{\mu\nu}-\Gamma^\sigma{}_{\rho\mu}g_{\sigma\nu}-\Gamma^\sigma{}_{\rho\nu}g_{\mu\sigma}=0$。定义 $\Gamma_{\mu\nu\rho}\equiv g_{\mu\sigma}\Gamma^\sigma{}_{\nu\rho}$（第一个指标是"被求导对象"、第二个是方向、第三个是分量），则

$$\partial_\rho g_{\mu\nu}=\Gamma_{\nu\rho\mu}+\Gamma_{\mu\rho\nu}. \tag{2.1}$$

**第二步：轮换两次。**

$$\partial_\mu g_{\nu\rho}=\Gamma_{\rho\mu\nu}+\Gamma_{\nu\mu\rho},\qquad
\partial_\nu g_{\rho\mu}=\Gamma_{\mu\nu\rho}+\Gamma_{\rho\nu\mu}. \tag{2.2}$$

**第三步：组合。** $\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}$ 的六项：

$$\Gamma_{\rho\mu\nu}+\Gamma_{\nu\mu\rho}+\Gamma_{\mu\nu\rho}+\Gamma_{\rho\nu\mu}-\Gamma_{\nu\rho\mu}-\Gamma_{\mu\rho\nu}.$$

**第四步：用无挠配对。** 无挠 $\Gamma^\sigma{}_{[\nu\rho]}=0$ 等价于 $\Gamma_{\mu\nu\rho}=\Gamma_{\mu\rho\nu}$（后两个指标对称）。逐对看：

- $\Gamma_{\rho\mu\nu}$ 与 $\Gamma_{\rho\nu\mu}$：后两指标是 $(\mu,\nu)$ 与 $(\nu,\mu)$，相等 ⇒ 合计 $2\Gamma_{\rho\mu\nu}$。
- $\Gamma_{\nu\mu\rho}$ 与 $-\Gamma_{\nu\rho\mu}$：后两指标 $(\mu,\rho)$ 与 $(\rho,\mu)$，相等 ⇒ 相消。
- $\Gamma_{\mu\nu\rho}$ 与 $-\Gamma_{\mu\rho\nu}$：同样相消。

故

$$\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}=2\Gamma_{\rho\mu\nu}.$$

升指标：

$$\Gamma^\sigma{}_{\mu\nu}=g^{\sigma\rho}\Gamma_{\rho\mu\nu}
=\frac12g^{\sigma\rho}\left(\partial_\mu g_{\nu\rho}+\partial_\nu g_{\rho\mu}-\partial_\rho g_{\mu\nu}\right).\qquad\square$$

**三个检验**：

1. **平直空间**：$g=$ 常数 ⇒ $\Gamma=0$ ✓。
2. **2D 极坐标** $ds^2=dr^2+r^2d\varphi^2$：$\Gamma^r{}_{\varphi\varphi}=-r$、$\Gamma^\varphi{}_{r\varphi}=1/r$。代公式：$\Gamma^r{}_{\varphi\varphi}=\frac12g^{rr}(-\partial_r g_{\varphi\varphi})=-\frac12\cdot2r=-r$ ✓。
3. **对称性**：公式明显对 $\mu\leftrightarrow\nu$ 对称（与无挠一致）。

**为什么唯一**：三个方程 (2.1)、(2.2) 对三个未知的 $\Gamma_{\rho\mu\nu}$（固定 $\rho$）是线性方程组，系数是 $g$；组合 $+-\!$ 给出解，且解唯一。所以"度量相容 + 无挠"不是两条独立的要求，而是"恰好定出唯一的联络"。

</details>

**3.** 用 2D 球面 $ds^2=a^2(d\theta^2+\sin^2\theta\,d\phi^2)$ 计算非零克氏符，并验证在北极处曲率有限。

<details markdown="1"><summary>点击显示答案</summary>

**度规分量**：$g_{\theta\theta}=a^2$，$g_{\phi\phi}=a^2\sin^2\theta$，$g_{\theta\phi}=0$；逆 $g^{\theta\theta}=1/a^2$，$g^{\phi\phi}=1/(a^2\sin^2\theta)$。

**非零导数**：$\partial_\theta g_{\phi\phi}=2a^2\sin\theta\cos\theta$；其余为零（$g$ 不依赖 $\phi$）。

**逐对指标算**：

$\Gamma^\theta{}_{\phi\phi}=\frac12g^{\theta\theta}\left(\partial_\phi g_{\phi\theta}+\partial_\phi g_{\theta\phi}-\partial_\theta g_{\phi\phi}\right)
=\frac12\cdot\frac{1}{a^2}\cdot(-2a^2\sin\theta\cos\theta)=-\sin\theta\cos\theta .$

$\Gamma^\phi{}_{\theta\phi}=\frac12g^{\phi\phi}\left(\partial_\theta g_{\phi\phi}+\partial_\phi g_{\theta\phi}-\partial_\phi g_{\theta\theta}\right)
=\frac12\cdot\frac{1}{a^2\sin^2\theta}\cdot2a^2\sin\theta\cos\theta=\cot\theta .$

$\Gamma^\phi{}_{\phi\theta}=\cot\theta$（对称）；$\Gamma^\theta{}_{\theta\theta}=\Gamma^\theta{}_{\theta\phi}=0$（$g_{\theta\theta}$ 常数）。

所以

$$\boxed{\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta,\qquad
\Gamma^\phi{}_{\theta\phi}=\Gamma^\phi{}_{\phi\theta}=\cot\theta,}$$

其余为零。$\square$

**在北极的行为**：$\theta\to0$ 时 $\cot\theta\sim1/\theta\to\infty$。但这不是几何奇异：

- 球面在北极完全光滑（它是流形上的普通点）；
- 球坐标在北极退化（所有 $\phi$ 对应同一点，$\partial_\phi$ 的长度 $\to0$）；
- 曲率标量 $R=2/a^2$ 处处有限（第 3 章自检 4 算）。

**从和乐角度看**：沿小圆 $\theta=\theta_0$ 平行移动一圈，转角 $\approx\pi\theta_0^2$（自检 5）。$\theta_0\to0$ 时转角 $\to0$，说明北极附近"越来越平"——曲率有限而非发散。$\Gamma$ 的发散被回路面积 $\sim\theta_0^2$ 压住了。$\square$

**这是广义相对论里最常见的误判**：看到 $\Gamma$ 发散就以为有奇点。正确判据是曲率标量（第 6 章的 $r=2GM$ 是另一个例子）。

</details>

**4.** 从 $S=\int\sqrt{-g_{\mu\nu}\dot x^\mu\dot x^\nu}\,\mathrm{d}\lambda$ 的变分推出测地线方程，并说明为什么 $\lambda$ 是仿射参数。

<details markdown="1"><summary>点击显示答案</summary>

记 $F\equiv-g_{\mu\nu}\dot x^\mu\dot x^\nu\gt0$（类时），$L=\sqrt F$。

**第一步：把 $\sqrt F$ 换成 $F$。** 沿真实轨道 $F$ 是常数（下一步会看到），故

$$\delta\int\sqrt F\,\mathrm{d}\lambda=\int\frac{\delta F}{2\sqrt F}\mathrm{d}\lambda
=\frac{1}{2\sqrt{F}}\,\delta\int F\,\mathrm{d}\lambda\quad\left(\sqrt F\ \text{常数}\right).$$

所以极值 $\int\sqrt F$ 等价于极值

$$S'=\int F\,\mathrm{d}\lambda=-\int g_{\mu\nu}\dot x^\mu\dot x^\nu\,\mathrm{d}\lambda .$$

**第二步：对 $S'$ 变分。**

$$\delta S'=-\int\left(2g_{\mu\nu}\dot x^\nu\delta\dot x^\mu+\partial_\rho g_{\mu\nu}\dot x^\mu\dot x^\nu\delta x^\rho\right)\mathrm{d}\lambda .$$

第一项分部积分（端点固定）：

$$-\int2g_{\mu\nu}\dot x^\nu\frac{\mathrm{d}(\delta x^\mu)}{\mathrm{d}\lambda}\mathrm{d}\lambda
=\int2\left(\frac{\mathrm{d}}{\mathrm{d}\lambda}\left(g_{\mu\nu}\dot x^\nu\right)\right)\delta x^\mu\,\mathrm{d}\lambda .$$

于是（把哑指标 $\mu\to\sigma$）

$$0=\delta S'=\int\left[2\frac{\mathrm{d}}{\mathrm{d}\lambda}\left(g_{\sigma\nu}\dot x^\nu\right)-\partial_\sigma g_{\mu\nu}\dot x^\mu\dot x^\nu\right]\delta x^\sigma\,\mathrm{d}\lambda .$$

**第三步：展开导数。**

$$\frac{\mathrm{d}}{\mathrm{d}\lambda}\left(g_{\sigma\nu}\dot x^\nu\right)
=g_{\sigma\nu}\ddot x^\nu+\partial_\rho g_{\sigma\nu}\dot x^\rho\dot x^\nu .$$

代入并用 $\dot x^\rho\dot x^\nu$ 的对称性把 $\partial_\rho g_{\sigma\nu}$ 对称化：

$$2g_{\sigma\nu}\ddot x^\nu+\left(\partial_\rho g_{\sigma\nu}+\partial_\nu g_{\sigma\rho}-\partial_\sigma g_{\nu\rho}\right)\dot x^\nu\dot x^\rho=0 .$$

**第四步：乘 $g^{\sigma\mu}$ 并认出克氏符。**

$$\ddot x^\mu+\tfrac12g^{\mu\sigma}\left(\partial_\rho g_{\sigma\nu}+\partial_\nu g_{\sigma\rho}-\partial_\sigma g_{\nu\rho}\right)\dot x^\nu\dot x^\rho=0
\;\Longleftrightarrow\;
\boxed{\ddot x^\mu+\Gamma^\mu{}_{\nu\rho}\dot x^\nu\dot x^\rho=0.}\qquad\square$$

**为什么 $\lambda$ 是仿射参数**：第一步用了"$\sqrt F$ 是常数"。若 $\lambda$ 不是仿射的，$\sqrt F$ 沿曲线不是常数，$\delta\int\sqrt F$ 与 $\delta\int F$ 不等价，方程会多出 $\propto\dot x^\mu$ 的项。反过来，如果方程写成 $\ddot x+\Gamma\dot x\dot x=\kappa\dot x$，重参数化 $\lambda\to\tilde\lambda(\lambda)$ 可以消掉 $\kappa$——这就是"仿射参数存在且唯一到 $a\lambda+b$"。

**两个补充**：

1. **零曲线**：$F=0$，第一步退化。此时直接用自平行方程 $\ddot x+\Gamma\dot x\dot x=0$（它自动保持 $F=0$：$\frac{d}{d\lambda}(g\dot x\dot x)=2g\dot x(\ddot x+\Gamma\dot x\dot x)=0$）。
2. **为什么是极大不是极小**：号差 $(-,+,+,+)$ 下 $F\gt0$ 对应类时；把 $S'$ 变到二阶会看到二阶变分的符号是负的（在平直空间里直线的 $\tau$ 最长）。这是洛伦兹号差的"反直觉"之一，第 6 章的黑洞轨道会再用到。

</details>

**5.** 在单位球面 $ds^2=d\theta^2+\sin^2\theta\,d\phi^2$ 上，把矢量沿纬度圈 $\theta=\theta_0$ 平行移动一圈。算出分量的转动角与物理和乐角，并检验赤道与 $\theta_0\to0$ 两个极限。

<details markdown="1"><summary>点击显示答案</summary>

**平行移动方程**：切矢是 $\partial_\phi$，$\mathrm{d}x^\phi/\mathrm{d}\phi=1$，$\mathrm{d}x^\theta/\mathrm{d}\phi=0$。于是

$$\frac{\mathrm{d}V^\theta}{\mathrm{d}\phi}+\Gamma^\theta{}_{\phi\phi}V^\phi=0
\;\Rightarrow\;\dot V^\theta=\sin\theta_0\cos\theta_0\,V^\phi,$$

$$\frac{\mathrm{d}V^\phi}{\mathrm{d}\phi}+\Gamma^\phi{}_{\phi\theta}V^\theta=0
\;\Rightarrow\;\dot V^\phi=-\cot\theta_0\,V^\theta .$$

（用了自检 3 的克氏符。）

**解**：对第一式再求导并代入第二式：

$$\ddot V^\theta=\sin\theta_0\cos\theta_0\,\dot V^\phi=-\cos^2\theta_0\,V^\theta .$$

故

$$V^\theta(\phi)=A\cos(\phi\cos\theta_0)+B\sin(\phi\cos\theta_0),$$

$V^\phi$ 由 $\dot V^\theta$ 给出。绕一圈 $\phi:0\to2\pi$：

$$V^\theta(2\pi)=A\cos(2\pi\cos\theta_0)+B\sin(2\pi\cos\theta_0).$$

**分量的转动角**：$\boxed{2\pi\cos\theta_0}$。$\square$

**物理和乐角**：分量是在基 $(\partial_\theta,\partial_\phi)$ 里写的，而基本身绕了一圈（$\partial_\phi$ 转了 $2\pi$）。所以物理转角是

$$\boxed{\Delta=2\pi-2\pi\cos\theta_0=2\pi\left(1-\cos\theta_0\right).}$$

**识别**：单位球面上纬度圈围出的球冠面积正是

$$A_{\rm cap}=\int_0^{2\pi}\mathrm{d}\phi\int_0^{\theta_0}\sin\theta\,\mathrm{d}\theta=2\pi\left(1-\cos\theta_0\right).$$

所以**和乐角 = 所围面积**——这就是 Gauss–Bonnet 的球面版本，也是第 3 章"曲率 = 单位面积的和乐"的定量依据。$\square$

**两个极限**：

- **赤道** $\theta_0=\pi/2$：$\Delta=2\pi$，即恒等变换。赤道是测地线，沿测地线平行移动当然不转动（物理上"没有转动"）。分量转了 $2\pi\cos(\pi/2)=0$，而基转了 $2\pi$，两者相抵 ✓。
- **小圆** $\theta_0\to0$：$\Delta\approx2\pi\cdot\frac{\theta_0^2}{2}=\pi\theta_0^2$ = 球冠面积 ✓。转角趋于零，说明北极附近曲率有限（与自检 3 的结论一致）。

**要点**：**分量转角的"$\cos\theta_0$"是坐标效应的一部分**；真正的几何信息是"$2\pi(1-\cos\theta_0)$"，它只依赖曲面本身的曲率，不依赖你选什么基。第 3 章会把这句话写成 $R^\mu{}_{\nu\rho\sigma}$ 的公式。

</details>

## 参考

- Wald《General Relativity》第 3.1–3.3 节（仿射联络、度规相容、克氏符、测地线、指数映射）。
- Carroll《Spacetime and Geometry》第 3 章（最清楚的入门推导；本章的克氏符推导与它一致）。
- Misner, Thorne & Wheeler《Gravitation》第 8–10 章（平行移动与和乐的几何图像）。
- Poisson《A Relativist's Toolkit》第 1 章（固有时与测地线的物理读法）。
- 第 1 章（流形与张量）、第 3 章（曲率与测地偏离）、第 6 章（Schwarzschild 的测地线）、第 8 章（零测地线作为生成元）。
