# 嵌入方法：分而治之的电子结构

> 路线图位置：第四部分（多电子问题怎么算）· 第 21 章（收官）
> 前置知识：[第 16 章](16-dft.md)（KS 框架、自相互作用与强关联失灵）、[第 17 章](17-beyond-dft-gw-dmft.md)（DMFT 的杂质自洽回路）、[第 18 章](18-multireference-casscf.md)（高精度波函数方法的疆界）、[第 14 章](14-exact-methods-fci-ed.md)（Hubbard 模型）；第 7 章（Weiss 平均场——嵌入思想的曾祖母）。
> 学习目标：把 QM/MM、DFT+U、子系统 DFT、DMET 识别为**同一个模式**的不同实例——"把体系切成'必须精确的碎片'与'可以便宜的环境'，在边界上自洽耦合"；会推 DFT+U 的 Dudarev 修正并证明它惩罚分数占据（第 16 章分段线性/导数不连续的局域修复版）；理解 DMET 的 Schmidt 浴构造及其与 DMFT 的对照（静态投影 vs 动力学浴）；会算 QM/MM 的标度账；能解释双重计数——嵌入方法的通用命门——在各实例中的形态与对策。
>
> 记号约定：原子单位（沿第四部分）。

---

## 1. 一句话总结

**嵌入方法的共同赌注是：真实的计算需求在空间（或轨道空间）上极不均匀——酶的活性位要量子、其余几万原子只要经典；过渡金属的 d 壳要 Hubbard、其余价电子 DFT 就够——于是"高精度方法算碎片、低精度方法算环境、边界自洽缝合"的框架能同时拿到两边的精度与速度。谱系从粗到细：QM/MM（经典环境 + 静电缝合，分子模拟的百年工艺）、DFT+U（在 d/f 子空间手工叠加 Hubbard 排斥，惩罚分数占据——恰好是第 16 章导数不连续失灵的局域修复）、子系统 DFT（两个 KS 体系共享密度，非加和动能泛函缝合）、DMET（从低阶波函数的 Schmidt 分解里切出有限维"浴"，碎片+浴用高阶方法严格解、整体自洽——静态版的 DMFT）、WF-in-DFT（CC/CAS 算核心、DFT 算环境）。它们共享同一个命门——**双重计数**：环境方法已经算过一遍的那部分相互作用，高精度方法不能再算第二遍；缝合处的势、投影、浴的构造全是围绕这个命门的工程。作为第四部分的收官：嵌入是"在哪个变量上做近似"之后再添的一维——**在哪里（空间上）做近似**。**

## 2. 模式与谱系

先把抽象模式立起来（它是第 7 章 Weiss 平均场的当代扩展——把"平均场"换成"低阶环境"，把"自洽"保留）：

$$\text{嵌入} = \underbrace{\text{碎片（高阶方法，小）}}_{\text{DFT+U 的 } d\text{ 壳 / DMET 的 impurity / QM 区}}\ +\ \underbrace{\text{环境（低阶方法，大）}}_{\text{DFT 的其余 / 平均场浴 / MM 力场}}\ +\ \underbrace{\text{缝合（自洽}}_{\text{势匹配 / 密度匹配 / 化学势匹配}}\text{）}.$$

四条实例按"环境语言"排队：

| 方法 | 碎片 | 环境 | 缝合 | 典型问题 |
|---|---|---|---|---|
| QM/MM | 量子化学区（DFT/MP2） | 分子力学（点电荷 + 弹簧） | 静电嵌入 + 极化 | 酶催化、溶液反应 |
| DFT+U | d/f 子空间（+Hubbard $U$） | DFT 其余 | 占据数投影 | Mott 氧化物、LSDA+U |
| 子系统 DFT | 各分子片段（各自 KS） | 其余片段 | 非加和动能 $T_s^\text{nadd}$ | 弱作用分子聚集体 |
| DMET | 杂质 + Schmidt 浴（严格解） | 整体低阶波函数 | 一体密度矩阵匹配 | 强关联晶格、大活性空间 |
| WF-in-DFT | CC/CAS 核心 | DFT 环境 | 嵌入势 + 动能修正 | 溶液中高精度反应能 |

共同命门"双重计数"将在各节点名。

## 3. QM/MM：百年工艺

酶催化的问题：活性位几十个原子需要量子力学（断键成键），蛋白+水几万个原子只需要经典力学（构象与静电）。**QM/MM**（Warshel–Levitt 1976；2013 诺贝尔化学奖）的缝合有两档：

- **机械嵌入**：QM 区与 MM 区只通过弹簧连接（断键处的连接原子）——静电被完全忽略，粗糙；
- **静电嵌入**：MM 点电荷进入 QM 区的哈密顿量（$\hat H_\text{QM} = \hat H_0 + \sum_I q_I/\lvert\vec r - \vec R_I\rvert$），QM 区的极化如实响应——主流。反向（QM 区极化 MM 区）需要极化力场，是加价的选项。

命门形态：边界处的化学键切断需要"连接原子"（link atom）补价；QM 区太小会把电荷转移效应切掉。标度账：QM 区 100 原子 DFT $\sim N^3$、MM 区 $10^5$ 原子线性——**总体线性于体系大小，量子精度只付给需要它的百分之一**。这一模式的价值不在单项精度而在"问题本来长这样"。

## 4. DFT+U：给 d 壳手工加 Hubbard

第 16 章 6.3 节的车祸现场：LSDA/GGA 把 NiO 算成金属。**DFT+U** 的手术：在 d/f 子空间的投影占据 $n_{mm'}^\sigma = \langle\varphi_m^\sigma\lvert\hat n\lvert\varphi_{m'}^\sigma\rangle$ 上叠加一个 Hubbard 型惩罚（Dudarev 形式，推导见自检问题 1）：

$$E_{+U} = \frac{U}{2}\sum_\sigma\Big[\mathrm{Tr}\big(n^\sigma\big) - \mathrm{Tr}\big(n^\sigma n^\sigma\big)\Big]\ =\ \frac{U}{2}\sum_\sigma\mathrm{Tr}\big[n^\sigma(1 - n^\sigma)\big]\ \ge\ 0.$$

三条读法：(i) $n$ 的本征值取 0 或 1（整数占据、$n$ 幂等）时修正为零——**惩罚的只是分数占据**；(ii) 分数占据正是第 16 章自检问题 4 里"分段线性被抹平"的表征——**DFT+U 是在局域子空间内手工恢复导数不连续**，把 $E(N)$ 被近似泛函压弯的凸性重新掰平（掰过头就是著名的 DFT+U 把体系推向电荷有序/局域化的偏置）；(iii) 修正的势 $v = U(\tfrac12 - n)$ 把占据轨道压低、空轨道抬高，能隙被砸开 $\sim U - W$（对照第 17 章 Hubbard-I 的 $\sqrt{U^2 + W^2} - W$）——NiO 的隙出来了。

命门形态（双重计数的教科书案例）：$U$ 里有一部分库仑已经被 DFT 的交换相关算过一遍——参数要么从头算（cRPA：约束 RPA 把 $W$ 里的 d–d 屏蔽扣掉再取低频极限），要么经验拟合；双重计数扣除干净与否直接决定结果可信度。**DFT+U 处在第一性原理与唯象之间**：形式粗糙（各向同性 $U$、静态、投影依赖），但便宜（KS 成本不变）且专治 d/f——工业界的主力工具。

## 5. 子系统 DFT 与 WF-in-DFT

**子系统 DFT**（frozen-density embedding）：把大体系密度分解 $n = \sum_A n_A$，每个片段在自己的嵌入势里做 KS：

$$v_\text{emb}^{A} = v_\text{ext} + v_H[n - n_A] + \frac{\delta E_{xc}[n]}{\delta n} - \frac{\delta E_{xc}[n_A]}{\delta n_A}\bigg\lvert_{n_A},$$

多出来的项是**非加和动能** $T_s^\text{nadd}[n_A, n_B] = T_s[n_A + n_B] - T_s[n_A] - T_s[n_B]$（自检问题 4 证明它在密度不交叠时严格为零、交叠时无好泛函）——命门所在。适用带：弱交叠的分子聚集体、溶液化的分层描述；共价断键处失效。

**WF-in-DFT**：同一思想的精度升级——碎片用 CCSD(T)/CASSCF（第 15、18 章），环境用 DFT，缝合势由冻结密度构造，动能修正与 DFT+U 一样是双重计数的角斗场。卖点是"溶液中的化学精度"：气相 CC 的精度带着溶剂的统计平均。这是嵌入谱系的"分子端旗手"，与固体端的 DMFT-in-DFT 遥相呼应。

## 6. DMET：Schmidt 浴与密度匹配

**密度矩阵嵌入理论**（Knizia–Chan 2012）的构造干净得像教学题：

1. **整体低阶解**：对整个晶格解一个便宜的哈密顿 $H_\text{low}$（如 $U = 0$ 的平均场），得基态 $|\Psi_\text{low}\rangle$；
2. **切碎片**：选定杂质（若干格点），对 $|\Psi_\text{low}\rangle$ 做跨切口的 Schmidt 分解——**环境只通过至多 $d$ 条 Schmidt 浴轨道与碎片纠缠**（自由 Slater 态的约化密度矩阵秩有限，见自检问题 2）；
3. **高阶解杂质**：碎片 + 浴构成小体系（如单格点 Hubbard 碎片 → 二格点杂质模型），用**严格方法**解（ED——第 14 章的机器、或 DMRG——第 20 章）；
4. **自洽**：调整 $H_\text{low}$ 的参数（化学势、跃迁），使杂质上的一体密度矩阵与嵌入波函数的匹配——整体物理量（能量、占据、自旋）从匹配后的关联密度矩阵读出。

**与 DMFT 的对照**（第 17 章 5 节，自检问题 5 展开）：DMET 的浴是**静态的**（一个基态的 Schmidt 投影，有限维）——抓基态性质、零温度、无符号问题（浴小到可以严格解）；DMFT 的浴是**动力学的**（Weiss 函数 $\mathcal G_0(\omega)$，连续谱）——抓谱函数、有限温度、要 QMC。一句话：**DMET 换掉了 DMFT 的谱，换来强关联基态的便宜与稳健**。

成绩单：一维/二维 Hubbard 全参数域基态能量误差 ~1%（对照 Lieb–Wu 精确解）；量子化学版的分子碎片化（把 CCSD(T) 精度推到大分子）同根同源。命门形态：碎片大小的收敛（关联长程时要拼大碎片）、几何嵌入（多碎片的一致性）、以及与一切嵌入共享的"环境近似传递性"假设。

## 7. 第四部分收官：方法地图的最终版

四篇正文 + 两篇补充写完，把地图钉上最后一颗图钉：

| | 变分对象 | 精度 | 代价 | 疆界 |
|---|---|---|---|---|
| FCI/ED | 全波函数 | 严格 | 指数 | 小体系 |
| HF/MP2/CC | 波函数（截断/指数化） | 黄金标准（单参考） | $N^{4}$–$N^7$ | 静态相关、固体 |
| DFT | 密度 | 泛函而定 | $N^3$ | 能隙、SIE、强关联 |
| GW/BSE | 格林函数 | 能谱好手 | $N^4$ | 顶角、强关联 |
| DMFT | 局域自能 | Mott 物理好手 | 多项式 | 非局域关联 |
| CASSCF/CASPT2 | 活性空间 | 多参考可靠 | 活性指数 | 活性大小 |
| DMRG | 低纠缠 MPS | 一维准严格 | $d^3\chi^3$ | 纠缠标度 |
| 嵌入 | 碎片高阶 + 环境低阶 | 两全 | 近线性 | 缝合/双重计数 |

三条贯穿线（本部分的方法论遗产）：**在哪个变量上近似**（波函数/密度/格林函数/纠缠几何）；**以何种哲学近似**（微扰截断要小参数、变分猜形式要运气、映射猜结构要检验）；**在哪里近似**（全体系/活性空间/空间碎片）。以及一条底线：**指数墙永远在场**——每种成功都是在墙下找到了自己的采光面。没有万能方法，只有对症的手术刀；而选刀的依据，是物理（能隙、纠缠、局域性），不是时尚。

## 小结

- 嵌入 = 碎片高阶 + 环境低阶 + 自洽缝合；四档实例共享此模式，各自承压于同一个命门：双重计数。
- DFT+U：Dudarev 修正惩罚分数占据 = 局域版导数不连续修复；$U$ 的双重计数扣除（cRPA）是可信度关键。
- DMET：Schmidt 浴静态投影 + 严格杂质解 + 密度匹配；与 DMFT 互为"基态/谱函数"镜像。
- QM/MM 的标度账使"量子精度只付百分之一体积"成为可能；WF-in-DFT 把它推到化学精度。
- 第四部分三问收官：哪个变量、何种哲学、哪块空间——指数墙下，每把刀都只在它的采光面里锋利。

## 自检问题

**1.** 推导 Dudarev 形式的 DFT+U 修正 $E_{+U} = \tfrac{U}{2}\sum_\sigma\mathrm{Tr}\big[n^\sigma(1-n^\sigma)\big]$，证明本征占据数为 0 或 1 时修正为零、分数占据被惩罚；并证明修正产生的势 $v = U(\tfrac12 - n)$ 把占据能级压低、空能级抬高——等价于在子空间内手工劈出一个能隙并恢复分段线性。

<details markdown="1"><summary>点击显示答案</summary>

**来源**：把 Hubbard 排斥对子空间占据做旋转不变（对各轨道取向平均）的处理，并对 DFT 已计入的平均相互作用（双重计数）做扣除后，剩余部分收敛为（Dudarev 1998 的简化形）：

$$E_{+U} = \frac{U}{2}\sum_\sigma\mathrm{Tr}\big[n^\sigma(1 - n^\sigma)\big].$$

**整数占据**：$n^\sigma$ 幂等（投影算符，$n^2 = n$）⇒ $\mathrm{Tr}\,n^2 = \mathrm{Tr}\,n$ ⇒ $E_{+U} = 0$。**分数占据**：本征值 $\nu\in(0,1)$ 上 $E_U(\nu) = \tfrac{U}{2}\nu(1-\nu) \in (0, U/8]$——**正的惩罚，$\nu = 1/2$ 处最重**。

**能级移动**：修正对占据数的导数即附加势：

$$v^\sigma = \frac{\partial E_{+U}}{\partial n^\sigma} = U\Big(\frac12 - n^\sigma\Big)\quad\Rightarrow\quad \varepsilon_\nu \to \varepsilon_\nu + U\Big(\frac12 - \nu\Big).$$

占据轨道（$\nu\to1$）压低 $-U/2$、空轨道（$\nu\to0$）抬高 $+U/2$——**子空间内隙被手工撑开 $\sim U$**（与带宽抵消后 $\sim U - W$，对照第 17 章 Hubbard-I 的 $\sqrt{U^2 + W^2} - W$ 大 $U$ 极限）。

**分段线性的恢复**：$E_U$ 对 $\nu$ 的二阶导为 $-U < 0$——**凹**修正；而近似 DFT 的 $E(N)$ 沿分数占据被压成**凸**（分数态低于弦、过度离域，第 16 章自检问题 4）。凹修正恰好把凸病掰直：$U$ 调准时子空间内的 $E(N)$ 回到分段线性、导数跳变（导数不连续性）被手工安放回来。**这就是"DFT+U = 局域化的导数不连续修复器"的确切含义**；$U$ 过大则矫枉过正——把本该部分离域的 d 带推向整数占据与电荷有序，即 DFT+U 已知的局域化偏置。

</details>

**2.** DMET 的浴构造：证明非相互作用 Slater 态在"单格点 vs 其余"的二分下，环境一侧至多携带 $d_\text{frag}$ 条 Schmidt 浴轨道；对半满一维 Hubbard 的 $U = 0$ 极限写出杂质模型（碎片 = 1 个 Hubbard 格点）并识别它就是第 13 章的两格点模型。

<details markdown="1"><summary>点击显示答案</summary>

**秩定理**：Slater 态是格点轨道的反对称积；单格点的约化密度矩阵 $\rho_\text{frag} = \mathrm{Tr}_\text{env}\lvert\Psi\rangle\langle\Psi\lvert$ 由碎片上的一体密度矩阵 $P = \langle c^\dagger c\rangle_\text{frag}$ 完全决定（Slater 的 Wick 性质），其秩 $\le$ 碎片的单粒子维数 $d_\text{sp}$（自旋分开时每自旋 1）。Schmidt 分解的秩 = $\rho_\text{frag}$ 的秩 ⇒ 环境只需 $d_\text{sp}$（自旋计）条浴轨道即可精确复制纠缠：

$$\lvert\Psi_\text{low}\rangle = \sum_{\alpha}^{d_\text{sp}} \lambda_\alpha\,\lvert\alpha\rangle_\text{frag}\lvert\alpha\rangle_\text{bath},\qquad \dim(\text{frag}\otimes\text{bath}) = d_\text{frag}\cdot 2^{d_\text{sp}}.$$

**Hubbard 实例**：半满、$U=0$ 的链，碎片 = 格点 A（自旋两通道各一条浴轨道 $b_\uparrow, b_\downarrow$）。杂质哈密顿：

$$H_\text{imp} = U\,n_{A\uparrow}n_{A\downarrow} + \sum_\sigma\Big[\varepsilon_A n_{A\sigma} + \varepsilon_b n_{b\sigma} + t'\big(c^\dagger_{A\sigma}c_{b\sigma} + \text{h.c.}\big)\Big] + (\text{浴内项})，$$

其中 $\varepsilon_{A,b}, t'$ 由 Schmidt 系数（即平均场占据）决定，自洽时再调整——**正是第 13 章 5 节的两格点 Hubbard 模型**（相互作用只开在碎片上）。严格解（4 维活性空间的 FCI，第 14 章的手艺）给出关联的一体密度矩阵；能量按 $E = \mathrm{Tr}[(h + \Sigma_\text{corr})\gamma]/2$ 型匹配式读出。**物理**：DMET 假设"强关联最激烈处（杂质）之外的环境可以用平均场描述其纠缠结构"——与 DMFT 的"自能局域"假设同族，但静态化。

</details>

**3.** QM/MM 的标度账：设酶–底物复合物 $3\times10^4$ 原子，QM 区 60 原子（DFT，$N^3$）+ MM 区（线性）。估算纯 QM（DFT）与 QM/MM 的成本比；再估算把 QM 区从 DFT 换成 DLPNO-CCSD(T)（近线性标度）时总成本的结构变化。

<details markdown="1"><summary>点击显示答案</summary>

**账**：DFT 标度 $N^3$（平面波/杂化各有常数）：纯 QM（$3\times10^4$ 原子）对 QM/MM 的 QM 区（60 原子）：

$$\frac{N_\text{tot}^3}{N_\text{QM}^3} = \left(\frac{3\times10^4}{60}\right)^3 = 500^3 = 1.25\times10^8.$$

量子部分便宜一亿倍；MM 区（$3\times10^4$ 原子、线性、每步 $\mu$s–ms）成为新瓶颈——**总成本由环境的经典力学决定**，而量子精度集中在 0.2% 的原子上。

**换 CCSD(T) 内核**：DLPNO-近线性 CCSD(T) 对 60 原子 $\sim$ 分钟–小时级/单点——比 60 原子的 DFT 贵得多但仍远小于"全体系任何量子方法"的成本；总成本结构变成"量子单点 × 统计采样步数"的乘积。**嵌入的经济学**：不是让量子变便宜，而是让量子**只算该算的**——采样（构象、时间演化）交给环境，电子结构交给碎片。WF-in-DFT（第 5 节）正是这条经济学的化学精度版。

</details>

**4.** 子系统 DFT 的非加和动能 $T_s^\text{nadd}[n_A, n_B]$：证明密度不交叠时严格为零；在交叠区用近似的 von Weizsäcker 泛函估计其量级；说明为什么共价成键区是该方法的雷区。

<details markdown="1"><summary>点击显示答案</summary>

**不交叠为零**：$n_A$ 与 $n_B$ 支集分离时，$n = n_A + n_B$ 的非相互作用基态就是两个孤立 KS 基态的空间拼接（动能算符局域），$T_s[n] = T_s[n_A] + T_s[n_B]$ ⇒ $T_s^\text{nadd} = 0$。此时嵌入势退化为静电 + $v_{xc}$ 的线性叠加——子系统 DFT 严格退化为"各自 KS + 库仑缝合"。

**交叠区**：精确的 $T_s^\text{nadd}$ 无已知好泛函（它包含碎片间交换的全部难度）。下界式近似是 von Weizsäcker 动能 $T_\text{vW}[n] = \tfrac18\int\lvert\nabla n\rvert^2/n$（对单电子严格）：

$$T_s^\text{nadd} \approx T_\text{vW}[n_A + n_B] - T_\text{vW}[n_A] - T_\text{vW}[n_B] \sim \int\frac{\lvert\nabla n_A\cdot\text{交叠}\rvert\ \cdots}{},$$

量级 $\sim$ 交叠区密度 × 动能密度——弱交叠（氢键、范德华接触）时 mHa 级（可控），强交叠（共价键区密度重组）时 Hartree 级（灾难）。**雷区机理**：共价键的能量恰恰藏在两片段密度的量子干涉里——$T_s^\text{nadd}$ 承担的正是这部分，而它没有可靠的近似。谱系定位：子系统 DFT = 嵌入中"缝合最薄"的一档，适合弱作用分层（第 16 章色散失灵的对策之一也在此家族：片段化 + 色散修正）。

</details>

**5.** DMET 与 DMFT 的正面对照：证明 (a) DMET 的浴维数有限（$\le$ 碎片单粒子维数）而 DMFT 的浴谱连续；(b) 两者在杂质与整体的"缝合变量"分别是静态（一体密度矩阵）与动力学（Weiss 函数）；(c) 由此解释 DMET 无符号问题、DMFT 有——以及各自牺牲了什么。

<details markdown="1"><summary>点击显示答案</summary>

**(a)**：DMET 浴 = 平均场基态的 Schmidt 投影（自检问题 2），维数 $d_\text{sp}$（碎片单粒子维数）封顶——**有限维希尔伯特空间**。DMFT 的浴由 Weiss 函数 $\mathcal G_0(\omega)$ 描述，其谱函数在整个频轴上连续（晶格态密度的连续谱注入杂质）——**无穷多自由度**，等价的哈密顿形式（Anderson 杂质模型）需要无穷浴能级。

**(b)**：DMET 的自洽变量是**一体密度矩阵**在杂质–浴–环境间的一致（静态、零温、基态性质）；DMFT 的是**格林函数**层级（$G_\text{loc}^{-1} + \Sigma = \mathcal G_0^{-1}$，全频轴）——动力学信息（谱、寿命、温度）只有在 DMFT 一侧存在。

**(c)**：DMET 的杂质–浴体系小到可以用 ED/DMRG **严格**解（第 14、20 章的机器）——费米子符号问题需要"对指数大的组态空间抽样"才成其为问题，而这里根本没有抽样，直接对角化；**代价：谱函数原则上不可得**（静态投影丢掉了频率轴——浴是单个基态的纠缠快照）。DMFT 要解连续谱的杂质问题，通用武器是 QMC（虚时间轴），于是继承符号问题（掺杂、阻挫时指数恶化）；**代价之外换来：完整的 $\Sigma(\omega)$、有限温、与 GW 组装（第 17 章）的接口**。总结成一张对表：**静态小浴（DMET）= 基态能量与占据的便宜严格；动力学大浴（DMFT）= 谱与相变的全面但昂贵**——嵌入家族内部的"变分流形 vs 表达能力"取舍，与波函数方法内部"CC vs FCI"的取舍同构。

</details>

## 参考

- A. Warshel & M. Levitt, J. Mol. Biol. 103, 227 (1976)：QM/MM 的起点；Lin & Truhlar, Annu. Rev. Phys. Chem. 64, 101 (2013)：现代综述。
- V. I. Anisimov, J. Zaanen & O. K. Andersen, Phys. Rev. B 44, 943 (1991)；S. L. Dudarev et al., Phys. Rev. B 57, 1505 (1998)：DFT+U 的奠基与标准形式。
- T. A. Wesolowski & A. Warshel, J. Phys. Chem. 97, 8050 (1993)：冻结密度嵌入；C. R. Jacob & J. Neugebauer, WIREs Comput. Mol. Sci. 4, 325 (2014)：子系统 DFT 综述。
- G. Knizia & G. K.-L. Chan, Phys. Rev. Lett. 109, 186404 (2012)：DMET 原始文献；Sun, Chan 等 JCTC 系列与 Q. Sun & G. K.-L. Chan, Acc. Chem. Res. 49, 2705 (2016)：化学版 DMET。
- F. R. Manby 等 J. Chem. Theory Comput. 8, 2564 (2012)：WF-in-DFT 嵌入；cRPA 定 $U$：F. Aryasetiawan et al., Phys. Rev. B 70, 195104 (2004)。
