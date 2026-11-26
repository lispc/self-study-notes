# 中心力场：Kepler 问题、Runge–Lenz 矢量与隐藏对称性

> 路线图位置：第 0 部分（牛顿力学的重审）· 第 2 章
> 前置知识：第 1 章（极坐标下的牛顿方程、约束与广义坐标）；第 5 章（最小作用量与 Euler–Lagrange 方程）、第 6 章（角动量作为转动对称性的 Noether 荷）。
> 学习目标：会证明中心力问题因角动量守恒降到一维并用有效势定性分析；会推导 Binet 方程并解出 Kepler 轨道；会验证 Runge–Lenz 矢量守恒并解释它对应隐藏的 SO(4) 对称性；会用 Kepler 方程从轨道求时间。

---

**单位约定**：本篇用通常单位；$k \equiv GMm$（吸引，$k \gt 0$），$\ell$ 为角动量大小（避免与拉氏量 $L$ 混淆）。

## 1. 一句话总结

**中心力问题（$V = V(r)$）靠角动量守恒从三维降到一维：轨道在平面内，径向运动由有效势 $V_{\mathrm{eff}} = V + \ell^2/(2mr^2)$ 决定。$V = -k/r$ 时还有一个额外的守恒矢量（Runge–Lenz），它把轨道锁成闭合的圆锥曲线——这是 SO(4) 隐藏对称性的经典表现，也解释了为什么只有 $1/r$ 与 $r^2$ 两种中心力给出全部闭合轨道（Bertrand 定理）。**

## 2. 约化到一维

### 2.1 平面运动

中心力 $\mathbf F = F(r)\hat{\mathbf r}$ 对原点的力矩为零，角动量

$$\boldsymbol\ell = \mathbf r\times\mathbf p$$

守恒。$\boldsymbol\ell$ 是常矢量，故 $\mathbf r$ 与 $\mathbf p$ 永远垂直于 $\boldsymbol\ell$——**运动被锁在一个平面内**。取该平面为 $xy$ 平面，极坐标 $(r,\theta)$：

$$L = \frac12 m\left(\dot r^2 + r^2\dot\theta^2\right) - V(r).$$

### 2.2 角动量与有效势

$\theta$ 是循环坐标，共轭动量守恒：

$$p_\theta = \frac{\partial L}{\partial\dot\theta} = mr^2\dot\theta \equiv \ell.$$

于是 $\dot\theta = \ell/(mr^2)$，代入能量：

$$E = \frac12 m\dot r^2 + \frac{\ell^2}{2mr^2} + V(r) \equiv \frac12 m\dot r^2 + V_{\mathrm{eff}}(r).$$

$$\boxed{\;V_{\mathrm{eff}}(r) \equiv V(r) + \frac{\ell^2}{2mr^2}.\;}$$

第二项是"离心势垒"：角动量越大，粒子越难靠近原点。**三维中心力问题化为了一维问题**（代价是 $\ell$ 作为一个参数）。

### 2.3 定性分析

由 $E = \frac12m\dot r^2 + V_{\mathrm{eff}}$：

- 允许区域由 $E \ge V_{\mathrm{eff}}(r)$ 给出；转折点 $E = V_{\mathrm{eff}}$ 处 $\dot r = 0$；
- 圆轨道：$V_{\mathrm{eff}}'(r_0) = 0$，即 $F(r_0) = -\ell^2/(mr_0^3)$（向心力 = 离心力）；
- 稳定性：$V_{\mathrm{eff}}''(r_0) \gt 0$ 时小扰动振荡；$\lt 0$ 时不稳定（自检 3）。

## 3. 轨道方程：Binet 方程

要轨道 $r(\theta)$ 而非 $r(t)$，令 $u = 1/r$，用 $\theta$ 作自变量。由 $\dot\theta = \ell u^2/m$：

$$\dot r = \frac{\mathrm{d}r}{\mathrm{d}\theta}\dot\theta = -\frac{u'}{u^2}\cdot\frac{\ell u^2}{m} = -\frac{\ell}{m}u'.$$

能量：

$$E = \frac{\ell^2}{2m}\left(u'^2 + u^2\right) + V(1/u).$$

对 $\theta$ 求导并除以 $u'$（非圆轨道），得 **Binet 方程**：

$$\boxed{\;u'' + u = -\frac{m\,F(1/u)}{\ell^2 u^2},\qquad F(r) = -V'(r).\;}$$

（自检 1 给出完整推导。）给定力律 $F(r)$，解这个二阶常微分方程即得轨道形状。

## 4. Kepler 问题

### 4.1 轨道

$V = -k/r$，$F = -k/r^2 = -ku^2$。Binet 方程：

$$u'' + u = \frac{mk}{\ell^2}.$$

通解：

$$u(\theta) = \frac{mk}{\ell^2}\left[1 + e\cos(\theta - \theta_0)\right],$$

即

$$r(\theta) = \frac{p}{1 + e\cos(\theta-\theta_0)},\qquad p \equiv \frac{\ell^2}{mk}.$$

这是以原点为焦点的**圆锥曲线**：$e \lt 1$ 椭圆、$e = 1$ 抛物线、$e \gt 1$ 双曲线。近日点在 $\theta = \theta_0$。

### 4.2 能量与偏心率

把解代回能量表达式，得到

$$e = \sqrt{1 + \frac{2E\ell^2}{mk^2}}.$$

（自检 1 的末尾。）于是：

- $E \lt 0$：$e \lt 1$，椭圆（束缚）；
- $E = 0$：$e = 1$，抛物线（临界）；
- $E \gt 0$：$e \gt 1$，双曲线（散射）。

椭圆的半长轴与半短轴：

$$a = \frac{p}{1-e^2} = -\frac{k}{2E},\qquad b = a\sqrt{1-e^2}.$$

**半长轴只依赖能量**（$a = -k/2E$），偏心率依赖能量与角动量——这是 Kepler 问题"能量决定大小、角动量决定形状"的精确版本。

### 4.3 Kepler 三定律

1. **轨道律**：行星沿椭圆运动，太阳在一个焦点上（§4.1）；
2. **面积律**：$\mathrm{d}A/\mathrm{d}t = \ell/(2m)$ 常数——角动量守恒的几何版；
3. **周期律**：$T^2 = \dfrac{4\pi^2}{GM}a^3$（自检 4）。

第三定律的推导只用面积律与椭圆面积：$T = \pi ab/(\ell/2m)$，代入 $b = a\sqrt{1-e^2}$ 与 $\ell^2 = mka(1-e^2)$ 即得。

## 5. Runge–Lenz 矢量与隐藏对称性

### 5.1 定义与守恒

定义 **Runge–Lenz 矢量**

$$\mathbf A \equiv \mathbf p\times\boldsymbol\ell - mk\,\hat{\mathbf r}.$$

直接求导（用 $\dot{\mathbf p} = -k\hat{\mathbf r}/r^2$、$\dot{\boldsymbol\ell} = 0$、$\mathrm{d}\hat{\mathbf r}/\mathrm{d}t = \dot\theta\,\hat{\boldsymbol\theta}$）：

$$\frac{\mathrm{d}\mathbf A}{\mathrm{d}t} = \left(-\frac{k}{r^2}\hat{\mathbf r}\right)\times\boldsymbol\ell - mk\,\dot\theta\,\hat{\boldsymbol\theta}.$$

用 $\boldsymbol\ell = mr^2\dot\theta\,\hat{\mathbf z}$ 与 $\hat{\mathbf r}\times\hat{\mathbf z} = -\hat{\boldsymbol\theta}$：

$$\left(-\frac{k}{r^2}\hat{\mathbf r}\right)\times\left(mr^2\dot\theta\,\hat{\mathbf z}\right) = km\dot\theta\,\hat{\boldsymbol\theta}.$$

两项相消：

$$\frac{\mathrm{d}\mathbf A}{\mathrm{d}t} = 0.$$

（完整推导见自检 2。）$\mathbf A$ 在轨道平面内（$\mathbf A\cdot\boldsymbol\ell = 0$），指向近日点，大小

$$|\mathbf A| = mk\,e.$$

### 5.2 它的意义：SO(4) 对称性

中心力问题本来只有 SO(3) 转动对称（守恒量 $\boldsymbol\ell$ 三个分量）。$1/r$ 势额外给出 $\mathbf A$ 三个守恒量（只有两个独立，因为 $\mathbf A\cdot\boldsymbol\ell = 0$）——合起来是 **6 个守恒量**，正是四维转动群 SO(4) 的维数。这就是 Kepler 问题的"隐藏对称性"：

- 经典层面：$\{\ell_i,\ell_j\} = \varepsilon_{ijk}\ell_k$、$\{\ell_i,A_j\} = \varepsilon_{ijk}A_k$、$\{A_i,A_j\} \propto \ell_k$——闭合的 $\mathfrak{so}(4)$ 代数；
- 量子层面：氢原子的 $2n^2$ 重简并（量子力学书 06s 篇的 Runge–Lenz 矢量解法），以及能级只依赖 $n$ 不依赖 $l$ 的"偶然简并"。

### 5.3 Bertrand 定理

为什么只有 $1/r$ 与 $r^2$ 两种中心力给出**所有**束缚轨道都闭合？Bertrand 定理（1873）的回答：只有这两种力律使径向振荡频率与角向频率成有理比（对 $1/r$ 恰好相等，对 $r^2$ 为 2:1），从而轨道在有限圈后闭合。其余力律（如 $1/r^3$）的轨道一般是非闭合的玫瑰花形（进动）。

## 6. 从轨道到时间：Kepler 方程

轨道 $r(\theta)$ 给了形状，但天文观测还需要 $r(t)$。引入**偏近点角** $\psi$：

$$r = a(1 - e\cos\psi),$$

则时间由 **Kepler 方程**给出：

$$M \equiv n(t - t_p) = \psi - e\sin\psi,\qquad n \equiv \frac{2\pi}{T} = \sqrt{\frac{GM}{a^3}},$$

$t_p$ 是过近日点的时刻。真近点角 $\theta$ 与 $\psi$ 的关系：

$$\tan\frac{\theta}{2} = \sqrt{\frac{1+e}{1-e}}\,\tan\frac{\psi}{2}.$$

**Kepler 方程是超越方程**（$\psi$ 不能显式解出），实践中用牛顿迭代；它的"不可解性"正是历史上大量近似方法（和后来的混沌研究）的起点之一。

## 7. 小结

- 中心力 ⇒ 角动量守恒 ⇒ 平面运动 + 一维有效势 $V_{\mathrm{eff}} = V + \ell^2/(2mr^2)$。
- Binet 方程 $u'' + u = -mF(1/u)/(\ell^2u^2)$ 给出轨道形状；$1/r$ 势给出圆锥曲线，$e = \sqrt{1+2E\ell^2/(mk^2)}$，$a = -k/(2E)$。
- Kepler 三定律：椭圆轨道、面积速度守恒、$T^2 \propto a^3$。
- Runge–Lenz 矢量 $\mathbf A = \mathbf p\times\boldsymbol\ell - mk\hat{\mathbf r}$ 是额外的守恒量，与 $\boldsymbol\ell$ 合成 $\mathfrak{so}(4)$ 代数——氢原子简并的经典根源。
- Bertrand 定理：只有 $1/r$ 与 $r^2$ 给出全部闭合的束缚轨道。
- 时间由 Kepler 方程 $M = \psi - e\sin\psi$ 给出（超越方程）。

## 自检问题

**1.** 从能量守恒与 $\dot\theta = \ell/(mr^2)$ 推出 Binet 方程，解出 Kepler 轨道并导出 $e = \sqrt{1+2E\ell^2/(mk^2)}$。

<details markdown="1"><summary>点击显示答案</summary>

令 $u = 1/r$，$\dot\theta = \ell u^2/m$。则

$$\dot r = \frac{\mathrm{d}r}{\mathrm{d}\theta}\dot\theta = -\frac{u'}{u^2}\cdot\frac{\ell u^2}{m} = -\frac{\ell}{m}u'.$$

能量：

$$E = \frac12 m\dot r^2 + \frac{\ell^2 u^2}{2m} + V(1/u) = \frac{\ell^2}{2m}\left(u'^2 + u^2\right) + V(1/u).$$

对 $\theta$ 求导：

$$0 = \frac{\ell^2}{m}\left(u'u'' + uu'\right) - V'(1/u)\frac{u'}{u^2}.$$

除以 $u'$（$u'\neq 0$）：

$$u'' + u = -\frac{m\,F(1/u)}{\ell^2u^2},\qquad F = -V'. \qquad\square$$

Kepler：$F = -ku^2$，方程 $u'' + u = mk/\ell^2$。解

$$u = \frac{mk}{\ell^2}\left(1 + e\cos(\theta-\theta_0)\right).$$

代回能量：

$$E = \frac{\ell^2}{2m}\left(u'^2 + u^2\right) - ku.$$

用 $u' = -(mk/\ell^2)e\sin(\theta-\theta_0)$、$u = (mk/\ell^2)(1+e\cos)$，记 $A \equiv mk/\ell^2$：$u'^2+u^2 = A^2[e^2\sin^2 + (1+e\cos)^2] = A^2(1 + 2e\cos + e^2)$。于是

$$E = \frac{\ell^2A^2}{2m}\left(1+2e\cos+e^2\right) - kA(1+e\cos).$$

用 $A = mk/\ell^2$：第一项系数 $\ell^2A^2/(2m) = m k^2/(2\ell^2)$，第二项 $kA = mk^2/\ell^2$。$\cos$ 的系数：$2e\cdot mk^2/(2\ell^2) - e\cdot mk^2/\ell^2 = 0$ ✓（这是守恒的体现）。剩下

$$E = \frac{mk^2}{2\ell^2}(1+e^2) - \frac{mk^2}{\ell^2} = \frac{mk^2}{2\ell^2}(e^2 - 1).$$

解出

$$e^2 = 1 + \frac{2E\ell^2}{mk^2}.\qquad\square$$

</details>

**2.** 证明 Runge–Lenz 矢量守恒，并验证 $|\mathbf A| = mke$、方向沿近日点。

<details markdown="1"><summary>点击显示答案</summary>

$\mathbf A = \mathbf p\times\boldsymbol\ell - mk\hat{\mathbf r}$。求导：

$$\dot{\mathbf A} = \dot{\mathbf p}\times\boldsymbol\ell + \mathbf p\times\dot{\boldsymbol\ell} - mk\,\dot{\hat{\mathbf r}}.$$

中心力问题中 $\dot{\boldsymbol\ell} = 0$；$\dot{\mathbf p} = -k\hat{\mathbf r}/r^2$；$\dot{\hat{\mathbf r}} = \dot\theta\hat{\boldsymbol\theta}$。所以

$$\dot{\mathbf A} = -\frac{k}{r^2}\hat{\mathbf r}\times\boldsymbol\ell - mk\dot\theta\hat{\boldsymbol\theta}.$$

用 $\boldsymbol\ell = mr^2\dot\theta\hat{\mathbf z}$ 与 $\hat{\mathbf r}\times\hat{\mathbf z} = -\hat{\boldsymbol\theta}$：

$$-\frac{k}{r^2}\hat{\mathbf r}\times\left(mr^2\dot\theta\hat{\mathbf z}\right) = -km\dot\theta\left(\hat{\mathbf r}\times\hat{\mathbf z}\right) = +km\dot\theta\hat{\boldsymbol\theta}.$$

故 $\dot{\mathbf A} = km\dot\theta\hat{\boldsymbol\theta} - mk\dot\theta\hat{\boldsymbol\theta} = 0$。$\square$

**大小与方向**：在近日点，$\mathbf p\perp\hat{\mathbf r}$、$\boldsymbol\ell$ 垂直轨道面，故 $\mathbf p\times\boldsymbol\ell$ 沿 $\hat{\mathbf r}$。记 $v_p$ 为近日点速度、$r_p$ 为近日点距离，$\ell = mr_pv_p$：

$$|\mathbf p\times\boldsymbol\ell| = mv_p\cdot mr_pv_p = \frac{\ell^2}{r_p}.$$

又 $\ell^2 = mka(1-e^2) = mkr_p(1+e)$（用 $r_p = a(1-e)$），故

$$|\mathbf p\times\boldsymbol\ell| = mk(1+e),\qquad |\mathbf A| = mk(1+e) - mk = mke.$$

$\mathbf A$ 沿 $\hat{\mathbf r}$（近日点方向），大小 $mke$。$\square$

**为什么这是隐藏对称性**：$\boldsymbol\ell$ 的 3 个分量 + $\mathbf A$ 的 3 个分量（约束 $\mathbf A\cdot\boldsymbol\ell = 0$，独立 2 个）共 6 个守恒量 = SO(4) 的维数；括号代数闭合为 $\mathfrak{so}(4)$（第 9 章的括号）。这就是氢原子能级只依赖 $n$ 的经典根源。

</details>

**3.** 有效势：求 $V = -k/r$ 的圆轨道半径与稳定性条件，并证明径向振荡频率等于轨道角频率。

<details markdown="1"><summary>点击显示答案</summary>

$$V_{\mathrm{eff}} = -\frac{k}{r} + \frac{\ell^2}{2mr^2},\qquad V_{\mathrm{eff}}' = \frac{k}{r^2} - \frac{\ell^2}{mr^3}.$$

圆轨道：$V_{\mathrm{eff}}'(r_0) = 0$：

$$\frac{k}{r_0^2} = \frac{\ell^2}{mr_0^3} \;\Longrightarrow\; r_0 = \frac{\ell^2}{mk}.$$

稳定性：

$$V_{\mathrm{eff}}''(r) = -\frac{2k}{r^3} + \frac{3\ell^2}{mr^4},\qquad V_{\mathrm{eff}}''(r_0) = -\frac{2k}{r_0^3} + \frac{3k}{r_0^3} = \frac{k}{r_0^3} \gt 0,$$

稳定。

径向小振动频率：

$$\omega_r = \sqrt{\frac{V_{\mathrm{eff}}''(r_0)}{m}} = \sqrt{\frac{k}{mr_0^3}}.$$

角向频率：

$$\omega_\theta = \dot\theta = \frac{\ell}{mr_0^2} = \frac{\sqrt{mk r_0}}{mr_0^2} = \sqrt{\frac{k}{mr_0^3}}.$$

$$\boxed{\;\omega_r = \omega_\theta\;}$$

——两个频率相等。这正是轨道闭合的原因（径向振荡与角向转动同步，轨道不"进动"），也是 Runge–Lenz 守恒与 SO(4) 简并的动力学机制。对比：对 $V = -k/r^3$（若稳定），频率比一般不是有理数，轨道呈玫瑰花形。$\square$

</details>

**4.** 从面积速度与椭圆几何推出 Kepler 第三定律 $T^2 = 4\pi^2 a^3/(GM)$。

<details markdown="1"><summary>点击显示答案</summary>

面积速度：$\mathrm{d}A/\mathrm{d}t = \frac12 r^2\dot\theta = \ell/(2m)$。椭圆面积 $\pi ab$，故

$$T = \frac{\pi ab}{\ell/(2m)} = \frac{2\pi m ab}{\ell}.$$

用 $b = a\sqrt{1-e^2}$：

$$T = \frac{2\pi m a^2\sqrt{1-e^2}}{\ell}.$$

再由 $\ell^2 = mka(1-e^2)$（半通径 $p = \ell^2/(mk) = a(1-e^2)$）：

$$\sqrt{1-e^2} = \frac{\ell}{\sqrt{mka}}.$$

代入：

$$T = \frac{2\pi m a^2}{\ell}\cdot\frac{\ell}{\sqrt{mka}} = 2\pi a^{3/2}\sqrt{\frac{m}{k}}.$$

用 $k = GMm$：

$$T^2 = \frac{4\pi^2 m}{k}a^3 = \frac{4\pi^2}{GM}a^3.\qquad\square$$

注意 $T$ 与行星质量无关（$m$ 在 $k = GMm$ 中约掉）——这是"引力质量 = 惯性质量"（等效原理）在 Kepler 问题里的第一次亮相，也是第 5 章 Galileo 不变性之外的另一条线索。

</details>

**5.** Bertrand 定理的检验：对 $V = \frac12 kr^2$（各向同性谐振子），证明所有束缚轨道闭合，并说明它与 Kepler 问题的频率比。

<details markdown="1"><summary>点击显示答案</summary>

二维各向同性谐振子：$H = \frac{p_x^2+p_y^2}{2m} + \frac12k(x^2+y^2)$。两个方向独立：

$$x(t) = A\cos(\omega t+\phi_x),\qquad y(t) = B\cos(\omega t+\phi_y),\qquad \omega = \sqrt{\frac{k}{m}},$$

**频率相同**，故轨道是闭合的——具体形状是椭圆（一般相位差下），参数为 $x^2/A^2 + y^2/B^2 - 2xy\cos\Delta/(AB) = \sin^2\Delta$。

有效势视角：$V_{\mathrm{eff}} = \frac12kr^2 + \ell^2/(2mr^2)$，圆轨道 $r_0^4 = \ell^2/(mk)$；$V_{\mathrm{eff}}''(r_0) = 4k$，故

$$\omega_r = \sqrt{\frac{4k}{m}} = 2\omega,\qquad \omega_\theta = \frac{\ell}{mr_0^2} = \omega.$$

频率比 $\omega_r:\omega_\theta = 2:1$——有理数，轨道闭合（每条径向振荡对应两次角向转圈）。

**对照**：Kepler 问题 $\omega_r:\omega_\theta = 1:1$；谐振子 $2:1$。Bertrand 定理说这两个是仅有的"所有束缚轨道都闭合"的中心力。一般力律的频率比依赖能量与角动量（无理数），轨道在环面上稠密缠绕（准周期），表现为进动的玫瑰花形——这是可积系统"环面运动"的标准图像（第 13 章）。$\square$

</details>

## 参考

- Landau & Lifshitz《力学》§14–15（中心力场与 Kepler 问题）、§18（Bertrand 定理的讨论）。
- Goldstein《Classical Mechanics》第 3 章（中心力问题、Runge–Lenz 矢量）、第 10 章（作用量–角变量与 Kepler 问题的分离）。
- 量子力学书 06s 篇（Runge–Lenz 矢量与 SO(4)：氢原子的矩阵力学解法）；第 5、6 章（作用量原理与 Noether 定理）；第 13 章（可积性与环面运动）。
