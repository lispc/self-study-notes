# 哈密顿方程与 Poisson 括号：相空间、流与对易子的出生地

> 路线图位置：第 2 部分（哈密顿力学与几何化）· 第 9 章
> 前置知识：第 1 章（约束与广义坐标）；第 5 章（最小作用量原理与 Euler–Lagrange 方程）尚未写出，可先读 Landau《力学》§1–2 或 Goldstein 第 2 章；多元微积分与线性代数。
> 学习目标：会从拉氏量做 Legendre 变换得到哈密顿量与哈密顿方程；会把演化看成相空间里保体积的流；熟练计算 Poisson 括号并用它判断守恒量；能说清 $\{q,p\}=1$ 到 $[\hat q,\hat p]=i\hbar$ 的对应到底对应了什么、又在哪里含糊。

---

**单位约定**：本篇是经典力学，$\hbar$ 与 $c$ 保留；相对论性例子中显式写出 $c$，需要取 $c=1$ 时会在小节内注明。

## 1. 一句话总结

**Legendre 变换把二阶的 Euler–Lagrange 方程改写为相空间 $(q,p)$ 上的一阶方程——哈密顿方程；解曲线是保相体积的流（刘维尔定理）；Poisson 括号把"演化"与"守恒"统一为同一个括号运算，并在量子化时升格为对易子 $[\,\cdot\,,\cdot\,]=i\hbar\{\,\cdot\,,\cdot\,\}$。本篇是量子化与协变相空间两条线的共同入口。**

## 2. 从拉氏量到哈密顿量：Legendre 变换

### 2.1 动机：把二阶方程拆成一阶

Euler–Lagrange 方程对时间 $t$ 是二阶的，初始数据需要 $(q,\dot q)$ 两组。哈密顿的看法是：把 $\dot q$ 换成独立的动量 $p$，用两倍数量的状态变量换一阶方程。这不是单纯的改写——相空间、辛结构、守恒量的代数都在这一步显露出来。

### 2.2 定义

正则共轭动量与哈密顿量定义为

$$p_i \equiv \frac{\partial L}{\partial \dot q^i},\qquad H(q,p,t) \equiv p_i\,\dot q^i - L(q,\dot q,t),$$

其中右端的 $\dot q$ 要用 $p$ 反解出来。这一步可行的条件是 Hessian 矩阵

$$M_{ij} \equiv \frac{\partial^2 L}{\partial \dot q^i\,\partial \dot q^j}$$

可逆。**Hessian 退化时 $\dot q$ 不能全部由 $p$ 解出，相空间被切出约束面——这正是第 12 章约束系统的入口。**

### 2.3 例子：一维粒子

$L = \frac12 m\dot q^2 - V(q)$ 给出 $p = m\dot q$，于是

$$H = \frac{p^2}{2m} + V(q).$$

### 2.4 例子：相对论粒子

取 $L = -mc^2\sqrt{1-\dot q^2/c^2}$，则

$$p = \frac{\partial L}{\partial \dot q} = \frac{m\dot q}{\sqrt{1-\dot q^2/c^2}}.$$

反解速度：$p^2(1-\dot q^2/c^2) = m^2\dot q^2$，整理得

$$\dot q = \frac{pc}{\sqrt{p^2 + m^2c^2}},$$

代回 $H = p\dot q - L$ 得

$$H = \sqrt{p^2c^2 + m^2c^4}.$$

两点值得记住：能量对 $p$ **不是二次的**；小速度展开 $H \simeq mc^2 + p^2/2m$ 把静止能与非相对论动能拆得干干净净。

### 2.5 几何：Legendre 变换是凸共轭

对固定的 $q$，$H(p) = \sup_{\dot q}\,[\,p\dot q - L(\dot q)\,]$ 是 $L$ 的 Legendre–Fenchel 共轭（$L$ 对 $\dot q$ 凸时上确界由驻点取得，即 $p = \partial L/\partial\dot q$）。这解释了为什么 $H$ 与 $L$ 同量纲、为什么 $\partial H/\partial p = \dot q$ 是共轭关系的另一半。

## 3. 哈密顿方程

### 3.1 推导

把 $H = p\dot q - L$ 全微分，用 $p = \partial L/\partial\dot q$ 消去 $\dot q$ 的微分：

$$\mathrm{d}H = \dot q\,\mathrm{d}p + p\,\mathrm{d}\dot q - \frac{\partial L}{\partial q}\mathrm{d}q - \frac{\partial L}{\partial \dot q}\mathrm{d}\dot q - \frac{\partial L}{\partial t}\mathrm{d}t.$$

中间两项 $p\,\mathrm{d}\dot q$ 与 $-\frac{\partial L}{\partial\dot q}\mathrm{d}\dot q$ 相消；再用 Euler–Lagrange 方程 $\partial L/\partial q = \mathrm{d}p/\mathrm{d}t$，得

$$\mathrm{d}H = \dot q\,\mathrm{d}p - \dot p\,\mathrm{d}q - \frac{\partial L}{\partial t}\mathrm{d}t.$$

与 $\mathrm{d}H = \frac{\partial H}{\partial q}\mathrm{d}q + \frac{\partial H}{\partial p}\mathrm{d}p + \frac{\partial H}{\partial t}\mathrm{d}t$ 逐项比较：

$$\boxed{\;\dot q^i = \frac{\partial H}{\partial p_i},\qquad \dot p_i = -\frac{\partial H}{\partial q^i},\qquad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t}.\;}$$

### 3.2 能量守恒

若 $L$ 不显含 $t$，则 $H$ 不显含 $t$，于是

$$\frac{\mathrm{d}H}{\mathrm{d}t} = \frac{\partial H}{\partial q^i}\dot q^i + \frac{\partial H}{\partial p_i}\dot p_i = \frac{\partial H}{\partial q^i}\frac{\partial H}{\partial p_i} - \frac{\partial H}{\partial p_i}\frac{\partial H}{\partial q^i} = 0.$$

$H$ 就是能量，也是时间平移对称性的 Noether 荷（第 6 章）。

### 3.3 矩阵形式：辛矩阵登场

把 $2n$ 个坐标堆成 $z = (q^1,\dots,q^n,p_1,\dots,p_n)^T$，哈密顿方程就是

$$\dot z = J\,\nabla H,\qquad J = \begin{pmatrix} 0 & \mathbb 1 \\ -\mathbb 1 & 0\end{pmatrix},$$

其中 $J$ 由 $n\times n$ 的零块与单位块拼成。$J$ 满足三个恒等式：

$$J^2 = -\mathbb 1,\qquad J^T = -J,\qquad \det J = 1.$$

这个 $J$ 是第 10 章的主角：它就是辛形式 $\omega = \mathrm{d}p_i\wedge\mathrm{d}q^i$ 的矩阵，哈密顿方程是"用辛形式把 $\mathrm{d}H$ 变成一个矢量场"。

### 3.4 相图

- **谐振子**：$H = \frac{p^2}{2m} + \frac12 m\omega^2 q^2$ 的等能线是椭圆，轨道绕原点匀速旋转（频率 $\omega$）。
- **单摆**：$H = \frac{p^2}{2ml^2} - mgl\cos\theta$。等能线在 $|E| \lt mgl$ 时是闭合的振动轨道，$E = mgl$ 处是**分离线**（separatrix），$E \gt mgl$ 时是贯穿的转动轨道。相图让"定性行为随参数突变"一眼可见。

## 4. 刘维尔定理：流保体积

### 4.1 流的散度为零

相空间中的"速度场"是 $(\dot q,\dot p) = (\partial H/\partial p,\,-\partial H/\partial q)$。它的散度

$$\nabla\cdot\dot z = \sum_i\left[\frac{\partial}{\partial q^i}\left(\frac{\partial H}{\partial p_i}\right) + \frac{\partial}{\partial p_i}\left(-\frac{\partial H}{\partial q^i}\right)\right] = 0.$$

所以哈密顿流是 $2n$ 维空间里的**不可压缩流**：像理想流体，但流体是"相空间中的概率"。

### 4.2 体积守恒

任意区域 $\Omega_t$ 随流演化，其体积变化率为 $\int_{\Omega_t}\nabla\cdot\dot z = 0$，故

$$\frac{\mathrm{d}}{\mathrm{d}t}\,\mathrm{Vol}(\Omega_t) = 0.$$

谐振子是最好看的例子：一个圆盘在流下被拉成椭圆、再转回来，形状一直在变，面积始终不变。

### 4.3 概率密度与刘维尔方程

设相空间概率密度为 $\rho(q,p,t)$，连续性方程 $\partial_t\rho + \nabla\cdot(\rho\,\dot z) = 0$ 展开为

$$\partial_t\rho + \dot z\cdot\nabla\rho + \rho\,\nabla\cdot\dot z = 0 \;\Longrightarrow\; \frac{\mathrm{d}\rho}{\mathrm{d}t} = 0,$$

即

$$\partial_t\rho = -\{\rho,H\} = \{H,\rho\}.$$

这就是**刘维尔方程**：沿轨道看，$\rho$ 是常数（"随波逐流不掉队"）。任何只依赖能量的分布 $\rho = f(H)$ 都是定态解——这正是统计力学取微正则/正则系综的依据（热统书第 6、7 章，待写）。

## 5. Poisson 括号

### 5.1 定义

对相空间上的两个函数 $f(q,p)$、$g(q,p)$，

$$\{f,g\} \equiv \sum_{i=1}^{n}\left(\frac{\partial f}{\partial q^i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q^i}\right).$$

### 5.2 代数性质

- **双线性**：对每个槽线性；
- **反对称**：$\{f,g\} = -\{g,f\}$，特别地 $\{f,f\} = 0$；
- **Leibniz 法则**：$\{f,gh\} = \{f,g\}h + g\{f,h\}$；
- **Jacobi 恒等式**：$\{f,\{g,h\}\} + \{g,\{h,f\}\} + \{h,\{f,g\}\} = 0$；
- **基本括号**：$\{q^i,q^j\} = 0$，$\{p_i,p_j\} = 0$，$\{q^i,p_j\} = \delta^i_{\ j}$。

性质决定的代数结构叫**泊松代数**；它比"相空间是 $\mathbb R^{2n}$"更本质——量子化只需要这套代数（自检 3 给出 Jacobi 的几何证明）。

### 5.3 演化与守恒量

对任意 $f(q,p,t)$，沿轨道求导：

$$\frac{\mathrm{d}f}{\mathrm{d}t} = \frac{\partial f}{\partial q^i}\dot q^i + \frac{\partial f}{\partial p_i}\dot p_i + \frac{\partial f}{\partial t} = \{f,H\} + \frac{\partial f}{\partial t}.$$

所以**不显含时间的量守恒，当且仅当它与 $H$ 的括号为零**：$\{f,H\} = 0$。这把"找守恒量"变成了"算一个括号"。

### 5.4 几何形式

把梯度堆成列矢量，括号就是

$$\{f,g\} = (\nabla f)^T J\,(\nabla g).$$

于是 $J$ 可以理解为"括号的核"：第 10 章会看到，$J$ 是辛形式 $\omega$ 的逆矩阵，$\{f,g\} = \omega(X_f,X_g)$。

### 5.5 例子：角动量代数

设 $\mathbf L = \mathbf q\times\mathbf p$，即 $L_i = \varepsilon_{ijk}q_j p_k$。直接计算给出

$$\{L_i,L_j\} = \varepsilon_{ijk}L_k.$$

（推导见自检 2。）这个结果值得停在原地看一眼：三维转动群的李代数 $\mathfrak{so}(3)$ 从二维相空间的括号里"长"了出来。量子化后它就是 $[\hat L_i,\hat L_j] = i\hbar\varepsilon_{ijk}\hat L_k$——角动量理论的全部代数结构，在经典力学里已经完整存在。

### 5.6 括号与矢量场

定义 $f$ 生成的哈密顿矢量场 $X_f$ 为"用 $f$ 去括号"：

$$X_f(g) \equiv \{f,g\}.$$

用 §3.3 的 $J$，可写成 $X_f = -J\nabla f$。可以证明（自检 3）

$$[X_f,X_g] = X_{\{f,g\}},$$

即**括号的 Jacobi 恒等式等价于矢量场的李括号封闭性**。这是"泊松代数 = 辛几何的代数影子"的精确表述。

## 6. 正则量子化：从括号到对易子

### 6.1 Dirac 的处方

把经典括号替换为对易子：

$$\{\,\cdot\,,\,\cdot\,\} \;\longrightarrow\; \frac{1}{i\hbar}[\,\cdot\,,\,\cdot\,].$$

基本括号立刻给出正则对易关系：

$$\{q^i,p_j\} = \delta^i_{\ j} \;\Longrightarrow\; [\hat q^i,\hat p_j] = i\hbar\,\delta^i_{\ j}.$$

这正是 QFT 书里 $[\hat\phi(\mathbf x),\hat\pi(\mathbf y)] = i\delta^3(\mathbf x-\mathbf y)$ 的量子力学原型——场论的正则量子化就是把这套处方逐字搬到无穷多个自由度（QFT 书第 4 阶段 01 篇）。

### 6.2 处方在哪里含糊：排序问题

括号只用到一阶导数，算符乘法却涉及次序。以 $f = q^2$、$g = p^2$ 为例：

$$\{q^2,p^2\} = 4qp.$$

量子化右边时，$4qp$ 该写成 $4\hat q\hat p$、$4\hat p\hat q$，还是 $2(\hat q\hat p+\hat p\hat q)$？三者相差 $O(\hbar)$。直接算对易子：

$$[\hat q^2,\hat p^2] = \hat q[\hat q,\hat p^2] + [\hat q,\hat p^2]\hat q = 2i\hbar(\hat q\hat p + \hat p\hat q),$$

而 $i\hbar\{q^2,p^2\} = 4i\hbar\,qp$。两者只有在把 $qp$ 理解为对称化 $\frac12(\hat q\hat p+\hat p\hat q)$ 时才一致。**所以"$[\,,\,]=i\hbar\{\,,\,\}$"必须附带一个排序约定；对称排序（Weyl 排序）是最自然的选择，它对应相空间路径积分的中点处方**（量子力学书 03s2，QFT 书第 4 阶段补充材料）。

### 6.3 角动量：没有排序问题

角动量的括号代数在量子化后逐字成立：

$$\{L_i,L_j\} = \varepsilon_{ijk}L_k \;\Longrightarrow\; [\hat L_i,\hat L_j] = i\hbar\,\varepsilon_{ijk}\hat L_k,$$

因为 $L_i$ 对 $q,p$ 是二次型，且代数在李括号下封闭，任何对称排序都给同一结果。这就是角动量理论"代数定一切"的经典根源（量子力学书第 05 篇）。

### 6.4 守恒量与对称性

$\{f,H\} = 0 \Rightarrow [\hat f,\hat H] = 0$（差 $O(\hbar)$ 的排序项）；Noether 荷在 Poisson 括号下构成李代数——整体对称性的荷代数（QFT 书第 5 阶段 02 篇）在经典层面就已经定型。

## 7. 与后面章节及 QFT 的接口

- **第 10 章**：括号的几何化——辛形式、正则变换、Darboux 定理；
- **第 12 章**：Hessian 退化 $\Rightarrow$ 约束、第一类/第二类、Dirac 括号；
- **QFT 书第 4 阶段 01 篇**：场的正则量子化就是本章逐字搬到无穷自由度；
- **QFT 书第 9 阶段 04 篇**：协变相空间把"辛形式"从 $(q,p)$ 搬到解空间，得到零锥上的 Poisson 括号；
- **量子力学书 03s2**：Weyl 排序与相空间量子力学。

## 小结

- Legendre 变换 $H = p\dot q - L$ 把二阶 EL 方程改写为一阶哈密顿方程；Hessian 可逆是前提，退化则是第 12 章的约束系统。
- 哈密顿流 $\dot z = J\nabla H$ 的散度为零（刘维尔定理），相体积守恒；概率密度满足刘维尔方程 $\partial_t\rho = \{H,\rho\}$，$\rho = f(H)$ 是定态。
- Poisson 括号是反对称、Leibniz、满足 Jacobi 的双线性运算；$\{q^i,p_j\}=\delta^i_{\ j}$ 定全部；$\mathrm{d}f/\mathrm{d}t = \{f,H\} + \partial_t f$，守恒量 $\Leftrightarrow$ 与 $H$ 括号为零。
- 括号的几何形式是 $\{f,g\} = (\nabla f)^T J\nabla g$；Jacobi 恒等式等价于哈密顿矢量场的李括号封闭 $[X_f,X_g] = X_{\{f,g\}}$。
- 量子化处方 $\{\,,\,\}\to [\,,\,]/i\hbar$ 在二次型（角动量）上干净，在 $q^2p^2$ 一类量上有排序歧义；Weyl 对称排序是自然选择，对应相空间路径积分的中点处方。

## 自检问题

**1.** 相对论粒子 $L = -mc^2\sqrt{1-\dot q^2/c^2}$：求 $p(\dot q)$ 与 $H(q,p)$，验证 $\partial H/\partial p = \dot q$，并取非相对论极限。

<details markdown="1"><summary>点击显示答案</summary>

求导：

$$p = \frac{\partial L}{\partial \dot q} = -mc^2\cdot\frac12\left(1-\frac{\dot q^2}{c^2}\right)^{-1/2}\cdot\left(-\frac{2\dot q}{c^2}\right) = \frac{m\dot q}{\sqrt{1-\dot q^2/c^2}}.$$

平方后解 $\dot q$：

$$p^2\left(1-\frac{\dot q^2}{c^2}\right) = m^2\dot q^2 \;\Longrightarrow\; p^2 = \dot q^2\left(m^2 + \frac{p^2}{c^2}\right) \;\Longrightarrow\; \dot q = \frac{pc}{\sqrt{p^2+m^2c^2}}.$$

哈密顿量：

$$H = p\dot q - L = \frac{p^2c}{\sqrt{p^2+m^2c^2}} + mc^2\sqrt{1-\frac{\dot q^2}{c^2}}.$$

用 $1-\dot q^2/c^2 = m^2c^2/(p^2+m^2c^2)$，第二项为 $m^2c^3/\sqrt{p^2+m^2c^2}$，两项合并：

$$H = \frac{c(p^2+m^2c^2)}{\sqrt{p^2+m^2c^2}} = \sqrt{p^2c^2 + m^2c^4}.$$

验证：

$$\frac{\partial H}{\partial p} = \frac{pc^2}{\sqrt{p^2c^2+m^2c^4}} = \frac{pc}{\sqrt{p^2+m^2c^2}} = \dot q.$$

非相对论极限：$\sqrt{p^2c^2+m^2c^4} = mc^2\sqrt{1+\frac{p^2}{m^2c^2}} \simeq mc^2 + \frac{p^2}{2m}$——静止能加动能，符号与量纲都对。

</details>

**2.** 证明 $\{L_i,L_j\} = \varepsilon_{ijk}L_k$（$L_i = \varepsilon_{ijk}q_j p_k$）。

<details markdown="1"><summary>点击显示答案</summary>

先用括号的基本性质证明两个引理：对 $L_i$ 与坐标、动量的括号有转动形式

$$\{L_i,q_j\} = \varepsilon_{ijk}q_k,\qquad \{L_i,p_j\} = \varepsilon_{ijk}p_k.$$

以第一个为例：$L_i = \varepsilon_{iab}q_a p_b$，于是

$$\{L_i,q_j\} = \varepsilon_{iab}\left(\{q_a,q_j\}p_b + q_a\{p_b,q_j\}\right) = \varepsilon_{iab}q_a(-\delta_{bj}) = -\varepsilon_{iaj}q_a = \varepsilon_{ija}q_a = \varepsilon_{ijk}q_k.$$

第二个同理（$\{q_a,p_j\} = \delta_{aj}$，得 $\varepsilon_{iab}\delta_{aj}p_b = \varepsilon_{ijb}p_b$）。

现在用 Leibniz 法则，并用两个引理把结果拆成两项：

$$\{L_i,L_j\} = \varepsilon_{jcd}\left(\{L_i,q_c\}p_d + q_c\{L_i,p_d\}\right) = \varepsilon_{jcd}\,\varepsilon_{ick}\,q_kp_d + \varepsilon_{jcd}\,\varepsilon_{idk}\,q_cp_k \equiv T_A + T_B.$$

计算 $T_A$：把两个 $\varepsilon$ 的共享指标 $c$ 挪到首位——$\varepsilon_{jcd} = \varepsilon_{cdj}$，$\varepsilon_{ick} = \varepsilon_{cki}$——再套标准恒等式 $\varepsilon_{cab}\varepsilon_{cde} = \delta_{ad}\delta_{be} - \delta_{ae}\delta_{bd}$，得

$$T_A = (\delta_{dk}\delta_{ji} - \delta_{di}\delta_{jk})\,q_kp_d = \delta_{ij}\,(q\cdot p) - q_jp_i.$$

计算 $T_B$：把共享指标 $d$ 挪到首位并注意反号——$\varepsilon_{jcd} = -\varepsilon_{dcj}$，$\varepsilon_{idk} = \varepsilon_{dki}$——同样套恒等式：

$$T_B = -(\delta_{ck}\delta_{ji} - \delta_{ci}\delta_{jk})\,q_cp_k = -\delta_{ij}\,(q\cdot p) + q_ip_j.$$

相加，$\delta_{ij}(q\cdot p)$ 两项相消：

$$\{L_i,L_j\} = q_ip_j - q_jp_i.$$

最后一步：把 $\varepsilon$ 的乘积展开，$\varepsilon_{ijk}\varepsilon_{kab} = \delta_{ia}\delta_{jb} - \delta_{ib}\delta_{ja}$，于是

$$\varepsilon_{ijk}L_k = \varepsilon_{ijk}\varepsilon_{kab}\,q_ap_b = q_ip_j - q_jp_i,$$

即 $\{L_i,L_j\} = \varepsilon_{ijk}L_k$。$\square$

（两个恒等式的用法是这类计算的通用套路：先把两个 $\varepsilon$ 的共享指标挪到同一位置，再套 $\varepsilon_{cab}\varepsilon_{cde} = \delta_{ad}\delta_{be} - \delta_{ae}\delta_{bd}$；挪动时每交换两个指标出一个负号，这一步最易出错。）

</details>

**3.** 证明 Poisson 括号的 Jacobi 恒等式：定义 $X_f(g) = \{f,g\}$，证明 $[X_f,X_g] = X_{\{f,g\}}$，并由此推出 Jacobi 恒等式。

<details markdown="1"><summary>点击显示答案</summary>

把 $X_f$ 写成分量：由 $\{f,g\} = (\nabla f)^TJ\nabla g$ 与 $J^T = -J$，有

$$X_f(g) = \{f,g\} = -(\nabla f)^T J\nabla g = (-J\nabla f)\cdot\nabla g \;\Longrightarrow\; X_f = -J\nabla f.$$

计算两个矢量场的李括号。记 $J$ 为常数矩阵，$(X_f)_k = -J_{ki}\partial_i f$：

$$[X_f,X_g]_k = (X_f)_j\partial_j(X_g)_k - (X_g)_j\partial_j(X_f)_k = J_{ji}\partial_i f\, J_{kl}\partial_j\partial_l g - J_{ji}\partial_i g\, J_{kl}\partial_j\partial_l f.$$

（负号两两抵消。）第一项中交换 $i\leftrightarrow j$ 并利用 $J_{ji} = -J_{ij}$：

$$J_{ji}J_{kl}\partial_i f\,\partial_j\partial_l g = -J_{ij}J_{kl}\partial_j f\,\partial_i\partial_l g.$$

另一方面，

$$X_{\{f,g\}} = -J\nabla\{f,g\},\qquad \{f,g\} = J_{ab}\partial_a f\,\partial_b g,$$

其第 $k$ 分量为

$$(X_{\{f,g\}})_k = -J_{kl}\partial_l\left(J_{ab}\partial_a f\,\partial_b g\right) = -J_{kl}J_{ab}\left(\partial_l\partial_a f\,\partial_b g + \partial_a f\,\partial_l\partial_b g\right).$$

把两个表达式逐项对比：第一项 $(-J_{kl}J_{ab}\partial_l\partial_a f\,\partial_b g)$ 与 $[X_f,X_g]_k$ 中含 $\partial g\,\partial^2 f$ 的项相同（重命名指标即见）；第二项 $(-J_{kl}J_{ab}\partial_a f\,\partial_l\partial_b g)$ 与含 $\partial f\,\partial^2 g$ 的项相同（再用 $J_{ab}=-J_{ba}$ 与 $i\leftrightarrow j$ 重排）。两项都吻合，故

$$[X_f,X_g] = X_{\{f,g\}}.$$

现在取它作用在 $h$ 上：

$$\{ \{f,g\}, h\} = X_{\{f,g\}}(h) = [X_f,X_g](h) = X_f(X_g h) - X_g(X_f h) = \{f,\{g,h\}\} - \{g,\{f,h\}\}.$$

利用反对称性把第一项写成 $-\{h,\{f,g\}\}$，移项即得

$$\{f,\{g,h\}\} + \{g,\{h,f\}\} + \{h,\{f,g\}\} = 0.\qquad\square$$

这个证明的要点：**Jacobi 恒等式不是一条独立的代数公理，而是"括号来自辛结构"的必然结果**——矢量场的李括号自动满足 Jacobi，而 $[X_f,X_g] = X_{\{f,g\}}$ 把它翻译成了括号语言。

</details>

**4.** 刘维尔定理：证明哈密顿流散度为零、相体积守恒，并证明任何 $\rho = f(H)$ 都是定态分布。

<details markdown="1"><summary>点击显示答案</summary>

散度：

$$\nabla\cdot\dot z = \frac{\partial \dot q^i}{\partial q^i} + \frac{\partial \dot p_i}{\partial p_i} = \frac{\partial^2 H}{\partial q^i\partial p_i} - \frac{\partial^2 H}{\partial p_i\partial q^i} = 0$$

（偏导可交换）。于是对任意区域 $\Omega_t$ 随流演化，

$$\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t}\mathrm{d}^{2n}z = \int_{\Omega_t}\nabla\cdot\dot z\;\mathrm{d}^{2n}z = 0.$$

概率密度：连续性方程 $\partial_t\rho + \partial_i(\rho\dot z^i) = 0$，展开并用散度为零：

$$\partial_t\rho + \dot z\cdot\nabla\rho = 0 \;\Longrightarrow\; \partial_t\rho = -\{\rho,H\}.$$

定态分布：若 $\rho = f(H)$，则

$$\partial_t\rho = -\{f(H),H\} = -f'(H)\{H,H\} = 0,$$

因为 $\{H,H\} = 0$（反对称性）。所以任何只依赖能量的分布都自动满足刘维尔方程——这正是微正则（$f$ 为 $\delta$ 函数）与正则（$f$ 为指数）系综作为定态的依据。

</details>

**5.** 带电粒子：取 $c=1$、高斯制，$H = \frac{(\mathbf p - e\mathbf A)^2}{2m} + e\varphi$。从哈密顿方程推出 $m\ddot{\mathbf q} = e(\mathbf E + \dot{\mathbf q}\times\mathbf B)$。

<details markdown="1"><summary>点击显示答案</summary>

哈密顿方程：

$$\dot q_i = \frac{\partial H}{\partial p_i} = \frac{p_i - eA_i}{m},\qquad \dot p_i = -\frac{\partial H}{\partial q_i} = \frac{e}{m}(p_j - eA_j)\partial_i A_j - e\,\partial_i\varphi.$$

用第一式把 $p_j - eA_j = m\dot q_j$ 代入第二式：

$$\dot p_i = e\,\dot q_j\,\partial_i A_j - e\,\partial_i\varphi.$$

另一方面，$p_i = m\dot q_i + eA_i$，所以

$$m\ddot q_i = \dot p_i - e\frac{\mathrm{d}A_i}{\mathrm{d}t} = \dot p_i - e\left(\partial_t A_i + \dot q_j\partial_j A_i\right).$$

合并：

$$m\ddot q_i = e\,\dot q_j\left(\partial_i A_j - \partial_j A_i\right) - e\left(\partial_i\varphi + \partial_t A_i\right).$$

认出电场 $\mathbf E = -\nabla\varphi - \partial_t\mathbf A$ 与磁场 $\mathbf B = \nabla\times\mathbf A$，并用矢量恒等式

$$\left[\dot{\mathbf q}\times(\nabla\times\mathbf A)\right]_i = \varepsilon_{ijk}\dot q_j\varepsilon_{klm}\partial_lA_m = \dot q_j\partial_iA_j - \dot q_j\partial_jA_i,$$

即得

$$m\ddot{\mathbf q} = e\left(\mathbf E + \dot{\mathbf q}\times\mathbf B\right).\qquad\square$$

这个练习说明：**最小耦合 $p\to p-eA$ 的全部内容就是哈密顿方程加一点指标代数**——经典电动力学与哈密顿力学的接口在 QFT 书里会再次出现（协变导数 $D_\mu = \partial_\mu + ieA_\mu$ 是同一件事的量子版）。

</details>

## 参考

- Landau & Lifshitz《力学》§40（哈密顿方程）、§42（Poisson 括号）；第七章其余各节（正则变换、刘维尔定理）。
- Goldstein《Classical Mechanics》第 8 章（哈密顿方程）、第 9 章（正则变换与括号）。
- Arnold《经典力学的数学方法》第 2–3 章（相空间与辛流形的几何观点）。
- 第 10、12 章（本仓库）：辛结构与约束系统的续篇；量子化接口见量子力学书第 03 篇与 QFT 书第 4 阶段 01 篇。
