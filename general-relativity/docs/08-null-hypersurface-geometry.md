# 零超曲面几何：生成元、膨胀、剪切与 Raychaudhuri 方程

> 路线图位置：第 2 部分（动力学与解）· 第 8 章
> 前置知识：第 3 章（曲率与 Bianchi 恒等式）、第 7 章（零超曲面、$I^\pm$、因果菱形）。
> 学习目标：能说清零超曲面的"法矢即生成元"这一退化性以及为什么需要辅助零矢 $n$；会算膨胀 $\Theta$、剪切 $\sigma_{ab}$ 与扭转 $\omega_{ab}$；会从 $[\nabla,\nabla]$ 推出 Raychaudhuri 方程；会把真空 Raychaudhuri 化成面积振幅 $\varrho$ 的二阶 ODE（论文 (3.25f)），并读出"剪切使面积增长变慢、使时钟读数变大"这条论文 §5 的核心不等式；认识陷俘面与 MOTS。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。零标架取 $\ell^2=n^2=0$、$\ell\cdot n=-1$。曲率约定沿用论文 (3.23)：$2\nabla_{[c}\nabla_{d]}v^a=R^a{}_{bcd}v^b$，$R_{bd}=R^a{}_{bad}$。

## 1. 一句话总结

**零超曲面的法矢是零的，因此它切于超曲面自身——法矢就是生成元，诱导度规退化，无法像类空超曲面那样用 $K_{\mu\nu}$ 定义膨胀。补救的办法是引入一个辅助零矢 $n$（$\ell\cdot n=-1$），把度规投影到二维 cut 上得到 $q_{ab}$；膨胀 $\Theta$、剪切 $\sigma_{ab}$ 都由 $\ell$ 沿生成元的演化定义，而 Raychaudhuri 方程说：在真空里 $\mathcal L_\ell\Theta=-\frac12\Theta^2-\sigma^2\le0$，膨胀只会减小——这就是聚焦。把 $\Theta$ 换成面积振幅 $\varrho$，真空 Raychaudhuri 变成一个极简的 ODE $\ddot\varrho+\frac{\varrho}{8}(\partial_u\bar q)^2=0$：$\varrho$ 是凹的，剪切越大面积增长越慢。论文全部"面积有上界、状态数有限"的论证都从这一个不等式出发。**

## 2. 退化性：为什么零超曲面特殊

设 $H$ 由 $f=0$ 定义，法余矢 $\ell_a=\nabla_a f$。$H$ 是零超曲面意味着

$$g^{ab}\ell_a\ell_b=0 .$$

于是

$$\ell^a\nabla_a f=g^{ab}\ell_a\ell_b=0,$$

即 $\ell^a\in TH$。**法矢落在切空间里**，这与类空超曲面（法矢类时、垂直于超曲面）截然不同。

三个后果：

1. **诱导度规退化**。把 $g_{ab}$ 拉回到 $H$ 上，它有一个零方向（$\ell$ 自己），秩为 2 而不是 3，号差 $(+,+)$。你没法用它定义"体积元"，也没法用它缩并出 $\Theta=\nabla\cdot\ell$ 的"三维迹"。
2. **生成元**。$\ell$ 的积分曲线叫**零生成元**。它们躺在 $H$ 内，是零测地线（§3）。
3. **需要辅助结构**。要谈"横向面积如何变化"，必须选一个**辅助零矢** $n^a$，满足

$$n^a n_a=0,\qquad n^a\ell_a=-1,$$

且 $n$ 不切于 $H$（它是"横向"方向）。$n$ 的选取不唯一（可以加一个沿 $\ell$ 的平移 $n\to n+\alpha\ell$），不同的选法对应不同的"切面族"，物理结果（如 $\Theta$ 的符号与零点）不依赖它。

**几何图像**：$\ell$ 与 $n$ 张成一个二维的"$t$–$r$"平面，$q_{ab}$ 是与之正交的二维"球面"方向。一个因果菱形的每张零片，就是在每个 cut（球面）上用 $(\ell,n,q)$ 这套标架描述的。

## 3. 生成元与仿射参数

对 $H$ 上一般的零法矢场（不一定写成梯度），生成元满足

$$\ell^b\nabla_b\ell^a=\kappa\,\ell^a .$$

$\kappa$ 叫**非仿射度**。它是沿生成元的函数，不是常数（除非 $H$ 是 Killing 视界，此时 $\kappa$ 是表面重力，$T_{\rm Hawking}=\kappa/2\pi$，第 13 章）。

若存在参数 $u$ 使 $\ell^a=(\partial_u)^a$ 且 $\kappa=0$，称 $u$ 为**仿射参数**：

$$\ell^b\nabla_b\ell^a=0 .$$

第 7 章自检 4 已经证明：当 $\ell_a=\nabla_a f$ 时自动 $\kappa=0$。一般情形下重参数化 $u\to u'$ 可令 $\kappa'=\kappa\,(\mathrm{d}u/\mathrm{d}u')^{-1}$ 的变换消去 $\kappa$（一维 ODE 总有解），代价是 $\ell$ 的归一化改变：

$$\ell\to e^{\int\kappa\,\mathrm{d}u}\,\ell .$$

**物理意义**：$u$ 是"沿光走的路程"。论文里 $u$ 从 cap 上置零、在角点 $S$ 读出，这个读数就是**引力时钟**。归一化（时钟的"秒长"）由 cap 上的面积元固定——这正是论文 (3.18) 的 $dA|_{\partial\Sigma_i}=\epsilon^2 dA|_S$。

## 4. 横向度规与三个运动学量

### 4.1 投影

$$\boxed{\;q_{ab}=g_{ab}+\ell_a n_b+n_a\ell_b\;}$$

验证（自检 2）：$q_{ab}\ell^b=q_{ab}n^b=0$，$q^a{}_a=2$，$q_{ab}=q_{(ab)}$。所以 $q_{ab}$ 是二维 cut 上的度规，面积元

$$\mathrm{d}A=\sqrt{q}\,\mathrm{d}^2y=\varrho^2\,\epsilon_0,$$

其中 $\epsilon_0$ 是固定参考面积元，$\varrho$ 是**面积振幅**（论文 (3.17c)–(3.17d) 的 $\varrho$）。

### 4.2 形变张量

$$\boxed{\;K_{ab}\equiv q_a{}^c q_b{}^d\nabla_c\ell_d\;}$$

它与类空超曲面的外曲率同名同构，但含义不同：现在是"横向度规沿生成元的演化率"。分解成三部分：

$$K_{ab}=\tfrac12\Theta\,q_{ab}+\sigma_{ab}+\omega_{ab},$$

$$\Theta\equiv q^{ab}K_{ab}\ (\text{膨胀}),\qquad \sigma_{ab}\equiv K_{(ab)}-\tfrac12\Theta q_{ab}\ (\text{剪切}),\qquad \omega_{ab}\equiv K_{[ab]}\ (\text{扭转}).$$

**两个立刻的化简**：

- $\Theta=\nabla_a\ell^a$（自检 2）。因为 $\ell$ 是仿射测地线，$\ell\cdot\nabla\ell=0$，所以 $q$ 与 $g$ 给出的迹相同。
- $\omega_{ab}=0$。因为 $\ell_a=\nabla_a f$ 是梯度，$\nabla_{[a}\ell_{b]}=0$（第 7 章自检 5 的同一条论证）。所以零超曲面的形变张量是对称的，$K_{ab}=K_{(ab)}$。**这是"超曲面正交"在零情形下的化身。**

### 4.3 与 Lie 导数的关系

在一族沿 $\ell$ 平移的 cut 上，

$$\boxed{\;K_{ab}=\tfrac12\mathcal L_\ell q_{ab}\;}$$

（严格说右边要投影，但因为 $q$ 已经正交于 $\ell$，投影自动成立。）推导见自检 3。于是

$$\mathcal L_\ell q_{ab}=2\sigma_{ab}+\Theta q_{ab},\qquad
\Theta=\frac{1}{\varrho^2}\mathcal L_\ell(\varrho^2)=2\frac{\dot\varrho}{\varrho},$$

最后一步是因为 $q_{ab}=\varrho^2\bar q_{ab}$ 且 $\bar q$ 的行列式固定为 1（论文 (3.17c)：把面积因子单独提出来）。

**为什么把 $\varrho$ 单独提出来**：$\Theta$ 依赖 $\varrho$ 的绝对大小，而 $\sigma_{ab}$ 只依赖"形状的变化率"。把面积因子剥离后，$\bar q_{ab}$ 只携带两个偏振（共形度规的自由数据），$\varrho$ 携带面积——这正是论文 §3.2 的自由数据清单。

## 5. Raychaudhuri 方程

### 5.1 一般形式

$$\boxed{\;\mathcal L_\ell\Theta=-\tfrac12\Theta^2-\sigma_{ab}\sigma^{ab}+\omega_{ab}\omega^{ab}-R_{ab}\ell^a\ell^b\;}$$

自检 4 给出从 $[\nabla_a,\nabla_b]$ 出发的完整推导。三项的物理含义：

- $-\frac12\Theta^2$：**自聚焦**。即使没有物质，光线也会因为"彼此靠拢"而加速会聚（因为面积是二维的，$\Theta$ 的减小是几何效应）。
- $-\sigma^2$：**剪切聚焦**。形状畸变消耗"会聚预算"——剪切越大，面积增长越慢。这是论文 §5 的核心。
- $-R_{ab}\ell^a\ell^b$：**物质聚焦**。零能量条件 $R_{ab}\ell^a\ell^b\ge0$ 时它也是负的（Einstein 方程 $R_{ab}\ell^a\ell^b=8\pi G_N T_{ab}\ell^a\ell^b$）。

### 5.2 真空 + 仿射 + 无扭转

$$\boxed{\;\mathcal L_\ell\Theta=-\tfrac12\Theta^2-\sigma_{ab}\sigma^{ab}\le0\;}$$

等价地（论文 (3.25e)）：

$$C_\ell\equiv\mathcal L_\ell\Theta+\tfrac12\Theta^2+\sigma_{ab}\sigma^{ab}=0 .$$

**聚焦定理**：若 $\Theta(u_0)\lt0$，则 $\mathcal L_\ell\Theta\le-\frac12\Theta^2$ 给出

$$\Theta(u)\le\frac{\Theta_0}{1+\frac12\Theta_0(u-u_0)},$$

所以 $\Theta\to-\infty$ 在有限仿射参数 $\Delta u\le 2/|\Theta_0|$ 内发生。这就是 Penrose 奇点定理的技术核心。

### 5.3 化成面积振幅的 ODE

把 $\Theta=2\dot\varrho/\varrho$ 与 $\sigma^2=\frac14(\partial_u\bar q)^{AB}(\partial_u\bar q)_{AB}$ 代入 §5.2：

$$\boxed{\;\frac{\mathrm{d}^2\varrho}{\mathrm{d}u^2}+\frac{\varrho}{8}\left(\partial_u\bar q\right)^{AB}\left(\partial_u\bar q\right)_{AB}=0\;}$$

这正是论文 (3.25f)。自检 5 给出完整推导，**包括那个 $1/8$ 从哪来**（它来自 $\Theta=2\dot\varrho/\varrho$、$\sigma^2$ 与 $\varrho$ 的标度无关性、以及一维 Raychaudhuri 的系数三者相乘）。

**这个 ODE 为什么好用**：

1. 它是**线性的**（在 $\varrho$ 里），给定 $\bar q(u)$ 就是标准的二阶 ODE，初值 $\varrho(0)$、$\dot\varrho(0)$ 由顶点或 cap 的数据给。
2. 系数 $\frac18(\partial_u\bar q)^2\ge0$，所以 $\ddot\varrho\le0$——**$\varrho$ 是凹函数**。
3. 在光滑顶点处 $\varrho(0)=0$、$\dot\varrho(0)=1$（沿局部 Lorentz 标架归一化），于是

$$\varrho(u)=u-\frac18\int_0^u (u-u')\varrho(u')\left(\partial_{u'}\bar q\right)^2\mathrm{d}u'\le u .$$

**面积上界**：$\mathrm{d}A=\varrho^2\epsilon_0$，故

$$A(u)=\int_S\varrho(u)^2\epsilon_0\le\int_S u^2\epsilon_0=4\pi u^2 .$$

反过来，**要给面积为 $A$ 的 cut，必须至少走 $u\ge\sqrt{A/4\pi}$**——这就是论文 (5.21c) 的时钟下界 $\bar u^*\ge(1-\epsilon)\sqrt{A/4\pi}$ 的来源（$(1-\epsilon)$ 来自 cap 截断与归一化）。

**等价的读法**：在固定面积下，剪切越大 ⇒ 相同 $u$ 处 $\varrho$ 越小 ⇒ 要达到给定面积需要更大的 $u$ ⇒ **时钟读数更大**。这正是论文 §5.2 说的 *"At fixed area, shear can only increase the clock reading"*，也是 §2 结尾"4 维与 JT 的关键区别"：4 维有引力波的两个偏振，它们改变剪切，从而改变时钟读数；JT 里没有这个机制，所以任意多的态可以有相同时钟波函数、导致类型 $\mathrm{I}_\infty$。

## 6. 陷俘面、MOTS 与奇点定理

### 6.1 二维类空曲面的两个膨胀

设 $S$ 是二维类空曲面，两个零法矢 $\ell,n$（$\ell\cdot n=-1$）。分别定义

$$\Theta_{(\ell)}=q^{ab}\nabla_a\ell_b,\qquad \Theta_{(n)}=q^{ab}\nabla_a n_b .$$

- $\Theta_{(\ell)}\lt0$、$\Theta_{(n)}\lt0$：**陷俘面**（trapped surface）。两个方向的光都在会聚。
- $\Theta_{(\ell)}=0$、$\Theta_{(n)}\lt0$：**边缘外陷俘面**（marginally outer trapped surface, MOTS）。
- $\Theta_{(\ell)}\gt0$、$\Theta_{(n)}\lt0$：**正常面**（normal surface），例如普通球面在平坦空间里。

**为什么用 MOTS 定义黑洞**：事件视界需要知道整个未来（"能否逃到无穷远"），是全局概念，在量子引力与数值模拟里都不可操作。MOTS 只依赖局部几何，是"此刻此地光线停止外逃"的准确表述。论文 (5.51) 就用它，第 13 章会看到它与熵的直接关系。

### 6.2 Penrose 奇点定理（一句话版）

若时空满足零能量条件、全局双曲、且含有一个陷俘面，则时空是**零测地不完备**的。

证明骨架：陷俘面上 $\Theta_{(\ell)}\lt0$ ⇒ 聚焦定理 ⇒ 沿每根出射生成元在有限仿射参数内 $\Theta\to-\infty$ ⇒ 相邻生成元相交（共轭点）⇒ 生成元不能无限延拓。$\square$

这条定理是"引力必然坍缩"的几何表述。论文不直接用它，但"$\Theta$ 的符号决定命运"这套语言贯穿全文。

## 7. 论文怎么用这一章

| 论文位置 | 用到的本章内容 |
|---|---|
| (3.20)–(3.22) | $K_{AB}=E_B^\mu\nabla_A\ell_\mu$、$\Theta=q^{ab}K_{ab}$、$\sigma_{ab}=K_{ab}-\frac12\Theta q_{ab}$ |
| (3.25a)–(3.25f) | $\mathcal L_\ell q_{AB}=2\sigma_{AB}+\Theta q_{AB}$、真空 Raychaudhuri、$\varrho$ 的 ODE |
| (4.27)、(5.21) | 由 $\varrho\le u$ 得面积上界/时钟下界 |
| §5.2 | 固定面积下剪切增大时钟读数 ⇒ 有限维 Hilbert 空间 |
| (5.51) | MOTS 作为局域黑洞定义 |
| App D.3 | 聚焦与"引力子态数目"的估计 |

**一句话记住**：论文的整个有限性论证可以压缩成一行——

$$\varrho\le u\quad\Longrightarrow\quad A\le 4\pi u^2\quad\Longrightarrow\quad\text{时钟截断 }u\le\ell(D)\text{ 给面积上界}.$$

## 8. 小结

- 零超曲面的法矢零且切于自身 ⇒ 诱导度规退化（秩 2），需要辅助零矢 $n$（$\ell\cdot n=-1$）。
- 生成元是零测地线，$\ell^b\nabla_b\ell^a=\kappa\ell^a$；仿射参数 $\kappa=0$，$u$ 既是"光走路程"也是引力时钟的读数。
- 横向度规 $q_{ab}=g_{ab}+\ell_an_b+n_a\ell_b$；形变张量 $K_{ab}=\frac12\mathcal L_\ell q_{ab}=\frac12\Theta q_{ab}+\sigma_{ab}$，扭转为零（$\ell$ 是梯度）。
- $\Theta=\nabla\cdot\ell=2\dot\varrho/\varrho$；真空 Raychaudhuri $\mathcal L_\ell\Theta=-\frac12\Theta^2-\sigma^2\le0$ ⇒ 聚焦。
- 面积振幅满足 $\ddot\varrho+\frac{\varrho}{8}(\partial_u\bar q)^2=0$ ⇒ $\varrho$ 凹、$\varrho\le u$ ⇒ $A\le 4\pi u^2$ ⇒ 时钟读数给面积下界（即面积给时钟下界）。
- 固定面积下剪切越大时钟读数越大——4 维特有，JT 没有。
- 陷俘面 $\Theta_{(\ell)},\Theta_{(n)}\lt0$；MOTS $\Theta_{(\ell)}=0,\Theta_{(n)}\lt0$；Penrose 定理：陷俘面 ⇒ 测地不完备。

## 自检问题

**1.** 证明零超曲面的法矢切于自身；并说明"$\ell^b\nabla_b\ell^a=\kappa\ell^a$"里为什么右端只能是 $\ell^a$ 的倍数。

<details markdown="1"><summary>点击显示答案</summary>

**切于自身**：$H=\{f=0\}$，$\ell_a=\nabla_a f$。零条件 $g^{ab}\ell_a\ell_b=0$。于是

$$\ell^a\nabla_a f=\ell^a\ell_a=g^{ab}\ell_a\ell_b=0 .$$

沿 $\ell$ 方向 $f$ 不变，故 $\ell$ 的积分曲线留在 $f$ 的等值面上，即 $\ell\in TH$。$\square$

**右端为什么是 $\ell^a$ 的倍数**：设 $\gamma$ 是生成元，切矢 $\ell^a$。加速度 $a^a=\ell^b\nabla_b\ell^a$ 度量"曲线偏离测地线"的程度。因为 $\ell^2=0$ 沿 $\gamma$ 恒定：

$$0=\ell^b\nabla_b(\ell^2)=2\ell_a\,\ell^b\nabla_b\ell^a=2\ell_a a^a .$$

所以 $a^a$ 与 $\ell^a$ 正交。可是在零矢量上，"与 $\ell$ 正交"的空间是三维的，包含 $\ell$ 自身与两个横向方向。还需要一条：$a^a$ 必须**切于 $H$**（因为 $\gamma\subset H$，加速度是曲线在 $H$ 内的二阶偏离，若 $H$ 光滑则 $a\in TH$）。而 $TH$ 是三维的，其"度量正交于 $\ell$"的子空间是二维的（$q$ 的像）。这里有一个细微之处：在零超曲面上，"与 $\ell$ 正交且切于 $H$"的方向恰好是一维的（因为 $TH$ 的零方向唯一，且 $n$ 不切于 $H$）。

更直接的论证：$\ell$ 是 $H$ 上唯一的零方向（除逐点缩放外）。$a^a$ 零（因为 $\ell$ 零且平行移动保持 $\ell^2$，$a\cdot\ell=0$ 且 $a$ 切于 $H$，在 $TH$ 中与 $\ell$ 正交的零矢量只能是 $\ell$ 的倍数），故

$$a^a=\kappa\ell^a .$$

（若不假定 $a$ 零，则可用 $H$ 的零性：$TH$ 中与 $\ell$ 正交的矢量必为 $\ell$ 的倍数加横向分量，而横向分量会离开 $TH$。）$\square$

**$\kappa$ 的名字**：非仿射度。在 Killing 视界上它是常数，等于表面重力，Hawking 温度 $T=\kappa/2\pi$。这个 $2\pi$ 与论文里"把 boost 解析延拓到 $i\pi$ 得到 $e^{-2\pi K}$"是同一个 $2\pi$——见第 13 章与 [QFT 书第 9 阶段 03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)。

</details>

**2.** 验证 $q_{ab}=g_{ab}+\ell_an_b+n_a\ell_b$ 满足 $q_{ab}\ell^b=0$、$q_{ab}n^b=0$、$q^a{}_a=2$；并证明 $\Theta=q^{ab}K_{ab}=\nabla_a\ell^a$。

<details markdown="1"><summary>点击显示答案</summary>

**正交性**：

$$q_{ab}\ell^b=\ell_a+\ell_a(n\cdot\ell)+n_a(\ell\cdot\ell)=\ell_a-\ell_a+0=0,$$

$$q_{ab}n^b=n_a+\ell_a(n\cdot n)+n_a(\ell\cdot n)=n_a+0-n_a=0 .$$

**迹**：

$$q^a{}_a=g^{ab}q_{ab}=g^{ab}\left(g_{ab}+\ell_an_b+n_a\ell_b\right)=4+2(\ell\cdot n)=4-2=2 .$$

所以 $q$ 是二维 cut 上的度规，号差 $(+,+)$。$\square$

**$\Theta=\nabla\cdot\ell$**：

$$q^{ab}K_{ab}=q^{ab}\nabla_a\ell_b=\left(g^{ab}+\ell^an^b+n^a\ell^b\right)\nabla_a\ell_b
=\nabla_a\ell^a+\ell^an^b\nabla_a\ell_b+n^a\ell^b\nabla_a\ell_b .$$

第二项：$\ell^a\nabla_a\ell_b=0$（仿射测地线），故为零。

第三项：$n^a\ell^b\nabla_a\ell_b=\frac12 n^a\nabla_a(\ell^b\ell_b)=\frac12 n^a\nabla_a(0)=0$。

所以

$$\boxed{\Theta=\nabla_a\ell^a .}\qquad\square$$

**为什么这件事值得单独说**：对类空超曲面，$K=h^{\mu\nu}\nabla_\mu n_\nu=\nabla_\mu n^\mu$ 也成立，但那里是因为 $n$ 是单位法矢；这里 $\ell$ 是零矢，$g$ 与 $q$ 给出的迹竟然相同，全靠"仿射"与"$\ell$ 零"两条。如果 $\ell$ 不是仿射的（$\kappa\neq0$），$\Theta$ 里就会多出 $\kappa$ 的项——这也是为什么论文必须先把仿射参数固定下来（(3.18) 的归一化）。

</details>

**3.** 证明在一族沿 $\ell$ 平移的 cut 上 $K_{ab}=\frac12\mathcal L_\ell q_{ab}$。

<details markdown="1"><summary>点击显示答案</summary>

$$q_{ab}=g_{ab}+\ell_a n_b+n_a\ell_b .$$

逐项求 Lie 导数。用 $\mathcal L_\ell g_{ab}=\nabla_a\ell_b+\nabla_b\ell_a$：

$$\mathcal L_\ell q_{ab}=\nabla_a\ell_b+\nabla_b\ell_a+\mathcal L_\ell(\ell_a n_b)+\mathcal L_\ell(n_a\ell_b).$$

先算 $\mathcal L_\ell\ell_a$：

$$\mathcal L_\ell\ell_a=\ell^c\nabla_c\ell_a+\ell_c\nabla_a\ell^c=0+\tfrac12\nabla_a(\ell^2)=0,$$

第一项用仿射测地线，第二项用 $\ell^2=0$。所以 $\ell$ 沿自己不变（几何上显然：$[\ell,\ell]=0$）。于是

$$\mathcal L_\ell(\ell_a n_b)=(\mathcal L_\ell\ell_a)n_b+\ell_a\mathcal L_\ell n_b=\ell_a\mathcal L_\ell n_b,$$

同理 $\mathcal L_\ell(n_a\ell_b)=n_a\mathcal L_\ell\ell_b+\ell_b\mathcal L_\ell n_a=\ell_b\mathcal L_\ell n_a$。合计

$$\mathcal L_\ell q_{ab}=\nabla_a\ell_b+\nabla_b\ell_a+\ell_a X_b+\ell_b X_a,\qquad X_a\equiv\mathcal L_\ell n_a .$$

现在用 $q$ 投影：$q_a{}^c q_b{}^d\ell_c=0$，故最后两项被投影掉：

$$q_a{}^c q_b{}^d\mathcal L_\ell q_{cd}=q_a{}^c q_b{}^d\left(\nabla_c\ell_d+\nabla_d\ell_c\right)=2K_{(ab)} .$$

**扭转为零**（$\ell$ 是梯度，$\nabla_{[a}\ell_{b]}=0$，第 7 章自检 5），故 $K_{ab}=K_{(ab)}$，于是

$$\boxed{K_{ab}=\tfrac12\,q_a{}^c q_b{}^d\,\mathcal L_\ell q_{cd}\;.}\qquad\square$$

在 cut 上把投影省略（$q_{AB}$ 本来就只在 cut 上有定义），就是论文 (3.25a)：

$$\mathcal L_\ell q_{AB}=2K_{AB}=2\sigma_{AB}+\Theta q_{AB}.$$

**要点**：这一步把"$\ell$ 的导数"翻译成"横向度规的演化"。它成立的三个前提缺一不可：$\ell$ 零、$\ell$ 仿射测地、$\ell$ 无扭转。论文的零锥数据之所以干净，就是因为这三条在零锥上自动满足。

</details>

**4.** 从 $[\nabla_a,\nabla_b]\ell^b=-R_{ab}\ell^b$ 出发，推出 $\mathcal L_\ell\Theta=-\frac12\Theta^2-\sigma^2+\omega^2-R_{ab}\ell^a\ell^b$。

<details markdown="1"><summary>点击显示答案</summary>

记 $B_{ab}=\nabla_a\ell_b$，$\Theta=\nabla\cdot\ell=B^a{}_a$。

**第一步：交换导数。**

$$\ell^a\nabla_a\Theta=\ell^a\nabla_a\nabla_b\ell^b=\ell^a\nabla_b\nabla_a\ell^b+\ell^a[\nabla_a,\nabla_b]\ell^b .$$

由 $[\nabla_a,\nabla_b]\ell^b=R^b{}_{cab}\ell^c=-R_{ac}\ell^c$（用 $R_{ab}=R^c{}_{acb}$ 的定义），

$$\ell^a[\nabla_a,\nabla_b]\ell^b=-R_{ac}\ell^a\ell^c .$$

**第二步：把 $\ell^a\nabla_b\nabla_a\ell^b$ 换成 $-\mathrm{tr}(B^2)$。** 用 $\ell^b\nabla_b\ell^a=0$ 的协变导数：

$$0=\nabla_b\left(\ell^a\nabla_a\ell^b\right)=\left(\nabla_b\ell^a\right)\left(\nabla_a\ell^b\right)+\ell^a\nabla_b\nabla_a\ell^b .$$

所以

$$\ell^a\nabla_b\nabla_a\ell^b=-B_b{}^aB_a{}^b .$$

**第三步：算 $\mathrm{tr}(B^2)$。** 把 $B$ 分解成"投影部分 + 沿 $\ell$ 与 $n$ 的部分"：

$$B_{ab}=\hat B_{ab}+\ell_a u_b+\ell_b v_a,\qquad \hat B_{ab}=\tfrac12\Theta q_{ab}+\sigma_{ab}+\omega_{ab}.$$

（沿 $\ell$ 的项可以写成 $\ell_a u_b+\ell_b v_a$ 的一般形式而不失一般性。）交叉项在 $B_b{}^aB_a{}^b$ 里全消：$q^{ac}\ell_c=0$，且 $\ell^a\ell_a=0$。于是

$$B_b{}^aB_a{}^b=\hat B_b{}^a\hat B_a{}^b .$$

代入 $\hat B$，交叉项再次因对称性相消（$\sigma$ 无迹对称、$\omega$ 反对称、$q$ 与两者都正交）：

$$\hat B_b{}^a\hat B_a{}^b=\tfrac14\Theta^2\,q_b{}^a q_a{}^b+\sigma_b{}^a\sigma_a{}^b+\omega_b{}^a\omega_a{}^b .$$

$q_b{}^a q_a{}^b=q^{ab}q_{ab}=2$（二维），$\sigma_b{}^a\sigma_a{}^b=\sigma^{ab}\sigma_{ab}$，$\omega_b{}^a\omega_a{}^b=-\omega^{ab}\omega_{ab}$。故

$$\mathrm{tr}(B^2)=\tfrac12\Theta^2+\sigma^2-\omega^2 .$$

**第四步：合并。**

$$\boxed{\ell^a\nabla_a\Theta=-\tfrac12\Theta^2-\sigma_{ab}\sigma^{ab}+\omega_{ab}\omega^{ab}-R_{ab}\ell^a\ell^b .}\qquad\square$$

**检验两个极限**：

- 平坦空间、球面对称的膨胀光锥：$\sigma=\omega=R=0$，得 $\dot\Theta=-\frac12\Theta^2$，解 $\Theta=2/u$（因为 $\varrho=u$，$\Theta=2/u$ ✓）。
- 真空 + 无扭转：$\dot\Theta=-\frac12\Theta^2-\sigma^2\le0$，聚焦。

**符号注意**：$R_{ab}$ 的符号依赖约定。本章用论文的 $R_{bd}=R^a{}_{bad}$；换成 Wald 的 $R_{ab}=R^c{}_{acb}$ 会整体翻号，但"零能量条件 ⇒ 聚焦"的结论不变，因为 $R_{ab}\ell^a\ell^b=8\pi G_NT_{ab}\ell^a\ell^b$ 的符号是物理的。

</details>

**5.** 把 $\Theta=2\dot\varrho/\varrho$ 与 $\sigma^2=\frac14(\partial_u\bar q)^{AB}(\partial_u\bar q)_{AB}$ 代入真空 Raychaudhuri，推出论文 (3.25f) $\ddot\varrho+\frac{\varrho}{8}(\partial_u\bar q)^2=0$；再证明 $\varrho\le u$（顶点处 $\varrho(0)=0,\dot\varrho(0)=1$），并解释"固定面积下剪切增大时钟读数"。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：$\Theta$ 与 $\varrho$。** $q_{AB}=\varrho^2\bar q_{AB}$，$\bar q$ 行列式为 1，故 $\sqrt q=\varrho^2\sqrt{\bar q}$，

$$\Theta=\frac{1}{\sqrt q}\partial_u\sqrt q=\frac{1}{\varrho^2}\partial_u(\varrho^2)=2\frac{\dot\varrho}{\varrho}.$$

**第二步：$\sigma^2$ 与 $\varrho$ 无关。** 由 (3.25a) 与 $q_{AB}=\varrho^2\bar q_{AB}$：

$$\sigma_{AB}=\tfrac12\mathcal L_\ell q_{AB}-\tfrac12\Theta q_{AB}
=\tfrac12\left(2\varrho\dot\varrho\,\bar q_{AB}+\varrho^2\dot{\bar q}_{AB}\right)-\tfrac{\dot\varrho}{\varrho}\varrho^2\bar q_{AB}
=\tfrac{\varrho^2}{2}\dot{\bar q}_{AB}.$$

缩并时用 $q^{AC}=\varrho^{-2}\bar q^{AC}$：

$$\sigma^2=\sigma_{AB}\sigma_{CD}q^{AC}q^{BD}
=\frac{\varrho^4}{4}\dot{\bar q}_{AB}\dot{\bar q}_{CD}\,\varrho^{-4}\bar q^{AC}\bar q^{BD}
=\frac14\left(\partial_u\bar q\right)^{AB}\left(\partial_u\bar q\right)_{AB}.$$

**$\varrho$ 完全抵消**——这是二维共形结构的红利，也是为什么论文能把"形状"与"面积"彻底分离。$\square$

**第三步：代入。** $\mathcal L_\ell\Theta=\partial_u(2\dot\varrho/\varrho)=2\ddot\varrho/\varrho-2\dot\varrho^2/\varrho^2$，且 $\frac12\Theta^2=2\dot\varrho^2/\varrho^2$，两者相加时 $\dot\varrho^2$ 项相消：

$$0=\mathcal L_\ell\Theta+\tfrac12\Theta^2+\sigma^2=\frac{2\ddot\varrho}{\varrho}+\sigma^2 .$$

代入 $\sigma^2=\frac14(\partial_u\bar q)^2$：

$$\boxed{\frac{2\ddot\varrho}{\varrho}+\frac14(\partial_u\bar q)^2=0
\;\Longleftrightarrow\;
\ddot\varrho+\frac{\varrho}{8}(\partial_u\bar q)^{AB}(\partial_u\bar q)_{AB}=0\;.}\qquad\square$$

**第四步：凹性与 $\varrho\le u$。** 系数 $\frac18(\partial_u\bar q)^2\ge0$（它是 $\bar q$ 的变率在 $\bar q$ 下的模方），$\varrho\gt0$，故 $\ddot\varrho\le0$。在光滑顶点取 $\varrho(0)=0$、$\dot\varrho(0)=1$，则 $\varrho$ 从原点出发、斜率 1、向下弯：

$$\varrho(u)=u-\frac18\int_0^u(u-u')\varrho(u')\left(\partial_{u'}\bar q\right)^2\mathrm{d}u'\le u .$$

**第五步：面积与时钟。** 面积 $A(u)=\int_S\varrho^2\epsilon_0\le u^2\int_S\epsilon_0=4\pi u^2$。所以：

- **给定 $u$**：剪切越大 ⇒ $\varrho$ 越小 ⇒ 面积越小。
- **给定面积 $A$**：剪切越大 ⇒ 需要更大的 $u$ 才能长到 $A$ ⇒ **时钟读数越大**。

这正是论文 §5.2 的 *"At fixed area, shear can only increase the clock reading"*，也是 (5.21c) 的 $\bar u^*\ge(1-\epsilon)\sqrt{A/4\pi}$。$\square$

**为什么这条不等式是全文的枢纽**：它把"时钟截断 $u\le\ell(D)$"翻译成"面积上界 $A\lesssim4\pi\ell(D)^2$"，再翻译成"角点面积算符在 $\mathcal H_D$ 上有界"，最后翻译成"$\mathcal H_D$ 有限维"。没有这一步，$G_N$ 有限的量子化就无从谈起。而在 JT 里 $\varrho$ 就是 dilaton、没有 $\bar q$ 的自由度（没有引力波），所以这条不等式不产生对态数的限制——这正是论文 §2 与 §5 的分水岭。

</details>

## 参考

- Poisson《A Relativist's Toolkit》第 2 章（零超曲面的 $q_{ab}$、$\Theta$、$\sigma$、$\omega$、Raychaudhuri 的标准处理；本章的主要母本）。
- Wald《General Relativity》第 9 章（Raychaudhuri 方程与奇点定理）、第 12 章（Killing 视界的表面重力）。
- Hawking & Ellis《The Large Scale Structure of Space-Time》第 4 章（聚焦定理与陷俘面）。
- Carroll《Spacetime and Geometry》第 9 章（黑洞与视界的热力学，$\kappa$ 与 $T$ 的关系）。
- [QFT 书第 9 阶段 03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)（JT 引力里 $\varrho$ 就是 dilaton：没有引力波自由度，所以出现 $\mathrm{I}_\infty$）、[04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)（面积谱与熵）。
- 论文 arXiv:2611.34924 §3.2（(3.20)–(3.25f) 的原始出处）、§4.4（(4.27) 的时钟下界）、§5.2（剪切与时钟的单调性）、App D.3（聚焦与态数估计）。
