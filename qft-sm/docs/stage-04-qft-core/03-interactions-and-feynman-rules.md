# 相互作用与微扰论：Wick 定理、费曼图与费曼规则

> 路线图位置：第 4 阶段（QFT 核心）· 第 3 篇（连接[自由标量场](01-scalar-field-quantization.md)与 [QED](05-qed.md) 的发动机舱）。
> 前置知识：[标量场量子化](01-scalar-field-quantization.md)（模式展开与对易关系、编时乘积、Feynman 传播子 $D_F$——本篇直接在它上面施工）；[量子力学书·微扰理论](../../../quantum-mechanics/docs/07-perturbation-theory.md)（含时微扰论的 Dyson 级数与费米黄金定则——本篇是它的场论翻版，你已经会一半）。
> 学习目标：会判断什么相互作用可以写进拉氏量、微扰论何时适用；会推相互作用绘景下的 Dyson 级数，说清时序算符为什么必然出现；会用 Wick 定理把编时乘积拆成正规乘积加收缩，并证明两点收缩恰是 $D_F$；能把 $\lambda\phi^4$ 四点函数一阶的全部 $7\times5\times3 = 105$ 种缩并按拓扑分类（$24+72+9$），读出连接树图系数恰为 $-i\lambda$；会数对称因子（$8$、$2$、$2$ 三个典型值两法互验）；能解释真空泡泡为什么在归一化中严格相消；会推 $\phi^3$ 理论的 $s,t,u$ 三通道树图振幅——它就是 QED 一切树图的模板。

全文用自然单位 $\hbar = c = 1$，度规 $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$。沿用第 01 篇的归一化：$[a_p, a_q^\dagger] = (2\pi)^3\,2\omega_p\,\delta^3(\vec p - \vec q)$。

---

## 1. 一句话总结

**自由场算不出任何物理——粒子永不散射、永不衰变、永不结合。本篇装上发动机：把相互作用哈密顿量当小量，跃迁振幅按 Dyson 级数展开成场算符的编时乘积；Wick 定理把每个编时乘积拆成"两两收缩 + 正规乘积"，而一对场的收缩恰好是第 01 篇的 Feynman 传播子 $D_F$。把每个收缩画成一条线、每个相互作用积分画成一个顶点，微扰论的第 $n$ 阶就变成"数所有 $n$ 顶点的图"——费曼规则是这套对应关系的字典，从此"算振幅"变成"画图、按表抄因子、积分"。**

## 2. 把相互作用写进拉氏量

### 2.1 自由场为什么不够

第 01 篇结尾的理论里，哈密顿量 $\colon\!H\!\colon = \int\frac{d^3p}{(2\pi)^3 2\omega_p}\,\omega_p a_p^\dagger a_p$ 是对角的：一个 $n$ 粒子态永远是 $n$ 粒子态，动量永远不变。没有散射截面、没有衰变率、没有束缚态——自由场只是把"无相互作用的多粒子世界"记录在案。物理要有故事，拉氏量必须有把不同粒子数、不同动量的态耦合起来的项。

### 2.2 允许写什么：定域 + 可重整

两条筛选标准（第二条的完整理由在第 06 篇）：

- **定域性**：$\mathcal L_{\mathrm{int}}(x)$ 只依赖同一点 $x$ 的场（如 $\varphi^4(x)$），不含 $\varphi(x)\varphi(y)$ 型的非定域项。非定域耦合会把类空间隔的两点绑进同一相互作用，微观因果性（第 01 篇 §8）不保。
- **可重整性**：耦合常数的质量量纲非负。自由拉氏密度量纲为 4（$d^4x$ 积分后无量纲的作用量），动能项 $½(\partial\varphi)^2$ 定出 $[\varphi] = 1$，于是 $\varphi^n$ 相互作用的耦合量纲为 $4-n$：$\varphi^3$ 的 $g$ 带量纲 1，$\varphi^4$ 的 $\lambda$ 无量纲，更高次幂为负量纲（不可重整，只能当有效理论——这正是第 06 篇 Wilson 视角的判据）。

对实标量场，候选只剩 $\varphi^3$ 与 $\varphi^4$。$\varphi^3$ 的势 $V = ½m^2\varphi^2 + \frac{g}{3!}\varphi^3$ 在 $\varphi \to -\infty$（或 $+\infty$，视符号）无下界——理论没有真正的基态。所以**主角是 $\lambda\phi^4$**：

$$\mathcal L = \frac12 \partial_\mu\varphi\,\partial^\mu\varphi - \frac12 m^2\varphi^2 - \frac{\lambda}{4!}\varphi^4, \qquad \mathcal H_{\mathrm{int}} = \frac{\lambda}{4!}\varphi^4.$$

$4!$ 是约定：它恰好约掉一个顶点四条腿的排列数，第 5 节的计数会看到每个图的系数因此干净利落。微扰适用条件是 $\lambda \ll 1$（更准确：在所涉能标上重整化后的 $\lambda$ 小，它随能标跑动，见第 06 篇）。

一个诚实的脚注（Dyson 1952）：若微扰级数对 $\lambda > 0$ 收敛，它就在 $\lambda = 0$ 附近解析，对很小的 $\lambda < 0$ 也该给出好定义的物理——但 $\lambda<0$ 的 $\phi^4$ 势无下界，理论根本不存在。矛盾说明**微扰级数的收敛半径是零**，它只在渐近意义下有用：$\lambda$ 足够小时，前若干阶给出惊人精确的答案（QED 的 $\alpha \approx 1/137$ 是史上最成功的例子）。对 $\varphi^3$ 同理（且更糟），但作为树图与一圈的练习场毫无问题——第 8 节会拿它练手。

## 3. 相互作用绘景与 Dyson 级数

### 3.1 三种绘景

| 绘景 | 谁演化 | 谁不动 | 用途 |
| --- | --- | --- | --- |
| 薛定谔 | 态 $\lvert\psi(t)\rangle$ | 算符 | 普物量子力学 |
| 海森堡 | 算符 $A_H(t)$ | 态 | 01 篇的自由场（$a_p, a_p^\dagger$ 不含时即此绘景） |
| 相互作用 | 态按 $H_{\mathrm{int}}$ 演化，算符按 $H_0$ 演化 | — | 微扰论专属 |

相互作用绘景是折中：算符带着**自由**演化，于是第 01 篇的全部算符技术（模式展开、对易关系、收缩）原样可用；而相互作用的信息全部装进态的演化里，可以按 $\lambda$ 展开。

### 3.2 定义与演化方程

取 $H = H_0 + H_{\mathrm{int}}$（$H_0$ 自由、可对角化），定义

$$\lvert\psi_I(t)\rangle = e^{iH_0 t}\,\lvert\psi_S(t)\rangle, \qquad A_I(t) = e^{iH_0 t}\,A_S\,e^{-iH_0 t}.$$

直接求导（用 $e^{iH_0t}H e^{-iH_0t} = H_0 + H_I(t)$，其中 $H_I(t) \equiv e^{iH_0t}H_{\mathrm{int}}e^{-iH_0t}$，$H_0$ 部分恰好消去）：

$$i\,\frac{d}{dt}\lvert\psi_I(t)\rangle = H_I(t)\,\lvert\psi_I(t)\rangle.$$

注意 $H_I(t) = \int d^3x\;\frac{\lambda}{4!}\,\varphi_I^4(t,\vec x)$ 含时（$\varphi_I$ 以自由方式演化），它是无穷多个自由度的算符——这一条方程就是量子力学含时微扰论的方程，只不过"系统"现在是整个场。

### 3.3 Dyson 级数

演化算符 $U_I(t, t_0)$（$\lvert\psi_I(t)\rangle = U_I(t,t_0)\lvert\psi_I(t_0)\rangle$，$U_I(t_0,t_0) = \mathbb 1$）满足 $i\,\partial_t U_I = H_I(t)\,U_I$。写成积分方程再迭代：

$$U_I(t,t_0) = \mathbb 1 - i\int_{t_0}^{t}\!\!dt_1\,H_I(t_1)U_I(t_1,t_0) = \mathbb 1 + (-i)\!\int_{t_0}^{t}\!\!dt_1\,H_I(t_1) + (-i)^2\!\int_{t_0}^{t}\!\!dt_1\!\int_{t_0}^{t_1}\!\!dt_2\,H_I(t_1)H_I(t_2) + \cdots$$

关键是第二步的积分区域是三角形的嵌套区间 $t_1 > t_2 > \cdots$——**算符自动按时序从晚到早排列**。把每步的三角形积分对称化到方形区域，代价是引入编时算符：

$$T\{H_I(t_1)H_I(t_2)\} = \theta(t_1 - t_2)\,H_I(t_1)H_I(t_2) + \theta(t_2 - t_1)\,H_I(t_2)H_I(t_1),$$

方形积分 $\int\!\!\int T\{\cdots\}$ 恰好等于 $2!$ 份同样的三角形积分（$n$ 个算符则是 $n!$ 份），于是级数收拢成紧凑的**时序指数**：

$$\boxed{\;U_I(t, t_0) = T\exp\Big[-i\int_{t_0}^{t} dt'\,H_I(t')\Big]\;}$$

**$T$ 不是外加的便利记号，而是级数本身的形状**：展开的每一项天然按时序排列。$T$ 对玻色子场不加符号；费米子场交换一次出一个负号（第 05 篇直接沿用，其完整推手是路径积分篇第 07 篇的格拉斯曼数）。

### 3.4 S 矩阵与一个诚实声明

散射实验问的是"很远过去入射的两个粒子，很远将来变成什么"，于是取

$$S \equiv U_I(+\infty, -\infty), \qquad S_{fi} = \langle f\lvert S\rvert i\rangle.$$

$\lvert i\rangle, \lvert f\rangle$ 取自由 Fock 态——这里藏着一个众所周知的含糊：$t = \pm\infty$ 时相互作用并不真的关闭。标准处理是给 $H_I$ 挂上 $e^{-\epsilon\lvert t\rvert}$（$\epsilon \to 0^+$，绝热开关）再取极限，物理结果是有限时间跃迁后再慢慢关灯；把这件事做严格正是散射形式理论（LSZ 约化，路线图第 4 项）的职责。本篇按物理教材的标准做法使用它，账单留给下一篇。

## 4. Wick 定理：编时乘积的完全拆解

### 4.1 障碍：$T$ 里面还是不对易的算符

要算的量形如 $\langle0\lvert T\{\varphi(x_1)\cdots\varphi(x_n)\,e^{-i\int H_I}\}\rvert 0\rangle$；指数展开后，每个时空积分里站着一大串场算符的编时乘积。$T$ 只把顺序按时间排好，**排好之后算符仍然不对易**，矩阵元还是没法逐项算。Wick 定理就是拆解这一大串的机器。

### 4.2 正规乘积与收缩

把场拆成正、负频两部分（第 01 篇的模式展开）：

$$\varphi(x) = \varphi^+(x) + \varphi^-(x), \qquad \varphi^+ \sim a_p e^{-ipx}\ (\text{湮灭}), \quad \varphi^- \sim a_p^\dagger e^{ipx}\ (\text{产生}).$$

**正规乘积** $\colon\!\cdots\!\colon$：把所有产生算符移到湮灭算符左边（玻色子不产生符号）。两条性质：$\langle0\rvert\colon\!(\cdots)\!\colon\rvert 0\rangle = 0$（右边最先碰 $|0\rangle$ 的湮灭算符给出零，除非全是产生算符——那又被 $\langle0\rvert$ 从左边杀死）；正规乘积内部可以对易重排。

**收缩**：一对算符"编时乘积减正规乘积"剩下的 $c$ 数。对两个场：

$$\overbrace{\varphi(x)\,\varphi(y)} \;\equiv\; T\{\varphi(x)\varphi(y)\} - \colon\!\varphi(x)\varphi(y)\!\colon \;=\; \langle0\rvert T\varphi(x)\varphi(y)\rvert 0\rangle = D_F(x-y).$$

最后一步验证（设 $x^0 > y^0$，另一时序同理）：$T\{\varphi\varphi\} = \varphi(x)\varphi(y)$ 展开四项，与正规乘积相比只剩湮灭在左、产生在右的那一项的排法之差：

$$\varphi^+(x)\varphi^-(y) - \varphi^-(y)\varphi^+(x) = [\varphi^+(x), \varphi^-(y)] = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\,e^{-ip(x-y)} \equiv D(x-y),$$

再并回两种时序正是第 01 篇 §8 算过的 $D_F$。**收缩就是 Feynman 传播子**——第 01 篇那句"$D_F$ 是微扰论的砖瓦"在此兑现（$i\epsilon$ 处方的推导、四种格林函数与光锥外行为见[第 02 篇](02-propagators-and-causality.md)）。

（下文用顶弧 $\overbrace{\varphi_i\varphi_j}$ 标出被收缩的一对；同一时空点的收缩如 $\overbrace{\varphi(y)\varphi(y)} = D_F(0)$。）

### 4.3 定理

$$\boxed{\;T\{\varphi_1\cdots\varphi_n\} = \colon\!\varphi_1\cdots\varphi_n\!\colon + \sum_{\text{单收缩}}\colon\!(\cdots)\!\colon + \sum_{\text{双收缩}}\colon\!(\cdots)\!\colon + \cdots\;}$$

右端穷尽一切收缩方式：0 个收缩的正规乘积，单项收缩（剩 $n-2$ 个算符正规序），双收缩，直到 $\lfloor n/2\rfloor$ 个收缩把算符两两配光。项数合计 $(n-1)!!$（奇数个算符时最后必剩一个无法配对的正规序单体，真空期望为零）。

证明思路（归纳法）：设 $T\{\varphi_1\cdots\varphi_n\}$ 已拆好；$T\{\varphi_1\cdots\varphi_{n+1}\}$ 中不妨设 $\varphi_{n+1}$ 时刻最早（$T$ 已把它排到最右）。把它逐步向左移过正规乘积里的每个 $\varphi_i$：移动湮灭部分 $\varphi_{n+1}^-$ 越过 $\varphi_i^+$ 时吐出 $c$ 数对易子 $[\varphi_i^+, \varphi_{n+1}^-]$——这正好是 $\varphi_i$ 与 $\varphi_{n+1}$ 的收缩。于是"全部收缩方式"逐个产生，归纳成立。完整记账冗长（教材都有），$n = 4$ 的显式展开放自检第 2 题逐行验证。

### 4.4 物理内核

对真空取期望，正规乘积项全部死去，只剩**完全收缩**的项：

$$\langle0\rvert T\{\varphi_1\cdots\varphi_{2n}\}\rvert 0\rangle = \sum_{\text{两两配对}} \prod_{\text{对}} D_F(x_i - x_j).$$

一句口诀：**真空期望 = 所有配对方案的传播子乘积之和**。$n$ 个点的自由关联函数由此一行写出；相互作用进来之后，顶点上的场也参与配对——配对方式的不同拓扑，就是费曼图。

## 5. $\lambda\phi^4$ 四点函数到一阶：逐图计数

### 5.1 相互作用真空与归一化分母

第 5 节的目标是四点关联函数 $\langle\Omega\rvert T\varphi_1\varphi_2\varphi_3\varphi_4\rvert\Omega\rangle$，其中 $\lvert\Omega\rangle$ 是**相互作用**理论的真空——它不是 $\lvert 0\rangle$（自由真空）。两者的桥梁是 Gell-Mann–Low 型恒等式：

$$\langle\Omega\rvert T\{\varphi_1\cdots\varphi_n\}\rvert\Omega\rangle = \frac{\langle0\rvert T\{\varphi_1\cdots\varphi_n\; e^{-i\int d^4y\, \mathcal H_I(y)}\}\rvert 0\rangle}{\langle0\rvert T\,e^{-i\int d^4y\, \mathcal H_I(y)}\rvert 0\rangle}.$$

<details markdown="1"><summary>补充说明：这个恒等式从哪来（推导骨架）</summary>

把相互作用挂上绝热开关后，相互作用的真空可写成 $\lvert\Omega\rangle \propto \lim_{T\to\infty} e^{-iHT}\lvert0\rangle$（用 $H = H_0 + H_{\mathrm{int}}$ 演化自由真空到无穷远未来；对基态不简并、能隙存在的理论，长时间投影自动选出基态分量）。海森堡算符与相互作用绘景算符的关系 $\varphi_H(t) = U_I^\dagger(t, t_0)\,\varphi_I(t)\,U_I(t, t_0)$ 把 $\langle\Omega\rvert T\{\varphi_H(x_1)\cdots\}\rvert\Omega\rangle$ 里的每段演化拼装起来：时序排列恰好让各段的 $U_I$ 首尾相接成 $U_I(\infty, -\infty) = T e^{-i\int H_I}$。两端各剩一份 $e^{-iHT}$ 投影，其真空分量在分子分母中相消，即得上式。这条链的严格化（态归一、绝热极限的存在性）属于散射形式理论；作为微扰论的工作恒等式，它到我们用到的每一阶都逐项可验。

</details>

分母 $\langle0\rvert T e^{-i\int\mathcal H_I}\rvert 0\rangle$ 从现在起就盯着它——第 5.3 节它的戏份是杀真空泡泡。

### 5.2 一百零五种缩并

把分子展开到 $\lambda$ 一阶：

$$\frac{-i\lambda}{4!}\int d^4y\;\langle0\rvert T\{\varphi_1\varphi_2\varphi_3\varphi_4\;\varphi(y)\,\varphi(y)\,\varphi(y)\,\varphi(y)\}\rvert 0\rangle.$$

按 Wick 定理只留完全收缩：8 个算符两两配对，共 $(8-1)!! = 105$ 种。按"外线 $\varphi_i$ 与顶点场 $\varphi(y)$ 怎么接"分三类：

**（a）四条外线全部接到顶点**：外线与 4 条顶点腿的配对方式 $4! = 24$ 种，系数 $24/4! = 1$：

$$-i\lambda\int d^4y\;D_F(x_1\!-\!y)D_F(x_2\!-\!y)D_F(x_3\!-\!y)D_F(x_4\!-\!y).$$

四条外线在一个顶点汇合——**连接的树图**，散射振幅的雏形。

**（b）两条外线接顶点，另两条外线互相收缩，剩下的两条顶点腿自相收缩**：选出接顶点的外线对 $\{i,j\}$ 共 $\binom42 = 6$ 种，各自在顶点腿上的分配 $4\times3 = 12$ 种，共 $72$ 种；系数 $72/4! = 3$，即 6 个形如

$$\frac{-i\lambda}{2}\int d^4y\;D_F(x_i\!-\!y)\,D_F(x_j\!-\!y)\,\overbrace{D_F(y\!-\!y)}^{\text{蝌蚪环}}\;\times\;D_F(x_k\!-\!x_l)$$

的项。这是**非连接**的：一块是带蝌蚪环的顶点（吃掉两条外线），另一块是自由传播线（另两条外线直接飞走）。系数 $1/2$ 是蝌蚪环两条腿互换的重复计数——对称因子 $S = 2$（第 7 节）。

**（c）外线全部互相收缩，顶点四条腿自相收缩（真空泡泡）**：外线配对 3 种 $\times$ 顶点自配对 3 种 $= 9$ 种，系数 $9/4! = 3/8$：

$$\frac{-i\lambda}{8}\int d^4y\;D_F(y\!-\!y)\,D_F(y\!-\!y)\;\times\;\big[D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23}\big].$$

括号里正是自由理论四点函数 $G_0^{(4)}$（自检第 2 题）。验算：$24 + 72 + 9 = 105 = 7!!$ ✓。

### 5.3 真空泡泡相消：分母的戏份

分母展开到同阶：$\langle0\rvert T e^{-i\int\mathcal H_I}\rvert 0\rangle = 1 + \frac{-i\lambda}{4!}\int d^4y\,\langle0\rvert T\varphi^4(y)\rvert 0\rangle + \cdots = 1 + \frac{-i\lambda}{8}\int d^4y\;D_F(0)^2 + \cdots$

分子里的（c）类恰好等于这个泡泡因子 $\times\, G_0^{(4)}$。做除法（$1/(1+a) = 1 - a + \cdots$）：

$$\frac{G_0^{(4)}\,(1 + a) + (\text{a 类}) + (\text{b 类})}{1 + a} = G_0^{(4)} + (\text{a 类}) + (\text{b 类}) + \cdots, \qquad a \equiv \frac{-i\lambda}{8}\int d^4y\,D_F(0)^2.$$

**真空泡泡严格消去。**这不是一阶的巧合：分母是 $e^{(\text{连接真空泡泡之和})}$ 的指数，分子的每个非连接项都带着同样的指数因子，相除后只剩不含真空泡泡的部分——这是**链接集团定理**的内容，路径积分语言下证明最短（[第 07 篇 §6](07-path-integral.md)会重新长出同一结论；本篇到一阶已显式验证）。

（b）类为什么不消？因为它的两块都挂着外线——归一化只杀"不含任何外点的连通块"。物理含义：非连接项对应"一部分入射粒子根本没参与相互作用、径直飞走"，它们属于 $S = \mathbb 1 + iT$ 里的 $\mathbb 1$；**散射振幅只由连接图贡献**。把这句话变成定理（关联函数的传播子极点留数 → 振幅）是 LSZ 的活，下一篇。

## 6. 费曼图与费曼规则

### 6.1 位置空间：逐元素的字典

把第 5 节的解析式与图形元素一一对上：

| 图元素 | 解析因子 |
| --- | --- |
| 顶点（一个相互作用点 $y$） | $-i\lambda \int d^4y$ |
| 内线（点 $y_1$ 到 $y_2$ 的收缩） | $D_F(y_1 - y_2)$ |
| 外线（外点 $x_i$ 到顶点） | $D_F(x_i - y)$ |
| 整体 | 除以对称因子 $S$ |

"Wick 缩并 → 线"是全部秘密：缩并对之间的每一条 $D_F$ 是一条线，顶点是相互作用积分。"画图"就是枚举缩并的拓扑等价类。

### 6.2 动量空间：$\delta$ 函数与截肢

散射实验标记的是动量，对四点函数做傅里叶变换 $G^{(4)}(p_1\ldots p_4) = \int \prod_i d^4x_i\, e^{i p_i x_i}\, G^{(4)}(x_1\ldots x_4)$。以 (a) 类树图为例，代入 $D_F(x-y) = \int\frac{d^4q}{(2\pi)^4}\frac{i\,e^{-iq(x-y)}}{q^2 - m^2 + i\epsilon}$，四个 $x_i$ 积分锁定 $q_i = p_i$，剩下的 $y$ 积分给出 $\int d^4y\, e^{i(p_1 + p_2 + p_3 + p_4)y} = (2\pi)^4\delta^{(4)}(\sum_i p_i)$：

$$G^{(4)}_{\text{树}} = (2\pi)^4\delta^{(4)}\Big(\sum_i p_i\Big)\;\times\underbrace{\;\Big[\;(-i\lambda)\prod_{i=1}^4 \frac{i}{p_i^2 - m^2 + i\epsilon}\;\Big]}_{\text{去掉外线传播子后剩 } i\mathcal M}.$$

两件事自动浮出：**每个顶点严格动量守恒**（$\delta$ 函数是 $\int d^4y$ 平移不变的傅里叶像）；外线各带一个传播子因子，而**不变振幅** $i\mathcal M$ 是把外线传播子"截肢"（amputate）后剩下的东西——截肢的合法性（在外线动量在壳 $p_i^2 \to m^2$ 处取留数）由 LSZ 定理背书。于是树图 $2\to2$：

$$i\mathcal M = -i\lambda.$$

$\phi^4$ 是接触相互作用：振幅与角度无关，质心系角分布平坦（高能下 $\frac{d\sigma}{d\Omega} \propto \lambda^2$——常数的相空间公式下一站细化）。

### 6.3 $\lambda\phi^4$ 费曼规则（动量空间速查）

| 对象 | 规则 |
| --- | --- |
| 内线（动量 $p$） | $\dfrac{i}{p^2 - m^2 + i\epsilon}$ |
| 顶点 | $-i\lambda$ |
| 外线（截肢约定） | $1$ |
| 每个顶点 | $(2\pi)^4\delta^{(4)}(\text{流入} - \text{流出})$ |
| 每个独立圈动量 $k$ | $\int \dfrac{d^4k}{(2\pi)^4}$ |
| 整体 | 除以对称因子 $S$，末尾剥离总 $\delta^{(4)}$ 得 $i\mathcal M$ |

圈图预告：$2\to2$ 的 $s$ 道一圈"鱼图"按上表抄出

$$i\mathcal M_{\text{鱼}} \supset \frac{(-i\lambda)^2}{2}\int\frac{d^4k}{(2\pi)^4}\;\frac{i}{k^2 - m^2 + i\epsilon}\;\frac{i}{(P-k)^2 - m^2 + i\epsilon}\qquad(P = p_1 + p_2),$$

大 $k$ 处被积函数 $\sim 1/k^4$，$\int d^4k$ 对数发散——发散不是事故，而是第 06 篇的正片（重整化）的入口。除以 $2$ 又是 $S = 2$。

## 7. 对称因子：图被数了几次

Wick 展开自带两套阶乘：每个顶点的 $\frac{1}{4!}$ 与时序指数的 $\frac{1}{n!}$（$n$ 个顶点）。它们**没有**把"同一个图被不同缩并方案重复数出"的次数除干净——剩下的多重数就是对称因子 $S$（图的自同构群阶数），解析式须再除以它。三个标准例（两法互验见自检第 4 题）：

- **"8 字"真空泡泡**（一阶、顶点两腿自缩成两个环）：顶点四腿两两配对 $3$ 种，系数 $3/4! = 1/8$，$S = 8$。图形验证：交换两个环（$2$）$\times$ 每个环两端互换（$2^2$），$2\times4 = 8$ ✓。
- **蝌蚪**（一阶、两条腿自缩成一个环）：系数 $12/24 = 1/2$，$S = 2$——环的两条腿互换。
- **鱼图**（二阶、两顶点两条内线相连）：见自检第 4 题的完整记账，$S = 2$——两条平行内线互换。

实用数法：固定外线后，问"顶点置换 $\times$ 各顶点腿的置换 $\times$ 内线置换，有多少个把图变回自己"。或者反过来：直接做 Wick 计数，看系数是 $1$ 还是 $1/2$、$1/8$。两种方法对不上说明图画错了。

（教材约定差异提示：有的书把 $1/S$ 并进"每条内线/顶点的组合权重"而不显式除 $S$，结果相同；与第 05 篇的 QED 规则对照时认准我们的约定——显式除以 $S$。顺带一句：带不同外线标签的树图通常 $S=1$，对称因子麻烦主要出在真空图、自能与带圈的关联函数上。）

## 8. $\phi^3$ 练习场：$s, t, u$ 三通道——QED 的模板

取 $\mathcal L_{\mathrm{int}} = -\frac{g}{3!}\varphi^3$（势无下界，第 2 节已声明；树图代数不受影响）。$2\to2$ 树图需要两个顶点：每顶点三条腿，两条接外线，剩一条与对方顶点相连——**内线只有一条，但外线的接法有三种**，按内线携带的动量命名（Mandelstam 变量，弹性散射、同质量 $m$）：

$$s = (p_1 + p_2)^2,\qquad t = (p_1 - p_3)^2,\qquad u = (p_1 - p_4)^2,\qquad s + t + u = 4m^2.$$

（$s$ 是质心系总能量平方；$t$ 是动量转移平方；恒等式证明见自检第 5 题。）按费曼规则抄出三个图之和：

$$i\mathcal M = (-ig)^2\left[\frac{i}{s - m^2 + i\epsilon} + \frac{i}{t - m^2 + i\epsilon} + \frac{i}{u - m^2 + i\epsilon}\right].$$

与 $\phi^4$ 的常数振幅对照：**内线传播子进了振幅**，角分布不再平坦——$t$、$u$ 随散射角变化，前向（小 $|t|$）被传播子放大。这正是"相互作用有内部结构"的第一个信号。

这张图是通往第 05 篇的桥：QED 的 $e^+e^- \to \mu^+\mu^-$ 是**只有 $s$ 道一个图**（内线换成光子传播子 $\frac{-i\eta_{\mu\nu}}{k^2+i\epsilon}$），康普顿散射是 $s + u$ 两道；外线因子从标量的 $1$ 换成旋量波函数 $u, v$ 与光子极化矢量。骨架完全相同——本篇练的就是那副骨架。

## 9. 小结

| 步骤 | 公式/结论 | 图像 |
| --- | --- | --- |
| 相互作用 | $\mathcal L_{\mathrm{int}} = -\frac{\lambda}{4!}\varphi^4$ | 定域 + 无量纲耦合 = 可微扰可重整 |
| Dyson 级数 | $U_I = T e^{-i\int H_I}$ | $T$ 是嵌套时间积分的形状 |
| Wick 定理 | 编时乘积 = 正规乘积 + 全部收缩方式 | 配对方案 = 图的拓扑 |
| 收缩 | $\overbrace{\varphi(x)\varphi(y)} = D_F(x-y)$ | 内线就是第 01 篇的传播子 |
| 真空期望 | 只剩完全收缩项；分母杀真空泡泡 | 振幅 = 连接图 |
| 费曼规则 | 内线 $\frac{i}{p^2-m^2+i\epsilon}$、顶点 $-i\lambda$、$\delta^4$、$\int\frac{d^4k}{(2\pi)^4}$、$\div S$ | 画图、抄因子、积分 |
| 树图结果 | $\phi^4$: $i\mathcal M = -i\lambda$；$\phi^3$: 三通道 $\frac{i}{s/t/u - m^2}$ | QED 树图的模板 |

下一站：[第 04 篇（S 矩阵、LSZ 约化与截面）](04-s-matrix-lsz-cross-sections.md)把"关联函数的截肢"变成定理，给出 $\langle f\rvert S\lvert i\rangle$ 与 $\mathcal M$ 的严格关系，并配上相空间公式——第 05 篇 QED 里实战。第 07 篇将用路径积分把本篇整套推导换一种语言重做一遍——两套语言的逐条对照是理解 QFT 的最好复习。

## 自检问题

**1.** 从 $i\,\partial_t U_I(t,t_0) = H_I(t)\,U_I(t,t_0)$、$U_I(t_0,t_0) = \mathbb 1$ 出发，把 $U_I$ 迭代到二阶，并显式验证：二阶的嵌套积分等于方形积分中的编时乘积（即 $\frac{1}{2!}$ 因子与时序算符的互相兑现）。

<details markdown="1"><summary>点击显示答案</summary>

积分方程：$U_I(t,t_0) = \mathbb 1 - i\int_{t_0}^{t}dt_1\,H_I(t_1)\,U_I(t_1, t_0)$。迭代一次给一阶项 $-i\int_{t_0}^t dt_1 H_I(t_1)$；再迭代一次：

$$U_I = \mathbb 1 + (-i)\int_{t_0}^{t}dt_1\,H_I(t_1) + (-i)^2\int_{t_0}^{t}dt_1\int_{t_0}^{t_1}dt_2\,H_I(t_1)H_I(t_2) + \mathcal O(H_I^3).$$

二阶项的积分区域是三角形 $t_1 \ge t_2$。定义 $T\{H_I(t_1)H_I(t_2)\}$，它把任意 $(t_1, t_2)$ 都排成晚者在前。于是

$$\int_{t_0}^{t}dt_1\int_{t_0}^{t}dt_2\;T\{H_I(t_1)H_I(t_2)\} = \int\!\!\int_{t_1 > t_2} H_I(t_1)H_I(t_2) + \int\!\!\int_{t_2 > t_1} H_I(t_2)H_I(t_1).$$

第二项换积分变量名 $(t_1 \leftrightarrow t_2)$ 后与第一项逐点相同，故方形积分 $= 2 \times$ 三角形积分，即三角形积分 $= \frac{1}{2!}\iint_{\text{方}} T\{\cdots\}$——$1/2!$ 被"$T$ 把 $n!$ 个时序区拼成全空间"吸收。对角线 $t_1 = t_2$ 测度为零，不必关心该处的顺序歧义。于是

$$U_I(t,t_0) = \mathbb 1 + (-i)\int H_I + \frac{(-i)^2}{2!}\iint T\{H_IH_I\} + \cdots = T\exp\Big[-i\int_{t_0}^{t}dt'\,H_I(t')\Big].$$

（$n$ 阶同理：嵌套积分 $= \frac{1}{n!}\times$ $n$ 维方形积分中的编时乘积。）

</details>

**2.** 写出 Wick 定理对 $T\{\varphi_1\varphi_2\varphi_3\varphi_4\}$ 的完整展开（正规乘积 $+ 6$ 个单收缩 $+ 3$ 个双收缩），取真空期望，验证结果与自由理论四点函数 $D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23}$ 一致（$D_{ij} \equiv D_F(x_i - x_j)$）。

<details markdown="1"><summary>点击显示答案</summary>

展开（顶弧标收缩对；单收缩项中未被收缩的算符保持正规序）：

$$T\{\varphi_1\varphi_2\varphi_3\varphi_4\} = \colon\!\varphi_1\varphi_2\varphi_3\varphi_4\!\colon$$

$$+\;\overbrace{\varphi_1\varphi_2}\colon\!\varphi_3\varphi_4\!\colon + \overbrace{\varphi_1\varphi_3}\colon\!\varphi_2\varphi_4\!\colon + \overbrace{\varphi_1\varphi_4}\colon\!\varphi_2\varphi_3\!\colon + \overbrace{\varphi_2\varphi_3}\colon\!\varphi_1\varphi_4\!\colon + \overbrace{\varphi_2\varphi_4}\colon\!\varphi_1\varphi_3\!\colon + \overbrace{\varphi_3\varphi_4}\colon\!\varphi_1\varphi_2\!\colon$$

$$+\;\overbrace{\varphi_1\varphi_2}\,\overbrace{\varphi_3\varphi_4} + \overbrace{\varphi_1\varphi_3}\,\overbrace{\varphi_2\varphi_4} + \overbrace{\varphi_1\varphi_4}\,\overbrace{\varphi_2\varphi_3}.$$

项数 $1 + 6 + 3 = 10 = (4-1)!!$ ✓（一般地 $\sum_k \binom{n}{2k}(2k-1)!! = (n-1)!!$）。取真空期望：正规乘积项与单收缩项（仍含正规乘积）全部为零，只剩三个双收缩项，收缩值 $D_{ij}$：

$$\langle0\rvert T\{\varphi_1\varphi_2\varphi_3\varphi_4\}\rvert 0\rangle = D_{12}D_{34} + D_{13}D_{24} + D_{14}D_{23}.$$

这正是自由理论里"四个振子两两配对传播"的直译——Wick 定理在自由极限退化为第 01 篇的已知结果，是其正确性的最小检验。（注意展开式本身是算符恒等式，不依赖真空期望：右侧每一项都保留着未被收缩的算符结构，供非真空矩阵元使用。）

</details>

**3.** 第 5.2 节的 $105$ 种缩并：独立完成三类计数（$24 + 72 + 9$），写出（b）类六个非连接项中的一个代表并解释其系数 $1/2$；最后解释为什么 $105 = 7!!$。

<details markdown="1"><summary>点击显示答案</summary>

**（a）** 四条外线全部接顶点：第一条外线挑 4 条腿之一，第二条挑剩余 3 条之一……共 $4\times3\times2\times1 = 4! = 24$ 种。系数 $24/4! = 1$，得连接树图 $-i\lambda\int d^4y\,\prod_i D_F(x_i - y)$。

**（b）** 先选接顶点的外线对 $\{i, j\}$：$\binom{4}{2} = 6$ 种；它们在 4 条腿上的分配 $4\times3 = 12$ 种；剩下两条外线互相收缩（1 种）、剩下两条腿互相收缩（1 种）。共 $72$ 种，系数 $72/24 = 3$。代表项（$\{i,j\} = \{1,2\}$）：

$$\frac{-i\lambda}{2}\int d^4y\;D_F(x_1\!-\!y)\,D_F(x_2\!-\!y)\,D_F(0)\;D_F(x_3\!-\!x_4).$$

系数 $1/2$ 的来源：固定 $\{1,2\}$ 后有 $12$ 种缩并给出同一个解析式——$12/4! = 1/2$。等价的图形读法：$y$ 处自缩成环的两条腿互换不改变图，自同构数 $2$，即 $S = 2$。六项 = 六种"哪一对外线进顶点"（$\{12\},\{13\},\{14\},\{23\},\{24\},\{34\}$，注意 $\{12\}$ 进顶点与 $\{34\}$ 进顶点是不同的图——自由飞走的外线对不同）。

**（c）** 外线两两配对 $3$ 种、顶点四腿两两配对 $3$ 种，$9$ 种，系数 $9/24 = 3/8$；解析式为泡泡因子 $\frac{-i\lambda}{8}\int D_F(0)^2$ 乘自由四点函数的三个配对项。

**总数**：8 个对象的完全配对数 $(8-1)!! = 7\times5\times3\times1 = 105$。递归理解：固定一个对象，它与其余 $7$ 个之一配对（$7$ 种），剩下 $6$ 个继续配对 $(6-1)!!$，故 $(8-1)!! = 7\times(6-1)!! = 7\times15$。分类求和 $24 + 72 + 9 = 105$ ✓——三种拓扑穷尽了所有配对，无遗漏无重复。

</details>

**4.** 用两种方法确定对称因子：（i）"8 字"真空泡泡 $S = 8$；（ii）$\phi^4$ 二阶 $2\to2$ 的鱼图（两顶点由两条内线相连）$S = 2$。第二种情形务必说明时序指数的 $\frac{1}{2!}$ 在哪一步进场。

<details markdown="1"><summary>点击显示答案</summary>

**（i）8 字泡泡。** 图形法：图的置换自同构 = 交换两个环（$2! = 2$）$\times$ 每个环的首尾腿互换（每环 $2$，共 $2^2 = 4$），$S = 2\times4 = 8$。Wick 法：一个顶点四腿两两配对 $3$ 种，系数 $3/4! = 1/8$，与 $1/S$ 吻合 ✓。

**（ii）鱼图。** 固定外线分布：$x_1, x_2$ 接顶点 $y$，$x_3, x_4$ 接顶点 $z$，$y, z$ 之间两条内线。Wick 计数（无 $1/2!$ 的裸计数）：$\varphi_1$ 挑 $y$ 的腿 $4$ 种、$\varphi_2$ 挑 $3$ 种、$\varphi_3$ 挑 $z$ 的腿 $4$ 种、$\varphi_4$ 挑 $3$ 种、$y$ 剩两腿与 $z$ 剩两腿配对 $2$ 种，共 $4\cdot3\cdot4\cdot3\cdot2 = 288$ 种。但 Dyson 展开的二阶项带系数 $\frac{1}{2!}\cdot\frac{(-i\lambda)^2}{(4!)^2}$（$1/2!$ 来自 $T$ 指数的展开；它之所以没被吸收掉，是因为完全收缩后的被积函数是 $c$ 数，$y \leftrightarrow z$ 交换下不变——不存在"不同时序区拼成全空间"的增益）。同时，"$x_1x_2$ 在 $y$"与"$x_1x_2$ 在 $z$"两种指派在 $y, z$ 都是全时空哑积分变量后给出相同的积分值。合计每条物理通道：

$$\frac{1}{2!}\cdot\frac{2\ \text{（}y\!\leftrightarrow\! z\text{ 指派）}\times 288}{(4!)^2}\,(-i\lambda)^2 = \frac{(-i\lambda)^2}{2}.$$

即系数 $\frac{1}{2}$，$S = 2$。图形法核验：保持图不变的置换 = 两条平行内线互换（$2$），顶点交换不是独立自同构（它必须连带外线一起动，而外线已固定），$S = 2$ ✓。

一般教训：对称因子 = $\frac{(4!)^v\,v!\,}{\text{ Wick 缩并数}}$ 的残余，等价于图的自同构群阶数；树图（所有腿角色互异）通常 $S = 1$，圈、环、真空结构才开始产生非平凡 $S$。

</details>

**5.** 推导 $\phi^3$ 理论 $2\to2$ 的三通道树图振幅；证明弹性同质量散射的 Mandelstam 恒等式 $s + t + u = 4m^2$；并说明为什么这两个树图的对称因子是 $1$。

<details markdown="1"><summary>点击显示答案</summary>

**振幅。** $s$ 道为例：顶点 $y$ 接 $p_1, p_2$ 与内线（动量 $q = p_1 + p_2$，$q^2 = s$），顶点 $z$ 接 $p_3, p_4$ 与同一内线。按规则：两顶点 $(-ig)^2$、内线 $\frac{i}{s - m^2 + i\epsilon}$，$i\mathcal M_s = \frac{(-ig)^2\, i}{s - m^2 + i\epsilon}$。$t$ 道（内线接 $p_1$ 与 $p_3$，动量 $p_1 - p_3$）与 $u$ 道（$p_1$ 与 $p_4$）同理，求和即得第 8 节的三通道公式。

**恒等式。** $s + t + u = (p_1{+}p_2)^2 + (p_1{-}p_3)^2 + (p_1{-}p_4)^2$。展开（$p_i^2 = m^2$，动量守恒 $p_1 + p_2 = p_3 + p_4$）：

$$= 3m^2 + p_2^2 + p_3^2 + p_4^2 + 2p_1\!\cdot\!(p_2 - p_3 - p_4) = 6m^2 + 2p_1\!\cdot\!(-p_1) = 6m^2 - 2m^2 = 4m^2. \;\blacksquare$$

（关键步 $p_2 - p_3 - p_4 = -p_1$ 直接由守恒移项而来。）

**对称因子。** 数 $s$ 道的 Wick 缩并：$\varphi_1\varphi_2$ 接 $y$ 的腿 $3\times2 = 6$ 种、$\varphi_3\varphi_4$ 接 $z$ 的腿 $6$ 种、$y$ 剩一腿接 $z$ 剩一腿 $1$ 种，共 $36$ 种。二阶系数 $\frac{1}{2!}\cdot\frac{(-ig)^2}{(3!)^2}$，$y\!\leftrightarrow\!z$ 指派贡献因子 $2$：

$$\frac{1}{2}\cdot\frac{2\times36}{36}\,(-ig)^2 = (-ig)^2\quad\Rightarrow\quad S = 1.$$

图形读法：三腿顶点的每条腿角色都不同（两条接指定外线、一条接内线），无可交换的结构。对比 $\phi^4$ 鱼图：多出的两条平行内线正是 $S=2$ 的来源——**对称因子惩罚的是"图里长得一样的部件"**。

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》第 4 章（相互作用绘景、Dyson 展开、Wick 定理、费曼图与费曼规则——本篇母本；§4.6 起的截面公式衔接下一篇）。
- Schwartz《Quantum Field Theory and the Standard Model》第 6–7 章（S 矩阵、编时乘积与费曼规则的协变推导；其第 4 章 old-fashioned 微扰论是历史路线，可对照跳读）。
- Srednicki《Quantum Field Theory》第 9–10 章（微扰展开与费曼图的路径积分推导，记号与本篇一致——与第 07 篇是同一母题的两个入口）。
- D. Tong 量子场论讲义（Cambridge，在线公开）第 3 章 "Interacting Fields"——推导节奏与本篇接近，配有完整习题。
