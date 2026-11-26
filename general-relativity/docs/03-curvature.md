# 曲率：平行移动的路径依赖与潮汐力

> 路线图位置：第 1 部分（微分几何工具）· 第 3 章
> 前置知识：第 2 章（联络、平行移动、和乐、测地线）。
> 学习目标：会用 $[\nabla,\nabla]$ 定义 Riemann 张量并写出其坐标表达式；能列出四条对称性并解释"4 维独立分量 20"的计数；会从第二 Bianchi 恒等式得到 $\nabla_\mu G^{\mu\nu}=0$ 并说清 $\frac12$ 从哪来；会写测地偏离方程并用 $R_{i0j0}\approx\partial_i\partial_j\Phi$ 解释潮汐力；认识 Weyl 张量与 Killing 矢量。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。**曲率约定与论文 (3.23) 一致**：

$$2\nabla_{[\rho}\nabla_{\sigma]}v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu,\qquad R_{\mu\nu}=R^\rho{}_{\mu\rho\nu}.$$

（与 Wald 相同；与一些教材差整体符号，比较公式前先对齐这一行。）

## 1. 一句话总结

**曲率就是"平行移动一圈不回到自己"的无穷小版本。** 把这件事写成代数，就是协变导数的对易子：$[\nabla_\rho,\nabla_\sigma]v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu$。Riemann 张量在 4 维有 20 个独立分量，缩并两次得 Ricci（10 个）与标量曲率；无迹部分（Weyl，10 个）是"纯潮汐"的部分，真空里只剩它。第二 Bianchi 恒等式经一次缩并给 $\nabla_\mu R^{\mu\nu}=\frac12\nabla^\nu R$，这迫使 Einstein 张量必须是 $R_{\mu\nu}-\frac12Rg_{\mu\nu}$——**系数 $\frac12$ 不是猜的，是恒等式逼出来的**。

## 2. 三条等价的定义路线

### 2.1 和乐（几何）

第 2 章：绕无穷小回路平行移动，$v$ 转了一个小角度，转角密度就是曲率：

$$\delta v^\mu=-\tfrac12R^\mu{}_{\nu\rho\sigma}v^\nu\,\Sigma^{\rho\sigma}.$$

### 2.2 对易子（代数）

$$\boxed{\;[\nabla_\rho,\nabla_\sigma]v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu\;}$$

这是最便于计算的版本，也是本书采用的定义。

### 2.3 测地偏离（物理）

两条相邻的测地线，间距 $\xi^\mu$ 满足

$$\frac{D^2\xi^\mu}{\mathrm{d}\tau^2}=R^\mu{}_{\nu\rho\sigma}T^\nu T^\rho\xi^\sigma
=-R^\mu{}_{\nu\rho\sigma}T^\nu\xi^\rho T^\sigma .$$

（两种写法等价：$R$ 对后两个指标反对称，把 $\xi$ 从第 4 个槽搬到第 3 个槽要加负号。**注意 $\xi$ 在哪个槽**——这是最容易出符号错的地方，自检 5 会用牛顿极限校准。）右边就是**潮汐力**：曲率是"相邻自由落体之间的相对加速度"。

**三条路线的等价性**不是本章要证的重点（它是标准的），但值得记住各自的用途：和乐给几何直觉，对易子给计算，测地偏离给物理。

## 3. Riemann 张量

### 3.1 坐标表达式

由 $[\nabla_\rho,\nabla_\sigma]v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu$ 逐项展开（自检 1）：

$$\boxed{\;R^\mu{}_{\nu\rho\sigma}
=\partial_\rho\Gamma^\mu{}_{\sigma\nu}-\partial_\sigma\Gamma^\mu{}_{\rho\nu}
+\Gamma^\mu{}_{\rho\lambda}\Gamma^\lambda{}_{\sigma\nu}
-\Gamma^\mu{}_{\sigma\lambda}\Gamma^\lambda{}_{\rho\nu}.\;}$$

**结构**：两项 $\partial\Gamma$（差）+ 两项 $\Gamma\Gamma$（差）。$\partial\Gamma$ 是二阶导数，$\Gamma\Gamma$ 是"非线性补偿"——它保证 $R$ 是张量（$\Gamma$ 的非齐次项在两次导数里相消）。

**为什么必须无挠**：展开时会出现 $-\Gamma^\beta{}_{\rho\sigma}\partial_\beta v^\mu+\Gamma^\beta{}_{\sigma\rho}\partial_\beta v^\mu$，只有 $\Gamma$ 对后两指标对称时才相消。**有挠的理论里，曲率与挠率会混在一起**（Einstein–Cartan），这是第 5s 章一阶引力的一个伏笔。

### 3.2 四条对称性

$$R_{\mu\nu\rho\sigma}=-R_{\nu\mu\rho\sigma}=-R_{\mu\nu\sigma\rho}=R_{\rho\sigma\mu\nu},\qquad
R_{\mu[\nu\rho\sigma]}=0 .$$

前三条是"反对称 + 成对交换"，第四条叫**第一 Bianchi 恒等式**（代数，不是微分）。

**计数**（自检 2）：先把 $(\mu\nu)$ 与 $(\rho\sigma)$ 各自反对称化，得 $6\times6=36$；成对交换对称再减到 $\frac{6\times7}{2}=21$；第一 Bianchi 给 1 个独立关系 ⇒

$$\boxed{4\ \text{维}: \quad 20\ \text{个独立分量}.}$$

### 3.3 为什么选坐标不能消掉曲率

第 2 章说过：每点可选坐标使 $\Gamma(p)=0$。此时

$$R^\mu{}_{\nu\rho\sigma}(p)=\partial_\rho\Gamma^\mu{}_{\sigma\nu}(p)-\partial_\sigma\Gamma^\mu{}_{\rho\nu}(p).$$

$\Gamma$ 的一阶导数**不能**再靠选坐标消掉（那是二阶导数自由度）。所以曲率是"坐标消不掉的弯曲"，这是"引力不能被等效原理局部消除"的精确含义：**潮汐力是等效原理消不掉的部分**。

## 4. Ricci、标量曲率、Einstein 张量

### 4.1 缩并

$$R_{\mu\nu}\equiv R^\rho{}_{\mu\rho\nu},\qquad R\equiv g^{\mu\nu}R_{\mu\nu},\qquad
G_{\mu\nu}\equiv R_{\mu\nu}-\tfrac12R\,g_{\mu\nu}.$$

$R_{\mu\nu}$ 对称（自检 2）。4 维中 10 个独立分量；$R$ 是 1 个标量。

### 4.2 第二 Bianchi 与 $\nabla G=0$

微分版的 Bianchi 恒等式：

$$\nabla_{[\lambda}R_{\mu\nu]\rho\sigma}=0 .$$

经两次缩并（自检 3 讨论 $\frac12$ 的来源）：

$$\boxed{\;\nabla^\mu R_{\mu\nu}=\tfrac12\nabla_\nu R
\;\Longleftrightarrow\;
\nabla^\mu G_{\mu\nu}=0\;}$$

**这条恒等式的重要性**：

1. **Einstein 方程的左边必须是 $G_{\mu\nu}$**：因为右边 $\nabla^\mu T_{\mu\nu}=0$（能量守恒），左边必须自动无散。$R_{\mu\nu}+\alpha Rg_{\mu\nu}$ 的无散性要求 $\alpha=-\frac12$。
2. **$\Lambda$ 项是允许的**：$\nabla^\mu(g_{\mu\nu}\Lambda)=0$ 自动成立，所以可以加。
3. **初始数据的约束**（第 11 章）：$\nabla^\mu G_{\mu\nu}=0$ 的 4 个分量意味着 10 个 Einstein 方程里只有 6 个是独立的演化方程，另外 4 个是约束。

### 4.3 真空 Einstein 方程的等价形式

$G_{\mu\nu}=0$ 与 $R_{\mu\nu}=0$ 等价（4 维）：对 $G_{\mu\nu}=0$ 取迹，

$$g^{\mu\nu}G_{\mu\nu}=R-\tfrac12 R\cdot4=-R=0\;\Longrightarrow\;R=0,$$

代回得 $R_{\mu\nu}=0$。**这一步在 $d\neq4$ 时不成立**（$R=\frac{2}{d-2}\cdot$ 某物），是"4 维特殊"的一个小例子。

带宇宙学常数时：$G_{\mu\nu}+\Lambda g_{\mu\nu}=0$ 取迹给 $R=4\Lambda$，代回得

$$\boxed{\;R_{\mu\nu}=\Lambda g_{\mu\nu}\;}$$

（论文 (3.19) 用的就是这一形式）。

## 5. Weyl 张量：潮汐的那一半

### 5.1 定义

$$\boxed{\;C_{\mu\nu\rho\sigma}=R_{\mu\nu\rho\sigma}
-\tfrac12\left(g_{\mu\rho}R_{\nu\sigma}-g_{\mu\sigma}R_{\nu\rho}+g_{\nu\sigma}R_{\mu\rho}-g_{\nu\rho}R_{\mu\sigma}\right)
+\tfrac{R}{6}\left(g_{\mu\rho}g_{\nu\sigma}-g_{\mu\sigma}g_{\nu\rho}\right).\;}$$

它有 Riemann 的全部对称性，且**所有缩并为零**（$C^\mu{}_{\nu\mu\sigma}=0$）。4 维中 10 个独立分量：

$$20\ (\text{Riemann})=10\ (\text{Ricci})+10\ (\text{Weyl}).$$

### 5.2 两个极端

- **真空**（$R_{\mu\nu}=0$）：$R_{\mu\nu\rho\sigma}=C_{\mu\nu\rho\sigma}$。**真空里的全部曲率都是潮汐**（第 6 章的 Schwarzschild 就是纯 Weyl）。
- **共形平坦**：$C_{\mu\nu\rho\sigma}=0$ $\Longleftrightarrow$ 度规可以写成 $\Omega^2\eta_{\mu\nu}$（局部）。**Weyl 是"形状畸变"，Ricci 是"体积变化"**。

**与 $\Lambda$ 的关系**：$R_{\mu\nu}=\Lambda g_{\mu\nu}$ 时 $R=4\Lambda$，代入定义可验证 $C$ 与 $\Lambda$ 无关——**宇宙学常数只改变 Ricci 部分，不改变 Weyl**。这就是为什么 de Sitter 与 Minkowski 的潮汐结构在局部上可以很像。

## 6. 测地偏离与潮汐力

### 6.1 方程

设一簇测地线 $x^\mu(\tau,s)$，$T^\mu=\partial_\tau x^\mu$、$\xi^\mu=\partial_s x^\mu$。由 $[T,\xi]=0$、测地线方程与 Ricci 恒等式（自检 5 给完整推导）：

$$\boxed{\;\frac{D^2\xi^\mu}{\mathrm{d}\tau^2}
=R^\mu{}_{\nu\rho\sigma}T^\nu T^\rho\xi^\sigma
=-R^\mu{}_{\nu\rho\sigma}T^\nu\xi^\rho T^\sigma\;}$$

**读法**：$\xi$ 是"两个自由落体之间的位移"，左边是它们的相对加速度，右边是曲率。**潮汐力 = 曲率**。

**再强调一次符号位置**：$\xi$ 必须落在**最后一个指标槽**——要么写成 $R^\mu{}_{\nu\rho\sigma}T^\nu T^\rho\xi^\sigma$，要么用反对称性写成 $-R^\mu{}_{\nu\rho\sigma}T^\nu\xi^\rho T^\sigma$。这两种是同一个式子；把负号丢掉（写成 $+R^\mu{}_{\nu\rho\sigma}T^\nu\xi^\rho T^\sigma$）会整体翻号，潮汐力就变成"吸引"而不是"剪切"。

### 6.2 牛顿极限

弱场、低速：$T^\mu\approx(1,\vec0)$，$\tau\approx t$。代入 $\xi$ 在第 4 槽的形式：

$$\frac{\mathrm{d}^2\xi^i}{\mathrm{d}t^2}\approx R^i{}_{00j}\xi^j=-R^i{}_{0j0}\xi^j .$$

定义**电潮汐张量**

$$E_{ij}\equiv R_{i0j0}.$$

则

$$\boxed{\;\frac{\mathrm{d}^2\xi^i}{\mathrm{d}t^2}=-E^i{}_j\,\xi^j,\qquad E_{ij}\approx\partial_i\partial_j\Phi\;}$$

（$E_{ij}\approx\partial_i\partial_j\Phi$ 的推导见自检 5）。这正是牛顿潮汐方程。

**取迹**：

$$E^i{}_i=g^{ij}E_{ij}=\nabla^2\Phi=R_{00}\ \bigl(=4\pi G_N\rho\bigr).$$

**对点质量** $\Phi=-G_NM/r$：

$$E_{ij}=G_NM\left(\frac{\delta_{ij}}{r^3}-\frac{3x_ix_j}{r^5}\right).$$

径向本征值 $-2G_NM/r^3$，横向 $+G_NM/r^3$。于是

$$\ddot\xi^r=+\frac{2G_NM}{r^3}\xi^r\ \text{（拉伸）},\qquad
\ddot\xi^\perp=-\frac{G_NM}{r^3}\xi^\perp\ \text{（压缩）}.$$

这就是"面条化"（spaghettification）。

**关键点**：$E_{ij}$ 在真空里无迹（$\nabla^2\Phi=0$），所以"拉伸 + 压缩"相抵——**潮汐力是纯粹的剪切**。而真空里 Riemann = Weyl，故

$$E_{ij}=R_{i0j0}=C_{i0j0}\quad(\text{真空}),$$

即潮汐张量是 Weyl 张量的"电部分"。Ricci 管体积（物质源），Weyl 管形状（潮汐），这句话在这里第一次变成公式。

## 7. Killing 矢量：度规的对称性

### 7.1 定义

$$K^\mu\ \text{是 Killing 矢量}\;\Longleftrightarrow\;\boxed{\;\nabla_{(\mu}K_{\nu)}=0\;}$$

等价说法：沿 $K$ 的流，度规不变，$\pounds_K g_{\mu\nu}=0$。

### 7.2 守恒量

沿测地线，$K_\mu\dot x^\mu$ 守恒：

$$\frac{\mathrm{d}}{\mathrm{d}\tau}\left(K_\mu\dot x^\mu\right)
=\dot x^\mu\dot x^\nu\nabla_\mu K_\nu
=\tfrac12\dot x^\mu\dot x^\nu\nabla_{(\mu}K_{\nu)}=0 .$$

这就是第 6 章 Schwarzschild 里"能量 $E=-K_{(t)}\cdot\dot x$、角动量 $L=K_{(\phi)}\cdot\dot x$"的来源，也是[理论力学书第 6 章](../../classical-mechanics/docs/06-noether-theorem.md) Noether 定理在时空几何里的化身。

### 7.3 数目

4 维时空最多有 10 个独立 Killing 矢量（$\frac{4\times5}{2}$）：

- 4 个平移 + 3 个转动 + 3 个 boost = 10（Minkowski，最大对称）；
- Schwarzschild：2 个（$\partial_t$ 与 $\partial_\phi$）；
- 一般时空：0 个。

**"Killing 矢量多 ⇒ 对称性高 ⇒ 容易解"**：Schwarzschild 的 2 个 Killing 矢量让我们能把测地线降到二维（第 6 章），de Sitter 的 10 个让它可以用共形坐标。

## 8. 小结

- 曲率 = 平行移动的路径依赖 = $[\nabla_\rho,\nabla_\sigma]v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu$ = 测地偏离。
- $R^\mu{}_{\nu\rho\sigma}=\partial_\rho\Gamma^\mu{}_{\sigma\nu}-\partial_\sigma\Gamma^\mu{}_{\rho\nu}+\Gamma\Gamma-\Gamma\Gamma$；四条对称性；4 维 20 个独立分量。
- 缩并：$R_{\mu\nu}$（10 个）、$R$、$G_{\mu\nu}=R_{\mu\nu}-\frac12Rg_{\mu\nu}$。
- 第二 Bianchi ⇒ $\nabla^\mu R_{\mu\nu}=\frac12\nabla_\nu R$ ⇒ $\nabla^\mu G_{\mu\nu}=0$ ⇒ 系数 $\frac12$ 被逼出来，且 $\Lambda$ 可以加。
- 4 维真空：$G=0\Leftrightarrow R_{\mu\nu}=0$；带 $\Lambda$：$R_{\mu\nu}=\Lambda g_{\mu\nu}$。
- Weyl = Riemann − Ricci 部分，10 个分量，无迹；真空曲率 = 纯 Weyl = 纯潮汐；共形平坦 $\Leftrightarrow C=0$。
- 测地偏离 $\frac{D^2\xi^\mu}{d\tau^2}=R^\mu{}_{\nu\rho\sigma}T^\nu\xi^\rho T^\sigma$；牛顿极限给 $\ddot\xi^i=-\partial_i\partial_j\Phi\,\xi^j$（拉伸 + 压缩，无迹）。
- Killing 矢量 $\nabla_{(\mu}K_{\nu)}=0$ ⇒ $K_\mu\dot x^\mu$ 守恒；4 维最多 10 个。

## 自检问题

**1.** 从 $[\nabla_\rho,\nabla_\sigma]v^\mu=R^\mu{}_{\nu\rho\sigma}v^\nu$ 出发，展开协变导数，推出 $R$ 的坐标表达式，并指出哪一步用了无挠性。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：展开一次。**

$$\nabla_\sigma v^\mu=\partial_\sigma v^\mu+\Gamma^\mu{}_{\sigma\alpha}v^\alpha .$$

**第二步：再作用一次。**

$$\nabla_\rho\nabla_\sigma v^\mu
=\partial_\rho\partial_\sigma v^\mu+\left(\partial_\rho\Gamma^\mu{}_{\sigma\alpha}\right)v^\alpha+\Gamma^\mu{}_{\sigma\alpha}\partial_\rho v^\alpha
+\Gamma^\mu{}_{\rho\beta}\left(\partial_\sigma v^\beta+\Gamma^\beta{}_{\sigma\alpha}v^\alpha\right)
-\Gamma^\beta{}_{\rho\sigma}\left(\partial_\beta v^\mu+\Gamma^\mu{}_{\beta\alpha}v^\alpha\right).$$

**第三步：反对称化 $\rho\leftrightarrow\sigma$。** 逐类看：

- $\partial_\rho\partial_\sigma v^\mu$：对称，相消。
- $\left(\partial_\rho\Gamma^\mu{}_{\sigma\alpha}-\partial_\sigma\Gamma^\mu{}_{\rho\alpha}\right)v^\alpha$：保留。
- $\Gamma^\mu{}_{\sigma\alpha}\partial_\rho v^\alpha-\Gamma^\mu{}_{\rho\alpha}\partial_\sigma v^\alpha$：保留。
- $\Gamma^\mu{}_{\rho\beta}\partial_\sigma v^\beta-\Gamma^\mu{}_{\sigma\beta}\partial_\rho v^\beta$：把哑指标 $\beta\leftrightarrow\alpha$ 改名，发现它**正好是上一行的负值**，相消。
- $\left(\Gamma^\mu{}_{\rho\beta}\Gamma^\beta{}_{\sigma\alpha}-\Gamma^\mu{}_{\sigma\beta}\Gamma^\beta{}_{\rho\alpha}\right)v^\alpha$：保留。
- $-\Gamma^\beta{}_{\rho\sigma}\partial_\beta v^\mu+\Gamma^\beta{}_{\sigma\rho}\partial_\beta v^\mu$：**只有无挠时为零**。

**第四步：结果。**

$$\boxed{R^\mu{}_{\nu\rho\sigma}=\partial_\rho\Gamma^\mu{}_{\sigma\nu}-\partial_\sigma\Gamma^\mu{}_{\rho\nu}
+\Gamma^\mu{}_{\rho\lambda}\Gamma^\lambda{}_{\sigma\nu}-\Gamma^\mu{}_{\sigma\lambda}\Gamma^\lambda{}_{\rho\nu}.}\qquad\square$$

**无挠性用在哪**：最后一行。有挠时它留下 $(\Gamma^\beta{}_{\sigma\rho}-\Gamma^\beta{}_{\rho\sigma})\partial_\beta v^\mu$，这会破坏"$R$ 只乘 $v$、不乘 $\partial v$"的结构——所以对易子定义曲率的前提是无挠（或者把挠率单独拿出来）。

**两个可检验的极限**：

1. 平直空间 $\Gamma=0$ ⇒ $R=0$ ✓。
2. 常数曲率空间（球面/双曲）的 $R$ 与 $\Gamma$ 同阶，符合"曲率是二阶导数但可被 $\Gamma\Gamma$ 抵消一部分"。

</details>

**2.** 验证 $R_{\mu\nu\rho\sigma}$ 的对称性，并完成"4 维 20 个独立分量"的计数。再证明 $R_{\mu\nu}$ 对称。

<details markdown="1"><summary>点击显示答案</summary>

**反对称性**：$R_{\mu\nu\rho\sigma}=-R_{\nu\mu\rho\sigma}$ 与 $R_{\mu\nu\rho\sigma}=-R_{\mu\nu\sigma\rho}$ 可直接从对易子的反对称性与坐标表达式读出（$\Gamma$ 的对称性使 $\partial\Gamma-\partial\Gamma$ 与 $\Gamma\Gamma-\Gamma\Gamma$ 各自反对称）。

**成对交换**：$R_{\mu\nu\rho\sigma}=R_{\rho\sigma\mu\nu}$。这一条不显然，标准证法是把它写成"度规的二阶导数组合"：

$$R_{\mu\nu\rho\sigma}=\tfrac12\left(\partial_\nu\partial_\rho g_{\mu\sigma}-\partial_\mu\partial_\rho g_{\nu\sigma}-\partial_\nu\partial_\sigma g_{\mu\rho}+\partial_\mu\partial_\sigma g_{\nu\rho}\right)+\text{（}\Gamma\Gamma\text{ 的非线性项）},$$

在局部惯性系（$\Gamma=0$）里只剩前一项，它对 $(\mu\nu)\leftrightarrow(\rho\sigma)$ 明显对称；由于两边都是张量，在局部惯性系成立就在所有点成立（第 1 章自检 4 的技巧）。

**第一 Bianchi**：$R_{\mu[\nu\rho\sigma]}=0$。在局部惯性系里 $\partial_{[\lambda}R_{\mu\nu]\rho\sigma}=0$ 是"二阶偏导可交换"的直接推论；一般情形由张量性延拓。

**计数**：

1. $(\mu\nu)$ 反对称 ⇒ 6 个独立组合；$(\rho\sigma)$ 反对称 ⇒ 6 个。合计 $36$。
2. 成对交换对称 ⇒ 把 $36$ 个看成 $6\times6$ 对称矩阵，独立数 $\frac{6\times7}{2}=21$。
3. 第一 Bianchi $R_{\mu[\nu\rho\sigma]}=0$ ⇒ 1 个独立关系。

$$36\to21\to20 .$$

**独立关系为什么只有 1 个**：$R_{\mu[\nu\rho\sigma]}$ 对四个指标全反对称，是 4-形式，在 4 维只有 1 个独立分量（正比于 $\epsilon_{\mu\nu\rho\sigma}$）。所以它给 1 个约束。

**$R_{\mu\nu}$ 对称**：$R_{\mu\nu}=g^{\rho\sigma}R_{\rho\mu\sigma\nu}$。用成对交换 $R_{\rho\mu\sigma\nu}=R_{\sigma\nu\rho\mu}$，再交换 $\rho\leftrightarrow\sigma$：

$$R_{\mu\nu}=R_{\sigma\nu\rho\mu}g^{\rho\sigma}=R_{\nu\mu},$$

最后一步是把哑指标重命名并认出右边的定义。$\square$

**4 维的巧合**：20 恰好也等于"度规的二阶导数在一点上的独立分量数"（$g_{\mu\nu}$ 有 10 个分量，每个有二阶导，扣掉坐标变换的 4 个自由度与一阶/零阶的约束）。这不是巧合：**Riemann 张量就是"坐标消不掉的度规二阶导数"的全部内容**。

</details>

**3.** 假设 Einstein 张量写成 $H_{\mu\nu}=R_{\mu\nu}+\alpha Rg_{\mu\nu}$，用第二 Bianchi 的缩并形式 $\nabla^\mu R_{\mu\nu}=\frac12\nabla_\nu R$ 证明：只有 $\alpha=-\frac12$ 时 $\nabla^\mu H_{\mu\nu}=0$ 对所有度规成立。再说明为什么 $\Lambda g_{\mu\nu}$ 可以额外加。

<details markdown="1"><summary>点击显示答案</summary>

**计算散度**：

$$\nabla^\mu H_{\mu\nu}=\nabla^\mu R_{\mu\nu}+\alpha\nabla_\nu R
=\tfrac12\nabla_\nu R+\alpha\nabla_\nu R
=\left(\tfrac12+\alpha\right)\nabla_\nu R .$$

要求对**所有**度规 $\nabla^\mu H_{\mu\nu}=0$，即对所有解（$\nabla_\nu R$ 不必为零）都成立，必须

$$\boxed{\alpha=-\tfrac12 .}\qquad\square$$

**为什么不能靠"只对某类解成立"蒙混**：如果只要求"在 $R=$ 常数的解上成立"，任何 $\alpha$ 都行。但 Einstein 方程的左边必须**恒等地**无散——否则一旦 $R$ 不是常数（有物质、有辐射），$\nabla^\mu G_{\mu\nu}=0$ 与 $\nabla^\mu T_{\mu\nu}=0$ 就不能同时成立。所以要求是"对任意度规"。

**$\Lambda$ 为什么可以加**：$\nabla^\mu(\Lambda g_{\mu\nu})=\Lambda\nabla^\mu g_{\mu\nu}=0$（度量相容），与度规无关。所以

$$G_{\mu\nu}+\Lambda g_{\mu\nu}$$

仍然恒等地无散，对应 $T_{\mu\nu}\to T_{\mu\nu}-\frac{\Lambda}{8\pi G}g_{\mu\nu}$（真空能）。

**深一层的读法**：$\nabla^\mu G_{\mu\nu}=0$ 是"几何的 Bianchi 恒等式"，$\nabla^\mu T_{\mu\nu}=0$ 是"物质的运动方程"。Einstein 方程把两者等同，于是**物质的守恒不是额外假设，而是几何恒等式的推论**。这是广义相对论最优雅的结构之一：它把"能动张量守恒"从一条独立的物理定律变成了"$G_{\mu\nu}$ 的数学性质"。

**反向的检验**：如果哪天发现某种物质不满足 $\nabla^\mu T_{\mu\nu}=0$（例如有能量泄漏到额外维度），那么 Einstein 方程就必须修改——因为左边恒无散。这正是修改引力理论的一个出发点。

</details>

**4.** 计算 2D 球面 $ds^2=a^2(d\theta^2+\sin^2\theta d\phi^2)$ 的 $R_{\theta\phi\theta\phi}$、$R_{\mu\nu}$ 与 $R$，并验证 $R_{\mu\nu}=\frac{1}{a^2}g_{\mu\nu}$、$R=2/a^2$。再说明为什么这与 Schwarzschild 的 $R=0$ 不矛盾。

<details markdown="1"><summary>点击显示答案</summary>

**用克氏符**（第 2 章自检 3）：$\Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta$，$\Gamma^\phi{}_{\theta\phi}=\cot\theta$。

**算 $R_{\theta\phi\theta\phi}$**：用定义 $R_{\theta\phi\theta\phi}=g_{\theta\mu}R^\mu{}_{\phi\theta\phi}$，先算 $R^\theta{}_{\phi\theta\phi}$：

$$R^\theta{}_{\phi\theta\phi}=\partial_\theta\Gamma^\theta{}_{\phi\phi}-\partial_\phi\Gamma^\theta{}_{\theta\phi}+\Gamma^\theta{}_{\theta\lambda}\Gamma^\lambda{}_{\phi\phi}-\Gamma^\theta{}_{\phi\lambda}\Gamma^\lambda{}_{\theta\phi}.$$

逐项：$\partial_\theta(-\sin\theta\cos\theta)=-(\cos^2\theta-\sin^2\theta)$；第二项为零；第三项 $\Gamma^\theta{}_{\theta\lambda}\Gamma^\lambda{}_{\phi\phi}=0$（$\Gamma^\theta{}_{\theta\cdot}=0$ 除了…全为零）；第四项 $-\Gamma^\theta{}_{\phi\phi}\Gamma^\phi{}_{\theta\phi}=-(-\sin\theta\cos\theta)(\cot\theta)=\sin\theta\cos^2\theta/\sin\theta=\cos^2\theta$。

合计：

$$R^\theta{}_{\phi\theta\phi}=-(\cos^2\theta-\sin^2\theta)+\cos^2\theta=\sin^2\theta .$$

于是

$$R_{\theta\phi\theta\phi}=g_{\theta\theta}R^\theta{}_{\phi\theta\phi}=a^2\sin^2\theta .$$

**Ricci**：$R_{\phi\phi}=R^\theta{}_{\phi\theta\phi}=g^{\theta\theta}R_{\theta\phi\theta\phi}=\frac{1}{a^2}\cdot a^2\sin^2\theta=\sin^2\theta=\frac{1}{a^2}g_{\phi\phi}$ ✓。

同理（或用对称性）$R_{\theta\theta}=1=\frac{1}{a^2}g_{\theta\theta}$。所以

$$\boxed{R_{\mu\nu}=\frac{1}{a^2}g_{\mu\nu},\qquad
R=g^{\mu\nu}R_{\mu\nu}=\frac{2}{a^2}.}\qquad\square$$

**这与 Schwarzschild 不矛盾**：Schwarzschild 是**真空**解，$R_{\mu\nu}=0$ 必然 $R=0$（4 维真空）。球面是**内禀弯曲的二维空间**，它的 Ricci 不为零——因为它不是"某个四维真空时空的截面"necessarily，而且二维里 $R_{\mu\nu}=\frac{R}{2}g_{\mu\nu}$ 恒成立（只有一种曲率）。

**一个更有用的对照**：如果把球面看作 4 维时空里的一个二维曲面（例如 Schwarzschild 的 $r=$ const、$t=$ const 面），它的**内禀**曲率是 $2/r^2$，但那个四维时空的整体曲率是 $R=0$。**内禀曲率与外曲率是两回事**：球面在平直三维空间里的内禀曲率来自"嵌入"，而 4 维 Schwarzschild 的真空性说的是"四维 Ricci 为零"。第 10 章的 GHY 项处理的正是"外曲率"（嵌入的弯曲），不是内禀曲率。

</details>

**5.** 推出测地偏离方程，并在牛顿极限下验证 $R_{i0j0}\approx\partial_i\partial_j\Phi$、$\ddot\xi^i=-\partial_i\partial_j\Phi\,\xi^j$；再说明为什么这个张量在真空里无迹、以及它与 Weyl 的关系。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：建立标架。** 设 $x^\mu(\tau,s)$ 是一族测地线，$T^\mu=\partial x^\mu/\partial\tau$，$\xi^\mu=\partial x^\mu/\partial s$。则 $[T,\xi]=0$，即

$$\nabla_T\xi^\mu=\nabla_\xi T^\mu .$$

**第二步：两步换序。** 相对加速度是

$$a^\mu\equiv\nabla_T\nabla_T\xi^\mu=\nabla_T\left(\nabla_\xi T\right)^\mu .$$

因为 $\nabla_TT=0$（测地线），所以 $\nabla_\xi\nabla_TT=0$；于是

$$a^\mu=\nabla_T\nabla_\xi T^\mu
=\nabla_\xi\nabla_TT^\mu+\left[\nabla_T,\nabla_\xi\right]T^\mu
=0+R^\mu{}_{\nu T\xi}T^\nu .$$

**第三步：写成标准形式。**

$$\boxed{\;\frac{D^2\xi^\mu}{\mathrm{d}\tau^2}=R^\mu{}_{\nu\rho\sigma}T^\nu T^\rho\xi^\sigma
=-R^\mu{}_{\nu\rho\sigma}T^\nu\xi^\rho T^\sigma\;}$$

（第二式用 $R$ 对后两指标反对称。）**注意 $\xi$ 落在最后一个槽**：这一步只用了"$[T,\xi]=0$ + 测地线 + Ricci 恒等式"，没有任何近似，所以符号是硬的。$\square$

**第四步：牛顿极限。** $T^\mu\approx(1,\vec0)$，$\tau\approx t$，取 $\xi$ 为纯空间：

$$\frac{\mathrm{d}^2\xi^i}{\mathrm{d}t^2}\approx R^i{}_{00j}\xi^j=-R^i{}_{0j0}\xi^j .$$

**第五步：算 $R_{i0j0}$。** $g_{00}=-(1+2\Phi)$，$g_{ij}\approx\delta_{ij}$，静态。先算联络：

$$\Gamma^i_{00}=\tfrac12g^{ij}\left(2\partial_0g_{j0}-\partial_jg_{00}\right)
=\tfrac12\delta^{ij}\left(0+2\partial_j\Phi\right)=\partial_i\Phi .$$

再由定义（静态 ⇒ $\partial_0=0$；一阶 ⇒ 丢掉 $\Gamma\Gamma$）：

$$R^i{}_{0j0}=\partial_j\Gamma^i_{00}-\partial_0\Gamma^i_{j0}+\Gamma\Gamma-\Gamma\Gamma
\approx\partial_j\partial_i\Phi .$$

于是

$$R_{i0j0}=g_{ik}R^k{}_{0j0}\approx\delta_{ik}\partial_k\partial_j\Phi=\partial_i\partial_j\Phi .$$

**核验（取迹）**：

$$g^{ij}R_{i0j0}=\delta^{ij}\partial_i\partial_j\Phi=\nabla^2\Phi ,$$

而 $\nabla^2\Phi=R_{00}$（第 5 章会独立算一遍）——两者一致 ✓。所以 $R_{i0j0}=+\partial_i\partial_j\Phi$ 的符号是对的。

**第六步：潮汐方程。**

$$\frac{\mathrm{d}^2\xi^i}{\mathrm{d}t^2}=-R^i{}_{0j0}\xi^j=-\partial_i\partial_j\Phi\,\xi^j .$$

这正是牛顿潮汐方程（两点各受 $-\nabla\Phi$，差一个梯度）。$\square$

**符号的直观检验**（点质量 $\Phi=-G_NM/r$）：

$$E_{ij}\equiv R_{i0j0}=G_NM\left(\frac{\delta_{ij}}{r^3}-\frac{3x_ix_j}{r^5}\right).$$

径向本征值 $-2G_NM/r^3$，故 $\ddot\xi^r=-\left(-2G_NM/r^3\right)\xi^r=+\frac{2G_NM}{r^3}\xi^r\gt0$——**拉伸**（里面的粒子落得更快，间距变大）✓。横向本征值 $+G_NM/r^3$，故 $\ddot\xi^\perp=-\frac{G_NM}{r^3}\xi^\perp\lt0$——**压缩** ✓。这个符号只有在 $\xi$ 位于第 4 槽时才对；若误写成第 3 槽，拉伸会变成压缩。

**无迹与 Weyl**：真空里 $R_{\mu\nu}=0$，所以

$$E^i{}_i=g^{ij}R_{i0j0}=R_{00}=0 .$$

潮汐张量无迹 ⇒ 纯剪切（拉伸与压缩相抵）。而真空里 Riemann = Weyl，故

$$E_{ij}=R_{i0j0}=C_{i0j0}\quad(\text{真空}),$$

即**潮汐张量是 Weyl 的"电部分"**。这就是"Ricci 管体积、Weyl 管形状"的公式版：物质（Ricci）改变一小团 test particles 的体积，潮汐（Weyl）只改变形状。引力波是真空扰动，所以是纯 Weyl，它的两个偏振正是剪切的两种模式。$\square$

</details>

## 参考

- Wald《General Relativity》第 3.2–3.3 节（Riemann 的定义与对称性）、第 3.4 节（Bianchi 恒等式与 Einstein 张量）、附录 B（曲率约定）。
- Carroll《Spacetime and Geometry》第 3 章（曲率的坐标计算与测地偏离）。
- Misner, Thorne & Wheeler《Gravitation》第 11–13 章（潮汐力的几何图像）、第 25 章（Weyl 张量）。
- Poisson《A Relativist's Toolkit》第 1 章（测地偏离）、第 5 章（Killing 矢量与守恒量）。
- [理论力学书第 6 章](../../classical-mechanics/docs/06-noether-theorem.md)（Noether 定理的力学版，Killing 矢量是它的几何版）；第 2 章（联络）、第 5 章（Einstein 方程与 $G_{\mu\nu}$ 的唯一性）、第 6 章（Schwarzschild：真空曲率 = 纯 Weyl）、第 8 章（零超曲面的 Raychaudhuri 用到 $R_{ab}\ell^a\ell^b$）。
