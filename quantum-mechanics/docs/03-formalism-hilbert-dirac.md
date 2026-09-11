# 形式体系：希尔伯特空间、算符与狄拉克记号——量子力学的语法

> 路线图位置：量子力学书 · 第一部分（形式体系）· 第 03 篇
> 前置知识：第 01 篇（[旧量子论](01-old-quantum-theory.md)）的历史动机；线性代数（本征值问题、厄米矩阵、幺正矩阵）。
> 学习目标：会用狄拉克记号陈述量子力学的全部公设（态、可观测量、测量、演化）；会推导 Robertson 不确定关系与 Ehrenfest 定理；会在坐标/动量表象与抽象记号之间自由翻译，并据此说清矩阵力学与波动力学为什么是同一套理论；会写密度算符并知道它何时不可或缺；为第 04 篇（[谐振子代数解法](04-harmonic-oscillator-ladder.md)）、第 05 篇（[角动量](05-angular-momentum.md)）、第 07 篇（[微扰论](07-perturbation-theory.md)）、第 09 篇（[二次量子化](09-second-quantization.md)）、第 10 篇（[线性响应](10-linear-response-kubo.md)）备好语言。
>
> 记号约定：本篇保留 $\hbar$（与第 04–06 篇一致，不使用自然单位）。态空间记 $\mathcal H$，内积 $\langle\phi|\psi\rangle$ 按物理惯例对第一个变量反线性、对第二个线性；$\dagger$ 为厄米共轭，$\mathbb 1$ 为单位算符。

---

## 1. 一句话总结

**量子力学的全部内容是五条公设：态是希尔伯特空间里的射线（ket），可观测量是厄米算符，测量结果出自谱定理加 Born 规则，时间演化是幺正算符（薛定谔方程），复合系统用张量积拼接——矩阵力学与波动力学只是这套语法在两个具体表象下的方言，而 $[x,p]=i\hbar$ 是把"量子"写进语法的唯一一处非对易。**

下面按"为什么需要 → 态 → 算符 → 测量 → 表象 → 演化 → 密度矩阵 → 张量积"的顺序把语法搭起来，全程用自旋 $1/2$ 这个最小非平庸希尔伯特空间当教具。

## 2. 为什么需要形式体系

### 2.1 旧量子论的失败

第 01 篇（[旧量子论](01-old-quantum-theory.md)）已经清点过 1913–1925 年的账目：玻尔模型能算氢原子能级，却算不出谱线强度、氦原子、反常 Zeeman 效应；量子化条件 $\oint p\,dq = nh$ 只适用于可分离的周期体系，没有任何理由延伸到一般系统。问题的本质是：**旧量子论没有"态"的概念**——它在经典轨道上打补丁，而不是另立一套动力学。

### 2.2 两套语言的降临

1925–1926 年，答案竟以两套面目完全不同的理论同时出现：

- **矩阵力学**（Heisenberg–Born–Jordan，1925）：抛弃轨道，只保留可观测量，力学量是无穷维矩阵，运动方程里出现 $pq - qp \neq 0$。它最辉煌的实战是第 06s 篇（[矩阵力学解氢原子](06s-hydrogen-matrix-mechanics.md)）：不解任何微分方程，纯靠代数与对易关系解出氢原子能级。
- **波动力学**（Schrödinger，1926）：态是波函数 $\psi(x)$，力学量是微分算符，能量本征值是边值问题的产物。第 06 篇（[氢原子波动力学](06-hydrogen-and-subshells.md)）就是这条路线。

两套理论给出的全部可检验预言逐一吻合，但一个满是矩阵、一个满是波——它们是同一回事吗？

### 2.3 Dirac–von Neumann 公理化

是同一回事。Dirac（1930）与 von Neumann（1932）给出的回答构成了本篇的主体：**抽象的态矢量 + 抽象的算符**，矩阵元与波函数都只是"在某组基下展开"的坐标。矩阵力学选了 $H$ 的本征基（所以 $H$ 是对角矩阵），波动力学选了 $x$ 的本征基（所以 $p$ 成了微分算符）；表象变换是幺正变换，物理预言与表象无关——等价性由此几乎自动成立（第 6.3 节）。

这套公理化的收益不仅是审美：它让"自旋"（没有经典对应的内禀自由度）自然地住进来（第 3.3 节），让对称性变成"与 $H$ 对易的幺正算符"（第 7.2 节），让统计混合态有了合法身份（第 8 节）。本篇把公设列全、把推导做透，后面每一篇都只是这套语法的应用题。

## 3. 态空间：希尔伯特空间与叠加原理

**公设 1（态）**：每个量子体系对应一个复希尔伯特空间 $\mathcal H$（完备的内积空间）；体系的纯态由 $\mathcal H$ 中的一条**射线**描述——即非零矢量 $|\psi\rangle$ 与其全体复数倍 $c|\psi\rangle$（$c\neq0$）代表同一物理态。通常取归一化代表元 $\langle\psi|\psi\rangle = 1$，于是态的自由度还剩一个无物理意义的整体相位 $e^{i\alpha}$。

### 3.1 ket、bra 与内积

- **ket** $|\psi\rangle \in \mathcal H$：态矢量本身。标签写什么都行：$|n\rangle$、$|x\rangle$、$|\uparrow\rangle$。
- **bra** $\langle\phi|$：对偶空间里的线性泛函，由 $\langle\phi|\psi\rangle \equiv (\,|\phi\rangle,\,|\psi\rangle\,)$ 定义，满足 $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^{*}$。
- **内积公理**：共轭对称、对第二变量线性、正定性 $\langle\psi|\psi\rangle \ge 0$（等号仅当 $|\psi\rangle = 0$）。
- **Schwarz 不等式**：$\lvert\langle\phi|\psi\rangle\rvert^2 \le \langle\phi|\phi\rangle\langle\psi|\psi\rangle$，等号当且仅当两矢量平行。这是第 5.2 节不确定关系推导的唯一数学输入。
- **归一化**：$\langle\psi|\psi\rangle = 1$ 与 Born 规则的概率解释配套（第 5.1 节）；幺正演化保证归一性不随时间丢失（自检问题 2）。

### 3.2 叠加原理

$|\psi\rangle = c_1|\psi_1\rangle + c_2|\psi_2\rangle$ 仍是合法态，且复系数 $c_i$ 的**相对相位**有物理后果：干涉项 $2\operatorname{Re}(c_1^{*}c_2\langle\psi_1|A|\psi_2\rangle)$ 会出现在任何可观测量 $A$ 的期望值里。这正是量子与经典的根本分野：经典概率相加，量子**振幅**相加。整体相位无意义、相对相位全是戏——这是"态是射线而非矢量"的全部含义。

### 3.3 全程教具：自旋 $1/2$

最小的非平庸希尔伯特空间是 $\mathcal H = \mathbb C^2$。取 $S_z$ 的本征基 $\{|{\uparrow}\rangle, |{\downarrow}\rangle\}$（本征值 $\pm\hbar/2$），一般态与三个方向的自旋算符为

$$|\psi\rangle = \alpha|{\uparrow}\rangle + \beta|{\downarrow}\rangle, \qquad \lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1,$$

$$S_i = \frac{\hbar}{2}\sigma_i, \qquad \sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\ \sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\ \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$

Pauli 矩阵满足 $\sigma_i\sigma_j = \delta_{ij}\mathbb 1 + i\varepsilon_{ijk}\sigma_k$，由此 $[S_i, S_j] = i\hbar\varepsilon_{ijk}S_k$——自旋代数是第 05 篇（[角动量](05-angular-momentum.md)）一般理论 $[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ 的最小表示。注意这个体系**没有经典对应**：它不是某个 $\psi(x)$ 的内化，而是希尔伯特空间公理凭空容纳的自由度——这正是公理化路线的战利品。后面每条抽象命题（谱定理、测量、演化）都先在 $\mathbb C^2$ 上演算一遍。

## 4. 算符：可观测量与谱

**公设 2（可观测量）**：每个可观测量 $A$ 对应 $\mathcal H$ 上的一个厄米算符（自伴算符），$A = A^\dagger$。

### 4.1 为什么非得厄米

测量值必须是实数，而厄米算符的本征值必为实数、不同本征值的本征矢必正交。证明两行：设 $A|a\rangle = a|a\rangle$，则 $a\langle a|a\rangle = \langle a|A|a\rangle = \langle a|A^\dagger|a\rangle = a^{*}\langle a|a\rangle$，故 $a = a^{*}$；再设 $A|a'\rangle = a'|a'\rangle$，$a'\neq a$，则 $(a' - a)\langle a'|a\rangle = \langle a'|A|a\rangle - \langle a'|A|a\rangle = 0$，故 $\langle a'|a\rangle = 0$。实验上"谱线是分立的实数"这件事实，在数学上被厄米性一口吞下。

### 4.2 谱定理、投影算符与完备性

**谱定理**（有限维即厄米矩阵可对角化；无穷维是 von Neumann 的深刻定理）：厄米算符 $A$ 的本征矢构成 $\mathcal H$ 的一组正交归一完备基。离散情形写

$$A = \sum_n a_n\,|a_n\rangle\langle a_n| \equiv \sum_n a_n P_n, \qquad \sum_n P_n = \mathbb 1, \qquad P_nP_m = \delta_{nm}P_n,$$

其中 $P_n = |a_n\rangle\langle a_n|$ 是投向第 $n$ 条本征子空间的**投影算符**。恒等分解 $\sum_n|a_n\rangle\langle a_n| = \mathbb 1$ 叫**完备性关系**（closure），是狄拉克记号里使用频率最高的技巧：任何地方插入一个 $\mathbb 1$，抽象等式立刻变成具体表象下的分量等式（第 6 节全程演示）。

函数的算符也由谱定理定义：$f(A) \equiv \sum_n f(a_n)P_n$。第 7 节的演化算符 $U = e^{-iHt/\hbar}$ 就是这样定义的，不需要纠结算符级数的收敛性。

### 4.3 对易子与相容可观测量

对易子 $[A,B] \equiv AB - BA$ 度量两个算符"谁先谁后"的差异。核心定理：**两个厄米算符拥有共同完备本征基，当且仅当 $[A,B] = 0$**（严格说：当且仅当它们对应的投影算符族彼此对易）。证明（离散非简并情形）：若 $A|a\rangle = a|a\rangle$ 且 $[A,B]=0$，则 $A(B|a\rangle) = BA|a\rangle = a(B|a\rangle)$，即 $B|a\rangle$ 仍是本征值 $a$ 的本征矢；非简并迫使 $B|a\rangle \propto |a\rangle$，故 $|a\rangle$ 也是 $B$ 的本征矢。反方向：有共同本征基则 $[A,B]$ 在这组基上处处为零。

物理读法：**对易的可观测量可以同时测准**（相容），其共同本征基由一组"好量子数"标记——第 05 篇（[角动量](05-angular-momentum.md)）的 $\{H, L^2, L_z\} \to |n,l,m\rangle$ 与第 06 篇氢原子的全部记账都建立在这句话上。不相容的可观测量则由不确定关系给出代价（第 5.2 节）。

## 5. 测量公设

**公设 3（测量）**：对态 $|\psi\rangle$ 测量可观测量 $A$：

1. 结果必为 $A$ 的某个本征值 $a_n$；
2. **Born 规则**：得到 $a_n$ 的概率为 $P(a_n) = \lVert P_n|\psi\rangle \rVert^2 = \langle\psi|P_n|\psi\rangle$（非简并时即 $\lvert\langle a_n|\psi\rangle\rvert^2$）；
3. **坍缩**：测量后态变为 $P_n|\psi\rangle/\sqrt{P(a_n)}$——若紧接着再测 $A$，必得同一 $a_n$。

**期望值**与**标准差**：

$$\langle A\rangle \equiv \sum_n a_n P(a_n) = \langle\psi|A|\psi\rangle, \qquad (\Delta A)^2 = \langle A^2\rangle - \langle A\rangle^2 = \lVert(A - \langle A\rangle)|\psi\rangle\rVert^2 \ge 0.$$

注意 Born 规则里概率对 $|\psi\rangle$ 是**二次**的——这正是"振幅相加、概率开方"带来干涉的数学根源，也解释了为什么态的整体相位（以及叠加系数的公共相位）不可观测。

### 5.2 Robertson 不确定关系的完整推导

**定理**：对任意厄米算符 $A$、$B$ 与任意态 $|\psi\rangle$，

$$\Delta A\,\Delta B \ge \frac{1}{2}\big\lvert\langle[A,B]\rangle\big\rvert.$$

**推导**：记 $\bar A = A - \langle A\rangle$、$\bar B = B - \langle B\rangle$（仍厄米），定义未归一矢量 $|f\rangle = \bar A|\psi\rangle$、$|g\rangle = \bar B|\psi\rangle$。由 Schwarz 不等式（第 3.1 节），

$$(\Delta A)^2(\Delta B)^2 = \langle f|f\rangle\langle g|g\rangle \ge \lvert\langle f|g\rangle\rvert^2 = \lvert\langle\bar A\bar B\rangle\rvert^2.$$

把 $\bar A\bar B$ 拆成厄米与反厄米部分：

$$\bar A\bar B = \underbrace{\tfrac{1}{2}\{\bar A,\bar B\}}_{\text{厄米}} + \underbrace{\tfrac{1}{2}[\bar A,\bar B]}_{\text{反厄米}}, \qquad [\bar A,\bar B] = [A,B].$$

厄米算符的期望值是实数，反厄米算符的期望值是纯虚数，故 $\langle\bar A\bar B\rangle = \tfrac12\langle\{\bar A,\bar B\}\rangle + \tfrac12\langle[A,B]\rangle$ 的实部、虚部各占一项，模方为两者平方和：

$$\big\lvert\langle\bar A\bar B\rangle\big\rvert^2 = \frac{1}{4}\big\lvert\langle\{\bar A,\bar B\}\rangle\big\rvert^2 + \frac{1}{4}\big\lvert\langle[A,B]\rangle\big\rvert^2 \ge \frac{1}{4}\big\lvert\langle[A,B]\rangle\big\rvert^2. \qquad \blacksquare$$

丢弃反对易子项得到的就是 **Robertson（1929）形式**；保留它的更强版本有时叫 Schrödinger 形式。三个要点：

- 不等式的右边**依赖态**：若 $|\psi\rangle$ 恰使 $\langle[A,B]\rangle = 0$，该态下两量可以同时测准（如自旋单态里测某方向分量的对易子期望为零），不确定关系并不禁止逐态的巧合；
- 取等号的充要条件是 Schwarz 取等（$\bar A|\psi\rangle = \lambda\bar B|\psi\rangle$）且反对易子期望为零（$\lambda$ 纯虚）——高斯波包对 $(x,p)$ 正是这样取等的（自检问题 1）;
- 这不是"测量仪器不够好"的陈述，而是**态本身的性质**：在制备好的 $|\psi\rangle$ 的系综上反复测量，分布宽度就满足它。

## 6. 表象：从抽象矢量到波函数与矩阵

### 6.1 坐标表象：波函数是展开系数

取位置算符 $x$ 的本征"矢"$|x\rangle$ 作基。连续谱没有归一化本征矢，改用 **$\delta$ 归一化**：

$$x|x'\rangle = x'|x'\rangle, \qquad \langle x|x'\rangle = \delta(x - x'), \qquad \int_{-\infty}^{\infty} dx\,|x\rangle\langle x| = \mathbb 1.$$

把完备性插进 $|\psi\rangle = \mathbb 1|\psi\rangle$：

$$|\psi\rangle = \int dx\,|x\rangle\langle x|\psi\rangle \equiv \int dx\,\psi(x)\,|x\rangle, \qquad \psi(x) \equiv \langle x|\psi\rangle.$$

**波函数不是态本身，而是态矢量在坐标基下的展开系数**——就像欧氏空间里的 $(v_1, v_2, v_3)$ 不是矢量 $\vec v$ 本身。Born 规则的连续版本随之读出：$\lvert\psi(x)\rvert^2 dx$ 是位置落在 $[x, x+dx]$ 的概率，归一化 $\int dx\,\lvert\psi\rvert^2 = 1$ 即 $\langle\psi|\psi\rangle = 1$ 的分量写法。动量表象完全平行：$\tilde\psi(p) = \langle p|\psi\rangle$，$\langle p|p'\rangle = \delta(p - p')$。

### 6.2 $[x,p]=i\hbar$：全部量子力学的核心对易子

**公设**（正则对易关系）：

$$[x_i, p_j] = i\hbar\,\delta_{ij}\,\mathbb 1, \qquad [x_i, x_j] = [p_i, p_j] = 0.$$

它是"量子"在形式体系里的全部藏身之处：$\hbar \to 0$ 时一切对易，回到经典。两个直接后果：

- **坐标表象里 $p = -i\hbar\,d/dx$**。在 $\langle x|\cdots|\psi\rangle$ 中夹入对易关系可推出 $\langle x|p|\psi\rangle = -i\hbar\,\frac{d}{dx}\psi(x)$；反过来，平移算符 $T(a) = e^{-ipa/\hbar}$ 满足 $T(a)|x\rangle = |x + a\rangle$——动量是空间平移的生成元（完整推导见自检问题 4）。这套"对称性生成元 = 守恒量"的语法将在第 05 篇推广到旋转（生成元是 $\vec J$）。
- **Heisenberg 不确定关系**：代入 Robertson 不等式，$\Delta x\,\Delta p \ge \hbar/2$（自检问题 1）。

由 $[x,p] = i\hbar$ 还可推出坐标基与动量基之间的变换函数：$\langle x|p\rangle = (2\pi\hbar)^{-1/2}e^{ipx/\hbar}$——**动量表象与坐标表象之间是傅里叶变换**，这正是 de Broglie 关系 $p = \hbar k$ 在形式体系里的位置。

### 6.3 表象变换 = 幺正变换：两套语言的等价

设 $\{|a_n\rangle\}$、$\{|b_n\rangle\}$ 是两组正交归一完备基，则 $U = \sum_n|b_n\rangle\langle a_n|$ 满足 $U^\dagger U = \mathbb 1$：表象变换是**幺正变换**。它保持一切内积，故保持全部 Born 概率——物理预言与表象无关。

现在可以正式回答第 2.2 节的问题。**矩阵力学**取 $H$ 的本征基 $\{|E_n\rangle\}$：$H$ 对角，$x$、$p$ 是无穷维矩阵 $x_{mn} = \langle E_m|x|E_n\rangle$，运动方程是矩阵的对易子方程；**波动力学**取 $x$ 的本征基：$x$ 变成"乘以 $x$"、$p$ 变成 $-i\hbar\partial_x$，本征值方程 $H|\psi\rangle = E|\psi\rangle$ 变成微分方程 $\big[-\frac{\hbar^2}{2m}\partial_x^2 + V(x)\big]\psi = E\psi$。两者是同一些抽象算符在两组基下的矩阵表示，之间只隔一个幺正变换 $\langle x|E_n\rangle = \psi_n(x)$。Schrödinger 在 1926 年等价性论文里做的正是这件事；第 06s 篇（[矩阵力学解氢原子](06s-hydrogen-matrix-mechanics.md)）与第 06 篇（[氢原子波动力学](06-hydrogen-and-subshells.md)）解出同一组 $E_n = -13.6\,\text{eV}/n^2$，就是这条定理的实战演示。

## 7. 时间演化

**公设 4（演化）**：封闭体系的态矢量满足薛定谔方程

$$i\hbar\frac{d}{dt}|\psi(t)\rangle = H|\psi(t)\rangle,$$

其中哈密顿算符 $H$ 是厄米算符（经典 $H$ 的算符化；如何写出具体体系的 $H$ 是第 04、06 篇的事）。

### 7.1 演化算符及其幺正性

$H$ 不含时时形式解为

$$|\psi(t)\rangle = U(t)|\psi(0)\rangle, \qquad U(t) = e^{-iHt/\hbar} = \sum_n e^{-iE_nt/\hbar}\,|E_n\rangle\langle E_n|,$$

第二步用了谱定理（第 4.2 节）。$H$ 厄米 $\Rightarrow$ $U^\dagger U = e^{iHt/\hbar}e^{-iHt/\hbar} = \mathbb 1$：**演化是幺正的**。直接推论：内积与归一化不随时间改变，$\langle\phi(t)|\psi(t)\rangle = \langle\phi(0)|\psi(0)\rangle$——概率守恒是公设 4 的定理而非额外假设（自检问题 2）。能量本征态只积累相位 $e^{-iE_nt/\hbar}$：定态的"定"指全部物理概率分布不随时间变，动力学全在**叠加态各分量相对相位的赛跑**里。

### 7.2 守恒量 = 与 $H$ 对易

由 Ehrenfest 型的计算（见 7.4 节），$\frac{d}{dt}\langle A\rangle = \frac{1}{i\hbar}\langle[A,H]\rangle + \langle\partial A/\partial t\rangle$。故不显含时的 $A$ 满足 $[A,H] = 0$ 时 $\langle A\rangle$ 守恒——且更强：$A$ 的全部测量概率分布都不变。结合第 4.3 节，**守恒量与 $H$ 有共同本征基，提供好量子数**：中心势里 $\{H, L^2, L_z\}$ 给出 $|n,l,m\rangle$，第 05、06 篇的全部记账由此展开。对称性 $\leftrightarrow$ 生成元 $\leftrightarrow$ 守恒律这条金线，在量子力学里比经典力学（Noether）更直白。

### 7.3 三种绘景对照表

"谁随时间变"是约定而非物理：把 $U(t)$ 从态上搬到算符上，预言不变。三种常用约定：

| 绘景 | 态矢量 | 算符（不显含时） | 基本方程 | 何时好用 |
| --- | --- | --- | --- | --- |
| 薛定谔 | $\lvert\psi_S(t)\rangle = U\lvert\psi_S(0)\rangle$ 随时间变 | $A_S$ 不变 | $i\hbar\partial_t\lvert\psi_S\rangle = H\lvert\psi_S\rangle$ | 波动力学、定态问题（第 04、06 篇） |
| 海森堡 | $\lvert\psi_H\rangle = \lvert\psi_S(0)\rangle$ 冻结 | $A_H(t) = U^\dagger A_S U$ 随时间变 | $\frac{dA_H}{dt} = \frac{1}{i\hbar}[A_H, H]$ | 与经典方程对照、谐振子（第 04 篇）、自发辐射 |
| 相互作用（狄拉克） | $\lvert\psi_I(t)\rangle = e^{iH_0t/\hbar}\lvert\psi_S(t)\rangle$ 随 $V$ 变 | $A_I(t) = e^{iH_0t/\hbar}A_S e^{-iH_0t/\hbar}$ 随 $H_0$ 变 | $i\hbar\partial_t\lvert\psi_I\rangle = V_I(t)\lvert\psi_I\rangle$ | 含时微扰（第 07 篇）、Kubo 公式（第 10 篇） |

其中相互作用绘景针对 $H = H_0 + V$：把"已知的" $H_0$ 的演化搬给算符，态只感受微扰 $V$——第 07 篇（[微扰论](07-perturbation-theory.md)）的 Dyson 级数与第 10 篇（[线性响应](10-linear-response-kubo.md)）的 Kubo 公式都以它为工作语言。三者的期望值完全一致：$\langle\psi_S(t)|A_S|\psi_S(t)\rangle = \langle\psi_H|A_H(t)|\psi_H\rangle$，等式本身就是 $U$ 左右各乘一次的恒等变形。

### 7.4 Ehrenfest 定理

对 $H = \frac{p^2}{2m} + V(x)$，在海森堡绘景下（自检问题 5）：

$$\frac{d\langle x\rangle}{dt} = \frac{\langle p\rangle}{m}, \qquad \frac{d\langle p\rangle}{dt} = -\big\langle V'(x)\big\rangle \quad\Longrightarrow\quad m\frac{d^2\langle x\rangle}{dt^2} = -\big\langle V'(x)\big\rangle.$$

期望值走经典轨道——但注意右边是 $\langle V'(x)\rangle$ 而非 $V'(\langle x\rangle)$：波包越宽，两者差越远，"经典对应"只在波包远窄于势场变化尺度时成立。谐振子是例外中的例外：$V' = m\omega^2x$ 是线性的，$\langle V'(x)\rangle = m\omega^2\langle x\rangle$ 严格成立，期望值精确地做简谐振动（自检问题 5 联系第 04 篇）。

## 8. 密度算符初步

到目前为止的"态"都是纯态。但两类常见情形逼我们超越 ket：

- **系综**：只知道体系以概率 $p_i$ 处于 $|\psi_i\rangle$（如未极化的电子束：$1/2$ 概率 $|\uparrow\rangle$、$1/2$ 概率 $|\downarrow\rangle$）；
- **子系统**：只关心复合系统的一半（第 9 节），另一半的相干信息被"偏迹"丢掉。

**定义**：密度算符 $\rho \equiv \sum_i p_i\,|\psi_i\rangle\langle\psi_i|$，$p_i \ge 0$、$\sum_i p_i = 1$。三条性质刻画全部合法密度算符：

$$\rho = \rho^\dagger, \qquad \operatorname{Tr}\rho = 1, \qquad \rho \ge 0\ \text{（半正定）}.$$

观测预言改写为 $\langle A\rangle = \operatorname{Tr}(\rho A)$；演化由薛定谔方程推出 **von Neumann 方程**：

$$i\hbar\frac{d\rho}{dt} = [H, \rho]$$

——注意与经典统计力学 Liouville 方程 $i\partial_t\rho_{\text{cl}} = \{H, \rho_{\text{cl}}\}$ 的同构（泊松括号换成对易子 $/i\hbar$）。

**纯态判据**：$\rho^2 = \rho$（等价地 $\operatorname{Tr}\rho^2 = 1$）当且仅当系综里只有一个态，$\rho = |\psi\rangle\langle\psi|$；混态则 $\operatorname{Tr}\rho^2 < 1$。关键区分：叠加 $|\psi\rangle = (|{\uparrow}\rangle + |{\downarrow}\rangle)/\sqrt 2$ 是纯态（$\rho$ 有非对角元，可干涉，是 $S_x$ 的本征态），而 $p_\uparrow = p_\downarrow = 1/2$ 的混态 $\rho = \mathbb 1/2$ 没有任何方向可测出相干性——**相干叠加与统计混合是两回事，密度矩阵的非对角元是两者的分水岭**。

本篇点到为止：开系统、退相干、纠缠熵都从这里出发；第 10 篇（[线性响应](10-linear-response-kubo.md)）里热平衡系综 $\rho = e^{-\beta H}/Z$ 与 Kubo 公式 $\chi(\omega) \propto \operatorname{Tr}(\rho[A(t), B(0)])$ 会大量使用这套语言。

## 9. 复合系统与张量积

**公设 5（复合系统）**：子系统 $A$、$B$ 的态空间分别为 $\mathcal H_A$、$\mathcal H_B$，则总系统的态空间是张量积

$$\mathcal H_{AB} = \mathcal H_A \otimes \mathcal H_B,$$

基矢 $|a_i\rangle \otimes |b_j\rangle$，维数相乘：$\dim\mathcal H_{AB} = \dim\mathcal H_A \cdot \dim\mathcal H_B$。两个自旋 $1/2$：$\mathbb C^2 \otimes \mathbb C^2 = \mathbb C^4$，基 $\{|{\uparrow\uparrow}\rangle, |{\uparrow\downarrow}\rangle, |{\downarrow\uparrow}\rangle, |{\downarrow\downarrow}\rangle\}$。

张量积里藏着量子力学最反常的资源：一般态 $\sum_{ij}c_{ij}|a_i\rangle|b_j\rangle$ **不能**写成 $|\phi\rangle_A \otimes |\chi\rangle_B$ 的乘积形式——这就是纠缠（如单态 $(|{\uparrow\downarrow}\rangle - |{\downarrow\uparrow}\rangle)/\sqrt 2$）。只测子系统 $A$ 时，合法语言正是第 8 节的约化密度矩阵 $\rho_A = \operatorname{Tr}_B\rho$——纯态总系统的子系统可以是混态，这是密度矩阵不可或缺的第二个理由（纠缠的定量刻画——Schmidt 分解与纠缠熵——见第 14s 篇[量子信息初步](14s-quantum-information.md)）。

**全同粒子**：交换两个全同粒子物理态不变，要求多体态空间只取张量积的（反）对称子空间——玻色子取对称、费米子取反对称（Pauli 原理由此而来；完整展开见[第 05s 篇 全同粒子与对称化公设](05s-identical-particles.md)）。逐个施密特正交化的"一次量子化"写法在粒子数一多时就笨重不堪，更高效的记账方式是把态空间换成 Fock 空间、把算符换成产生湮灭算符——那是第 09 篇（[二次量子化](09-second-quantization.md)）的全部动机。

## 10. 接口：这套语法往后通到哪里

- **第 04 篇（[谐振子代数解法](04-harmonic-oscillator-ladder.md)）**：只用 $[x,p] = i\hbar$ 与谱定理，不碰任何微分方程——升降算符 $a, a^\dagger$ 是本篇"算符代数"路线的第一次全力展示。
- **第 05 篇（[角动量](05-angular-momentum.md)）**：把"对称性生成元"思想用到旋转，$[J_i, J_j] = i\hbar\varepsilon_{ijk}J_k$ 的谱由对易关系完全决定；好量子数 $(j, m)$ 是第 4.3 节相容可观测量定理的样板。
- **第 06 篇与 06s 篇**：氢原子的波动力学解法与矩阵力学解法，是第 6.3 节等价性定理的双面展示。
- **第 07 篇（[微扰论](07-perturbation-theory.md)）**：定态微扰是谱定理的近亲（本征问题的小变形），含时微扰全程住在相互作用绘景。
- **第 09 篇（[二次量子化](09-second-quantization.md)）**：张量积 + 全同粒子的工业化处理。
- **第 10 篇（[线性响应](10-linear-response-kubo.md)）**：密度矩阵 + 相互作用绘景的联合作业。

## 小结

- 五条公设：态 = 希尔伯特空间射线；可观测量 = 厄米算符；测量 = 谱定理 + Born 规则 + 坍缩；演化 = 幺正 $U = e^{-iHt/\hbar}$（薛定谔方程）；复合系统 = 张量积。
- 谱定理给出完备性 $\sum_n|a_n\rangle\langle a_n| = \mathbb 1$，是狄拉克记号的第一技巧；$[A,B]=0 \Leftrightarrow$ 共同本征基，是好量子数的全部来源。
- Robertson：$\Delta A\,\Delta B \ge \tfrac12\lvert\langle[A,B]\rangle\rvert$，由 Schwarz 不等式 + 厄米/反厄米分解两步推出；核心特例 $\Delta x\,\Delta p \ge \hbar/2$。
- 波函数 $\psi(x) = \langle x|\psi\rangle$ 是展开系数；连续谱用 $\delta$ 归一化；表象变换是幺正变换，矩阵力学与波动力学只差一组基。
- 三种绘景（薛定谔/海森堡/相互作用）物理等价，分工不同；Ehrenfest：期望值走经典轨道（谐振子严格成立）。
- 密度算符 $\rho$：厄米、归一、半正定；纯态 $\operatorname{Tr}\rho^2 = 1$；演化走 von Neumann 方程 $i\hbar\dot\rho = [H,\rho]$；第 10 篇大量复用。

## 自检问题

**1.** 由 $[x,p] = i\hbar$ 推出 $\Delta x\,\Delta p \ge \hbar/2$，并证明归一化高斯波包 $\psi(x) = (2\pi\sigma^2)^{-1/4}\exp(-x^2/4\sigma^2)$ 使等号成立。

<details markdown="1"><summary>点击显示答案</summary>

**推出**：Robertson 不等式 $\Delta A\,\Delta B \ge \tfrac12\lvert\langle[A,B]\rangle\rvert$（第 5.2 节已证）中取 $A = x$、$B = p$，代入 $[x,p] = i\hbar$：

$$\Delta x\,\Delta p \ge \frac{1}{2}\lvert\langle i\hbar\rangle\rvert = \frac{\hbar}{2}.$$

**高斯波包取等**：$\lvert\psi\rvert^2 = (2\pi\sigma^2)^{-1/2}e^{-x^2/2\sigma^2}$ 是方差 $\sigma^2$ 的高斯分布，由对称性 $\langle x\rangle = 0$，故 $(\Delta x)^2 = \sigma^2$。动量期望：$\langle p\rangle = -i\hbar\int\psi^{*}\psi'\,dx = 0$（$\psi'\propto x\psi$ 为奇函数）。$p^2 = -\hbar^2\partial_x^2$ 作用：

$$p^2\psi = -\hbar^2\left(\frac{x^2}{4\sigma^4} - \frac{1}{2\sigma^2}\right)\psi \;\Longrightarrow\; (\Delta p)^2 = \langle p^2\rangle = \frac{\hbar^2}{4\sigma^4}\sigma^2 \cdot 1 - \left(-\frac{\hbar^2}{2\sigma^2}\right) = \frac{\hbar^2}{4\sigma^2},$$

（用 $\langle x^2\rangle = \sigma^2$）。于是 $\Delta x\,\Delta p = \sigma\cdot\hbar/(2\sigma) = \hbar/2$，取等。

**为什么取等**（一般性判据）：第 5.2 节推导中等号要求 $\bar A|\psi\rangle = \lambda\bar B|\psi\rangle$ 且 $\lambda$ 纯虚。这里 $\langle x\rangle = \langle p\rangle = 0$，而

$$p\,\psi = -i\hbar\,\frac{-x}{2\sigma^2}\psi = \frac{i\hbar}{2\sigma^2}\,x\,\psi,$$

即 $p|\psi\rangle = \lambda x|\psi\rangle$、$\lambda = i\hbar/2\sigma^2$ 纯虚——两个条件同时满足，故高斯波包是最小不确定波包。

</details>

**2.** 证明幺正演化保持内积与归一化，并由此说明 Born 规则给出的总概率恒为 1（概率守恒）。

<details markdown="1"><summary>点击显示答案</summary>

**内积不变**：$|\psi(t)\rangle = U(t)|\psi(0)\rangle$、$|\phi(t)\rangle = U(t)|\phi(0)\rangle$，故

$$\langle\phi(t)|\psi(t)\rangle = \langle\phi(0)|U^\dagger(t)U(t)|\psi(0)\rangle = \langle\phi(0)|\psi(0)\rangle,$$

用到 $U^\dagger U = \mathbb 1$（$U = e^{-iHt/\hbar}$ 而 $H = H^\dagger$，故 $U^\dagger = e^{+iHt/\hbar} = U^{-1}$）。取 $|\phi\rangle = |\psi\rangle$ 即得归一化保持：$\langle\psi(t)|\psi(t)\rangle = 1$ 对所有 $t$ 成立。

**概率守恒**：对任意完备本征基 $\{|a_n\rangle\}$（Born 规则给出的测量 $A$ 的概率分布），

$$\sum_n P(a_n, t) = \sum_n \lvert\langle a_n|\psi(t)\rangle\rvert^2 = \sum_n \langle\psi(t)|a_n\rangle\langle a_n|\psi(t)\rangle = \langle\psi(t)|\psi(t)\rangle = 1,$$

中间一步用了完备性关系 $\sum_n|a_n\rangle\langle a_n| = \mathbb 1$。逻辑链：薛定谔方程 + $H$ 厄米 $\Rightarrow$ 演化幺正 $\Rightarrow$ 归一化保持 $\Rightarrow$ 任意时刻 Born 概率归一。**公设 3 与公设 4 是自洽的**：归一化只需要在制备时做一次，演化永不破坏它。

（连续谱版本同样成立：坐标表象里 $\frac{d}{dt}\int\lvert\psi\rvert^2dx = 0$ 由概率流连续性方程 $\partial_t\rho + \nabla\cdot\vec j = 0$ 给出，$\vec j = \frac{\hbar}{m}\operatorname{Im}(\psi^{*}\nabla\psi)$——那是这条抽象定理在坐标表象下的微分形式。）

</details>

**3.** 自旋 $1/2$ 粒子处于沿 $z$ 方向的磁场中，$H = \frac{\hbar\omega}{2}\sigma_z$（$\omega = eB/m_ec$ 取大小）。$t = 0$ 时制备在 $S_x$ 本征值 $+\hbar/2$ 的态。求 $t$ 时刻测 $S_x$ 得 $\pm\hbar/2$ 的概率，并计算 $\langle S_x(t)\rangle$、$\langle S_y(t)\rangle$。（完整矩阵计算。）

<details markdown="1"><summary>点击显示答案</summary>

**初态**：$S_x = \frac{\hbar}{2}\sigma_x$ 的本征值 $+\hbar/2$ 对应 $\sigma_x$ 本征值 $+1$ 的本征矢

$$|{+x}\rangle = \frac{1}{\sqrt 2}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \frac{1}{\sqrt 2}\big(|{\uparrow}\rangle + |{\downarrow}\rangle\big).$$

**演化算符**：$\sigma_z$ 对角，故

$$U(t) = e^{-iHt/\hbar} = e^{-i\omega t\sigma_z/2} = \begin{pmatrix} e^{-i\omega t/2} & 0 \\ 0 & e^{i\omega t/2} \end{pmatrix}, \qquad |\psi(t)\rangle = \frac{1}{\sqrt 2}\begin{pmatrix} e^{-i\omega t/2} \\ e^{i\omega t/2} \end{pmatrix}.$$

**测 $S_x$ 的概率**：$|{\pm x}\rangle = \frac{1}{\sqrt 2}(1, \pm 1)^T$，振幅

$$\langle {+x}|\psi(t)\rangle = \frac{1}{2}\big(e^{-i\omega t/2} + e^{i\omega t/2}\big) = \cos\frac{\omega t}{2}, \qquad \langle {-x}|\psi(t)\rangle = \frac{1}{2}\big(e^{-i\omega t/2} - e^{i\omega t/2}\big) = -i\sin\frac{\omega t}{2}.$$

$$P\big(S_x = +\tfrac{\hbar}{2}\big) = \cos^2\frac{\omega t}{2}, \qquad P\big(S_x = -\tfrac{\hbar}{2}\big) = \sin^2\frac{\omega t}{2}, \qquad \text{和} = 1\ \checkmark$$

$t = \pi/\omega$ 时自旋完全翻到 $-x$——这就是 **Rabi 振荡 / 自旋进动**。

**期望值**：

$$\langle S_x\rangle = \frac{\hbar}{2}\big(P_+ - P_-\big) = \frac{\hbar}{2}\cos\omega t, \qquad \langle S_y\rangle = \frac{\hbar}{2}\psi^\dagger\sigma_y\psi = \frac{\hbar}{2}\sin\omega t, \qquad \langle S_z\rangle = 0.$$

（$\psi^\dagger\sigma_y\psi = \tfrac12(e^{i\omega t/2}, e^{-i\omega t/2})(0,-i;i,0)(e^{-i\omega t/2}, e^{i\omega t/2})^T = \tfrac{i}{2}(e^{-i\omega t} - e^{i\omega t}) = \sin\omega t$。）自旋期望矢量以角频率 $\omega$ 绕 $z$ 轴（磁场方向）进动——第 5、7 节语法在 $\mathbb C^2$ 上的完整闭环：制备（公设 1）→ 演化（公设 4）→ 测量分布（公设 3）。

</details>

**4.** 从 $[x,p] = i\hbar$ 推出坐标表象中 $\langle x|p|\psi\rangle = -i\hbar\,\frac{d}{dx}\psi(x)$，并证明平移算符 $T(a) = e^{-ipa/\hbar}$ 满足 $T(a)|x\rangle = |x+a\rangle$（动量是平移生成元）。

<details markdown="1"><summary>点击显示答案</summary>

**第一步（动量算符的微分形式）**：在对易关系左乘 $\langle x|$、右乘 $|\psi\rangle$ 之前，先建立 $|x\rangle$ 基下 $p$ 的矩阵元。利用 $\langle x|p\rangle = (2\pi\hbar)^{-1/2}e^{ipx/\hbar}$（第 6.2 节，本身由对易关系推出：$\langle x|[x,p]|p\rangle = i\hbar\langle x|p\rangle$ 给出 $x\langle x|p\rangle = i\hbar\,\partial_p\langle x|p\rangle$ 之外，更直接的做法如下）——用平移论证反推最干净，我们把两步合一：

定义平移算符 $T(a)$ 为把波函数整体搬运 $a$ 的算符：$\langle x|T(a)|\psi\rangle \equiv \psi(x - a)$（波函数向右移 $a$，在 $x$ 处取值等于原函数在 $x-a$ 处的值）。对无穷小 $a = \epsilon$ 展开：

$$\psi(x - \epsilon) = \psi(x) - \epsilon\,\frac{d\psi}{dx} + O(\epsilon^2) = \langle x|\left(\mathbb 1 - \frac{i\epsilon}{\hbar}\,p\right)|\psi\rangle + O(\epsilon^2),$$

第二步是 $T(\epsilon) = e^{-ip\epsilon/\hbar} \approx \mathbb 1 - i\epsilon p/\hbar$ 的定义。比较 $O(\epsilon)$ 项：

$$-\langle x|\frac{ip}{\hbar}|\psi\rangle = -\frac{d\psi}{dx} \;\Longrightarrow\; \boxed{\langle x|p|\psi\rangle = -i\hbar\,\frac{d}{dx}\psi(x)}.$$

**验证与对易关系自洽**：$\langle x|[x,p]|\psi\rangle = x(-i\hbar\psi') - (-i\hbar)(x\psi)' = -i\hbar x\psi' + i\hbar\psi + i\hbar x\psi' = i\hbar\psi(x) = \langle x|i\hbar|\psi\rangle$ ✓——微分形式确实实现了 $[x,p] = i\hbar$。

**第二步（有限平移）**：$T(a) = e^{-ipa/\hbar}$ 与 $x$ 的对易关系由 $[p, x] = -i\hbar$ 经 Baker–Campbell–Hausdorff（$[p, f(x)] = -i\hbar f'(x)$）得 $T^\dagger(a)\,x\,T(a) = x + a$。于是

$$x\,\big(T(a)|x'\rangle\big) = T(a)\,T^\dagger(a)\,x\,T(a)|x'\rangle = T(a)(x' + a)|x'\rangle = (x' + a)\,\big(T(a)|x'\rangle\big),$$

即 $T(a)|x'\rangle$ 是 $x$ 的本征值为 $x' + a$ 的本征矢：$T(a)|x'\rangle = |x' + a\rangle$（相位约定内）。取厄米共轭 $\langle x|T(a) = \langle x - a|$，立即还原第一步的定义 $\langle x|T(a)|\psi\rangle = \psi(x-a)$。**闭环**：对易关系 $\leftrightarrow$ 微分表示 $\leftrightarrow$ 平移生成元，三者等价——这套"对称性生成元"逻辑在第 05 篇会原样搬到旋转与角动量。

</details>

**5.** 在海森堡绘景下推导 Ehrenfest 定理，并对谐振子 $H = p^2/2m + \frac12 m\omega^2x^2$ 验证期望值精确服从经典运动方程（联系第 04 篇）。

<details markdown="1"><summary>点击显示答案</summary>

**一般推导**：海森堡算符 $A_H(t) = U^\dagger A_S U$，$U = e^{-iHt/\hbar}$。求导（$A_S$ 不显含时）：

$$\frac{dA_H}{dt} = \frac{dU^\dagger}{dt}A_S U + U^\dagger A_S\frac{dU}{dt} = \frac{iH}{\hbar}U^\dagger A_S U - U^\dagger A_S\frac{iH}{\hbar}U = \frac{1}{i\hbar}[A_H, H],$$

（$H$ 与 $U$ 对易，可自由穿过）。取期望即 $\frac{d}{dt}\langle A\rangle = \frac{1}{i\hbar}\langle[A,H]\rangle$（$|\psi_H\rangle$ 冻结，时间依赖性全在算符上）。

**对 $x$、$p$ 计算**：$H = p^2/2m + V(x)$，用 $[x, p^2] = 2i\hbar p$（由 $[x,p] = i\hbar$ 归纳）与 $[p, V(x)] = -i\hbar V'(x)$（自检问题 4 的 BCH 引理）：

$$\frac{dx_H}{dt} = \frac{1}{i\hbar}[x, H] = \frac{1}{i\hbar}\cdot\frac{2i\hbar p}{2m} = \frac{p_H}{m}, \qquad \frac{dp_H}{dt} = \frac{1}{i\hbar}[p, V(x)] = -V'(x_H).$$

取期望：$m\frac{d^2\langle x\rangle}{dt^2} = \frac{d\langle p\rangle}{dt} = -\langle V'(x)\rangle$——Ehrenfest 定理。

**谐振子验证**：$V'(x) = m\omega^2x$ 线性，故 $\langle V'(x)\rangle = m\omega^2\langle x\rangle$ **严格成立**（无波包宽度修正）：

$$m\frac{d^2\langle x\rangle}{dt^2} = -m\omega^2\langle x\rangle \;\Longrightarrow\; \langle x\rangle(t) = \langle x\rangle_0\cos\omega t + \frac{\langle p\rangle_0}{m\omega}\sin\omega t,$$

期望值精确做经典简谐振动。**联系第 04 篇**（[谐振子代数解法](04-harmonic-oscillator-ladder.md)）：海森堡绘景下升降算符的演化极简——

$$\frac{da_H}{dt} = \frac{1}{i\hbar}[a, \hbar\omega(a^\dagger a + \tfrac12)] = -i\omega\,a_H \;\Longrightarrow\; a_H(t) = a(0)e^{-i\omega t},$$

代回 $x_H(t) = \sqrt{\hbar/2m\omega}\,(a_H + a_H^\dagger) = x(0)\cos\omega t + \frac{p(0)}{m\omega}\sin\omega t$——**算符本身服从经典解的形式**，取期望即上式。谐振子是"量子力学里经典味道最浓"的系统：对易子把非对易性锁进 $[x(t), x(t')] \neq 0$ 这类等时/异时关系里，而期望值层面与经典不可区分。

</details>

## 参考

- Sakurai《Modern Quantum Mechanics》第 1 章（Fundamental Concepts）：狄拉克记号、公设、相容可观测量与本篇第 3–5、7 节一一对应（自旋 $1/2$ 教具的出处）。
- Shankar《Principles of Quantum Mechanics》第 1 章（数学准备：线性代数与狄拉克记号）与第 4 章（公设）：公设的完整陈述、Robertson 推导与 Ehrenfest 定理。
- Griffiths《量子力学概论》第 3 章（形式理论）：希尔伯特空间语言对波动力学的重写，连续谱 $\delta$ 归一化的细心处理。
- Dirac《The Principles of Quantum Mechanics》第 1–3 章：bra/ket 记号与表象理论的原始表述（第 6 节的历史源头）。
- von Neumann《Mathematical Foundations of Quantum Mechanics》第 2、5、6 章：希尔伯特空间公理化、谱定理与密度算符的严格数学基础（第 4、8 节的进阶阅读）。
