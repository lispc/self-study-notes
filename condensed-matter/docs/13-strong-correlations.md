# 强关联浅尝：Mott 绝缘体、Hubbard 模型与高温超导悬案

> 本书位置：凝聚态物理入门导论第 13 章（第三部分：现代专题）。
> 前置知识：[能带论](04-band-theory.md)（紧束缚、金属/绝缘体判据）、[磁性](07-magnetism.md)（交换作用、Heisenberg 模型）、定态微扰论（[QFT 书第 2 阶段笔记](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md) 的第 3 节正好是我们需要的工具）、二次量子化记号。
> 学习目标：说清能带论为什么会失败（Mott 的论证）；写出 Hubbard 模型并在三个极限下把它解掉；从二阶微扰论完整推出超交换 $J=4t^2/U$；知道掺杂、重费米子、高温超导各自"难在哪"，以及数值方法在这场持久战中的角色。

---

## 1. 一句话总结

**当电子之间的库仑排斥 $U$ 与电子跳跃带来的动能收益 $t$ 同量级甚至更大时，"先看单体能带、再把相互作用当微扰"的整个框架就失效了：半满的能带可以是绝缘体（Mott 绝缘体），自旋自由度通过虚跳跃获得反铁磁耦合 $J=4t^2/U$，而掺入少量载流子后出现的物理——包括铜氧化物高温超导——至今没有一个可控的小参数可以展开，是凝聚态物理最著名的开放问题。**

本篇保留 $\hbar$ 与 $k_B$（本书约定；推导中二者基本不登场，只在估算温度尺度时出现）。下面把这句话逐层拆开。

## 2. 能带论何时失败：Mott 的定性论证

回顾[第 4 章](04-band-theory.md)的判据：每个原胞含奇数个电子 $\Rightarrow$ 能带半满 $\Rightarrow$ 金属。这条判据在一大批材料上公然失败：**过渡金属氧化物** NiO、CoO、MnO 都有部分填充的 $3d$ 壳层，能带论斩钉截铁地预言它们是金属，实验上它们却是相当好的绝缘体（而且是反铁磁体）。同样地，把钠蒸汽的原子间距人为拉大——每个原子仍然贡献一个 $3s$ 电子，"能带"仍然半满——它绝不会一直导电下去。

Mott（1949 年前后）给出的定性论证极其朴素。考虑晶格常数为 $a$ 的单价电子晶格，问：一个电子从某原子跑到**近邻**已被占据的原子上，代价和收益各是什么？

- **代价**：双占据意味着两个电子挤在同一个原子轨道上，感受到未屏蔽的库仑排斥，量级为

$$U \sim \frac{e^2}{4\pi\varepsilon_0\, a_{\text{轨道}}},$$

对 $d$ 轨道（空间上很局域）这可以高达几 eV。

- **收益**：电子离域化成 Bloch 波，获得动能收益，量级为带宽 $W \sim zt$（$z$ 是配位数，$t$ 是近邻跳跃幅度）。$t$ 由相邻原子的轨道交叠决定，随原子间距指数衰减。

结论：**原子间距小（交叠强）时 $W > U$，电子离域，是金属；原子间距大（交叠弱）时 $U > W$，电子宁可钉在各自原子上，是绝缘体。** 绝缘的原因不是"能带填满了"，而是"挪动电荷要付 $U$ 的代价"——这叫 **Mott 绝缘体**，它的能隙是相互作用撑开的，与能带绝缘体的单粒子能隙完全是两回事。1949 年 Mott 的论证是定性的；把这个图像变成一个可以推导的模型，就是下一节的 Hubbard 模型（1963）。

## 3. Hubbard 模型：t 与 U 的竞争

取紧束缚极限：每个格点 $i$ 只保留一个轨道，电子在该轨道上的产生湮灭算符为 $c^\dagger_{i\sigma}, c_{i\sigma}$（$\sigma=\uparrow,\downarrow$），满足费米子反对易关系 $\{c_{i\sigma}, c^\dagger_{j\sigma'}\} = \delta_{ij}\delta_{\sigma\sigma'}$。对整个多体问题只保留两项最大的矩阵元：

1. **跳跃**：近邻格点间轨道的交叠积分 $t$，来自单体哈密顿量（动能 + 晶格势）的非对角元；
2. **同点库仑排斥**：同一格点双占据的代价 $U$，即库仑相互作用在同一条 Wannier 轨道上的对角矩阵元

$$U = \int d^3r\, d^3r'\; \lvert\phi(\vec r)\rvert^2 \lvert\phi(\vec r')\rvert^2\, \frac{e^2}{4\pi\varepsilon_0 \lvert \vec r - \vec r'\rvert}.$$

其余各项（点间库仑、交换积分等）都小一个量级以上，先扔掉。得到 **Hubbard 模型**：

$$\boxed{H = -t \sum_{\langle ij\rangle, \sigma} \left( c^\dagger_{i\sigma} c_{j\sigma} + \mathrm{h.c.} \right) + U \sum_i n_{i\uparrow} n_{i\downarrow}}, \qquad n_{i\sigma} = c^\dagger_{i\sigma} c_{i\sigma}.$$

$\langle ij\rangle$ 表示只对最近邻求和。这个模型里只有两个能量尺度：

- $t$（或带宽 $W\sim zt$）：电子**离域**的收益，偏向金属；
- $U$：电子**双占据**的代价，偏向局域化、绝缘。

全部物理都装在无量纲比值 $U/t$ 和填充数 $n = N_e/N_{\text{sites}}$（每个格点的平均电子数，$0\le n\le 2$）里。**半满 $n=1$**（每格点一个电子）是关联效应最剧烈的填充，也是铜氧化物母相所在的位置。注意这个模型"看起来"只有两项，却既不能在小 $U/t$ 时绕能带金属微扰到 Mott 相，也不能在大 $U/t$ 时绕原子极限微扰到底——它是一般意义上不可解的，这正是它出名的原因。

## 4. 两个可解极限与夹在中间的 Mott 绝缘体

### 4.1 $U=0$：能带金属

$U=0$ 时 $H$ 是二次型，平移不变性保证 Bloch 基对角化它。以格距 $a$ 的简单立方晶格为例，傅里叶变换 $c_{i\sigma} = \frac{1}{\sqrt N}\sum_{\vec k} e^{i\vec k\cdot\vec r_i} c_{\vec k\sigma}$ 给出

$$H = \sum_{\vec k, \sigma} \varepsilon_{\vec k}\, c^\dagger_{\vec k\sigma} c_{\vec k\sigma}, \qquad \varepsilon_{\vec k} = -2t\big(\cos k_x a + \cos k_y a + \cos k_z a\big).$$

带宽 $W = 2zt = 12t$。半满时（每个 $\vec k$ 态填两个自旋，共填满半个 Brillouin 区）存在明确的费米面：这就是[第 4 章](04-band-theory.md)的能带金属，无相互作用极限下唯一可能的结局。

### 4.2 $t=0$：原子极限

$t=0$ 时格点之间完全脱耦，每个格点独立。单个格点的 Hilbert 空间只有 4 个态，$H_i = U n_{i\uparrow} n_{i\downarrow}$（取单占据能量为零点）立刻对角化：

| 格点态 | 记号 | 能量 | 占据数 |
|---|---|---|---|
| 空 | $\lvert 0\rangle$ | $0$ | $0$ |
| 单占据 | $\lvert\uparrow\rangle,\ \lvert\downarrow\rangle$ | $0$ | $1$ |
| 双占据 | $\lvert\uparrow\downarrow\rangle$ | $U$ | $2$ |

重点不在能量本征值本身，而在**单粒子谱**：往系统里加/减一个电子要花多少能量？

- 向**空格点**加一个电子：能量 $0$；
- 向**已单占据**的格点加一个电子（自旋须相反）：能量 $U$；
- 从**单占据**格点移走一个电子：能量 $0$。

半满（每格点恰一个电子）时，化学势发生跳变：移走电子的化学势 $\mu^- = 0$，加入电子的化学势 $\mu^+ = U$。**电荷能隙 $\Delta = \mu^+ - \mu^- = U$**——谱分裂成 $\omega = 0$（下 Hubbard 带的雏形）与 $\omega = U$（上 Hubbard 带的雏形）两根极点。注意此时自旋完全简并（$2^N$ 重），磁性还完全没有登场。

### 4.3 半满、$U \gg t$：Mott 绝缘体与 Hubbard 带

现在打开小的 $t$。半满时基态里绝大多数格点单占据；任何一次跳跃都造出一个双占据格点（能量 $U$），所以**低频电荷激发仍然隔着 $\sim U$ 的能隙**——绝缘性在有限 $t$ 下存活，这就是 Mott 绝缘体。把原子极限的两根极点"加宽"成能带，得到：

- **下 Hubbard 带**（LHB）：从单占据格点移走电子（空穴在其中传播），中心在 $\mu$ 下方；
- **上 Hubbard 带**（UHB）：向单占据格点加电子（双占据在其中传播），中心在 $\mu$ 上方 $\sim U$ 处。

与能带绝缘体的区别值得强调：能带绝缘体的能隙是"带填满了"，Mott 绝缘体的能隙是"加电子要付 $U$"，即使能带只填了一半。电荷被冻结了，**自旋却还活着**——每个格点上那个孤立的自旋 $1/2$ 之间靠什么相互作用？下一节的答案是本篇技术上最重要的推导。

## 5. 超交换：从 Hubbard 到 Heisenberg（完整推导）

**结论先行**：半满大 $U$ 的 Hubbard 模型在低能下等价于反铁磁 Heisenberg 模型

$$H_{\text{eff}} = J \sum_{\langle ij\rangle} \left( \vec S_i \cdot \vec S_j - \tfrac14\, n_i n_j \right), \qquad J = \frac{4t^2}{U} > 0.$$

这就是[第 7 章](07-magnetism.md)提到的**超交换**（superexchange）机制的微观出处：磁性绝缘体里没有巡游电子，相邻自旋却通过"虚拟地跳到对方格点再跳回来"获得反铁磁耦合。下面用二阶简并微扰论完整推导。微扰论的框架（$H = H_0 + V$，能量修正逐级展开）见[量子力学阶段的微扰论笔记](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)；这里把方法用在格点模型上。

### 5.1 两个格点的精确设定

只需考虑一对近邻格点 $1, 2$（每对的推导相同）。取

$$H_0 = U\,(n_{1\uparrow}n_{1\downarrow} + n_{2\uparrow}n_{2\downarrow}), \qquad V = -t \sum_\sigma \left( c^\dagger_{1\sigma} c_{2\sigma} + c^\dagger_{2\sigma} c_{1\sigma} \right),$$

半满即两个电子。Hilbert 空间按 $H_0$ 的能量分层：

- **低能子空间**（$E = 0$，4 重简并）：两个格点各单占据

$$\lvert\uparrow,\downarrow\rangle,\ \lvert\downarrow,\uparrow\rangle,\ \lvert\uparrow,\uparrow\rangle,\ \lvert\downarrow,\downarrow\rangle,$$

其中 $\lvert\sigma,\sigma'\rangle \equiv c^\dagger_{1\sigma} c^\dagger_{2\sigma'}\lvert 0\rangle$。

- **高能子空间**（$E = U$，2 维）：双占据态

$$\lvert d_1\rangle = c^\dagger_{1\uparrow} c^\dagger_{1\downarrow}\lvert 0\rangle, \qquad \lvert d_2\rangle = c^\dagger_{2\uparrow} c^\dagger_{2\downarrow}\lvert 0\rangle.$$

### 5.2 一阶微扰：零

$V$ 作用在任何单占据态上，必然把一个电子搬到已被占据的格点上——产物是双占据态，落在高能子空间里。所以 $V$ 在低能子空间内的矩阵元全为零：$\langle \beta | V | \alpha \rangle = 0$。物理含义：**真实**的跳跃被 $U$ 禁止了，一阶没有任何效应。

### 5.3 二阶微扰：虚跳跃

二阶有效哈密顿量（简并微扰论，记 $P$ 为低能子空间的投影）为

$$\langle\beta\rvert H_{\text{eff}}\lvert\alpha\rangle = \sum_{m \in \text{高能}} \frac{\langle\beta\rvert V \lvert m\rangle\langle m\rvert V \lvert\alpha\rangle}{E_0 - E_m} = -\frac{1}{U}\sum_{m=\lvert d_1\rangle,\lvert d_2\rangle} \langle\beta\rvert V\lvert m\rangle\langle m\rvert V\lvert\alpha\rangle.$$

先算 $V$ 作用在基态组态上。约定态的算符次序 $\lvert\sigma,\sigma'\rangle = c^\dagger_{1\sigma}c^\dagger_{2\sigma'}\lvert0\rangle$，小心处理反对易带来的符号：

$$V\lvert\uparrow,\downarrow\rangle = -t\lvert d_1\rangle - t\lvert d_2\rangle,$$

$$V\lvert\downarrow,\uparrow\rangle = +t\lvert d_1\rangle + t\lvert d_2\rangle,$$

（两式之间差一个总符号，来自 $c_{2\uparrow}$ 与 $c^\dagger_{1\downarrow}$ 交换次序；自检问题 2 要求你亲手核对这个符号。）而平行自旋态被泡利原理直接封杀：

$$V\lvert\uparrow,\uparrow\rangle = V\lvert\downarrow,\downarrow\rangle = 0.$$

代入二阶公式。对角元：$\lvert\uparrow,\downarrow\rangle$ 经两个中间态各贡献 $\lvert t\rvert^2$，共 $-2t^2/U$；非对角元：$\lvert\uparrow,\downarrow\rangle \to \lvert d_1\rangle \to \lvert\downarrow,\uparrow\rangle$ 与经 $\lvert d_2\rangle$ 的两条路径**同号**（上面的相对符号在这里起决定作用），各贡献 $-t^2/U$，共 $-2t^2/U$。于是在 $\{\lvert\uparrow,\downarrow\rangle, \lvert\downarrow,\uparrow\rangle\}$ 子空间里

$$H_{\text{eff}} = -\frac{2t^2}{U} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix},$$

而 $\lvert\uparrow,\uparrow\rangle, \lvert\downarrow,\downarrow\rangle$ 的能量修正为零。

### 5.4 对角化：单态被压低

$H_{\text{eff}}$ 的两个本征态是自旋单态与三重态的 $m=0$ 分量：

$$\lvert s\rangle = \frac{\lvert\uparrow,\downarrow\rangle - \lvert\downarrow,\uparrow\rangle}{\sqrt2}, \qquad E_s^{(2)} = -\frac{4t^2}{U},$$

$$\lvert t_0\rangle = \frac{\lvert\uparrow,\downarrow\rangle + \lvert\downarrow,\uparrow\rangle}{\sqrt2}, \qquad E_{t_0}^{(2)} = 0.$$

物理图像很干净：单态里两个电子"反对称地各占一半两个格点"，$V$ 把它与双占据态**相长**耦合（$V\lvert s\rangle = -2t\,\lvert D\rangle$，$\lvert D\rangle = (\lvert d_1\rangle + \lvert d_2\rangle)/\sqrt2$，矩阵元 $\lvert\langle D|V|s\rangle\rvert = 2t$，能量压低 $-(2t)^2/U = -4t^2/U$）；三重态里两个跳跃路径**相消**干涉，$V\lvert t_0\rangle = 0$——泡利原理禁止平行自旋靠近，三重态享受不到离域的动能收益。**反铁磁（单态）有利的根源是动能，不是某种神秘的"磁力"。**

### 5.5 写成 Heisenberg 形式

用 $\vec S_1\cdot\vec S_2 = S_1^z S_2^z + \tfrac12(S_1^+ S_2^- + S_1^- S_2^+)$，它在单态上取 $-3/4$、三重态上取 $+1/4$。要同时复现 $E_s^{(2)} = -4t^2/U$ 与 $E_{t}^{(2)} = 0$，取

$$H_{\text{eff}} = J\left(\vec S_1\cdot\vec S_2 - \tfrac14\right), \qquad J \equiv E_{t} - E_{s} = \frac{4t^2}{U}.$$

（$-\tfrac14 n_1 n_2$ 一项在半满时为常数，只是能量零点；离开半满才重要。）对每对近邻重复同一推导，就得到本节开头的格子 Heisenberg 模型。$J>0$ 即**反铁磁**耦合。

量级估算：铜氧化物里典型的 $t \sim 0.3\ \text{eV}$、$U \sim 3\ \text{eV}$，

$$J = \frac{4 \times (0.3\ \text{eV})^2}{3\ \text{eV}} = 0.12\ \text{eV} \;\approx\; k_B \times 1400\ \text{K},$$

与 La$_2$CuO$_4$ 实测的交换常数 $J \approx 130\ \text{meV}$ 定量吻合——这个不起眼的二阶效应撑起了一整类材料的磁性。

<details markdown="1"><summary>补充说明：为什么叫"超"交换</summary>

[第 7 章](07-magnetism.md)讲过 Heisenberg 模型里 $J$ 的一个来源是**直接交换**：相邻原子的轨道直接交叠，泡利原理 + 库仑相互作用产生自旋依赖的能量分裂。但在氧化物里，磁性离子（如 Cu$^{2+}$）之间隔着一个氧离子，$d$ 轨道几乎不直接交叠，直接交换可以忽略。耦合是通过中间氧 $2p$ 轨道的"接力"跳跃实现的（$d$–$p$–$d$ 虚过程），所以叫超交换。本篇在有效单带 Hubbard 模型里推导的 $J = 4t^2/U$，在数学结构上与之完全相同：都是"高能电荷涨落被积掉后，低能自旋获得有效耦合"。Anderson 1950 年代的超交换理论正是这类微扰推导的开端，后来发展成固体中磁性相互作用的系统分类（Goodenough–Kanamori 规则）。

</details>

## 6. 掺杂：一切物理都变了

半满 Mott 绝缘体是"冻结"的态；用化学掺杂（如 La$_{2-x}$Sr$_x$CuO$_4$ 里的 Sr）移走少量电子，引入浓度 $x$ 的**空穴**，物理立刻变得丰富而困难：

- 空穴在反铁磁自旋背景中运动，每一步都打乱自旋排列、留下"磁挫败"的痕迹——**电荷自由度与自旋自由度强耦合**，再没有干净的分离；
- **Nagaoka 定理**：$U\to\infty$、只掺**一个**空穴的 Hubbard 模型（在特定晶格上）基态是**铁磁**的——一个空穴就能翻转整块磁体。这定理条件苛刻（无穷大 $U$、单个空穴、特定晶格），实际材料中不适用，但它戏剧性地说明掺杂系统的基态对参数极度敏感；
- 大 $U$ 下更诚实的出发点是 **t–J 模型**：把双占据态彻底投影掉（Gutzwiller 投影），只保留空穴跳跃与超交换

$$H_{t\text{-}J} = -t\sum_{\langle ij\rangle,\sigma} P\left(c^\dagger_{i\sigma}c_{j\sigma} + \mathrm{h.c.}\right)P + J\sum_{\langle ij\rangle}\left(\vec S_i\cdot\vec S_j - \tfrac14 n_i n_j\right),$$

$P$ 是"禁止双占据"的投影算符。注意 $P$ 使算符代数变得别扭（不再是普通费米子），这正是 t–J 模型难解的技术根源之一。高温超导的多数微观讨论都在 t–J 或掺杂 Hubbard 模型的框架里进行。

## 7. 重费米子与近藤效应

强关联的另一张面孔出现在含稀土/锕系元素（Ce、Yb、U）的金属间化合物里，如 CeAl$_3$、CeCu$_6$。最小图像是**近藤效应**：

- 稀释的磁性杂质（局域自旋 $\vec S$）与导带电子（自旋 $\vec s$）通过反铁磁交换耦合 $J_K\, \vec S\cdot\vec s$（微观上又是同一类虚跳跃机制）；
- 高温下磁性杂质近似自由，导带电子在其上发生**自旋翻转散射**；微扰论算到三阶，散射率含 $\ln(k_B T / D)$ 项（$D$ 为带宽），随降温**增大**。叠加在普通金属"降温电阻减小"的行为上，电阻出现**极小值**——Kondo 1964 年正是为解释这个老实验谜题而做此计算；
- 继续降温穿过 **Kondo 温度** $T_K \sim D\, e^{-1/(J_K \rho)}$，导带电子把局域磁矩**屏蔽**成单态（"Kondo 单态"云），杂质从散射源变成相干晶格的一部分。

在重费米子化合物中，$f$ 电子的局域磁矩排成晶格，每个都被导带屏蔽；低温下形成相干的**重电子能带**：比热系数 $\gamma$ 比普适金属大 2–3 个数量级，对应**有效质量 $m^*/m_e \sim 10^2$–$10^3$**——电子像背了整个晶格在爬行。重费米子是"局域磁矩 ↔ 巡游电子"这场拔河的低温和解产物，也是[第 6 章](06-interacting-electron-gas.md) Fermi 液体理论最极端的秀场：准粒子依然成立，只是重得离谱。

## 8. 高温超导：诚实的悬案

1986 年 Bednorz 与 Müller 在铜氧化物 La$_{2-x}$Ba$_x$CuO$_4$ 中发现 $T_c \approx 35\ \text{K}$ 的超导，随后 YBCO（$T_c \approx 93\ \text{K}$，突破液氮温度）、Bi 系、Hg 系（$T_c \approx 134\ \text{K}$）接连刷新纪录。近四十年过去，**配对机制仍无公认答案**。先摆实验事实（铜氧化物相图的通用骨架）：

- **母相**：$x=0$ 是反铁磁 Mott 绝缘体（正是本篇第 4、5 节的物理；$J\sim 130\ \text{meV}$）；
- **掺杂 $x$ 很小**（百分之几）就杀死反铁磁长程序，随后出现**赝能隙**区：$T_c$ 之上很大一片温区里谱已部分失去低能权重，却没有超导相干——不像任何已知的"正常金属"；
- **超导穹顶**：$T_c(x)$ 呈钟形，在"最佳掺杂" $x \approx 0.16$ 处达峰；配对对称性被一系列相位敏感实验（角分辨光电子谱、Josephson 干涉、SQUID 显微镜）钉死为 **$d_{x^2-y^2}$ 波**——能隙在费米面上有节点，符号四瓣交替，与[第 8 章](08-superconductivity.md)的各向同性 $s$ 波 BCS 完全不同；
- **奇异金属**：穹顶上方、赝能隙区之外的宽广温区，电阻**严格线性于 $T$**（$\rho \propto T$）直到远超 $k_B T$ 超过任何声子能量的温度，违背 Boltzmann 输运的整个框架（声子散射给出 $\rho\propto T$ 只在高温渐近成立，且应饱和）。

为什么难？一句话：**没有小参数**。

- BCS 之所以可解，是因为弱耦合：配对相互作用 $\lambda \ll 1$，平均场精确；Mott 物理之所以可定性，是因为 $U/t \gg 1$ 时可以把 $t$ 当微扰。而铜氧化物里 $U/t \sim 8$–$10$，两头不靠：从金属端做微扰论到 $U/t \sim 8$ 早已失控，从 Mott 端展开到 $x \sim 0.15$ 也早已离开微扰成立的区域。
- 同时是**二维**（涨落强，有效理论的红外行为敏感）、**强关联**（单粒子图像失效，ARPES 看到的"准粒子权重"在欠掺杂区趋近于零）、**多尺度**（$t, J, T_c$ 横跨两个数量级）。
- 于是每个可计算的极限都与实验隔着一道非微扰的鸿沟。这是凝聚态物理版的"强耦合量子场论"处境——QFT 书里微扰论失效时的窘迫（[重整化笔记](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)讨论过耦合跑到强区的情形）在这里不是边缘话题，而是主题本身。

值得诚实记录的现状：理论上存在若干竞争框架（自旋涨落介导配对、RVB/自旋液体、条纹序、预成型配对 + 相位涨落……），各自解释一部分实验，无一统摄全局。共识只有：配对胶水**很可能**与磁性涨落有关（$d$ 波 + 紧邻反铁磁相是最强的暗示），但"很可能"不是推导。

## 9. 方法学：没有小参数时怎么办

解析微扰论两头失效，强关联问题的主战场移到了数值与场论：

- **精确对角化（ED）**：直接对角化 Hubbard/t–J 的 Hamiltonian，物理透明，但 Hilbert 空间随格点数 $N$ 指数增长（$4^N$），实际只能算 $\sim 20$ 个格点——热力学极限遥不可及，靠有限尺寸标度外推。
- **量子 Monte Carlo（QMC）**：把配分函数写成路径积分后随机采样。对费米子在一般填充下遭遇**符号问题**：玻尔兹曼权重不正（正可负），信噪比随 $\beta$ 与体积指数恶化。半满 Hubbard（无掺杂、特定晶格）因对称性豁免，一掺杂即沦陷——恰好挡住了最重要的问题。
- **动力学平均场理论（DMFT）**：取配位数 $z\to\infty$ 时自能变成**局域**的（$\Sigma(\vec k, \omega) \to \Sigma(\omega)$），格点模型精确映射为一个自洽的"杂质 + 浴"问题（正是 Kondo 那类问题）。DMFT 给出了 Mott 转变的第一张定量相图（三峰谱：上下 Hubbard 带 + 准粒子峰），但丢掉空间涨落，对二维低 $T$ 物理需要团簇推广。
- **场论方法**：重整化群（识别低能相关/无关算符）、规范场论（自旋液体里的分数化激发）提供概念框架与可能的低能有效理论，但缺乏受控的展开参数，目前更多是组织思想的工具而非计算机器。

坦率地说：数值方法在持续逼近（DMRG、张量网络、改进的 QMC 不断刷新边界），但"从 Hubbard 模型推出高温超导相图"仍无人做到。这不是失败宣言，而是这个问题的度量衡。

## 小结

| 情形 | 物理图像 | 电荷能隙 | 自旋自由度 |
|---|---|---|---|
| $U=0$，半满 | 能带金属，有费米面 | 无 | 与电荷混杂，无独立动力学 |
| $t=0$，半满 | 孤立原子集合，谱在 $0$ 与 $U$ 两根极点 | $U$ | $2^N$ 重简并 |
| 半满，$U \gg t$ | Mott 绝缘体，上下 Hubbard 带 | $\sim U$ | Heisenberg 反铁磁，$J = 4t^2/U$ |
| 掺杂空穴 | t–J 物理，电荷与自旋强耦合 | 复杂（赝能隙等） | 磁挫败，可能介导配对 |

- 能带论失败的信号：能带没填满却是绝缘体（过渡金属氧化物）→ 相互作用能隙，即 Mott 物理。
- Hubbard 模型只有 $t, U$ 两个尺度，但一般情形不可解；可解极限是 $U=0$（金属）、$t=0$（原子）与半满大 $U$（Mott + Heisenberg）。
- 超交换 $J = 4t^2/U$ 是二阶微扰的产物，磁性[第 7 章](07-magnetism.md)的 Heisenberg 模型在此获得微观地基；反铁磁有利源于动能。
- 掺杂、重费米子（Kondo 屏蔽、$m^* \sim 10^3 m_e$）、高温超导（$d$ 波、赝能隙、奇异金属）是同一族"无小参数"难题；数值方法（ED、QMC、DMFT）与场论方法各守一段，悬案未决。

## 自检问题

**1.** 在原子极限（$t=0$）推导单粒子谱：往半满的 Hubbard 链加/减一个电子各有哪些可能的能量，权重是多少？由此说明电荷能隙为 $U$。

<details markdown="1"><summary>点击显示答案</summary>

半满时每个格点单占据（自旋 $\uparrow$ 或 $\downarrow$ 各半）。

**加电子**（$N \to N+1$）：新电子落在哪个格点上、自旋如何，决定能量代价。

- 落到空格点：半满下没有空格点，概率为零；
- 落到单占据格点（自旋须相反）：$c^\dagger_{i\bar\sigma}$ 作用在 $\lvert\sigma\rangle_i$ 上得到双占据 $\lvert\uparrow\downarrow\rangle_i$，能量 $U$。

所以加入谱只有一根极点 $\omega = U$，权重等于"可接受该自旋的格点比例"：对加 $\uparrow$ 电子，目标格点须是 $\downarrow$ 占据，比例为 $n_{\downarrow} = 1/2$（归一化上，加 $\uparrow$ 的谱权重中 $1/2$ 在 $\omega = U$）。更标准的写法是单格点推迟 Green 函数（原子极限）

$$G_\sigma(\omega) = \frac{1 - n_{\bar\sigma}}{\omega + i0^+} + \frac{n_{\bar\sigma}}{\omega - U + i0^+}, \qquad n_{\bar\sigma} = \tfrac12 \text{（半满）},$$

两根极点 $\omega = 0$ 与 $\omega = U$，权重各 $1/2$。

**减电子**（$N \to N-1$）：从单占据格点移走电子得空格点，能量 $0$；谱在 $\omega = 0$。

**能隙**：化学势的两个边 $\mu^- = E(N) - E(N-1) = 0$，$\mu^+ = E(N+1) - E(N) = U$，故电荷能隙

$$\Delta = \mu^+ - \mu^- = U.$$

注意：这里没有打开任何"带"——$t=0$ 时极点都是平的（无色散），打开 $t$ 后它们展宽成上下 Hubbard 带，但只要 $U \gg W$，能隙存活。

</details>

**2.** 补全超交换推导中被省略的费米子符号：验证 $V\lvert\uparrow,\downarrow\rangle = -t\lvert d_1\rangle - t\lvert d_2\rangle$ 与 $V\lvert\downarrow,\uparrow\rangle = +t\lvert d_1\rangle + t\lvert d_2\rangle$，并由此说明为什么三重态得不到能量修正。

<details markdown="1"><summary>点击显示答案</summary>

约定 $\lvert\sigma,\sigma'\rangle = c^\dagger_{1\sigma} c^\dagger_{2\sigma'}\lvert0\rangle$，$V = -t\sum_\sigma(c^\dagger_{1\sigma}c_{2\sigma} + c^\dagger_{2\sigma}c_{1\sigma})$。

对 $\lvert\uparrow,\downarrow\rangle = c^\dagger_{1\uparrow}c^\dagger_{2\downarrow}\lvert0\rangle$：

- $\sigma = \downarrow$、$2 \to 1$ 项：

$$-t\, c^\dagger_{1\downarrow} c_{2\downarrow} c^\dagger_{1\uparrow} c^\dagger_{2\downarrow}\lvert0\rangle = -t\, c^\dagger_{1\downarrow}\big({-}c^\dagger_{1\uparrow}\big) c_{2\downarrow} c^\dagger_{2\downarrow}\lvert0\rangle = +t\, c^\dagger_{1\downarrow} c^\dagger_{1\uparrow}\lvert0\rangle = -t\lvert d_1\rangle,$$

用了 $c_{2\downarrow}$ 与 $c^\dagger_{1\uparrow}$ 反对易（不同格点也反对易）、$c_{2\downarrow}c^\dagger_{2\downarrow}\lvert0\rangle = \lvert0\rangle$、$c^\dagger_{1\downarrow}c^\dagger_{1\uparrow} = -c^\dagger_{1\uparrow}c^\dagger_{1\downarrow}$。

- $\sigma = \uparrow$、$1 \to 2$ 项：

$$-t\, c^\dagger_{2\uparrow} c_{1\uparrow} c^\dagger_{1\uparrow} c^\dagger_{2\downarrow}\lvert0\rangle = -t\, c^\dagger_{2\uparrow} c^\dagger_{2\downarrow}\lvert0\rangle = -t\lvert d_2\rangle.$$

- 其余两项（$c_{2\uparrow}$、$c_{1\downarrow}$）湮灭在空格自旋上，为零。合起来 $V\lvert\uparrow,\downarrow\rangle = -t\lvert d_1\rangle - t\lvert d_2\rangle$。

对 $\lvert\downarrow,\uparrow\rangle = c^\dagger_{1\downarrow}c^\dagger_{2\uparrow}\lvert0\rangle$：

- $\sigma = \uparrow$、$2 \to 1$ 项：

$$-t\, c^\dagger_{1\uparrow} c_{2\uparrow} c^\dagger_{1\downarrow} c^\dagger_{2\uparrow}\lvert0\rangle = -t\, c^\dagger_{1\uparrow}\big({-}c^\dagger_{1\downarrow}\big)\lvert0\rangle = +t\, c^\dagger_{1\uparrow}c^\dagger_{1\downarrow}\lvert0\rangle = +t\lvert d_1\rangle,$$

这里 $c_{2\uparrow}$ 穿过 $c^\dagger_{1\downarrow}$ 才碰到自己的伙伴，多出一个负号——**这就是两式相对符号的出处**。

- $\sigma = \downarrow$、$1 \to 2$ 项：$-t\, c^\dagger_{2\downarrow} c_{1\downarrow} c^\dagger_{1\downarrow} c^\dagger_{2\uparrow}\lvert0\rangle = -t\, c^\dagger_{2\downarrow}c^\dagger_{2\uparrow}\lvert0\rangle = +t\lvert d_2\rangle$。

于是对三重态 $\lvert t_0\rangle = (\lvert\uparrow,\downarrow\rangle + \lvert\downarrow,\uparrow\rangle)/\sqrt2$：

$$V\lvert t_0\rangle = \frac{1}{\sqrt2}\big(-t\lvert d_1\rangle - t\lvert d_2\rangle + t\lvert d_1\rangle + t\lvert d_2\rangle\big) = 0,$$

两条虚跳跃路径**相消干涉**；二阶能量修正 $-\sum_m \lvert\langle m|V|t_0\rangle\rvert^2/U = 0$。物理根源是泡利原理：三重态两电子自旋平行，无法进入同一轨道的中间态。对单态 $\lvert s\rangle$ 则是相长干涉，$V\lvert s\rangle = -\sqrt2 t(\lvert d_1\rangle + \lvert d_2\rangle) = -2t\lvert D\rangle$，修正 $-(2t)^2/U = -4t^2/U$。符号约定变了每一项会变，但**相对符号**和最终能差不变。

</details>

**3.** 取 $t \approx 0.3\ \text{eV}$、$U \approx 3\ \text{eV}$，估算超交换耦合 $J$ 对应的温度尺度，并与 La$_2$CuO$_4$ 的实测 $J \approx 130\ \text{meV}$ 比较。

<details markdown="1"><summary>点击显示答案</summary>

$$J = \frac{4t^2}{U} = \frac{4 \times (0.3\ \text{eV})^2}{3\ \text{eV}} = \frac{4 \times 0.09}{3}\ \text{eV} = 0.12\ \text{eV} = 120\ \text{meV}.$$

换算成温度（$k_B = 8.617\times 10^{-5}\ \text{eV/K}$）：

$$T_J = \frac{J}{k_B} = \frac{0.12}{8.617\times 10^{-5}}\ \text{K} \approx 1.4\times 10^3\ \text{K}.$$

与实测值 $J_{\text{exp}} \approx 130\ \text{meV}$（$\approx 1500\ \text{K}$）相比，简单单带 Hubbard 估算只差不到 10%——考虑到模型把氧轨道、点间库仑全扔了，这个吻合度好得出奇，说明 $t$–$U$ 两参数图像抓住了主导尺度。

注意两点：

- $T_J \sim 1400\ \text{K}$ 是**微观交换**尺度，不是 Néel 温度。La$_2$CuO$_4$ 的 $T_N \approx 300\ \text{K}$ 远低于 $T_J$，因为 CuO$_2$ 面是准二维的：面内强耦合、面间弱耦合 $J' \ll J$，长程序要等三维耦合建立（Mermin–Wagner 定理禁止纯二维有限温磁序，见[第 7 章](07-magnetism.md)）。
- 这也解释了为什么铜氧化物的磁激发（自旋波）能延伸到 $\sim 300\ \text{meV}$ 的能量——超交换虽是高阶效应，尺度却一点都不小。

</details>

**4.** 半满 Hubbard 模型在大 $U$ 时是绝缘体。为什么这个结论不能用"能带填满了"来解释？请从谱和填充两个角度各给一个论据。

<details markdown="1"><summary>点击显示答案</summary>

**填充角度**：半满意味着每个格点平均一个电子、Brillouin 区里正好填满一半 $\vec k$ 态。无相互作用时（$U=0$）存在明确的费米面，态密度在 $\mu$ 处非零——按[第 4 章](04-band-theory.md)的判据这是不折不扣的金属。绝缘性是在 $U/t$ 增大后**连续出现的**（能隙随 $U$ 打开），而填充数从头到尾没变。若绝缘靠"填满"，能隙应在 $U=0$ 就存在。

**谱的角度**：看加减电子的能量（自检问题 1 的原子极限，或大 $U$ 下 Hubbard 带的推广）。能带绝缘体的能隙是"价带顶到导带底"的单粒子能隙，上下两个带是同一组 Bloch 轨道被周期性势场劈出来的；Mott 绝缘体的上下 Hubbard 带则分别是**移走电子**（空穴传播）与**加入电子**（双占据传播）的激发，能隙 $\sim U$ 由相互作用撑开。判据性实验是光电子谱/反光电子谱（PES/IPES）：Mott 绝缘体里加减谱之间的能隙随 $U$ 变化，且在 $U \to 0$ 极限能隙闭合回金属——而能带绝缘体把相互作用关掉能隙依然存在（那是它的全部来源）。

一句话：能带绝缘体是"没地方放电子"，Mott 绝缘体是"放电子要付钱"。

</details>

**5.** 解释为什么"电阻随温度降低出现极小值"暗示近藤屏蔽，并说明极小值两侧的电阻行为各由什么散射机制主导。

<details markdown="1"><summary>点击显示答案</summary>

普通金属中电阻随降温**单调下降**：电子–声子散射率随声子数 $n_{\text{声子}} \propto T$（高温）减少，$\rho_{\text{声子}}(T) \to 0$（$T \to 0$ 时剩残余电阻 $\rho_0$）。所以电阻**上升**的转折必须有新的、随降温增强的散射源。

磁性杂质提供的就是这个源。导带电子与局域自旋的交换耦合 $J_K \vec S\cdot\vec s$ 允许**自旋翻转散射**；微扰论到二阶只给常数贡献，到**三阶**出现对数项（来自自旋算符不对易：$S^+ S^- \neq S^- S^+$，时间次序不同的图不完全抵消），散射率

$$\tau^{-1} \propto J_K^2 \rho\,(1 + 2 J_K \rho \ln(k_B T / D) + \cdots), \qquad \rho\ \text{为费米面处态密度},$$

$J_K < 0$（反铁磁）时对数项随 $T$ 降低而**增大**。于是总电阻

$$\rho(T) = \underbrace{\rho_{\text{声子}}(T)}_{\text{随 } T \text{ 降而减}} + \underbrace{\rho_0 + c\, J_K^2\rho\big(1 + 2J_K\rho \ln(k_B T/D)\big)}_{\text{磁杂质，随 } T \text{ 降而增}},$$

两项竞争给出**极小值**（极小温度 $T_{\min} \propto \sqrt{c_{\text{杂质}}}$，随杂质浓度移动——这是判定近藤效应而非其他机制的实验指纹）。

极小值的出现暗示：低温处存在一种"散射越来越强"的机制，而对数发散不可能一直持续（微扰论在 $k_B T \sim T_K = D e^{-1/\lvert J_K\rvert\rho}$ 处失效）。强耦合区的真实物理（需要 Wilson 数值重整化群或 Bethe ansatz 才能算清）是：导带电子在 $T_K$ 以下把局域自旋**屏蔽**成总自旋单态——磁矩消失了，散射源被"吸收"进一个重整化极强的 Fermi 液体。电阻在 $T \to 0$ 趋于饱和（幺正极限），比热系数巨大。所以电阻极小是"自由磁矩 → 被屏蔽单态"这场 crossover 的中点路标。

</details>

## 参考

- Kittel《固体物理导论》（第 8 版）第 11–12 章：抗磁/顺磁与铁磁/反铁磁部分中关于交换作用与绝缘体磁性的讨论（超交换的唯象表述）。
- Ashcroft & Mermin《Solid State Physics》第 32–33 章：绝缘体磁性与巡游电子磁性；Kondo 效应与电阻极小的经典讨论见第 34 章。
- P. Fazekas, *Lecture Notes on Electron Correlation and Magnetism*，第 4–5 章：Mott 转变与 Hubbard 模型的系统讲义，本篇第 2–5 节与之对应。
- A. Auerbach, *Interacting Electrons and Quantum Magnetism*，第 3 章：超交换与 t–J 模型的推导。
- P. Coleman, *Introduction to Many-Body Physics*，第 15–17 章：Kondo 效应、重费米子与 DMFT 的现代处理。
- A. Georges, G. Kotliar, W. Krauth, M. Rozenberg, *Rev. Mod. Phys.* **68**, 13 (1996)：DMFT 的奠基性综述。
- B. Keimer et al., *Nature* **518**, 179 (2015)：高温超导研究现状的通俗但严谨的综述，第 8 节的相图事实均可在其中找到出处。
