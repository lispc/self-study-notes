# QED：旋量场、光子场与规范不变性——从拉氏量到散射截面

> 路线图位置：第 4 阶段（QFT 核心）· 第 5 篇
> 前置知识：Dirac 方程与旋量（[第 3 阶段：Klein–Gordon 与 Dirac 方程](../stage-03-relativistic-qm/01-klein-gordon-and-dirac.md)）、标量场量子化、S 矩阵与费曼图微扰论（前面几篇笔记）。
> 学习目标：理解定域 U(1) 规范对称性如何唯一地逼出 QED 拉氏量；会用费曼规则、Casimir 技巧和求迹公式完整算出 $e^+e^-\to\mu^+\mu^-$ 与康普顿散射的树图截面。

---

## 1. 一句话总结

**要求 Dirac 旋量场的相位变换 $\psi\to e^{i\alpha(x)}\psi$（定域 U(1)）成为拉氏量的对称性，就必须引入一个以特定方式同步变换的矢量场 $A_\mu$ 来"修补"动能项——这个场就是光子；由此得到的拉氏量 $\mathcal L=\bar\psi(i\gamma^\mu D_\mu-m)\psi-\frac14F_{\mu\nu}F^{\mu\nu}$ 就是量子电动力学（QED），它的树图预言（如 $d\sigma/d\Omega=\frac{\alpha^2}{4s}(1+\cos^2\theta)$ 和 Klein–Nishina 公式）与实验精确符合。**

下面把这句话逐层拆开。全文采用自然单位 $\hbar=c=1$，度规号差 $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$。

## 2. 规范原理：从整体 U(1) 到定域 U(1)

### 2.1 整体 U(1) 与守恒流

自由 Dirac 拉氏量

$$\mathcal L_{\text{Dirac}} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$$

在**整体**相位变换

$$\psi(x)\;\longrightarrow\; e^{i\alpha}\psi(x), \qquad \bar\psi(x)\;\longrightarrow\; e^{-i\alpha}\bar\psi(x) \qquad (\alpha\ \text{为常数})$$

下不变：质量项里两个相位直接抵消，动能项里 $\partial_\mu$ 作用在常数相位上不产生新项。这是群 U(1)（所有模为 1 的复数，即一个圆）的整体作用。由 Noether 定理，它对应守恒流与守恒荷

$$j^\mu = \bar\psi\gamma^\mu\psi, \qquad \partial_\mu j^\mu = 0, \qquad Q = \int d^3x\; \psi^\dagger\psi = \text{常数},$$

物理上这就是**电荷守恒**。

### 2.2 定域化：动能项出问题了

现在提出一个更强的要求：让相位 $\alpha$ 依赖于时空点，

$$\psi(x)\;\longrightarrow\; e^{i\alpha(x)}\psi(x).$$

物理动机很直白：既然整体相位不可观测，那么在芝加哥和月球上"独立地"重定相位基准，物理也不该变——相位基准应该是定域的自由度。质量项 $\bar\psi\psi$ 依然不变，但动能项出事了：

$$\bar\psi\,\partial_\mu\psi \;\longrightarrow\; \bar\psi\,\partial_\mu\psi + i\,(\partial_\mu\alpha)\,\bar\psi\psi.$$

多出来的 $i(\partial_\mu\alpha)\bar\psi\psi$ 一项消不掉——**普通导数与定域相位变换不对易**。

### 2.3 协变导数：引入 $A_\mu$ 来补偿

补救办法是修改导数的定义。引入一个新的矢量场 $A_\mu(x)$，定义**协变导数**

$$D_\mu = \partial_\mu + ieA_\mu,$$

并要求 $A_\mu$ 在相位变换下同步改变：

$$A_\mu(x)\;\longrightarrow\; A_\mu(x) - \frac{1}{e}\,\partial_\mu\alpha(x).$$

验证（一行代数，值得亲手做一遍）：

$$D_\mu\psi \;\longrightarrow\; \big(\partial_\mu + ieA_\mu - i\,\partial_\mu\alpha\big)\big(e^{i\alpha}\psi\big) = e^{i\alpha}\big(\partial_\mu + ieA_\mu\big)\psi = e^{i\alpha}\,D_\mu\psi.$$

关键之处：$D_\mu\psi$ 与 $\psi$ **以完全相同的相位变换**，多出来的 $\partial_\mu\alpha$ 被 $A_\mu$ 的变换律精确吃掉。于是把拉氏量里所有 $\partial_\mu$ 换成 $D_\mu$（这叫**最小耦合**），$\bar\psi i\gamma^\mu D_\mu\psi$ 就在定域 U(1) 下不变了。

**这就是"规范对称性强迫光子存在"的准确含义**：定域相位不变性不是一个可以随便添加的装饰，它逻辑上要求存在一个与费米子以 $-ie\bar\psi\gamma^\mu\psi A_\mu$ 形式耦合的矢量场。$A_\mu$ 就是电磁四势，耦合常数 $e$ 就是基本电荷。注意这套构造并没有"推导"出电磁学的全部——比如 $e$ 的数值、为什么 $\alpha(x)$ 只依赖一个函数而不是多个，都是 U(1) 这个群选择的输入。

### 2.4 场强张量：$A_\mu$ 自己的动能项

$A_\mu$ 要成为动力学场，还需要它自己的动能项，且必须规范不变。观察协变导数的对易子：

$$[D_\mu, D_\nu] = ie\big(\partial_\mu A_\nu - \partial_\nu A_\mu\big) \equiv ie\,F_{\mu\nu}.$$

由于 $D_\mu$ 作用在"带相位"的对象上仍是协变的，对易子里所有 $\partial\alpha$ 项必然抵消——可以直接验证 $F_{\mu\nu}\to F_{\mu\nu}$ 在 $A_\mu\to A_\mu-\partial_\mu\alpha/e$ 下不变（$\partial_\mu\partial_\nu\alpha$ 对称相消）。$F_{\mu\nu}$ 就是电磁场强张量：$F^{0i}=-E^i$，$F^{ij}=-\epsilon^{ijk}B^k$。最简的规范不变、Lorentz 不变、可重整的动能项是

$$\mathcal L_{\text{photon}} = -\frac14 F_{\mu\nu}F^{\mu\nu} = \frac12\big(\vec E^2 - \vec B^2\big),$$

这正是 Maxwell 理论的拉氏量。

<details markdown="1"><summary>补充说明：规范对称性其实不是"对称性"</summary>

定域 U(1) 严格说不是物理对称性，而是**描述冗余**：$A_\mu$ 与 $A_\mu-\partial_\mu\alpha$ 描述同一个物理态，正如量子力学里 $|\psi\rangle$ 与 $e^{i\alpha}|\psi\rangle$ 是同一射线。它的后果之一是光子只有 **2 个**物理极化（横向），尽管 $A_\mu$ 有 4 个分量——规范变换加 Lorentz 条件恰好削掉两个非物理自由度。这也是量子化规范场时为什么必须"固定规范"（Faddeev–Popov 程序，见后续 Yang–Mills 理论笔记）。把它叫作"对称性"是历史沿用；它的深层地位在几何语言里最清楚：$A_\mu$ 是 U(1) 主丛上的**联络**，$D_\mu$ 是联络决定的协变导数，$F_{\mu\nu}$ 是曲率。

</details>

## 3. QED 拉氏量逐项解读

把上面的零件组装起来：

$$\boxed{\;\mathcal L_{\text{QED}} = \bar\psi\big(i\gamma^\mu D_\mu - m\big)\psi - \frac14 F_{\mu\nu}F^{\mu\nu}\;}$$

逐项看：

- $\bar\psi(i\gamma^\mu\partial_\mu - m)\psi$：自由电子（及其反粒子正电子）的动能与质量项。质量项规范不变，因为 $\bar\psi$ 与 $\psi$ 的相位抵消——**费米子可以有质量**。
- $-e\,\bar\psi\gamma^\mu\psi\, A_\mu = -e\,j^\mu A_\mu$：$D_\mu$ 展开后自动带出的相互作用项。它把守恒流 $j^\mu$ 耦合到电磁场上，是 QED 全部相互作用的来源（一个顶点，两条费米子线一条光子线）。
- $-\frac14F_{\mu\nu}F^{\mu\nu}$：光子的动能项，含 $\vec E,\vec B$。

**光子为什么无质量**：给 $A_\mu$ 加质量项 $\frac12 m_\gamma^2 A_\mu A^\mu$（Proca 项），在规范变换下

$$A_\mu A^\mu \;\longrightarrow\; A_\mu A^\mu - \frac{2}{e}A^\mu\partial_\mu\alpha + \frac{1}{e^2}(\partial_\mu\alpha)(\partial^\mu\alpha) \;\neq\; A_\mu A^\mu,$$

规范不变性被破坏。反过来，既然定域 U(1) 是整个构造的出发点，$m_\gamma^2A_\mu A^\mu$ 就被禁止——**规范不变性强制光子严格无质量**。这与实验上限 $m_\gamma \lesssim 10^{-18}\,\mathrm{eV}$ 一致（若光子有质量，Coulomb 定律会变成 Yukawa 型，行星磁场观测可以给出极严的限制）。

最后提一句量纲：$[\psi]=3/2$，$[A_\mu]=1$，故 $[e]=0$——$e$ 无量纲，相互作用可重整。无量纲耦合写成

$$\alpha = \frac{e^2}{4\pi} \approx \frac{1}{137},$$

精细结构常数 $\alpha\ll 1$ 正是 QED 微扰论好用到变态的根本原因。

## 4. QED 费曼规则（速查）

由上面的拉氏量经正则量子化 + Wick 定理可推出以下规则（推导见前面的微扰论笔记，这里直接取用）。约定所有动量沿线流向取定。

| 对象 | 规则 |
| --- | --- |
| 费米子传播子（$\psi$ 内线，动量 $p$） | $\dfrac{i(\slashed p + m)}{p^2 - m^2 + i\epsilon}$ |
| 光子传播子（$A_\mu$ 内线，动量 $k$，Feynman 规范 $\xi=1$） | $\dfrac{-i\eta_{\mu\nu}}{k^2 + i\epsilon}$ |
| 顶点（$\bar\psi\gamma^\mu\psi A_\mu$） | $-ie\gamma^\mu$ |
| 入射费米子 $e^-(p,s)$ | $u^s(p)$ |
| 出射费米子 | $\bar u^s(p)$ |
| 入射反费米子 $e^+(p,s)$ | $\bar v^s(p)$ |
| 出射反费米子 | $v^s(p)$ |
| 入射光子（极化 $\lambda$） | $\varepsilon_\mu^{(\lambda)}(k)$ |
| 出射光子 | $\varepsilon_\mu^{*(\lambda)}(k)$ |

使用要点：

- 沿每条费米子线**逆着费米子数流的方向**从右往左把因子排成矩阵乘积；
- 每个顶点处四动量守恒，内线动量 $p$ 积分 $\int d^4p/(2\pi)^4$（圈动量）；
- 闭合费米子圈多一个因子 $(-1)$ 并对旋量指标取迹；
- 旋量和约定 $\sum_s u^s(p)\bar u^s(p) = \slashed p + m$，$\sum_s v^s(p)\bar v^s(p) = \slashed p - m$（下节全靠它们）。

## 5. $e^+e^-\to\mu^+\mu^-$：树图截面的完整计算

这是本章的核心演算，也是历史上 QFT 与实验精确对上的第一批过程之一。设初态 $e^-(p_1)e^+(p_2)\to\mu^-(p_3)\mu^+(p_4)$，在质心系中计算，并忽略 $m_e$ 与 $m_\mu$（对 $\sqrt s \gg m_\mu$ 的对撞机能量是好近似；保留 $m_\mu$ 的结果只差平庸的运动学因子）。

### 5.1 振幅

树图只有一张：$s$ 道虚光子交换。按费曼规则（电子线逆着费米子流读，$\mu$ 子线同理）：

$$i\mathcal M = \bar u(p_3)\big({-}ie\gamma^\mu\big)v(p_4)\;\frac{-i\eta_{\mu\nu}}{s}\;\bar v(p_2)\big({-}ie\gamma^\nu\big)u(p_1),$$

其中 $s = (p_1+p_2)^2$。整理得

$$\boxed{\;\mathcal M = \frac{e^2}{s}\,\big[\bar u(p_3)\gamma^\mu v(p_4)\big]\,\big[\bar v(p_2)\gamma_\mu u(p_1)\big]\;}$$

注意结构：两个"流"（$\mu$ 子流与电子流）由光子的 $\eta_{\mu\nu}$ 收缩——这正是经典物理里"电流与电流相互作用"的量子版本。

### 5.2 Casimir 技巧与求迹

实验上初态电子/正电子通常不极化，探测器也不测末态自旋，所以要算**非极化平均**

$$\frac14\sum_{\text{spins}}|\mathcal M|^2 = \frac14\,\frac{e^4}{s^2}\sum_{\text{spins}}\big[\bar u(p_3)\gamma^\mu v(p_4)\big]\big[\bar v(p_2)\gamma_\mu u(p_1)\big]\big[\bar u(p_3)\gamma^\nu v(p_4)\big]^*\big[\bar v(p_2)\gamma_\nu u(p_1)\big]^*.$$

（因子 $1/4$：初态两个费米子各 2 个自旋态，平均各贡献 $1/2$；末态是求和不是平均。）

**共轭规则**：利用 $(\gamma^\mu)^\dagger = \gamma^0\gamma^\mu\gamma^0$，

$$\big[\bar u\gamma^\mu v\big]^* = \big[\bar u\gamma^\mu v\big]^\dagger = v^\dagger(\gamma^\mu)^\dagger\gamma^0 u = v^\dagger\gamma^0\gamma^\mu u = \bar v\gamma^\mu u.$$

于是每个流的模方变成旋量双线性乘积，用完备性 $\sum_s u^s\bar u^s = \slashed p + m$、$\sum_s v^s\bar v^s = \slashed p - m$ 把自旋求和化为**求迹**（这就是 Casimir 技巧）：

$$\sum_{\text{spins}}\big[\bar u(p_3)\gamma^\mu v(p_4)\big]\big[\bar v(p_4)\gamma^\nu u(p_3)\big] = \mathrm{tr}\big[\slashed p_3\gamma^\mu\slashed p_4\gamma^\nu\big],$$

$$\sum_{\text{spins}}\big[\bar v(p_2)\gamma_\mu u(p_1)\big]\big[\bar u(p_1)\gamma_\nu v(p_2)\big] = \mathrm{tr}\big[\slashed p_2\gamma_\mu\slashed p_1\gamma_\nu\big],$$

其中已忽略质量（$m_\mu=m_e=0$）。两条费米子线完全解耦成两个独立的迹，只剩 Lorentz 指标互相收缩。

**求迹公式**（来自 $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$，证明见自检问题 2）：

$$\mathrm{tr}\big(\gamma^\mu\gamma^\nu\big) = 4\eta^{\mu\nu},$$

$$\mathrm{tr}\big(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\big) = 4\big(\eta^{\mu\nu}\eta^{\rho\sigma} - \eta^{\mu\rho}\eta^{\nu\sigma} + \eta^{\mu\sigma}\eta^{\nu\rho}\big).$$

（奇数个 $\gamma$ 矩阵的迹为零。）代入：

$$\mathrm{tr}\big[\slashed p_3\gamma^\mu\slashed p_4\gamma^\nu\big] = 4\big(p_3^\mu p_4^\nu + p_3^\nu p_4^\mu - \eta^{\mu\nu}\,p_3\!\cdot\! p_4\big),$$

电子线同理。两个张量收缩时，含 $\eta^{\mu\nu}$ 的项全部相消（可直接验证），剩下

$$\mathrm{tr}_\mu \cdot \mathrm{tr}_e = 16\times 2\,\big[(p_1\!\cdot\! p_3)(p_2\!\cdot\! p_4) + (p_1\!\cdot\! p_4)(p_2\!\cdot\! p_3)\big] = 32\big[(p_1\!\cdot\! p_3)(p_2\!\cdot\! p_4) + (p_1\!\cdot\! p_4)(p_2\!\cdot\! p_3)\big].$$

用无质量运动学 $t=(p_1-p_3)^2=-2p_1\!\cdot\! p_3=-2p_2\!\cdot\! p_4$，$u=(p_1-p_4)^2=-2p_1\!\cdot\! p_4$，上式 $=8(t^2+u^2)$。因此

$$\frac14\sum_{\text{spins}}|\mathcal M|^2 = \frac{e^4}{4s^2}\times 8(t^2+u^2) = \frac{2e^4(t^2+u^2)}{s^2}.$$

### 5.3 质心系运动学与截面

质心系中 $\sqrt s = 2E$，$|\vec p| = E$。取 $\vec p_1$ 沿 $z$ 轴，$\mu^-$ 出射角为 $\theta$：

$$t = -\frac{s}{2}(1-\cos\theta), \qquad u = -\frac{s}{2}(1+\cos\theta), \qquad t^2 + u^2 = \frac{s^2}{2}\big(1+\cos^2\theta\big).$$

代入得到一个干净的最终结果：

$$\frac14\sum_{\text{spins}}|\mathcal M|^2 = e^4\big(1+\cos^2\theta\big).$$

$2\to2$ 无质量末态的微分截面公式为

$$\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2 s}\,\overline{|\mathcal M|^2},$$

所以

$$\boxed{\;\frac{d\sigma}{d\Omega}\Big(e^+e^-\to\mu^+\mu^-\Big) = \frac{\alpha^2}{4s}\big(1+\cos^2\theta\big)\;}$$

总截面（用 $\int d\Omega\,(1+\cos^2\theta) = 2\pi\int_{-1}^{1}(1+x^2)\,dx = 16\pi/3$）：

$$\boxed{\;\sigma_{\text{tot}} = \frac{4\pi\alpha^2}{3s}\;}$$

### 5.4 物理讨论

- **$1/s$ 行为**：截面随质心能量平方反比下降。量纲上必然如此（$s$ 道虚光子交换无量纲耦合，$[\sigma]=-2$ 只能由 $1/s$ 提供），物理上则反映 $s$ 道虚光子传播子 $1/s$ 的压制。这是点粒子相互作用的标志——若有内部结构（形状因子），高能下会偏离。
- **$1+\cos^2\theta$ 角分布**：这是"自旋 1 虚光子 + 自旋 1/2 费米子"的标志性形状，已由 PEP、PETRA、LEP 等 $e^+e^-$ 对撞机在极宽能区反复验证（电弱修正在高能可测，见后续笔记）。
- **$R$ 值**：把 $\mu^+$ 换成夸克对，同样的公式给出 $\sigma(e^+e^-\to q\bar q) = 3\sum_q Q_q^2\cdot\frac{4\pi\alpha^2}{3s}$（因子 3 来自色）。比值

$$R \equiv \frac{\sigma(e^+e^-\to\text{强子})}{\sigma(e^+e^-\to\mu^+\mu^-)} = 3\sum_q Q_q^2$$

在 $2m_\mu < \sqrt s$ 且低于新味道阈值的区间是常数阶梯：$u,d,s$ 区间 $R = 3\times(4/9+1/9+1/9)=2$；跨过粲夸克阈值后 $R=10/3$。实验上看到的阶梯与平台值直接证实了**夸克带分数电荷且有三色**——这是 QFT 与实验对上的第一个里程碑式的胜利之一。
- 数值感受：$\sqrt s = 10\,\mathrm{GeV}$ 时 $\sigma_{\text{tot}} \approx 4\pi\alpha^2/(3s) \approx 0.87\,\mathrm{nb}$（用 $1\,\mathrm{GeV}^{-2}=0.389\,\mathrm{mb}$ 换算）。

## 6. 康普顿散射：$\gamma e^-\to\gamma e^-$

第二个经典过程。运动学：入射光子 $k$、靶电子 $p$；出射光子 $k'$、电子 $p'$。定义 Mandelstam 变量 $s=(p+k)^2$，$u=(p-k')^2$，$t=(k-k')^2$，满足 $s+t+u=2m^2$。

### 6.1 两张树图与振幅

树图有**两张**图，缺一不可：

- **$s$ 道**：电子先吸收入射光子，中间电子动量 $p+k$，再发射出射光子；
- **$u$ 道**：电子先发射出射光子，中间电子动量 $p-k'$，再吸收入射光子。

两张图由**交叉对称**联系：交换 $k \leftrightarrow -k'$（同时 $\varepsilon\leftrightarrow\varepsilon^*$、$\mu\leftrightarrow\nu$）。按费曼规则写出：

$$i\mathcal M = -ie^2\,\varepsilon_\mu^*(k')\,\varepsilon_\nu(k)\;\bar u(p')\left[\gamma^\mu\frac{\slashed p + \slashed k + m}{s - m^2}\gamma^\nu + \gamma^\nu\frac{\slashed p - \slashed k' + m}{u - m^2}\gamma^\mu\right]u(p).$$

注意分母：$(p+k)^2 - m^2 = s - m^2$，$(p-k')^2 - m^2 = u - m^2$（$i\epsilon$ 此处不会碰到极点，省略）。

### 6.2 Ward 恒等式：规范不变性的试金石

规范不变性在振幅层面的表现是 **Ward 恒等式**：把任何一个外光子的极化矢量替换成其动量，振幅必须为零，

$$k_\nu\,\mathcal M^\nu = 0 \qquad \big(\mathcal M \equiv \varepsilon_\nu(k)\mathcal M^\nu\big).$$

物理原因：$\varepsilon_\mu \to \varepsilon_\mu + c\,k_\mu$ 正是坐标空间规范变换 $A_\mu\to A_\mu-\partial_\mu\alpha/e$ 的动量空间版本；物理振幅不能在规范变换下改变。

验证的代数骨架（建议亲手做一遍，是理解 Ward 恒等式最好的练习）。把 $\varepsilon_\nu(k)\to k_\nu$，即在两项中分别把右边的 $\gamma^\nu$ 换成 $\slashed k$：

- **$s$ 道项**：利用 $\slashed k = (\slashed p + \slashed k - m) - (\slashed p - m)$。前一半使

$$\gamma^\mu(\slashed p+\slashed k+m)\slashed k \;\supset\; \gamma^\mu(\slashed p+\slashed k+m)(\slashed p+\slashed k-m) = \gamma^\mu\big[(p+k)^2 - m^2\big] = \gamma^\mu(s-m^2),$$

恰好消掉传播子分母，贡献 $\gamma^\mu u(p)$；后一半含 $(\slashed p - m)u(p)=0$（Dirac 方程），为零。
- **$u$ 道项**：$\slashed k$ 现在在最左边，用 $\slashed k = (\slashed p' - m) - (\slashed p - \slashed k' - m)$。前一半被 $\bar u(p')(\slashed p'-m)=0$ 杀死；后一半使 $(\slashed p-\slashed k'-m)(\slashed p-\slashed k'+m) = u - m^2$ 消掉分母，贡献 $-\bar u(p')\gamma^\mu u(p)$。

两项符号相反，精确抵消：$k_\nu\mathcal M^\nu \propto \bar u(p')\gamma^\mu u(p) - \bar u(p')\gamma^\mu u(p) = 0$。**注意是两张图之和为零，单独每张图都不为零**——这就是为什么树图必须两张都算，少一张就破坏规范不变性。

<details markdown="1"><summary>补充说明：Ward 恒等式的实用价值</summary>

计算极化求和时要用 $\sum_\lambda \varepsilon_\mu^{*(\lambda)}\varepsilon_\nu^{(\lambda)}$，规范固定后这个求和含有非物理极化。Ward 恒等式保证：在 QED 的树图和任意圈中，可以把该求和直接替换成 $-\eta_{\mu\nu}$，非物理极化的贡献自动为零。这将大量简化康普顿截面的求迹计算。Ward 恒等式是更一般的 Ward–Takahashi 恒等式（格林函数层面）在外线振幅上的特例，它保证了 QED 的可重整性中电荷普适性等深刻性质——更系统的讨论见后续重整化笔记。

</details>

### 6.3 截面：Klein–Nishina 公式（推导骨架）

取**实验室系**：靶电子静止，$p=(m,\vec 0)$，入射光子能量 $\omega$，出射光子能量 $\omega'$、散射角 $\theta$。

**运动学先定 $\omega'$**：由能动量守恒（$p+k-k'=p'$，两边平方，$p'^2=m^2$）得

$$\frac{\omega'}{\omega} = \frac{1}{1 + \dfrac{\omega}{m}(1-\cos\theta)}.$$

这就是康普顿波长移动的相对论形式：光子把一部分能量交给反冲电子，$\omega'<\omega$。

**非极化振幅平方**：对初态电子自旋与光子极化平均（各 $1/2$，共 $1/4$），对末态求和。用 Casimir 技巧后，

$$\frac14\sum|\mathcal M|^2 = \frac{e^4}{4}\,\mathrm{tr}\Big[(\slashed p' + m)\Big(\frac{\Gamma^\mu}{s-m^2} + \frac{\widetilde\Gamma^\mu}{u-m^2}\Big)(\slashed p + m)\Big(\cdots\Big)\Big]$$

这类表达式，每个图自身给出含 4 个 $\gamma$ 矩阵的迹（两次），**交叉项**（$s$ 道振幅与 $u$ 道振幅的干涉）给出含 **6 个** $\gamma$ 矩阵的迹。展开步骤骨架：

1. 用求迹公式把 4 个、6 个 $\gamma$ 的迹全部化为度规缩并（6 $\gamma$ 迹有 15 项，耐心活；也可先利用实验室系关系把 $\slashed p$ 项化简）；
2. 用实验室系不变量 $p\cdot k = m\omega$，$p\cdot k' = m\omega'$，$k\cdot k' = \omega\omega'(1-\cos\theta)$，$s-m^2=2m\omega$，$u-m^2=-2m\omega'$ 代入；
3. $s$ 道、$u$ 道的自平方分别正比于 $(s-m^2)^{-2}$ 与 $(u-m^2)^{-2}$ 的项，交叉项正比于 $(s-m^2)^{-1}(u-m^2)^{-1}$——**正是这个交叉项产生了最终结果里"负的 $\sin^2\theta$ 修正"**；少算交叉项会得到错误的角分布。全部化简后的中间结果是

$$\frac14\sum\big|\mathcal M\big|^2 = 2e^4\left[\frac{\omega}{\omega'} + \frac{\omega'}{\omega} - \sin^2\theta\right];$$

4. 实验室系两体相空间（靶静止，$\omega'$ 由角度唯一确定）经 $\delta$ 函数积掉反冲电子动量与 $\omega'$ 后给出

$$\frac{d\sigma}{d\cos\theta} = \frac{1}{4m\omega}\cdot\frac{2\pi\,\omega'^2}{16\pi^2 m\omega}\;\frac14\sum|\mathcal M|^2 = \frac{\omega'^2}{32\pi m^2\omega^2}\;\frac14\sum|\mathcal M|^2.$$

代入并用 $e^2 = 4\pi\alpha$ 化简（完整代数见 Peskin §5.5，是出名的"值得做一遍"的计算），得到 **Klein–Nishina 公式**：

$$\boxed{\;\frac{d\sigma}{d\cos\theta} = \frac{\pi\alpha^2}{m^2}\left(\frac{\omega'}{\omega}\right)^{\!2}\left[\frac{\omega'}{\omega} + \frac{\omega}{\omega'} - \sin^2\theta\right]\;}$$

高能下 $\omega'\ll\omega$，方括号中 $\omega/\omega'$ 项主导，前向峰显著增强——物理上是软光子发射的增强。

### 6.4 Thomson 极限

低能极限 $\omega \ll m$ 时 $\omega'\to\omega$，方括号变成 $2-\sin^2\theta = 1+\cos^2\theta$，于是

$$\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{2m^2}\big(1+\cos^2\theta\big), \qquad \sigma_{\text{Thomson}} = \frac{8\pi\alpha^2}{3m^2} = \frac{8\pi}{3}r_e^2,$$

其中 $r_e = \alpha/m \approx 2.82\times10^{-15}\,\mathrm{m}$ 是**经典电子半径**，$\sigma_{\text{Thomson}}\approx 6.65\times10^{-29}\,\mathrm{m^2}$。注意角分布 $1+\cos^2\theta$ 与 $e^+e^-\to\mu^+\mu^-$ 相同——这不是巧合，低能光子的偶极辐射图样与虚光子交换的角动量结构一致。经典电动力学里 Thomson 截面要靠"辐射阻尼"等别扭的半经典论证得到，而在 QED 里它只是 Klein–Nishina 公式的一行极限。

## 7. 小结

| 内容 | 要点 |
| --- | --- |
| 规范原理 | 定域 U(1)：$\partial_\mu\to D_\mu=\partial_\mu+ieA_\mu$，$A_\mu\to A_\mu-\partial_\mu\alpha/e$；光子被强迫引入 |
| 拉氏量 | $\bar\psi(i\slashed D-m)\psi-\frac14F^2$；$F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ 规范不变；$A_\mu A^\mu$ 破坏规范不变性 ⟹ 光子无质量 |
| 费曼规则 | 顶点 $-ie\gamma^\mu$；传播子 $i(\slashed p+m)/(p^2-m^2)$、$-i\eta_{\mu\nu}/k^2$；外线 $u,v,\varepsilon_\mu$ |
| $e^+e^-\to\mu^+\mu^-$ | $\frac14\sum\lvert\mathcal M\rvert^2=e^4(1+\cos^2\theta)$；$d\sigma/d\Omega=\frac{\alpha^2}{4s}(1+\cos^2\theta)$；$\sigma=\frac{4\pi\alpha^2}{3s}$；$R=3\sum_q Q_q^2$ |
| 康普顿散射 | $s$ 道 + $u$ 道两张图；Ward 恒等式 $k_\mu\mathcal M^\mu=0$ 是规范不变性的检验；Klein–Nishina 公式；低能极限回到 Thomson 截面 $\frac{8\pi}{3}r_e^2$ |
| 技术收获 | Casimir 技巧（自旋求和→求迹）、求迹公式、交叉对称、Mandelstam 变量 |

**往前看**：树图 QED 与实验的符合已经极好，但更深的物理在一圈修正里——真空极化、顶角修正、电子自能。它们的第一个杰作是电子反常磁矩：树图给出 $g=2$（Dirac 方程的预言），一圈修正给出 $g-2=\alpha/\pi$，即 $a_e=\alpha/(2\pi)$。这个无量纲小数如今被算到五圈、测到 12 位有效数字，是整个物理学中理论与实验符合精度最高的数字。下一篇笔记我们就动手算它。

## 自检问题

**1.** 证明 $D_\mu\psi$ 在定域 U(1) 下与 $\psi$ 以相同方式变换，并由此说明为什么 $\bar\psi\gamma^\mu D_\mu\psi$ 和 $\bar\psi\psi$ 都规范不变，而 $\frac12m_\gamma^2A_\mu A^\mu$ 不是。

<details markdown="1"><summary>点击显示答案</summary>

设 $\psi\to e^{i\alpha(x)}\psi$，$A_\mu\to A_\mu - \frac1e\partial_\mu\alpha$。则

$$D_\mu\psi \to \big(\partial_\mu + ieA_\mu - i\partial_\mu\alpha\big)\big(e^{i\alpha}\psi\big) = e^{i\alpha}\partial_\mu\psi + i(\partial_\mu\alpha)e^{i\alpha}\psi + ieA_\mu e^{i\alpha}\psi - i(\partial_\mu\alpha)e^{i\alpha}\psi = e^{i\alpha}D_\mu\psi,$$

第二、四项（$\partial_\mu\alpha$ 项）精确抵消。于是：

- $\bar\psi\gamma^\mu D_\mu\psi \to e^{-i\alpha}\bar\psi\gamma^\mu e^{i\alpha}D_\mu\psi = \bar\psi\gamma^\mu D_\mu\psi$（相位抵消）；
- $\bar\psi\psi$ 同理不变。

而 $A_\mu A^\mu \to (A_\mu - \frac1e\partial_\mu\alpha)(A^\mu - \frac1e\partial^\mu\alpha) = A_\mu A^\mu - \frac{2}{e}A^\mu\partial_\mu\alpha + \frac{1}{e^2}(\partial\alpha)^2 \neq A_\mu A^\mu$，多出的两项无法消去。结论：费米子质量项合法（相位在 $\bar\psi\psi$ 中成对抵消），光子质量项非法——光子无质量是规范不变性的直接后果。

</details>

**2.** 由 $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$ 推出 $\mathrm{tr}(\gamma^\mu\gamma^\nu)=4\eta^{\mu\nu}$ 与四 $\gamma$ 求迹公式，并说明为什么奇数个 $\gamma$ 矩阵的迹为零。

<details markdown="1"><summary>点击显示答案</summary>

**两个 $\gamma$**：$\mathrm{tr}(\gamma^\mu\gamma^\nu) = \mathrm{tr}(2\eta^{\mu\nu} - \gamma^\nu\gamma^\mu) = 2\eta^{\mu\nu}\mathrm{tr}(1) - \mathrm{tr}(\gamma^\mu\gamma^\nu)$（第二步用迹的循环性），故 $2\,\mathrm{tr}(\gamma^\mu\gamma^\nu) = 8\eta^{\mu\nu}$，即 $\mathrm{tr}(\gamma^\mu\gamma^\nu)=4\eta^{\mu\nu}$。

**奇数个**：插入 $(\gamma^5)^2 = 1$ 并用 $\{\gamma^5,\gamma^\mu\}=0$ 与循环性，

$$\mathrm{tr}(\gamma^{\mu_1}\cdots\gamma^{\mu_{2n+1}}) = \mathrm{tr}(\gamma^5\gamma^5\gamma^{\mu_1}\cdots\gamma^{\mu_{2n+1}}) = -\mathrm{tr}(\gamma^5\gamma^{\mu_1}\cdots\gamma^{\mu_{2n+1}}\gamma^5) = -\mathrm{tr}(\gamma^{\mu_1}\cdots\gamma^{\mu_{2n+1}}),$$

每个 $\gamma^\mu$ 与 $\gamma^5$ 交换产生一个负号，奇数个共产生奇数个负号，移项得该迹等于自身的相反数，故为零。

**四个 $\gamma$**：反复用反对易关系把 $\gamma^\mu$ 依次向右挪动直到与 $\gamma^\nu$ 相邻相消：

$$\gamma^\mu\gamma^\nu = 2\eta^{\mu\nu} - \gamma^\nu\gamma^\mu \;\Rightarrow\; \mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 2\eta^{\mu\nu}\mathrm{tr}(\gamma^\rho\gamma^\sigma) - \mathrm{tr}(\gamma^\nu\gamma^\mu\gamma^\rho\gamma^\sigma).$$

对第二项继续把 $\gamma^\mu$ 右移两步，共产生三项度规缩并，最后一项回到原迹（循环性）。整理：

$$\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma) = 4\big(\eta^{\mu\nu}\eta^{\rho\sigma} - \eta^{\mu\rho}\eta^{\nu\sigma} + \eta^{\mu\sigma}\eta^{\nu\rho}\big).$$

注意符号规律：第一、三项为正，中间项为负——收缩的"交叉"一次出一个负号。

</details>

**3.** 从 $\frac14\sum|\mathcal M|^2 = \frac{2e^4(t^2+u^2)}{s^2}$ 出发，补全 $e^+e^-\to\mu^+\mu^-$ 的总截面推导，并解释为什么初态平均因子是 $1/4$ 而不是 $1/2$。

<details markdown="1"><summary>点击显示答案</summary>

质心系无质量运动学：$E = \sqrt s/2$，$|\vec p|=E$，取 $p_1 = E(1,0,0,1)$，$p_3 = E(1,\sin\theta,0,\cos\theta)$。则

$$t = (p_1-p_3)^2 = -2p_1\!\cdot\! p_3 = -\frac{s}{2}(1-\cos\theta), \qquad u = -\frac{s}{2}(1+\cos\theta).$$

$$t^2 + u^2 = \frac{s^2}{4}\big[(1-\cos\theta)^2 + (1+\cos\theta)^2\big] = \frac{s^2}{2}\big(1+\cos^2\theta\big).$$

代回：$\frac14\sum|\mathcal M|^2 = \frac{2e^4}{s^2}\cdot\frac{s^2}{2}(1+\cos^2\theta) = e^4(1+\cos^2\theta)$。微分截面

$$\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2 s}e^4(1+\cos^2\theta) = \frac{16\pi^2\alpha^2}{64\pi^2 s}(1+\cos^2\theta) = \frac{\alpha^2}{4s}(1+\cos^2\theta).$$

总截面：$\sigma = \frac{\alpha^2}{4s}\cdot 2\pi\int_{-1}^{1}(1+x^2)dx = \frac{\alpha^2}{4s}\cdot 2\pi\cdot\frac{8}{3} = \frac{4\pi\alpha^2}{3s}$。

**平均因子**：非极化束流中每个初态费米子的 2 个自旋取向以等概率出现，所以每个初态粒子贡献因子 $1/2$。初态有**两个**粒子（$e^-$ 和 $e^+$），故 $1/2\times1/2 = 1/4$。末态自旋不求平均而是求和（所有末态都接收），光子若也在初态则再乘 $1/2$。$1/2$ 只对应"只有一个带自旋的初态粒子"的情形，比如极化靶上的散射。

</details>

**4.** 验证康普顿振幅的 Ward 恒等式 $k_\nu\mathcal M^\nu = 0$（把 $s$ 道项的化简详细写出，$u$ 道项只需说明要点），并说明为什么"只画 $s$ 道一张图"在原则上是错的。

<details markdown="1"><summary>点击显示答案</summary>

令 $\varepsilon_\nu(k)\to k_\nu$。$s$ 道项的核心结构是 $\gamma^\mu(\slashed p+\slashed k+m)\slashed k\,u(p)/(s-m^2)$。把 $\slashed k$ 拆成

$$\slashed k = (\slashed p + \slashed k - m) - (\slashed p - m).$$

第一部分：

$$\gamma^\mu\frac{(\slashed p+\slashed k+m)(\slashed p+\slashed k-m)}{s-m^2}u(p) = \gamma^\mu\frac{(p+k)^2 - m^2}{s-m^2}u(p) = \gamma^\mu u(p),$$

其中用了 $(\slashed q+m)(\slashed q-m) = q^2 - m^2$（因为 $\slashed q\slashed q = q^2$）。第二部分含 $(\slashed p-m)u(p) = 0$（Dirac 方程），为零。所以 $s$ 道贡献 $\bar u(p')\gamma^\mu u(p)$。

$u$ 道项中 $\slashed k$ 在最左侧与 $\bar u(p')$ 相邻，用 $\slashed k = (\slashed p' - m) - (\slashed p - \slashed k' - m)$（由 $p' = p+k-k'$ 即 $k = p' - (p-k')$）：第一部分被 $\bar u(p')(\slashed p' - m)=0$ 杀死；第二部分使 $(\slashed p-\slashed k'-m)(\slashed p-\slashed k'+m) = u-m^2$ 消掉分母，贡献 $-\bar u(p')\gamma^\mu u(p)$。两项相消，$k_\nu\mathcal M^\nu = 0$。

**为什么必须两张图**：上面看到每张图单独贡献 $\pm\bar u(p')\gamma^\mu u(p) \neq 0$——任何单独一张图都不满足 Ward 恒等式，即单独一张图不是规范不变的。规范不变性是**整个振幅**（所有同阶图之和）的性质。若只画 $s$ 道图，计算出的截面会依赖于非物理的极化分量，结果随规范选择而变，物理上不可接受。这也印证了费曼规则的正确使用原则：同一阶的所有图一张都不能少。

</details>

**5.** 由 Klein–Nishina 公式推出 Thomson 极限 $\sigma = \frac{8\pi\alpha^2}{3m^2}$，并估算其数值（以 $\mathrm{m}^2$ 为单位）。

<details markdown="1"><summary>点击显示答案</summary>

低能极限 $\omega \ll m$：由 $\omega'/\omega = [1 + (\omega/m)(1-\cos\theta)]^{-1} \to 1$，即弹性散射。Klein–Nishina 公式退化为

$$\frac{d\sigma}{d\cos\theta} = \frac{\pi\alpha^2}{m^2}\big(1 + 1 - \sin^2\theta\big) = \frac{\pi\alpha^2}{m^2}\big(1 + \cos^2\theta\big).$$

对角度积分：

$$\sigma = \int_{-1}^{1}d(\cos\theta)\,\frac{\pi\alpha^2}{m^2}(1+\cos^2\theta) = \frac{\pi\alpha^2}{m^2}\left[2 + \frac{2}{3}\right] = \frac{8\pi\alpha^2}{3m^2} = \frac{8\pi}{3}r_e^2, \qquad r_e \equiv \frac{\alpha}{m}.$$

数值：$r_e = \alpha/m_e$，用自然单位 $m_e = 0.511\,\mathrm{MeV}$，$\alpha = 1/137.036$，得 $r_e = 1/(137.036\times0.511\,\mathrm{MeV}) = 2.818\times10^{-3}\,\mathrm{MeV}^{-1}$。换算：$1\,\mathrm{MeV}^{-1} = 197.33\times10^{-15}\,\mathrm{m}\times 10^{-3} = 1.9733\times10^{-13}\,\mathrm{m}$，故 $r_e = 2.818\times10^{-3}\times1.9733\times10^{-13}\,\mathrm{m} \approx 2.82\times10^{-15}\,\mathrm{m}$。于是

$$\sigma_{\text{Thomson}} = \frac{8\pi}{3}(2.82\times10^{-15}\,\mathrm{m})^2 \approx 8.38\times(7.95\times10^{-30})\,\mathrm{m}^2 \approx 6.65\times10^{-29}\,\mathrm{m}^2 = 0.665\,\mathrm{barn}.$$

这正是经典的 Thomson 散射截面——QED 在低能端与经典电磁理论无缝衔接，也是康普顿散射公式正确性的第一个历史检验。

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》：§4.5（QED 费曼规则）、§5.1（$e^+e^-\to\mu^+\mu^-$，本章第 5 节的母本）、§5.5（康普顿散射与 Klein–Nishina 公式的完整代数）。
- Schwartz《Quantum Field Theory and the Standard Model》：第 8、9 章（规范不变性与 QED）、第 13 章（QED 截面计算）。
- Srednicki《Quantum Field Theory》：第 45–51 章（旋量电动力学的路径积分处理）。
- Zee《Quantum Field Theory in a Nutshell》第 II.1、III.4 章（规范原理的物理动机与风格化讲述）。
- （规范原理的几何视角）Nakahara《Geometry, Topology and Physics》规范场论章节，或 Baez & Muniain《Gauge Fields, Knots and Gravity》前几章。
