# 弯曲时空量子场论与半经典引力：没有偏好真空的世界

> 路线图位置：第 9 阶段（代数量子引力专题）· 第 1 篇
> 前置知识：第 4 阶段的标量场量子化（01 篇）、传播子族（02 篇）、路径积分与泛函行列式（07 篇）；量子力学书第 10 篇（密度矩阵与热平均）；广义相对论书第 6、7、8 章（Schwarzschild、因果结构、零超曲面）尚未写出时，可先接受"全局双曲时空 + 类时 Killing 矢量"的表述。
> 学习目标：说清"真空不唯一"的确切含义与 Bogoliubov 变换；会用 Bogoliubov 系数算粒子数；陈述并推导 Unruh 与 Hawking 温度的量纲与几何来源；写出半经典 Einstein 方程并说明其自洽性条件；知道 in-in 形式为何是反作用计算的正确语言、它与 S 矩阵的区别。

---

**单位约定**：本篇取自然单位 $\hbar = c = 1$（首次说明）；度规号差沿用本书 $\eta = \mathrm{diag}(+1,-1,-1,-1)$。弯曲时空公式里的整体符号不影响物理结果；欧氏化时只关心度规的符号无关部分（会单独注明）。

## 1. 一句话总结

**在弯曲时空里，没有全局时间就没有唯一的时间平移，也就没有唯一的真空——不同观测者的"粒子"通过 Bogoliubov 变换互相混合；加速观测者把闵氏真空看成热浴（Unruh），黑洞视界把入射真空看成热辐射（Hawking）；把量子场的期望值放回 Einstein 方程右边得到半经典方程，其单圈修正由有效作用量与 in-in（闭合时间路径）传播子组织。**

## 2. 真空不唯一与 Bogoliubov 变换

### 2.1 弯曲背景上的自由场

标量场作用量与场方程：

$$S = \int\mathrm{d}^4x\sqrt{-g}\left[\frac12 g^{\mu\nu}\partial_\mu\varphi\,\partial_\nu\varphi - \frac12 m^2\varphi^2\right],\qquad \left(\Box + m^2\right)\varphi = 0,$$

其中 $\Box = g^{\mu\nu}\nabla_\mu\nabla_\nu$。取全局双曲时空（有柯西面），在柯西面 $\Sigma$ 上定义 Klein–Gordon 内积

$$(f,g) \equiv i\int_\Sigma\mathrm{d}\Sigma^\mu\left(f^*\partial_\mu g - (\partial_\mu f^*)\,g\right),$$

它对满足场方程的函数与 $\Sigma$ 的选择无关（流守恒）。一组完备模式 $\{u_i\}$ 满足

$$(u_i,u_j) = \delta_{ij},\qquad (u_i,u_j^*) = 0,\qquad (u_i^*,u_j^*) = -\delta_{ij},$$

场展开为

$$\varphi = \sum_i\left(a_i u_i + a_i^\dagger u_i^*\right),\qquad [a_i,a_j^\dagger] = \delta_{ij},$$

真空由 $a_i|0\rangle = 0$ 定义。

### 2.2 正频分解依赖什么

"模式 $u_i$ 是正频的"这个说法，需要先有"频率"——即一个时间方向。严格说：

- **有类时 Killing 矢量 $\xi$** 的时空（稳态），$\mathcal L_\xi u_i = -i\omega_i u_i$、$\omega_i \gt 0$ 给出一个偏好的正频分解，于是有"静态真空"（如 Schwarzschild 外区的 Boulware 真空）。
- **一般时空没有 Killing 矢量**，任意选一组完备模式都能定义一套"真空"，彼此一般不等价——这就是"真空不唯一"。
- 即使有 Killing 矢量，静态真空也未必**物理**：Boulware 真空在 Schwarzschild 视界上发散，真正的物理态由正则性（视界处无奇点）或初始条件选择（Hartle–Hawking / Unruh 态）。

### 2.3 Bogoliubov 变换

设 $\{u_i\}$ 与 $\{v_j\}$ 是两组完备正交模式，各自定义一套产生湮灭算符 $(a,a^\dagger)$ 与 $(b,b^\dagger)$。把一组模式按另一组展开：

$$v_j = \sum_i\left(\alpha_{ji}u_i + \beta_{ji}u_i^*\right).$$

这就是**Bogoliubov 变换**。用内积读出系数：

$$\alpha_{ji} = (u_i,v_j),\qquad \beta_{ji} = -(u_i^*,v_j).$$

把 $\varphi$ 用两套算符分别展开并比较，得

$$b_j = \sum_i\left(\alpha^*_{ji}a_i - \beta^*_{ji}a_i^\dagger\right).$$

由 $\{v_j\}$ 的正交归一性得到系数的约束：

$$\alpha\alpha^\dagger - \beta\beta^\dagger = \mathbb 1,\qquad \alpha\beta^T - \beta\alpha^T = 0.$$

**关键在于 $\beta \neq 0$**：只要两套模式的正频子空间不同，$b$ 的真空就含有 $a$ 的粒子。

### 2.4 粒子数：真空是压缩态

在 $a$-真空里数 $b$-粒子：

$$N_j \equiv \langle 0_A|b_j^\dagger b_j|0_A\rangle = \sum_i\lvert\beta_{ji}\rvert^2,\qquad \langle N\rangle = \operatorname{Tr}\left(\beta\beta^\dagger\right).$$

推导一行：$b_j|0_A\rangle = -\sum_i\beta^*_{ji}a_i^\dagger|0_A\rangle$，它的模方就是 $\sum_i|\beta_{ji}|^2$。

更强的陈述：在 $b$-粒子的 Fock 空间里，$a$-真空是**压缩态**。对角情形（$\alpha,\beta$ 对角）下

$$|0_A\rangle = \prod_j\frac{1}{\cosh\theta_j}\sum_{n=0}^\infty\left(-\tanh\theta_j\right)^n|n_j\rangle_B,\qquad \tanh\theta_j = \left|\frac{\beta_{jj}}{\alpha_{jj}}\right|,$$

它是左右（或不同模式）纠缠的叠加——这个结构在 Unruh 与 Hawking 效应里都会原样出现。

## 3. Unruh 效应

### 3.1 Rindler 楔

闵氏时空取 $t,x$ 与横向 $\mathbf x_\perp$。右楔 $x \gt |t|$ 内定义 Rindler 坐标

$$t = \xi\sinh\eta,\qquad x = \xi\cosh\eta,\qquad \mathrm{d}s^2 = \xi^2\mathrm{d}\eta^2 - \mathrm{d}\xi^2 - \mathrm{d}x_\perp^2.$$

$\xi = 0$ 是 Rindler 视界。固定 $\xi$ 的观测者随固有时间 $\mathrm{d}\tau = \xi\,\mathrm{d}\eta$ 运动，其固有加速度大小为 $1/\xi$；在 $\xi = 1/a$ 处加速度恰为 $a$。

### 3.2 欧氏化：温度的几何来源

把 Rindler 时间解析延拓到虚时，$\eta = -\mathrm{i}\tau$，度规变成（忽略整体符号）

$$\mathrm{d}s_E^2 = \mathrm{d}\xi^2 + \xi^2\mathrm{d}\tau^2 + \mathrm{d}x_\perp^2.$$

在 $(\xi,\tau)$ 平面里这是极坐标；**只有当 $\tau$ 的周期为 $2\pi$ 时原点才没有锥形奇点**。沿观测者 $\xi = 1/a$ 的固有时周期为

$$\beta = \xi\,(2\pi) = \frac{2\pi}{a} \;\Longrightarrow\; T = \frac{1}{\beta} = \frac{a}{2\pi}.$$

恢复 $\hbar,c,k_B$：$T = \hbar a/(2\pi c k_B)$。

### 3.3 Bogoliubov 系数与热谱

把闵氏模式与 Rindler 模式联系起来，可以得到

$$\left|\frac{\beta_{\omega}}{\alpha_{\omega}}\right| = e^{-\pi\omega/a},$$

于是

$$\langle N_\omega\rangle = \frac{\lvert\beta\rvert^2}{\lvert\alpha\rvert^2 - \lvert\beta\rvert^2} = \frac{1}{e^{2\pi\omega/a} - 1},$$

正是温度 $T = a/2\pi$ 的玻色分布。等价地，把闵氏真空对左楔求迹：

$$\rho_R = \operatorname{Tr}_L|0_M\rangle\langle 0_M| = \frac{1}{Z}\sum_n e^{-2\pi n\omega/a}|n_R\rangle\langle n_R| = \frac{e^{-K/T}}{Z},$$

其中 $K$ 是 Rindler boost 生成元。**闵氏真空在加速观测者看来是精确的热态**，左右两楔之间是热场二重态式的纠缠。

### 3.4 物理

- 粒子探测器以固有加速度 $a$ 在闵氏真空中运动，会以温度 $a/2\pi$ 被激发——"真空"不是"什么都没有"，而是依赖于观测者的概念。
- 等效原理给出与 Hawking 的桥：近视界区域的几何局部就是 Rindler，把 $a$ 换成表面引力 $\kappa$ 即可。

## 4. Hawking 辐射

### 4.1 表面引力与近视界几何

稳态黑洞有 Killing 矢量 $\xi = \partial_t$。在视界上定义**表面引力** $\kappa$：

$$\xi^\nu\nabla_\nu\xi^\mu = \kappa\,\xi^\mu\quad(\text{视界上}).$$

在近视界坐标（Kruskal 型）中，几何局部等价于 $\kappa$ 为加速度的 Rindler 时空。于是 Unruh 的欧氏论证逐字搬过来：

$$T_H = \frac{\kappa}{2\pi}.$$

### 4.2 Schwarzschild

$f(r) = 1 - 2GM/r$，视界 $r_s = 2GM$，

$$\kappa = \frac12 f'(r_s) = \frac{GM}{r_s^2} = \frac{1}{4GM} \;\Longrightarrow\; T_H = \frac{1}{8\pi GM}.$$

（$\hbar,c$ 恢复后 $T_H = \hbar c^3/(8\pi GMk_B)$，太阳质量黑洞约 $6\times10^{-8}$ K——比宇宙微波背景冷七个数量级。）温度随质量**反比**：小黑洞更热、蒸发更快（寿命 $\propto M^3$，第 8 阶段 01 篇自检 5）。

### 4.3 波包图像与灰体因子

另一种算法：把入射真空的模式沿几何光学追到 $\mathscr I^+$。模式在视界附近被无限蓝移，出射波包的有效温度正是 $T_H$；由于部分模式被势垒散射回黑洞，实际谱要乘**灰体因子** $\Gamma(\omega)$：

$$\frac{\mathrm{d}E}{\mathrm{d}t\,\mathrm{d}\omega} \propto \frac{\omega^3}{e^{\omega/T_H}-1}\,\Gamma(\omega).$$

重要之处：**这是运动学与几何的结果**，没有用到引力本身的量子化——弯曲时空 QFT 已经足够。

### 4.4 熵与黑洞力学

Bekenstein–Hawking 熵

$$S_{\mathrm{BH}} = \frac{A}{4G}\quad\left(\text{恢复单位 } \frac{k_Bc^3A}{4G\hbar}\right),$$

以及黑洞力学四定律（第零：视界上 $\kappa$ 常数；第一：$\mathrm{d}M = \frac{\kappa}{8\pi G}\mathrm{d}A + \Omega\,\mathrm{d}J + \Phi\,\mathrm{d}Q$；第二：$\mathrm{d}A \ge 0$；第三：$\kappa\to0$ 不可达）。这些定律与热力学四定律逐条对应，但**微观态是什么**——这是第 4 篇与第 8 阶段导览的核心问题（广义相对论书第 13 章）。

## 5. 半经典 Einstein 方程

### 5.1 方程与自洽性

把量子场的重整化期望值放到 Einstein 方程右边：

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\,\langle T_{\mu\nu}\rangle_{\mathrm{ren}}.$$

左边满足 Bianchi 恒等式 $\nabla^\mu G_{\mu\nu} = 0$，所以右边必须守恒：

$$\nabla^\mu\langle T_{\mu\nu}\rangle_{\mathrm{ren}} = 0.$$

这不是自动的：重整化方案必须保持广义协变性（如维数正规化），否则会引入反常的"非守恒能动张量"。另一个微妙之处是**迹反常**：经典共形不变的理论在量子层面有

$$\langle T^\mu_{\ \mu}\rangle \neq 0,$$

其系数是普适的（由 Weyl 张量平方与 Euler 密度组合），它给半经典解带来额外的源——这在高曲率早期宇宙与黑洞蒸发中都有物理后果。

### 5.2 单圈有效作用量与泛函行列式

路径积分在鞍点附近展开：

$$Z = \int\mathcal D\varphi\;e^{iS[\varphi]} \approx e^{iS_{\mathrm{cl}}}\left(\det K\right)^{-1/2},\qquad K \equiv \left.\frac{\delta^2S}{\delta\varphi^2}\right|_{\varphi_{\mathrm{cl}}},$$

有效作用量 $\Gamma = -i\ln Z$：

$$\Gamma = S_{\mathrm{cl}} + \frac{i}{2}\operatorname{Tr}\ln K + O(\hbar^2).$$

$K = -\Box - m^2 - \xi R$（$\xi$ 为曲率耦合）。$\operatorname{Tr}\ln K$ 的导数展开给出 Seeley–DeWitt 系数：

$$\Gamma^{(1)} \supset \frac{1}{32\pi^2}\int\mathrm{d}^4x\sqrt{-g}\left[\frac{1}{\epsilon}\,a_2(x) + \cdots\right],\qquad a_2 \sim R_{\mu\nu\rho\sigma}^2,\ R_{\mu\nu}^2,\ R^2,$$

$\epsilon$ 是维数正规化的极点。这就是"曲率平方反项"的场论来源，也解释了为什么引力的一圈是 $R^2$ 型（第 8 阶段 01 篇 §2.3）。

### 5.3 适用域与失效

半经典方程是**混合**理论：物质量子、引力经典。它的展开参数是 $\ell_P^2/R^2$（$R$ 为曲率半径），在 $R \to \ell_P$ 处崩溃；它也不能描述度规的量子叠加（"Schrödinger 猫"式的几何）。它的价值在于：**在 $R \gg \ell_P$ 的一切场合预言可靠**，包括黑洞蒸发的绝大部分过程、早期宇宙的扰动、以及本文第 4 篇的反作用计算。

## 6. in-in 形式：反作用的正确语言

### 6.1 为什么 S 矩阵不够用

散射理论算的是 $\langle \mathrm{out}|\mathrm{in}\rangle$；反作用要算的是**给定态上的期望值**：

$$\langle \psi|U^\dagger(t,t_0)\,O(t)\,U(t,t_0)|\psi\rangle.$$

它含 $U$ 与 $U^\dagger$ 各一次——一条"去"的路径与一条"回"的路径。这就是**闭合时间路径**（closed time path, in-in, Schwinger–Keldysh）形式。

### 6.2 闭合时间路径

场在两条支上取两份：$\varphi_+$（前向）与 $\varphi_-$（后向）。生成泛函

$$Z[j_+,j_-] = \int\mathcal D\varphi_+\,\mathcal D\varphi_-\,e^{iS[\varphi_+]-iS[\varphi_-]}\cdots,$$

关联函数按支指标组织成 $2\times2$ 矩阵（Keldysh 空间）：$G_{++}$、$G_{--}$、$G_{+-}$、$G_{-+}$。要点：

- 只有特定组合（推迟/超前）有经典极限；对称组合给出涨落谱；
- 因为 $Z[j,j]=1$，$j_+=j_-$ 的源不产生跃迁——这是幺正性的体现；
- 源的二阶导数会带出**接触项**（$\delta^4(x-y)$ 型），它们与算符排序（Weyl 排序）一一对应（QM 书 03s2、QFT 书第 4 阶段补充材料）。

### 6.3 与第 4 篇（论文 §6）的对表

论文 §6 的半经典极限正是 in-in 计算：

- 相干态 + Ehrenfest（论文 (6.1)–(6.2)）：期望值走经典轨迹；
- 二阶 Einstein 张量 $E^{(2)}_{ab}[h,h]$ 的期望值（(6.13)）——引力子两点函数当作源；
- 推迟 Green 函数解出 $\bar g = g_0 + \Delta g$（(6.16)）；
- 附录 D.1：Hessian $K$ 的行列式与单圈生成泛函，就是本节 (5.2) 的 $(\det K)^{-1/2}$；接触项来自 $j$ 的二阶变分。

一句话：**论文第 6 节的"反作用"= 本章 5.2 的单圈有效作用量 + 本章第 6 节的 in-in 期望值**。

## 7. 小结

- 弯曲时空中没有全局时间就没有唯一真空；有 Killing 矢量只给静态观测者一个偏好分解，物理态还要由正则性/初始条件选（Boulware 真空在视界发散）。
- Bogoliubov 变换 $v_j = \sum(\alpha_{ji}u_i + \beta_{ji}u_i^*)$ 联系两套模式；$\beta \neq 0$ 意味着粒子产生，$\langle N\rangle = \operatorname{Tr}(\beta\beta^\dagger)$；真空在另一套模式看来是压缩态。
- Unruh：加速观测者看到温度 $T = a/2\pi$，来源是欧氏 Rindler 几何的 $2\pi$ 周期性。
- Hawking：近视界几何 = Rindler（$a \to \kappa$），$T_H = \kappa/2\pi$；Schwarzschild $T = 1/(8\pi GM)$；熵 $S = A/4G$ 与四定律。
- 半经典方程 $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G\langle T_{\mu\nu}\rangle$ 要求 $\nabla^\mu\langle T\rangle = 0$；单圈有效作用量 $\Gamma = S_{\mathrm{cl}} + \frac{i}{2}\operatorname{Tr}\ln K$ 给出曲率平方反项与迹反常；in-in 形式是期望值（而非 S 矩阵）的生成泛函，接触项与排序由它组织。

## 自检问题

**1.** 单模 Bogoliubov 变换 $v = \cosh\theta\,u + \sinh\theta\,u^*$：求 $b$ 与 $a$ 的关系，验证归一化 $\lvert\alpha\rvert^2 - \lvert\beta\rvert^2 = 1$，并计算 $a$-真空中的 $b$-粒子数。

<details markdown="1"><summary>点击显示答案</summary>

由展开 $v = \alpha u + \beta u^*$，$\alpha = \cosh\theta$、$\beta = \sinh\theta$。把 $\varphi = a u + a^\dagger u^* = b v + b^\dagger v^*$ 用 $u,u^*$ 的线性无关性比较系数：

$$a = \alpha b + \beta^* b^\dagger = \cosh\theta\,b + \sinh\theta\,b^\dagger.$$

解出 $b$（用 $\cosh^2 - \sinh^2 = 1$）：

$$b = \cosh\theta\,a - \sinh\theta\,a^\dagger.$$

归一化：$\lvert\alpha\rvert^2 - \lvert\beta\rvert^2 = \cosh^2\theta - \sinh^2\theta = 1$ ✓。

粒子数：$b|0_A\rangle = -\sinh\theta\,a^\dagger|0_A\rangle = -\sinh\theta\,|1_A\rangle$，故

$$\langle 0_A|b^\dagger b|0_A\rangle = \sinh^2\theta.$$

热谱对照：若 $\tanh\theta = e^{-\pi\omega/a}$，则

$$\langle N\rangle = \frac{\tanh^2\theta}{1-\tanh^2\theta} = \frac{1}{e^{2\pi\omega/a}-1},$$

正是温度 $T = a/2\pi$ 的玻色分布——Unruh 效应的全部内容就在这个单模算术里。

</details>

**2.** 用欧氏化论证 Unruh 温度 $T = a/2\pi$，并估算 $a = g = 9.8\ \mathrm{m/s^2}$ 时的温度。

<details markdown="1"><summary>点击显示答案</summary>

Rindler 度规 $\mathrm{d}s^2 = \xi^2\mathrm{d}\eta^2 - \mathrm{d}\xi^2 - \mathrm{d}x_\perp^2$。解析延拓 $\eta = -\mathrm{i}\tau$：

$$\mathrm{d}s_E^2 = \mathrm{d}\xi^2 + \xi^2\mathrm{d}\tau^2 + \mathrm{d}x_\perp^2.$$

$(\xi,\tau)$ 平面用极坐标表示：度规 $\mathrm{d}\xi^2 + \xi^2\mathrm{d}\tau^2$ 在 $\tau$ 的周期为 $2\pi$ 时是平坦平面；否则原点有锥形奇点（曲率奇点），能量动量张量发散。故欧氏时间周期 $\Delta\tau = 2\pi$。

固有时与坐标时的关系：$\mathrm{d}\tau_{\mathrm{proper}} = \xi\,\mathrm{d}\eta$。在 $\xi = 1/a$（固有加速度为 $a$ 的观测者）处，

$$\beta = \tau_{\mathrm{proper}}^{\mathrm{period}} = \frac{1}{a}\cdot 2\pi = \frac{2\pi}{a}.$$

温度是虚时周期的倒数：$T = 1/\beta = a/2\pi$。

数值：恢复单位 $T = \hbar a/(2\pi c k_B)$，

$$T = \frac{1.055\times10^{-34}\times 9.8}{2\pi\times 3.0\times10^8\times 1.38\times10^{-23}}\ \mathrm{K} \approx 4\times10^{-20}\ \mathrm{K}.$$

地球重力对应的 Unruh 温度远低于任何可测尺度——这就是为什么 Unruh 效应至今没有直接观测。

</details>

**3.** 从 Schwarzschild 度规求表面引力与 Hawking 温度，并解释为什么小黑洞更热。

<details markdown="1"><summary>点击显示答案</summary>

$f(r) = 1 - 2GM/r$。Killing 矢量 $\xi = \partial_t$ 在视界 $r_s = 2GM$ 上的表面引力

$$\kappa = \frac12\left.\frac{\mathrm{d}f}{\mathrm{d}r}\right|_{r_s} = \frac12\cdot\frac{2GM}{r_s^2} = \frac{GM}{4G^2M^2} = \frac{1}{4GM}.$$

（这一步可以从 $\xi^\nu\nabla_\nu\xi^\mu = \kappa\xi^\mu$ 直接算：在 $r$ 方向 $\xi^\nu\nabla_\nu\xi^r = \Gamma^r_{tt}(\xi^t)^2 = \frac12 g^{rr}\partial_r g_{tt}$，在视界上取绝对值即得上式。）

温度：

$$T_H = \frac{\kappa}{2\pi} = \frac{1}{8\pi GM}.$$

反比于质量：$M$ 越小温度越高。物理图像：$T_H \sim \hbar c^3/(GMk_B)$，是"引力势能尺度"与"量子热尺度"的唯一组合；黑洞越小，视界曲率越大（$\kappa \propto 1/M$），近视界的 Rindler 加速度越大，Unruh 温度越高。

数值：太阳质量黑洞 $T \approx 6\times10^{-8}$ K；原初小黑洞（$10^{12}$ kg）温度可达 $10^{11}$ K，会剧烈蒸发——这是早期宇宙与 TeV 引力实验里搜索原初黑洞的动机。

</details>

**4.** 说明半经典方程为什么要求 $\nabla^\mu\langle T_{\mu\nu}\rangle = 0$，并解释迹反常为什么不与它矛盾。

<details markdown="1"><summary>点击显示答案</summary>

对半经典方程取协变散度：

$$\nabla^\mu\left(G_{\mu\nu} + \Lambda g_{\mu\nu}\right) = 8\pi G\,\nabla^\mu\langle T_{\mu\nu}\rangle.$$

左边：$\nabla^\mu G_{\mu\nu} = 0$ 是 Bianchi 恒等式（几何恒等式，与场方程无关）；$\nabla^\mu g_{\mu\nu} = 0$ 是度规相容性。故

$$\nabla^\mu\langle T_{\mu\nu}\rangle_{\mathrm{ren}} = 0.$$

物理含义：引力是"守恒流的源"；如果量子场的能动张量不守恒，方程无解（或者说重整化破坏了广义协变性，方案不可用）。

迹反常：对经典共形不变的理论（$m=0$、共形耦合），经典 $T^\mu_{\ \mu} = 0$。量子化后

$$\langle T^\mu_{\ \mu}\rangle = c\,W_{\mu\nu\rho\sigma}W^{\mu\nu\rho\sigma} - a\,E_4 + \cdots \neq 0,$$

其中 $E_4$ 是 Euler 密度。它与守恒不矛盾：**一个张量可以既守恒又带迹**——$T_{\mu\nu} = T^{\mathrm{(tf)}}_{\mu\nu} + \frac14 g_{\mu\nu}T$，第二项在 $\nabla^\mu g_{\mu\nu}=0$ 下自动守恒。迹反常的物理后果：共形耦合场在弯曲背景中产生"反常能量"，给半经典解带来额外的源（例如 Starobinsky 型暴胀与黑洞蒸发的晚期修正）。

一句话：守恒约束的是散度，迹反常改变的是迹——两者是能动张量的不同分量结构，互不冲突。

</details>

**5.** 从高斯路径积分推出 $\Gamma = S_{\mathrm{cl}} + \frac{i}{2}\operatorname{Tr}\ln K$，并说明它与论文 (5.28a) 的 $\det_C K_0$ 因子的关系。

<details markdown="1"><summary>点击显示答案</summary>

写 $\varphi = \varphi_{\mathrm{cl}} + \eta$，展开到二阶：

$$S[\varphi] = S_{\mathrm{cl}} + \frac12\eta^T K\,\eta + O(\eta^3),\qquad K = \left.\frac{\delta^2S}{\delta\varphi^2}\right|_{\varphi_{\mathrm{cl}}}.$$

高斯积分（洛伦兹号差下是 Fresnel 型，配 $i\epsilon$ 收敛）：

$$Z \approx e^{iS_{\mathrm{cl}}}\int\mathcal D\eta\;e^{\frac{i}{2}\eta^T K\eta} = e^{iS_{\mathrm{cl}}}\left(\det K\right)^{-1/2}.$$

用 $\ln\det K = \operatorname{Tr}\ln K$：

$$Z = e^{iS_{\mathrm{cl}} - \frac12\operatorname{Tr}\ln K} \equiv e^{i\Gamma} \;\Longrightarrow\; \Gamma = S_{\mathrm{cl}} + \frac{i}{2}\operatorname{Tr}\ln K.$$

（$\frac{i}{2}\operatorname{Tr}\ln K$ 的实部给出 $-\frac12\operatorname{Tr}\ln|K|$，虚部给出相位；单圈发散在 $\operatorname{Tr}\ln K$ 的紫外端。）

与论文 (5.28a) 的关系：论文的 $Z(j_L,j_R)/Z(0,0)$ 前面有一个 $(\det_C K_0)^{-1/2}/(\det_C K_0)^{-1/2}$ 的比值，其中 $\det_C$ 表示沿闭合时间路径（Keldysh 轮廓）的泛函行列式、$K_0$ 是 $j=0$ 处的 Hessian。这正是本节结果的 in-in 版本：

- 轮廓 $C$ 上的行列式 = 两份场（$\varphi_\pm$）的联合行列式；
- 归一化 $Z(j)/Z(0)$ 使 $\det$ 因子在平方项里相消，只留下源的双线性项；
- 接触项来自 $K_j$ 对 $j$ 的导数（$\delta^2K/\delta j^2$），与 (4.28) 的 $\hat O_2$ 对应。

所以"单圈有效作用量"与"in-in 生成泛函"是同一件事的两种坐标：前者按背景场组织，后者按源与闭合轮廓组织。

</details>

## 参考

- Wald《Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics》(Chicago, 1994)：第 3 章（弯曲时空中的量子场论）、第 4 章（黑洞附近的量子效应）——本篇 2–4 节的标准参考。
- Birrell & Davies《Quantum Fields in Curved Space》(Cambridge, 1982)：Bogoliubov 变换、Unruh 与 Hawking 效应的系统计算。
- Unruh, Phys. Rev. D 14 (1976) 870；Hawking, Commun. Math. Phys. 43 (1975) 199：两篇原始论文。
- Calzetta & Hu, Phys. Rev. D 35 (1987) 495：闭合时间路径（in-in）形式在弯曲时空中的系统处理；DeWitt, Phys. Rep. 19 (1975) 295：单圈有效作用量与引力。
- 第 4 阶段 06 篇（一圈与重整化：迹反常与曲率平方反项的场论背景）；第 9 阶段 02 篇（算子代数：KMS 与热态的严格表述）；第 9 阶段 04 篇（论文 §6 的半经典极限与反作用）。
