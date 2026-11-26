# 格点场论：路径积分的另一种算法

> 路线图位置：第 4 阶段（QFT 核心）· 第 9 篇（选学"非微扰算法"），在 [07 篇](07-path-integral.md)（路径积分）与 [08 篇](08-constructive-qft-triviality.md)（严格性回望）之后读。
> 前置知识：[07 篇](07-path-integral.md)的欧氏路径积分与 Wick 转动；[Yang–Mills 笔记](../stage-06-standard-model/01-yang-mills.md)的协变导数与场强；[QCD 笔记](../stage-06-standard-model/03-qcd.md)的禁闭与 Wilson 圈（本篇给出其中"格点证据"的方法来源）。
> 学习目标：理解微扰场论与格点场论是同一量子场论框架下两条相对独立、优势互补的定义与计算路线；看懂 Wilson 格点规范理论的构造（链接变量、plaquette 作用量、连续极限）；知道强耦合展开如何免费送出禁闭面积律、费米子上格为什么有 doubling 麻烦、Monte Carlo 怎么把路径积分变成统计力学问题；以及连续极限 / 无穷体积 / 统计误差这三本账怎么还。

---

## 1. 一句话总结

**量子场论要算的对象只有一个——欧氏路径积分 $Z = \int\mathcal D\phi\,e^{-S_E[\phi]}$。微扰场论把相互作用当作对自由理论的小修正，按耦合常数逐级展开；格点场论把时空离散成有限格点，把这个无穷维积分变成有限维（但巨大）的数值积分，用 Monte Carlo 直接采样。二者平行：格点原则上不需要微扰级数作中间依据，它本身就是 QFT 的一种非微扰正则化（甚至是非微扰定义）；二者互补：弱耦合区微扰论系统透明，强耦合区格点是唯一的第一性原理工具——QCD 高能散射用前者，强子谱与禁闭用后者，$g-2$ 这类精确预言则要在接口处把它们缝起来。**

全文用自然单位 $\hbar = c = 1$，全部讨论在欧氏空间进行（格点工作的前提正是 [07 篇](07-path-integral.md)的 Wick 转动）。

## 2. 两条平行路线：同一个 $Z$，两种打开方式

把作用量写成 $S = S_0 + g\,S_{\mathrm{int}}$。微扰场论在 $g$ 小时做级数展开 $A = A_0 + gA_1 + g^2A_2 + \cdots$；格点场论不做这个假设，它直接计算有限格点上的 $Z_L(a, V)$，然后外推回连续时空。逐项对照：

| 方面 | 微扰场论 | 格点场论 |
|---|---|---|
| 基本思路 | 相互作用 = 对自由理论的小修正 | 时空离散化，直接处理路径积分 |
| 展开参数 | 耦合 $g$（须小） | 不需要 $g$ 小；系统误差由格距 $a$ 控制 |
| 主要工具 | 费曼图、解析计算、重整化群 | Monte Carlo 采样、数值积分、格点重整化 |
| 主要优势 | 弱耦合下系统、透明、高精度 | 强耦合与非微扰现象唯一可行 |
| 必须处理的极限 | 紫外正规化与重整化（红外另说） | 连续极限 $a\to0$、无穷体积、统计误差 |

"平行"一词值得说精确：

- 二者**独立**研究同一批可观测量：粒子质量与能谱、两点/多点关联函数、散射与衰变量、耦合随能标的跑动、相变与临界现象——结果相互对照、互为输入。
- 格点**不是**对微扰结果的数值逼近：它的出发点是路径积分本身，与微扰级数无关。严格地说，微扰场论通常是一种近似方案，而格点场论还充当 QFT 的**非微扰正则化**——对每个格距 $a \gt 0$，理论是有限自由度的良定义对象（规范理论情形甚至是严格数学对象，见 [08 篇](08-constructive-qft-triviality.md)第 6 节），"定义理论"与"计算理论"在这里合一。
- 二者也**不互斥**：格点上同样可以做微扰展开（格点微扰论），用来校准离散化误差与设计改进作用量。

## 3. Wilson 格点规范理论：规范不变性怎么离散化

### 3.1 热身：标量场

$d$ 维超立方格点 $a\mathbb Z^d$（格距 $a$）上，场 $\phi_x$ 住格点，导数换成差分，作用量

$$S_L = a^d\sum_x\left[\frac12\sum_\mu\left(\frac{\phi_{x+\hat\mu}-\phi_x}{a}\right)^2 + \frac{m^2}{2}\phi_x^2 + \frac{\lambda}{4!}\phi_x^4\right].$$

$Z = \int\prod_x d\phi_x\,e^{-S_L}$ 是有限维积分（有限体积下），自由情形是可以精确求值的高斯积分（自检题 2 做完一个一维玩具）。动量空间天然有紫外截断：晶格动量限制在 Brillouin 区 $[-\pi/a, \pi/a]$——**格点从一开始就把"正规化"内建了**，这正是它作为非微扰正则化的含义。

### 3.2 规范自由度住在哪里：链接变量

天真地把 $A_\mu(x)$ 放在格点上做差分离散，定域规范不变性立刻丢失（差分破坏协变导数结构）。Wilson（1974）的正确做法：把规范自由度放在**链接**上——链接变量

$$U_\mu(x) \in \mathrm{SU}(N) \qquad\text{（位于 } x \to x+\hat\mu\text{ 的链接上）},$$

物理意义是平行输运：$U_\mu(x) = \mathcal P\exp\big(ig\int_x^{x+\hat\mu}A_\mu\,dx^\mu\big) \approx e^{igaA_\mu(x)}$。定域规范变换下

$$U_\mu(x) \;\longrightarrow\; \Omega(x)\,U_\mu(x)\,\Omega^\dagger(x+\hat\mu),$$

即链接变量按"两端各转一次"变换——它本来就是规范场沿链接的有限元诗（holonomy）。费米子住格点上按 $\psi_x \to \Omega(x)\psi_x$ 变换，于是 $\bar\psi_x\,U_\mu(x)\,\psi_{x+\hat\mu}$ 严格规范不变：**规范不变的离散"最近邻耦合"天然存在**，代价是抛弃了"$A_\mu$ 的差分导数"这个天真对象。

### 3.3 Plaquette 与 Wilson 作用量

最小的规范不变纯规范构造是绕 $1\times1$ 小方块（plaquette）一圈的乘积取迹：

$$U_p(x) \equiv U_\mu(x)\,U_\nu(x+\hat\mu)\,U^\dagger_\mu(x+\hat\nu)\,U^\dagger_\nu(x),$$

首尾相接，两个 $\Omega$ 全部对消，$\mathrm{Tr}\,U_p$ 规范不变（它就是最小 Wilson 圈）。Wilson 作用量

$$S_W = \beta_L \sum_p\left(1 - \frac{1}{N}\,\mathrm{Re}\,\mathrm{Tr}\,U_p\right), \qquad \beta_L \equiv \frac{2N}{g^2},$$

求和跑遍所有（非定向）plaquette。连续极限（自检题 1 推导）：代入 $U_\mu = e^{igaA_\mu}$，用 BCH 公式得 $\mathrm{Re}\,\mathrm{Tr}\,U_p = N - \frac{g^2a^4}{2}\mathrm{Tr}\,F_{\mu\nu}^2 + O(a^5)$，于是 $S_W \to \frac14\int d^4x\,F_{\mu\nu}^aF^{a\mu\nu}$——正是 Yang–Mills 作用量，离散化误差从 $O(a^2)$ 起步（可用 Symanzik 改进纲领系统地压低）。

注意记号陷阱：这里的 $\beta_L = 2N/g^2$ 与 $\beta$ 函数毫无关系，是格点文献的标准记号，$\beta_L$ **大**对应**弱**耦合。

### 3.4 观测量：Wilson 圈与禁闭判据

静态夸克–反夸克对（间距 $R$）的能量由 $R\times T$ 矩形 Wilson 圈读出：$W(R,T) = \big\langle \frac1N\mathrm{Tr}\,U_C \big\rangle \sim e^{-V(R)T}$（$T\gg R$）。**面积律** $W \sim e^{-\sigma RT}$ 对应线性势 $V(R) = \sigma R$——禁闭。这正是 [QCD 笔记](../stage-06-standard-model/03-qcd.md)第 5 节引用的格点证据的定义。

## 4. 强耦合展开：面积律几乎免费

格点最漂亮的免费午餐：在强耦合端（$g$ 大、$\beta_L$ 小）直接对 $e^{-S_W}$ 做 $\beta_L$ 的级数展开。每条链接上的群积分有严格规则

$$\int dU\,U_{ij} = 0, \qquad \int dU\,U_{ij}\,U^\dagger_{kl} = \frac{1}{N}\,\delta_{il}\delta_{jk},$$

所以展开式中只有"链接都被配对"的项幸存——对 Wilson 圈而言，领头非零项要求用 plaquette 把圈围的**最小面积**铺满：每块 plaquette 贡献因子 $\beta_L/(2N^2)$，于是

$$W(R,T) \approx \left(\frac{\beta_L}{2N^2}\right)^{RT} = e^{-\sigma a^2 RT}, \qquad \sigma = \frac{1}{a^2}\ln\frac{2N^2}{\beta_L}$$

（计数推导见自检题 3）。**强耦合下禁闭是格点规范理论的平庸性质**——这与微扰论里禁闭完全不可见形成戏剧性对照。

但天下没有免费的连续极限：渐近自由要求 $a \to 0$ 时 $g(a) \to 0$，即 $\beta_L \to \infty$——恰好走出强耦合展开的适用区。物理弦张力必须在从强耦合到弱耦合的整个渡越区存活下来；Monte Carlo（第 6 节）证实了这一点（SU(3) 在 $\beta_L \approx 6$ 附近平滑渡越，之后 $\sigma$ 按渐近自由的标度律走）。这个"强耦合端免费、连续极限要过关"的张力，正是 [08 篇](08-constructive-qft-triviality.md)里千禧年难题卡点的数值版：格点上质量间隙好证（强耦合区），难的是把它带进 $a \to 0$ 的极限。

## 5. 费米子上格：doubling 的麻烦

标量与规范场一帆风顺，费米子却踩坑。天真的对称差分离散给出自由逆传播子

$$D^{-1}(p) = \frac{i}{a}\sum_\mu \gamma_\mu \sin(ap_\mu) + m,$$

极点出现在 $\sin(ap_\mu) = 0$ 处：每个动量分量可以取 $0$ **或** $\pi/a$（Brillouin 区角落），$d=4$ 时共 $2^4 = 16$ 个极点——1 个想要的费米子加 15 个**加倍子**（doublers）。这不是笨拙而是定理：Nielsen–Ninomiya no-go 定理说，在相当一般的条件下，格点上无法构造只有一个费米子、且保持连续手征对称性的局域无相互作用 Dirac 算符。

出路举例（自检题 4 推导 doubling 与它的移除）：

- **Wilson 费米子**：加一个二阶差分项（Wilson 项），极点处的有效质量变为 $m + 2kr/a$（$k$ = 该极点位于 $\pi/a$ 的分量数）——加倍子拿到 $O(1/a)$ 的质量，连续极限下解耦。代价：$m=0$ 时手征对称性被显式破坏，给数值工作带来加法定理的麻烦；
- **现代方案**：staggered（把加倍子重新解释为"味道"）、domain-wall / overlap 费米子（满足 Ginsparg–Wilson 关系，在格点上恢复一种受控的手征对称性），各有所长，是当今主流。

## 6. Monte Carlo：把路径积分变成统计力学

### 6.1 问题与办法

费米子是 Grassmann 变量，先解析积掉：$Z = \int\prod dU\,\det M[U]\,e^{-S_W}$，$M$ 是格点 Dirac 算符。剩下的积分有多大？$32^3\times 64$ 的格子上，SU(3) 链接变量 $= 4\times 8\times 32^3\times 64 \approx 7\times10^7$ 个实积分变量——直接数值积分无望。出路是**重要性采样**：把 $e^{-S}$ 当 Boltzmann 权重，用 Markov 链（Metropolis、heatbath；含费米子行列式时用 Hybrid Monte Carlo）生成典型构型系综，观测量 = 系综平均 + 统计误差（$\propto 1/\sqrt{N_{\mathrm{cfg}}}$）。这正是 [07 篇](07-path-integral.md)"路径积分 = 统计力学配分函数"那条的兑现：格点场论与凝聚态 Monte Carlo 是同一套技术（凝聚态书的量子 Monte Carlo 一章是近亲）。

一个关键的合法性事实：零密度矢量 QCD 的费米子行列式非负（Dirac 算符的 $\gamma_5$-厄米性保证本征值共轭成对），$e^{-S_{\mathrm{eff}}}$ 是正当的概率权重；一旦加化学势（有限密度）行列式变复——**符号问题**，重要性采样崩塌，这是有限密度 QCD 至今困难的原因（凝聚态书 22 章 QMC 的符号问题是同一堵墙）。

### 6.2 三本账：连续、体积、统计（与手征）

格点数字变成物理数字要过三关外推，外加误差预算：

- **连续极限** $a \to 0$：在一系列 $a$ 上计算，按 $O(a^2)$（Wilson 作用量；改进后可更好）外推。$a$ 由某个物理量（如 $r_0$、$m_\Omega$）事后定标。代价经验标度 $\propto a^{-5\sim-7}$——把格距减半，账单涨一两个数量级（自检题 5 做量纲与规模估算）；
- **无穷体积** $V \to \infty$：有限体积效应指数小（$\sim e^{-m_\pi L}$），但要求盒子 $m_\pi L \gtrsim 4$；
- **统计误差**：随 $\sqrt{N_{\mathrm{cfg}}}$ 缓慢下降，且接近连续极限时 Markov 链出现临界慢化；
- 对含轻夸克的计算还有第四关：**手征外推**（模拟在比物理值大的 $m_q$ 上做，外推到物理点）。

战利品（回扣本讲义各处引用的"格点证据"）：纯规范与全 QCD 的强子谱（与实验吻合到百分量级）、弦张力 $\sigma$ 与线性势、强子矩阵元（衰变常数、形状因子、$g-2$ 的强子真空极化——见 [SM 拉氏量笔记](../stage-06-standard-model/04-standard-model-lagrangian.md)第 9 节）、跑动 $\alpha_s$、禁闭的面积律图像（见 [QCD 笔记](../stage-06-standard-model/03-qcd.md)）。

## 7. 两条路线的分工与接口

- **高能归微扰**：渐近自由保证 $Q^2$ 大时 $\alpha_s$ 小，DIS、DGLAP、喷注、LHC 截面（直到 NNLO）都是微扰 QCD 的地盘（路线图终点自测第 2 条）；
- **低能归格点**：禁闭、强子谱、矩阵元这些微扰级数逐阶为零或发散的对象，格点从路径积分直接给出数字；
- **接口**：格点输出（衰变常数、HVP、PDF 的矩）是微扰与唯象分析的输入；微扰论则给格点提供短距离匹配系数与改进作用量的设计（格点微扰论）。一个现代的精确预言（如 $g-2$）是两条路线在接口处缝合的产物。
- 在本讲义地图中的位置：[07 篇](07-path-integral.md)给出表述（欧氏路径积分），[08 篇](08-constructive-qft-triviality.md)回答存在性（格点作为严格对象），本篇给出算法（格点作为计算工具），[QCD 笔记](../stage-06-standard-model/03-qcd.md)消费其结果。

## 小结

- 微扰与格点是同一路径积分的两条平行路线：前者按 $g$ 展开（近似方案），后者离散化后直接数值处理（同时是 QFT 的非微扰正则化/定义）；优势互补，互不隶属，接口处缝合。
- Wilson 构造：规范自由度放链接（holonomy $U_\mu$），最小规范不变块是 plaquette；$S_W = \beta_L\sum_p(1 - \frac1N\mathrm{ReTr}U_p)$ 连续极限回到 $-\frac14F^2$；$\beta_L = 2N/g^2$。
- 强耦合展开领头阶即得面积律 $W \sim (\beta_L/2N^2)^{RT}$——禁闭在强耦合端免费，难的是带进 $a\to0$（千禧年卡点的数值版）。
- 费米子上格有 doubling（$2^d$ 极点，Nielsen–Ninomiya 定理），Wilson 项以显式手征破坏为代价移除加倍子。
- Monte Carlo = 重要性采样 + Markov 链；零密度 QCD 行列式非负使其合法，符号问题是有限密度的墙；连续极限、无穷体积、统计误差（加手征外推）是三本账。

## 自检问题

**1.** 从 $U_\mu(x) = e^{igaA_\mu(x)}$ 出发，用 BCH 公式证明 $\mathrm{Re}\,\mathrm{Tr}\,U_p = N - \frac{g^2a^4}{2}\mathrm{Tr}\,F_{\mu\nu}^2 + O(a^5)$，并完成 Wilson 作用量连续极限 $S_W \to \frac14\int F^aF^a$ 的系数核对（$\mathrm{Tr}(T^aT^b) = \frac12\delta^{ab}$）。

<details markdown="1"><summary>点击显示答案</summary>

记 $X = gaA_\mu(x)$、$Y = gaA_\nu(x+\hat\mu)$。plaquette 是两段 BCH 的嵌套：

$$U_p = e^{X}e^{Y}e^{X'}e^{Y'},\qquad X' = -gaA_\mu(x+\hat\nu),\quad Y' = -gaA_\nu(x).$$

反复用 $e^Ae^B = e^{A+B+\frac12[A,B]+\cdots}$ 合并四个指数，$O(a)$ 项成对抵消（$A_\mu(x) - A_\mu(x+\hat\nu) = -a\,\partial_\nu A_\mu + O(a^2)$ 给出微商项），领头不可消项是链接变量的对易子：

$$\log U_p = i\,ga^2\big(\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu,A_\nu]\big) + O(a^3) = i\,ga^2 F_{\mu\nu} + O(a^3).$$

于是（$\mathrm{Tr}\,F = 0$ 杀死 $O(a^2)$ 项；$F$ 厄米使 $\mathrm{Tr}\,F^2$ 为实）

$$\mathrm{Re}\,\mathrm{Tr}\,U_p = \mathrm{Re}\,\mathrm{Tr}\Big(1 + iga^2F - \tfrac{g^2a^4}{2}F^2 + \cdots\Big) = N - \frac{g^2a^4}{2}\,\mathrm{Tr}\,F_{\mu\nu}^2 + O(a^5).$$

代入 Wilson 作用量：

$$S_W = \frac{2N}{g^2}\sum_{x,\,\mu\lt\nu}\frac{g^2a^4}{2N}\,\mathrm{Tr}\,F_{\mu\nu}^2 = a^4\sum_{x,\,\mu\lt\nu}\frac12 F_{\mu\nu}^aF_{\mu\nu}^a = \frac{a^4}{4}\sum_x F_{\mu\nu}^aF^{a\mu\nu} \;\longrightarrow\; \frac14\int d^4x\,F^aF^a,$$

其中倒数第二步用了 $\sum_{\mu\lt\nu} = \frac12\sum_{\mu,\nu}$（$F_{\mu\nu}$ 反对称）把指标补全。✓ 离散化修正的领头阶是 $O(a^2)$（$a$ 的奇次幂在求和中对称相消）——这是 Symanzik 改进纲领的起点。

</details>

**2.** 一维玩具：把 $0+1$ 维欧氏自由标量（量子谐振子的欧氏版）放在 $N$ 格点、间距 $a$ 的周期链上，$S = a\sum_i\big[\frac12\big(\frac{x_{i+1}-x_i}{a}\big)^2 + \frac{m^2}{2}x_i^2\big]$。用递推求出两点函数 $G_n = \langle x_n x_0\rangle$ 的形式 $G_n \propto r^{\lvert n\rvert}$，定义有效质量 $m_E$ 并证明 $a\to0$ 时回到连续结果 $G(t) \propto e^{-m\lvert t\rvert}$。

<details markdown="1"><summary>点击显示答案</summary>

高斯积分的逆矩阵：$G_n = (K^{-1})_{n0}$，其中 $S = \frac12\sum_{ij}x_iK_{ij}x_j$，$K$ 的对角元是 $m^2a + 2/a$、最近邻元是 $-1/a$。对 $n \neq 0$，逆矩阵元满足齐次递推

$$\Big(m^2a + \frac{2}{a}\Big)G_n - \frac{1}{a}\big(G_{n+1} + G_{n-1}\big) = 0.$$

设 $G_n = A\,r^{\lvert n\rvert}$，代入得特征方程

$$r + \frac{1}{r} = 2 + m^2a^2 \;\Longrightarrow\; r = 1 + \frac{m^2a^2}{2} - ma\sqrt{1 + \frac{m^2a^2}{4}}$$

（取 $\lvert r\rvert \lt 1$ 的根，保证衰减）。定义有效质量 $r = e^{-m_E a}$，则 $\cosh(m_E a) = 1 + \frac{m^2a^2}{2}$，即

$$\sinh\frac{m_E a}{2} = \frac{ma}{2} \;\Longrightarrow\; m_E = m + O(m^3a^2).$$

连续极限：$ma \to 0$ 时 $r \to 1 - ma + \frac{(ma)^2}{2} - \cdots = e^{-ma}$，于是 $G_n \propto e^{-m\lvert n\rvert a} = e^{-m\lvert t\rvert}$——连续欧氏两点函数恢复（$n=0$ 处的源项定出归一 $A \to 1/2m$，此处略）。

这个玩具把第 6 节的"三本账"演示了一遍：离散化给出**严格可算**的对象（有限维高斯积分），连续极限是把 $m_E(a)$ 外推到 $a \to 0$ 的过程，格点修正 $O(a^2)$ 明码标价——真实格点 QCD 把这里的"递推可解"换成"Monte Carlo 可估"。

</details>

**3.** 强耦合展开：对纯规范 Wilson 作用量，利用链接积分规则证明 Wilson 圈的领头阶是 $W(R,T) \approx \big(\beta_L/2N^2\big)^{RT}$，从而读出弦张力 $\sigma = \frac{1}{a^2}\ln(2N^2/\beta_L)$。

<details markdown="1"><summary>点击显示答案</summary>

把 $e^{-S_W}$ 按 $\beta_L$ 展开（略去每块 plaquette 的常数因子 $e^{\beta_L}$，它在 $Z$ 中相消）：

$$e^{-S_W} \propto \prod_p\left[1 + \frac{\beta_L}{2N}\big(\mathrm{Tr}\,U_p + \mathrm{Tr}\,U_p^\dagger\big) + O(\beta_L^2)\right].$$

代入 $W(C) = \frac1N\langle\mathrm{Tr}\,U_C\rangle$ 并逐条链接做群积分，规则是 $\int dU\,U_{ij} = 0$、$\int dU\,U_{ij}U^\dagger_{kl} = \frac1N\delta_{il}\delta_{jk}$：**每条链接上的 $U$ 必须与同一链接上的 $U^\dagger$ 配对**，否则积分为零。

Wilson 圈自己的边界链接只携带 $U$。要让它们配对，唯一（领头）办法是从圈上每块相邻 plaquette 的展开项里取 $\mathrm{Tr}\,U_p$（它沿与圈相反的方向含 $U^\dagger$）；而这些 plaquette 新引入的内侧链接又得继续配对——于是被迫不断扩张，直到用 plaquette 把 $C$ 所围的**最小矩形面**铺满。铺满后所有链接两两配对：

- 每块 plaquette 贡献系数 $\frac{\beta_L}{2N}$；
- 每次 $U$–$U^\dagger$ 链接配对贡献 $\frac1N$：$RT$ 块 plaquette 共有 $2RT$ 条独立链接（矩形铺砌的边数），贡献 $(1/N)^{2RT}$；缩并后剩余 $N$ 次自由求和（每个顶点一个色循环）贡献 $N^{RT+1}$，再乘圈外的 $1/N$。

合起来：

$$W(R,T) \approx \frac1N\cdot N^{RT+1}\cdot\left(\frac{\beta_L}{2N}\right)^{RT}\cdot N^{-2RT} = \left(\frac{\beta_L}{2N^2}\right)^{RT}$$

（领头阶；高阶修正来自鼓包、折叠与更大面积的面）。

与 $W \sim e^{-\sigma a^2 RT}$（$RT$ 是以 $a^2$ 为单位的面积）对照，读出

$$\sigma = \frac{1}{a^2}\ln\frac{2N^2}{\beta_L}.$$

**评注**：$\beta_L \to \infty$（连续极限方向）时此式给出 $\sigma \to -\infty$，说明强耦合展开早在到达连续极限前就失效——物理弦张力靠 Monte Carlo 在渡越区"接力"过去（正文第 4 节末），这正是"格点上禁闭易证、连续极限难拿"的算术化。

</details>

**4.** 费米子 doubling：写出天真对称差分离散的动量空间逆传播子，数出 $d$ 维的极点个数；再加入 Wilson 项 $-\frac{r}{2a}\sum_\mu\bar\psi_x(\psi_{x+\hat\mu} + \psi_{x-\hat\mu} - 2\psi_x)$，证明极点质量变为 $m + 2kr/a$（$k$ 为该极点在 $\pi/a$ 方向上的分量数），加倍子因此在 $a\to0$ 时解耦，并指出代价。

<details markdown="1"><summary>点击显示答案</summary>

对称差分 $\partial_\mu\psi \to \frac{1}{2a}(\psi_{x+\hat\mu} - \psi_{x-\hat\mu})$ 在平面波 $\psi_x = e^{ip\cdot x}\chi$ 上给出本征值 $\frac{i}{a}\sin(ap_\mu)$，故

$$D^{-1}(p) = \frac{i}{a}\sum_\mu\gamma_\mu\sin(ap_\mu) + m.$$

极点（无质量情形的零点）满足 $\sin(ap_\mu) = 0$：每个分量 $p_\mu \in \{0, \pi/a\}$（Brillouin 区 $[-\pi/a, \pi/a]$ 内），$d$ 个分量独立选择，共 $2^d$ 个极点；$d=4$ 时 16 个，除 $p = 0$ 外 15 个是加倍子。各区角处的 $\gamma$ 矩阵结构可以等价于不同手征的组合——这正是连续极限想恢复手征对称性时灾难的来源，Nielsen–Ninomiya 定理将其升格为"无自由手征费米子上格"的定理。

加入 Wilson 项：其二阶差分在动量空间为

$$-\frac{r}{2a}\cdot\frac{2}{a}\big(\cos(ap_\mu) - 1\big) = \frac{r}{a}\big(1 - \cos(ap_\mu)\big),$$

逆传播子变为

$$D_W^{-1}(p) = \frac{i}{a}\sum_\mu\gamma_\mu\sin(ap_\mu) + m + \frac{r}{a}\sum_\mu\big(1 - \cos(ap_\mu)\big).$$

在区角处 $\sin = 0$，质量项读出：每个位于 $\pi/a$ 的分量贡献 $\cos = -1$，即 $2r/a$。含 $k$ 个 $\pi/a$ 分量的极点有效质量为

$$m_k = m + \frac{2kr}{a}, \qquad k = 0, 1, \dots, d.$$

$a \to 0$ 时所有 $k \geq 1$ 的加倍子质量 $\sim 1/a$ 发散，从低能谱中解耦，只留下 $k=0$ 的物理极点。

**代价**：$m = 0$ 时 Wilson 项仍在——它显式破坏了手征对称性（连续理论里 $m=0$ 的拉氏量应有 $\{\gamma_5, D\} = 0$，Wilson 项是二阶导数算符，不与 $\gamma_5$ 反对易）。后果：无保护的加法手征 Ward 恒等式、夸克质量发生加性重整化、数值上必须做手征外推。Ginsparg–Wilson 关系的现代解（domain-wall、overlap）正是为了把"解耦加倍子"与"保住手征"同时拿下。

</details>

**5.** 规模与代价的算术：SU(3) 纯规范模拟，$48^3\times 96$ 格子、$a^{-1} = 3$ GeV。估算 (a) 积分变量个数；(b) 物理盒长 $L$ 与 $m_\pi L$（取 $m_\pi = 140$ MeV）；(c) 若把 $a$ 减半且保持物理体积，按代价 $\propto a^{-6}$ 估算账单倍数。

<details markdown="1"><summary>点击显示答案</summary>

(a) 每格点 4 条链接，每条是 SU(3) 群元（$N^2 - 1 = 8$ 个实参数）：

$$N_{\mathrm{var}} = 4\times 8\times 48^3\times 96 = 32\times 110\,592\times 96 \approx 3.4\times10^8$$

个实积分变量。（含费米子时，代价主体不再是变量数而是每次求值都要做的 Dirac 算符求逆——这才是格点 QCD 贵的真正来源。）

(b) $1\ \mathrm{GeV}^{-1} = 0.1973$ fm，故 $a = \frac{1}{3}\ \mathrm{GeV}^{-1} = 0.0658$ fm，

$$L = 48a = 15.8\ \mathrm{GeV}^{-1} \approx 3.1\ \mathrm{fm}, \qquad T = 96a \approx 6.2\ \mathrm{fm},$$

$$m_\pi L = 0.140\ \mathrm{GeV}\times 15.8\ \mathrm{GeV}^{-1} \approx 2.2.$$

$m_\pi L \approx 2.2 \lt 4$——这个盒子的有限体积修正（$\sim e^{-m_\pi L} \approx 11\%$ 的指数尾巴）不可忽略，要么加大 $L$，要么把有限体积修正本身做进拟合。这就是"体积账"的日常。

(c) $a \to a/2$ 且物理体积不变：格点数 $\times 2^4 = 16$（时空各翻倍）。按经验标度代价 $\propto a^{-6}$（格点数 $\times a^{-4}$ 之外，Dirac 算符条件数恶化再贡献 $\sim a^{-2}$）：

$$\text{账单倍数} \approx 2^6 = 64.$$

即使取乐观标度 $a^{-5}$ 也是 32 倍。结论：连续极限不是"把 $a$ 调小"的旋钮，而是逐数量级攀登的成本墙——这就是为什么改进作用量（压低 $O(a^2)$ 系数）、更大体积的统计方法与几十年来专用机的历史（以及为什么强子谱能算到百分量级，而某些矩阵元仍是前沿）共同构成了这个领域的面貌。

</details>

## 参考

- Montvay & Münster《Quantum Fields on a Lattice》(Cambridge, 1994)：标准教材——Wilson 作用量、强耦合展开、费米子 doubling 与 Monte Carlo 方法的系统推导（自检题 1、3、4 的母本）。
- Rothe《Lattice Gauge Theories: An Introduction》(World Scientific, 4th ed. 2012)：更平缓的入门，面积律与强耦合展开讲得尤其清楚。
- Creutz《Quarks, Gluons and Lattices》(Cambridge, 1983)：经典小书，Monte Carlo 与渡越区物理图像的原始叙述。
- Gattringer & Lang《Quantum Chromodynamics on the Lattice》(Springer, 2010)：现代数值格点 QCD（HMC、改进费米子、外推与误差预算）的入口。
- Wilson, Phys. Rev. D 10 (1974) 2445：格点规范理论原始论文（链接变量与禁闭）。
- Nielsen & Ninomiya, Nucl. Phys. B185 (1981) 20；B193 (1981) 173：费米子 doubling 的 no-go 定理。
- Smit《Introduction to Quantum Fields on a Lattice》(Cambridge, 2002)：格点作为 QFT 非微扰定义/正则化的严格视角，与 [08 篇](08-constructive-qft-triviality.md)互参。
