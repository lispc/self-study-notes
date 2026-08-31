# 超越 DFT：准粒子 GW 与动力学平均场 DMFT

> 路线图位置：第四部分（多电子问题怎么算）· 第 17 章
> 前置知识：[第 16 章](16-dft.md)（KS 框架与它的失灵清单——本章的出发点）；第 6 章[相互作用电子气](06-interacting-electron-gas.md)（屏蔽与介电函数、RPA、Fermi 液体与准粒子）；第 13 章[强关联浅尝](13-strong-correlations.md)（Hubbard 模型、原子极限、Hubbard 带、Mott 物理）；[QFT 书一圈重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)（Dyson 方程、自能与真空极化——本章的图语言直接来自那里）。
> 学习目标：理解为什么激发态谱必须用格林函数的语言（谱函数 = 光电发射实验的直接预言）；会从 Dyson 方程读出"自能 = 一切相互作用修正"，并推出 GW 近似的逻辑（用第 6 章的屏蔽 $W$ 做一阶自能）；理解 DMFT 的映射（晶格 → 自洽杂质）与原子极限下 $\Sigma(\omega) = U^2/4\omega$ 的 Hubbard 带劈裂；把 FCI → HF → MP2/CC → DFT → GW/DMFT 串成一张"在哪里做近似"的完整地图。
>
> 记号约定：原子单位（同第 14 章）。频率为实轴或 Matsubara 视上下文注明；$\mu$ 为化学势，半满 Hubbard 模型取 $\mu = U/2$（粒子–空穴对称点）。

---

## 1. 一句话总结

**DFT 的失灵清单（能隙偏小、强关联判金属）有一个共同根源：KS 本征值本来就不是激发能——要激发谱就得换货币，从基态密度换成单粒子格林函数 $G$，那里谱函数的极点就是准粒子能量，而相互作用的一切修正收拢成一个自能 $\Sigma$。GW 近似把 $\Sigma$ 取到屏蔽相互作用的最低阶（$\Sigma = iGW$，$W$ 正是第 6 章 RPA 介电函数屏蔽过的库仑）——一步就修好 Si 的能隙（0.5 → 1.25 eV，实验 1.17），是"QFT 费曼图直接上岗干活"的范本。DMFT 走另一头：承认强关联时自能非微扰，但假设它主要是局域的（$\Sigma(\vec k,\omega)\to\Sigma(\omega)$），把晶格问题自洽地映射成一个杂质模型严格求解——原子极限下 $\Sigma = U^2/4\omega$ 精确劈出间隔为 $U$ 的上下 Hubbard 带，晶格上再生长出费米液体准粒子峰，第 13 章的 Mott 物理由此成为可计算的谱。GW 从弱关联端、DMFT 从强关联端修补 DFT；与前面的 HF/MP2/CC/DFT 合起来，方法地图的经纬是同一个问题——你愿意在哪个变量（波函数、密度、格林函数）上、以什么代价做近似。**

## 2. 谱与准粒子：实验看到的是什么

角分辨光电发射（ARPES）问的是：拿走一个能量 $\omega$、动量 $\vec k$ 的电子的概率——这正是**谱函数** $A(\vec k,\omega) = -\tfrac1\pi\mathrm{Im}\,G(\vec k,\omega)$（$G$ 为单粒子格林函数）。Fermi 液体（第 6 章 7 节）保证相互作用体系在费米面附近仍有形状良好的准粒子极点：

$$G(\vec k,\omega) \approx \frac{Z_{\vec k}}{\omega - \varepsilon^\ast_{\vec k} + i\,\mathrm{sgn}(\omega)\lvert\Gamma_{\vec k}\rvert} + (\text{非相干背景}),$$

准粒子能量 $\varepsilon^\ast$（重整化 $Z$ 缩水）、寿命 $\Gamma \sim (\omega - \mu)^2$（第 6 章的衰变率计算）。**KS 本征值不在故事里**：它是替身体系的拉格朗日乘子（第 16 章）。LDA 能带常与实验接近，靠的是误差相消——DFT 低估的能隙与忽略的动力学屏蔽大体互相抵消；GW 把这笔糊涂账分开算清。

## 3. 格林函数与 Dyson 方程

单粒子格林函数 $G(1,2) = -i\langle\Psi_0\lvert T\big[\hat\psi(1)\hat\psi^\dagger(2)\big]\lvert\Psi_0\rangle$（$1 = (\vec r_1, t_1, \sigma_1)$）——与 QFT 书的传播子同一对象，只是"真空"换成了基态、相对论场换成了电子算符。核心方程是 **Dyson 方程**：

$$G^{-1} = G_0^{-1} - \Sigma \qquad\Longleftrightarrow\qquad G = G_0 + G_0\Sigma G_0 + G_0\Sigma G_0\Sigma G_0 + \cdots,$$

几何级数的求和——图语言：自由传播 + 一次自能插入 + 两次 + ……全部串起来（推导见自检问题 1；同一结构在 [QFT 书重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)里重整化传播子）。自能 $\Sigma$ 的含义：**相互作用对传播的全部修正**——HF 交换是它的静态非局域最低阶（$\Sigma \to \Sigma_x$，裸相互作用 $v$ 的一阶），库仑屏蔽、等离子激元激发、粒子碰撞寿命全是它的高阶内容。KS-DFT 干的事可以粗译成"把 $\Sigma$ 的交换关联部分硬塞进一个局域静态势 $v_{xc}$"——便宜，但激发谱（$\Sigma$ 的频率依赖、动量依赖、复数部分）全丢。超越 DFT = 把 $\Sigma$ 当正经对象算。

## 4. GW：用屏蔽库仑做自能

### 4.1 逻辑：Hedin 阶梯的第一级

精确自能没有闭式，但 Hedin（1965）给了一个原则上精确的自洽方程组，其中自能写成

$$\Sigma(1,2) = i\,G(1,2)\,W(1,2)\,\Gamma(1,2),$$

$W$ 是**屏蔽**库仑（第 6 章 4–6 节的主角），$\Gamma$ 是顶角修正。**GW 近似 = 取 $\Gamma \to 1$**（丢顶角）：自能 = 一个传播子乘一个屏蔽相互作用，频率依赖、动量依赖全保留。两个极限自检（见自检问题 2）：

- $W \to v$（不屏蔽）：$\Sigma \to$ Fock 交换——HF 是 GW 的裸库仑极限；
- $W \to$ 静态屏蔽：屏蔽交换（screened HF）——**屏蔽正是 HF 高估能隙的解药**（第 16 章对照表末行）。

物理直觉：拿走/放回一个电子时，周围的电子云已经替你把库仑穴铺好——感受到的不是裸电荷而是屏蔽电荷（第 6 章 Thomas–Fermi 的 $k_{TF}$、RPA 的 $\varepsilon(q,\omega)$）。用 $W$ 而不是 $v$ 做自能，就是把"别人的电子让开的效应"计入代价。

### 4.2 实践与成绩单

标准流程 $G_0W_0$：拿 DFT 的 KS 本征值/波函数当 $G_0$ 的输入，$W$ 用 RPA（介电函数 $\varepsilon = 1 - vP_0$，第 6 章 6 节原封搬来）算，解 Dyson 方程一次性（或自洽迭代）得准粒子能级。成绩单的招牌行：

| | LDA | $G_0W_0$ | 实验 |
|---|---|---|---|
| Si 能隙 | ~0.5 eV | ~1.25 eV | 1.17 eV |
| Ge 能隙 | ~0（金属） | ~0.75 eV | 0.74 eV（半导体） |

半导体/绝缘体能隙、分子电离能、激发谱普遍修到实验附近的百分之几。代价 $N^4$（介电函数的本征分解是大头），介于 DFT 与 CC 之间。**未解的问题**：顶角修正（$\Gamma\ne1$）与自洽程度对结果的影响体系依赖，GW 不是万能终点——但作为"第一性原理能隙"的默认选项，它统治半导体电子结构三十年。

### 4.3 与本书主线的对位

GW 是全书"场论思想的应用现场"最直白的一例：QFT 书里为重整化发展的 Dyson 方程、真空极化、屏蔽电荷，在这里以半导体能隙的形式落地。第 6 章算过的 $W$、第 16 章抱怨过的能隙、QFT 书的传播子——三条线在此汇合。

## 5. DMFT：把晶格折叠成一个杂质

### 5.1 动机：强关联的自能非微扰，但也许很局域

强关联（第 13 章）的病理：$U$ 与带宽同量级，微扰级数没有小参数；Mott 能隙来自 $\Sigma$ 的剧烈行为（原子极限下 $\Sigma = U^2/4\omega$ 在 $\omega = 0$ 处奇异——见 5.2）。出路不是更好的微扰，而是换近似方向：**动力学平均场理论（DMFT）假设自能主要是局域的**，

$$\Sigma(\vec k, \omega)\ \approx\ \Sigma(\omega)\qquad(\text{与 }\vec k\text{ 无关}).$$

这个假设在**无穷维/无穷配位数极限下严格成立**（Metzner–Vollhardt 1989：自能的非局域部分按 $1/z$ 修正，$z$ 为配位数），三维 lattice 上意外地好。直觉与第 7 章 Weiss 平均场同构：配位数越大，单个键的信息越不重要，自能越像"泡在一锅平均介质里"——只是这里的平均场是**动力学**的（频率依赖的 bathing Green 函数），它保留了全部局域时间涨落——量子涨落不被平均掉。

### 5.2 原子极限：Hubbard-I 自能

DMFT 的体检标本是 $t = 0$（孤立原子，第 13 章 4.2 节）。杂质格林函数由 $E(N) = \{0, -\mu, U - 2\mu\}$ 三个 $N = 0,1,2$ 态给出（自洽方程退化为平凡），谱函数两个极点（推导见自检问题 4）：

$$G(\omega) = \frac{\omega}{\omega^2 - U^2/4} \qquad\Longrightarrow\qquad \Sigma(\omega) = \frac{U^2}{4\omega}\qquad(\mu = U/2),$$

两个 Hubbard 带，权重各 ½，中心 $\pm U/2$，间隔 $U$——第 13 章 4.3 节的 Hubbard 带在此获得谱函数的定量形式。$\Sigma$ 在 $\omega\to0$ 处奇异：**任何围绕有限自能的展开（HF、微扰、KS）在此地原理上失效**——这就是 DFT 判 NiO 为金属而实验是绝缘体的病理解剖。

### 5.3 晶格 DMFT：自洽循环与三峰谱

有限 $t$ 时，DMFT 把晶格问题折叠成一个**安德森杂质模型**（一个相互作用格点 + 自洽决定的非相互作用浴）并自洽：

1. 猜 $\Sigma(\omega)$ → 求晶格局域格林函数 $G_\text{loc} = \sum_{\vec k}\big[\omega + \mu - \varepsilon_{\vec k} - \Sigma\big]^{-1}$；
2. 反解出浴格林函数 $G_0^{-1} = G_\text{loc}^{-1} + \Sigma$（Weiss 函数——第 7 章 Weiss 场的格林函数后代）；
3. 用严格解法解杂质模型（ED：就是第 14 章的对角化；或连续时间 QMC）得新的 $\Sigma$ → 循环。

收敛后的谱函数随 $U/W$ 演出 Mott 转变的完整戏码：金属相是**三峰结构**——费米面上的准粒子峰（Fermi 液体残余，宽度 $\sim ZW$）骑在上下 Hubbard 带之间；$U$ 增大，$Z \to 0$、准粒子峰坍缩，谱裂成两带留出 Mott 隙。与第 6 章（准粒子）和第 13 章（Mott）的接口在此闭环：**DMFT = 第 6 章的准粒子语言 + 第 13 章的 Hubbard 物理，装进一个可解的自洽回路**。

### 5.4 实践：DFT+DMFT

真实材料的工作流：DFT 给能带 $\varepsilon_{\vec k}$（弱相关的骨架）→ 投影出 d/f 子空间的窄带 Hubbard 问题 → DMFT 解出 $\Sigma(\omega)$ → 谱函数/输运/光学。成绩单：NiO 的能隙与磁矩、Ce 的 $\alpha$–$\gamma$ 相变（f 电子局域–离域）、V₂O₃ 的 Mott 转变、铁镍的磁性交换能——第 13 章"能带论失败名单"逐项回收。代价：杂质求解器（QMC）+ 每个 $\vec k$ 点求和，贵但多项式；边界：非局域关联（短程反铁磁涨落、维度低的体系）要 cluster 扩展，那是更远的方法学前沿。

## 6. 方法地图收束：本部分的总结算

四步走完，把整架梯子画全（$N$ 计体系规模）：

| 方法 | 在哪做近似 | 代价 | 强项 | 死穴 |
|---|---|---|---|---|
| FCI/ED | 只在基组 | 指数 | 严格标尺 | 指数墙 |
| HF | 单行列式 | $N^4$ | 交换精确、变分 | 零关联、能隙高估 |
| MP2 | 二阶微扰 | $N^5$ | 便宜的动态相关 | 静态相关发散 |
| CCSD(T) | 指数截断 $T_2$($+T_3$) | $N^7$ | 单参考黄金标准 | 多参考、固体 |
| DFT | 泛函形式 | $N^3$ | 固体日常、几何 | 能隙、SIE、强关联 |
| GW | 自能取 $iGW$ | $N^4$ | 能隙/激发谱 | 顶角、强关联 |
| DMFT | $\Sigma$ 局域化 | 多项式+求解器 | Mott、f 电子 | 非局域关联 |

三条读法：(i) **变近似的位置**——波函数（FCI→CC）、密度（DFT）、格林函数（GW/DMFT），三种货币各有汇率；(ii) **变近似的哲学**——微扰截断（MP2、GW）可系统改进但需要小参数，变分猜形式（DFT）与映射猜结构（DMFT）无小参数但能碰强关联；(iii) **指数墙永远在场**——每种方法都是在墙下选择哪一块砖不去搬。至于更远的岛——多参考（[第 18 章](18-multireference-casscf.md)）、激发态（[第 19 章](19-excited-states.md)）、张量网络（[第 20 章](20-dmrg-tensor-networks.md)）、嵌入方法（[第 21 章](21-embedding-methods.md)）——它们各自是这张地图上某处的放大镜。

## 小结

- 激发谱的正确货币是 $G$ 与谱函数 $A = -\pi^{-1}\mathrm{Im}G$；自能 $\Sigma$（Dyson 方程）收纳相互作用的一切修正，KS 本征值不是它的合法替身。
- GW = $\Gamma\to1$ 的 Hedin 一级：$\Sigma = iGW$，$W$ 直接来自第 6 章 RPA；HF 是其裸库仑极限、屏蔽是其灵魂；Si 能隙 0.5 → 1.25 eV 的招牌修复。
- DMFT = "$\Sigma$ 局域"的严格映射 + 杂质自洽；原子极限 $\Sigma = U^2/4\omega$ 劈出 Hubbard 带、解释 KS 方法的 Mott 车祸；晶格上长出三峰结构与 Mott 转变。
- DFT+DMFT 把第 13 章的失败名单逐项回收；GW 从弱关联端、DMFT 从强关联端包抄。
- 方法选择的统一坐标系：在哪个变量上、以何种哲学、付多大代价做近似——没有免费的午餐，只有对口的工具。

## 自检问题

**1.** 从 $G = G_0 + G_0VG$ 型迭代（或微扰级数重排）推导 Dyson 方程 $G^{-1} = G_0^{-1} - \Sigma$，并说明 $\Sigma$ 的静态极限如何回到 HF。

<details markdown="1"><summary>点击显示答案</summary>

**推导**（几何级数）：自由传播子 $G_0$ 上插入一次相互作用修正记为 $\Sigma$ 的卷积——严格说，把一切"单粒子不可约"的修正块定义为 $\Sigma$（砍断一条内部传播线后断成两截的图不算），则 $G$ 满足

$$G = G_0 + G_0\Sigma G_0 + G_0\Sigma G_0\Sigma G_0 + \cdots = G_0 + G_0\Sigma G.$$

最后一步是递归自嵌套（级数的尾部又是 $G$ 本身）。两边左乘 $G_0^{-1}$、整理：

$$G_0^{-1}G = 1 + \Sigma G\;\Longrightarrow\;\big(G_0^{-1} - \Sigma\big)G = 1\;\Longrightarrow\;G^{-1} = G_0^{-1} - \Sigma.$$

**读法**：$\Sigma$ 是"插入块"的自能——不可约性保证级数不重复计数；Dyson 方程把无穷级数压缩成一个求逆。

**HF 极限**：$\Sigma$ 的最低阶（一阶、静态、非局域）是 Fock 交换 $\Sigma_x(\vec r,\vec r') = -v(\lvert\vec r - \vec r'\rvert)\rho(\vec r,\vec r')$（$\rho$ 为密度矩阵）。取 $\Sigma \to \Sigma_x$，Dyson 方程正是 HF 轨道方程的格林函数版本；能量上讲，$G_0\Sigma_xG_0$ 给出 HF 交换能（第 6 章）。**更高阶的一切（屏蔽、动力学、虚部）都是超越 HF 的自能内容**——GW 只是这些内容的第一个系统化候选。

</details>

**2.** 证明 GW 的两个极限：(a) $W \to v$（裸库仑）时 $\Sigma \to \mathrm{i}Gv$ = Fock 交换；(b) $W$ 取静态屏蔽时得屏蔽交换近似。用 HF 高估能隙的事实解释"屏蔽"修正的方向为什么对。

<details markdown="1"><summary>点击显示答案</summary>

**(a)**：$\Sigma(1,2) = iG(1,2)W(1,2)$ 中令 $W \to v(\lvert\vec r_1 - \vec r_2\rvert)\delta(t_1 - t_2^+)$：

$$\Sigma \to i\,G(\vec r_1,\vec r_2; t_1 - t_2^+)\,v(r_{12})\delta(t_1 - t_2) \;\propto\; -v(r_{12})\,\rho(\vec r_1,\vec r_2)\quad(\text{静态，与 }\omega\text{ 无关}),$$

（$iG$ 在等时极限给出密度矩阵，符号规则吃掉 $i$）——正是 Fock 交换算符。HF 是 GW 的"零级屏蔽"极限。

**(b)**：$W(\vec q) = v(\vec q)/\varepsilon(\vec q) = v/(1 + k_{TF}^2/q^2)$（静态、长波，第 6 章 Thomas–Fermi），自能成为屏蔽交换：实空间里库仑的长程尾巴被指数压低（$W(r)\sim e^{-k_{TF}r}/r$）。

**方向为什么对**：HF 能隙高估（如 NiO 的 HF 能隙 ~10 eV 级 vs 实验 ~4 eV）的根源是裸交换的非局域刚性——拿走一个电子时，交换势在所有地方同时骤变，能隙被夸大。物理上，其余电子的屏蔽会**软化**这个势：空穴周围聚起屏蔽云，有效相互作用减弱、能隙收缩。实验证据：把 Si 的 HF 能隙（>5 eV）与 LDA（0.5 eV）夹在两端，GW（1.25 eV）落在中间且贴近实验——**屏蔽恰到好处地补上 KS 低估的那块**。一句话：HF 的错与 DFT 的错方向相反，GW 用屏蔽交换站在中间——这不是巧合，是"裸 → 屏蔽 → 局域平均"谱系的自然标度。

</details>

**3.** 从第 6 章搬运屏蔽：写出 RPA 介电函数 $\varepsilon = 1 - vP_0$ 与屏蔽库仑 $W = \varepsilon^{-1}v$ 的推导骨架，说明 Thomas–Fermi 是它的哪个极限；并算长波静态度 $W(q\to0,\omega=0) \to v(q)\,q^2/k_{TF}^2$ 的行为。

<details markdown="1"><summary>点击显示答案</summary>

**骨架**（第 6 章 4、6 节）：外电荷 $\rho_\text{ext}$ 直接产生势 $v\rho_\text{ext}$；电子气以密度响应 $\delta n = P_0\,\delta v_\text{tot}$（$P_0$ 为 Lindhard 函数——第 3 章费米海泡利限制下的密度响应），感应电荷产生 $v\delta n$：

$$\delta v_\text{tot} = v\rho_\text{ext} + vP_0\,\delta v_\text{tot}\;\Longrightarrow\;\delta v_\text{tot} = \frac{v}{1 - vP_0}\rho_\text{ext} \equiv \varepsilon^{-1}v\,\rho_\text{ext},\qquad \varepsilon(q,\omega) = 1 - v(q)P_0(q,\omega).$$

环图求和（RPA）= 这条自洽链的图语言：泡泡链几何级数，与 QFT 真空极化（[QFT 书](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)）同构——第 6 章已排演，本章照搬进 $W$。

**TF 极限**：$P_0(q\to0,\omega\to0) = -g(E_F) = -3n/2E_F$（第 3 章态密度；静态密度响应为负）→ $\varepsilon(q) = 1 + k_{TF}^2/q^2$，$k_{TF}^2 = 4\pi g(E_F)$（高斯单位）。

**长波行为**：

$$W(q\to0) = \frac{v(q)}{1 + k_{TF}^2/q^2} \approx \frac{4\pi}{q^2}\cdot\frac{q^2}{k_{TF}^2} = \frac{4\pi}{k_{TF}^2}\;\longrightarrow\;\text{有限常数}.$$

裸库仑的 $1/q^2$ 尖峰（长程刚性）被屏蔽**削平成常数**——这正是 (2) 里能隙收缩的动量空间机制。频率依赖（动力学屏蔽：$\omega$ 大时电子来不及响应、$W \to v$）给出自能的寿命与卫星结构（等离激元伴线），是 GW 谱超出静态方法的看家本领。

</details>

**4.** 原子极限 Hubbard-I：对半满孤立 Hubbard 格点求 $G(\omega)$ 与 $\Sigma(\omega) = U^2/4\omega$，画出/描述谱函数，并解释 $\Sigma$ 在 $\omega = 0$ 的奇异性为什么判了"围绕有限自能展开"的方法（HF、微扰、KS）的死刑。

<details markdown="1"><summary>点击显示答案</summary>

**谱表示**：杂质（原子）上 $N = 0,1,2$ 的能量为 $E_0 = 0$、$E_1 = -\mu$、$E_2 = U - 2\mu$。 Lehmann 表示（添加/移除电子的极点，权重为热平均）：

$$G(\omega) = \frac{P(N=1)\ \text{项}}{\omega - (E_1 - E_0) + i0^+} + \frac{\cdots}{\omega - (E_2 - E_1) - i0^+}\;\xrightarrow{\ \mu = U/2\ }\; \frac12\left[\frac{1}{\omega + U/2 + i0^+} + \frac{1}{\omega - U/2 - i0^+}\right],$$

（半满：$N=1$ 概率 ½，两极点各带权重 ½——分别来自移除与添加电子）。合并：

$$G(\omega) = \frac{\omega}{\omega^2 - U^2/4} \qquad\Longrightarrow\qquad G^{-1} = \omega - \frac{U^2}{4\omega} = \omega - \Sigma(\omega),\qquad \boxed{\Sigma(\omega) = \frac{U^2}{4\omega}}.$$

**谱**：两个 δ 峰（Hubbard 带）在 $\omega = \pm U/2$，间隔 $U$，权重各 ½——第 13 章 4.2–4.3 节的定性 Hubbard 带在此定量化。

**奇异性的判决**：$\omega\to0$ 时 $\lvert\Sigma\rvert\to\infty$。一切以"自能有限且可微扰展开"为前提的方法在此崩塌：HF 的静态 $\Sigma$ 无法在谱中央产生任何结构（它只能整体平移能带）；微扰级数的每阶都在 $\omega = 0$ 处更奇异（$U^2/\omega$ 的级数展开无意义）；KS 的局域势 $v_{xc}$ 同理只能在能带图上做刚体移动。**Mott 能隙是自能的动力学行为（对 $\omega$ 的强依赖）直接雕刻进谱函数的结构**——这就是 NiO 在 DFT 里是金属的根本原因（第 16 章 6.3），也是 DMFT 把 $\Sigma(\omega)$ 当主角的根本动机。

</details>

**5.** DMFT 自洽回路：写出局域格林函数 $G_\text{loc}$、Weiss 函数 $\mathcal G_0$ 与杂质模型三者的关系；证明无穷配位数极限下"自能局域"严格成立（论证骨架即可）；最后用 Hubbard-I 自能代入有限带宽晶格，求准粒子带边并核对 Mott 隙 ~ $U - W$ 的量级。

<details markdown="1"><summary>点击显示答案</summary>

**回路**：

$$G_\text{loc}(\omega) = \sum_{\vec k}\frac{1}{\omega + \mu - \varepsilon_{\vec k} - \Sigma(\omega)}\;=\;\int\text d\varepsilon\,\frac{\rho_0(\varepsilon)}{\omega + \mu - \varepsilon - \Sigma(\omega)},$$

（$\rho_0$ 为非相互作用态密度；$\Sigma$ 无 $\vec k$ 依赖使求和可积）。定义 Weiss 函数

$$\mathcal G_0^{-1}(\omega) = G_\text{loc}^{-1}(\omega) + \Sigma(\omega),$$

它扮演"浴的格林函数"：杂质模型（一个相互作用格点 + 产生 $\mathcal G_0$ 的非相互作用于）严格解出新的 $\Sigma$，回代循环——收敛时晶格要求的 $G_\text{loc}$ 与杂质产出的 $G_\text{imp}$ 相等，自洽闭合。$\mathcal G_0$ 就是第 7 章 Weiss 分子场的格林函数版本：**静态平均场 → 动力学平均场**，自旋的近邻耦合 → 电子的浴谱。

**无穷维论证骨架**（Metzner–Vollhardt）：把跃迁 $t$ 按配位数 $z$ 缩放（$t^\ast = t/\sqrt z$，保持带宽有限），非局域自能图的每条逾期的动量转移携带 $1/z$ 压缩因子——二阶自能的非局域部分 $\Sigma(\vec k)$ 中，自旋/密度通道的非局域项随 $z\to\infty$ 严格消失，只剩 $\Sigma(\omega)$。与经典 Weiss 理论 $z\to\infty$ 严格、$z = 6$–12 已很好同一个剧本——只是量子版保留了时间维度上的全部涨落。

**Hubbard-I 代入晶格**：$G(\vec k,\omega) = \big[\omega - \varepsilon_{\vec k} - U^2/4\omega\big]^{-1}$，极点由

$$\omega^2 - \varepsilon_{\vec k}\,\omega - U^2/4 = 0\;\Longrightarrow\;\omega_\pm(\varepsilon_{\vec k}) = \frac{\varepsilon_{\vec k} \pm\sqrt{\varepsilon_{\vec k}^2 + U^2}}{2}.$$

带宽 $W$ 的带（$\varepsilon \in [-W/2, W/2]$）劈成两支：上带边 $\omega_+^\max = \tfrac{1}{2}\big[\tfrac W2 + \sqrt{\tfrac{W^2}4 + U^2}\big]$，下带边 $\omega_-^\max$ 同理，Mott 隙

$$E_g = \omega_+(-W/2) - \omega_- (W/2) = \sqrt{U^2 + W^2/4} - W/2\;\xrightarrow{\ U\gg W\ }\;U - \frac W2 + O(W^2/U),$$

大 $U$ 时回到第 13 章的口号 $E_g \lesssim U$；小 $U$ 时隙闭合（Hubbard-I 在金属侧定性太粗——准粒子峰要完整 DMFT 才长出来，但隙的量级与开关方向正确）。**核对完毕**：DMFT 的原子极限精确、弱耦合方向定性正确，中间的 Mott 转变由自洽回路自动演出。

</details>

## 参考

- Fetter & Walecka《Quantum Theory of Many-Particle Systems》第 3–6 章：格林函数、Dyson 方程与自能的系统讲法（与 QFT 书的传播子语言互为镜像）。
- L. Hedin, Phys. Rev. 139, A796 (1965)：Hedin 方程组的原始文献。
- F. Aryasetiawan & O. Gunnarsson, Rep. Prog. Phys. 61, 237 (1998)：《The GW method》综述——本章第 4 节的主线参考。
- W. Metzner & D. Vollhardt, Phys. Rev. Lett. 62, 324 (1989)：$d\to\infty$ 与自能局域性。
- A. Georges, G. Kotliar, W. Krauth & M. J. Rozenberg, Rev. Mod. Phys. 68, 13 (1996)：《DMFT》综述——第 5 节的权威参考（含 Hubbard-I 与三峰谱）。
- G. Kotliar et al., Rev. Mod. Phys. 78, 865 (2006)：DFT+DMFT 电子结构方法综述（第 5.4 节）。
