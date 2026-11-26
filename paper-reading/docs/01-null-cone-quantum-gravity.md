# 从零锥出发的代数量子引力：Chandrasekaran 论文思路摘要

> 路线图位置：论文阅读 · 第 1 篇（目标论文 arXiv:2611.34924）
> 前置知识：广义相对论 [5s](../../general-relativity/docs/05s-first-order-gravity.md)、[7](../../general-relativity/docs/07-causal-structure.md)、[8](../../general-relativity/docs/08-null-hypersurface-geometry.md)、[10](../../general-relativity/docs/10-boundary-terms-action.md)、[12](../../general-relativity/docs/12-covariant-phase-space.md) 五章；QFT [第 4 阶段 07s](../../qft-sm/docs/stage-04-qft-core/07s-phase-space-path-integral-and-ordering.md) 与[第 9 阶段四篇](../../qft-sm/README.md)；理论力学 [9–10](../../classical-mechanics/docs/09-hamilton-equations-poisson-brackets.md)、[12](../../classical-mechanics/docs/12-constraints-dirac-theory.md)；量子力学 [03s2](../../quantum-mechanics/docs/03s2-phase-space-quantum-mechanics.md)、[14s](../../quantum-mechanics/docs/14s-quantum-information.md)、[09s2](../../quantum-mechanics/docs/09s2-second-quantization-rigor.md)。
> 学习目标：能不看原文复述论文的十步论证链，并说出每一步用到仓库里的哪一章；能解释四个主要结论各自的关键机制；能说清 §2 的 JT 引力为什么必须放在开头（它是反例）；能判断哪些地方是论文的新东西、哪些是标准工具的组合。

---

**单位约定**：$c=1$；论文正文用 $G_N$ 显式、$\hbar=1$（恢复 $\hbar$ 的地方会标出）；度规号差 $\eta=\mathrm{diag}(-,+,+,+)$，与本书一致、与 QFT 书相反。面积谱步长等量子结果保留 $\hbar$。

## 1. 一句话总结

**这篇论文要做的不是"把引力场量子化"，而是"在有限子区域上，先解掉约束、把相空间压到边界与角点，再用算子代数的方式造出 Hilbert 空间，使得每一次中间态求和都绝对收敛"。** 它选零锥作边界（约束退化成输运方程，能解），选一阶引力作变量（标架是物理数据，约束不带导数），选代数优先（没有优选真空），选高斯态作表示（给出类型 I 因子，可以取迹、可以截断）。四个结论——振幅绝对收敛、因果菱形 Hilbert 空间有限维、黑洞熵的对数修正与 Sen 的欧氏结果一致、单圈半经典 Einstein 方程——都是这条链上的推论。

## 2. 问题：为什么非要做这件事

微扰量子引力把度规写成"背景 + 小扰动"，两圈就不可重整。三条主流替代路线各有卡点：

- **弦论**：长波极限给 GR，但弦耦合展开本身不是非微扰的定义（至少在平直空间散射之外）。
- **圈量子引力**：Ashtekar 变量 + 群平均可以处理切片内的 diffeo，但**Hamiltonian 约束**（"如何切片"）仍未有令人满意的解，半经典连续极限也未确立。
- **AdS/CFT**：边界 CFT 给出非微扰定义，但只在有渐近 AdS 边界时成立；有限体区域内的可观测量要靠边界对偶间接翻译。

论文的切口是：**不选无穷远边界，选一个有限因果菱形的边界。** 这个边界是两张零锥 + 两个 cap，天然带一个角点 $S$。三件事同时变好：

1. 零锥上的约束是**输运方程**，可以沿生成元一步步积分——约束能真解掉，而不是加括号。
2. 角点是**唯一的"内部边界交点"**，所有边界物理（面积、boost 荷、时钟）都堆在那里。
3. 有限区域意味着**不需要渐近结构**，也就不需要 AdS 或渐近平坦。

前置：[GR 7 因果结构](../../general-relativity/docs/07-causal-structure.md) §5（因果菱形的形状）。

## 3. 四个关键想法

### 3.1 舞台：因果菱形，用 caps 切掉顶点

$D=I^+(p)\cap I^-(q)$。两张零片 $H_p$、$H_q$ 交于角点 $S$（Minkowski 里是二维球面）。在 $t=\mp(T-\epsilon)$ 各取一个小球作 cap，把两个顶点切掉——目的是让零生成元有有限的仿射长度，否则顶点处面积振幅 $\varrho\to0$、时钟读数无定义。**caps 的大小不改变 $S$ 的位置**（[GR 7 自检 3](../../general-relativity/docs/07-causal-structure.md) 算过这件事）。

### 3.2 变量：一阶引力（Palatini/Plebański）

不用 $g_{\mu\nu}$，用标架 $e^a{}_\mu$ 与自旋联络 $\omega^{ab}{}_\mu$。三个理由：

1. 标架给出**局部 Lorentz 标架**，才能在角点问"在哪个标架里测量"——标架的位置与取向是物理的边缘模。
2. 引力波的**两个偏振**可以干净地放在 cut 的共形度规里。
3. **简单性约束不含导数** ⇒ 变分不产生边界项 ⇒ 同一套边界变量可以缝合，且带着 2 个传播自由度。

前置：[GR 5s](../../general-relativity/docs/05s-first-order-gravity.md)。

### 3.3 策略：代数优先

弯曲时空没有优选真空，时空本身还在涨落，"先选态再定义算符"不可行。所以：

$$\text{先定可观测量代数（用约化作用量对源 }j\text{ 求导来定义插入）}
\;\longrightarrow\;
\text{再选表示（GNS）}.$$

标题里的 "algebraic" 就是这个意思。它不是什么哲学立场，而是**唯一在"没有背景"时仍然可操作的定义顺序**。

前置：[QFT 第 9 阶段 02 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md)（GNS、型分类）、[量子力学 09s2](../../quantum-mechanics/docs/09s2-second-quantization-rigor.md)（C*-代数的入口）。

### 3.4 时钟：角点 boost

零生成元的仿射参数 $u$ 从 cap 上置零、在角点读出。这不是一个"外部时间"，而是**边界几何自己的读数**：

- 角点标架的相对 boost 相位就是 $u$ 的共轭量；
- boost 荷是 $\hat K=\hat{\mathcal A}/(8\pi G_N)$——**面积就是 boost 荷**；
- 单位 boost 的 Noether 荷 $Q_\xi=\mathcal A/(8\pi G_N)$；
- 解析延拓 boost 到 $i\pi$，角点项给 $e^{-2\pi K}=e^{-\mathcal A/(4G_N\hbar)}$——Gibbs 权重。

前置：[GR 12](../../general-relativity/docs/12-covariant-phase-space.md) §5–6 与自检 5；[QFT 第 9 阶段 03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)（JT 里的同一构造）。

## 4. 论证链：十步

### 第 1 步：零锥上的自由数据

在 $H_p$ 上可以自由指定：每张 cut 的**共形度规** $\bar q_{AB}$（两个偏振）+ **面积振幅** $\varrho$ + cap 上的面积元与膨胀的初值。面积沿生成元的演化由 **Raychaudhuri 方程**积分出来：

$$\ddot\varrho+\frac{\varrho}{8}\left(\partial_u\bar q\right)^{AB}\left(\partial_u\bar q\right)_{AB}=0 .$$

这是论文 (3.25f)。**没有椭圆约束**——这就是"约束能解掉"的全部内容。

> 工具：[GR 8](../../general-relativity/docs/08-null-hypersurface-geometry.md) §4–5（含这个 $1/8$ 的完整推导）。

### 第 2 步：约化相空间

解约束后的相空间 $\mathcal P(D)$ 由 $(e,\omega(e),e_\Sigma)$ 模掉 diffeo 与局部 Lorentz 变换组成（论文 (3.19)）。**"有限 $G_N$ 下的约化相空间"** 就是这个意思：没有背景度规，没有微扰展开，$G_N$ 在指数里而不是在展开参数里。

> 工具：[GR 5s](../../general-relativity/docs/05s-first-order-gravity.md)（一阶变量）、[GR 7](../../general-relativity/docs/07-causal-structure.md)（特征初值的适定性）、[理论力学 12](../../classical-mechanics/docs/12-constraints-dirac-theory.md)（约化相空间的一般框架）。

### 第 3 步：辛形式只剩边界与角点

在约束面上，bulk 的辛形式消去，只剩下边界项与角点项。于是读出两件事：

- 辐射数据的 Poisson 括号（$\bar q_{AB}$ 与它的共轭动量）；
- **角点 boost 荷 $K=\mathcal A/(8\pi G_N)$**。

论文 (3.41)、(3.51)、(3.50c)。

> 工具：[GR 12](../../general-relativity/docs/12-covariant-phase-space.md) §3–6（预辛势、$\Omega$ 与切片无关、Noether 荷、边缘模）、[GR 10](../../general-relativity/docs/10-boundary-terms-action.md) §4（零边界项是全导数 ⇒ 只剩角点）。

### 第 4 步：把括号提升为对易关系

论文 §4.1：用**约化作用量的形变**来定义可观测量代数——耦合一个源 $j$，对 $j$ 求导就是插入算符。这是"代数优先"的技术实现。

> 工具：[QFT 07s](../../qft-sm/docs/stage-04-qft-core/07s-phase-space-path-integral-and-ordering.md)（源、生成泛函、接触项）、[GR 12](../../general-relativity/docs/12-covariant-phase-space.md) §7。

### 第 5 步：高斯态给类型 I 因子

在正则对上取高斯波函数（挤压态），边界可观测量生成的代数是**类型 I**。对比：QFT 的局域代数是类型 III$_1$，**没有迹、没有密度矩阵**。类型 I 的意义是：

- 有密度矩阵 $\rho$、有 von Neumann 熵；
- 可以被**有限维**截断到 $\mathcal B(\mathcal H_D)$；
- 迹上的求和是真正的求和（而不是形式记号）。

> 工具：[QFT 第 9 阶段 02 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md)（型分类、III$_1$ 为什么没有迹）、[量子力学 03s2](../../quantum-mechanics/docs/03s2-phase-space-quantum-mechanics.md)（高斯态、Wigner 函数）。

### 第 6 步：绝对收敛（论文最锋利的一刀）

相邻区域空间缝合（entangling product）：两侧的角点荷相加为零，只保留同时满足两边约束的态。时间合成（沿 cap 粘合）：把恒等算子按正交基展开，

$$\langle\phi|U_{M_2}U_{M_1}|\psi\rangle=\sum_\alpha\langle\phi|U_{M_2}|e_\alpha\rangle\langle e_\alpha|U_{M_1}|\psi\rangle .$$

两个因子都是同一个 Hilbert 空间里的内积，**幺正性保证它们的范数不随时间变**，于是 Cauchy–Schwarz：

$$\sum_\alpha\left|\langle\phi|U_{M_2}|e_\alpha\rangle\langle e_\alpha|U_{M_1}|\psi\rangle\right|\le\sqrt{\langle\phi|\phi\rangle\langle\psi|\psi\rangle}.$$

**求和绝对收敛，即使中间切片上有无穷多个态。**

具体算例：零锥上引力子对的产生与湮灭。第 $k$ 个径向模的方差是 $(\Delta q_k)^2=1/(2sk)$（$s=\mathcal A/(4G_N\hbar)$），两个插入的相位给出 $e^{-2ik/s}$，求和

$$\sum_k\frac{e^{-2ik/s}}{k^2}=\mathrm{Li}_2\!\left(e^{-2i/s}\right),$$

**有限闭式**。而按 $G_N$ 逐阶展开，$O(G_N)$ 修正里出现 $\sum_k 1/k$ 的**对数发散**。同一组图，先求和再展开是有限的，先展开再求和是发散的——**求和的顺序有物理意义**。

> 工具：[QFT 第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)（论文层面的复述）、[量子力学 14s](../../quantum-mechanics/docs/14s-quantum-information.md)（迹距离/保真度是同一套 Hilbert 空间不等式的亲戚）。

### 第 7 步：有限维 Hilbert 空间

时钟读数 $\bar u^*$ 给面积一个上界（因为 $\varrho\le u$，面积 $\le4\pi u^2$）；固定面积下，**剪切只会增大时钟读数**——所以在 4 维里"投影到 $\bar u^*\le\ell(D)$"同时限制了辐射态。于是：

$$\ell(D)\text{ 固定}\;\Longrightarrow\;\mathcal H_D\text{ 有限维}\;\Longrightarrow\;\hat{\mathcal A}\text{ 离散谱，步长 }8\pi G_N\hbar .$$

步长的来源：插入一个 boost 频率为 $k$ 的引力子，面积加 $8\pi G_N\hbar k$（论文 (4.12b)）。

> 工具：[GR 8](../../general-relativity/docs/08-null-hypersurface-geometry.md) §5.3（$\varrho\le u$ 与"剪切增大时钟读数"）、[QFT 第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)。

### 第 8 步：熵与对数修正

把未来半边与它的时间反射沿 cap 粘起来，时间演化与它的伴随相消，只剩角点的相对 boost；解析延拓到 $i\pi$（半转），每个态得到权重 $e^{-s_i}$，$s_i=\mathcal A_i/(4G_N\hbar)$。于是

$$S(\rho_D)=-\mathrm{Tr}(\rho_D\log\rho_D)=\frac{\langle\hat{\mathcal A}\rangle}{4G_N}+\log Z_{D,1}.$$

面积项是 Bekenstein–Hawking。$\log Z$ 给出对数修正。固定质量、对两个角点求和后：

$$q=\frac{257}{302},\qquad \frac{q}{2(1-q)}-\frac12=\frac{106}{45},$$

与 Sen 用欧氏方法得到的一圈系数一致（自检 5 验算）。

> 工具：[QFT 第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)（完整链条）、[GR 12](../../general-relativity/docs/12-covariant-phase-space.md) §5（Wald 熵 $A/4G$ 的经典版）。

### 第 9 步：半经典极限

相干初态下，$\langle T_{\mu\nu}\rangle$ 满足单圈半经典 Einstein 方程；反作用用 in-in（Schwinger–Keldysh）形式算，接触项由排序处方管住。

> 工具：[QFT 第 9 阶段 01 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/01-qft-curved-spacetime-semiclassical.md)（单圈有效作用量、in-in、半经典方程）、[QFT 07s](../../qft-sm/docs/stage-04-qft-core/07s-phase-space-path-integral-and-ordering.md)（接触项）。

### 第 10 步：公理化（App E）

把上面的结构抽象成一组 Lorentzian 公理：闭时空的振幅决定切上的 Hilbert 空间与边界代数上的迹；当欧氏圆柱的迹有限时，这与欧氏 Osterwalder–Schrader 公理等价。这一步是"合法性声明"，不是新计算。

> 工具：仓库没有专章——这是**已知缺口**（见 [GR 书接口](../../general-relativity/README.md)与本篇 §7）。

## 5. 四个主要结论

| 结论 | 关键机制 | 前置 |
|---|---|---|
| 每个中间态求和绝对收敛 | 幺正性 + Cauchy–Schwarz；$\mathrm{Li}_2$ vs $\log$ | 本篇 §4 第 6 步 |
| 因果菱形 Hilbert 空间有限维 | 时钟截断 + 聚焦（$\varrho\le u$）+ 剪切增大时钟读数 | [GR 8](../../general-relativity/docs/08-null-hypersurface-geometry.md) |
| 黑洞熵的对数修正 $106/45$ | 类型 I 的迹 + $2\pi$ boost 权重 + 角点单圈 | [QFT 9-04](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md) |
| 单圈半经典 Einstein 方程 | 相干态 + in-in + 接触项 | [QFT 9-01](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/01-qft-curved-spacetime-semiclassical.md) |

## 6. §2 的 JT 引力为什么必须放开头

它是**反例**，不是热身。

JT 里 dilaton 在两个角点被固定，时钟读数只依赖测地长度，所以**任意占据数态都可以有相同的时钟波函数** ⇒ 无限多正交态 ⇒ 类型 $\mathrm{I}_\infty$ ⇒ $\mathrm{Tr}\,W=\infty$，密度矩阵不存在。

4 维之所以不同，只因为一件事：**引力波有两个偏振**。固定面积下，剪切改变时钟读数，于是"时钟截断"同时限制了辐射态。**是传播自由度救了有限性。**

这个对照把论文的逻辑讲透了：2 维里"零锥 + 角点"的所有结构都在，唯独缺了"剪切影响时钟"这条链；4 维里补上它，整个有限性论证才成立。

> 前置：[QFT 第 9 阶段 03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)（JT 的完整构造与 $\mathrm{I}_\infty$）、[GR 8](../../general-relativity/docs/08-null-hypersurface-geometry.md) §5.3。

## 7. 读法与已知缺口

**三遍读法**：

1. **第一遍**：读 §1 + §2 + §5 的结论段，建立"零锥 → 有限维 → 熵"的主线。跳过所有公式。
2. **第二遍**：读 §3 + §4，每读一节回到本篇 §4 的对应步，把"这一步要什么工具"对上仓库章节。
3. **第三遍**：读 App A–D，只挑你要复现的计算（推荐 App B 的 (B.3)，因为它与 [GR 8](../../general-relativity/docs/08-null-hypersurface-geometry.md) §5.3 是同一件事的两种写法）。

**已知缺口**（仓库里还没有、读论文时会卡的地方）：

1. **Lorentzian 公理体系（App E）**：闭时空振幅 → Hilbert 空间 + 迹，与欧氏 Osterwalder–Schrader 的等价。任何书都没写。
2. **弯曲时空单圈热核（Seeley–DeWitt $a_2$）与角点单圈**（App D.1/D.3）：$106/45$ 的系数就是 $a_2$ 的 Gauss–Bonnet 项积出来的。QFT 06 篇有一圈重整化，但没有曲率热核。
3. **Sen 的熵函数方法**：作为欧氏侧的对照，仓库只有结论。
4. **纠缠积（entangling product）的完整代数版**（§3.6）：[QFT 9-02](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md) 有代数语言，但没有"两侧荷相加为零"的缝合定理。

这四条不影响读懂主线；卡住时按"结论级"处理即可。

## 8. 小结

- 论文的目标是有限子区域的**非微扰**代数量子化，不是"量子化度规"。
- 三个选择：零锥边界（约束变输运方程）、一阶引力（标架是物理数据、约束不带导数）、代数优先（没有优选真空）。
- 十步链：自由数据 → 约化相空间 → 辛形式只剩角点 → 括号量子化 → 高斯态给类型 I → Cauchy–Schwarz 保证绝对收敛 → 时钟截断给有限维 → boost 权重给熵 → 相干态给半经典方程 → 公理化。
- 核心不等式只有一条：$\varrho\le u$（聚焦）⇒ 面积上界 ⇒ 态数有限。4 维的传播自由度让"剪切增大时钟读数"，这是与 JT 的分水岭。
- 最锋利的结论是"求和顺序有物理意义"：非微扰求和 $\mathrm{Li}_2$ 有限，逐阶展开 $\log$ 发散。
- 与已知物理的唯一定量对照是 $106/45$ 与 Sen 的欧氏结果一致。

## 自检问题

**1.** 为什么必须用零锥作边界？如果改用类空切片，会在哪一步卡住？请把"卡住"具体到方程类型。

<details markdown="1"><summary>点击显示答案</summary>

**类空切片上的问题**：给定 $(h_{ij},K_{ij})$，要满足

$$\mathcal H=h^{ij}\left(K_{ij}K^{kl}-K_{ik}K_{jl}\right)+\ldots=0,\qquad
\mathcal H_i=\nabla_j\left(K^j{}_i-\delta^j_iK\right)=0 .$$

这是**四个椭圆型方程**（在适当的叶层上），约束的是 $h_{ij}$ 与 $K_{ij}$ 的**空间分布**：要判断一组数据是否合法，必须解一个边值问题，global 且非局部。解完之后还要选规范、演化——这就是 ADM 路线的全部困难（[理论力学 12](../../classical-mechanics/docs/12-constraints-dirac-theory.md) 的框架，[GR 11](../../general-relativity/README.md) 的计划内容）。

**零锥上的对照**：在零锥上，约束退化成**沿生成元的输运方程**。最典型的是 Raychaudhuri：

$$\ddot\varrho+\frac{\varrho}{8}\left(\partial_u\bar q\right)^2=0 .$$

这是**常微分方程**（沿 $u$），给定初值就能积分。其余约束（论文 App A 的 null constraints）也都是"给定 cut 上的数据，沿生成元推进"的结构。所以：

- **卡住的位置**：类空切片卡在"约束是椭圆方程，不能显式解"；零锥不卡，因为约束是 ODE。
- **代价**：零锥的边界不是类空切片，诱导度规退化，边界项不能直接用 GHY（[GR 10](../../general-relativity/docs/10-boundary-terms-action.md) §4）；而且要在角点处理边缘模。
- **收益**：约束真解掉了，得到的是**约化相空间**，不是"约束面 + Dirac 括号"。这使论文能把 Poisson 括号直接提升为对易关系（§4），不需要处理第一类约束的量子化问题。

**一句话**：类空切片把困难放在"解约束"，零锥把它挪到"处理退化边界"。论文选择后者，因为退化边界上的物理恰好都集中在角点上——而角点正是它想要的。$\square$

</details>

**2.** 为什么"类型 I"是熵计算的前提？如果代数是类型 III$_1$，会在哪一步失败？

<details markdown="1"><summary>点击显示答案</summary>

**类型 III$_1$ 的困难**（QFT 局域代数的标准情形，[QFT 9-02](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md)）：

1. **没有迹**。类型 III 的 von Neumann 代数上不存在正规的半有限迹 $\mathrm{Tr}$，因此不能写 $\rho=\sum p_i|i\rangle\langle i|$，也不能定义 $\mathrm{Tr}\,\rho$。
2. **没有密度矩阵**。任何态都是"奇异"的，不能由某个可积算符表示；只能作为代数上的线性泛函存在。
3. **没有 von Neumann 熵**。$-\mathrm{Tr}\rho\log\rho$ 无从定义（不存在 $\rho$）。
4. **没有有限维截断**。类型 III 的投影等价类结构不允许"取前 $N$ 个态"这种操作，因为不存在最小投影。

**在哪一步失败**：

- 论文 §5 的熵公式 $S=\langle\hat{\mathcal A}\rangle/4G_N+\log Z$ 直接用 $\mathrm{Tr}$ 与 $\rho_D$——在类型 III 里这两个对象不存在。**第 8 步直接失效。**
- 论文 §5.2 的"有限维 $\mathcal H_D$"也无从谈起：没有迹就不能说"维数"。

**论文怎么绕开**：它构造的表示（高斯态 + 有限维截断）使代数成为类型 I，具体是 $\mathcal B(\mathcal H_D)$（有限维矩阵代数）在某个极限下的直和/积分。类型 I 的代数**天生带迹**（矩阵的迹），所以：

$$\rho_D=\frac{e^{-\hat{\mathcal A}/4G_N\hbar}}{Z},\qquad S=-\mathrm{Tr}\rho_D\log\rho_D$$

全部有定义。

**为什么这不"作弊"**：类型不是代数本身的内在属性，而是"代数 + 态"的配对（GNS 表示）的属性。同一个抽象代数，在不同态下可以给出不同类型。论文选高斯态，正是选了一个让表示为类型 I 的态。这里的关键物理是**有限 $G_N$ + 时钟截断**：截断把无限维压成有限维，有限维矩阵代数必然是类型 I。

**对照**：QFT 在 Minkowski 真空下是 III$_1$，这不是"数学缺陷"，而是"没有自然的热力学"的精确表述——这正是为什么黑洞熵在 QFT 里要靠引力补上。论文的做法相反：**从一开始就用引力让代数变成类型 I**，于是热力学是内建的。$\square$

</details>

**3.** 复述绝对收敛的三步证明，并解释为什么"先展开再求和"会出 $\log$ 发散而"先求和再展开"不会。

<details markdown="1"><summary>点击显示答案</summary>

**三步**：

1. **幺正性**：时间演化 $U_M$ 保范数（论文 (4.18)）。所以 $\|U_{M_1}|\psi\rangle\|=\||\psi\rangle\|$、$\|U_{M_2}^\dagger|\phi\rangle\|=\||\phi\rangle\|$。
2. **Cauchy–Schwarz**：在恒等分解 $\sum_\alpha|e_\alpha\rangle\langle e_\alpha|=1$ 下，
$$\sum_\alpha\left|\langle\phi|U_{M_2}|e_\alpha\rangle\langle e_\alpha|U_{M_1}|\psi\rangle\right|
\le\left(\sum_\alpha|\langle e_\alpha|U_{M_2}^\dagger|\phi\rangle|^2\right)^{1/2}
\left(\sum_\alpha|\langle e_\alpha|U_{M_1}|\psi\rangle|^2\right)^{1/2}
=\|\phi\|\,\|\psi\| .$$
3. **截断的误差可控**：对多个 cut，用投影 $P_j$ 只保留有限个态；误差由 $\|(1-P_j)U_j\cdots U_1|\psi\rangle\|$ 控制，逐 cut 趋于零（论文 (4.31)）。所以"取前 $N$ 个态"的截断收敛到真振幅。

**关键点**：第 2 步完全没有用到 $H$ 的具体形式，只用了"两个因子在同一个 Hilbert 空间里、范数固定"。所以这个证明对**任何**幺正演化都成立——绝对收敛不是动力学的巧合，而是 Hilbert 空间几何的必然。

**为什么先展开会出 $\log$**：逐阶展开 $G_N$ 等价于把 $e^{-2ik/s}$ 按 $1/s$ 展开（$s=\mathcal A/4G_N\hbar$，$G_N\to0$ 时 $s\to\infty$）：

$$e^{-2ik/s}=1-\frac{2ik}{s}+O(1/s^2).$$

求和 $\sum_k(\Delta q_k)^4e^{-2ik/s}$：

- 零阶：$\sum_k 1/k^2=\zeta(2)$，收敛；
- 一阶：$\frac{1}{s}\sum_k 1/k$，**对数发散**（$k$ 到 UV 截断 $\Lambda$ 时 $\sim\log\Lambda$）。

**为什么先求和不会**：$\sum_k e^{-2ik/s}/k^2=\mathrm{Li}_2(e^{-2i/s})$ 在 $k\to\infty$ 时被 $e^{-2ik/s}$ 的相位"抹平"——注意这不是衰减（模为 1），而是**振荡求和**（Abel/Dirichlet 求和），$\mathrm{Li}_2$ 在单位圆上除 $z=1$ 外解析。所以求和本身收敛，极限 $s\to\infty$ 才出现 $1/s$ 的奇异性。

**物理解读**：$e^{-2ik/s}$ 是"引力子对在角点 boost 下的相位"。它含 $1/s=4G_N\hbar/\mathcal A$——**不是小参数**，是与 $k$ 无关的固定相位。逐阶展开等于假设 $k\ll s$（所有模的波长都远小于面积尺度），而 UV 的模恰恰不满足。所以：

$$\text{展开参数 }G_N\text{ 与求和指标 }k\text{ 不对易}
\;\Longleftrightarrow\;
\text{UV 与红外在角点处纠缠}.$$

这正是"非微扰但有限"的含义：不是找到了新的抵消，而是**根本没有产生发散的那一步**。$\square$

</details>

**4.** 为什么 JT 引力给出 $\mathrm{I}_\infty$ 而 4 维给出有限维？请把差别定位到一个具体的自由度。

<details markdown="1"><summary>点击显示答案</summary>

**JT 的结构**：二维 dilaton 引力，作用量 $\Phi(R+2)$ 型。因果菱形的"面积"就是 dilaton 的值 $\Phi(S_L),\Phi(S_R)$，在两个角点被固定。

- 时钟读数 $u^*$ 只依赖测地长度（论文 (2.4c)、(2.13b)）；
- **每个占据数态可以有相同的时钟波函数**；
- 于是 $\Psi_n$ 构成无限正交族，代数弱闭包是 $\mathcal B(\mathcal H_D)$，$\mathcal H_D$ 无限维 ⇒ 类型 $\mathrm{I}_\infty$；
- 迹 $\mathrm{Tr}\,W=\sum_n e^{-2\pi(K_L+K_R)}=\infty$ ⇒ 没有密度矩阵。

**4 维多出的东西**：**引力波的两个偏振**，编码在 cut 的共形度规 $\bar q_{AB}$ 里。它们的作用是：

1. $\bar q_{AB}$ 的变率就是剪切 $\sigma_{AB}=\frac{\varrho^2}{2}\partial_u\bar q_{AB}$；
2. 剪切出现在 Raychaudhuri 里：$\ddot\varrho+\frac{\varrho}{8}(\partial_u\bar q)^2=0$；
3. 所以**固定面积下，剪切越大，$\varrho$ 增长越慢，要达到给定面积需要的 $u$ 越大**——时钟读数变大。

于是"投影到 $u^*\le\ell(D)$"不再只限制几何，还**同时限制了辐射态**：剪切不能任意大，$\bar q$ 不能任意"抖动"。这就把无限维压成有限维。

**定位到自由度**：差别就是"$\bar q_{AB}$ 有没有动力学"。JT 里 dilaton 是唯一的度量自由度，且被边界条件钉死；4 维里 $\bar q_{AB}$ 是**传播自由度**（两个偏振），它的变率通过 Raychaudhuri 反作用于时钟。

**这个对照的方法论意义**：它说明"有限性"不是来自"离散化"或"截断"，而是来自**动力学对几何的反作用**。论文没有引入任何格点或 UV 截断；它只是让"传播自由度影响时钟"这条链跑通，然后数学自己给出有限维。这是全文最值得学的一招。$\square$

</details>

**5.** 验证 $q=257/302$ 与 $106/45$ 的关系；并说明这两个数各自是什么、为什么要经过 $q$ 才能得到 $106/45$。

<details markdown="1"><summary>点击显示答案</summary>

**代数验证**：

$$1-q=1-\frac{257}{302}=\frac{45}{302},\qquad 2(1-q)=\frac{90}{302},$$

$$\frac{q}{2(1-q)}=\frac{257/302}{90/302}=\frac{257}{90},\qquad
\frac{q}{2(1-q)}-\frac12=\frac{257}{90}-\frac{45}{90}=\frac{212}{90}=\frac{106}{45}.\qquad\square$$

**$q$ 是什么**：由 (5.68)，$q=257/302$ 是**配分函数随面积增长的指数**：$Z_{D,1}\sim s_b^{q}$（更准确地说，$\log Z$ 正比于 $q\log s_b$）。它来自两个因子：

- 态密度随面积的幂次（与 $\mathcal H_D$ 的维数增长有关）；
- 单圈行列式的 $106/45$（(5.67c)）。

具体地，(5.67c) 给出 $\log\mathrm{Tr}(\hat C_b^\dagger\hat C_b)=\frac{106}{45}\log s_b+O(1)$，而 (5.66) 的测度给 $q$ 一个 $1/2$ 的修正。所以 $q$ 是"总幂次"，$106/45$ 是"单圈部分的幂次"。

**为什么要经过 $q$**：因为熵的 $\log$ 修正有两个来源，它们在 (5.69) 里合成：

$$S=\frac{\mathcal A}{4G_N}+\log Z,\qquad \log Z\sim q\log s_b .$$

但实验/欧氏对照的是**固定质量**下的熵，不是固定面积。从面积变到质量要换变量：$s_b\propto G_N^2M^2/\hbar$，$\mathrm{d}s_b/s_b\propto2\,\mathrm{d}M/M$。换变量时 $q$ 的幂次被 $1/(2(1-q))$ 的 Jacobian 修正，再减去面积项本身的 $1/2$：

$$\frac{q}{2(1-q)}-\frac12=\frac{106}{45}.$$

**读法的要点**：

- $q=257/302$ 是**理论内部**的量（洛伦兹迹的增长指数）；
- $106/45$ 是**与欧氏结果对照**的量（固定质量下熵的 $\log$ 系数，Sen 1994）；
- 两者差一个换变量的 Jacobian。这个 Jacobian 不是拟合出来的，是 $s_b\propto M^2$ 与 $q$ 的幂次决定的。

**为什么这个对照有分量**：Sen 的结果来自完全不同的方法（欧氏路径积分 + 熵函数 + 热核），而这里来自洛伦兹迹 + 类型 I 密度矩阵 + 角点单圈。两条路给出同一个有理数 $106/45$，这是论文唯一的定量外部检验，也是它最硬的地方。$\square$

</details>

## 参考

- V. Chandrasekaran, "An algebraic quantization of gravity from the null cone", arXiv:2611.34924v1（2026）。本仓库的原文抽取件不在版本控制内，阅读时以 arXiv 为准。
- 论文 §1 的文献地图：微扰不可重整 [1]、圈量子引力的 Hamiltonian 约束 [3–6]、AdS/CFT 与纠缠熵 [7–10]、子区域代数与边缘模 [11–14]、零锥初值 [21–25]、JT 引力 [26]、三维引力 [27]、Virasoro TQFT [28]、Sen 的熵修正 [34]。
- 本仓库的伴读：[QFT 第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)（论文逐节复述）、[03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)（JT）、[02 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md)（算子代数）、[01 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/01-qft-curved-spacetime-semiclassical.md)（弯曲时空 QFT）。
- 几何前置：[GR 5s](../../general-relativity/docs/05s-first-order-gravity.md)、[7](../../general-relativity/docs/07-causal-structure.md)、[8](../../general-relativity/docs/08-null-hypersurface-geometry.md)、[10](../../general-relativity/docs/10-boundary-terms-action.md)、[12](../../general-relativity/docs/12-covariant-phase-space.md)。
- 算符语言：[QFT 07s](../../qft-sm/docs/stage-04-qft-core/07s-phase-space-path-integral-and-ordering.md)（相空间路径积分、Weyl 排序、接触项）、[量子力学 03s2](../../quantum-mechanics/docs/03s2-phase-space-quantum-mechanics.md)（Wigner 函数与 Moyal 星积）。
- 经典力学底座：[理论力学 9–10](../../classical-mechanics/docs/09-hamilton-equations-poisson-brackets.md)（辛形式）、[12](../../classical-mechanics/docs/12-constraints-dirac-theory.md)（约束与约化）。
