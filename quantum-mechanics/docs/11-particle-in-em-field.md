# 电磁场中的粒子：最小耦合、AB 效应与 Landau 能级

> 路线图位置：量子力学书 · 第五部分（外场、对称性与几何相位）· 第 11 篇
> 前置知识：第 03 篇（演化算符与表象）；第 03s 篇（坐标表象与概率流）；第 04 篇（升降算符解法——Landau 能级的引擎）；第 05 篇（自旋，本篇主体只处理无自旋粒子，自旋相关修正见第 07s3 篇 Zeeman）。
> 学习目标：会从最小耦合 $q\vec p \to \vec p - q\vec A$ 写出电磁场中的薛定谔方程，分清正则动量与机械动量；会证明规范变换下波函数的局域相位协变性，并说出这条"局域相位自由度"如何预示 QFT 的规范原理；会解释 Aharonov–Bohm 效应为什么表明**势**而非只有场进入量子力学；会用代数方法解出均匀磁场的 Landau 能级 $\hbar\omega_c(n+\tfrac12)$，数清每能级简并度 = 磁通量子数，并在对称规范下写出最低 Landau 能级波函数（凝聚态书量子霍尔一章的砖块）。
>
> 记号约定：SI 单位，保留 $\hbar$。粒子电荷 $q$（电子 $q = -e$，$e > 0$ 为元电荷）；磁场沿 $z$。磁通量子 $\Phi_0 = h/e = 4.14\times10^{-15}\ \text{T}\cdot\text{m}^2$；磁长度 $\ell_B = \sqrt{\hbar/(eB)} \approx 25.7\ \text{nm}/\sqrt{B[\text{T}]}$（凝聚态书的长度标尺，本篇一并引入）。

---

## 1. 一句话总结

**电磁场以最小耦合进入量子力学：$H = \frac{(\vec p - q\vec A)^2}{2m} + q\varphi$——哈密顿量里站着的是矢势 $\vec A$ 而非磁场 $\vec B$；规范变换 $\vec A\to\vec A+\nabla\chi$ 由波函数的局域相位 $\psi\to e^{iq\chi/\hbar}\psi$ 精确补偿，但代价是"整体相位不可观测"升级为"闭路相位可干涉"——Aharonov–Bohm 效应（电子绕过无场区域仍积累相位 $q\Phi/\hbar$）证明势携带真实物理；均匀磁场把连续谱离散化为 Landau 能级 $\hbar\omega_c(n+\tfrac12)$，每个能级每单位面积容纳 $B/\Phi_0$ 个态（简并度 = 穿过样品的磁通量子数）——量子霍尔效应的全部舞台在本书库里第一次搭好。**

## 2. 最小耦合：正则动量不是机械动量

经典拉格朗日 $L = \frac12m\dot{\vec r}^2 + q\dot{\vec r}\cdot\vec A - q\varphi$ 给出正则动量 $\vec p = m\dot{\vec r} + q\vec A$：**机械（速度）动量 $\vec\Pi = m\dot{\vec r} = \vec p - q\vec A$ 与正则动量 $p$ 不再相等**。量子化按正则对易关系 $[x_i, p_j] = i\hbar\delta_{ij}$ 执行，哈密顿量

$$\boxed{\ H = \frac{(\vec p - q\vec A)^2}{2m} + q\varphi\ },\qquad \vec\Pi \equiv \vec p - q\vec A,$$

薛定谔方程 $i\hbar\partial_t\psi = \left[\frac{(-i\hbar\nabla - q\vec A)^2}{2m} + q\varphi\right]\psi$。两条直接后果：

1. **动量算符的测量意义换了人**：$-i\hbar\nabla$ 测的是正则动量；速度算符 $\dot{\vec r} = \frac{i}{\hbar}[H,\vec r] = \vec\Pi/m$。
2. **机械动量不对易**：

$$[\Pi_x, \Pi_y] = iq\hbar\,(\nabla\times\vec A)_z = iq\hbar B_z.$$

磁场的全部量子效应都藏在这一条对易关系里——下一节它直接生成 Landau 能级。

## 3. 规范变换：局域相位协变性

规范变换 $\vec A\to\vec A' = \vec A + \nabla\chi$，$\varphi\to\varphi' = \varphi - \partial_t\chi$ 下，场强不变（$\vec E,\vec B$ 是规范冗余下的不变量）。薛定谔方程形式不变的条件是波函数**同时**做局域相位旋转：

$$\psi'(\vec r,t) = e^{iq\chi(\vec r,t)/\hbar}\,\psi(\vec r,t),$$

一行代数即可验证（自检问题 1）：$(-i\hbar\nabla - q\vec A')\psi' = e^{iq\chi/\hbar}(-i\hbar\nabla - q\vec A)\psi$——相位梯度恰好吃掉 $\nabla\chi$。

三点读出：

- **概率密度与概率流规范不变**（可观测量必须如此）：$\vec j = \frac{1}{2m}\big[\psi^*\vec\Pi\psi + (\vec\Pi\psi)^*\psi\big]$。
- **局域相位自由度**：$\chi(\vec r)$ 逐点独立——要求理论在每点独立的相位旋转下不变，正是 QFT 里**规范原理**的起点：把整体对称升级为局域对称，必须引入规范场（见 QFT 书[整体对称 vs 规范对称](../../qft-sm/docs/stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)——本篇是它最古老的单粒子实例）。
- **整体 vs 闭路**：$e^{iq\chi/\hbar}$ 在单点上看是冗余相位（不可观测）；但绕闭合回路一周的总相位 $\frac{q}{\hbar}\oint\nabla\chi\cdot d\vec l$ 形式上是零——除非 $\vec A$ 有不能被单值 $\chi$ 吃掉的部分。这正是 AB 效应的位置。

## 4. Aharonov–Bohm 效应：势是物理的

**设置**（磁 AB，1960）：无限长螺线管（半径 $R$，磁通 $\Phi$），电子双缝实验绕螺线管两侧通过。电子可达区域里 $\vec B = 0$、$\vec E = 0$，但矢势不为零（$\oint\vec A\cdot d\vec l = \Phi eq 0$）。

**相位**：沿路径 $\mathcal C$ 的波函数携带相位 $\frac{q}{\hbar}\int_{\mathcal C}\vec A\cdot d\vec l$（把 §3 的规范相位从"补偿项"读成"动力学记账"）。两路之差：

$$\Delta\phi = \frac{q}{\hbar}\oint\vec A\cdot d\vec l = \frac{q\Phi}{\hbar} = 2\pi\,\frac{\Phi}{\Phi_0}.$$

干涉条纹随 $\Phi$ 整体平移，周期恰为 $\Phi_0 = h/e$——**电子从未踏入场强非零的区域，相移却真实可测**。

**三层理解**（一浪比一浪深）：

1. **规范不变性没被破坏**：单条路径的相位依赖规范（$\vec A$ 可换规范），但**闭路**相位 $\frac{q}{\hbar}\oint\vec A\cdot d\vec l = \frac{q}{\hbar}\Phi$ 只依赖管内磁通——观测的是规范不变量。$\vec B=0$ 区域的 $\vec A$ 局部看是纯规范（可取 $\vec A = \nabla\chi$），但空间有"洞"（螺线管）使 $\chi$ 无法全局单值——拓扑障碍使环路相位非零。这套语言（**和乐**，holonomy）在第 13 篇将以 Berry 相位的身份全面回归：AB 相位就是最干净的 Berry 相位。
2. **与局域性不冲突**：经典运动方程只含 $\vec E,\vec B$（规范不变），经典粒子确实"感觉不到"管内；量子干涉比较的是两条路径，相位由路径包围的磁通决定——这正是法拉第定律 $\oint\vec E\cdot d\vec l = -d\Phi/dt$ 的"兄弟"：变化磁通的感应电场推动条纹移动（屏蔽实验变体），静态时纯粹是几何。没有超光速影响。
3. **实验闭环**：Chambers 1960 首证；**Tonomura 1986**（外镀超导屏蔽的环形磁体，磁通被锁死在环内且不漏）一锤定音——条纹平移 $\Delta\phi/2\pi$ 个周期，精确随 $\Phi$ 走。电 AB（时变标势的干涉）同年由 Bayh 演示。

**Byers–Yang 定理**：只穿过多连通区域孔洞的磁通，一切平衡态可观测量都是 $\Phi$ 的周期函数，周期 $\Phi_0$——超导环的磁通量子化（周期换成 $h/2e$，库珀对电荷 $2e$，见凝聚态书[超导电性](../../condensed-matter/docs/08-superconductivity.md)）与 Laughlin 规范泵浦（[量子霍尔](../../condensed-matter/docs/11-quantum-hall-effect.md)）都用这条定理。

## 5. Landau 能级：代数解法

均匀磁场 $\vec B = B\hat z$（电子 $q=-e$，取 $\vec p_z$ 解耦的规范）。核心原料是 §2 的对易关系 $[\Pi_x,\Pi_y] = -ie\hbar B$——与谐振子的 $[a,a^\dagger]=1$ 同构。按第 04 篇的剧本定义升降算符：

$$a \equiv \frac{\Pi_x - i\Pi_y}{\sqrt{2e\hbar B}},\qquad a^\dagger \equiv \frac{\Pi_x + i\Pi_y}{\sqrt{2e\hbar B}},\qquad [a,a^\dagger] = 1.$$

（验证 $[a,a^\dagger] = \frac{2i[\Pi_x,\Pi_y]}{2e\hbar B} = 1$ 用到上面的对易关系。）把哈密顿量凑成 $a,a^\dagger$（自检问题 2 走完全程）：

$$H = \frac{\Pi_x^2+\Pi_y^2}{2m} + \frac{p_z^2}{2m} = \hbar\omega_c\left(a^\dagger a + \tfrac12\right) + \frac{p_z^2}{2m},\qquad \omega_c \equiv \frac{eB}{m}.$$

**全部解**——Landau 能级：

$$\boxed{\ E_n = \hbar\omega_c\left(n + \tfrac12\right) + \frac{\hbar^2k_z^2}{2m}\ },\qquad n = 0,1,2,\cdots$$

三维气体里每条抛物线色散被压成一串一维子带（二维时干脆是一排 $\delta$ 峰）。零点能 $\tfrac12\hbar\omega_c$ 与简并在磁场中的无能隙与否无关——它是"垂直方向被禁闭成振子"的代价，顺带给出反磁化率的朗道项（凝聚态书[自由电子气](../../condensed-matter/docs/03-free-electron-gas.md)）。

## 6. 简并度记账：一个态一份磁通量子

取 Landau 规范 $\vec A = (0, Bx, 0)$：$H = \frac{p_x^2}{2m} + \frac{(p_y + eBx)^2}{2m}$（电子），$p_y$ 守恒。设 $\psi = e^{ik_y y}\,\phi(x)$：一维振子，中心在

$$x_0 = -\frac{\hbar k_y}{eB} = -k_y\ell_B^2,$$

即每个 $k_y$ 对应一条振子（同一 $E_n$），只要中心落在样品 $[0, L_x]$ 内。$k_y$ 间距 $2\pi/L_y$，故

$$N = \frac{L_x}{2\pi/L_y\cdot\ell_B^2} = \frac{L_xL_y}{2\pi\ell_B^2} = \frac{B\,L_xL_y}{\Phi_0}\qquad\Longleftrightarrow\qquad \boxed{\ \frac{N}{A} = \frac{B}{\Phi_0}\ }$$

**每个 Landau 能级、每单位面积容纳 $B/\Phi_0$ 个态：一个态对应一份磁通量子 $h/e$。** 这条记账是整数量子霍尔效应 $\sigma_{xy} = \nu e^2/h$ 的分子（填充因子 $\nu$ = 填满的 Landau 能级数，凝聚态书第 11 章从本篇终点出发）。同理立即读出：量子霍尔平台出现时每能级一个 $B/\Phi_0 \sim 2.4\times10^{15}\ \text{m}^{-2}/\text{T}$ 的海量简并，无序把 $\delta$ 峰展宽成带、中间留出迁移率隙——平台与拓扑的故事交给凝聚态书。

## 7. 对称规范与最低 Landau 能级

对称规范 $\vec A = \frac12\vec B\times\vec r = \frac{B}{2}(-y, x, 0)$ 下，角动量 $L_z$ 守恒（不与 $p_y$ 类的好量子数共存——规范选择决定哪套简并量子数显形，能级与简并度本身规范不变）。最低 Landau 能级（LLL, $n=0$）的波函数是一族解析函数：

$$\psi_m(z) = \frac{z^m\,e^{-\lvert z\rvert^2/4\ell_B^2}}{\sqrt{2\pi\,2^m m!\,\ell_B^{2m+2}}},\qquad z \equiv x + iy,\quad m = 0,1,2,\cdots$$

（复坐标 $z$；归一化与 $\langle r^2\rangle_m = 2(m+1)\ell_B^2$ 见自检问题 5。）第 $m$ 个态是半径 $\sim\sqrt{2(m+1)}\,\ell_B$ 的环——LLL 的轨道随 $m$ 一圈圈往外铺，正是"每面积一个态"的同心圆版本。

**为什么值得记住这串函数**：凝聚态书里 Laughlin 波函数 $\prod_{i<j}(z_i - z_j)^q\,e^{-\sum\lvert z_i\rvert^2/4\ell_B^2}$（[分数量子霍尔](../../condensed-matter/docs/11s-fractional-quantum-hall.md)）就是 LLL 波函数的多体多项式；磁长度 $\ell_B$ 是全书量子霍尔叙事的长度标尺（25.7 nm @ 1 T，比晶格常数大两个数量级——宏观简并的几何根源）。

## 8. 接口

- **第 13 篇（绝热与 Berry）**：AB 相位重新登场——以 Berry 相位/和乐的身份；Landau 能级是陈数与量子霍尔的谱系起点。
- **凝聚态书**：第 11 章（整数/分数量子霍尔——本篇的直接下游）、第 8 章（超导磁通量子化 $h/2e$）、第 3 章（朗道抗磁性与 de Haas–van Alphen）。
- **QFT 书**：规范原理与规范场（整体 vs 规范对称）——本篇是它的单粒子序章；$\vec\Pi$ 的非对易是光子自能/反磁化率的近亲。
- **第 07s3 篇**：弱磁场下束缚态能级的 Zeeman 微扰——与本篇的强场/自由粒子互补。

## 小结

| 概念 | 公式 | 备注 |
| --- | --- | --- |
| 最小耦合 | $H = \frac{(\vec p - q\vec A)^2}{2m} + q\varphi$ | 正则 vs 机械动量 |
| 核心对易关系 | $[\Pi_x,\Pi_y] = iq\hbar B$ | 磁场的量子身份 |
| 规范协变 | $\psi\to e^{iq\chi/\hbar}\psi$ | 局域相位自由度 → 规范原理 |
| AB 相位 | $\Delta\phi = q\Phi/\hbar$ | 闭路、规范不变、拓扑 |
| Landau 能级 | $\hbar\omega_c(n+\tfrac12)$ | 升降算符同构谐振子 |
| 简并度 | $N/A = B/\Phi_0$ | 一态一磁通量子 |
| LLL 波函数 | $z^m e^{-\lvert z\rvert^2/4\ell_B^2}$ | Laughlin 的砖块 |

一句话收束：磁场进入量子力学不是靠 $q\vec v\times\vec B$ 的力，而是靠把 $p$ 换成 $p - qA$ 这一笔改写——正则动量从此背着矢势，闭路相位成了可观测量（AB），连续谱折成天量简并的 Landau 梯子（QH）。规范结构从第一页就在场。

## 自检问题

**1.** 完整证明：规范变换 $\vec A\to\vec A+\nabla\chi$、$\varphi\to\varphi-\partial_t\chi$ 配合 $\psi\to e^{iq\chi/\hbar}\psi$ 使薛定谔方程不变；并证明概率流 $\vec j = \frac{1}{2m}[\psi^*\vec\Pi\psi + (\vec\Pi\psi)^*\psi]$ 规范不变。

<details markdown="1"><summary>点击显示答案</summary>

对空间部分，关键是逐点验证共变导数的变换：设 $\psi' = e^{iq\chi/\hbar}\psi$，对乘积求导

$$-i\hbar\nabla\psi' = -i\hbar\nabla\big(e^{iq\chi/\hbar}\psi\big) = e^{iq\chi/\hbar}\big(q\nabla\chi\,\psi - i\hbar\nabla\psi\big),$$

于是

$$\vec\Pi'\psi' = \big[-i\hbar\nabla - q(\vec A+\nabla\chi)\big]e^{iq\chi/\hbar}\psi = e^{iq\chi/\hbar}\big(q\nabla\chi\,\psi - i\hbar\nabla\psi - q\vec A\psi - q\nabla\chi\,\psi\big) = e^{iq\chi/\hbar}\,\vec\Pi\psi.$$

即 $\vec\Pi'\psi' = e^{iq\chi/\hbar}\vec\Pi\psi$，平方除以 $2m$ 后动能项同样只多出整体相位。时间部分：

$$\big(i\hbar\partial_t - q\varphi'\big)\psi' = e^{iq\chi/\hbar}\big(-q\,\partial_t\chi\,\psi + i\hbar\partial_t\psi\big) - q(\varphi - \partial_t\chi)e^{iq\chi/\hbar}\psi = e^{iq\chi/\hbar}\big(i\hbar\partial_t - q\varphi\big)\psi.$$

两边相等，薛定谔方程 $i\hbar\partial_t\psi' = \Big[\frac{\vec\Pi'^2}{2m}+q\varphi'\Big]\psi'$ 与原方程逐项等价——形式不变。

概率流：$\psi'^*\psi' = \psi^*\psi$ 已不变；$\vec j' = \frac{1}{2m}\big[\psi'^*\vec\Pi'\psi' + (\vec\Pi'\psi')^*\psi'\big] = \frac{1}{2m}\big[\psi^*\vec\Pi\psi + (\vec\Pi\psi)^*\psi\big] = \vec j$（相位因子相消）。可观测量如预期规范不变——$\vec A$ 与相位各自都变，组合出不变的 $\vec j$，这正是"规范冗余"的含义。

</details>

**2.** 从 $[\Pi_x,\Pi_y] = -ie\hbar B$ 出发，验证 $[a,a^\dagger]=1$，并完整推导 $H = \hbar\omega_c(a^\dagger a + \tfrac12)$（二维情形）。

<details markdown="1"><summary>点击显示答案</summary>

对易子：$[a,a^\dagger] = \frac{1}{2e\hbar B}[\Pi_x - i\Pi_y,\ \Pi_x + i\Pi_y] = \frac{1}{2e\hbar B}\big(i[\Pi_x,\Pi_y] - i[\Pi_y,\Pi_x]\big) = \frac{2i[\Pi_x,\Pi_y]}{2e\hbar B} = \frac{2i(-ie\hbar B)}{2e\hbar B} = 1.$

哈密顿量：先算乘积

$$(\Pi_x - i\Pi_y)(\Pi_x + i\Pi_y) = \Pi_x^2 + \Pi_y^2 + i(\Pi_x\Pi_y - \Pi_y\Pi_x) = \Pi_x^2 + \Pi_y^2 + i[\Pi_x,\Pi_y] = \Pi_x^2 + \Pi_y^2 + e\hbar B.$$

故 $\Pi_x^2 + \Pi_y^2 = 2e\hbar B\,aa^\dagger - e\hbar B = 2e\hbar B\,(aa^\dagger - \tfrac12) = 2e\hbar B\,(a^\dagger a + \tfrac12)$（末步用 $aa^\dagger = a^\dagger a + 1$）。于是

$$H = \frac{\Pi_x^2+\Pi_y^2}{2m} = \frac{e\hbar B}{m}\Big(a^\dagger a + \frac12\Big) = \hbar\omega_c\Big(a^\dagger a + \frac12\Big).$$

谱由 $a^\dagger a$ 的整数谱直接读出：$E_n = \hbar\omega_c(n+\tfrac12)$。注意与第 04 篇谐振子的微妙差别：这里的振子坐标是 $(\Pi_x,\Pi_y)$——**速度空间**的振子；实空间轨道（第 7 节的 $z^m$ 环）来自另一套对易（导向中心），简并度由它承载。

</details>

**3.** 在 Landau 规范下数简并：证明每单位面积每能级 $N/A = eB/h = B/\Phi_0$，并解释为什么超导环的磁通量子是 $h/2e$ 而这里用 $h/e$。

<details markdown="1"><summary>点击显示答案</summary>

Landau 规范 $\vec A = (0,Bx,0)$：$H = \frac{p_x^2}{2m} + \frac{(p_y + eBx)^2}{2m}$（电子 $q=-e$，$\Pi_y = p_y - qA_y = p_y + eBx$）。平移不变的方向是 $y$：$\psi = e^{ik_yy}\phi(x)$，化为以 $x_0 = -\hbar k_y/(eB) = -k_y\ell_B^2$ 为中心的一维振子，能量只依赖振子量子数 $n$，与 $k_y$ 无关——这就是简并的来源。中心须落在样品内 $x_0\in[0,L_x]$：$k_y$ 的允许范围宽度 $L_x/\ell_B^2$，间距 $\Delta k_y = 2\pi/L_y$：

$$N = \frac{L_x/\ell_B^2}{2\pi/L_y} = \frac{L_xL_y}{2\pi\ell_B^2} = \frac{eB\,L_xL_y}{h}\ \Rightarrow\ \frac{N}{A} = \frac{eB}{h} = \frac{B}{\Phi_0}.$$

物理读法：磁场每增加一份 $h/e$ 磁通，每个能级就多一个座位。超导环里绕环电子的等效电荷是库珀对电荷 $q = 2e$（配对态，凝聚态书第 8 章），同样论证给出 $\Phi_0^{\rm sc} = h/2e$——磁通量子化实验（London 预言、Deaver–Fairbank 1961 实测）正是 AB 类环路相位条件 $\frac{q}{\hbar}\oint\vec A\cdot d\vec l = 2\pi n$ 的超导版本。

</details>

**4.** 推导磁 AB 效应的双缝相位差 $\Delta\phi = q\Phi/\hbar$；论证为什么这既不违反规范不变性（整体相位不可观测）也不违反相对论因果性（B = 0 区域里什么都没发生）。

<details markdown="1"><summary>点击显示答案</summary>

相位推导：定态薛定谔方程 $H\psi = E\psi$ 中，若区域里 $\vec B = 0$，可取 $\vec A = \nabla\chi$（局部纯规范）。代入 $\psi = e^{iq\chi/\hbar}u$，$u$ 满足**自由**薛定谔方程（第 1 题的逆操作）。故沿路径 $\mathcal C$ 传播的自由波额外携带相位 $e^{\frac{iq}{\hbar}\int_{\mathcal C}\nabla\chi\cdot d\vec l}$。两条路径相干叠加，叉积相位差

$$\Delta\phi = \frac{q}{\hbar}\Big(\int_1\nabla\chi\cdot d\vec l - \int_2\nabla\chi\cdot d\vec l\Big) = \frac{q}{\hbar}\oint\vec A\cdot d\vec l = \frac{q\Phi}{\hbar}.$$

条纹位置随 $\Phi$ 移动，周期 $\Phi_0 = h/\lvert q\rvert$。

规范不变性：单条路径相位含 $\int\vec A\cdot d\vec l$ 依赖规范选择，确实不可观测；但干涉取决于**闭路**积分 $\oint\vec A\cdot d\vec l = \Phi$（斯托克斯定理，管内磁通）——规范不变量。可见 AB 效应观测的是环路拓扑量，不是势本身的"数值"。

因果性：$\vec B = 0$ 区域里波函数满足自由方程（刚证），局域测量（沿单路径的任何局域实验）完全探测不到 $\Phi$。相移只在**比较两条路径**的干涉里出现，而两条路径合成的回路包围磁通——这是几何/整体的联系，不是管内事件向外的超光速传信。改变 $\Phi$ 若要瞬时改变远处条纹，将违反相对论——实际上静态 AB 无信息传递；时变磁通伴随的感应电场（法拉第）承担一切因果影响。

</details>

**5.** 对称规范下验证 LLL 波函数 $\psi_m = \frac{z^m e^{-\lvert z\rvert^2/4\ell_B^2}}{\sqrt{2\pi\,2^m m!\,\ell_B^{2m+2}}}$ 归一，并计算 $\langle r^2\rangle_m = 2(m+1)\ell_B^2$。

<details markdown="1"><summary>点击显示答案</summary>

归一化：极坐标 $d^2r = r\,dr\,d\theta$，$\lvert z^m\rvert^2 = r^{2m}$：

$$\int d^2r\,\lvert\psi_m\rvert^2 = \frac{2\pi}{2\pi\,2^m m!\,\ell_B^{2m+2}}\int_0^\infty r^{2m+1}e^{-r^2/2\ell_B^2}\,dr.$$

换元 $u = r^2/2\ell_B^2$（$r\,dr = \ell_B^2du$，$r^{2m} = (2\ell_B^2u)^m$）：积分 $= 2^m\ell_B^{2m+2}\Gamma(m+1) = 2^m m!\,\ell_B^{2m+2}$。代回：$2^m m!\ell_B^{2m+2}/(2^m m!\ell_B^{2m+2}) = 1$ ✓。

半径平方：同样换元，$\int_0^\infty r^{2m+3}e^{-r^2/2\ell_B^2}dr = \frac12(2\ell_B^2)^{m+2}\Gamma(m+2) = 2^{m+1}\ell_B^{2m+4}(m+1)!$（被积函数多一个 $r^2$，等价于 $2\ell_B^2(m+1)$ 倍上一个积分）：

$$\langle r^2\rangle_m = \frac{2^{m+1}\ell_B^{2m+4}(m+1)!}{2^m m!\,\ell_B^{2m+2}} = 2(m+1)\ell_B^2.$$

第 $m$ 个 LLL 轨道是半径 $\sqrt{2(m+1)}\,\ell_B$ 的环，相邻环之间的面积 $\pi(\langle r^2\rangle_{m+1}-\langle r^2\rangle_m) = 2\pi\ell_B^2 = \Phi_0/B$——每圈恰好一份数磁通量子，"一个态一份磁通"的同心圆账本与第 6 节的 Landau 规范账本一致（规范选择换的是记账方式，不是物理）。

</details>

## 参考

- Sakurai《现代量子力学》规范变换与 AB 效应一节（势与规范原理的标准讨论）。
- 朗道《量子力学》"均匀磁场中的运动"一节——Landau 能级与经典回旋轨道的对应。
- Griffiths《量子力学概论》AB 效应习题与讨论。
- Tonomura et al., *Phys. Rev. Lett.* **56**, 792 (1986)——屏蔽环磁通 AB 的判定实验。
- 凝聚态书[第 11 章 量子 Hall 效应](../../condensed-matter/docs/11-quantum-hall-effect.md)（Landau 能级的多体与输运下半场）、[第 8 章 超导电性](../../condensed-matter/docs/08-superconductivity.md)（磁通量子化 $h/2e$）。
