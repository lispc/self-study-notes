# 因果结构：光锥、Cauchy 面与因果菱形

> 路线图位置：第 2 部分（动力学与解）· 第 7 章
> 前置知识：第 1–3 章（流形、度规、联络、曲率）；第 6 章（Schwarzschild 解的因果结构作为例子）。
> 学习目标：会用 $I^\pm$、$J^\pm$ 描述因果序；能说清全局双曲性为什么等价于"初值问题适定"；会在 Minkowski 中把因果菱形的边界拆成两张零锥 + 两个 cap + 一个角点 $S$；知道"因果菱形"为什么是量子场论里局域代数的标准区域。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。本章的"类时"指 $g(v,v)\lt 0$，"类光"指 $g(v,v)=0$ 且 $v\neq0$，"类空"指 $g(v,v)\gt 0$（零矢量按惯例归入类空）。

## 1. 一句话总结

**度规的因果结构（而不是它的具体分量）决定了"什么能影响什么"。$I^\pm(p)$ 是能用类时曲线到达的点集，$J^\pm(p)$ 是加上类光曲线后的闭包；全局双曲性——存在 Cauchy 面、且任意两点间的因果夹逼 $J^+(p)\cap J^-(q)$ 紧——等价于"给定初始数据，演化唯一确定"。因果菱形 $D=I^+(p)\cap I^-(q)$ 是这套语言里最小的"完整可演化区域"：它的边界是两张零超曲面，二者相交于一个二维角点 $S$。这个形状同时是**零锥初值问题**（第 9 章）与**量子场论局域代数**（[QFT 书第 9 阶段](../../qft-sm/README.md)）的舞台。**

## 2. 因果序

### 2.1 三类矢量与两类曲线

在每点 $p$，切空间被光锥分成三块（号差 $-,+,+,\!+$）：

| 类型 | 条件 | 物理含义 |
|---|---|---|
| 类时 | $g(v,v)\lt 0$ | 有质量粒子的世界线切矢 |
| 类光（零） | $g(v,v)=0,\ v\neq0$ | 光子的世界线切矢 |
| 类空 | $g(v,v)\gt 0$ | 同时刻两点的连线 |

一条曲线叫**类时/类光/因果**曲线，若处处切矢类时/类光/类时或类光。因果曲线允许"分段换类型"，但**不能回头**：一旦选定了时间定向（本章固定为过去 → 未来），因果曲线的时间坐标必须单调。

### 2.2 因果过去与因果未来

对点 $p$，定义

$$I^+(p)=\{q:\ \exists\ \text{从 }p\text{ 到 }q\text{ 的未来指向类时曲线}\},$$

$$J^+(p)=\{q:\ \exists\ \text{从 }p\text{ 到 }q\text{ 的未来指向因果曲线}\}.$$

$I^-(p)$、$J^-(p)$ 反号定义。三个基本事实（本章自检 1 证第一条）：

1. **$I^\pm(p)$ 是开集**。类时曲线可以在每点附近小幅扰动，故 $I^+$ 含邻域。
2. **$I^+(p)\subset J^+(p)$**，且 $J^+$ 是 $I^+$ 的闭包的一部分。一般只有 $I^+\subset J^+\subset\overline{I^+}$；在强因果时空里 $\mathrm{int}\,J^+=I^+$。
3. **全局双曲时空里 $J^\pm(p)$ 是闭集**。这一条不平凡，它等价于"因果夹逼紧"，见 §4。

**为什么区分 $I$ 与 $J$**：$I$ 是开集，方便做微分与极限；$J$ 含类光边界（光锥面本身），是"能否收到信号"的正确答案。$\partial J^+(p)$ 就是过 $p$ 的未来零锥，第 8 章要研究它的几何。

### 2.3 因果性条件的层级

从弱到强：

- **年表性（chronology）**：无闭合类时曲线。等价于 $p\notin I^+(p)$。
- **因果性（causality）**：无闭合因果曲线。比年表性强——它排除了"沿闭合零测地线绕回来"。
- **强因果性**：每点的每个邻域 $U$ 含更小的邻域 $V$，使得没有因果曲线离开 $V$ 后又回到 $V$。它排除了"因果曲线任意接近闭合"的退化情形（如圆柱时空的角向紧致化）。
- **稳定因果性**：在度规的小扰动下仍保持因果性。强因果 + 紧性 ⇒ 稳定因果。
- **全局双曲性**：强因果 + 对任意 $p,q$，$J^+(p)\cap J^-(q)$ 紧。**这是本章的主角。**

## 3. 类空超曲面与法矢

设 $\Sigma$ 是余维 1 的类空超曲面，$n^\mu$ 是它的单位法矢。类空意味着 $n$ 类时，取

$$n^\mu n_\mu=-1,\qquad n^0\gt 0\ (\text{指向未来}).$$

诱导度规（**第一基本形式**）是投影算符

$$\boxed{\;h_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu\;}$$

因为 $h_{\mu\nu}n^\nu=g_{\mu\nu}n^\nu+n_\mu(n\cdot n)=n_\mu-n_\mu=0$。验证它是 $\Sigma$ 上的度规：对任意切于 $\Sigma$ 的 $u,v$，$h(u,v)=g(u,v)$，且号差为 $(+,+,+)$。

**外曲率**（第二基本形式）度量 $\Sigma$ 在时空中的弯曲：

$$K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma .$$

取迹 $K=h^{\mu\nu}K_{\mu\nu}=\nabla_\mu n^\mu$。第 10 章的 GHY 项就是 $\int_{\partial M}\sqrt{h}\,K$。

**符号警告**：$K$ 的符号依赖 $n$ 的取向。把 $n\to-n$ 会翻 $K\to-K$，而 GHY 项必须与 $S_{\rm EH}$ 的符号配合。第 10 章会把这笔账算清。

## 4. 依赖域与 Cauchy 面

### 4.1 依赖域

$$\boxed{\;D^\pm(\Sigma)=\{p:\ \text{每条过 }p\text{ 的过去/未来不可延因果曲线都交 }\Sigma\}.\;}$$

直觉：$D^+(\Sigma)$ 是"$\Sigma$ 上的数据能唯一决定"的区域。$D(\Sigma)=D^+(\Sigma)\cup D^-(\Sigma)$。

### 4.2 Cauchy 面与全局双曲性

**Cauchy 面**是满足 $D(\Sigma)=M$ 的**无因果交**（achronal：任意两点不可类时相连）闭集。等价刻画（Geroch）：

$$\text{全局双曲}\iff \text{存在 Cauchy 面}\iff M\cong\mathbb{R}\times\Sigma\ \text{（拓扑）}.$$

并且全局双曲时空可被一族互不相交的 Cauchy 面叶层化（$t=\text{const}$），每张都是类空超曲面。**ADM 分解（第 11 章）就建立在这个叶层上。**

### 4.3 为什么"全局双曲"是初值问题的正确条件

引力场方程是双曲型 PDE。双曲型方程的基本定理是：**给定 Cauchy 面上的初始数据，解在依赖域内存在且唯一，并对初值连续依赖**。若时空不全局双曲，则要么有"从奇点冒出来"的信息（解不唯一），要么有闭合因果曲线（初值问题病态）。

具体到 GR：

- 类空切片上的初值问题是**约束 + 演化**：$(h_{\mu\nu},K_{\mu\nu})$ 必须满足 Hamiltonian 与动量约束（4 个椭圆方程），满足后才能演化（第 11 章）。
- 零锥上的初值问题是**纯演化**：零超曲面上的数据只受"输运方程"约束，沿生成元积分即可（第 8、9 章）。

**这两条路线的差别，就是论文为什么要选零锥作为边界的技术原因。**

## 5. 因果菱形

### 5.1 定义

设 $q\in I^+(p)$（即 $q$ 在 $p$ 的未来）。**因果菱形**

$$\boxed{\;D\equiv I^+(p)\cap I^-(q).\;}$$

- $p$ 叫**过去顶点**，$q$ 叫**未来顶点**；
- $\partial D$ 由两张零超曲面组成：$H_p=\partial I^+(p)\cap \overline{I^-(q)}$（**出射**零片）与 $H_q=\partial I^-(q)\cap\overline{I^+(p)}$（**入射**零片）；
- 两张零片相交于**角点** $S=H_p\cap H_q$，一般是二维曲面（Minkowski 里是球面）。

### 5.2 Minkowski 里的显式形状

取 $p=(-T,\vec 0)$、$q=(T,\vec 0)$。光锥方程：

$$I^+(p):\ t+T\gt|\vec x|,\qquad I^-(q):\ T-t\gt|\vec x|.$$

于是

$$D=\{|\vec x|\lt T-|t|\},\qquad \partial D=\{|\vec x|=T-|t|\}.$$

把 $|t|$ 拆开：

- $t\le0$：$|\vec x|=t+T$ —— 从 $p$ 发出的出射零锥面 $H_p$；
- $t\ge0$：$|\vec x|=T-t$ —— 向 $q$ 会聚的入射零锥面 $H_q$；
- $t=0$：两式同时成立，$|\vec x|=T$ —— **角点 $S$ 是半径 $T$ 的二维球面**。

**加上 caps**：论文把两个顶点切掉，在 $t=\mp(T-\epsilon)$ 各取一个半径 $\epsilon$ 的小 3-球作 cap。注意一个漂亮的事实：半径 $\epsilon$、球心在 $t=-T+\epsilon$ 的球面，其未来零锥的**外包络**恰好是 $t+T=|\vec x|$（因为 $\min_{|x'|=\epsilon}|\vec x-\vec x'|=|\vec x|-\epsilon$）。所以 caps 只削掉顶点附近，**角点 $S$ 仍是 $|\vec x|=T$ 的球面，与 $\epsilon$ 无关**。这就是论文图 7 的形状：两张零片 + 两个 cap + 一个角点。

### 5.3 为什么是"菱形"

在 $1+1$ 维里，$D$ 就是标准的菱形（两个三角形的并）。在 $3+1$ 维里，每个 $t=\text{const}$ 截面是半径 $T-|t|$ 的球，$t=0$ 处最大。它是"两个光锥的公共部分"，也叫**双锥**。

## 6. 零锥作为边界：双零片

### 6.1 零超曲面的特殊之处

$H_p=\partial I^+(p)$ 是零超曲面。它的法矢 $\ell_a=\nabla_a f$（$f=t+T-|\vec x|$）满足 $g^{ab}\ell_a\ell_b=0$——**法矢自己是零的**。这有一个立刻的推论：

$$\ell^a\nabla_a f=g^{ab}\ell_a\ell_b=0,$$

即**零法矢切于零超曲面**。所以零超曲面不能像类空超曲面那样"沿法矢离开自己"——它的法矢就是它自己的生成元方向。第 8 章整章都在处理这个退化性带来的后果（诱导度规退化、需要辅助零矢 $n$、膨胀与剪切）。

### 6.2 双零片与特征初值

两张零片的并 $H_p\cup H_q$ 叫**双零片**（double null sheet）。它上面的数据是：

- 每张零片上沿生成元的两个函数（出射零片上的"新闻"与面积密度）；
- 角点 $S$ 上的二维数据（共形度规 = 两个偏振 + 面积元）；
- caps 上的数据（面积元与膨胀的初值）。

论文 §3.2 的自由数据正是这个清单：**共形度规给两个偏振，Raychaudhuri 从初值积分出面积**。这些在 [QFT 书第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)有论文层面的复述，本章只负责几何。

### 6.3 为什么不用类空切片

| | 类空切片 $\Sigma$ | 零锥 $H$ |
|---|---|---|
| 约束类型 | Hamiltonian + momentum（椭圆，非局部） | 输运方程（双曲，沿生成元积分） |
| 自由数据 | $h_{ij}$、$K_{ij}$ 满足 4 个约束 | 共形度规 + 面积初值，无椭圆约束 |
| 与"边界数据"的关系 | 边界在无穷远或人为截断 | 边界就是零锥本身，天然带角点 |
| 量子化的入口 | ADM 相空间（第 11 章） | 协变相空间只剩边界项（第 12 章） |

这不是说类空路线错了，而是说**零锥路线让"解约束"变成"解 ODE"**——这是论文能在有限 $G_N$ 下写出约化相空间的前提。

## 7. 全局双曲性的失效与"局域黑洞"

黑洞内部不全局双曲：奇点在未来，事件视界之后的信息不能由外部 Cauchy 面决定。更麻烦的是，**事件视界是全局概念**（要知道整个未来才能判断"能否逃到无穷远"），在量子引力里不好用。

局域的替代品是**边缘陷俘面**（marginally outer trapped surface, MOTS）：一个二维类空曲面，其出射零法矢的膨胀为零、入射零法矢的膨胀为负：

$$\Theta_{(\ell)}=0,\qquad \Theta_{(n)}\lt 0 .$$

这是论文 (5.51) 的定义，也是数值相对论里"找黑洞"的标准做法。它只依赖局部几何，不需要知道整个时空的未来。第 8 章会把 $\Theta$ 讲清楚，第 13 章会用它算黑洞热力学。

## 8. 因果菱形为什么是量子场论的标准区域

在代数量子场论里，给每个区域 $O$ 配一个 von Neumann 代数 $\mathcal{A}(O)$（[QFT 书第 9 阶段 02 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md)）。因果菱形是最常用的一类区域，原因有三：

1. **它是"完整"的**：$D=D''$（取两次因果补不变），所以 $\mathcal{A}(D)$ 是因果完备的代数。
2. **它的模流有几何意义**：在真空中，楔形区域的模哈密顿量是 boost 生成元（Bisognano–Wiedemann）；对共形场论，因果菱形的模流是共形变换。**"boost = 时间演化"这条线索，正是论文用角点 boost 当引力时钟的量子场论前身。**
3. **可缝合**：两个相邻的因果菱形共享一个角点 $S$，缝合条件就是"两侧的角点荷相加为零"（论文 §3.6 的 entangling product）。这是论文把"区域拼接"变成"代数张量积的约束"的技术基础。

## 9. 小结

- 因果结构由 $I^\pm$（类时可达）与 $J^\pm$（因果可达）刻画；$I$ 开、$J$ 含光锥边界。
- 因果性条件层层加强：年表 → 因果 → 强因果 → 稳定因果 → 全局双曲。
- 类空超曲面：法矢类时 $n^2=-1$，诱导度规 $h_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu$，外曲率 $K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma$。
- 全局双曲 ⇔ 存在 Cauchy 面 ⇔ $M\cong\mathbb{R}\times\Sigma$ ⇔ 初值问题适定。
- 因果菱形 $D=I^+(p)\cap I^-(q)$：边界 = 两张零片 $H_p$、$H_q$ + 两个 cap；零片相交于角点 $S$（Minkowski 中是球面）。
- 零超曲面的法矢是零的、且切于自身——诱导度规退化，这是第 8 章的全部困难来源。
- 局域黑洞用 MOTS（$\Theta_{(\ell)}=0,\Theta_{(n)}\lt0$）定义，不依赖事件视界。
- 因果菱形是 QFT 局域代数与模流的标准区域，"角点 boost ↔ 时间"是论文引力时钟的前身。

## 自检问题

**1.** 证明 $I^+(p)$ 是开集；再说明为什么 $J^+(p)$ 一般不必是开集，以及"$J^+$ 闭"需要什么条件。

<details markdown="1"><summary>点击显示答案</summary>

**$I^+$ 开**：设 $q\in I^+(p)$，则存在未来指向类时曲线 $\gamma:[0,1]\to M$，$\gamma(0)=p$，$\gamma(1)=q$。在 $q$ 附近取一个法邻域 $U$（指数映射是微分同胚）。因为 $\gamma$ 在 $q$ 处的切矢 $\dot\gamma(1)$ 类时，且"类时"是切空间里的开条件（$g(v,v)\lt 0$ 是开不等式），存在 $q$ 的邻域 $V\subset U$ 使得对每个 $q'\in V$，从 $\gamma(1-\delta)$ 到 $q'$ 的测地线仍然类时（指数映射连续，$g(\exp^{-1}q',\exp^{-1}q')$ 在 $q'=q$ 处为负，故在小邻域内仍为负）。把 $\gamma|_{[0,1-\delta]}$ 与这段类时测地线接起来，得到 $p\to q'$ 的类时曲线。故 $V\subset I^+(p)$，$I^+$ 开。$\square$

**$J^+$ 不必开**：取类光曲线。在 Minkowski 中 $J^+(0)$ 的边界是光锥面 $t=|\vec x|$，其上每点都是 $J^+$ 的点，但任何邻域都含 $t\lt|\vec x|$ 的类空点（不在 $J^+$ 中）。所以 $J^+$ 有非空边界，不是开集。它的内部才是 $I^+$：$\mathrm{int}\,J^+(p)=I^+(p)$（在强因果时空里成立；一般时空里只能保证 $I^+\subset J^+\subset\overline{I^+}$ 这类包含关系）。

**$J^+$ 闭的条件**：全局双曲。理由是全局双曲时 $J^+(p)\cap J^-(q)$ 对任意 $q$ 紧，取 $q$ 沿时间趋于未来，$J^+(p)$ 是这些紧集的递增并，因而是闭的（在合适的拓扑论证下）。反过来，若 $J^+$ 不闭，就会有"因果曲线跑到边界外"的病态，破坏初值问题的适定性。

**要点**：开/闭的区别不是技术洁癖——$I$ 用来做微分几何（开集上可以取坐标、做扰动），$J$ 用来陈述因果性（信号能否到达）。两者差一个光锥面，而第 8 章整章研究的正是这个面。

</details>

**2.** 证明：若 $\Sigma$ 是 Cauchy 面，则时空无闭合因果曲线。（提示：数一条闭合因果曲线与 $\Sigma$ 的交点。）

<details markdown="1"><summary>点击显示答案</summary>

反证。设 $\gamma$ 是一条闭合因果曲线，即存在 $t_0\lt t_1$ 使 $\gamma(t_0)=\gamma(t_1)=p$，且 $\gamma$ 处处因果、时间定向单调（沿 $\gamma$ 的固有时或仿射参数单调）。

**第一步：$\gamma$ 必与 $\Sigma$ 相交。** 取 $p=\gamma(t_0)$。若 $p\in\Sigma$ 则已相交。否则 $p\in D(\Sigma)$（因为 $D(\Sigma)=M$），故每条过 $p$ 的不可延因果曲线都交 $\Sigma$。$\gamma$ 延长成闭合曲线后可以无限重复，得到一条过 $p$ 的不可延因果曲线，它必须交 $\Sigma$。所以存在 $t_*\in[t_0,t_1]$ 使 $\gamma(t_*)\in\Sigma$。

**第二步：相交只能发生一次。** 若 $\gamma$ 与 $\Sigma$ 交于两个不同点 $\gamma(t_1),\gamma(t_2)$，$t_1\lt t_2$，则 $\gamma$ 在 $t_1$ 与 $t_2$ 之间的段是一条连接这两点的因果曲线，于是这两点因果相关。但 $\Sigma$ 是**无因果交**的（achronal）：$\Sigma$ 上任意两点不可由因果曲线相连。矛盾。

**第三步：闭合曲线必须交两次。** $\gamma$ 从 $p$ 出发，若 $p\notin\Sigma$，它在某个时刻第一次进入 $\Sigma$（记为 $t_*$），之后必须离开 $\Sigma$ 才能回到 $p$；但 $p$ 不在 $\Sigma$ 上。回到 $p$ 后再沿曲线走一圈，又要进入 $\Sigma$——第二次相交。矛盾。若 $p\in\Sigma$，则 $\gamma$ 立即离开 $\Sigma$，绕一圈回来又在 $p\in\Sigma$ 相交，同样两次。矛盾。$\square$

**结论**：Cauchy 面存在 ⇒ 无闭合因果曲线。这条论证说明"全局双曲"比"因果"强得多：它不仅排除闭合曲线，还保证每条因果曲线都被 $\Sigma$ 恰好穿过一次——这正是"初始数据唯一决定演化"的几何内容。

</details>

**3.** 在 Minkowski 时空中取 $p=(-T,\vec 0)$、$q=(T,\vec 0)$，写出 $D$、$\partial D$ 的两张零片、caps 与角点 $S$；验证 $S$ 是二维球面。再说明为什么 caps 的大小不影响 $S$。

<details markdown="1"><summary>点击显示答案</summary>

**光锥与 $D$**：

$$I^+(p)=\{t+T\gt|\vec x|\},\qquad I^-(q)=\{T-t\gt|\vec x|\},$$

$$D=I^+(p)\cap I^-(q)=\{|\vec x|\lt T-|t|\}.$$

**边界**：$\partial D=\{|\vec x|=T-|t|\}$，分成两片：

$$H_p:\ |\vec x|=t+T\ (t\le0),\qquad H_q:\ |\vec x|=T-t\ (t\ge0).$$

$H_p$ 是从 $p$ 发出的未来零锥的外侧；$H_q$ 是会聚到 $q$ 的过去零锥。

**角点**：令两式相等，$t+T=T-t\Rightarrow t=0$，于是

$$S=\{t=0,\ |\vec x|=T\}\cong S^2 .$$

**caps**：在 $t=-T+\epsilon$ 与 $t=T-\epsilon$ 各取球 $\{|\vec x|\le\epsilon\}$。它们是 $D$ 的两个"底/顶"边界，与零片在 $|\vec x|=\epsilon$ 处接上：$t=-T+\epsilon$ 时 $T-|t|=\epsilon$ ✓。

**caps 大小不影响 $S$**：半径 $\epsilon$、球心在 $(\pm(T-\epsilon),\vec 0)$ 的球面，其上一点 $x'$ 到 $x$ 的距离最小值是 $\big||\vec x|-\epsilon\big|$。所以"从球面出发能到达的点"满足 $\big||\vec x|-\epsilon\big|\le t-t_0$，外包络是 $|\vec x|-\epsilon\le t-t_0$，即

$$|\vec x|\le t+T-\epsilon+\epsilon=t+T .$$

**外包络与 $\epsilon$ 无关**，就是从顶点 $p$ 发出的零锥。所以切掉顶点只改变零片的"起点"，不改变它们相交的位置——$S$ 始终是 $|\vec x|=T$ 的球面。$\square$

**为什么这重要**：论文用 caps 截断顶点是为了让零生成元有有限的仿射长度（否则顶点处 $\varrho\to0$，时钟读数无定义）。上面这个计算说明**截断不改变角点 $S$ 的位置**，只改变读时钟的起点——这是 (3.18) 里 $dA|_{\partial\Sigma_i}=\epsilon^2 dA|_S$ 这条边界条件的几何依据。

</details>

**4.** 证明 $H_p=\partial I^+(p)$ 是零超曲面，且其法矢切于自身；再证明生成元是零测地线，并说明仿射参数的意义。

<details markdown="1"><summary>点击显示答案</summary>

**零超曲面**：$H_p$ 是 $f=0$ 的水平集，$f=t+T-|\vec x|$。法矢（用度规升指标前的余矢）

$$\ell_a=\nabla_a f=(1,\hat{\vec x}),\qquad |\hat{\vec x}|=1 .$$

在号差 $(-,+,+,+)$ 下

$$g^{ab}\ell_a\ell_b=-1+|\hat{\vec x}|^2=0 .$$

所以 $H_p$ 是**零**超曲面（法矢类光），不是类空也不是类时。

**法矢切于自身**：

$$\ell^a\nabla_a f=g^{ab}\ell_a\ell_b=0 .$$

$\ell^a\nabla_a f$ 正是"沿 $\ell$ 方向 $f$ 的变化率"，它为零意味着 $\ell$ 落在 $f$ 的等值面上，即 $\ell\in T H_p$。**零超曲面的法矢是它自己的切矢**——这是它与类空超曲面的根本区别。

**生成元是零测地线**：$\ell$ 的积分曲线满足 $\dot x^a=\ell^a$。因为 $\ell_a=\nabla_a f$ 是梯度，

$$\ell^b\nabla_b\ell_a=\ell^b\nabla_a\ell_b=\tfrac12\nabla_a(\ell^2)=0 .$$

所以 $\ell^b\nabla_b\ell^a=0$——积分曲线是**仿射参数化的零测地线**。一般情形（$H$ 由 $\ell^2=0$ 定义而非 $f$ 的梯度）会得到 $\ell^b\nabla_b\ell^a=\kappa\ell^a$，$\kappa$ 叫**非仿射度**；重参数化 $u\to u'$ 可以把 $\kappa$ 消掉，代价是 $\ell\to e^{\int\kappa}\ell$。

**仿射参数的意义**：$\ell^a=(\partial_u)^a$，$u$ 就是沿生成元"走的距离"。在论文里，$u$ 从 cap 上归一化（$u=0$ 在 $\partial\Sigma_0$），在角点 $S$ 读出——**这个读数就是引力时钟**（[QFT 书第 9 阶段 03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)）。$\square$

**补充**：注意 $\ell$ 与 $f$ 的归一化不是唯一的。$f\to e^{\omega}f$ 会给 $\ell\to e^\omega(\ell+f\nabla\omega)$，在 $H_p$ 上 $f=0$，故 $\ell\to e^\omega\ell$——这是生成元的重参数化，对应"选不同的时钟刻度"。论文 (3.27) 用 cap 上的面积元固定这个刻度。

</details>

**5.** 验证 $h_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu$ 是到 $\Sigma$ 上的投影（$h_{\mu\nu}n^\nu=0$，$h_\mu{}^\rho h_{\rho\nu}=h_{\mu\nu}$），并说明为什么 $K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma$ 是对称的。

<details markdown="1"><summary>点击显示答案</summary>

**投影性**：

$$h_{\mu\nu}n^\nu=g_{\mu\nu}n^\nu+n_\mu(n\cdot n)=n_\mu-n_\mu=0 .$$

**幂等性**：

$$h_\mu{}^\rho h_{\rho\nu}=(g_\mu{}^\rho+n_\mu n^\rho)(g_{\rho\nu}+n_\rho n_\nu)
=g_{\mu\nu}+n_\mu n_\nu+n_\mu n_\nu+n_\mu n^\rho n_\rho n_\nu .$$

用 $n^2=-1$：最后一项 $=n_\mu(-1)n_\nu=-n_\mu n_\nu$。合计

$$h_\mu{}^\rho h_{\rho\nu}=g_{\mu\nu}+n_\mu n_\nu=h_{\mu\nu}.\qquad\square$$

**$K$ 的对称性**：$K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma$。反对称部分

$$K_{[\mu\nu]}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_{[\rho}n_{\sigma]} .$$

而 $n$ 是超曲面的法矢，$n_a\propto\nabla_a f$（$f$ 定义 $\Sigma$），故 $\nabla_{[\rho}n_{\sigma]}=0$（梯度的旋度为零，Frobenius 定理的可积性条件）。所以 $K_{[\mu\nu]}=0$，$K$ 对称。$\square$

**几何意义**：$K_{\mu\nu}$ 度量"相邻法矢的差在 $\Sigma$ 上的投影"，即 $\Sigma$ 嵌入时空的弯曲程度。$K=0$ 的超曲面叫**全测地**（测地线留在曲面内），例如 Minkowski 的 $t=\text{const}$ 平面。

**接口**：第 10 章的 GHY 项就是 $K$ 的积分；第 11 章的 ADM 分解用 $h_{ij}$ 与 $K_{ij}$ 作正则变量（$K_{ij}$ 的迹与无迹部分分别是"时间膨胀率"与"剪切"）。

</details>

## 参考

- Wald《General Relativity》第 8 章（因果结构、全局双曲性、Cauchy 面）、第 9 章（奇点定理的因果预备）。
- Hawking & Ellis《The Large Scale Structure of Space-Time》第 6 章（$I^\pm$、$J^\pm$ 的严格性质与因果性条件层级）。
- Carroll《Spacetime and Geometry》第 5 章（因果结构与 Penrose 图）。
- Poisson《A Relativist's Toolkit》第 2 章（零超曲面）、第 9 章（因果菱形与局域黑洞）。
- [QFT 书第 9 阶段 02 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/02-operator-algebras-in-qft.md)（局域代数与因果菱形）、[03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)（JT 引力中的因果菱形与时钟）、[04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)（零锥数据与角点）。
- 论文 arXiv:2611.34924 §1、§3.2（因果菱形作为量子化区域）、§5.3（MOTS 定义 (5.51)）。
