# 补充材料：全同粒子与对称化公设——交换简并、Pauli 原理与交换作用

> 路线图位置：量子力学书 · 第二部分（可精确求解的体系）· 第 05 篇（[角动量理论](05-angular-momentum.md)）的补充材料（第 05s 篇，建议在第 06 篇之前读——氢原子的多电子记账要用它）
> 前置知识：第 03 篇（[形式体系](03-formalism-hilbert-dirac.md)第 9 节：复合系统与张量积、第 8 节约化密度矩阵）；第 05 篇（自旋 1/2 与旋量、第 6 节角动量相加与 CG 系数）。
> 学习目标：说清"全同"在量子力学里为什么比经典严格得多；会构造交换算符并证明其本征值只能取 $\pm 1$；陈述对称化公设并理解它如何把张量积空间砍掉一半；会用 Slater 行列式写 $N$ 个费米子的态并从中读出 Pauli 不相容原理；会构造两电子的自旋单态/三重态，并由此把"交换作用"（Heisenberg 耦合的出生地）从纯静电库仑排斥中推导出来；知道为什么 $S_N$ 的高维表示（"副统计"）在自然界缺席。
>
> 记号约定：本篇保留 $\hbar$（与第 05 篇一致）。交换算符记 $P_{ij}$；无量纲自旋算符记 $\vec s = \vec S/\hbar$（$\vec s = \vec\sigma/2$），$\vec s_1\cdot\vec s_2$ 的本征值为 $+1/4$（三重态）与 $-3/4$（单态）。库仑耦合简记 $e^2 \equiv e_{\rm SI}^2/(4\pi\varepsilon_0)$。

---

## 1. 一句话总结

**经典里两个"全同"粒子靠轨迹始终可分辨，量子里波函数一旦重叠，"哪个是哪个"就原则上不可观测——这迫使态空间从张量积砍到对称（玻色子，$+1$）或反对称（费米子，$-1$）子空间：这是独立于五大公设之外的一条公设（对称化公设）。反对称的直系结论是 Pauli 不相容：两个费米子不能占据同一单粒子态——元素周期表的座位账本由此而来；而对两个电子，总波函数反对称把空间部分与自旋部分锁成"对称配单态、反对称配三重态"，纯静电的库仑排斥经此一锁就冒出依赖于自旋的能量差——交换作用 $-2J\,\vec s_1\cdot\vec s_2$，铁磁性的量子根源。**

## 2. 经典可分辨 vs 量子不可分辨：交换简并

经典力学里"全同粒子"是个方便的说法：两个台球无论多像，逐帧盯住轨迹总能说"这是第一颗"。分辨依靠的是**连续的历史**，不依靠粒子自身的任何性质。

量子力学里没有这件事。两个粒子在 $t=0$ 标上"1 号""2 号"之后各自演化，波函数立刻开始扩散、重叠；碰撞之后重叠到无法再拆。此时"1 号在 $\vec r_1$、2 号在 $\vec r_2$"的概率密度 $|\Psi(\vec r_1,\vec r_2)|^2$ 与"1 号在 $\vec r_2$、2 号在 $\vec r_1$"的 $|\Psi(\vec r_2,\vec r_1)|^2$ 描述**同一个测量事件**（探测器只记录"这里有一个、那里有一个"，不记录编号）。任何可观测的力学量因此必须对粒子交换对称：$F(\vec r_1,\vec r_2) = F(\vec r_2,\vec r_1)$。

形式上，全同粒子的哈密顿量 $H = h(1) + h(2) + V(\lvert\vec r_1-\vec r_2\rvert)$ 与交换对易（第 3 节）。于是若 $\Psi(\vec r_1,\vec r_2)$ 是能量本征态，$\Psi(\vec r_2,\vec r_1)$ 也是，且能量相同——**交换简并**（exchange degeneracy）：任意线性组合 $c_1\Psi(\vec r_1,\vec r_2) + c_2\Psi(\vec r_2,\vec r_1)$ 都是同能量的解。薛定谔方程本身**挑不出**该选哪一个。公设必须出面。

## 3. 交换算符与对称化公设

定义**交换算符** $P_{12}$：

$$(P_{12}\Psi)(\vec r_1,\vec r_2) \equiv \Psi(\vec r_2,\vec r_1).$$

三条基本性质（自检问题 1）：

1. $P_{12}^2 = \mathbb 1$，且 $P_{12}$ 既幺正又厄米；
2. 对任意全同粒子体系的 $H$，$[P_{12}, H] = 0$；
3. 本征值只能取 $\pm 1$（厄米 + 平方为一）。

**对称化公设**：全同粒子的物理态空间不是整个张量积 $\mathcal H^{\otimes N}$，而是其在置换群 $S_N$ 作用下的对称子空间（所有 $P_{ij}$ 本征值 $+1$）或反对称子空间（所有 $P_{ij}$ 本征值 $-1$）：

$$\mathcal H^{\otimes N} \;\longrightarrow\; \mathrm{Sym}^N\mathcal H \quad(\text{玻色子})\qquad\text{或}\qquad \wedge^N\mathcal H \quad(\text{费米子}).$$

实验事实：**自旋为整数的粒子是玻色子（光子、声子、${}^4$He 原子），自旋为半整数的粒子是费米子（电子、质子、中子、${}^3$He）**。"自旋-统计"这条对应关系的真正证明需要相对论性量子场论（QFT 书第 4–5 阶段的主题之一），本篇作为公设与实验事实接受。

公设的后果立刻可见：物理态是所有 $P_{ij}$ 的**共同**本征态（对 $N\ge 3$ 这是个非平庸限制，见第 5 节与自检问题 5——$S_N$ 还有高维表示，但那意味着"交换后的态是另一个态"，"全同"就名存实亡；自然界没有这种"副统计"粒子）。

## 4. 两粒子：对称/反对称态与 Pauli 不相容

取正交归一的单粒子轨道 $\psi_a,\psi_b$。对称化公设允许的态只有两个：

$$\Psi_\pm(\vec r_1,\vec r_2) = \frac{1}{\sqrt{2}}\big[\psi_a(\vec r_1)\psi_b(\vec r_2) \pm \psi_b(\vec r_1)\psi_a(\vec r_2)\big],$$

（轨道不正交时归一化为 $[2(1\pm\lvert\langle a\vert b\rangle\rvert^2)]^{-1/2}$，H$_2$ 共价键计算用的正是它。）

**Pauli 不相容原理**是反对称的零行子：令 $a = b$，

$$\Psi_-(\vec r_1,\vec r_2) = \frac{1}{\sqrt2}\big[\psi_a(\vec r_1)\psi_a(\vec r_2) - \psi_a(\vec r_1)\psi_a(\vec r_2)\big] = 0.$$

波函数恒为零，**态不存在**——不是"能量很高"，是根本没有这个态。玻色子一侧取 $a=b$ 完全合法且给出增强因子 2（玻色-爱因斯坦凝聚与受激辐射的根源，见凝聚态书）。

注意精确表述是"两个费米子不能占据同一**包括自旋的单粒子态**（自旋轨道）"。空间轨道相同、自旋相反的两个电子是允许的：$\psi_a(\vec r_1)\psi_a(\vec r_2)\times(\lvert\uparrow_1\downarrow_2\rangle - \lvert\downarrow_1\uparrow_2\rangle)/\sqrt2$ 反对称，合法。于是每个空间亚层 $l$ 的座位数是 $2(2l+1)$：$2l+1$ 个 $m_l$ 方向 $\times$ 2 个自旋投影——第 06 篇周期表记账的地基正是本篇。

## 5. $N$ 个粒子：Slater 行列式

$N$ 个费米子占据轨道 $\{\varphi_{\alpha_1},\cdots,\varphi_{\alpha_N}\}$（$\varphi$ 含自旋），反对称态是**Slater 行列式**：

$$\Psi(\vec x_1,\cdots,\vec x_N) = \frac{1}{\sqrt{N!}}\begin{vmatrix} \varphi_{\alpha_1}(\vec x_1) & \varphi_{\alpha_2}(\vec x_1) & \cdots \\ \varphi_{\alpha_1}(\vec x_2) & \varphi_{\alpha_2}(\vec x_2) & \cdots \\ \vdots & \vdots & \ddots \end{vmatrix},$$

（$\vec x \equiv (\vec r, m_s)$ 统记坐标与自旋。）三条读法：

- 交换两粒子 = 交换两行 = 行列式变号——反对称自动内置；
- 两轨道相同 = 两列相同 = 行列式为零——Pauli 原理自动内置；
- 行列式按行展开的 $N!$ 项正是 $\sum_P (-1)^P\prod_i\varphi_{\alpha_i}(\vec x_{Pi})$——第 09 篇开篇引用的正是这个形式，那里将说明它在 $N$ 大时如何指数爆炸，从而逼出二次量子化。

玻色子的对应物是**积和式**（permanent，行列式去掉全部 $(-1)^P$ 因子）。

关于"$\pm 1$ 之外没有别的选择"：要求 $|\Psi\rangle$ 是**每一个**置换算符的本征态，本征值集合 $\chi(P)$ 就构成群 $S_N$ 的一维表示。$S_3$ 的一维表示只有平庸（全 $+1$）与交替（按置换奇偶 $\pm 1$）两个（自检问题 5）——其余表示（如二维标准表示）会把置换后的态映到别的态上，破坏"全同"的可操作含义。自然界只见到玻色/费米两族。

## 6. 两电子的自旋：单态与三重态

两个自旋 1/2 的自旋空间 $\mathbb C^2\otimes\mathbb C^2$ 按总自旋分解（第 05 篇第 6 节 CG 系数的特例 $1/2\otimes1/2 = 1\oplus0$）：

| 态 | $S, M$ | 自旋波函数 | 交换对称性 |
| --- | --- | --- | --- |
| 三重态 $\lvert t_+\rangle$ | $1, +1$ | $\lvert\uparrow\uparrow\rangle$ | 对称 |
| 三重态 $\lvert t_0\rangle$ | $1, 0$ | $(\lvert\uparrow\downarrow\rangle + \lvert\downarrow\uparrow\rangle)/\sqrt2$ | 对称 |
| 三重态 $\lvert t_-\rangle$ | $1, -1$ | $\lvert\downarrow\downarrow\rangle$ | 对称 |
| 单态 $\lvert s\rangle$ | $0, 0$ | $(\lvert\uparrow\downarrow\rangle - \lvert\downarrow\uparrow\rangle)/\sqrt2$ | **反对称** |

单态是**各向同性的**（$S=0$，任何方向测都是零），也是最大纠缠态——第 14 篇（[测量、EPR 与 Bell](14-measurement-epr-bell.md)）里唱主角的正是它。

电子是费米子，**总**波函数必须反对称，于是空间部分与自旋部分被锁死：

$$\Psi_{\rm total} = \Psi_{\rm space}^{\rm 对称}\otimes\lvert s\rangle \quad\text{或}\quad \Psi_{\rm space}^{\rm 反对称}\otimes\lvert t_{M}\rangle.$$

**同一个空间构型，自旋单态与三重态对应不同的空间对称性，因而有不同的库仑能量**——下一节把这句话变成公式。

## 7. 交换作用：Pauli 原理的第一份"工资"

设置：两个电子分别占据正交轨道 $\psi_a,\psi_b$（如激发态氦的 $1s\,2s$，或 H$_2$ 的两个原子轨道组合），库仑排斥 $V = e^2/r_{12}$。空间部分由第 4 节的 $\Psi_\pm$ 给出。直接计算（自检问题 4）：

$$\langle V\rangle_\pm = K \pm J,$$

其中

$$K = \iint \lvert\psi_a(\vec r_1)\rvert^2\,\lvert\psi_b(\vec r_2)\rvert^2\,\frac{e^2}{r_{12}}\;{\rm d}^3r_1{\rm d}^3r_2 \quad(\text{直接积分：两团电荷云的经典排斥})，$$

$$J = \iint \psi_a^*(\vec r_1)\psi_b^*(\vec r_2)\,\frac{e^2}{r_{12}}\,\psi_b(\vec r_1)\psi_a(\vec r_2)\;{\rm d}^3r_1{\rm d}^3r_2 \quad(\text{交换积分：纯量子，无经典对应}).$$

对实轨道与排斥势 $J > 0$。代入第 6 节的锁定关系（空间对称 $\leftrightarrow$ 自旋单态）：

$$E_{\rm 单态} = K + J, \qquad E_{\rm 三重态} = K - J \qquad (J>0 \Rightarrow \text{三重态低 } 2J).$$

把它改写成自旋哈密顿量：用 $\vec s_1\cdot\vec s_2$ 的本征值 $-3/4$（单态）与 $+1/4$（三重态），

$$\boxed{\ H_{\rm eff} = {\rm const} - 2J\,\vec s_1\cdot\vec s_2\ }$$

这就是 **Heisenberg 交换耦合**。三点必须说清：

1. **没有新的力**。$J$ 来自库仑排斥 + 反对称化，"交换力"是对称性强加的记账，不是第六种相互作用。
2. **$J$ 的符号决定磁性倾向**：$J>0$ 三重态（平行自旋）能量低——Hund 第一规则（同壳层内自旋尽量平行）与局域磁矩的起点；巡游电子铁磁体（真实的铁）的完整故事见凝聚态书[磁性](../../condensed-matter/docs/07-magnetism.md)与[第 07s 篇：铁为什么是铁磁体](../../condensed-matter/docs/07s-why-iron-magnetic.md)。
3. **基态氦用不上它**：两个电子同占 $1s$，空间波函数只能对称，自旋必为单态（"仲氦"）；三重态（"正氦"）要求空间反对称，能量更高——$1s\,2s$ 组态的两条谱线（单态线与三重态线）是原子光谱里交换分裂的最干净展示。

第 07s2 篇会从另一头碰同一堵墙：Slater 行列式展开收敛慢的病根之一就是波函数没写进 $r_{12}$，而"显关联"正是对行列式语言的救赎。

## 8. 接口：这套记账往后通到哪里

- **第 06 篇（氢原子与亚层）**：$2(2l+1)$ 座位、Madelung 填充——本篇是它的前置。
- **第 09 篇（二次量子化）**：Fock 空间 = 把对称/反对称子空间换成产生湮灭算符的语言，本篇的 $N!$ 灾难在那里痊愈。
- **第 08s 篇（散射形式理论）**：全同粒子的散射截面必须对末态做（反）对称化——Mott 散射、电子-电子散射。
- **第 14 篇（EPR 与 Bell）**：自旋单态是最大纠缠态，Bell 实验的标准载体。
- **凝聚态书**：磁性（交换作用的多体展开）、超流 ${}^4$He 与 ${}^3$He 的统计差异、泡利不相容压力与简并物质。

## 小结

| 概念 | 内容 | 后果 |
| --- | --- | --- |
| 交换简并 | $[P_{12},H]=0$ 但薛定谔方程挑不出组合 | 需要新公设 |
| 对称化公设 | 玻色子取 $\mathrm{Sym}^N$，费米子取 $\wedge^N$ | 自旋-统计对应（QFT 证明） |
| Pauli 不相容 | 反对称态在 $a=b$ 时恒为零 | 周期表座位账本 $2(2l+1)$ |
| Slater 行列式 | $N!$ 项打包反对称与 Pauli | $N$ 大时爆炸 → 二次量子化 |
| 单态/三重态 | 自旋反对称配空间对称（反之亦然） | 氦的仲/正两族 |
| 交换作用 | $H_{\rm eff} = {\rm const} - 2J\vec s_1\cdot\vec s_2$ | 铁磁性的量子根源（无新力） |

一句话收束：全同性不是标签游戏，而是一条把态空间砍半的公设；费米子的那一半在砍掉"两个电子同态"的同时，顺手把库仑能变成自旋的函数——物质的结构（周期表）与物质的磁性（交换作用）都从这一刀开始。

## 自检问题

**1.** 证明 $P_{12}$ 幺正、厄米、$P_{12}^2=\mathbb 1$ 且与全同粒子哈密顿对易；由此说明本征值为何只能取 $\pm 1$，以及为什么可观测量的概率解释强制 $\lvert\Psi(\vec r_1,\vec r_2)\rvert^2 = \lvert\Psi(\vec r_2,\vec r_1)\rvert^2$ 对物理态成立。

<details markdown="1"><summary>点击显示答案</summary>

幺正性：$\langle P\phi\vert P\psi\rangle = \iint \phi^*(\vec r_2,\vec r_1)\psi(\vec r_2,\vec r_1)\,{\rm d}^3r_1{\rm d}^3r_2$，换积分变量名 ($\vec r_1\leftrightarrow\vec r_2$，雅可比为 1) 得 $\iint\phi^*(\vec r_1,\vec r_2)\psi(\vec r_1,\vec r_2) = \langle\phi\vert\psi\rangle$——内积不变。厄米性：同理 $\langle\phi\vert P\psi\rangle = \iint\phi^*(\vec r_1,\vec r_2)\psi(\vec r_2,\vec r_1) = \langle P\phi\vert\psi\rangle$。$P^2 = \mathbb 1$ 显然（换两次回来）。厄米算符本征值实；$P^2=1$ 把它们限制在 $\pm1$。

对易：$H = h(1)+h(2)+V(\lvert\vec r_1-\vec r_2\rvert)$，$(PH P\Psi)(\vec r_1,\vec r_2) = H(\vec r_2,\vec r_1)\Psi(\vec r_2,\vec r_1)$，而 $h(\vec r_2)+h(\vec r_1) = h(\vec r_1)+h(\vec r_2)$、$\lvert\vec r_2-\vec r_1\rvert = \lvert\vec r_1-\vec r_2\rvert$，故 $PHP = H$，即 $[P,H]=0$。

概率密度对称性：若 $P\Psi = \pm\Psi$（公设选定），则 $\lvert\Psi(\vec r_2,\vec r_1)\rvert = \lvert\pm\Psi(\vec r_1,\vec r_2)\rvert$，模方相等。反过来讲物理：探测器对编号一无所知，"$\vec r_1$ 处与 $\vec r_2$ 处各有一个粒子"的事件在两种标签下是同一事件，概率必须一致——对称化公设正是让理论自动满足这一致性的最经济方案。

</details>

**2.** 从反对称两粒子态出发推出 Pauli 不相容原理；并说明为什么两个电子同占一个空间轨道、自旋却相反是允许的。

<details markdown="1"><summary>点击显示答案</summary>

取 $\psi_a = \psi_b$：$\Psi_- = [\psi_a(1)\psi_a(2) - \psi_a(1)\psi_a(2)]/\sqrt2 \equiv 0$。零矢量不归一、不是任何态——"两个费米子同一自旋轨道"的态不存在。这比"能量无穷大"更强：是对态空间本身的删减。

同轨道反自旋：单粒子态要连自旋一起数。取 $\varphi_1 = \psi_a\lvert\uparrow\rangle$、$\varphi_2 = \psi_a\lvert\downarrow\rangle$，二者**不同**（自旋正交），Slater 行列式

$$\Psi = \frac{1}{\sqrt2}\psi_a(\vec r_1)\psi_a(\vec r_2)\big[\lvert\uparrow_1\downarrow_2\rangle - \lvert\downarrow_1\uparrow_2\rangle\big]$$

不为零：空间部分对称（两因子相同），自旋部分是单态（反对称），乘积反对称——合法。这正是氦基态的构型，也是每个亚层 $2(2l+1)$ 个座位中"×2"的来源。

</details>

**3.** 从 $\lvert\uparrow\uparrow\rangle$ 出发用总自旋升降算符构造三重态 $m=0$ 分量，再验证单态 $(\lvert\uparrow\downarrow\rangle-\lvert\downarrow\uparrow\rangle)/\sqrt2$ 是 $\vec S^2$ 的零本征值本征态。

<details markdown="1"><summary>点击显示答案</summary>

记 $S_\pm = S_{1\pm}+S_{2\pm}$，作用规则 $S_-\lvert\uparrow\rangle = \hbar\lvert\downarrow\rangle$。$\lvert t_+\rangle = \lvert\uparrow\uparrow\rangle$ 是 $S_z$ 本征值 $\hbar$ 的最大权态，必为三重态。用 CG 递推：

$$S_-\lvert\uparrow\uparrow\rangle = \hbar(\lvert\downarrow\uparrow\rangle + \lvert\uparrow\downarrow\rangle).$$

另一方面三重态满足 $S_-\lvert 1,1\rangle = \hbar\sqrt{1(1+1)-1\cdot0}\,\lvert1,0\rangle = \hbar\sqrt2\,\lvert1,0\rangle$，比较得

$$\lvert t_0\rangle = \frac{\lvert\uparrow\downarrow\rangle + \lvert\downarrow\uparrow\rangle}{\sqrt2}.$$

单态 $\lvert s\rangle = (\lvert\uparrow\downarrow\rangle - \lvert\downarrow\uparrow\rangle)/\sqrt2$：先看 $S_z\lvert s\rangle = 0$；再算 $S_+\lvert s\rangle = \hbar(\lvert\uparrow\uparrow\rangle - \lvert\uparrow\uparrow\rangle) = 0$，同理 $S_-\lvert s\rangle = 0$。于是 $\vec S^2 = S_z^2 + \frac12(S_+S_- + S_-S_+)$ 作用给出零：$\vec S^2\lvert s\rangle = 0\cdot\hbar^2\lvert s\rangle$，确为 $S=0$。对称性判别：$P_{12}$ 交换两格自旋，$\lvert t_0\rangle$ 不变（对称），$\lvert s\rangle$ 变号（反对称）——与第 6 节的锁定关系一致。

</details>

**4.** 对 $\Psi_\pm = [\psi_a(1)\psi_b(2)\pm\psi_b(1)\psi_a(2)]/\sqrt2$（$\langle a\vert b\rangle = 0$）计算 $\langle V\rangle_\pm = K\pm J$，写出 $K$ 与 $J$ 的表达式；再利用 $\vec s_1\cdot\vec s_2$ 的本征值把两个能量打包成 $H_{\rm eff} = {\rm const} - 2J\vec s_1\cdot\vec s_2$，并说明 $J>0$ 时基态自旋如何取。

<details markdown="1"><summary>点击显示答案</summary>

展开 $\lvert\Psi_\pm\rvert^2$（取实轨道，复数时 $J\to$ 共轭配对，结果同样成立）：

$$\lvert\Psi_\pm\rvert^2 = \tfrac12\big[\lvert\psi_a(1)\psi_b(2)\rvert^2 + \lvert\psi_b(1)\psi_a(2)\rvert^2 \pm 2\psi_a(1)\psi_b(2)\psi_b(1)\psi_a(2)\big].$$

前两项代入场论对称性（积分变量换名后相等）给出 $K$；交叉项给出 $\pm J$：

$$\langle V\rangle_\pm = \underbrace{\iint \lvert\psi_a(1)\rvert^2\lvert\psi_b(2)\rvert^2\frac{e^2}{r_{12}}}_{K}\ \pm\ \underbrace{\iint \psi_a(1)\psi_b(2)\frac{e^2}{r_{12}}\psi_b(1)\psi_a(2)}_{J}.$$

$K$ 是两团电荷密度分布的经典静电排斥能；$J$ 无经典对应——被积函数像"两个电子互换身份再重叠"。

打包：空间对称（$+$）配自旋单态（$\vec s_1\cdot\vec s_2 = -3/4$），空间反对称（$-$）配三重态（$+1/4$），要求 $c_0 + c_1(-3/4) = K+J$、$c_0 + c_1(1/4) = K-J$，解得 $c_1 = -2J$、$c_0 = K - J/2$。故 $H_{\rm eff} = (K - J/2) - 2J\vec s_1\cdot\vec s_2$，自旋依赖部分即 Heisenberg 形式。

$J>0$ 时三重态（$K-J$）低于单态（$K+J$），差 $2J$：基态取**平行自旋**——这正是 Hund 第一规则（交换通道上自旋平行省库仑能），也是局域磁矩/铁磁倾向的微观机制（多体版本见凝聚态书磁性章）。

</details>

**5.** 证明 $S_3$ 的对换互不对易（如 $(12)(13)\ne(13)(12)$）；进而证明：若 $|\Psi\rangle$ 是全部六个置换算符的共同本征态，本征值只能取"全 $+1$"或"按奇偶 $\pm1$"两套；说明为什么二维表示（副统计）不满足这个条件。

<details markdown="1"><summary>点击显示答案</summary>

复合置换从右往左作用。$(12)(13)$：$1\to 3\to 3$，$3\to 1\to 2$，$2\to 2\to 1$，即循环 $(132)$。$(13)(12)$：$1\to2\to2$，$2\to1\to3$，$3\to3\to1$，即 $(123)$。$(132)\ne(123)$（后者把 1 送到 2，前者送到 3），故对换不对易，$S_3$ 非阿贝尔。

设 $P|\Psi\rangle = \chi(P)|\Psi\rangle$，$\chi(P) = \pm1$（每个 $P$ 都满足 $P^2 = e$... 三阶循环满足 $P^3=e$，本征值是三次根；但由 $P|\Psi\rangle$ 共线与 $\chi((123)) = \chi((13))\chi((12)) = \chi(12)^2\chi(13)^0$——具体地 $(123) = (13)(12)$，故 $\chi((123)) = \chi(13)\chi(12) = (\pm1)(\pm1) = \pm1$，同时三次根中实的只有 $\pm1$，自洽）。于是 $\chi$ 是群同态 $S_3\to\{\pm1\}$。对换只有两类（$(12),(13),(23)$ 互相共轭：$(13) = (23)(12)(23)$），同态要求共轭元素同值，全部对换一个值 $\varepsilon = \pm1$：

- $\varepsilon = +1$：平庸表示，$\chi\equiv1$（玻色子）；
- $\varepsilon = -1$：交替表示，$\chi(P) = (-1)^{P}$（费米子）。

只有这两套。二维标准表示下，对换把 $|\Psi\rangle$ 映到**另一个独立的**矢量（二维空间里旋转/反射），交换产生可分辨的新态——"全同"失效；自然界没有发现对应粒子（"副统计"），非阿贝尔统计只在二维激发（任意子）中以推广形式出现，见凝聚态书[分数量子霍尔](../../condensed-matter/docs/11s-fractional-quantum-hall.md)。

</details>

## 参考

- Griffiths《量子力学概论》第 5 章（全同粒子）——对称化公设与交换作用的标准入门。
- Shankar《Principles of Quantum Mechanics》第 10 章（Systems of Identical Particles）——包括积和式与统计的讨论。
- Cohen-Tannoudji《量子力学》第 XIV 章（全同粒子体系）——最详尽。
- 朗道《量子力学》全同粒子一节——从不可分辨性出发的极简论证。
- 凝聚态书[磁性](../../condensed-matter/docs/07-magnetism.md)（交换作用的多体展开）与[第 07s 篇](../../condensed-matter/docs/07s-why-iron-magnetic.md)（巡游铁磁体）。
