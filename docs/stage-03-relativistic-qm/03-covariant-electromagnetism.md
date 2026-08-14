# 电磁学的协变形式：F_μν 与规范势

> 路线图位置：第 3 阶段（经典场论 + 相对论量子力学，过渡桥梁）· 第 3 篇
> 前置知识：本科电动力学（三维形式的 Maxwell 方程、洛伦兹力）、狭义相对论（四维矢量、指标升降）、本阶段第二篇（场的拉格朗日形式）。
> 学习目标：把 Maxwell 方程从三维形式改写成四维协变形式；掌握规范势 $A^\mu$、场强张量 $F_{\mu\nu}$、两条协变 Maxwell 方程、场的洛伦兹变换与两个不变量；理解规范自由度的物理含义（含 Aharonov–Bohm 效应），为 QED 的规范原理铺路。

---

## 1. 一句话总结

**电场和磁场不是两个独立的场，而是同一个反对称四维张量 $F_{\mu\nu}$ 在不同参考系里的不同"切片"：一旦把 $\vec E$、$\vec B$ 打包成 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$，四个 Maxwell 方程坍缩成两条——含源的 $\partial_\mu F^{\mu\nu}=J^\nu$ 和恒等式 $\partial_{[\lambda}F_{\mu\nu]}=0$；场的变换、洛伦兹力、能量传输全都变成透明的四维张量运算，而规范势 $A_\mu$ 的冗余（规范自由度）将在量子理论里升格为整个 QED 的构造原理。**

下面把这句话逐层拆开。全章取自然单位 $c=1$（首次出现处会注明恢复 $c$ 的方式），采用 Heaviside–Lorentz 约定（即 $\mu_0=\epsilon_0=1$，库仑定律写成 $\vec F=q_1q_2\hat r/4\pi r^2$），度规号差 $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$，与路线图的其余笔记一致。

## 2. 三维形式的 Maxwell 方程：问题在哪

先回顾真空以外、含源的四个 Maxwell 方程（Heaviside–Lorentz 单位制，$c=1$）：

$$\nabla\cdot\vec E = \rho, \qquad \nabla\times\vec B - \partial_t\vec E = \vec J,$$

$$\nabla\cdot\vec B = 0, \qquad \nabla\times\vec E + \partial_t\vec B = 0.$$

这四个方程在牛顿力学的伽利略变换下**形式会变**，但在洛伦兹变换下保持不变——正是这个矛盾催生了狭义相对论。三维写法把问题掩盖了：它把 $\vec E$ 和 $\vec B$ 当成两个独立的三维矢量，但 Einstein 在 1905 年论文开头就指出，运动电荷与磁铁的实验里，"谁是电场、谁是磁场"取决于观测者：

- **磁铁静止、线圈运动**：线圈中的电荷在磁场里运动，受洛伦兹力 $q\vec v\times\vec B$，被解释为"磁力"；
- **线圈静止、磁铁运动**：同一段导线里测到的却是变化的磁场感应出的**电场** $\nabla\times\vec E=-\partial_t\vec B$。

两种描述给出完全相同的电流。"电场"与"磁场"的区分是**依赖参考系的**，就像"空间"与"时间"的区分依赖参考系一样。协变化的目标：找到一个四维对象，把 $\vec E$、$\vec B$ 统一装进去，使 Maxwell 方程写成在洛伦兹变换下逐项形式不变的张量方程。

## 3. 四维流与电荷守恒

先处理源。电荷密度 $\rho$ 与电流密度 $\vec J$ 打包成**四维流**

$$J^\mu = (\rho,\ \vec J), \qquad \text{即 } J^0=\rho,\ J^i = J^i.$$

它确实是四维矢量：$\rho$ 是"单位体积的电荷"，体积元因洛伦兹收缩变小、电荷总量不变，$\rho$ 像四矢量的时间分量那样变换；$\vec J=\rho\vec u$ 则像空间分量。

电荷守恒的三维写法是连续性方程 $\partial_t\rho+\nabla\cdot\vec J=0$。用四维记号，这正是

$$\boxed{\partial_\mu J^\mu = \partial_t\rho + \partial_i J^i = 0}$$

——一个洛伦兹标量方程：电荷守恒在所有惯性系里长得一模一样。注意这里 $\partial_\mu=\partial/\partial x^\mu=(\partial_t,\ \nabla)$ 是协变指标，空间部分带正号（度规号差 $(+,-,-,-)$ 下 $\partial^\mu=(\partial_t,-\nabla)$，别混淆）。

## 4. 规范势 $A^\mu$

### 4.1 从齐次方程到势

Maxwell 方程里的两个**齐次**方程（$\nabla\cdot\vec B=0$ 与 $\nabla\times\vec E=-\partial_t\vec B$）不含源，它们的作用是让势的存在成为可能：

- $\nabla\cdot\vec B=0$ ⟹ 存在矢量场 $\vec A$，使 $\vec B=\nabla\times\vec A$（无散场是旋度场）；
- 代入法拉第定律：$\nabla\times(\vec E+\partial_t\vec A)=0$ ⟹ 无旋场是梯度场，存在标量 $\phi$，使 $\vec E+\partial_t\vec A=-\nabla\phi$。

合起来：

$$\boxed{\vec B = \nabla\times\vec A, \qquad \vec E = -\nabla\phi - \partial_t\vec A}$$

这两条自动满足两个齐次 Maxwell 方程（梯度无旋、旋度无散），代价是引入了 $\phi$ 与 $\vec A$。把它们打包：

$$A^\mu = (\phi,\ \vec A), \qquad A_\mu = \eta_{\mu\nu}A^\nu = (\phi,\ -\vec A).$$

（可以验证 $A^\mu$ 确实是四维矢量——例如 $\phi$ 和 $\vec A$ 满足的波动方程在洛伦兹变换下协变，见 4.3 节。）

### 4.2 规范自由度：冗余，不是对称性

给定 $(\vec E,\vec B)$，势并不唯一。取任意标量函数 $\alpha(x)$，做变换

$$A_\mu \;\longrightarrow\; A_\mu + \partial_\mu\alpha,$$

三维写法即 $\phi\to\phi+\partial_t\alpha$、$\vec A\to\vec A-\nabla\alpha$。代回 $\vec E,\vec B$：

$$\vec B \to \nabla\times(\vec A-\nabla\alpha) = \vec B - \nabla\times\nabla\alpha = \vec B,$$

$$\vec E \to -\nabla(\phi+\partial_t\alpha) - \partial_t(\vec A-\nabla\alpha) = \vec E.$$

场完全不变。这叫**规范变换**。关键点：规范变换不改变任何可观测量，所以它不是普通意义上的"对称性"（对称性是不同物理状态之间的等价映射，往往对应守恒荷），而是**描述的冗余**——$(\phi,\vec A)$ 比物理实在多了一个函数的自主权。用规范场论的语言：物理位形空间是势的空间**除以**规范变换。这个看似技术性的观察将在 QED 篇（[QED：旋量场、光子场与规范不变性](../stage-04-qft-core/05-qed.md)）中反转为核心原理：要求理论在**局域**规范变换 $\alpha(x)$ 下不变，反过来强制了 $A_\mu$ 的存在及其与物质场的耦合形式。

### 4.3 Lorenz 规范与波动方程

利用规范自由度，总可以要求

$$\partial_\mu A^\mu = 0 \qquad\text{（Lorenz 规范）},$$

三维写法即 $\partial_t\phi+\nabla\cdot\vec A=0$。把两个含源 Maxwell 方程用势改写，在此规范下交叉导数项消去，得到四个退耦的非齐次波动方程：

$$\Box\, A^\mu = J^\mu, \qquad \Box \equiv \partial_\mu\partial^\mu = \partial_t^2 - \nabla^2.$$

（推导：$\partial_\mu F^{\mu\nu}=\partial_\mu\partial^\mu A^\nu-\partial^\nu(\partial_\mu A^\mu)=\Box A^\nu$，第二项被 Lorenz 条件杀死。）无源时 $\Box A^\mu=0$ 的解是平面波——光的波动性就藏在 Maxwell 理论里，且波速恒为 1（恢复单位即 $c$），与参考系无关。注意规范条件仍未用尽自由度：再加一个满足 $\Box\alpha=0$ 的 $\alpha$ 不破坏 Lorenz 条件，这部分剩余自由度在量子化时与光子的两个横向偏振密切相关。

### 4.4 Aharonov–Bohm 效应：势是"真"的吗

经典层面，$\vec A$ 只是计算工具——有规范任意性的量通常不物理。但量子力学里，带电粒子在矢势中获得的相位是

$$\varphi = q\int \vec A\cdot d\vec x \qquad (\hbar=1;\ \text{恢复单位为 } \varphi = q\int\vec A\cdot d\vec x/\hbar).$$

Aharonov–Bohm（1959，实验验证见 Chambers 1960 与 Tonomura 等的电子全息实验）：无限长理想螺线管，内部有磁场 $\vec B$，外部 $\vec B=0$ 但 $\vec A\neq 0$（环绕螺线管打转）。让电子双缝干涉，两束分别从螺线管两侧绕行——两束全程都处于 $\vec B=0$ 的区域，不受任何洛伦兹力，但干涉条纹的相对相位差为

$$\Delta\varphi = q\oint \vec A\cdot d\vec x = q\,\Phi,$$

其中 $\Phi$ 是螺线管内的磁通（Stokes 定理）。改变 $\Phi$ 条纹就移动——实验上看得清清楚楚。

教训分两层：

1. $\vec A$ **不只是**数学工具——它在 $\vec B=0$ 处产生可测效应；三维的 $\vec E,\vec B$ 作为局域场量的描述并不完备。
2. 但真正物理的仍是**规范不变量**：单个 $\vec A$ 的值没有意义（可加任意梯度），有意义的是环路积分 $q\oint\vec A\cdot d\vec x$（holonomy / Wilson loop 的电磁版本），它等于磁通、规范变换下不变。

到了非阿贝尔规范理论（Yang–Mills），Wilson loop 将升格为基本可观测量之一。这是后话，先在电磁学里把直觉建好。

## 5. 场强张量 $F_{\mu\nu}$

### 5.1 定义与矩阵形式

势的规范冗余提示：物理含量在势的"旋度"里。定义**场强张量**（电磁张量）

$$\boxed{F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu}$$

三条立刻可验证的性质：

- **反对称**：$F_{\mu\nu}=-F_{\nu\mu}$，故 $4\times 4$ 反对称张量只有 $\binom{4}{2}=6$ 个独立分量——恰好 3 个 $\vec E$ + 3 个 $\vec B$；
- **规范不变**：$A_\mu\to A_\mu+\partial_\mu\alpha$ 时 $F_{\mu\nu}$ 多了 $\partial_\mu\partial_\nu\alpha-\partial_\nu\partial_\mu\alpha=0$（偏导可对易）；
- 分量直接给出场：$F_{0i}=\partial_t A_i-\partial_i A_0=-\partial_t A^i-\partial_i\phi=E^i$，$F_{ij}=-(\partial_i A^j-\partial_j A^i)=-\epsilon_{ijk}B^k$。

升上指标（$F^{0i}=\eta^{00}\eta^{ii}F_{0i}=-E^i$，$F^{ij}=F_{ij}$），写成矩阵（行 $\mu$、列 $\nu$）：

$$F^{\mu\nu} = \begin{pmatrix}
0 & -E_x & -E_y & -E_z\\
E_x & 0 & -B_z & B_y\\
E_y & B_z & 0 & -B_x\\
E_z & -B_y & B_x & 0
\end{pmatrix},
\qquad\text{即 } F^{0i}=-E^i,\ \ F^{ij}=-\epsilon_{ijk}B^k.$$

（若用 $(-+++)$ 号差，矩阵整体差一个负号——这是号差约定的常见坑，本路线图统一 $(+---)$。）

### 5.2 Maxwell 方程坍缩成两条

**含源方程**：

$$\boxed{\partial_\mu F^{\mu\nu} = J^\nu}$$

- $\nu=0$：$\partial_i F^{i0}=\partial_i E^i=\nabla\cdot\vec E=\rho$ ——Gauss 定律；
- $\nu=i$：$\partial_t F^{0i}+\partial_j F^{ji}=-\partial_t E^i+(\nabla\times\vec B)^i=J^i$ ——Ampère–Maxwell 定律。

**齐次方程** = Bianchi 恒等式：

$$\boxed{\partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0}$$

它不是动力学方程，而是 $F$ 由势给出（$F=dA$，"旋度的旋度"类结构）带来的**恒等式**：把 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ 代入，六项两两抵消。逐个指标选取：

- $(\lambda\mu\nu)=(ijk)$ 全取空间：$\partial_i F_{jk}+\partial_j F_{ki}+\partial_k F_{ij}=-2\nabla\cdot\vec B=0$ ——无磁单极；
- $(0ij)$：$\partial_t F_{ij}+\partial_i F_{j0}+\partial_j F_{0i}=-\epsilon_{ijk}\partial_t B^k + (\partial_i E^j-\partial_j E^i)=0$，即 $\nabla\times\vec E=-\partial_t\vec B$ ——法拉第定律。

**四条 Maxwell 方程 = 一条张量方程 + 一条恒等式。** 这就是协变化的全部分红。

## 6. 场的洛伦兹变换与不变量

### 6.1 张量变换规则

$F^{\mu\nu}$ 是真二阶张量，洛伦兹变换下

$$F'^{\mu\nu} = \Lambda^\mu_{\ \rho}\,\Lambda^\nu_{\ \sigma}\,F^{\rho\sigma}.$$

取沿 $x$ 方向、速度 $v$ 的 boost（$\gamma=1/\sqrt{1-v^2}$），逐分量代入即得（自检问题 3 会亲手算一个分量）：

$$E'_\parallel = E_\parallel, \qquad B'_\parallel = B_\parallel,$$

$$\vec E'_\perp = \gamma\big(\vec E + \vec v\times\vec B\big)_\perp, \qquad \vec B'_\perp = \gamma\big(\vec B - \vec v\times\vec E\big)_\perp,$$

其中 $\parallel$、$\perp$ 相对 boost 方向。写成显式分量（boost 沿 $x$）：$E'_y=\gamma(E_y-vB_z)$，$B'_z=\gamma(B_z-vE_y)$ 等。**电场和磁场在 boost 下互相混合**——这正是第 2 节"运动电荷与磁铁"佯谬的定量解答：一个参考系里的纯 $\vec E$，换个系就是 $\vec E$ 加 $\vec B$ 的混合。Einstein 1905 年论文的标题《论动体的电动力学》说的就是这个。

### 6.2 两个洛伦兹不变量

由 $F$ 能造出两个独立的标量（收缩全部指标）：

$$F_{\mu\nu}F^{\mu\nu} = 2\big(\vec B^2 - \vec E^2\big), \qquad
F_{\mu\nu}\tilde F^{\mu\nu} = -4\,\vec E\cdot\vec B,$$

其中**对偶张量** $\tilde F^{\mu\nu}=\frac12\epsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}$（$\epsilon^{0123}=+1$），效果是把 $\vec E\leftrightarrow\vec B$ 互换（差号差与符号约定）。

**应用**：不变量在所有系同值，所以它们直接判定"能不能找到一个特殊参考系"——

- 若 $\vec E\cdot\vec B\neq 0$：任何参考系里两者都不垂直，**不存在**纯电场或纯磁场系；
- 若 $\vec E\cdot\vec B=0$ 且 $\vec B^2-\vec E^2<0$：可找到一个系使 $\vec B'=0$（纯电场系）；$\vec B^2-\vec E^2>0$ 时则存在纯磁场系；
- 若两者都为零（$\vec E\cdot\vec B=0$ 且 $\vec B^2=\vec E^2$）：任何系里都垂直且等值——这正是**平面电磁波**（$c=1$ 下 $|\vec E|=|\vec B|$，恢复单位是 $|\vec E|=c|\vec B|$）。"$\vec E\perp\vec B$、$|\vec E|=|\vec B|$"是洛伦兹不变性质，不可能通过换系把光波"变没"。

<details markdown="1"><summary>补充说明：不变量的来历与第三不变量之缺席</summary>

一个反对称二阶张量在洛伦兹群下的独立不变量为什么恰好是两个？线性代数的说法：$F$ 作为 $4\times 4$ 反对称矩阵，洛伦兹变换相当于"相似变换"的推广，本征值结构由特征多项式的系数刻画；反对称矩阵的特征多项式是偶次的，只有两个独立系数，分别正比于 $\vec B^2-\vec E^2$ 与 $(\vec E\cdot\vec B)^2$。群论的说法：在复化后，$F$ 等价于两个 SU(2) 三元组（自对偶/反自对偶部分），每个贡献一个不变量，合起来就是上面两个实不变量。

"没有第三个不变量"有直接的物理推论：只靠不变量就能完全分类电磁场的"代数类型"（纯辐射场 vs 可化为纯电场/磁场的场等），这正是上面三条应用的依据。

</details>

## 7. 带电粒子的协变运动方程

最后处理"带电粒子在场中如何运动"。三维的洛伦兹力 $\vec F=q(\vec E+\vec v\times\vec B)$ 不是四维矢量的分量形式，但下面这个方程是：

$$\boxed{\frac{dp^\mu}{d\tau} = q\,F^\mu_{\ \nu}\,u^\nu}$$

其中 $\tau$ 是固有时，$u^\mu=dx^\mu/d\tau=\gamma(1,\vec v)$ 是四维速度，$p^\mu=mu^\mu$。右边是四维矢量（张量缩并），左边也是——方程协变。验证它的分量：

**空间分量**（$F^i_{\ 0}=E^i$，$F^i_{\ j}=-F^{ij}=\epsilon_{ijk}B^k$）：

$$\frac{dp^i}{d\tau} = q\big(E^i\,\gamma + \epsilon_{ijk}B^k\,\gamma v^j\big)
\;\Longrightarrow\;
\frac{d\vec p}{dt} = q\big(\vec E + \vec v\times\vec B\big).$$

正是洛伦兹力。**时间分量**（$F^0_{\ i}=-F^{0i}=E^i$）：

$$\frac{dp^0}{d\tau} = q\,\vec E\cdot\gamma\vec v
\;\Longrightarrow\;
\frac{dE_{\text{粒子}}}{dt} = q\,\vec E\cdot\vec v.$$

即功率公式：只有电场做功，磁场力恒垂直于速度、不改变粒子能量。三维理论里这是两条分开的陈述，协变形式里它们是同一个方程的不同分量。

<details markdown="1"><summary>补充说明：这条方程从哪里推出</summary>

它不是凭空写的。带电粒子的作用量取

$$S = -m\int d\tau - q\int A_\mu\,dx^\mu,$$

第二项是规范不变的（规范变换只给作用量加边界项，不影响运动方程）。对 $x^\mu(\tau)$ 变分即得 $dp^\mu/d\tau=qF^\mu_{\ \nu}u^\nu$。反过来，要求"粒子拉氏量在规范变换下不变"几乎唯一地决定了 $A_\mu$ 以**最小耦合**形式进入——这正是 QED 规范原理在经典力学里的预演。粒子与场的完整闭合系统（粒子的 $J^\mu$ 又作为 Maxwell 方程的源）由拉氏量 $\mathcal L = -\frac14 F^2 - J\cdot A$ 加粒子项统一描述，见下节。

</details>

## 8. 与前后文的衔接

- **回看第 2 篇**（[场的拉格朗日形式](02-lagrangian-field-theory.md)）：电磁场的拉氏密度

$$\mathcal L = -\frac14 F_{\mu\nu}F^{\mu\nu} - J^\mu A_\mu$$

对 $A_\mu$ 做欧拉–拉格朗日变分即得 $\partial_\mu F^{\mu\nu}=J^\nu$（$-\frac14$ 的归一化使动能项系数为 $+\frac12(\partial_t\vec A)^2$，即正则动量正是 $\vec E$）。Maxwell 理论是一个标准的经典场论，本篇的所有方程都是那篇机器的产出。
- **往前看**：$A_\mu$ 量子化后，其平面波激发就是**光子**；规范原理 $\psi\to e^{iq\alpha(x)}\psi$、$A_\mu\to A_\mu+\partial_\mu\alpha$ 将反过来成为构造 QED 拉氏量的出发点，见第 4 阶段 [QED 篇](../stage-04-qft-core/05-qed.md)。
- 相互作用项 $-J^\mu A_\mu$ 在 Dirac 理论里即 $-q\bar\psi\gamma^\mu\psi A_\mu$，它就是 QED 费曼图里那个唯一的顶点的经典化身。

## 小结

| 三维对象 | 四维对象 | 对应方程 |
|---|---|---|
| $\rho,\ \vec J$ | 四维流 $J^\mu=(\rho,\vec J)$ | 电荷守恒 $\partial_\mu J^\mu=0$ |
| $\phi,\ \vec A$ | 规范势 $A^\mu=(\phi,\vec A)$ | Lorenz 规范 $\partial_\mu A^\mu=0$ 下 $\Box A^\mu=J^\mu$；规范冗余 $A_\mu\to A_\mu+\partial_\mu\alpha$ |
| $\vec E,\ \vec B$ | 场强张量 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$（$F^{0i}=-E^i$，$F^{ij}=-\epsilon_{ijk}B^k$） | $\partial_\mu F^{\mu\nu}=J^\nu$（Gauss + Ampère–Maxwell）；Bianchi $\partial_\lambda F_{\mu\nu}+\text{循环}=0$（无磁单极 + 法拉第） |
| $\vec E\leftrightarrow\vec B$ 依参考系混合 | $F'^{\mu\nu}=\Lambda^\mu_{\ \rho}\Lambda^\nu_{\ \sigma}F^{\rho\sigma}$ | 不变量 $F^2=2(\vec B^2-\vec E^2)$、$F\tilde F=-4\,\vec E\cdot\vec B$ |
| 洛伦兹力 + 功率 | $dp^\mu/d\tau=qF^\mu_{\ \nu}u^\nu$ | 空间分量 $\dot{\vec p}=q(\vec E+\vec v\times\vec B)$；时间分量 $\dot E=q\vec E\cdot\vec v$ |
| 矢势的环路积分 | 规范不变相位（holonomy） | Aharonov–Bohm：$\Delta\varphi=q\oint\vec A\cdot d\vec x=q\Phi$ |

## 自检问题

**1.** 从 $\partial_\mu F^{\mu\nu}=J^\nu$ 出发，分别取 $\nu=0$ 与 $\nu=i$，拆出 Gauss 定律与 Ampère–Maxwell 定律，并说明位移电流项在哪个位置出现。

<details markdown="1"><summary>点击显示答案</summary>

约定 $F^{0i}=-E^i$、$F^{ij}=-\epsilon_{ijk}B^k$，且 $\partial_\mu=(\partial_t,\nabla)$、$J^\mu=(\rho,\vec J)$。

**$\nu=0$**：$F^{00}=0$（反对称），只剩空间求和：

$$\partial_\mu F^{\mu 0}=\partial_i F^{i0}=\partial_i(+E^i)=\nabla\cdot\vec E = J^0=\rho.$$

即 Gauss 定律 $\nabla\cdot\vec E=\rho$。

**$\nu=i$**：时间项与空间项都出现：

$$\partial_\mu F^{\mu i}=\partial_t F^{0i}+\partial_j F^{ji}=-\partial_t E^i+\partial_j(-\epsilon_{jik}B^k).$$

注意 $\partial_j\epsilon_{jik}B^k=\epsilon_{jik}\partial_j B^k=(\nabla\times\vec B)^i$（用 $\epsilon_{jik}=-\epsilon_{ijk}$ 配合叉乘定义验算）。于是

$$-\partial_t E^i+(\nabla\times\vec B)^i = J^i \;\Longrightarrow\; \nabla\times\vec B=\vec J+\partial_t\vec E.$$

即 Ampère–Maxwell 定律。**位移电流** $\partial_t\vec E$ 就是 $F^{0i}$ 的时间导数项：它来自场强张量的电分量，而不是磁分量——Maxwell 补上的那一项在协变形式里被自动包含，因为 $\partial_\mu$ 对时间和空间一视同仁。

</details>

**2.** 从 Bianchi 恒等式 $\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0$ 拆出 $\nabla\cdot\vec B=0$ 与法拉第定律。

<details markdown="1"><summary>点击显示答案</summary>

用下指标分量 $F_{0i}=E^i$、$F_{ij}=-\epsilon_{ijk}B^k$。指标全同或重复的选取给出 $0=0$，非平凡的只有两类。

**全空间指标 $(\lambda\mu\nu)=(123)$**：

$$\partial_1 F_{23}+\partial_2 F_{31}+\partial_3 F_{12}
= \partial_1(-B^1)+\partial_2(-B^2)+\partial_3(-B^3) = -\nabla\cdot\vec B = 0,$$

即 $\nabla\cdot\vec B=0$（这里用到 $F_{23}=-\epsilon_{231}B^1=-B^1$ 等，$\epsilon_{231}=+1$）。

**一个时间指标，取 $(\lambda\mu\nu)=(0ij)$，$i,j$ 固定**：

$$\partial_t F_{ij}+\partial_i F_{j0}+\partial_j F_{0i}
= -\epsilon_{ijk}\partial_t B^k - \partial_i E^j + \partial_j E^i = 0.$$

两边乘 $\epsilon_{ijl}$ 并对 $i,j$ 求和，用 $\epsilon_{ijl}\epsilon_{ijk}=2\delta_{lk}$ 与 $\epsilon_{ijl}(\partial_j E^i-\partial_i E^j)=-2(\nabla\times\vec E)^l$，得

$$-2\,\partial_t B^l - 2(\nabla\times\vec E)^l = 0
\;\Longrightarrow\;
\nabla\times\vec E = -\partial_t\vec B.$$

即法拉第电磁感应定律。物理上，这两条之所以是恒等式而非动力学方程，是因为它们只反映"场由势给出"：$F=dA$ 自动满足 $dF=0$（微分形式语言里 $d^2=0$）。

</details>

**3.** 某参考系里只有纯电场 $\vec E=(0,E,0)$（沿 $y$），$\vec B=0$。求沿 $x$ 方向以速度 $v$ boost 后的场，验证变换公式 $B'_z=\gamma(B_z-vE_y)$ 这一个分量。

<details markdown="1"><summary>点击显示答案</summary>

沿 $x$ 的 boost：

$$\Lambda^\mu_{\ \nu} = \begin{pmatrix}
\gamma & -\gamma v & 0 & 0\\
-\gamma v & \gamma & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix}.$$

原系中 $F^{\mu\nu}$ 只有 $F^{02}=-E$、$F^{20}=+E$ 非零。计算 $F'^{32}=\Lambda^3_{\ \rho}\Lambda^2_{\ \sigma}F^{\rho\sigma}$：$\Lambda^3_{\ \rho}=\delta^3_{\ \rho}$，$\Lambda^2_{\ \sigma}=\delta^2_{\ \sigma}$，所以

$$F'^{32}=F^{32}=0 \;\Longrightarrow\; B'_x = 0.$$

计算 $F'^{21}$（应等于 $-B'_z$，因 $F^{21}=-\epsilon_{213}B^3=+B^3$ 的相反约定：$F^{21}=-\epsilon_{213}B_z$，$\epsilon_{213}=-1$，故 $F^{21}=B_z$）：

$$F'^{21}=\Lambda^2_{\ \rho}\Lambda^1_{\ \sigma}F^{\rho\sigma}=\Lambda^2_{\ 2}\Lambda^1_{\ 0}F^{20}
=1\cdot(-\gamma v)\cdot E = -\gamma v E.$$

由 $F'^{21}=B'_z$（见上）得

$$\boxed{B'_z = -\gamma v E}$$

与公式 $B'_z=\gamma(B_z-vE_y)=\gamma(0-vE)=-\gamma vE$ 一致。同时 $F'^{02}=\Lambda^0_{\ \rho}\Lambda^2_{\ \sigma}F^{\rho\sigma}=\gamma\cdot 1\cdot(-E)$，即 $E'_y=\gamma E$。

物理读法：新系里看到沿 $y$ 的电场被增强到 $\gamma E$，并且凭空出现沿 $z$ 的磁场 $\vec B'=\gamma\,\vec v\times\vec E$ 的对应分量。这正是"运动电荷周围既有电场又有磁场"的原因：静止系里只有电场的电荷，换到它运动的参考系，就必须同时有磁场——磁力不过是电力在洛伦兹变换下的另一半面孔。

</details>

**4.** 某区域中 $\vec E\cdot\vec B\neq 0$。证明：不存在任何惯性系使该处为纯磁场（$\vec E'=0$）或纯电场（$\vec B'=0$）。再说明 $\vec E\cdot\vec B=0$ 且 $\vec E^2>\vec B^2$ 时纯电场系存在，并指出如何找到它。

<details markdown="1"><summary>点击显示答案</summary>

两个洛伦兹不变量

$$I_1 = \vec B^2-\vec E^2, \qquad I_2 = \vec E\cdot\vec B$$

在所有惯性系取相同值（它们分别是 $-\frac12 F_{\mu\nu}F^{\mu\nu}$ 与 $-\frac14 F_{\mu\nu}\tilde F^{\mu\nu}$ 的三维写法）。

**第一部分**：设存在某系使 $\vec E'=0$（纯磁场），则在该系 $I_2=\vec E'\cdot\vec B'=0$。由不变性，原系也必须有 $\vec E\cdot\vec B=0$，与假设矛盾。纯电场情形（$\vec B'=0\Rightarrow I_2=0$）同理。所以 $\vec E\cdot\vec B\neq 0$ 时两种"纯"参考系都不存在——任何观测者都同时看到电场和磁场，且永不垂直。

**第二部分**：设 $\vec E\cdot\vec B=0$（故 $\vec E\perp\vec B$）且 $I_1<0$。取 boost 方向沿 $\vec E\times\vec B$（与两场都垂直），速度大小待定。因场与 boost 方向垂直，用垂直分量公式：

$$\vec E' = \gamma(\vec E+\vec v\times\vec B), \qquad \vec B' = \gamma(\vec B-\vec v\times\vec E).$$

取 $\hat v\parallel\vec E\times\vec B$，则 $\vec v\times\vec B$ 沿 $-\vec E$ 方向（验右手定则），$\vec v\times\vec E$ 沿 $+\vec B$ 方向。令 $\vec E'=0$ 的条件是 $\vec v\times\vec B=-\vec E$，即 $vB=E$（$v=E/B$）。由于 $E^2>B^2$ 时 $v=E/B>1$，超光速、不可能——这正对应 $I_1>0$ 时只能找到纯磁场系（取 $v=B/E<1$ 使 $\vec B'=0$ 的对偶情形）。**本题 $E^2>B^2$，应反过来令 $\vec B'=0$**：$\vec v\times\vec E=\vec B$，即 $v=B/E<1$，合法。于是 boost 到以 $v=B/E$ 沿 $\vec E\times\vec B$ 方向运动的系，$\vec B'=0$、$\vec E'=\gamma(\vec E+\vec v\times\vec B)\neq 0$——纯电场系存在。

临界情形 $E=B$（且垂直）：$v=1$，只有光速 boost，任何有质量观测者都到不了——这就是平面电磁波无法被"变没"的原因。

</details>

**5.** 电子双缝干涉装置中，在双缝后方放置一根垂直于电子束平面的无限长理想螺线管（半径 $a$，内部磁通 $\Phi$，外部 $\vec B=0$）。电子从两侧绕行。求两束的相对相位差，并说明：为什么这个效应不违反"电子全程不受力"？为什么它证明 $\vec A$ 比 $\vec B$ "更基本"，又不与规范任意性矛盾？

<details markdown="1"><summary>点击显示答案</summary>

**势与相位**：螺线管外 $\vec B=\nabla\times\vec A=0$，但 $\vec A\neq 0$。取柱坐标，对称性给出

$$\vec A = \frac{\Phi}{2\pi r}\,\hat\varphi \qquad (r>a),$$

验证：$\oint\vec A\cdot d\vec x=\frac{\Phi}{2\pi r}\cdot 2\pi r=\Phi=\int\vec B\cdot d\vec S$（Stokes），且 $r>a$ 处旋度为零。

带电粒子在电磁场中的波函数沿路径 $\gamma$ 获得相位 $q\int_\gamma\vec A\cdot d\vec x$（$\hbar=1$；恢复单位为 $q\int\vec A\cdot d\vec x/\hbar$，电子 $q=-e$）。上路 $\gamma_1$ 与下路 $\gamma_2$ 合起来构成绕螺线管的闭合环路，故相对相位差

$$\Delta\varphi = q\left(\int_{\gamma_1}-\int_{\gamma_2}\right)\vec A\cdot d\vec x
= q\oint \vec A\cdot d\vec x = q\,\Phi
\;\;\xrightarrow{\text{恢复单位}}\;\; \frac{q\Phi}{\hbar}.$$

磁通每改变 $\Delta\Phi=2\pi\hbar/|e|=h/e$（磁通量子，超导中是 $h/2e$），条纹移动一个整周期——实验（Tonomura 等，电子全息，1986）精确证实。

**三个概念要点**：

1. **不违反"不受力"**：经典力确实为零（$\vec B=0\Rightarrow$ 无洛伦兹力），经典轨道上没有任何效应。相位是**量子**效应：波函数遍布两条路径，它探测的是 $\vec A$ 沿环路的整体性质，不是局域的力。
2. **$\vec A$ 更基本**：只用 $\vec E,\vec B$ 的局域描述无法解释该效应（两场在电子经过处都为零）；$\vec A$ 的描述可以。在这个意义上势承载了 $\vec B$ 之外的物理信息（区域拓扑非平庸：外部区域不是单连通的，无散的 $\vec A$ 不必全局是梯度）。
3. **与规范任意性不矛盾**：可测的是闭合环路积分 $q\oint\vec A\cdot d\vec x$，规范变换 $A_\mu\to A_\mu+\partial_\mu\alpha$ 给它加 $q\oint d\alpha$；只要 $\alpha$ 单值，这就是零。物理可观测量是规范不变的 holonomy（Wilson loop），不是某点的 $\vec A$。这正是第 4 节强调的："势不只是工具，但物理的是规范不变量。"

</details>

## 参考

- Purcell & Morin《电磁学》（Berkeley 物理教程卷 2）第 5–6 章——"电场与磁场的相对性"讲得最直观，运动电荷与磁铁的讨论即出于此。
- Griffiths《电动力学导论》第 10 章（势与规范）与第 12 章（电动力学与相对论）——$F^{\mu\nu}$、对偶张量、场变换与不变量的标准推导。
- Jackson《Classical Electrodynamics》第 11–12 章——协变电动力学的完备参考（注意其号差约定与本书单位制，读时对照本篇约定）。
- Landau & Lifshitz《场论》（卷 2）第 1–4 章——从最小作用量原理一气推出 $F_{\mu\nu}$、Maxwell 方程与洛伦兹力，与本篇第 7–8 节的风格最贴近。
- Goldstein《经典力学》相对论电动力学相关章节——带电粒子协变运动方程与作用量 $-m\int d\tau-q\int A\cdot dx$ 的推导。
