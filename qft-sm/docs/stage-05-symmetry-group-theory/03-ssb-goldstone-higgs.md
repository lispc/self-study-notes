# 自发对称性破缺：Goldstone 定理与 Higgs 机制

> 路线图位置：第 5 阶段（对称性与群论补课）· 第 3 篇（[电弱统一](../stage-06-standard-model/02-electroweak-unification.md)的理论地基）。
> 前置知识：[整体对称 vs 规范对称](02-global-vs-gauge-symmetry.md)（"规范对称性是冗余"——本篇 §4 翻盘的前提）；[场的拉格朗日形式](../stage-03-relativistic-qm/02-lagrangian-field-theory.md)（诺特定理、守恒荷）；[QED](../stage-04-qft-core/05-qed.md) §2（规范不变性禁止光子质量项）；[传播子与因果性](../stage-04-qft-core/02-propagators-and-causality.md)自检第 5 题（力程 $1/m$——弱作用为什么需要重媒介）；凝聚态书[磁学](../../../condensed-matter/docs/07-magnetism.md)（Landau 序参量与铁磁体——自发破缺概念的原产地，未读可跳）。
> 学习目标：分清显式/自发、离散/连续、整体/定域三组对子各自的物理后果；会把对称破缺整理成真空流形 $G\to H$ 并数出 Goldstone 玻色子个数；能走完 Goldstone 定理的谱论证（守恒荷 + 谱分解 $\Rightarrow$ 无质量粒子）；会算墨西哥帽势的质谱，会做 Abel 模型的幺正规范与自由度账本 $2+2 = 3+1$；能解释 Goldstone 定理为何在规范理论中不适用（Elitzur 定理的直觉）；知道 $\pi$ 介子是赝 Goldstone 玻色子并会用线性 $\sigma$ 模型算它的质量。

全文用自然单位 $\hbar = c = 1$，度规 $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$。

---

## 1. 一句话总结

**对称性有两种"破"法：写进拉氏量叫显式破缺，藏进真空叫自发破缺。自发破缺里拉氏量与哈密顿量完好如初，但基态不唯一、且每个候选真空都不再对称——对称性只是被真空"选边"隐藏了。代价与礼物同时到来：每破缺一个连续整体对称的生成元，谱里就多出一个严格无质量的 Goldstone 玻色子（Goldstone 定理）——它是沿真空流形滑行、回复力为零的集体模式。真正的翻盘发生在把破缺的整体对称升级为定域规范对称之时：本该出现的 Goldstone 模式是纯规范自由度，被规范场吸收为纵向极化，规范玻色子从 $|D\mu\phi|^2$ 的真空期望值项获得质量——这就是 Higgs 机制，质量与规范一致性（可重整性）两全。标准模型里 $W/Z$ 与费米子的全部质量起源，都是这一套。**

## 2. 对称性怎么"破"：三组对子

### 2.1 显式 vs 自发

**显式破缺**：拉氏量本身不再对称。例子是[第 02 篇](02-global-vs-gauge-symmetry.md)讲过的同位旋——$u,d$ 夸克质量差与电磁相互作用把它撕开，后果是 $m_n - m_p \approx 1.3\,\mathrm{MeV}$ 与 $\pi$ 三重态的内部劈裂：可计算的修正。

**自发破缺**：拉氏量严格对称，但能量最低的态不唯一、且单个真空不对称。全部标量势 $V(\phi)$ 满足 $V(g\phi) = V(\phi)$（$g$ 为群元），于是极小点成群地出现：群作用把一个极小搬到另一个。体系必须"住在"其中一个里——**选择真空就是选择方向，对称性从此隐藏**（hidden symmetry）。

精确的说法用守恒荷：$Q\rvert\Omega\rangle \neq \rvert\Omega\rangle$，更准确地 $\langle\Omega\rvert[Q, \varphi]\rvert\Omega\rangle \neq 0$（对称变换仍在，只是真空不再被它保持）。有限体积里体系可在诸真空间隧穿，热力学极限（$V\to\infty$）下隧穿振幅指数熄灭——不同真空属于不同的超选择扇区，叠加它们不属于这个理论。**对称性没有死，它被藏进了简并真空的集合。**

### 2.2 离散 vs 连续：先看没有 Goldstone 的情形

实标量双井势 $V = \frac{\lambda}{4}(\varphi^2 - v^2)^2$：两个极小 $\varphi = \pm v$，选一个，$\langle\varphi\rangle = v \neq 0$ 破坏 $\mathbb Z_2$。涨落 $\varphi = v + h$ 有质量 $m_h^2 = V''(v) = 2\lambda v^2$，谱里**没有**无质量模式——离散破缺的真空流形是孤立点集，没有可以"滑行"的连续方向。这个对照反衬出连续对称的本质区别。

### 2.3 连续主角：墨西哥帽

复标量场加整体 U(1)（$\varphi \to e^{i\alpha}\varphi$）：

$$V(\varphi) = -\mu^2\lvert\varphi\rvert^2 + \lambda\lvert\varphi\rvert^4, \qquad \mu^2, \lambda > 0,$$

极小在圆 $\lvert\varphi\rvert = v/\sqrt2$ 上（$v = \mu/\sqrt\lambda$），真空流形是圆周 $S^1$。参数化涨落：

$$\varphi(x) = \frac{v + h(x) + i\,\pi(x)}{\sqrt2}\qquad\text{（或极坐标 } \varphi = \tfrac{v+h}{\sqrt2}e^{i\pi/v}\text{），}$$

$h$ 是径向模、$\pi$ 是沿谷底的角向模。势的展开（完整计算自检第 1 题）给

$$m_h^2 = 2\lambda v^2 = 2\mu^2, \qquad m_\pi^2 = 0,$$

且不出现 $h\pi$ 混合。图像一目了然：径向被势墙束缚（有质量），角向沿等势的谷底滑行——**回复力为零，这就是 Goldstone 玻色子**。

### 2.4 凝聚态原产地：序参量语言

自发破缺是凝聚态物理出口的概念：铁磁体（$\langle\vec M\rangle \neq 0$ 破坏自旋旋转）、晶体（点阵破坏连续平移）、超流（凝聚体波函数取定相位破坏 U(1)）。Landau 范式把"对称性 + 序参量"当作物态分类的总纲——见凝聚态书[磁学](../../../condensed-matter/docs/07-magnetism.md)一章。量子场论学的正是这套语言的相对论版：序参量 = 场的真空期望值，激发谱 = 涨落。对应表：

| 体系 | 破缺 | 序参量 | 无质量模式 |
| --- | --- | --- | --- |
| 铁磁体 | $\mathrm{SO(3)}\to$ 无 | $\langle\vec M\rangle$ | 磁振子（见 §3.4 的计数修正） |
| 晶体 | 平移 $\to$ 点阵 | 密度波矢 | 声学声子 $\times 3$ |
| 超流 $^4\mathrm{He}$ | $\mathrm{U(1)}\to$ 无 | 凝聚相位 | 声子 $\times 1$ |
| 本篇 $\varphi^4$ | $\mathrm{U(1)}\to$ 无 | $\langle\varphi\rangle$ | $\pi \times 1$ |

## 3. Goldstone 定理

### 3.1 陈述与计数

**定理（相对论场论版）**：连续整体对称群 $G$ 自发破缺到 $H$（$H$ = 保持真空的子群，真空流形为 $G/H$），则理论谱中恰有 $\dim G - \dim H$ 个无质量标量粒子（Goldstone 玻色子），各自对应一个被破缺的生成元——真空流形的切坐标。

计数先于证明走三例（自检第 4 题逐个验证）：

| 破缺链 | $\dim G - \dim H$ | Goldstone 的现实身份 |
| --- | --- | --- |
| $\mathrm{SU(2)_L\times U(1)_Y} \to \mathrm{U(1)_{em}}$ | $4 - 1 = 3$ | 被规范场吃掉（§4，电弱正餐见[第 6 阶段第 2 篇](../stage-06-standard-model/02-electroweak-unification.md)） |
| 手征 $\mathrm{SU(2)\times SU(2)} \to \mathrm{SU(2)}$ | $6 - 3 = 3$ | $\pi^\pm, \pi^0$（§3.5） |
| $\mathrm{SU(5)} \to \mathrm{SU(3)\times SU(2)\times U(1)}$ | $24 - 12 = 12$ | 大统一理论里被 12 个重规范玻色子吃掉 |

### 3.2 谱论证：定理的证明

量子证明的核心是**守恒荷夹在真空中间必有无质量态搭桥**。分四步：

**第 1 步（破缺的精确含义）**：连续对称给出守恒荷 $Q = \int d^3x\,J^0$（诺特定理，[第 3 阶段第 2 篇](../stage-03-relativistic-qm/02-lagrangian-field-theory.md)）。自发破缺即存在某个场 $\varphi$ 使

$$\langle\Omega\rvert[Q, \varphi]\rvert\Omega\rangle \neq 0$$

（墨西哥帽里取 $\varphi$ 本身：$[Q,\varphi] = i\varphi$ 的虚部，期望值 $\propto v$）。

**第 2 步（时间无关性）**：电荷守恒 $\dot Q = 0$，故 $F(t) \equiv \langle\Omega\rvert[Q, \varphi]\rvert\Omega\rangle$ 是**非零常数**，与 $t$ 无关。

**第 3 步（谱分解）**：把 $Q$ 写开 $Q = \int d^3x\,J^0(t,\vec x)$，在 $[J^0, \varphi]$ 中间插入完备基。平移不变性把每个矩阵元带上相位：

$$\langle\Omega\rvert J^0(t, \vec x)\rvert n\rangle = e^{-iE_n t + i\vec p_n\cdot\vec x}\;\langle\Omega\rvert J^0(0)\rvert n\rangle,$$

对 $\vec x$ 积分给出 $(2\pi)^3\delta^3(\vec p_n)$——**只有零动量的态有贡献**。

**第 4 步（逼出零能量）**：于是 $F(t)$ 是零动量态的叠加，各项携带 $e^{-iE_n t}$。一个由离散频率构成的级数要等于与 $t$ 无关的非零常数，唯一出路：**谱里存在 $E_n = 0$ 的零动量态**。零动量而零能量 = 无质量粒子（$E = \sqrt{p^2 + m^2}$ 在 $p = 0$ 处给 $E = 0$ 当且仅当 $m = 0$）。$\blacksquare$

证明里 Lorentz 不变性藏在"能量谱 $E_n(\vec p) = \sqrt{p^2 + m^2}$"一步；非相对论系统没有这条，计数可以改变（§3.4）。

### 3.3 经典影子：几何版本

不用量子化也能看到定理的影子：势在对称群下不变 $V(g\varphi) = V(\varphi)$，沿群轨道方向（真空流形切向）$V$ 恒定——一阶导为零、二阶导也为零，海森矩阵多出零本征值。量子证明强于经典论证之处：它保证量子涨落不把这个零模"涨"掉（$d \ge 3$ 时成立；$d \le 2$ 时连续对称的自发破缺被 Goldstone 模自身的红外涨落抹平——Mermin–Wagner/Coleman 定理，二维磁体没有长程序的原因）。

### 3.4 非相对论的修正：铁磁体只有一支磁振子

凝聚态书里的计数对不上 $\dim G - \dim H$：铁磁体 $\mathrm{SO(3)}$ 全破缺（3 个生成元），磁振子却只有**一支**（且色散是二次型 $\omega \propto k^2$）；反铁磁体有两支线性磁振子。原因：相对论定理用了 Lorentz；非相对论系统的正确计数由对易子期望值 $\langle[Q_i, Q_j]\rangle$ 是否为零分流（Watanabe–Brauner，2011）——铁磁体的破缺荷互不对易（$[Q_i,Q_j] = i\epsilon_{ijk}Q_k$ 的真空期望非零），三个"槽位"挤进一支二次型模式；反铁磁体对易子期望为零，回到线性型、但计数仍受修正。细节属凝聚态（磁振子与自旋波见[磁学](../../../condensed-matter/docs/07-magnetism.md)），记住分界即可：**相对论场论 = 线性色散、严格每生成元一个；非相对论允许"批发"。**

### 3.5 赝 Goldstone：$\pi$ 介子为什么轻而不无

QCD 在 $m_u = m_d = 0$ 的极限下有严格的手征对称 $\mathrm{SU(2)_L\times SU(2)_R}$（轻夸克质量项 $\bar q_L M q_R + \mathrm{h.c.}$ 不再对角变换），它在真空上自发破缺到对角子群 $\mathrm{SU(2)}_V$——按定理应配发 3 个 Goldstone。现实里 $m_u, m_d \approx$ 几 MeV **显式**破坏手征对称：帽底不再严格平坦，谷底"晃"出小质量——

$$m_{\pi^0} \approx 135\,\mathrm{MeV}, \quad m_{\pi^\pm} \approx 140\,\mathrm{MeV}\qquad\text{vs}\qquad m_p \approx 938\,\mathrm{MeV}.$$

轻（比质子轻一个量级）而不无——这正是"近似对称 + 自发破缺 + 微小显式破缺"的指纹：**赝 Goldstone 玻色子**。定量关系（Gell-Mann–Oakes–Renner）$m_\pi^2 f_\pi^2 = -(m_u + m_d)\langle\bar q q\rangle$ 说的是"显式破缺越小、赝 Goldstone 越轻"；用线性 $\sigma$ 模型可以把这个 $m_\pi^2 \propto$（显式破缺）算干净（自检第 5 题）。

## 4. Higgs 机制：定域化的翻盘

### 4.1 为什么必须走这条奇怪的路

把 §2.3 的整体 U(1) 升级为定域规范对称（QED 的构造方式，[第 4 阶段第 5 篇](../stage-04-qft-core/05-qed.md) §2）。三步死局与一条活路：

- **质量项被禁**：$m^2 A_\mu A^\mu$ 在 $A_\mu \to A_\mu + \partial_\mu\alpha$ 下不变性破坏——规范不变性强制矢量玻色子无质量（那是光子的处境）。
- **但弱媒介必须重**：力程 $1/m$（[传播子篇](../stage-04-qft-core/02-propagators-and-causality.md)自检第 5 题）——$m_W \approx 80\,\mathrm{GeV}$ 对应 $0.0025\,\mathrm{fm}$，弱作用的短程性要求重的媒介。
- **硬加质量项的代价**：破坏 Ward 恒等式 → 高能截面失控（幺正性坏）→ 有效耦合带负质量量纲 → 不可重整（第 06 篇 Wilson 判据）。
- **活路**：质量不写进拉氏量，而从真空期望值里"长"出来——规范不变性毫发无损，质量分文不少。

### 4.2 Abel 模型：完整演算

$$\mathcal L = \lvert D_\mu\varphi\rvert^2 - \Big(-\mu^2\lvert\varphi\rvert^2 + \lambda\lvert\varphi\rvert^4\Big) - \tfrac14 F_{\mu\nu}F^{\mu\nu},\qquad D_\mu = \partial_\mu - igA_\mu.$$

按 $\varphi = \frac{v+h}{\sqrt2}e^{i\pi/v}$ 展开（$v = \mu/\sqrt\lambda$），动能项里出现**混合项** $g\,v\,A^\mu\partial_\mu\pi$——Goldstone 与规范场不再是可以分开谈论的粒子。定域规范变换 $\varphi\to e^{i\alpha(x)}\varphi$、$A_\mu\to A_\mu + \frac1g\partial_\mu\alpha$ 恰好能动 $\pi$：取 $\alpha = -\pi/v$（**幺正规范**）把相位场整体消去，$\varphi = \frac{v+h}{\sqrt2}$，代入：

$$\lvert D_\mu\varphi\rvert^2 = \frac12(\partial h)^2 + \frac{g^2v^2}{2}A_\mu A^\mu + \big(g^2 v\big)h\,A_\mu A^\mu + \cdots$$

读出：**规范玻色子获得质量 $m_A = gv$**（来自真空项，不是质量项！），$h$ 仍是 $m_h = \sqrt{2}\,\mu$ 的普通标量，$\pi$ 从谱中消失。规范不变性从头到尾成立——拉氏量没有任何一处"被破坏"。

（幺正规范不是唯一选择：$R_\xi$ 规范保留 $\pi$ 型场与相应鬼场以换取良好的大动量传播子行为——幺正规范里 $\pi$ 消失但规范传播子分子带 $k_\mu k_\nu/m^2$ 增长项，高能计算用 $R_\xi$ 更顺手。与[路径积分篇](../stage-04-qft-core/07-path-integral.md) §8 的规范固定一脉相承。）

### 4.3 自由度账本：$\pi$ 去哪了

它没有消失，它**变成了纵向极化**。记账：

$$\underbrace{\text{无质量矢量 } 2}_{A_\mu} + \underbrace{\text{复标量 } 2}_{h, \pi} = 4 \quad=\quad \underbrace{\text{有质量矢量 } 3}_{A_\mu\ \text{(吃了 }\pi)} + \underbrace{\text{实标量 } 1}_{h}.$$

直观：混合项 $gv\,A\cdot\partial\pi$ 说"$A$ 与 $\partial\pi$ 在同一条极化线上跳舞"；幺正规范用规范自由度把 $\pi$ 换成 $A$ 的纵向分量（Stückelberg 图像：$A_L \sim \frac1m\partial\alpha$）。**守恒的是自由度总数，不是场的名单**——Higgs 机制的全部"魔术"就这一行账。

### 4.4 与 Goldstone 定理不矛盾：Elitzur

定理的证明有一个前提：$Q$ 是**作用在物理希尔伯特空间上的对称**（态与算符都是规范不变的物理对象）。规范"对称性"不是这种东西——它是冗余描述（[第 02 篇](02-global-vs-gauge-symmetry.md)的全部主题）。**Elitzur 定理**：定域规范对称不可能自发破缺——规范不变算符的真空期望值自动规范不变，谈不上"选方向"；看起来"破缺"的只是某个规范固定后的表述。所以 $\pi$ 的消失不是与定理打架，而是定理根本管不到这里：$\pi$ 是规范坐标，从来不是物理谱的成员。教科书那句"$\mathrm{SU(2)\times U(1)}$ 自发破缺到 $\mathrm{U(1)}$"是速记，严格说的是"标量场的规范轨道在势谷底选了一个代表，未破缺方向 $T\langle\phi\rangle = 0$ 的规范场保持无质量"。

### 4.5 非阿贝尔一般公式

标量多重态 $\phi$（真空值 $\langle\phi\rangle = \frac{1}{\sqrt2}\vec v$）+ 规范群 $G$：幺正规范后动能项给质量矩阵

$$\mathcal L \supset \frac12\,M^2_{ab}\,A^a_\mu A^{b\mu},\qquad M^2_{ab} = \frac{g^2}{2}\;\vec v^{\,T} T_a T_b\;\vec v,$$

结构判据干净利落：$T_a\langle\phi\rangle = 0$（生成元湮灭真空）$\iff$ $a$ 属于未破缺子群 $H$ $\iff$ $M^2_{ab}$ 的第 $a$ 行列为零——**未破缺方向的规范玻色子保持无质量，破缺方向的吃掉对应 Goldstone 变重**。电弱：$\mathrm{SU(2)_L\times U(1)_Y}$ 四个规范场，$\langle H\rangle$ 使 $T_3 + Y$ 幸存（光子无质量），$W^\pm$ 与 $Z$ 吃掉 3 个 Goldstone 变重——实算（质量谱、$\rho$ 参数）见[电弱统一](../stage-06-standard-model/02-electroweak-unification.md)；大统一 SU(5) 的版本给 12 个超重 $X/Y$ 玻色子。

### 4.6 历史与正名

机制的谱系：Anderson（1962）在超导体里看到"等离激元获得能隙而不破坏规范结构"的雏形；1964 年三篇论文（Englert–Brout、Higgs、Guralnik–Hagen–Kibble）确立相对论版；Kibble（1967）推广到非阿贝尔——同年 Weinberg 与 Salam 把它装进 $\mathrm{SU(2)\times U(1)}$；'t Hooft（1971）证明自发破缺的规范理论可重整，理论就此立足；2012 年 7 月 4 日 CERN 宣布发现希格斯玻色子（$m_h \approx 125\,\mathrm{GeV}$），2013 年 Nobel 物理学奖授 Englert 与 Higgs。

两个常见误读的正名：其一，"希格斯场给粒子质量"不是糖浆式粘滞——质量 $=$ 耦合常数 $\times$ 真空期望值（规范玻色子：$m = gv$ 的公式一眼看穿；费米子：Yukawa 耦合，第 6 阶段第 2 篇），汤川耦合为零的粒子（如中微子在最小 SM 里）依旧无质量。其二，**希格斯玻色子 $\neq$ 希格斯场**：$h$ 只是径向模的量子（真空圆上的"半径涨落"），2012 年看到的是它；弥漫全空间、取值 $v/ \sqrt2 \approx 174\,\mathrm{GeV}$ 的是场本身——背景而非粒子。

## 5. 小结

| 对子 | 什么被破 | 后果 |
| --- | --- | --- |
| 显式 / 自发 | 拉氏量 / 真空 | 可计算修正 / 隐藏对称 + 简并真空 |
| 离散 / 连续 | —— | 无 Goldstone / 每个破缺生成元一个无质量模 |
| 整体连续 / 定域化 | 物理对称 / 冗余 | Goldstone 玻色子真实存在 / 被吃成纵向极化，规范玻色子获质量 |

要点回顾：

- 自发破缺 = 拉氏量对称 + 真空选边：$Q\rvert\Omega\rangle \neq \rvert\Omega\rangle$，对称性藏进超选择扇区；
- Goldstone 定理（谱论证）：守恒荷的非零真空矩阵元强迫谱中出现无质量粒子，个数 = $\dim G - \dim H$；
- 非相对论系统计数可打折（铁磁 3→1，对易子期望值分流）——相对论线性、非相对论可批发；
- 显式小破缺把 Goldstone 变赝 Goldstone：$\pi$ 介子 $m_\pi^2 \propto m_q$；
- Higgs 机制：质量从 $\lvert D\phi\rvert^2$ 的真空项长出，$m_A = gv$；自由度账本 $2+2 = 3+1$；Elitzur：规范对称不可破，$\pi$ 是坐标不是粒子；
- 质量矩阵 $M^2_{ab} = \frac{g^2}{2}v^T T_aT_b v$：湮灭真空的生成元免费，破缺的变重。

## 自检问题

**1.** 对墨西哥帽势 $V = -\mu^2\lvert\varphi\rvert^2 + \lambda\lvert\varphi\rvert^4$ 完成质谱计算：求真空位置 $v$，按 $\varphi = \frac{v+h+i\pi}{\sqrt2}$ 展开到二次阶，证明 $m_h^2 = 2\lambda v^2$、$m_\pi^2 = 0$、且无 $h\pi$ 混合项。

<details markdown="1"><summary>点击显示答案</summary>

**真空**：$\lvert\varphi\rvert = r$ 处 $V(r) = -\mu^2 r^2 + \lambda r^4$，$\frac{dV}{dr} = -2\mu^2 r + 4\lambda r^3 = 0$ 给 $r = 0$（极大）或 $r^2 = \mu^2/2\lambda$。取 $\varphi = v/\sqrt2$（圆上任意一点，对称性等价），$v = \mu/\sqrt\lambda$，且 $\mu^2 = \lambda v^2$。

**展开**：$\lvert\varphi\rvert^2 = \frac{(v+h)^2 + \pi^2}{2} = \frac{v^2}{2} + \frac{1}{2}\big(2vh + h^2 + \pi^2\big)$。记 $X \equiv 2vh + h^2 + \pi^2$，则

$$V = -\frac{\mu^2}{2}(v^2 + X) + \frac{\lambda}{4}(v^2 + X)^2 = \mathrm{const} + \frac14\Big(-2\mu^2 + 2\lambda v^2\Big)X + \frac{\lambda}{4}X^2.$$

一次项系数 $-\mu^2 + \lambda v^2 = 0$（真空条件），所以

$$V = \mathrm{const} + \frac{\lambda}{4}\big(2vh + h^2 + \pi^2\big)^2 \supset \lambda v^2 h^2.$$

**读谱**：$V$ 的二次项只有 $h^2$（$\pi^2$ 与交叉项全部乘在带 $2vh$ 的因子后面，至少三次），对照 $\frac12 m^2\phi^2$：

$$m_h^2 = 2\lambda v^2 = 2\mu^2,\qquad m_\pi^2 = 0,\qquad (\text{无 } h\pi\text{ 混合}).$$

$\pi$ 无质量的根源在最后一步现形：它只以 $h^2 + \pi^2$ 组合出现在括号内，而括号整体被平方后乘 $\lambda$——真空条件恰把一次项（唯一能给 $\pi^2$ 的通道）消成零。**U(1) 把谷底方向整体保护成等势，零回复力是群论的必然**，不是参数巧合。

</details>

**2.** 补全 Goldstone 定理谱论证的三个关键步骤：（i）证明平移不变性给出 $\langle\Omega\rvert J^0(t,\vec x)\rvert n\rangle = e^{-iE_nt + i\vec p_n\cdot\vec x}\langle\Omega\rvert J^0(0)\rvert n\rangle$；（ii）说明为什么 $\int d^3x$ 积分只留下零动量态；（iii）严格论证"时间无关的非零 $F(t)$ 强迫 $E_n = 0$ 的态存在"。最后回答：证明在哪一步对规范理论失效。

<details markdown="1"><summary>点击显示答案</summary>

**（i）** 平移算符 $P^\mu$ 作用于态与算符：$J^0(t,\vec x) = e^{iP\cdot x}J^0(0)e^{-iP\cdot x}$（$x = (t,\vec x)$，约定 $P\cdot x = E t - \vec p\cdot\vec x$ 的方向因子）。于是

$$\langle\Omega\rvert J^0(t,\vec x)\rvert n\rangle = \langle\Omega\rvert e^{i\hat Px}J^0(0)e^{-i\hat Px}\rvert n\rangle = e^{i p_\Omega\cdot x}\langle\Omega\rvert J^0(0)\rvert n\rangle e^{-ip_n\cdot x} = e^{-iE_n t + i\vec p_n\cdot\vec x}\,\langle\Omega\rvert J^0(0)\rvert n\rangle,$$

（用了真空动量 $p_\Omega = 0$，$P^\mu\rvert n\rangle = p_n^\mu\rvert n\rangle$）。

**（ii）** $Q(t) = \int d^3x\,J^0(t,\vec x)$ 夹进谱分解后，每个中间态携带空间相位 $e^{i\vec p_n\cdot\vec x}$，$\int d^3x\;e^{i\vec p_n\cdot\vec x} = (2\pi)^3\delta^3(\vec p_n)$——只保留 $\vec p_n = 0$ 的态。这是守恒荷"空间积分"的普遍效应：它看不见动量。

**（iii）** 第（ii）步后 $F(t) = \sum_{n,\,\vec p_n = 0}\big[e^{-iE_nt}c_n - e^{+iE_nt}c_n^*\big]$（$c_n \equiv \langle\Omega\rvert J^0\rvert n\rangle\langle n\rvert\varphi\rvert\Omega\rangle$ 的简写），是离散频率的级数。若所有 $E_n > 0$：各项随 $t$ 振荡，级数（作为分布）只能叠加出振荡或零——不可能叠加出非零常数（频率 $\neq 0$ 的项无一处贡献常数分量；平均值为零）。而 $F(t) \equiv \langle[Q,\varphi]\rangle$ 由电荷守恒保证是非零常数。矛盾的唯一出口：**存在 $E_n = 0$ 的零动量态**，其 $e^{-iE_nt} = 1$ 正好供应常数。零动量 + 零能量 $\Rightarrow m_n = 0$。$\blacksquare$

**规范理论何处失效**：第 1 步。$Q$ 必须是作用在物理希尔伯特空间上的良定义对称——而规范荷是冗余的标签（生成"变换"把态映射到同一物理态的不同描述，第 02 篇），物理态的规范不变算符矩阵元自动规范不变，$\langle[Q,\varphi]\rangle \ne 0$ 这一步对规范不变的可观测量根本取不到。Elitzur 定理是这句话的定理化。规范固定后"看起来"破缺的 $\langle\varphi\rangle = v$ 是描述依赖的记账，不进 $F(t)$ 的论证。

</details>

**3.** 重做 Abel 模型的 Higgs 机制：（i）从 $\varphi = \frac{v+h}{\sqrt2}e^{i\pi/v}$ 的展开式里显式找出混合项 $gv\,A^\mu\partial_\mu\pi$；（ii）验证幺正规范 $\alpha = -\pi/v$ 把它消去并给出 $m_A = gv$；（iii）写出自用度账本 $2 + 2 = 3 + 1$，并说明为什么说"$\pi$ 变成了纵向极化"。

<details markdown="1"><summary>点击显示答案</summary>

**（i）** $D_\mu\varphi = \frac{e^{i\pi/v}}{\sqrt2}\Big[\partial_\mu h + i\,\frac{(v+h)}{v}\,\partial_\mu\pi - ig(v+h)A_\mu\Big]$，取模方（相位模长为 1）：

$$\lvert D\varphi\rvert^2 = \frac12\big(\partial h\big)^2 + \frac12(v+h)^2\Big(\frac{\partial_\mu\pi}{v} - gA_\mu\Big)^2.$$

展开第二项：$\frac{1}{2}(\partial\pi)^2 - gv\,A^\mu\partial_\mu\pi + \frac{g^2v^2}{2}A^2 + \cdots$——**混合项** $-gv\,A^\mu\partial_\mu\pi$ 亮出真身：$A$ 与 $\partial\pi$ 以固定组合 $\partial_\mu\pi/v - gA_\mu$ 出现，两者不再是可以分开谈论的独立激发。

**（ii）** 规范变换下 $\big(\partial_\mu\pi - gA_\mu\big)$ 与 $e^{i\pi/v}$ 的组合不变（$D\varphi$ 协变）。取 $\alpha(x) = -\pi(x)/v$：$\varphi \to \frac{v+h}{\sqrt2}$（相位消失），$A_\mu \to A_\mu + \frac1g\partial_\mu\alpha$ 把纵向部分吸收进自身。新规范下

$$\lvert D\varphi\rvert^2 = \frac12(\partial h)^2 + \frac{g^2v^2}{2}A^2 + g^2vh\,A^2 + \frac{g^2}{2}h^2A^2,\qquad m_A^2 = g^2v^2.$$

$\pi$ 从拉氏量中消失；$hA^2$ 型相互作用留在谱里（希格斯玻色子对规范玻色子的耦合 $\propto$ 质量——实验上正是靠这类耦合看到 $h$）。

**（iii）** 无质量 U(1) 规范场两个横极化 + 复标量两个实分量 = 4；破缺后：有质量矢量三个极化 + 实标量 $h$ 一个 = 4。"吃掉"的机制语言版本：混合项在动量空间是 $A_\mu p^\mu\pi$ 型（"导数耦合"），把 $A$ 的传播本征态改组——其中沿 $p^\mu$ 方向的纵向本征态以 $\partial\pi$ 为原料（Stückelberg 恒等式：有质量矢量的纵向分量 $A_L \sim \frac1{m_A}\partial(\text{相位})$）。幺正规范只是把这个组合里的 $\pi$ 显式代入消掉。**账本两侧都是 4：Higgs 机制是自由度的重新洗牌，不是凭空造质量。**

</details>

**4.** 对三条破缺链逐一验证 Goldstone 计数与质量矩阵判据：（i）手征 $\mathrm{SU(2)\times SU(2)}\to\mathrm{SU(2)}$ 给 3 个 $\pi$；（ii）$\mathrm{SU(2)_L\times U(1)_Y}\to\mathrm{U(1)_{em}}$ 给 3 个被吃的模式；（iii）$\mathrm{SU(5)}\to\mathrm{SU(3)\times SU(2)\times U(1)}$ 给 12 个。并用 $M^2_{ab} = \frac{g^2}{2}v^T T_aT_b v$ 证明"$T_a\langle\phi\rangle = 0\iff$ 第 $a$ 行列为零"。

<details markdown="1"><summary>点击显示答案</summary>

**计数**：（i）$\dim\mathrm{SU(2)\times SU(2)} = 6$，$\dim\mathrm{SU(2)} = 3$，破缺生成元 $6 - 3 = 3$——$\pi^+, \pi^0, \pi^-$（§3.5 的赝 Goldstone）。（ii）$\dim\mathrm{SU(2)\times U(1)} = 3 + 1 = 4$，$\dim\mathrm{U(1)_{em}} = 1$，破缺 $3$——被 $W^\pm, Z$ 吃掉；光子沿幸存方向 $Q = T_3 + Y$ 无质量。（iii）$\dim\mathrm{SU(5)} = 5^2 - 1 = 24$，$\dim\big(\mathrm{SU(3)\times SU(2)\times U(1)}\big) = 8 + 3 + 1 = 12$，破缺 $12$——12 个超重规范玻色子（大统一理论标志性预言，质子衰变的媒介）。

**判据**：质量矩阵可写成 $M^2_{ab} = g^2\big(T_a\langle\phi\rangle\big)^\dagger\big(T_b\langle\phi\rangle\big)$（把 $\frac{1}{\sqrt2}$ 并入 $\vec v$ 的约定差一个因子，结构不变——它是两个矢量的内积）。

- 若 $T_a\langle\phi\rangle = 0$：对任意 $b$，$M^2_{ab} = g^2\big(T_a\langle\phi\rangle\big)^\dagger\big(T_b\langle\phi\rangle\big) = 0$，第 $a$ 行全零；厄米性给第 $a$ 列也全零。该规范场无质量。
- 若 $T_a\langle\phi\rangle \neq 0$：对角元 $M^2_{aa} = g^2\lVert T_a\langle\phi\rangle\rVert^2 > 0$，该方向必获得质量（与谁混合只改本征值分布，不改变"有质量"的结论——正定子块）。

所以"生成元湮灭真空 $\iff$ 规范场无质量"是内积结构的直接推论，与具体群无关。电弱里 $\langle H\rangle = \frac1{\sqrt2}(0, v)^T$：$T_3\langle H\rangle + Y\langle H\rangle = 0$（光子方向幸存），而 $T_1\langle H\rangle, T_2\langle H\rangle \ne 0$、$T_3 - Y$ 组合也不湮灭——$W^\pm$ 与 $Z$ 变重（实算见电弱篇 §5）。

</details>

**5.** 线性 $\sigma$ 模型：取 $V = \lambda\big(\sigma^2 + \vec\pi^{\,2} - v^2\big)^2 - \varepsilon\sigma$（$\varepsilon > 0$ 小）。求新的真空 $\langle\sigma\rangle = f$，证明 $m_\pi^2 = \varepsilon/f$ 且 $m_\pi^2 \to 0$（$\varepsilon\to0$）、$m_\sigma^2 \approx 8\lambda v^2$，并解释它如何模拟"$m_u, m_d$ 显式破缺手征对称给 $\pi$ 质量"。

<details markdown="1"><summary>点击显示答案</summary>

**真空**：对 $\sigma$ 求极小（$\pi = 0$ 处，$\varepsilon\sigma$ 偏置了符号选择）：

$$\frac{\partial V}{\partial\sigma} = 4\lambda\sigma\big(\sigma^2 + \vec\pi^{\,2} - v^2\big) - \varepsilon = 0\;\Big|_{\pi=0}\;\Longrightarrow\;4\lambda f\,(f^2 - v^2) = \varepsilon\;\Longrightarrow\;f^2 - v^2 = \frac{\varepsilon}{4\lambda f} > 0.$$

$\varepsilon = 0$ 时回到 $f = v$（简并圆上任一点）；$\varepsilon > 0$ 把帽底压出一个倾斜，真空从圆上一点滑到 $f > v$——**显式破缺选边**。

**质量**：海森矩阵在 $(\sigma, \vec\pi) = (f, 0)$ 处：

$$\frac{\partial^2V}{\partial\pi_i\,\partial\pi_j} = \delta_{ij}\,4\lambda\,(f^2 - v^2) = \delta_{ij}\,\frac{\varepsilon}{f},\qquad \frac{\partial^2V}{\partial\sigma^2} = 4\lambda\,(3f^2 - v^2) = 8\lambda f^2 + \frac{\varepsilon}{f}.$$

（径向：$\frac{\partial}{\partial\sigma}\big[4\lambda\sigma(\cdots)\big]$ 在极小处展开；用 $f^2 - v^2 = \varepsilon/4\lambda f$ 化简。）对照 $\frac12 m^2\phi^2$：

$$m_\pi^2 = \frac{\varepsilon}{f} = 4\lambda\big(f^2 - v^2\big)\;\xrightarrow{\;\varepsilon\to0\;}\;0,\qquad m_\sigma^2 = 8\lambda f^2 + \frac{\varepsilon}{f} \approx 8\lambda v^2.$$

**解读**：$\varepsilon$ 项 $-\varepsilon\sigma$ 显式破坏手征对称（$\sigma$ 与 $\vec\pi$ 在手征 $\mathrm{SU(2)\times SU(2)}$ 下同属一个多重态 $(\sigma, \vec\pi)$，单独拉出 $\sigma$ 的线性项破坏之），它的全部效应是把谷底的简并压成单个极小、坡度 $\propto\varepsilon$——Goldstone 模的"零回复力"变成"弱回复力"，$m_\pi^2$ **正比于显式破缺强度**。这正是 QCD 里 $\varepsilon \leftrightarrow m_u + m_d$ 的角色：夸克质量项显式破坏手征对称，把 3 个本该无质量的 $\pi$ 压成 $135\text{–}140\,\mathrm{MeV}$ 的赝 Goldstone；精确到领头阶的关系就是 Gell-Mann–Oakes–Renner $m_\pi^2 f_\pi^2 = -(m_u + m_d)\langle\bar qq\rangle$——把本模型的 $\varepsilon, f, v$ 换成 QCD 的 $m_q, f_\pi, \langle\bar qq\rangle$，结构与本式同形。

</details>

## 参考

- Schwartz《Quantum Field Theory and the Standard Model》第 28 章（对称性自发破缺、Goldstone 定理与 Higgs 机制——与本篇结构最接近的现代讲法）。
- Srednicki《Quantum Field Theory》第 28–29 章（自发破缺与规范版，记号轻、推导干净）。
- Peskin & Schroeder《An Introduction to Quantum Field Theory》第二部分对称性破缺相关章节（Goldstone 定理的谱论证与电弱应用的衔接）。
- 原始论文：Englert & Brout (1964)、Higgs (1964)、Guralnik–Hagen–Kibble (1964)（三篇 1964 机制原始文献）；Kibble (1967)（非阿贝尔推广）；Anderson (1962)（凝聚态先声）。
- Weinberg《The Quantum Theory of Fields》第二卷第 19 章（Goldstone 定理的公理化表述与谱证明的严谨版本）；Elitzur 定理的原始文献 (Elitzur, 1975)。
- 凝聚态接口：Anderson《Basic Notions of Condensed Matter Physics》（对称破缺作为凝聚态的第一性概念）；磁振子与非相对论计数见凝聚态书磁学一篇。
