# 补充材料：不解微分方程的氢原子——Runge–Lenz 矢量、SO(4) 与 Pauli 的矩阵力学解

> 路线图位置：量子力学书 · 第二部分（可精确求解的体系）· 第 06s 篇（接[第 06 篇 氢原子与电子亚层](06-hydrogen-and-subshells.md)之后）
> 前置知识：第 05 篇第 2–3 节（角动量对易关系、Casimir、升降算符——本篇的全部工具）与第 6 节（角动量相加）；[第 01 篇 旧量子论](01-old-quantum-theory.md)（历史背景：Balmer 公式与玻尔–索末菲模型）；[第 04 篇 谐振子的产生/湮灭算符解法](04-harmonic-oscillator-ladder.md)第 3 节（纯代数解出能谱的第一个范例）。
> 学习目标：知道 1925–1926 年矩阵力学要解决什么问题、Pauli 为什么能抢在薛定谔之前交出 Balmer 谱；记住量子 Runge–Lenz 矢量的定义、对称化次序的必要性与 $[H, \vec A] = 0$、$\vec L\cdot\vec A = 0$ 两条基本性质；会推 $[L_i, A_j]$ 与 $[A_i, A_j]$ 的闭合代数；会把束缚态子空间上的代数重标度成 $\mathrm{so}(4) = \mathrm{su}(2)\oplus\mathrm{su}(2)$，从 Casimir 与约束推出 $E_n = -13.6\ \mathrm{eV}/n^2$ 与 $n^2$ 简并——全程不解任何微分方程。
>
> 记号约定：本篇保留 $\hbar$（与第 05 篇一致）。库仑耦合常数简记 $k \equiv Ze^2/(4\pi\varepsilon_0)$（量纲为能量×长度），$m_e$ 为电子质量（折合质量近似），$\varepsilon_{ijk}$ 为全反对称符号（$\varepsilon_{123} = +1$），重复指标求和。

---

## 1. 一句话总结

**氢原子的能谱根本不需要解微分方程：库仑势除了旋转对称性外还藏着第二个守恒量——Runge–Lenz 矢量 $\vec A$，它与角动量 $\vec L$ 的六个分量在束缚态子空间上闭合成 so(4) 李代数，而 so(4) 不过是两个独立的 su(2)；氢原子的第 $n$ 个能级就是 su(2)$\oplus$su(2) 的 $(j, j)$ 不可约表示，维数 $(2j+1)^2 = n^2$ 自动给出简并度，Casimir 本征值自动给出 $E_n \propto -1/n^2$——1926 年 1 月 Pauli 用这套纯对易关系的矩阵力学推出了 Balmer 公式，比薛定谔的波动力学论文还早投稿十天。**

## 2. 矩阵力学：只有对易关系的量子力学

1925 年 7 月 Heisenberg 提交了一篇奇怪的文章（Z. Phys. 33, 879）：他主张抛弃电子轨道这种不可观测的对象，只保留光谱学真正测量的东西——跃迁频率与强度，把它们组织成两张"表"。Born 几天后认出这些表就是数学里的**矩阵**，表的乘法规则正是不对易的矩阵乘法。到 1925 年秋（Born–Jordan 论文与三人合作的"Dreimännerarbeit"），新力学已经成型，其全部内容为三条：

- 可观测量是厄米矩阵（算符），坐标与动量满足基本对易关系
  $$[x_i, p_j] = i\hbar\,\delta_{ij};$$
- 运动方程是算符方程
  $$\dot O = \frac{i}{\hbar}[H, O]$$
  （这就是后来所谓的海森堡绘景）；
- 定态问题 = 把哈密顿矩阵 $H$ 对角化，对角元就是能级。

注意这份清单里**没有波函数、没有微分方程**——整个理论只需要对易关系。这立刻引出一个尖锐的检验：旧量子论（见[第 01 篇](01-old-quantum-theory.md)）用玻尔–索末菲条件能凑出氢的 Balmer 谱，但那套规则本质上只适用于可分离变量的周期系统，连氦原子都对付不了。**矩阵力学能不能只用对易关系推出氢原子能谱？** Pauli 在 1926 年 1 月 17 日交出了答案（Z. Phys. 36, 336）——而薛定谔波动力学的第一篇论文 1 月 27 日才投稿。矩阵力学先拿到了 Balmer 公式。

Pauli 的秘密武器是一个经典力学里早就知道、但一直被当成奇技淫巧的守恒量：Runge–Lenz 矢量。

## 3. 量子 Runge–Lenz 矢量

### 3.1 经典回顾：椭圆轨道为什么不进动

经典开普勒问题 $H = p^2/2m_e - k/r$ 中，除了角动量 $\vec L$（守恒 ⟺ 轨道平面固定），还有一个守恒矢量

$$\vec A_{\mathrm{cl}} = \frac{1}{m_e}\,\vec p\times\vec L - k\,\hat r,$$

它沿轨道长轴指向**近日点**，大小正比于偏心率。$\vec A_{\mathrm{cl}}$ 守恒 ⟺ 近日点方向不动 ⟺ 轨道闭合。Bertrand 定理说：能让一切束缚轨道都闭合的中心势只有 $1/r$ 与 $r^2$ 两种——Runge–Lenz 守恒是库仑势（和谐振子）的专属财产，这就是"隐藏对称性"的经典形态。

### 3.2 量子化：对称化不是小事

把 $\vec p\times\vec L$ 直接换成算符会出问题：$\vec p$ 与 $\vec L$ 不对易，$(\vec p\times\vec L)^\dagger = -\vec L\times\vec p \neq \vec p\times\vec L$，不是厄米算符，不能当可观测量。补救办法是取对称化组合——**量子 Runge–Lenz 矢量**

$$\boxed{\;\vec A = \frac{1}{2m_e}\big(\vec p\times\vec L - \vec L\times\vec p\big) - k\,\hat r\;}$$

利用 $[p_j, L_k] = -i\hbar\varepsilon_{kjm}p_m$ 做指标收缩可得 $\vec p\times\vec L = -\vec L\times\vec p + 2i\hbar\,\vec p$，于是有等价形式

$$\vec A = \frac{1}{m_e}\big(\vec p\times\vec L - i\hbar\,\vec p\big) - k\,\hat r,$$

其中那项 $-i\hbar\vec p$ 正是对称化的残骸：少了它 $\vec A$ 不厄米，后面的闭合代数也会留下洗不掉的残渣（第 4.3 节会再看到它立功）。

### 3.3 两条基本性质

**守恒**：直接（但冗长）的对易子计算给出

$$[H, \vec A] = 0,$$

即 $\vec A$ 的三个分量都是运动常数——这正是经典 $\dot{\vec A}_{\mathrm{cl}} = 0$ 的量子版本。于是束缚态子空间里有六个守恒量：$\vec L$ 三个、$\vec A$ 三个。

**与角动量正交**：

$$\vec L\cdot\vec A = \vec A\cdot\vec L = 0$$

（证明是纯 $\varepsilon$ 恒等式体操，留作自检问题 1）。经典对应：$\vec A_{\mathrm{cl}}$ 躺在轨道平面内，而 $\vec L$ 垂直于轨道平面。这条约束在第 5 节会把两个 su(2) 的量子数锁成相等，是整篇算账的枢轴之一。

## 4. 闭合代数：六个守恒量生成 so(4)

### 4.1 前两个对易子

$[L_i, L_j] = i\hbar\varepsilon_{ijk}L_k$ 是第 05 篇的老结果。第二个对易子

$$[L_i, A_j] = i\hbar\varepsilon_{ijk}A_k$$

说的是**$\vec A$ 是矢量算符**——它在旋转下像矢量一样变换。这是必然：$\vec A$ 由 $\vec r$、$\vec p$、$\vec L$ 这些矢量拼成，而任何由矢量拼出的矢量都满足这条代数（验证一个分量留作自检问题 2）。

### 4.2 第三个对易子：$[A_i, A_j]$ 的关键步骤

这是最费劲的一步，先看结构。用 $\varepsilon$ 收缩与 $[p_j, x_i] = -i\hbar\delta_{ij}$ 可证恒等式 $(\vec p\times\vec L)_i = x_i p^2 - (\vec p\cdot\vec x)\,p_i - i\hbar p_i$，代入 3.2 节的等价形式，把 $\vec A$ 完全写成 $\vec x, \vec p$ 的多项式：

$$A_i = \frac{1}{m_e}\Big(x_i p^2 - (\vec p\cdot\vec x)\,p_i - 2i\hbar\,p_i\Big) - k\,\frac{x_i}{r}.$$

计算 $[A_i, A_j]$ 只需要基本对易关系及其推论 $[p_i, f(\vec r)] = -i\hbar\,\partial_i f$（特别是 $[p_i, 1/r] = i\hbar x_i/r^3$）。展开后的几十项分成三类：

- **动能×动能**：第一项内部的对易子，全部归于正比于 $\varepsilon_{ijk}L_k p^2$ 的结构；
- **动能×势能**：含 $1/r$、$1/r^2$、$1/r^3$ 的项。$1/r^3$ 项成对相消，$1/r^2$ 项恰好被对称化带来的 $-2i\hbar\vec p$ 的贡献抵消——次序对称化在这里第二次立功；
- **势能×势能**：$[x_i/r,\, x_j/r] = 0$，恒为零。

全部收拾干净后，剩下的项以 $H = p^2/2m_e - k/r$ 重新合并，得到

$$\boxed{\;[A_i, A_j] = -\frac{2i\hbar}{m_e}\,\varepsilon_{ijk}\,L_k H\;}$$

（因 $[H, L_k] = 0$，右边 $L_k$ 与 $H$ 的次序无所谓）。量纲自查：$A$ 的量纲是"能量×长度"，$[A_i, A_j] \sim (\text{能量}\times\text{长度})^2$；右边 $\hbar L_k H/m_e \sim \hbar^2 E/m_e \sim (\text{能量}\times\text{长度})^2$，一致。

**结构点评**：这个对易子的特别之处在于右边含有 $H$ 本身——代数不是在全希尔伯特空间上朴素地闭合，而是"带着能量标签"闭合。这正是下一步的动机：限制到一个能量本征子空间上，$H$ 变成数，代数才真正封闭。

## 5. 束缚态子空间：so(4) = su(2)⊕su(2) 与 Balmer 谱

### 5.1 重标度出 so(4)

取 $H$ 的某个束缚态本征子空间（$E < 0$），在其上 $H$ 就是数 $E$。定义重标度的 Runge–Lenz 矢量

$$\vec M \equiv \sqrt{-\frac{m_e}{2E}}\;\vec A \qquad (E < 0,\ \text{根号为正实数}),$$

则（自检问题 3）

$$[L_i, L_j] = i\hbar\varepsilon_{ijk}L_k, \qquad [L_i, M_j] = i\hbar\varepsilon_{ijk}M_k, \qquad [M_i, M_j] = i\hbar\varepsilon_{ijk}L_k.$$

六个生成元、三组结构常数全同构——这正是四维旋转群的李代数 **so(4)**（六个生成元对应四维空间的六个旋转平面）。库仑束缚态的隐藏对称性至此完全显形。

### 5.2 拆成两个 su(2)

so(4) 有个其他正交群没有的特殊性质：它是两个 su(2) 的直和。定义

$$\vec J_\pm \equiv \frac{1}{2}\big(\vec L \pm \vec M\big),$$

直接代入上面的对易关系（自检问题 3）：

$$[J_{+i}, J_{+j}] = i\hbar\varepsilon_{ijk}J_{+k}, \qquad [J_{-i}, J_{-j}] = i\hbar\varepsilon_{ijk}J_{-k}, \qquad [J_{+i}, J_{-j}] = 0,$$

即 $\vec J_+$ 与 $\vec J_-$ 各自是一套独立的角动量代数，且互相对易：so(4) = su(2) $\oplus$ su(2)。于是本征态可以贴两对角动量标签 $(j_+, j_-)$，每个 $j$ 按第 05 篇第 3 节的代数取 $0, \tfrac12, 1, \dots$，表示维数 $(2j_+ + 1)(2j_- + 1)$。

### 5.3 约束：两个量子数必须相等

物理的旋转生成元只有 $\vec L = \vec J_+ + \vec J_-$，$\vec J_\pm$ 单独并不是可观测的角动量——它们只是记账工具。记账工具有一个必须满足的红线，即 3.3 节的约束 $\vec L\cdot\vec A = 0$（从而 $\vec L\cdot\vec M = 0$）：

$$J_+^2 - J_-^2 = \frac{1}{4}\big(L^2 + M^2 + 2\vec L\cdot\vec M\big) - \frac{1}{4}\big(L^2 + M^2 - 2\vec L\cdot\vec M\big) = \vec L\cdot\vec M = 0,$$

所以 $J_+^2 = J_-^2$，即

$$j_+ = j_- \equiv j, \qquad \text{表示维数}\ (2j+1)^2.$$

氢原子的第 $j$ 个能级承载 su(2)$\oplus$su(2) 的 $(j, j)$ 不可约表示。（允许半整数 $j$ 出现，因为 $\vec J_\pm$ 不是物理旋转；物理的 $\vec L$ 只会合成出整数 $l$，见下。）

### 5.4 Casimir 算账：能级出来了

还差一个把 $\vec A$ 与 $H$ 直接挂钩的恒等式。把 $A^2$ 用 4.2 节的展开式硬算（同样是 $\varepsilon$ 体操），得

$$\boxed{\;A^2 = \frac{2H}{m_e}\big(L^2 + \hbar^2\big) + k^2\;}$$

对照经典版本 $A_{\mathrm{cl}}^2 = 2EL^2/m_e + k^2$：量子情形多出一项 $\hbar^2$，这是算符次序修正，也正是它让下面 $n$ 从 1 而不是从 0 开始数。

在能量为 $E$ 的子空间上，$M^2 = -\frac{m_e}{2E}A^2 = -(L^2 + \hbar^2) - \frac{m_e k^2}{2E}$，于是

$$J_+^2 + J_-^2 = \frac{1}{2}\big(L^2 + M^2\big) = -\frac{\hbar^2}{2} - \frac{m_e k^2}{4E}.$$

左边在两个 su(2) 里的本征值是 $2j(j+1)\hbar^2$，右边解出 $E$：

$$-\frac{m_e k^2}{4E} = 2j(j+1)\hbar^2 + \frac{\hbar^2}{2} = \frac{\hbar^2}{2}(2j+1)^2 \quad\Longrightarrow\quad E = -\frac{m_e k^2}{2\hbar^2(2j+1)^2}.$$

令 $n \equiv 2j + 1$，则 $j = 0, \tfrac12, 1, \dots$ 恰好给出 $n = 1, 2, 3, \dots$，代回 $k = Ze^2/(4\pi\varepsilon_0)$：

$$E_n = -\frac{m_e}{2\hbar^2}\left(\frac{Ze^2}{4\pi\varepsilon_0}\right)^2\frac{1}{n^2} = -\frac{Z^2 \times 13.6\ \mathrm{eV}}{n^2}, \qquad \text{简并度}\ (2j+1)^2 = n^2\ (\text{不含自旋}).$$

**Balmer 谱从对易关系里长出来了**——没有波函数、没有径向方程、没有级数截断。

### 5.5 白捡的奖品：$l$ 的内容也对上了

这套代数不止给简并度，连每个能级里有哪几个 $l$ 都一并给出。物理角动量 $\vec L = \vec J_+ + \vec J_-$ 是两个 $j$ 的合成（第 05 篇第 6 节的机器）：

$$j \otimes j = 0 \oplus 1 \oplus \cdots \oplus 2j \quad\Longrightarrow\quad l = 0, 1, \dots, n-1,\ \text{每个恰好一次},$$

与[第 06 篇](06-hydrogen-and-subshells.md)第 2.2 节"截断条件 $n = n_r + l + 1$、$n_r \ge 0$"给出的 $l$ 范围完全一致，且 $\sum_{l=0}^{n-1}(2l+1) = n^2 = (2j+1)^2$。两种语言逐字互译：$n_r = n - l - 1$ 在代数这边对应"CG 分解中第 $l$ 个通道的序号"。

## 6. 对照与遗产

| 条目 | 波动力学（第 06 篇） | 矩阵力学（本篇） |
| --- | --- | --- |
| 出发点 | 薛定谔方程 + 束缚态边界条件 | 对易关系 + Runge–Lenz 守恒 |
| $n$ 的来历 | 径向级数截断，$n = n_r + l + 1$ | so(4) 表示标签，$n = 2j + 1$ |
| 能级 | $E_n = -Z^2 \times 13.6\ \mathrm{eV}/n^2$ | 同左 |
| 简并度 | $\sum_{l=0}^{n-1}(2l+1) = n^2$ | $(2j+1)^2 = n^2$ |
| $l$ 的取值 | 由 $n_r \ge 0$ 得 $l \le n - 1$ | $j \otimes j = 0 \oplus \cdots \oplus 2j$ |
| 波函数 | $R_{nl}(r)Y_l^m$ 显式可得 | 不提供（需另造坐标表象） |

三条遗产：

- **兑现承诺**：[第 06 篇](06-hydrogen-and-subshells.md)第 2.3 节说"$l$ 简并来自隐藏 SO(4) 对称性"，本篇把这句话算完了：简并不是径向方程的数值巧合，而是 $(j, j)$ 表示的维数，是表示论的必然。势偏离 $1/r$（多电子屏蔽）就毁掉 $\vec A$ 的守恒，$l$ 简并当即消失——对称性解释自动预言了简并的脆弱性。
- **方法论**：本篇与[谐振子代数解法](04-harmonic-oscillator-ladder.md)是同一哲学的两次演示——量子力学的深层结构装在对易代数里，波函数只是某个表象里的投影。海森堡绘景的运动方程 $\dot O = (i/\hbar)[H, O]$ 后来原样搬进量子场论，是场算符演化的标准语言。
- **矩阵力学缺什么**：它给出能级与简并，但不"自动"给出波函数和跃迁矩阵元的空间结构——Pauli 当年也算出了 Balmer 谱线强度，但远不如波动力学顺手。1926 年 3 月薛定谔证明两种力学在数学上等价，此后物理教科书普遍先教波动力学，而把代数解法当作"进阶技巧"。就理解对称性而言，次序应该反过来。

## 小结

- 矩阵力学（Heisenberg 1925）的全部输入是 $[x_i, p_j] = i\hbar\delta_{ij}$ 与 $\dot O = (i/\hbar)[H, O]$；Pauli 1926 年用它率先推出 Balmer 谱。
- 量子 Runge–Lenz 矢量 $\vec A = \tfrac{1}{2m_e}(\vec p\times\vec L - \vec L\times\vec p) - k\hat r$ 需要对称化才厄米；满足 $[H, \vec A] = 0$、$\vec L\cdot\vec A = 0$。
- 闭合代数：$[L_i, A_j] = i\hbar\varepsilon_{ijk}A_k$，$[A_i, A_j] = -\tfrac{2i\hbar}{m_e}\varepsilon_{ijk}L_k H$；右边带 $H$ 是重标度的动机。
- 束缚态上 $\vec M = \sqrt{-m_e/2E}\,\vec A$ 与 $\vec L$ 生成 so(4)；$\vec J_\pm = (\vec L \pm \vec M)/2$ 把它拆成两个对易的 su(2)。
- 约束 $\vec L\cdot\vec A = 0$ 锁定 $j_+ = j_- = j$；由 $A^2 = \tfrac{2H}{m_e}(L^2 + \hbar^2) + k^2$（注意量子的 $\hbar^2$ 修正）与 Casimir 解出 $n = 2j+1 = 1, 2, \dots$、$E_n = -Z^2 \times 13.6\ \mathrm{eV}/n^2$、简并度 $n^2$，$l = 0, \dots, n-1$ 由 $j \otimes j$ 合成给出。

## 自检问题

**1.** 用 $\varepsilon$ 恒等式证明 $\vec L\cdot\vec A = 0$（即 $\vec L$ 与 $\vec p\times\vec L$、$\vec L\times\vec p$、$\hat r$ 三部分分别正交）。

<details markdown="1"><summary>点击显示答案</summary>

先备两个零件。**零件一**：$\varepsilon_{ijk}L_iL_k = \tfrac12\varepsilon_{ijk}[L_i, L_k] = \tfrac12 i\hbar\,\varepsilon_{ijk}\varepsilon_{ikl}L_l = i\hbar L_j$（用到 $\varepsilon_{ijk}\varepsilon_{ikl} = 2\delta_{jl}$）。**零件二**：$\vec p\cdot\vec L = \varepsilon_{klm}p_kx_lp_m = \varepsilon_{klm}x_lp_kp_m - i\hbar\varepsilon_{klm}\delta_{kl}p_m = 0$（第一项对称×反对称为零，第二项 $\varepsilon_{klm}\delta_{kl} = 0$）；同理 $\vec L\cdot\vec p = \varepsilon_{klm}x_lp_mp_k = 0$。

逐项来：

$$\vec L\cdot(\vec p\times\vec L) = \varepsilon_{ijk}L_ip_jL_k = \varepsilon_{ijk}p_jL_iL_k + i\hbar\,\varepsilon_{ijk}\varepsilon_{ijm}p_mL_k,$$

其中把 $L_i$ 移过 $p_j$ 用了 $L_ip_j = p_jL_i + i\hbar\varepsilon_{ijm}p_m$。第一项由零件一 $= i\hbar\,p_jL_j = i\hbar\,\vec p\cdot\vec L = 0$；第二项 $\varepsilon_{ijk}\varepsilon_{ijm} = 2\delta_{km}$，得 $2i\hbar\,p_kL_k = 0$。

$$\vec L\cdot(\vec L\times\vec p) = \varepsilon_{ijk}L_iL_jp_k = i\hbar L_kp_k = i\hbar\,\vec L\cdot\vec p = 0$$

（用零件一的轮换版本 $\varepsilon_{ijk}L_iL_j = i\hbar L_k$）。

$$\vec L\cdot\hat r = \frac{1}{r}\varepsilon_{ijk}x_jp_kx_i = \frac{1}{r}\varepsilon_{ijk}x_j\big(x_ip_k - i\hbar\delta_{ki}\big) = 0$$

（$x_jx_i$ 对称，$\varepsilon_{ijk}\delta_{ki} = 0$）。三项全为零，故 $\vec L\cdot\vec A = 0$。$\blacksquare$

</details>

**2.** 验证 $[L_i, A_j] = i\hbar\varepsilon_{ijk}A_k$ 的一个分量：$[L_z, A_x] = i\hbar A_y$。

<details markdown="1"><summary>点击显示答案</summary>

写出 $A_x = \tfrac{1}{2m_e}(p_yL_z - p_zL_y - L_yp_z + L_zp_y) - k\,x/r$。需要的零件：$[L_z, p_y] = i\hbar\varepsilon_{zyx}p_x = -i\hbar p_x$，$[L_z, L_y] = -i\hbar L_x$，$[L_z, p_z] = [L_z, L_z] = 0$，$[L_z, x] = i\hbar\varepsilon_{zxy}y = i\hbar y$（$x$ 与 $1/r$ 对易）。逐项：

$$[L_z,\, p_yL_z] = -i\hbar p_xL_z, \qquad [L_z,\, p_zL_y] = -i\hbar p_zL_x,$$

$$[L_z,\, L_yp_z] = -i\hbar L_xp_z, \qquad [L_z,\, L_zp_y] = -i\hbar L_zp_x,$$

$$[L_z,\, -kx/r] = -i\hbar k\,y/r.$$

带上 $A_x$ 中各项的正负号合起来：

$$[L_z, A_x] = \frac{i\hbar}{2m_e}\big(p_zL_x - p_xL_z - L_zp_x + L_xp_z\big) - i\hbar k\,\frac{y}{r}.$$

圆括号正是 $2m_e\big(A_y + k\,y/r\big)$ 的展开，代入后 $y/r$ 项相消：

$$[L_z, A_x] = i\hbar\big(A_y + k\,y/r\big) - i\hbar k\,y/r = i\hbar A_y. \qquad \blacksquare$$

物理含义：$\vec A$ 像矢量一样参与旋转（与 $\vec r$、$\vec p$、$\vec L$ 同一代数行为），所以它在中心势里守恒这件事与旋转对称性自洽。

</details>

**3.** 从 $[A_i, A_j] = -\tfrac{2i\hbar}{m_e}\varepsilon_{ijk}L_kH$ 出发，证明束缚态子空间上 $\vec J_\pm = (\vec L \pm \vec M)/2$ 闭合成两个互相对易的 su(2) 代数。

<details markdown="1"><summary>点击显示答案</summary>

在能量 $E < 0$ 的本征子空间上 $H$ 替换为数 $E$。先算重标度后的对易子：

$$[M_i, M_j] = \Big(-\frac{m_e}{2E}\Big)[A_i, A_j] = \Big(-\frac{m_e}{2E}\Big)\Big(-\frac{2i\hbar}{m_e}\Big)\varepsilon_{ijk}L_k E = i\hbar\varepsilon_{ijk}L_k,$$

而 $[L_i, M_j] = \sqrt{-m_e/2E}\,[L_i, A_j] = i\hbar\varepsilon_{ijk}M_k$（标量因子与 $L_i$ 对易）。于是

$$[J_{+i}, J_{+j}] = \frac{1}{4}\big([L_i, L_j] + [L_i, M_j] + [M_i, L_j] + [M_i, M_j]\big) = \frac{i\hbar}{4}\varepsilon_{ijk}\big(L_k + M_k + M_k + L_k\big) = i\hbar\varepsilon_{ijk}J_{+k}.$$

同理 $[J_{-i}, J_{-j}] = i\hbar\varepsilon_{ijk}J_{-k}$。交叉对易子：

$$[J_{+i}, J_{-j}] = \frac{1}{4}\big([L_i, L_j] - [L_i, M_j] + [M_i, L_j] - [M_i, M_j]\big) = \frac{i\hbar}{4}\varepsilon_{ijk}\big(L_k - M_k + M_k - L_k\big) = 0.$$

两个 su(2) 各自闭合、互相独立，即 so(4) = su(2) $\oplus$ su(2)。$\blacksquare$ 注意关键的符号配合：$[M_i, M_j]$ 必须给出 $+i\hbar\varepsilon_{ijk}L_k$（负能 $E<0$ 把 $[A_i,A_j]$ 里的负号翻正），否则组合不出这种对称拆分——这就是重标度因子里要取 $-m_e/2E > 0$ 的原因；对 $E > 0$ 的散射态，得到的将是 so(3,1) 而非 so(4)。

</details>

**4.** 利用 $A^2 = \tfrac{2H}{m_e}(L^2 + \hbar^2) + k^2$ 与 $J_+^2 = J_-^2 = j(j+1)\hbar^2$，推出 $E_n$、$n = 2j+1$ 的取值范围与简并度，并数值验证 $Z=1$ 的基态能量。

<details markdown="1"><summary>点击显示答案</summary>

在能量为 $E < 0$ 的子空间上：

$$M^2 = -\frac{m_e}{2E}A^2 = -\frac{m_e}{2E}\cdot\frac{2E}{m_e}\big(L^2 + \hbar^2\big) - \frac{m_e k^2}{2E} = -\big(L^2 + \hbar^2\big) - \frac{m_e k^2}{2E}.$$

于是

$$J_+^2 + J_-^2 = \frac{1}{2}\big(L^2 + M^2\big) = -\frac{\hbar^2}{2} - \frac{m_e k^2}{4E}.$$

左边 $= 2j(j+1)\hbar^2$，解出

$$-\frac{m_e k^2}{4E} = 2j(j+1)\hbar^2 + \frac{\hbar^2}{2} = \frac{\hbar^2}{2}\big(4j^2 + 4j + 1\big) = \frac{\hbar^2}{2}(2j+1)^2,$$

即 $E = -\dfrac{m_e k^2}{2\hbar^2(2j+1)^2}$。由 su(2) 表示论 $j = 0, \tfrac12, 1, \tfrac32, \dots$，故 $n \equiv 2j+1$ 取遍 $1, 2, 3, \dots$；$j$ 允许半整数是因为 $\vec J_\pm$ 不是物理旋转，物理角动量 $\vec L = \vec J_+ + \vec J_-$ 的分解 $j \otimes j$ 只含整数 $l$。代回 $k = Ze^2/(4\pi\varepsilon_0)$：

$$E_n = -\frac{m_e}{2\hbar^2}\Big(\frac{Ze^2}{4\pi\varepsilon_0}\Big)^2\frac{1}{n^2}, \qquad \text{简并度}\ (2j+1)^2 = n^2.$$

数值验证（$Z = 1$，$n = 1$）：用 $E_1 = -\tfrac12 m_ec^2\alpha^2$，$m_ec^2 = 511\ \mathrm{keV}$、$\alpha = 1/137.036$：

$$E_1 = -\frac{1}{2}\times 5.11\times10^5\ \mathrm{eV}\times\frac{1}{137.036^2} \approx -13.6\ \mathrm{eV}. \qquad \blacksquare$$

</details>

**5.** 对 $n = 3$：定出 $j$，用角动量合成 $j \otimes j$ 数出包含的 $l$ 与总简并度，并与第 06 篇的亚层计数对上。

<details markdown="1"><summary>点击显示答案</summary>

$n = 2j + 1 = 3$ 给出 $j = 1$，即能级承载 su(2)$\oplus$su(2) 的 $(1, 1)$ 表示，维数 $(2\cdot1+1)^2 = 9$。

物理角动量 $\vec L = \vec J_+ + \vec J_-$，其取值由两个自旋 1 的合成给出（第 05 篇第 6 节）：

$$1 \otimes 1 = 0 \oplus 1 \oplus 2,$$

即 $l = 0, 1, 2$ 各出现一次——对应化学记号 $3s$、$3p$、$3d$ 三个亚层。各 $l$ 的 $m$ 简并数分别为 $2l+1 = 1, 3, 5$，合计

$$1 + 3 + 5 = 9 = 3^2,$$

与 $(2j+1)^2$ 一致，也与第 06 篇第 2.3 节的计数 $\sum_{l=0}^{n-1}(2l+1) = n^2$ 逐项对上（第 06 篇的 $n = 3$ 壳层正是 $3s^2 3p^6 3d^{10}$，轨道部分 $2 + 6 + 10 = 18 = 2n^2$，除以自旋因子 2 即 9）。

两种语言的逐项翻译：波动力学说"$n = n_r + l + 1$、$n_r \ge 0$ 所以 $l \le n-1$"，代数解法这边说"$l$ 是 $j \otimes j$ 的 CG 分解通道，最大值为 $2j = n-1$"——$n_r$ 就是分解中从最大值往下数的通道序号（$n=3$ 时 $3s$ 对应 $n_r = 2$、$3p$ 对应 $n_r = 1$、$3d$ 对应 $n_r = 0$）。$\blacksquare$

</details>

## 参考

- Pauli, "Über das Wasserstoffspektrum vom Standpunkt der neuen Quantenmechanik", Z. Phys. 36, 336 (1926)——本篇的原始文献；历史背景另见 Heisenberg, Z. Phys. 33, 879 (1925)。
- Sakurai《现代量子力学》第 3 章：角动量代数与 SO(4) 氢原子简并的群论讨论（与第 05 篇进阶阅读一致）。
- Baym《Lectures on Quantum Mechanics》：Runge–Lenz 矢量与氢原子 SO(4) 对称性的章节，$[A_i, A_j]$ 与 $A^2$ 恒等式的完整推导讲得最细。
- Greiner《Quantum Mechanics: Symmetries》氢原子章：so(4) 李代数、重标度与 Casimir 算账的系统表述。
