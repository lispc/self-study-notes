# 电弱统一：SU(2)×U(1)、希格斯机制与 W/Z/光子质量谱

> 路线图位置：第 6 阶段（标准模型）· 第 2 篇——电弱理论的核心构造
> 前置知识：第 4 阶段的量子场论基础（路径积分、传播子、费曼规则）、本阶段 [01-yang-mills.md](01-yang-mills.md)（非阿贝尔规范场的构造）、[../stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md](../stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)（整体对称 vs 规范对称、Goldstone 定理）。
> 学习目标：从四费米理论的危机出发，亲手推出 Glashow–Weinberg–Salam 理论的质量谱——$M_W$、$M_Z$、弱混合角 $\theta_W$、无质量光子，以及 Yukawa 耦合如何给出费米子质量。

---

## 1. 一句话总结

**弱相互作用和电磁相互作用本是同一个规范理论 $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$：四个无质量规范玻色子；希格斯二重态取得真空期望值 $v\approx 246\ \mathrm{GeV}$ 后，其中三个规范玻色子"吃掉"三个 Goldstone 模式变重（$W^\pm$、$Z$），剩下一个沿未破缺方向 $Q=T_3+Y$ 的规范场保持无质量——它就是光子。费米子则被 Yukawa 耦合缝在真空期望值上获得质量。**

下面把这句话逐层拆开。全文用自然单位 $\hbar = c = 1$（质量与能量同用 GeV 计量），度规号差 $\eta = \mathrm{diag}(+1,-1,-1,-1)$。

## 2. 为什么四费米理论必须升级

### 2.1 四费米相互作用的量纲灾难

1934 年费米为 $\beta$ 衰变 $n\to p\,e^-\bar\nu$ 写下的相互作用是四个费米子场在同一点相乘：

$$\mathcal{L}_{\mathrm{Fermi}} = -\frac{G_F}{\sqrt2}\,\big[\bar p\,\gamma^\mu(1-\gamma^5)n\big]\,\big[\bar e\,\gamma_\mu(1-\gamma^5)\nu\big],$$

其中费米常数由 $\mu$ 子寿命测得

$$G_F \approx 1.166\times 10^{-5}\ \mathrm{GeV}^{-2}.$$

灾难藏在量纲里。自然单位下作用量无量纲，$[\mathcal L]=4$（能量四次方），而每个费米子场量纲 $3/2$，所以 $G_F$ 的量纲是 $-2$。**耦合常数带负质量量纲的理论不可重整**：微扰论高阶图的发散需要越来越高的导数算符来吸收，永远无法用有限个参数完成重整化。

更直白的是幺正性破坏。树图阶散射振幅正比于 $G_F$，没有传播子压分母，振幅只能随能量增长：

$$\mathcal M \sim G_F\,E^2, \qquad \sigma \sim G_F^2\,s.$$

截面随 $s$（质心系能量平方）无限增长。但分波幺正性要求单个分波截面有上界 $\sim 1/s$，两者冲突发生在 $G_F s\sim 1$，即

$$\sqrt{s}\;\sim\;G_F^{-1/2}\;\sim\;300\ \mathrm{GeV}.$$

四费米理论在这个能量以上连概率守恒都保不住——它必然只是某个更深层理论的低能有效近似。

### 2.2 媒介玻色子：把点相互作用"摊开"

电磁作用没有这个问题，因为相互作用由光子传播：两个电荷不直接接触，顶点因子 $e$ 无量纲，动量依赖全在传播子 $-i/q^2$ 里。照猫画虎，给弱作用也配媒介玻色子 $W$，振幅变成

$$\mathcal M \sim g^2\,\frac{1}{q^2 - M_W^2}\;\xrightarrow{\ |q^2|\ll M_W^2\ }\;-\frac{g^2}{M_W^2}.$$

低能下传播子压成常数，四费米理论自动恢复，并且给出关系

$$\frac{G_F}{\sqrt2} = \frac{g^2}{8M_W^2}.$$

弱力极短程（原子核尺度以下），而 Yukawa 势 $e^{-Mr}/r$ 的力程 $\sim 1/M$，所以 $W$ 必须**很重**（量级 $10$–$100\ \mathrm{GeV}$）——这不是缺陷，正是四费米"点相互作用"假象的根源。

### 2.3 矛盾：规范不变性禁止质量项

我们希望媒介子是规范玻色子（只有这样理论才可重整，见 01-yang-mills.md 的规范原理），但直接写质量项会立刻破坏规范对称性：

$$\frac12 M^2 A_\mu A^\mu \quad\text{在}\quad A_\mu \to A_\mu + \partial_\mu\alpha\ \text{下不是不变的}.$$

于是一个尖锐的矛盾摆在面前：

- **实验要求**媒介玻色子很重（短程力、四费米近似）；
- **可重整性要求**它是规范场，而规范场不能裸带质量。

出路只有一个：质量不写在拉氏量里，而是**对称性自发破缺后"二次展开"出来的**。这就是希格斯机制存在的理由——它不是装饰品，是可重整性与短程弱力之间唯一的和解方案。

### 2.4 宇称破坏与 V−A：只有左手参与

1956 年李政道、杨振宁指出弱作用中宇称守恒从未被检验过；1957 年吴健雄的 $^{60}\mathrm{Co}$ $\beta$ 衰变实验看到电子优先沿核自旋反方向出射——镜像过程与真实过程发生率不同，**宇称被最大程度地破坏**。

随后 Feynman–Gell-Mann、Sudarshan–Marshak（1958）定下弱流的洛伦兹结构为 **V−A**（矢量减轴矢量）：

$$J^\mu \propto \bar\psi\,\gamma^\mu(1-\gamma^5)\,\psi' = 2\,\bar\psi_L\,\gamma^\mu\,\psi'_L,$$

即弱作用只耦合**左手费米子**（和右手反费米子）。用手征投影算符

$$P_L = \tfrac12(1-\gamma^5), \qquad P_R = \tfrac12(1+\gamma^5), \qquad \psi_{L,R} = P_{L,R}\,\psi,$$

这意味着左手和右手费米子在弱作用眼里是**不同的粒子**——它们必须被赋予不同的规范量子数。这是理解下一节全部表结构的钥匙。

## 3. $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ 结构

### 3.1 左手二重态、右手单态

既然弱作用把中微子变成电子、把上夸克变成下夸克，媒介子必然在双重态内部"换座位"。模仿普通同位旋（第 5 阶段），定义**弱同位旋** $\mathrm{SU}(2)_L$，把左手费米子两两绑成二重态：

$$L = \begin{pmatrix}\nu_L\\ e_L\end{pmatrix}, \qquad Q_L = \begin{pmatrix}u_L\\ d_L\end{pmatrix},$$

生成元 $T^i = \sigma^i/2$（泡利矩阵）。右手费米子不参与 SU(2) 变换，是单态：$e_R$、$u_R$、$d_R$（"原版"标准模型里没有 $\nu_R$）。

光有 SU(2) 给不出电磁作用——二重态内部两个成员电荷不同，需要一个额外的阿贝尔对称性来区分，这就是**超荷** $\mathrm{U}(1)_Y$。电荷由 **Gell-Mann–西岛关系**给出：

$$\boxed{\,Q = T_3 + Y\,}$$

其中 $T_3 = \pm\tfrac12$ 是二重态上/下分量的弱同位旋第三分量，单态 $T_3=0$。一代费米子的量子数：

| 场 | SU(2)$_L$ | $T_3$ | $Y$ | $Q=T_3+Y$ |
|---|---|---|---|---|
| $L=(\nu_L,e_L)^T$ | $\mathbf{2}$ | $(+\tfrac12,-\tfrac12)$ | $-\tfrac12$ | $(0,-1)$ |
| $e_R$ | $\mathbf{1}$ | $0$ | $-1$ | $-1$ |
| $Q_L=(u_L,d_L)^T$ | $\mathbf{2}$ | $(+\tfrac12,-\tfrac12)$ | $\tfrac16$ | $(+\tfrac23,-\tfrac13)$ |
| $u_R$ | $\mathbf{1}$ | $0$ | $\tfrac23$ | $+\tfrac23$ |
| $d_R$ | $\mathbf{1}$ | $0$ | $-\tfrac13$ | $-\tfrac13$ |
| 希格斯 $H=(H^+,H^0)^T$ | $\mathbf{2}$ | $(+\tfrac12,-\tfrac12)$ | $\tfrac12$ | $(+1,0)$ |

注意超荷不是随便填的：每一行都必须通过 $Q=T_3+Y$ 与已知电荷对账（这其实也是反常相消的要求，此处不展开）。以上内容复制成三代，量子数完全相同。

### 3.2 协变导数

规范群有两个因子，各带一个耦合常数：SU(2) 的 $g$ 和 U(1) 的 $g'$。协变导数（规范原理，推导见 01-yang-mills.md）为

$$\boxed{\,D_\mu = \partial_\mu - i g\, T^i W^i_\mu - i g'\, Y B_\mu\,}$$

其中 $W^i_\mu$（$i=1,2,3$）是 SU(2) 规范场，$B_\mu$ 是 U(1) 规范场；作用在单态上 $T^i\to 0$，$Y$ 取表中的数值。例如

$$D_\mu L = \Big(\partial_\mu - i g\,\frac{\sigma^i}{2}W^i_\mu + i\,\frac{g'}{2}B_\mu\Big)L, \qquad D_\mu e_R = \big(\partial_\mu + i g' B_\mu\big)e_R.$$

拉氏量的费米子部分就是 $\sum_f \bar f\,i\gamma^\mu D_\mu f$——每个场按自己的量子数"交费"。

## 4. 希格斯机制热身：Abel 模型

先看最简版本，把"规范场怎么吃 Goldstone 模式"演算一遍，再上电弱正餐。

取一个复标量场 $\phi$ 加 U(1) 规范场 $A_\mu$：

$$\mathcal L = (D_\mu\phi)^*D^\mu\phi - V(\phi) - \frac14 F_{\mu\nu}F^{\mu\nu}, \qquad D_\mu\phi = (\partial_\mu - igA_\mu)\phi,$$

势取墨西哥帽形：

$$V(\phi) = -\mu^2\lvert\phi\rvert^2 + \lambda\lvert\phi\rvert^4, \qquad \mu^2,\lambda>0.$$

**第 1 步：真空不在原点。** 对 $\lvert\phi\rvert$ 求极小，$-\mu^2 + 2\lambda\lvert\phi\rvert^2 = 0$，得

$$\langle\phi\rangle = \frac{v}{\sqrt2}, \qquad v = \frac{\mu}{\sqrt\lambda}.$$

**第 2 步：按真空展开涨落。** 复标量有两个实自由度，参数化为径向模 $h(x)$ 加角向模 $\pi(x)$：

$$\phi(x) = \frac{v + h(x)}{\sqrt2}\,e^{i\pi(x)/v}.$$

$\pi$ 是沿势谷底部滚动的方向——在**整体**对称破缺里它就是 Goldstone 定理保证的无质量玻色子。

**第 3 步：规范变换吃掉 $\pi$。** 但这里对称性是**定域**的。规范变换 $\phi\to e^{i\alpha(x)}\phi$、$A_\mu\to A_\mu + \frac1g\partial_\mu\alpha$，取 $\alpha = -\pi/v$，相位场被完全消去。这个规范叫**幺正规范**（unitary gauge），剩下的场是

$$\phi = \frac{v+h}{\sqrt2}, \qquad D_\mu\phi = \frac{1}{\sqrt2}\partial_\mu h - \frac{ig}{\sqrt2}(v+h)A_\mu.$$

**第 4 步：读出质量。** 代入动能项：

$$\lvert D_\mu\phi\rvert^2 = \frac12(\partial_\mu h)^2 + \frac{g^2v^2}{2}A_\mu A^\mu + \cdots$$

$A_\mu A^\mu$ 的系数正是 Proca 质量项 $\frac12 M_A^2 A_\mu A^\mu$，于是

$$\boxed{\,M_A = gv\,}$$

同时 $V$ 展开后 $h$ 获得质量 $m_h^2 = 2\lambda v^2$，并且出现 $A$–$h$ 三线性耦合 $g^2 v\, h A_\mu A^\mu$（"希格斯与矢量玻色子的耦合正比于其质量"的雏形）。

**自由度账目**：破缺前，复标量 2 个实分量 + 无质量矢量 2 个偏振 = 4；破缺后，实标量 $h$ 1 个 + 有质量矢量 3 个偏振（多出一个纵向模）= 4。账目平衡——规范场的纵向偏振不是凭空来的，它就是被"吃掉"的 Goldstone 模式 $\pi$。

<details markdown="1"><summary>补充说明：这和 Goldstone 定理矛盾吗？</summary>

不矛盾，而且差别正是整个机制的命门。对照 [../stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md](../stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)：

- **整体对称破缺**：真空桶里不同的方向是不同的物理态，谷底的平移模式是货真价实的无质量粒子（Goldstone 定理）。
- **规范对称破缺**：规范变换只是描述的冗余，$\phi$ 空间里沿谷底的两个点经规范变换相连，是**同一个物理态的两种写法**——所以"沿谷底滚动"根本没有物理内容，$\pi$ 可以被规范选择消掉（幺正规范）。所谓"规范对称性破缺"严格说只是口头说法：定域规范对称性不能被破缺（Elitzur 定理），破缺的其实是与之伴随的整体结构；真空的规范依赖性靠 Higgs 机制（而非 Goldstone 玻色子）表现出来。

一句话：整体破缺给你无质量粒子，规范破缺给规范玻色子质量——同一个墨西哥帽，两种命运。

</details>

## 5. 电弱情形：$|D_\mu H|^2$ 展开与质量谱

### 5.1 希格斯二重态与真空

电弱理论把上面的复标量升级为 SU(2) 二重态、超荷 $Y=\tfrac12$ 的希格斯场：

$$H = \begin{pmatrix}H^+\\ H^0\end{pmatrix}, \qquad V(H) = -\mu^2 H^\dagger H + \lambda (H^\dagger H)^2.$$

与 Abel 模型同理，极小值在 $H^\dagger H = v^2/2$、$v = \mu/\sqrt\lambda$。用 SU(2) 变换总可以把真空期望值转到下分量，取

$$\langle H\rangle = \frac{1}{\sqrt2}\begin{pmatrix}0\\ v\end{pmatrix}, \qquad v \approx 246\ \mathrm{GeV}.$$

（$v$ 的数值不是理论输入，而是由 $G_F$ 反解出来的，见自检问题 3 之后的小结表。）$H$ 有 4 个实分量（复二重态），其中 3 个将被吃掉，剩 1 个物理场 $h$——下面看账怎么算的。

### 5.2 展开 $|D_\mu H|^2$：带电 sector

把 $H=\langle H\rangle$ 代入动能项 $(D_\mu H)^\dagger D^\mu H$（$\partial_\mu$ 作用在常数 $v$ 上为零）。用 $T^i=\sigma^i/2$、$Y=\tfrac12$：

$$D_\mu\langle H\rangle = -\frac{iv}{2\sqrt2}\begin{pmatrix} g(W^1_\mu - iW^2_\mu)\\[2pt] g'B_\mu - gW^3_\mu \end{pmatrix}.$$

取模方（用上分量乘其复共轭、下分量乘其复共轭相加）：

$$\lvert D_\mu H\rvert^2 \;\supset\; \frac{v^2}{8}\Big[\, g^2\big(W^1_\mu W^{1\mu} + W^2_\mu W^{2\mu}\big) + \big(gW^3_\mu - g'B_\mu\big)^2 \,\Big].$$

定义带电组合

$$W^\pm_\mu = \frac{W^1_\mu \mp iW^2_\mu}{\sqrt2},$$

则 $W^1_\mu W^{1\mu} + W^2_\mu W^{2\mu} = 2W^+_\mu W^{-\mu}$，质量项写成 $M_W^2\,W^+_\mu W^{-\mu}$，读出

$$\boxed{\,M_W = \frac{gv}{2}\,}$$

$W^\pm$ 确实是电荷 $\pm 1$ 的场：它在电磁规范变换下的转动角正比于 $\pm e$（把 $W^{1,2}$ 看作 SU(2) 空间的矢量，绕未破缺方向 $Q$ 旋转即可验证）。

### 5.3 中性 sector：对角化出 $Z$ 与光子

中性部分是 $W^3$ 与 $B$ 的 $2\times2$ 质量矩阵：

$$\lvert D_\mu H\rvert^2\;\supset\; \frac{v^2}{8}\begin{pmatrix}W^3_\mu & B_\mu\end{pmatrix} \begin{pmatrix} g^2 & -gg'\\ -gg' & g'^2 \end{pmatrix} \begin{pmatrix}W^{3\mu}\\ B^\mu\end{pmatrix}.$$

这个矩阵行列式为零（$g^2g'^2 - g^2g'^2=0$），必有一个零本征值——**无质量规范场自动出现**，不需要额外调节。本征值与本征矢：

- 有质量方向 $Z_\mu \propto gW^3_\mu - g'B_\mu$，本征值 $(g^2+g'^2)$；
- 无质量方向 $A_\mu \propto g'W^3_\mu + gB_\mu$（光子）。

归一化并定义**弱混合角**（Weinberg 角）$\theta_W$：

$$\cos\theta_W = \frac{g}{\sqrt{g^2+g'^2}}, \qquad \sin\theta_W = \frac{g'}{\sqrt{g^2+g'^2}},$$

$$\begin{pmatrix}Z_\mu\\ A_\mu\end{pmatrix} = \begin{pmatrix} \cos\theta_W & -\sin\theta_W\\ \sin\theta_W & \cos\theta_W \end{pmatrix} \begin{pmatrix}W^3_\mu\\ B_\mu\end{pmatrix}, \qquad \boxed{\,M_Z = \frac{\sqrt{g^2+g'^2}\,v}{2} = \frac{M_W}{\cos\theta_W}\,}$$

### 5.4 电磁耦合 $e$ 与未破缺的 U(1)

光子的耦合常数 $e$ 也由 $g,g'$ 定出。把中性流项 $gT_3 W^3 + g'YB$ 用 $Z,A$ 反解代入，$A_\mu$ 的系数为

$$g\sin\theta_W\,T_3 + g'\cos\theta_W\,Y = \frac{gg'}{\sqrt{g^2+g'^2}}\,(T_3 + Y) = \frac{gg'}{\sqrt{g^2+g'^2}}\,Q,$$

正比于电荷 $Q$！所以

$$\boxed{\,e = \frac{gg'}{\sqrt{g^2+g'^2}} = g\sin\theta_W\,}$$

而 $Z$ 的耦合涉及 $T_3 - Q\sin^2\theta_W$ 的组合——**中性弱流**的预言，它与电磁流是两种不同的相互作用。

**光子为什么恰好无质量？** 破缺前有四个生成元 $T_1,T_2,T_3,Y$。检查谁湮灭真空：$T_3\langle H\rangle = -\tfrac12\langle H\rangle$（$\sigma^3/2$ 作用在下分量给出 $-1/2$），$Y\langle H\rangle = +\tfrac12\langle H\rangle$，于是

$$Q\,\langle H\rangle = (T_3 + Y)\langle H\rangle = 0.$$

组合 $Q=T_3+Y$ 保持不破缺——残余的 $\mathrm{U}(1)_{\mathrm{EM}}$。未破缺生成元的规范场不能有质量（它的规范变换仍然精确地保持真空和拉氏量），这个场就是 $A_\mu$。破缺模式：

$$\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y \;\longrightarrow\; \mathrm{U}(1)_{\mathrm{EM}}.$$

四个生成元破三个，三个规范玻色子（$W^+,W^-,Z$）各吃掉一个 Goldstone 模式获得质量和纵向偏振；第四个（光子）幸存。自由度总账：破缺前 4 个无质量规范玻色子（$4\times2=8$ 偏振）+ 希格斯 4 个实分量 = 12；破缺后 3 个有质量矢量（$3\times3=9$）+ 光子（2）+ 希格斯玻色子 $h$（1）= 12。账目平衡。

### 5.5 实验判决

- **1973 年**，CERN 的 Gargamelle 气泡室观测到 $\bar\nu_\mu e \to \bar\nu_\mu e$ 等无电荷交换的中微子散射——**中性流**存在，这是 GWS 理论区别于纯带电流模型的独特预言；
- **1983 年**，UA1/UA2 在 $p\bar p$ 对撞中直接发现 $W$（$M_W\approx 80\ \mathrm{GeV}$）与 $Z$（$M_Z\approx 91\ \mathrm{GeV}$），质量与 $\sin^2\theta_W\approx 0.23$ 的预言吻合（Rubbia 与 van der Meer 获 1984 年诺贝尔奖）；
- **2012 年**，ATLAS 与 CMS 发现 $m_h\approx 125\ \mathrm{GeV}$ 的希格斯玻色子——机制的最后一块拼图。

数值对账：$e\approx0.31$、$\sin^2\theta_W\approx0.23$ 给出 $g\approx0.65$、$g'\approx0.36$，于是 $M_W=gv/2\approx 80\ \mathrm{GeV}$、$M_Z\approx 91\ \mathrm{GeV}$——一个 $v$ 同时定出三个量，这不是巧合而是理论的自洽性检验。

## 6. 费米子质量：Yukawa 耦合

### 6.1 为什么裸质量项不合法

Dirac 质量项 $-m\bar\psi\psi = -m(\bar\psi_L\psi_R + \bar\psi_R\psi_L)$ 把左手和右手缝在一起。但左手是 SU(2) 二重态、右手是单态，这个乘积在规范变换下**不是不变的**——手征理论的费米子禁止裸质量。这和规范玻色子面临的禁令完全同源。

### 6.2 Yukawa 项：希格斯当媒人

希格斯二重态的量子数恰好能缝合左右手：$\bar L$ 是 $\bar{\mathbf{2}}$（$Y=+\tfrac12$），$H$ 是 $\mathbf{2}$（$Y=\tfrac12$），$e_R$ 是单态（$Y=-1$），于是

$$\mathcal L_{\mathrm{Yukawa}} \supset -y_e\,\bar L H\, e_R + \mathrm{h.c.}$$

是 SU(2) 单态且超荷 $\tfrac12+\tfrac12-1=0$——规范不变！代入 $H=\langle H\rangle$（下分量 $v/\sqrt2$），$\bar L H e_R \supset \frac{v}{\sqrt2}\bar e_L e_R$，于是

$$\mathcal L \supset -\frac{y_e v}{\sqrt2}\,\bar e e \quad\Longrightarrow\quad \boxed{\,m_e = \frac{y_e v}{\sqrt2}\,}$$

质量出现了，但拉氏量从头到尾规范不变——裸质量的禁令被真空期望值合法地绕过。

**上型夸克需要翻转的二重态。** $\bar Q_L H d_R$ 给出下型夸克质量没问题，但给 $u$ 夸克造质量需要取 $H$ 的上分量，而它不带真空期望值。解法是电荷共轭二重态

$$\tilde H \equiv i\sigma_2 H^*,$$

它仍是 SU(2) 二重态但 $Y=-\tfrac12$（$i\sigma_2$ 把二重态与反二重态互换，这是 SU(2) 的赝实性），且 $\langle\tilde H\rangle = (v/\sqrt2,\ 0)^T$——真空期望值翻到了上分量。于是一代的完整 Yukawa 项为

$$\mathcal L_{\mathrm{Yukawa}} = -y_d\,\bar Q_L H\, d_R - y_u\,\bar Q_L \tilde H\, u_R - y_e\,\bar L H\, e_R + \mathrm{h.c.}$$

### 6.3 三代与 CKM 矩阵

推广到三代，Yukawa 常数变成 $3\times3$ 复矩阵 $y_u^{ij}, y_d^{ij}, y_e^{ij}$（$i,j=1,2,3$ 是代指标）。破缺后质量矩阵 $M_u^{ij} = y_u^{ij}v/\sqrt2$ 一般**不对角**。每个矩阵可用双幺正变换对角化（$M = U_L^\dagger\, \mathrm{diag}\, U_R$），于是得到 $6$ 个夸克质量 + $3$ 个轻子质量，共 $9$ 个 Yukawa 参数。

关键：$M_u$ 和 $M_d$ 一般**不能同时**对角化——把上夸克转到质量本征态基的幺正变换 $U_u$ 与下夸克的 $U_d$ 不同，带电流 $\bar u_L\gamma^\mu d_L$ 里就出现失配矩阵

$$V_{\mathrm{CKM}} = U_u\, U_d^\dagger,$$

这就是 **Cabibbo–Kobayashi–Maskawa 矩阵**：夸克味混合的来源。$3\times3$ 幺正矩阵去掉不可观测的夸克整体相位后剩 4 个物理参数——3 个混合角 + 1 个复相位，后者是标准模型里 **CP 破坏**的来源（Kobayashi–Maskawa 因此获 2008 年诺贝尔奖）。注意 CKM 只出现在**带电**流中：中性流里 $U_u^\dagger U_u = 1$ 自动抵消，这是味道改变中性流在树图阶被禁戒（GIM 机制）的原因。

**"希格斯场不是糖浆"。** 常见的科普比喻"粒子在希格斯场的海洋里游泳被拖慢"是误导：质量不是阻力（阻力耗散能量、正比于速度，而真空中匀速运动的粒子没有任何摩擦）。正确的图像是：真空中 $H$ 取常数值 $v$，Yukawa 耦合把左手和右手费米子**缝合成一个 Dirac 粒子**，$m_f = y_f v/\sqrt2$ 是缝合的强度——静止的粒子同样有这个质量。另外，你身体的质量绝大部分来自质子内部的 QCD 束缚能，与希格斯几乎无关。

## 7. $\rho$ 参数：二重态希格斯的指纹

定义可测量

$$\rho \equiv \frac{M_W^2}{M_Z^2\cos^2\theta_W}.$$

回看第 5 节的推导：$M_W = gv/2$、$M_Z = \sqrt{g^2+g'^2}v/2$、$\cos\theta_W = g/\sqrt{g^2+g'^2}$，代入得 $\rho = 1$——**树图阶自动成立**，没有用任何精细调节。为什么理论如此"自觉"？

秘密藏在希格斯势的额外对称性里。$V(H)$ 只依赖组合 $H^\dagger H$。把二重态 $H$ 的 4 个实分量排成 4 维实矢量，$H^\dagger H$ 是其长度平方，所以 $V$ 其实有 $\mathrm{SO}(4)\simeq \mathrm{SU}(2)_L\times\mathrm{SU}(2)_R$ 的整体对称性——比规范群 $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ **更大**。真空期望值把它破缺到对角子群 $\mathrm{SU}(2)_V$（custodial 对称性，"监护对称性"），这个残余对称性在三个 $W^i$ 之间旋转，强制三个规范玻色子的质量满足 $M_W = M_Z\cos\theta_W$。

它的价值在于反向推理：若希格斯是别的表示（如三重态），custodial 对称一般不成立，$\rho\neq1$。实验上 $\rho = 1.0004\pm0.0002$（偏离 1 的十万分之四来自顶夸克等的圈图修正），与二重态预言精确吻合——这是"希格斯是二重态"最硬的间接证据之一。

## 8. 小结

破缺前后对照（规范玻色子 + 标量自由度合计 $8+4 = 9+2+1 = 12$，账目平衡）：

| | 破缺前：SU(2)$_L\times$U(1)$_Y$ | 破缺后：U(1)$_{\mathrm{EM}}$ |
|---|---|---|
| 规范玻色子 | $W^1,W^2,W^3,B$ 全部无质量 | $W^\pm$（$gv/2$）、$Z$（$M_W/\cos\theta_W$）有质量；$\gamma$ 无质量 |
| 标量 | 希格斯二重态 4 个实分量 | 3 个被吃掉成为纵向偏振；剩 1 个物理 $h$（$m_h=\sqrt{2\lambda}\,v$） |
| 费米子 | 全部无质量（手征禁戒裸质量） | $m_f = y_f v/\sqrt2$，9 个 Yukawa + CKM 4 参数 |
| 守恒荷 | $T_1,T_2,T_3,Y$ | 只剩电荷 $Q=T_3+Y$（湮灭真空） |

核心公式链：$v = (\sqrt2 G_F)^{-1/2} \approx 246\ \mathrm{GeV}$，$M_W = gv/2$，$M_Z = M_W/\cos\theta_W$，$e = g\sin\theta_W$，$\rho = 1$（树图）。所有质量都追溯到同一个 $v$——这就是"统一"二字的兑现。与标准模型拉氏量的逐项对照见 [04-standard-model-lagrangian.md](04-standard-model-lagrangian.md)。

## 自检问题

**1.** 从 $D_\mu = \partial_\mu - ig\frac{\sigma^i}{2}W^i_\mu - ig'\frac12 B_\mu$ 与 $\langle H\rangle = (0, v/\sqrt2)^T$ 出发，展开 $\lvert D_\mu H\rvert^2$，推出 $M_W = gv/2$ 并写出中性 sector 的质量矩阵。

<details markdown="1"><summary>点击显示答案</summary>

先算矩阵作用。$\sigma^1\langle H\rangle = (v/\sqrt2, 0)^T$，$\sigma^2\langle H\rangle = (-iv/\sqrt2, 0)^T$（注意 $-i\sigma^2(0,1)^T = (0,1)^T$ 类计算：$\sigma^2(0,1)^T = (-i,0)^T$），$\sigma^3\langle H\rangle = -(0, v/\sqrt2)^T$。于是

$$\Big(g\frac{\sigma^i}{2}W^i_\mu + \frac{g'}{2}B_\mu\Big)\langle H\rangle = \frac{v}{2\sqrt2}\begin{pmatrix} g(W^1_\mu - iW^2_\mu)\\ g'B_\mu - gW^3_\mu \end{pmatrix},$$

$$D_\mu\langle H\rangle = -\frac{iv}{2\sqrt2}\begin{pmatrix} g(W^1_\mu - iW^2_\mu)\\ g'B_\mu - gW^3_\mu \end{pmatrix}.$$

模方是上分量与其复共轭之积加下分量与其复共轭之积。上分量给出

$$\frac{v^2}{8}g^2\,(W^1_\mu - iW^2_\mu)(W^{1\mu} + iW^{2\mu}) = \frac{v^2}{8}g^2\big(W^1_\mu W^{1\mu} + W^2_\mu W^{2\mu}\big) = \frac{g^2v^2}{4}W^+_\mu W^{-\mu},$$

与质量项 $M_W^2 W^+_\mu W^{-\mu}$ 对比得 $M_W = gv/2$。下分量给出

$$\frac{v^2}{8}\big(gW^3_\mu - g'B_\mu\big)^2 = \frac{v^2}{8}\begin{pmatrix}W^3_\mu & B_\mu\end{pmatrix}\begin{pmatrix} g^2 & -gg'\\ -gg' & g'^2\end{pmatrix}\begin{pmatrix}W^{3\mu}\\ B^\mu\end{pmatrix},$$

即所求中性质量矩阵。

</details>

**2.** 对角化上一题的中性质量矩阵，定义 $\theta_W$，并验证 $e = g\sin\theta_W$ 确实等于 $gg'/\sqrt{g^2+g'^2}$。

<details markdown="1"><summary>点击显示答案</summary>

矩阵 $M^2 = \frac{v^2}{4}\begin{pmatrix} g^2 & -gg'\\ -gg' & g'^2\end{pmatrix}$（提出 $\frac12 M^2$ 归一后的系数）。行列式 $= g^2g'^2 - g^2g'^2 = 0$，迹 $= g^2+g'^2$，故本征值为 $0$ 与 $(g^2+g'^2)v^2/4$，后者即 $M_Z^2$。

零本征矢满足 $g^2 a = gg' b$，即 $(a,b)\propto(g', g)$；归一化得 $A_\mu = \sin\theta_W W^3_\mu + \cos\theta_W B_\mu$，其中

$$\sin\theta_W = \frac{g'}{\sqrt{g^2+g'^2}}, \qquad \cos\theta_W = \frac{g}{\sqrt{g^2+g'^2}}.$$

于是

$$e = g\sin\theta_W = \frac{gg'}{\sqrt{g^2+g'^2}},$$

直接验证成立（对 $g'$ 也对称：$e = g'\cos\theta_W$）。物理检查：中性流中 $A_\mu$ 的耦合系数 $g\sin\theta_W T_3 + g'\cos\theta_W Y = e(T_3+Y) = eQ$，正比于电荷——光子的确是电磁场的规范玻色子。

</details>

**3.** 数出电弱破缺前后的全部玻色自由度，并说明三个 Goldstone 模式"去哪了"。

<details markdown="1"><summary>点击显示答案</summary>

**破缺前**：4 个无质量规范玻色子 $W^1,W^2,W^3,B$，无质量矢量各 2 个横向偏振，共 $4\times2=8$；希格斯二重态 $H$ 是复二重态，4 个实标量分量。合计 $8+4=12$。

**破缺后**：$W^+, W^-, Z$ 有质量，有质量矢量各 3 个偏振（多一个纵向模），共 $3\times3=9$；光子无质量，2 个偏振；剩 1 个实标量 $h$。合计 $9+2+1=12$。账目平衡。

三个"消失"的希格斯分量对应希格斯流形上沿 $\mathrm{SU}(2)\times\mathrm{U}(1)/\mathrm{U}(1)_{\mathrm{EM}}$ 三个破缺方向的涨落——它们是整体对称破缺意义下的 Goldstone 模式。但规范对称性是冗余而非物理对称性，这些模式可以被规范变换消去（幺正规范）；它们的物理内容没有丢，而是转移成 $W^\pm$ 和 $Z$ 的**纵向偏振**。形象地说，三个规范玻色子"吃掉"三个 Goldstone 模式，各自长胖出一个纵向自由度。剩下的第四个分量（沿真空期望值方向的径向涨落）无处可吃，成为物理的希格斯玻色子 $h$。

</details>

**4.** 由 Yukawa 项 $-y_f\bar Q_L H f_R + \mathrm{h.c.}$ 推出 $m_f = y_f v/\sqrt2$，并用 $m_t = 173\ \mathrm{GeV}$ 估算顶夸克的 Yukawa 耦合 $y_t$，说明其物理含义。

<details markdown="1"><summary>点击显示答案</summary>

代入真空期望值 $H \to (0, v/\sqrt2)^T$（对下型费米子；上型用 $\tilde H$，结构相同），$\bar Q_L H f_R \to \frac{v}{\sqrt2}\bar f_L f_R$，于是

$$\mathcal L \supset -\frac{y_f v}{\sqrt2}\big(\bar f_L f_R + \bar f_R f_L\big) = -\frac{y_f v}{\sqrt2}\,\bar f f,$$

与 Dirac 质量项 $-m_f\bar f f$ 对比得 $m_f = y_f v/\sqrt2$。

顶夸克：

$$y_t = \frac{\sqrt2\,m_t}{v} = \frac{\sqrt2\times 173}{246} \approx 0.99 \approx 1.$$

**物理含义**：费米子质量的巨大跨度（电子 $m_e\approx 0.5\ \mathrm{MeV}$ 对应 $y_e\approx 3\times10^{-6}$，顶夸克 $y_t\approx1$，相差五个数量级）全部压在无量纲的 Yukawa 耦合上——标准模型不解释这个谱，只是参数化它，这是"味之谜"。顶夸克 $y_t\approx 1$ 意味着它与希格斯场的耦合最强（希格斯衰变、圈图修正里顶夸克都唱主角），也是希格斯势被顶夸克圈图显著修正、乃至真空亚稳性讨论的技术根源。

</details>

**5.** 为什么电磁 $\mathrm{U}(1)$ 保持不破缺？写出判断真空湮灭的生成元组合，并推导 $Q=T_3+Y$ 作用在 $\langle H\rangle$ 上的结果。

<details markdown="1"><summary>点击显示答案</summary>

真空期望值 $\langle H\rangle$ 破缺某个生成元 $T$，当且仅当 $T\langle H\rangle \neq 0$（以 $T$ 为参数的规范变换把真空转到另一个点）；若 $T\langle H\rangle = 0$，该方向的规范变换保持真空不动，对称性不破缺，对应规范场保持无质量。

逐个检查四个生成元对 $\langle H\rangle = (0, v/\sqrt2)^T$ 的作用：

$$T_1\langle H\rangle = \frac{\sigma^1}{2}\langle H\rangle = \frac{v}{2\sqrt2}\begin{pmatrix}1\\0\end{pmatrix}\neq0, \qquad T_2\langle H\rangle = \frac{\sigma^2}{2}\langle H\rangle = \frac{v}{2\sqrt2}\begin{pmatrix}-i\\0\end{pmatrix}\neq0,$$

$$T_3\langle H\rangle = \frac{\sigma^3}{2}\langle H\rangle = -\frac12\langle H\rangle\neq0, \qquad Y\langle H\rangle = +\frac12\langle H\rangle\neq0.$$

四个单独都不湮灭真空，各破缺。但取线性组合：

$$Q\,\langle H\rangle = (T_3 + Y)\langle H\rangle = \Big(-\frac12 + \frac12\Big)\langle H\rangle = 0.$$

所以组合 $Q = T_3+Y$——正是电荷——保持不破缺。破缺模式 $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y\to\mathrm{U}(1)_{\mathrm{EM}}$ 的残余对称性由这一个生成元张成，其规范场就是第 5 节对角化出的无质量组合 $A_\mu$。这也解释了为什么希格斯真空期望值必须放在**电中性**分量（下分量 $H^0$，$Q=-\tfrac12+\tfrac12=0$）：若带电分量取得真空期望值，电荷本身就被破缺，光子会变重，原子无法存在。

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》第 20 章（Abel Higgs 模型与 GWS 理论，与本篇推导一一对应）、21.3 节（$\rho$ 参数与 custodial 对称）。
- Schwartz《Quantum Field Theory and the Standard Model》第 29 章（弱相互作用，含四费米理论极限与幺正性讨论）。
- Cheng & Li《Gauge Theory of Elementary Particle Physics》电弱标准模型章节（记号详尽，适合对账每一个因子）。
- Griffiths《Introduction to Elementary Particles》第 10 章（规范理论）——电弱部分物理图像清楚，推导负担最轻。
- （群论视角补充）Georgi《Weak Interactions and Modern Particle Theory》前几章；Zee《Quantum Field Theory in a Nutshell》对称破缺与 Higgs 机制部分。
