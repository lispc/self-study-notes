# 绝热定理与 Berry 相位：慢变化的几何学

> 路线图位置：量子力学书 · 第五部分（外场、对称性与几何相位）· 第 13 篇——凝聚态书[量子霍尔](../../condensed-matter/docs/11-quantum-hall-effect.md)与[拓扑物态](../../condensed-matter/docs/12-topological-phases.md)两章的 Berry 曲率地基（第 10 篇 Kubo 笔记末尾那句预告在此兑现）
> 前置知识：第 03 篇（演化算符、表象变换）；第 07 篇（含时微扰论——本篇是它的"慢极限"搭档：07 管快而弱的扰动，本篇管慢而任意的扰动）；第 05 篇（自旋 1/2 与泡利矩阵，主例题道具）；第 11 篇（AB 效应与 Landau 能级——两大道具与下游接口）。
> 学习目标：会陈述绝热定理与绝热条件 $\hbar\,\lvert\langle m\vert\dot n\rangle\rvert \ll \lvert E_m - E_n\rvert$，并把展开系数的方程推到一阶（几何相位由此显形）；会证明 Berry 相位 $\gamma_n = i\oint\langle n\vert\nabla_R n\rangle\cdot d\vec R$ 的规范不变性与可观测性；会在自旋 1/2 旋转磁场中算出 $\gamma = \mp\Omega/2$（立体角）；会把 AB 相位认作 Berry 相位；会写下 Bloch 能带的 Berry 曲率、反常速度与陈数 $\frac{1}{2\pi}\int_{\rm BZ}\Omega\,d^2k\in\mathbb Z$——整数量子霍尔电导量子化的拓扑内核。
>
> 记号约定：保留 $\hbar$。参数空间记 $\vec R(t)$（磁场方向、磁通、核坐标……），哈密顿量 $H(\vec R)$；瞬时本征态 $H(\vec R)\lvert n(\vec R)\rangle = E_n(\vec R)\lvert n(\vec R)\rangle$，非简并分支。

---

## 1. 一句话总结

**扰动慢到绝热极限时，体系停在本征态上"随波逐流"（绝热定理），但除了动力学相位 $-\int E\,dt/\hbar$ 之外还要捡起一个只依赖参数空间闭合路径的几何相位 $\gamma_n = i\oint\langle n(\vec R)\vert\nabla_R n(\vec R)\rangle\cdot d\vec R$（Berry 相位）——它在态的相位约定下不变，因此可以通过干涉观测；自旋 1/2 给出 $\gamma = \mp\Omega/2$（闭合路径张的立体角），AB 相位 $q\Phi/\hbar$ 是它最干净的实例；把"连接"对参数求旋度得 Berry 曲率——参数空间里的"磁场"，能带上的它在布里渊区积分出整数（陈数），整数量子霍尔效应的电导量子化正是这个整数的物理读数。**

## 2. 绝热定理：慢变化的规则

含时哈密顿量 $H(\vec R(t))$ 没有守恒能量，但若变化足够慢、且谱有隙，演化近似"贴着本征态走"：初始在第 $n$ 支的态，$t$ 时刻仍在第 $n$ 支（只差相位）。把态展开到**瞬时本征基**：

$$\lvert\psi(t)\rangle = \sum_n c_n(t)\,e^{i\theta_n(t)}\lvert n(\vec R(t))\rangle,\qquad \theta_n(t) \equiv -\frac{1}{\hbar}\int_0^t E_n(\vec R(t'))\,dt'，$$

代入薛定谔方程（自检问题 1）得到系数方程

$$\dot c_n = -c_n\langle n\vert\dot n\rangle - \sum_{meq n}c_m\,e^{i(\theta_m-\theta_n)}\frac{\langle n\vert\dot H\vert m\rangle}{E_m - E_n}.$$

**绝热条件**：非对角项被快速振荡的相位差压制，只要

$$\hbar\,\big\lvert\langle m\vert\dot n\rangle\big\rvert \ll \lvert E_m - E_n\rvert\qquad(\forall\,meq n)$$

（等价地 $\hbar\lvert\langle m\vert\dot H\vert n\rvert\rvert \ll \lvert E_m-E_n\rvert^2$），非对角转移可忽略，$c_n$ 只剩对角方程 $\dot c_n = -c_n\langle n\vert\dot n\rangle$，积分出

$$c_n(T) = e^{i\gamma_n}\,c_n(0),\qquad \gamma_n = i\int_0^T\langle n(\vec R(t))\vert\dot n(\vec R(t))\rangle\,dt = i\oint_{\mathcal C}\langle n\vert\nabla_R n\rangle\cdot d\vec R.$$

这就是**绝热定理**（一阶论证版；严格版要谱隙条件，Kato 1950——本篇引用）。最后一式把时间积分改写成参数空间环路 $\mathcal C$ 上的线积分：$\gamma_n$ 不依赖走多快、只依赖**走的路径**——几何量。它曾被当作可吸收的相位惯例埋没了几十年，直到 Berry（1984）证明它规范不变、可观测。

## 3. Berry 相位：规范不变、可干涉观测

**规范不变性**（自检问题 2）：本征态的相位约定 $\lvert n\rangle\to e^{i\beta(\vec R)}\lvert n\rangle$ 使"连接"（Berry connection）

$$\vec A_n(\vec R) \equiv i\langle n\vert\nabla_R n\rangle\ \longrightarrow\ \vec A_n - \nabla\beta$$

——与矢势在规范变换下的行为一模一样。但**闭路**积分的变化是 $\oint\nabla\beta\cdot d\vec R = \beta(\text{终点}) - \beta(\text{起点}) = 0$（单值相位），故 $\gamma_n$ 不变。单独一条路径的几何相位依赖约定，闭合回路的才是物理——与第 11 篇 AB 效应的结构逐字相同（§5 会看到这不是比喻）。

**可观测性**：把两条路径的输出干涉（或把 $\gamma$ 与动力学相位混频），干涉条纹只依赖相位差。分子光谱（双原子转动能级的半整数量子数异常）、螺旋光纤中光子偏振的旋转（Tomita–Chiao 1986）是教科书级验证。

**曲率**：与电磁学的类比可以推到底——对连接求旋度：

$$\vec\Omega_n(\vec R) = \nabla_R\times\vec A_n = i\,\big\langle\nabla_R n\,\big\vert\times\big\vert\nabla_R n\big\rangle,$$

**Berry 曲率**：参数空间里的"磁场"，规范不变（旋度吃掉梯度）。斯托克斯定理把环路相位写成曲率通量：

$$\gamma_n = \oint_{\mathcal C}\vec A_n\cdot d\vec R = \int_{S(\mathcal C)}\vec\Omega_n\cdot d\vec S.$$

曲率的源是**简并点**：单值光滑的相位约定无法覆盖整个参数空间时（狄拉克弦的同类），$\vec\Omega$ 像磁单极子一样从简并点发出——下一节的二能级模型里这是定量事实。

## 4. 例题一：自旋 1/2 在旋转磁场中

主例题：$H = -\mu\,B\,\hat n(\vec R)\cdot\vec\sigma$（磁场大小恒定、方向 $\hat n(\theta,\varphi)$ 慢转）。本征态沿 $\pm\hat n$，取上支

$$\lvert n,+\rangle = \begin{pmatrix}\cos\frac\theta2\\[2pt] e^{i\varphi}\sin\frac\theta2\end{pmatrix}.$$

计算连接的 $\varphi$ 分量（自检问题 3 完整走）：

$$A_\varphi^{(+)} = i\langle n,+\vert\partial_\varphi n,+\rangle = -\sin^2\frac\theta2 = -\frac{1-\cos\theta}{2}.$$

闭合路径（$\varphi: 0\to2\pi$，$\theta$ 固定——绕圆锥一周）：

$$\boxed{\ \gamma_\pm = \mp\frac{\Omega}{2}\ },\qquad \Omega = 2\pi(1-\cos\theta)\ (\text{路径张的立体角}).$$

三件事读出：

1. **答案只用几何**：立体角 $\Omega$ 与转速、$\mu B$ 的大小统统无关（只要绝热条件满足）——这是"几何相位"命名的实证。
2. **曲率是单极子**：把参数取 $\vec R = R\hat n$（$R$ 为磁场大小），则 $\vec\Omega_\pm(\vec R) = \mp\frac{1}{2}\frac{\vec R}{R^3}$——从原点（$\vec R=0$ 正是二能级简并点）发出的"磁单极"，单极荷 $\mp\frac12$。全空间总通量 $\mp\frac{1}{2R^2}\times4\pi R^2 = \mp2\pi$：把相位约定铺满球面时必须留一道"狄拉克缝"，这是它的定量表达（自检问题 3 完整推导）。
3. **上下两支反号**：$\gamma_+ + \gamma_- = 0$（规范选择下成立；两支曲率通量之和恒为零，因为总跃迁概率守恒的痕迹）。

**绝热与严格的对照**：自旋 1/2 旋转磁场可以精确解（进动方程），绝热极限下精确解给出 $\theta$ 锥面上的进动加一个慢相位——慢相位正是 $\mp\Omega/2$。几何相位不是近似修正，是绝热极限下**精确保留**的量（07 篇含时微扰论丢弃的恰是它——快慢两种极限的分界线画在这里）。

## 5. 例题二：AB 效应是 Berry 相位

第 11 篇的磁 AB：电子约束在环上（半径 $\rho$），螺线管磁通 $\Phi$ 穿过环心。把"参数"取为电子在环上的位置角 $\alpha\in[0,2\pi)$（或等价地把 $\Phi$ 当参数），顺时针绕环一周 = 参数空间闭合回路。环上 $\vec B = 0$，但 $\vec A$ 沿环均匀：$A_\alpha = \Phi/(2\pi\rho)$（$\oint\vec A\cdot d\vec l = \Phi$）。

绕环一周的波函数相位（携带矢势的最小耦合版本，第 11 篇 §4）：

$$\gamma_{\rm AB} = \frac{q}{\hbar}\oint\vec A\cdot d\vec l = \frac{q\Phi}{\hbar}.$$

用 Berry 的语言复述：哈密顿量以磁通为周期（Byers–Yang，$\Phi\to\Phi+\Phi_0$ 时差一个规范变换），参数空间是**圆环长度 $\Phi_0$ 的闭合圈**；绕一圈捡起的 Berry 相位 $q\Phi/\hbar$。**AB 效应 = 环上边界条件的 Berry 相位**——第 11 篇里"拓扑障碍使闭路相位非零"那句线积分，就是本篇的 $\gamma_n$。

这个视角立刻量产新结果：环上基态能量随 $\Phi$ 振荡（持续电流 persistent current）、超导环的磁通量子化（$h/2e$ 周期）——凝聚态书第 8 章的原料。

## 6. Berry 曲率进能带：反常速度与陈数

**布洛赫能带**（凝聚态书[能带理论](../../condensed-matter/docs/04-band-theory.md)）：周期体系中晶带动量 $k$ 是好量子数，能带 $\varepsilon_n(k)$。把本篇的参数 $\vec R$ 换成 $\vec k$：每个能带自带一条 Berry 连接 $\vec A_n(k) = i\langle u_{nk}\vert\nabla_k u_{nk}\rangle$ 与曲率 $\vec\Omega_n(k)$。

**反常速度**：外加电场 $\vec E$ 使 $\hbar\dot k = q\vec E$（准经典的加速定理）。半经典运动方程里，$\varepsilon(k)$ 的梯度之外多出一项**垂直于电场的横向速度**：

$$\dot{\vec r} = \frac{1}{\hbar}\nabla_k\varepsilon_n(\vec k) + \dot{\vec k}\times\vec\Omega_n(\vec k),$$

第二项就是反常速度——Berry 曲率的直接动力学效应（反常霍尔效应的微观来源：即使没有杂质偏置，曲率也把电子往横向推）。

**陈数与量子霍尔**：布里渊区是个**环面**（$k$ 与 $k+\vec G$ 认同）——无边的闭合参数空间。占据能带的曲率在整个布里渊区的积分（配 $2\pi$ 归一）

$$\boxed{\ N_n = \frac{1}{2\pi}\int_{\rm BZ}\Omega^z_n(\vec k)\,d^2k\ \in\ \mathbb Z\ },$$

是整数（陈数，自检问题 5 给出量子化的论证梗概：环面没法全局单值地铺相位约定，补丁与补丁之间的"缝"贡献的整数绕数就是 $N_n$——与狄拉克磁单极荷的整值化同构）。能带占满后对布洛赫电子求和，反常速度贡献的横向电导精确为

$$\sigma_{xy} = \frac{e^2}{h}\sum_{n\in\text{占据}}N_n\qquad(\text{TKNN, 1982})，$$

**整数量子霍尔效应的电导量子化 = 陈数**。第 10 篇 Kubo 公式的预告（$\sigma_{xy}$ 是占据带 Berry 曲率的 BZ 积分）在此闭合：线性响应与几何相位是同一枚硬币——凝聚态书第 11 章从 Laughlin 泵浦角度重讲这枚硬币，第 12 章把它推广成拓扑物态的总纲。

**Born–Oppenheimer 顺带收编**：分子里电子快、原子核慢——核坐标 $\vec R_{\rm nuc}$ 是"慢参数"，电子态贴着绝热面走并给核运动提供 Berry 相位。锥形交叉（两电子面相切的点）周围绕一圈拾得 $\gamma = \pi$——分子光谱里的"分子 AB 效应"（Jahn–Teller 体系的能级反常）。绝热定理从原子钟到分子光谱到量子霍尔共用一台发动机。

## 7. 小结

| 概念 | 公式 | 备注 |
| --- | --- | --- |
| 绝热条件 | $\hbar\lvert\langle m\vert\dot n\rangle\rvert \ll \lvert E_m-E_n\rvert$ | 慢 + 有隙 |
| Berry 相位 | $\gamma_n = i\oint\langle n\vert\nabla_R n\rangle\cdot d\vec R$ | 规范不变、可干涉 |
| Berry 曲率 | $\vec\Omega_n = \nabla_R\times\vec A_n = i\langle\nabla n\vert\times\vert\nabla n\rangle$ | 参数空间的"磁场" |
| 自旋 1/2 | $\gamma_\pm = \mp\Omega/2$ | 立体角；曲率 = 单极子 $\mp\vec R/2R^3$ |
| AB | $\gamma_{\rm AB} = q\Phi/\hbar$ | Berry 相位的最干净实例 |
| 反常速度 | $\dot{\vec r} = \frac{1}{\hbar}\nabla_k\varepsilon + \dot{\vec k}\times\vec\Omega$ | 反常霍尔效应 |
| 陈数 | $N = \frac{1}{2\pi}\int_{\rm BZ}\Omega\,d^2k\in\mathbb Z$ | $\sigma_{xy} = (e^2/h)\sum N$（TKNN） |

一句话收束：慢演化不只积累 $e^{-\int Edt/\hbar}$，还在参数空间抄一条近路带回来一个只认路径不认速度的相位；把相位求旋度，就得到横在能带里的"磁场"——它的整数通量把欧姆定律的电导钉死在 $e^2/h$ 的整数倍上。几何从序参量晋升为可观测量。

## 自检问题

**1.** 从瞬时本征基展开出发推导系数方程，给出绝热条件，并指出对角项 $\langle n\vert\dot n\rangle$ 的实部为什么只能贡献相位（归一化的推论）。

<details markdown="1"><summary>点击显示答案</summary>

设 $\lvert\psi\rangle = \sum_n c_ne^{i\theta_n}\lvert n(t)\rangle$（$\theta_n$ 含动力学相位，$E_n$ 全为实）。代入 $i\hbar\partial_t\lvert\psi\rangle = H\lvert\psi\rangle$，左边

$$i\hbar\sum_n\Big(\dot c_n + ic_n\dot\theta_n\Big)e^{i\theta_n}\lvert n\rangle + i\hbar c_ne^{i\theta_n}\lvert\dot n\rangle,$$

右边 $= \sum_n c_ne^{i\theta_n}E_n\lvert n\rangle = \sum_n c_ne^{i\theta_n}(-\hbar\dot\theta_n)\lvert n\rangle$（按定义）。两边投影到 $\langle m\vert$，$E_n\lvert n\rangle$ 项与 $\dot\theta$ 项相消（这正是把动力学相位抽出来的用意），剩下

$$\dot c_m = -\sum_n c_ne^{i(\theta_n-\theta_m)}\langle m\vert\dot n\rangle.$$

把 $\langle m\vert\dot n\rangle$（$meq n$）用本征方程的微分改写：$H\lvert n\rangle = E_n\lvert n\rangle$ 对 $t$ 求导再投影 $\langle m\vert$（$meq n$）：$\langle m\vert\dot H\vert n\rangle + E_m\langle m\vert\dot n\rangle = E_n\langle m\vert\dot n\rangle$，故

$$\langle m\vert\dot n\rangle = \frac{\langle m\vert\dot H\vert n\rangle}{E_n - E_m}\qquad(m eq n),$$

即系数方程正文形式。绝热条件：非对角项都带快振荡相位 $e^{i(\theta_n-\theta_m)}$（频率 $\omega_{mn} = (E_n-E_m)/\hbar$），长时间平均下被压制，条件是耦合强度远小于频率：

$$\Big\lvert\frac{\langle m\vert\dot H\vert n\rangle}{E_n-E_m}\Big\rvert \ll \frac{\lvert E_m-E_n\rvert}{\hbar}\quad\Longleftrightarrow\quad \hbar\lvert\langle m\vert\dot n\rangle\rvert \ll \lvert E_m - E_n\rvert.$$

对角项：$\partial_t\langle n\vert n\rangle = 0 = \langle n\vert\dot n\rangle + \langle\dot n\vert n\rangle = 2\operatorname{Re}\langle n\vert\dot n\rangle$——实部为零，$-c_n\langle n\vert\dot n\rangle$ 是纯虚数，只转相位不动模长，$\lvert c_n\rvert$ 守恒（绝热定理的内容），其积分即 Berry 相位。

</details>

**2.** 证明：相位重定 $\lvert n(\vec R)\rangle\to e^{i\beta(\vec R)}\lvert n(\vec R)\rangle$ 下 Berry 连接平移 $\vec A_n\to\vec A_n - \nabla\beta$，而闭路 Berry 相位不变；由此说明为什么 $\gamma_n$ 可通过干涉实验观测，而"单条路径的几何相位"没有操作意义。

<details markdown="1"><summary>点击显示答案</summary>

连接的变换：

$$\vec A_n' = i\big(e^{-i\beta}\langle n\vert\big)\nabla\big(e^{i\beta}\lvert n\rangle\big) = i\big(i\nabla\beta + \langle n\vert\nabla n\rangle\big) = -\nabla\beta + \vec A_n.$$

闭路积分：

$$\gamma_n' = \oint\vec A_n'\cdot d\vec R = \gamma_n - \oint\nabla\beta\cdot d\vec R = \gamma_n - \big[\beta(\vec R_{\rm 终}) - \beta(\vec R_{\rm 起})\big] = \gamma_n,$$

末步用了相位函数的单值性（$\beta$ 是参数空间上的良定义函数，回路终点即起点）。故 $\gamma_n$ 是规范不变量。

可观测性：单一路径的总相位（动力学 + 几何）依赖态的约定（含 $\beta$ 的规范），单独不可测；但把同一初态经两条不同闭合路径送出再做干涉，相位差 $\Delta = \big[-\int_1Edt + \gamma_1\big] - \big[-\int_2Edt + \gamma_2\big]/\hbar$ 中一切约定相消（$\beta$ 的端点值对两条路径相同），剩下的 $\gamma_1 - \gamma_2$ 与动力学差都是物理。控制参数路径（如反向绕行使动力学部分对称相消）即可单独读出 Berry 相位——分子光谱、光纤偏振、中子干涉的实验方案全是这个骨架。

</details>

**3.** 对 $\lvert n,+\rangle = (\cos\frac\theta2,\ e^{i\varphi}\sin\frac\theta2)^{\rm T}$ 完整计算 $A_\varphi = i\langle n,+\vert\partial_\varphi n,+\rangle$，对常 $\theta$ 闭合路径积分得 $\gamma_+ = -\Omega/2$，并写出曲率的单极子形式。

<details markdown="1"><summary>点击显示答案</summary>

$$\partial_\varphi\lvert n,+\rangle = \begin{pmatrix}0\\ ie^{i\varphi}\sin\frac\theta2\end{pmatrix},\qquad \langle n,+\rvert = \Big(\cos\frac\theta2,\ e^{-i\varphi}\sin\frac\theta2\Big),$$

$$\langle n,+\vert\partial_\varphi n,+\rangle = e^{-i\varphi}\sin\frac\theta2\cdot ie^{i\varphi}\sin\frac\theta2 = i\sin^2\frac\theta2\ \Rightarrow\ A_\varphi = i\cdot i\sin^2\frac\theta2 = -\sin^2\frac\theta2 = -\frac{1-\cos\theta}{2}.$$

闭合路径 $\varphi:0\to2\pi$（$\theta$ 固定）：

$$\gamma_+ = \oint A_\varphi\,d\varphi = -2\pi\,\frac{1-\cos\theta}{2} = -\frac{\Omega}{2},\qquad \Omega = 2\pi(1-\cos\theta),$$

$\Omega$ 正是圆锥面在球上割出的立体角。下支 $\lvert n,-\rangle = (-e^{-i\varphi}\sin\frac\theta2,\ \cos\frac\theta2)^{\rm T}$ 同法得 $A_\varphi^{(-)} = +\frac{1-\cos\theta}2$，$\gamma_- = +\Omega/2$。

曲率：以 $\vec R = R\hat n$（$R = \lvert\vec R\rvert$，磁场大小）为参数。方位对称使连接只有 $\hat\varphi$ 分量；线元 $d\vec R$ 的 $\varphi$ 分量是 $R\sin\theta\,d\varphi$，故 $\oint\vec A\cdot d\vec R = \oint A_\varphi\,d\varphi$ 要求

$$\vec A_\pm = \frac{A_\varphi^{\pm}}{R\sin\theta}\,\hat\varphi = \mp\frac{1-\cos\theta}{2R\sin\theta}\,\hat\varphi$$

——这正是"磁单极矢势"（狄拉克弦规范）的原形。直接取旋度（球坐标公式）：

$$\vec\Omega_\pm(\vec R) = \mp\frac{1}{2}\,\frac{\vec R}{R^3}，$$

从原点（简并点 $\vec R = 0$，两能级 $\mp\mu\lvert\vec R\rvert$ 相碰处）发出的磁单极，荷 $\mp\frac12$；半径 $R$ 的球面总通量 $\mp\frac{1}{2R^2}\cdot4\pi R^2 = \mp2\pi$，与赤道回路（$\theta=\pi/2$，$\Omega = 2\pi$，$\gamma_\pm = \mp\pi$）经斯托克斯定理对表一致。

</details>

**4.** 把 AB 环（第 11 篇）改写成 Berry 相位语言：参数是什么、闭合回路是什么、$\gamma_{\rm AB} = q\Phi/\hbar$ 如何作为 Berry 相位读出；由它解释超导环磁通量子化的 $h/2e$ 周期。

<details markdown="1"><summary>点击显示答案</summary>

设置：约束在半径 $\rho$ 环上的电子，环心磁通 $\Phi$（环上 $\vec B = 0$）。沿环方位角 $\alpha$，矢势切向均匀，$A_\alpha^{\rm EM} = \Phi/(2\pi\rho)$。环上薛定谔方程（最小耦合 $\frac{1}{2m}(-\frac{i\hbar}{\rho}\partial_\alpha - qA_\alpha^{\rm EM})^2\psi = E\psi$）的本征态可取 $\psi_m = e^{im\alpha}$，能量

$$E_m(\Phi) = \frac{1}{2m}\Big(\frac{\hbar m}{\rho} - \frac{q\Phi}{2\pi\rho}\Big)^2 = \frac{\hbar^2}{2m\rho^2}\Big(m - \frac{q\Phi}{h}\Big)^2\qquad(m\in\mathbb Z)，$$

随 $\Phi$ 抛物线周期平移，周期 $h/\lvert q\rvert$。

Berry 读法：把"参数"取为磁通 $\Phi$ 本身。$H(\Phi + \Phi_0)$ 与 $H(\Phi)$ 差一个规范变换（第 11 篇 Byers–Yang 定理），所以参数空间是**周长 $\Phi_0$ 的圆圈**；$\Phi$ 从 $0$ 慢加到 $\Phi_0$，哈密顿量回到自身（差规范），体系沿能带绝热爬升——绕参数空间一整圈。圈上捡起的相位即波函数在恒等规范下的净相位差：$\psi_m$ 在 $\Phi$ 处与 $\Phi + \Phi_0$ 处的"同一态"差 $e^{iq\Phi_0/\hbar} = e^{2\pi i} = 1$（电子），而沿圈累积的相位速率是 $\frac{q}{\hbar}$：本征函数的净相位 $= \frac{q}{\hbar}\Phi$，圈积

$$\gamma_{\rm AB} = \frac{q\Phi}{\hbar}.$$

等价路径：参数取位置角 $\alpha$，连接 $A_\alpha = \frac{q}{\hbar}\rho A_\alpha^{\rm EM} = \frac{q\Phi}{2\pi\hbar}$，一圈积分 $\oint A_\alpha\,d\alpha = \frac{q\Phi}{\hbar}$ 同值。两条路读到同一个数：**AB 相位 = 边界条件圆上的 Berry 相位**。

超导环：绕环的载流子是库珀对 $q = 2e$，环上超导波函数单值性要求总相位（含 $\gamma_{\rm AB} = 2e\Phi/\hbar$）为 $2\pi$ 整数倍：$\frac{2e\Phi}{\hbar} + \delta_{\rm 动力学} = 2\pi n$，基态取动力学相位最小的分支，解出 $\Phi = n\frac{h}{2e}$——磁通量子化（凝聚态书第 8 章）。$\Phi_0^{\rm sc} = h/2e$ 正是 Berry 相位量子化条件 $\gamma = 2\pi n$ 的直接产物。

</details>

**5.** 给出陈数整值化的论证梗概：为什么 $\frac{1}{2\pi}\int_{\rm BZ}\Omega\,d^2k$ 必须是整数（补丁 + 缝的论证），并写出 TKNN 公式 $\sigma_{xy} = \frac{e^2}{h}\sum_{\rm occ}N_n$ 的机制（反常速度对满带的求和）。

<details markdown="1"><summary>点击显示答案</summary>

整值化（狄拉克量子化的孪生论证）：布里渊区是环面（闭合、无边界）。Berry 连接 $\vec A = i\langle u\vert\nabla u\rangle$ 依赖相位约定，而相位没法在整张环面上全局单值光滑地选（拓扑障碍；第 3 节单极子的"狄拉克缝"）。做法：把环面切成两块有界补丁 $S_1, S_2$，各选一份光滑规范，$A^{(1)}, A^{(2)}$。在补丁边界缝 $\partial S_1 = -\partial S_2$ 上两份规范差一个单值函数 $e^{i\beta}$。斯托克斯：

$$\int_{\rm BZ}\Omega\,d^2k = \oint_{\partial S_1}A^{(1)}\cdot dl + \oint_{\partial S_2}A^{(2)}\cdot dl = \oint_{\partial S_1}\big(A^{(1)} - A^{(2)}\big)\cdot dl = \oint_{\partial S_1}\nabla\beta\cdot dl = 2\pi\times(\text{绕数})，$$

绕数（缝上相位 $e^{i\beta}$ 绕单位圆的净圈数）是整数拓扑不变量——光滑形变（能隙不闭合）改变不了绕圈次数。故 $N = \frac{1}{2\pi}\int\Omega\,d^2k\in\mathbb Z$，且在能带保持孤立的任何微扰下不变。（三维参数空间的版本给出"曲率单极子"图像：$N$ = 简并点被布里渊区包住的净单极荷。）

TKNN 机制：满带里布洛赫电子在电场 $\vec E$ 下 $\hbar\dot k = q\vec E$ 慢扫布里渊区（恰好是绝热定理的场景！），速度 $\dot{\vec r} = \frac{1}{\hbar}\nabla_k\varepsilon + \dot{\vec k}\times\vec\Omega$。对满带求和：$\nabla_k\varepsilon$ 项积遍整个 BZ 为零（周期函数全微分），反常速度项给横向电流密度

$$j_y = -e\int_{\rm BZ}\frac{d^2k}{(2\pi)^2}\,\big(\dot{\vec k}\times\vec\Omega\big)_y = \frac{e^2}{h}E_x\sum_{\rm occ}\frac{1}{2\pi}\int_{\rm BZ}\Omega^z\,d^2k = \frac{e^2}{h}\Big(\sum_{\rm occ}N_n\Big)E_x.$$

即 $\sigma_{xy} = \frac{e^2}{h}\sum_{\rm occ}N_n$：**电导量子化 = 占据带陈数之和**。整数性保证平台在无序与弱微扰下钉死不动（能隙不闭，陈数不变）——凝聚态书第 11 章 Laughlin 泵浦从另一头（规范 + 绝热 + 能隙）推出同一公式，两路会师即"拓扑"的全部含义。

</details>

## 参考

- Berry, *Proc. R. Soc. Lond. A* **392**, 45 (1984)——原始论文，短得可以在一次茶歇读完。
- Griffiths《量子力学概论》（第 3 版）第 10 章（绝热近似与 Berry 相位）——本篇主线的本科版本。
- Sakurai–Napolitano《现代量子力学》Berry 相位一节——规范结构与 AB 的联系。
- Xiao, Chang & Niu, *Rev. Mod. Phys.* **82**, 1959 (2010)——半经典动力学、反常速度与陈数的权威综述。
- 凝聚态书[第 11 章 量子 Hall 效应](../../condensed-matter/docs/11-quantum-hall-effect.md)（Laughlin 泵浦与平台的下半场）、[第 12 章 拓扑物态](../../condensed-matter/docs/12-topological-phases.md)（陈数的全景）；本书[第 10 篇 线性响应](10-linear-response-kubo.md)（Kubo 与 TKNN 的会师点）。
