# 多胶子振幅的隐秘简单性：旋量螺旋度与 Parke–Taylor 公式

> 路线图位置：第 7 阶段（现代振幅方法选学）· 第 1 篇——前沿导览，选学
> 前置知识：第 4 阶段的费曼规则与 S 矩阵（../stage-04-qft-core/03-interactions-and-feynman-rules.md、../stage-04-qft-core/04-s-matrix-lsz-cross-sections.md）；Yang–Mills 的三/四胶子顶点与规范不变性（../stage-06-standard-model/01-yang-mills.md）。不需要超对称。
> 学习目标：看清纯胶子树图散射中费曼图方法失控的两层原因（组合爆炸 + 单张图没有物理意义）；学会无质量旋量螺旋度（spinor-helicity）记号的基本代数；读懂 MHV 振幅的 Parke–Taylor 公式并能逐条做健康检查；知道这条线索通向哪里。

---

## 1. 一句话总结

**纯胶子树图振幅用费曼图算，图数随外线数超指数爆炸（8 胶子约三万张图），且每张图单独规范依赖、螺旋度信息又被极化求和抹掉，答案的简单性完全埋在海量抵消里；换用无质量旋量螺旋度变量后，对称性把三点振幅唯一锁死，全部树图振幅可由递推缝出，最终结果简单得离谱——最典型的 MHV 振幅就是一行 Parke–Taylor 公式。费曼图的复杂是表象，简单才是本质；这就是现代振幅学的起点。**

全文用自然单位 $\hbar = c = 1$，度规 $\eta = \mathrm{diag}(+1,-1,-1,-1)$；所有外动量一律取**出射**约定（入射粒子的动量就是负的出射动量）。

## 2. 灾难现场：费曼图计数

### 2.1 图数爆炸

纯 Yang–Mills 理论只有两个顶点（三胶子 $\propto g f^{abc}$、四胶子 $\propto g^2 ff$，见 ../stage-06-standard-model/01-yang-mills.md 第 5 节），但 $n$ 个胶子树级散射要画的费曼图张数是：

| 外线数 $n$ | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|
| 费曼图张数 | 4 | 25 | 220 | 2485 | 34300 | 559405 | 10525900 |

计数引自 Mangano–Parke 综述与 Elvang–Huang 教材第 1 章。增长是超指数的：就算只用三顶点，把 $n$ 条外线缝成二叉树的方式已有 $\sim(2n-5)!!$ 种（$n=6$ 时 $7!!=105$），再乘上四顶点的插入方式、色因子与 Lorentz 指标的分配。数值计算尚可硬扛，但"理解"在图数面前无望。

### 2.2 比数量更糟的三件事

真正令人不安的不是图多，而是每张图单独没有物理意义：

1. **单图规范依赖。** 只有全部图之和规范不变；每张图都拖着一堆规范相关的项，必须在求和中恰好抵消。改规范或做场重定义，等于把贡献在图之间重新洗牌。
2. **螺旋度结构被抹掉。** 标准流程算到模方 $\sum_{\mathrm{pol}}\lvert\mathcal M\rvert^2$，用 $\sum \epsilon_\mu\epsilon_\nu^* \to -\eta_{\mu\nu} + (\text{规范项})$ 替换——不同螺旋度取值之间存在的惊人简单结构，在这一步被平均掉了。
3. **顶点本身臃肿。** 三胶子顶点含三个 Lorentz 结构（$\eta_{\mu\nu}(k_1-k_2)_\rho$ 之类），四胶子顶点含三对结构常数收缩；每一项单独都不对应任何可测的东西。

一句话：费曼图方法把**局域性**摆在明面上，代价是把答案的简单性埋进抵消里。

### 2.3 悬念：答案却很简单

人们算出的结果却简单得反常。1986 年 Parke 和 Taylor 把当时刚算完的 5、6 胶子振幅结果盯了半天，猜出一个普适公式（Berends–Giele 于 1988 年用递推关系证明）。先剧透结论，符号后面定义：$n$ 个胶子中恰有两个取负螺旋度、其余全正（这叫 **MHV**，极大螺旋度破坏组态）时，色序树图振幅为

$$\mathcal{A}_n^{\mathrm{tree}}\big(1^+\cdots i^-\cdots j^-\cdots n^+\big) \;=\; \frac{\langle ij\rangle^4}{\langle 12\rangle\,\langle 23\rangle\cdots \langle n1\rangle},$$

而"全正"与"只差一个负"的螺旋度组态在树级**恒等于零**。$n=8$ 的三万多张图，加起来就是这一行。本章剩下的任务：把每个符号讲清楚，并理解它为什么必然如此。

（"色序"：先把色因子按 $\mathrm{Tr}(T^{a_1}T^{a_2}\cdots T^{a_n})$ 的轮转次序分解，每个迹的系数称为色序振幅，它只由**平面**取向的图贡献。爆炸式图数的一大部分来自色因子与外线置换，色序之后物理结构才露出来。）

## 3. 无质量运动学的母语：旋量螺旋度

### 3.1 动量是一张 2×2 矩阵

取 $\sigma^\mu = (\mathbf 1, \vec\sigma)$，把四动量映成 $2\times2$ 矩阵

$$p_{a\dot a} \;\equiv\; p_\mu\,(\sigma^\mu)_{a\dot a} \;=\; \begin{pmatrix} p^0-p^3 & -p^1+ip^2 \\ -p^1-ip^2 & p^0+p^3 \end{pmatrix}, \qquad a,\dot a = 1,2,$$

关键性质（自检题 1 证明）：

$$\det p_{a\dot a} = (p^0)^2 - \vec p\,^2 = p^2 = m^2.$$

于是**无质量 ⟺ 行列式为零 ⟺ 秩不超过一**，从而必可分解为两个二分量旋量的外积：

$$p_{a\dot a} = \lambda_a\,\tilde\lambda_{\dot a}.$$

这是全部魔术的开关：无质量运动学的自然变量不是满足约束 $p^2=0$ 的四分量 $p_\mu$，而是**自由的** $2+2$ 分量 $(\lambda,\tilde\lambda)$——在壳条件从约束变成了构造。对实动量，$p_{a\dot a}$ 厄米，$p^0>0$ 时 $\tilde\lambda = +\lambda^*$，$p^0<0$ 时 $\tilde\lambda = -\lambda^*$（差一个相位约定）；一旦允许复动量，$\lambda$ 与 $\tilde\lambda$ 相互独立——这一点在第 4、5 节是命脉。洛伦兹群在此写法下表现为 $SL(2,\mathbb C)$：$\lambda$、$\tilde\lambda$ 各按一个基本表示变换，下面定义的括号是不变量。

### 3.2 两种括号

Lorentz 不变的基本建筑材料只有两种"括号"：

$$\langle ij\rangle \equiv \varepsilon^{ab}\lambda_{ia}\lambda_{jb}, \qquad [ij] \equiv \varepsilon^{\dot a\dot b}\tilde\lambda_{i\dot a}\tilde\lambda_{j\dot b},$$

其中 $\varepsilon$ 是反对称符号（$\varepsilon^{12}=+1$）。它们的性质（自检题 2 证明前三条）：

- 反对称：$\langle ij\rangle = -\langle ji\rangle$，$\langle ii\rangle = 0$；$[\,\cdot\,]$ 同理；
- 回到运动学不变量：$\langle ij\rangle[ji] = 2\,p_i\cdot p_j \equiv s_{ij}$；
- 动量守恒（全部出射）：$\sum_i \lambda_{ia}\tilde\lambda_{i\dot a} = 0$，即 $\sum_i \langle ji\rangle[ik] = 0$ 对任意 $j,k$ 成立；
- Schouten 恒等式：$\langle ij\rangle\langle kl\rangle + \langle ik\rangle\langle lj\rangle + \langle il\rangle\langle jk\rangle = 0$——二分量空间里任意三个旋量线性相关，把 $\lambda_l$ 用 $\lambda_j,\lambda_k$ 展开即得。

每个括号质量量纲为 1。$n$ 点无质量振幅就是这两类括号的有理函数。

### 3.3 小群：螺旋度变成"缩放权重"

观察缩放 $(\lambda,\tilde\lambda) \to (t\lambda,\, t^{-1}\tilde\lambda)$ 保持 $p_{a\dot a}$ 不变——这就是（复化的）小群旋转：$t = e^{i\theta}$ 时正是绕动量轴转 $\theta$ 角。螺旋度为 $h$ 的外线态在此旋转下获得相位 $e^{2ih\theta}$，因此振幅必须满足

$$\mathcal A\big(\dots;\, t\lambda_i,\, t^{-1}\tilde\lambda_i;\, \dots\big) = t^{-2h_i}\,\mathcal A\big(\dots;\, \lambda_i,\tilde\lambda_i;\, \dots\big),$$

胶子 $h = \pm1$，权重 $t^{\mp2}$。**这一条缩放律，加上 Lorentz 不变性和"极点只能来自多粒子中间态"（局域性与幺正性的在壳表述），将在第 4 节把三点振幅完全锁死。** 注意此处没有任何拉氏量输入——这是在壳纲领的胚胎：无质量粒子的 S 矩阵很大程度上由对称性与自洽性决定，而非由某个写下的拉氏量决定。

### 3.4 极化矢量也用旋量写

引入任意参考零动量 $q$（$q \neq p$），螺旋度 $\pm$ 的极化矢量可写成

$$\epsilon^{+}_{\mu}(p;q) = \frac{\langle q|\gamma_\mu|p]}{\sqrt2\,\langle qp\rangle}, \qquad \epsilon^{-}_{\mu}(p;q) = \frac{[q|\gamma_\mu|p\rangle}{\sqrt2\,[qp]},$$

其中 $\langle q|\gamma_\mu|p] \equiv \lambda_q^a\,(\sigma_\mu)_{a\dot a}\,\tilde\lambda_p^{\dot a}$（整体符号各文献约定不同，物理性质不受影响）。三条关键性质：

- $p\cdot\epsilon = 0$：横波性自动成立（$\tilde\lambda_p^{\dot a}\tilde\lambda_{p\dot a} = 0$）；
- $q\cdot\epsilon = 0$，且把 $q$ 换成 $q'$ 只使 $\epsilon_\mu$ 改变一个正比于 $p_\mu$ 的项——即一次规范变换。所以 $q$ 是"每条腿自选的规范"：振幅对所有 $q$ 的独立性正是 Ward 恒等式；实际计算中给每条外线选不同的 $q$，可以让大部分图直接为零；
- 小群权重正确：$\epsilon^\pm \to t^{\pm2}\epsilon^\pm$，正好与上节 $t^{-2h}$ 的约定配套。

## 4. 三点振幅：被锁死的"原子"

树图的终极积木是三点振幅。三个无质量动量全部出射且和为零时，$s_{12} = s_{23} = s_{31} = 0$（例如 $s_{12} = (p_1+p_2)^2 = p_3^2 = 0$），于是每对括号满足 $\langle ij\rangle[ji] = 0$。

- **实动量**：$\tilde\lambda \propto \lambda^*$，两种括号同生同灭，全为零——三点在壳振幅对实动量恒为零。物理上这就是"4D 无质量粒子没有非共线的 $1\to2$ 过程"。
- **复动量**：$\langle\,\rangle$ 与 $[\,]$ 相互独立，可以只有一边为零（例如 $[ij]=0$ 而 $\langle ij\rangle\neq0$，对应 $\tilde\lambda_1 \parallel \tilde\lambda_2 \parallel \tilde\lambda_3$）。正是在复化运动学里，三点振幅成为非平凡的原子。

取 $[\,\cdot\,]=0$ 的分支，考察螺旋度组态 $(1^-2^-3^+)$。要求 Lorentz 不变、质量量纲为 1（$n$ 点树级振幅量纲为 $4-n$）、且极点只能对应这些腿的共线构型，写通式 $c\,\langle12\rangle^\alpha\langle23\rangle^\beta\langle31\rangle^\gamma$，小群权重逐腿给出

$$\alpha+\gamma = 2\ \ (\text{腿 }1,\ h=-1), \qquad \alpha+\beta = 2\ \ (\text{腿 }2), \qquad \beta+\gamma = -2\ \ (\text{腿 }3,\ h=+1),$$

解唯一：$\alpha = 3,\ \beta = \gamma = -1$。于是

$$\boxed{\;\mathcal A(1^-2^-3^+) = g\,\frac{\langle12\rangle^3}{\langle23\rangle\langle31\rangle}\;}$$

（常数由量纲与耦合匹配定出为 $g$，色序约定下吸收群因子。）另一半支对称地给出 $\mathcal A(1^+2^+3^-) = g\,[12]^3/([23][31])$。而全正组态 $(1^+2^+3^+)$：权重方程给出 $\alpha=\beta=\gamma=-1$，结果 $\propto 1/(\langle12\rangle\langle23\rangle\langle31\rangle)$ 量纲为 $-3$，不对，且全是没有任何动量流经过的"极点"，违反局域性，只能为零；$(1^-2^-3^-)$ 同理。

**量纲 + 小群 + Lorentz + 极点结构，唯一锁定三点振幅，连拉氏量都不需要。** 对照费曼图语言里的同一步——"写下三胶子顶点"——那边是含三个 Lorentz 结构的庞然大物，这边是一行有理函数。

## 5. 从原子缝出一切：BCFW 一瞥

2005 年 Britto–Cachazo–Feng–Witten 的把戏：挑两条腿做复形变，例如 $[1\,2\rangle$ 形变

$$\hat\lambda_1 = \lambda_1 + z\lambda_2, \qquad \hat{\tilde\lambda}_2 = \tilde\lambda_2 - z\tilde\lambda_1,$$

它同时保持在壳（每项仍秩一）与动量守恒（验证：$\hat p_1 + \hat p_2 = p_1 + p_2$）。于是振幅成为复变量 $z$ 的有理函数 $\mathcal A(z)$，$\mathcal A(0)$ 是物理答案。极点出现在某个中间传播子被打到在壳处 $\hat P^2(z_P) = 0$，而因子化定理保证留数 = 左右两个低点振幅之积。若 $z\to\infty$ 时 $\mathcal A(z)\to0$（对本例这类形变成立；这是 BCFW 的非平凡技术前提，对规范理论与引力都成立），柯西定理给出

$$\mathcal A(0) = \sum_{\text{极点 }P} \mathcal A_L(z_P)\,\frac{1}{P^2}\,\mathcal A_R(z_P).$$

**全部树图振幅由三点原子递推缝出。**

以 $\mathcal A(1^-2^-3^+4^+)$ 为例：形变后只有 $s_{23}$ 通道的极点依赖 $z$（$s_{12}$ 通道被形变保成常数；而 $s_{34}=s_{12}$、$s_{41}=s_{23}$ 是同一批极点）。该通道唯一的非零螺旋度分配是左 $(\hat 2^-,3^+,\hat P^-)$、右 $(\hat P^+,4^+,\hat 1^-)$——两个三点原子缝一次：

$$\mathcal A(1^-2^-3^+4^+) = \mathcal A\big(\hat 2^- 3^+ \hat P^-\big)\,\frac{1}{s_{23}}\,\mathcal A\big(\hat P^+ 4^+ \hat 1^-\big) \;=\; \frac{\langle12\rangle^4}{\langle12\rangle\langle23\rangle\langle34\rangle\langle41\rangle},$$

末等号代入极点位置 $z_* = [32]/[31]$ 后用 Schouten 恒等式化简即得（几步直接但繁琐的代数，完整写出见 Elvang–Huang 例 3.1）。归纳上去就是一般的 Parke–Taylor 公式。同一递推也立刻解释了"全正/单负为零"：三点原子里没有这些组态，缝不出来。

## 6. Parke–Taylor 公式的健康检查

再把公式请出来：

$$\mathcal{A}_n^{\mathrm{tree}}\big(1^+\cdots i^-\cdots j^-\cdots n^+\big) \;=\; \frac{\langle ij\rangle^4}{\langle 12\rangle\,\langle 23\rangle\cdots \langle n1\rangle}.$$

逐条体检（细节留作自检题）：

- **量纲**：分子 4 个括号、分母 $n$ 个括号，总量纲 $4-n$ ✓；
- **小群权重**：普通正螺旋度腿只出现在分母两个括号里，权重 $t^{-2}$（$h=+1$ ✓）；$i,j$ 两条负螺旋度腿由分子补回 $t^4$，净权重 $t^{+2}$（$h=-1$ ✓）；
- **轮转不变**：分母就是一圈括号，色序振幅要求的循环对称性显然 ✓；
- **软极限**：$p_{n+1}\to0$ 时 $\mathcal A_{n+1} \to \dfrac{\langle n1\rangle}{\langle n,n{+}1\rangle\langle n{+}1,1\rangle}\,\mathcal A_n$——正是 Weinberg 软定理的旋量形式 ✓；
- **多粒子因子化**：$s_{k,k+1}\to0$ 极点处分解为低阶振幅之积（自检题 5 验证一个例子）✓。

对照一下：这五条性质在费曼图语言里**没有一条是显然的**，每一条都靠图与图之间的抵消实现。还要强调：公式里没有 $\epsilon$、没有 $q$、没有色因子——规范冗余从第一行起就不在场。

## 7. 这一切意味着什么

- **两种"显然"的对峙。** 费曼图让局域性与幺正性显然，把简单性藏起来；旋量螺旋度加在壳递推让简单性显然，局域性与幺正性反而成了要证明的定理。有没有一种表述，让所有性质同时成为几何定理？这正是"正几何"纲领的问题意识——而它的主场在 N=4 超对称 Yang–Mills，下一篇见。
- **这不是玩具竞赛的技术。** 圈层面的推广（广义幺正性等）正是今天 LHC 上 NNLO QCD 计算的主力语言之一——路线图终点自测里"看懂 NNLO 截面"那条，走到深处会回到本篇的符号。
- **诚实的边界。** 本篇全部是树级、纯胶子、色序之后的振幅。夸克与有质量外线有系统的推广（massive spinor-helicity），圈图层面有广义幺正性与被积函数技术；Elvang–Huang 教材是标准入口。

## 小结

- 纯胶子树图的费曼图数超指数爆炸（$n=8$ 达 34300 张），且单图规范依赖、螺旋度结构被极化求和抹掉；爆炸是表象，Parke–Taylor 的一行公式才是本质。
- 无质量动量分解为旋量对 $p_{a\dot a} = \lambda_a\tilde\lambda_{\dot a}$；$\langle ij\rangle$、$[ij]$ 是全部建筑材料；小群缩放把螺旋度变成权重 $t^{-2h}$。
- 三点振幅被对称性唯一锁死，$\mathcal A(1^-2^-3^+) = g\langle12\rangle^3/(\langle23\rangle\langle31\rangle)$；BCFW 复形变把全部树图由三点原子递推缝出。
- Parke–Taylor：MHV 振幅 $= \langle ij\rangle^4/(\langle12\rangle\langle23\rangle\cdots\langle n1\rangle)$；全正与单负组态为零；量纲、权重、轮转、软极限、因子化逐条体检通过。

## 自检问题

**1.** 证明 $\det(p_\mu\sigma^\mu) = p^2$，从而无质量动量对应的 $2\times2$ 矩阵秩不超过 1，必可写成 $\lambda_a\tilde\lambda_{\dot a}$；并说明实正能动量时 $\tilde\lambda$ 与 $\lambda^*$ 的关系。

<details markdown="1"><summary>点击显示答案</summary>

直接算行列式：

$$\det\begin{pmatrix} p^0-p^3 & -p^1+ip^2 \\ -p^1-ip^2 & p^0+p^3 \end{pmatrix} = (p^0-p^3)(p^0+p^3) - \big(p^1-ip^2\big)\big(p^1+ip^2\big) = (p^0)^2-(p^3)^2-(p^1)^2-(p^2)^2 = p^2.$$

$p^2 = 0$ ⟺ 行列式为零 ⟺ 两行（列）线性相关 ⟺ 矩阵可写成外积 $p_{a\dot a} = \lambda_a\mu_{\dot a}$。

对实动量，$p_{a\dot a}$ 厄米（$(\sigma^\mu)_{a\dot a}$ 厄米、$p_\mu$ 实），于是 $\lambda_a\mu_{\dot a}$ 厄米，这迫使 $\mu = e^{i\phi}\lambda^*$。再看迹：$\mathrm{tr}\,p_{a\dot a} = 2p^0$，而 $\mathrm{tr}(\lambda\mu^T) \sim \lVert\lambda\rVert^2$ 正定的符号由 $e^{i\phi}$ 决定——$p^0>0$ 要求正号，$p^0<0$ 要求负号。取相位约定即 $\tilde\lambda = \pm\lambda^*$（$\pm$ 对应 $p^0$ 的符号）。剩余的自由度 $\lambda \to e^{i\varphi}\lambda$、$\tilde\lambda \to e^{-i\varphi}\tilde\lambda$ 不改变 $p$——正是小群旋转。

</details>

**2.** 从括号的定义出发证明：(i) $\langle ij\rangle = -\langle ji\rangle$；(ii) $\langle ij\rangle[ji] = 2\,p_i\cdot p_j$；(iii) $\sum_i \langle ji\rangle[ik] = 0$。

<details markdown="1"><summary>点击显示答案</summary>

(i) $\varepsilon^{ab}$ 反对称：$\langle ij\rangle = \varepsilon^{ab}\lambda_{ia}\lambda_{jb} = -\varepsilon^{ab}\lambda_{ib}\lambda_{ja} = -\langle ji\rangle$（旋量是普通交换的复数，即" commuting 旋量"）。

(ii) 用显式参数化。对 $E>0$ 的实无质量动量 $p^\mu = E(1,\hat n)$，$p_\mu\sigma^\mu = E(1-\hat n\cdot\vec\sigma)$。取 $\hat n\cdot\vec\sigma$ 的本征值为 $-1$ 的单位本征旋量 $\chi$（自旋指向 $-\hat n$），则 $1-\hat n\cdot\vec\sigma = 2\,\chi\chi^\dagger$，故

$$\lambda = \sqrt{2E}\,\chi, \qquad \tilde\lambda = \sqrt{2E}\,\chi^*.$$

于是 $\langle ij\rangle = 2\sqrt{E_iE_j}\,\det(\chi_i,\chi_j)$，$[ji] = 2\sqrt{E_iE_j}\,\det(\chi_j^*,\chi_i^*) = 2\sqrt{E_iE_j}\,\big(\det(\chi_i,\chi_j)\big)^*$，乘积为

$$\langle ij\rangle[ji] = 4E_iE_j\,\big\lvert\det(\chi_i,\chi_j)\big\rvert^2.$$

而 $\det(\chi_i,\chi_j) = \langle\chi_i^c|\chi_j\rangle$（$\chi_i^c = \varepsilon\chi_i^*$，自旋指向 $+\hat n_i$；$\chi_j$ 指向 $-\hat n_j$），自旋-$1/2$ 的重叠公式给出 $\lvert\langle\chi_i^c|\chi_j\rangle\rvert^2 = (1+\hat n_i\cdot(-\hat n_j))/2 = (1-\hat n_i\cdot\hat n_j)/2$。代回：

$$\langle ij\rangle[ji] = 4E_iE_j\cdot\frac{1-\hat n_i\cdot\hat n_j}{2} = 2E_iE_j(1-\hat n_i\cdot\hat n_j) = 2\,p_i\cdot p_j.$$

(iii) 全部出射约定下动量守恒即 $\sum_i p_{i,a\dot a} = \sum_i \lambda_{ia}\tilde\lambda_{i\dot a} = 0$。左乘 $\varepsilon^{ba}\lambda_{jb}$、右乘 $\varepsilon^{\dot b\dot a}\tilde\lambda_{k\dot b}$ 收缩，即得 $\sum_i\langle ji\rangle[ik] = 0$。

</details>

**3.** 用小群权重与量纲推出 $\mathcal A(1^-2^-3^+)$ 的形式，并证明 $\mathcal A(1^+2^+3^+) = 0$（复化运动学，$[\,\cdot\,]=0$ 分支）。

<details markdown="1"><summary>点击显示答案</summary>

设 $\mathcal A = c\,\langle12\rangle^\alpha\langle23\rangle^\beta\langle31\rangle^\gamma$（Lorentz 不变的 holomorphic 量只能由 $\langle ij\rangle$ 构成；有理形式是局域性所允许的极点结构的唯一候选——多点共线不存在时只可能有这三对腿的共线极点）。

**小群权重**：腿 $i$ 的权重 = 含 $\lambda_i$ 的括号次数之和，须等于 $-2h_i$：

- 腿 1（$h=-1$）：$\alpha+\gamma = +2$；
- 腿 2（$h=-1$）：$\alpha+\beta = +2$；
- 腿 3（$h=+1$）：$\beta+\gamma = -2$。

三式相加：$2(\alpha+\beta+\gamma) = 2$，即 $\alpha+\beta+\gamma = 1$——量纲自动为 1，与"树级 $n$ 点振幅量纲 $4-n$"一致，无需额外约束。解得 $\alpha = 3,\ \beta = \gamma = -1$，即

$$\mathcal A(1^-2^-3^+) = c\,\frac{\langle12\rangle^3}{\langle23\rangle\langle31\rangle},$$

与 QCD 拉氏量三点顶点的直接计算对比定出 $c = g$（色序约定）。

**全正组态**：权重方程变为 $\alpha+\gamma = -2$、$\alpha+\beta = -2$、$\beta+\gamma = -2$，解得 $\alpha=\beta=\gamma=-1$，候选 $\propto 1/(\langle12\rangle\langle23\rangle\langle31\rangle)$。它量纲为 $-3$，与要求的 $+1$ 矛盾（三层括号极点却无任何传播子动量可供流动）；更重要的是这些"极点"不对应任何多粒子中间态——在实运动学极限下三点运动学整个退化。故唯一自洽的取值是 $\mathcal A(1^+2^+3^+) = 0$。

</details>

**4.** 对 Parke–Taylor 公式做体检：验证量纲、轮转对称性与逐腿小群权重；并推出 $p_{n+1}\to0$ 时的软因子。

<details markdown="1"><summary>点击显示答案</summary>

**量纲**：每个括号量纲 1。分子 $\langle ij\rangle^4$ 为 4；分母 $\langle12\rangle\cdots\langle n1\rangle$ 共 $n$ 个括号为 $n$。总量纲 $4-n$，正是 $n$ 点树级振幅（LSZ 后的约化振幅）的质量量纲。✓

**轮转**：分母括号沿 $1\to2\to\cdots\to n\to1$ 走一圈，循环移位 $i\to i+1$ 后公式不变（MHV 位置 $i,j$ 同步平移）。✓

**小群权重**：腿 $k$（$k\neq i,j$，$h=+1$）只出现在 $\langle k-1,k\rangle$ 与 $\langle k,k+1\rangle$ 中，共 2 次且在分母，权重 $t_k^{-2} = t_k^{-2h_k}$ ✓。腿 $i$（$h=-1$）：分母 2 次、分子 4 次，净 $t_i^{+2} = t_i^{-2h_i}$ ✓；腿 $j$ 同理。

**软极限**：取正螺旋度软胶子 $n+1$，夹在 $n$ 与 $1$ 之间（色序相邻）。Parke–Taylor 分母中含 $n+1$ 的因子是 $\langle n,n{+}1\rangle\langle n{+}1,1\rangle$。软极限 $p_{n+1}\to0$ 即 $\lambda_{n+1}\to0$ 与 $\tilde\lambda_{n+1}\to0$ 同时（实软动量），于是

$$\mathcal A_{n+1} = \frac{\langle ij\rangle^4}{\langle12\rangle\cdots\langle n,n{+}1\rangle\langle n{+}1,1\rangle\cdots} \;\longrightarrow\; \frac{\langle n1\rangle}{\langle n,n{+}1\rangle\langle n{+}1,1\rangle}\;\mathcal A_n,$$

其中把分母的 $\langle n,n{+}1\rangle\langle n{+}1,1\rangle$ 换成 $\langle n1\rangle$ 补上 $\mathcal A_n$ 的分母缺口。前置因子 $S(n,n{+}1,1) = \langle n1\rangle/(\langle n,n{+}1\rangle\langle n{+}1,1\rangle)$ 正是 Weinberg 软胶子因子的旋量形式（用 $s_{ij} = \langle ij\rangle[ji]$ 可改写成熟悉的 $\dfrac{p_n\cdot\epsilon}{p_n\cdot p_{n+1}} - \dfrac{p_1\cdot\epsilon}{p_1\cdot p_{n+1}}$ 的共线 eikonal 形）。

</details>

**5.** 在 $s_{45}\to0$ 处验证 Parke–Taylor 的因子化：取复运动学中 $\langle45\rangle\to0$ 的分支，证明 $\mathcal A_5^{\mathrm{MHV}}(1^-2^-3^+4^+5^+)$ 等于 $\mathcal A_4\times\dfrac{1}{s_{45}}\times\mathcal A_3$（整体符号由传播子的 $i$ 与 $\lvert-P\rangle$ 的相位约定吸收）。

<details markdown="1"><summary>点击显示答案</summary>

$\langle45\rangle = 0$ 意味 $\lambda_4 \parallel \lambda_5$，写 $\lambda_5 = c\,\lambda_4$。中间动量 $P = p_4+p_5$ 在此分支上自动在壳：

$$P_{a\dot a} = \lambda_{4a}\big(\tilde\lambda_{4\dot a} + c\,\tilde\lambda_{5\dot a}\big),$$

即 $\lambda_P = \lambda_4$、$\tilde\lambda_P = \tilde\lambda_4 + c\tilde\lambda_5$，且 $s_{45} = \langle45\rangle[54] \to 0$。

**右边**：因子化通道中 4、5 两条腿同取 $+$，三点振幅为 $\mathcal A_3(4^+5^+(-P)^-) = [45]^3/([5(-P)][(-P)4])$（取相位约定 $\lvert(-P)] = -\lvert P]$）。计算括号：

$$[5P] = [54] + c[55] = [54], \qquad [P4] = [44] + c[54] = c[54],$$

故 $\mathcal A_3 = [45]^3/(c[45]^2) = [45]/c$。另一侧是 MHV 四点振幅，用 $\lambda_P = \lambda_4$ 即 $\langle3P\rangle = \langle34\rangle$、$\langle P1\rangle = \langle41\rangle$：

$$\mathcal A_4(1^-2^-3^+P^+) = \frac{\langle12\rangle^4}{\langle12\rangle\langle23\rangle\langle3P\rangle\langle P1\rangle} = \frac{\langle12\rangle^4}{\langle12\rangle\langle23\rangle\langle34\rangle\langle41\rangle}.$$

乘起来除以 $s_{45} = \langle45\rangle[54] = -\langle45\rangle[45]$：

$$\mathcal A_4\,\frac{1}{s_{45}}\,\mathcal A_3 = -\,\frac{\langle12\rangle^4}{c\,\langle12\rangle\langle23\rangle\langle34\rangle\langle41\rangle\langle45\rangle}.$$

**左边**：直接对五点公式取同一极限，用 $\langle51\rangle = c\langle41\rangle$：

$$\mathcal A_5 = \frac{\langle12\rangle^4}{\langle12\rangle\langle23\rangle\langle34\rangle\langle45\rangle\langle51\rangle} = \frac{\langle12\rangle^4}{c\,\langle12\rangle\langle23\rangle\langle34\rangle\langle45\rangle\langle41\rangle}.$$

两边只差一个整体符号——它正是因子化定理中 $i/s_{45}$ 的 $i$ 与 $\lvert-P\rangle$ 相位约定所吸收的部分（不同教科书约定相反，物理截面不受影响）。等式成立。✓ 注意整个检验只用了旋量代数，没有画一张图。

</details>

## 参考

- Elvang & Huang《Scattering Amplitudes in Gauge Theory and Gravity》(Cambridge, 2015；arXiv:1308.1697)：第 1 章（图数爆炸计数与动机）、第 2 章（旋量螺旋度形式）、第 3 章（BCFW 递推与四点例子）——本篇的技术母本。
- Mangano & Parke, Phys. Rept. 200 (1991) 301：多部分子振幅经典综述（图数计数表与 helicity 方法的早期形态）。
- Parke & Taylor, Phys. Rev. Lett. 56 (1986) 2459（MHV 公式原始论文）；Berends & Giele, Nucl. Phys. B306 (1988) 759（递推证明）。
- Britto, Cachazo, Feng & Witten, Phys. Rev. Lett. 94 (2005) 181602（BCFW 原文）；Witten, Commun. Math. Phys. 252 (2004) 189（hep-th/0312171，扭量弦——振幅简单性的几何源头之一）。
- Dixon, TASI 1995 讲义（hep-ph/9601359）：计算导向的 helicity 技术入门。
- Schwartz《Quantum Field Theory and the Standard Model》第 27 章：同一内容的标准教科书讲法，可与本篇互参。
