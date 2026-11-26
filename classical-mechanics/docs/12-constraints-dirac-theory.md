# 约束系统与 Dirac 理论：规范冗余的正则语言

> 路线图位置：第 2 部分（哈密顿力学与几何化）· 第 12 章
> 前置知识：第 9 章（哈密顿方程、Poisson 括号）、第 10 章（辛结构）；线性代数。
> 学习目标：会识别奇异拉氏量并走完 Dirac–Bergmann 算法；能区分第一类与第二类约束并说出各自的处理方式（规范变换 / Dirac 括号）；会数物理自由度；理解"哈密顿量是约束的线性组合"以及它与广义相对论时间问题的关系。

---

**单位约定**：第 2、3 节的参数化粒子取 $c=1$；电磁场用高斯制；其余保留通常单位。

## 1. 一句话总结

**当拉氏量的 Hessian 退化时，$\dot q$ 不能全部由 $p$ 解出，相空间被约束面切开：第一类约束生成规范变换（物理态是轨道上的等价类），第二类约束用 Dirac 括号消去（自由度成对砍掉）；物理自由度公式为 $(2n-2F-S)/2$。广义相对论是"哈密顿量纯为约束"的极端例子，也是量子引力时间问题的源头。**

## 2. 约束从哪里来

### 2.1 奇异拉氏量

第 9 章要求 Hessian $M_{ij} = \partial^2L/\partial\dot q^i\partial\dot q^j$ 可逆，才能把 $\dot q$ 解成 $p$ 的函数。若 $\det M = 0$，动量定义

$$p_i = \frac{\partial L}{\partial \dot q^i}(q,\dot q)$$

就给出若干**不涉及速度**的关系。按秩–零化度定理，至少有 $\dim\ker M$ 个组合只含 $q,p$：这些就是**主约束**（primary constraints），记作

$$\phi_m(q,p) \approx 0.$$

### 2.2 "弱等" $\approx$ 的含义

Dirac 用 $\approx$ 表示"在约束面上成立"，以区别于恒等式 $=$。运算规则：可以先算 Poisson 括号再取约束面，但不能在括号内先把约束代掉——因为约束的括号可能不为零（这正是第二类约束的来源）。

### 2.3 三个标准例子

- **参数化粒子**：把时间 $t$ 也当坐标，$S = \int\mathrm{d}\tau\left[\frac12 m\dot q^2/\dot t - V(q)\dot t\right]$。动量 $p_t = -\left[\frac12 m\dot q^2/\dot t^2 + V\right]$ 与 $p = m\dot q/\dot t$ 之间有关系，相空间被切一刀。
- **电磁场**：$A_0$ 没有时间导数，$\pi^0 = 0$ 是主约束；一致性条件再给出 Gauss 定律。
- **相对论粒子**：$p^2 - m^2 \approx 0$ 是质壳约束（用 einbein 形式时它是次级约束）。

## 3. Dirac–Bergmann 算法

### 3.1 总哈密顿量

正则哈密顿量 $H_c = p_i\dot q^i - L$ 不含速度（若含，说明还有主约束未被识别）。由于主约束的存在，$H_c$ 不唯一，可以加上约束的任意组合：

$$H_T = H_c + u^m\,\phi_m,$$

$u^m$ 是待定的拉格朗日乘子（它们是相空间的任意函数，不是动力学变量）。

### 3.2 一致性条件

约束必须随时间保持：

$$\dot\phi_m = \{\phi_m, H_T\} = \{\phi_m,H_c\} + u^n\{\phi_m,\phi_n\} \approx 0.$$

对每个 $m$，这给出三种可能：

1. **定出乘子**：若矩阵 $\{\phi_m,\phi_n\}$ 在约束面上可逆，则 $u^n$ 被唯一确定，没有新约束——这些约束是**第二类**；
2. **产生新约束**：若某个 $\{\phi_m,H_c\}$ 不能由已有约束及其乘子消掉，则它给出一个**次级约束**（secondary constraint），加入列表后重新检查；
3. **恒等**：若 $\{\phi_m,H_c\}$ 弱为零且乘子项可消，则该约束是**第一类**。

### 3.3 迭代与分类

重复"加入新约束 → 检查一致性"直到封闭。最后把所有约束分成两类：

- **第一类**：与所有约束的 Poisson 括号都弱为零，$\{\phi_a,\phi_b\}\approx 0$；
- **第二类**：存在某个约束使括号不弱为零。

第一类约束生成规范变换（§4），第二类约束用 Dirac 括号消去（§5）。

### 3.4 一个完整的账本：参数化粒子

取 $q^0 = t$，$q^1 = q$，拉氏量

$$L = \frac12 m\frac{\dot q^2}{\dot t} - V(q)\,\dot t.$$

动量：$p = m\dot q/\dot t$，$p_t = -\frac12 m\dot q^2/\dot t^2 - V = -H(q,p)$，其中 $H = p^2/2m + V$。正则哈密顿量：

$$H_c = p_t\dot t + p\dot q - L = \left(-\frac12 m\frac{\dot q^2}{\dot t} - V\dot t\right) + m\frac{\dot q^2}{\dot t} - \left(\frac12 m\frac{\dot q^2}{\dot t} - V\dot t\right) = 0.$$

（这三项精确相消，见自检 1。）于是唯一的约束是

$$\phi = p_t + H(q,p) \approx 0,$$

它由动量的定义直接给出（主约束），且 $\{\phi,\phi\} = 0$ 自动成立——**第一类**。总哈密顿量 $H_T = N\phi$，$N$ 任意：这就是重参数化规范。

## 4. 第一类约束与规范变换

### 4.1 约束生成变换

第一类约束 $\phi$ 通过括号生成相空间变换：

$$\delta f = \varepsilon\,\{f,\phi\}.$$

若 $\phi$ 是第一类，则 $\delta\phi\approx 0$——变换把约束面映到自身，且不改变物理态。规范变换 = 由第一类约束生成的变换（含其任意函数 $\varepsilon(t)$ 的版本）。

### 4.2 "哈密顿量纯为约束"

参数化粒子的例子给出一个深刻的结构：$H_T = N\phi$，**总哈密顿量完全是约束的线性组合**，在约束面上为零。所谓"时间演化"其实是沿规范轨道的滑动，物理演化必须相对于某个内部变量（如 $t$ 本身）来定义——这就是"时间问题"的力学原型（QFT 书第 8 阶段 01 篇的自检 4 用的正是这个玩具模型）。

### 4.3 广义相对论：ADM 形式

ADM 分解下，度规写成

$$\mathrm{d}s^2 = -N^2\mathrm{d}t^2 + h_{ij}(\mathrm{d}x^i + N^i\mathrm{d}t)(\mathrm{d}x^j + N^j\mathrm{d}t),$$

其中 lapse $N$ 与 shift $N^i$ 没有时间导数（不是动力学变量），空间度规 $h_{ij}$ 有 6 个分量。总哈密顿量

$$H = \int\mathrm{d}^3x\left[N\,\mathcal H + N^i\,\mathcal H_i\right],$$

$\mathcal H\approx 0$（超哈密顿约束）与 $\mathcal H_i\approx 0$（动量约束）共 4 个第一类约束，$N,N^i$ 是乘子。**这就是"引力没有哈密顿量、只有约束"的精确含义**；量子化后 $\hat{\mathcal H}\Psi = 0$ 就是 Wheeler–DeWitt 方程，波函数不含时间。

注意一个技术要点：GR 的第一类约束代数**不闭合为李代数**——两个约束的括号含度规依赖的"结构函数"而非常数。这使量子化远比 Yang–Mills 困难（QFT 书第 8 阶段 01 篇 §4.2）。

## 5. 第二类约束与 Dirac 括号

### 5.1 定义

设 $\phi_a$（$a = 1,\dots,S$）是第二类约束，矩阵 $C_{ab} = \{\phi_a,\phi_b\}$ 在约束面上可逆。**Dirac 括号**定义为

$$\{f,g\}_D \equiv \{f,g\} - \{f,\phi_a\}\,C^{ab}\,\{\phi_b,g\},$$

其中 $C^{ab}$ 是 $C_{ab}$ 的逆矩阵（指标求和）。

### 5.2 性质

- **约束变成"强零"**：对任意 $f$，$\{\phi_a,f\}_D = 0$——约束与一切量的括号为零，所以可以在括号内直接令 $\phi_a = 0$；
- **仍是泊松括号**：Dirac 括号满足反对称、Leibniz、Jacobi（因为它是"沿约束面投影"的辛结构）；
- **与约化相空间一致**：在约束面上，Dirac 括号等于"先解约束、再算 Poisson 括号"的结果。

### 5.3 玩具例子

二维相空间 $(q_1,p_1,q_2,p_2)$，两个约束 $\phi_1 = q_2$、$\phi_2 = p_2$。则 $C_{12} = \{q_2,p_2\} = 1$，$C = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$，$C^{-1} = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$。于是

$$\{q_2,p_2\}_D = 1 - \{q_2,q_2\}(-1)\{p_2,p_2\} - \cdots = 0,$$

而 $\{q_1,p_1\}_D = \{q_1,p_1\} = 1$：二维系统被约化成一维，且 $(q_1,p_1)$ 仍是正则对（自检 4 完整计算）。

### 5.4 物理例子：Proca 场

大质量矢量场 $\mathcal L = -\frac14 F_{\mu\nu}F^{\mu\nu} + \frac12 m^2 A_\mu A^\mu$ 有两个约束：

$$\phi_1 = \pi^0 \approx 0,\qquad \phi_2 = \partial_i\pi^i + m^2A_0 \approx 0.$$

第二式是 $\phi_1$ 的一致性条件（大质量版本的 Gauss 定律）。它们的括号

$$\{\pi^0(\mathbf x),\,\partial_i\pi^i(\mathbf y) + m^2A_0(\mathbf y)\} = m^2\,\delta^3(\mathbf x - \mathbf y) \neq 0$$

——**第二类**（自检 3）。结果：大质量矢量有 3 个偏振（无质量的只有 2 个），这是"质量吃掉一个标量自由度"的场论版本。

## 6. 自由度计数与规范固定

### 6.1 计数公式

$n$ 个广义坐标的相空间有 $2n$ 维。每个**第一类**约束生成一个规范方向，砍掉 2 维（约束本身 + 其规范轨道）；每个**第二类**约束只砍 1 维（约束面本身）。物理自由度（位形空间的维数）为

$$N_{\mathrm{dof}} = \frac{2n - 2F - S}{2}.$$

### 6.2 标准账本

- **电磁场**：$n = 4$（$A_\mu$），$2n = 8$；两个第一类（$\pi^0$、Gauss），$F = 2$，$S = 0$：$N = (8-4)/2 = 2$——两个横向偏振。
- **广义相对论**：ADM 相空间 $6$ 个 $h_{ij}$ 加 $6$ 个 $\pi^{ij}$，共 $12$ 维；$4$ 个第一类约束（$\mathcal H,\mathcal H_i$），$F = 4$：$N = (12-8)/2 = 2$——引力子的两个偏振（自检 5）。
- **Proca**：$n = 4$，$2n = 8$；1 个第二类对（$S = 2$），$F = 0$：$N = (8-2)/2 = 3$。

### 6.3 规范固定

每个第一类约束可以配一个**规范条件** $\chi_a\approx 0$（如 Lorenz 规范 $\partial_\mu A^\mu = 0$、ADM 的 $N = 1, N^i = 0$）。条件与约束合起来变成第二类，Dirac 括号变成可逆的——这就是 Faddeev–Popov 程序的经典前身（QFT 书第 4 阶段 07 篇 §8）。规范固定的代价是：结果必须与规范选择无关（Ward 恒等式 / BRST 上同调保证这一点）。

## 7. 量子化三条路

### 7.1 Dirac 量子化

- **第一类**：把约束提升为算符条件 $\hat\phi_a|\psi\rangle = 0$（物理态子空间）。一致性要求约束代数无反常（$[\hat\phi_a,\hat\phi_b]$ 的系数算符排序得当）。电磁场的 **Gupta–Bleuler** 条件 $\partial^\mu A_\mu^{(+)}|\psi\rangle = 0$ 是标准实现：只允许两个横向偏振存活（自检 2 的量子版）。
- **第二类**：把 Dirac 括号换成对易子，$[\,,\,] = i\hbar\{\,,\,\}_D$；约束已经"花掉"，不再对态提条件。

### 7.2 路径积分

规范理论的路径积分要对规范轨道商掉：Faddeev–Popov 行列式 + 鬼场，或等价的 BRST 形式（QFT 书第 4 阶段 07 篇 §8、第 6 阶段 01 篇）。第一类约束的代数结构决定鬼场的相互作用。

### 7.3 排序与反常

量子化把"约束代数"变成"算符代数"，可能出现反常（经典对称性在量子层面破缺）：引力/规范理论的自洽性要求反常相消（标准模型里 Higgs 与夸克、轻子的量子数配合正是为此）。这是"约束代数"最深刻的量子后果，超出本章范围（QFT 书第 6 阶段 04 篇）。

## 8. 与协变相空间、广义相对论的接口

- **协变相空间**：不选定时间叶层，直接在解空间上定义辛形式；约束变成"规范零模"，边缘模（edge modes）是规范荷的载体。第 9 阶段 04 篇的零锥正则引力正是这个语言的场论版本。
- **广义相对论**：ADM 约束是第一类约束的几何化身；"哈密顿量 = 约束"意味着时间演化是规范——第 11 章与广义相对论书第 11、12 章的起点。
- **量子引力**：约束代数的结构函数（而非常数）使 Wheeler–DeWitt 量子化极难定义；代数量子引力（QFT 书第 9 阶段）选择先解约束、在约化相空间上量子化——这是绕过该困难的路线。

## 小结

- 奇异拉氏量（Hessian 退化）产生约束；Dirac–Bergmann 算法通过一致性条件迭代，把约束分为第一类与第二类。
- 第一类约束生成规范变换，物理态是规范轨道上的等价类；第二类约束用 Dirac 括号消去，约束变成强零。
- 物理自由度 $N = (2n-2F-S)/2$：电磁场 2、Proca 3、广义相对论 2。
- 参数化粒子与 ADM 显示"总哈密顿量纯为约束"：$H_T = N\phi$（GR 为 $\int(N\mathcal H + N^i\mathcal H_i)$），时间演化是规范——量子引力的时间问题。
- 量子化：第一类 → 物理态条件（Gupta–Bleuler / Wheeler–DeWitt），第二类 → 括号换对易子；路径积分用 Faddeev–Popov/BRST 处理规范冗余。

## 自检问题

**1.** 参数化粒子：$L = \frac12 m\dot q^2/\dot t - V(q)\dot t$。证明 $H_c = 0$，求出唯一的约束并判断其类型，数出物理自由度。

<details markdown="1"><summary>点击显示答案</summary>

动量：

$$p = \frac{\partial L}{\partial\dot q} = m\frac{\dot q}{\dot t},\qquad p_t = \frac{\partial L}{\partial\dot t} = -\frac12 m\frac{\dot q^2}{\dot t^2} - V(q).$$

用 $p$ 表示 $\dot q/\dot t = p/m$，则

$$p_t = -\frac{p^2}{2m} - V(q) \equiv -H(q,p).$$

正则哈密顿量：

$$H_c = p_t\dot t + p\dot q - L = \left(-\frac{p^2}{2m}-V\right)\dot t + \frac{p^2}{m}\dot t - \left(\frac{p^2}{2m} - V\right)\dot t = 0.$$

三项精确相消（这里用了 $\dot q = (p/m)\dot t$）。约束：

$$\phi = p_t + H(q,p) \approx 0.$$

类型：只有一个约束且 $\{\phi,\phi\} = 0$，故**第一类**。总哈密顿量 $H_T = N\phi$，$N$ 任意（重参数化规范）。

计数：$n = 2$（$t,q$），$2n = 4$；$F = 1$，$S = 0$，故

$$N_{\mathrm{dof}} = \frac{4 - 2}{2} = 1,$$

正是"粒子位置作为时间的函数"这一个物理自由度。$t$ 与 $p_t$ 只是把一维运动嵌入二维相空间的方式。

</details>

**2.** 电磁场：从 $L = -\frac14F_{\mu\nu}F^{\mu\nu}$ 出发，求出主约束、次级约束，判断类型并数出偏振数；再说明 Gupta–Bleuler 条件如何留下两个横向偏振。

<details markdown="1"><summary>点击显示答案</summary>

$A_0$ 没有时间导数：$\pi^0 = \partial L/\partial\dot A_0 = 0$，主约束 $\phi_1 = \pi^0\approx 0$。空间分量 $\pi^i = \partial L/\partial\dot A_i = F^{i0}$（即电场）。

正则哈密顿量（分部积分后）：

$$H_c = \int\mathrm{d}^3x\left[\frac12\left(\pi_i^2 + B_i^2\right) - A_0\,\partial_i\pi^i\right],\qquad B_i = \frac12\varepsilon_{ijk}F_{jk}.$$

一致性条件：

$$\dot\phi_1 = \{\pi^0,H_T\} = -\frac{\delta H_T}{\delta A_0} = \partial_i\pi^i \approx 0,$$

即 Gauss 定律 $\phi_2 = \partial_i\pi^i\approx 0$（次级约束）。再查 $\phi_2$ 的一致性：$\{\partial_i\pi^i, H_c\} = 0$（Gauss 定律生成规范变换，与 $H_c$ 对易），封闭。

类型：$\{\phi_1,\phi_2\} = \{\pi^0(\mathbf x), \partial_i\pi^i(\mathbf y)\} = 0$，两个都是**第一类**。

计数：$n = 4$，$2n = 8$；$F = 2$，$S = 0$：$N = (8-4)/2 = 2$。

Gupta–Bleuler：物理态满足 $\partial^\mu A_\mu^{(+)}|\psi\rangle = 0$（只取湮灭部分，避免算符等式过强）。在动量空间，这个条件消去纵向与时间方向各一个偏振，剩下两个横向偏振 $|\psi\rangle \sim a_{\mathbf k,\pm}^\dagger|0\rangle$，与计数一致。两点差别值得注意：经典约束要求 $\partial_i\pi^i = 0$ 严格成立，量子条件只要求正频部分——这就是"弱条件"的含义。

</details>

**3.** Proca 场：证明 $\phi_1 = \pi^0$ 与 $\phi_2 = \partial_i\pi^i + m^2A_0$ 是第二类约束，并数出偏振数。

<details markdown="1"><summary>点击显示答案</summary>

拉氏量 $\mathcal L = -\frac14F_{\mu\nu}F^{\mu\nu} + \frac12m^2A_\mu A^\mu$。$\pi^0 = 0$ 仍是主约束。正则哈密顿量（分部积分）：

$$H_c = \int\mathrm{d}^3x\left[\frac12(\pi_i^2 + B_i^2) + \frac12m^2A_i^2 - A_0\,\partial_i\pi^i - \frac12m^2A_0^2\right].$$

一致性：

$$\dot\phi_1 = \{\pi^0, H_T\} = -\frac{\delta H_T}{\delta A_0} = \partial_i\pi^i + m^2A_0 \approx 0,$$

即 $\phi_2 = \partial_i\pi^i + m^2A_0$（大质量 Gauss 定律）。

括号：

$$\{\phi_1(\mathbf x), \phi_2(\mathbf y)\} = \{\pi^0(\mathbf x),\, m^2A_0(\mathbf y)\} = m^2\,\delta^3(\mathbf x-\mathbf y) \neq 0.$$

因此两个约束构成**第二类对**（$S = 2$，$F = 0$）。计数：

$$N = \frac{2n - S}{2} = \frac{8 - 2}{2} = 3,$$

三个偏振——大质量矢量比无质量多一个纵向自由度。机制：规范场"吃掉"一个标量模式变成纵向偏振（Higgs 机制的阿贝尔模型原型，QFT 书第 5 阶段 03 篇）。若取 $m\to 0$，括号系数消失，约束退化为第一类，自由度跳回 2——相变式的"偏振数跳变"正是规范对称性恢复的标志。

</details>

**4.** Dirac 括号：对约束 $\phi_1 = q_2$、$\phi_2 = p_2$，验证 $\{\phi_a,f\}_D = 0$（任意 $f$），并验证 $\{q_2,p_2\}_D = 0$、$\{q_1,p_1\}_D = 1$。

<details markdown="1"><summary>点击显示答案</summary>

$C_{ab} = \{\phi_a,\phi_b\}$：

$$C = \begin{pmatrix}\{q_2,q_2\} & \{q_2,p_2\}\\ \{p_2,q_2\} & \{p_2,p_2\}\end{pmatrix} = \begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix},\qquad C^{-1} = \begin{pmatrix}0 & -1\\ 1 & 0\end{pmatrix}.$$

取 $f = q_2$：

$$\{q_2,f\}_D = \{q_2,f\} - \{q_2,\phi_1\}C^{11}\{\phi_1,f\} - \{q_2,\phi_1\}C^{12}\{\phi_2,f\} - \{q_2,\phi_2\}C^{21}\{\phi_1,f\} - \{q_2,\phi_2\}C^{22}\{\phi_2,f\}.$$

代入 $\{q_2,\phi_1\} = 0$，$\{q_2,\phi_2\} = 1$，$C^{21} = 1$，$C^{22} = 0$：

$$\{q_2,f\}_D = \{q_2,f\} - 1\cdot 1\cdot\{q_2,f\} = 0.$$

取 $f = p_2$ 同理（$\{p_2,\phi_1\} = -1$，$\{p_2,\phi_2\} = 0$，$C^{12} = -1$）：$\{p_2,f\}_D = \{p_2,f\} - (-1)(-1)\{p_2,f\} = 0$。故两个约束与一切量的 Dirac 括号为零，可以在括号内直接令 $q_2 = p_2 = 0$。

约化后的正则对：$\{q_1,p_1\}_D$ 只涉及 $\{q_1,p_1\}$ 与含 $q_2,p_2$ 的项（均为零），故

$$\{q_1,p_1\}_D = 1.$$

结论：Dirac 括号把二维相空间约化成一维，$(q_1,p_1)$ 仍满足标准括号——与"先令 $q_2=p_2=0$ 再算括号"完全一致。这正是 Dirac 括号的用途：不必显式解约束，也能在约束面上做正确的辛几何。

</details>

**5.** 广义相对论的自由度：ADM 变量为 $(h_{ij},\pi^{ij})$，共 6+6 维相空间；约束为 $\mathcal H\approx 0$、$\mathcal H_i\approx 0$。解释为什么物理自由度是 2，而不是 $10-4 = 6$ 或 $12-4 = 8$。

<details markdown="1"><summary>点击显示答案</summary>

ADM 分解中，度规的 10 个分量被分成两类：lapse $N$、shift $N^i$ 共 4 个**没有时间导数**（它们不是动力学变量，是拉格朗日乘子）；空间度规 $h_{ij}$ 有 6 个分量（对称 $3\times3$ 矩阵），配 6 个共轭动量 $\pi^{ij}$。所以相空间是 $12$ 维，不是 $20$ 维。

4 个约束（$\mathcal H$ 与三个 $\mathcal H_i$）都是**第一类**：它们生成时间重参数化与空间微分同胚。每个第一类约束砍 2 维（约束面 1 维 + 规范轨道 1 维），故

$$N_{\mathrm{dof}} = \frac{12 - 2\times 4}{2} = 2,$$

即引力子的两个偏振。错误算法有两个典型：

- "$10 - 4 = 6$"：把 $N,N^i$ 当成动力学变量，又多减了约束——错在把"乘子"与"约束"混为一谈；
- "$12 - 4 = 8$"：只减了约束面，忘了每个第一类约束还带一条规范轨道（时间/空间重参数化的任意性）。

补充一句：$N$ 与 $N^i$ 的任意性不是"规范选择的自由"，而是**理论本身没有为它们提供演化方程**——它们是被约束决定的乘子。这正是"引力没有哈密顿量"的准确含义，也是 Wheeler–DeWitt 量子化（$\hat{\mathcal H}\Psi = 0$）与时间问题的起点。

</details>

## 参考

- P. A. M. Dirac《Lectures on Quantum Mechanics》(1964)：约束系统正则理论的原始讲义。
- Henneaux & Teitelboim《Quantization of Gauge Systems》(1992)：Dirac–Bergmann 算法的系统处理，第一类/第二类约束与 BRST。
- Goldstein《Classical Mechanics》第 8 章（奇异拉氏量与约束的初等处理）；Landau & Lifshitz《力学》§40 起（哈密顿形式的基础）。
- 第 9、10 章（括号与辛结构）；量子化与规范固定的场论版本见 QFT 书第 4 阶段 07 篇、第 6 阶段 01 篇；ADM 与时间问题见 QFT 书第 8 阶段 01 篇、广义相对论书第 11 章。
