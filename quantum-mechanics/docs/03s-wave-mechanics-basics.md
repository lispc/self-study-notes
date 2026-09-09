# 补充材料：波动力学基础——坐标表象、一维定态与隧穿

> 路线图位置：量子力学书 · 第一部分（形式体系）· 第 03 篇（[形式体系](03-formalism-hilbert-dirac.md)）的补充材料
> 前置知识：第 03 篇（坐标表象 $\psi(x) = \langle x|\psi\rangle$、正则对易关系 $[x,p] = i\hbar$、演化算符 $U = e^{-iHt/\hbar}$）。
> 学习目标：会把第 03 篇的抽象公设落到坐标表象，写出含时薛定谔方程并理解概率流；会处理自由粒子的波包运动；会陈述并使用一维定态的三条一般性质；会完整求解无限深与有限深方势阱；会计算方势垒透射系数与 $\delta$ 势的束缚态和散射态。
>
> 记号约定：本篇保留 $\hbar$（与第 03–06 篇一致，不使用自然单位）；一维问题中 $k$ 总表示波数、$\kappa$ 总表示衰减常数。

---

## 1. 一句话总结

**波动力学不是另一套理论，而是第 03 篇那台抽象机器在坐标表象里的长相：公设 4 落到 $\psi(x,t)$ 上就是含时薛定谔方程，概率守恒落成分微分形式就是连续性方程；一维定态问题的一切 richness 都来自同一条边界条件逻辑——波函数在大 $|x|$ 处必须可积，这条要求把连续的能量压成离散的束缚态谱，而在势垒区它放行了经典力学禁止的隧穿。**

本书像 Sakurai 一样先讲公理后讲波函数，所以本篇的问题不是"薛定谔方程是什么"，而是"第 03 篇的机器选了坐标基之后长什么样、能算什么"。答案分四块：坐标表象本身（第 2 节）、自由粒子（第 3 节）、一维定态的通论与两个标准势阱（第 4、5 节）、以及波动力学最出圈的预言——隧穿（第 6 节）。

## 2. 落到坐标表象：含时方程与概率流

### 2.1 公设 4 的坐标表象

第 03 篇的演化公设是抽象方程 $i\hbar\,\partial_t|\psi\rangle = H|\psi\rangle$。取坐标基 $|\vec r\rangle$，左乘 $\langle\vec r|$，代入坐标表象里的算符形象 $\langle\vec r|\vec p\,|\psi\rangle = -i\hbar\nabla\psi(\vec r)$（第 03 篇第 6.2 节）与经典哈密顿量的算符化 $H = p^2/2m + V(\vec r)$，立刻得到**含时薛定谔方程**：

$$i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V(\vec r)\,\psi.$$

这不是新公设，而是"公设 4 + 正则对易关系 + 一个具体 $H$"在坐标基下的分量写法——矩阵力学与波动力学的等价性（第 03 篇第 6.3 节）在这一行里最直观：同一台机器，换了一组基。

### 2.2 概率密度与概率流

Born 规则的坐标版本说 $\rho(\vec r,t) = \lvert\psi(\vec r,t)\rvert^2$ 是概率密度。抽象层面上概率守恒已由演化幺正性保证（第 03 篇自检问题 2）；坐标表象里它有一条更精细的**微分形式**：定义概率流密度

$$\vec j = \frac{\hbar}{2mi}\left(\psi^{*}\nabla\psi - \psi\nabla\psi^{*}\right) = \frac{\hbar}{m}\operatorname{Im}\left(\psi^{*}\nabla\psi\right),$$

则由薛定谔方程可直接推出**连续性方程**（推导留自检问题 1）：

$$\frac{\partial\rho}{\partial t} + \nabla\cdot\vec j = 0.$$

读法与电磁学完全一样：概率像流体一样局域守恒，某区域内概率的减少等于流出边界的通量。两个直接推论：

- **归一化的局域保持**：对全空间积分（$\psi$ 在无穷远足够快地衰减），$\frac{d}{dt}\int\rho\,d^3r = 0$——幺正性的微分化身；
- **定态的流**：若 $\psi$ 是实函数（可乘相位 $e^{-iEt/\hbar}$），则 $\vec j = 0$——一维束缚态可取实（第 4.2 节），故一维束缚态里没有净概率流，"定"字名副其实。平面波 $e^{ikx}$ 则给出 $\vec j = \hbar\vec k/m\cdot\lvert\psi\rvert^2$，即"速度 × 密度"，与流体力学的 $\rho\vec v$ 一致。

连续性方程里势 $V$ 在推导中自动消去（自检问题 1）——概率守恒不依赖势的具体形状，只依赖 $H$ 厄米。这条性质在数值模拟里也是检验算法正确性的第一探针。

## 3. 自由粒子：平面波、波包与展宽

### 3.1 平面波解与色散关系

$V = 0$ 时，能量本征态就是动量本征态：

$$\psi_k(x,t) = e^{i(kx - \omega t)}, \qquad E = \hbar\omega = \frac{\hbar^2k^2}{2m}.$$

$\omega(k) = \hbar k^2/2m$ 是自由粒子的**色散关系**——$\omega$ 不是 $k$ 的线性函数，这一件事决定了波包的全部命运（下两小节）。平面波本身不可归一化（$\delta$ 归一化，第 03 篇第 6.1 节），它不是物理态，而是叠加的"基函数"——正如第 03 篇强调的，连续谱本征矢是展开工具。

### 3.2 波包叠加：群速度 vs 相速度

物理的自由粒子是平面波的叠加——**波包**：

$$\psi(x,t) = \int_{-\infty}^{\infty}\frac{dk}{\sqrt{2\pi}}\,\tilde\psi(k)\,e^{i(kx - \omega(k)t)}.$$

这就是第 03 篇"动量表象与坐标表象之间是傅里叶变换"的时间演化版：每个 $k$ 分量只积累相位 $e^{-i\omega(k)t}$（定态叠加的标准操作）。设 $\tilde\psi(k)$ 集中在 $k_0$ 附近，把色散关系展开 $\omega(k) \approx \omega_0 + \omega'(k_0)(k - k_0)$，积分给出

$$\psi(x,t) \approx e^{i(k_0x - \omega_0t)}\,F\big(x - v_g t\big), \qquad v_g = \frac{d\omega}{dk}\bigg|_{k_0} = \frac{\hbar k_0}{m}.$$

包络 $F$ 以**群速度** $v_g$ 整体平移，而载波相位以**相速度** $v_p = \omega/k = \hbar k/2m$ 行进。注意两个事实：

- $v_g = \hbar k_0/m = \langle p\rangle/m$——波包的质心以经典速度运动，这是 Ehrenfest 定理（第 03 篇第 7.4 节）对自由粒子的精确兑现；
- $v_p = v_g/2 \neq v_g$——相速度没有直接的物理观测意义（可观测的是包络与概率流），这正是"de Broglie 波不是经典波"的定量表达。色散（$\omega$ 非线性）使不同 $k$ 分量相速度各异，包络必然变形——下一小节的主角。

### 3.3 高斯波包展宽

取第 03 篇自检问题 1 的最小不确定高斯波包作初态，$\psi(x,0) = (2\pi\sigma^2)^{-1/4}e^{-x^2/4\sigma^2}$（$\Delta x(0) = \sigma$、$\Delta p = \hbar/2\sigma$）。其 $k$ 空间分布仍是高斯，每个分量积累相位 $e^{-i\hbar k^2t/2m}$ 后积回坐标空间（高斯积分，留作练习），$|\psi(x,t)|^2$ 仍是以 $x = 0$ 为中心的高斯，但宽度增长：

$$\Delta x(t) = \sigma\sqrt{1 + \left(\frac{\hbar t}{2m\sigma^2}\right)^2}.$$

物理读法：**位置越确定的初态，动量弥散越大，波包散开得越快**——$\Delta x(0) \cdot \Delta p = \hbar/2$ 的账单以展宽的形式到期支付。量级感受：对电子，$\sigma = 1$ Å 的波包在 $\sim 10^{-16}$ s 内宽度翻倍；对 $1\,\mu\text{g}$ 的尘埃，同样 $\sigma$ 下展宽时间远超宇宙年龄。宏观物体不"散架"靠的不是这个公式失效，而是 $\hbar/m$ 太小（以及退相干，第 10 篇的接口）。波包质心严格走匀速直线（3.2 节），展宽只发生在包络宽度上——"自由量子粒子"的经典对应是**质心**的经典化，不是整个波包。

## 4. 一维定态通论

### 4.1 分离变量

$V$ 不含时，设 $\psi(x,t) = \varphi(x)\,T(t)$ 代入含时方程，两边同除 $\varphi T$，左边只含 $t$、右边只含 $x$，必同为常数 $E$：

$$T(t) = e^{-iEt/\hbar}, \qquad \underbrace{-\frac{\hbar^2}{2m}\frac{d^2\varphi}{dx^2} + V(x)\varphi = E\varphi}_{\text{定态薛定谔方程}}.$$

这正是抽象本征问题 $H|\psi\rangle = E|\psi\rangle$ 的坐标表象（第 03 篇第 6.3 节预告过它）。一般解是定态叠加 $\psi(x,t) = \sum_n c_n\varphi_n(x)e^{-iE_nt/\hbar}$——演化算符的谱展开在坐标表象里的样子。于是"解量子力学问题"在一维世界里被压缩成：**解这个二阶常微分方程的边值问题**。

### 4.2 一维束缚态的三条一般性质与宇称

不依赖 $V(x)$ 的具体形状，一维束缚态有四条通用定理（前两条的证明思路见自检问题 2 的旁注，Griffiths 第 2 章有完整证明）：

1. **无简并**：一维束缚态能级永不简并。同一 $E$ 若有两个解 $\varphi_1, \varphi_2$，朗斯基行列式 $W = \varphi_1\varphi_2' - \varphi_1'\varphi_2$ 为常数（方程无一次导数项），在无穷远处两解都衰减故 $W = 0$，迫使 $\varphi_1 \propto \varphi_2$。（对照：三维中心势的 $m$ 简并来自角向自由度，第 06 篇；一维没有"角向"。）
2. **可取实**：$\varphi$ 是实解，因为方程实系数——$\varphi^{*}$ 也是同能解，无简并迫使 $\varphi^{*} \propto \varphi$，适当取相位即实。推论：一维束缚态概率流恒为零（第 2.2 节）。
3. **节点定理**（陈述）：把束缚态按能量排序 $E_1 < E_2 < \cdots$，第 $n$ 个激发态恰有 $n$ 个节点（基态无节点）。直觉：能量越高、波数越大、振荡越快；严格版本是 Sturm–Liouville 理论。数节点是一维问题里最便宜的"量子数速查"——氢原子径向波函数的 $n_r$ 计数（第 06 篇）就是它的三维版本。
4. **宇称**：若 $V(-x) = V(x)$，则 $[H, \Pi] = 0$（$\Pi$ 为宇称算符），定态可取为宇称本征态：偶 $\varphi(-x) = \varphi(x)$ 或奇 $\varphi(-x) = -\varphi(x)$。这是第 03 篇"对易 $\Rightarrow$ 共同本征基"的第一个波动力学实例，也是第 5.2 节把有限深阱解按奇偶分类的许可证。

## 5. 方势阱：边界条件制造能级

### 5.1 无限深方势阱：完整解

$$V(x) = \begin{cases} 0, & 0 < x < a, \\ \infty, & \text{其余}. \end{cases}$$

阱外 $\varphi = 0$，阱内是自由粒子方程 $\varphi'' = -k^2\varphi$、$k = \sqrt{2mE}/\hbar$。边界条件 $\varphi(0) = \varphi(a) = 0$（波函数连续，阱壁无穷迫使阱外为零）给出

$$\varphi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}, \qquad E_n = \frac{n^2\pi^2\hbar^2}{2ma^2}, \qquad n = 1, 2, 3, \dots$$

（完整推导：能级、归一化、正交性，见自检问题 2。）三件事值得盯住：

- **能级是边界条件的产物**：微分方程对任意 $E$ 都有解，是 $\varphi(a) = 0$ 把 $k$ 钉死在 $n\pi/a$ 上——"量子化 = 边值问题"的最简实例，也是第 4.1 节那句话的兑现；
- **$n = 0$ 被排除**：$\varphi \equiv 0$ 不是态（不可归一化），故存在**零点能** $E_1 = \pi^2\hbar^2/2ma^2 > 0$——不确定关系禁止"静止在阱底"（$\Delta p$ 不能为零，否则 $\Delta x$ 发散，粒子不可能关在宽度 $a$ 里）；
- **节点定理的实例**：$\varphi_n$ 在阱内恰有 $n-1$ 个节点。

这组 $\{\varphi_n\}$ 同时是区间 $[0,a]$ 上的完备正交归一基（傅里叶正弦级数的量子力学身份），任意初态的演化都是它的叠加。

### 5.2 有限深方势阱：奇偶分类与图解

更现实的是有限深阱（对称放置以利用宇称，第 4.2 节性质 4）：

$$V(x) = \begin{cases} 0, & \lvert x\rvert < a, \\ V_0 > 0, & \lvert x\rvert > a. \end{cases}$$

束缚态 $0 < E < V_0$。阱内振荡、阱外衰减：

$$\varphi_{\text{内}} = \begin{cases} A\cos kx \\ B\sin kx \end{cases}, \qquad \varphi_{\text{外}} = C e^{-\kappa\lvert x\rvert}, \qquad k = \frac{\sqrt{2mE}}{\hbar},\quad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}.$$

由于 $V$ 偶，解按宇称分类。$\varphi$ 与 $\varphi'$ 在 $x = \pm a$ 连续（$V$ 有限跳跃不破坏导数连续），等价于**对数导数** $\varphi'/\varphi$ 连续（自动消去振幅）：

$$\text{偶宇称：}\ k\tan(ka) = \kappa; \qquad \text{奇宇称：}\ k\cot(ka) = -\kappa.$$

这是关于 $E$ 的**超越方程**，没有闭式解，但图解法给出全部定性结论。令无量纲变量

$$\xi = ka, \qquad \eta = \kappa a, \qquad \xi^2 + \eta^2 = \frac{2mV_0a^2}{\hbar^2} \equiv R^2,$$

偶宇称条件变成 $\eta = \xi\tan\xi$ 与半径 $R$ 的圆求交点（推导与"至少一个束缚态"的证明见自检问题 3）：

- **至少一个束缚态**：无论阱多浅多窄（$R$ 多小），$\xi\tan\xi$ 从原点出发的支总与圆相交一次——一维对称势阱**永远**至少束缚一个态（一般的一维吸引势也如此，这是三维所无的性质：浅三维阱可以没有束缚态）；
- **束缚态数目**：$R$ 每跨过一个 $\pi/2$ 就多一条支路参与相交，数目 $N \approx \lceil 2R/\pi \rceil$——深而宽的阱束缚态多；
- **波函数渗漏**：$\varphi \sim e^{-\kappa|x|}$ 伸进经典禁区（$E < V_0$ 区）——动能算符是二阶导数，波函数不能像经典粒子那样"急停"，只能指数衰减。这条"渗漏"正是下一节隧穿的全部物理。

$V_0 \to \infty$ 时 $\kappa \to \infty$，$\eta \to \infty$，交点趋于 $\xi = n\pi/2$——光滑地回到 5.1 节（注意阱宽定义差了因子 2）。

## 6. 势垒与隧穿：波动力学的招牌预言

### 6.1 $E < V_0$ 的方势垒透射

$$V(x) = \begin{cases} V_0 > 0, & 0 < x < a, \\ 0, & \text{其余}, \end{cases} \qquad E < V_0.$$

经典力学里这个粒子 100% 被弹回。波动力学里，分区写波函数：

$$\varphi = \begin{cases} e^{ikx} + r\,e^{-ikx}, & x < 0, \\ A e^{\kappa x} + B e^{-\kappa x}, & 0 < x < a, \\ t\,e^{ikx}, & x > a, \end{cases} \qquad k = \frac{\sqrt{2mE}}{\hbar},\ \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}.$$

势垒内部是第 5.2 节的"渗漏"区——振幅衰减但不恒零，到达 $x = a$ 时还剩 $\sim e^{-\kappa a}$，衔接条件把这部分振幅放出右侧。四个衔接方程（$\varphi, \varphi'$ 在 $x = 0, a$ 连续）解四个未知数 $r, A, B, t$（完整推导见自检问题 4），透射系数

$$T = \lvert t\rvert^2 = \left[1 + \frac{V_0^2\,\sinh^2(\kappa a)}{4E(V_0 - E)}\right]^{-1} \xrightarrow{\ \kappa a \gg 1\ }\ \frac{16E(V_0 - E)}{V_0^2}\,e^{-2\kappa a}.$$

要点：**$T > 0$——隧穿发生了**，且对垒宽呈指数敏感（$e^{-2\kappa a}$）。这个指数依赖是隧穿全部应用的总开关：$\alpha$ 衰变的 Geiger–Nuttall 定律（寿命对能量指数敏感）、扫描隧穿显微镜（电流对针尖距离指数敏感，成就了原子级成像）、闪存的写入机制。指数因子的形式 $e^{-2\int\kappa\,dx}$ 对缓变势垒的推广就是 WKB 近似（第 07s 篇，[变分法与 WKB](07s-variational-and-wkb.md)）。

一句话补充 **共振透射**：当 $E > V_0$ 时公式里的 $\sinh$ 变 $\sin$，$T = \left[1 + \frac{V_0^2\sin^2(k'a)}{4E(E-V_0)}\right]^{-1}$（$k' = \sqrt{2m(E-V_0)}/\hbar$），在 $k'a = n\pi$ 处 $T = 1$——垒内恰好容纳整数个半波长，前后界面的反射波相消，势垒变"透明"。散射态也可以有结构，不只束缚态才有量子化味道。

### 6.2 $\delta$ 势：可解性最好的玩具

$$V(x) = -\lambda\,\delta(x), \qquad \lambda > 0.$$

$\delta$ 函数的奇异性把衔接条件改成**导数跃变**：把定态方程在 $[-\epsilon, \epsilon]$ 上积分并令 $\epsilon \to 0$，

$$\varphi'(0^+) - \varphi'(0^-) = -\frac{2m\lambda}{\hbar^2}\,\varphi(0).$$

**束缚态**（唯一一个）：$\varphi(x) = \sqrt{\kappa}\,e^{-\kappa\lvert x\rvert}$，跃变条件给出（自检问题 5）

$$\kappa = \frac{m\lambda}{\hbar^2}, \qquad E = -\frac{\hbar^2\kappa^2}{2m} = -\frac{m\lambda^2}{2\hbar^2}.$$

恰好一个束缚态——5.2 节"至少一个"在这里收紧为"恰好一个"。**散射态**（$E > 0$）同样两个衔接方程解出：

$$T = \frac{1}{1 + \dfrac{m\lambda^2}{2\hbar^2 E}}, \qquad R = 1 - T.$$

漂亮的一笔：把 $T$ 看作 $k$ 的解析函数，$t(k) \propto 1/(k - i m\lambda/\hbar^2)$ 在**正虚轴上的极点** $k = im\lambda/\hbar^2$ 恰好对应束缚态能量 $E = \hbar^2k^2/2m = -m\lambda^2/2\hbar^2$——"散射振幅的极点 = 束缚态"这条一般定理的最小实例，第 08 篇（[散射理论](08-scattering-theory.md)）会把它发扬光大。

### 6.3 双阱一句话

两个 $\delta$ 势（或两个方阱）相距 $d$ 组成**双阱**：孤立时各有一个基态 $E_0$，靠近后左右两态经垒下隧穿耦合，能级劈裂成对称/反对称一对 $E_0 \pm \lvert t_{\text{tun}}\rvert$，劈裂大小 $\propto e^{-\kappa d}$——"隧穿使简并解除"。这是化学键（成键/反键轨道）、氨分子反转、以及凝聚态书紧束缚模型的共同原型；劈裂的定量计算是 WKB 方法的标准习题，见第 07s 篇（[变分法与 WKB](07s-variational-and-wkb.md)）。

## 7. 接口：与全书挂接

- **谐振子**：第 04 篇（[谐振子代数解法](04-harmonic-oscillator-ladder.md)）全程不碰微分方程；坐标表象里同一个 $H$ 的本征函数是 Hermite 多项式乘高斯，$\varphi_n(x) \propto H_n(\xi)e^{-\xi^2/2}$（$\xi = \sqrt{m\omega/\hbar}\,x$）——能级 $E_n = \hbar\omega(n+\tfrac12)$ 与 $n$ 个节点的结构同代数解法逐一吻合，是"表象无关性"的又一次实战对账。
- **三维与氢原子**：把本篇的分离变量用到中心势 $V(r)$，角向一次性被球谐函数解掉，径向化为带离心垒的等效一维问题——第 4.2 节的节点定理变成 $n_r$ 计数，"边界条件制造能级"变成级数截断 $n = n_r + l + 1$，全部展开在第 06 篇（[氢原子与电子亚层](06-hydrogen-and-subshells.md)）。
- **散射理论**：本篇的一维散射（$T$、$R$、极点）是第 08 篇三维散射（分波、相移、截面）的预科。
- **变分法与 WKB**：有限深阱的图解方程对一般势无解析解，第 07s 篇（[变分法与 WKB](07s-variational-and-wkb.md)）给出系统近似工具，隧穿指数 $e^{-2\int\kappa dx}$ 在那里成为定理而非拟合。

## 小结

- 坐标表象把公设 4 变成 $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi$；概率守恒的微分形式是 $\partial_t\rho + \nabla\cdot\vec j = 0$，$\vec j = \frac{\hbar}{m}\operatorname{Im}(\psi^{*}\nabla\psi)$，$V$ 在推导中自动消去。
- 自由粒子：色散 $\omega = \hbar k^2/2m$ 决定一切——$v_g = \hbar k/m$ 是包络（质心）速度、$v_p = v_g/2$ 不可直接观测；高斯波包展宽 $\Delta x(t) = \sigma\sqrt{1 + (\hbar t/2m\sigma^2)^2}$，初态越窄散得越快。
- 一维束缚态四性质：无简并、可取实（故零概率流）、第 $n$ 态 $n-1$ 个节点（节点定理）、$V$ 偶则解有宇称。
- 无限深阱：$\varphi_n = \sqrt{2/a}\sin(n\pi x/a)$、$E_n = n^2\pi^2\hbar^2/2ma^2$，有零点能；有限深阱：奇偶分类，偶宇称满足 $\xi\tan\xi = \eta$、$\xi^2 + \eta^2 = 2mV_0a^2/\hbar^2$，至少一个束缚态，波函数渗漏进禁区。
- 隧穿：$T = \left[1 + \frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\right]^{-1} > 0$，宽垒极限 $\propto e^{-2\kappa a}$；$E > V_0$ 有共振透射 $T = 1$；$\delta$ 势唯一束缚态 $E = -m\lambda^2/2\hbar^2$，散射振幅极点即束缚态；双阱劈裂指向 WKB（第 07s 篇）。

## 自检问题

**1.** 由含时薛定谔方程推导概率流连续性方程 $\partial_t\rho + \nabla\cdot\vec j = 0$（$V$ 为实势），并说明 $V$ 为什么在结果中消失。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：$\rho = \psi^{*}\psi$，对时间求导：

$$\frac{\partial\rho}{\partial t} = \psi^{*}\frac{\partial\psi}{\partial t} + \frac{\partial\psi^{*}}{\partial t}\psi.$$

由薛定谔方程 $\partial_t\psi = \frac{i\hbar}{2m}\nabla^2\psi + \frac{1}{i\hbar}V\psi$ 及其复共轭 $\partial_t\psi^{*} = -\frac{i\hbar}{2m}\nabla^2\psi^{*} - \frac{1}{i\hbar}V\psi^{*}$（$V$ 实为关键），代入：

$$\frac{\partial\rho}{\partial t} = \frac{i\hbar}{2m}\left(\psi^{*}\nabla^2\psi - \psi\nabla^2\psi^{*}\right) + \underbrace{\frac{1}{i\hbar}\left(V\psi^{*}\psi - V\psi\psi^{*}\right)}_{=\,0}.$$

势的两项逐字相消——**$V$ 实保证 $H$ 厄米，厄米保证概率守恒**，链条在分量计算里显形。剩下的项用恒等式 $\nabla\cdot(\psi^{*}\nabla\psi) = \lvert\nabla\psi\rvert^2 + \psi^{*}\nabla^2\psi$ 与其共轭相减：

$$\psi^{*}\nabla^2\psi - \psi\nabla^2\psi^{*} = \nabla\cdot\left(\psi^{*}\nabla\psi - \psi\nabla\psi^{*}\right),$$

于是

$$\frac{\partial\rho}{\partial t} = \frac{i\hbar}{2m}\nabla\cdot\left(\psi^{*}\nabla\psi - \psi\nabla\psi^{*}\right) = -\nabla\cdot\vec j, \qquad \vec j = \frac{\hbar}{2mi}\left(\psi^{*}\nabla\psi - \psi\nabla\psi^{*}\right). \qquad \blacksquare$$

**推论**：全空间积分并用散度定理（$\psi$ 在无穷远衰减使面积分为零），$\frac{d}{dt}\int\rho\,d^3r = 0$——第 03 篇"幺正演化保持归一化"的微分形式。若 $V$ 有虚部（光学势，模拟吸收），$V - V^{*} = 2i\operatorname{Im}V$ 不消去，$\partial_t\rho + \nabla\cdot\vec j = \frac{2}{\hbar}\operatorname{Im}V\cdot\rho$，概率有源汇——虚势正是"粒子被吸走"的记账方式。

</details>

**2.** 完整求解无限深方势阱（$V = 0$ 于 $0 < x < a$、$V = \infty$ 于阱外）：推出能级 $E_n$、归一化常数，并验证不同能级波函数的正交性。

<details markdown="1"><summary>点击显示答案</summary>

**能级**：阱外 $\varphi = 0$（无穷势垒迫使波函数为零，否则 $\langle V\rangle$ 发散）；阱内方程 $\varphi'' = -k^2\varphi$、$k = \sqrt{2mE}/\hbar$，通解

$$\varphi(x) = A\sin kx + B\cos kx.$$

波函数处处连续（$V$ 的无穷跳跃只破坏导数，不破坏函数本身——方程两边积分一次可见）。$\varphi(0) = 0 \Rightarrow B = 0$；$\varphi(a) = 0 \Rightarrow \sin ka = 0$，故

$$k_n = \frac{n\pi}{a}, \qquad E_n = \frac{\hbar^2k_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2ma^2}, \qquad n = 1, 2, \dots$$

$n = 0$ 给出 $\varphi \equiv 0$（不是态），$n < 0$ 与正 $n$ 只差相位——零点能 $E_1 > 0$ 是边界条件与不确定关系的联合产物。

**归一化**：

$$1 = \lvert A\rvert^2\int_0^a\sin^2\frac{n\pi x}{a}\,dx = \lvert A\rvert^2\cdot\frac{a}{2} \;\Longrightarrow\; A = \sqrt{\frac{2}{a}}, \qquad \varphi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}.$$

**正交性**（$n \neq m$）：积化和差，

$$\int_0^a\varphi_n\varphi_m\,dx = \frac{2}{a}\cdot\frac{1}{2}\int_0^a\left[\cos\frac{(n-m)\pi x}{a} - \cos\frac{(n+m)\pi x}{a}\right]dx = \frac{1}{a}\left[\frac{a\sin(n-m)\pi}{(n-m)\pi} - \frac{a\sin(n+m)\pi}{(n+m)\pi}\right] = 0.$$

合写 $\langle\varphi_n|\varphi_m\rangle = \delta_{nm}$。这并非巧合：$\varphi_n$ 是厄米算符 $H$ 不同本征值的本征矢，正交性是第 03 篇第 4.1 节那条两行定理的实例。完备性（任意 $\varphi(x)$ 可展开为 $\sum c_n\varphi_n$）即傅里叶正弦级数定理——$\{\varphi_n\}$ 撑起阱内粒子的整个希尔伯特空间。

</details>

**3.** 推导有限深方势阱（$V = 0$ 于 $\lvert x\rvert < a$、$V = V_0$ 于阱外）偶宇称束缚态的条件 $\xi\tan\xi = \eta$（$\xi = ka$、$\eta = \kappa a$、$\xi^2 + \eta^2 = 2mV_0a^2/\hbar^2 \equiv R^2$），并证明：无论 $V_0a^2$ 多小，至少存在一个偶宇称束缚态。

<details markdown="1"><summary>点击显示答案</summary>

**条件推导**：束缚态 $0 < E < V_0$。偶宇称解：

$$\varphi(x) = \begin{cases} A\cos kx, & \lvert x\rvert < a, \\ C\,e^{-\kappa\lvert x\rvert}, & \lvert x\rvert > a, \end{cases} \qquad k = \frac{\sqrt{2mE}}{\hbar},\quad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}.$$

$x = a$ 处 $\varphi$ 与 $\varphi'$ 连续（$V$ 有限跳跃，定态方程积分一次得 $\varphi'$ 连续）：

$$A\cos ka = Ce^{-\kappa a}, \qquad -kA\sin ka = -\kappa Ce^{-\kappa a}.$$

两式相除消去振幅（即对数导数连续）：$k\tan ka = \kappa$。乘以 $a$ 得 $\xi\tan\xi = \eta$；而

$$\xi^2 + \eta^2 = (k^2 + \kappa^2)a^2 = \frac{2mE + 2m(V_0 - E)}{\hbar^2}a^2 = \frac{2mV_0a^2}{\hbar^2} = R^2,$$

$E$ 完全消去——束缚态能量由"曲线 $\eta = \xi\tan\xi$ 与圆 $\xi^2 + \eta^2 = R^2$ 的交点"给出。

**至少一个束缚态**：只需看第一象限（$\xi, \eta > 0$）内区间 $\xi \in (0, \min(\pi/2, R))$。定义

$$g(\xi) = \xi\tan\xi - \sqrt{R^2 - \xi^2}.$$

- 左端：$g(0^+) = 0 - R = -R < 0$（曲线在原点、圆在高度 $R$）；
- 右端：若 $R < \pi/2$，在 $\xi = R$ 处 $\eta = 0$，$g(R) = R\tan R - 0 > 0$；若 $R \ge \pi/2$，$\xi \to (\pi/2)^-$ 时 $\xi\tan\xi \to +\infty$ 而圆上的 $\eta$ 有限，$g \to +\infty$。

$g$ 连续，由介值定理至少一个零点——交点存在，**至少一个偶宇称束缚态，与 $R$ 多小无关**。$\blacksquare$（奇宇称支 $\eta = -\xi\cot\xi$ 从 $\xi = \pi/2$ 才开始，故浅阱的那个态一定是偶宇称的；$R$ 每增加约 $\pi/2$ 多交一条支，束缚态逐一"出生"。）

</details>

**4.** 完整推导 $E < V_0$ 方势垒（$0 < x < a$ 内 $V = V_0$）的透射系数 $T = \left[1 + \frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\right]^{-1}$。

<details markdown="1"><summary>点击显示答案</summary>

**波函数与衔接条件**：如正文 6.1 节，$k = \sqrt{2mE}/\hbar$、$\kappa = \sqrt{2m(V_0-E)}/\hbar$。两组边界条件：

$x = 0$：$\ 1 + r = A + B$，$\ ik(1 - r) = \kappa(A - B)$；

$x = a$：$\ Ae^{\kappa a} + Be^{-\kappa a} = te^{ika}$，$\ \kappa(Ae^{\kappa a} - Be^{-\kappa a}) = ikte^{ika}$。

**先解 $A, B$（用 $t$ 表示）**：由 $x = a$ 两式加减，

$$A = \frac{t}{2}\left(1 + \frac{ik}{\kappa}\right)e^{ika - \kappa a}, \qquad B = \frac{t}{2}\left(1 - \frac{ik}{\kappa}\right)e^{ika + \kappa a}.$$

**代回 $x = 0$**：第一式乘 $ik$ 后与第二式相加消去 $r$：$2ik = (\kappa + ik)A - (\kappa - ik)B$。代入 $A, B$ 并注意 $(\kappa \pm ik)(1 \pm ik/\kappa) = (\kappa \pm ik)^2/\kappa$：

$$2ik = \frac{t\,e^{ika}}{2\kappa}\left[(\kappa + ik)^2 e^{-\kappa a} - (\kappa - ik)^2 e^{\kappa a}\right].$$

展开 $(\kappa \pm ik)^2 = (\kappa^2 - k^2) \pm 2ik\kappa$，方括号内按 $e^{\pm\kappa a} = \cosh\kappa a \pm \sinh\kappa a$ 归并：

$$(\kappa + ik)^2 e^{-\kappa a} - (\kappa - ik)^2 e^{\kappa a} = -2(\kappa^2 - k^2)\sinh\kappa a + 4ik\kappa\cosh\kappa a,$$

$$2ik = t\,e^{ika}\left[2ik\cosh\kappa a - \frac{\kappa^2 - k^2}{\kappa}\sinh\kappa a\right] \;\Longrightarrow\; t = \frac{e^{-ika}}{\cosh\kappa a + i\,\dfrac{\kappa^2 - k^2}{2k\kappa}\sinh\kappa a}.$$

**取模方**：$\lvert\cosh + i\alpha\sinh\rvert^2 = \cosh^2 + \alpha^2\sinh^2 = 1 + (1 + \alpha^2)\sinh^2$，而

$$1 + \alpha^2 = 1 + \frac{(\kappa^2 - k^2)^2}{4k^2\kappa^2} = \frac{(k^2 + \kappa^2)^2}{4k^2\kappa^2},$$

代入 $k^2 + \kappa^2 = 2mV_0/\hbar^2$、$k^2\kappa^2 = 4m^2E(V_0 - E)/\hbar^4$：

$$T = \lvert t\rvert^2 = \left[1 + \frac{(k^2+\kappa^2)^2}{4k^2\kappa^2}\sinh^2\kappa a\right]^{-1} = \left[1 + \frac{V_0^2\sinh^2(\kappa a)}{4E(V_0 - E)}\right]^{-1}. \qquad \blacksquare$$

**极限自查**：$a \to 0$ 时 $T \to 1$（垒消失）✓；$\kappa a \gg 1$ 时 $\sinh \approx e^{\kappa a}/2$，$T \approx \frac{16E(V_0-E)}{V_0^2}e^{-2\kappa a}$——指数因子是主角；$E \to V_0$ 时 $\kappa \to 0$、$\sinh\kappa a \to \kappa a$，$T \to [1 + mV_0a^2/2\hbar^2]^{-1}$，连续过渡 ✓。

</details>

**5.** 对吸引 $\delta$ 势 $V(x) = -\lambda\delta(x)$（$\lambda > 0$）：推导导数跃变条件，求出唯一束缚态的能量 $E = -m\lambda^2/2\hbar^2$ 与归一化波函数。

<details markdown="1"><summary>点击显示答案</summary>

**跃变条件**：定态方程

$$-\frac{\hbar^2}{2m}\varphi'' - \lambda\delta(x)\varphi = E\varphi$$

在 $[-\epsilon, \epsilon]$ 上积分，令 $\epsilon \to 0$（$\varphi$ 连续故 $\int E\varphi\,dx \to 0$）：

$$-\frac{\hbar^2}{2m}\left[\varphi'(\epsilon) - \varphi'(-\epsilon)\right] - \lambda\varphi(0) = 0 \;\Longrightarrow\; \boxed{\varphi'(0^+) - \varphi'(0^-) = -\frac{2m\lambda}{\hbar^2}\varphi(0)}.$$

$\delta$ 奇异性使导数有限跳变，波函数本身仍连续。

**束缚态**：$x \neq 0$ 处是自由方程，$E < 0$ 时衰减解 $\varphi = Ae^{-\kappa\lvert x\rvert}$（$\kappa = \sqrt{-2mE}/\hbar$，已满足连续性）。导数：$\varphi'(0^+) = -\kappa A$、$\varphi'(0^-) = +\kappa A$，跃变 $= -2\kappa A$。代入跃变条件：

$$-2\kappa A = -\frac{2m\lambda}{\hbar^2}A \;\Longrightarrow\; \kappa = \frac{m\lambda}{\hbar^2}, \qquad E = -\frac{\hbar^2\kappa^2}{2m} = -\frac{m\lambda^2}{2\hbar^2}. \qquad \blacksquare$$

$\kappa$ 被唯一确定——**恰好一个**束缚态（对照自检问题 3：一维吸引势"至少一个"，$\delta$ 势收紧为"恰好一个"）。

**归一化**：

$$1 = \lvert A\rvert^2\int_{-\infty}^{\infty}e^{-2\kappa\lvert x\rvert}dx = \lvert A\rvert^2\cdot\frac{1}{\kappa} \;\Longrightarrow\; \varphi(x) = \sqrt{\kappa}\,e^{-\kappa\lvert x\rvert}.$$

**特征尺度**：$1/\kappa = \hbar^2/m\lambda$——吸引越强束缚越紧、波函数越局域。与氢原子基态（第 06 篇）对照：$a_0 = \hbar^2/m_e(e^2/4\pi\varepsilon_0)$ 与 $1/\kappa$ 同构，库仑吸引的"$e^2/4\pi\varepsilon_0$"就是三维版的 $\lambda$。

</details>

## 参考

- Griffiths《量子力学概论》第 1 章（波函数：概率诠释、归一化、概率流）与第 2 章（定态、无限深/有限深阱、$\delta$ 势、自由粒子波包）——本篇第 2–6 节的主线出处。
- Shankar《Principles of Quantum Mechanics》第 5 章（一维问题）：一维定态一般性质（无简并、节点）的干净证明与方势问题的系统处理。
- Sakurai《Modern Quantum Mechanics》第 2 章与附录 B（波动力学）：作为公理化叙述之后"落到波函数"的对照读物，与本篇的定位完全一致。
- 朗道《量子力学（非相对论理论）》§§17–25（一维运动、势阱、势垒透射、准经典性）：更凝练的同题材处理，WKB 接口（§§48–53）为第 07s 篇预热。
