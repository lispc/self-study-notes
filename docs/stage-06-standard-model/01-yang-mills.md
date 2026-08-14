# 非阿贝尔规范理论（Yang–Mills）：协变导数、场强与渐近自由

> 路线图位置：第 6 阶段（标准模型）· 第 1 篇
> 前置知识：QED 的 U(1) 规范不变性与费曼规则（../stage-04-qft-core/05-qed.md）；单圈重整化与跑动耦合（../stage-04-qft-core/06-one-loop-renormalization.md）；SU(N) 群与生成元的基本概念（第 5 阶段）。
> 学习目标：从"定域相位变换"这条唯一假设出发，推出非阿贝尔规范理论的全部经典结构——协变导数、规范场的非标量变换律、场强张量与自耦合——并理解为什么这套理论在高能"渐近自由"、低能"禁闭"。

---

## 1. 一句话总结

**把 QED 的定域 U(1) 相位变换推广为定域 SU(N) 变换，"导数必须协变"这一要求强迫我们引入 $N^2-1$ 个规范场；由于生成元互不对易，规范场自身携带"荷"并彼此相互作用（三/四玻色子顶点），这使得真空的磁响应反号——反屏蔽压倒屏蔽，耦合随能量升高而减小，这就是渐近自由，也是 QCD 与整个标准模型的动力学基石。**

下面把这句话逐层推导出来。全文采用自然单位 $\hbar = c = 1$，度规 $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$。

## 2. 从 QED 的 U(1) 到 SU(N)

### 2.1 回顾：QED 的出发点

QED 的全部规范结构来自一个要求：Dirac 场的**定域**相位变换

$$\psi(x) \;\longrightarrow\; e^{i\alpha(x)}\,\psi(x)$$

应当是理论的对称性。自由拉氏量 $\bar\psi(i\slashed\partial - m)\psi$ 不满足它——因为 $\partial_\mu$ 作用在 $e^{i\alpha(x)}$ 上多出一项 $(\partial_\mu\alpha)$——于是被迫引入规范场 $A_\mu$ 并把普通导数换成协变导数 $D_\mu = \partial_\mu + ieA_\mu$，同时给 $A_\mu$ 配上平移变换律 $A_\mu \to A_\mu - \frac{1}{e}\partial_\mu\alpha$ 把多余的项吃掉。

### 2.2 推广：物质场带着"颜色"指标

现在把单个旋量换成一个 $N$ 分量的旋量列

$$\psi(x) = \begin{pmatrix} \psi_1(x) \\ \vdots \\ \psi_N(x) \end{pmatrix},$$

每个分量本身仍是 Dirac 旋量；新指标是**内禀**的（对 QCD 就是红、绿、蓝三种颜色，$N=3$）。整体变换 $\psi \to U\psi$（$U \in \mathrm{SU}(N)$ 与 $x$ 无关）显然是对称性。1954 年杨振宁与 Mills 的问题是：**能否要求这个变换定域化**——

$$\psi(x) \;\longrightarrow\; U(x)\,\psi(x), \qquad U(x) = e^{i\alpha^a(x) T^a} \in \mathrm{SU}(N)?$$

其中 $T^a$（$a = 1, \dots, N^2-1$）是 $\mathfrak{su}(N)$ 的生成元，取基础表示中的 $N\times N$ 厄米无迹矩阵，满足

$$[T^a, T^b] = i f^{abc}\, T^c, \qquad \mathrm{Tr}\big(T^a T^b\big) = \tfrac12\,\delta^{ab}.$$

$f^{abc}$ 是全反对称的结构常数。对 SU(2)，$T^a = \sigma^a/2$，$f^{abc} = \epsilon^{abc}$——这就是大家熟悉的角动量代数；对 SU(3)，$T^a = \lambda^a/2$（Gell-Mann 矩阵）。

**与 U(1) 的本质区别只有一句话**：U(1) 的"生成元"只有一个且与自身对易，而 $[T^a, T^b] \neq 0$。接下来所有新物理——规范场的非标量变换律、场强里的非线性项、自耦合顶点、渐近自由——全都从这一个对易子长出来。

## 3. 协变导数：用"同方式变换"定出规范场

### 3.1 要求与构造

动能项 $\bar\psi\, i\gamma^\mu \partial_\mu \psi$ 在定域变换下不是不变的：

$$\partial_\mu \big(U\psi\big) = U\,\partial_\mu\psi + (\partial_\mu U)\,\psi,$$

多出来的第二项破坏了不变性。和 QED 一样，补救办法是引入规范场并定义**协变导数**

$$\boxed{D_\mu = \partial_\mu + i g A_\mu^a T^a \equiv \partial_\mu + i g A_\mu}$$

其中 $g$ 是耦合常数，并且引入了**矩阵值规范场**的简写 $A_\mu \equiv A_\mu^a T^a$（$N\times N$ 厄米无迹矩阵）。注意现在需要 $N^2 - 1$ 个规范场 $A_\mu^a$——每个生成元配一个（SU(3) 即 8 个胶子）。

**构造原则**：要求 $D_\mu\psi$ 与 $\psi$ 以**完全相同的方式**变换，

$$D_\mu \psi \;\longrightarrow\; U(x)\, D_\mu \psi,$$

这样 $\bar\psi\, i\gamma^\mu D_\mu \psi$ 才是规范不变的（$\bar\psi \to \bar\psi U^\dagger$，$U^\dagger U = 1$）。

### 3.2 推出规范场的变换律

把要求写成算符形式：变换后的协变导数 $D_\mu' = \partial_\mu + igA_\mu'$ 应满足

$$D_\mu'\, U\psi = U\, D_\mu \psi \qquad \forall\,\psi,$$

即 $D_\mu' = U D_\mu U^{-1}$（协变导数按"伴随"方式变换，像一个好张量）。展开左边：

$$\big(\partial_\mu + igA_\mu'\big) U \psi = (\partial_\mu U)\psi + U\partial_\mu\psi + ig A_\mu' U\,\psi,$$

右边：

$$U\big(\partial_\mu + igA_\mu\big)\psi = U\partial_\mu\psi + ig\, U A_\mu\,\psi.$$

逐项对比，$\partial_\mu\psi$ 项自动相等，剩下

$$(\partial_\mu U) + ig A_\mu' U = ig\, U A_\mu,$$

右乘 $U^{-1}$ 解出

$$\boxed{A_\mu \;\longrightarrow\; U A_\mu U^{-1} + \frac{i}{g}\,(\partial_\mu U)\,U^{-1}}$$

这就是非阿贝尔规范场的变换律。取无穷小变换 $U \simeq 1 + i\alpha^a T^a$，用 $[T^b, T^c] = if^{bca}T^a = if^{abc}T^a$（结构常数循环对称）展开到一阶：

$$\delta A_\mu^a = -\frac{1}{g}\,\partial_\mu \alpha^a - f^{abc}\,\alpha^b A_\mu^c + O(\alpha^2).$$

**与 QED 逐项对比**：

- 第一项 $-\frac{1}{g}\partial_\mu\alpha^a$ 就是 QED 里的平移 $A_\mu \to A_\mu - \frac{1}{e}\partial_\mu\alpha$，每个分量各有一份；
- 第二项 $-f^{abc}\alpha^b A_\mu^c$ 是**全新**的：即使 $\alpha$ 是常数（整体变换），$A_\mu^a$ 也要变！这说明规范场自身携带规范荷——它是伴随表示的矢量（整体变换下 $A_\mu \to U A_\mu U^{-1}$，正是伴随表示的变换方式）。

物理上读作：**光子不带电荷，胶子却带色荷**。这一句话将在第 5 节变成顶点、在第 7 节变成渐近自由。

## 4. 场强张量：曲率、协变而非不变

### 4.1 定义：从协变导数的对易子来

平直时空里普通导数对易 $[\partial_\mu, \partial_\nu] = 0$；协变导数则不然——它的不对易程度正是规范场的"曲率"。直接计算（作用在任意 $\psi$ 上，注意 $A_\mu$ 是矩阵，$\partial_\mu$ 会对它求导）：

$$[D_\mu, D_\nu]\,\psi = ig\big(\partial_\mu A_\nu - \partial_\nu A_\mu\big)\psi + (ig)^2 [A_\mu, A_\nu]\,\psi.$$

于是定义**场强张量**（矩阵值）为

$$[D_\mu, D_\nu] = ig\, F_{\mu\nu}, \qquad \boxed{F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]}$$

写成分量形式 $F_{\mu\nu} = F_{\mu\nu}^a T^a$，用 $[T^b, T^c] = if^{bca}T^a$：

$$F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a - g f^{abc} A_\mu^b A_\nu^c.$$

前两项就是电磁场的 $F_{\mu\nu}$（每个分量一份）；**第三项是纯非阿贝尔的**：场强不再是规范场强度的线性函数，而含有两个规范场的乘积。几何语言里，$A_\mu$ 是纤维丛上的联络，$F_{\mu\nu}$ 是它的曲率——"协变导数绕无穷小闭环一周不平的程度"。

### 4.2 变换律：协变而非不变

由 $D_\mu' = U D_\mu U^{-1}$ 立刻得到

$$[D_\mu', D_\nu'] = U\,[D_\mu, D_\nu]\,U^{-1} \quad\Longrightarrow\quad \boxed{F_{\mu\nu} \;\longrightarrow\; U F_{\mu\nu} U^{-1}}$$

无穷小形式：$\delta F_{\mu\nu}^a = -f^{abc}\alpha^b F_{\mu\nu}^c$，即场强按**伴随表示**变换。

**停下来体会这个区别**：

- QED 中 $F_{\mu\nu}$ 是规范**不变**的，$\vec E$、$\vec B$ 直接就是可观测量；
- Yang–Mills 中 $F_{\mu\nu}^a$ 只是规范**协变**的——它的数值依赖于规范选择，色电场、色磁场本身**不是**规范不变的可观测量。这是非阿贝尔理论里"什么可观测"这个问题的第一道关口（后面讲禁闭时会再遇到）。

### 4.3 拉氏量：唯一（可重整的）选择

$F_{\mu\nu}$ 虽不是不变的，但它的"长度平方"是：取迹后共轭变换相消，

$$\mathrm{Tr}\big(F_{\mu\nu}F^{\mu\nu}\big) \;\longrightarrow\; \mathrm{Tr}\big(U F_{\mu\nu}F^{\mu\nu} U^{-1}\big) = \mathrm{Tr}\big(F_{\mu\nu}F^{\mu\nu}\big).$$

用归一化 $\mathrm{Tr}(T^aT^b) = \frac12\delta^{ab}$，$\mathrm{Tr}(F^2) = \frac12 F_{\mu\nu}^a F^{a\mu\nu}$。于是纯 Yang–Mills 拉氏量为

$$\mathcal{L}_{\mathrm{YM}} = -\frac{1}{4}\, F_{\mu\nu}^a F^{a\mu\nu} = -\frac{1}{2}\,\mathrm{Tr}\big(F_{\mu\nu}F^{\mu\nu}\big),$$

系数 $-1/4$ 的选择使动能项正则归一。耦合物质场就是 $\mathcal{L} = \bar\psi(i\slashed{D} - m)\psi - \frac14 F^a F^a$，规范不变性由构造保证。量纲分析：四维中 $g$ 无量纲，理论可重整（严格证明见参考）。

## 5. 展开 $-\frac14 F^2$：自由场论里自带的相互作用

把 $F_{\mu\nu}^a = (\partial_\mu A_\nu^a - \partial_\nu A_\mu^a) - g f^{abc} A_\mu^b A_\nu^c$ 代入 $-\frac14 F^a F^a$，按 $g$ 的幂次展开：

$$\mathcal{L}_{\mathrm{YM}} = \underbrace{-\frac14\big(\partial_\mu A_\nu^a - \partial_\nu A_\mu^a\big)^2}_{\text{动能项（8 个"自由光子"式传播子）}} \;\underbrace{+\,g\, f^{abc}\,\big(\partial_\mu A_\nu^a\big) A^{b\mu} A^{c\nu}}_{\text{三规范玻色子顶点}} \;\underbrace{-\,\frac{g^2}{4}\, f^{abc} f^{ade}\, A_\mu^b A_\nu^c A^{d\mu} A^{e\nu}}_{\text{四规范玻色子顶点}}.$$

（展开细节：$F^aF^a$ 的交叉项为 $-\frac12 f_{\mu\nu}^a G^{a\mu\nu}$，其中 $f_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a$、$G_{\mu\nu}^a = -gf^{abc}A_\mu^bA_\nu^c$，得 $+\frac{g}{2}f^{abc}f_{\mu\nu}^a A^{b\mu}A^{c\nu}$；再由 $f_{\mu\nu}^a$ 两项交换哑指标后贡献相等，合并为上式的 $g f^{abc}(\partial_\mu A_\nu^a)A^{b\mu}A^{c\nu}$。完整分步推导见自检问题 3。）

**这是本篇最重要的公式之一**。逐条读：

1. **三玻色子顶点** $\propto g f^{abc}$：一个规范玻色子可以辐射/吸收另一个——因为规范场自己带荷，电磁式"发光"过程在纯规范场内部就能发生；
2. **四玻色子顶点** $\propto g^2 f f$：直接的接触散射，没有 QED 类比；
3. **QED 对照**：$\mathcal{L}_{\mathrm{QED}} \supset -\frac14 F^2$ 展开后**只有动能项**，光子之间没有任何顶点——光与光的相互作用要靠费米子圈间接产生（Euler–Heisenberg），是量子效应而非经典顶点。

**结论**：纯 Yang–Mills 理论**没有任何物质场，也是一个相互作用理论**。胶子既是"信使"又是"源"。禁闭与渐近自由这两件 QCD 最深刻的事，种子都埋在这两个自耦合顶点里。

## 6. 量子化：一句话交代

规范场的二次型算符因为有规范冗余而奇异（纯规范方向无动能），路径积分需要对每个规范轨道只数一次：引入**规范固定**项（如协变规范的 $-\frac{1}{2\xi}(\partial_\mu A^{a\mu})^2$）并配合 **Faddeev–Popov 鬼场**——格拉斯曼数的复标量鬼 $c^a$，拉氏量含 $\bar c^a(-\partial^2)\,c^a + g f^{abc}(\partial_\mu\bar c^a) A^{b\mu} c^c$。注意与 QED 不同：由于规范变换律中含 $A$ 自身，FP 行列式**依赖于 $A_\mu$**，鬼场不可省略——它参与圈图并保证 S 矩阵幺正。机制与推导见 ../stage-04-qft-core/07-path-integral.md（QED 里讲过的 FP 手续，把群因子换成非阿贝尔版本即可），此处不展开。

## 7. 渐近自由：反屏蔽与 Nobel 2004

### 7.1 跑动耦合复习

在 ../stage-04-qft-core/06-one-loop-renormalization.md 中已经看到：量子涨落使耦合常数依赖能标 $\mu$，由 $\beta$ 函数 $\beta(g) = \mu\,\mathrm{d}g/\mathrm{d}\mu$ 控制（Wilson 视角：积分掉壳层自由度后有效耦合漂移）。QED 的结果是 $\beta(e) = +e^3/(12\pi^2) + \cdots > 0$：**有效电荷随距离减小而增大**——真空极化的虚 $e^+e^-$ 对像电介质一样**屏蔽**裸电荷，凑近了才看到"裸"的强耦合。

### 7.2 SU(N) 的 $\beta$ 函数：反号

对 SU(N) 规范理论加 $n_f$ 味基础表示 Dirac 费米子，单圈计算（背景场方法最干净，见参考）给出

$$\boxed{\beta(g) = -\,\frac{b_0\, g^3}{16\pi^2} + O(g^5), \qquad b_0 = \frac{11N - 2n_f}{3}}$$

- **$11N/3$** 来自规范玻色子圈（含鬼圈），符号为负——**反屏蔽**；
- **$-2n_f/3$** 来自费米子圈，与 QED 同号（屏蔽），要把渐近自由"拉回去"。

对 QCD（$N = 3$）：$b_0 = 11 - \frac{2n_f}{3} > 0$ 要求 $n_f \leq 16$；现实世界 $n_f = 6$，绰绰有余。于是 $\beta < 0$：耦合随能标升高而**减小**。解 Callan–Symanzik 方程得

$$\alpha_s(Q^2) = \frac{g^2(Q^2)}{4\pi} = \frac{4\pi}{b_0\,\ln(Q^2/\Lambda_{\mathrm{QCD}}^2)},$$

$\Lambda_{\mathrm{QCD}} \sim 200\ \mathrm{MeV}$ 是"跑动累积出来的"内禀能标（维度嬗变：无量纲的 $g$ 换成了有量纲的 $\Lambda$）。$Q \to \infty$ 时 $\alpha_s \to 0$（对数地慢），这就是**渐近自由**。

### 7.3 物理图像：抗磁 vs 顺磁

为什么胶子圈会反号？一个富有启发的类比（Nielsen–Olesen 1981）：

- **QED 真空极化**像电介质：虚偶极子沿外场排列，**屏蔽**电荷。等价地，带电粒子的轨道做圆周运动（回旋轨道），产生反抗外磁场的磁矩——**抗磁**响应，对应 $\beta > 0$。
- **非阿贝尔真空**里，胶子自身带荷又带磁矩。自旋为 1 的带电规范玻色子在色磁场中的基态（最低 Landau 能级）能量为 $E^2 = (2n+1)gB - gS_z B$；$S_z = 1,\ n = 0$ 时 $E^2 = -gB < 0$——能量随磁场**降低**，真空"喜欢"产生色磁场，是自旋磁矩沿外场排列的**顺磁**响应。顺磁（反屏蔽，把色荷"涂开"到周围）与抗磁（屏蔽）竞争，系数 $11/3 \times$（顺磁占优）$-$ $\frac{4}{3}\times\frac{n_f}{2}\times$（抗磁）给出 $b_0$ 的符号：**自旋 1 的顺磁赢了**。

<details markdown="1"><summary>补充说明：Nielsen–Olesen 的"双迈斯纳"直觉</summary>

把上面反过来用，可以直觉地理解禁闭：既然 Yang–Mills 真空对外加色磁场是"顺磁占优、倾向于把场涂开"的介质，那么换一个角度看，它对**色电场**表现为（相对论性对偶意义下的）**抗磁/超导**介质。类比超导体排斥磁场（迈斯纳效应）把磁通挤成 Abrikosov 涡旋管：夸克–反夸克对之间的色电通量被真空挤压成**通量管**，能量正比于管长，$V(r) \sim \sigma r$，$\sigma \sim (420\ \mathrm{MeV})^2$ 为弦张力——拉开夸克需要无穷能量，这就是**禁闭**的图像。磁性超导体的库珀对换成假想的颜色磁单极凝聚，即"**双超导**"（dual superconductor）机制。它是图像而非证明；格点 QCD 的弦张力测量是它的数值证据。

</details>

### 7.4 后果与历史

- **高能**：$Q^2$ 大时 $\alpha_s$ 小，夸克在强子内部近似自由——这**事后合法化**了部分子模型与深度非弹性散射中的 Bjorken 标度（1969 年 SLAC 实验看到质子内部像有自由点状成分），并允许用微扰论计算硬过程。这是下一篇 QCD 笔记（第 3 篇）的起点。
- **低能**：$Q \to \Lambda_{\mathrm{QCD}}$ 时 $\alpha_s$ 变大，微扰论失效——定性上指向禁闭（严格证明仍未完成，是 Clay 千禧问题）。
- **历史**：渐近自由由 Gross 与 Wilczek、Politzer 于 1973 年独立发现，三人获 **2004 年诺贝尔物理学奖**。它恰逢其时地解释了 SLAC 的标度行为，使 QCD 从众多强相互作用候选理论中脱颖而出。

## 8. 小结

U(1)（QED）与 SU(N)（Yang–Mills）的对照：

| 性质 | U(1)（QED） | SU(N)（Yang–Mills） |
|---|---|---|
| 物质场变换 | $\psi \to e^{i\alpha(x)}\psi$ | $\psi \to U(x)\psi$，$U \in \mathrm{SU}(N)$ |
| 规范场个数 | 1（光子） | $N^2 - 1$（如 8 个胶子） |
| 规范场变换 | $A_\mu \to A_\mu - \frac{1}{e}\partial_\mu\alpha$（平移，整体变换下不变） | $A_\mu \to U A_\mu U^{-1} + \frac{i}{g}(\partial_\mu U)U^{-1}$（整体变换下按伴随表示变） |
| 规范场是否带荷 | 不带电 | 带色荷（伴随表示） |
| 场强变换 | 规范**不变**（可观测量） | 规范**协变**：$F \to U F U^{-1}$ |
| 自耦合顶点 | 无 | 三玻色子 $\propto g f^{abc}$；四玻色子 $\propto g^2 f f$ |
| $\beta$ 函数符号（单圈） | $\beta(e) = +e^3/12\pi^2 > 0$（屏蔽） | $\beta(g) = -b_0 g^3/16\pi^2$，$b_0 = \frac{11N - 2n_f}{3}$（反屏蔽，若 $n_f$ 不太大） |
| 红外/紫外行为 | 紫外耦合增大（Landau 极点问题） | 紫外自由、红外强耦合（禁闭） |

要点回顾：

- 一切从"$\psi \to U(x)\psi$ 应为对称性"出发：协变导数 $D_\mu = \partial_\mu + igA_\mu^aT^a$ 与规范场的非标量变换律是被强迫的；
- $F_{\mu\nu} \propto [D_\mu, D_\nu]$ 是曲率，协变而非不变；$-\frac14 F^aF^a$ 规范不变；
- 展开 $-\frac14 F^2$ 自动出现三/四玻色子顶点——**纯规范理论自己就在相互作用**，这是与 QED 的本质差别；
- 胶子自耦合带来反屏蔽，$\beta < 0$ → 渐近自由（Nobel 2004），同时暗示红外禁闭。

## 自检问题

**1.** 从 $D_\mu\psi$ 须与 $\psi$ 同方式变换这一要求出发，完整推导规范场的变换律 $A_\mu \to U A_\mu U^{-1} + \frac{i}{g}(\partial_\mu U)U^{-1}$，并给出无穷小形式。

<details markdown="1"><summary>点击显示答案</summary>

要求 $(D_\mu\psi)' = U(D_\mu\psi)$ 对任意 $\psi$ 成立。左边展开：

$$(\partial_\mu + igA_\mu')(U\psi) = (\partial_\mu U)\psi + U\,\partial_\mu\psi + ig A_\mu' U\psi;$$

右边：

$$U(\partial_\mu + igA_\mu)\psi = U\partial_\mu\psi + ig\, U A_\mu\,\psi.$$

两边都有 $U\partial_\mu\psi$，消去后比较 $\psi$ 的系数：

$$(\partial_\mu U) + ig A_\mu' U = ig\,U A_\mu \quad\Longrightarrow\quad A_\mu' = U A_\mu U^{-1} + \frac{i}{g}(\partial_\mu U)U^{-1}.$$

取 $U = e^{i\alpha^a T^a} \simeq 1 + i\alpha^a T^a$，$U^{-1} \simeq 1 - i\alpha^a T^a$，保留一阶：

$$A_\mu' \simeq A_\mu + i\alpha^b A_\mu^c\,[T^b, T^c] - \frac{1}{g}(\partial_\mu\alpha^a) T^a.$$

用 $[T^b, T^c] = if^{bca}T^a = if^{abc}T^a$（$f$ 循环对称），第二项 $= -f^{abc}\alpha^b A_\mu^c\,T^a$，故

$$\delta A_\mu^a = -\frac{1}{g}\partial_\mu\alpha^a - f^{abc}\alpha^b A_\mu^c.$$

第一项是 QED 平移律的 $N^2-1$ 份拷贝；第二项表明 $A$ 在整体变换（$\alpha$ 常数）下也按伴随表示变换——规范场自己带荷。

</details>

**2.** 从 $[D_\mu, D_\nu]$ 算出 $F_{\mu\nu}$ 的分量表达式，并验证其协变变换律 $F_{\mu\nu} \to UF_{\mu\nu}U^{-1}$。

<details markdown="1"><summary>点击显示答案</summary>

作用在 $\psi$ 上计算（$\partial_\mu$ 是算符，对右边的 $A_\nu\psi$ 用乘积法则）：

$$[D_\mu, D_\nu]\psi = [\partial_\mu + igA_\mu,\ \partial_\nu + igA_\nu]\psi = ig(\partial_\mu A_\nu)\psi - ig(\partial_\nu A_\mu)\psi + (ig)^2(A_\mu A_\nu - A_\nu A_\mu)\psi,$$

纯 $\partial_\mu\partial_\nu\psi$ 项对易相消，而 $\partial_\mu(A_\nu\psi) - A_\nu\partial_\mu\psi = (\partial_\mu A_\nu)\psi$。于是

$$[D_\mu, D_\nu] = ig\big(\partial_\mu A_\nu - \partial_\nu A_\mu + ig[A_\mu, A_\nu]\big) \equiv ig F_{\mu\nu}.$$

代入 $A_\mu = A_\mu^aT^a$，对易子项 $ig[T^b,T^c]A_\mu^bA_\nu^c = ig\cdot if^{bca}A_\mu^bA_\nu^c T^a = -gf^{abc}A_\mu^bA_\nu^c T^a$，得

$$F_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a - g f^{abc}A_\mu^b A_\nu^c.$$

验证变换律：由第 3 节 $D_\mu' = U D_\mu U^{-1}$（即 $D_\mu' (U\psi) = U D_\mu\psi$），于是

$$igF_{\mu\nu}' = [D_\mu', D_\nu'] = U D_\mu U^{-1} U D_\nu U^{-1} - (\mu \leftrightarrow \nu) = U[D_\mu, D_\nu]U^{-1} = ig\, U F_{\mu\nu} U^{-1},$$

即 $F_{\mu\nu} \to UF_{\mu\nu}U^{-1}$。协变而非不变：这与电磁 $F_{\mu\nu}$ 的规范不变性形成对照。

</details>

**3.** 展开 $-\frac14 F_{\mu\nu}^aF^{a\mu\nu}$，写出三玻色子项与四玻色子项中结构常数的收缩方式，并说明为什么 QED 没有对应项。

<details markdown="1"><summary>点击显示答案</summary>

记线性部分 $f_{\mu\nu}^a = \partial_\mu A_\nu^a - \partial_\nu A_\mu^a$，非线性部分 $G_{\mu\nu}^a = -g f^{abc}A_\mu^b A_\nu^c$，则 $F^a = f^a + G^a$ 且

$$-\frac14 F^aF^a = -\frac14 f^a f^a - \frac12 f_{\mu\nu}^a G^{a\mu\nu} - \frac14 G_{\mu\nu}^a G^{a\mu\nu}.$$

**三次项**：

$$-\frac12 f_{\mu\nu}^a\big(-g f^{abc}A^{b\mu}A^{c\nu}\big) = \frac{g}{2} f^{abc}\big(\partial_\mu A_\nu^a - \partial_\nu A_\mu^a\big)A^{b\mu}A^{c\nu} = g f^{abc}\big(\partial_\mu A_\nu^a\big)A^{b\mu}A^{c\nu},$$

最后一步用了第二项交换哑指标 $\mu\leftrightarrow\nu$、$b\leftrightarrow c$ 后 $f^{abc}$ 反对称而 $A^{b\mu}A^{c\nu}$ 对称收缩给出相同贡献。结构：一个导数动量因子 $\times$ 一个 $f^{abc}$ $\times$ $g$。

**四次项**：

$$-\frac14\big(-g f^{abc}A_\mu^bA_\nu^c\big)\big(-g f^{ade}A^{d\mu}A^{e\nu}\big) = -\frac{g^2}{4} f^{abc} f^{ade} A_\mu^b A_\nu^c A^{d\mu} A^{e\nu}.$$

结构：两个 $f$ 收缩 $\times$ $g^2$，无导数（接触相互作用）。

**QED 为什么没有**：U(1) 只有一个生成元且 $[T,T]=0$，等价于 $f^{abc} = 0$，$F_{\mu\nu}$ 严格线性，$-\frac14F^2$ 只含动能项。光子不带电荷，所以不存在光子–光子树级顶点。

</details>

**4.** 用 $b_0$ 的公式判断：SU(3) 规范理论中基础表示 Dirac 费米子加到多少味会失去渐近自由？若为 Weyl 费米子，界限如何变化？

<details markdown="1"><summary>点击显示答案</summary>

渐近自由要求 $\beta(g) = -b_0 g^3/16\pi^2 < 0$，即 $b_0 > 0$。$N = 3$ 时

$$b_0 = \frac{11 \times 3 - 2n_f}{3} = 11 - \frac{2n_f}{3} > 0 \quad\Longleftrightarrow\quad n_f < \frac{33}{2} = 16.5,$$

即 **$n_f \leq 16$ 时渐近自由，$n_f \geq 17$ 时失去**（$b_0 \leq 0$，$\beta \geq 0$，耦合随能标增大——低能自由、紫外病态，像 QED 一样）。

Weyl 费米子自由度是 Dirac 的一半，费米子项减半：$b_0 = \frac{11N - n_f^{(W)}}{3}$（每味 Weyl 贡献 $1$ 而非 $2$），界限变为 $n_f^{(W)} < 33$，即 **33 味 Weyl 费米子**才失去渐近自由。物理上：费米子圈总是屏蔽的（与 QED 同号），味数够多就能压倒胶子的反屏蔽。

</details>

**5.** 为什么 QED 没有渐近自由？把论证建立在顶点结构而非公式记忆上。

<details markdown="1"><summary>点击显示答案</summary>

关键在于**光子自身没有相互作用顶点**。耦合随能标跑动来自量子涨落对"试探电荷受力"的修正，分两类：

1. **费米子圈（真空极化）**：虚 $e^+e^-$ 偶极在外电场中排列，屏蔽裸电荷——近看耦合更强，$\beta > 0$。这是 QED 里**唯一**的单圈来源。
2. **规范玻色子圈**：只有在规范玻色子**自身带荷**时才存在——带荷的规范场涨落同样参与对外荷的响应。

U(1) 的 $f^{abc} = 0$，展开 $-\frac14F^2$ 只有动能项，没有三光子、四光子顶点，光子对电荷源"视而不见"，第 2 类贡献恒为零。于是 $\beta(e) = +e^3/12\pi^2 + O(e^5) > 0$：屏蔽，耦合紫外增大，不存在渐近自由。

反过来，非阿贝尔理论中三/四玻色子顶点（$\propto gf^{abc}$、$g^2ff$）让胶子圈上场；自旋 1 带荷粒子的顺磁（反屏蔽）响应以 $11/3$ 对 $4/3$ 的优势压过费米子的抗磁屏蔽，$\beta$ 反号，渐近自由登场。一句话：**有没有自耦合顶点，决定了 $\beta$ 的符号之争有没有悬念。**

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》第 15 章（15.1–15.3：非阿贝尔规范不变性的几何与拉氏量）与第 16 章（16.1–16.2：相互作用顶点与 Faddeev–Popov；16.5：背景场方法与渐近自由）。
- Schwartz《Quantum Field Theory and the Standard Model》第 25 章（非阿贝尔规范理论）与第 26 章（QCD、$\beta$ 函数与渐近自由的计算）。
- Zee《Quantum Field Theory in a Nutshell》第 IV.5、VII.1 章（Yang–Mills 的结构与渐近自由的直觉）。
- Cheng & Li《Gauge Theory of Elementary Particle Physics》第 8 章（规范理论一般构造与 QCD）。
- Nielsen & Olesen 原始短文之外的教科书式讲解见 Peskin 16.5 末尾及 Schwartz 26 章关于顺磁/抗磁竞争的讨论。
