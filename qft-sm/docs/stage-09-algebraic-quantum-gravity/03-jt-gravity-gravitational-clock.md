# JT 引力与引力时钟：二维的完整演练

> 路线图位置：第 9 阶段（代数量子引力专题）· 第 3 篇
> 前置知识：第 9 阶段 01 篇（弯曲时空 QFT 与热态）、02 篇（GNS 与型分类）；第 4 阶段的路径积分与辛形式；广义相对论书第 6、8 章（Schwarzschild、零超曲面）尚未写出时，可先接受 AdS₂ 与零坐标的表述。
> 学习目标：写出 JT 作用量并解出 dilaton 与几何；会在二维因果菱形上定义引力时钟并算出 $u_*(w)$；能复现"固定角点 dilaton 仍有无限多正交态"与 type $I_\infty$、迹发散；理解它与四维纲领的差别（剪切）和共同点（时钟、角点荷、粘合）。

---

**单位约定**：本篇取自然单位 $\hbar = c = 1$（首次说明）；二维度规号差沿用本书 $(+,-)$；AdS 半径记 $L$。

## 1. 一句话总结

**JT 引力是"dilaton + AdS₂"：约束把几何锁死，只留 dilaton 与物质；在有限因果菱形上，零生成元的仿射参数定义引力时钟，dilaton 在角点处生成 boost。固定角点 dilaton 与物质态后，时钟波函数的相位仍给出无限多正交态——代数 type $I_\infty$、迹发散、没有密度矩阵。这是四维纲领必须跨过的第一课：在二维，时钟与面积无关；在四维，剪切把两者绑在一起。**

## 2. JT 引力

### 2.1 作用量

二维 dilaton 引力（Jackiw–Teitelboim）的作用量：

$$I = \frac{1}{16\pi G}\int_D\mathrm{d}^2x\sqrt{-g}\;\Phi\left(R + \frac{2}{L^2}\right) + I_{\partial D} + I_{\mathrm{matter}},$$

$\Phi$ 是 dilaton（在二维没有传播自由度，是拉格朗日乘子式的场），$L$ 是 AdS₂ 半径。一阶形式（论文 (2.2)）把自旋联络与标架独立变分：

$$I[e,\omega,Y,\Phi,\varphi] = \int_D\left[Y_\mu T^\mu + \Phi\left(\mathrm{d}\omega^{01} + L^{-2}\epsilon_g\right) - \frac12\mathrm{d}\varphi\wedge\star\mathrm{d}\varphi\right] + I_{\partial D},$$

$Y_\mu$ 是拉格朗日乘子，变分它强制挠率为零 $T^\mu = 0$，从而把自旋联络锁定为标架的 Levi-Civita 联络。

### 2.2 运动方程

变分 $\Phi$：曲率固定，

$$R = -\frac{2}{L^2}.$$

变分 $g^{ab}$：二维恒等式 $R_{ab} - \frac12g_{ab}R \equiv 0$ 使 Einstein 张量自动为零，剩下的方程全来自 $\Phi R$ 的分部积分：

$$\left(\nabla_a\nabla_b - g_{ab}\nabla^2\right)\Phi + \frac{1}{L^2}g_{ab}\Phi = \frac12 T_{ab},$$

$T_{ab}$ 是物质能动张量。取迹并用 $R = -2/L^2$ 化简，得到 dilaton 的"波动方程"；取零分量则得到**零约束**（自检 1）：

$$\partial_u^2\Phi = -\left(\partial_u\varphi\right)^2,$$

其中 $u$ 是沿零生成元的仿射参数，且已把 $16\pi G$ 吸收进 $\Phi$（与论文的归一化一致）。

### 2.3 全局坐标

AdS₂ 的全局坐标：

$$\mathrm{d}s^2 = L^2\sec^2\sigma\left(-\mathrm{d}\tau^2 + \mathrm{d}\sigma^2\right),\qquad \sigma\in\left(-\frac{\pi}{2},\frac{\pi}{2}\right).$$

$\sigma = \pm\pi/2$ 是 AdS 边界。无物质时 dilaton 的解为

$$\Phi = \Phi_0\,\frac{\cos\tau}{\cos\sigma},$$

它满足 $(\nabla_a\nabla_b - g_{ab}\nabla^2)\Phi + L^{-2}g_{ab}\Phi = 0$（自检 1 验证）。

### 2.4 因果菱形与角点

取两个角点之间的一条类空测地线 $\Sigma$（长度 $w$），以及从过去/未来尖端出发的两族零生成元；在 $\Sigma$ 两端截出角点 $S_{L,R}$。菱形的边界是两片零锥 $H_p\cup H_q$ 加两个小盖 $\Sigma_0,\Sigma_1$。在角点 $S_i$ 处，dilaton 的值 $\Phi(S_i)$ 就是该角点的 boost 荷（§4.2）。

## 3. 引力时钟

### 3.1 定义

**引力时钟**：沿入射零生成元，从盖 $\Sigma_0$ 走到角点 $S$ 的仿射参数（在 $\Sigma_0$ 上把切矢在局部 Lorentz 标架里归一化，并令 $u=0$ 于 $\Sigma_0$）。它只依赖几何，不依赖任何外部时钟。

### 3.2 显式计算

沿右侧零生成元，取 $\tau = \sigma$（出射方向）。设 $\Sigma_0$ 位于 $\lambda = \lambda_c = \epsilon w/2$（$\epsilon \ll 1$），角点在 $\lambda = w/2$。由

$$\lambda(\sigma) = L\int_0^\sigma\sec s\,\mathrm{d}s = L\ln\left(\sec\sigma + \tan\sigma\right),\qquad u(\sigma) = L\tan\sigma,$$

得

$$u_* (w) = \left(\partial_u\lambda\right)_{\Sigma_0}\left[u(w/2) - u(\lambda_c)\right] = L\,\frac{\sinh\frac{w}{2L} - \sinh\frac{\lambda_c}{L}}{\cosh\frac{\lambda_c}{L}}.$$

（推导见自检 2。）单调性：$u_*$ 随 $w$ 严格递增，故时钟是"好时钟"；小 $w$ 极限 $u_* \simeq (1-\epsilon)w/2$，就是"从盖到角点的固有时"。

### 3.3 物质冲击

把物质按 $\partial_u^2\Phi = -(\partial_u\varphi)^2$ 积分两次，取尖端正则条件 $\partial_u\Phi(0) = 0$：

$$\Delta\Phi(u_*) = -\int_0^{u_*}(u_* - u)\left(\partial_u\varphi\right)^2\mathrm{d}u.$$

于是**同样的 $u_*$、不同的物质分布**给出不同的角点 dilaton——物质可以改变角点的 boost 荷，却不改变时钟读数。这正是"给定时钟读数后，仍有大量物质态"的精确含义。

## 4. 约化相空间与量子化

### 4.1 辛势与括号

把 $\theta_M = Y_\mu\delta e^\mu + \Phi\,\delta\omega^{01} - (\star\mathrm{d}\varphi)\delta\varphi$ 沿边界积分，得到（论文 (2.7)）

$$\Theta = p_{u_*}\,\delta u_* + \sum_{i=L,R}\int_\epsilon^1\left(\partial_v\varphi_i\right)\delta\varphi_i\,\mathrm{d}v + \int_{\Sigma_0}\pi_\varphi\,\delta\varphi_0\,\mathrm{d}x + \sum_{i=L,R}K_i\,\delta\Gamma_i,$$

四项分别是：时钟动量、两条零生成元上的标量剖面、盖上的场与动量、两个角点的 boost 荷（$K_i = \Phi(S_i)$）与快度。相空间就是这样"时钟 $\times$ 两个剖面 $\times$ 盖场 $\times$ 角点荷"的直积。

### 4.2 角点 dilaton 生成 boost

辛形式 $\Omega = \delta\Theta$ 中 $K_i = \Phi(S_i)$ 与快度 $\Gamma_i$ 共轭：

$$\{K_i,\Gamma_j\} = \delta_{ij}.$$

所以角点 dilaton 就是该角点的 boost 生成元——二维版本的一般相对论事实："解掉约束后，哈密顿量只剩边界（角点）项"（论文 §3.4；GR 书第 12 章）。

### 4.3 Hilbert 空间

在固定角点荷 $K_{L,R}$ 的子空间上：

- 时钟：$u_*$ 取值在 $\mathbb R_+$，波函数属于 $L^2(\mathbb R_+,\mathrm{d}u_*)$；
- 物质：两条零生成元上的剖面 $\varphi_i(v)$ 与盖上的 $(\varphi_0,\pi_\varphi)$ 组成 Fock 空间 $\mathcal H_\varphi$；
- 总空间 $\mathcal H_\Sigma = L^2(\mathbb R_+,\mathrm{d}u_*)\otimes\mathcal H_\varphi$；投影到"时钟读数不超过 $\ell(D)$"：

$$\mathcal H_D = P_D\,\mathcal H_\Sigma,\qquad P_D = \mathbf 1_{[0,\ell(D)]}(\hat u_*).$$

### 4.4 无限多正交态

固定角点荷与一个归一化物质态 $|\xi\rangle$，取任意归一化平滑时钟波函数 $h(u_*)$（支撑在 $(0,\ell(D))$），定义

$$\Psi_n(u_*) = h(u_*)\,e^{2\pi i n F(u_*)},\qquad F(u_*) = \int_0^{u_*}\lvert h(v)\rvert^2\,\mathrm{d}v,\qquad n\in\mathbb Z.$$

则

$$\langle\Psi_m|\Psi_n\rangle = \int_0^{\ell(D)}h^*h\,e^{2\pi i(n-m)F(u_*)}\,\mathrm{d}u_* = \int_0^1 e^{2\pi i(n-m)s}\,\mathrm{d}s = \delta_{mn},$$

（换元 $s = F(u_*)$，注意 $F(\ell(D)) = 1$、$\mathrm{d}s = |h|^2\mathrm{d}u_*$）。**无限多个正交态，全部有相同的时钟概率分布 $|h|^2$、相同的角点荷、相同的物质态**——它们只差相位随 $u_*$ 的缠绕方式。

观测上可以区分：$u_*p_{u_*}$ 的对称化生成元 $\hat Q = -\mathrm{i}\hbar(u_*\partial_{u_*} + \tfrac12)$ 的期望值差为 $2\pi n\hbar\int u_*|h|^4\mathrm{d}u_*$（论文 (2.15)）。于是这些态线性无关，$\mathcal H_D$ 无限维。

### 4.5 代数：type $I_\infty$

$u_*$ 的有界函数、dilations、以及剖面的涂抹算符在弱闭包下生成全部有界算符：

$$\pi_\omega(\mathcal A)'' = B(\mathcal H_D),$$

是 **$I_\infty$ 型因子**（第 2 篇的型分类）。有限 $G_N$ 下"可观测量 = 一切有界算符"——但 Hilbert 空间还是无限维的。

## 5. 迹与热权重

### 5.1 粘合与时间反射

把因果菱形的未来半部与它的时间反射沿 $\Sigma_1$ 粘合：$W = C_D^\dagger C_D$。时间演化 $U$ 与 $U^\dagger$ 相消（幺正性），只剩角点处 boost 的贡献。把 boost 快度解析延拓到 $\eta = \mathrm{i}\pi$（半圈旋转），每个角点的权重是

$$e^{-\pi K_i/\hbar},\qquad K_i = \Phi(S_i).$$

两个角点合起来：$e^{-2\pi(K_L+K_R)/\hbar}$。

### 5.2 迹发散

$$W = C_D^\dagger C_D,\qquad \langle\Psi_m|W|\Psi_n\rangle = e^{-2\pi(K_L+K_R)/\hbar}\,\delta_{mn}.$$

取前 $N$ 个正交态：

$$\operatorname{Tr}_{\mathcal H_D}W \ge \sum_{n=1}^N\langle\Psi_n|W|\Psi_n\rangle = N\,e^{-2\pi(K_L+K_R)/\hbar}\ \xrightarrow{N\to\infty}\ \infty.$$

所以 $W/\operatorname{Tr}W$ 不能定义密度矩阵——**$I_\infty$ 的"热态"没有归一化**。对比四维：正是"有限维"把 $Z_{D,1} = \operatorname{Tr}e^{-\hat A/4G}$ 变成有限数，从而熵可算（第 4 篇）。

### 5.3 与热态/KMS 的关系

boost 权重 $e^{-2\pi K/\hbar}$ 与热权重 $e^{-\beta H}$ 是同一件事：把 boost 看作"Rindler 时间"的哈密顿量，角点 dilaton 是它的生成元，$2\pi$ 来自欧氏几何的周期性（第 1 篇的 Unruh 论证）。所以：

- JT 的"迹权重"= Unruh/Hawking 热权重在二维的精确版本；
- 若迹有限，$W/\operatorname{Tr}W$ 满足 KMS 条件（第 2 篇 §3.1）；
- 这里迹发散，KMS 只能作为"形式上的权重"存在——这暴露了二维模型的病：**无限多的零能模**。

## 6. 与四维纲领的对照

### 6.1 共同点

| 结构 | JT（二维） | 四维 |
|---|---|---|
| 引力时钟 | 零生成元的仿射参数 | 同左，且依赖剪切 |
| 角点荷 | $\Phi(S)$ 生成 boost | $A/8\pi G$ 生成 boost |
| 粘合 | 时间反射 + 解析延拓 | 同左 |
| 迹权重 | $e^{-2\pi\Phi(S)/\hbar}$ | $e^{-A/4G\hbar}$ |
| 代数 | $I_\infty$（迹发散） | $I$ 型，时钟投影后有限维 |

### 6.2 差别：剪切的角色

JT 的时钟只依赖测地线长度（$u_*$ 是 $w$ 的函数），与角点面积/荷无关。于是：

- 任意物质态都能配同一个时钟波函数 $\Rightarrow$ 固定时钟读数不限制物质 $\Rightarrow$ 无限多正交态；
- 没有"聚焦"机制把时钟与面积绑在一起。

四维则不同：剪切通过 Raychaudhuri 方程使测地线汇聚，同样的初始面积元在角点处需要更长的仿射参数（论文 (3.26)–(3.27)）。因此**限制时钟读数同时限制了辐射**，这正是四维有限维证明的物理内核（论文 §5.2）。

### 6.3 教训清单

1. 引力时钟与角点荷是"背景独立"语言的正确起点；
2. "解约束 → 约化相空间 → 辛形式 → 量子化"这条管线在二维走得通；
3. 纯态 + Fock 表示给 $I$ 型，但**维数**才是熵能否定义的关键；
4. 二维的病（无限零能模）在四维被剪切治好——这是四维论文最值得记住的物理。

## 7. 小结

- JT 引力：$S = \frac{1}{16\pi G}\int\sqrt{-g}\,\Phi(R+2/L^2)$；运动方程 $R = -2/L^2$ 加 dilaton 方程与零约束 $\partial_u^2\Phi = -(\partial_u\varphi)^2$。
- 引力时钟 $u_*$：沿零生成元的仿射参数，由 (2.4c) 给出；物质冲击 $\Delta\Phi(u_*) = -\int_0^{u_*}(u_*-u)(\partial_u\varphi)^2\mathrm{d}u$ 表明"同一时钟、不同角点荷"。
- 约化相空间：时钟动量 + 两条零剖面 + 盖场 + 角点 boost 荷；$\{K_i,\Gamma_i\} = \delta_{ij}$，$K_i = \Phi(S_i)$。
- 量子化：$L^2(\mathbb R_+)\otimes$ Fock；$\Psi_n = h\,e^{2\pi i nF}$ 无限正交，代数 $I_\infty$；迹权重 $e^{-2\pi K}$，$\operatorname{Tr}W = \infty$，没有密度矩阵。
- 与四维：结构一一对应，唯独"时钟与面积无关"导致无限维；四维靠剪切（Raychaudhuri）把时钟与辐射绑定，才得到有限维与可定义的熵。

## 自检问题

**1.** 从 JT 作用量变分：验证 $R = -2/L^2$，并推出零约束 $\partial_u^2\Phi = -(\partial_u\varphi)^2$。

<details markdown="1"><summary>点击显示答案</summary>

**变分 $\Phi$**：$\delta I/\delta\Phi = 0$ 直接给出

$$R + \frac{2}{L^2} = 0.$$

**变分 $g^{ab}$**：关键事实是二维恒等式 $R_{ab} - \frac12g_{ab}R\equiv 0$，所以 $\Phi R$ 的变分只剩分部积分项：

$$\delta\int\sqrt{-g}\,\Phi R = \int\sqrt{-g}\left[\left(\nabla_a\nabla_b - g_{ab}\nabla^2\right)\Phi\right]\delta g^{ab} + \text{边界项}.$$

加上 $L^{-2}$ 项与物质项：

$$\left(\nabla_a\nabla_b - g_{ab}\nabla^2\right)\Phi + \frac{1}{L^2}g_{ab}\Phi = \frac12T_{ab}.$$

取共形规范 $\mathrm{d}s^2 = -e^{2\omega}\mathrm{d}u\,\mathrm{d}v$（$u,v$ 为零坐标）。此时

$$R = 8e^{-2\omega}\partial_u\partial_v\omega,\qquad T_{uu} = (\partial_u\varphi)^2,\qquad T_{vv} = (\partial_v\varphi)^2.$$

$uu$ 分量的方程（用 $\nabla_u\nabla_u\Phi = \partial_u^2\Phi - 2\partial_u\omega\,\partial_u\Phi$，并注意 $g_{uu} = 0$）：

$$\partial_u^2\Phi - 2\partial_u\omega\,\partial_u\Phi = \frac12 T_{uu} = \frac12(\partial_u\varphi)^2.$$

选仿射参数使 $\partial_u\omega = 0$（在零边界附近总可以），并把 $16\pi G$ 吸收进 $\Phi$ 与 $\varphi$ 的归一化，即得

$$\partial_u^2\Phi = -\left(\partial_u\varphi\right)^2.$$

（符号约定：物质项进入作用量时取正，若取相反的号差习惯则整体变号；物理内容——"剪切式聚焦"——不变。）$\square$

两次积分（自检 2 的方法）给出 $\Delta\Phi(u_*) = -\int_0^{u_*}(u_*-u)(\partial_u\varphi)^2\mathrm{d}u$：物质越多，角点 dilaton 越被压低。

</details>

**2.** 由 $\lambda(\sigma) = L\ln(\sec\sigma+\tan\sigma)$、$u(\sigma) = L\tan\sigma$ 推出 $u_*(w)$ 的表达式，并验证小 $w$ 极限。

<details markdown="1"><summary>点击显示答案</summary>

记 $\Sigma_0$ 在 $\lambda = \lambda_c$、角点在 $\lambda = w/2$。由 $\lambda$ 与 $u$ 的定义：

$$\lambda = L\ln\left(\sec\sigma + \tan\sigma\right) = L\,\mathrm{asinh}\left(\tan\sigma\right),\qquad u = L\tan\sigma.$$

于是 $\tan\sigma = u/L$，$\lambda = L\,\mathrm{asinh}(u/L)$，即

$$u(\lambda) = L\sinh\left(\frac{\lambda}{L}\right).$$

（这正是 (2.4b)。）时钟读数按 (2.4c)：从 $\Sigma_0$ 到角点的仿射参数差，乘上 $\Sigma_0$ 处的归一化因子 $(\partial_u\lambda)|_{\Sigma_0}$：

$$u_* = \left(\partial_u\lambda\right)_{\Sigma_0}\left[u(w/2) - u(\lambda_c)\right] = \frac{L\left[\sinh\frac{w}{2L} - \sinh\frac{\lambda_c}{L}\right]}{\cosh\frac{\lambda_c}{L}}.$$

（用 $\partial_u\lambda = 1/(\partial_\lambda u) = 1/\cosh(\lambda/L)$，在 $\lambda_c$ 处取值。）$\square$

小 $w$ 极限：$\sinh\frac{w}{2L}\approx\frac{w}{2L}$、$\sinh\frac{\lambda_c}{L}\approx\frac{\lambda_c}{L}$、$\cosh\frac{\lambda_c}{L}\approx1$：

$$u_* \approx L\cdot\frac{\frac{w}{2L} - \frac{\lambda_c}{L}}{1} = \frac{w}{2} - \lambda_c = \frac{w}{2}\left(1-\epsilon\right),$$

即"从盖到角点的固有时"的 $(1-\epsilon)$ 倍。单调性：$\mathrm{d}u_*/\mathrm{d}w = \frac{1}{2}\cosh\frac{w}{2L}/\cosh\frac{\lambda_c}{L} \gt 0$，严格递增——好时钟。

</details>

**3.** 证明 $\Psi_n = h\,e^{2\pi i nF}$ 正交归一，并说明 $n$ 的物理意义。

<details markdown="1"><summary>点击显示答案</summary>

内积：

$$\langle\Psi_m|\Psi_n\rangle = \int_0^{\ell(D)}h^*(u_*)e^{-2\pi i mF(u_*)}h(u_*)e^{2\pi i nF(u_*)}\,\mathrm{d}u_*.$$

换元 $s = F(u_*)$：$\mathrm{d}s = |h(u_*)|^2\mathrm{d}u_*$，$F(0) = 0$，$F(\ell(D)) = \int_0^{\ell(D)}|h|^2 = 1$（$h$ 归一化且支撑在区间内）。于是 $h^*h\,\mathrm{d}u_* = \mathrm{d}s$：

$$\langle\Psi_m|\Psi_n\rangle = \int_0^1 e^{2\pi i(n-m)s}\,\mathrm{d}s = \delta_{mn}.$$

$n$ 的物理意义：它标记时钟波函数相位随累积概率 $F$ 的缠绕数。由于 $F$ 是单调映射，$e^{2\pi i nF(u_*)}$ 就是"在 $u_*$ 空间里以 $h$ 的分布为测度、绕 $n$ 圈的相位"。可观测的效应：dilation 生成元 $\hat Q = -\mathrm{i}(u_*\partial_{u_*} + \tfrac12)$ 的期望值随 $n$ 平移 $2\pi n\int u_*|h|^4$——所以不同 $n$ 的态可以被测量区分，$\mathcal H_D$ 至少是无限维的。这正是"时钟读数分布相同、但态不同"的精确版本。

</details>

**4.** 说明解析延拓 $\eta\to\mathrm{i}\pi$ 如何给出权重 $e^{-\pi K/\hbar}$，两个角点为什么给出 $e^{-2\pi K/\hbar}$，并证明 $W$ 的迹发散。

<details markdown="1"><summary>点击显示答案</summary>

boost 由 $K = \Phi(S)$ 生成：$e^{\mathrm{i}\eta K/\hbar}$。解析延拓到 $\eta = \mathrm{i}\pi$：

$$e^{\mathrm{i}(\mathrm{i}\pi)K/\hbar} = e^{-\pi K/\hbar}.$$

这是"半圈欧氏旋转"的权重：把洛伦兹 boost 的半圈（快度 $\mathrm{i}\pi$）变成欧氏旋转的 $\pi$，与 Unruh 论证里的 $2\pi$ 周期同源（两个半圈合成一整圈）。

菱形有两个角点 $S_L,S_R$，每个贡献一个因子，故总权重

$$e^{-\pi K_L/\hbar}\,e^{-\pi K_R/\hbar} = e^{-2\pi(K_L+K_R)/\hbar}.$$

迹：$W = C_D^\dagger C_D$，在 $\{\Psi_n\}$ 上对角，

$$\langle\Psi_m|W|\Psi_n\rangle = e^{-2\pi(K_L+K_R)/\hbar}\,\delta_{mn}.$$

取任意 $N$：

$$\operatorname{Tr}W \ge \sum_{n=1}^{N}\langle\Psi_n|W|\Psi_n\rangle = N\,e^{-2\pi(K_L+K_R)/\hbar}.$$

$K_i = \Phi(S_i)$ 固定且有限，$N\to\infty$ 时右端发散，故 $\operatorname{Tr}W = \infty$。$\square$

物理含义：$I_\infty$ 型代数的"热态"没有归一化密度矩阵；若强行归一化，$W/\operatorname{Tr}W$ 不是一个良定义的态。这是二维 JT 的病，也是四维必须证明"有限维"的动机。

</details>

**5.** 用"$I_\infty$"与"有限维 $I_d$"对比，说明为什么"$\operatorname{Tr}W$ 有限"是熵可定义的关键；并写出有限维情形下的配分函数与熵。

<details markdown="1"><summary>点击显示答案</summary>

**$I_\infty$（JT）**：$\mathcal H_D$ 无限维，$\operatorname{Tr}W = \sum_{n=1}^\infty e^{-2\pi(K_L+K_R)/\hbar} = \infty$。没有归一化密度矩阵 $\rho = W/\operatorname{Tr}W$，$S = -\operatorname{Tr}\rho\ln\rho$ 无从定义；只能谈论"每个态的权重"，不能谈论"热态的熵"。

**有限维 $I_d$**：$\mathcal H_D$ 是 $d$ 维，$\hat A$ 的谱 $\{A_1,\dots,A_m\}$ 有限（每个本征值重数有限）。配分函数

$$Z_{D,1} = \operatorname{Tr}_{\mathcal H_D}e^{-\hat A/(4G_N)} = \sum_{j=1}^{m}d_j\,e^{-A_j/(4G_N)} \lt \infty,$$

其中 $d_j$ 是简并度。密度矩阵与熵：

$$\rho_D = \frac{e^{-\hat A/(4G_N)}}{Z_{D,1}},\qquad S = -\operatorname{Tr}\rho_D\ln\rho_D = \frac{\langle\hat A\rangle}{4G_N} + \ln Z_{D,1}.$$

$\ln Z_{D,1}$ 有限，才有"对 $\ln\langle A\rangle$ 的修正系数"可言（论文 (5.65)–(5.69) 的 $106/45$）。$\square$

一句话：**代数的型决定"有没有密度矩阵"，Hilbert 空间的维数决定"配分函数收不收敛"**——两件事都必须在谈熵之前解决。论文 §5.2 的有限维定理正是同时解决这两件事的那一步。

</details>

## 参考

- Harlow & Jafferis, JHEP 02 (2020) 177（arXiv:1804.01081）："The Factorization Problem in Jackiw–Teitelboim Gravity"——JT 的完整量子化与引力时钟的直接来源。
- Iliesiu, Pufu, Verlinde & Wang, JHEP 11 (2019) 091（arXiv:1905.02726）："An exact quantization of Jackiw–Teitelboim gravity"——一阶形式与精确谱。
- Maldacena & Stanford, Phys. Rev. D 94 (2016) 106002（arXiv:1606.07801）：JT 与 Schwarzian 的经典参考（本篇未展开）。
- 论文 arXiv:2611.34924 §2（本篇的骨架与符号来源）；第 9 阶段 01 篇（Unruh 与热权重的四维版本）、02 篇（型分类）、04 篇（四维的有限维论证）。
