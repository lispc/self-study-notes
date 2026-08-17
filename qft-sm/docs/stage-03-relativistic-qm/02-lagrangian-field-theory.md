# 场的拉格朗日形式：从弦的振动到诺特定理

> 路线图位置：第 3 阶段（经典场论 + 相对论量子力学，过渡桥梁）· 第 2 篇
> 前置知识：分析力学（最小作用量原理、质点系的欧拉–拉格朗日方程）、狭义相对论（四维矢量与指标升降）、第一篇（Klein–Gordon 与 Dirac 方程）。
> 学习目标：把分析力学从"有限个质点"推广到"场"这一无穷自由度系统；会写作用量、会推场的欧拉–拉格朗日方程；吃透诺特定理的推导与三个最重要的例子，理解"对称性 ⟺ 守恒律"这台机器的构造。

---

## 1. 一句话总结

**场就是无穷多自由度的力学系统：把珠链的指标 $i$ 换成连续标签 $x$，分立拉氏量就变成拉氏密度的空间积分；对它做四维化（$S=\int d^4x\,\mathcal L$，$\mathcal L$ 是洛伦兹标量），最小作用量原理给出场的欧拉–拉格朗日方程——Klein–Gordon 方程和 Maxwell 方程都是它的产物；而诺特定理告诉我们：每一个连续对称变换都对应一个守恒流 $\partial_\mu j^\mu=0$ 和一个守恒荷，能量、动量、电荷、角动量全部由此而来。**

下面把这句话逐层拆开。全章取自然单位 $\hbar=c=1$，度规号差 $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$。

## 2. 从珠链到场：连续极限

### 2.1 分立系统

考虑 $N$ 个质量为 $m$ 的珠子，等间距 $a$ 穿在一根弦上，只能沿横向做小振动，第 $i$ 个珠子的位移记为 $q_i(t)$。相邻珠子间由劲度系数 $k$ 的弹簧连接。拉氏量是标准的"动能减势能"：

$$L = \sum_{i=1}^{N}\left[\frac{1}{2}m\dot q_i^{\,2} - \frac{1}{2}k\,(q_{i+1}-q_i)^2\right].$$

欧拉–拉格朗日方程 $\dfrac{d}{dt}\dfrac{\partial L}{\partial \dot q_i}-\dfrac{\partial L}{\partial q_i}=0$ 给出 $N$ 个耦合振子的运动方程：

$$m\ddot q_i = k\,(q_{i+1}-2q_i+q_{i-1}).$$

### 2.2 取极限 $a\to 0$

现在让珠子越来越密：$a\to 0$，同时保持弦的**线密度** $\mu$ 与**张力** $Y$ 有限。分立标签 $i$ 变成连续坐标 $x=ia$，位移 $q_i(t)$ 变成一个二元函数：

$$q_i(t)\ \longrightarrow\ \phi(x,t).$$

这就是**场**：它不是"新种类的物理对象"，只是无穷多自由度的力学系统——每个空间点 $x$ 处挂着一个"坐标" $\phi(x)$，连续标签 $x$ 扮演了过去指标 $i$ 的角色。

为了保持各项有限，质量与劲度要按 $m=\mu a$、$k=Y/a$ 缩放（珠子越轻、弹簧越硬，总量才有限）。逐项看拉氏量的极限：

- 动能：$\sum_i \frac12 m\dot q_i^2 = \sum_i a\cdot\frac12\frac{m}{a}\dot\phi^2 \longrightarrow \displaystyle\int dx\,\frac12\mu(\partial_t\phi)^2$；
- 势能：$q_{i+1}-q_i \simeq a\,\partial_x\phi$，故 $\sum_i \frac12 k(q_{i+1}-q_i)^2 = \sum_i a\cdot\frac12 (ka)(\partial_x\phi)^2 \longrightarrow \displaystyle\int dx\,\frac12 Y(\partial_x\phi)^2$。

于是

$$\boxed{L = \int dx\,\Big[\underbrace{\tfrac12\mu(\partial_t\phi)^2}_{\text{动能密度}} - \underbrace{\tfrac12 Y(\partial_x\phi)^2}_{\text{势能密度}}\Big] \equiv \int dx\,\mathcal L}$$

被积函数 $\mathcal L$ 叫**拉氏密度（Lagrangian density）**。对连续极限下的运动方程，可以直接对场用变分，也可以从分立方程取极限：即 $m\ddot q_i \to \mu a\,\partial_t^2\phi$，$k(q_{i+1}-2q_i+q_{i-1}) \to (Y/a)\,a^2\partial_x^2\phi$，等式两边约去 $a$ 得

$$\mu\,\partial_t^2\phi - Y\,\partial_x^2\phi = 0,$$

即一维波动方程，波速 $v^2=Y/\mu$。**"场论"的全部新意就在这一步：自由度从有限变成不可数无穷，其余机器——拉氏量、变分、欧拉–拉格朗日方程——原样照搬。**

## 3. 四维化：作用量与场的欧拉–拉格朗日方程

### 3.1 作用量

第 2 节的弦是一维空间 + 时间。相对论要求时空平权，所以推广到 $3+1$ 维：场 $\phi(x^\mu)=\phi(t,\vec x)$，作用量

$$S = \int dt\,L = \int d^4x\ \mathcal L\big(\phi,\ \partial_\mu\phi\big).$$

注意两点约定：

- 我们只讨论 $\mathcal L$ 依赖 $\phi$ 及其**一阶**导数的理论——这对应运动方程至多是二阶微分方程，与牛顿力学"$F=ma$ 是二阶的"一脉相承；
- $\mathcal L$ 不含 $x^\mu$ 的显式依赖——这对应时空平移对称性（第 7 节会看到它的回报）。

**为什么要求 $\mathcal L$ 是洛伦兹标量？** 因为 $d^4x$ 在（proper）洛伦兹变换下不变（雅可比行列式 $|\det\Lambda|=1$），只要 $\mathcal L$ 是标量，作用量 $S$ 就是洛伦兹不变的；而物理规律由 $\delta S=0$ 给出，于是运动方程自动洛伦兹协变。这是"拉氏量写法"在相对论中的最大优势：**把对称性直接写进 $\mathcal L$，协变性免费获得。**

### 3.2 从 $\delta S=0$ 推导欧拉–拉格朗日方程

给场一个无穷小扰动 $\phi(x)\to\phi(x)+\delta\phi(x)$，要求 $\delta\phi$ 在时空边界上为零。作用量的变分：

$$\delta S = \int d^4x\left[\frac{\partial\mathcal L}{\partial\phi}\,\delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\mu(\delta\phi)\right].$$

对第二项做**分部积分**（这是场论推导中最常用的一步，务必熟练）：

$$\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\mu(\delta\phi) = \partial_\mu\!\left[\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\delta\phi\right] - \partial_\mu\!\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right)\delta\phi.$$

方括号里的全导数项积分后只贡献边界，$\delta\phi$ 在边界上为零，故消失。于是

$$\delta S = \int d^4x\left[\frac{\partial\mathcal L}{\partial\phi} - \partial_\mu\!\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right)\right]\delta\phi = 0.$$

$\delta\phi(x)$ 是任意函数，括号必须处处为零：

$$\boxed{\ \partial_\mu\!\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right) - \frac{\partial\mathcal L}{\partial\phi} = 0\ }$$

这就是**场的欧拉–拉格朗日方程**。与质点力学的 $\frac{d}{dt}\frac{\partial L}{\partial\dot q}-\frac{\partial L}{\partial q}=0$ 对比：唯一的变化是 $\frac{d}{dt}$ 升级为四散度 $\partial_\mu$，$\dot q$ 升级为 $\partial_\mu\phi$——时间求导变成时空求导，正是"时空平权"的体现。若理论含多个场 $\phi_a$，每个场各得一个这样的方程。

<details markdown="1"><summary>补充说明：ℒ 并不唯一——相差全导数的拉氏密度等价</summary>

若 $\mathcal L' = \mathcal L + \partial_\mu F^\mu(\phi)$，则 $S' = S + \int d^4x\,\partial_\mu F^\mu$，多出来的项只依赖场在边界上的值。变分时边界上的场固定不动（$\delta\phi=0$），所以 $\delta S' = \delta S$，两者给出**完全相同**的运动方程。

这不是书呆子注记：诺特定理里"$\mathcal L$ 只变一个全导数也算对称"（第 6 节的 $K^\mu$）用的正是同一事实；电磁学里把 $-\frac12(\partial_\mu A_\nu)(\partial^\mu A^\nu)$ 改写成 $-\frac14F_{\mu\nu}F^{\mu\nu}$ 也要丢一个全导数。以后遇到"两个看起来不一样的 $\mathcal L$ 给出同一个理论"，先检查它们是不是只差全导数。

</details>

## 4. 三个实例

### 4.1 实标量场 → Klein–Gordon 方程

取最简单的洛伦兹标量拉氏密度：

$$\mathcal L = \frac12(\partial_\mu\phi)(\partial^\mu\phi) - \frac12 m^2\phi^2 = \frac12\dot\phi^2 - \frac12(\nabla\phi)^2 - \frac12m^2\phi^2.$$

两项计算：

$$\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)} = \partial^\mu\phi, \qquad \frac{\partial\mathcal L}{\partial\phi} = -m^2\phi.$$

代入欧拉–拉格朗日方程：

$$\partial_\mu\partial^\mu\phi + m^2\phi = 0 \qquad\Longleftrightarrow\qquad (\Box + m^2)\phi = 0.$$

正是 Klein–Gordon 方程。现在我们可以回答第一篇留下的悬念：**KG 方程的"正确身份"是经典场的运动方程**——它和 Maxwell 方程地位相同，是某个经典场论（$\mathcal L$ 如上）的欧拉–拉格朗日方程。第一篇里把 $\phi$ 当单粒子波函数所遇到的一切困难（负能量、负概率密度），根源在于这个错误解读；把它当经典场、再量子化，困难自然消解（第 4 阶段）。注意它与弦的波动方程的相似性：$\frac12m^2\phi^2$ 相当于给弦上每一点加了一个回复力（"床垫模型"里的弹簧床），$m$ 就是这个内禀回复频率。

### 4.2 电磁场 → 真空 Maxwell 方程

场变量是四维势 $A_\mu(x)$。定义场强张量

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu,$$

取拉氏密度

$$\mathcal L = -\frac14 F_{\mu\nu}F^{\mu\nu} = \frac12\big(\vec E^2 - \vec B^2\big).$$

关键一步（自检问题 3 要求你亲手验证）：

$$\frac{\partial\mathcal L}{\partial(\partial_\mu A_\nu)} = -F^{\mu\nu}, \qquad \frac{\partial\mathcal L}{\partial A_\nu} = 0.$$

欧拉–拉格朗日方程立刻给出

$$\partial_\mu F^{\mu\nu} = 0,$$

这包含了真空 Maxwell 方程中的两个：$\nu=0$ 是 $\nabla\cdot\vec E=0$（无源高斯定律），$\nu=i$ 是 $\nabla\times\vec B = \partial_t\vec E$（无电流安培定律）。另外两个（$\nabla\cdot\vec B=0$ 与法拉第定律）不是动力学方程，而是 $F_{\mu\nu}$ 定义式 $\partial_\mu A_\nu-\partial_\nu A_\mu$ 的恒等式（Bianchi 恒等式）：

$$\partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0.$$

四句真空 Maxwell 方程就这样被一句话 $\mathcal L=-\frac14F^2$ 装下了。这个 $\mathcal L$ 还藏着一个更深的对称性——规范对称性，第 8 节再回头点它一句。

### 4.3 Dirac 场（一句话）

旋量场的拉氏密度是

$$\mathcal L = \bar\psi\,(i\gamma^\mu\partial_\mu - m)\,\psi, \qquad \bar\psi\equiv\psi^\dagger\gamma^0.$$

把 $\bar\psi$ 与 $\psi$ 当独立变量，对 $\bar\psi$ 用欧拉–拉格朗日方程即得 $(i\gamma^\mu\partial_\mu-m)\psi=0$——第一篇的 Dirac 方程。同样，它的正确身份是经典（旋量）场的运动方程。

## 5. 哈密顿量与正则动量（为正则量子化埋伏笔）

照搬分析力学的定义，场 $\phi$ 的**正则共轭动量密度**为

$$\pi(x) \equiv \frac{\partial\mathcal L}{\partial\dot\phi(x)},$$

哈密顿量（密度）为

$$H = \int d^3x\,\big[\pi\dot\phi - \mathcal L\big] \equiv \int d^3x\,\mathcal H.$$

例如实标量场：$\pi=\dot\phi$，$\mathcal H = \frac12\pi^2+\frac12(\nabla\phi)^2+\frac12m^2\phi^2$。类比质点力学中 $(q,p)\to$ 算符、$[q,p]=i$，**正则量子化**就是把 $(\phi,\pi)$ 提升为算符并施加等时对易关系 $[\phi(\vec x),\pi(\vec y)]=i\delta^{(3)}(\vec x-\vec y)$——这是第 4 阶段的第一课，此处只需记住 $\pi$ 的定义，见后续笔记。

## 6. 诺特定理：连续对称性 ⟺ 守恒流

### 6.1 陈述

**诺特定理（Noether, 1918）**：若理论在某个**连续**变换下不变（精确地说：任意场形下 $\mathcal L$ 至多改变一个全导数），则存在一个流 $j^\mu(x)$，对一切满足运动方程的场构型（on shell）有

$$\partial_\mu j^\mu = 0,$$

并对应一个守恒荷

$$Q = \int d^3x\,j^0, \qquad \frac{dQ}{dt}=0.$$

荷守恒的证明一步到位：$\dfrac{dQ}{dt}=\displaystyle\int d^3x\,\partial_0 j^0 = -\int d^3x\,\nabla\cdot\vec j = -\oint_{\infty}\vec j\cdot d\vec S = 0$，最后一步用场在无穷远处消失。物理图像：$j^0$ 是"荷密度"，$\vec j$ 是"流密度"，荷只能流动，不能创生或湮灭。

### 6.2 推导（纯场变换）

先做最简单也是核心的一步：坐标不动，只变场，

$$\phi(x)\ \longrightarrow\ \phi(x) + \alpha\,\Delta\phi(x),$$

$\alpha$ 是无穷小**常数**参数（"整体"对称性；"$\alpha$ 依赖 $x$"是规范对称性，见第 8 节）。**对称性的定义**：变换后（不假设场满足运动方程，即 off shell）拉氏密度至多变一个全导数：

$$\delta\mathcal L = \alpha\,\partial_\mu K^\mu.$$

（$K^\mu=0$ 即 $\mathcal L$ 严格不变，是最常见的情形；时空平移会用到 $K^\mu\neq0$，见 6.3。）

另一方面直接计算 $\delta\mathcal L$，再做一次和第 3 节一模一样的分部积分：

$$\delta\mathcal L = \frac{\partial\mathcal L}{\partial\phi}\,\alpha\Delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\alpha\,\partial_\mu\Delta\phi = \alpha\,\partial_\mu\!\left[\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\Delta\phi\right] + \alpha\underbrace{\left[\frac{\partial\mathcal L}{\partial\phi} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right]}_{=\,0\ \text{（on shell，欧拉–拉格朗日方程）}}\Delta\phi.$$

当场满足运动方程时，后一项为零，于是 $\delta\mathcal L = \alpha\,\partial_\mu\big[\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\Delta\phi\big]$。与对称性条件 $\delta\mathcal L=\alpha\,\partial_\mu K^\mu$ 比较，即得

$$\boxed{\ j^\mu \equiv \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\Delta\phi - K^\mu, \qquad \partial_\mu j^\mu = 0\ }$$

注意推导的逻辑：**off shell 时 $\delta\mathcal L$ 是全导数**（对称性假设），**on shell 时 $\delta\mathcal L$ 是另一个全导数**（用了运动方程），两个全导数之差给出守恒流。守恒流只在 on shell 才守恒——守恒律是"对称性 + 运动方程"的联合产物。

### 6.3 含坐标变换的情形：标准形式

时空变换 $x^\mu\to x^\mu+\delta x^\mu$ 会同时带动场变化。对标量场，"场跟着坐标一起平移"意味着新场在新坐标下取旧场的值，即

$$\phi(x)\ \longrightarrow\ \phi(x+\delta x) = \phi(x) + \delta x^\nu\,\partial_\nu\phi \quad\Longrightarrow\quad \Delta\phi = \partial_\nu\phi\ \delta x^\nu.$$

（把无穷小参数 $\delta x^\nu$ 吸收进 $\Delta\phi$ 的定义。）同时，$\mathcal L$ 作为洛伦兹标量本身也随之变化：

$$\delta\mathcal L = \delta x^\nu\,\partial_\nu\mathcal L = \partial_\mu\!\big(\delta^\mu_{\ \nu}\,\mathcal L\,\delta x^\nu\big) \quad\Longrightarrow\quad K^\mu = \delta^\mu_{\ \nu}\,\mathcal L\,\delta x^\nu.$$

代入 6.2 的方框公式：

$$j^\mu = \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\nu\phi\ \delta x^\nu - \delta^\mu_{\ \nu}\,\mathcal L\,\delta x^\nu \equiv T^\mu_{\ \nu}\,\delta x^\nu,$$

其中

$$\boxed{\ T^\mu_{\ \nu} = \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\nu\phi - \delta^\mu_{\ \nu}\,\mathcal L\ }$$

就是**正则能动张量（canonical energy-momentum tensor）**——诺特定理在时空平移下的产物。因为 $\delta x^\nu$ 任意，$\partial_\mu T^\mu_{\ \nu}=0$ 给出**四个**守恒流（$\nu=0,1,2,3$），对应四个守恒荷。这就是下一节第一个例子的来源。

## 7. 诺特定理的三个例子

### 7.1 时空平移 → 能量与动量

四个平移方向各给一个守恒荷：

- **时间平移** $\delta x^0=a$：$E = \displaystyle\int d^3x\,T^{00}$；
- **空间平移** $\delta x^i=a^i$：$P^i = \displaystyle\int d^3x\,T^{0i}$。

合起来 $P^\nu=\int d^3x\,T^{0\nu}$ 是守恒的总四动量。对实标量场具体计算：$\dfrac{\partial\mathcal L}{\partial(\partial_\mu\phi)}=\partial^\mu\phi$，故

$$T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - \eta^{\mu\nu}\mathcal L$$

（标量场碰巧对称：$T^{\mu\nu}=T^{\nu\mu}$；一般有旋场不对称，见 7.3）。能量密度

$$T^{00} = \dot\phi^2 - \mathcal L = \frac12\dot\phi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2 = \mathcal H,$$

正是第 5 节的哈密顿密度——**哈密顿量 = 时间平移的诺特荷**，这与分析力学里"$H$ 生成时间平移"完全呼应。动量密度 $T^{0i}=-\dot\phi\,\partial_i\phi$（负号来自空间指标的号差）。

### 7.2 U(1) 整体相位对称 → 电荷

取复标量场（把 $\phi$ 与 $\phi^*$ 当独立变量）：

$$\mathcal L = (\partial_\mu\phi^*)(\partial^\mu\phi) - m^2\phi^*\phi.$$

它在整体相位转动下不变（$\mathcal L$ 严格不变，$K^\mu=0$）：

$$\phi \to e^{i\alpha}\phi, \qquad \phi^*\to e^{-i\alpha}\phi^* \qquad\Longrightarrow\qquad \Delta\phi = i\phi,\quad \Delta\phi^* = -i\phi^*.$$

诺特流（两个场各自的贡献相加）：

$$j^\mu = \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\Delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi^*)}\,\Delta\phi^* = (\partial^\mu\phi^*)(i\phi) + (\partial^\mu\phi)(-i\phi^*) = -i\big(\phi^*\partial^\mu\phi - \phi\,\partial^\mu\phi^*\big).$$

整体乘以 $-1$ 只是"正电荷"的命名约定，写成标准形式

$$j^\mu = i\big(\phi^*\partial^\mu\phi - \phi\,\partial^\mu\phi^*\big), \qquad j^0 = i\big(\phi^*\partial^0\phi - \phi\,\partial^0\phi^*\big).$$

这正是第一篇里 KG 方程那个"因 $j^0$ 不定号而被判死刑、不能当概率密度"的守恒流！现在它的真面目清楚了：**$j^0$ 是电荷密度，本来就不该正定**——正能解与负能解携带相反的荷，量子化后它们就是粒子与反粒子（见后续笔记）。第一篇的错误不是算错了流，而是认错了流的物理身份。

对 Dirac 场同样成立：$\psi\to e^{i\alpha}\psi$ 给出 $j^\mu=\bar\psi\gamma^\mu\psi$，$j^0=\psi^\dagger\psi\ge 0$ 碰巧正定——但守恒的真正原因同样是 U(1) 对称性，而不是"碰巧正定"。

### 7.3 洛伦兹变换 → 角动量（简述）

无穷小洛伦兹变换 $\delta x^\mu = \omega^\mu_{\ \nu}\,x^\nu$，反对称性 $\omega_{\mu\nu}=-\omega_{\nu\mu}$ 给出 $6$ 个独立参数（3 转动 + 3 推快/boost）。代入 6.3 的公式，利用 $\omega$ 的反对称性可把守恒流写成

$$M^{\mu\nu\rho} = x^\nu T^{\mu\rho} - x^\rho T^{\mu\nu}, \qquad \partial_\mu M^{\mu\nu\rho}=0,$$

守恒荷 $J^{\nu\rho}=\int d^3x\,M^{0\nu\rho}$：空间–空间分量 $J^{ij}$ 是**角动量**，时间–空间分量 $J^{0i}$ 对应 boost 的守恒量（质心定理的相对论版本）。

两点注记，都只需知道结论：

- 对有旋场（矢量、旋量），$\Delta\phi$ 还多一项"自旋部分"（如 $A_\mu$ 作为矢量自身也要转），$M^{\mu\nu\rho}$ 相应多出**自旋角动量**项——轨道部分与自旋部分单独都不守恒，合起来才守恒；
- 正则 $T^{\mu\nu}$ 对有旋场一般不对称，可通过加"改进项"（散度类项，不改变守恒荷）把它对称化，即 **Belinfante 对称化**；对称化后的 $T^{\mu\nu}$ 正是广义相对论里引力场的源。细节见 Peskin §2.2 或 Schwartz 第 3 章。

## 8. 往前看：对称性是整个标准模型的骨架

把本章提炼成一台机器：

$$\text{连续对称性（一个群）}\ \xrightarrow{\text{诺特定理}}\ \text{守恒流}\ \xrightarrow{\int d^3x\,j^0}\ \text{守恒荷}.$$

能量、动量、角动量、电荷——物理学里所有"守恒量"都是这台机器的产出。这绝不是巧合：诺特定理说明**守恒律不是额外的经验事实，而是对称性的推论**。标准模型的整个构造逻辑就是这台机器的工业化应用：先指定对称群 $SU(3)\times SU(2)\times U(1)$，再要求拉氏量不变，相互作用的形式就被锁死。

而且本章的对称性还只是"**整体**"对称：变换参数 $\alpha$ 是全时空统一的常数。**规范对称性**是它的升级：允许 $\alpha=\alpha(x)$ 逐点不同。$\mathcal L$ 单靠旧场不可能保持这种不变性——$\partial_\mu\alpha(x)$ 会捣乱——除非引入一个新场（规范场）按特定方式变换去"吸收"它。换言之，**局域对称性强迫相互作用存在**：U(1) 局域化给出电磁场与光子，$SU(3)$ 局域化给出胶子。这就是"对称性决定相互作用"，是第 5–6 阶段的主线（见后续笔记）。

## 9. 小结

- 场 = 无穷多自由度的力学系统：分立指标 $i\to$ 连续标签 $x$，$L=\sum_i[\cdots]\to\int d^3x\,\mathcal L$。
- 作用量 $S=\int d^4x\,\mathcal L$，$\mathcal L$ 取洛伦兹标量则协变性免费；$\delta S=0$（+ 分部积分）给出场的欧拉–拉格朗日方程 $\partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}-\frac{\partial\mathcal L}{\partial\phi}=0$。
- $\mathcal L=\frac12(\partial\phi)^2-\frac12m^2\phi^2\to$ KG；$\mathcal L=-\frac14F^2\to$ Maxwell；$\mathcal L=\bar\psi(i\gamma^\mu\partial_\mu-m)\psi\to$ Dirac——三个"相对论波动方程"的统一身份：经典场的运动方程。
- 正则动量 $\pi=\partial\mathcal L/\partial\dot\phi$，$H=\int(\pi\dot\phi-\mathcal L)$：正则量子化的入口。
- 诺特定理：off shell 对称（$\delta\mathcal L=\partial_\mu K^\mu$）+ on shell 运动方程 ⟹ 守恒流 $j^\mu=\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\Delta\phi - K^\mu$。

| 对称性 | 无穷小变换 | 守恒流 | 守恒荷 |
|---|---|---|---|
| 时间平移 | $\delta x^0=a$ | $T^{\mu 0}$ | $E=\int T^{00}$ |
| 空间平移 | $\delta x^i=a^i$ | $T^{\mu i}$ | $P^i=\int T^{0i}$ |
| U(1) 相位 | $\phi\to e^{i\alpha}\phi$ | $j^\mu=i(\phi^*\partial^\mu\phi-\phi\,\partial^\mu\phi^*)$ | 电荷 $Q$ |
| 洛伦兹 | $\delta x^\mu=\omega^\mu_{\ \nu}x^\nu$ | $M^{\mu\nu\rho}=x^\nu T^{\mu\rho}-x^\rho T^{\mu\nu}$ | 角动量 + boost |

## 自检问题

**1.** 从珠链的运动方程 $m\ddot q_i=k(q_{i+1}-2q_i+q_{i-1})$ 出发，求其色散关系 $\omega(k)$，并验证长波极限与连续场方程 $\mu\,\partial_t^2\phi=Y\,\partial_x^2\phi$ 一致。

<details markdown="1"><summary>点击显示答案</summary>

取格点平面波试解 $q_i(t)=e^{i(kia-\omega t)}$（$a$ 为间距），代入：

$$-m\omega^2 = k\big(e^{ika}-2+e^{-ika}\big) = 2k(\cos ka - 1) = -4k\sin^2\frac{ka}{2},$$

故色散关系为

$$\omega(k) = 2\sqrt{\frac{k}{m}}\,\Big|\sin\frac{ka}{2}\Big|.$$

这是周期函数，第一布里渊区 $|k|\le\pi/a$——分立晶格只有有限带宽，这是连续体所没有的特征。

长波极限 $ka\ll1$：$\sin(ka/2)\simeq ka/2$，于是

$$\omega \simeq a\sqrt{\frac{k}{m}}\,|k| = \sqrt{\frac{Y}{\mu}}\,|k| \equiv v|k|,$$

其中用到 $m=\mu a$、$Y=ka$，故 $a^2 k/m = (ka)\cdot(a/m) = Y/\mu$，即 $v^2=Y/\mu$。

另一边，连续波动方程 $\mu\,\partial_t^2\phi=Y\,\partial_x^2\phi$ 代入平面波 $\phi=e^{i(kx-\omega t)}$ 得 $\mu\omega^2=Yk^2$，即 $\omega=\sqrt{Y/\mu}\,|k|$。两者精确一致：**连续极限只保留了分立色散关系的长波（线性）部分**；短波物理（布里渊区边界、色散弯曲）在取极限时被丢弃了。

</details>

**2.** 补全从 $\delta S=0$ 到场的欧拉–拉格朗日方程的推导：明确写出分部积分与边界项处理，并说明"$\mathcal L$ 只依赖 $\phi$ 与 $\partial_\mu\phi$"这一假设用在哪里。

<details markdown="1"><summary>点击显示答案</summary>

设 $S=\int d^4x\,\mathcal L(\phi,\partial_\mu\phi)$，变分 $\phi\to\phi+\delta\phi$，$\delta\phi$ 在时空边界 $\partial\Omega$ 上为零。因 $\mathcal L$ 只依赖 $\phi$ 与 $\partial_\mu\phi$（不含更高阶导数与显式 $x^\mu$），链式法则只给出两项：

$$\delta S = \int d^4x\left[\frac{\partial\mathcal L}{\partial\phi}\delta\phi + \frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\mu(\delta\phi)\right].$$

（若 $\mathcal L$ 含二阶导数 $\partial_\mu\partial_\nu\phi$，这里会多出需要两次分部积分的项，运动方程可达四阶——所以"只含一阶导数"的假设就用在"链式法则到此为止"这一步。）

对第二项用乘积求导的逆运算：

$$\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\partial_\mu(\delta\phi) = \partial_\mu\!\left[\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\delta\phi\right] - \partial_\mu\!\left(\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right)\delta\phi.$$

全导数项由高斯定理化为边界积分：

$$\int d^4x\,\partial_\mu\!\left[\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\delta\phi\right] = \oint_{\partial\Omega} dS_\mu\,\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\,\delta\phi = 0,$$

因 $\delta\phi|_{\partial\Omega}=0$。剩余

$$\delta S = \int d^4x\left[\frac{\partial\mathcal L}{\partial\phi} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\right]\delta\phi = 0 \quad \forall\,\delta\phi,$$

由变分法基本引理（$\delta\phi$ 任意，可取成任意点附近的鼓包函数），括号处处为零，即欧拉–拉格朗日方程。

</details>

**3.** 对 $\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}$（$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$），验证 $\dfrac{\partial\mathcal L}{\partial(\partial_\mu A_\nu)}=-F^{\mu\nu}$，并补全"真空 Maxwell 方程"的全部四条从何而来。

<details markdown="1"><summary>点击显示答案</summary>

先把 $\mathcal L$ 展开成两项：

$$\mathcal L = -\frac14\big(\partial_\alpha A_\beta-\partial_\beta A_\alpha\big)\big(\partial^\alpha A^\beta-\partial^\beta A^\alpha\big) = -\frac12\Big[(\partial_\alpha A_\beta)(\partial^\alpha A^\beta) - (\partial_\alpha A_\beta)(\partial^\beta A^\alpha)\Big],$$

其中交叉项用了哑指标换名与反对称性合并。对 $\partial_\mu A_\nu$ 求导（用 $\dfrac{\partial(\partial_\alpha A_\beta)}{\partial(\partial_\mu A_\nu)}=\delta^\mu_\alpha\delta^\nu_\beta$）：

- 第一项贡献：$-\frac12\cdot 2\,\partial^\mu A^\nu = -\partial^\mu A^\nu$；
- 第二项贡献：$+\frac12\cdot 2\,\partial^\nu A^\mu = +\partial^\nu A^\mu$。

合计 $\dfrac{\partial\mathcal L}{\partial(\partial_\mu A_\nu)} = -\big(\partial^\mu A^\nu-\partial^\nu A^\mu\big) = -F^{\mu\nu}$。

又 $\partial\mathcal L/\partial A_\nu=0$（$\mathcal L$ 不含 $A$ 本身），欧拉–拉格朗日方程给出

$$\partial_\mu F^{\mu\nu}=0.$$

展开：$\nu=0$ 时 $\partial_i F^{i0}=\nabla\cdot\vec E=0$（无源高斯定律）；$\nu=i$ 时 $\partial_0F^{0i}+\partial_jF^{ji}=0$，用 $F^{0i}=-E^i$、$F^{ij}=-\epsilon_{ijk}B_k$ 化为 $\nabla\times\vec B=\partial_t\vec E$（无电流安培定律）。

剩下两条**不是**运动方程，而是 $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ 这一**定义**的恒等式。直接代入：

$$\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu} = (\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu) + \text{循环} = 0,$$

六项两两相消（偏导可交换）。取 $(\lambda,\mu,\nu)=(1,2,3)$ 得 $\nabla\cdot\vec B=0$（无磁单极），取 $(0,i,j)$ 组合得 $\nabla\times\vec E=-\partial_t\vec B$（法拉第定律）。四条真空 Maxwell 方程齐了：**两条来自变分原理，两条来自"用势表示场"的几何。**

</details>

**4.** 对实标量场 $\mathcal L=\frac12(\partial_\mu\phi)(\partial^\mu\phi)-\frac12m^2\phi^2$，写出 $T^{\mu\nu}$ 与能量密度 $T^{00}$，并直接验证 on shell 有 $\partial_\mu T^{\mu\nu}=0$。

<details markdown="1"><summary>点击显示答案</summary>

由 $T^\mu_{\ \nu}=\dfrac{\partial\mathcal L}{\partial(\partial_\mu\phi)}\partial_\nu\phi-\delta^\mu_{\ \nu}\mathcal L$ 及 $\dfrac{\partial\mathcal L}{\partial(\partial_\mu\phi)}=\partial^\mu\phi$，升指标得

$$T^{\mu\nu} = \partial^\mu\phi\,\partial^\nu\phi - \eta^{\mu\nu}\mathcal L = \partial^\mu\phi\,\partial^\nu\phi - \frac12\eta^{\mu\nu}\big[(\partial_\alpha\phi)(\partial^\alpha\phi)-m^2\phi^2\big].$$

能量密度：

$$T^{00} = \dot\phi^2 - \mathcal L = \dot\phi^2 - \frac12\dot\phi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2 = \frac12\dot\phi^2 + \frac12(\nabla\phi)^2 + \frac12m^2\phi^2 \ge 0.$$

注意它**正定**——经典场论里能量毫无问题；第一篇 KG 方程的"负能量"是把它当单粒子波函数的错误解读所致。

验证守恒（逐项对 $\mu$ 求散度）：

$$\partial_\mu T^{\mu\nu} = (\partial_\mu\partial^\mu\phi)\,\partial^\nu\phi + \partial^\mu\phi\,\partial_\mu\partial^\nu\phi - \partial^\nu\mathcal L.$$

而

$$\partial^\nu\mathcal L = \partial^\nu\Big[\frac12(\partial_\alpha\phi)(\partial^\alpha\phi) - \frac12m^2\phi^2\Big] = \partial^\alpha\phi\,\partial^\nu\partial_\alpha\phi - m^2\phi\,\partial^\nu\phi,$$

（$\frac12$ 与对称两项合并成一项）代回，中间两项 $\partial^\mu\phi\,\partial_\mu\partial^\nu\phi$ 与 $\partial^\alpha\phi\,\partial^\nu\partial_\alpha\phi$ 是同一个表达式（换哑指标名），恰好抵消，剩下

$$\partial_\mu T^{\mu\nu} = (\Box\phi)\,\partial^\nu\phi + m^2\phi\,\partial^\nu\phi = \big[(\Box+m^2)\phi\big]\,\partial^\nu\phi = 0,$$

最后一步用了运动方程 $(\Box+m^2)\phi=0$。**守恒只在 on shell 成立**——这正是第 6 节强调的"对称性 + 运动方程的联合产物"在具体例子中的样子。

</details>

**5.** 复标量场的 U(1) 诺特流 $j^\mu=i(\phi^*\partial^\mu\phi-\phi\,\partial^\mu\phi^*)$ 中，$j^0$ 不定号，为什么这 disqualify 它做概率密度、却完全不妨碍它做电荷密度？Dirac 场的情形又有何不同？

<details markdown="1"><summary>点击显示答案</summary>

**概率密度的要求**：必须把 $|j^0|$ 解释成"在某处找到粒子的概率"，因此 (i) $j^0\ge 0$ 处处成立，(ii) 归一化 $\int d^3x\,j^0=1$ 不随时间变。看平面波解 $\phi\propto e^{-i\omega t+i\vec p\cdot\vec x}$：$j^0=i(\phi^*\,\partial^0\phi-\phi\,\partial^0\phi^*)$，代入 $\partial^0\phi=-i\omega\phi$、$\partial^0\phi^*=+i\omega\phi^*$ 得 $j^0=2\omega|\phi|^2>0$；但对负频率解 $\phi\propto e^{+i\omega t-i\vec p\cdot\vec x}$，同样计算给出 $j^0=-2\omega|\phi|^2<0$。KG 方程正负频率解同样合法、缺一不可（完备性），所以 $j^0$ 可正可负——**(i) 失败**，它做不了概率密度。这正是第一篇对 KG 的判决。

**电荷密度的逻辑完全不同**：电荷本来就有正负两种，$j^0$ 变号是**优点**而非缺陷——它自动容纳了两种荷。诺特定理只要求 U(1) 对称性，保证 $\partial_\mu j^\mu=0$ 与 $Q$ 守恒；$j^0$ 的符号约定哪个是"正"纯属命名。量子化之后（第 4 阶段），正频率解承载粒子、负频率解翻转为承载反粒子，$Q$ 变成粒子数减负粒子数的算符——"不定号的经典流"摇身一变成为"粒子–反粒子对称"的预告。

**Dirac 场**：$j^\mu=\bar\psi\gamma^\mu\psi$，$j^0=\bar\psi\gamma^0\psi=\psi^\dagger\psi=\sum_a|\psi_a|^2\ge 0$，正定。所以历史上 Dirac 方程能（暂时）被当作概率诠释的单粒子方程，救场的就是 $\gamma^0$ 这个因子：$\bar\psi\gamma^\mu\psi$ 里 $\mu=0$ 分量恰好变成 $\psi^\dagger\psi$。但负能解与空穴问题依旧存在（第一篇），真正彻底的解决仍然是场量子化——那时 $j^\mu$ 同样是守恒的**电荷流**（正电子带反号荷），"正定"只是经典旋量层面的巧合。

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》§2.2——诺特定理的标准推导与能动张量，与本篇第 6、7 节直接对应。
- Schwartz《Quantum Field Theory and the Standard Model》第 3 章（Classical Field Theory）——拉氏场论与诺特定理，含 Belinfante 张量。
- Zee《Quantum Field Theory in a Nutshell》第 I.3 章（From Mattress to Field）——"床垫模型"的珠链连续极限，本篇第 2 节的来源。
- Srednicki《Quantum Field Theory》第 1–3 讲——标量场拉氏量、正则动量与量子化的衔接。
- Goldstein《Classical Mechanics》连续系统与场一章——从分立质点到场的分析力学推广（经典力学视角）。
