# 标准模型拉氏量：逐项读懂那著名的一页

> 路线图位置：第 6 阶段（标准模型）· 收官篇——组装说明书
> 前置知识：第 4 阶段的规范场论与 Yang–Mills 理论、第 5 阶段的 QCD、本阶段的电弱对称性自发破缺（这些笔记见路线图相应章节；本章在每个概念首次出现时给出够用的直觉解释，但完整推导请回到前置笔记）。
> 学习目标：把印在 T 恤上的那一页标准模型拉氏量逐项翻译成人话——每个符号都认识，每一项的物理角色都能说清，并理解为什么它如此成功又明显不是终点。

---

## 1. 一句话总结

**标准模型是一个以 $\mathrm{SU}(3)_C\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ 为规范群的可重整量子场论：规范玻色子的动能项（含自耦合）、费米子与规范场的协变动能项、希格斯场的动能与势、以及 Yukawa 耦合四大块，就是全部内容；费米子和 $W/Z$ 玻色子的质量都不允许直接写进拉氏量，它们是希格斯场取得真空期望值后"二次展开"出来的副产品。**

下面把这句话逐层拆开。全文用自然单位 $\hbar = c = 1$（质量和能量同量纲，都用 eV 计量），度规号差 $\eta = \mathrm{diag}(+1,-1,-1,-1)$。

## 2. 那一页的总结构

纪念品商店里那页公式看起来吓人，其实只有四行骨架：

$$\boxed{\;\mathcal{L}_{\mathrm{SM}} = \underbrace{-\tfrac14 G^a_{\mu\nu}G^{a\mu\nu} -\tfrac14 W^i_{\mu\nu}W^{i\mu\nu} -\tfrac14 B_{\mu\nu}B^{\mu\nu}}_{\mathcal{L}_{\mathrm{gauge}}} \;+\; \underbrace{\sum_f \bar f\, i\gamma^\mu D_\mu\, f}_{\mathcal{L}_{\mathrm{fermion}}} \;+\; \underbrace{|D_\mu H|^2 - V(H)}_{\mathcal{L}_{\mathrm{Higgs}}} \;+\; \underbrace{\mathcal{L}_{\mathrm{Yukawa}}}_{\text{费米子质量来源}}\;}$$

每一块的职责：

- $\mathcal{L}_{\mathrm{gauge}}$：12 个规范玻色子（8 胶子、3 个 $W^i$、1 个 $B$）的动能与**自相互作用**；
- $\mathcal{L}_{\mathrm{fermion}}$：所有夸克、轻子的动能，以及它们与规范玻色子的全部相互作用（协变导数 $D_\mu$ 一手包办）；
- $\mathcal{L}_{\mathrm{Higgs}}$：希格斯二重态 $H$ 的动能项和墨西哥帽势 $V(H)$，负责电弱对称性自发破缺；
- $\mathcal{L}_{\mathrm{Yukawa}}$：费米子与希格斯的耦合，破缺后变成费米子质量。

本章的目标：读完之后，这页公式上的每一项你都能指着说"它是什么、它负责什么物理"。

## 3. 规范群与粒子内容总表

### 3.1 规范群

标准模型的全部力由规范群

$$\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$$

决定，三个因子各带一个耦合常数 $g_s,\ g,\ g'$：

- $\mathrm{SU}(3)_C$：**色**（color），强相互作用（QCD，见第 5 阶段笔记），8 个胶子 $G^a_\mu$（$a=1,\dots,8$，对应 8 个生成元 $T^a = \lambda^a/2$，$\lambda^a$ 是 Gell-Mann 矩阵）；
- $\mathrm{SU}(2)_L$：**弱同位旋**（weak isospin），只耦合左手费米子，3 个规范场 $W^i_\mu$（$i=1,2,3$，生成元 $T^i = \sigma^i/2$，$\sigma^i$ 是泡利矩阵）；
- $\mathrm{U}(1)_Y$：**超荷**（hypercharge $Y$），1 个规范场 $B_\mu$。注意：U(1)$_Y$ **不是**电磁作用；电磁 U(1)$_{\mathrm{EM}}$ 要等对称性破缺后才从 SU(2)$_L\times$U(1)$_Y$ 里"剩"下来。

电荷由 **Gell-Mann–西岛关系** 给出：

$$Q = T_3 + Y,$$

其中 $T_3$ 是弱二重态中成员（上/下分量）的弱同位旋第三分量。这个关系是本表自洽性的检验器：下面每一行的 $Q$ 都应等于 $T_3 + Y$。

### 3.2 一代费米子

| 场 | SU(3)$_C$ | SU(2)$_L$ | $T_3$ | $Y$ | $Q=T_3+Y$ |
|---|---|---|---|---|---|
| $Q_L = \begin{pmatrix}u_L\\ d_L\end{pmatrix}$ | $\mathbf{3}$ | $\mathbf{2}$ | $(+\tfrac12, -\tfrac12)$ | $\tfrac16$ | $(+\tfrac23, -\tfrac13)$ |
| $u_R$ | $\mathbf{3}$ | $\mathbf{1}$ | $0$ | $\tfrac23$ | $+\tfrac23$ |
| $d_R$ | $\mathbf{3}$ | $\mathbf{1}$ | $0$ | $-\tfrac13$ | $-\tfrac13$ |
| $L_L = \begin{pmatrix}\nu_L\\ e_L\end{pmatrix}$ | $\mathbf{1}$ | $\mathbf{2}$ | $(+\tfrac12, -\tfrac12)$ | $-\tfrac12$ | $(0, -1)$ |
| $e_R$ | $\mathbf{1}$ | $\mathbf{1}$ | $0$ | $-1$ | $-1$ |
| 希格斯 $H = \begin{pmatrix}H^+\\ H^0\end{pmatrix}$ | $\mathbf{1}$ | $\mathbf{2}$ | $(+\tfrac12, -\tfrac12)$ | $\tfrac12$ | — |

三点说明：

- 没有 $\nu_R$（在"原版"标准模型里中微子无质量；中微子质量的留白见第 8 节）。
- 夸克是色三重态（红绿蓝三种色，$Q_L$ 实际上有 3 个色分量，与 SU(2) 二重态结构相乘，共 6 个分量）；轻子是色单态，不参与强作用。
- 以上内容重复成**三代**（$u,d \to c,s \to t,b$；$e \to \mu \to \tau$），量子数完全相同，只有 Yukawa 耦合不同。所以完整粒子清单是：一代 15 个手征费米子场 $\times 3$ 代 $=45$ 个，加 12 个规范玻色子和 1 个希格斯二重态。

### 3.3 左手与右手：为什么要分列

任何 Dirac 旋量 $\psi$ 可以用手征投影算符拆成两半：

$$P_L = \tfrac12(1-\gamma^5), \qquad P_R = \tfrac12(1+\gamma^5), \qquad \psi_{L,R} = P_{L,R}\,\psi.$$

由 $\gamma^5$ 的性质（$(\gamma^5)^2=1$、$\{\gamma^5,\gamma^\mu\}=0$）可知 $P_{L,R}^2 = P_{L,R}$、$P_LP_R=0$、$P_L+P_R=1$，确实是投影。高能极限下，$\psi_L$ 大致是"自旋与动量反平行"（左手螺旋）的部分，$\psi_R$ 反之。

为什么表格里左右手要分开列、量子数还不一样？因为**弱相互作用破坏宇称**：实验（吴健雄 1957 年的 $^{60}$Co $\beta$ 衰变）发现弱作用只耦合左手费米子（和右手反费米子）。所以 SU(2)$_L$ 把 $u_L,d_L$ 绑成二重态，而 $u_R,d_R$ 各自是单态——它们在规范群下是完全不同的粒子，必须分开列。这是标准模型最"不对称"也最有性格的一条公理：它是**手征理论**。

## 4. $\mathcal{L}_{\mathrm{gauge}}$：规范玻色子的动能与自耦合

三个规范场各配一个场强张量：

$$G^a_{\mu\nu} = \partial_\mu G^a_\nu - \partial_\nu G^a_\mu + g_s f^{abc} G^b_\mu G^c_\nu \quad (a=1,\dots,8),$$

$$W^i_{\mu\nu} = \partial_\mu W^i_\nu - \partial_\nu W^i_\mu + g\, \epsilon^{ijk} W^j_\mu W^k_\nu \quad (i=1,2,3),$$

$$B_{\mu\nu} = \partial_\mu B_\nu - \partial_\nu B_\mu.$$

其中 $f^{abc}$ 是 SU(3) 的结构常数（$[T^a,T^b]=if^{abc}T^c$），$\epsilon^{ijk}$ 是 SU(2) 的结构常数（就是 Levi-Civita 符号）。拉氏量是

$$\mathcal{L}_{\mathrm{gauge}} = -\tfrac14 G^a_{\mu\nu}G^{a\mu\nu} -\tfrac14 W^i_{\mu\nu}W^{i\mu\nu} -\tfrac14 B_{\mu\nu}B^{\mu\nu}.$$

**关键点在最后那两项二次方。** 电磁场的场强 $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ 是线性的，$-\tfrac14 F^2$ 只含光子动能，光子之间不直接相互作用（QED 里光子-光子散射要靠电子圈，极其微弱）。而非阿贝尔场强里多了 $g f^{abc}A^bA^c$ 这个**非线性项**，代入 $-\tfrac14 G^2$ 展开，除了动能项外还有：

$$\mathcal{L}_{\mathrm{gauge}} \supset \underbrace{-g_s f^{abc}\,(\partial_\mu G^a_\nu)\, G^{b\mu} G^{c\nu}}_{\text{三规范玻色子顶点}} \; \underbrace{-\tfrac14 g_s^2 f^{abe}f^{cde}\, G^a_\mu G^b_\nu G^{c\mu}G^{d\nu}}_{\text{四规范玻色子顶点}}.$$

$W$ 的部分同理（$\epsilon^{ijk}$ 换成结构常数即可）。物理含义：**非阿贝尔规范玻色子自己携带"荷"（胶子带色，$W$ 带弱荷），所以它们彼此直接相互作用**。这是 Yang–Mills 理论与 Maxwell 理论的本质区别（完整理论见 Yang–Mills 笔记），它带来两个后果：

- 胶子自耦合是 QCD **渐近自由**（高能变弱）与低能**禁闭**的根源（见 QCD 笔记）；
- $W^i$ 的自耦合给出电弱理论里的三规范、四规范玻色子顶点（如 $WW\gamma$、$WWZ$），已被 LEP 对撞机精确验证。

而 U(1) 的 $B_{\mu\nu}$ 没有非线性项——阿贝尔场不带自己的荷，$B$ 场"孤零零"没有自耦合。

## 5. $\mathcal{L}_{\mathrm{fermion}}$：协变导数一手包办全部相互作用

### 5.1 协变导数：按表示"各交各的税"

普通导数 $\partial_\mu$ 在规范变换下不协变，要升级成协变导数 $D_\mu$（规范原理，见 Yang–Mills 笔记）。每个场按它在规范群下的表示交费：

$$D_\mu = \partial_\mu - i g_s\, T^a G^a_\mu - i g\, T^i W^i_\mu - i g'\, Y B_\mu,$$

规则：色三重态上 $T^a = \lambda^a/2$，色单态上 $T^a = 0$；弱二重态上 $T^i = \sigma^i/2$，弱单态上 $T^i = 0$；$Y$ 取第 3 节表里的值。于是五种费米子场的协变导数各不相同——$Q_L$ 三个群全交税，$e_R$ 只交超荷税：

$$\begin{aligned}
D_\mu Q_L &= \Big(\partial_\mu - i g_s \tfrac{\lambda^a}{2} G^a_\mu - i g \tfrac{\sigma^i}{2} W^i_\mu - i g' \tfrac16 B_\mu\Big) Q_L,\\
D_\mu u_R &= \Big(\partial_\mu - i g_s \tfrac{\lambda^a}{2} G^a_\mu - i g' \tfrac23 B_\mu\Big) u_R,\\
D_\mu d_R &= \Big(\partial_\mu - i g_s \tfrac{\lambda^a}{2} G^a_\mu + i g' \tfrac13 B_\mu\Big) d_R,\\
D_\mu L_L &= \Big(\partial_\mu - i g \tfrac{\sigma^i}{2} W^i_\mu + i g' \tfrac12 B_\mu\Big) L_L,\\
D_\mu e_R &= \Big(\partial_\mu + i g' B_\mu\Big) e_R.
\end{aligned}$$

### 5.2 动能项 = 相互作用项

费米子部分的拉氏量就是把五个场（乘三代）的 Dirac 动能项加起来：

$$\mathcal{L}_{\mathrm{fermion}} = \bar Q_L i\gamma^\mu D_\mu Q_L + \bar u_R i\gamma^\mu D_\mu u_R + \bar d_R i\gamma^\mu D_\mu d_R + \bar L_L i\gamma^\mu D_\mu L_L + \bar e_R i\gamma^\mu D_\mu e_R.$$

把 $D_\mu = \partial_\mu + (\text{规范场项})$ 代入，$\partial_\mu$ 部分给出费米子自由传播子，其余每一项都是一个**费米子–规范玻色子顶点**。例如：

- $g_s\, \bar Q_L \gamma^\mu \tfrac{\lambda^a}{2} G^a_\mu Q_L$：胶子–夸克顶点（QCD 的基本顶点，与味无关、只认色）；
- $\dfrac{g}{\sqrt2}\big(\bar u_L \gamma^\mu d_L\, W^+_\mu + \mathrm{h.c.}\big)$：**带电流**顶点，$W^\pm_\mu = (W^1_\mu \mp i W^2_\mu)/\sqrt2$。它把 $u_L$ 变成 $d_L$——这就是 $\beta$ 衰变、$\mu$ 衰变等一切味改变弱过程的基本机制（夸克跨代混合即 CKM 矩阵，也挂在这里）；
- $\bar\psi\gamma^\mu(g T_3 W^3_\mu + g' Y B_\mu)\psi$：**中性流**，$W^3$ 与 $B$ 的线性组合，破缺后重组为 $Z$ 和光子 $\gamma$（下一节）。

"最小耦合"的威力在于：写下协变导数，所有相互作用顶点就被规范对称性**唯一锁定**，没有自由发挥的余地——这就是"规范原理决定相互作用"这句口号的实际内容。

### 5.3 被禁止的一项：费米子质量

注意 $\mathcal{L}_{\mathrm{fermion}}$ 里**没有** $-m\bar\psi\psi$ 这样的质量项。这不是疏忽，是写不进去。Dirac 质量项分解为

$$m\bar\psi\psi = m\big(\bar\psi_L\psi_R + \bar\psi_R\psi_L\big),$$

它把左手场和右手场缝合在一起。但在标准模型里左右手量子数不同：

- $\bar u_L d_L\cdots$：弱二重态乘弱单态，在 SU(2)$_L$ 下不是单态——规范变换后多出一个因子，破坏不变性；
- 超荷也对不上，例如 $\bar e_L e_R$ 的超荷是 $-(-\tfrac12) + (-1) = -\tfrac12 \neq 0$。

结论：**手征规范理论里，裸费米子质量项与规范不变性不兼容**。这是个深刻的两难：实验明明告诉我们电子有质量！出路只有一个——质量不能是"生来就有"的，必须是某个携带恰好量子数的场取得真空期望值后"补发"的。这个场就是希格斯二重态。

## 6. $\mathcal{L}_{\mathrm{Higgs}}$ 与 Yukawa：质量的总账房

### 6.1 希格斯动能项与势

$$\mathcal{L}_{\mathrm{Higgs}} = (D_\mu H)^\dagger (D^\mu H) - V(H), \qquad V(H) = -\mu^2 H^\dagger H + \lambda (H^\dagger H)^2 \quad (\mu^2, \lambda > 0).$$

$H$ 是 SU(2)$_L$ 二重态、$Y = \tfrac12$ 的复标量场。注意 $V(H)$ 里 $\mu^2$ 项的**符号是负的**——这不是笔误，而是全部剧情的开关：$H=0$ 不再是势的最小值，势的形状是著名的"墨西哥帽"。对 $H^\dagger H$ 求极小：

$$\frac{\partial V}{\partial (H^\dagger H)} = -\mu^2 + 2\lambda\, H^\dagger H = 0 \;\Longrightarrow\; \langle H^\dagger H\rangle = \frac{\mu^2}{2\lambda} \equiv \frac{v^2}{2},$$

即希格斯场在真空里取非零期望值（自发对称性破缺，见电弱对称性破缺笔记）。取幺正规范（吃掉三个 Goldstone 玻色子，它们变成 $W^\pm, Z$ 的纵向分量）：

$$\langle H\rangle = \frac{1}{\sqrt2}\begin{pmatrix}0\\ v\end{pmatrix}, \qquad H(x) = \frac{1}{\sqrt2}\begin{pmatrix}0\\ v + h(x)\end{pmatrix},$$

其中 $v = \mu/\sqrt\lambda \approx 246\ \mathrm{GeV}$（由 $\mu$ 子衰定出的费米常数 $G_F$ 决定），$h(x)$ 是可观测的**希格斯玻色子**（2012 年发现，$m_h = \sqrt{2\lambda}\,v \approx 125\ \mathrm{GeV}$）。

### 6.2 $W$、$Z$ 获得质量，光子幸存

把 $H = (0, v/\sqrt2)^T$ 代入动能项 $(D_\mu H)^\dagger(D^\mu H)$，$\partial_\mu$ 作用在常数 $v$ 上为零，只剩规范场部分。用 $T^i = \sigma^i/2$、$Y=\tfrac12$ 直接算：

$$D_\mu H = -\frac{i}{2}\frac{v}{\sqrt2}\begin{pmatrix} g(W^1_\mu - iW^2_\mu)\\ g'B_\mu - gW^3_\mu \end{pmatrix},$$

取模方（这是关键中间步骤，值得自己动手算一遍）：

$$|D_\mu H|^2 \;\supset\; \frac{v^2}{8}\Big[ g^2\big(W^1_\mu W^{1\mu} + W^2_\mu W^{2\mu}\big) + \big(gW^3_\mu - g'B_\mu\big)^2 \Big].$$

这正是自旋 1 场的质量项 $\tfrac12 M^2 A_\mu A^\mu$ 的形状。逐项读出：

**带电玻色子**：用 $W^\pm_\mu = (W^1_\mu \mp iW^2_\mu)/\sqrt2$ 重写，得 $M_W^2 W^+_\mu W^{-\mu}$，

$$\boxed{M_W = \tfrac12 g v}$$

**中性玻色子**：$(gW^3 - g'B)$ 这个组合有质量，与其正交的组合无质量。定义**弱混合角**（温伯格角）$\theta_W$：

$$\sin\theta_W \equiv \frac{g'}{\sqrt{g^2+g'^2}}, \qquad \cos\theta_W \equiv \frac{g}{\sqrt{g^2+g'^2}},$$

做正交转动：

$$Z_\mu = \cos\theta_W\, W^3_\mu - \sin\theta_W\, B_\mu, \qquad A_\mu = \sin\theta_W\, W^3_\mu + \cos\theta_W\, B_\mu,$$

则有质量的是 $Z$，无质量的是 $A$：

$$\boxed{M_Z = \tfrac12\sqrt{g^2+g'^2}\,v, \qquad M_A = 0}$$

由两式立刻得到树级关系

$$M_W = M_Z \cos\theta_W.$$

**光子为什么保持无质量？** 因为真空期望值还保留了一个未破缺的对称性。破缺前生成元有四个（$T_1,T_2,T_3,Y$）；检查哪个组合湮灭真空：$T_3\langle H\rangle = -\tfrac12\langle H\rangle$（$\sigma^3$ 作用在下分量），$Y\langle H\rangle = +\tfrac12\langle H\rangle$，所以

$$Q\,\langle H\rangle = (T_3 + Y)\langle H\rangle = 0.$$

电荷 $Q$ 仍是好对称性——这就是残余的 $\mathrm{U}(1)_{\mathrm{EM}}$，其规范玻色子（光子）不能有质量。破缺模式是 $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y \to \mathrm{U}(1)_{\mathrm{EM}}$：四个生成元破三个（$W^\pm, Z$ 各吃一单位质量），剩一个（光子）。这正是 Gell-Mann–西岛关系 $Q = T_3 + Y$ 在破缺后的兑现。

**电荷与耦合的关系**：把 $W^3, B$ 用 $Z, A$ 反解代回中性流项，含 $A_\mu$ 的部分系数恰好都是 $eQ$（用 $Q = T_3+Y$ 逐场验证），其中

$$\boxed{e = \frac{gg'}{\sqrt{g^2+g'^2}} = g\sin\theta_W = g'\cos\theta_W}$$

电磁耦合 $e$ 不是独立参数，它是 $g, g'$ 的混血儿。

### 6.3 Yukawa 项：费米子质量的唯一合法来源

第 5.3 节说裸质量项写不进去。但 $H$ 的量子数（$\mathbf{2}$，$Y=\tfrac12$）恰好能当"媒人"：$\bar Q_L$ 是 $\bar{\mathbf{2}}$（$Y=-\tfrac16$），$d_R$ 是 $\mathbf{1}$（$Y=-\tfrac13$），于是 $\bar Q_L H d_R$ 是 SU(2) 单态且超荷 $-\tfrac16+\tfrac12-\tfrac13=0$ ——规范不变！上夸克方向要用电荷共轭的二重态 $\tilde H \equiv i\sigma^2 H^*$（$Y=-\tfrac12$，其真空期望值在上分量）。全部 Yukawa 项：

$$\mathcal{L}_{\mathrm{Yukawa}} = -y_d\, \bar Q_L H\, d_R - y_u\, \bar Q_L \tilde H\, u_R - y_e\, \bar L_L H\, e_R + \mathrm{h.c.},$$

$y_f$ 是无量纲耦合常数（每代每类各一个，所以是味空间里的 $3\times3$ 矩阵）。代入 $\langle H\rangle = (0, v/\sqrt2)^T$ 和 $\langle\tilde H\rangle = (v/\sqrt2, 0)^T$：

$$-y_d \frac{v}{\sqrt2}\, \bar d_L d_R - y_u \frac{v}{\sqrt2}\, \bar u_L u_R - y_e \frac{v}{\sqrt2}\, \bar e_L e_R + \mathrm{h.c.},$$

与质量项 $-m(\bar\psi_L\psi_R + \mathrm{h.c.})$ 对比，得

$$\boxed{m_f = \frac{y_f\, v}{\sqrt2}}$$

**说人话的版本**：真空里弥漫着希格斯场的常数背景 $v$；费米子通过 Yukawa 耦合与这个背景"挂钩"，左手和右手被 $v$ 缝合起来，表现为质量。两个常见误解要纠正：

- 质量来自**希格斯场的真空期望值** $v$，不是来自希格斯**玻色子** $h(x)$ 这个粒子。2012 年发现的 $h$ 是 $v$ 之上的量子涨落，它与质量的关系是"同一张发票的两个条目"；
- 也**不是**"希格斯场像糖浆一样拖住粒子"——真空中没有摩擦，惯性质量的正确图像是左手态与右手态以频率 $m$ 互相转化（$\bar\psi_L\psi_R$ 混合两手性），粒子无法保持纯手征地匀速前进。

同时 $y_f$ 千差万别（$y_e \sim 3\times10^{-6}$，$y_t \approx 1$），标准模型对此**零解释**——味物理之谜就藏在这串数字里。夸克部分还要对角化 $3\times3$ 的 $y_u, y_d$ 矩阵，两组对角化基的 mismatch 给出 CKM 混合矩阵（3 个转角 + 1 个 CP 相位，见后续味物理笔记）。

## 7. 逐项总结：每一项 ↔ 它负责的物理

| 拉氏量中的项 | 直接产物 | 对应物理 |
|---|---|---|
| $-\tfrac14 G^2$（含 $g_s, g_s^2$ 自耦合） | 胶子传播子 + 三/四胶子顶点 | 渐近自由、禁闭、强子结构 |
| $-\tfrac14 W^2 - \tfrac14 B^2$ | $W,B$ 传播子 + 弱自耦合顶点 | 弱规范玻色子动力学、$WW\gamma/WWZ$ 顶点 |
| $\bar f i\gamma^\mu D_\mu f$ | $q\bar q g$、$ffW$、$ffZ$、$ff\gamma$ 顶点 | QCD 相互作用；$\beta$ 衰变、$\mu$ 衰变（带电流）；中性流与电磁流 |
| $\|D_\mu H\|^2$ | $M_W, M_Z$；$hWW, hZZ$ 耦合 | 弱力短程（$\sim M_W^{-1} \sim 10^{-18}$ m）；希格斯与规范玻色子的耦合 |
| $V(H) = -\mu^2H^\dagger H + \lambda(H^\dagger H)^2$ | $v \approx 246$ GeV、$m_h \approx 125$ GeV、$h^3, h^4$ 自耦合 | 电弱对称性破缺的总开关；希格斯玻色子本身 |
| $-y_f \bar f_L H f_R + \mathrm{h.c.}$ | $m_f = y_f v/\sqrt2$ | 夸克、轻子质量谱；CKM 混合与 CP 破坏 |

## 8. 参数清点与留白

数一遍标准模型的自由参数（中微子无质量的"原版"）：

| 类别 | 参数 | 个数 |
|---|---|---|
| 规范耦合 | $g_s,\ g,\ g'$ | 3 |
| 希格斯势 | $\mu^2,\ \lambda$（等价地 $v,\ m_h$） | 2 |
| 费米子质量 | 6 夸克 + 3 带电轻子的 $y_f$ | 9 |
| CKM 矩阵 | 3 转角 + 1 CP 相位 | 4 |
| 强 CP | $\theta_{\mathrm{QCD}}$ | 1 |
| **合计** | | **19** |

19 个参数全部要从实验输入，理论一个也算不出来——这既是标准模型的伟大（19 个数预言了从原子对撞机到天体物理的海量数据，且屡屡精确到小数点后好几位），也是它的局限。三个最刺眼的留白：

- **中微子有质量**（振荡实验已证实），而 $\nu_R$ 不在拉氏量里——至少要加新参数（2 个独立质量差、3 个混合角、若干相位），甚至新机制；
- **暗物质**：宇宙学要求一种不参与电磁与强作用的大质量成分，标准模型 19 个参数里没有它的位置；
- **引力**：$\mathcal{L}_{\mathrm{SM}}$ 与爱因斯坦的 $\mathcal{L}_{\mathrm{EH}}$ 至今无法在同一个量子理论里共存。

所以这一页是"迄今为止最好的物理学"，同时明摆着不是终点。

## 9. 收官：回到路线图的自测

学到这里，你应该能拿起那页著名公式，从左到右逐项说出"符号定义 + 物理职责"，并说清楚 $W/Z$ 和费米子的质量各自从哪一项来、光子为什么免费。还有一个很好的试金石：**$\mu$ 子反常磁矩 $g-2$ 为什么那么难算？** 答案是：$a_\mu = (g-2)/2$ 是 $\mu$ 子与光子顶点的高阶修正，而本章这页纸上的**每一个顶点**都能插进圈图里——QED 圈、弱作用圈（$W, Z, h$ 内线）、以及最难的强作用圈（低能 QCD 非微扰，胶子自耦合把夸克圈糊成"强子真空极化"，只能靠格点 QCD 或实验数据反推）。$g-2$ 的精确预言要求把整页拉氏量当作一台机器整体开动，它是检验"你是否真的读懂了这页纸"的终极考题（计算细节见后续辐射修正笔记）。

## 小结

- $\mathcal{L}_{\mathrm{SM}} = \mathcal{L}_{\mathrm{gauge}} + \mathcal{L}_{\mathrm{fermion}} + \mathcal{L}_{\mathrm{Higgs}} + \mathcal{L}_{\mathrm{Yukawa}}$，规范群 $\mathrm{SU}(3)_C\times\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$，电荷 $Q = T_3 + Y$。
- 费米子是手征的：左手二重态、右手单态，宇称破坏写进了粒子表。
- 非阿贝尔场强的非线性项 → 规范玻色子自耦合（三/四顶点）→ 渐近自由与禁闭。
- 协变导数按表示收税，展开即得全部费米子–规范玻色子顶点；裸质量项被规范不变性禁止。
- 希格斯势 $-\mu^2H^\dagger H + \lambda(H^\dagger H)^2$ 使 $v\approx246$ GeV；$M_W=\tfrac12gv$，$M_Z=\tfrac12\sqrt{g^2+g'^2}v$，$M_W = M_Z\cos\theta_W$，$e = g\sin\theta_W$；光子因 $Q\langle H\rangle=0$ 保持无质量。
- 费米子质量 $m_f = y_f v/\sqrt2$：来自 Yukawa 耦合 × 真空期望值，不是希格斯玻色子的"糖浆"。
- 19 个自由参数；中微子质量、暗物质、引力是三大留白。

## 自检问题

**1.** 为什么标准模型里不能写 $-m_e\bar e e$ 这样的电子质量项？请从 SU(2)$_L$ 和 U(1)$_Y$ 两方面说明。

<details markdown="1"><summary>点击显示答案</summary>

Dirac 质量项用手征分量展开为 $-m_e(\bar e_L e_R + \bar e_R e_L)$。

**SU(2)$_L$ 方面**：$e_L$ 住在二重态 $L_L$ 里，$\bar e_L$ 按 $\bar{\mathbf{2}}$ 变换；$e_R$ 是单态 $\mathbf{1}$。于是 $\bar e_L e_R$ 整体按 $\bar{\mathbf{2}}$ 变换——SU(2)$_L$ 规范变换 $U(x)$ 后多出一个因子 $U^\dagger(x)$，不是不变量。规范场的动能项与相互作用项都严格不变，唯独它不变，整理论不自洽（规范对称性破了的 Yang–Mills 理论不可重整、不可自洽量子化）。

**U(1)$_Y$ 方面**：双线性 $\bar\psi_1\psi_2$ 的超荷是 $-Y_1 + Y_2$（共轭翻号）。$\bar e_L e_R$ 的超荷为 $-(-\tfrac12) + (-1) = -\tfrac12 \neq 0$，规范变换下获得相位 $e^{-i\alpha(x)/2}$，也不不变。

出路是引入 $Y = +\tfrac12$ 的二重态 $H$：$\bar L_L H e_R$ 的超荷 $+\tfrac12+\tfrac12-1=0$、且 $\bar{\mathbf{2}}\otimes\mathbf{2}\otimes\mathbf{1}$ 含单态，两项检查都通过。$H$ 取真空期望值后，这个 Yukawa 项退化成有效的质量项 $m_e = y_e v/\sqrt2$。

</details>

**2.** 从 $|D_\mu H|^2$ 出发，补全 $M_W = gv/2$ 的推导中从二次型到质量本征态的关键步骤。

<details markdown="1"><summary>点击显示答案</summary>

幺正规范下 $H = (0, v/\sqrt2)^T$，$\partial_\mu H = 0$，所以

$$D_\mu H = -i\Big(g\frac{\sigma^i}{2}W^i_\mu + g'\frac12 B_\mu\Big)\frac{1}{\sqrt2}\begin{pmatrix}0\\v\end{pmatrix} = -\frac{iv}{2\sqrt2}\begin{pmatrix} g(W^1_\mu - iW^2_\mu)\\ g'B_\mu - gW^3_\mu \end{pmatrix},$$

其中用了 $\sigma^1(0,v)^T = (v,0)^T$、$\sigma^2(0,v)^T = (-iv,0)^T$、$\sigma^3(0,v)^T = (0,-v)^T$。复二重态取模方 $|D_\mu H|^2 = (D_\mu H)^\dagger(D^\mu H)$：

$$|D_\mu H|^2 = \frac{v^2}{8}\Big[g^2|W^1_\mu - iW^2_\mu|^2 + (gW^3_\mu - g'B_\mu)^2\Big].$$

引入带电组合 $W^\pm_\mu = (W^1_\mu \mp iW^2_\mu)/\sqrt2$，则 $|W^1 - iW^2|^2 = 2\,W^+_\mu W^{-\mu}$，于是第一项为 $\frac{g^2v^2}{4}W^+_\mu W^{-\mu}$。与 Proca 质量项 $M_W^2 W^+_\mu W^{-\mu}$ 对比（复场质量项不带 $\tfrac12$），得

$$M_W^2 = \frac{g^2v^2}{4} \;\Longrightarrow\; M_W = \frac{gv}{2}.$$

中性部分 $\frac{v^2}{8}(gW^3 - g'B)^2$：质量本征态是归一化组合 $Z_\mu = (gW^3_\mu - g'B_\mu)/\sqrt{g^2+g'^2}$，代回得 $\frac12\cdot\frac{(g^2+g'^2)v^2}{4}Z_\mu Z^\mu$，即 $M_Z = \tfrac12\sqrt{g^2+g'^2}\,v$；正交组合 $A_\mu$ 在二次型中系数为零，无质量。

</details>

**3.** 证明 $e = g\sin\theta_W$，并解释为什么光子的耦合对中微子是零。

<details markdown="1"><summary>点击显示答案</summary>

中性流相互作用来自协变导数的后两项：$\bar\psi\gamma^\mu(gT_3W^3_\mu + g'YB_\mu)\psi$。由转动定义反解：

$$W^3_\mu = \cos\theta_W Z_\mu + \sin\theta_W A_\mu, \qquad B_\mu = -\sin\theta_W Z_\mu + \cos\theta_W A_\mu.$$

含 $A_\mu$ 的系数为 $gT_3\sin\theta_W + g'Y\cos\theta_W$。代入 $\sin\theta_W = g'/\sqrt{g^2+g'^2}$、$\cos\theta_W = g/\sqrt{g^2+g'^2}$：

$$gT_3\frac{g'}{\sqrt{g^2+g'^2}} + g'Y\frac{g}{\sqrt{g^2+g'^2}} = \frac{gg'}{\sqrt{g^2+g'^2}}(T_3 + Y) = \frac{gg'}{\sqrt{g^2+g'^2}}\,Q.$$

电磁相互作用的标准形式是 $eQ\,A_\mu$，所以

$$e = \frac{gg'}{\sqrt{g^2+g'^2}} = g\sin\theta_W = g'\cos\theta_W.$$

对中微子：$\nu_L$ 有 $T_3 = +\tfrac12$、$Y = -\tfrac12$，故 $Q = 0$，与 $A_\mu$ 的耦合 $eQ = 0$——中微子不参与电磁作用。但它与 $Z$ 的耦合（正比于 $T_3 - Q\sin^2\theta_W = \tfrac12$）不为零，所以中微子仍被弱中性流"看见"——这正是 1973 年 Gargamelle 气泡室发现中性流时观测的那类过程。

</details>

**4.** 已知 $m_t \approx 173$ GeV、$v \approx 246$ GeV，估算 $y_t$；再用 $y_e/y_t$ 说明"味物理之谜"指的是什么。

<details markdown="1"><summary>点击显示答案</summary>

由 $m_f = y_f v/\sqrt2$：

$$y_t = \frac{\sqrt2\, m_t}{v} = \frac{\sqrt2 \times 173}{246} \approx 0.99 \approx 1.$$

顶夸克的 Yukawa 耦合几乎是 1——无量纲耦合"自然"量级，顶夸克质量大纯粹是因为它和希格斯耦合得满满当当。

电子这边：$m_e \approx 0.511$ MeV，

$$y_e = \frac{\sqrt2 \times 0.511\ \mathrm{MeV}}{246\ \mathrm{GeV}} \approx 2.9\times10^{-6}.$$

于是 $y_e/y_t \sim 3\times10^{-6}$。标准模型对这组数字**没有任何解释**：Yukawa 耦合是自由参数，实验测多少就是多少。为什么三代费米子的质量跨越至少 5 个数量级、且呈现近似层级结构？为什么混合角是那几个值？这一连串"为什么"就是**味物理之谜**（flavor puzzle）。它与"参数个数"问题互为表里：19 个参数里 13 个（9 个质量 + 4 个 CKM）属于 Yukawa 部门——标准模型拉氏量的大部分"任意性"都堆在这里，提示背后可能有更深层结构（味对称性、复合结构等），但目前没有实验定论。

</details>

**5.** 为什么说 $\mu$ 子 $g-2$ 的理论预言"动用了整页拉氏量"？按贡献类型列举，并指出哪一类最难。

<details markdown="1"><summary>点击显示答案</summary>

$a_\mu = (g-2)/2$ 是光子–$\mu$ 子顶点的圈图修正。Schwinger 1948 年算出的领头项 $a_\mu = \alpha/(2\pi)$ 只用一个 $ee\gamma$ 顶点，但往高阶走，本章每一项都会进圈：

- **QED 部分**：纯光子/电子圈（$\mathcal{L}_{\mathrm{fermion}}$ 中的 $eQ A_\mu$ 顶点），已算到五圈，精度极高，是 $e$（即 $g, g'$ 的混合）的检验；
- **电弱部分**：圈内跑 $W^\pm$、$Z$、$h$（来自 $|D_\mu H|^2$ 的 $hWW$、$hZZ$ 耦合与 Yukawa 顶点），被 $M_W^2$ 压低（$\sim G_F m_\mu^2$），贡献约 $10^{-9}$ 量级，正好压在实验精度边缘，不可不算；
- **强子部分**：光子先涨落成夸克对、再被胶子"染色"（强子真空极化），或夸克圈两端各挂一个光子（强子光-by-光散射）。这里用到 $\mathcal{L}_{\mathrm{gauge}}$ 的胶子自耦合与 $q\bar q g$ 顶点——而且在**低能区**，$\alpha_s$ 大、微扰论失效。

最难的正是强子部分：低能 QCD 非微扰（禁闭、渐近自由的另一面），圈积分不能解析算，只能靠 $e^+e^-\to$ 强子的实验色散积分或格点 QCD 数值计算。长期以来它是理论误差的主要来源，也是实验值（Fermilab/BNL）与理论值之间 $\sigma$ 级张力的焦点之一。所以说 $g-2$ 是把整页 $\mathcal{L}_{\mathrm{SM}}$ 当一台机器整体开动——任何新物理（超对称、轻夸克……）若有新粒子能进圈，也会在这里露马脚，这正是它作为"新物理探针"的价值。

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》第 20 章（规范理论总览）与第 21 章（自发破缺）；Chapter 20.1–20.2 的粒子内容与量子数表与本章对应。
- Schwartz《Quantum Field Theory and the Standard Model》第 29 章（标准模型拉氏量逐项展开，与本章结构几乎一一对应）及第 26–28 章（电弱理论与 QCD 背景）。
- Srednicki《Quantum Field Theory》Part III（第 86–89 讲：标准模型的规范群、费米子内容与破缺模式）。
- Zee《Quantum Field Theory in a Nutshell》Part VII（电弱统一的直觉讲法，适合第一遍建立图像）。
- Georgi《Weak Interactions and Modern Particle Theory》前几章（$V-A$ 结构与电弱唯象的经典讲义）。
