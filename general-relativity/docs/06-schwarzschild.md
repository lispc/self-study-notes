# Schwarzschild 解与黑洞几何

> 路线图位置：第 2 部分（动力学与解）· 第 6 章
> 前置知识：第 2 章（测地线）、第 3 章（曲率、Killing 矢量）、第 4 章（$\star$ 与 Komar 荷）、第 5 章（Einstein 方程与弱场极限）、第 7 章（因果结构，可并行）。
> 学习目标：会从球对称 ansatz 解出 Schwarzschild；能说清 $r=2G_NM$ 是坐标奇异而非几何奇异（Kretschmann 判据）；会写 Kruskal 延拓并解释四个区域；会用有效势算圆轨道、ISCO、光子球；会算光线偏折与近日点进动；知道视界面积、表面重力与 $T,S$ 的公式（第 13 章的入口）。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。记 $m\equiv G_NM$（几何质量，长度量纲）。曲率约定同第 3 章。

## 1. 一句话总结

**球对称真空解只有一个（Birkhoff），它就是 Schwarzschild：$\mathrm{d}s^2=-(1-2G_NM/r)\mathrm{d}t^2+\frac{\mathrm{d}r^2}{1-2G_NM/r}+r^2\mathrm{d}\Omega^2$。** $r=2G_NM$ 处度规分量发散，但曲率标量 $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=48G_N^2M^2/r^6$ 有限——那是坐标奇异，几何上是一张光滑的零超曲面（视界）。Kruskal 坐标把它延拓成四个区域，黑洞 = 无法逃到未来无穷远的区域。测地线给出全部经典检验：水星近日点进动、光线偏折、引力红移；有效势给出 ISCO $r=6G_NM$ 与光子球 $r=3G_NM$。

## 2. 对称性假设

球对称意味着存在 $SO(3)$ 作用，轨道是二维球面。最一般的球对称度规可以写成

$$\boxed{\;\mathrm{d}s^2=-e^{2\alpha(r)}\mathrm{d}t^2+e^{2\beta(r)}\mathrm{d}r^2+r^2\left(\mathrm{d}\theta^2+\sin^2\theta\,\mathrm{d}\phi^2\right)\;}$$

其中 $r$ 是**面积半径**（定义为"半径为 $r$ 的球面面积为 $4\pi r^2$"），这样 $r^2\mathrm{d}\Omega^2$ 的部分就被固定了。剩下两个待定函数 $\alpha,\beta$。

**静态 + 球对称**（不要求静态也可以，Birkhoff 会告诉你结果是静态的）意味着度规不依赖 $t$，且没有 $t$–$r$ 交叉项（交叉项可以通过重定义 $t$ 消掉）。

## 3. 解方程

真空（$\Lambda=0$）：$R_{\mu\nu}=0$。需要的 Christoffel 符号（非零的）：

$$\Gamma^t{}_{tr}=\alpha',\quad \Gamma^r{}_{tt}=e^{2(\alpha-\beta)}\alpha',\quad \Gamma^r{}_{rr}=\beta',$$
$$\Gamma^r{}_{\theta\theta}=-re^{-2\beta},\quad \Gamma^r{}_{\phi\phi}=-re^{-2\beta}\sin^2\theta,\quad
\Gamma^\theta{}_{r\theta}=\Gamma^\phi{}_{r\phi}=\frac1r,\quad \Gamma^\theta{}_{\phi\phi}=-\sin\theta\cos\theta,\quad \Gamma^\phi{}_{\theta\phi}=\cot\theta .$$

Ricci 分量（自检 1 给推导）：

$$R_{tt}=e^{2(\alpha-\beta)}\left(\alpha''+\alpha'^2-\alpha'\beta'+\frac{2\alpha'}{r}\right),$$
$$R_{rr}=-\left(\alpha''+\alpha'^2-\alpha'\beta'-\frac{2\beta'}{r}\right),$$
$$R_{\theta\theta}=e^{-2\beta}\left(1+r\alpha'-r\beta'\right)-1,\qquad R_{\phi\phi}=R_{\theta\theta}\sin^2\theta .$$

**第一步：$R_{tt}=R_{rr}=0$。** 把 $R_{rr}$ 乘 $e^{2(\alpha-\beta)}$ 与 $R_{tt}$ 相加，方括号里的 $\alpha''+\alpha'^2-\alpha'\beta'$ 相消，剩

$$\frac{2\alpha'}{r}+\frac{2\beta'}{r}=0\;\Longrightarrow\;\alpha'+\beta'=0\;\Longrightarrow\;\alpha+\beta=\text{常数}.$$

重定义 $t\to e^{\text{常数}}t$ 可令常数 $=0$，即

$$\boxed{\;\beta=-\alpha\;}$$

**第二步：$R_{\theta\theta}=0$。** 代入 $\beta=-\alpha$：

$$e^{2\alpha}\left(1+2r\alpha'\right)=1 .$$

注意这是全导数：

$$\frac{\mathrm{d}}{\mathrm{d}r}\left(r\,e^{2\alpha}\right)=e^{2\alpha}+2r\alpha'e^{2\alpha}=1
\;\Longrightarrow\;r\,e^{2\alpha}=r-2G_NM .$$

（积分常数写成 $-2G_NM$，符号由下面的牛顿极限定。）

**第三步：结果。**

$$\boxed{\;e^{2\alpha}=1-\frac{2G_NM}{r},\qquad e^{2\beta}=\left(1-\frac{2G_NM}{r}\right)^{-1}\;}$$

$$\boxed{\;\mathrm{d}s^2=-\left(1-\frac{2G_NM}{r}\right)\mathrm{d}t^2+\frac{\mathrm{d}r^2}{1-\frac{2G_NM}{r}}+r^2\mathrm{d}\Omega^2\;}$$

**第四步：定常数。** 大 $r$ 展开：

$$g_{00}=-\left(1-\frac{2G_NM}{r}\right)=-\left(1+\frac{2\Phi}{c^2}\right)\bigg|_{\Phi=-\frac{G_NM}{r}}\ \checkmark$$

与第 5 章的弱场形式 $g_{00}=-(1+2\Phi)$、$\Phi=-G_NM/r$ 一致。

**带 $\Lambda$**：同样步骤给 $f=1-2G_NM/r-\Lambda r^2/3$（Schwarzschild–de Sitter）。

## 4. Birkhoff 定理

**定理**：球对称的真空解局部等距于 Schwarzschild（带 $\Lambda$ 时等距于 Schwarzschild–dS）。

**证明思路**：上面的推导只用了"球对称 + 真空"，**没有**假设静态。$R_{tt}=R_{rr}=0$ 强迫 $\alpha'+\beta'=0$，$R_{\theta\theta}=0$ 强迫 $re^{2\alpha}=r-2G_NM$——常数与 $t$ 无关，所以解自动静态。$\square$

**物理推论**：

1. **球对称坍缩不辐射引力波**。脉动球的 monopole 辐射为零；引力波从四极开始（quadrupole）。这是"LIGO 测到的都是双星并合（四极）"的理论根据。
2. **Birkhoff 是"引力版的 Gauss 定理"**：球外场只由总质量决定，与内部如何运动无关。
3. **但要注意**：Birkhoff 说的是"球对称真空解唯一"，不是"球对称物体外部一定是 Schwarzschild"——如果外部有物质/辐射，就不适用。恒星内部的解是 TOV 方程（不在本书范围）。

## 5. 坐标奇异 vs 几何奇异

### 5.1 曲率判据

Schwarzschild 的 Kretschmann 标量（自检 2）：

$$\boxed{\;R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=\frac{48G_N^2M^2}{r^6}\;}$$

- $r=2G_NM$：有限（$=\frac{3}{4G_N^4M^4}$）⇒ **不是几何奇异**。
- $r=0$：发散 ⇒ **真奇异**（曲率不变量发散）。

### 5.2 为什么 $r=2G_NM$ 看起来奇异

在 Schwarzschild 坐标里：

- $g_{tt}\to0$、$g_{rr}\to\infty$；
- $g^{rr}=f\to0$，所以 $r=\text{const}$ 的曲面在 $r=2G_NM$ 处变成**零**超曲面（法矢 $n=\partial_r$ 的长度平方为 $f$，$f=0$ ⇒ 零）。

**"$t$ 是时间、$r$ 是空间"的标签在 $r\lt2G_NM$ 处翻转**：那里 $f\lt0$，$g_{tt}>0$、$g_{rr}\lt0$——$r$ 变成时间方向。所以"$r=2G_NM$ 是时间的转折点"，用 $t,r$ 坐标跨越它必然出问题（就像在地球仪上用经纬度跨越极点）。

### 5.3 判据清单（与第 2 章 §7 一致）

1. $g_{\mu\nu}$ 分量发散 ⇒ 可能只是坐标坏。
2. 曲率张量的分量在**某组**坐标里发散 ⇒ 强提示。
3. 曲率**标量**发散 ⇒ 真奇异。
4. 测地线不完备 ⇒ 最严格（Penrose 定义）。

**Schwarzschild 的 $r=0$ 满足 3 与 4**（类光/类时测地线在有限仿射参数内终止），而 $r=2G_NM$ 都不满足。

## 6. Kruskal 延拓

### 6.1 乌龟坐标

定义**乌龟半径**

$$r_*\equiv r+2G_NM\ln\left|\frac{r}{2G_NM}-1\right|,\qquad
\mathrm{d}r_*=\frac{\mathrm{d}r}{1-2G_NM/r}=\frac{\mathrm{d}r}{f}.$$

于是

$$\mathrm{d}s^2=-f\left(\mathrm{d}t^2-\mathrm{d}r_*^2\right)+r^2\mathrm{d}\Omega^2
=-f\,\mathrm{d}u\,\mathrm{d}v+r^2\mathrm{d}\Omega^2,$$

$$u\equiv t-r_*,\qquad v\equiv t+r_* .$$

$r\to2G_NM$ 时 $r_*\to-\infty$，$u\to+\infty$、$v\to-\infty$——所以 $t,r$ 坐标的"奇异"是"乌龟坐标把视界推到了无穷远"。

### 6.2 Kruskal 坐标

$$\boxed{\;U\equiv-e^{-u/(4G_NM)},\qquad V\equiv e^{v/(4G_NM)}\;}$$

用 $\mathrm{d}U\,\mathrm{d}V=\frac{1}{16G_N^2M^2}e^{r_*/(2G_NM)}\mathrm{d}u\,\mathrm{d}v$ 与 $f\,e^{-r_*/(2G_NM)}=\frac{2G_NM}{r}e^{-r/(2G_NM)}$：

$$\boxed{\;\mathrm{d}s^2=-\frac{32G_N^3M^3}{r}e^{-\frac{r}{2G_NM}}\,\mathrm{d}U\,\mathrm{d}V
+r^2\mathrm{d}\Omega^2\;}$$

其中 $r$ 由 $UV=-e^{r_*/(2G_NM)}=e^{r/(2G_NM)}\left(1-\frac{r}{2G_NM}\right)$ 隐式给出（等价地 $UV=0\Leftrightarrow r=2G_NM$）。

### 6.3 三个关键事实

1. **$r=2G_NM$ 处正则**：$U=0$（或 $V=0$）是一条光滑的零超曲面；前置因子 $\frac{32G_N^3M^3}{r}e^{-r/2G_NM}$ 在 $r=2G_NM$ 处等于 $16G_N^2M^2e^{-1}$，有限且非零。
2. **$r=0$ 是真奇异**：$UV=1$ 是双曲线，曲率在此发散。
3. **四个区域**：

| 区域 | $U$ | $V$ | 物理 |
|---|---|---|---|
| I | $\lt0$ | $\gt0$ | 外部（$r\gt2G_NM$） |
| II | $\gt0$ | $\gt0$ | 黑洞内部（未来） |
| III | $\lt0$ | $\lt0$ | 另一个外部（平行宇宙） |
| IV | $\gt0$ | $\lt0$ | 白洞内部（过去） |

区域 II 的特征：任何未来指向的因果曲线都无法到达 $r=\infty$。**这就是"黑洞"的定义性陈述**——不需要"$r=2G_NM$ 是奇点"这种错话。

**Penrose 图**：把 $U,V$ 换成 $\tilde U=\arctan U$、$\tilde V=\arctan V$，得到有限大小的菱形，四个区域对称排列，$r=0$ 是上下两条锯齿边界，$\mathscr{I}^\pm$ 是左右两条类光无穷远。第 7 章会用它讨论因果结构。

## 7. 测地线

### 7.1 两个守恒量

两个 Killing 矢量：$\xi_{(t)}=\partial_t$、$\xi_{(\phi)}=\partial_\phi$。第 3 章 §7.2：

$$E\equiv-g_{t\mu}\dot x^\mu=f\dot t=\left(1-\frac{2G_NM}{r}\right)\dot t,\qquad
L\equiv r^2\dot\phi .$$

（$E$ 是单位质量能量，$L$ 是单位质量角动量；点表示对仿射参数。）

### 7.2 有效势

用 $-f\dot t^2+\dot r^2/f+r^2\dot\phi^2=\epsilon$（$\epsilon=-1$ 类时、$0$ 类光）：

$$\boxed{\;\dot r^2=E^2-V_{\rm eff}(r),\qquad
V_{\rm eff}(r)=f(r)\left(\epsilon+\frac{L^2}{r^2}\right)\;}$$

**类时**（$\epsilon=-1$）：$V_{\rm eff}=f(1+L^2/r^2)$。大 $r$：$V_{\rm eff}\to1-\frac{2G_NM}{r}+\frac{L^2}{r^2}$——Newton + 离心 ✓。

**类光**（$\epsilon=0$）：$V_{\rm eff}=fL^2/r^2$。

### 7.3 圆轨道与 ISCO

圆轨道：$V_{\rm eff}'=0$。对类时（自检 4）：

$$L^2=\frac{G_NM r^2}{r-3G_NM},\qquad r\gt3G_NM .$$

$r=3G_NM$ 是**光子球**（类光圆轨道）；$r\lt3G_NM$ 没有圆轨道。

**ISCO**（最内稳定圆轨道）：$L^2(r)$ 的极小值（稳定性的边缘），

$$\frac{\mathrm{d}}{\mathrm{d}r}\left(\frac{r^2}{r-3G_NM}\right)=0
\;\Longrightarrow\;\frac{r^2-6G_NMr}{(r-3G_NM)^2}=0
\;\Longrightarrow\;\boxed{r_{\rm ISCO}=6G_NM .}$$

**数值**：对 Schwarzschild 黑洞，ISCO 处的**局部**轨道速度（相对静止观测者）是

$$v=\frac{r\Omega}{\sqrt f}\bigg|_{r=6G_NM}=\frac{\sqrt{1/6}}{\sqrt{1-1/3}}=\frac12,$$

即**半个光速**；引力红移因子 $\sqrt{f}=\sqrt{2/3}\approx0.816$。这些是吸积盘物理的基准数。（若误用 $v=\sqrt{m/r}$ 会得到 $0.408$，那是"坐标速度"，不是局部速度。）

### 7.4 光线偏折

类光测地线。用 $u=1/r$ 与 $L=bE$（$b$ 是碰撞参数）：

$$\boxed{\;\frac{\mathrm{d}^2u}{\mathrm{d}\phi^2}+u=3G_NMu^2\;}$$

零阶（直线）：$u_0=\sin\phi/b$。一阶修正给（自检 5）

$$\boxed{\;\Delta\phi=\frac{4G_NM}{b}\;}$$

**数值检验**：太阳的 $2G_NM_\odot/c^2\approx2.95$ km，$b=R_\odot\approx6.96\times10^5$ km，偏折 $\approx1.75''$——1919 年 Eddington 观测到的正是这个量级。

### 7.5 近日点进动

类时轨道的一阶修正给

$$\Delta\phi_{\rm peri}=\frac{6\pi G_NM}{a(1-e^2)}$$

每圈。水星：$a=5.79\times10^7$ km、$e=0.2056$，给 $\approx43''/$世纪——与观测（扣除行星摄动后）一致。

**这两个检验的共同结构**：都是把 Newton 结果作为零阶、把 $G_NM u$ 作为一阶修正，而修正项的来源是"$1/r$ 势外加一个相对论修正"。第 3 章 §6 的潮汐张量与此同源。

## 8. 黑洞热力学（预告）

$$r_h=2G_NM,\qquad A=4\pi r_h^2=16\pi G_N^2M^2 .$$

**表面重力**：

$$\kappa=\frac{f'(r_h)}{2}=\frac{1}{4G_NM}.$$

（$\kappa$ 的定义与第 8 章的"非仿射度"一致：$\xi^b\nabla_b\xi^a=\kappa\xi^a$，$\xi=\partial_t$ 在视界上。）

**Hawking 温度**：

$$T_{\rm H}=\frac{\kappa}{2\pi}=\frac{1}{8\pi G_NM}\qquad(\hbar=1).$$

**Bekenstein–Hawking 熵**：

$$S_{\rm BH}=\frac{A}{4G_N}=4\pi G_NM^2 .$$

**三条一致性检验**：

1. **热力学第一定律**：$\mathrm{d}M=T\mathrm{d}S$。验证：$\mathrm{d}S=8\pi G_NM\,\mathrm{d}M$，$T\mathrm{d}S=\frac{1}{8\pi G_NM}\cdot8\pi G_NM\,\mathrm{d}M=\mathrm{d}M$ ✓。
2. **Wald 熵**（第 12 章）：$S=2\pi\oint Q_\xi=\frac{A}{4G_N}$ ✓。
3. **论文的权重**（[QFT 书第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)）：$e^{-2\pi K}=e^{-A/4G_N\hbar}$，指数正是 $S_{\rm BH}$。

**MOTS 检验**：在 $r=2G_NM$ 的球面上，出射零法矢的膨胀 $\Theta_{(\ell)}=0$（因为面积沿生成元不变），入射的 $\Theta_{(n)}\lt0$（面积向内收缩）——正是第 7、8 章定义的边缘陷俘面。**所以 Schwarzschild 视界是 MOTS 的原型**，也是论文 (5.51) 的检验案例。

## 9. 与论文的接口

| 论文位置 | Schwarzschild 提供什么 |
|---|---|
| §5.3 对数修正 | 大黑洞背景：$A=16\pi G_N^2M^2$、固定质量对 $M$ 的换变量 |
| (5.51) MOTS | 视界是 $\Theta_{(\ell)}=0$、$\Theta_{(n)}\lt0$ 的原型 |
| §5.2 面积谱 | 面积算符的经典值 $A$、步长 $8\pi G_N\hbar$ 的相对大小 |
| App D 单圈 | $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ 与热核系数 $a_2$ 的背景 |
| §6 半经典 | 弱场极限回到 $\nabla^2\Phi=4\pi G_N\rho$（第 5 章） |

**一句话**：论文在 §5.3 做的是"在 Schwarzschild 背景上数状态、算熵"，所以这一章是它的"经典底图"。

## 10. 小结

- 球对称真空解唯一（Birkhoff）：Schwarzschild；解只用了"球对称 + 真空"，静态性是推论。
- $r=2G_NM$ 是坐标奇异（Kretschmann 有限，$48G_N^2M^2/r^6$）；$r=0$ 是真奇异。
- Kruskal 延拓把视界变成光滑零超曲面，四个区域：两个外部 + 黑洞 + 白洞。
- 两个 Killing 矢量给 $E$、$L$；有效势 $V_{\rm eff}=f(\epsilon+L^2/r^2)$。
- 光子球 $r=3G_NM$；ISCO $r=6G_NM$；光线偏折 $4G_NM/b$；近日点进动 $6\pi G_NM/[a(1-e^2)]$。
- 视界面积 $A=16\pi G_N^2M^2$、$\kappa=1/(4G_NM)$、$T=1/(8\pi G_NM)$、$S=A/4G_N$；第一定律 $\mathrm{d}M=T\mathrm{d}S$ 自洽。
- 视界是 MOTS 的原型；论文的熵与面积谱都以它为经典基准。

## 自检问题

**1.** 用球对称 ansatz 与 $R_{\mu\nu}=0$ 解出 Schwarzschild，写清"$\alpha'+\beta'=0$"与"$re^{2\alpha}=r-2G_NM$"两步。

<details markdown="1"><summary>点击显示答案</summary>

**ansatz**：$\mathrm{d}s^2=-e^{2\alpha}\mathrm{d}t^2+e^{2\beta}\mathrm{d}r^2+r^2\mathrm{d}\Omega^2$。

**第一步：列 $R_{tt}$、$R_{rr}$。** 由 Christoffel 符号（正文 §3）与

$$R_{\mu\nu}=\partial_\rho\Gamma^\rho{}_{\mu\nu}-\partial_\nu\Gamma^\rho{}_{\rho\mu}+\Gamma^\rho{}_{\rho\lambda}\Gamma^\lambda{}_{\mu\nu}-\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\rho\mu}$$

逐项算，得

$$R_{tt}=e^{2(\alpha-\beta)}\left(\alpha''+\alpha'^2-\alpha'\beta'+\frac{2\alpha'}{r}\right),$$
$$R_{rr}=-\left(\alpha''+\alpha'^2-\alpha'\beta'-\frac{2\beta'}{r}\right).$$

**第二步：$R_{tt}=0$ 与 $R_{rr}=0$ 组合。** 把 $R_{tt}$ 除以 $e^{2(\alpha-\beta)}$，与 $R_{rr}$ 相加：

$$\left(\alpha''+\alpha'^2-\alpha'\beta'+\frac{2\alpha'}{r}\right)-\left(\alpha''+\alpha'^2-\alpha'\beta'-\frac{2\beta'}{r}\right)=0$$

$$\Longrightarrow\;\frac{2}{r}\left(\alpha'+\beta'\right)=0\;\Longrightarrow\;\alpha'+\beta'=0 .$$

积分：$\alpha+\beta=C$。重定义 $t\to e^{C}t$ 可令 $C=0$，即 $\beta=-\alpha$。$\square$

**第三步：$R_{\theta\theta}=0$。** 代入 $\beta=-\alpha$：

$$R_{\theta\theta}=e^{2\alpha}\left(1+r\alpha'-r(-\alpha')\right)-1=e^{2\alpha}\left(1+2r\alpha'\right)-1=0 .$$

即 $e^{2\alpha}(1+2r\alpha')=1$。注意

$$\frac{\mathrm{d}}{\mathrm{d}r}\left(r\,e^{2\alpha}\right)=e^{2\alpha}+2r\alpha'e^{2\alpha}=e^{2\alpha}\left(1+2r\alpha'\right)=1 .$$

积分：

$$r\,e^{2\alpha}=r+C .$$

**第四步：定 $C$。** 设 $C=-2G_NM=-2m$：

$$e^{2\alpha}=1-\frac{2m}{r},\qquad e^{2\beta}=\frac{1}{1-2m/r}.$$

大 $r$ 与弱场 $g_{00}=-(1+2\Phi)$、$\Phi=-G_NM/r$ 对照，确认 $C=-2G_NM$ ✓。$\square$

**第五步：检验。** 把解代回 $R_{\theta\theta}$：

$$e^{2\alpha}(1+2r\alpha')=\left(1-\frac{2m}{r}\right)\left(1+2r\cdot\frac{2m/r^2}{2(1-2m/r)}\right)
=\left(1-\frac{2m}{r}\right)+\frac{2m}{r}=1\;\checkmark .$$

**要点**：整个推导只用了两个方程（$R_{tt}=R_{rr}=0$ 与 $R_{\theta\theta}=0$），$R_{\phi\phi}=0$ 自动满足（球对称）。**两个未知函数、两个独立方程，唯一解。**

</details>

**2.** 验证 Schwarzschild 的 $R_{\hat t\hat r\hat t\hat r}=-2G_NM/r^3$ 等正交归一分量，并算出 Kretschmann 标量 $48G_N^2M^2/r^6$。

<details markdown="1"><summary>点击显示答案</summary>

**正交归一标架**：$\hat e^{\hat t}=f^{1/2}\mathrm{d}t$、$\hat e^{\hat r}=f^{-1/2}\mathrm{d}r$、$\hat e^{\hat\theta}=r\,\mathrm{d}\theta$、$\hat e^{\hat\phi}=r\sin\theta\,\mathrm{d}\phi$。

**独立分量**（Schwarzschild 的曲率只有 6 个独立分量，都是 $m/r^3$ 的量级）：

$$R_{\hat t\hat r\hat t\hat r}=-\frac{2m}{r^3},\qquad
R_{\hat t\hat\theta\hat t\hat\theta}=R_{\hat t\hat\phi\hat t\hat\phi}=\frac{m}{r^3},$$
$$R_{\hat r\hat\theta\hat r\hat\theta}=R_{\hat r\hat\phi\hat r\hat\phi}=-\frac{m}{r^3},\qquad
R_{\hat\theta\hat\phi\hat\theta\hat\phi}=\frac{2m}{r^3}.$$

**验证其中一个：$R_{\hat t\hat r\hat t\hat r}=-2m/r^3$。**

正交归一标架：$\hat e^{\hat t}=f^{1/2}\mathrm{d}t$、$\hat e^{\hat r}=f^{-1/2}\mathrm{d}r$。所以

$$R_{\hat t\hat r\hat t\hat r}=e_{\hat t}{}^t e_{\hat r}{}^r e_{\hat t}{}^t e_{\hat r}{}^r R_{trtr}
=f^{-1/2}f^{1/2}f^{-1/2}f^{1/2}R_{trtr}=R_{trtr}.$$

**算 $R^t{}_{rtr}$**（$\alpha=\frac12\ln f$，$\beta=-\alpha$）：

$$R^t{}_{rtr}=\partial_t\Gamma^t_{rr}-\partial_r\Gamma^t_{tr}+\Gamma^t_{t\lambda}\Gamma^\lambda_{rr}-\Gamma^t_{r\lambda}\Gamma^\lambda_{tr}
=0-\alpha''+\alpha'\beta'-\alpha'^2 .$$

用 $\beta'=-\alpha'$：

$$R^t{}_{rtr}=-\alpha''-\alpha'^2-\alpha'^2=-\left(\alpha''+2\alpha'^2\right).$$

于是

$$R_{trtr}=g_{tt}R^t{}_{rtr}=\left(-e^{2\alpha}\right)\left[-\left(\alpha''+2\alpha'^2\right)\right]
=e^{2\alpha}\left(\alpha''+2\alpha'^2\right).$$

**化简**：$\alpha'=\frac{f'}{2f}$、$\alpha''=\frac{f''}{2f}-\frac{f'^2}{2f^2}$，故

$$\alpha''+2\alpha'^2=\frac{f''}{2f}-\frac{f'^2}{2f^2}+2\cdot\frac{f'^2}{4f^2}=\frac{f''}{2f}.$$

所以

$$R_{trtr}=e^{2\alpha}\cdot\frac{f''}{2f}=f\cdot\frac{f''}{2f}=\frac{f''}{2}
=-\frac{2m}{r^3}\quad\left(f''=-\frac{4m}{r^3}\right).\qquad\square$$

**其余分量**同法可得（或由球对称与 $R_{\mu\nu}=0$ 的代数关系推出）：

**Kretschmann**：

$$R_{\hat a\hat b\hat c\hat d}R^{\hat a\hat b\hat c\hat d}
=4\left[\left(-\frac{2m}{r^3}\right)^2+2\left(\frac{m}{r^3}\right)^2+2\left(-\frac{m}{r^3}\right)^2+\left(\frac{2m}{r^3}\right)^2\right]$$

$$=4\cdot\frac{m^2}{r^6}\left[4+2+2+4\right]=\frac{48m^2}{r^6}.$$

（前面的因子 4：每个独立分量在 $R_{abcd}R^{abcd}$ 里出现 4 次，来自 $ab$ 的两种次序与 $cd$ 的两种次序。）$\square$

**两个读数**：

- $r=2m$：$R^2_{\rm K}=48m^2/(16m^4)=3/m^4$，有限 ⇒ 视界不是曲率奇异。
- $r\to0$：发散 ⇒ 真奇异。
- 大 $r$：$\sim m^2/r^6$ ⇒ 曲率按 $1/r^3$ 衰减（潮汐），比 $1/r^2$（Newton 势的梯度）更快。

**为什么这个判据可信**：$R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ 是标量（所有指标缩并），换坐标不变。所以"在某坐标里有限"就是"几何上有限"。这是第 2 章 §7 判据清单的第 3 条。

</details>

**3.** 从 $U=-e^{-u/(4G_NM)}$、$V=e^{v/(4G_NM)}$ 出发，验证 Kruskal 度规的形式，并说明 $r=2G_NM$ 处为什么正则。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：$du\,dv$ 与 $dU\,dV$ 的关系。**

$$u=t-r_*,\quad v=t+r_*\;\Longrightarrow\;\mathrm{d}u\,\mathrm{d}v=\mathrm{d}t^2-\mathrm{d}r_*^2 .$$

$$U=-e^{-u/(4m)},\ V=e^{v/(4m)}\;\Longrightarrow\;
\mathrm{d}U=\frac{1}{4m}e^{-u/(4m)}\mathrm{d}u,\quad
\mathrm{d}V=\frac{1}{4m}e^{v/(4m)}\mathrm{d}v .$$

$$\mathrm{d}U\,\mathrm{d}V=\frac{1}{16m^2}e^{(v-u)/(4m)}\mathrm{d}u\,\mathrm{d}v
=\frac{1}{16m^2}e^{r_*/(2m)}\mathrm{d}u\,\mathrm{d}v .$$

**第二步：Schwarzschild 的 $\mathrm{d}t^2-\mathrm{d}r_*^2$。**

$$\mathrm{d}s^2=-f\,\mathrm{d}t^2+\frac{\mathrm{d}r^2}{f}+r^2\mathrm{d}\Omega^2
=-f\left(\mathrm{d}t^2-\frac{\mathrm{d}r^2}{f^2}\right)+r^2\mathrm{d}\Omega^2
=-f\left(\mathrm{d}t^2-\mathrm{d}r_*^2\right)+r^2\mathrm{d}\Omega^2 .$$

**第三步：合并。**

$$\mathrm{d}s^2=-f\cdot16m^2e^{-r_*/(2m)}\mathrm{d}U\,\mathrm{d}V+r^2\mathrm{d}\Omega^2 .$$

用 $r_*/(2m)=r/(2m)+\ln|r/(2m)-1|$：

$$e^{-r_*/(2m)}=\frac{e^{-r/(2m)}}{|r/(2m)-1|}=\frac{2me^{-r/(2m)}}{|r-2m|},$$

而 $f=(r-2m)/r$。对 $r\gt2m$：

$$f\,e^{-r_*/(2m)}=\frac{r-2m}{r}\cdot\frac{2me^{-r/(2m)}}{r-2m}=\frac{2m}{r}e^{-r/(2m)} .$$

所以

$$\boxed{\;\mathrm{d}s^2=-\frac{32m^3}{r}e^{-r/(2m)}\mathrm{d}U\,\mathrm{d}V+r^2\mathrm{d}\Omega^2\;}$$

（$m=G_NM$ 时前因子是 $32G_N^3M^3$）。$\square$

**第四步：$r=2m$ 处的正则性。**

$UV=-e^{(v-u)/(4m)}=-e^{r_*/(2m)}$。在 $r=2m$：$r_*=r+2m\ln|r/2m-1|\to-\infty$ ⇒ $e^{r_*/(2m)}\to e^{r/(2m)}\cdot|r/2m-1|\to0$。所以

$$r=2m\iff UV=0\iff U=0\ \text{或}\ V=0 .$$

**$U=0$ 或 $V=0$ 是光滑的零超曲面**（不是奇点）。前置因子

$$\frac{32m^3}{r}e^{-r/(2m)}\bigg|_{r=2m}=\frac{32m^3}{2m}e^{-1}=16m^2e^{-1},$$

有限且非零 ⇒ 度规在视界处非退化（$\det g\propto U V$ 的坐标里，$UV=0$ 只是"该坐标的一半退化"，几何上没有）。

**第五步：$r=0$ 是真奇异。** $UV=1$ 是双曲线，$r=0$ 对应它；曲率 $48m^2/r^6\to\infty$。$\square$

**三个可检验的读数**：

1. **$t\to\infty$ 对应什么**：$U\to0^-$（$V$ 有限）。所以"$t=\infty$"不是几何边界，只是 $U=0$ 这条视界。
2. **$U$ 与 $V$ 都是零坐标**：$\partial_U$、$\partial_V$ 是零矢量，所以 $U,V$ 是"双零坐标"——第 8 章的双零片语言在这里第一次出现。
3. **最大延拓**：Kruskal 是 Schwarzschild 的**最大解析延拓**（在球对称假设下）。它不可再延拓（$r=0$ 与 $\mathscr{I}$ 是边界），这由测地线完备性判定。

</details>

**4.** 从有效势 $V_{\rm eff}=f(1+L^2/r^2)$ 推出圆轨道的 $L^2(r)$，再求 ISCO 半径，并算 ISCO 处的轨道速度与红移因子。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：$V_{\rm eff}'=0$。**

$$V_{\rm eff}=f\left(1+\frac{L^2}{r^2}\right),\qquad
V_{\rm eff}'=f'\left(1+\frac{L^2}{r^2}\right)+f\left(-\frac{2L^2}{r^3}\right)=0 .$$

$f=1-2m/r$，$f'=2m/r^2$：

$$\frac{2m}{r^2}\left(1+\frac{L^2}{r^2}\right)-\left(1-\frac{2m}{r}\right)\frac{2L^2}{r^3}=0 .$$

两边乘 $r^3/2$：

$$mr\left(1+\frac{L^2}{r^2}\right)-L^2\left(1-\frac{2m}{r}\right)=0$$

$$mr+\frac{mL^2}{r}-L^2+\frac{2mL^2}{r}=0$$

$$mr-L^2+\frac{3mL^2}{r}=0\;\Longrightarrow\;L^2\left(1-\frac{3m}{r}\right)=mr .$$

所以

$$\boxed{L^2=\frac{mr^2}{r-3m},\qquad r\gt3m .}\qquad\square$$

**第二步：ISCO。** 稳定性要求 $V_{\rm eff}''\gt0$；边缘 $V_{\rm eff}''=0$ 等价于 $L^2(r)$ 的极小（因为 $L$ 随 $r$ 的单调性改变符号处就是稳定性的转折）。算

$$\frac{\mathrm{d}}{\mathrm{d}r}\left(\frac{r^2}{r-3m}\right)
=\frac{2r(r-3m)-r^2}{(r-3m)^2}=\frac{r^2-6mr}{(r-3m)^2} .$$

令其为零：

$$r^2-6mr=0\;\Longrightarrow\;\boxed{r_{\rm ISCO}=6m=6G_NM .}\qquad\square$$

**第三步：ISCO 处的物理量。**

- 局部轨道速度（相对静止观测者）：$v=\frac{r\Omega}{\sqrt f}=\frac{\sqrt{m/r}}{\sqrt{1-2m/r}}\Big|_{r=6m}=\frac12$（$c=1$）。
- 红移因子：$\sqrt{f}=\sqrt{1-2/6}=\sqrt{2/3}\approx0.816$。
- 轨道角频率（坐标时）：$\Omega=\sqrt{m/r^3}=\frac{1}{6\sqrt{6}\,m}$。

**第四步：与光子球对照。** 类光圆轨道：$V_{\rm eff}=fL^2/r^2$，故 $V_{\rm eff}'=0$ 等价于

$$\frac{\mathrm{d}}{\mathrm{d}r}\left(\frac{f}{r^2}\right)=0 .$$

对 $f=1-2m/r$：

$$\frac{f}{r^2}=\frac{1}{r^2}-\frac{2m}{r^3},\qquad
\frac{\mathrm{d}}{\mathrm{d}r}\left(\frac{f}{r^2}\right)=-\frac{2}{r^3}+\frac{6m}{r^4}=0
\;\Longrightarrow\;r=3m .$$

所以光子球 $r=3G_NM$（不稳定圆轨道）。$\square$

**三点读法**：

1. **$3m$ 与 $6m$ 的来历**：$3m$ 来自"$\mathrm{d}(f/r^2)/\mathrm{d}r=0$"（类光），$6m$ 来自"$\mathrm{d}(L^2)/\mathrm{d}r=0$"（类时稳定性的边缘）。两个数不是巧合，它们分别是 $f$ 与 $r^2$ 的"临界平衡"。
2. **ISCO 的物理意义**：吸积盘的内边缘。因为 $r\lt6m$ 没有稳定圆轨道，物质只能螺旋落入——这是 X 射线双星谱的"内边缘" $6G_NM$ 的来源，也是测量黑洞自旋的基准（对 Kerr 会移动）。
3. **$r=3m$ 的光子球**：光可以绕黑洞转圈，形成"光子环"；EHT 的环状图像与此直接相关。

</details>

**5.** 用 $u''+u=3G_NMu^2$ 算光线偏折角 $\Delta\phi=4G_NM/b$。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：类光测地线方程。** 由 $L=bE$、$u=1/r$ 与 $\dot r^2=E^2-fL^2/r^2$，对 $\phi$ 求导得

$$\frac{\mathrm{d}^2u}{\mathrm{d}\phi^2}+u=3G_NMu^2 .$$

**第二步：零阶。** 忽略右边：$u_0''+u_0=0$ ⇒

$$u_0=\frac{\sin\phi}{b}$$

（选 $\phi=0$ 为最近点，$u=1/b$ 是最大）。

**第三步：一阶。** 令 $u=u_0+u_1$，$u_1$ 线性于 $G_NM$：

$$u_1''+u_1=3G_NMu_0^2=\frac{3G_NM}{b^2}\sin^2\phi=\frac{3G_NM}{2b^2}\left(1-\cos2\phi\right).$$

试解 $u_1=A+B\cos2\phi$：

$$u_1''+u_1=A-3B\cos2\phi .$$

匹配：

$$A=\frac{3G_NM}{2b^2},\qquad -3B=-\frac{3G_NM}{2b^2}\;\Longrightarrow\;B=\frac{G_NM}{2b^2}.$$

所以

$$u_1=\frac{G_NM}{2b^2}\left(3+\cos2\phi\right).$$

**第四步：定偏折。** 总解

$$u=\frac{\sin\phi}{b}+\frac{G_NM}{2b^2}\left(3+\cos2\phi\right).$$

光子从 $u=0$ 来、到 $u=0$ 去。在 $\phi\to0^+$（出射方向附近），令 $u=0$：

$$0=\frac{\phi}{b}+\frac{G_NM}{2b^2}\left(3+1\right)=\frac{\phi}{b}+\frac{2G_NM}{b^2}
\;\Longrightarrow\;\phi=-\frac{2G_NM}{b}.$$

由对称性，入射侧同样偏 $\frac{2G_NM}{b}$，两者之和为

$$\boxed{\Delta\phi=\frac{4G_NM}{b}.}\qquad\square$$

**第五步：数值与检验。**

- 太阳：$2G_NM_\odot/c^2=2.95$ km、$b=R_\odot=6.96\times10^5$ km ⇒ $\Delta\phi=8.5\times10^{-6}$ rad $=1.75''$。
- Eddington 1919：在日全食时测星光偏折，量级吻合（现代射电观测精确到 $10^{-4}$）。
- 与"Newton 粒子"对照：把光子当以 $c$ 运动的粒子，Newton 引力给的偏折是 $2G_NM/b$——**正好一半**。所以"偏折角是 Newton 的两倍"是广义相对论的经典判据。

**一个容易忽略的细节**：$u_1$ 的常数项 $\frac{3G_NM}{2b^2}$ 必须保留。它在小 $\phi$ 处给 $u$ 一个常量偏移 $\frac{2G_NM}{b^2}$，正是这个偏移把两个渐近方向不对称地推开了 $\frac{2G_NM}{b}$。若只留 $\cos2\phi$ 项，会得到 $\Delta\phi=G_NM/b$——只有正确值的四分之一，**比 Newton 值 $2G_NM/b$ 还小一半**，这是最常见的符号/常数错误。

**检验办法**：算 $\Delta\phi=\phi_{\rm out}-\phi_{\rm in}$ 时，两端都要用同一个解 $u(\phi)$ 求 $u=0$ 的根，不能凭对称性只算一边再乘 2 而丢掉常数项。

</details>

## 参考

- Wald《General Relativity》第 6 章（Schwarzschild、Birkhoff、Kruskal、测地线、光线偏折、近日点进动）、第 12 章（表面重力）。
- Carroll《Spacetime and Geometry》第 5 章（Schwarzschild 与 Kruskal 图）、第 6 章（测地线与经典检验）。
- Misner, Thorne & Wheeler《Gravitation》第 31–33 章（Schwarzschild 几何的详细图像、ISCO、吸积盘）。
- Poisson《A Relativist's Toolkit》第 9 章（黑洞与视界的局域定义）。
- [QFT 书第 9 阶段 03 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/03-jt-gravity-gravitational-clock.md)（JT 引力的 Schwarzschild 类比）、[04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)（论文的熵计算以 Schwarzschild 为背景）；第 7 章（因果结构与 Penrose 图）、第 8 章（视界作为零超曲面）、第 13 章（黑洞热力学）。
