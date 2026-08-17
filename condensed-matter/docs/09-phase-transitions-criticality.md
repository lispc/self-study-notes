# 相变与临界现象：Landau 理论与重整化群

> 本书位置：凝聚态物理入门导论 第 9 章（第二部分：相互作用、序与相变）。
> 前置知识：第 7 章[磁性](07-magnetism.md)（Ising 模型、平均场近似）；统计力学基础（配分函数、自由能、关联函数）。
> 学习目标：会用 Landau 自由能推出平均场临界指数；会用 Ginzburg 判据判断平均场何时失效；理解普适性与标度律；抓住 Wilson 重整化群的图像——块自旋、耦合流、不动点，并看清它与 QFT 跑动耦合是同一套数学。

---

约定：本书保留 $k_B$。本章几乎全是经典统计力学（临界涨落是热涨落而非量子涨落），$\hbar$ 基本不出现；记约化温度

$$t \equiv \frac{T - T_c}{T_c},$$

临界点对应 $t = 0$。

## 1. 一句话总结

**趋近连续相变的临界点时，关联长度发散，一切微观细节被"洗掉"，系统只剩少数几个临界指数；Landau 理论用对称性写下序参量的多项式自由能，给出平均场指数，这只在上临界维度 $d \ge 4$ 以上正确；$d < 4$ 时涨落不可忽略，Wilson 重整化群揭示了真正的机制——临界指数由标度变换下耦合常数流的不动点决定，因此只依赖空间维度与序参量对称性（普适类），这正是 QFT 中跑动耦合与重整化的同一套数学，在这里获得最清晰的物理诠释。**

下面把这句话逐层拆开。

## 2. 相变的分类与序参量

**一级相变 vs 连续相变。** Ehrenfest 的分类看自由能的导数：一级相变中自由能本身连续、一阶导数（熵、体积、磁化强度）跳变——有潜热、两相共存，如水的沸腾；连续相变中一阶导数连续，二阶及以上（比热、磁化率、压缩率）发散或不连续，如铁磁体在 Curie 点退磁。现代语言更本质：**连续相变 = 临界点处关联长度 $\xi$ 发散的相变**。这条发散的 $\xi$ 是本章全部故事的发动机。

**序参量（order parameter）。** 连续相变的标志是某个量在高温相为零、低温相非零，这个量叫序参量：

- 铁磁体：磁化强度 $m$（零场下 $T > T_c$ 时 $m=0$，$T<T_c$ 时 $m \neq 0$）；
- 气液临界点：密度差 $\rho - \rho_c$；
- 超导/超流：复序参量 $\psi$（见第 8 章）。

序参量非零意味着**自发对称破缺**：哈密顿量具有对称群 $G$（Ising 模型的 $\mathbb{Z}_2$、Heisenberg 模型的 $O(3)$、超导的 $U(1)$），高温相保持全部 $G$，低温相的基态只保持某个子群 $H$。序参量的**对称性质**（是标量、矢量还是复数，分量数 $n$ 是几）是后面一切分类的输入数据——临界指数只依赖它和维度 $d$，与微观相互作用细节无关。

## 3. Landau 理论：对称性写下的自由能

### 3.1 展开式：对称性决定允许项

Landau 的思想惊人地朴素：在 $T_c$ 附近序参量 $m$ 很小，假设自由能是 $m$ 的解析函数，做泰勒展开；**对称性禁戒的项不许出现**。对 Ising 型铁磁体，零场时哈密顿量在 $m \to -m$ 下不变（$\mathbb{Z}_2$），展开只允许偶次项：

$$F(m) = F_0 + a(T-T_c)\,m^2 + b\,m^4 - h\,m, \qquad a > 0,\ b > 0,$$

其中 $h$ 是外磁场（与 $m$ 共轭的场），它显式破缺 $\mathbb{Z}_2$ 所以线性项只有乘上 $h$ 才合法。各系数的原则：

- $a > 0$：高温时 $m=0$ 是极小；系数 $a(T-T_c)$ 在 $T_c$ 处变号是相变的全部驱动；
- $b > 0$：保证大 $m$ 时自由能上升、系统稳定（若 $b < 0$ 就必须加 $m^6$ 项，而 $b$ 变号正是**一级相变**的 Landau 描述）；
- 解析性假设是 Landau 理论的软肋——它本质上假设自由能无奇异性，所以它能给出的临界行为必然是"平均场式"的。

换一个系统，对称性换一套允许项：液晶的序参量是无迹张量 $Q_{ij}$，可以构造三次不变量 $\mathrm{tr}\,Q^3$，于是向列相转变是一级的；超导的 $\psi$ 是复数，规范不变性只允许 $\lvert\psi\rvert^2$、$\lvert\psi\rvert^4$——"对称性决定允许项"是 Landau 理论真正的干货。

### 3.2 自发对称破缺的双井图像

平衡态由自由能极小决定，$\partial F/\partial m = 0$ 给出**状态方程**

$$2a(T-T_c)\,m + 4b\,m^3 = h. \tag{$\ast$}$$

令 $h = 0$，得 $m\big(2at + 4bm^2\big) = 0$：

- $t > 0$（$T > T_c$）：唯一实解 $m = 0$；$F$ 是单井，井底在原点。
- $t < 0$（$T < T_c$）：$m=0$ 处二阶导数 $2at < 0$，变成极大；新的极小出现在

$$m^2 = -\frac{at}{2b} = \frac{a\lvert t\rvert}{2b}, \qquad m = \pm\sqrt{\frac{a\lvert t\rvert}{2b}}.$$

$F$ 变成对称的双井。系统必须选一个井安家：选 $+$ 还是选 $-$ 不由哈密顿量决定（它对两者一视同仁），而由偶然的历史（涨落、无穷小外场）决定——这就是自发对称破缺的 Landau 图像，也就是第 7 章磁性篇中零场下 $m \neq 0$ 的热力学根源。两井之间不能连续地互相转化而不爬过势垒，这正是"对称性真的破了"的操作含义。

### 3.3 平均场临界指数：完整推导

**$\beta = 1/2$（序参量如何随 $t$ 长出来）。** 由上式，$t \to 0^-$ 时

$$m \propto \lvert t\rvert^{1/2} \;\Longrightarrow\; \beta = \tfrac12.$$

**$\delta = 3$（临界等温线）。** 令 $t = 0$，状态方程 $(\ast)$ 化为 $4bm^3 = h$，即

$$m = \left(\frac{h}{4b}\right)^{1/3} \propto h^{1/\delta} \;\Longrightarrow\; \delta = 3.$$

**$\gamma = 1$（磁化率发散）。** 把状态方程 $(\ast)$ 对 $h$ 求导（$\chi \equiv \partial m/\partial h$）：

$$2at\,\chi + 12 b m^2\,\chi = 1 \;\Longrightarrow\; \chi = \frac{1}{2at + 12bm^2}.$$

- $t > 0$：$m = 0$，$\chi = \dfrac{1}{2a}\,t^{-1}$；
- $t < 0$：代入 $m^2 = a\lvert t\rvert/(2b)$，分母 $= -2a\lvert t\rvert + 6a\lvert t\rvert = 4a\lvert t\rvert$，$\chi = \dfrac{1}{4a}\lvert t\rvert^{-1}$。

两侧都是 $\chi \propto \lvert t\rvert^{-1}$，故 $\gamma = \gamma' = 1$；附带得到一个可检验的**振幅比** $C^+/C^- = 2$。

**比热：跳变而非发散。** $t < 0$ 时把 $m^2$ 代回 $F$：

$$F_{\min} - F_0 = at\,m^2 + bm^4 = -\frac{a^2t^2}{2b} + \frac{a^2t^2}{4b} = -\frac{a^2 t^2}{4b},$$

而 $t > 0$ 时 $F_{\min} - F_0 = 0$。由 $C = -T\,\partial^2 F/\partial T^2$，$t$ 对 $T$ 是线性的，二阶导数有限，于是

$$C(T_c^-) - C(T_c^+) = \frac{T_c\, a^2}{2b\,T_c^2} = \frac{a^2}{2bT_c},$$

即比热在 $T_c$ 处有一个**有限跳变** $\Delta C = a^2/(2bT_c)$。按临界指数记号这记作 $\alpha = 0$（不发散）。记住这个结果——下一节它将被实验当众处刑。

## 4. 涨落的失败：Ginzburg 判据与上临界维度

### 4.1 比热：跳变还是发散

Landau 理论把序参量当成一个均匀的经典数 $m$，完全忽略了它的空间涨落。实验不买账：

- 液氦 $\lambda$ 点（$^4$He 超流转变）的比热呈尖锐的（近对数）发散，不是有限跳变；
- 2D Ising 模型的 Onsager 精确解（第 8 节）给出 $C \propto -\ln\lvert t\rvert$——对数发散；
- 各种铁磁体在 $T_c$ 附近 $C \propto \lvert t\rvert^{-\alpha}$，$\alpha \approx 0.1$。

平均场什么时候可信？答案由涨落的大小决定，这就是 Ginzburg 判据。

### 4.2 Ginzburg 判据：涨落何时重要

允许 $m$ 在空间上变化（Ginzburg–Landau 自由能加梯度项 $c(\nabla m)^2$）。涨落要"自我平均"才谈得上用一个数 $m$ 描述系统；天然的平均体积是**关联体积** $\xi^d$（距离超过 $\xi$ 的两点涨落无关）。由涨落–响应关系，体积 $V$ 内平均序参量的方差是

$$\big\langle (\delta m)^2 \big\rangle_{V} \;=\; \frac{k_B T\,\chi}{V}, \qquad V \sim \xi^d.$$

平均场自洽的条件是：关联体积内的涨落远小于序参量本身，

$$\frac{k_B T_c\,\chi}{\xi^d} \;\ll\; m^2.$$

代入平均场结果：$\chi \sim (2a\lvert t\rvert)^{-1}$；Ornstein–Zernike 关联函数给出 $\xi^2 = c/(2a\lvert t\rvert)$；$m^2 = a\lvert t\rvert/(2b)$。于是

$$\frac{\langle(\delta m)^2\rangle_{\xi^d}}{m^2} \;\sim\; \frac{k_B T_c\,(2a\lvert t\rvert/c)^{d/2}\,(2b)}{(2a\lvert t\rvert)\cdot a\lvert t\rvert} \;\propto\; \lvert t\rvert^{(d-4)/2}.$$

看 $t \to 0$ 的极限，三种命运：

- **$d > 4$**：比值 $\to 0$——越靠近临界点涨落越不重要，平均场渐近正确；
- **$d < 4$**：比值 $\to \infty$——涨落必然压倒平均值，平均场指数错误；
- **$d = 4$**：边缘情形，平均场指数乘上对数修正。

所以 **上临界维度 $d_c = 4$**。物理解读：这是一场维度竞赛——$\xi$ 发散时，"被平均掉的体积" $\xi^d$ 按 $\xi^d \sim \lvert t\rvert^{-d/2}$ 涨，而涨落强度 $\chi$ 按 $\lvert t\rvert^{-1}$ 涨；$d/2$ 与 $1$ 谁大，决定谁赢。

### 4.3 为什么有些系统的平均场好用到离谱

把上面的比值等于 1 反解出涨落开始重要的约化温度 $\lvert t_G\rvert$（Ginzburg 区宽度）：$\lvert t_G\rvert \sim b^2(k_B T_c)^2/(a\,c^3)$，注意 $c \sim a\,\xi_0^2$（$\xi_0$ 是零温关联长度），故 $\lvert t_G\rvert \propto \xi_0^{-6}$——对关联长度**极度敏感**。

- 常规超导：$\xi_0 \sim 10^3\ \text{Å}$（Cooper 对很大），$\lvert t_G\rvert \lesssim 10^{-10}$，实验永远够不着涨落区——所以 BCS（本质就是平均场）好得出奇，Landau 比热跳变定量正确；
- 铁磁、气液：$\xi_0 \sim$ 晶格/分子尺度，$\lvert t_G\rvert \sim O(1)$，整个临界区都被涨落控制，平均场指数从头到尾是错的。

## 5. 临界指数与普适性

### 5.1 六个临界指数

临界点附近的奇异行为由六个指数刻画（$\sim$ 表示"正比于"，两侧指数相同、振幅不同）：

| 指数 | 定义 | 物理量 |
| --- | --- | --- |
| $\alpha$ | $C \propto \lvert t\rvert^{-\alpha}$ | 比热（$h=0$） |
| $\beta$ | $m \propto \lvert t\rvert^{\beta}$（$t \to 0^-$） | 序参量 |
| $\gamma$ | $\chi \propto \lvert t\rvert^{-\gamma}$ | 磁化率/压缩率 |
| $\delta$ | $m \propto h^{1/\delta}$（$t=0$） | 临界等温线 |
| $\nu$ | $\xi \propto \lvert t\rvert^{-\nu}$ | 关联长度 |
| $\eta$ | $G(r) \propto r^{-(d-2+\eta)}$（$t=0$） | 关联函数的幂律 |

$G(r) = \langle m(r)m(0)\rangle - \langle m\rangle^2$ 是两点关联函数；$\eta$ 度量它偏离平均场 Ornstein–Zernike 形式（$\eta = 0$）的程度，常叫"反常维度"——这个名字与 QFT 里的 anomalous dimension 是同一个东西，不是巧合（见第 7.3 节）。

### 5.2 标度律：六个指数只有两个独立

实验和理论上发现六个指数满足四组代数关系（**标度律**）：

$$\alpha + 2\beta + \gamma = 2 \quad(\text{Rushbrooke}), \qquad \gamma = \beta(\delta - 1) \quad(\text{Widom}),$$

$$\gamma = \nu(2 - \eta) \quad(\text{Fisher}), \qquad d\,\nu = 2 - \alpha \quad(\text{Josephson}).$$

Fisher 关系有一行推导：$\chi$ 是 $G(r)$ 的积分，关联函数幂律延伸到 $\xi$ 被截断，$\chi \sim \int^{\xi} d^d r\, r^{-(d-2+\eta)} \sim \xi^{2-\eta}$，两边指数对照即得。Josephson 关系（**超标度**，含维度 $d$）只在 $d < 4$ 成立——$d \ge 4$ 时平均场指数（$\nu = 1/2,\ \alpha = 0$）已经违反它，这正是涨落"危险地无关"的信号。六个指数减四个关系，**只剩两个自由度**；标度假设（第 6 节）解释了为什么。

### 5.3 普适性：不同材料为何共享指数

实验事实：3D Ising 模型、气液临界点、二元合金有序–无序转变、单轴铁磁体，临界指数在误差内完全相同。这惊世骇俗——这些系统的微观相互作用毫无共同之处。经验规律：

- 临界指数只依赖**空间维度 $d$** 与**序参量分量数/对称性 $n$**（外加少量全局特征如力程长短）；
- $d$ 和 $n$ 相同的所有系统构成一个**普适类（universality class）**；
- 微观细节（晶格结构、耦合强度、$T_c$ 数值）属于"非普适"数据。

普适性为什么必然成立？这正是重整化群要回答的问题（第 7 节，自检第 4 题）。

## 6. 标度假设：Widom 标度形式

**标度假设**：临界点附近，自由能的奇异部分不是独立依赖 $t$ 和 $h$，而只依赖一个组合：

$$f_s(t, h) = \lvert t\rvert^{2-\alpha}\, F_\pm\!\left(\frac{h}{\lvert t\rvert^{\beta\delta}}\right),$$

其中 $F_\pm$（$\pm$ 对应 $t \gtrless 0$）是普适的标度函数。一句话：**$t$ 设定唯一的尺度，$h$ 只能以 $h/\lvert t\rvert^{\beta\delta}$ 的身份出现**。所有标度律（Rushbrooke、Widom）都是对 $f_s$ 求导、比对定义得到的代数恒等式——自检第 3 题让你亲手推 Rushbrooke 关系。

## 7. Wilson 重整化群：普适性的发动机

### 7.1 Kadanoff 块自旋变换

Kadanoff 的图像（1966）：临界点上 $\xi$ 发散，系统在一切尺度上都"看起来一样"，所以应该可以**逐级丢掉短距离细节而不改变长程物理**。操作分两步：

1. **粗粒化**：把 $b^d$ 个格点自旋合并成一个"块自旋"（取多数或平均），晶格常数从 $a$ 变成 $ba$；
2. **重标度**：把长度单位缩小 $b$ 倍，$r \to r' = r/b$，使块自旋模型与原始模型"看起来一样"。

两步合称一次**块自旋变换**或重整化群（RG）变换。配分函数不变（只是把求和分两步做），但有效哈密顿量的参数变了：$(K, h) \to (K', h')$，其中 $K = J/(k_B T)$ 是无量纲耦合。反复迭代，就得到参数空间中的一条轨道——**耦合常数流**。

一个能算到底的例子是 1D Ising：每隔一个自旋求和（$b=2$ 抽稀），

$$\sum_{\sigma_2 = \pm 1} e^{K\sigma_2(\sigma_1 + \sigma_3)} = 2\cosh K(\sigma_1+\sigma_3) \;\propto\; e^{K'\sigma_1\sigma_3},$$

配系数给出 $e^{2K'} = \cosh 2K$，即 $K' = \mathrm{artanh}(\tanh^2 K) < K$。每变换一次耦合就变小，一切流向 $K = 0$（高温无序）——RG 变换顺带**证明了 1D Ising 没有有限温度相变**。

### 7.2 不动点、相关方向与临界面

一般 $d$ 维中，流在耦合常数空间里展开。关键是**不动点**：$K^*$ 满足 $K' = K^*$，再变换也不动。物理上不动点处 $\xi$ 只能取 $\xi = \xi/b$ 的解：$\xi = 0$（平庸不动点：完全有序或完全无序）或 $\xi = \infty$（**临界不动点**）。在不动点附近把变换线性化，方向分两类：

- **相关方向（relevant）**：本征值 $b^{y}$，$y > 0$——沿它偏离不动点的分量被**放大**，流离不动点而去。Ising 普适类恰有两个：约化温度 $t$（$y_t$）与外场 $h$（$y_h$）；
- **无关方向（irrelevant）**：$y < 0$——分量被**压缩**，迭代几次就消失。微观细节（次近邻耦合、晶格各向异性……）全在这里。

关联长度给出指数与几何的桥梁：$\xi = b\,\xi'$ 而 $t' = b^{y_t} t$，迭代到 $t' \sim O(1)$ 时 $\xi' \sim O(1)$，故

$$\xi \propto \lvert t\rvert^{-1/y_t} \;\Longrightarrow\; \nu = \frac{1}{y_t}.$$

**临界面（critical surface）**：耦合空间中所有最终被吸到临界不动点的初始点的集合，余维数 = 相关方向数（Ising：2——要调到临界点必须同时调 $t = 0$ 和 $h = 0$）。**临界面上任何一点——无论它对应铁、镍、气液还是 Ising 模型——长波行为都由同一个不动点控制**，所以共享同一组指数。这就是普适性的机制性解释，也是自检第 4 题的答案骨架。

<details markdown="1"><summary>补充说明：为什么叫"群"</summary>

严格说 RG 只是**半群**：变换只能朝粗粒化方向走（丢掉的短波信息捡不回来），没有逆元。真正的结构是"参数空间上的半流"。把它叫群是历史遗留（来自 QFT 中改变正规化点的操作），不必较真——要紧的是流的结构：不动点、稳定/不稳定流形、吸引域。

</details>

### 7.3 与 QFT 的跑动耦合：同一套数学

把下面的对照表读透，QFT 书里的重整化会突然变得具体：

| 统计力学（本章） | 量子场论 |
| --- | --- |
| 块自旋：积分掉 $a$ 到 $ba$ 间的自由度 | Wilson 积分：积掉动量壳层 $\Lambda/b$ 到 $\Lambda$ |
| 耦合常数流 $K \to K'$ | 跑动耦合 $g(\mu)$，由 $\beta$ 函数描述 |
| 不动点 $K^*$ | $\beta(g^*) = 0$ 的点 |
| 相关方向（$y > 0$） | 可重整（super-renormalizable / relevant）算符 |
| 无关方向（$y < 0$） | 不可重整算符，被 $1/\Lambda$ 压低 |
| 临界面 | 流向同一不动点的低能理论族 |
| $\eta$（反常维度） | anomalous dimension（同名同物） |

QFT 笔记[一圈修正与重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)中的 Wilson 有效理论视角——截断 $\Lambda$ 是物理的、任何 QFT 都是低能有效理论、不可重整项被 $1/\Lambda$ 自动压低——正是本章"无关方向被流动抹掉、长波物理只由不动点决定"的场论版本。反过来，统计力学给了这套数学最清晰的物理诠释：**这里的流图直接画在"所有可能材料构成的参数空间"上**，普适性就是流的几何。同一套结构，两处开花。

### 7.4 $\varepsilon = 4 - d$ 展开：把感想变成数字

$d = 4$ 是平均场恰好自洽的边缘维度，Wilson–Fisher 的办法是把 $d$ 当连续变量、在 $\varepsilon = 4 - d$ 很小时做微扰：$\phi^4$ 耦合无量纲化后的一圈 $\beta$ 函数为

$$\beta(u) \equiv \frac{du}{d\ell} = -\varepsilon\,u + \frac{n+8}{6}\,u^2 + O(u^3),$$

除平庸不动点 $u = 0$（高斯不动点，$d<4$ 时不稳定）外，出现非平庸的 **Wilson–Fisher 不动点** $u^* = 6\varepsilon/(n+8) + O(\varepsilon^2)$——它是 $\varepsilon$ 的一阶小量，所以微扰论**可控**。在它附近线性化就得到指数的修正，例如 $\beta = \tfrac12 - \dfrac{3\varepsilon}{2(n+8)} + O(\varepsilon^2)$。大胆令 $\varepsilon = 1$（$d = 3$，谈不上小），再配上级数重求和（Borel 等），给出的指数与实验、Monte Carlo 高度吻合。临界现象是"微扰论 + 重整化"这套机器在粒子物理之外最辉煌的战果——Wilson 因此拿了 1982 年诺贝尔奖。

## 8. 实例：Ising 模型在三种维度下的指数

把三种方法摆在一起，看平均场错在哪、错多少：

| 指数 | 平均场（Landau） | 2D Ising 精确解 | 3D Ising 数值 |
| --- | --- | --- | --- |
| $\alpha$ | $0$（跳变） | $0$（对数发散） | $0.110$ |
| $\beta$ | $1/2$ | $1/8$ | $0.326$ |
| $\gamma$ | $1$ | $7/4$ | $1.237$ |
| $\delta$ | $3$ | $15$ | $4.79$ |
| $\nu$ | $1/2$ | $1$ | $0.630$ |
| $\eta$ | $0$ | $1/4$ | $0.036$ |

几点注释：

- **2D 精确解**：Onsager（1944）算出自由能（比热对数发散）；杨振宁（1952）算出自发磁化 $m = \big(1 - \sinh^{-4}(2K)\big)^{1/8}$，临界的 $\beta = 1/8$ 由此而来。这是理论物理史上公认最硬的计算之二。
- **3D 数值**：来自 Monte Carlo、高温级数展开，以及近年的共形 bootstrap——不同方法在小数点后第三位互相吻合，是普适性最铁的实验外证据。
- **趋势**：$d$ 越低偏离平均场越远（2D 的 $\beta = 0.125$ vs $3$D 的 $0.326$ vs 平均场 $0.5$），正是 Ginzburg 判据所预言的：低维涨落更强。$d = 1$ 干脆没有相变（第 7.1 节的抽稀已证明）。
- 任取一行验证标度律：3D 行 $\alpha + 2\beta + \gamma = 0.110 + 0.652 + 1.237 \approx 2$；$\gamma \approx \nu(2-\eta)$ 给出 $0.630 \times 1.964 \approx 1.237$。全对上。

## 小结

| 概念 | 一句话 |
| --- | --- |
| 序参量 | 高温为零、低温非零；其对称性（分量数 $n$）是普适类的标签 |
| Landau 理论 | 对称性决定自由能展开；双井 = 自发对称破缺；给出平均场指数 |
| 平均场指数 | $\beta = 1/2,\ \gamma = 1,\ \delta = 3,\ \alpha = 0$（跳变） |
| Ginzburg 判据 | $\langle(\delta m)^2\rangle_{\xi^d} \ll m^2$；自洽条件 $\propto \lvert t\rvert^{(d-4)/2}$ |
| 上临界维度 | $d_c = 4$：以上平均场对，以下涨落主导，等于时有对数修正 |
| 普适性 | 指数只依赖 $d$ 与 $n$；不同材料共享指数 |
| 标度律 | 六指数两独立：Rushbrooke、Widom、Fisher、Josephson |
| 标度假设 | $f_s = \lvert t\rvert^{2-\alpha} F(h/\lvert t\rvert^{\beta\delta})$，一切标度律之源 |
| Wilson RG | 块自旋 → 耦合流 → 不动点；相关方向定指数，无关方向洗细节，临界面给普适性 |
| 与 QFT | 跑动耦合、$\beta$ 函数、反常维度是同一套数学 |
| $\varepsilon$ 展开 | $u^* = 6\varepsilon/(n+8)$，指数修正可从 $\varepsilon = 4-d$ 级数算 |

## 自检问题

**1.** 从 Landau 自由能 $F = F_0 + a(T-T_c)m^2 + bm^4 - hm$ 出发，完整推出平均场指数 $\beta = 1/2$、$\gamma = 1$、$\delta = 3$，并计算临界点两侧磁化率的振幅比。

<details markdown="1"><summary>点击显示答案</summary>

平衡条件 $\partial F/\partial m = 0$ 给出状态方程 $2at\,m + 4bm^3 = h$（$t = (T-T_c)/T_c$）。

- **$\beta$**：$h = 0$，$t < 0$ 时非零解 $m^2 = -at/(2b) = a\lvert t\rvert/(2b)$，故 $m \propto \lvert t\rvert^{1/2}$，$\beta = 1/2$。
- **$\delta$**：$t = 0$ 时 $4bm^3 = h$，$m \propto h^{1/3}$，$\delta = 3$。
- **$\gamma$**：状态方程对 $h$ 求导得 $\chi = (2at + 12bm^2)^{-1}$。$t > 0$：$m = 0$，$\chi = t^{-1}/(2a)$；$t < 0$：代入 $m^2 = a\lvert t\rvert/(2b)$，分母为 $4a\lvert t\rvert$，$\chi = \lvert t\rvert^{-1}/(4a)$。两侧均 $\propto \lvert t\rvert^{-1}$，$\gamma = 1$；振幅比 $C^+/C^- = (1/2a)/(1/4a) = 2$。这个比值是平均场理论不依赖 $a, b$ 的可检验预言。

</details>

**2.** 推导 Ginzburg 判据，并说明它为什么给出上临界维度 $d_c = 4$。

<details markdown="1"><summary>点击显示答案</summary>

平均场把 $m$ 当均匀数，自洽的前提是关联体积 $V \sim \xi^d$ 内的涨落远小于序参量本身。由涨落–响应关系 $\langle(\delta m)^2\rangle_V = k_B T\chi/V$，条件是

$$\frac{k_B T_c\,\chi}{\xi^d} \ll m^2.$$

代入平均场量 $\chi \sim (2a\lvert t\rvert)^{-1}$、$\xi^2 = c/(2a\lvert t\rvert)$、$m^2 = a\lvert t\rvert/(2b)$，左边与右边之比

$$\frac{k_B T_c\,(2a\lvert t\rvert)^{d/2-1}\,c^{-d/2}\cdot 2b}{a\lvert t\rvert} \propto \lvert t\rvert^{d/2 - 2} = \lvert t\rvert^{(d-4)/2}.$$

$t \to 0$ 时：$d > 4$ 比值趋于零（平均场渐近自洽）；$d < 4$ 比值发散（涨落必然胜出）；$d = 4$ 比值常数化、需更细分析（对数修正）。分界线即上临界维度 $d_c = 4$。本质：$\xi^d \sim \lvert t\rvert^{-d/2}$ 与 $\chi \sim \lvert t\rvert^{-1}$ 的赛跑。

</details>

**3.** 从标度假设 $f_s(t,h) = \lvert t\rvert^{2-\alpha} F(h/\lvert t\rvert^{\Delta})$ 推出 Rushbrooke 关系 $\alpha + 2\beta + \gamma = 2$。

<details markdown="1"><summary>点击显示答案</summary>

记标度变量 $x = h/\lvert t\rvert^{\Delta}$。对 $h$ 求导：

$$m = -\frac{\partial f_s}{\partial h} = -\lvert t\rvert^{2-\alpha-\Delta} F'(x).$$

令 $h \to 0$（$x \to 0$，$F'(0)$ 为常数），比对 $m \propto \lvert t\rvert^{\beta}$ 得

$$\beta = 2 - \alpha - \Delta.$$

再求一次导：

$$\chi = \frac{\partial m}{\partial h} = -\lvert t\rvert^{2-\alpha-2\Delta} F''(x),$$

比对 $\chi \propto \lvert t\rvert^{-\gamma}$ 得

$$\gamma = -(2 - \alpha - 2\Delta) = 2\Delta - 2 + \alpha.$$

三式相加消去 $\Delta$：

$$\alpha + 2\beta + \gamma = \alpha + 2(2-\alpha-\Delta) + (2\Delta - 2 + \alpha) = 2.$$

关键是"单尺度"结构：每次对 $h$ 求导多出一个 $\lvert t\rvert^{-\Delta}$，指数关系因此纯粹是量纲 bookkeeping。

</details>

**4.** 为什么块自旋变换"必然"给出普适性？请用流、不动点、相关/无关方向的语言论证。

<details markdown="1"><summary>点击显示答案</summary>

每个微观系统是耦合常数空间里的一个点；块自旋变换保持配分函数（因而保持长波物理）不变，同时把这个点沿一条轨道移动。迭代时：

- 沿**无关方向**（$y < 0$）的分量按 $b^{y}$ 收缩——晶格结构、次近邻耦合等一切微观差异被指数级洗掉；
- 临界面上的所有点最终汇聚到**同一个临界不动点**；
- 长波可观测量（指数）只由不动点处的线性化决定，即只由**相关方向**的本征值 $y_t, y_h$ 决定（如 $\nu = 1/y_t$）。

于是必然性来自结构本身：只要两个系统经粗粒化后流进同一不动点的吸引域，它们的大尺度行为就不可能不同——差异只能藏在短波长，而短波长正是被 RG 逐步丢弃的东西。微观上无限多种材料，宏观上只剩有限多个不动点，这就是普适类。例外只可能出现在系统的对称性或维度不同（落入别的临界面），或存在额外相关方向（如长程相互作用改变动力学区）时。

</details>

**5.** 3D Ising 的 $\beta \approx 0.326$ 与平均场值 $1/2$ 差多远？差距的来源是什么？用 $\varepsilon$ 展开的一阶结果检验你的解释。

<details markdown="1"><summary>点击显示答案</summary>

绝对差 $0.5 - 0.326 = 0.174$，相对差约 $35\%$——不是小修正，平均场定量上完全失败。

**来源**：$d = 3 < d_c = 4$，Ginzburg 判据失效，涨落主导临界区。RG 语言：$d < 4$ 时高斯不动点（平均场对应物）在 $\phi^4$ 方向上是**不稳定**的，真正的临界行为由 Wilson–Fisher 不动点控制，其相关本征值与平均场不同。

**定量检验**：$\varepsilon$ 展开给出（$n$ 为序参量分量数）

$$\beta = \frac{1}{2} - \frac{3\varepsilon}{2(n+8)} + O(\varepsilon^2).$$

取 $n = 1$（Ising）、$\varepsilon = 1$（$d = 3$）：$\beta \approx \tfrac12 - \tfrac{3}{18} = \tfrac13 \approx 0.333$。一阶微扰就把 $0.5$ 拉到 $0.333$，吃掉了与真值 $0.326$ 之间差距的 $96\%$——差距的全部来源正是"被平均场忽略的涨落"，而涨落的领头效应可以用 $\varepsilon = 4-d$ 级数逐项算出。另可用标度律交叉验证：$\beta = \nu(d-2+\eta)/2 = 0.630 \times 1.036/2 \approx 0.326$，自洽。

</details>

## 参考

- Goldenfeld《Lectures on Phase Transitions and the Renormalization Group》第 5 章（Landau 理论与平均场失效）、第 8–10 章（标度假设、RG 与 $\varepsilon$ 展开）——与本章对应最直接，Ginzburg 判据的讲法即出自此书。
- Kardar《Statistical Physics of Fields》第 4–5 章（Landau–Ginzburg 理论、RG 微扰展开）——推导密度更高，适合二刷。
- Kittel《固体物理导论》磁性相关章节——平均场与 Landau 自由能在铁磁体中的具体用法。
- Ashcroft & Mermin《Solid State Physics》第 33 章（磁有序）——平均场临界行为的扼要讨论；此书对临界现象着墨不多，专题请以上面两本为主。
- 原始文献：Onsager, Phys. Rev. 65, 117 (1944)（2D Ising 精确解）；Yang（杨振宁）, Phys. Rev. 85, 808 (1952)（自发磁化 $1/8$）；Wilson, Phys. Rev. B 4, 3174, 3184 (1971)（RG 的奠基两篇）。
