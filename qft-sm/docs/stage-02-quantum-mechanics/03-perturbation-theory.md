# 微扰论：从定态修正到费米黄金定则

> 路线图位置：第 2 阶段（量子力学）· 近似方法
> 前置知识：薛定谔方程、谐振子的升降算符解法、氢原子能级与简并、线性代数（本征值问题、对角化）。
> 学习目标：掌握非简并与简并定态微扰论的公式和推导骨架；理解三种绘景与 Dyson 级数；把费米黄金定则从 sinc² 极限完整推出来；看清"QFT 里算散射截面"本质上就是这套含时微扰论的相对论升级版。

---

## 1. 一句话总结

**量子力学里能严格求解的问题屈指可数，其余全靠"在一个可解的 H₀ 上加小扰动 λV 逐级展开"；定态微扰论修正能级和波函数，含时微扰论描述跃迁，而当末态是连续谱时跃迁概率随时间线性增长，其斜率就是费米黄金定则 $\Gamma=\dfrac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho(E_f)$——这条公式一路活到 QFT，散射截面不过是用相对论相空间替换 $\rho(E_f)$ 之后的同一句话。**

下面把这句话逐层拆开。本篇保留 $\hbar$（量子力学阶段惯例；黄金定则同时给出 $\hbar=1$ 的形式），到第 8 节进入 QFT 语境时再采用 $\hbar=c=1$ 的自然单位。

## 2. 为什么需要微扰论

量子力学的全部动力学原则上都装在薛定谔方程里，但**能写出解析解的情形少得可怜**：自由粒子、谐振子、氢原子（库仑势）、几个理想化的方势阱/δ 势——大致就这么多。真实的物理系统永远带着"不完美"：

- 真实振子有非谐修正 $\lambda x^4$；
- 原子处在外加电磁场中（Stark 效应、Zeeman 效应）；
- 电子感受到自旋–轨道耦合、核的有限体积、相对论修正（精细结构）；
- 原子与电磁场耦合，会吸收光、辐射光——这根本不是定态问题。

微扰论的策略是：把哈密顿量拆成"会解的主要部分"加"小的修正"，

$$H = H_0 + \lambda V,$$

其中 $\lambda$ 是一个无量纲的记账参数（最后令 $\lambda=1$），物理量按 $\lambda$ 的幂级数展开。这不只是技术工具，更是一种世界观：**物理学中绝大多数定量预言都是围绕某个可解点的级数展开**。QFT 里所有散射截面的计算（费曼图按耦合常数 $\alpha$ 的阶数组织）在数学结构上就是本章内容的直系后代，见第 8 节。

要清醒认识一点：微扰级数常常**不收敛**，只是渐近级数——但对小 $\lambda$，前几阶往往给出惊人的精度（QED 的 $g-2$ 是著名例子）。本篇只关心如何正确写出前几阶。

## 3. 定态微扰论（非简并）

### 3.1 设定与展开

设 $H_0$ 已解：

$$H_0\lvert n^{(0)}\rangle = E_n^{(0)}\lvert n^{(0)}\rangle,$$

且 $E_n^{(0)}$ **非简并**（每个能级只对应一个态）。对 $H = H_0 + \lambda V$ 展开

$$\lvert n\rangle = \lvert n^{(0)}\rangle + \lambda\lvert n^{(1)}\rangle + \lambda^2\lvert n^{(2)}\rangle + \cdots,$$

$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots.$$

约定修正态与未微扰态正交：$\langle n^{(0)}|n^{(k)}\rangle = 0$（$k\ge 1$），这可以通过重新归一化总做到，它把 $|n\rangle$ 方向的自由度全部吸收进 $\lvert n^{(0)}\rangle$。

### 3.2 逐级求解（推导骨架）

代入本征方程 $H|n\rangle = E_n|n\rangle$，比较 $\lambda$ 的各次幂：

- **$\lambda^0$ 阶**：就是 $H_0$ 的本征方程，无新内容。
- **$\lambda^1$ 阶**：

$$(H_0 - E_n^{(0)})\lvert n^{(1)}\rangle = (E_n^{(1)} - V)\lvert n^{(0)}\rangle.$$

用 $\langle n^{(0)}\rvert$ 左乘：左边因 $\langle n^{(0)}\rvert H_0 = E_n^{(0)}\langle n^{(0)}\rvert$ 而为零，右边给出

$$\boxed{E_n^{(1)} = \langle n^{(0)}\rvert V\lvert n^{(0)}\rangle}$$

——能量的一阶修正就是 $V$ 在未微扰态里的期望值。再用 $\langle m^{(0)}\rvert$（$m\neq n$）左乘同一方程，得 $\langle m^{(0)}|n^{(1)}\rangle = \dfrac{V_{mn}}{E_n^{(0)}-E_m^{(0)}}$，其中 $V_{mn}\equiv\langle m^{(0)}\rvert V\lvert n^{(0)}\rangle$。于是波函数一阶修正

$$\boxed{\lvert n^{(1)}\rangle = \sum_{m\neq n}\frac{V_{mn}}{E_n^{(0)}-E_m^{(0)}}\,\lvert m^{(0)}\rangle}$$

注意分母是**能级差**：$V$ 只"混入"能量相近的态，远态被能量分母压制。这个"能级差越小混合越强"的直觉在简并情形（第 4 节）会走到极端。

- **$\lambda^2$ 阶**：用同样手法（取 $\lambda^2$ 阶方程、左乘 $\langle n^{(0)}\rvert$、代入已得的 $\lvert n^{(1)}\rangle$），得

$$\boxed{E_n^{(2)} = \sum_{m\neq n}\frac{\lvert V_{mn}\rvert^2}{E_n^{(0)}-E_m^{(0)}}}$$

两个观察：**基态的二阶修正恒为负**（所有分母 $E_0^{(0)}-E_m^{(0)}<0$）——微扰总把基态往下推；而能级排斥（level repulsion）也写在这里：相邻两能级互相把对方推开。

### 3.3 例子：非谐振子算到底

取 $H_0 = \dfrac{p^2}{2m} + \dfrac12 m\omega^2 x^2$，微扰 $V = \lambda x^4$（把 $\lambda$ 当作有量纲的耦合常数）。用升降算符

$$x = \sqrt{\frac{\hbar}{2m\omega}}\,(a + a^\dagger),$$

一阶修正是 $\langle n\rvert x^4\lvert n\rangle$。展开 $(a+a^\dagger)^4$，只有含两个 $a$、两个 $a^\dagger$ 的项在 $\lvert n\rangle$ 中有非零期望值；六项分别给出

$$(n+1)(n+2),\ (n+1)^2,\ n(n+1),\ n(n+1),\ n^2,\ n(n-1),$$

相加得 $6n^2+6n+3$。因此

$$E_n^{(1)} = \lambda\left(\frac{\hbar}{2m\omega}\right)^2(6n^2+6n+3) = \frac{3\lambda\hbar^2}{4m^2\omega^2}\,(2n^2+2n+1).$$

基态能量到一阶为

$$E_0 = \frac{\hbar\omega}{2} + \frac{3\lambda\hbar^2}{4m^2\omega^2} + O(\lambda^2).$$

能级间距被拉大（$E_n^{(1)}$ 随 $n$ 增长），物理上对应 $x^4$ 势比谐振子势"更陡"。若再要二阶，需要 $\langle m\rvert x^4\lvert n\rangle$ 把 $n$ 变到 $n\pm2, n\pm4$ 的矩阵元代入 3.2 节的公式，留给读者练手。

## 4. 简并微扰论

### 4.1 问题在哪

若 $E_n^{(0)}$ 有 $g$ 重简并，第 3 节的公式立刻爆炸：分母 $E_n^{(0)}-E_m^{(0)}$ 在简并子空间内部为零。物理原因很简单——简并意味着 $H_0$ 无法区分子空间内的基矢量，而 $V$ 一般会**挑选出特定组合**，就像不稳定的铅笔尖朝哪个方向倒下由扰动决定。

### 4.2 解法：先在简并子空间里对角化

正确步骤：在 $g$ 维简并子空间中取 $H_0$ 本征态的任意基 $\{\lvert n,\alpha\rangle\}$（$\alpha=1,\dots,g$），构造 $V$ 的限制矩阵

$$W_{\alpha\beta} = \langle n,\alpha\rvert V\lvert n,\beta\rangle,$$

对角化这个 $g\times g$ 厄米矩阵。它的**本征值就是一阶能量修正**，**本征矢就是"正确的"零级态**（good states）。一阶能量劈裂为

$$E_{n,\alpha} = E_n^{(0)} + \lambda\,\varepsilon_\alpha,\qquad \alpha = 1,\dots,g,$$

其中 $\varepsilon_\alpha$ 是 $W$ 的本征值。劈裂后不再简并的态，就可以对剩余的非简并部分套用第 3 节公式。

实操中常先找与 $V$ 对易的对称性（如角动量分量），它自动把 $W$ 分块对角化，省下大量计算——下面的例子正是如此。

### 4.3 例子：氢原子的线性 Stark 效应

氢原子置於沿 $z$ 方向的匀强电场 $\mathcal{E}$，微扰为电子在电场中的势能

$$V = e\mathcal{E}\,z$$

（电子电荷 $-e$）。考虑 $n=2$ 能级：四重简并，态为 $\lvert 2s\rangle$ 与 $\lvert 2p, m=0,\pm1\rangle$。

利用对称性瘦身：$z\propto r\cos\theta$ 与 $L_z$ 对易，所以 $V$ 只在**相同 $m$** 的态之间有矩阵元；于是 $m=\pm1$ 的两个态不与任何东西混合，一阶不变。剩下的只有 $\{\lvert 2s\rangle, \lvert 2p,m{=}0\rangle\}$ 张成的二维子空间。又 $z$ 是奇宇称算符，对角元 $\langle 2s\rvert z\lvert 2s\rangle = \langle 2p\rvert z\lvert 2p\rangle = 0$。唯一的非零矩阵元（代入径向波函数直接积分）为

$$\langle 2s\rvert z\lvert 2p,m{=}0\rangle = -3a_0,$$

其中 $a_0$ 是玻尔半径。于是

$$W = -3ea_0\mathcal{E}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},$$

本征值 $\varepsilon_\pm = \mp 3ea_0\mathcal{E}$，对应"好态"

$$\lvert\pm\rangle = \frac{1}{\sqrt2}\big(\lvert 2s\rangle \mp \lvert 2p,m{=}0\rangle\big).$$

结果：$n=2$ 能级一阶劈裂成三条：$E_2 \pm 3ea_0\mathcal{E}$（对称叠加态）和 $E_2$（$m=\pm1$，未动）。劈裂**线性**正比于 $\mathcal{E}$——因为叠加态 $\lvert\pm\rangle$ 不再是宇称本征态，携带了永久电偶极矩。这正是"微扰挑选好态"的样板：$H_0$ 里 $\lvert 2s\rangle$、$\lvert 2p\rangle$ 地位平等，$V$ 一加入就指认了 $\frac{1}{\sqrt2}(\lvert 2s\rangle\mp\lvert 2p\rangle)$ 才是能量本征态。

## 5. 含时微扰论（本章重心）

### 5.1 三种绘景

同一个物理可以用三种等价的"记账方式"描述，区别只在于**把演化算符的哪一部分挂在态上、哪一部分挂在算符上**。设 $H = H_0 + V(t)$，$H_0$ 不含时。

| 绘景 | 态矢的演化 | 算符的演化 |
| --- | --- | --- |
| 薛定谔绘景 | $i\hbar\partial_t\lvert\psi_S\rangle = H\lvert\psi_S\rangle$（全部 $H$） | 不演化 |
| 海森堡绘景 | 不演化 | $i\hbar\dfrac{dA_H}{dt} = [A_H, H]$（全部 $H$） |
| 相互作用绘景 | $i\hbar\partial_t\lvert\psi_I\rangle = V_I\lvert\psi_I\rangle$（只含 $V$） | $i\hbar\dfrac{dA_I}{dt} = [A_I, H_0]$（只含 $H_0$） |

三者通过幺正变换联系：

$$\lvert\psi_I(t)\rangle = e^{iH_0t/\hbar}\lvert\psi_S(t)\rangle,\qquad A_I(t) = e^{iH_0t/\hbar}A_S\,e^{-iH_0t/\hbar},$$

而海森堡绘景用的是完整 $H$ 的演化算符。可以直接验证所有期望值 $\langle\psi\rvert A\lvert\psi\rangle$ 在三种绘景中相同——物理与记账方式无关。

相互作用绘景的精髓：把 $H_0$ 引起的"平凡进动"（各能级以 $e^{-iE_nt/\hbar}$ 自转）从态上剥掉，**态的剩余变化全部来自相互作用 $V$**。这正是微扰展开的天然舞台：$V=0$ 时相互作用绘景中的态干脆不动。

### 5.2 演化方程与 Dyson 级数

相互作用绘景中态满足

$$i\hbar\frac{d}{dt}\lvert\psi_I(t)\rangle = V_I(t)\lvert\psi_I(t)\rangle,\qquad V_I(t) = e^{iH_0t/\hbar}V(t)\,e^{-iH_0t/\hbar}.$$

形式上写成演化算符 $\lvert\psi_I(t)\rangle = U_I(t)\lvert\psi_I(0)\rangle$，则 $U_I$ 满足积分方程

$$U_I(t) = 1 - \frac{i}{\hbar}\int_0^t V_I(t')\,U_I(t')\,dt'.$$

反复迭代自身，得到 **Dyson 级数**：

$$U_I(t) = 1 - \frac{i}{\hbar}\int_0^t V_I(t_1)\,dt_1 + \left(-\frac{i}{\hbar}\right)^2\int_0^t dt_1\int_0^{t_1} dt_2\,V_I(t_1)V_I(t_2) + \cdots$$

每一阶是一个时间有序的积分，紧凑写法是时序指数 $U_I(t) = T\exp\!\big[-\frac{i}{\hbar}\int_0^t V_I(t')dt'\big]$。请把这个式子记住：QFT 里的 $S$ 矩阵就是它的相对论场论版，费曼图是这个级数逐项的图示记账法（第 8 节）。

### 5.3 一阶跃迁振幅

设 $t=0$ 时系统处于 $H_0$ 的本征态 $\lvert i\rangle$，微扰 $V(t)$ 打开。到一阶，$t$ 时刻跃迁到另一本征态 $\lvert f\rangle$ 的概率振幅为

$$c_f(t) = \langle f\rvert U_I(t)\lvert i\rangle = -\frac{i}{\hbar}\int_0^t \langle f\rvert V_I(t')\lvert i\rangle\,dt' = -\frac{i}{\hbar}\int_0^t V_{fi}(t')\,e^{i\omega_{fi}t'}\,dt',$$

其中 $\omega_{fi} = (E_f - E_i)/\hbar$ 是跃迁的（角）频率。相因子 $e^{i\omega_{fi}t'}$ 就是相互作用绘景"剥掉 $H_0$ 进动"的直接体现。

### 5.4 常微扰：sinc² 登场

最简单的非平庸情形：$t=0$ 突然加上**不含时**的 $V$（阶跃微扰）。积分是初等的：

$$c_f(t) = -\frac{i}{\hbar}V_{fi}\int_0^t e^{i\omega_{fi}t'}dt' = -\frac{V_{fi}}{\hbar\omega_{fi}}\big(e^{i\omega_{fi}t} - 1\big),$$

跃迁概率

$$P_{i\to f}(t) = \lvert c_f(t)\rvert^2 = \frac{\lvert V_{fi}\rvert^2}{\hbar^2}\cdot\frac{4\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}.$$

固定 $t$，把它看作 $\omega_{fi}$ 的函数：这是一个中心在 $\omega_{fi}=0$ 的峰（正比于 $\mathrm{sinc}^2$），

- **峰高** $\propto t^2$（在 $\omega_{fi}=0$ 处 $4\sin^2(\omega t/2)/\omega^2 \to t^2$）；
- **峰宽** $\sim 2\pi/t$（第一个零点在 $\omega_{fi} = 2\pi/t$）；
- **峰下面积** $\displaystyle\int_{-\infty}^{\infty}\frac{4\sin^2(\omega t/2)}{\omega^2}\,d\omega = 2\pi t$——随时间**线性**增长。

两个重要解读：

1. **$t$ 越大，峰越窄越高**：长时间后只有 $\omega_{fi}\approx 0$（即 $E_f \approx E_i$）的跃迁存活——这就是"跃迁中的能量守恒"，它的精度受 $\Delta E\,\Delta t \gtrsim \hbar$ 限制。注意这不是不确定性原理对单个测量的限制，而是微扰打开时间有限导致的频率分辨率。
2. **面积 $\propto t$**：如果对一群能量密集的末态求和，总概率随时间线性增长——"跃迁率"（单位时间概率）成为常数。这正是下一节黄金定则的雏形。

## 6. 费米黄金定则

### 6.1 连续谱与态密度

第 5.4 节的 $P_{i\to f}(t)$ 随时间振荡，单个末态没有稳定的"率"。物理上感兴趣的情形是末态属于**连续谱**（或宏观上密集的离散谱）：散射问题里的平面波末态、原子辐射时光子的连续模、固体里的能带。把末态用能量和其余量子数 $\beta$ 标记，定义**态密度** $\rho(E_f)$：能量落在 $[E_f, E_f+dE_f]$ 内的末态数为 $\rho(E_f)\,dE_f$（$\beta$ 已积分或固定）。

总跃迁概率是对末态的求和转积分：

$$P(t) = \int dE_f\,\rho(E_f)\,\frac{\lvert V_{fi}\rvert^2}{\hbar^2}\cdot\frac{4\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}.$$

### 6.2 sinc² → δ 的极限

当 $t$ 足够大，峰 $\frac{4\sin^2(\omega t/2)}{\omega^2}$ 比 $\lvert V_{fi}\rvert^2\rho(E_f)$ 变化的能量尺度窄得多，可以把后者取出峰外；用面积公式，

$$\frac{4\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}\ \xrightarrow{t\ \text{大}}\ 2\pi t\,\delta(\omega_{fi}) = 2\pi t\,\hbar\,\delta(E_f - E_i),$$

（最后一步用 $\delta(\omega_{fi}) = \hbar\,\delta(E_f-E_i)$，因为 $\omega_{fi} = (E_f-E_i)/\hbar$）。代回积分：

$$P(t) = \frac{2\pi}{\hbar}\,\lvert V_{fi}\rvert^2\,\rho(E_f)\Big\rvert_{E_f=E_i}\cdot t.$$

概率线性增长，斜率即**跃迁率**

$$\boxed{\Gamma = \frac{2\pi}{\hbar}\,\lvert V_{fi}\rvert^2\,\rho(E_f)}\qquad\Longleftrightarrow\qquad \Gamma = 2\pi\lvert V_{fi}\rvert^2\rho(E_f)\ \ (\hbar=1)$$

这就是**费米黄金定则**（Fermi's golden rule）。三个要素各司其职：矩阵元 $\lvert V_{fi}\rvert^2$ 是"相互作用的强度"，$\rho(E_f)$ 是"有多少末态可以去"，$\delta(E_f-E_i)$ 强制能量守恒。

<details markdown="1"><summary>补充说明：黄金定则的适用条件（时间不能太短也不能太长）</summary>

推导里对 $t$ 有两个方向的要求，必须同时满足：

- **$t$ 不能太短**：sinc² 峰要窄到能在 $\lvert V_{fi}\rvert^2\rho(E_f)$ 近似不变的范围内，即 $t \gg \hbar/\Delta E$，其中 $\Delta E$ 是末态连续谱的典型能宽。在此之前概率按 $t^2$ 增长（"量子 Zeno 区"），没有常数率可言。
- **$t$ 不能太长**：一阶微扰要求 $P(t) = \Gamma t \ll 1$，即 $t \ll 1/\Gamma$。再往后初态被显著抽空，必须计入所有阶（Weisskopf–Wigner 理论），结果是从"线性增长"过渡到初态的**指数衰减** $e^{-\Gamma t}$——同一个 $\Gamma$ 换了个身份成为寿命的倒数。

两个窗口相容的条件是 $\hbar\Gamma \ll \Delta E$：跃迁率对应的能宽远小于连续谱宽度。黄金定则失效的典型情形：(i) 末态离散（此时是两能级间的 Rabi 振荡，概率不单调）；(ii) 耦合太强（$\Gamma t$ 很快达到 1）；(iii) 连续谱有尖锐结构（如阈值附近 $\rho$ 剧烈变化）。

</details>

## 7. 例子：简谐微扰——吸收与受激辐射

把常微扰换成以频率 $\omega$ 振荡的微扰（如原子处在单色电磁波中）：

$$V(t) = W(\vec r)\,e^{-i\omega t} + W^\dagger(\vec r)\,e^{i\omega t}.$$

代入一阶振幅公式，出现两个积分，分母分别是 $\omega_{fi} - \omega$ 和 $\omega_{fi} + \omega$。各取共振项：

- **$\omega_{fi} = +\omega$（吸收）**：$E_f = E_i + \hbar\omega$，系统从场里吸收一个能量量子 $\hbar\omega$ 跃迁上去；
- **$\omega_{fi} = -\omega$（受激辐射）**：$E_f = E_i - \hbar\omega$，系统向场里放出一个 $\hbar\omega$ 跃迁下来。

对连续末态套黄金定则，吸收率

$$\Gamma_{i\to f} = \frac{2\pi}{\hbar}\,\lvert W_{fi}\rvert^2\,\rho(E_f = E_i + \hbar\omega).$$

与第 5.4 节相比，唯一的差别是能量守恒条件从 $E_f=E_i$ 平移成 $E_f = E_i \pm \hbar\omega$——微扰自身携带频率，可以"找补"能量差。

**与 Einstein 系数的关系（一句话版）**：把上式用于黑体辐射场中的原子并与 Planck 谱对比，Einstein（1917）论证出吸收与受激辐射系数相等（$B_{12}=B_{21}$），并被迫引入**自发辐射**系数 $A$，且 $A/B = \hbar\omega^3/(\pi^2 c^3)$；自发辐射本身只有在把电磁场也量子化（QED）之后才能从第一性原理推导——那时它将变成黄金定则对"原子 + 光子连续谱"的直接应用。

## 8. 通往 QFT 的桥

现在把本章的机器推向相对论。对照表如下：

- **截面 = 跃迁率 ÷ 通量**。散射实验里入射粒子流密度 $\Phi$、末态是连续谱，定义微分截面 $d\sigma = d\Gamma/\Phi$。在非相对论的 Born 近似里，把黄金定则用于盒归一化的平面波末态，就得到 $d\sigma/d\Omega = \big(\frac{m}{2\pi\hbar^2}\big)^2\big\lvert\int e^{-i\vec k'\cdot\vec r}V(\vec r)e^{i\vec k\cdot\vec r}d^3r\big\rvert^2$——跃迁率加通量，一步到位。
- **$\rho(E_f)$ 的相对论版 = Lorentz 不变相空间**。自然单位 $\hbar=c=1$ 下，每个末态粒子贡献 $d^3p/((2\pi)^3\,2E)$，能量守恒的 $\delta(E_f-E_i)$ 升级为四动量守恒的 $(2\pi)^4\delta^4(P_f - P_i)$，合起来就是 QFT 里的相空间体积元 $d\Phi_n$。态密度的角色原封不动，只是穿上了 Lorentz 协变的外衣。
- **Dyson 级数 = $S$ 矩阵**。第 5.2 节的时序指数在 QFT 里就是 $S = T\exp\!\big[-i\int \mathcal H_I\,d^4x\big]$，逐级展开、用 Wick 定理收缩，每一项对应一组费曼图——**费曼规则无非是"一路微扰下去"的系统化记账术**。
- **矩阵元 $\lvert V_{fi}\rvert^2$ → $\lvert\mathcal M\rvert^2$**。相互作用哈密顿量的矩阵元换成 Lorentz 不变振幅，黄金定则的"矩阵元平方乘相空间"结构一字不改。

一个具体的锚点：在 [QED 笔记](../stage-04-qft-core/05-qed.md)中算出的

$$\frac{d\sigma}{d\Omega}\Big(e^+e^-\to\mu^+\mu^-\Big) = \frac{\alpha^2}{4s}\big(1+\cos^2\theta\big),\qquad \sigma = \frac{4\pi\alpha^2}{3s},$$

其逻辑骨架与本章完全一样：取相互作用的**一阶**（耦合常数 $e$ 的二阶）振幅、平方、乘相空间、除以通量。区别只在于 $H_0$ 换成自由场论、$\lvert i\rangle,\lvert f\rangle$ 换成多粒子 Fock 态、非相对论态密度换成 Lorentz 不变相空间。学会本章，QFT 截面公式对你来说就不是新物理，而是"黄金定则 + 协变化"。

## 小结

- 定态微扰论（非简并）：$E_n^{(1)} = \langle n^{(0)}\rvert V\lvert n^{(0)}\rangle$，$E_n^{(2)} = \sum_{m\ne n}\lvert V_{mn}\rvert^2/(E_n^{(0)}-E_m^{(0)})$，波函数一阶修正在能量分母压制下混入近邻态。
- 简并微扰论：先在简并子空间对角化 $V$，本征值给一阶劈裂，本征矢给"好态"（Stark 效应里 $V$ 亲自挑选出 $(\lvert 2s\rangle\mp\lvert 2p\rangle)/\sqrt2$）。
- 含时微扰论：相互作用绘景把 $H_0$ 的平凡进动剥掉，态只被 $V_I$ 驱动；Dyson 级数逐级展开；一阶振幅 $c_f = -\frac{i}{\hbar}\int V_{fi}e^{i\omega_{fi}t}dt$。
- 常微扰的跃迁概率是 sinc² 峰：越高越窄、面积 $\propto t$；对连续末态求和后概率线性增长，斜率即费米黄金定则 $\Gamma = \frac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho(E_f)$，能量守恒以 $\delta(E_f-E_i)$ 出现；适用窗口 $\hbar/\Delta E \ll t \ll 1/\Gamma$。
- 简谐微扰把守恒条件平移 $\pm\hbar\omega$：吸收与受激辐射，Einstein $A$/$B$ 系数由此校准。
- 通往 QFT：截面 = 率/通量，相空间是 $\rho(E_f)$ 的协变化，$S$ 矩阵是 Dyson 级数的场论版，费曼规则是其记账术。

| 公式 | 内容 | 要害 |
| --- | --- | --- |
| $E_n^{(1)}=\langle n\rvert V\lvert n\rangle$ | 一阶能量 | 期望值 |
| $E_n^{(2)}=\sum_{m\ne n}\lvert V_{mn}\rvert^2/(E_n^{(0)}{-}E_m^{(0)})$ | 二阶能量 | 能级排斥 |
| $\det(W - \varepsilon I)=0$ | 简并劈裂 | 子空间对角化 |
| $c_f=-\frac{i}{\hbar}\int_0^t V_{fi}e^{i\omega_{fi}t'}dt'$ | 一阶振幅 | 相互作用绘景 |
| $\Gamma=\frac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho(E_f)$ | 黄金定则 | sinc² → $\delta$ |

## 自检问题

**1.** 推导非简并定态微扰论的二阶能量修正公式。

<details markdown="1"><summary>点击显示答案</summary>

把 $\lvert n\rangle = \lvert n^{(0)}\rangle + \lambda\lvert n^{(1)}\rangle + \lambda^2\lvert n^{(2)}\rangle$ 与 $E_n = E_n^{(0)}+\lambda E_n^{(1)}+\lambda^2 E_n^{(2)}$ 代入 $(H_0+\lambda V)\lvert n\rangle = E_n\lvert n\rangle$，收集 $\lambda^2$ 项：

$$(H_0 - E_n^{(0)})\lvert n^{(2)}\rangle = (E_n^{(1)} - V)\lvert n^{(1)}\rangle + E_n^{(2)}\lvert n^{(0)}\rangle.$$

左乘 $\langle n^{(0)}\rvert$：左边为零；右边利用 $\langle n^{(0)}|n^{(1)}\rangle = 0$（正交约定），得

$$E_n^{(2)} = \langle n^{(0)}\rvert V\lvert n^{(1)}\rangle.$$

代入一阶波函数修正 $\lvert n^{(1)}\rangle = \sum_{m\ne n}\frac{V_{mn}}{E_n^{(0)}-E_m^{(0)}}\lvert m^{(0)}\rangle$：

$$E_n^{(2)} = \sum_{m\ne n}\frac{V_{mn}}{E_n^{(0)}-E_m^{(0)}}\,\langle n^{(0)}\rvert V\lvert m^{(0)}\rangle = \sum_{m\ne n}\frac{\lvert V_{mn}\rvert^2}{E_n^{(0)}-E_m^{(0)}}.$$

推论：基态二阶修正恒负；近邻能级互相排斥。

</details>

**2.** 两能级系统在简并子空间中的完整计算：$H_0$ 有两个简并态 $\lvert 1\rangle, \lvert 2\rangle$（能量 $E_0$），微扰矩阵为 $W = \begin{pmatrix} a & v \\ v^* & b \end{pmatrix}$，求一阶劈裂与好态。

<details markdown="1"><summary>点击显示答案</summary>

解久期方程 $\det(W - \varepsilon I) = (a-\varepsilon)(b-\varepsilon) - \lvert v\rvert^2 = 0$：

$$\varepsilon_\pm = \frac{a+b}{2} \pm \sqrt{\left(\frac{a-b}{2}\right)^2 + \lvert v\rvert^2}.$$

一阶能量 $E_\pm = E_0 + \lambda\varepsilon_\pm$，劈裂大小

$$\Delta E = \lambda\,\sqrt{(a-b)^2 + 4\lvert v\rvert^2}.$$

注意：即使对角元相等（$a=b$），只要 $v\neq0$ 仍有劈裂 $2\lambda\lvert v\rvert$；即使 $v=0$，只要 $a\neq b$ 也劈裂。好态由 $(W-\varepsilon_\pm I)\vec c = 0$ 给出。以 $v$ 为实数为例，写成混合角形式：$c_1/c_2 = v/(\varepsilon_\pm - a)$；当 $a=b$ 时 $\varepsilon_\pm = a\pm v$，好态是对称/反对称组合 $(\lvert 1\rangle \pm \lvert 2\rangle)/\sqrt2$——与正文 Stark 效应中 $(\lvert 2s\rangle\mp\lvert 2p\rangle)/\sqrt2$ 完全同构（那里 $a=b=0$，$v=-3ea_0\mathcal{E}$）。

</details>

**3.** 写出相互作用绘景中态的演化方程，并从 Dyson 级数推出一阶跃迁振幅。

<details markdown="1"><summary>点击显示答案</summary>

定义 $\lvert\psi_I(t)\rangle = e^{iH_0t/\hbar}\lvert\psi_S(t)\rangle$。对时间求导：

$$i\hbar\partial_t\lvert\psi_I\rangle = -H_0 e^{iH_0t/\hbar}\lvert\psi_S\rangle + e^{iH_0t/\hbar}\,i\hbar\partial_t\lvert\psi_S\rangle = -H_0\lvert\psi_I\rangle + e^{iH_0t/\hbar}(H_0+V)\lvert\psi_S\rangle = V_I\lvert\psi_I\rangle,$$

其中 $V_I = e^{iH_0t/\hbar}V e^{-iH_0t/\hbar}$。演化算符满足 $U_I = 1 - \frac{i}{\hbar}\int_0^t V_I(t')U_I(t')dt'$，迭代一次（把 $U_I \approx 1$ 代入积分号内）即一阶 Dyson 项：

$$U_I^{(1)}(t) = -\frac{i}{\hbar}\int_0^t V_I(t')\,dt'.$$

初态 $\lvert i\rangle$、末态 $\lvert f\rangle$ 均为 $H_0$ 本征态，矩阵元

$$c_f(t) = \langle f\rvert U_I^{(1)}\lvert i\rangle = -\frac{i}{\hbar}\int_0^t \langle f\rvert e^{iH_0t'/\hbar}V(t')e^{-iH_0t'/\hbar}\lvert i\rangle\,dt' = -\frac{i}{\hbar}\int_0^t V_{fi}(t')\,e^{i\omega_{fi}t'}dt',$$

用到了 $e^{-iH_0t'/\hbar}\lvert i\rangle = e^{-iE_it'/\hbar}\lvert i\rangle$ 与 $\langle f\rvert e^{iH_0t'/\hbar} = e^{iE_ft'/\hbar}\langle f\rvert$，两相位合成 $e^{i(E_f-E_i)t'/\hbar} = e^{i\omega_{fi}t'}$。

</details>

**4.** 从常微扰的跃迁概率出发推导费米黄金定则，把 sinc² → δ 的极限过程写清楚。

<details markdown="1"><summary>点击显示答案</summary>

常微扰下 $P_{i\to f}(t) = \frac{\lvert V_{fi}\rvert^2}{\hbar^2}\,\frac{4\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}$。对连续末态求和转积分：

$$P(t) = \int dE_f\,\rho(E_f)\,\frac{\lvert V_{fi}\rvert^2}{\hbar^2}\,\frac{4\sin^2(\omega_{fi}t/2)}{\omega_{fi}^2}.$$

关键极限：令 $x = \omega t/2$，则

$$\int_{-\infty}^{\infty}\frac{4\sin^2(\omega t/2)}{\omega^2}\,d\omega = 2t\int_{-\infty}^{\infty}\frac{\sin^2 x}{x^2}\,dx = 2\pi t,$$

即函数列 $\frac{4\sin^2(\omega t/2)}{\omega^2}$ 峰高 $\sim t^2$、宽度 $\sim 1/t$、面积 $2\pi t$，因此

$$\frac{4\sin^2(\omega t/2)}{\omega^2} \xrightarrow{t\to\infty} 2\pi t\,\delta(\omega).$$

当 $t$ 大到峰宽远小于 $\rho\lvert V\rvert^2$ 的变化尺度时，可把缓变因子取出峰外（在 $\omega_{fi}=0$ 处取值），积分得

$$P(t) = \frac{\lvert V_{fi}\rvert^2}{\hbar^2}\,\rho\,\cdot\,2\pi t\,\delta(\omega_{fi})\ \text{的积分} = \frac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho(E_f)\Big|_{E_f=E_i}\,t,$$

其中用了 $\delta(\omega_{fi}) = \hbar\delta(E_f-E_i)$。两边除以 $t$，即

$$\Gamma = \frac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho(E_f).$$

推导的软肋在"缓变因子取出峰外"这一步：它要求连续谱足够密、$\rho$ 足够光滑，且 $t$ 不能大到一阶微扰失效（$\Gamma t\ll1$）。

</details>

**5.** 用黄金定则估算一个具体跃迁率：长度为 $L$ 的一维周期性箱子中，动量为 $\hbar k$（$k>0$）的自由粒子被弱 δ 势垒 $V(x) = g\,\delta(x)$ 散射，求它被反射（$k\to -k$）的跃迁率，并与"经典"估计（碰壁频率 × 反射概率）对比。

<details markdown="1"><summary>点击显示答案</summary>

盒归一化平面波 $\psi_k = e^{ikx}/\sqrt L$，周期边界条件要求 $k = 2\pi n/L$。

**矩阵元**：

$$V_{fi} = \langle{-k}\rvert V\lvert k\rangle = \frac{g}{L}\int e^{ikx}\delta(x)e^{ikx}dx = \frac{g}{L},\qquad \lvert V_{fi}\rvert^2 = \frac{g^2}{L^2}.$$

**态密度**（只取能量守恒的末态方向 $k'=-k$ 一侧）：$dn = \frac{L}{2\pi}dk'$，$E = \hbar^2k'^2/2m$，故

$$\rho(E) = \frac{dn}{dE} = \frac{L}{2\pi}\cdot\frac{m}{\hbar^2 k}.$$

**黄金定则**：

$$\Gamma = \frac{2\pi}{\hbar}\cdot\frac{g^2}{L^2}\cdot\frac{Lm}{2\pi\hbar^2 k} = \frac{mg^2}{\hbar^3 k\,L}.$$

**对比**：粒子以速度 $v = \hbar k/m$ 运动，单位时间撞壁 $v/L$ 次；弱 δ 势垒的反射概率（Born 近似）$R \simeq \big(\frac{mg}{\hbar^2 k}\big)^2$。于是

$$\frac{v}{L}\cdot R = \frac{\hbar k}{mL}\cdot\frac{m^2g^2}{\hbar^4 k^2} = \frac{mg^2}{\hbar^3 k\,L} = \Gamma.$$

两者精确一致：黄金定则的"率"就是经典的"尝试频率 × 单次概率"。$L$ 在最终结果中按 $1/L$ 出现——箱子越大撞壁越稀——这正是用"率"而非"概率"描述散射的正确行为；换成通量语言（除以粒子密度 $1/L$）就得到与 $L$ 无关的反射系数，这一步"率 ÷ 通量 = 截面"正是通往 QFT 截面公式的最后一块砖。

</details>

## 参考

- Griffiths《量子力学概论》（第 3 版）第 7 章（定态微扰论）、第 11 章（含时微扰论与黄金定则）——本篇的主要线索。
- Sakurai《现代量子力学》第 5 章（近似方法）——三种绘景与 Dyson 级数的更紧凑讲法。
- Shankar《Principles of Quantum Mechanics》第 17 章（定态微扰）、第 18 章（含时微扰）——推导详尽，适合跟着动手算。
