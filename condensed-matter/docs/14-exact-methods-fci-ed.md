# 多电子问题与精确解：基组、FCI 与对角化

> 路线图位置：第四部分（多电子问题怎么算）· 第 14 章
> 前置知识：第 6 章[相互作用电子气](06-interacting-electron-gas.md)（二次量子化、Slater 行列式、Hartree–Fock 变分——本章把它的语言推广到任意基组）；量子力学的变分原理与微扰论（[QFT 书微扰论笔记](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)）；第 2 章 Born–Oppenheimer 近似的量级论证；第 4 章[能带论](04-band-theory.md)（平面波与倒空间）。
> 学习目标：会写出一般基组下的电子哈密顿量并数清积分与未知数的个数；理解 Slater 行列式空间的维数灾难（指数墙）与 Slater–Condon 规则带来的稀疏性；会在最小基组上亲手做完 H₂ 的严格解（FCI），并看清 RHF 解离错误的根源——静态相关；知道分子的 FCI 与晶格模型的严格对角化（ED）是同一件事，以及 QMC 为什么接不了班（符号问题）。
>
> 记号约定：从本篇起，第四部分采用**原子单位**（$\hbar = m_e = e = 4\pi\varepsilon_0 = 1$；长度单位 Bohr，能量单位 Hartree，$1\ \mathrm{Ha} = 27.2$ eV）——量子化学与电子结构文献的标准约定。$M$ 为自旋轨道态数，$N$ 为电子数，$N_\mathrm{o} = N$、$N_\mathrm{v} = M - N$ 为占据/空轨道数。

---

## 1. 一句话总结

**多电子问题在原理上早已解决——Born–Oppenheimer 分离后的非相对论薛定谔方程写下就是全部物理；难在求解：波函数是 $3N$ 个变量的反对称函数，而任何基组展开下严格解（FCI）的维数按二项式系数 $\binom{2M}{N}$ 指数增长，10 个电子 10 个轨道就是 $2\times10^5$、翻一倍就 $10^{11}$——这堵"指数墙"是一切近似方法的出发点。FCI 的价值不在算大体系，而在充当标尺：哈密顿量在行列式基下极度稀疏（Slater–Condon 规则：只耦合相差不超过两个轨道的行列式），小体系可以精确对角化，从而给后面每一级近似（HF → MP2 → CC → DFT）校准误差；最小基组的 H₂ 就是第一块校准砧——它的严格解暴露出 RHF 解离能错 8.5 eV 的静态相关病灶。**

## 2. 问题设定：电子哈密顿量

### 2.1 Born–Oppenheimer：先冻结离子

固体或分子里有电子与原子核两类粒子，但质量差 $M_\mathrm{ion}/m_e \sim 10^4$：电子在飞，核在爬。第 2 章已算过声速 $v_s \sim 10^3$–$10^4$ m/s 比费米速度 $v_F \sim 10^6$ m/s（[第 3 章](03-free-electron-gas.md)）小两个量级，对应能量上 $\hbar\omega_\text{ph} \sim 0.03$–$0.1$ eV $\ll E_F \sim$ 数 eV——电子对核的位置变化是瞬时响应的（绝热近似），核则只见到电子云的平均势。于是**核坐标退化为参数**：解电子的薛定谔方程得 $E(\{\vec R_I\})$，再把 $E$ 当作离子的势能面去解核的运动（声子，第 2 章）。量子化学 99% 的工作发生在这个电子方程上（数量级的论证见自检问题 5；近似失效的场合——圆锥交叉附近、金属中的非绝热效应——本篇不碰）。

### 2.2 电子哈密顿量与二次量子化形式

固定核位置后，$N$ 个电子的哈密顿量为（原子单位）

$$H = \sum_{i=1}^N\left(-\frac12\nabla_i^2 - \sum_I\frac{Z_I}{\lvert\vec r_i - \vec R_I\rvert}\right) + \sum_{i<j}\frac{1}{\lvert\vec r_i - \vec r_j\rvert}.$$

第 6 章的二次量子化语言（Slater 行列式 + 产生湮灭算符）把它变成代数形式：取 $M$ 个正交归一的自旋轨道 $\{\chi_p\}$，

$$H = \sum_{pq} h_{pq}\, a_p^\dagger a_q + \frac12\sum_{pqrs}\langle pq\lvert rs\rangle\, a_p^\dagger a_q^\dagger a_s a_r,$$

其中单体积分与双体积分为

$$h_{pq} = \int \chi_p^*(\vec x)\left(-\frac12\nabla^2 + v_\text{ext}(\vec r)\right)\chi_q(\vec x)\,\text d\vec x,\qquad \langle pq\lvert rs\rangle = \iint\frac{\chi_p^*(1)\chi_q^*(2)\chi_r(1)\chi_s(2)}{r_{12}}\,\text d1\,\text d2,$$

（$\vec x = (\vec r, \sigma)$ 含自旋；反对称组合 $\langle pq\lVert rs\rangle = \langle pq\lvert rs\rangle - \langle pq\lvert sr\rangle$ 后面反复出现。）**先数账**：单体积分 $M^2$ 个、双体积分 $M^4$ 个——光是"把哈密顿量存下来"就是 $O(M^4)$。100 个轨道约 $10^7$ 个非零双体积分，尚可；固体里平面波数以万计，这个账本身就是第一课：**问题是四体量的海洋里求一个基态**。

## 3. 基组：把连续问题变成有限问题

### 3.1 分子一侧：局域轨道基组

展开波函数的自然基底是原子轨道（LCAO 的语言，第 4 章紧束缚已见过）。Slater 型轨道 $e^{-\zeta r}$ 物理正确但积分难算，实际用高斯函数的线性组合去逼近它；精度按两层旋钮系统性提高：

- **zeta 层**（轨道变多、变柔）：双 ζ、三 ζ……描述同一条原子轨道的径向柔性；
- **极化层**（加角动量）：在 p 壳上配 d 函数、d 壳上配 f 函数，让电子云能变形。

**相关性一致基组**（cc-pVnZ，n = D,T,Q,5,…）把两层旋钮拧成一个序列，能量随 n 近似指数收敛——这给了"向基组极限外推"一条系统化的路。本章不碰积分求值本身（那套高斯手艺见补充材料[高斯基组与双体积分求值](14s-gaussian-integrals.md)），只把积分当作给定的数。

### 3.2 固体一侧：平面波 + 赝势

周期体系（第 4 章 Bloch 定理）的天然基底是平面波 $e^{i\vec k\cdot\vec r}$，截断在动能 $E_\text{cut} = \tfrac12G_\text{cut}^2$ 以下，典型 300–600 eV 对应每条能带上千个平面波；同时 BZ 里连续的 $\vec k$ 折算成离散网格采样。芯电子（对化学键无贡献、却贡献了大部分平面波）用**赝势**替换成光滑的有效势——"冻芯近似"。平面波的四大优点：正交（无重叠积分）、系统性（加 $E_\text{cut}$ 就变好）、无基组超完备误差（局域基组的 BSSE）、与 FFT 天作之合。

### 3.3 冻芯与活性空间

同样的思想反过来用在行列式上：芯轨道冻结、只让价层电子激发，可大幅压缩 $M$ 与 $N$。代价是丢掉芯–价相关——一切"冻结"都是在指数墙上换呼吸空间。

## 4. FCI：行列式空间中的严格解

### 4.1 组态空间与它的维数

$N$ 个电子在 $M$ 个自旋轨道上的所有占据方式构成 Slater 行列式集合，维数是二项式系数

$$\dim = \binom{M}{N} \qquad (\text{如 } \tbinom{4}{2} = 6,\ \tbinom{20}{10} = 184{,}756,\ \tbinom{40}{20} \approx 1.4\times10^{11}),$$

水分子在 cc-pVTZ 下 $M = 84$、$N = 10$：$\binom{84}{10} \approx 2\times10^{13}$。利用斯特林公式，固定填充比 $N/M$ 时 $\ln\dim \propto M$——**每加一个轨道，维数乘上一个常数因子**，这就是"指数墙"的定量表述（自检问题 2 让你亲手数一遍）。墙的形态比高度更冷酷：50 个电子 50 个轨道（$10^{29}$ 维）在化学上只是"中等分子"。

### 4.2 Slater–Condon 规则：墙上的稀疏裂缝

把 $H$ 在行列式基下写成巨型矩阵，看似 $\dim^2$ 个元素，实则**绝大多数为零**。规则（用产生湮灭算符的反对易关系可证，自检问题 1）：

- **对角元**：占据轨道的加和——单体项之和加库仑/交换直项：

$$\langle D\lvert H\lvert D\rangle = \sum_{i\in D} h_{ii} + \frac12\sum_{i,j\in D}\big(J_{ij} - K_{ij}\big);$$

- **单激发**（相差一个轨道 $i\to a$）：$\langle D_i^a\lvert H\lvert D\rangle = h_{ai} + \sum_{j\in D}\langle aj\lVert ij\rangle$；
- **双激发**（$ij\to ab$）：$\langle D_{ij}^{ab}\lvert H\lvert D\rangle = \langle ab\lVert ij\rangle$——**一个反对称双体积分，完**；
- **相差三个及以上轨道：严格为零**。

物理直白：单体算符只挪一个电子，双体算符最多挪两个。于是每行只有 $1 + N_\mathrm{o}N_\mathrm{v} + \binom{N_\mathrm{o}}{2}\binom{N_\mathrm{v}}{2}$ 个非零元——矩阵是**极端稀疏**的。

### 4.3 迭代对角化与 FCI 的意义

稀疏矩阵求最低本征值不需要全对角化，只需反复算矩阵–向量乘积 $\sigma = Hc$（Lanczos 或 Davidson 迭代，后者是量子化学的标准配置）。每次乘积的成本 $\sim \dim\times N_\mathrm{o}^2N_\mathrm{v}^2$——维数的指数仍在，但"能精确算的体系"从 $\binom{20}{10}$ 推到了 $10^9$–$10^{10}$ 量级（配合对称性约化，现代 FCI 代码处理 $\sim 10^{10}$ 行列式）。

FCI 的意义由两条性质保证：**变分性**（能量是严格上界）与**基组内严格性**（再无近似——唯一的近似是基组截断与 BO）。于是小体系的 FCI = 给一切近似方法校准的实验台：

| 体系 | 用途 |
|---|---|
| He、Be 原子 | 相关能的教科书数值 |
| H₂ 最小基 | 静态相关的显微镜（4.4 节与自检问题 3） |
| H₂O 双 ζ | 检验 MP2/CC 的逐阶收敛 |
| Hubbard 4×4 | 强关联方法的靶子（第 5 节） |

### 4.4 显微镜下的第一课：H₂ 的严格解 vs RHF

最小基组下 H₂ 只有两个空间轨道（两个 H 的 1s 组合成成键 $\sigma_g$ 与反键 $\sigma_u$），$M = 4$、$N = 2$，$\binom{4}{2} = 6$ 个行列式；对称性分类后，基态所在的块只有两个组态：$|G\rangle = \lvert\sigma_g^2\rangle$ 与 $|U\rangle = \lvert\sigma_u^2\rangle$。FCI 就是对角化这个 2×2 矩阵——完整推导见自检问题 3，结论先摆出来：

- **平衡键长附近**：基态几乎纯 $|G\rangle$（$|U\rangle$ 权重百分之几），RHF 与 FCI 几乎重合，误差 ~1 eV（这就是第 15 章的"动态相关"）；
- **拉伸解离时**：$\sigma_g$–$\sigma_u$ 能隙趋于零，两个组态简并化，FCI 基态变成 $\tfrac{1}{\sqrt2}(|G\rangle - |U\rangle)$——数学上是两个行列式的强混合，物理上这个组合恰好把电子**局域回各自的原子**（共价解离成两个中性 H）；
- **RHF 的死法**：单行列式被锁死在 $|G\rangle = 50\%$ 离子构型 + 50% 共价构型上，解离极限能量高出严格值 $J/2 = \tfrac{5}{16}\ \mathrm{Ha} \approx 8.5$ eV——化学精度（0.04 eV）的两百倍。

**静态相关**由此得名：在近简并的组态之间，波函数必须用多个"参考"来构造，任何单一行列式（HF 及其微扰论亲戚）都会系统性翻车。它划出了第 15 章（动态相关，MP2/CC 的主场）与第 16–17 章（DFT 及其强关联修补）的分界线。

## 5. 晶格一侧：Hubbard 模型与严格对角化

第 13 章把强关联问题压缩进 Hubbard 模型 $H = -t\sum_{\langle ij\rangle\sigma}c^\dagger_{i\sigma}c_{j\sigma} + U\sum_i n_{i\uparrow}n_{i\downarrow}$——它就是一个 $M = 2L$（$L$ 个格点）、$N$ 个电子的"基组"，FCI 在这个基组下的名字叫**严格对角化（ED）**。同一堵墙、同一种稀疏（t 挪一个电子、U 是对角）。半个世纪强关联方法的标尺就是这么来的：4×4 格点半满 $\binom{32}{16}$（对称性前 $\sim9\times10^8$）已经是超算级，6×6 超出一切显式方法。

墙上最后的指望是量子蒙特卡洛（QMC）：不从维数硬啃，而是抽样。它对玻色子体系（如液氦）和部分费米子体系近乎完美，但对一般费米子撞上**符号问题**——反对称波函数让样本权重有正有负，抵消后的"平均符号"随温度降低与体系增大指数衰减，信噪比指数崩塌（Troyer–Wiese 甚至证明了它是 NP-hard）。半满无阻挫的 Hubbard 模型恰好躲过（符号可吸收进重新定义的边界条件），掺杂或阻挫一出现就现形——这堵墙外没有免费的门。

## 小结

- 阶梯的起点与标尺：BO 分离 → 电子哈密顿量 → 基组（分子：cc-pVnZ 局域基；固体：平面波+赝势+冻芯）→ 行列式空间 → FCI 严格解。
- 指数墙：$\dim = \binom{M}{N}$，$\ln\dim \propto M$；稀疏性：Slater–Condon，只耦合 ≤2 激发。
- H₂ 显微镜：FCI 揭示静态相关，RHF 解离错 8.5 eV；动态/静态相关在此分家。
- 晶格 ED 与 FCI 同构；QMC 的符号问题保证墙外无通用捷径。
- 后三章的路线：HF（已有，第 6 章）→ 微扰（MP2）→ 指数化（CC）→ 换变量（DFT）→ 换对象（GW/DMFT）——每一步都在这道墙下讨生活。

## 自检问题

**1.** 用产生湮灭算符的反对易关系证明 Slater–Condon 规则：$H$ 在两个 Slater 行列式之间的矩阵元，当行列式相差三个及以上自旋轨道时严格为零；并写出双激发矩阵元恰为一个反对称积分 $\langle ab\lVert ij\rangle$ 的推导。

<details markdown="1"><summary>点击显示答案</summary>

行列式可写成 $|D\rangle = a_1^\dagger a_2^\dagger\cdots a_N^\dagger|0\rangle$（按轨道序）。矩阵元 $\langle D'|H|D\rangle$ 中每个算符必须找到配对：

**单体项** $\sum_p h_{pq}a_p^\dagger a_q$：$a_q$ 必须湮灭 $|D\rangle$ 中的一个占据轨道（否则该项为零），$a_p^\dagger$ 必须产生 $|D'\rangle$ 中的一个轨道。因此 $|D'\rangle$ 与 $|D\rangle$ 至多相差**一个**轨道（$i\to a$ 型单激发或完全相同），否则单体项贡献为零。

**双体项** $a_p^\dagger a_q^\dagger a_s a_r$：同理最多移动**两个**电子。若 $|D'\rangle$ 与 $|D\rangle$ 相差 ≥3 个轨道，单体与双体项全部无法配对：

$$\langle D'|H|D\rangle = 0 \qquad (\lvert D'\rvert,\lvert D\rvert \text{ 相差} \ge 3 \text{ 个轨道}).$$

**双激发元**：设 $|D'\rangle = |D_{ij}^{ab}\rangle$（把占据的 $i,j$ 换成空的 $a,b$）。只有双体项中的 $a_a^\dagger a_b^\dagger a_j a_i$（含顺序因子）能配对。把行列式排序到"标准位形"需要固定的置换次数，单体项无贡献，双体项用 Wick 定理收缩：

$$\langle D_{ij}^{ab}\lvert H\lvert D\rangle = \langle ab\lvert rs\rangle\langle\cdots\rangle\ \text{组合} = \langle ab\lVert ij\rangle = \langle ab\lvert ij\rangle - \langle ab\lvert ji\rangle.$$

两个相减的项来自两个电子（自旋算符配对的两种方式）的反对称化——正因如此，反对称积分 $\lVert\cdot\rVert$ 是整个电子结构方法的自然货币。**推论**：哈密顿矩阵每行非零元个数 $= 1 + N_\mathrm{o}N_\mathrm{v} + \tbinom{N_\mathrm{o}}{2}\tbinom{N_\mathrm{v}}{2}$，与 $\dim^2$ 相比微不足道——迭代对角化（4.3 节）的全部生计就在这条缝里。

</details>

**2.** 数清指数墙：计算 $\binom{20}{10}$、$\binom{40}{20}$、$\binom{100}{50}$；用斯特林公式证明固定填充比 $\nu = N/M$ 时 $\ln\dim \sim M\,s(\nu)$（$s$ 为熵密度），并估算每加一个轨道维数乘多少（取半满）。

<details markdown="1"><summary>点击显示答案</summary>

**数值**：

$$\binom{20}{10} = 184{,}756,\qquad \binom{40}{20} = 137{,}846{,}528{,}820 \approx 1.4\times10^{11},\qquad \binom{100}{50} \approx 1.01\times10^{29}.$$

**斯特林**：$\ln n! = n\ln n - n + O(\ln n)$，

$$\ln\binom{M}{N} = M\ln M - N\ln N - (M-N)\ln(M-N) + O(\ln M) \equiv M\,s(\nu),\qquad s(\nu) = -\nu\ln\nu - (1-\nu)\ln(1-\nu),$$

正是伯努利熵。**每加一个轨道**（半满 $\nu = 1/2$）：$s(1/2) = \ln 2$，故维数每加一个自旋轨道乘以 $e^{s/1}\approx e^{0.693} = 2$——每加一个**空间**轨道（两个自旋轨道）乘 4。数值验证：从 $\binom{40}{20}$ 到 $\binom{100}{50}$，$\lg\dim$ 从 11.1 到 29.0，平均每空间轨道 $18/(30) \times 2$……直接看公式即可。

**换算成账单**：即便矩阵元只存 8 字节、矩阵向量乘只做一遍，$10^{29}$ 维需要的内存超过 $10^{30}$ 字节——比可观测宇宙的原子数还多。墙不是工程问题，是信息量问题：**基态波函数本身就含有指数多比特的信息**（量子计算"量子优越性"的物理底色），任何把它显式写出来的方法都注定只够得着小体系。后三章的一切方法，本质都是拒绝显式写波函数。

</details>

**3.** 完成 H₂ 最小基组的 FCI：在 $|G\rangle = \lvert\sigma_g^2\rangle$、$|U\rangle = \lvert\sigma_u^2\rangle$ 组成的 2×2 块中写出哈密顿矩阵（用局域积分 $J = (aa\lvert aa)$ 表达），求本征值；证明解离极限 $R\to\infty$ 处 FCI 基态能量恰为 $2E(\mathrm{H})$，而 RHF 高出 $J/2 = 5/16\ \mathrm{Ha} \approx 8.5$ eV；解释基态波函数 $\tfrac{1}{\sqrt2}(|G\rangle - |U\rangle)$ 为什么就是两个中性原子。

<details markdown="1"><summary>点击显示答案</summary>

**矩阵元**。记 $\sigma_{g,u} = (a\pm b)/\sqrt2$，所有跨原子积分在 $R\to\infty$ 时归零，仅剩同址库仑 $J = (aa\lvert aa) = (bb\lvert bb) = \tfrac58$ Ha（H 的 1s）。单体部分：$\langle G\lvert\sum h\lvert G\rangle = 2\varepsilon_g \to 2E(\mathrm H)$，同理 $|U\rangle$（两 MO 能级都趋于氢原子能级）。双体部分逐项展开（对称化空间波函数，交叉积分归零后）：

$$\langle G\lvert V\lvert G\rangle = \langle U\lvert V\lvert U\rangle = \frac{J}{2},\qquad \langle G\lvert V\lvert U\rangle = \frac{J}{2}.$$

（例如 $\langle G\lvert V\lvert G\rangle = \tfrac14[J_{aa} + J_{bb} + \text{跨项}] \to \tfrac14(2J) = J/2$；交叉项同理，四个保号项两两相消只留两个同址项。）

**本征值**：

$$H_{2\times2} = \begin{pmatrix} 2E_\mathrm{H} + J/2 & J/2 \\ J/2 & 2E_\mathrm{H} + J/2 \end{pmatrix}\;\Longrightarrow\; E_\pm = 2E_\mathrm{H} + \frac{J}{2} \pm \frac{J}{2},$$

即 $E_- = 2E_\mathrm{H}$（共价，解离正确）与 $E_+ = 2E_\mathrm{H} + J$（离子，$\mathrm{H^+H^-}$ 型）。

**RHF 的错误**：RHF 锁定单行列式 $|G\rangle$，能量 $2E_\mathrm{H} + J/2$，比严格基态高

$$E_\mathrm{RHF} - E_\mathrm{FCI} = \frac{J}{2} = \frac{5}{16}\ \mathrm{Ha} \approx 8.5\ \mathrm{eV},$$

是化学精度（1 kcal/mol ≈ 0.043 eV）的两百倍。根源：$|G\rangle$ 展开成局域形式是 $\tfrac14$ 权重的 $\lvert aa\rangle,\lvert bb\rangle$（离子，各 $\tfrac14$）与 $\lvert ab\rangle,\lvert ba\rangle$（共价，各 $\tfrac14$）——**一半离子污染**，而无穷远处离子构型能量高 $J$。

**波函数的物理**：

$$\frac{1}{\sqrt2}\big(|G\rangle - |U\rangle\big) = \frac{1}{\sqrt2}\cdot\frac{1}{2}\big[(aa+ab+ba+bb) - (aa - ab - ba + bb)\big] = \frac{1}{\sqrt2}(ab + ba),$$

恰好是共价波函数 $\tfrac{1}{\sqrt2}\big[a(1)b(2) + b(1)a(2)\big]$——一个电子一个原子、对称化以配合单重态自旋。**FCI 用两个行列式的相消干掉了全部离子污染**；这就是静态相关的全部内容：近简并组态的强混合。顺带：把 $|U\rangle$ 的权重调对所需的信息量随 $R$ 增大而急剧上升，任何"围绕单参考展开且收敛半径有限"的方法（下章的 MP 系列）都会在此发散——第 15 章自检问题 5 亲自演示。

</details>

**4.** 迭代对角化的成本账：证明一次矩阵–向量乘积 $\sigma = Hc$ 的成本约为 $\dim\times N_\mathrm{o}^2N_\mathrm{v}^2/4$ 次乘加；对 $\binom{20}{10}$（$N_\mathrm{o} = N_\mathrm{v} = 10$）估算一次乘积的浮点运算量，并说明为什么说"稀疏性把墙推远了两格、但没拆掉"。

<details markdown="1"><summary>点击显示答案</summary>

**每个行列式的耦合数**：由 Slater–Condon，从任一行列式出发，单激发目标 $N_\mathrm{o}N_\mathrm{v}$ 个（选一个占据、选一个空轨道），双激发目标 $\tbinom{N_\mathrm{o}}{2}\tbinom{N_\mathrm{v}}{2} \approx N_\mathrm{o}^2N_\mathrm{v}^2/4$ 个——后者占绝对主导。每个目标对应一个双体积分与一次乘加。对 $c$ 的每个分量（共 $\dim$ 个）都要生成这些耦合：

$$\text{成本} \approx \dim\times\frac{N_\mathrm{o}^2N_\mathrm{v}^2}{4}\ \text{乘加}.$$

**数值**：$\dim = 184{,}756$，$N_\mathrm{o} = N_\mathrm{v} = 10$：

$$1.85\times10^5 \times \frac{10^4}{4} \approx 5\times10^8\ \text{乘加/迭代},$$

微秒级的现代内核上毫秒量级——完全平凡。但把体系加倍到 $\binom{40}{20} \approx 1.4\times10^{11}$、$N_\mathrm{o} = N_\mathrm{v} = 20$：

$$1.4\times10^{11}\times\frac{1.6\times10^5}{4} \approx 6\times10^{15}\ \text{乘加/迭代} \times\ (\text{数百次迭代})\ (\text{还要存 } \dim \text{ 维向量 } \approx 1\ \text{TB}),$$

从"笔记本毫秒"跳到"超算小时–天"。**推远两格**指：朴素对角化 $\dim^2$ 存储、$\dim^3$ 运算；稀疏迭代把它压到 $\dim\cdot N^2M^2$ 与 $\dim$ 存储——指数仍在 $\dim$ 里，只是系数小了天文数字倍。墙没拆，只是往后挪了两格：这就是 FCI 能摸到 $10^{10}$ 行列式、却永远摸不到 $10^{20}$ 的原因。

</details>

**5.** Born–Oppenheimer 近似的量级账：利用第 2、3 章的数值，论证电子与离子的动力学可以用绝热参数 $\eta \sim \sqrt{m_e/M_\mathrm{ion}}$ 分离，并估算 $\eta$；指出两类 BO 失效的场合。

<details markdown="1"><summary>点击显示答案</summary>

**量级链**：离子的振动频率 $\omega_\text{ph}$ 与电子跃迁频率 $\omega_e$ 之比可以由同一种弹簧的两种质量估出——化学键的力常数对电子（质量 $m_e$）与对核（质量 $M$）给出不同频率：

$$\frac{\omega_\text{ph}}{\omega_e} \sim \sqrt{\frac{m_e}{M}} \equiv \eta.$$

用第 2、3 章的独立数字核对：$\hbar\omega_\text{ph} \sim 0.03$–$0.1$ eV（Debye/声学声子），电子能标 $E_F \sim 3$–$5$ eV 或键能 $\sim$ 数 eV，比值 $\sim 10^{-2}$；而 $\sqrt{m_e/m_p} = \sqrt{1/1836} \approx 0.023$——两种算法一致，$\eta \approx 2\times10^{-2}$。

**结论**：时间尺度差 ~50 倍、能量尺度差 ~$10^3$ 倍，电子在核的"慢运动"里始终瞬时达到基态（绝热跟随），核则只感受电子基态能量形成的势能面 $E(\{R_I\})$。误差以 $\eta^2 \sim 5\times10^{-4}$ 进入能量——比化学精度小两个量级，可以安心忽略（非绝热修正项的系统性处理即"绝热近似之后的第一阶修正"，属于前沿话题）。

**失效场合**：(i) **圆锥交叉**附近——两个电子态的势能面相交，$\Delta E \to 0$，"瞬时基态"失去意义，光化学的非绝热跃迁全发生在这里；(ii) **金属**——能隙处处为零、激发谱连续，绝热展开的能标分离失效，声子与电子必须耦合处理（电声相互作用、超导的 BCS 配对正是这个耦合的产物，第 8 章）。注意 BO 失效不推翻"电子结构先行"的方法论——它只是提醒：势能面 $E(\{R_I\})$ 这个概念本身在上述场合要小心使用。

</details>

## 参考

- Szabo & Ostlund《Modern Quantum Chemistry》第 1–3 章：二次量子化、Slater 行列式与最小基 H₂ 的完整推演（本章 4.4 节与自检问题 3 的原型）。
- Helgaker, Jørgensen & Olsen《Molecular Electronic-Structure Theory》第 1 章（二次量子化）与 FCI 章节（Slater–Condon、行列式计数、迭代对角化）。
- A. Szabo & N. Ostlund 习题集与 C. David Sherrill 的《Notes on the formulation of FCI》：行列式计数与稀疏性的教学版整理。
- M. Troyer & U.-J. Wiese, Phys. Rev. Lett. **94**, 170201 (2005)：费米子符号问题的复杂性证明（第 5 节）。
- H. Fehske, R. Schneider & A. Weiße (eds.)《Computational Many-Particle Physics》：Hubbard 模型 ED 与 QMC 的方法论章节。
