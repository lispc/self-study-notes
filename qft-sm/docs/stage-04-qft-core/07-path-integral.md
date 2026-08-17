# 路径积分表述：对所有历史求和

> 路线图位置：第 4 阶段（QFT 核心）· 第 7 篇，与算符形式的量子化笔记平行。
> 前置知识：量子力学（传播子、演化算符）、经典场论的作用量与 Euler–Lagrange 方程（见 ../stage-03-relativistic-qm/02-lagrangian-field-theory.md）。
> 学习目标：从量子力学的时间切片推出路径积分，掌握场论生成泛函 $Z[J]$ 的计算技术（高斯积分、Wick 定理、微扰展开），理解为什么费曼图可以从"对所有场历史求和"中自动长出来。

---

## 1. 一句话总结

**量子振幅等于对连接初末态的所有历史（路径、场构型）求和，每个历史贡献等模长的相位 $e^{iS/\hbar}$；经典极限下相位相消只留下满足 $\delta S=0$ 的那条历史，而微扰论的全部费曼规则——传播子、顶点、配对缩并——都可以从生成泛函 $Z[J]=\int\mathcal{D}\varphi\,e^{i(S+\int J\varphi)}$ 对源 $J$ 求导中机械地读出，与正则算符形式完全等价。**

下面把这句话逐层拆开。本文取自然单位 $\hbar=c=1$、度规号差 $\eta=\mathrm{diag}(+1,-1,-1,-1)$；在讨论经典极限的两节里会暂时把 $\hbar$ 恢复出来。

## 2. 量子力学复习：从传播子到路径积分

### 2.1 传播子

量子力学里，粒子从 $(x_a, t_a)$ 到 $(x_b, t_b)$ 的振幅是传播子

$$K(x_b, t_b; x_a, t_a) = \langle x_b |\, e^{-iH(t_b - t_a)}\, | x_a \rangle .$$

它包含了系统的全部动力学信息：本征值、本征函数、散射振幅都能从 $K$ 里提取。Feynman 的问题是：**能不能不经过希尔伯特空间和算符，直接用经典量（作用量）算出 $K$？**

### 2.2 时间切片推导（骨架）

设 $T = t_b - t_a$，把它 $N$ 等分，$\epsilon = T/N$，$t_j = t_a + j\epsilon$。利用演化算符的半群性质，在每个中间时刻插入位置本征态的完备基 $\int dx_j\,|x_j\rangle\langle x_j| = 1$：

$$K = \int dx_1 \cdots dx_{N-1}\ \prod_{j=0}^{N-1} \langle x_{j+1} | e^{-i\epsilon H} | x_j \rangle , \qquad x_0 = x_a,\ x_N = x_b.$$

关键一步是算单个无穷小矩阵元。对 $H = p^2/2m + V(x)$，当 $\epsilon \to 0$ 时动能与势能的不可对易性只贡献 $O(\epsilon^2)$（Baker–Campbell–Hausdorff），所以可以在该精度下把 $e^{-i\epsilon H}$ 拆成 $e^{-i\epsilon p^2/2m}e^{-i\epsilon V(x)}$。在中间插入动量完备基 $\int \frac{dp}{2\pi}|p\rangle\langle p|$，用 $\langle x|p\rangle = e^{ipx}$，得

$$\langle x_{j+1} | e^{-i\epsilon H} | x_j \rangle
= \int \frac{dp_j}{2\pi}\ \exp\Big\{ i\epsilon \Big[ p_j \frac{x_{j+1} - x_j}{\epsilon} - \frac{p_j^2}{2m} - V(x_j) \Big] \Big\} + O(\epsilon^2).$$

注意大括号里已经是**纯 c-number**：$p\dot x - H$。对 $p_j$ 的积分是高斯型（带 $i$ 的 Fresnel 积分，靠 $\epsilon \to \epsilon - i0$ 收敛），配方积出：

$$\langle x_{j+1} | e^{-i\epsilon H} | x_j \rangle
= \Big( \frac{m}{2\pi i\epsilon} \Big)^{1/2} \exp\Big\{ i\epsilon \Big[ \frac{m}{2}\Big(\frac{x_{j+1}-x_j}{\epsilon}\Big)^2 - V(x_j) \Big] \Big\}.$$

指数里出现了拉氏量 $L = \frac{m}{2}\dot x^2 - V$——**勒让德变换 $H \to L$ 是高斯积分配方的自动结果**，这是整个推导里最漂亮的一步。把 $N$ 个因子乘起来：

$$K = \lim_{N\to\infty} \Big( \frac{m}{2\pi i\epsilon} \Big)^{N/2} \int \prod_{j=1}^{N-1} dx_j\ \exp\Big\{ \frac{i}{\hbar} \sum_{j=0}^{N-1} \epsilon\, L(x_j, \dot x_j) \Big\}.$$

（这里把 $\hbar$ 恢复了，下面马上讨论它的作用。）求和在 $N\to\infty$ 时变成沿折线路径的作用量 $S[x] = \int_{t_a}^{t_b} L\,dt$。形式上记作

$$\boxed{K(x_b, t_b; x_a, t_a) = \int \mathcal{D}x\ e^{iS[x]/\hbar}}$$

其中"测度"

$$\mathcal{D}x \;\equiv\; \lim_{N\to\infty} \Big( \frac{m}{2\pi i\epsilon} \Big)^{N/2} \prod_{j=1}^{N-1} dx_j$$

是对所有满足端点条件 $x(t_a)=x_a$、$x(t_b)=x_b$ 的连续路径的求和。

<details markdown="1"><summary>补充说明：路径积分测度在数学上到底是什么</summary>

诚实地说：闵氏时空中 $e^{iS/\hbar}$ 是振荡的，路径空间上**不存在**通常意义（可数可加）的 Lebesgue 型测度使 $\int\mathcal{D}x\,e^{iS}$ 成为严格定义好的积分。数学上干净的做法是做 Wick 转动 $t \to -i\tau$：被积函数变成 $e^{-S_E/\hbar}$，此时确实存在严格的 **Wiener 测度**（布朗运动路径的测度，几乎所有路径连续但处处不可微——这与切片里 $\langle(\Delta x)^2\rangle \sim \epsilon$ 一致）。物理学家通常在欧氏空间算好再解析延拓回闵氏时空。另一种态度是把切片极限本身当作定义（Fresnel 积分意义下），配合 $i\epsilon$ 正则化，一切物理计算都自洽。学习阶段记住结论即可：**路径积分是一个有严格欧氏对应物的、计算上完全可靠的记号**。

</details>

## 3. 物理图像：相位相消与经典极限

### 3.1 所有路径等振幅

路径积分的第一条惊人之处：每条路径贡献的模长都是 $|\mathcal{D}x|$ 一样，**唯一不同的是相位** $S[x]/\hbar$。"哪条路径贡献大"这个问题没有意义——有意义的是**哪些路径的相位能互相加强**。

设某条路径附近的典型作用量变化为 $\delta S$。若 $\delta S \gg \hbar$，邻域内各路径的相位 $e^{iS/\hbar}$ 快速旋转、均匀扫过单位圆，求和后相互抵消。只有 $S$ 取**驻值**的路径——$\delta S = 0$——附近的一阶相位变化为零，邻域路径相干加强。

### 3.2 $\hbar \to 0$：稳相近似

把路径写成经典解加涨落：$x(t) = x_{\mathrm{cl}}(t) + \eta(t)$（$\eta$ 在端点为零），展开

$$S[x] = S[x_{\mathrm{cl}}] + \frac{1}{2}\int dt\,dt'\ \eta(t)\, \frac{\delta^2 S}{\delta x(t)\,\delta x(t')}\Big|_{x_{\mathrm{cl}}} \eta(t') + O(\eta^3),$$

一阶项因 $\delta S[x_{\mathrm{cl}}]=0$ 消失。代入路径积分，二阶项是高斯泛函积分，给出一个由 $\delta^2 S$ 的行列式决定的前因子（van Vleck–Morette 行列式）：

$$K \approx \big(\det \textstyle\frac{i}{2\pi}\delta^2 S\big)^{-1/2}\, e^{iS[x_{\mathrm{cl}}]/\hbar} \times \big(1 + O(\hbar)\big).$$

$\hbar \to 0$ 时只剩下经典路径的贡献——**经典力学是量子力学的"几何光学极限"**：正如光在波长趋于零时沿光程驻值的直线传播，粒子在 $\hbar$ 可忽略时沿作用量驻值的轨道运动；量子涨落对应衍射修正，按 $\hbar$ 的幂次展开。宏观世界的决定性不是基本规律变了，而是 $S/\hbar \sim 10^{30}$ 以上的相位相消把一切非经典路径洗掉了。

### 3.3 双缝：最朴素的"两历史求和"

双缝实验里电子从源到屏上一点只有两类几何路径（穿过上缝 / 下缝），路径积分退化为两项之和：

$$K \approx e^{iS_1/\hbar} + e^{iS_2/\hbar}, \qquad
|K|^2 = 2 + 2\cos\frac{S_1 - S_2}{\hbar}.$$

相位差由路径差决定，给出干涉条纹。这个例子虽然平庸，却把要点暴露得最清楚：**振幅相加、概率取模方**，而"电子到底走了哪条缝"是个没有物理意义的问题——振幅的构成方式不允许这样分解。挡掉一条缝（测量路径）改变了求和的集合，条纹随之消失。

## 4. 到场论：生成泛函 $Z[J]$

### 4.1 从 $x(t)$ 到 $\varphi(\mathbf{x}, t)$

场论只是把量子力学的推导复制到无穷多个自由度：广义坐标从 $x(t)$ 换成每个空间点一个的场值 $\varphi(\mathbf{x}, t)$，作用量换成场的拉氏量积分（记号见 ../stage-03-relativistic-qm/02-lagrangian-field-theory.md）。以实标量场为例，

$$S[\varphi] = \int d^4x\ \Big[ \frac{1}{2}(\partial_\mu\varphi)(\partial^\mu\varphi) - \frac{1}{2}m^2\varphi^2 - V(\varphi) \Big].$$

时间切片、逐点插入场本征态完备基 $|\{\varphi(\mathbf{x})\}\rangle$，同样的步骤给出场跃迁振幅的路径积分。**真空到真空振幅**是其中最有用的对象：让初末态都是真空并送入外源 $J(x)$ 与场耦合，定义**生成泛函**

$$\boxed{Z[J] = \int \mathcal{D}\varphi\ \exp\Big\{ i\int d^4x\ \big[ \mathcal{L}(\varphi) + J(x)\varphi(x) \big] \Big\}}$$

$Z[0]$（除以合适的归一化）就是真空在无穷长时间内的存活振幅 $\langle 0 | e^{-iHT} | 0 \rangle$；它的相位含真空能，所以对数 $\log Z$ 是可加的广延量。

### 4.2 关联函数 = 泛函导数

泛函导数的定义与普通导数平行：$\dfrac{\delta J(x)}{\delta J(y)} = \delta^4(x-y)$。对 $Z[J]$ 求一次导数就把一个 $i\varphi(x)$ 拉进被积函数：

$$\frac{1}{Z[0]}\Big(\frac{1}{i}\frac{\delta}{\delta J(x_1)}\Big)\cdots\Big(\frac{1}{i}\frac{\delta}{\delta J(x_n)}\Big) Z[J]\Big|_{J=0}
= \frac{1}{Z[0]}\int\mathcal{D}\varphi\ \varphi(x_1)\cdots\varphi(x_n)\, e^{iS[\varphi]}.$$

右边正是路径积分版的关联函数。与算符形式对照，它等于编时真空期望值：

$$\boxed{\langle 0 |\, T\,\varphi(x_1)\cdots\varphi(x_n)\, |0\rangle
= \frac{1}{Z[0]}\Big(\frac{1}{i}\Big)^{\!n} \frac{\delta^n Z[J]}{\delta J(x_1)\cdots\delta J(x_n)}\Big|_{J=0}}$$

注意一个技术事实：路径积分里的场是 c-number（普通函数），乘积无所谓顺序；它对**时间排序的算符乘积**给出正确的答案，时间排序是路径积分自动实现的（切片推导中算符本来就按时间先后排列）。而 $i\epsilon$ 收敛因子——最早在 2.2 节的高斯积分里引入——正好对应算符形式里为挑出真空所做的 $T\to\infty(1-i\epsilon)$ 绝热转动。

所以 $Z[J]$ 名副其实：**它把全部 $n$ 点关联函数打包成一个对象**，对 $J$ 的泰勒展开系数就是它们。物理上 $J$ 可以想成一台"粒子源/汇"装置：$\delta Z/\delta J$ 测量"源在 $x$ 处产生一个粒子"的振幅。

## 5. 自由场计算：本章的技术核心

### 5.1 有限维高斯积分（全部技巧的源头）

先回忆普通积分。$A$ 为 $n\times n$ 实对称正定矩阵：

$$\int d^n x\ \exp\Big( -\frac{1}{2} x^T A x + J^T x \Big) = \frac{(2\pi)^{n/2}}{\sqrt{\det A}}\ \exp\Big( \frac{1}{2} J^T A^{-1} J \Big).$$

推导只有两步：把 $A$ 正交对角化约化为 $n$ 个一维高斯积分（得 $\det$ 因子）；对 $J$ 配方 $x \to x + A^{-1}J$（得指数里的 $J^T A^{-1}J$）。**场论的自由场就是这个公式**，把 $x$ 换成场 $\varphi(x)$、把矩阵 $A$ 换成微分算符。

### 5.2 配方求出 $Z_0[J]$

自由标量场的作用量分部积分后写成二次型：

$$S_0[\varphi] = \frac{1}{2}\int d^4x\ \big[(\partial\varphi)^2 - m^2\varphi^2\big]
= -\frac{1}{2}\int d^4x\ \varphi(x)\,(\Box + m^2)\,\varphi(x).$$

对照有限维公式，$A \leftrightarrow i(\Box + m^2)$，需要它的逆——即满足

$$(\Box_x + m^2)\,D_F(x - y) = -i\,\delta^4(x - y)$$

的格林函数。傅里叶变换给出 $D_F(x-y) = \int \frac{d^4k}{(2\pi)^4}\,\frac{i\,e^{-ik\cdot(x-y)}}{k^2 - m^2}$，但 $k^2 = m^2$ 处的极点需要处方。路径积分的收敛因子 $i\epsilon$（等价地 $m^2 \to m^2 - i\epsilon$）自动选定 **Feynman 处方**：

$$D_F(x - y) = \int \frac{d^4k}{(2\pi)^4}\ \frac{i}{k^2 - m^2 + i\epsilon}\ e^{-ik\cdot(x-y)}.$$

对 $k^0$ 积分（上/下半平面留数定理）可以验证，这个极点选择给出"正频率向未来、负频率向过去"传播，正是编时乘积需要的边条件。

现在做场平移（配方的连续版）：$\varphi(x) \to \varphi(x) + i\int d^4y\,D_F(x-y)J(y)$。代入 $S_0 + \int J\varphi$，一次项相消，得到

$$\boxed{Z_0[J] = Z_0[0]\ \exp\Big( -\frac{1}{2}\int d^4x\,d^4y\ J(x)\,D_F(x-y)\,J(y) \Big)}$$

前因子 $Z_0[0]$ 对应有限维公式里的 $(\det A)^{-1/2}$——一个（形式上无穷的）泛函行列式，与 $J$ 无关，在计算关联函数的归一化比值中消去。

### 5.3 两点函数回到 Feynman 传播子

对 $Z_0$ 求两次泛函导数。记 $J\!D_F\!J \equiv \int d^4x\,d^4y\,J(x)D_F(x-y)J(y)$：

$$\frac{1}{i}\frac{\delta Z_0}{\delta J(x_1)} = Z_0[J]\cdot i\int d^4y\,D_F(x_1-y)J(y),$$

再对 $J(x_2)$ 求导并令 $J=0$（此时含 $J$ 的项全部消失，只剩 $\delta^4$ 作用出来的那一项）：

$$\langle 0|T\,\varphi(x_1)\varphi(x_2)|0\rangle
= \frac{1}{Z_0[0]}\Big(\frac{1}{i}\Big)^{\!2}\frac{\delta^2 Z_0}{\delta J(x_1)\delta J(x_2)}\Big|_{0} = D_F(x_1 - x_2).$$

**传播子就是二次型中微分算符的逆**——这不是巧合，是配方的直接后果。

### 5.4 Wick 定理：缩并配对自动出现

再求两次导数算四点函数。对 $e^{-\frac12 J D_F J}$ 逐次作用 $\delta/\delta J$，由乘积法则，最终不为零的项必须把所有 $J$ 恰好两两"配干净"。直接计算得

$$\langle 0|T\,\varphi_1\varphi_2\varphi_3\varphi_4|0\rangle
= D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23},$$

其中 $\varphi_i \equiv \varphi(x_i)$，$D_{ij} \equiv D_F(x_i - x_j)$。这正是 **Wick 定理**：自由场的 $n$ 点函数等于全部两两配对（缩并）方式之和，奇数点函数为零（$J$ 配不干净）。在路径积分语言里它不是一个需要证明的算符恒等式，而是**高斯积分求导的组合学**——高斯分布的一切矩由二阶矩决定。

## 6. 相互作用：费曼图从展开中长出来

加入相互作用，以 $\lambda\varphi^4$ 为例，$\mathcal{L}_{\mathrm{int}} = -\frac{\lambda}{4!}\varphi^4$。被积函数里 $e^{i\int\mathcal{L}_{\mathrm{int}}}$ 中的 $\varphi(x)$ 可以替换成对源的导数 $\varphi \to \frac{1}{i}\frac{\delta}{\delta J}$ 并提到积分号外：

$$Z[J] = \mathcal{N}\ \exp\Big\{ i\int d^4x\ \mathcal{L}_{\mathrm{int}}\Big[ \frac{1}{i}\frac{\delta}{\delta J(x)} \Big] \Big\}\ Z_0[J],$$

$\mathcal{N}$ 为归一化常数。把指数按 $\lambda$ 的幂次泰勒展开：

$$Z[J] = \mathcal{N}\Big[ 1 + i\int d^4x\,\mathcal{L}_{\mathrm{int}}\Big[\tfrac{1}{i}\tfrac{\delta}{\delta J}\Big] + \cdots \Big] Z_0[J].$$

每一项都是对 $e^{-\frac12 J D_F J}$ 的一批泛函导数，而 5.4 节已经看到：**求导 = 用各种方式把源 $J$ 配对成传播子** $D_F$。逐项追踪这些配对，就得到：

- 每条连接两点的线 $\leftrightarrow$ 一个 $D_F$（传播子）；
- 每个 $\mathcal{L}_{\mathrm{int}}$ 出现的点 $\leftrightarrow$ 一个顶点（$\varphi^4$ 理论中是四条线的交点，附因子 $-i\lambda$）；
- 交换顶点、交换线的不同配对方案给出对称因子和组合数。

这正是费曼图的构成规则。微扰级数 = 把"对相互作用历史的求和"按耦合常数展开，每一阶是有限个图。**结论：路径积分与正则算符形式（Dyson 级数 + Wick 定理）给出同一套费曼规则**——前者把 Wick 配对藏在高斯积分的导数里，后者藏在算符收缩里，组合学完全相同。具体的顶点因子、对称因子计算见标量场量子化与费曼规则的后续笔记。

## 7. 费米子：格拉斯曼数与 Berezin 积分

费米场算符反对易，其经典对应物不能是普通 c-number——路径积分要求引入**格拉斯曼数**：满足

$$\{\theta_i, \theta_j\} = 0,\qquad \theta_i^2 = 0$$

的"数"。由于平方为零，任何函数的泰勒展开到一阶就截止：$f(\theta) = a + b\theta$。Berezin 积分由两条公理完全定义：

$$\int d\theta\ 1 = 0, \qquad \int d\theta\ \theta = 1.$$

注意第一条与普通积分截然不同（平移不变性 + 无"无穷远"概念的必然结果）。对格拉斯曼变量做高斯积分，以一对 $\bar\theta, \theta$ 为例：

$$\int d\bar\theta\,d\theta\ e^{-\bar\theta a \theta}
= \int d\bar\theta\,d\theta\ \big(1 - \bar\theta a \theta\big) = a,$$

推广到 $n$ 维得 $\int \prod_i d\bar\theta_i d\theta_i\ e^{-\bar\theta A \theta} = \det A$。**与玻色情形的 $(2\pi)^n/\sqrt{\det A}$ 对照：行列式翻到了分子上**。取对数看自由能，玻色贡献 $-\frac12\mathrm{Tr}\log A$，费米贡献 $+\mathrm{Tr}\log A$——圈图计算中费米子圈相对玻色子圈多一个整体的负号。这个负号（加上圈动量积分的组合学）就是费曼规则里"每个闭合费米子圈附 $-1$"的根源，也是 Pauli 不相容原理在微扰论中的记账方式。

## 8. 规范场：过计数与 Faddeev–Popov

对规范场 $A_\mu$ 直接写 $\int\mathcal{D}A\,e^{iS}$ 有一个明显的问题：相差一个规范变换 $A_\mu \to A_\mu + \partial_\mu\alpha$（非阿贝尔情形为 $A_\mu \to U A_\mu U^{-1} - i(\partial_\mu U)U^{-1}$）的场构型物理上完全相同，而作用量在其上不变。朴素的路径积分把**每条规范轨道上的无穷多个等价构型都算了一遍**，对紧致规范群这贡献一个无穷大的总体因子（轨道体积），更严重的是二次型算符沿规范方向有零模、不可逆，第 5 节的配方直接失败。

Faddeev–Popov 的修复思想是：插入一个写得像 $1$ 的泛函恒等式

$$1 = \Delta_{\mathrm{FP}}[A]\int \mathcal{D}\alpha\ \delta\big( G[A^\alpha] \big),$$

其中 $G[A] = 0$ 是规范固定条件（如 Lorenz 规范 $\partial_\mu A^\mu = 0$）。轨道体积 $\int\mathcal{D}\alpha$ 作为常数因子分离出去扔掉，剩下的是"只在规范面上积分、但乘以补偿行列式 $\Delta_{\mathrm{FP}}$"的积分。把 $\Delta_{\mathrm{FP}} = \det\big(\delta G/\delta\alpha\big)$ 用格拉斯曼辅助场 $\bar c, c$ 写出来（第 7 节的公式倒过来用：$\det M = \int\mathcal{D}\bar c\,\mathcal{D}c\,e^{-\bar c M c}$），这个行列式就变成了拉氏量里的新"场"——**Faddeev–Popov 鬼场**。鬼场是只出现在圈内的反对易标量，作用是精确扣除规范自由度的过计数。这里只做存在性声明；鬼顶点的具体形式、与 BRST 对称的关系留给 Yang–Mills 理论的后续笔记。

## 9. 为什么路径积分是现代 QFT 的母语

- **协变性显式**：被积函数 $e^{iS}$ 里只有 Lorentz 不变的作用量，没有任何依赖参考系的算符排序。场的对称性（规范、超对称、引力）在拉氏量层面一目了然。
- **规范理论处理自然**：第 8 节的整个 Faddeev–Popov 程序在算符形式里极其笨拙（要么破坏协变性，要么引入不定度规空间）。没有路径积分，非阿贝尔规范理论的可重整化证明难以想像。
- **非微扰门户**：瞬子、隧道效应对应欧氏路径积分的经典鞍点；格点 QCD 把 $\int\mathcal{D}\varphi\,e^{-S_E}$ 直接离散化做蒙特卡洛数值积分——这是今天从第一性原理算强子谱的唯一方法，整个框架就是欧氏路径积分。
- **与统计物理统一**：Wick 转动 $t \to -i\tau$ 后 $Z$ 就是统计力学的配分函数，温度 $T \leftrightarrow$ 虚时周期 $1/T$。QFT 与临界现象是同一套数学（Wilson 的重整化群两边通吃）。

## 10. 诚实声明：本文没有证明什么

本文从量子力学切片推出路径积分（第 2 节），又断言场论关联函数的路径积分表达式等于算符编时乘积（4.2 节）——后者**我们只是对照了结构，没有严格证明**。完整的等价性证明需要：对场论重复切片构造（含正则对易关系的正确实现）、处理泛函行列式与 $i\epsilon$ 的对应、以及证明微扰论逐阶一致。标准教材的处理见 Peskin & Schroeder 第 9 章（量子力学切片 + 标量场 $Z[J]$ 与算符的对照），更严格的讨论见 Weinberg 第一卷第 9 章。学习策略上建议：把第 5、6 节的计算技术练熟（这是日常工具），等价性的概念性确信留到两边都算过同一个物理量（如两点函数）并看到结果一致之后自然建立。

## 小结

| 对象 | 表达式 | 要点 |
|---|---|---|
| QM 传播子 | $K = \int\mathcal{D}x\,e^{iS/\hbar}$ | 时间切片 + 完备基；$H\to L$ 来自动量高斯积分 |
| 经典极限 | $\hbar\to0$ 稳相近似 | $\delta S=0$ 路径相干加强；经典力学 = 几何光学极限 |
| 生成泛函 | $Z[J]=\int\mathcal{D}\varphi\,e^{i(S+\int J\varphi)}$ | 对 $J$ 求导给出全部关联函数 |
| 自由场 | $Z_0 = Z_0[0]\,e^{-\frac12 J D_F J}$ | 配方；传播子 = 二次型算符之逆（$+i\epsilon$） |
| Wick 定理 | $n$ 点函数 = 全部两两配对 | 高斯积分求导的组合学 |
| 相互作用 | $e^{iS_{\mathrm{int}}[\delta/\delta J]}Z_0$ 展开 | 逐项 = 费曼图，与算符形式同一套规则 |
| 费米子 | $\int\mathcal{D}\bar\psi\mathcal{D}\psi\,e^{iS} \Rightarrow \det$ | Berezin 积分；det 在分子上 $\Rightarrow$ 费米圈负号 |
| 规范场 | Faddeev–Popov 行列式 + 鬼场 | 规范轨道过计数必须扣除 |

## 自检问题

**1.** 在时间切片推导中，从 $\langle x_{j+1}|e^{-i\epsilon H}|x_j\rangle$ 到被积函数里的 $e^{i\epsilon L}$，勒让德变换 $H \to L$ 是在哪一步、以什么机制出现的？

<details markdown="1"><summary>点击显示答案</summary>

出现在**对中间动量 $p_j$ 的高斯积分配方**这一步。插入动量完备基后被积函数是

$$\int \frac{dp_j}{2\pi}\ \exp\Big\{ i\epsilon\Big[ p_j \dot x_j - \frac{p_j^2}{2m} - V(x_j)\Big]\Big\},\qquad \dot x_j \equiv \frac{x_{j+1}-x_j}{\epsilon}.$$

这是关于 $p_j$ 的高斯积分，稳定点在 $\partial/\partial p_j: \ \dot x_j - p_j/m = 0$，即 $p_j = m\dot x_j$。配方 $-\frac{1}{2m}(p_j - m\dot x_j)^2 + \frac{m}{2}\dot x_j^2$ 后，积分给出前因子 $(m/2\pi i\epsilon)^{1/2}$，留在指数里的是

$$\frac{m}{2}\dot x_j^2 - V(x_j) = p_j\dot x_j - H(p_j, x_j)\Big|_{p_j = m\dot x_j} = L(x_j, \dot x_j).$$

所以机制是：**哈密顿表述里 $p$ 是独立变量，对它做（稳相/高斯）积分恰好执行了勒让德变换**。一般地，只要 $H$ 对 $p$ 是二次的，这步严格成立；若 $H$ 含 $p$ 的高次项，路径积分的"自然"出生形式是相空间形式 $\int\mathcal{D}x\,\mathcal{D}p\,e^{i\int(p\dot x - H)}$，坐标形式只是它的特例。

</details>

**2.** 用稳相近似解释：为什么 $\hbar \to 0$ 时只有经典路径存活？二阶涨落项对应的物理是什么？

<details markdown="1"><summary>点击显示答案</summary>

每条路径贡献等模相位 $e^{iS[x]/\hbar}$。取一条非驻值路径，其邻域内 $S$ 的一阶变化 $\delta S \neq 0$，于是相差 $\delta x$ 的两条邻近路径相位差为 $\delta S/\hbar$。$\hbar$ 趋于零时这个相位差任意大，邻域内相位在单位圆上密集均匀分布，求和（积分）后抵消为零——**相消干涉**。

在驻值路径 $x_{\mathrm{cl}}$（$\delta S = 0$）附近，相位的一阶变化消失，邻域内所有路径的相位在量级 $\hbar$ 的宽度内保持一致，**相干加强**。形式上展开 $S = S_{\mathrm{cl}} + \frac12 \eta\, \delta^2 S\, \eta + O(\eta^3)$，高斯积分得

$$K \approx \big(\det \tfrac{i}{2\pi}\delta^2 S\big)^{-1/2} e^{iS_{\mathrm{cl}}/\hbar}\big(1 + O(\hbar)\big).$$

领头的 $e^{iS_{\mathrm{cl}}/\hbar}$ 就是经典物理（Hamilton 主函数满足 Hamilton–Jacobi 方程）。**二阶涨落项是围绕经典轨道的量子涨落**：$\det(\delta^2 S)$ 衡量经典轨道附近"相位盆地"的宽度，给出振幅的领头量子修正（半经典的 van Vleck 行列式）；更高阶项构成按 $\hbar$ 展开的 WKB 级数。焦点（$\delta^2 S$ 出现零模）处该近似失效，对应光学中的焦散。

</details>

**3.** 从 $Z_0[J] = Z_0[0]\exp(-\frac12 J D_F J)$ 出发，计算自由场四点函数，验证 Wick 定理的配对结构。

<details markdown="1"><summary>点击显示答案</summary>

记 $W[J] = -\frac12\int\int J(x)D_F(x-y)J(y)$（$Z_0 = Z_0[0]e^{W}$），并利用 $\delta W/\delta J(x) = -\int D_F(x-y)J(y)\,dy$（用了 $D_F$ 的对称性，两个相同项合并消掉因子 $1/2$）。逐次求导：

$$\frac{1}{i}\frac{\delta Z_0}{\delta J_1} = Z_0\cdot i\!\int D_F(x_1 - y)J(y),$$

$$\Big(\frac{1}{i}\Big)^{\!2}\frac{\delta^2 Z_0}{\delta J_1\delta J_2} = Z_0\Big[ D_{12} - \Big(\!\int D_{1y}J_y\Big)\Big(\!\int D_{2y}J_y\Big)\Big],$$

继续对 $J_3, J_4$ 求导后令 $J=0$：任何残留 $J$ 因子的项全部消失，只剩下四次求导中每次都有导数作用在"已拉下来的 $J$ 上"产生 $\delta^4$、从而把所有 $J$ 配干净的项。追踪组合：

$$\langle 0|T\varphi_1\varphi_2\varphi_3\varphi_4|0\rangle = D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23}.$$

共 $3 = (4-1)!!$ 项，正是四个对象两两配对的方案数。一般地 $2n$ 点函数含 $(2n-1)!!$ 个配对项，奇数点函数为零（必有 $J$ 配不干净，令 $J=0$ 后消失）。**Wick 定理 = 高斯测度下"一切矩由协方差决定"**，缩并就是协方差 $D_F$。

</details>

**4.** 为什么格拉斯曼高斯积分给出 $\det A$（分子），而玻色高斯积分给出 $1/\sqrt{\det A}$（分母）？这与费米子圈的负号有什么关系？

<details markdown="1"><summary>点击显示答案</summary>

根源是 Berezin 积分"只保留最高次项"：由于 $\theta^2 = 0$，指数展开到有限阶截止，

$$e^{-\bar\theta A\theta} = \sum_k \frac{(-1)^k}{k!}(\bar\theta A\theta)^k,$$

而积分 $\int\prod_i d\bar\theta_i d\theta_i$ 只挑出恰好包含每个 $\bar\theta_i, \theta_i$ 各一次的项。这个项的系数按定义就是 $\det A$（行列式正是"每行每列各取一个元、带置换符号求和"）。玻色情形相反：普通高斯积分 $\int d^n z\,e^{-\frac12 z^T A z}$ 对角化后是 $n$ 个 $\sqrt{2\pi/a_i}$ 的乘积，得 $(2\pi)^{n/2}/\sqrt{\det A}$——**积分值与"量子涨落算符的本征值"成反比**。

对圈图的后果：单圈有效作用量 $\sim \mathrm{Tr}\log$（涨落算符）。玻色圈贡献 $-\frac12\mathrm{Tr}\log$，费米圈贡献 $+\mathrm{Tr}\log$（来自 $\det$ 在分子，$\log\det A = +\mathrm{Tr}\log A$）。两者的相对符号，加上费米子线交换带来的组合符号，合并成费曼规则里"**每个闭合费米子圈乘 $-1$**"。物理上这是 Pauli 原理的记账：全同费米子中间态的交换振幅必须反对称。

</details>

**5.** 朴素地对规范场做 $\int\mathcal{D}A\,e^{iS}$ 为什么会发散？Faddeev–Popov 程序用一句话概括是怎么修复的？

<details markdown="1"><summary>点击显示答案</summary>

**发散原因**：规范不变性意味着作用量 $S[A]$ 沿规范轨道 $A_\mu \to A_\mu + \partial_\mu\alpha$（及有限规范变换）是常数。路径积分对场构型求和时，物理上等价的整条轨道被重复计数；沿轨道方向的积分不被 $e^{iS}$ 抑制，贡献正比于规范群的（无穷）体积。更技术地说，二次涨落算符沿规范方向有零本征值，$A^{-1}$ 不存在，第 5 节的配方无法执行——传播子都定义不了。

**Faddeev–Popov 的修复（一句话）**：插入恒等式 $1 = \Delta_{\mathrm{FP}}[A]\int\mathcal{D}\alpha\,\delta(G[A^\alpha])$（沿轨道的 $\delta$ 函数），把积分分解为"轨道体积 $\times$ 规范面上的受限积分"，扔掉与物理无关的轨道体积，并用格拉斯曼鬼场把补偿行列式 $\Delta_{\mathrm{FP}}$ 写进拉氏量——**相当于给无穷大的过计数除以规范群体积，留下的 Jacobian 必须作为鬼场圈参与计算才能保证幺正性**。细节（鬼顶点、BRST）见 Yang–Mills 的后续笔记。

</details>

## 参考

- Peskin & Schroeder《An Introduction to QFT》第 9 章（切片推导、$Z[J]$、与算符形式的对照）、第 9.4–9.5 节（格拉斯曼数、量子电动力学的路径积分）——与本篇对应最直接。
- Schwartz《Quantum Field Theory and the Standard Model》第 14 章（路径积分与生成泛函）、第 15–16 章（规范场的 Faddeev–Popov 与鬼）。
- Srednicki《Quantum Field Theory》第 6–9 章（标量场 $Z[J]$ 的系统性推导，记号干净，适合动手复算）。
- Zee《Quantum Field Theory in a Nutshell》第 I.2–I.3 章（路径积分直觉与"对历史求和"的物理图像，入门最友好）。
- （进阶）Weinberg《The Quantum Theory of Fields》第一卷第 9 章——路径积分与算符形式等价性的严格讨论。
