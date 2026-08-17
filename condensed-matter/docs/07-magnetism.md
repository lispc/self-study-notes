# 磁性：交换作用、磁模型与自旋波

> 路线图位置：第二部分（相互作用、序与相变）· 第 7 章
> 前置知识：本科量子力学（自旋 1/2、角动量相加、全同粒子与 Pauli 原理）、统计力学基础（正则系综、配分函数）；第 2 章[晶格振动与声子](02-lattice-vibrations-phonons.md)的玻色子语言。
> 学习目标：理解交换作用的真正来源（库仑 + Pauli 原理，而非磁偶极）；写下 Ising/Heisenberg 模型并用平均场求解；推导自旋波色散与 Bloch $T^{3/2}$ 定律，并认清 magnon 的 Goldstone 玻色子身份。
>
> 记号约定：本书保留 $\hbar$ 与 $k_B$（不取自然单位），$S$ 表示自旋量子数，$\mathbf{S}_i$ 是格点 $i$ 上的自旋算符，$z$ 为配位数。

---

## 1. 一句话总结

**磁性是量子力学与静电学的合谋：交换作用来自库仑排斥在 Pauli 原理约束下对自旋构型的依赖；它被抽象成 Ising/Heisenberg 自旋模型后，平均场给出 Curie–Weiss 定律的骨架，而自旋波——铁磁体自发破缺自旋旋转对称性的 Goldstone 玻色子——给出 $\omega\propto k^2$ 的色散和磁化强度的 Bloch $T^{3/2}$ 定律。**

下面逐层展开：先问磁性从哪来，再建模型、解模型、听模型的"振动"。

## 2. 磁性从哪里来：交换作用

### 2.1 先排除一个错误答案：磁偶极相互作用

直觉上，磁铁吸引磁铁，自旋带着磁矩 $\boldsymbol{\mu} = -g\mu_B \mathbf{S}/\hbar$，两个磁矩之间的偶极–偶极相互作用似乎是磁性的天然来源。算一下量级就知不对：

$$E_{\text{dip}} \sim \frac{\mu_0}{4\pi}\frac{\mu_B^2}{r^3} \sim 10^{-4}\ \text{eV} \;\sim\; 1\ \text{K} \qquad (r \sim 2\ \text{Å}).$$

而铁的居里温度 $T_c \approx 1043$ K。如果磁矩靠偶极相互作用排列，热运动在 1 K 就把它冲垮了，室温铁磁体根本不可能存在。真正的相互作用必须强两到三个数量级——只能来自库仑能（eV 量级）。但库仑相互作用 $e^2/(4\pi\varepsilon_0 r_{12})$ 不含自旋，它怎么会管自旋朝哪？答案藏在全同性原理里。

### 2.2 双电子模型：Pauli 原理如何让库仑作用"变成"自旋耦合

考虑两个电子，各自局域在轨道 $\varphi_a$、$\varphi_b$ 上（氢分子的 Heitler–London 图像，或相邻格点上的两个 d 电子）。哈密顿量

$$H = h(1) + h(2) + V(1,2), \qquad V(1,2) = \frac{e^2}{4\pi\varepsilon_0\,r_{12}},$$

本身**与自旋无关**。但两个电子是费米子，总波函数必须反对称，于是空间部分的对称性被自旋部分锁定：

- 自旋三重态（对称自旋波函数）$\Rightarrow$ 空间部分**反对称**：

$$\Psi_T = \frac{1}{\sqrt2}\big[\varphi_a(\mathbf r_1)\varphi_b(\mathbf r_2) - \varphi_b(\mathbf r_1)\varphi_a(\mathbf r_2)\big]\,\chi_{\text{triplet}};$$

- 自旋单重态（反对称自旋波函数）$\Rightarrow$ 空间部分**对称**：

$$\Psi_S = \frac{1}{\sqrt2}\big[\varphi_a(\mathbf r_1)\varphi_b(\mathbf r_2) + \varphi_b(\mathbf r_1)\varphi_a(\mathbf r_2)\big]\,\chi_{\text{singlet}}.$$

（为简单起见忽略轨道重叠 $\langle\varphi_a|\varphi_b\rangle$，它只改动归一化，不改变定性结论。）反对称的空间波函数在 $\mathbf r_1 = \mathbf r_2$ 处为零——两个电子自动互相回避，库仑排斥能更低；对称波函数则允许电子靠近，排斥能更高。分别计算能量期望值：

$$E_{S/T} = C \pm J_{\text{ex}},$$

其中直接积分与交换积分分别为

$$C = \int d^3r_1\, d^3r_2\; \lvert\varphi_a(\mathbf r_1)\rvert^2\, V(1,2)\, \lvert\varphi_b(\mathbf r_2)\rvert^2,$$

$$J_{\text{ex}} = \int d^3r_1\, d^3r_2\; \varphi_a^*(\mathbf r_1)\varphi_b^*(\mathbf r_2)\, V(1,2)\, \varphi_b(\mathbf r_1)\varphi_a(\mathbf r_2).$$

于是单重态与三重态之间出现能级劈裂

$$E_S - E_T = 2 J_{\text{ex}}.$$

注意整个推导里哈密顿量没有一处显含自旋：劈裂完全来自"空间构型 $\leftrightarrow$ 自旋构型"被反对称性绑定。这就是**交换作用**：它是**库仑能 + Pauli 原理**，不是任何磁相互作用。

最后一步是把它写成自旋算符的语言。两个自旋 1/2 有

$$\mathbf{S}_1\cdot\mathbf{S}_2 = \begin{cases} +\hbar^2/4, & \text{三重态},\\ -3\hbar^2/4, & \text{单重态},\end{cases}$$

所以双电子体系的有效哈密顿量可以等价地写成（$\hbar=1$ 地把 $\mathbf S$ 当无量纲算符，恢复 $\hbar$ 时把 $J$ 理解为能量）

$$H_{\text{eff}} = \text{const} - 2J_{\text{ex}}\, \mathbf{S}_1\cdot\mathbf{S}_2,$$

它忠实地复现 $E_T = C - J_{\text{ex}}$、$E_S = C + J_{\text{ex}}$。$J_{\text{ex}} > 0$ 时三重态（自旋平行）能量低，是**铁磁**耦合；$J_{\text{ex}} < 0$ 时单重态能量低，是**反铁磁**耦合。符号取决于具体轨道与成键几何——H₂ 分子中单重态更低（成键即反铁磁关联），而某些正交轨道组态下交换积分可以为正。磁性的丰富性就藏在这个符号问题里。

## 3. 磁相互作用的三种典型机制

真实材料里"两个电子共享库仑能"的实现方式不同，给出三类交换机制：

- **直接交换**：相邻原子的磁轨道直接重叠，上节的双电子积分就是字面意义的机制。适用于轨道空间延展较大的情形；实际绝缘体中它往往给出反铁磁符号。
- **超交换（superexchange）**：两个磁离子不直接重叠，而是通过中间的非磁离子（如 MnO 中的 O²⁻）发生虚跃迁，产生反铁磁耦合。这是绝大多数绝缘体反铁磁体（MnO、NiO、La₂CuO₄ 的母化合物）的机制，其微观推导（Hubbard 模型大 $U$ 极限下 $J = 4t^2/U$）留给第 13 章[强关联浅尝](13-strong-correlations.md)。
- **RKKY 相互作用**：金属中的局域磁矩通过极化传导电子的 Fermi 海间接耦合，相互作用随距离振荡衰减，$\propto \cos(2k_F r)/r^3$（三维）。符号随距离在铁磁/反铁磁之间振荡，是稀土磁性与自旋玻璃的关键。这里只记住"以 Fermi 面为媒介、带 $2k_F$ 振荡"这两个特征即可。

共同点：三者都是库仑 + 量子力学（Pauli 原理、虚跃迁、Fermi 统计）的产物，能量尺度都是 eV 的若干分之一，足以支撑室温以上的磁序。

## 4. 磁模型：Ising 与 Heisenberg

既然有效相互作用可以写成 $-J\,\mathbf{S}_i\cdot\mathbf{S}_j$，凝聚态的做法是把它抽象成定义在晶格上的自旋模型，再去研究集体的磁有序。两个主角：

**Heisenberg 模型**（各向同性，自旋是三维矢量算符）：

$$H = -J\sum_{\langle ij\rangle} \mathbf{S}_i\cdot\mathbf{S}_j - g\mu_B \mathbf{B}\cdot\sum_i \mathbf{S}_i.$$

**Ising 模型**（极端各向异性，自旋只取 $\sigma_i = \pm 1$）：

$$H = -J\sum_{\langle ij\rangle} \sigma_i\sigma_j - h\sum_i \sigma_i.$$

约定 $J > 0$ 为铁磁耦合（不同教材符号约定不同，读文献时先确认）。$\langle ij\rangle$ 表示最近邻键，每根键只算一次。两者分别是现实磁体在连续/离散对称性两端的理想化：Ising 模型对称性是离散的 $\mathbb{Z}_2$（全体自旋翻转），Heisenberg 模型是连续的 SU(2) 自旋转动。

**基态性质**（零外场、$J>0$）：

- Ising 铁磁：基态为全体 $+1$ 或全体 $-1$，二重简并，$\mathbb{Z}_2$ 被基态自发破缺。
- Heisenberg 铁磁：全体自旋指向同一方向的态是**严格本征态**（每根键上 $\mathbf{S}_i\cdot\mathbf{S}_j$ 都取最大值 $S^2$），基态能量 $E_0 = -\tfrac12 N z J S^2$；由于 SU(2) 对称，磁化方向任意，构成连续简并的基态流形（球面 $S^2$）。
- 反铁磁（$J<0$）：经典图像是 Néel 态（相邻自旋反平行），但它**不是**量子 Heisenberg 模型的本征态，真实基态有量子涨落修正，见第 7 节。

## 5. 平均场理论

自旋模型一般无法严格求解（一维 Ising 与二维 Ising 是著名例外）。平均场理论是最粗、也最有教学价值的近似：它把涨落的环境替换成一个"平均场"，把多体问题压回单体问题。

### 5.1 Weiss 分子场与自洽方程

以 Heisenberg 铁磁为例，把注意力放在格点 $i$ 上。它感受到的相互作用能是 $-J\mathbf{S}_i\cdot\sum_{j\,\text{nn}\,i}\mathbf{S}_j$。平均场近似把邻居的自旋替换为平均值 $\langle\mathbf{S}\rangle = m\hat z$（$m$ 即每个格点的平均自旋，正比于磁化强度），于是格点 $i$ 上的单体哈密顿量为

$$H_i^{\text{MF}} = -\big(zJm + g\mu_B B\big) S_i^z \equiv -h_{\text{eff}}\, S_i^z,$$

其中 $h_{\text{eff}} = zJm + g\mu_B B$ 就是 **Weiss 分子场**：每个自旋仿佛处在一个由全体邻居平均产生的有效磁场里。问题退化为"磁场中的单个自旋"，其热平衡平均值对 $S = 1/2$ 为（取 $\hbar = 1$，自旋算符无量纲）

$$m = \frac12 \tanh\!\left(\frac{zJm + g\mu_B B}{2 k_B T}\right).$$

这就是**自洽方程**：等式右边的 $m$ 产生有效场，有效场又极化出自旋 $m$。一般 $S$ 的情形把 $\tfrac12\tanh$ 换成 Brillouin 函数 $S\,B_S$。

### 5.2 Curie–Weiss 定律与临界指数

**居里温度**。零外场下看自洽方程有没有 $m \neq 0$ 的解。利用 $\tanh x \approx x$（$x$ 小）线性化：

$$m \approx \frac{zJ}{4k_B T}\, m,$$

非零解存在的条件是 $zJ/(4k_BT) \geq 1$，即 $T \leq T_c$，其中（$S=1/2$）

$$k_B T_c = \frac{zJ}{4}; \qquad \text{一般 } S:\quad k_B T_c = \frac{zJ\, S(S+1)}{3}.$$

$T_c$ 正比于 $zJ$——配位数越大、耦合越强，磁序越耐高温。这是平均场全部预言中最稳健的一个标度。

**Curie–Weiss 定律**。$T > T_c$ 时加小外场 $B$，线性化自洽方程：

$$m \approx \frac{zJm + g\mu_B B}{4k_B T} \;\Longrightarrow\; m\left(1 - \frac{T_c}{T}\right) = \frac{g\mu_B B}{4k_B T},$$

于是磁化率（单位体积含 $n$ 个磁矩）

$$\chi = \frac{\partial (ng\mu_B m)}{\partial B}\bigg|_{B=0} = \frac{C}{T - T_c}, \qquad C = \frac{n\,(g\mu_B)^2}{4k_B}\ \ (S=\tfrac12).$$

这正是实验上高温区普遍成立的 **Curie–Weiss 定律**；顺磁居里定律 $\chi = C/T$ 是它的 $T_c \to 0$ 极限。拟合实验的 $\chi^{-1}(T)$ 直线可以读出 $T_c$ 与有效磁矩。

**临界指数 $\beta$**。在 $T_c$ 以下附近展开 $\tanh x \approx x - x^3/3$，自洽方程给出（自检问题 2 让你补全）

$$m^2 \propto T_c - T \quad\Longrightarrow\quad m \propto (T_c - T)^{1/2},$$

即平均场临界指数 $\boxed{\beta = 1/2}$。

### 5.3 平均场哪里错了

平均场把所有涨落平均掉了，后果有两个层次：

- **定量上错**：三维 Heisenberg 模型的实验值 $\beta \approx 0.36$，三维 Ising 是 $\beta \approx 0.326$，都不是 $1/2$；$T_c$ 本身也被高估（真实涨落会提前瓦解有序）。临界指数与晶格细节无关、只依赖维数与对称性，这种**普适性**是重整化组的领地，第 9 章[相变与临界现象](09-phase-transitions-criticality.md)专门讲。
- **定性上也可能错**：平均场预言一维 Ising 模型有有限温相变（$k_BT_c^{\text{MF}} = zJ/4 = J/2$，$z=2$），但严格解表明一维 Ising **任何 $T>0$ 都没有磁序**。原因见自检问题 5：低维体系中畴壁的熵代价太低，涨落获胜。

尽管如此，平均场给出的"分子场 $\to$ 自洽 $\to$ 失稳温度 $\to$ 临界幂律"这套范式是研究一切有序相（包括第 8 章的超导）的默认第一步。

## 6. 自旋波与磁振子

平均场告诉你基态有序、有限温失稳，但它说不清低温下体系的**激发**是什么。这一节做线性自旋波理论，它是本章的物理高潮：铁磁体的低能激发是一种集体玻色模——magnon（磁振子），而且它就是自发对称性破缺的 Goldstone 玻色子。

### 6.1 Holstein–Primakoff 变换与线性自旋波

取零场铁磁 Heisenberg 模型，基态取全体自旋沿 $+z$。低温下每个格点的自旋只是轻微偏离满极化，自然的语言是把"偏离"量子化为玻色子。**Holstein–Primakoff 变换**：

$$S_i^z = S - a_i^\dagger a_i, \qquad S_i^+ \approx \sqrt{2S}\, a_i, \qquad S_i^- \approx \sqrt{2S}\, a_i^\dagger,$$

其中 $a_i, a_i^\dagger$ 是格点上的玻色子湮灭/产生算符，$n_i = a_i^\dagger a_i$ 数出该格点"翻转了多少自旋"。可以验证 $[S_i^+, S_i^-] = 2S_i^z$ 在保留到 $1/S$ 阶的意义下成立；展开省略了 $n_i/S$ 阶的非线性项，这就是**线性自旋波近似**（低温、$n_i \ll S$ 时自洽）。

代入 $\mathbf{S}_i\cdot\mathbf{S}_j = \tfrac12(S_i^+S_j^- + S_i^-S_j^+) + S_i^zS_j^z$，保留到玻色算符的二次项：

$$\mathbf{S}_i\cdot\mathbf{S}_j \approx S^2 - S\,(n_i + n_j) + S\,(a_i^\dagger a_j + a_j^\dagger a_i),$$

于是

$$H \approx E_0 + JS\sum_{\langle ij\rangle}\big(n_i + n_j - a_i^\dagger a_j - a_j^\dagger a_i\big), \qquad E_0 = -\tfrac12 NzJS^2.$$

这是玻色子的紧束缚型 hopping 哈密顿量，Fourier 变换 $a_i = \tfrac{1}{\sqrt N}\sum_{\mathbf k} e^{i\mathbf k\cdot\mathbf r_i} a_{\mathbf k}$ 立刻对角化：

$$H \approx E_0 + \sum_{\mathbf k} \hbar\omega_{\mathbf k}\, a_{\mathbf k}^\dagger a_{\mathbf k}, \qquad \hbar\omega_{\mathbf k} = 2JS\Big(z - \sum_{\boldsymbol\delta} e^{i\mathbf k\cdot\boldsymbol\delta}\Big),$$

$\boldsymbol\delta$ 跑遍 $z$ 个最近邻矢量。简立方晶格（$z=6$）上 $\hbar\omega_{\mathbf k} = 4JS\big[3 - \cos k_xa - \cos k_ya - \cos k_za\big]$，长波极限

$$\boxed{\hbar\omega_{\mathbf k} \approx 2JSa^2 k^2 \equiv Dk^2}$$

这就是铁磁 magnon 的**二次色散**，$D = 2JSa^2$ 叫自旋波刚度。一个 consistency check：单 magnon 态 $|\mathbf k\rangle \propto \sum_i e^{i\mathbf k\cdot\mathbf r_i} S_i^-\,|\text{FM}\rangle$ 其实是模型的**严格本征态**，能量恰好 $E_0 + \hbar\omega_{\mathbf k}$——线性自旋波在单粒子 sector 是精确的，近似只发生在多 magnon 相互作用上。

### 6.2 为什么 ω∝k²：magnon 是 Goldstone 玻色子

把这条色散与第 2 章声子的 $\omega = v_s k$ 并排放着看：

- 声子：平移对称性（在晶格上已部分破缺）的 Goldstone 模，**线性**色散；
- magnon：铁磁体自发破缺自旋旋转对称性 SU(2) $\to$ U(1)（磁化选定了一个方向，绕该方向的转动仍是对称性）的 **Goldstone 玻色子**，**二次**色散。

Goldstone 定理保证 $\omega_{\mathbf k=0} = 0$：$\mathbf k = 0$ 的 magnon 对应全体自旋一致地、无穷小地偏转，不花任何能量——这就是 $\hbar\omega_0 = 2JS(z - z) = 0$ 的物理。但为什么是 $k^2$ 而不是 $k$？关键在于铁磁体的序参量（磁化）本身就是破缺对称性的守恒荷（总自旋）：序参量的动力学由 Berry 相位项主导，有效拉氏量含一阶时间导数而非二阶，于是 $\omega \sim k^2$。由此还产生一个 Goldstone 计数上的微妙之处：SU(2) $\to$ U(1) 破缺了**两个**生成元（$S^x, S^y$），却只得到**一种** magnon——这两个生成元互为共轭（像 $x$ 与 $p$），合并成一支"二型"Goldstone 模。

这套"对称性自发破缺 $\Rightarrow$ 无质量（无能隙）集体模"的逻辑与粒子物理完全同构：QFT 笔记在[电弱统一](../../qft-sm/docs/stage-06-standard-model/02-electroweak-unification.md)里讨论过 Goldstone 定理在规范对称性下的命运（被 Higgs 机制"吃掉"），而这里破缺的是**整体**对称性——整体与规范对称性在自发破缺时的本质区别见[整体对称性 vs 规范对称性](../../qft-sm/docs/stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)。铁磁体是观察"裸"Goldstone 玻色子最干净的舞台。

### 6.3 Bloch T^{3/2} 定律

二次色散有一个立刻可测的后果：低温磁化强度偏离饱和值的规律。每激发一个 magnon 翻转一个单位的自旋，故

$$\frac{\Delta M(T)}{M(0)} = \frac{1}{NS}\sum_{\mathbf k} \frac{1}{e^{\hbar\omega_{\mathbf k}/k_BT} - 1} \;\xrightarrow{\;N\to\infty\;}\; \frac{a^3}{S}\int\!\frac{d^3k}{(2\pi)^3}\, \frac{1}{e^{Dk^2/k_BT}-1}.$$

换元 $x = Dk^2/(k_BT)$，$k^2 dk = \tfrac12 (k_BT/D)^{3/2} x^{1/2}dx$，于是

$$\frac{\Delta M}{M(0)} = \frac{\Gamma(\tfrac32)\,\zeta(\tfrac32)}{4\pi^2 S}\left(\frac{k_BT}{2JS}\right)^{3/2} \approx \frac{0.0587}{S}\left(\frac{k_BT}{2JS}\right)^{3/2}.$$

磁化强度按 $\boxed{T^{3/2}}$ 从饱和值滑落，这就是 **Bloch 定律**，已被铁磁体的低温磁化测量精确证实。推导的关键中间步骤（积分换元）留给你在自检问题 4 中亲手走一遍。

一个值得注意的副产品：被积函数含 $k^2 dk$，在二维换成 $k\, dk$，低温积分在小 $k$ 处对数发散——二维 Heisenberg 铁磁在任何 $T>0$ 都无法维持长程序（Mermin–Wagner 定理的物理实质）。连续对称性的破缺对维度极其敏感，离散对称性的 Ising 模型则没这个限制。

## 7. 反铁磁一句

反铁磁 Heisenberg 模型（$J<0$）用两套子格做同样的自旋波展开，结论与铁磁有两大差别：**色散是线性的** $\hbar\omega_{\mathbf k} \approx \hbar c_s k$（序参量 Néel 矢量不是守恒荷，拉氏量是普通的二阶时间导数，所以回到类声子行为）；**量子涨落即使在 $T=0$ 也不消失**，子格磁化被零点涨落从满值 $S$ 削减（三维削减约百分之几，一维自旋 1/2 链甚至彻底摧毁 Néel 序）。反铁磁是量子涨落比铁磁强得多的体系，其极端情形（自旋液体）属于第 13 章的话题。

## 8. 畴与磁滞

最后从微观回到宏观。既然交换作用要求全体磁矩同向，为什么一块未磁化的铁块对外不显磁性？因为**磁畴**：样品分成许多磁化方向不同的小区域，宏观磁矩互相抵消。驱动力不在交换作用（它只管近邻），而在长程的**磁偶极能**——第 2 节嫌弃它弱，但它作用距离无限远，全体磁矩同向会在样品外产生杂散场，静磁能 $\propto M^2V$；分畴以畴壁处的交换能 + 磁晶各向异性能为代价，换整体静磁能的下降。畴壁本身是一个有限厚度（典型几十纳米）的连续自旋扭转结构：交换作用希望它宽（变化平缓便宜），各向异性希望它窄，平衡给出有限宽度。

外场下畴壁移动、磁畴转动，磁化随之增长；而畴壁被缺陷、晶界**钉扎**，移动不可逆，于是撤场后磁化不退回原路——这就是**磁滞回线**与剩磁。工程上"硬磁/软磁"之分本质上就是畴壁钉扎强弱之分。畴与磁滞提醒我们：第 2–6 节讲的是单畴理想磁体的物理，真实器件是多畴、多缺陷的非平衡系统——但钉扎的仍然是交换作用与 Goldstone 物理写下的基本常数。

## 9. 小结

- 磁性 = 库仑能 + Pauli 原理；磁偶极相互作用（$\sim$1 K）比居里温度小三个量级，只是宏观分畴的推手。
- 双电子模型给出 $E_S - E_T = 2J_{\text{ex}}$，等效为 $H_{\text{eff}} = -2J_{\text{ex}}\,\mathbf{S}_1\cdot\mathbf{S}_2$；机制上分为直接交换、超交换（第 13 章）、RKKY。
- 平均场：$m = \tfrac12\tanh[(zJm + g\mu_B B)/2k_BT]$，$k_BT_c = zJS(S+1)/3$，$\chi = C/(T - T_c)$，$\beta = 1/2$；涨落使它定量全错，第 9 章收拾残局。
- 线性自旋波：Holstein–Primakoff 变换把自旋翻转变为玻色子，$\hbar\omega_{\mathbf k} \approx 2JSa^2k^2$。

| | 声子 | 铁磁 magnon | 反铁磁 magnon |
|---|---|---|---|
| 破缺的对称性 | 平移 | 自旋 SU(2) → U(1) | 自旋 SU(2) → U(1) |
| 色散 | $\omega \propto k$ | $\omega \propto k^2$ | $\omega \propto k$ |
| 低温后果 | $C_V \propto T^3$ | $\Delta M \propto T^{3/2}$ | $\Delta M \propto T^2$ |
| 量子涨落（$T=0$） | 零点振动 | 无（基态严格本征） | 削减子格磁化 |

- magnon 是整体对称性自发破缺的 Goldstone 玻色子；与 QFT 中 Goldstone/Higgs 的讨论互为镜像。

## 自检问题

**1.** 对第 2 节的双电子模型，证明单重态与三重态的能量劈裂为 $E_S - E_T = 2J_{\text{ex}}$，并验证有效哈密顿量 $H_{\text{eff}} = \text{const} - 2J_{\text{ex}}\,\mathbf{S}_1\cdot\mathbf{S}_2$ 复现这一劈裂。

<details markdown="1"><summary>点击显示答案</summary>

**劈裂**：$H = h(1) + h(2) + V(1,2)$ 中单体部分对两种空间构型给出相同的 $2\varepsilon_0$（自旋无关）。相互作用项的期望值为

$$E_{S/T}^{(V)} = \langle\Psi_{S/T}\lvert V\lvert\Psi_{S/T}\rangle = \frac12\big(2C \pm 2J_{\text{ex}}\big) = C \pm J_{\text{ex}},$$

其中交叉项 $\langle\varphi_a(1)\varphi_b(2)|V|\varphi_b(1)\varphi_a(2)\rangle = J_{\text{ex}}$，$\pm$ 号来自 $\Psi_{S/T}$ 展开式中两项的相对符号。于是

$$E_S - E_T = (C + J_{\text{ex}}) - (C - J_{\text{ex}}) = 2J_{\text{ex}}.$$

**等效自旋哈密顿量**：$\mathbf{S}_1\cdot\mathbf{S}_2 = \tfrac12\big[(\mathbf{S}_1+\mathbf{S}_2)^2 - \mathbf{S}_1^2 - \mathbf{S}_2^2\big]$。三重态总自旋 $S_{\text{tot}}=1$，本征值 $\tfrac12[2 - \tfrac34 - \tfrac34] = +\tfrac14$；单重态 $S_{\text{tot}}=0$，本征值 $-\tfrac34$（取 $\hbar = 1$）。代入 $H_{\text{eff}}$：

$$E_T = \text{const} - \tfrac12 J_{\text{ex}}, \qquad E_S = \text{const} + \tfrac32 J_{\text{ex}},$$

差值 $E_S - E_T = 2J_{\text{ex}}$，且取 $\text{const} = C + \tfrac12 J_{\text{ex}}$ 时两个绝对能量也分别对上。

</details>

**2.** 从 $S = 1/2$ 的平均场自洽方程出发，求 $T_c$，并证明 $T_c$ 以下附近 $m \propto (T_c - T)^{1/2}$。

<details markdown="1"><summary>点击显示答案</summary>

零外场自洽方程为

$$m = \frac12\tanh\!\left(\frac{zJm}{2k_BT}\right).$$

**求 $T_c$**：相变点处 $m \to 0^+$，用 $\tanh x \approx x$ 线性化，$m = \tfrac12\cdot\tfrac{zJm}{2k_BT}$，非零解要求

$$1 = \frac{zJ}{4k_BT_c} \;\Longrightarrow\; k_BT_c = \frac{zJ}{4}.$$

**临界行为**：记 $a = zJ/(2k_BT)$，方程为 $2m = \tanh(am)$。$T$ 略低于 $T_c$ 时 $am$ 是小量，展开 $\tanh(am) = am - (am)^3/3$：

$$2m = am - \frac{a^3m^3}{3} \;\Longrightarrow\; m^2 = \frac{3(a - 2)}{a^3}.$$

$T \to T_c^-$ 时 $a \to a_c = 2$，把 $a = 2T_c/T$ 代入：$a - 2 = 2(T_c - T)/T \approx 2(T_c-T)/T_c$，而 $a^3 \approx 8$，故

$$m^2 \approx \frac{3}{4}\,\frac{T_c - T}{T_c} \;\Longrightarrow\; m = \frac{\sqrt3}{2}\left(\frac{T_c - T}{T_c}\right)^{1/2}.$$

即平均场临界指数 $\beta = 1/2$。注意这个结果（以及 $\chi$ 的发散）对 $S$ 的取值与晶格结构一律成立——这正是平均场"普适但错误"的特征。

</details>

**3.** 写出线性自旋波推导的骨架：从 Holstein–Primakoff 变换到 $\hbar\omega_{\mathbf k}$，并指出每一步的近似。

<details markdown="1"><summary>点击显示答案</summary>

骨架分四步：

**第一步（变换）**。令 $n_i = a_i^\dagger a_i$，取

$$S_i^z = S - n_i, \qquad S_i^+ = \sqrt{2S}\,a_i + O\!\left(\tfrac{n_i}{\sqrt S}\right), \qquad S_i^- = \sqrt{2S}\,a_i^\dagger + O\!\left(\tfrac{n_i}{\sqrt S}\right).$$

精确形式里 $S_i^+ = \sqrt{2S - n_i}\,a_i$，丢掉的是 $n_i/S$ 阶修正——近似 1（要求 $n_i \ll S$，低温自洽）。

**第二步（展开哈密顿量）**。代入 $\mathbf{S}_i\cdot\mathbf{S}_j = \tfrac12(S_i^+S_j^- + S_i^-S_j^+) + S_i^zS_j^z$，保留玻色算符二次项（四次项 $\propto a^\dagger a^\dagger a a$ 描述 magnon 相互作用，丢掉——近似 2）：

$$\mathbf{S}_i\cdot\mathbf{S}_j \approx S^2 - S(n_i + n_j) + S(a_i^\dagger a_j + a_j^\dagger a_i).$$

**第三步（Fourier 对角化）**。$a_i = N^{-1/2}\sum_{\mathbf k} e^{i\mathbf k\cdot\mathbf r_i}a_{\mathbf k}$，注意 $\sum_{\langle ij\rangle}(n_i + n_j) = z\sum_i n_i$，而 $\sum_{\langle ij\rangle}a_i^\dagger a_j = \tfrac12\sum_{\mathbf k}\sum_{\boldsymbol\delta}e^{i\mathbf k\cdot\boldsymbol\delta}\,a_{\mathbf k}^\dagger a_{\mathbf k}$，得到

$$H = E_0 + \sum_{\mathbf k}\hbar\omega_{\mathbf k}\,a_{\mathbf k}^\dagger a_{\mathbf k}, \qquad \hbar\omega_{\mathbf k} = 2JS\Big(z - \sum_{\boldsymbol\delta}e^{i\mathbf k\cdot\boldsymbol\delta}\Big).$$

**第四步（长波极限）**。$k \to 0$ 时 $\sum_{\boldsymbol\delta}e^{i\mathbf k\cdot\boldsymbol\delta} \approx z - \tfrac12\sum_{\boldsymbol\delta}(\mathbf k\cdot\boldsymbol\delta)^2$。简立方中 $\sum_{\boldsymbol\delta}(\mathbf k\cdot\boldsymbol\delta)^2 = 2a^2k^2$，故

$$\hbar\omega_{\mathbf k} \approx 2JSa^2 k^2.$$

近似 1、2 在单 magnon sector 不造成任何误差（单 magnon 态是严格本征态），它们只在 $T$ 升高、magnon 密度变大时才失效。

</details>

**4.** 推导 Bloch $T^{3/2}$ 定律中的积分，即证明 $\displaystyle\int\!\frac{d^3k}{(2\pi)^3}\frac{1}{e^{Dk^2/k_BT}-1} = \frac{\Gamma(3/2)\zeta(3/2)}{4\pi^2}\left(\frac{k_BT}{D}\right)^{3/2}$。

<details markdown="1"><summary>点击显示答案</summary>

三维球对称化：

$$I = \frac{1}{(2\pi)^3}\cdot 4\pi\int_0^\infty \frac{k^2\,dk}{e^{Dk^2/k_BT}-1} = \frac{1}{2\pi^2}\int_0^\infty \frac{k^2\,dk}{e^{Dk^2/k_BT}-1}.$$

换元 $x = Dk^2/(k_BT)$，即 $k = (k_BT x/D)^{1/2}$，$dk = \tfrac12(k_BT/D)^{1/2}x^{-1/2}dx$，于是

$$k^2\,dk = \frac12\left(\frac{k_BT}{D}\right)^{3/2} x^{1/2}dx, \qquad I = \frac{1}{4\pi^2}\left(\frac{k_BT}{D}\right)^{3/2}\int_0^\infty \frac{x^{1/2}\,dx}{e^x - 1}.$$

剩下的积分是 Bose–Einstein 积分的标准形：把 $1/(e^x-1) = \sum_{n\geq1}e^{-nx}$ 逐项积分，

$$\int_0^\infty \frac{x^{1/2}}{e^x-1}dx = \sum_{n=1}^\infty \frac{1}{n^{3/2}}\int_0^\infty x^{1/2}e^{-x}dx = \Gamma\!\left(\tfrac32\right)\zeta\!\left(\tfrac32\right),$$

数值上 $\Gamma(\tfrac32) = \sqrt\pi/2 \approx 0.886$、$\zeta(\tfrac32) \approx 2.612$，乘积约 $2.315$。代回并用 $D = 2JSa^2$ 整理出每个格点的自旋翻转数：

$$\frac{\Delta M}{M(0)} = \frac{a^3}{S}\,I = \frac{\Gamma(\tfrac32)\zeta(\tfrac32)}{4\pi^2 S}\left(\frac{k_BT}{2JS}\right)^{3/2} \approx \frac{0.0587}{S}\left(\frac{k_BT}{2JS}\right)^{3/2}.$$

要点有两个：被积函数低能端 $\sim k^2\cdot(k_BT/Dk^2)$ 有限，三维积分收敛（二维则对数发散——Mermin–Wagner）；全部温度依赖来自换元时冒出的 $(k_BT/D)^{3/2}$ 因子。

</details>

**5.** 用畴壁论证说明：一维 Ising 模型在任何 $T > 0$ 都没有长程磁序；并定性说明为什么二维不同。

<details markdown="1"><summary>点击显示答案</summary>

一维 Ising 模型 $H = -J\sum_i \sigma_i\sigma_{i+1}$（$J>0$），基态全体同向，能量 $E_0 = -JN$。从基态出发引入一个**畴壁**：某键两侧自旋反向，该键能量从 $-J$ 变 $+J$，代价

$$\Delta E = 2J,$$

与畴壁位置无关。但畴壁可以放在 $N$ 根键中的任意一根上，熵增 $\Delta S = k_B\ln N$。于是引入一个畴壁的自由能变化

$$\Delta F = 2J - k_BT\ln N \;\xrightarrow{\;N\to\infty\;}\; -\infty \qquad (\text{任意 } T>0).$$

热力学极限下产生畴壁总是降低自由能，体系会自发被畴壁切碎：关联在两个畴壁相遇的尺度上就被打断，$\langle\sigma_i\rangle = 0$，任何有限温度都没有自发磁化（严格解给出 $T_c = 0$，与此一致）。

**二维的对比**：畴壁不再是点，而是长度为 $L$ 的线，能量代价 $\Delta E = 2JL$ 随长度增长；路径数约为 $\sim 3^L$（每步三个方向），熵 $\Delta S \sim k_B L\ln 3$。于是

$$\Delta F \approx \big(2J - k_BT\ln 3\big)L,$$

低温下系数为正，长畴壁被压制，磁序得以存活——二维 Ising 有有限温相变（Onsager 严格解 $k_BT_c \approx 2.27J$，与这个粗糙估计同量级）。物理图像：点状畴壁"免费"，线状畴壁"按长度收费"，维度决定了涨落的价目表。

</details>

## 参考

- Kittel《固体物理导论》（第 8 版）第 11–12 章：抗磁/顺磁、交换作用与铁磁序——本章第 2–5 节的主线；第 12 章自旋波部分对应第 6 节。
- Ashcroft & Mermin《Solid State Physics》第 32–33 章：交换相互作用的微观讨论与自旋波（含 HP 变换）的更细致推导。
- A. Auerbach《Interacting Electrons and Quantum Magnetism》第 2、9–10 章：双电子交换与自旋波理论的现代讲法。
- J. M. D. Coey《Magnetism and Magnetic Materials》第 4–5 章：交换机制分类与畴/磁滞的材料视角。
