# 超导：Cooper 对、BCS 与凝聚态版的希格斯机制

> 本书位置：凝聚态物理入门导论第 8 章
> 前置知识：第 3 章（金属自由电子气）的费米面与态密度、[第 2 章](02-lattice-vibrations-phonons.md) 的声子概念、[第 7 章](07-magnetism.md) 的 Landau 平均场思想；一点点电磁学（Maxwell 方程）。
> 学习目标：从四个实验事实出发，推出 London 方程与穿透深度；完整推导 Cooper 对的束缚能；读懂 BCS 的能隙方程与凝聚能；最后看清"超导 = U(1) 自发对称性破缺 + 规范场获质量"，即凝聚态版的希格斯机制。

约定：本书保留 $\hbar$ 与 $k_B$（不取自然单位）；电磁部分用 SI 单位制（$\mu_0$ 显式出现）；电子电荷记为 $-e$（$e>0$）。

---

## 1. 一句话总结

**超导是费米面上任意微弱的电子–电子吸引（来自电声子相互作用）引发的配对不稳定性：电子结成 Cooper 对并凝聚成一个有宏观相位的复序参量，自发破缺电磁 U(1) 规范对称性——Goldstone 模式被规范场"吃掉"，光子在超导体内获得质量，磁场被指数排拒（迈斯纳效应），电流无耗散地流动。它是希格斯机制在凝聚态物理中的原型。**

## 2. 实验事实：超导体的四张名片

超导不是一条性质，而是一组性质。任何理论必须同时解释下面四个实验事实。

### 2.1 零电阻（Kamerlingh Onnes, 1911）

汞在 $T_c \approx 4.2\ \mathrm{K}$ 以下电阻骤降为零（仪器测不出任何残余电阻，持续性电流实验给出的上限是衰减时间超过 $10^5$ 年）。注意 $T_c$ 是**相变温度**：电阻是陡降到零，不是平滑变小——超导是一个真正的热力学相。

### 2.2 迈斯纳效应（Meissner & Ochsenfeld, 1933）

把超导体放进外磁场再降温穿过 $T_c$，磁感应线被**主动排出**体内：$B = 0$ 是超导相的平衡性质，**与制备历史无关**。

这一点常被低估。零电阻只给出"完美导体"：对完美导体，$E = 0$ 意味着 $\partial B/\partial t = 0$，磁通只是被**冻结**——先加磁场再降温的样品会把磁通留在体内。迈斯纳效应说明超导体不只是完美导体，而是**完全抗磁体**。正是这个差别逼出了 London 方程里那个关键的额外假设（第 3 节）。

### 2.3 能隙（比热与隧道实验）

低温下超导体的电子比热不按金属的 $C \propto T$ 行为，而是指数小：

$$C_{\mathrm{es}} \propto e^{-\Delta / k_B T},$$

直接暗示激发谱中存在能隙 $\Delta \sim k_B T_c$：从基态产生激发需要越过有限能量。后来的电子隧道实验（Giaever, 1960）直接测出了这个能隙。

### 2.4 同位素效应（Maxwell; Reynolds et al., 1950）

汞的不同同位素测得

$$T_c \propto M^{-1/2},$$

$M$ 是原子核质量。电子性质本身与核质量几乎无关，唯一能随 $M$ 变化的是**晶格振动频率** $\omega \propto \sqrt{\kappa/M}$。所以同位素效应等于一份"指纹鉴定"：**超导的电子间吸引来自晶格（声子）**。

## 3. London 唯象理论

在微观机制还不清楚的 1935 年，London 兄弟先写下了描述超流电流的唯象方程。它推导电学性质只用两个假设：超流电子无碰撞、且无回滞地把磁场排出去。

### 3.1 第一 London 方程：零电阻

设超流电子密度 $n_s$，在电场 $E$ 中做无阻尼加速：

$$m \frac{\partial \vec v_s}{\partial t} = -e \vec E.$$

电流密度 $\vec J_s = -n_s e\, \vec v_s$，代入得

$$\frac{\partial \vec J_s}{\partial t} = \frac{n_s e^2}{m}\, \vec E.$$

正常导体里电流由 $E$ 驱动并耗散（$\vec J = \sigma \vec E$）；这里电场驱动的是电流的**时间变化率**——恒定电流不需要任何电场维持。这就是零电阻。

### 3.2 第二 London 方程：迈斯纳效应

对第一方程取旋度，并用 Maxwell 方程 $\nabla\times\vec E = -\partial \vec B/\partial t$：

$$\frac{\partial}{\partial t}\left(\nabla\times\vec J_s + \frac{n_s e^2}{m}\,\vec B\right) = 0.$$

括号中的量只是个运动常数——这正是"完美导体冻结磁通"的数学表达，它**不能**解释迈斯纳效应。London 兄弟的关键一步是把这提升为超导态的**本构关系**：假设该量不仅守恒，而且恒等于零：

$$\boxed{\;\nabla\times\vec J_s = -\frac{n_s e^2}{m}\,\vec B\;}$$

这是一个额外假设，不是推导出来的；它的正确性由它预言的迈斯纳效应背书。第 7 节我们会看到这个假设在微观层面自动出现。

### 3.3 穿透深度 $\lambda_L$

静磁场下用 $\nabla\times\vec B = \mu_0 \vec J_s$（忽略位移电流）。对第二 London 方程再取旋度：

$$\nabla\times(\nabla\times\vec B) = -\nabla^2 \vec B = \mu_0\,\nabla\times\vec J_s = -\frac{\mu_0 n_s e^2}{m}\,\vec B,$$

即

$$\nabla^2 \vec B = \frac{\vec B}{\lambda_L^2}, \qquad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}.$$

对占据 $x>0$ 的半无限超导体、表面平行加磁场 $B_0$，解为

$$B(x) = B_0\, e^{-x/\lambda_L}.$$

磁场只能渗入表面约 $\lambda_L$ 的一层。**London 穿透深度**典型值 $n_s \sim 10^{28}\ \mathrm{m^{-3}}$ 给出 $\lambda_L \sim 30$–$50\ \mathrm{nm}$，与实验吻合。磁场进不去，体内 $B = 0$——迈斯纳效应就这样从第二 London 方程里掉了出来。

## 4. 电声子吸引：同位素效应的暗示

电子之间怎么会吸引？同位素效应指认了晶格。直观图像如下。

一个电子快速穿过晶格时，把带正电的离子实微微拉向自己，在身后留下一团缓慢弛豫的正电荷极化云；晶格惯性大，这团极化要持续约 $\omega_D^{-1}$（$\omega_D$ 是 Debye 频率）才消散。第二个电子若在这段时间内经过，会被这团正电荷吸引。用场论的话说：**两个电子通过交换虚声子产生有效吸引**——这是推迟相互作用，第一个电子"压弯晶格"，第二个电子来"享受凹坑"。

两个定量要点：

- **能量窗口**：声子最多携带 $\hbar\omega_D$ 的能量，有效吸引只存在于费米面附近宽度 $\hbar\omega_D$ 的薄壳内（壳外动量守恒与声子色散对不上）。典型 $\hbar\omega_D \sim 10$–$30\ \mathrm{meV}$，远小于费米能 $\varepsilon_F \sim \mathrm{eV}$——这是"弱耦合"的物理基础。
- **净符号**：屏蔽库仑排斥与声子吸引竞争，弱耦合超导体里后者在壳层内胜出，净相互作用近似为常数吸引 $-V$（$V>0$）。

于是模型的输入极简：费米面、壳层内的常数吸引 $-V$、截止 $\hbar\omega_D$。同位素效应顺带解释了：$T_c$ 若由 $\omega_D \propto M^{-1/2}$ 控制，自然有 $T_c \propto M^{-1/2}$（见自检第 2 题）。

## 5. Cooper 问题：任意弱吸引下的束缚对

1956 年 Cooper 问了一个看似简单的问题：**在填满的费米海之上，给两个额外电子加任意弱的吸引，它们会不会形成束缚态？** 答案是永远会。这是 BCS 理论的种子，也是本章最重要的推导，我们完整做一遍。

### 5.1 问题的设置

费米海填满 $k < k_F$。两个额外电子只能占据 $k > k_F$ 的态（Pauli 原理）。取一对总动量为零的电子（后面会看到这样束缚最强）：$\vec k\uparrow$ 与 $-\vec k\downarrow$。双电子波函数按平面波展开：

$$\Psi(\vec r_1, \vec r_2) = \sum_{\vec k} g(\vec k)\, e^{i\vec k\cdot(\vec r_1 - \vec r_2)}, \qquad g(\vec k) = 0 \ \ (k < k_F).$$

相互作用只在壳层 $0 < \xi_k < \hbar\omega_D$ 内取常数吸引（$\xi_k = \varepsilon_k - \varepsilon_F$ 是相对费米面的动能）：

$$\langle \vec k\uparrow, -\vec k\downarrow |\, \hat V \,| \vec k'\uparrow, -\vec k'\downarrow \rangle = -V \quad (\text{两电子都在壳层内}).$$

### 5.2 动量空间的薛定谔方程

定态方程 $\hat H \Psi = E \Psi$ 逐分量写出（$E$ 以 $2\varepsilon_F$ 为零点）：

$$2\xi_k\, g(\vec k) - V \sum_{\vec k'}{}^{\prime}\, g(\vec k') = E\, g(\vec k),$$

其中 $\sum'$ 只对壳层内的 $\vec k'$ 求和。吸引是常数是关键的简化：定义 $C = \sum'_{\vec k'} g(\vec k')$（一个与 $\vec k$ 无关的数），则

$$g(\vec k) = \frac{V C}{2\xi_k - E}.$$

两边对壳层内 $\vec k$ 求和，约去 $C$，得到**自洽方程**：

$$1 = V \sum_{\vec k}{}^{\prime}\, \frac{1}{2\xi_k - E}.$$

### 5.3 求和化积分：常数态密度的威力

把壳层内求和换成能量积分。记 $N(0)$ 为费米面处**单自旋**的态密度（单位体积），则

$$1 = N(0) V \int_0^{\hbar\omega_D} \frac{d\xi}{2\xi - E}.$$

寻找束缚解 $E = -E_b < 0$（能量低于两个自由电子的 $0$）：

$$1 = N(0) V \int_0^{\hbar\omega_D} \frac{d\xi}{2\xi + E_b} = \frac{N(0) V}{2}\, \ln\frac{2\hbar\omega_D + E_b}{E_b}.$$

反解出 $E_b$：

$$E_b = \frac{2\hbar\omega_D}{e^{2/N(0)V} - 1} \;\;\xrightarrow{N(0)V \ll 1}\;\; \boxed{\,E_b \simeq 2\hbar\omega_D\, e^{-2/N(0)V}\,}.$$

### 5.4 三个教训

1. **任意弱吸引都束缚**。根源是费米面附近单粒子态密度 $N(0)$ 是常数——壳层积分 $\int d\xi/(2\xi + E_b)$ 在 $E_b \to 0$ 时对数发散，无论 $V$ 多小都能凑出 $1$。对比三维自由空间：态密度 $\propto \sqrt{\xi}$，积分在零能处收敛，吸引必须超过阈值才有束缚态。**费米海把一个"可能有"的束缚问题变成了"一定有"。** 从维度看，被钉在费米面上的两个电子，其相对运动的态密度与二维自由粒子一样是常数，所以它们继承了"二维方阱永远有束缚态"的性质。
2. **非解析性**。$E_b \propto e^{-2/N(0)V}$ 在 $V = 0$ 处有本质奇点，任何按 $V$ 展开的微扰论逐阶都是零。这解释了为什么超导（$T_c \sim$ 几 K 对应 $E_b \sim \mathrm{meV}$）逃不过常规微扰论，也预告了 BCS 必须走变分/自洽的路。
3. **为什么配 $(\vec k\uparrow, -\vec k\downarrow)$**。总动量为零时，两个电子可互相散射进入的终态相空间最大（整个壳层球面都参与），束缚最强；自旋相反（单态）则让空间波函数对称、两个电子可以在吸引最生效的小距离处充分重叠。

Cooper 对本身不是玻色子气：$E_b \sim \mathrm{meV}$ 对应对尺寸（相干长度）$\xi_0 \sim \hbar v_F/E_b \sim 10^3\ \text{\AA}$，远大于电子间距——**百万量级的 Cooper 对互相交叠**。单个对的束缚不等于超导，但它证明了一件事：费米海对配对吸引是不稳定的。把这个不稳定性做完整的多体推广，就是 BCS。

## 6. BCS 理论：从一对到整个费米面

Bardeen、Cooper、Schrieffer（1957）把 Cooper 的一对电子推广为**所有费米面附近电子的集体配对**。本节只讲骨架：哈密顿量、变分/平均场、能隙方程、凝聚能。细节推导见参考教材。

### 6.1 配对（约化）哈密顿量

只保留对配对最重要的散射项——一对 $(\vec k\uparrow, -\vec k\downarrow)$ 整体散射到 $(\vec k'\uparrow, -\vec k'\downarrow)$：

$$H_{\mathrm{red}} = \sum_{\vec k,\sigma} \xi_k\, c^\dagger_{\vec k\sigma} c_{\vec k\sigma} - V \sum_{\vec k,\vec k'}{}^{\prime}\, c^\dagger_{\vec k'\uparrow} c^\dagger_{-\vec k'\downarrow}\, c_{-\vec k\downarrow} c_{\vec k\uparrow}.$$

### 6.2 BCS 变分波函数与能隙参数

BCS 猜的基态是"每个 $\vec k$ 的配对态要么空、要么被占"的乘积：

$$|\Psi_{\mathrm{BCS}}\rangle = \prod_{\vec k}\left(u_{\vec k} + v_{\vec k}\, c^\dagger_{\vec k\uparrow} c^\dagger_{-\vec k\downarrow}\right)|0\rangle, \qquad |u_{\vec k}|^2 + |v_{\vec k}|^2 = 1.$$

注意它**不守恒电子数**：各项混合了 $0$ 和 $2$ 个电子。这在数学上是变分的方便，在物理上是深刻的——第 7 节会看到这正是对称性破缺的体现。等价地，平均场做法定义复的**能隙参数**（序参量）

$$\Delta \equiv V \sum_{\vec k}{}^{\prime}\, \langle c_{-\vec k\downarrow} c_{\vec k\uparrow} \rangle,$$

假设 $\Delta \neq 0$ 并自洽求解。$\Delta \neq 0$ 意味着"湮灭一对电子"有非零期望值——粒子数守恒（U(1) 对称性）被基态自己破坏了。

对平均场哈密顿量做 Bogoliubov 变换（把 $c$ 与 $c^\dagger$ 线性混合成新的费米子算符 $\gamma$），对角化后：

$$H_{\mathrm{MF}} = E_{\mathrm{gs}} + \sum_{\vec k} E_k\, \gamma^\dagger_{\vec k} \gamma_{\vec k}, \qquad \boxed{\,E_k = \sqrt{\xi_k^2 + |\Delta|^2}\,}$$

准粒子是电子与空穴的相干叠加，激发一个准粒子至少花 $\lvert\Delta\rvert$，破坏一对要花 $2\lvert\Delta\rvert$。第 2.3 节的比热能隙就是它。振幅系数为

$$u_{\vec k}^2,\ v_{\vec k}^2 = \frac{1}{2}\left(1 \pm \frac{\xi_k}{E_k}\right),$$

即费米面附近 $\pm\lvert\Delta\rvert$ 的壳层里"占据/空着"被抹平——费米面消失了。

### 6.3 能隙方程与 $\Delta(T=0)$

自洽条件 $\Delta = V\sum' \langle c_{-\vec k\downarrow} c_{\vec k\uparrow}\rangle = V\sum' u_{\vec k} v_{\vec k}$ 给出**能隙方程**：

$$1 = \frac{V}{2} \sum_{\vec k}{}^{\prime} \frac{1}{E_k} \;=\; N(0)V \int_0^{\hbar\omega_D} \frac{d\xi}{\sqrt{\xi^2 + \Delta^2}} \;=\; N(0)V\, \operatorname{arcsinh}\frac{\hbar\omega_D}{\Delta}.$$

弱耦合 $N(0)V \ll 1$ 时 $\operatorname{arcsinh}(\hbar\omega_D/\Delta) \approx \ln(2\hbar\omega_D/\Delta)$，于是

$$\boxed{\;\Delta(0) = 2\hbar\omega_D\, e^{-1/N(0)V}\;}$$

与 Cooper 对的 $E_b \simeq 2\hbar\omega_D e^{-2/N(0)V}$ 对比：形式一样，**指数里的 2 变成了 1**。这不是巧合——Cooper 问题里只有孤立的一对电子享受吸引；BCS 里整个费米面集体配对，自洽性把配对效应增强（指数减半 = 能隙按指数平方根放大）。多体背景使不稳定性的标度比两体猜测更大。

### 6.4 凝聚能与热力学

$T=0$ 时超导态相对正常态的能量降低（凝聚能，单位体积）：

$$E_S - E_N = -\frac{1}{2} N(0)\,\Delta^2.$$

量级估计：正常态只有费米面附近 $\sim\Delta$ 壳层内的 $N(0)\Delta$ 个电子参与重组，每个省 $\sim\Delta$，故 $\sim N(0)\Delta^2$。它决定热力学临界场：破坏超导的磁场能量与凝聚能相抵，$\mu_0 H_c^2/2 = \tfrac12 N(0)\Delta^2$。

有限温度下 $\Delta(T)$ 单调下降并在 $T_c$ 处连续归零（平均场相变），BCS 给出

$$k_B T_c = 1.13\, \hbar\omega_D\, e^{-1/N(0)V}, \qquad \frac{2\Delta(0)}{k_B T_c} = 3.53,$$

后者是弱耦合 BCS 的普适常数，在常规超导中被大量实验验证。最后一句关于**相干因子**：BCS 的准粒子是电子–空穴混合，不同探针的散射算符在这个混合下带不同符号——超声衰减系数在 $T_c$ 以下单调下降，而核磁弛豫率 $1/T_1$ 出现一个峰（Hebel–Slichter 峰）。这个峰是配对态相干性的判决性证据，当年直接锁定了 BCS 理论。

## 7. 超导 = U(1) 自发对称性破缺：凝聚态版希格斯机制

现在是本章的思想高潮。前面所有结果可以装进一个更深刻的框架：**超导是电磁 U(1) 规范对称性的自发破缺，迈斯纳效应是规范玻色子（光子）在介质内获得质量**。这就是 Anderson–Higgs 机制，比粒子物理的希格斯机制更早出现在超导语境里。QFT 书里[电弱统一](../../qft-sm/docs/stage-06-standard-model/02-electroweak-unification.md)讲的希格斯机制与这里的结构逐条对应；关于整体对称与规范对称的概念区分，见[整体对称 vs 规范对称](../../qft-sm/docs/stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)。

### 7.1 序参量与对称性破缺

第 6 节已经看到 BCS 基态 $\langle c_{-\vec k\downarrow} c_{\vec k\uparrow}\rangle \neq 0$。宏观地看，凝聚体由一个**复序参量**描述：

$$\Psi(\vec r) = \lvert\Psi(\vec r)\rvert\, e^{i\varphi(\vec r)},$$

它扮演"Cooper 对的宏观波函数"的角色。微观哈密顿量在全局相位变换 $c \to e^{i\theta} c$（即 U(1)，对应粒子数/电荷守恒）下不变；变换下 $\Psi \to e^{-2i\theta}\Psi$，所以任何一个 $\Psi \neq 0$ 的态都**不是**对称的——基态从连续简并的"相位环"里自发选了一个 $\varphi$。这就是 U(1) 自发对称性破缺。

用 Ginzburg–Landau 自由能把话说定量（$T < T_c$ 时 $\alpha < 0$，$\beta > 0$）：

$$F = \int d^3r \left[\alpha \lvert\Psi\rvert^2 + \frac{\beta}{2}\lvert\Psi\rvert^4 + \frac{1}{2m^*}\left\lvert\left(-i\hbar\nabla + 2e\vec A\right)\Psi\right\rvert^2 + \frac{B^2}{2\mu_0}\right],$$

其中 $m^* = 2m$，$2e$ 是 Cooper 对的电荷大小（规范导数里取 $\Psi$ 带电荷 $-2e$）。前两项是熟悉的"墨西哥帽"：帽底 $\lvert\Psi\rvert_0 = \sqrt{-\alpha/\beta}$，相位任意。

### 7.2 全局版本：Goldstone 模式

先把 $\vec A$ 关掉。把 $\Psi = \lvert\Psi\rvert_0 e^{i\varphi}$ 代入动能项：

$$\frac{\hbar^2 \lvert\Psi\rvert_0^2}{2m^*}\, (\nabla\varphi)^2.$$

只有相位的**梯度**花能量。所以 $\varphi$ 的长波涨落（$\varphi(\vec r)$ 缓慢变化）能量趋于零——这就是 Goldstone 定理：连续对称性破缺必伴生无能隙模式。在中性系统（超流 $^4$He）里它就是声学声子（Bogoliubov 声），确实被观测到。

### 7.3 规范版本：Goldstone 被"吃掉"，光子获得质量

耦合电磁场后剧情改变。理论有**局域** U(1) 规范对称性：联合变换

$$\varphi \to \varphi - \frac{2e}{\hbar}\chi(\vec r), \qquad \vec A \to \vec A + \nabla\chi$$

下自由能不变。于是相位 $\varphi$ 不再对应物理自由度——可以选规范（幺正规范）把 $\Psi$ 取成实数，Goldstone 模式"消失"了。它的能量去哪了？代入动能项：

$$\frac{1}{2m^*}\left\lvert(-i\hbar\nabla + 2e\vec A)\Psi\right\rvert^2 \;\longrightarrow\; \frac{(2e)^2 \lvert\Psi\rvert_0^2}{2m^*}\, A^2.$$

**出现了一项正比于 $A^2$ 的项**。场的二次项就是质量项：光子在超导体内获得了有效质量。对 $\vec A$ 变分（$J = -\delta F/\delta \vec A$）：

$$\vec J = -\frac{(2e)^2 \lvert\Psi\rvert_0^2}{m^*}\,\vec A = -\frac{n_s e^2}{m}\,\vec A,$$

其中 $n_s = 2\lvert\Psi\rvert_0^2$ 是超流密度。取旋度立刻回到第二 London 方程；配合 Maxwell 方程再次得到 $\nabla^2\vec B = \vec B/\lambda_L^2$——**London 方程和迈斯纳效应从对称性破缺里自动掉了出来，不再需要第 3 节的额外假设**。有质量的光子进不了超导体：磁场以 $\lambda_L$ 为特征长度指数衰减，这正是"质量越大穿透越浅"的相对论关系 $\lambda \sim \hbar/mc$ 的非相对论版本。

### 7.4 与电弱希格斯机制的逐条对照

| 概念 | 超导体 | 电弱理论 |
| --- | --- | --- |
| 破缺的对称性 | 电磁 U(1)（在超导介质内） | $\mathrm{SU(2)}\times\mathrm{U(1)}$ |
| 序参量 / 凝聚体 | Cooper 对凝聚 $\Psi$，电荷 $-2e$ | Higgs 真空期望值 $\langle\phi\rangle$ |
| 获质量的规范玻色子 | 光子（介质内），穿透深度 $\lambda_L$ | $W^\pm$、$Z^0$ |
| 被吃掉的 Goldstone 模式 | 相位 $\varphi$（变成光子的纵向极化） | 三个 Goldstone（变成 $W^\pm$、$Z^0$ 的纵模） |
| 残余的振幅模式 | $\lvert\Psi\rvert$ 涨落（"Higgs mode"） | Higgs 玻色子 |

自由度守恒在超导里看得最清楚：破缺前 = 复标量 $\Psi$（2 个实自由度）+ 无质量光子（2 个偏振）；破缺后 = 实振幅模（1 个）+ 有质量光子（3 个偏振，新增的第 3 个就是吃掉的相位模）。这套"规范对称性破缺后规范玻色子获质量"的逻辑，1964 年被 Higgs、Englert–Brout、Guralnik–Hagen–Kibble 搬进了相对论场论；Anderson 早在 1963 年就指出超导里已经有了它的完整非相对论实现。

最后一句防止误会：相位 $\varphi$ 被规范"吃掉"不意味着它没有物理后果。**相位差**是规范不变的：它决定了磁通量子化 $\Phi_0 = h/2e$（注意分母是 $2e$，是对配对的直接测量）和 Josephson 效应——后者已经成为电压基准与超导量子比特的基础。

<details open markdown="1"><summary>补充说明：超导序参量的相位为什么"既被吃掉又可观测"</summary>

规范冗余说的只是：**逐点独立的**相位转动不携带物理内容，可以选规范把它定死。这和"相位没有任何物理意义"是两回事。

- **可观测的是相位的规范不变组合**：绕环一周的环绕数（磁通量子化）、两点间由 Josephson 电流 $I = I_c\sin\delta\varphi$ 锁定的相位差。
- **破缺的是对称性，不是冗余**。严格说，规范对称性不真正"破缺"（Elitzur 定理）；在幺正规范里固定规范后，破缺的是剩余的全局 U(1)（相位整体刚性转动）。本书沿用教科书惯例说"U(1) 自发破缺"，严格含义见 QFT 书[整体对称 vs 规范对称](../../qft-sm/docs/stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)一篇。

</details>

## 8. 小结

- 四个实验事实：零电阻、迈斯纳效应（主动排磁，与历史无关）、比热能隙 $e^{-\Delta/k_BT}$、同位素效应 $T_c \propto M^{-1/2}$（电声子机制的指纹）。
- London 唯象理论：无阻尼 + "冻结量恒为零"的额外假设 → 穿透深度 $\lambda_L = \sqrt{m/\mu_0 n_s e^2}$。
- Cooper 问题：费米面上方两个电子 + 壳层内常数吸引 → 任意弱吸引必有束缚态，$E_b \simeq 2\hbar\omega_D e^{-2/N(0)V}$，非解析，微扰论失效。
- BCS：配对哈密顿量 → Bogoliubov 变换 → $E_k = \sqrt{\xi_k^2+\lvert\Delta\rvert^2}$；能隙方程给出 $\Delta(0) = 2\hbar\omega_D e^{-1/N(0)V}$，$2\Delta(0)/k_BT_c = 3.53$；凝聚能 $-\tfrac12 N(0)\Delta^2$。
- 深层图像：$\Psi = \lvert\Psi\rvert e^{i\varphi}$ 自发选定相位，破缺 U(1)；规范场耦合下 Goldstone 相位模被光子吃掉变成其纵模，光子获质量 → London 方程与迈斯纳效应自动成立。超导是希格斯机制的凝聚态原型。

| 问题 | 答案 | 关键公式 |
| --- | --- | --- |
| 磁场为什么进不去 | 光子获质量（Anderson–Higgs） | $\nabla^2 \vec B = \vec B/\lambda_L^2$ |
| 吸引从哪来 | 交换虚声子（推迟、壳层 $\hbar\omega_D$） | $T_c \propto \omega_D \propto M^{-1/2}$ |
| 为什么弱耦合就够 | 费米面态密度常数，对数发散 | $E_b \simeq 2\hbar\omega_D e^{-2/N(0)V}$ |
| 能隙多大 | 集体配对自洽增强 | $\Delta(0) = 2\hbar\omega_D e^{-1/N(0)V}$ |
| 对称性发生了什么 | U(1) 自发破缺，相位被吃掉 | $\vec J = -(n_s e^2/m)\vec A$ |

## 自检问题

**1.** 从第二 London 方程 $\nabla\times\vec J_s = -(n_se^2/m)\vec B$ 出发，推导 $\nabla^2\vec B = \vec B/\lambda_L^2$，并求半无限超导体（占据 $x>0$，表面加平行磁场 $B_0$）中的磁场分布。

<details markdown="1"><summary>点击显示答案</summary>

静磁场下用 Ampère 定律 $\nabla\times\vec B = \mu_0 \vec J_s$（超流电流是唯一电流源，位移电流忽略）。对第二 London 方程取旋度：

$$\nabla\times(\nabla\times\vec J_s) = -\frac{n_s e^2}{m}\,\nabla\times\vec B = -\frac{\mu_0 n_s e^2}{m}\,\vec J_s.$$

左边展开 $\nabla(\nabla\cdot\vec J_s) - \nabla^2\vec J_s$。稳态下连续性方程 $\nabla\cdot\vec J_s = 0$，于是

$$\nabla^2\vec J_s = \frac{\vec J_s}{\lambda_L^2}, \qquad \lambda_L^2 = \frac{m}{\mu_0 n_s e^2}.$$

再对 $\vec B = -(\lambda_L^2\mu_0)^{-1} \cdot m/(n_se^2)$ 型关系代回（或对称地对 $\nabla\times\vec B = \mu_0\vec J_s$ 取旋度），得同一形式的 $\nabla^2\vec B = \vec B/\lambda_L^2$。

半无限几何：$\vec B = B(x)\hat z$，方程化为 $B''(x) = B(x)/\lambda_L^2$，通解 $A e^{x/\lambda_L} + C e^{-x/\lambda_L}$。物理要求 $x\to\infty$ 有界排除第一项；边界 $B(0) = B_0$ 定出

$$B(x) = B_0\, e^{-x/\lambda_L}.$$

磁场指数衰减，渗入深度即 $\lambda_L$。

</details>

**2.** 用 BCS 结果 $k_B T_c = 1.13\,\hbar\omega_D e^{-1/N(0)V}$ 推导同位素效应 $T_c \propto M^{-1/2}$。需要哪些近似假设？

<details markdown="1"><summary>点击显示答案</summary>

晶格振动的特征频率由"弹性系数 / 离子质量"决定：$\omega_D \propto \sqrt{\kappa/M}$。换同位素只改 $M$ 不改化学（电子结构、弹性系数 $\kappa$ 不变），故

$$\omega_D \propto M^{-1/2}.$$

BCS 公式里 $M$ 只通过 $\omega_D$ 进入——**前提是** $N(0)V$ 与 $M$ 无关。$N(0)$ 是纯电子性质，$V$ 中的电声子矩阵元在一级近似下也不含 $M$（声子频率的 $M$ 依赖在构成无量纲耦合 $N(0)V$ 时相消）。于是

$$T_c \propto \omega_D\, e^{-1/N(0)V} \propto M^{-1/2}.$$

实验上汞等同位素系数确实接近 $-1/2$；偏离（如某些过渡金属 $\alpha \neq 1/2$）来自库仑赝势 $\mu^*$ 的修正与强耦合效应——这本身也是电声子机制的进一步证据。

</details>

**3.** Cooper 问题中，为什么"壳层内态密度取常数 $N(0)$"保证了任意弱吸引都有束缚态？若相互作用发生在三维自由空间（态密度 $\propto\sqrt{\xi}$），结论会怎样？

<details markdown="1"><summary>点击显示答案</summary>

自洽方程是

$$1 = V \int_0^{\hbar\omega_D} d\xi\, \frac{N(\xi)}{2\xi + E_b}.$$

常数态密度 $N(\xi) = N(0)$ 时，被积函数在小 $\xi$ 处 $\sim 1/\xi$，积分**对数发散**：

$$\int_0 d\xi\, \frac{N(0)}{2\xi + E_b} = \frac{N(0)}{2}\ln\frac{2\hbar\omega_D + E_b}{E_b} \;\xrightarrow{E_b\to 0}\; \infty.$$

左边固定为 $1$，而右边随 $E_b \to 0$ 无界增长，所以**无论 $V$ 多小**都存在足够小的 $E_b$ 使等式成立——束缚态必有。

三维自由空间里 $N(\xi) \propto \sqrt{\xi}$，小 $\xi$ 处被积函数 $\sim \sqrt{\xi}/(2\xi+E_b) \sim \xi^{-1/2}$，积分**在 $E_b = 0$ 处收敛**到有限值 $\propto \sqrt{\hbar\omega_D}$。于是方程只在 $V > V_c$（某个有限阈值）时有解：弱吸引无束缚态。

本质差别：态密度在零能处的行为决定束缚方程是否有解。费米面把有效态密度钉成常数（等价于二维），所以对配对吸引"零阈值"。

</details>

**4.** 从能隙方程 $1 = N(0)V \operatorname{arcsinh}(\hbar\omega_D/\Delta)$ 推出弱耦合极限下的 $\Delta(0)$，并说明弱耦合条件 $N(0)V \ll 1$ 如何保证 $\Delta \ll \hbar\omega_D$ 自洽。

<details markdown="1"><summary>点击显示答案</summary>

弱耦合下 $\hbar\omega_D/\Delta \gg 1$（待验证），用大宗量近似

$$\operatorname{arcsinh} x = \ln\left(x + \sqrt{x^2+1}\right) \approx \ln(2x), \qquad x \gg 1,$$

能隙方程变为

$$1 \approx N(0)V \ln\frac{2\hbar\omega_D}{\Delta} \;\;\Longrightarrow\;\; \ln\frac{2\hbar\omega_D}{\Delta} = \frac{1}{N(0)V},$$

指数化：

$$\Delta(0) = 2\hbar\omega_D\, e^{-1/N(0)V}.$$

**自洽性检查**：$N(0)V \ll 1$ 时 $e^{-1/N(0)V}$ 指数小，故 $\Delta/\hbar\omega_D = 2e^{-1/N(0)V} \ll 1$，大宗量近似确实成立。同时 $\Delta \ll \hbar\omega_D \ll \varepsilon_F$，说明能隙只扰动费米面附近极薄的壳层——这与把 $N(\xi)$ 近似为常数、把相互作用近似为壳层内常数的整个弱耦合框架自洽。

</details>

**5.** 把 $\Psi = \lvert\Psi\rvert_0 e^{i\varphi}$ 代入 GL 动能项 $\frac{1}{2m^*}\lvert(-i\hbar\nabla + 2e\vec A)\Psi\rvert^2$，说明：(a) 无规范场时相位模是无能隙的 Goldstone 模式；(b) 有规范场时相位可以被规范掉，$\vec A$ 获得质量项，并由此恢复 London 方程。

<details markdown="1"><summary>点击显示答案</summary>

直接计算规范导数：

$$(-i\hbar\nabla + 2e\vec A)\Psi = \left(\hbar\nabla\varphi + 2e\vec A\right)\Psi - i\hbar\, e^{i\varphi}\nabla\lvert\Psi\rvert.$$

取 $\lvert\Psi\rvert = \lvert\Psi\rvert_0$ 常数（忽略振幅涨落），动能项化为

$$f_{\mathrm{kin}} = \frac{\lvert\Psi\rvert_0^2}{2m^*}\left(\hbar\nabla\varphi + 2e\vec A\right)^2.$$

(a) $\vec A = 0$：$f_{\mathrm{kin}} = \frac{\hbar^2\lvert\Psi\rvert_0^2}{2m^*}(\nabla\varphi)^2$。均匀相位不花能量，只有梯度花能量；波矢 $\vec q \to 0$ 的相位涨落能量 $\propto q^2 \to 0$——无能隙的 Goldstone 模式。

(b) 规范变换 $\vec A \to \vec A + \nabla\chi$、$\varphi \to \varphi - (2e/\hbar)\chi$ 保持 $f_{\mathrm{kin}}$ 不变。选 $\chi = (\hbar/2e)\varphi$ 把相位完全消去（幺正规范），剩余

$$f_{\mathrm{kin}} = \frac{(2e)^2\lvert\Psi\rvert_0^2}{2m^*}\, A^2,$$

即光子的质量项。对 $\vec A$ 变分得电流 $\vec J = -\delta F/\delta\vec A = -\frac{(2e)^2\lvert\Psi\rvert_0^2}{m^*}\vec A$；定义 $n_s = 2\lvert\Psi\rvert_0^2$、$m^* = 2m$，这正是

$$\vec J = -\frac{n_s e^2}{m}\vec A,$$

取旋度即第二 London 方程。Goldstone 模式的"能量"变成了规范场的质量——它作为光子的第三（纵向）极化继续存在。

</details>

## 参考

- Kittel《固体物理导论》第 8 版第 10 章（超导）——实验事实与 London 唯象，入门最快。
- Ashcroft & Mermin《固体物理》第 34 章（Superconductivity）——Cooper 对与 BCS 的完整推导，本章第 5、6 节的主线。
- Tinkham《Introduction to Superconductivity》第 1–3 章——London/GL 理论与 BCS 的干净讲法。
- Annett《Superconductivity, Superfluids and Condensates》第 4–6 章——从序参量与对称性破缺角度统一讲超流与超导，与本章第 7 节对应。
- 进阶：Schrieffer《Theory of Superconductivity》第 1–3 章；Altland & Simons《Condensed Matter Field Theory》第 6 章（对称性破缺与 Anderson–Higgs 机制的场论语言）。
