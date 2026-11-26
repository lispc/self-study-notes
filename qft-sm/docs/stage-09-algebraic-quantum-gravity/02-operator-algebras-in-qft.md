# QFT 中的算子代数：从 GNS 到型分类

> 路线图位置：第 9 阶段（代数量子引力专题）· 第 2 篇
> 前置知识：量子力学书 9s2（C*-代数、GNS 构造、Haag 定理）；第 4 阶段 01 篇（标量场量子化）；线性代数（有限维例子先行）。
> 学习目标：会用 GNS 构造把"态"变成"表示"；能区分 I/II/III 型因子并说出判据（极小投影、迹、投影等价类）；理解局域代数为什么是 III₁ 型、有限系统为什么是 $B(\mathcal H)$；知道"纯态延拓 + 型 I 因子"在代数量子引力中的作用，以及它与局域 QFT 的 III 型为什么不矛盾。

---

**单位约定**：本篇取自然单位 $\hbar = c = 1$（首次说明）。

## 1. 一句话总结

**代数 QFT 先把可观测量组织成局域 C*-代数，再用态经 GNS 构造造出表示；von Neumann 代数的 Murray–von Neumann 型分类（I/II/III）刻画"有没有极小投影、有没有迹"；自由场的局域代数是既无迹又无极小投影的 III₁ 型，因此连续 QFT 里"密度矩阵与冯诺依曼熵"没有直接意义；而有限 $G_N$ 的因果菱形代数在纯高斯态下给出不可约表示，$\pi_\omega(\mathcal A)'' = B(\mathcal H)$ 是 I 型——有限维 Hilbert 空间与熵计数由此成为可能。**

## 2. 从 C*-代数到局域代数

### 2.1 为什么先代数后表示

9s2 的教训：无穷自由度下 CCR/CAR 的不可约表示不可数多且彼此不等价（van Hove 现象、Haag 定理）。若把"Fock 空间"当作定义，就等于偷偷选了一个表示。代数路线把顺序倒过来：

1. 先给定**代数** $\mathcal A$（可观测量与它们的代数关系）；
2. 再给定**态** $\omega$（正、归一的线性泛函，即一套自洽的期望值规则）；
3. 态经 **GNS 构造**生成 Hilbert 空间与表示。

代数绝对，表示随态——这是整个第 9 阶段的语法基础。

### 2.2 Haag–Kastler 公理

局域代数把"时空区域"编码进代数：

$$\mathcal O \;\longmapsto\; \mathcal A(\mathcal O),$$

$\mathcal O$ 跑遍时空中的有界开区域。公理（陈述级）：

- **isotony**：$\mathcal O_1 \subset \mathcal O_2 \Rightarrow \mathcal A(\mathcal O_1)\subset \mathcal A(\mathcal O_2)$；
- **局域性**：类空间隔的区域，其代数元对易；
- **协变性**：Poincaré 群（或时空等距群）自同构作用于网；
- **谱条件**：能量–动量谱在前向光锥内；
- **真空唯一**：存在唯一的 Poincaré 不变态。

$\mathcal A$ 的全网加上范数闭包，构成一个 C*-代数；真空态 $\omega_0$ 的 GNS 表示就是通常的 Fock 表示。

### 2.3 自由场的 Weyl 代数

自由标量场的局域代数由**涂抹的 Weyl 算符**生成：

$$W(f) = e^{i\phi(f)},\qquad \phi(f) = \int\mathrm{d}^3x\,f(\mathbf x)\,\phi(\mathbf x),$$

满足 Weyl 关系

$$W(f)W(g) = e^{-i\sigma(f,g)/2}\,W(f+g),$$

其中 $\sigma(f,g)$ 是经典场解空间上的辛形式（第 4 阶段的等时对易子就是它的量子影子）。Weyl 代数就是 CCR 代数；有限自由度时由 Stone–von Neumann 定理唯一，无穷自由度时表示不唯一。

## 3. 态与 GNS 构造

### 3.1 态

**态**是正、归一的线性泛函 $\omega:\mathcal A\to\mathbb C$：

$$\omega(A^*A)\ge 0,\qquad \omega(\mathbb 1) = 1.$$

- **纯态**：不能写成两个不同态的凸组合；
- **混合态**：否则；
- **KMS 态**：满足

$$\omega_\beta(A\,\alpha_{t}(B)) = \omega_\beta(\alpha_{t+i\beta}(B)\,A),$$

其中 $\alpha_t$ 是时间平移自同构。这是"热平衡"的代数定义：虚时平移 $i\beta$ 把 $A$ 从右边搬到左边。有限维时它等价于 $\rho = e^{-\beta H}/Z$；无穷自由度时它是热态的定义（因为密度矩阵可能不存在）。

### 3.2 GNS 构造

给定 $\mathcal A$ 与 $\omega$：

1. 在代数上定义内积 $\langle A|B\rangle_\omega \equiv \omega(A^*B)$（半正定）；
2. 商去零范数子空间 $\mathcal N = \{A:\omega(A^*A)=0\}$，完备化得 Hilbert 空间 $\mathcal H_\omega$；
3. 左乘给出表示 $\pi_\omega(A)|B\rangle = |AB\rangle$；
4. 循环矢量 $|\Omega_\omega\rangle = |\mathbb 1\rangle$，满足 $\langle\Omega_\omega|\pi_\omega(A)|\Omega_\omega\rangle = \omega(A)$。

结论：**每个态都给出一个表示，且表示中有循环矢量**；$\omega$ 是纯态当且仅当 $\pi_\omega$ 不可约（自检 3）。

### 3.3 有限维例子：$M_2(\mathbb C)$

取 $\mathcal A = M_2(\mathbb C)$，态 $\omega(A) = \operatorname{Tr}(\rho A)$，$\rho = \mathrm{diag}(p,1-p)$。

GNS 空间 $\mathcal H_\omega = M_2$（作为 4 维复矢量空间），内积 $\langle A|B\rangle = \operatorname{Tr}(\rho A^*B)$；表示 $\pi(A)|B\rangle = |AB\rangle$；循环矢量 $|\Omega\rangle = |\mathbb 1\rangle$。取 $\rho = |0\rangle\langle 0|$ 时，零范数子空间是 $\{A: A|0\rangle = 0\}$，商掉后 $\mathcal H_\omega \cong \mathbb C^2$，表示就是标准表示（自检 2）。

### 3.4 表示与态：真空 vs 热态

同一代数，不同态给出不同表示：

- 真空 $\omega_0$ 的 GNS 表示 = Fock 表示；
- 热态（KMS 态）的 GNS 表示一般与 Fock 表示**不等价**（热态包含任意多粒子，且是混合的）；
- 不同相（如对称破缺的不同真空）给出真正不等价的表示。

"选表示"不是数学偏好，而是选物理态。

## 4. von Neumann 代数与型分类

### 4.1 从 C*-代数到 von Neumann 代数

$\mathcal A$ 的 GNS 表示取弱闭包，得到 **von Neumann 代数** $\mathcal M = \pi_\omega(\mathcal A)''$（双重交换子定理：$\mathcal M'' = \mathcal M$）。型分类是 von Neumann 代数（而非 C*-代数）的不变量。

### 4.2 因子

$\mathcal M$ 的**中心**是 $\mathcal Z(\mathcal M) = \mathcal M\cap\mathcal M'$。若 $\mathcal Z = \mathbb C\mathbb 1$，称 $\mathcal M$ 为**因子**。因子的意义：它不能再分解成直和，对应"单相"的物理系统。

$B(\mathcal H)$ 是因子：与所有算符对易的只有 $c\mathbb 1$（自检 1）。

### 4.3 三类因子

| 型 | 判据 | 典型例子 |
|---|---|---|
| I | 有极小投影；$\cong B(\mathcal H)$ | 有限维系统 $M_n(\mathbb C)$、格点模型、Fock 表示 |
| II$_1$ | 有有限迹、无极小投影 | 有限温度热力学极限的某些代数 |
| II$_\infty$ | 有半有限迹但迹无穷 | 跨越 II$_1$ 与 III 的构造 |
| III | 无迹；非零投影互相等价 | 自由场的局域代数（III₁） |

**I 型再细分**：$B(\mathcal H)$ 的维数给出 $I_n$（$\mathcal H$ 为 $n$ 维）与 $I_\infty$（无穷维）。I 型的判据是"有极小投影"——可以找到不能再细分的"原子"态。

### 4.4 迹的意义

- I 型：迹 $\operatorname{Tr}$ 存在，密度矩阵 $\rho$ 存在，$S = -\operatorname{Tr}\rho\ln\rho$ 可用；
- II 型：迹存在（半有限），可定义密度矩阵与熵，但无极小投影（连续谱）；
- III 型：**没有迹**——任何两个非零投影都等价，密度矩阵与冯诺依曼熵没有意义（自检 4）。

## 5. 局域代数的型：为什么是 III₁

### 5.1 物理图像

任意小区域 $\mathcal O$ 里有**无穷多自由度**（场在任意小的体积里仍有无限多模式）。这导致：

- 每个非零投影都等价于整个空间的投影（没有"最小"的量子）；
- 于是不存在迹（自检 4 的论证），也不存在密度矩阵。

严格结论（自由场）：$\mathcal A(\mathcal O)''$（在真空表示中）是 **III₁ 型因子**。这个结论与 $\mathcal O$ 多小无关，只要它有非空内部。

### 5.2 后果：纠缠熵是"相对量"

连续 QFT 中，区域 $A$ 与补集的纠缠熵是紫外发散的（面积律 $\times$ 截断），因为 $A$ 的代数没有密度矩阵；有意义的量是**相对熵** $S(\rho\|\sigma)$ 与"分割依赖"的熵差。物理上常用的"纠缠熵"总是带着截断（格点、$\epsilon$ 切、或相对熵的参考态）。

### 5.3 split 性质与有限系统

- **split 性质**：若两个区域之间有"collar"，则存在中间的 I 型因子 $\mathcal N$ 使 $\mathcal A(\mathcal O_1)\subset\mathcal N\subset\mathcal A(\mathcal O_2)$。这让某些"带 collar"的构造可以把区域局部近似成 I 型，但局域代数本身仍是 III 型。
- **有限格点**：自由度有限，代数是 $B(\mathcal H)$，I 型，密度矩阵与熵全部良好。连续极限才是 III 型出现的地方——与 9s2 的 Haag 定理故事同构：有限自由度万事大吉，无穷自由度群魔乱舞。

## 6. 代数量子引力中的用法：论文的逻辑

### 6.1 论文构造了什么

论文 §4.2 的步骤（对应 (4.7)–(4.17)）：

1. 固定角点面积 $A$，把入射零锥上的辐射模式与角点边缘模展开成可数多组正则对 $(q_j,p_j)$；
2. 选一个**高斯态** $|\Omega_A\rangle$（每个正则对的中心与宽度给定），激发它得到 Fock 空间 $K_A$；
3. 边界源生成的算符在 $K_A$ 上可以逼近任意秩一投影，故入射可观测量代数满足 $\mathcal M_A = B(K_A)$——**I 型**；
4. 再把这个"固定面积子代数"上的纯态延拓为全代数 $\mathcal A$ 上的纯态 $\omega$，取 GNS 表示，得

$$\pi_\omega(\mathcal A)'' = B(\mathcal H_\omega).$$

### 6.2 为什么能是 I 型：纯态 + Fock 表示

关键定理：**纯态的 GNS 表示不可约**（自检 3）。于是 $\pi_\omega(\mathcal A)'' = B(\mathcal H_\omega)$ 自动成立——这是纯态的普遍性质，不依赖动力学的细节。

对 CCR/Weyl 代数，Fock 表示本身就是不可约的：纯高斯态给出的就是 Fock 表示，故 $\pi_\omega(\mathcal A)'' = B(\mathcal H_\omega)$，是 I 型（无穷维时 $I_\infty$）。这与 JT 引力的结论一致（第 3 篇：type $I_\infty$ 且迹发散）。

### 6.3 与局域 QFT 的 III 型不矛盾

论文的代数**不是**某个局域场代数 $\mathcal A(\mathcal O)$：

- 它包含边界数据与边缘模（角点面积、boost 角、角度嵌入），不是"区域内部的场算符"；
- 它是在**固定角点面积**的子空间上构造的，且选的是**纯**高斯态；真空在局域区域上的限制是**混**态（与补集纠缠），所以局域代数给 III 型；
- 有限 $G_N$ 的截断使自由度有效有限（时钟投影后甚至有限维），I 型是自然的。

一句话：**"纯态 + Fock 表示 ⇒ I 型"与"真空在局域区域上 ⇒ III 型"是两套代数、两套态，不冲突。**

### 6.4 熵与密度矩阵

I 型的好处是熵可以直接算。取 $\rho_D = e^{-\hat A/(4G_N)}/Z_{D,1}$，则

$$S(\rho_D) = -\operatorname{Tr}\rho_D\ln\rho_D = \frac{\langle\hat A\rangle}{4G_N} + \ln Z_{D,1},$$

正是论文 (5.50)。若代数是 III 型，这一步无从谈起（没有 $\rho_D$）——这就是为什么"选对代数与态"是代数量子引力计熵的前提。

### 6.5 纯态延拓：Kadison–Singer

论文引用 Kadison–Singer 定理：**子代数上的纯态可以延拓为全代数上的纯态**（并且可以要求延拓保持纯性）。这一步保证：

- 入射子代数上的纯高斯态能延拓到包含"改变面积"算符的全代数；
- 延拓后表示不可约，型 I 因子的结论不被破坏；
- 但延拓不唯一——论文脚注 20 明确把"不同 $\omega$ 是否给出幺正等价的表示"留作未来工作。这是本篇需要记住的开放点。

## 7. 小结

- 代数路线：先代数（可观测量与关系），再态（正归一泛函），再 GNS 表示；表示随态，代数绝对。
- GNS 三元组 $(\mathcal H_\omega,\pi_\omega,\Omega_\omega)$：循环矢量、左乘表示；纯态 $\Leftrightarrow$ 表示不可约。
- von Neumann 代数分型：I（有极小投影，$\cong B(\mathcal H)$）、II（有迹、无原子）、III（无迹、投影等价）；局域场代数是 III₁，因此没有密度矩阵与冯诺依曼熵。
- 有限自由度/格点是 I 型；split 性质提供"带 collar 的 I 型近似"，但局域代数本身仍是 III 型。
- 论文的因果菱形代数：固定面积 + 纯高斯态 + GNS ⇒ $B(\mathcal H_\omega)$ 是 I 型；密度矩阵存在，$S = \langle A\rangle/4G_N + \ln Z$；纯态延拓（Kadison–Singer）保证不可约性，但延拓的唯一性未定。

## 自检问题

**1.** 证明 $B(\mathcal H)$ 是因子：其中心只有 $c\mathbb 1$。

<details markdown="1"><summary>点击显示答案</summary>

设 $T\in B(\mathcal H)$ 与所有算符对易。取任意两个矢量 $\lvert\psi\rangle,\lvert\phi\rangle$，考察秩一算符 $\lvert\psi\rangle\langle\phi\rvert$：

$$T\lvert\psi\rangle\langle\phi\rvert = \lvert\psi\rangle\langle\phi\rvert T\quad\text{对所有 }\psi,\phi.$$

两边作用在任意 $\lvert\chi\rangle$ 上：

$$T\lvert\psi\rangle\langle\phi\vert\chi\rangle = \lvert\psi\rangle\langle\phi\vert T\vert\chi\rangle \;\Longrightarrow\; \langle\phi\vert\chi\rangle\,T\lvert\psi\rangle = \langle\phi\vert T\vert\chi\rangle\,\lvert\psi\rangle.$$

固定 $\psi$，取 $\chi$ 使 $\langle\phi|\chi\rangle \neq 0$，则 $T\lvert\psi\rangle$ 正比于 $\lvert\psi\rangle$：$T\lvert\psi\rangle = c(\psi)\lvert\psi\rangle$。再用两个线性无关的 $\psi_1,\psi_2$ 与 $T$ 的线性性证明 $c(\psi_1) = c(\psi_2)$：

$$T(\lvert\psi_1\rangle + \lvert\psi_2\rangle) = c(\psi_1+\psi_2)(\lvert\psi_1\rangle+\lvert\psi_2\rangle) = c(\psi_1)\lvert\psi_1\rangle + c(\psi_2)\lvert\psi_2\rangle,$$

比较系数得 $c(\psi_1+\psi_2) = c(\psi_1) = c(\psi_2) \equiv c$。故 $T = c\mathbb 1$。中心平凡，$B(\mathcal H)$ 是因子。$\square$

若 $\mathcal H$ 有限维，$B(\mathcal H)\cong M_n(\mathbb C)$，是 $I_n$ 型；无穷维时是 $I_\infty$ 型。两者都有极小投影（秩一投影），这是 I 型的标志。

</details>

**2.** 对 $\mathcal A = M_2(\mathbb C)$、$\omega(A) = \operatorname{Tr}(\rho A)$：构造 GNS 三元组；分别取 $\rho = \mathrm{diag}(p,1-p)$ 与 $\rho = \lvert0\rangle\langle0\rvert$，说明表示与空间的变化。

<details markdown="1"><summary>点击显示答案</summary>

**构造**：$\mathcal H_\omega = M_2(\mathbb C)$（4 维），内积

$$\langle A|B\rangle_\omega = \operatorname{Tr}(\rho A^*B).$$

正定性：$\langle A|A\rangle = \operatorname{Tr}(\rho A^*A) \ge 0$，等号当且仅当 $\sqrt\rho A = 0$。表示 $\pi(A)\lvert B\rangle = \lvert AB\rangle$；循环矢量 $\lvert\Omega\rangle = \lvert\mathbb 1\rangle$。验证：

$$\langle\Omega\vert\pi(A)\vert\Omega\rangle = \operatorname{Tr}(\rho\,\mathbb 1^* A\,\mathbb 1) = \operatorname{Tr}(\rho A) = \omega(A),$$

且 $\pi(B)\lvert\Omega\rangle = \lvert B\rangle$，故 $\Omega$ 循环。$\pi(A)^\dagger = \pi(A^*)$ 由内积定义直接验证：

$$\langle X\vert\pi(A)^\dagger\vert Y\rangle = \langle\pi(A)X\vert Y\rangle = \operatorname{Tr}(\rho X^*A^*Y) = \langle X\vert\pi(A^*)Y\rangle.$$

**$\rho = \mathrm{diag}(p,1-p)$，$0 \lt p \lt 1$**：内积非退化，$\mathcal H_\omega$ 是 4 维；表示 $A\mapsto$ 左乘，可分解成两个不可约分量（左乘作用在"行"指标上，列指标给出二重简并），故**表示可约**——$\omega$ 是混合态。

**$\rho = \lvert0\rangle\langle0\rvert$**：$\langle A|A\rangle = \langle0\vert A^*A\vert0\rangle = \lVert A\vert0\rangle\rVert^2$。零范数子空间为 $\{A: A\lvert0\rangle = 0\}$（一维复子空间）。商掉后，$\lvert B\rangle\mapsto B\lvert0\rangle$ 给出同构 $\mathcal H_\omega\cong\mathbb C^2$；表示 $\pi(A)$ 就是 $A$ 在 $\mathbb C^2$ 上的标准作用，$\Omega = \lvert0\rangle$。这是不可约表示——与"$\rho$ 是秩一投影 $\Leftrightarrow\omega$ 纯"一致。

这个例子把 GNS 的三件事一次演完：内积、商零范数、纯态给出不可约表示。

</details>

**3.** 证明：若 $\omega$ 是纯态，则 GNS 表示不可约（即 $\pi_\omega(\mathcal A)' = \mathbb C\mathbb 1$）。

<details markdown="1"><summary>点击显示答案</summary>

反证。设表示可约，则存在非平凡投影 $E\in\pi_\omega(\mathcal A)'$，$E\neq 0,\mathbb 1$。令 $\lambda = \langle\Omega|E|\Omega\rangle$；由 $0 \lt E \lt \mathbb 1$ 得 $0 \lt \lambda \lt 1$。定义两个泛函

$$\omega_1(A) = \frac{1}{\lambda}\langle\Omega|E\,\pi_\omega(A)E|\Omega\rangle,\qquad \omega_2(A) = \frac{1}{1-\lambda}\langle\Omega|(\mathbb 1-E)\,\pi_\omega(A)(\mathbb 1-E)|\Omega\rangle.$$

先用 $E\in\pi'$ 把 $E$ 穿过 $\pi(A)$：$\langle\Omega|E\pi(A)E|\Omega\rangle = \langle E\Omega|\pi(A)|E\Omega\rangle$。因为 $E$ 与 $\pi(\mathcal A)$ 对易、$\langle\Omega|\pi(A)|\Omega\rangle = \omega(A)$，逐项展开：

$$\omega(A) = \lambda\,\omega_1(A) + (1-\lambda)\,\omega_2(A).$$

$\omega_1,\omega_2$ 都是正归一的（$\omega_i(\mathbb 1) = 1$），所以 $\omega$ 是两个不同态的凸组合——与纯性矛盾。故 $\pi_\omega$ 不可约。$\square$

（逆命题：若表示不可约，则 $\omega$ 纯——用同样构造的逆否命题即可。）于是"纯态 $\Leftrightarrow$ 不可约 $\Leftrightarrow$ $\pi_\omega(\mathcal A)'' = B(\mathcal H_\omega)$"三件事等价，这正是论文"纯态延拓 ⇒ 型 I 因子"的依据。

</details>

**4.** 证明 III 型因子没有迹：利用"任意两个非零投影等价"这一性质，导出矛盾。

<details markdown="1"><summary>点击显示答案</summary>

设 $\mathcal M$ 是 III 型因子，其定义性质是：任意两个非零投影 $P,Q$ 都等价（存在部分等距 $V$ 使 $P = V^*V$、$Q = VV^*$）。假设存在非零正迹泛函 $\tau$，满足 $\tau(AB) = \tau(BA)$ 与 $\tau(A^*A) \ge 0$。

取任意非零投影 $P$。由等价性，$P\sim\mathbb 1$，即存在部分等距 $V$ 使 $P = V^*V$、$\mathbb 1 = VV^*$。迹的循环性给出

$$\tau(P) = \tau(V^*V) = \tau(VV^*) = \tau(\mathbb 1).$$

归一化 $\tau(\mathbb 1) = 1$，故**所有非零投影的迹都等于 $1$**。

取两个正交的非零投影 $P,Q$（$PQ = 0$）。则 $P+Q$ 也是投影，且 $\tau(P+Q) = \tau(P) + \tau(Q) = 1 + 1 = 2$。但 $P+Q$ 非零，由上面的论证 $\tau(P+Q) = 1$——矛盾（$2\neq 1$）。

故 III 型因子不存在迹。$\square$

推论：没有迹就没有（归一化的）密度矩阵，$-\operatorname{Tr}\rho\ln\rho$ 无从定义——局域 QFT 的纠缠熵必须是"相对"或"带截断"的量。

</details>

**5.** 由 $\rho_D = e^{-\hat A/(4G_N)}/Z_{D,1}$ 推出论文 (5.50)：$S = \langle\hat A\rangle/(4G_N) + \ln Z_{D,1}$；并说明为什么"有限维"是这一切的前提。

<details markdown="1"><summary>点击显示答案</summary>

直接计算：

$$S = -\operatorname{Tr}\rho_D\ln\rho_D = -\operatorname{Tr}\left[\rho_D\left(-\frac{\hat A}{4G_N} - \ln Z_{D,1}\right)\right] = \frac{\operatorname{Tr}(\rho_D\hat A)}{4G_N} + \ln Z_{D,1}\,\operatorname{Tr}\rho_D.$$

用 $\operatorname{Tr}\rho_D = 1$ 与 $\langle\hat A\rangle = \operatorname{Tr}(\rho_D\hat A)$：

$$S = \frac{\langle\hat A\rangle}{4G_N} + \ln Z_{D,1}.\qquad\square$$

"有限维"的作用有三层：

1. **迹存在**：$\operatorname{Tr}$ 是 I 型代数的东西；III 型里没有归一化迹，$\rho_D$ 无从定义；
2. **$Z_{D,1} = \operatorname{Tr}e^{-\hat A/(4G_N)}$ 有限**：若 Hilbert 空间无穷维且 $e^{-\hat A/4G}$ 的谱无下界，配分函数发散（JT 引力的 $I_\infty$ 正是如此：$\operatorname{Tr}W = \infty$，见第 3 篇）；
3. **熵有限**：$\ln Z_{D,1}$ 与 $S$ 才是有意义的数，才能谈"对数修正系数"（论文 (5.65)–(5.69) 的 $106/45$）。

所以论文 §5.2 的"因果菱形 Hilbert 空间有限维"不是技术细节，而是整条熵计算链条的**前提定理**——它把代数从 $I_\infty$ 压到有限 $I_d$。

</details>

## 参考

- Haag《Local Quantum Physics: Fields, Particles, Algebras》(Springer, 2nd ed., 1996)：局域代数、Haag–Kastler 公理、GNS 与型分类的物理表述。
- Bratteli & Robinson《Operator Algebras and Quantum Statistical Mechanics》卷 1（C*-代数、态与 GNS）、卷 2（von Neumann 代数、KMS 态）：标准数学参考。
- Witten, Rev. Mod. Phys. 90 (2018) 045003（arXiv:1803.04993）："Notes on Some Entanglement Properties of Quantum Field Theory"——局域代数的 III₁ 型与纠缠熵的严格讨论。
- Kadison & Singer, Amer. J. Math. 81 (1959) 383：纯态延拓定理。
- 量子力学书 9s2（GNS 与 Haag 定理的入门版）；第 9 阶段 04 篇（论文 §4 的代数构造与有限维论证）；Chandrasekaran–Longo–Penington–Witten, JHEP 02 (2023) 082（arXiv:2206.10780）：de Sitter 空间的可观测量代数与型分类的物理应用。
