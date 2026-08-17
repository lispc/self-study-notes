# 拓扑物态入门：Berry 相、SSH 模型与陈数

> 本书位置：凝聚态物理入门导论第 12 章（第三部分：现代专题）
> 前置知识：能带论（第 4 章：Bloch 定理、Brillouin 区、紧束缚模型）、本科量子力学（含时微扰、绝热定理最好见过）、量子 Hall 效应的实验事实（[第 11 章](11-quantum-hall-effect.md)）。
> 学习目标：理解为什么有些物态不能用局域序参量刻画；掌握 Berry 相位、Berry 联络与曲率的推导；把 SSH 模型从紧束缚哈密顿量一路算到绕数与边缘零模；知道陈数（TKNN 不变量）的定义与量子化 Hall 电导的关系；对拓扑绝缘体的 $Z_2$ 分类有定性的认识。

约定：本章保留 $\hbar$（必要时出现 $k_B$），与本书其他章一致；晶格常数常取为 $1$ 以简化记号。

---

## 1. 一句话总结

**绝缘体并不都平庸：两块能隙相同的材料，其 Bloch 波函数在 Brillouin 区上的"整体扭结方式"可以不同，这种扭结由整数拓扑不变量（绕数、陈数、$Z_2$ 指标）刻画，只要体材料能隙不关闭就改变不掉；而拓扑不变量不为零的材料，边界上必然存在受保护的导电态——这就是拓扑物态的核心逻辑，Berry 相位则是把"波函数的整体几何"变成可计算量的通用工具。**

## 2. 什么是拓扑物态

到上一章为止，本书描述相与相变的语言都是 Landau 的：**对称性 + 局域序参量**。铁磁体自发破缺旋转对称，序参量是局域磁化强度 $\vec M(\vec x)$；超导体破缺 U(1) 规范对称，序参量是配对振幅 $\langle c_\uparrow c_\downarrow\rangle$（见第 7、8 章）。序参量是局域的，相变伴随对称性改变。

1980 年整数量子 Hall 效应的发现（第 11 章）打破了这个框架。二维电子气在强磁场下的 Hall 电导精确量子化为 $\sigma_{xy} = N e^2/h$，$N$ 是整数，精度达 $10^{-9}$ 量级。问题出在哪：

- 不同 $N$ 的量子 Hall 态**对称性完全相同**，没有局域序参量能区分它们；
- $N$ 是整数，不随杂质、样品形状、相互作用细节改变——它是**全局**的性质；
- 要改变 $N$，必须让体材料的能隙关闭一次（经过金属性的临界点），即"拓扑相变不遵循 Landau 范式"。

这类由**全局拓扑不变量**而非局域序参量分类的物态，统称**拓扑物态**。粗略地说，拓扑不变量是"Bloch 波函数作为 Brillouin 区上的映射"的同伦类指标：连续地形变哈密顿量（不关闭能隙），波函数连续变化，整数指标不可能连续地从一个整数流到另一个整数，所以它被保护。本章的任务是把这句话变成具体计算。

三件事值得先记住：

1. **工具**：Berry 相位——波函数沿参数空间闭回路转一圈带回来的几何相位，是所有拓扑不变量的建筑砖块。
2. **最小模型**：SSH 模型——一维二聚化链，拓扑不变量是绕数 $\nu$，物理后果是边缘零能模。
3. **物理后果**：体-边对应——体的拓扑数 $=$ 边界上受保护态的数目。

## 3. Berry 相位：绝热演化中的几何相位

### 3.1 绝热定理与"被遗忘的相位"

设哈密顿量依赖一组外部参数 $\vec R = (R_1, R_2, \dots)$（可以是磁场、原子位置、动量……），$\vec R$ 随时间缓慢变化：$H(t) = H(\vec R(t))$。对每个瞬时的 $\vec R$，有瞬时本征态

$$H(\vec R)\,\lvert n(\vec R)\rangle = E_n(\vec R)\,\lvert n(\vec R)\rangle.$$

**绝热定理**：若系统 $t=0$ 时处于 $\lvert n(\vec R(0))\rangle$，且 $\vec R(t)$ 变化足够慢（$\hbar\dot{\vec R}$ 远小于能隙乘相关矩阵元），则系统始终跟着瞬时本征态走：

$$\lvert\psi(t)\rangle = e^{i\gamma_n(t)}\,e^{-\frac{i}{\hbar}\int_0^t E_n(\vec R(t'))\,dt'}\,\lvert n(\vec R(t))\rangle.$$

第二个因子是熟悉的**动力学相位**；Berry（1984）的洞见是：第一个相位 $\gamma_n$ 不是可有可无的约定，它含有物理。

### 3.2 Berry 联络：推导关键步骤

把上面的试探解代入含时 Schrödinger 方程 $i\hbar\,\partial_t\lvert\psi\rangle = H\lvert\psi\rangle$。左端对时间求导，利用 $H\lvert n\rangle = E_n\lvert n\rangle$ 后，动力学相位项恰好与右端抵消，剩下

$$-\hbar\,\dot\gamma_n\,\lvert n\rangle + i\hbar\,\partial_t\lvert n\rangle = 0.$$

左乘 $\langle n(\vec R(t))\rvert$，得

$$\dot\gamma_n = i\,\langle n\vert\partial_t n\rangle = i\,\langle n\vert\vec\nabla_{\!\vec R}\, n\rangle\cdot\dot{\vec R}.$$

（用到 $\langle n\vert\partial_t n\rangle$ 为纯虚数——对 $\langle n\vert n\rangle = 1$ 求导即知 $2\,\mathrm{Re}\langle n\vert\partial_t n\rangle = 0$。）于是

$$\gamma_n(T) = \int_0^T i\,\langle n\vert\vec\nabla_{\!\vec R}\,n\rangle\cdot\dot{\vec R}\,dt \equiv \int_{\mathcal C} \vec{\mathcal A}_n(\vec R)\cdot d\vec R,$$

其中定义了 **Berry 联络**

$$\vec{\mathcal A}_n(\vec R) \equiv i\,\langle n(\vec R)\vert\vec\nabla_{\!\vec R}\vert n(\vec R)\rangle.$$

注意它只依赖参数空间中的路径 $\mathcal C$，不依赖走这条路径的快慢——"绝热"只保证系统不跳能级，相位本身与用时无关。这就是为什么它叫**几何相位**。

**规范结构**：瞬时本征态的相位是人为约定。若重新定义 $\lvert n(\vec R)\rangle \to e^{i\alpha(\vec R)}\lvert n(\vec R)\rangle$，则

$$\vec{\mathcal A}_n \to \vec{\mathcal A}_n - \vec\nabla_{\!\vec R}\,\alpha,$$

与电磁学中矢势的规范变换一模一样（数学上 Berry 联络就是一个 U(1) 联络）。所以对**开放路径**，$\gamma_n$ 依赖于相位约定，本身不物理。

### 3.3 闭回路：Berry 相 = 曲率通量

让参数走一条**闭回路** $\mathcal C$：$\vec R(T) = \vec R(0)$。此时态矢首尾必须重合到只差一个相位，单值性要求 $\alpha(T) - \alpha(0) = 2\pi\times\text{整数}$，于是

$$\gamma_n(\mathcal C) = \oint_{\mathcal C} \vec{\mathcal A}_n\cdot d\vec R \pmod{2\pi}$$

是**规范不变**的物理量。仿照电磁学定义规范不变的 **Berry 曲率**（三维参数空间中）

$$\vec\Omega_n = \vec\nabla_{\!\vec R}\times\vec{\mathcal A}_n,$$

用 Stokes 定理，闭路相位等于曲率的通量：

$$\gamma_n(\mathcal C) = \int_{S}\vec\Omega_n\cdot d\vec S,$$

$S$ 是以 $\mathcal C$ 为边界的任意曲面。曲率有一个便于实际计算的形式：对 $H\lvert n\rangle = E_n\lvert n\rangle$ 求梯度并左乘 $\langle m\rvert$（$m\neq n$），得

$$\langle m\vert\vec\nabla_{\!\vec R}\,n\rangle = \frac{\langle m\vert\vec\nabla_{\!\vec R}H\vert n\rangle}{E_n - E_m},$$

代入曲率定义整理后得到

$$\vec\Omega_n = -\,\mathrm{Im}\sum_{m\neq n}\frac{2\,\langle n\vert\vec\nabla_{\!\vec R}H\vert m\rangle\times\langle m\vert\vec\nabla_{\!\vec R}H\vert n\rangle}{(E_n-E_m)^2}.$$

两点读法：分母是能隙的平方——**简并点（能级交叉）是曲率的"源"**，就像磁单极；曲率完全由哈密顿量决定，不含任何相位约定。

<details markdown="1"><summary>补充说明：自旋 1/2 在磁场中的 Berry 相——立体角的一半</summary>

经典例子：自旋 1/2 置于方向缓慢转动的磁场中，$H = -\mu\,\vec B\cdot\vec\sigma$，参数空间就是 $\vec B$ 本身。自旋顺（逆）着 $\vec B$ 的瞬时本征态 $\lvert\pm;\hat B\rangle$ 的 Berry 曲率，代入上面的公式（或用球坐标直接算）得

$$\vec\Omega_\pm = \mp\,\frac{\hat B}{2 B^2},$$

即 $\vec B=0$ 处有一个"磁单极"。当 $\hat B$ 沿闭合锥面转一圈，Berry 相位为

$$\gamma_\pm = \mp\,\frac{\Omega_{\text{立体角}}}{2},$$

恰是回路张的立体角的一半。这个"$1/2$"与自旋 $1/2$ 的 SU(2) 双重覆盖同出一源（见 [QFT 书的 SO(3)/SU(2) 笔记](../../qft-sm/docs/stage-00-math/01-so3-su2-and-angular-momentum.md)）。能级简并点 $B=0$ 是曲率的奇点——这个图像在第 5 节理解陈数时还会回来。

</details>

### 3.4 Aharonov–Bohm 相位就是一个 Berry 相位

AB 效应中，带电粒子的波函数绕螺线管一周获得相位 $\Delta\varphi = q\oint\vec A\cdot d\vec x/\hbar$（推导见 [QFT 书《协变电磁学》4.4 节](../../qft-sm/docs/stage-03-relativistic-qm/03-covariant-electromagnetism.md)）。用 Berry 的语言重新看：把粒子装在一个无场区域的小盒子里，盒子中心位置 $\vec R$ 是绝热参数；螺线管的矢势 $\vec A(\vec r)$ 在盒内只是让瞬时本征波函数带上相位因子 $e^{iq\int^{\vec r}\vec A\cdot d\vec x'/\hbar}$，于是

$$\vec{\mathcal A}_n(\vec R) = i\langle n\vert\vec\nabla_{\!\vec R}\vert n\rangle = \frac{q}{\hbar}\vec A(\vec R).$$

电磁矢势直接当了 Berry 联络，AB 相位就是对应的闭路 Berry 相，磁通 $\Phi$ 就是 Berry 曲率通量。电磁学中的"规范势—场强—通量"三件套，在参数空间里以"Berry 联络—曲率—相位"的样子原样重现——这不是巧合，规范场论的数学（纤维丛上的联络）同时支配着两者。凝聚态拓扑物态的全部不变量，都是 Berry 联络在 **Brillouin 区**这个参数空间上的积分。

## 4. SSH 模型：一维拓扑绝缘体完整算一遍

SSH 模型（Su–Schrieffer–Heeger，1979 年为聚乙炔而提）是最小、也是唯一能"算到底"的拓扑模型。本节的计算请跟着动手做一遍。

### 4.1 二聚化链与紧束缚哈密顿量

考虑一维链，每个原胞含 A、B 两个格点。电子只能在最近邻之间跳跃，且胞内跳跃 $v$ 与胞间跳跃 $w$ 不同（二聚化）：

$$H = \sum_{n=1}^{N}\Big[\,v\,c^\dagger_{A,n}c^{}_{B,n} + w\,c^\dagger_{A,n+1}c^{}_{B,n} + \mathrm{h.c.}\,\Big].$$

$v = w$ 就是普通的等间距链（第 4 章的单原子链，元胞里其实只有一个格点）；$v\neq w$ 时链上化学键长短交替，像聚乙炔里的单双键交替。设 $v, w > 0$，两个极限值得记住：

- $w = 0$：每个原胞内部自成二聚体，链断成互不相干的"哑铃"；
- $v = 0$：二聚体错开一格，**首尾各剩一个孤悬的格点**。

直觉已经暗示：$v < w$ 的链两头有"无人配对"的边缘格点。下面把这句话变成定理。

### 4.2 动量空间：$H(k) = \vec d(k)\cdot\vec\sigma$

周期边界条件下做 Fourier 变换，$c_{\alpha,n} = \frac{1}{\sqrt N}\sum_k e^{ikn}c_{\alpha,k}$（晶格常数取 1，$k \in (-\pi, \pi]$），哈密顿量按 $k$ 分块：

$$H = \sum_k \begin{pmatrix} c^\dagger_{A,k} & c^\dagger_{B,k} \end{pmatrix} H(k) \begin{pmatrix} c^{}_{A,k} \\ c^{}_{B,k} \end{pmatrix}, \qquad H(k) = \begin{pmatrix} 0 & h(k) \\ h^*(k) & 0 \end{pmatrix},$$

其中 $h(k) = v + w e^{-ik}$。写成泡利矩阵的形式：

$$H(k) = \vec d(k)\cdot\vec\sigma, \qquad \vec d(k) = \bigl(v + w\cos k,\ \ w\sin k,\ \ 0\bigr).$$

能谱立即得到：

$$E_\pm(k) = \pm\lvert\vec d(k)\rvert = \pm\sqrt{v^2 + w^2 + 2vw\cos k}.$$

两半填充时（每原胞一个电子）下能带填满，体系是绝缘体，能隙 $E_g = 2\lvert v - w\rvert$。**能隙只在 $v = w$（$k = \pi$）处关闭**——这正是候选的拓扑相变点。

注意 $\vec d(k)$ 被约束在 $xy$ 平面内（$d_z = 0$）。这不是偶然：哈密顿量有**手征（子格）对称性** $\sigma_z H(k)\sigma_z = -H(k)$，它迫使 $d_z = 0$，同时保证能谱关于 $E=0$ 对称。这条对称性是 SSH 拓扑保护的靠山。

### 4.3 绕数 $\nu$：定义与计算

$k$ 扫过 Brillouin 区一圈（$-\pi \to \pi$），$\vec d(k)$ 在 $xy$ 平面上描出一条闭曲线：以 $(v, 0)$ 为圆心、$w$ 为半径的圆。这条圆**是否绕过原点**，是一个只能取整数的性质——**绕数**

$$\nu = \frac{1}{2\pi}\oint dk\,\frac{d_x\,\partial_k d_y - d_y\,\partial_k d_x}{d_x^2 + d_y^2} = \frac{1}{2\pi}\oint d\varphi,$$

其中 $\varphi(k) = \arg\bigl(d_x + i d_y\bigr)$ 是 $\vec d$ 的方位角。代入 $\vec d(k)$ 直接算被积函数：

$$d_x\,\partial_k d_y - d_y\,\partial_k d_x = (v + w\cos k)(w\cos k) - (w\sin k)(-w\sin k) = vw\cos k + w^2,$$

所以

$$\nu = \frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{w^2 + vw\cos k}{v^2 + w^2 + 2vw\cos k}\,dk.$$

这个积分可以用围道积分严格做（令 $z = e^{ik}$，用辐角原理数零点，见自检第 2 题），但几何图像更快：

- $v > w$：圆不包原点，$\varphi$ 来回摆动后净转角为零，$\nu = 0$；
- $v < w$：圆包原点，$\varphi$ 单调扫过 $2\pi$，$\nu = 1$。

（验证极限：$v = 0$ 时 $\vec d = w(\cos k, \sin k)$，$\varphi = k$，$\nu = 1$；$w = 0$ 时 $\vec d$ 缩成一点，$\nu = 0$。）

**同伦论证（为什么 $\nu$ 改不动）**：$\nu$ 是映射 $k \mapsto \hat d(k)$（从圆 $S^1$ 到圆 $S^1$，因为 $\vec d \neq 0$ 时可归一化）的环绕次数，是整数。连续改变 $v/w$ 而不经过 $v = w$，曲线 $\vec d(k)$ 连续形变且始终不碰原点，环绕次数不可能连续地从 0 变成 1——**只有能隙关闭（$\vec d = 0$ 有解）时 $\nu$ 才能跳变**。这就是"拓扑不变量被能隙保护"的精确含义。

### 4.4 边缘零能模：显式求解

现在取**开边界**的链（$N$ 个原胞），设 $v < w$，直接找 $E = 0$ 的、只住在 A 子格上的态：

$$\lvert\psi\rangle = \sum_{n=1}^{N} \psi_{A,n}\,c^\dagger_{A,n}\lvert 0\rangle.$$

把它代入 $H\lvert\psi\rangle = 0$。$H$ 中含 $c^{}_{A,n}$ 的项作用后正比于 B 子格上的态，系数必须逐项为零。看第 $n$ 个 B 格点上的系数：来自胞内键 $v\,\psi_{A,n}$ 与胞间键 $w\,\psi_{A,n+1}$，于是

$$v\,\psi_{A,n} + w\,\psi_{A,n+1} = 0 \quad\Longrightarrow\quad \psi_{A,n+1} = -\frac{v}{w}\,\psi_{A,n},$$

即

$$\psi_{A,n} = \left(-\frac{v}{w}\right)^{n-1}\psi_{A,1},\qquad n = 1, \dots, N.$$

而 $H$ 中含 $c^{}_{B,n}$ 的项作用在 A 子格态上恒为零，A 格点方程自动满足——解是自洽的。这是一条**左边缘态**：波函数从链的左端起指数衰减，$v < w$ 保证可归一化，衰减长度（恢复晶格常数 $a$）

$$\xi = \frac{a}{\ln(w/v)}.$$

同理，只住 B 子格的零能解满足 $w\,\psi_{B,n} + v\,\psi_{B,n+1} \cdots$ 的镜像递推，给出**右边缘态** $\psi_{B,n} \propto (-v/w)^{N-n}$。几个要点：

- 零能是精确的：手征对称性保证能谱关于零对称，而边缘态只住一个子格，任何保持子格对称的微扰（包括无序）都不能让它离开 $E = 0$——只能改变它的衰减长度。
- $v = 0$ 极限：$\psi_{A,n} = \delta_{n,1}$，正是"孤悬格点"的图像，$\xi \to 0$。
- $v \to w$ 时 $\xi \to \infty$，边缘态溶入体中——与体材料能隙关闭同步发生，这不是巧合。
- $v > w$ 时递推给出的"解"指数增长、不可归一化：没有边缘态，与 $\nu = 0$ 一致。

### 4.5 体-边对应

把上面两节拼起来，得到 SSH 模型的核心定理的一个实例：

$$\nu = 1\ (\text{体}, v<w) \;\Longleftrightarrow\; \text{每条边缘一个零能模}; \qquad \nu = 0\ (\text{体}, v>w) \;\Longleftrightarrow\; \text{无边缘态}.$$

**体-边对应（bulk–boundary correspondence）**：周期体系的拓扑不变量（只用 Bloch 波函数定义，不提及任何边界）预言了开边界体系边缘态的数目。物理图像：界面两侧拓扑数之差只能由"界面上的态"来吸收——把 $\nu=1$ 的材料接到真空（$\nu = 0$）上，中间某处 $\nu$ 必须变化，而 $\nu$ 变化要求能隙关闭，能隙关闭处就是边缘态所在。这个论证对一切拓扑物态都成立：量子 Hall 的手征边缘态（第 11 章）、拓扑绝缘体的表面态（第 6 节）都是它的化身。

## 5. 二维推广：陈数与量子 Hall 效应

### 5.1 TKNN 不变量：Brillouin 区上的 Berry 曲率通量

二维晶体的 Bloch 态 $\lvert u_n(\vec k)\rangle$ 依赖参数 $\vec k = (k_x, k_y)$，而 Brillouin 区因 $k$ 与 $k + \vec G$ 等价，拓扑上是一个**环面** $T^2$。对每条能带定义 Berry 联络与曲率（参数空间就是动量空间）：

$$\mathcal A_i^{(n)}(\vec k) = i\langle u_n\vert\partial_{k_i} u_n\rangle, \qquad \Omega_n(\vec k) = \partial_{k_x}\mathcal A_y^{(n)} - \partial_{k_y}\mathcal A_x^{(n)},$$

**陈数**（第一陈数；在凝聚态语境常叫 TKNN 不变量，Thouless–Kohmoto–Nightingale–den Nijs，1982）定义为曲率在整个 Brillouin 区上的积分：

$$C_n = \frac{1}{2\pi}\int_{\mathrm{BZ}} \Omega_n(\vec k)\,d^2k \;\in\; \mathbb{Z}.$$

$C_n$ 必为整数的证明见自检第 5 题——本质原因是 Brillouin 区没有边界，"规范选择的接缝"上的 Berry 相位必须自洽，迫使总通量以 $2\pi$ 为单位量子化（与 Dirac 磁单极的荷量子化同一论证）。

**物理意义（TKNN 公式）**：对绝缘体（Fermi 面在能隙中），把所有填满能带的陈数求和，Hall 电导为

$$\sigma_{xy} = \frac{e^2}{h}\sum_{n\ \text{占据}} C_n,$$

即第 11 章里"精确量子化的整数" $N$ 不是 Landau 能级的计数游戏，而是占据带的几何性质（严格推导用 Kubo 公式，见参考； Landau 能级图像与陈数图像的联系也见第 11 章）。这解释了量子化对杂质与细节的惊人稳定性：改变 $C_n$ 需要关闭体材料能隙。

### 5.2 一个可算的模型：Qi–Wu–Zhang

无磁场的晶格模型也能有 $C \neq 0$（Haldane 1988 年首先在石墨烯蜂窝格子模型中指出这一点，其物理是"净磁通为零的交错磁通"）。最干净的例子是 Qi–Wu–Zhang 模型——正方格子上两轨道（或两子格）模型：

$$H(\vec k) = \sin k_x\,\sigma_x + \sin k_y\,\sigma_y + \bigl(m + \cos k_x + \cos k_y\bigr)\sigma_z.$$

相图一句话：$\lvert m\rvert > 2$ 时 $C = 0$（平庸绝缘体），$0 < \lvert m\rvert < 2$ 时 $C = \pm 1$（拓扑非平庸，符号在 $m=0$ 两侧相反），$m = 0, \pm 2$ 处能隙关闭、发生拓扑相变。它是 SSH 的二维表亲：同样两分量 $\vec d(\vec k)$，只是现在 $\vec d$ 有 $z$ 分量，拓扑荷从"绕数"升级为"球面覆盖次数"（$\hat d$ 把环面 $T^2$ 包到球面 $S^2$ 上的度数，正是陈数）。

## 6. 拓扑绝缘体：时间反演保护的 $Z_2$ 分类

陈数要求打破时间反演对称（时间反演把 $\vec k$ 与 Berry 曲率都反号，$\Omega$ 为奇函数时 $C = 0$）。那么**保持**时间反演的材料还有没有拓扑？2005 年 Kane–Mele 与 Bernevig–Zhang 的回答：有，靠**自旋轨道耦合**。

物理链条是这样的：强自旋轨道耦合（重原子，如 HgTe、Bi）使能带发生"反转"——原本在 Fermi 面上下的两条带交换了轨道成分。由于时间反演下 $T^2 = -1$（自旋 1/2 费米子），Kramers 定理保证每个 $\vec k$ 处能级至少二重简并，能带交叉不能完全消除；结果是体系不能用陈数分类，但存在一个新的 $\mathbb{Z}_2$ 不变量 $\nu \in \{0, 1\}$（可用占据带的"time-reversal polarization"或 Pfaffian 构造定义，细节见参考）。

- **$\nu = 1$：二维量子自旋 Hall 绝缘体**。边缘上有一对**螺旋（helical）态**：自旋向上的电子只往一个方向走、自旋向下只往反方向走。时间反演禁止背散射（背散射要求翻转自旋，而时间反演不变的非磁性杂质做不到），所以边缘导电受保护。2007 年 HgTe/CdTe 量子阱实验（König 等）观测到预言的 $2e^2/h$ 边缘电导平台。
- **三维推广：强拓扑绝缘体**（如 $\mathrm{Bi}_2\mathrm{Se}_3$、$\mathrm{Bi}_2\mathrm{Te}_3$）。表面上有**奇数个 Dirac 锥**：表面态的低能色散是 $E = \pm\hbar v_F\lvert\vec k\rvert$ 的二维无质量 Dirac 锥，自旋与动量锁定（spin-momentum locking）。单个 Dirac 锥无法在任何保持时间反演的二维晶格里单独存在（与下面第 7 节的费米子加倍定理呼应），它只能作为三维拓扑体材料的表面出现。ARPES 实验拍到的自旋分辨表面态能谱与这个图像精确吻合。

## 7. 与高能物理的联系

这一章到处是高能物理的"回声"。SSH 与 QWZ 的 $H(\vec k) = \vec d(\vec k)\cdot\vec\sigma$ 就是动量空间里的（无质量）Dirac 哈密顿量，能隙关闭点处的低能激发是货真价实的 Dirac/Weyl 费米子；石墨烯与拓扑绝缘体表面态把"Dirac 锥"从场论教科书搬上了实验台。更深一层的对应是**手征反常**：QFT 中 (1+1) 维无质量 Dirac 费米子在晶格上无法单独实现（Nielsen–Ninomiya 费米子加倍定理），正如 SSH 链单个边缘的零模必须成对出现；三维 Weyl 半金属的节点总是成对、外加平行电磁场时出现负磁阻（手征反常的凝聚态化身）；体-边对应本身正是高能理论家"反常入流（anomaly inflow）"——体理论的反常由边界模式精确抵消——的固体版本。学凝聚态拓扑，等于用便宜的模型把 QFT 最微妙的概念亲手算一遍。

## 8. 小结

| 概念 | 定义 | 物理后果 |
| --- | --- | --- |
| Berry 联络 | $\mathcal A_n = i\langle n\rvert\vec\nabla_{\!\vec R}\lvert n\rangle$ | 规范依赖，开路径相位不物理 |
| Berry 相位 | $\gamma_n = \oint \mathcal A_n\cdot d\vec R$（闭路，$\mathrm{mod}\ 2\pi$ 规范不变） | AB 相、绝热输运 |
| Berry 曲率 | $\Omega_n = \vec\nabla\times\vec{\mathcal A}_n$（规范不变） | 简并点是其"源"；一切拓扑不变量的原料 |
| SSH 绕数 | $\nu = \frac{1}{2\pi}\oint d\varphi \in \mathbb{Z}$ | $\nu = 1 \Leftrightarrow$ 边缘零模（体-边对应） |
| 陈数（TKNN） | $C_n = \frac{1}{2\pi}\int_{\mathrm{BZ}}\Omega_n\,d^2k \in \mathbb{Z}$ | $\sigma_{xy} = \frac{e^2}{h}\sum C_n$ |
| $Z_2$ 不变量 | $\nu \in \{0,1\}$，时间反演保护 | 螺旋边缘态 / 表面 Dirac 锥 |

- 拓扑物态不由局域序参量区分，而由 Bloch 波函数在 Brillouin 区上的整体拓扑分类；拓扑不变量是整数，只要不关闭体能隙就不可改变。
- 工具链：绝热演化 $\to$ Berry 联络 $\to$ Berry 曲率 $\to$ 在闭流形（回路 / Brillouin 区）上积分 $\to$ 整数不变量。
- 体-边对应把"体的整数"翻译成"边界的态"：SSH 的边缘零模、量子 Hall 的手征边缘态、拓扑绝缘体的 Dirac 表面态是同一原理的三个化身。

## 自检问题

**1.** 从含时 Schrödinger 方程出发，推导 Berry 相位满足 $\dot\gamma_n = i\langle n\vert\partial_t n\rangle$，并说明绝热近似在哪里进入、结果为什么不依赖演化快慢。

<details markdown="1"><summary>点击显示答案</summary>

写试探解 $\lvert\psi(t)\rangle = e^{i\gamma_n(t)}e^{-\frac{i}{\hbar}\int_0^t E_n\,dt'}\lvert n(\vec R(t))\rangle$，代入 $i\hbar\partial_t\lvert\psi\rangle = H\lvert\psi\rangle$。对时间求导给出三项：

$$i\hbar\partial_t\lvert\psi\rangle = \Big[-\hbar\dot\gamma_n + E_n\Big]\lvert\psi\rangle + i\hbar\,e^{i\gamma_n - \frac{i}{\hbar}\int E_n}\partial_t\lvert n\rangle,$$

右端 $H\lvert\psi\rangle = E_n\lvert\psi\rangle$。两边 $E_n$ 项抵消，剩下 $-\hbar\dot\gamma_n\lvert n\rangle + i\hbar\partial_t\lvert n\rangle = 0$，左乘 $\langle n\rvert$ 得 $\dot\gamma_n = i\langle n\vert\partial_t n\rangle$。

**绝热近似的位置**：完整代入时 $\partial_t\lvert n\rangle$ 在其他瞬时本征态 $\lvert m\rangle$（$m\neq n$）方向也有分量，会驱动跃迁；绝热条件（$\vec R$ 变化远慢于能隙对应的时间尺度）让我们丢掉这些分量，只保留沿 $\lvert n\rangle$ 的投影。

**与快慢无关**：积分得 $\gamma_n = \int i\langle n\vert\vec\nabla_{\!\vec R} n\rangle\cdot d\vec R$，被积函数只含参数空间的几何，时间 $t$ 完全消去——只要绝热条件成立，沿同一路径走多慢都给出同一相位，故称几何相位。

</details>

**2.** 计算 SSH 模型的绕数：证明 $v < w$ 时 $\nu = 1$、$v > w$ 时 $\nu = 0$。

<details markdown="1"><summary>点击显示答案</summary>

$\vec d(k) = (v + w\cos k,\ w\sin k)$ 是 $xy$ 平面内以 $(v,0)$ 为圆心、$w$ 为半径、逆时针描出的圆。绕数

$$\nu = \frac{1}{2\pi}\int_{-\pi}^{\pi}\frac{w^2 + vw\cos k}{v^2 + w^2 + 2vw\cos k}\,dk$$

是被包原点"看"这条圆转过的净角度除以 $2\pi$。

**几何论证**：$v > w$ 时原点在圆外，从原点看圆上的点，方位角 $\varphi(k)$ 在一个有限区间内来回摆动，走一圈净变化为零，$\nu = 0$；$v < w$ 时原点在圆内，$\varphi$ 单调转满 $2\pi$，$\nu = 1$；$v = w$ 时圆过原点，能隙关闭，$\nu$ 无定义。

**解析验证**（取极限）：$v = 0$ 时 $\vec d = w(\cos k, \sin k)$，$\varphi = k$，直接得 $\nu = \frac{1}{2\pi}\cdot 2\pi = 1$；$w = 0$ 时 $\vec d$ 恒为 $(v,0)$，$\varphi \equiv 0$，$\nu = 0$。严格积分可用 $z = e^{ik}$ 化为围道积分：记 $q(k) = d_x + i\,d_y = v + w e^{ik}$，则

$$\nu = \frac{1}{2\pi i}\int_{-\pi}^{\pi}\partial_k \ln q(k)\,dk = \frac{1}{2\pi i}\oint_{\lvert z\rvert = 1}\frac{q'(z)}{q(z)}\,dz,$$

由辐角原理等于 $q(z) = v + wz$ 在单位圆内的零点数减极点数：唯一零点 $z = -v/w$ 在圆内当且仅当 $v < w$（此时 $\nu = 1$），否则在圆外（$\nu = 0$），与几何一致。

</details>

**3.** 对开边界 SSH 链（$v < w$）显式求出左边缘零模波函数，并给出局域长度。

<details markdown="1"><summary>点击显示答案</summary>

设零模只住 A 子格：$\lvert\psi\rangle = \sum_n \psi_{A,n}c^\dagger_{A,n}\lvert 0\rangle$。代入 $H\lvert\psi\rangle = 0$：

- $H$ 中含湮灭算符 $c^{}_{B,n}$ 的项作用在该态上为零，故 A 格点上的方程自动满足；
- 含 $c^{}_{A,n}$ 的项作用后落在 B 子格，第 $n$ 个 B 格点上的总系数为 $v\,\psi_{A,n} + w\,\psi_{A,n+1}$（胞内键从 $A_n$ 跳到 $B_n$、胞间键从 $A_{n+1}$ 跳到 $B_n$）。

令其逐项为零得递推 $\psi_{A,n+1} = -(v/w)\psi_{A,n}$，解为

$$\psi_{A,n} = \left(-\frac{v}{w}\right)^{n-1}\psi_{A,1},$$

$v < w$ 保证 $\sum_n\lvert\psi_{A,n}\rvert^2$ 收敛（$N\to\infty$ 时），归一化后 $\lvert\psi_{A,1}\rvert^2 = 1 - (v/w)^2$。波函数振幅随 $e^{-na/\xi}$ 衰减，局域长度

$$\xi = \frac{a}{\ln(w/v)}.$$

右边缘同理存在只住 B 子格的零模 $\psi_{B,n} \propto (-v/w)^{N-n}$。$v = w$ 时 $\xi \to \infty$，边缘态不再局域——与体能隙关闭同时发生。

</details>

**4.** 用同伦论证说明：为什么只要不关闭能隙，连续改变 SSH 模型的参数就不可能改变绕数 $\nu$？

<details markdown="1"><summary>点击显示答案</summary>

绕数只在 $\vec d(k) \neq 0$ 对所有 $k$ 成立时（即能隙不关闭时）有定义。此时可把 $\vec d$ 归一化为 $\hat d = \vec d/\lvert\vec d\rvert$，于是 $\nu$ 是连续映射

$$\hat d:\ S^1\ (\text{Brillouin 区}) \longrightarrow S^1\ (\text{单位圆，因 } d_z = 0)$$

的**环绕次数**（映射度），由定义是整数。

现在连续改变参数（如 $v/w$）：$\vec d(k)$ 随之连续形变，只要中途不经过 $\vec d = 0$，映射 $\hat d$ 就连续形变（同伦）。整数函数若在参数上连续，只能是常数——$\nu$ 无法从 0 "连续滑到" 1。只有当能隙在某点关闭时，$\vec d(k^*) = 0$，$\hat d$ 在该点无定义，映射暂时失去意义，再次打开能隙后 $\nu$ 才允许取新的整数值。

这正是"能隙保护拓扑"的数学内容，也是拓扑相变（如 $v = w$）必然伴随能隙关闭的原因。完全相同的论证适用于陈数（$T^2 \to S^2$ 的映射度）与 $Z_2$ 指标。

</details>

**5.** 证明陈数 $C_n = \frac{1}{2\pi}\int_{\mathrm{BZ}}\Omega_n\,d^2k$ 必为整数。

<details markdown="1"><summary>点击显示答案</summary>

困难在于：Berry 联络 $\mathcal A_n = i\langle u_n\vert\nabla_{\vec k}\vert u_n\rangle$ 依赖 Bloch 态的相位（规范）选择，而**没有边界**的流形上一般不存在全局光滑的规范——若存在，Stokes 定理给出 $\int_{\mathrm{BZ}}\Omega = \oint_{\partial\mathrm{BZ}}\mathcal A = 0$，那就永远只有 $C = 0$ 了。

把 Brillouin 区（环面）分成两块有边界的区域 $S_1, S_2$，接缝为闭曲线 $\partial S$。在 $S_i$ 内各选一个光滑规范 $\lvert u^{(i)}(\vec k)\rangle$，接缝上两规范相差相位：

$$\lvert u^{(2)}\rangle = e^{i\chi(\vec k)}\lvert u^{(1)}\rangle \quad\Longrightarrow\quad \mathcal A^{(2)} = \mathcal A^{(1)} - \nabla_{\vec k}\chi.$$

对每块分别用 Stokes 定理：

$$2\pi C_n = \int_{S_1}\Omega + \int_{S_2}\Omega = \oint_{\partial S}\bigl(\mathcal A^{(1)} - \mathcal A^{(2)}\bigr)\cdot d\vec k = \oint_{\partial S}\nabla_{\vec k}\chi\cdot d\vec k.$$

右端是相位 $\chi$ 沿接缝转一圈的总变化。波函数必须单值，$e^{i\chi}$ 绕接缝一周必须回到自身，所以 $\chi$ 的净变化是 $2\pi$ 的整数倍：

$$C_n = \frac{1}{2\pi}\cdot 2\pi\times(\text{整数}) \in \mathbb{Z}.$$

这与 Dirac 证明磁单极荷量子化是同一个论证（球面两块补丁 + 接缝上单值性）：**曲率通量量子化的根源是相位选择的单值性约束**——Berry 相位的规范不变性加上 Brillouin 区的周期性，迫使 $C_n$ 取整数。

</details>

## 参考

- Asbóth, Oroszlány, Pályi《A Short Course on Topological Insulators》（Lecture Notes in Physics 919）第 1–2 章——SSH 模型与 Berry 相位的标准入门，本章第 4 节与之平行。
- Bernevig & Hughes《Topological Insulators and Topological Superconductors》第 1、3、8 章——Berry 相位、QWZ/Haldane 模型与 $Z_2$ 拓扑绝缘体。
- Thouless《Topological Quantum Numbers in Nonrelativistic Physics》第 1、4 章——TKNN 原始论证与 Kubo 公式推导。
- Kittel《固体物理导论》第 7 章、Ashcroft & Mermin《Solid State Physics》第 10 章——紧束缚近似与能带论打底（对应本书第 4 章）。
- 本书 [第 11 章](11-quantum-hall-effect.md)（量子 Hall 效应：Landau 能级与边缘态的实验入口）。
