# 对称性与守恒律：Noether 定理

> 路线图位置：第 1 部分（拉格朗日力学：对称性第一性原理）· 第 6 章
> 前置知识：第 5 章（最小作用量原理、Euler–Lagrange 方程）；第 9 章可先跳过（守恒量的括号代数会在第 9 章讲，本篇只用到定义）。
> 学习目标：会陈述并证明 Noether 定理（力学版）：连续对称性 ⇒ 守恒流；能从时间平移、空间平移、转动分别导出能量、动量、角动量；理解"对称性只要求拉氏量差一个全导数"的含义；会写场论版的 Noether 流与能动张量，并知道它向 QFT 的对接点（U(1) 电荷、Ward 恒等式）。

---

**单位约定**：本篇保留通常单位；场论部分取 $c=1$（第 5 节首次说明）。

## 1. 一句话总结

**每一个连续对称性对应一个守恒量：时间平移 → 能量，空间平移 → 动量，转动 → 角动量，内部相位 → 电荷。Noether 定理的推导只有一行——把"拉氏量在变换下只变全导数"与 Euler–Lagrange 方程合起来，全导数恰好抵消，剩下的就是一个守恒流。这是整个 QFT 的对称性母机：标准模型的每一条守恒律、每一个 Ward 恒等式、每一个流代数，都是同一条定理的场论版本。**

## 2. 对称性的语言

### 2.1 连续变换

考虑单参数连续变换

$$q^i \;\longrightarrow\; q^i + \varepsilon\,\delta q^i(q,t),$$

$\varepsilon$ 是小参数，$\delta q^i$ 是变换的"方向"（可以是坐标的函数，但不含速度）。例子：

- 时间平移：$t\to t+\varepsilon$，$\delta q^i = \dot q^i$；
- 空间平移：$\mathbf q\to\mathbf q + \varepsilon\mathbf a$，$\delta q^i = a^i$；
- 转动：$\mathbf q\to\mathbf q + \varepsilon\,\hat{\mathbf n}\times\mathbf q$，$\delta\mathbf q = \hat{\mathbf n}\times\mathbf q$。

### 2.2 "对称"的确切含义

拉氏量在变换下**不必严格不变**，只要求差一个全导数：

$$\delta L = \varepsilon\,\frac{\mathrm{d}K}{\mathrm{d}t},$$

$K(q,t)$ 是某个函数。原因是全导数不改变作用量的变分（第 5 章 §6），所以运动方程不受影响。这个"最多差全导数"的宽松定义正是 Noether 定理能覆盖时间平移的关键（那里 $K = L$）。

### 2.3 例：时间平移的 $K$

$q(t+\varepsilon)\approx q(t) + \varepsilon\dot q$，所以

$$\delta L = \varepsilon\left(\frac{\partial L}{\partial q^i}\dot q^i + \frac{\partial L}{\partial \dot q^i}\ddot q^i\right) + \varepsilon\frac{\partial L}{\partial t} = \varepsilon\frac{\mathrm{d}L}{\mathrm{d}t} - \varepsilon\frac{\partial L}{\partial t}.$$

若 $L$ 不显含 $t$，则 $\delta L = \varepsilon\,\mathrm{d}L/\mathrm{d}t$，即 $K = L$。

## 3. Noether 定理（力学版）

### 3.1 推导

把 $\delta L$ 按链式法则写开：

$$\delta L = \varepsilon\left[\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial \dot q^i}\frac{\mathrm{d}}{\mathrm{d}t}\delta q^i\right] = \varepsilon\frac{\mathrm{d}K}{\mathrm{d}t}.$$

在**真实轨道**上，Euler–Lagrange 方程给出 $\partial L/\partial q^i = \mathrm{d}p_i/\mathrm{d}t$，$p_i = \partial L/\partial\dot q^i$。代入第一项：

$$\frac{\mathrm{d}p_i}{\mathrm{d}t}\delta q^i + p_i\frac{\mathrm{d}}{\mathrm{d}t}\delta q^i = \frac{\mathrm{d}}{\mathrm{d}t}\left(p_i\,\delta q^i\right) = \frac{\mathrm{d}K}{\mathrm{d}t}.$$

整理即得

$$\boxed{\;\frac{\mathrm{d}}{\mathrm{d}t}\left[p_i\,\delta q^i - K\right] = 0.\;}$$

**Noether 荷**：

$$Q \equiv p_i\,\delta q^i - K$$

在真实轨道上守恒。这就是 Noether 定理的全部内容——**没有第二条方程，也没有额外假设**。

### 3.2 三个基本例子

- **时间平移**（$\delta q^i = \dot q^i$，$K = L$）：
  $$Q = p_i\dot q^i - L = H.$$
  能量守恒，条件是 $L$ 不显含 $t$。
- **空间平移**（$\delta q^i = a^i$，$K = 0$，$L$ 不显含 $q$）：
  $$Q = p_i a^i \;\Longrightarrow\; \mathbf P = \mathbf p.$$
  动量守恒，条件是 $L$ 不显含该方向坐标（空间的均匀性）。
- **转动**（$\delta\mathbf q = \hat{\mathbf n}\times\mathbf q$，$K = 0$）：
  $$Q = \mathbf p\cdot(\hat{\mathbf n}\times\mathbf q) = \hat{\mathbf n}\cdot(\mathbf q\times\mathbf p) = \hat{\mathbf n}\cdot\mathbf L.$$
  角动量守恒，条件是 $L$ 各向同性。

三者的共同点：**守恒量 = 正则动量 × 对称变换的方向**（再减 $K$）。这个结构在量子力学里原样保留：守恒量是"生成对称变换的算符"（第 9 章的 $Q$ 与 $\{Q,\cdot\}$）。

### 3.3 一个内部对称的例子

取复坐标 $q$（两个实自由度），$L = |\dot q|^2 - V(|q|^2)$。相位变换 $q\to e^{\mathrm{i}\alpha}q$，小参数 $\delta q = \mathrm{i}q$、$\delta q^* = -\mathrm{i}q^*$。$L$ 严格不变（$K = 0$），故

$$Q = p\,\delta q + p^*\delta q^* = \mathrm{i}\left(p q - p^* q^*\right)$$

守恒。这在量子化后就是"粒子数（电荷）守恒"的经典原型（第 5 节的场论版本给出 $Q = N_a - N_b$）。

## 4. 守恒量的代数

### 4.1 括号封闭

守恒量的 Poisson 括号一般还是守恒量：若 $\{Q_a,H\} = 0$、$\{Q_b,H\} = 0$，则由 Jacobi 恒等式

$$\{H,\{Q_a,Q_b\}\} = -\{Q_a,\{Q_b,H\}\} - \{Q_b,\{H,Q_a\}\} = 0.$$

于是守恒量构成一个**李代数**（在括号下封闭）。这个代数是量子化后算符代数的经典前身：$\{Q_a,Q_b\} = f_{ab}^{\ \ c}Q_c \Rightarrow [\hat Q_a,\hat Q_b] = \mathrm{i}\hbar f_{ab}^{\ \ c}\hat Q_c$（第 9 章）。

### 4.2 角动量代数

以 $\mathbf L = \mathbf q\times\mathbf p$ 为例，第 9 章已算出

$$\{L_i,L_j\} = \varepsilon_{ijk}L_k.$$

这不是巧合：**角动量守恒量的代数结构 = 转动群的李代数 $\mathfrak{so}(3)$**。量子化后就是 $[\hat L_i,\hat L_j] = \mathrm{i}\hbar\varepsilon_{ijk}\hat L_k$——角动量理论（量子力学书第 05 篇）的全部代数内容在经典力学里已经完整存在。

### 4.3 对称性与简并

守恒量带来简并：若 $[H,Q] = 0$（量子）或 $\{H,Q\}=0$（经典），则 $Q$ 的不同的本征值给出不同的"扇区"，而同一本征值内的态能量相同。氢原子的 $2n^2$ 重简并来自隐藏的 SO(4) 对称性（Runge–Lenz 矢量，第 2 章；量子力学书 06s 篇）——这是"对称性 ⇒ 简并"的最著名例子。

## 5. 场论版本

### 5.1 Noether 流

场论里对称变换是 $\varphi_a(x)\to\varphi_a(x) + \varepsilon\,\delta\varphi_a(x)$，拉氏密度满足

$$\delta\mathcal L = \varepsilon\,\partial_\mu K^\mu.$$

同样的推导给出**Noether 流**：

$$j^\mu \equiv \frac{\partial\mathcal L}{\partial(\partial_\mu\varphi_a)}\,\delta\varphi_a - K^\mu,\qquad \partial_\mu j^\mu = 0\quad(\text{在壳}).$$

守恒荷 $Q = \int\mathrm{d}^3x\,j^0$。与力学版的对应：$p_i\to\partial\mathcal L/\partial(\partial_0\varphi_a)$，$K\to K^0$。

### 5.2 能动张量

对时空平移 $\delta\varphi_a = \partial^\nu\varphi_a$（$K^\mu$ 相应地取），得到

$$T^{\mu\nu} = \frac{\partial\mathcal L}{\partial(\partial_\mu\varphi_a)}\,\partial^\nu\varphi_a - \eta^{\mu\nu}\mathcal L,\qquad \partial_\mu T^{\mu\nu} = 0.$$

$T^{00}$ 是能量密度，$T^{0i}$ 是动量密度。**规范场的 $T^{\mu\nu}$ 一般不对称**，可以加一个散度型改进项使其对称——**Belinfante 改进**。对称化的 $T^{\mu\nu}$ 正是广义相对论里引力的源（QFT 书第 3 阶段 02 篇）。

### 5.3 内部对称：U(1) 电荷

复标量场 $\mathcal L = \partial_\mu\varphi^*\partial^\mu\varphi - m^2\varphi^*\varphi$，相位变换 $\delta\varphi = \mathrm{i}\varphi$、$\delta\varphi^* = -\mathrm{i}\varphi^*$：

$$j^\mu = \mathrm{i}\left(\varphi^*\partial^\mu\varphi - \varphi\,\partial^\mu\varphi^*\right),\qquad \partial_\mu j^\mu = 0.$$

量子化后 $Q = \int j^0 = N_a - N_b$（QFT 书第 4 阶段 01 篇的自检）——**电荷 = 粒子数减反粒子数**。这是标准模型里所有内部量子数的原型。

## 6. 破缺与近似对称

### 6.1 显式破缺：Noether 恒等式

若变换不是严格对称，把同一套代数重做一遍（不对 $\delta L$ 作任何假设）：

$$\partial_\mu\left[\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi_a)}\delta\varphi_a\right] = \left[\frac{\partial\mathcal L}{\partial\varphi_a} - \partial_\mu\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi_a)}\right]\delta\varphi_a + \delta\mathcal L.$$

在壳（方括号为零）时

$$\partial_\mu j^\mu = \delta\mathcal L.$$

**流的散度 = 拉氏量在变换下的变化**：对称时为零（守恒），破缺时正比于破缺项。在 QFT 里这条恒等式放进关联函数就是 **Ward–Takahashi 恒等式**（QFT 书第 4 阶段 05 篇 §6.2），它保证可重整性、电荷普适性与反常的计算。

### 6.2 自发破缺

对称性可以"藏起来"：拉氏量严格对称，但真空（基态）不对称。此时 Noether 流仍守恒，但守恒荷的发现在无穷体积下失效，取而代之的是**Goldstone 玻色子**（QFT 书第 5 阶段 03 篇）。这是"对称性决定相互作用"的另一面：破缺的模式决定低能谱。

## 7. 小结

- 连续对称性（拉氏量差全导数）⇒ 守恒荷 $Q = p_i\delta q^i - K$；证明只用链式法则与 Euler–Lagrange 方程。
- 三个基本对应：时间平移 → 能量（$K = L$）、空间平移 → 动量、转动 → 角动量；内部相位 → 电荷。
- 守恒量在 Poisson 括号下封闭成李代数，量子化后成为算符代数：$\{Q_a,Q_b\} = f_{ab}^{\ \ c}Q_c \Rightarrow [\hat Q_a,\hat Q_b] = \mathrm{i}\hbar f_{ab}^{\ \ c}\hat Q_c$。
- 场论版：$j^\mu = \partial\mathcal L/\partial(\partial_\mu\varphi)\delta\varphi - K^\mu$；时空平移给出 $T^{\mu\nu}$（需 Belinfante 对称化）；U(1) 给出电荷 $N_a - N_b$。
- 破缺时 $\partial_\mu j^\mu = \delta\mathcal L$（Ward 恒等式）；自发破缺给 Goldstone 玻色子。

## 自检问题

**1.** 从 $\delta L = \varepsilon\,\mathrm{d}K/\mathrm{d}t$ 完整推出守恒荷 $Q = p_i\delta q^i - K$，并说明每一步用了什么。

<details markdown="1"><summary>点击显示答案</summary>

$$\delta L = \varepsilon\left[\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial\dot q^i}\frac{\mathrm{d}}{\mathrm{d}t}\delta q^i\right] = \varepsilon\frac{\mathrm{d}K}{\mathrm{d}t}.$$

除以 $\varepsilon$，在真实轨道上用 Euler–Lagrange 方程 $\partial L/\partial q^i = \mathrm{d}p_i/\mathrm{d}t$（$p_i = \partial L/\partial\dot q^i$）：

$$\frac{\mathrm{d}p_i}{\mathrm{d}t}\delta q^i + p_i\frac{\mathrm{d}}{\mathrm{d}t}\delta q^i = \frac{\mathrm{d}K}{\mathrm{d}t}.$$

左边是乘积的导数：$\frac{\mathrm{d}}{\mathrm{d}t}(p_i\delta q^i)$。于是

$$\frac{\mathrm{d}}{\mathrm{d}t}\left(p_i\delta q^i - K\right) = 0.\qquad\square$$

用到的三件事：链式法则（定义 $\delta L$）、Euler–Lagrange 方程（把 $\partial L/\partial q$ 换成 $\dot p$）、乘积法则（合并成全导数）。**没有用到 $\delta q$ 的具体形式**——所以定理对任意连续变换成立，只要 $\mathrm{d}K/\mathrm{d}t$ 存在。

</details>

**2.** 时间平移：取 $\delta q^i = \dot q^i$、$K = L$，导出能量守恒 $E = p_i\dot q^i - L$，并直接用 Euler–Lagrange 方程验证 $\mathrm{d}E/\mathrm{d}t = 0$（当 $\partial L/\partial t = 0$）。

<details markdown="1"><summary>点击显示答案</summary>

Noether 荷：

$$Q = p_i\dot q^i - L = H = E.$$

直接验证（不引用 Noether 定理）：$E = p_i\dot q^i - L$，

$$\frac{\mathrm{d}E}{\mathrm{d}t} = \dot p_i\dot q^i + p_i\ddot q^i - \frac{\partial L}{\partial q^i}\dot q^i - \frac{\partial L}{\partial\dot q^i}\ddot q^i - \frac{\partial L}{\partial t}.$$

用 $p_i = \partial L/\partial\dot q^i$，第二项与第四项相消；用 Euler–Lagrange $\dot p_i = \partial L/\partial q^i$，第一项与第三项相消：

$$\frac{\mathrm{d}E}{\mathrm{d}t} = -\frac{\partial L}{\partial t}.$$

故 $L$ 不显含 $t$ 时能量守恒。$\square$

注意：$H = p_i\dot q^i - L$ 是第 9 章的哈密顿量；这条自检说明"哈密顿量是时间平移的 Noether 荷"——不是定义，而是定理。

</details>

**3.** 转动：$\delta\mathbf q = \varepsilon\,\hat{\mathbf n}\times\mathbf q$，导出守恒量 $\hat{\mathbf n}\cdot\mathbf L$（$\mathbf L = \mathbf q\times\mathbf p$），并说明为什么这说明 $L$ 各向同性。

<details markdown="1"><summary>点击显示答案</summary>

$\delta\mathbf q = \hat{\mathbf n}\times\mathbf q$，$K = 0$（若 $L$ 各向同性），故

$$Q = \mathbf p\cdot(\hat{\mathbf n}\times\mathbf q) = \hat{\mathbf n}\cdot(\mathbf q\times\mathbf p) = \hat{\mathbf n}\cdot\mathbf L.$$

由于 $\hat{\mathbf n}$ 任意，三个分量 $L_x,L_y,L_z$ 都守恒。$\square$

"为什么说明 $L$ 各向同性"：若 $L$ 依赖某个特殊方向 $\mathbf m$（如 $L$ 含 $\mathbf m\cdot\mathbf q$ 项），则绕 $\mathbf m$ 的转动仍是 $L$ 的对称（$\mathbf m\cdot(\hat{\mathbf n}\times\mathbf q) = 0$ 当 $\hat{\mathbf n}\parallel\mathbf m$），但绕垂直于 $\mathbf m$ 的轴转动会改变 $L$，相应的 $L_\perp$ 不守恒。**守恒量的个数 = 对称群的维数**（这里是 3，对应 SO(3)）。

补充：一般中心力 $V(r)$ 下 $L$ 各向同性，故 $\mathbf L$ 守恒——第 2 章的中心力问题（Kepler）正是靠这一条把三维降到一维。$\square$

</details>

**4.** 场论：从 U(1) 相位变换导出 $j^\mu = \mathrm{i}(\varphi^*\partial^\mu\varphi - \varphi\partial^\mu\varphi^*)$ 与 $\partial_\mu j^\mu = 0$，并说明量子化后 $Q = N_a - N_b$。

<details markdown="1"><summary>点击显示答案</summary>

$$\mathcal L = \partial_\mu\varphi^*\partial^\mu\varphi - m^2\varphi^*\varphi,\qquad \delta\varphi = \mathrm{i}\varphi,\quad \delta\varphi^* = -\mathrm{i}\varphi^*.$$

因为 $\mathcal L$ 只依赖 $|\varphi|^2$ 与 $|\partial\varphi|^2$，相位变换严格不变（$K^\mu = 0$）。Noether 流：

$$j^\mu = \frac{\partial\mathcal L}{\partial(\partial_\mu\varphi)}\delta\varphi + \frac{\partial\mathcal L}{\partial(\partial_\mu\varphi^*)}\delta\varphi^* = \partial^\mu\varphi^*(\mathrm{i}\varphi) + \partial^\mu\varphi(-\mathrm{i}\varphi^*) = \mathrm{i}\left(\varphi^*\partial^\mu\varphi - \varphi\partial^\mu\varphi^*\right).$$

守恒：$\partial_\mu j^\mu = \mathrm{i}(\partial_\mu\varphi^*\partial^\mu\varphi + \varphi^*\Box\varphi - \partial_\mu\varphi\partial^\mu\varphi^* - \varphi\Box\varphi^*)$。第一、三项相消；用场方程 $\Box\varphi = -m^2\varphi$、$\Box\varphi^* = -m^2\varphi^*$，第二、四项相消。$\square$

量子化：$\varphi = \int\frac{\mathrm{d}^3p}{(2\pi)^3\sqrt{2\omega_p}}\left(a_{\mathbf p}e^{-\mathrm{i}px} + b_{\mathbf p}^\dagger e^{\mathrm{i}px}\right)$，$\varphi^\dagger$ 含 $a^\dagger,b$。代入 $Q = \int\mathrm{d}^3x\,j^0$，利用等时对易关系，交叉项相消、对角项给出

$$Q = \int\frac{\mathrm{d}^3p}{(2\pi)^3}\left(a_{\mathbf p}^\dagger a_{\mathbf p} - b_{\mathbf p}^\dagger b_{\mathbf p}\right) = N_a - N_b,$$

即"粒子数减反粒子数"（QFT 书第 4 阶段 01 篇 §7 的自检）。$\square$

要点：**经典 Noether 荷的"粒子数差"解释，是量子化后才显现的**；经典层面 $Q$ 只是 $\varphi,\dot\varphi$ 的一个双线性泛函。

</details>

**5.** 能动张量：从时空平移导出 $T^{\mu\nu} = \partial\mathcal L/\partial(\partial_\mu\varphi_a)\,\partial^\nu\varphi_a - \eta^{\mu\nu}\mathcal L$，验证 $\partial_\mu T^{\mu\nu} = 0$（在壳），并说明为什么需要 Belinfante 改进。

<details markdown="1"><summary>点击显示答案</summary>

时空平移 $\delta\varphi_a = \partial^\nu\varphi_a$（沿 $\nu$ 方向平移），$K^\mu = \delta^\mu{}_\nu\mathcal L$（拉氏密度随平移变 $\partial_\nu\mathcal L$）。于是

$$j^\mu = \frac{\partial\mathcal L}{\partial(\partial_\mu\varphi_a)}\partial^\nu\varphi_a - \delta^\mu{}_\nu\mathcal L \equiv T^{\mu\nu}.$$

守恒：$\partial_\mu T^{\mu\nu} = 0$ 在壳。

直接验证（以单标量场为例）：$T^{\mu\nu} = \partial^\mu\varphi\partial^\nu\varphi - \eta^{\mu\nu}\mathcal L$，

$$\partial_\mu T^{\mu\nu} = (\Box\varphi)\partial^\nu\varphi + \partial^\mu\varphi\partial_\mu\partial^\nu\varphi - \partial^\nu\mathcal L.$$

而 $\partial^\nu\mathcal L = \partial^\nu\left(\frac12\partial_\alpha\varphi\partial^\alpha\varphi - \frac12m^2\varphi^2\right) = \partial^\nu\partial_\alpha\varphi\,\partial^\alpha\varphi - m^2\varphi\partial^\nu\varphi = \partial^\mu\varphi\,\partial_\mu\partial^\nu\varphi - m^2\varphi\partial^\nu\varphi$。代入：

$$\partial_\mu T^{\mu\nu} = (\Box\varphi + m^2\varphi)\partial^\nu\varphi = 0\quad(\text{场方程}).\qquad\square$$

**为什么需要 Belinfante 改进**：对有自旋的场（矢量场、旋量场），上述"正则" $T^{\mu\nu}$ 一般**不对称**（$T^{0i} \neq T^{i0}$）。但角动量守恒要求 $T^{\mu\nu}$ 对称（否则角动量流不守恒），而广义相对论要求引力源是对称的能动张量。Belinfante 的办法是加一个散度型改进项

$$T^{\mu\nu}\to T^{\mu\nu} + \partial_\rho\left(\Sigma^{\rho\mu\nu} - \Sigma^{\mu\rho\nu} - \Sigma^{\nu\rho\mu}\right),$$

其中 $\Sigma$ 由场的自旋结构给出；改进不改变总能量动量（散度的空间积分在无穷远为零），但使 $T^{\mu\nu}$ 对称。$\square$

</details>

## 参考

- Landau & Lifshitz《力学》§6–7（能量、动量、角动量作为时空对称性的 Noether 荷）。
- Goldstein《Classical Mechanics》第 2 章（变分原理与守恒律）、第 8 章（Noether 定理的场论推广）。
- 第 5 章（作用量原理）、第 9 章（守恒量的括号代数、正则量子化）；场论版本见 QFT 书第 3 阶段 02 篇（诺特流与能动张量）、第 4 阶段 01 篇（U(1) 荷 $N_a - N_b$）、第 4 阶段 05 篇（Ward 恒等式）、第 5 阶段 03 篇（自发破缺与 Goldstone）。
