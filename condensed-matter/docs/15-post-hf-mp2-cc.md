# HF 之后：相关能、MP2 与耦合簇

> 路线图位置：第四部分（多电子问题怎么算）· 第 15 章
> 前置知识：[第 14 章](14-exact-methods-fci-ed.md)（FCI、H₂ 显微镜、静态相关）；第 6 章[相互作用电子气](06-interacting-electron-gas.md)（HF 变分、交换穴、RPA 环图）；[QFT 书微扰论](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)与[一圈重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)（费曼图、Wick 定理的语言）。
> 学习目标：理解相关能的定义与量级（1% 的能量、100% 的化学）；会推 Brillouin 定理与 MP2 能量公式，并把 Goldstone 图认作 QFT 费曼图的凝聚态表亲；会用一个两能级模型亲手证明截断 CI 不大小一致而耦合簇严格大小一致；理解 $e^T$ 拟设为何自动包含断开的高阶激发（这是 CC 精度的来源）、CCSD(T) 为什么叫黄金标准、代价 $N^6/N^7$ 如何把它挡在固体门外。
>
> 记号约定：原子单位（同第 14 章）。$i,j,k,l$ 计占据自旋轨道，$a,b,c,d$ 计空轨道，$p,q,r,s$ 通用；$\Phi_0$ 为 HF 基态行列式；$\Phi_{ij}^{ab}$ 为双激发行列式。

---

## 1. 一句话总结

**HF 的误差叫相关能——总量级仅 ~1%，却是化学的全部：H₂ 解离错的 8.5 eV（静态相关，第 14 章）与平衡位形的 ~1 eV 短程回避不足（动态相关）都记在这本账上。修账有两条路：MP2 用二阶微扰把"电子成对虚激发"的动能收益算出来（Goldstone 图 = QFT 费曼图的同一台机器），代价 $N^5$、精度 ~1 kcal/mol 量级，但在静态相关处发散；耦合簇把修正写成指数拟设 $\Psi = e^T\Phi_0$，指数自动生成一切"断开的"高阶激发乘积——这正是动态相关的主体——从而严格大小一致、精度随截断 rank 系统性爬升（CCSD $N^6$、CCSD(T) $N^7$，后者是单参考问题的黄金标准）。CC 的疆界也清楚：静态相关面前 $e^T$ 收敛半径失效（多参考问题），固体面前 $N^7$ 代价失效——两条边界分别通向下一章的 DFT 与第 13 章的强关联。**

## 2. 相关能：HF 差的那 1%

**定义**（ Löwdin）：$E_\text{corr} = E_\text{exact} - E_\text{HF}$（同一基组、同一几何）。量级账：

- 总能量：每个电子 ~ 数十 Ha（H₂O 约 −76 Ha）；
- HF 误差：每对电子 ~ 0.02–0.04 Ha（H₂ 平衡位形 $E_\text{corr} \approx -0.041$ Ha ≈ 1.1 eV，He 原子 $-0.042$ Ha）；
- 化学精度：1 kcal/mol = 1.6 mHa = 0.043 eV——反应能与势垒的实验可信度。

于是 HF 相对误差 $10^{-3}$ 量级，绝对误差却是化学精度的几十倍：**算反应必须修相关**。

**病根**（第 6 章 3 节的延续）：HF 的单行列式里，**同自旋**电子通过交换穴互相回避（$g_{\uparrow\uparrow}(0) = 0$），但**反自旋**电子没有任何关联——平均场上每个电子照样能踩在反自旋电子头上。真实库仑下任何两个电子都该互相回避一点：这份"反自旋对也躲开"的短程收益就是**动态相关**，需要至少两个行列式的线性组合（把一对电子虚激发出去、降低同处概率）才能表达。**静态相关**则是另一头：第 14 章的 H₂ 解离——近简并组态必须强混合，单参考的误差以 eV 计。本章的方法（MP2、CC）是动态相关的手术刀；静态相关是它的手术禁区（第 5 节）。

## 3. MP2：二阶微扰论

### 3.1 分割与 Brillouin 定理

把 $H$ 拆成"已解的"与"微扰"：$H = H_0 + V$，取 $H_0 = \sum_i \varepsilon_i a_i^\dagger a_i$（Fock 算符——HF 自己的产物，本征值即轨道能）。第一步检查一阶：$E^{(1)} = \langle\Phi_0\lvert V\lvert\Phi_0\rangle$ 修的正是 HF 能量定义里已有的部分（$E_\text{HF} = \langle H\rangle$），而波函数一阶修正 $\Phi^{(1)} = \sum_\mu \frac{\langle\mu\lvert H\lvert\Phi_0\rangle}{E_0 - E_\mu}\Phi_\mu$ 里**单激发不出现**——Brillouin 定理：

$$\langle\Phi_i^a\lvert H\lvert\Phi_0\rangle = 0 \qquad(\text{正则 HF 轨道}),$$

证明见自检问题 1（ HF 轨道的变分条件恰是单激发梯度为零）。于是最低阶的非平凡修正是**纯双激发**的二阶能量：

$$\boxed{\;E_\text{MP2} = \frac14\sum_{ijab}\frac{\lvert\langle ij\lVert ab\rangle\vert^2}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b}\;}$$

（求和跑遍占据对 $ij$ 与空轨道对 $ab$；推导见自检问题 1；物理：每对占据电子"借"能量虚跳到空轨道再还回来，收益 $\propto$ 耦合平方除以能隙——标准二阶微扰结构，与第 13 章超交换 $J = 4t^2/U$ 同一模板。）

### 3.2 Goldstone 图：费曼图的凝聚态表亲

画出 $\langle ij\lVert ab\rangle\lVert ab\rangle ij\rangle$ 的耦合：两条电子线在两处相互作用——这就是最简单的 **Goldstone 图**。规则与 QFT 的费曼图（[QFT 书](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)）严格同构：线的传播、顶点的耦合、分母的"能量减能量"；差别只在"时间"是绝热开关的微扰序、粒子是电子而非相对论量子场。**连接簇（Goldstone）定理**保证只有连接图进入能量——断开的图等于子系统的能量乘积，会被逐块抵消（这就是 MP2 天生大小一致的图论表述，也是 QFT 里"只有连接图贡献 S 矩阵"的同一句话）。第 6 章 6 节的 RPA 环图、本章的 MP2 图、QFT 的真空极化图——同一棵树上三根枝。

### 3.3 性能与疆界

- **代价**：能量求和本身 $O(N_\mathrm{o}^2N_\mathrm{v}^2)$，瓶颈在把双体积分从原子轨道基变换到分子轨道基（四指标变换 $O(M^5)$）——习惯记 **$N^5$**。百原子分子日常可算。
- **精度**：平衡态、单参考体系 ~ 1–3 kcal/mol；更贵的修正（MP3/4）不保证单调变好——微扰级数常常渐近发散。
- **疆界**：分母 $\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b \to 0$ 时发散。HOMO–LUMO 能隙小的体系—— stretched 键、过渡金属、强关联——分母塌掉，MP2 灾难性地过度修正（自检问题 5 用第 14 章的 H₂ 亲手演示：解离处 MP2 $\to -\infty$ 而 FCI 完好）。**MP2 是"有能隙才有收敛半径"的方法**。

## 4. 耦合簇：指数拟设

### 4.1 先看 CI 为什么不够好

组态相互作用写 $\Psi = (1 + C_1 + C_2 + \cdots)\Phi_0$，线性、直观，截断到 CISD 久经考验——但有个结构性缺陷：**截断 CI 不大小一致**（size-extensive）。两个远离的子系统 A、B，严格能量应严格可加 $E(AB) = E(A) + E(B)$；截断 CI 做不到——自检问题 2 用一个两能级模型给出定量演示：CISD 对耦合双激发（A 上一个 double × B 上一个 double，整体是四激发）视而不见，能量高出缺陷 $\sim 4v^4/\Delta^3 \sim E_\text{corr}^2/\Delta$。He 原子 $E_\text{corr} \approx 0.042$ Ha、$\Delta \sim 1$ Ha 时缺陷已 ~7 mHa，超化学精度 4 倍——**体系越大、错误按分子数累积越快**，这对要算反应能（大分子差值）的化学是致命伤。

### 4.2 $e^T$：让断开的激发自动相乘

耦合簇的拟设是指数：

$$\Psi_\text{CC} = e^{T}\Phi_0,\qquad T = T_1 + T_2 + T_3 + \cdots,\qquad T_n = \frac{1}{(n!)^2}\sum t_{ij\cdots}^{ab\cdots} a_a^\dagger a_b^\dagger\cdots a_j a_i\cdots,$$

$T_n$ 把 $n$ 对电子激发出去，系数 $t$ 叫**簇振幅**。妙处全在指数的展开：$e^{T_2}\Phi_0 = (1 + T_2 + \tfrac12 T_2^2 + \cdots)\Phi_0$ 中 $\tfrac12T_2^2$ 项是**两对电子独立激发**——一个四激发，但它不是"四个电子协同跳"的连接四激发，而是"两处各自的双激发碰巧同时发生"的**断开乘积**。把 $\Psi$ 按 CI 系数展开（自检问题 4）：

$$c_2 = t_2 + \tfrac12t_1^2,\qquad c_3 = t_1t_2 + \tfrac{\text{次}}{6}t_1^3,\qquad c_4 \supset \tfrac12 t_2t_2',\ \cdots$$

动态相关的主要成分正是这些大量而微弱的独立对激发（每对 ~0.02 Ha，簇振幅 $\sim10^{-2}$–$10^{-1}$），它们的**乘积项**贡献了波函数里数量占绝对优势的高阶 CI 系数——CCSD 不算 $T_4$ 却精确包含 $\tfrac12T_2^2$ 的全部四激发，这就是**同 rank 下 CC 远胜 CI** 的原因。QFT 的对应物：这不是别的，就是把微扰级数按连接部分**指数化重求和**——与生成泛函 $Z = e^{iS_\text{连接}}$ 的 linked-cluster 定理一模一样。

### 4.3 大小一致：一行证明

非相互作用体系 $H = H_A + H_B$、$T = T_A + T_B$（$T_A$ 只作用在 A 的轨道上）。纯激发算符之间对易，故

$$e^{T} = e^{T_A + T_B} = e^{T_A}e^{T_B},\qquad \Psi_{AB} = e^{T_A}e^{T_B}\Phi_A\Phi_B = \Psi_A\cdot\Psi_B,$$

波函数严格可乘 ⇒ 能量严格可加，**任何截断 rank 下都成立**（自检问题 2 的模型里同一计算一行验证）。CI 做不到的，指数天生白送。

### 4.4 CC 方程与黄金标准

振幅方程取投影形式：

$$\langle\Phi_\mu\lvert\bar H\lvert\Phi_0\rangle = 0,\qquad \bar H \equiv e^{-T}He^{T},$$

即"激发后的波函数不再有残余单/双激发梯度"。$\bar H$ 的 BCH 展开**有限终止**：$H$ 至多双体，每个与 $T$ 的嵌套对易子至少消掉一条湮灭线，四重嵌套之后严格为零（自检问题 3）——CC 方程是有限项的、可显式编程的非线性方程组，迭代求解。截断 $T = T_1 + T_2$ 即 **CCSD**；三激发用微扰近似补上即 **CCSD(T)**。

经验账本（单参考、平衡几何）：

| 方法 | 代价 | 典型误差 |
|---|---|---|
| HF | $N^4$ | ~1 eV / 键 |
| MP2 | $N^5$ | 5–10 kcal/mol |
| CCSD | $N^6$ | 2–4 kcal/mol |
| CCSD(T) | $N^7$ | **~1 kcal/mol**（黄金标准） |
| CCSDT、CCSDTQ… | $N^8$、$N^9$ | 向 FCI 收敛 |

对成千上万小–中分子的反应能，CCSD(T)/cc-pVQZ 与实验的符合度达到"理论值可以当实验用"的程度——这是量子化学五十年最大的工程成就。**疆界有二**：静态相关（多参考）时振幅不再小、$e^T$ 展开失效（Cr₂ 分子是著名车祸现场；对付它要 CASSCF 等多参考方法，见[第 18 章](18-multireference-casscf.md)）；固体时 $N^7$ 的 $N$ 以万计——周期体系 CC 至今是稀有技能。两条边界合起来，恰好画出下一章 DFT 的领地：**便宜、能算固体、但精度不可系统控制**——量子化学的镜像互补。

## 5. 小结

- 相关能 = 化学的全部；动态（短程、双激发主导、MP2/CC 可修）与静态（近简并、多参考、需要别的方法）是两种病。
- MP2 = $H_0$ 取 Fock 的二阶微扰；Brillouin 定理保证一阶纯双激发；Goldstone 图与 QFT 费曼图同构；连接簇定理 = 大小一致的图论面孔。
- 截断 CI 不大小一致（缺陷 $\sim E_\text{corr}^2/\Delta$），CC 的 $e^T$ 通过自动生成断开乘积严格修复；同 rank 下 CC ≫ CI。
- CCSD(T)：单参考黄金标准 ~1 kcal/mol，$N^7$；疆界 = 静态相关与固体。
- 方法选择的坐标系：**能隙大、单参考 → CC 阶梯；能隙小、强混合 → 第 13 章与第 17 章；要算固体 → 第 16 章 DFT**。

## 自检问题

**1.** 证明 Brillouin 定理 $\langle\Phi_i^a\lvert H\lvert\Phi_0\rangle = 0$（正则 HF 轨道），并从 Rayleigh–Schrödinger 二阶能量公式出发推导 MP2 能量表达式。

<details markdown="1"><summary>点击显示答案</summary>

**Brillouin**：HF 能量 $E_\text{HF}(\{\phi\})$ 对轨道的变分（在正交约束下）给出 HF 方程；把变分方向取成"轨道 $i$ 混入空轨道 $a$"（酉变换生成元 $\kappa_{ai}$），驻点条件即

$$0 = \frac{\partial E_\text{HF}}{\partial\kappa_{ai}}\bigg|_0 = \langle\Phi_i^a\lvert H\lvert\Phi_0\rangle\ (\text{自旋适配后恰为该梯度}).$$

换句话说：**若单激发矩阵元非零，就能沿该方向再降能量，与"HF 是行列式中的能量极小"矛盾**。（注意仅对正则轨道成立；局域化轨道不满足。）

**MP2 推导**：Rayleigh–Schrödinger：$E^{(2)} = \sum_{\mu\ne0}\frac{\lvert\langle\mu\lvert H\lvert\Phi_0\rangle\vert^2}{E_0^{(0)} - E_\mu^{(0)}}$，$\mu$ 跑遍激发行列式。由 Brillouin，单激发矩阵元为零；由 Slater–Condon（第 14 章），三重以上激发也为零；只剩双激发 $\Phi_{ij}^{ab}$，其矩阵元 $\langle\Phi_{ij}^{ab}\lvert H\lvert\Phi_0\rangle = \langle ab\lVert ij\rangle$，未微扰能量差 $E_0^{(0)} - E_{ij}^{ab\,(0)} = \varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b$（占据轨道能量之和减空轨道能量之和）。对全部 $(ij,ab)$ 求和，每个反对称积分被四种指标排序重复计入，除以 4：

$$E_\text{MP2} = \frac14\sum_{ijab}\frac{\lvert\langle ij\lVert ab\rangle\vert^2}{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b}.$$

**核对结构**：分子是耦合平方、分母是"要付的能隙"——与超交换 $J = 4t^2/U$（第 13 章 5.3 节）逐项同构；那里虚跳的是局域电子、这里虚跳的是费米海上的电子对（第 3 章的费米面薄层在此处表现为：主导贡献来自 HOMO/LUMO 附近的轨道对）。

</details>

**2.** 大小一致性的解剖：设每个子系统只有一个能量为 $\Delta$ 的双激发组态、耦合 $v$。对双子系统分别求严格解、CISD 解与 CCSD 解，证明 CISD 能量高出 $4v^4/\Delta^3$，而 CCSD 严格可加；用 He 原子数据估算真实 CISD 的缺陷量级。

<details markdown="1"><summary>点击显示答案</summary>

**单体**：$2\times2$ 矩阵 $[\,E_0,\ v;\ v,\ E_0+\Delta\,]$，基态 $E = E_0 - \tfrac{v^2}{\Delta} + O(v^4)$（记 $E_\text{corr} = -v^2/\Delta$）。

**复合体系**：组态空间由 $|00\rangle, |d0\rangle, |0d\rangle, |dd\rangle$ 张成（$d$ 为激发）。严格基态 = 单体基态之积，能量恰 $2(E_0 - v^2/\Delta)$——对本模型严格。

**CISD**：四激发 $|dd\rangle$ 被截掉，剩三维空间 $\{|00\rangle,|d0\rangle,|0d\rangle\}$；由对称性约化为 $2\times2$：

$$\begin{pmatrix} 2E_0 & \sqrt2\,v \\ \sqrt2\,v & 2E_0 + \Delta \end{pmatrix}\;\Longrightarrow\; E_\text{CISD} = 2E_0 + \tfrac{\Delta}{2} - \sqrt{\tfrac{\Delta^2}{4} + 2v^2} \approx 2E_0 - \frac{2v^2}{\Delta} + \frac{4v^4}{\Delta^3}.$$

比严格值高出

$$\delta_\text{CISD} = \frac{4v^4}{\Delta^3} = \frac{4E_\text{corr}^2}{\Delta}\qquad(\text{每对子系统}).$$

**CCSD**：复合簇算符 $T = T_A + T_B$，$\Psi = e^{T_A}e^{T_B}|00\rangle$——指数展开自动包含 $T_AT_B|00\rangle \propto |dd\rangle$，即严格乘积态，能量精确可加。（本模型双激发是唯一的激发类型，CCSD = FCI = 严格。）

**真实量级**：He 的 $E_\text{corr} \approx 0.042$ Ha、典型 $\Delta \sim 1$ Ha：

$$\delta \sim \frac{4\times(0.042)^2}{1} \approx 7\ \mathrm{mHa} \approx 1.9\ \mathrm{kcal/mol}$$

每对 He–He 相互作用单元——化学精度的四倍，且随分子尺寸**线性累积**（$n$ 个单元缺陷 $\propto n$）。CI 阶梯每上一级（CISDT、CISDTQ）修掉一部分，但"截断就不严格可加"是结构性的；CC 从根上免疫。

</details>

**3.** 证明相似变换 $\bar H = e^{-T}He^{T}$ 的 BCH 展开在四重嵌套对易子后严格终止（$H$ 为至多双体算符、$T$ 为纯激发算符），并说明这条"有限性"对 CC 方程的可编程性意味着什么。

<details markdown="1"><summary>点击显示答案</summary>

**记号**：把正常乘积（相对参考态 $\Phi_0$）中的算符分类：纯激发（只有 $a_a^\dagger a_i$ 型）、纯退激发（$a_i^\dagger a_a$）、对角（$a_p^\dagger a_p$）与混合型。$T$ 只含纯激发项，故 $[T, T'] = 0$（两条纯激发串互不干扰）。

**关键引理（逐线计数）**：考虑嵌套对易子 $[\cdots[[H,T],T],\cdots]$ 中任一条**连接**的收缩链。$T$ 的每条激发线（$a_a^\dagger a_i$）要与 $H$ 中的算符收缩，只有两种下场：与 $H$ 的湮灭（空穴）算符 $a_i$ 收缩（此时消灭一条 $H$ 的退激发线），或把链延长。每多嵌套一层 $T$，能被"接住"的 $H$ 侧退激发线**严格减少至少一条**：因为每个 $T$ 线至多消费一条 $H$ 侧的孔湮灭线，而链要维持连接、不产生已抵消的真空泡。

**计数**：$H$ 的双体项 $a^\dagger a^\dagger aa$ 至多带**两条**孔湮灭线。第一层 $[H,T]$ 消掉一部分，第二层 $[[H,T],T]$ 再消；连接的四重嵌套 $[[[H,T],T],T]$ 需要第三条孔线来维持非零收缩——已不存在；故

$$\bar H = H + [H,T] + \frac12[[H,T],T] + \frac16[[[H,T],T],T] + \frac1{24}[[[[H,T],T],T],T],$$

第四项之后全为零。（第四项非零来自双体项的极端收缩拓扑；教材中常直接引用"双体哈密顿量的 BCH 在四重嵌套截断"。）

**可编程性**：$\bar H$ 是**有限个**多项式项之和，每项是簇振幅 $t$ 的低次多项式乘双体积分——CC 振幅方程因此是显式的、有限长度的非线性方程组，可以直接代码生成（这正是 CC 代码从 1970 年代手工推导到今日自动生成的发展线）。对比：微扰论每高一阶要重画全部图、CI 要处理不断增大的矩阵——CC 的"指数 + 有限 BCH"是三种结构里唯一把**非线性**作为代价换来**有限性**的。

</details>

**4.** 把 $\Psi = e^{T_1 + T_2}\Phi_0$ 展开到四级激发，写出 CI 系数与簇振幅的关系（$c_2, c_3, c_4$ 各包含哪些项）；用典型数值（$\lvert t_2\rvert \sim 0.05$、连接 $t_4 \sim 10^{-3}$）说明为什么 CCSD 里被丢弃的 $T_4$ 无关紧要、而 CISD 里被丢弃的四激发不可忽略。

<details markdown="1"><summary>点击显示答案</summary>

指数展开（$T_1, T_2$ 对易）：

$$e^{T_1}e^{T_2} = 1 + T_1 + \Big(T_2 + \tfrac12T_1^2\Big) + \Big(T_1T_2 + \tfrac16T_1^3\Big) + \Big(\tfrac12T_2^2 + \tfrac12T_1^2T_2 + \tfrac1{24}T_1^4\Big) + \cdots$$

对应到激发 rank：

$$c_1 = t_1,\qquad c_2 = t_2 + \tfrac12t_1^2,\qquad c_3 = t_1t_2 + \tfrac16t_1^3,\qquad c_4 \supset \tfrac12\,t_2t_2' + \tfrac12t_1^2t_2 + \tfrac1{24}t_1^4\ (\text{外加连接的 } t_4,\ \text{CCSD 中取零}).$$

**数量级对比**：典型 $\lvert t_2\rvert \sim 0.05$ 时，断开的四激发系数 $\tfrac12t_2t_2' \sim 1.3\times10^{-3}$；而真正的连接四激发 $\lvert t_4\rvert \sim 10^{-3}$ 上下——**同量级甚至更小**。结论：

- CCSD 丢弃的是 $t_4$（连接部分，~10^{-3}），保留 $\tfrac12t_2^2$（断开部分，~10^{-3}）——丢弃的是次要成分；
- CISD 丢弃的是**全部**四激发：断开 + 连接——把大头（断开乘积）也扔了，且由此产生大小不一致（自检问题 2）。

**物理翻译**：动态相关 = 海量"各自独立、互不相干"的电子对激发。它们对能量的贡献以乘积形式进入高阶微扰（每对独立地 $-v^2/\Delta$，两对独立就是乘出来），指数拟设恰好把这些乘积一网打尽。"连接簇"才需要显式的更高 rank——那是小得多的修正。**CC 的天才之处：用对的变量（簇振幅而非 CI 系数）让主要物理变成低阶项**。

</details>

**5.** 用第 14 章最小基 H₂ 的结果证明：解离极限处 MP2 发散到 $-\infty$，而 FCI 有限；给出 MP2 修正在键长上的定性曲线，并说明它对"微扰法何时可用"的启示。

<details markdown="1"><summary>点击显示答案</summary>

**设置**：参考态 $\Phi_0 = \lvert\sigma_g^2\rangle$（RHF），唯一的双激发是 $\lvert\sigma_u^2\rangle$，耦合即第 14 章算过的非对角元

$$\lvert\langle\Phi_{gg}^{uu}\lvert H\lvert\Phi_0\rangle\vert = \frac{J}{2}\ (\text{解离处}),$$

分母是轨道能隙的两倍：

$$2(\varepsilon_g - \varepsilon_u) = 2\Delta(R),\qquad \Delta(R) \to 0\ (R\to\infty),$$

因为成键/反键轨道都退化为氢原子 1s（劈裂来自交叠，随 $R$ 指数消失）。于是（此模型里 MP2 = 二阶微扰）

$$E_\text{MP2}(R) = -\frac{(J/2)^2}{2\Delta(R)}\;\xrightarrow{\;R\to\infty\;}\;-\infty.$$

**对照**：FCI 给出 $2E_\mathrm{H}$（严格、有限）；真实需要的"相关修正"是有限的 $J/2$。MP2 想用微扰级数修一个**本质非微扰**的问题——严格解里 $\lvert\sigma_u^2\rangle$ 的权重是 $\tfrac{1}{\sqrt2}$（O(1)！），而微扰论的前提是修正是小量。收敛半径为零：级数在 $\Delta \to 0$ 处遭遇奇点，二阶项先以 $1/\Delta$ 爆炸，更高阶以更高次幂爆炸（发散方向逐阶交替——渐近级数的典型行为）。

**定性曲线**：平衡键长处 $\Delta$ 大（~10 eV），MP2 修正 ~1 eV、贴住 FCI；键拉长，修正先增后爆，在 $\Delta \sim E_\text{corr}$ 附近越过 FCI 冲向 $-\infty$——能级"交叉"型错误。

**启示**：(i) 微扰法的适用判据是"耦合/能隙"小，不是"相互作用"弱——静态相关恰恰是耦合 $\sim$ 能隙；(ii) 诊断信号：HOMO–LUMO 能隙小、自然轨道占据数离开 0/1——出现即应换轨道（换参考、换 DFT、换强关联方法）；(iii) CC 的 $e^T$ 在此模型里能精确重排微扰级数（两态问题自检问题 2 同构），所以 CCSD 在解离处比 MP2 强得多——但真实多参考问题里它同样失效，只是"死得更晚"。**能隙是本章一切方法的氧气**。

</details>

## 参考

- Szabo & Ostlund《Modern Quantum Chemistry》第 4 章（HF 与 Brillouin 定理）、第 6 章（MP 微扰、CI 与大小一致性问题）。
- Shavitt & Bartlett《Many-Electron Methods in Chemistry and Physics》第 1、10 章：耦合簇的系统推导（含 BCH 终止与连接簇定理）。
- T. D. Crawford & H. F. Schaefer III, "An Introduction to Coupled Cluster Theory"（Rev. Comput. Chem. 14, 33 (2000)）：CC 的最佳短篇入门，含 CI/CC 系数关系的表格。
- Helgaker, Jørgensen & Olsen 第 14 章：CC 的完整现代处理。
- Bartlett & Musiał, Rev. Mod. Phys. 79, 291 (2007)：耦合簇五十年综述。
