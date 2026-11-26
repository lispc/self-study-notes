# Hamilton–Jacobi 方程：作用量作为生成函数

> 路线图位置：第 2 部分（哈密顿力学与几何化）· 第 11 章
> 前置知识：第 9 章（哈密顿方程、Poisson 括号）、第 10 章（正则变换、生成函数、作用量–角变量）；偏微分方程的一阶解法（分离变量）。
> 学习目标：会把作用量看成末端点的函数并读出 $p = \partial S/\partial q$、$E = -\partial S/\partial t$；会写出并求解 Hamilton–Jacobi 方程（自由粒子、谐振子）；理解 $S$ 是"把 $H$ 变成零"的正则变换的生成函数；会用作用量–角变量求频率；知道 H–J 方程是薛定谔方程的 $\hbar\to0$ 极限（WKB 与旧量子论的源头）。

---

**单位约定**：本篇保留通常单位；第 6 节 WKB 部分会显式写出 $\hbar$。

## 1. 一句话总结

**Hamilton–Jacobi 方程 $\partial_tS + H(q,\partial_qS,t) = 0$ 是哈密顿力学的"波动方程"：它的完全解 $S(q,\alpha,t)$ 是一个正则变换的生成函数，把系统送到"所有坐标都是常数"的平凡表示。$S$ 就是经典作用量，它的等值面垂直于轨道（力学版的波前）；量子力学把 $S$ 换成相位 $e^{\mathrm{i}S/\hbar}$，H–J 方程就成了薛定谔方程的 $\hbar\to0$ 极限——这是旧量子论与 WKB 的出生地。**

## 2. 作用量作为末端点的函数

### 2.1 定义

固定起点 $(q_0,t_0)$，让终点 $(q,t)$ 变动。沿真实轨道积分：

$$S(q,t) \equiv \int_{t_0}^{t}L\left(q(t'),\dot q(t'),t'\right)\mathrm{d}t'.$$

$S$ 是终点 $(q,t)$ 的函数——**同一个 $S$ 既编码了轨道，又编码了动量**。

### 2.2 两个偏导数

考虑终点变动 $\delta q$、$\delta t$ 引起的 $S$ 变化。对作用量作变分（端点不再固定）：

$$\delta S = \left[p_i\delta q^i - H\,\delta t\right]_{\text{终点}} - \left[p_i\delta q^i - H\,\delta t\right]_{\text{起点}}.$$

起点固定，故

$$\boxed{\;\delta S = p_i\,\delta q^i - H\,\delta t \;\Longrightarrow\; \frac{\partial S}{\partial q^i} = p_i,\qquad \frac{\partial S}{\partial t} = -H.\;}$$

（推导见自检 1。）这两条是 H–J 理论的全部内容：**作用量是"动量势"和"能量势"**。

### 2.3 几何图像

把 $S(q,t) = \text{const}$ 看成"波前"。$\partial_qS = p$ 说明动量垂直于波前——与几何光学里"光线垂直于波前"同构。Hamilton 正是从光学类比得到这套理论的：**力学是几何光学的短波极限**。

## 3. Hamilton–Jacobi 方程

### 3.1 方程

把 $p = \partial_qS$ 代入 $H(q,p,t) = -\partial_tS$：

$$\boxed{\;\frac{\partial S}{\partial t} + H\left(q,\frac{\partial S}{\partial q},t\right) = 0.\;}$$

这是一阶非线性偏微分方程（$n$ 个空间变量 + 时间）。它的解 $S(q,t)$ 给出全部轨道：解方程 $\partial_qS = p$ 与 $q$ 的初值，即得 $q(t)$。

### 3.2 完全解

H–J 方程的通解含任意函数；有用的是**完全解**：含 $n$ 个独立常数 $\alpha_1,\dots,\alpha_n$ 的解

$$S = S(q,\alpha,t).$$

则轨道由隐式方程给出：

$$\beta_i = \frac{\partial S}{\partial \alpha_i} = \text{常数},\qquad p_i = \frac{\partial S}{\partial q^i}.$$

（$\beta_i$ 是新的"坐标"，$\alpha_i$ 是新的"动量"——见 §4。）$n$ 个方程 $\beta = \partial_\alpha S$ 解出 $q(t)$，$n$ 个常数 $\beta$ 由初值定。

### 3.3 例子：自由粒子

$H = p^2/2m$。H–J：

$$\partial_tS + \frac{1}{2m}\left(\partial_qS\right)^2 = 0.$$

分离变量 $S = -Et + W(q)$：$-E + W'^2/2m = 0$，$W' = \sqrt{2mE} \equiv \alpha$，故

$$S(q,\alpha,t) = \alpha q - \frac{\alpha^2}{2m}t + \text{const}.$$

$\beta = \partial S/\partial\alpha = q - (\alpha/m)t$，即 $q = \beta + (\alpha/m)t$——匀速运动，$\alpha = p$、$\beta$ 是初位置 ✓。

### 3.4 例子：谐振子

$H = p^2/2m + \frac12m\omega^2q^2$。分离变量 $S = -Et + W(q)$：

$$\frac{1}{2m}W'^2 + \frac12m\omega^2q^2 = E \;\Longrightarrow\; W = \int\sqrt{2mE - m^2\omega^2q^2}\,\mathrm{d}q.$$

积分出来（或用三角代换）：

$$S = -Et + \frac{m\omega}{2}\left[q\sqrt{\frac{2E}{m\omega^2}-q^2} + \frac{2E}{m\omega^2}\arcsin\left(q\sqrt{\frac{m\omega^2}{2E}}\right)\right].$$

另一个更漂亮的等价形式（用初始位置 $Q$ 作常数）：

$$S(q,Q,t) = \frac{m\omega}{2}\left[\left(q^2+Q^2\right)\cot\omega t - 2qQ\csc\omega t\right].$$

验证见自检 3：$\partial_qS = p$、$\partial_QS = -p_0$、$\partial_tS = -H$。

## 4. 生成函数视角

### 4.1 $S$ 是第二型生成函数

第 10 章的 $F_2(q,P,t)$ 生成正则变换 $(q,p)\to(Q,P)$，满足

$$p_i = \frac{\partial F_2}{\partial q^i},\qquad Q^i = \frac{\partial F_2}{\partial P_i},\qquad K = H + \frac{\partial F_2}{\partial t}.$$

把 $F_2 = S(q,\alpha,t)$、$P_i = \alpha_i$ 代入：$p_i = \partial_qS$ ✓、$Q^i = \partial_{\alpha_i}S = \beta_i$ ✓、新哈密顿量

$$K = H + \partial_tS = 0$$

（最后一步是 H–J 方程）。所以：

$$\boxed{\;\text{H–J 方程 = 找一个正则变换，把 }H\text{ 变成 }0.\;}$$

新坐标 $Q = \beta$、新动量 $P = \alpha$ 都是常数——**系统被"解掉"了**。这就是 H–J 方法的全部策略：不解运动方程，直接构造"平凡化"的正则变换。

### 4.2 与辛几何的关系

第 10 章说过：正则变换保持 $\omega = \mathrm{d}p\wedge\mathrm{d}q$。H–J 的 $S$ 是 $\omega = \mathrm{d}\theta$ 的"势"：$\theta = p\,\mathrm{d}q = \partial_qS\,\mathrm{d}q = \mathrm{d}S$（在变换后的坐标里）。$S$ 的等值面是辛流形的 Lagrange 子流形——这是 H–J 理论的几何化表述（Arnold 的"波前与焦散"图像）。

## 5. 作用量–角变量

### 5.1 周期运动

对一维周期运动（能量 $E$ 固定），定义**作用量**

$$J \equiv \oint p\,\mathrm{d}q = 2\int_{q_-}^{q_+}\sqrt{2m\left(E - V(q)\right)}\,\mathrm{d}q.$$

$J$ 是能量 $E$ 的函数（也是相图上闭合轨道的面积）。把 $S$ 写成 $S(q,J)$，定义**角变量**

$$Q = \frac{\partial S}{\partial J},\qquad \nu = \frac{\partial H}{\partial J}.$$

则 $\dot Q = \nu$ 是常数（频率），$\dot J = 0$——运动变成"匀速转动"。

### 5.2 谐振子

$E = \frac12m\omega^2A^2$（振幅 $A$），相图椭圆面积

$$J = \pi A\sqrt{2mE} = \pi\sqrt{\frac{2E}{m\omega^2}}\sqrt{2mE} = \frac{2\pi E}{\omega}.$$

于是

$$H = E = \frac{\omega}{2\pi}J,\qquad \nu = \frac{\partial H}{\partial J} = \frac{\omega}{2\pi}.$$

$\nu$ 是每秒周期数，$\omega = 2\pi\nu$ ✓。

### 5.3 绝热不变量

若参数（如 $\omega$）随时间缓慢变化（远慢于一个周期），$J$ 近似不变——**绝热不变量**。对谐振子：$J = 2\pi E/\omega$ 不变，故 $\omega$ 减小时 $E$ 跟着减小（$E\propto\omega$）。这是绝热定理的经典版本，也是量子力学里"缓慢变化哈密顿量的本征态跟随"的经典影子（量子力学书第 13 篇 Berry 相位的语境）。

## 6. 半经典与量子接口

### 6.1 从薛定谔方程到 H–J

把 $\psi = e^{\mathrm{i}S/\hbar}$ 代入薛定谔方程 $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\partial_q^2\psi + V\psi$：

$$-\partial_tS = \frac{1}{2m}\left(\partial_qS\right)^2 + V - \frac{\mathrm{i}\hbar}{2m}\partial_q^2S.$$

$\hbar\to0$ 时右端最后一项消失，正是 H–J 方程：

$$\partial_tS + \frac{1}{2m}\left(\partial_qS\right)^2 + V = 0.$$

下一阶（$\hbar^1$）给出振幅的输运方程（连续性方程），见自检 5。**H–J 方程是薛定谔方程的几何光学极限**——这句话的技术内容就是上面这一行。

### 6.2 量子化条件

旧量子论（Bohr–Sommerfeld）假设

$$\oint p\,\mathrm{d}q = n h.$$

WKB 的连接公式（在转折点处的 Airy 匹配）把它修正为

$$\oint p\,\mathrm{d}q = 2\pi\hbar\left(n + \frac{\mu}{4}\right),$$

$\mu$ 是转折点数（一维势阱 $\mu = 2$，故 $(n+\frac12)h$）。对谐振子：$J = 2\pi E/\omega$，代入得

$$E_n = \hbar\omega\left(n + \frac12\right)$$

——**零点能是 Maslov 修正的直接产物**。量子力学书 07s 篇的 WKB 与此完全一致。

### 6.3 路径积分的稳相

路径积分的半经典极限

$$\int\mathcal{D}q\;e^{\frac{\mathrm{i}}{\hbar}S[q]} \xrightarrow{\hbar\to0} \sum_{\text{经典轨道}} A\,e^{\frac{\mathrm{i}}{\hbar}S_{\mathrm{cl}}}$$

中的 $S_{\mathrm{cl}}$ 正是 H–J 完全解在经典轨道上的取值；振幅 $A$ 是 van Vleck 行列式（QFT 书第 4 阶段 07s 篇）。三条路线（H–J、WKB、路径积分稳相）在 $\hbar\to0$ 处汇合。

## 7. 小结

- 作用量作为终点函数满足 $\mathrm{d}S = p\,\mathrm{d}q - H\,\mathrm{d}t$：$\partial_qS = p$、$\partial_tS = -H$。
- H–J 方程 $\partial_tS + H(q,\partial_qS,t) = 0$；完全解含 $n$ 个常数 $\alpha$，轨道由 $\beta = \partial_\alpha S$ 隐式给出。
- $S(q,\alpha,t)$ 是第二型生成函数，把 $H$ 变成 $K = 0$——H–J 就是"平凡化"的正则变换。
- 作用量–角变量：$J = \oint p\,\mathrm{d}q$、$Q = \partial S/\partial J$、$\nu = \partial H/\partial J$；谐振子 $H = \omega J/2\pi$。
- 半经典：$\psi = e^{\mathrm{i}S/\hbar}$ 的 $\hbar^0$ 阶给出 H–J，$\hbar^1$ 阶给出输运方程；量子化条件 $\oint p\,\mathrm{d}q = 2\pi\hbar(n+\mu/4)$，谐振子 $E_n = \hbar\omega(n+\frac12)$。

## 自检问题

**1.** 从端点变动的变分推出 $\mathrm{d}S = p\,\mathrm{d}q - H\,\mathrm{d}t$，并说明为什么 $\partial_qS = p$、$\partial_tS = -H$。

<details markdown="1"><summary>点击显示答案</summary>

$$S = \int_{t_0}^{t}L(q,\dot q,t')\mathrm{d}t'.$$

对终点 $(q,t)$ 作变分（起点固定）：$\delta S = \int_{t_0}^{t}\left[\frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial\dot q}\delta\dot q\right]\mathrm{d}t' + L\,\delta t$。最后一项来自积分上限的移动（$S$ 多积了一小段 $\delta t$）。

对第二项分部积分，用 $\delta\dot q = \mathrm{d}(\delta q)/\mathrm{d}t'$：

$$\int\frac{\partial L}{\partial\dot q}\delta\dot q\,\mathrm{d}t' = \left[\frac{\partial L}{\partial\dot q}\delta q\right]_{t_0}^{t} - \int\frac{\mathrm{d}}{\mathrm{d}t'}\left(\frac{\partial L}{\partial\dot q}\right)\delta q\,\mathrm{d}t'.$$

沿真实轨道，Euler–Lagrange 方程使两个积分项相消；起点 $\delta q(t_0) = 0$。剩下

$$\delta S = p\,\delta q(t) + L\,\delta t = p\,\delta q + L\,\delta t.$$

注意终点位移 $\delta q$ 与时间位移 $\delta t$ 下的"全变分"是 $\delta q_{\text{全}} = \delta q + \dot q\,\delta t$，整理后

$$\delta S = p\left(\delta q_{\text{全}} - \dot q\delta t\right) + L\delta t = p\,\delta q_{\text{全}} - \left(p\dot q - L\right)\delta t = p\,\delta q - H\,\delta t.$$

故

$$\frac{\partial S}{\partial q} = p,\qquad \frac{\partial S}{\partial t} = -H.\qquad\square$$

关键点：$S$ 的偏导数给出**终点的动量与能量**——作用量是"动量势 + 能量势"。

</details>

**2.** 自由粒子：解 H–J 方程，验证 $S = \alpha q - \alpha^2t/2m$ 满足方程，并由 $\beta = \partial S/\partial\alpha$ 得到匀速运动。

<details markdown="1"><summary>点击显示答案</summary>

$H = p^2/2m$，H–J：$\partial_tS + (\partial_qS)^2/2m = 0$。分离变量 $S = -Et + W(q)$：

$$-E + \frac{W'^2}{2m} = 0 \;\Longrightarrow\; W' = \sqrt{2mE} \equiv \alpha \;\Longrightarrow\; W = \alpha q.$$

$E = \alpha^2/2m$，故

$$S(q,\alpha,t) = \alpha q - \frac{\alpha^2}{2m}t.$$

验证：$\partial_tS = -\alpha^2/2m = -E$；$\partial_qS = \alpha$；$\partial_tS + (\partial_qS)^2/2m = -E + E = 0$ ✓。

轨道：$\beta = \partial S/\partial\alpha = q - (\alpha/m)t$ 为常数，故

$$q(t) = \beta + \frac{\alpha}{m}t.$$

$\alpha = p$（动量）、$\beta = q_0$（初位置）——正是匀速直线运动。$\square$

注意 $S$ 就是熟悉的"$\frac12mv^2t = p^2t/2m$"（差一个常数 $\alpha q - \alpha^2t/2m$；在 $q = q_0 + (p/m)t$ 上它等于 $p(q-q_0) - p^2t/2m = p^2t/2m$，与 $\int\frac12mv^2\mathrm{d}t$ 一致）。

</details>

**3.** 谐振子：验证 $S(q,Q,t) = \frac{m\omega}{2}\left[(q^2+Q^2)\cot\omega t - 2qQ\csc\omega t\right]$ 满足 H–J 方程，并读出 $p$ 与 $p_0$。

<details markdown="1"><summary>点击显示答案</summary>

先算 $\partial_qS$：

$$\partial_qS = \frac{m\omega}{2}\left[2q\cot\omega t - 2Q\csc\omega t\right] = m\omega\left(q\cot\omega t - Q\csc\omega t\right) \equiv p.$$

再算 $\partial_tS$：

$$\partial_tS = \frac{m\omega}{2}\left[-(q^2+Q^2)\omega\csc^2\omega t + 2qQ\,\omega\csc\omega t\cot\omega t\right] = \frac{m\omega^2}{2}\left[-(q^2+Q^2)\csc^2 + 2qQ\csc\cot\right].$$

而

$$H = \frac{p^2}{2m} + \frac12m\omega^2q^2 = \frac{m\omega^2}{2}\left(q\cot - Q\csc\right)^2 + \frac{m\omega^2}{2}q^2.$$

展开平方：$(q\cot - Q\csc)^2 = q^2\cot^2 + Q^2\csc^2 - 2qQ\cot\csc$。用 $\csc^2 - \cot^2 = 1$：

$$H = \frac{m\omega^2}{2}\left[q^2\cot^2 + Q^2\csc^2 - 2qQ\cot\csc + q^2\right] = \frac{m\omega^2}{2}\left[q^2\csc^2 + Q^2\csc^2 - 2qQ\cot\csc\right].$$

于是

$$\partial_tS + H = \frac{m\omega^2}{2}\left[-(q^2+Q^2)\csc^2 + 2qQ\csc\cot + (q^2+Q^2)\csc^2 - 2qQ\cot\csc\right] = 0.\quad\square$$

初始动量：$\partial_QS = m\omega\left(Q\cot\omega t - q\csc\omega t\right)$。在 $t\to0$ 时 $\cot\approx1/(\omega t)$、$\csc\approx1/(\omega t)$：

$$\partial_QS \approx \frac{m(Q-q)}{t} \xrightarrow{q\to Q + (p_0/m)t} -p_0.$$

故 $\beta = \partial_QS = -p_0$ 是常数（初始动量）。$\square$

</details>

**4.** 作用量–角变量：对谐振子算出 $J = 2\pi E/\omega$、$H(J) = \omega J/2\pi$，并验证 $\nu = \partial H/\partial J = \omega/2\pi$。

<details markdown="1"><summary>点击显示答案</summary>

相图轨道 $H = \frac{p^2}{2m} + \frac12m\omega^2q^2 = E$ 是椭圆，半轴

$$a_q = \sqrt{\frac{2E}{m\omega^2}},\qquad a_p = \sqrt{2mE}.$$

面积

$$J = \pi a_q a_p = \pi\sqrt{\frac{2E}{m\omega^2}}\sqrt{2mE} = \frac{2\pi E}{\omega}.$$

故

$$H = E = \frac{\omega}{2\pi}J,\qquad \nu = \frac{\partial H}{\partial J} = \frac{\omega}{2\pi}.$$

$\nu$ 是每秒的周期数，$2\pi\nu = \omega$ ✓。$\square$

补充：由 $S(q,J) = \int p\,\mathrm{d}q$ 与 $Q = \partial S/\partial J$，$\dot Q = \partial H/\partial J = \nu$——角变量以恒定频率前进，$J$ 不变。这就是"可积系统在作用量–角变量下是匀速转动"的最简单实例（第 13 章的一般理论）。

</details>

**5.** WKB：把 $\psi = e^{\mathrm{i}S/\hbar}$ 代入薛定谔方程，导出 $\hbar^0$ 阶的 H–J 方程与 $\hbar^1$ 阶的输运方程；再用 $\oint p\,\mathrm{d}q = 2\pi\hbar(n+\frac12)$ 求谐振子能谱。

<details markdown="1"><summary>点击显示答案</summary>

代入：

$$\partial_t\psi = \frac{\mathrm{i}}{\hbar}\partial_tS\,\psi,\qquad \partial_q^2\psi = \left[-\frac{1}{\hbar^2}\left(\partial_qS\right)^2 + \frac{\mathrm{i}}{\hbar}\partial_q^2S\right]\psi.$$

薛定谔方程 $i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\partial_q^2\psi + V\psi$：

$$-\partial_tS\,\psi = \left[\frac{1}{2m}\left(\partial_qS\right)^2 - \frac{\mathrm{i}\hbar}{2m}\partial_q^2S + V\right]\psi.$$

即

$$\partial_tS + \frac{1}{2m}\left(\partial_qS\right)^2 + V = \frac{\mathrm{i}\hbar}{2m}\partial_q^2S.$$

**$\hbar^0$ 阶**：右端为零，H–J 方程 ✓。

**$\hbar^1$ 阶**：写 $\psi = A\,e^{\mathrm{i}S/\hbar}$（$A$ 为实振幅），代入后虚部给

$$\partial_t\left(A^2\right) + \partial_q\left(A^2\frac{\partial_qS}{m}\right) = 0,$$

即概率密度 $\rho = A^2$ 的连续性方程（速度 $v = \partial_qS/m$）。这是"WKB 振幅"的输运方程。$\square$

**谐振子能谱**：$p = \sqrt{2m(E - \frac12m\omega^2q^2)}$，$\oint p\,\mathrm{d}q = 2\pi E/\omega$（§5.2）。量子化条件

$$\frac{2\pi E}{\omega} = 2\pi\hbar\left(n + \frac12\right) \;\Longrightarrow\; E_n = \hbar\omega\left(n + \frac12\right).\qquad\square$$

零点能 $\frac12\hbar\omega$ 来自 Maslov 修正 $\mu/4 = 1/2$（两个转折点）；旧量子论的 $\oint p\,\mathrm{d}q = nh$ 会给出 $E_n = n\hbar\omega$，缺掉零点能。这正是"半经典方法在拓扑（转折点）处留下相位"的第一个实例。

</details>

## 参考

- Landau & Lifshitz《力学》§47（Hamilton–Jacobi 方程）、§48–49（分离变量与作用量–角变量）；§51（绝热不变量）。
- Goldstein《Classical Mechanics》第 10 章（Hamilton–Jacobi 理论、作用量–角变量、WKB 的经典对应）。
- Arnold《经典力学的数学方法》第 3 章（H–J 的几何解释：Lagrange 子流形与波前）。
- 量子力学书 07s 篇（WKB、连接公式与量子化条件）、01 篇（旧量子论与 Bohr–Sommerfeld）；第 9、10 章（正则形式与辛结构）；QFT 书第 4 阶段 07 篇（路径积分的稳相极限）。
