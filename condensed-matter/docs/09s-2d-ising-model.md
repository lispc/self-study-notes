# 补充阅读：二维方格子 Ising 模型——最简单的相变系统及其数学

> 本书位置：凝聚态物理入门导论 第 9 章补充阅读（配套正文：[相变与临界现象](09-phase-transitions-criticality.md)，下文简称"第 9 章"）。
> 前置知识：第 9 章正文（临界指数、标度律、普适性）；第 7 章[磁性](07-magnetism.md)（Ising 模型的平均场处理）；统计力学基础（配分函数、自由能、Boltzmann 权重）。
> 学习目标：理解"二维方格子 Ising 模型是已知最简单的会产生相变的物理系统"这句话的全部含义；掌握一维无相变的畴壁论证与转移矩阵解法；会复述 Peierls 论证的组合估计；会推 Kramers–Wannier 对偶并解出精确 $T_c$；记住 Onsager/Yang 精确解的临界指数及其与平均场的逐项对比。

---

约定：本书保留 $k_B$。本篇几乎不用 $\hbar$——Ising 模型是纯经典模型，连量子力学都不需要，这本身就是"最简单"的一层含义。通篇用无量纲耦合

$$K \equiv \beta J = \frac{J}{k_B T},$$

与第 9 章一致。约化温度仍记 $t = (T - T_c)/T_c$。

## 1. 一句话总结

**二维方格子 Ising 模型把"相互作用多体系统"削减到极限——自由度是离散的（$\sigma = \pm 1$）、相互作用是二体最近邻的、动力学是零（纯平衡态统计）、连量子力学都被拿掉了——简单到不能再简单，却拥有真正的连续相变：有序相的存在性有严格证明（Peierls 论证，几行组合估计），临界温度有一个基于对偶性的漂亮推导（Kramers–Wannier，半页纸），自由能和自发磁化有精确解（Onsager 1944、Yang 1952）；它因此成为整个相变理论——Landau、标度律、重整化群、普适性——的"裁判样本"，任何近似方法先拿它对答案。**

下面逐层展开：先定义模型并讲清"简单"的确切所指，再说明为什么一维就不行（维度是分水岭），然后依次给出 Peierls 论证、Kramers–Wannier 对偶与精确解的骨架。

## 2. 模型定义与"最简单"的含义

**定义。** 在方格子的每个格点 $i$ 上放一个二值变量 $\sigma_i = \pm 1$（"自旋向上/向下"），哈密顿量

$$H = -J \sum_{\langle ij \rangle} \sigma_i \sigma_j,$$

其中 $\langle ij \rangle$ 表示对所有最近邻键求和，$J > 0$ 为铁磁耦合：同向键贡献能量 $-J$，反向键贡献 $+J$。统计力学由配分函数给出：

$$Z = \sum_{\{\sigma_i = \pm 1\}} e^{-\beta H} = \sum_{\{\sigma_i\}} \exp\!\Big( K \sum_{\langle ij\rangle} \sigma_i \sigma_j \Big).$$

**"简单"到底指什么。** 把它和见过的其他模型逐项对照：

- **离散 vs 连续**：每个自由度只取两个值，没有积分、没有连续对称性。对比第 7 章的 Heisenberg 模型 $\hat H = -J\sum_{\langle ij\rangle} \hat{\mathbf S}_i \cdot \hat{\mathbf S}_j$——那是量子模型，自旋是算符、有对易关系、有自旋波动力学；Ising 模型里 $\sigma_i$ 是普通的数，哈密顿量对角化问题是平凡的，全部难度集中在**组合求和**（$2^N$ 个位形的计数）上。
- **无动能项**：$H$ 就是全部能量，没有 $p^2/2m$，没有时间演化问题；相变纯粹是**能量与熵的竞争**。
- **最短力程、最强对称性**：只有最近邻耦合，对称群只有 $\mathbb{Z}_2$（全体自旋翻转 $\sigma_i \to -\sigma_i$）。

再削减就会失去相变：离散变量不能再少（一个值就没有变量了），$\mathbb{Z}_2$ 是最小的非平凡对称群，而最近邻是格子上的最小力程。唯一还能调的旋钮是**维度**——下一节说明这正好是生死线。

**它要回答的问题**：零外场下，系统降温时会不会在有限温度 $T_c > 0$ 处自发选一个方向（$\langle \sigma_i \rangle = m \neq 0$），即发生 $\mathbb{Z}_2$ 自发对称破缺？这正是第 9 章第 2 节定义的铁磁连续相变。

## 3. 为什么没有更简单的：一维 Ising 无相变

### 3.1 畴壁论证：基态总是被熵摧毁

一维链 $H = -J \sum_{i=1}^{N} \sigma_i \sigma_{i+1}$（自由边界），基态全体同向，能量 $E_0 = -JN$。插入**一段畴壁**：在某根键上让左右两侧反平行。代价只有这根键从 $-J$ 翻到 $+J$，

$$\Delta E = 2J,$$

与墙的粗细无关、与链长无关。但墙可以放在 $N$ 根键中的任意一根上，于是带来熵

$$\Delta S = k_B \ln N.$$

自由能的变化

$$\Delta F = \Delta E - T\,\Delta S = 2J - k_B T \ln N.$$

对**任意** $T > 0$，只要 $N$ 足够大就有 $\ln N > 2J/(k_B T)$，即 $\Delta F < 0$——引入畴壁**降低**自由能。于是热力学极限下畴壁必然大量出现，链被切成平均长度 $\sim e^{2K}$ 的碎段，任意两点自旋关联随距离指数衰减，$\langle \sigma_i \rangle = 0$。有序基态被熵无条件摧毁，**任何有限温度下都没有相变**（$T = 0$ 处才有"临界点"）。

注意论证的维度结构：$d$ 维中包围一团翻转自旋的"墙"是 $(d-1)$ 维对象，尺寸 $R$ 的墙能量 $\sim J R^{d-1}$、熵 $\sim k_B R$。$d = 1$ 时能量是常数而熵发散，熵恒赢；$d = 2$ 时能量 $\propto R$ 与熵 $\propto R$ 同阶竞争，低温时能量可以赢——这就是 Peierls 论证（第 4 节）能成功的几何原因。**维度 $d = 2$ 是离散对称性出现有限温度相变的最低维度。**

### 3.2 转移矩阵：自由能解析的精确验证

畴壁论证是"物理图像"，转移矩阵给出可算到底的验证。把配分函数按相邻自旋对分组：

$$Z = \sum_{\{\sigma_i\}} \prod_{i=1}^{N} e^{K \sigma_i \sigma_{i+1}} = \mathrm{Tr}\,\mathbb{T}^N,$$

其中转移矩阵 $\mathbb{T}$ 是 $2 \times 2$ 矩阵，矩阵元 $\mathbb{T}_{\sigma\sigma'} = e^{K\sigma\sigma'}$：

$$\mathbb{T} = \begin{pmatrix} e^{K} & e^{-K} \\ e^{-K} & e^{K} \end{pmatrix}.$$

本征值

$$\lambda_+ = 2\cosh K, \qquad \lambda_- = 2\sinh K.$$

热力学极限下只有最大本征值存活，每个自旋的自由能

$$f = -k_B T \lim_{N\to\infty} \frac{\ln Z}{N} = -k_B T \ln \lambda_+ = -k_B T \ln\big(2\cosh K\big),$$

它对一切有限 $K$（即一切 $T > 0$）是**解析函数**——没有任何奇异性，即没有相变。关联长度也可以精确算：$\langle \sigma_0 \sigma_r \rangle = (\lambda_-/\lambda_+)^r = (\tanh K)^r$，即

$$\xi = \frac{1}{\ln \coth K},$$

只在 $K \to \infty$（$T \to 0$）时发散，与"临界点躺在 $T = 0$"的结论一致。对照第 9 章第 7.1 节的抽稀 RG（$K' < K$，一切流向 $K = 0$），三种方法同答一题。

**本节的教训**：一维的失败不是"模型太简单"的失败，而是维度的失败。同一个模型搬到方格子上，故事完全反转。

## 4. Peierls 论证：二维有序相存在的严格证明骨架

Peierls（1936）的思想（后由 Dobrushin、Griffiths 严格化）：不用算配分函数，直接估计"一个自旋被翻转"的概率。

**设定。** 取 $N \times N$ 方格子，边界上所有自旋固定为 $+1$（这等价于加了一个无穷小的对称破缺场，最后取热力学极限再看体内自旋）。问：中心某个自旋 $\sigma_0$ 为 $-1$ 的概率有多大？

**围道（contour）。** 若 $\sigma_0 = -1$，它必属于一块连通（或嵌套）的翻转区域，该区域被一条**闭合围道**包围——围道画在对偶格子上，每一段分隔一对反平行最近邻自旋。关键观察：

- **能量代价正比于围道长度**：围道每长一段就对应一根反向键，长为 $L$ 的围道恰好对应 $L$ 根断键，故含这条围道的位形相对"围道内全部翻回 $+1$"的位形能量高 $2JL$，Boltzmann 权重压低 $e^{-2KL}$：

$$\mathrm{Prob}(\text{指定围道 } \gamma \text{ 出现}) \le e^{-2KL}.$$

**围道计数。** 从某点出发、长为 $L$ 的闭合围道有多少条？第一步有 4 个方向可走，之后每一步至多 3 个方向（不许立刻回头，否则不构成围道），故

$$\#\{\text{长为 } L \text{ 的围道}\} \le 4 \cdot 3^{L-1}.$$

要求围道包围原点只会进一步限制（围道长度 $L \ge 4$，且必须伸到原点附近，至多再贡献一个 $\sim L$ 的因子，不影响下面的指数竞争）。

**Peierls 判据。** 把所有可能围道的贡献相加（联合界/union bound）：

$$\mathrm{Prob}(\sigma_0 = -1) \;\le\; \sum_{L=4,6,8,\dots} \big(\text{围道数}\big)\, e^{-2KL} \;\lesssim\; \sum_{L \ge 4} 4 \cdot 3^{L-1}\, e^{-2KL}.$$

右边的几何级数在 $3e^{-2K} < 1$ 时收敛，并且 $K$ 足够大（$T$ 足够低）时总和可以压到 $1/2$ 以下（具体数值见自检第 2 题）。于是

$$\langle \sigma_0 \rangle = 1 - 2\,\mathrm{Prob}(\sigma_0 = -1) \;>\; 0 \qquad (T \text{ 足够低}).$$

体内自旋跟着边界走：**低温下自发磁化非零，有序相严格存在**（这叫 Peierls 判据：围道平均密度趋于零）。

**与一维对照**：一维的"围道"是孤立的点，数量 $\propto N$ 而代价恒为 $2J$，熵恒胜；二维围道长度 $L$ 同时控制能量（$e^{-2KL}$）和熵（$3^L$），低温把 $e^{-2KL}$ 压得比 $3^L$ 涨得快，能量赢。同一个组合结构，维度决定胜负。

## 5. Kramers–Wannier 对偶：临界温度的精确值

Peierls 只告诉你"存在某个 $T_c > 0$"，没告诉你数值。Kramers 与 Wannier（1941，早于 Onsager 解）用对偶性把方格子的 $T_c$ **钉死**。骨架分两步：把同一个 $Z$ 写两遍。

### 5.1 高温展开：变量 $\tanh K$ 的闭合回路

对单根键，因为 $\sigma_i\sigma_j = \pm 1$ 只有两值，有恒等式

$$e^{K\sigma_i\sigma_j} = \cosh K + \sigma_i\sigma_j \sinh K = \cosh K\,\big(1 + v\,\sigma_i\sigma_j\big), \qquad v \equiv \tanh K.$$

代入配分函数并把 $2N$ 根键（$N$ 格点方格子）的因子全部乘开：

$$Z = (\cosh K)^{2N} \sum_{\{\sigma_i\}} \prod_{\langle ij\rangle} \big(1 + v\,\sigma_i\sigma_j\big).$$

乘开后每一项对应"在每根键上选 $1$ 或选 $v\,\sigma_i\sigma_j$"。对某个自旋 $\sigma_i = \pm 1$ 求和时，凡 $\sigma_i$ 出现**奇数次**的项相互抵消（$\sum_{\sigma=\pm1}\sigma = 0$），只有每个格点都出现偶数次的项存活——几何上这正是格子上**闭合回路**（每点度数偶）。每条长 $L$ 的回路贡献 $v^L$：

$$Z(K) = 2^N (\cosh K)^{2N} \sum_{\text{闭合回路}} v^{L}, \qquad v = \tanh K.$$

高温时 $v$ 小，回路短而稀，这是无序相的图画。

### 5.2 低温展开：变量 $e^{-2K}$ 的畴壁围道

从全体同向的基态出发，激发态由畴壁刻画：畴壁画在**对偶格子**（方格子的对偶还是方格子）上，是闭合回路；长 $L$ 的畴壁断 $L$ 根键，权重 $e^{-2KL}$。计及基态简并因子 2：

$$Z(K) = 2\,e^{2NK} \sum_{\text{对偶格子上的闭合回路}} \big(e^{-2K}\big)^{L}.$$

低温时 $e^{-2K}$ 小，畴壁短而稀，这是有序相的图画（与第 4 节同一组围道）。

### 5.3 自对偶钉死 $T_c$

两式右端的回路求和是**同一个函数**（方格子自对偶：回路都画在方格子上），只是变量不同：高温展开用 $v = \tanh K$，低温展开用 $e^{-2K}$。定义对偶耦合 $K^*$ 使两者相等：

$$\tanh K^* = e^{-2K} \;\Longleftrightarrow\; \sinh 2K \cdot \sinh 2K^* = 1.$$

（等价性的验证：$\sinh 2K^* = \dfrac{2\tanh K^*}{1 - \tanh^2 K^*} = \dfrac{2e^{-2K}}{1 - e^{-4K}} = \dfrac{1}{\sinh 2K}$。）于是配分函数满足对偶关系

$$\frac{Z(K)}{(\sinh 2K)^{N}} = \frac{Z(K^*)}{(\sinh 2K^*)^{N}} \cdot (\text{解析因子}),$$

即**高温相的物理与低温相的物理互为镜像**：每算出一侧，另一侧免费得到。现在看奇异性：若相变点唯一（只有一个 $K_c$），它必须在对偶映射 $K \leftrightarrow K^*$ 下不动，否则奇点会成对出现。不动点条件 $K_c = K^*$ 给出

$$\sinh 2K_c = 1 \;\Longrightarrow\; 2K_c = \ln(1 + \sqrt{2}) = 0.8814,$$

$$\boxed{k_B T_c = \frac{2J}{\ln(1+\sqrt{2})} \approx 2.269\,J.}$$

这正是 Onsager 精确解里的临界温度——Kramers–Wannier 在精确解出现前三年就拿到了它。注意逻辑的精细处：对偶性证明的是"**若**临界点唯一**则**它在此"，存在性与唯一性由 Peierls 论证（低温有序）加上高温展开的收敛性（高温无序）补上。

## 6. 精确解的里程碑：Onsager 与 Yang

### 6.1 Onsager（1944）：自由能

把第 3.2 节的转移矩阵思想搬到二维：对 $N$ 列的条带，转移矩阵是 $2^N \times 2^N$ 矩阵，自由能由其**最大本征值**决定。Onsager 用转移矩阵代数的精细结构（后由 Kaufman 用旋量表示简化）在热力学极限下求出每自旋自由能

$$-\beta f = \ln 2 + \frac{1}{2\pi^2}\int_0^{\pi}\!\! d\theta \int_0^{\pi}\!\! d\phi\; \ln\Big( \cosh^2 2K - \sinh 2K\,(\cos\theta + \cos\phi) \Big),$$

奇异性来自被积函数在 $\sinh 2K = 1$、$\theta = \phi = \pi$ 处碰零——正是对偶预言的 $K_c$。对比热的推论：

$$C \propto -\ln \lvert t \rvert \qquad (t \to 0),$$

**对数发散**，按指数记号记 $\alpha = 0$（弱于任何幂律）。这一结果当众处刑了平均场的"比热有限跳变"（第 9 章第 4.1 节），是涨落重要性的第一个严格证据。

### 6.2 Yang（1952）：自发磁化

Onsager 没有算出序参量本身（他在 1948 年的一次会议上写下了结果但未发表推导）。杨振宁（1952）完成了这个公认更硬的计算：

$$m = \Big[1 - \sinh^{-4}(2K)\Big]^{1/8} \qquad (T < T_c), \qquad m = 0 \quad (T > T_c).$$

$T \to T_c^-$ 时 $\sinh 2K \to 1$，方括号线性趋于零，故 $m \propto \lvert t \rvert^{1/8}$——**$\beta = 1/8$**，与平均场的 $1/2$ 天差地别（详细展开见自检第 5 题）。序参量比平均场预言的"瘦"得多：涨落把磁化涨掉了大半。

### 6.3 临界指数：精确解 vs 平均场

| 指数 | 定义 | 2D Ising 精确值 | 平均场值 |
| --- | --- | --- | --- |
| $\alpha$ | $C \propto \lvert t\rvert^{-\alpha}$ | $0$（对数发散） | $0$（有限跳变） |
| $\beta$ | $m \propto \lvert t\rvert^{\beta}$ | $1/8$ | $1/2$ |
| $\gamma$ | $\chi \propto \lvert t\rvert^{-\gamma}$ | $7/4$ | $1$ |
| $\delta$ | $m \propto h^{1/\delta}$（$t=0$） | $15$ | $3$ |
| $\nu$ | $\xi \propto \lvert t\rvert^{-\nu}$ | $1$ | $1/2$ |
| $\eta$ | $G(r) \propto r^{-(d-2+\eta)}$（$t=0$） | $1/4$ | $0$ |

（$\gamma, \delta, \nu, \eta$ 的精确值来自级数展开与后来的标度/共形场论分析，不在 Onsager/Yang 的原始计算内。）逐行可见平均场在 $d = 2$ 全面失真——Ginzburg 判据说 $d < 4$ 涨落主导，二维是离 $d_c = 4$ 最远、涨落最凶的情形。

**标度律检验**（第 9 章第 5.2 节）逐项通过：

- Rushbrooke：$\alpha + 2\beta + \gamma = 0 + \tfrac{2}{8} + \tfrac{7}{4} = 2$ ✓
- Widom：$\beta(\delta - 1) = \tfrac{1}{8}\times 14 = \tfrac{7}{4} = \gamma$ ✓
- Fisher：$\nu(2 - \eta) = 1 \times \tfrac{7}{4} = \tfrac{7}{4} = \gamma$ ✓
- Josephson：$d\nu = 2 = 2 - \alpha$ ✓

六指数两独立的结构在一个**严格可解**的模型上得到完美验证——这是标度假说最有力的支撑。

**关于推导的诚实说明**：Onsager 的原始论文长达数十页，被公认为理论物理中最艰难的计算之一；Kaufman（1949）的旋量方法已大幅简化，现代标准做法是把回路求和化为 Pfaffian（Kasteleyn–Fisher–Temperley 的二聚体方法）或把转移矩阵 Jordan–Wigner 费米子化成自由费米子（Schultz–Mattis–Lieb 1964），骨架仍是"二维 Ising = 自由费米子"。想走通完整推导的读者请直接看参考中 Baxter 的书。

## 7. 与第 9 章的衔接

精确解在整个相变理论中的角色可以总结为三句话：

1. **裁判样本**。第 9 章的 Landau 理论、Ginzburg 判据、标度假设、$\varepsilon$ 展开、Monte Carlo——每个方法第一个对答案的对象就是 2D Ising。$\varepsilon$ 展开在 $\varepsilon = 2$（$d = 2$）处的级数重求和结果与精确指数吻合，是这套微扰机器可信度的关键证据。
2. **普适类的标准像**。二维 Ising 普适类不止包括这个格子模型：气液临界点（格子气模型与之严格等价）、二元合金的有序–无序转变、吸附单原子层的相分离，凡 $d = 2$、序参量对称性 $\mathbb{Z}_2$ 的系统都共享 $\beta = 1/8$ 这组指数——微观细节被 RG 流洗掉（第 9 章第 7 节），Onsager 解出的是整个普适类的指数。
3. **共形不变性的入口**。二维临界点上标度不变性升级为更大的**共形不变性**，二维共形场论把 Ising 临界点的指数、关联函数乃至全部算符内容组织成有限几个"最小模型"之一——这是 1984 年 Belavin–Polyakov–Zamolodchikov 之后的故事，已超出本讲义范围，但值得知道：$\beta = 1/8$ 这些"古怪"的数字在共形场论里是几个简单分数的自然结果。

## 小结

| 概念 | 一句话 |
| --- | --- |
| 模型 | $H = -J\sum_{\langle ij\rangle}\sigma_i\sigma_j$，$\sigma = \pm 1$：离散、经典、最近邻、$\mathbb{Z}_2$——不能再简 |
| 一维无相变 | 畴壁 $\Delta F = 2J - k_B T\ln N < 0$；转移矩阵本征值 $2\cosh K, 2\sinh K$，$f$ 解析 |
| 维度是分水岭 | $d=1$ 熵恒胜；$d=2$ 能量与熵同阶竞争，低温能量胜 |
| Peierls 论证 | 围道数 $\le 4\cdot 3^{L-1}$、代价 $e^{-2KL}$；低温下 $\mathrm{Prob}(\sigma_0=-1) < 1/2 \Rightarrow m > 0$ |
| KW 对偶 | 高温展开（$\tanh K$ 回路）$\leftrightarrow$ 低温展开（$e^{-2K}$ 畴壁）；$\sinh 2K\,\sinh 2K^* = 1$ |
| 精确 $T_c$ | $\sinh 2K_c = 1 \Rightarrow k_B T_c = 2J/\ln(1+\sqrt2) \approx 2.269J$ |
| Onsager | 自由能精确解，$C \propto -\ln\lvert t\rvert$，$\alpha = 0$ |
| Yang | $m = [1-\sinh^{-4}2K]^{1/8}$，$\beta = 1/8$ |
| 指数对比 | 2D Ising：$\alpha=0,\beta=1/8,\gamma=7/4,\delta=15,\nu=1,\eta=1/4$；平均场：$0,1/2,1,3,1/2,0$ |
| 标度律 | Rushbrooke/Widom/Fisher/Josephson 四条全部严格成立 |
| 地位 | 相变理论的裁判样本；二维 Ising 普适类的标准像；共形场论的入口 |

## 自检问题

**1.** 完整复现一维 Ising 的畴壁自由能论证，并用转移矩阵求出本征值、自由能与关联长度，说明为什么 $\lambda_-/\lambda_+ < 1$ 意味着无自发磁化。

<details markdown="1"><summary>点击显示答案</summary>

畴壁论证：基态 $E_0 = -JN$（全同向）。插入一段畴壁（某键两侧反平行）只翻转该键能量 $-J \to +J$，故 $\Delta E = 2J$；墙可置于 $N$ 根键中任一根，$\Delta S = k_B \ln N$。于是

$$\Delta F = 2J - k_B T \ln N,$$

对任意 $T > 0$，$N \to \infty$ 时 $\Delta F < 0$，畴壁自由 proliferate，长程序被摧毁。

转移矩阵：$Z = \mathrm{Tr}\,\mathbb{T}^N$，$\mathbb{T}_{\sigma\sigma'} = e^{K\sigma\sigma'}$。矩阵 $\begin{pmatrix} e^K & e^{-K} \\ e^{-K} & e^K \end{pmatrix}$ 的本征矢为 $(1,\pm1)$，本征值

$$\lambda_\pm = e^K \pm e^{-K} = 2\cosh K,\ 2\sinh K.$$

自由能 $f = -k_B T \ln\big(2\cosh K\big)$ 对一切 $K < \infty$ 解析，无相变。两点关联：把 $\sigma$ 表示成 Pauli 矩阵 $\tau^z$，$\langle\sigma_0\sigma_r\rangle = (\lambda_-/\lambda_+)^r = (\tanh K)^r$，故 $\xi = 1/\ln\coth K$，仅 $K\to\infty$ 发散。

关于磁化：加小场 $h$ 后转移矩阵变为 $\mathbb{T}_{\sigma\sigma'} = e^{K\sigma\sigma' + \beta h(\sigma+\sigma')/2}$，零场极限下 $m \propto \lim_{h\to0}\partial \ln\lambda_{\max}/\partial h$。关键在于 $\lambda_+ > \lambda_-$ 严格成立（间隙 $2e^{-K} > 0$ 对一切有限 $K$ 不闭合），最大本征值非简并、对 $h$ 解析，故 $m(T, h\to0^\pm) \to 0$。二维情形不同：$T < T_c$ 时热力学极限下转移矩阵谱 gap 闭合（两相简并），$m$ 在 $h \to 0$ 处不连续——这正是自发对称破缺的谱语言。

</details>

**2.** 推导 Peierls 围道计数中的 $3^{L-1}$，并用粗略的联合界估计自发磁化非零的温度下界（与精确 $T_c$ 比较）。

<details markdown="1"><summary>点击显示答案</summary>

计数：围道是对偶格子上的闭路径。从任一出发点，第一步有 4 个方向；此后每步到达一个顶点，至多 3 个出方向可选（排除立即回头——回头段两侧不是反平行键，不构成围道的一部分）。闭合约束只会减少选择，故从固定点出发的长 $L$ 围道数 $\le 4\cdot 3^{L-1}$。包围固定格点只再贡献一个 $\lesssim L$ 的多项式因子，不影响指数估计，先略去。

联合界：

$$\mathrm{Prob}(\sigma_0 = -1) \le \sum_{L=4}^{\infty} 4\cdot 3^{L-1} e^{-2KL} = \frac{4}{3}\sum_{L=4}^\infty x^L = \frac{4x^4}{3(1-x)}, \qquad x \equiv 3e^{-2K}.$$

要求级数收敛需 $x < 1$ 即 $e^{-2K} < 1/3$；要求总和 $< 1/2$（使 $\langle\sigma_0\rangle = 1-2P > 0$），解 $\dfrac{4x^4}{3(1-x)} = \dfrac12$ 即 $8x^4 + 3x - 3 = 0$。数值求解：$x = 0.67$ 时 $8(0.2015) + 2.01 - 3 = 0.62 > 0$；$x = 0.64$ 时 $8(0.1678) + 1.92 - 3 = 0.26 > 0$；$x = 0.61$ 时 $8(0.1385)+1.83-3 = -0.06 < 0$，故 $x_c \approx 0.62$。回代 $e^{-2K} = x/3 \approx 0.207$，$2K \approx 1.58$，即 $k_B T \lesssim 1.27\,J$ 时磁化严格非零。

评价：这个下界（$\approx 1.3J$）只有精确值 $2.269J$ 的一半多——联合界高估了围道数（允许自交、未计闭合约束），但 Peierls 论证的价值不在数值而在**定性结论的严格性**：存在有限的 $T_c > 0$。计入围道必须闭合、不得自交等修正后估计可以显著改进。

</details>

**3.** 从恒等式 $e^{K\sigma\sigma'} = \cosh K\,(1 + v\,\sigma\sigma')$ 出发，推导高温展开的回路生成规则，并说明 $\tanh K$ 为何自然出现。

<details markdown="1"><summary>点击显示答案</summary>

恒等式来源：$\sigma\sigma' = \pm 1$ 只有两值，任何关于 $\sigma\sigma'$ 的函数都是线性的：$e^{K\sigma\sigma'} = A + B\,\sigma\sigma'$。取 $\sigma\sigma' = +1$ 得 $e^K = A + B$，取 $-1$ 得 $e^{-K} = A - B$，解出 $A = \cosh K$、$B = \sinh K$，故

$$e^{K\sigma\sigma'} = \cosh K\,\big(1 + v\,\sigma\sigma'\big), \qquad v = \tanh K.$$

$\tanh K$ 是自然展开参数的原因就在这里：它把单键 Boltzmann 权重写成"无关联（$1$）+ 关联（$v\sigma\sigma'$）"的插值，$T \to \infty$ 时 $v \to 0$ 权重均匀，$T \to 0$ 时 $v \to 1$。

回路规则：$Z = (\cosh K)^{2N}\sum_{\{\sigma\}}\prod_{\langle ij\rangle}(1 + v\,\sigma_i\sigma_j)$。把 $2N$ 个因子乘开，每项是每根键上选 $1$ 或选 $v\sigma_i\sigma_j$ 的一个选择——用图表示：选了 $v\sigma_i\sigma_j$ 的键画成粗线。逐项对 $\sigma_i = \pm 1$ 求和：格点 $i$ 处若有奇数条粗键相连，该项含 $\sigma_i$ 的奇次幂，$\sum_{\sigma_i}\sigma_i^{\text{奇}} = 0$，项被杀死；若每个格点都有偶数条（0、2 或 4 条）粗键相连，每项对 $\sigma$ 求和贡献 $2^N$。"每个顶点偶数条边"的图正是**闭合回路（允许自交）的并集**，于是

$$Z = 2^N(\cosh K)^{2N}\sum_{\text{回路 } \Gamma} v^{L(\Gamma)},$$

$L(\Gamma)$ 为总边数。高温下 $v$ 小，长回路被压低，回路稀而短——无序相的图像；$v \to 1$ 时回路失控增殖，正对应临界。

</details>

**4.** 由 $\sinh 2K_c = 1$ 解出 $K_c$ 并数值验证 $k_B T_c \approx 2.269\,J$；论述"自对偶为什么能钉死临界点"，以及论证中隐藏了什么假设。

<details markdown="1"><summary>点击显示答案</summary>

求解：$\sinh 2K_c = 1 \Rightarrow 2K_c = \mathrm{arsinh}\,1 = \ln(1 + \sqrt{1+1}) = \ln(1+\sqrt2)$。数值：$\sqrt2 = 1.41421$，$1+\sqrt2 = 2.41421$，$\ln 2.41421 = 0.88137$，故 $K_c = 0.44069$，

$$k_B T_c = \frac{J}{K_c} = \frac{2J}{0.88137} = 2.2692\,J.$$

验证自洽：$\sinh 0.88137 = (e^{0.88137} - e^{-0.88137})/2 = (2.41421 - 0.41421)/2 = 1$ ✓。

为什么钉死：对偶关系把配分函数（除以解析因子后）在 $K$ 与 $K^*$ 处的值联系起来，$\sinh 2K\,\sinh 2K^* = 1$ 是高温侧与低温侧的一一映射，$K \to 0$ 映到 $K^* \to \infty$，反之亦然。于是自由能的任何奇异性（相变点）若在 $K_c$ 出现，必然也在 $K_c^*$ 出现——奇点在对偶下成对。映射 $K \mapsto K^*$ 有唯一不动点 $K_c = K^*$ 即 $\sinh 2K_c = 1$。**若系统只有一个相变点，它必须就是这个不动点**，否则至少有两个奇点互为对偶。

隐藏的假设："临界点唯一"。对偶性本身并不证明存在性也不证明唯一性——它只给出"若有唯一相变点则在此处"。论证闭环靠两个独立输入：高温级数展开的收敛性证明高温侧无序（无自发磁化）；Peierls 论证证明低温侧有序（$m > 0$）。两侧性质不同，故至少有一个相变点；唯一性则需更强的单调性论证（Griffiths 不等式等），物理上"只有一个临界点"对方格子 Ising 是成立的。Onsager 精确解最终确认：奇点确实只在 $\sinh 2K = 1$ 处。

</details>

**5.** 用 Yang 磁化公式在 $T \to T_c^-$ 展开，验证 $\beta = 1/8$；再用 2D Ising 的精确指数检验 Rushbrooke 标度律 $\alpha + 2\beta + \gamma = 2$。

<details markdown="1"><summary>点击显示答案</summary>

展开：$T \to T_c^-$ 时 $K \to K_c^+$。记 $\delta K \equiv K - K_c \to 0^+$。在 $K_c$ 处 $\sinh 2K_c = 1$，$\cosh 2K_c = \sqrt{1 + \sinh^2 2K_c} = \sqrt2$，故

$$\sinh 2K = \sinh 2K_c + 2\cosh 2K_c\,\delta K + O(\delta K^2) = 1 + 2\sqrt2\,\delta K + O(\delta K^2).$$

于是

$$\sinh^{-4} 2K = \big(1 + 2\sqrt2\,\delta K\big)^{-4} = 1 - 8\sqrt2\,\delta K + O(\delta K^2),$$

$$m = \big[1 - \sinh^{-4}2K\big]^{1/8} = \big(8\sqrt2\,\delta K\big)^{1/8}\big(1 + O(\delta K)\big).$$

把 $\delta K$ 换成约化温度：$K = K_c T_c/T$，故 $\delta K = K_c\,(T_c/T - 1) = K_c\,\dfrac{T_c - T}{T} = K_c\,\lvert t\rvert\,\big(1 + O(\lvert t\rvert)\big)$，是 $\lvert t\rvert$ 的线性函数。所以

$$m \propto \lvert t\rvert^{1/8} \qquad \Longrightarrow \qquad \beta = \frac{1}{8}.$$

振幅也算出来了：$m \approx (8\sqrt2\,K_c\,\lvert t\rvert)^{1/8} = (8\sqrt2 \times 0.4407\,\lvert t\rvert)^{1/8} \approx (4.984\,\lvert t\rvert)^{1/8}$。

Rushbrooke 检验：2D Ising 精确值 $\alpha = 0$（对数发散，弱于任何正幂）、$\beta = 1/8$、$\gamma = 7/4$：

$$\alpha + 2\beta + \gamma = 0 + 2\times\frac18 + \frac74 = \frac14 + \frac74 = 2.\ \checkmark$$

作为对照，平均场值 $0 + 2\times\frac12 + 1 = 2$ 也满足——标度律是普适的结构关系，独立于具体指数取值；真正区分理论对错的是指数本身。附带检验 Widom：$\beta(\delta - 1) = \frac18 \times 14 = \frac74 = \gamma$ ✓。六指数两独立的标度结构在精确解上全部闭合，这正是"2D Ising 是相变理论裁判样本"的定量含义。

</details>

## 参考

- Pathria & Beale《Statistical Mechanics》（第 3 版）第 12–13 章：Ising 模型的一维转移矩阵解法、临界现象综述——与本篇第 3、6 节对应最直接。
- Kardar《Statistical Physics of Fields》第 3 章：对偶性与级数展开的简洁讲法，Kramers–Wannier 对偶的推导可对照本篇第 5 节。
- Goldenfeld《Lectures on Phase Transitions and the Renormalization Group》第 5 章：Ising 模型与平均场失效的讨论，衔接第 9 章正文。
- Baxter《Exactly Solved Models in Statistical Mechanics》第 1、7 章：二维 Ising 精确解的标准现代教材处理（含自由费米子化简），想走通 Onsager 推导从这里入门。
- 原始文献：Onsager, Phys. Rev. 65, 117 (1944)——自由能精确解，以难读著称；Yang（杨振宁）, Phys. Rev. 85, 808 (1952)——自发磁化 $m = [1-\sinh^{-4}2K]^{1/8}$；Kramers & Wannier, Phys. Rev. 60, 252 (1941)——对偶性与 $T_c$ 的定位，早于精确解三年。
