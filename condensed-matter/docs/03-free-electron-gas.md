# 金属自由电子气：Drude、Sommerfeld 与费米海

> 路线图位置：第一部分（结构与无相互作用电子）· 第 3 章
> 前置知识：本科量子力学（一维势阱的驻波量子化、Pauli 原理）；统计力学基础（巨正则系综与 Fermi–Dirac 分布——本篇直接取用，推导不作要求）；第 2 章[晶格振动与声子](02-lattice-vibrations-phonons.md)的 k 空间模式计数经验（同一套手艺）。
> 学习目标：会做 k 空间态计数（周期边界条件 → 每个态占 $(2\pi/L)^3$）；会推 $k_F = (3\pi^2 n)^{1/3}$、$E_F$、态密度 $g(E)\propto\sqrt E$，并记住量级账（$E_F\sim$ 数 eV、$T_F\sim 10^4$ K、$v_F\sim 10^6$ m/s）；理解简并判据 $T\ll T_F$ 为什么让室温金属仍是彻底量子化的"费米海"，以及为什么"只有费米面附近 $k_BT$ 薄层内的电子参与一切"；会用 Sommerfeld 展开推出电子比热 $C=\gamma T$ 与 Pauli 顺磁的常数磁化率，看清 Drude 经典图像的三场灾难如何被逐一修复。
>
> 记号约定：本书保留 $\hbar$ 与 $k_B$；电磁量用高斯单位制书写（磁化率公式中不出现 $\mu_0$；07s 章改用 SI 单位制，公式相差一个 $\mu_0$ 因子，数值结论一致）。$n$ 为传导电子数密度，$g(E)$ 为单位体积总态密度（含自旋二重），$N(E_F)$ 在磁性等上下文中指单位体积或每原子态密度，用时注明。

---

## 1. 一句话总结

**金属是一盒子被 Pauli 原理压实的量子电子气：$T=0$ 时电子从最低能态填起、把 $\vec k$ 空间填成一个实心球（费米球），球面即费米面、球面能量即费米能 $E_F\sim$ 数 eV——对应温度 $T_F\sim 10^4$ K 远高于任何金属的熔点，所以室温的金属依然是零温的那片"费米海"，只有表面 $k_BT$ 薄层内的电子能被热、电场、光扰动。Drude 的经典气体在电导上侥幸得分、在比热与磁化率上惨败；Sommerfeld 只把统计从 Maxwell–Boltzmann 换成 Fermi–Dirac（运动学一字不改），比热从 $\tfrac32 nk_B$ 崩塌为 $\gamma T$（缩小 $\sim T/T_F\approx 1\%$），磁化率从 Curie 发散变为常数——费米海从此成为全书（能带、屏蔽、RKKY、Cooper 对、Stoner、量子霍尔）的共同底座。**

## 2. Drude 模型：经典电子气的成绩单与三场灾难（1900）

Drude 刚知道电子（1897）就把它塞进了当时最成功的分子动理学：金属 = 一盒经典理想气体，电子在离子实之间自由飞行，平均每 $\tau$ 撞一次（碰撞随机化速度），其余假设一概从简。成绩与灾难并存：

**得分项**。

- 直流电导：外场 $E$ 下，两次碰撞间电子被加速 $-eE$，稳态漂移速度 $v_d = -eE\tau/m$，给出 $\boxed{\sigma = ne^2\tau/m}$。形式完全正确，$\tau$ 吸收一切微观细节。
- Wiedemann–Franz 定律：金属的 $\kappa/\sigma$ 几乎是普适常数。经典动理学同样预言比值普适（$\propto k_B/e$ 的平方），量级也对——更妙（或更险）的是 Drude 计算里记错一个因子 2，得出的数值 $2.2\times10^{-8}\ \mathrm{W\Omega K^{-2}}$ 与当时的实验几乎完全吻合。这是一场著名的巧合，见第 4.4 节。
- 金属对可见光不透明但紫外透明、良导电导热——"带电气体"的图像大方向不坏。

**灾难项**（每一场都指向同一个病根：经典统计把**所有**电子都当作活跃的）。

1. **电子比热**：经典气体每个电子贡献 $\tfrac32 k_B$。金属每原子一两个电子，若果真如此，金属比热应比绝缘体同位素固体高出约一半——实验上根本看不到，电子比热只有经典预言的百分之一量级。
2. **顺磁磁化率**：每个电子带 $1\,\mu_B$ 的磁矩，经典顺磁给 Curie 律 $\chi\propto 1/T$，降温应发散；实测金属的 $\chi$ 是与温度几乎无关的常数（第 7 章与[07s](07s-why-iron-magnetic.md)里那些 $10^{-5}$ 量级的数）。
3. **自由程**：按经典图像，电子是撞在离子实上的弹珠，平均自由程应 $\sim$ 原子间距（Å）。实测低温高纯金属中 $l$ 可达 mm 甚至 cm——经典粒子在密集离子阵列里穿行亿万个格点而不散射，除非"粒子"根本不是那样运动的。

三场灾难在 1926–1928 年被同一个手术治好：**把电子换成费米子**（Pauli 不相容 + Fermi–Dirac 统计），其余假设全留。

## 3. 费米海：Pauli 填充出来的基态

### 3.1 k 空间态计数

电子关在边长 $L$ 的盒子（体积 $V = L^3$）里自由飞行，能量 $\varepsilon(\vec k) = \hbar^2k^2/2m$。边界条件用周期边界（物理上等价于无限大材料的取样窗口，与第 2 章数声子模式同一做法）：$\psi(\vec r + L\hat x) = \psi(\vec r)$ 迫使

$$k_x = \frac{2\pi n_x}{L},\quad n_x \in \mathbb Z \qquad(\text{三分量同理}).$$

于是允许的 $\vec k$ 排成一个立方点阵，**每个态在 $\vec k$ 空间占据体积 $(2\pi/L)^3$**；再乘自旋二重：

$$\text{d}N = 2\times\frac{V}{(2\pi)^3}\,\text{d}^3k \qquad\Longrightarrow\qquad \frac{\text{d}N}{V} = \frac{2\,\text{d}^3k}{(2\pi)^3} = \frac{k^2\,\text dk}{\pi^2}.$$

$T=0$ 时 Pauli 原理下令：**每格坐一个电子，从能量最低（$k=0$）往外填**，填到总数耗尽为止——占据区是一个半径 $k_F$ 的球（费米球）。由 $\tfrac{N}{V} = 2\cdot\tfrac{4\pi}{3}k_F^3/(2\pi)^3$：

$$\boxed{\;k_F = (3\pi^2 n)^{1/3}\;},\qquad E_F = \frac{\hbar^2 k_F^2}{2m},\qquad v_F = \frac{\hbar k_F}{m}.$$

$k_F^{-1}$ 与原子间距同量级（$n\sim$ 每立方埃一个电子 $\Rightarrow k_F\sim\text{Å}^{-1}$）——费米球是原子尺度密度直接焊出来的，没有可调参数。

顺手把**态密度**积分出来（第 4、6 章与 07s 都要用）：

$$g(E) \equiv \frac{\text dn}{\text dE} = \frac{k^2}{\pi^2}\frac{\text dk}{\text dE} = \frac{1}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\!\sqrt E \;\propto\; \sqrt E,\qquad g(E_F) = \frac{3n}{2E_F}.$$

### 3.2 量级账：为什么室温的金属是"零温"的

代入真实密度（数值核对见自检问题 1）：

| | $n\ (10^{28}\,\mathrm{m^{-3}})$ | $k_F\ (\text{Å}^{-1})$ | $E_F$ (eV) | $T_F = E_F/k_B\ (10^4$ K$)$ | $v_F\ (10^6\ \mathrm{m/s})$ |
|---|---|---|---|---|---|
| Na | 2.5 | 0.92 | 3.2 | 3.8 | 1.1 |
| Cu | 8.5 | 1.36 | 7.0 | 8.1 | 1.6 |
| Al | 18.1 | 1.75 | 11.7 | 13.6 | 2.0 |

关键一行是 $T_F$：**费米温度在几万 K**，而金属熔点最多几千 K。判据 $T\ll T_F$ 在金属全部存在范围内成立——金属直到熔化都是简并的。这不是巧合：$E_F \propto \hbar^2n^{2/3}/m$ 只由密度与普适常数决定（没有任何小参数）——把电子挤到原子间距，$E_F$ 就必然是 eV 量级，量子性就不可逃避。同一个机制把电子气的简并压顶到 $P\sim(2/5)nE_F\sim$ 数万大气压（自检问题 4）——金属靠离子的库仑笼子装住这片海，白矮星靠它扛住引力（Chandrasekhar 极限的源头）。

### 3.3 费米面：金属低能物理的舞台

有限温度下占据数是 Fermi–Dirac 分布

$$f(E) = \frac{1}{e^{(E-\mu)/k_BT} + 1} \qquad\xrightarrow{\;T\to0\;}\qquad \theta(\mu - E),$$

化学势 $\mu(T)$ 在 $T\ll T_F$ 时几乎钉死在 $E_F$（偏移 $\sim(T/T_F)^2$，自检问题 2）。分布从"零温阶跃"软化成"$E_F$ 上下各约 $k_BT$ 的过渡带"——宽度 0.025 eV（300 K）对 3–12 eV 的 $E_F$，**只有约千分之几的电子态被热搅动**。这句话是金属物理的总纲：

- 加热：只有费米面薄层内的电子能吸收能量 → 比热崩塌（第 4 节）；
- 磁场：只有薄层内自旋能翻转 → Pauli 顺磁常数化（07s 第 5 节的推导正用此图像）；
- 电场：只有费米面附近的空态可被加速填充 → 输运是费米面的几何性质；
- 光：$\omega$ 超过等离子体频率 $\omega_p$ 后，电子的惯性跟不上场的快速振荡、来不及屏蔽 → 金属对远紫外近乎透明。

后文把这片占据区的边界面叫**费米面**：自由电子气里它是球；第 4 章加周期势后它被扭曲成复杂曲面——金属/绝缘体之分、de Haas–van Alphen 振荡、第 11 章的 Landau 量子化，全都挂在费米面的形状上。把电子从海里打到海面之上，海里留下一个空位（**空穴**，带 $+e$）——"电子–空穴对激发"是第 6 章粒子–空穴连续谱的主角。

## 4. Sommerfeld 修正：换统计、不换运动学

Sommerfeld（1927–28）的手术只有一处：占据数从 Boltzmann 换成 Fermi–Dirac。粒子的能谱、自由飞行、碰撞 $\tau$ 全部照旧。三场灾难逐一收账。

### 4.1 Sommerfeld 展开

要算任何 $\int\!\varphi(E) f(E)\,\text dE$ 型的热平均，标准工具是 Sommerfeld 展开（完整推导见自检问题 2）：

$$\int_0^\infty \varphi(E) f(E)\,\text dE = \int_0^{\mu}\varphi(E)\,\text dE + \frac{\pi^2}{6}(k_BT)^2\,\varphi'(\mu) + O(T^4).$$

直觉：$f$ 在 $\mu$ 处从 1 切到 0，修正项来自过渡带的"数值微分"——被积函数的导数乘过渡带宽度 $(k_BT)^2$ 的量级。对 $g\propto\sqrt E$，粒子数守恒给出 $\mu(T) \approx E_F\big[1 - \tfrac{\pi^2}{12}(T/T_F)^2\big]$，偏移可忽略。

### 4.2 比热：$\tfrac32 nk_B$ 崩塌为 $\gamma T$

对能量密度 $u = \int E\,g(E) f\,\text dE$ 用两次展开（代数见自检问题 3），$T$ 的线性修正为

$$u(T) \approx u(0) + \frac{\pi^2}{6}\,g(E_F)(k_BT)^2 \qquad\Longrightarrow\qquad \boxed{\;C_V = \frac{\partial u}{\partial T} = \frac{\pi^2}{3}g(E_F)k_B^2\,T \equiv \gamma T\;},$$

代入 $g(E_F) = 3n/2E_F$：

$$C_V = \frac{\pi^2}{2}nk_B\,\frac{T}{T_F}.$$

物理一目了然：**有效参与的电子份额 $\sim T/T_F$**（系数 $\pi^2/2$ 来自过渡带的形状）。300 K 的 Na：$T/T_F\approx0.8\%$，比热只有 Drude 值的 $\tfrac{\pi^2}{3}(T/T_F)\approx3\%$——灾难一修复，且预言了干净的 $\gamma T$ 律。实验上把低温 $C_V$ 拟合成 $C = \gamma T + \beta T^3$（电子线性项 + 声子立方项，正好是第 2 章 Debye $T^3$ 与本篇 $\gamma T$ 的相加），$\gamma$ 直接量出费米面态密度：

$$\gamma_{\text{free}} = \frac{\pi^2}{3}g(E_F)k_B^2 \qquad\text{（Na：理论 } 1.09\text{，实验 } 1.38\ \mathrm{mJ\,mol^{-1}K^{-2}}\text{）}.$$

差出的 20–30% 是相互作用对准粒子的"增重"（有效质量 $m^*$），第 6 章 Fermi 液体理论的领地；极端情形（重费米子，$\gamma$ 放大上千倍、$m^*\sim10^3 m_e$）是第 13 章强关联的招牌。

### 4.3 磁化率：Curie 发散变常数

外场把自旋向上/向下的两条态密度曲线错开 $\pm\mu_B B$，海面附近一边露出、一边淹没一薄层——又是只有 $k_BT$ 带内的电子响应。结果是

$$\chi_P = 2\mu_B^2\,g_{\text{每自旋}}(E_F) = \mu_B^2\,g(E_F) = \frac{3n\mu_B^2}{2E_F},$$

一个与温度无关的常数（完整推导在[07s 自检问题 3](07s-why-iron-magnetic.md)，那里连同 Landau 抗磁一起算了铜铝的账）。经典 Curie 的 $\chi\propto1/T$ 之所以发散，是错误地让全部电子磁矩都跟着场转；Pauli 只放行费米面薄层，发散就此掐断。**灾难二修复**。

### 4.4 输运：$\sigma = ne^2\tau/m$ 幸存，Wiedemann–Franz 从巧合转正

奇怪的是电导公式一字未改地活了下来。定性原因（自检问题 5）：稳态下**整个费米球被电场整体拖着漂移**，电流由全体电子的漂移贡献（正比于 $n$），而散射只发生在费米面附近（球内深处无空态可去）；两相抵消，Drude 的 $\sigma = ne^2\tau/m$ 形式不动——它的得分从来不是经典统计的功劳。

有了正确的比热，热导 $\kappa$ 中的"载流电子数"被换成 $\sim T/T_F$ 份额、每个载流电子的比热与速度按费米面取值，Wiedemann–Franz 比值精确化为

$$L \equiv \frac{\kappa}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^{\!2} = 2.44\times10^{-8}\ \mathrm{W\Omega K^{-2}},$$

与室温实验高度吻合——Drude 当年靠记错因子 2 "蒙中"的数值，如今有了推导。同时 $\tau$ 的微观来源也清楚了：散射者是声子（第 2 章）与杂质，Drude 设想的"撞离子实"并不存在（周期阵列根本不散射 Bloch 波，第 4 章）；低温纯金属中 $\tau$ 长到自由程 mm–cm——**灾难三修复**。

## 5. 与后续章节的接口

- **第 4 章（能带论）**：周期势把费米球扭曲成费米面；金属/绝缘体判据 = "$E_F$ 落在带内还是带隙里"；态密度的 van Hove 奇点挂在能带极值上；空穴作为"满带中的空位"正式登场。
- **第 6 章（相互作用电子气）**：凝胶模型就是给这片海加上库仑作用；交换积分在费米球内进行（交换穴半径 $\sim k_F^{-1}$）、Thomas–Fermi 屏蔽由 $g(E_F)$ 出发、Fermi 液体把"费米面 + 准粒子"结构整体继承——$\gamma$ 的增强即 $m^*/m$。
- **第 7 章/07s**：RKKY 以费米海为媒介（$2k_F$ 振荡来自直径 $2k_F$ 的费米球）、Stoner 铁磁 = 交换对抗"极化费米海的动能代价"、Pauli 顺磁的账本。
- **第 8 章（超导）**：Cooper 问题 = "费米海对任意弱的配对吸引不稳定"——对数发散正源于费米面态密度为常数；BCS 波函数是费米海的重新组织。
- **第 11 章（量子霍尔）**：强磁场把费米球切成 Landau 能级；填充因子 $\nu$ = 每能级装了几层海面。
- **第 13 章（强关联）**：重费米子的 $\gamma$ 千倍增强 = 费米海概念在强相互作用下被拉伸到极限仍在工作的证据（也是它快要失效的警报）。

## 小结

- 态计数：周期边界 → 每个 $\vec k$ 态占 $(2\pi/L)^3$，自旋 ×2；Pauli 填充 → 费米球，$k_F = (3\pi^2n)^{1/3}$，$g(E)\propto\sqrt E$，$g(E_F) = 3n/2E_F$。
- 量级：$E_F\sim$ 数 eV，$T_F\sim10^4$ K $\gg$ 熔点，$v_F\sim10^6$ m/s，$k_F^{-1}\sim$ Å。金属永远是简并的；一切响应只来自费米面 $k_BT$ 薄层。
- Drude vs Sommerfeld 账本：

| | Drude（经典） | Sommerfeld（费米海） |
|---|---|---|
| 统计 | Maxwell–Boltzmann | Fermi–Dirac，$T\ll T_F$ 简并 |
| 活跃电子 | 全部 | $E_F$ 附近 $\sim k_BT$ 薄层 |
| 电子比热 | $\tfrac32 nk_B$（大百倍） | $\gamma T$，$\gamma=\tfrac{\pi^2}{3}g(E_F)k_B^2$ |
| 磁化率 | $\propto 1/T$ 发散 | Pauli 常数 $\mu_B^2g(E_F)$ |
| 电导 | $\sigma = ne^2\tau/m$ | 同式幸存（全体漂移，表面散射） |
| WF 定律 | 记错因子 2 的巧合 | $L = \tfrac{\pi^2}{3}(k_B/e)^2$ 精确 |
| 自由程 | $\sim$ 原子间距 | 低温可达 mm–cm（无周期势散射） |

- 费米海是全书的底座语言：空穴、电子–空穴对、费米面几何、简并压都出自本篇。

## 自检问题

**1.** 从周期边界条件出发完成态计数，推出 $k_F = (3\pi^2 n)^{1/3}$ 与 $E_F$ 公式；由钠的密度（$\rho = 0.97\ \mathrm{g/cm^3}$，摩尔质量 23 g/mol，每个原子贡献 1 个传导电子）核对表格里 Na 的整行数值。

<details markdown="1"><summary>点击显示答案</summary>

**态计数**：周期边界 $e^{ik_xL} = 1$ 给 $k_x = 2\pi n_x/L$，三分量同理，允许 $\vec k$ 构成点阵，格点间距 $2\pi/L$，每态占 $\vec k$ 空间体积 $(2\pi/L)^3 = (2\pi)^3/V$。自旋 2 重：

$$N = 2\times\frac{V}{(2\pi)^3}\times\frac{4\pi}{3}k_F^3 = V\,\frac{k_F^3}{3\pi^2}\;\Longrightarrow\; n = \frac{k_F^3}{3\pi^2}\;\Longrightarrow\; k_F = (3\pi^2 n)^{1/3}.$$

**钠的数值**：$n = \rho N_A/M = \dfrac{0.97\ \mathrm{g/cm^3}}{23\ \mathrm{g/mol}}\times6.02\times10^{23}\ \mathrm{mol^{-1}} = 2.5\times10^{22}\ \mathrm{cm^{-3}} = 2.5\times10^{28}\ \mathrm{m^{-3}}$。

$$k_F = (3\pi^2\times2.5\times10^{28})^{1/3} = (7.4\times10^{29})^{1/3} \approx 9.0\times10^{9}\ \mathrm{m^{-1}} = 0.90\ \text{Å}^{-1},$$

$$E_F = \frac{\hbar^2k_F^2}{2m} = \frac{(1.055\times10^{-34})^2(9.0\times10^9)^2}{2\times9.11\times10^{-31}} \approx 4.9\times10^{-19}\ \mathrm J \approx 3.1\ \mathrm{eV},$$

$$T_F = \frac{E_F}{k_B} = \frac{3.1\ \mathrm{eV}}{8.62\times10^{-5}\ \mathrm{eV/K}} \approx 3.6\times10^4\ \mathrm K,\qquad v_F = \frac{\hbar k_F}{m} \approx 1.05\times10^6\ \mathrm{m/s}.$$

（与表中 3.2 eV、$3.8\times10^4$ K 的出入来自密度取整。）要点：全部量由密度一键锁定——原子间距 $\bar r \sim 2$ Å 的物质，$E_F$ 就必然是 eV 量级、$T_F$ 必然是几万 K，金属必然简并。

</details>

**2.** 推导 Sommerfeld 展开到 $T^2$ 阶，并证明 $\mu(T) = E_F\big[1 - \tfrac{\pi^2}{12}(T/T_F)^2 + O(T^4)\big]$。

<details markdown="1"><summary>点击显示答案</summary>

**展开**：设 $\varphi(0) = 0$，记 $F(E) = \int_0^E \varphi(E')\,\text dE'$。分部积分（$f(\infty)\to0$，$F(0)=0$）：

$$I = \int_0^\infty \varphi f\,\text dE = \int_0^\infty f\,\text dF = \big[Ff\big]_0^\infty - \int_0^\infty F\,\frac{\partial f}{\partial E}\,\text dE = \int_0^\infty F(E)\left(-\frac{\partial f}{\partial E}\right)\text dE.$$

$-\partial f/\partial E = \dfrac{1}{k_BT}\dfrac{e^{(E-\mu)/k_BT}}{\big[e^{(E-\mu)/k_BT}+1\big]^2}$ 是 $\mu$ 处宽 $\sim k_BT$ 的对称峰（归一化为 1，且各阶矩有限）。令 $E = \mu + x$ 展开 $F(\mu+x) = F(\mu) + xF'(\mu) + \tfrac12 x^2F''(\mu)+\cdots$：零阶给 $F(\mu)$；一阶奇函数对对称峰积分为零；二阶需要 $\int x^2(-\partial f/\partial x)\,\text dx = \tfrac{\pi^2}{3}(k_BT)^2$（换元 $y = x/k_BT$ 后是标准积分）。于是

$$I = F(\mu) + \frac{\pi^2}{6}(k_BT)^2\,F''(\mu) + O(T^4) = \int_0^{\mu}\varphi\,\text dE + \frac{\pi^2}{6}(k_BT)^2\,\varphi'(\mu) + O(T^4).$$

**化学势**：粒子数守恒 $n = \int_0^\infty g f\,\text dE = \int_0^{\mu} g\,\text dE + \tfrac{\pi^2}{6}(k_BT)^2 g'(\mu)$。设 $\mu = E_F + \delta$（$\delta\ll E_F$），左边在 $T=0$ 恰是 $\int_0^{E_F}g\,\text dE$，展开右端第一项 $\int_0^{E_F+\delta} = \int_0^{E_F} + g(E_F)\delta$：

$$0 = g(E_F)\,\delta + \frac{\pi^2}{6}(k_BT)^2\,g'(E_F) \;\Longrightarrow\; \delta = -\frac{\pi^2}{6}(k_BT)^2\,\frac{g'}{g}.$$

对自由电子 $g\propto E^{1/2}$，$g'/g = \tfrac{1}{2E_F}$：

$$\mu(T) = E_F\left[1 - \frac{\pi^2}{12}\left(\frac{T}{T_F}\right)^2\right].$$

300 K 的 Na：修正 $\sim(300/3.8\times10^4)^2\sim10^{-4}$——化学势在金属的全部工作温区内几乎不动，"以 $E_F$ 为化学势"是极好的近似。

</details>

**3.** 推导电子比热 $C_V = \tfrac{\pi^2}{3}g(E_F)k_B^2T$，估算 300 K 时它占 Drude 预言的比例；说明低温下如何用 $C = \gamma T + \beta T^3$ 同时定出 $\gamma$ 与 Debye $\Theta_D$。

<details markdown="1"><summary>点击显示答案</summary>

**能量**：$u = \int_0^\infty E\,g(E) f\,\text dE$。Sommerfeld 展开（取 $\varphi = Eg$）：

$$u = \int_0^{\mu} E\,g\,\text dE + \frac{\pi^2}{6}(k_BT)^2\big[g + Eg'\big]_{\mu}.$$

$\mu$ 偏离 $E_F$ 的部分要与粒子数守恒联立消去。由自检问题 2，$\mu - E_F = -\tfrac{\pi^2}{6}(k_BT)^2\,g'/g$，把第一项的积分上限写成 $E_F + (\mu - E_F)$：

$$\int_0^{\mu} Eg\,\text dE = \int_0^{E_F}Eg\,\text dE + E_F\,g\cdot(\mu - E_F) + O(T^4) = u(0) - \frac{\pi^2}{6}(k_BT)^2\,E_F\,g'.$$

代回（第三项中 $\mu$ 处取值换成 $E_F$ 处，差 $O(T^4)$）：含 $g'$ 的两项 $-E_F g'$ 与 $+E_F g'$ **恰好相消**——这是必须的：若比热依赖 $g'$，则换能量零点会改变物理，荒谬。净结果

$$u(T) = u(0) + \frac{\pi^2}{6}\,g(E_F)(k_BT)^2,$$

$$C_V = \frac{\partial u}{\partial T} = \frac{\pi^2}{3}\,g(E_F)\,k_B^2\,T = \gamma T,\qquad \gamma = \frac{\pi^2}{3}g(E_F)k_B^2 = \frac{\pi^2}{2}nk_B\frac{1}{T_F}.$$

**比例**：$\dfrac{C_V^{\text{Sommerfeld}}}{C_V^{\text{Drude}}} = \dfrac{\pi^2/2\cdot nk_B T/T_F}{3nk_B/2} = \frac{\pi^2}{3}\frac{T}{T_F}$。Na 在 300 K：$\tfrac{\pi^2}{3}\times\tfrac{300}{3.8\times10^4}\approx2.6\%$——Drude 的电子比热大了几十倍，这就是灾难一。

**实验**：低温下（$T\lesssim\Theta_D/50$）声子比热进入 Debye $T^3$ 区（第 2 章），总比热

$$C = \underbrace{\gamma T}_{\text{电子}} + \underbrace{\beta T^3}_{\text{声子}},\qquad \beta = \frac{12\pi^4}{5}\frac{nk_B}{\Theta_D^3}.$$

把数据画成 $C/T$ 对 $T^2$ 的直线：截距 = $\gamma$（量出 $g(E_F)$，直通费米面）、斜率 = $\beta$（定出 $\Theta_D$）。一条低温比热曲线同时校验本篇与第 2 章——这是固体实验的经典开场测量，也是发现"$\gamma$ 异常"（重费米子、赝能隙）的标准探针。

</details>

**4.** 证明 $T=0$ 的费米海具有"简并压" $P = \tfrac25 nE_F$，估算其数量级，并说明为什么这个压强既不把金属炸开、也不违背"零温没有热运动"。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：$T=0$ 总能量

$$U_0 = 2V\int_{k<k_F}\frac{\hbar^2k^2}{2m}\frac{\text d^3k}{(2\pi)^3} = \frac{3}{5}N E_F.$$

压强是绝热压缩的回复力：$P = -\partial U_0/\partial V\big|_N$。$N$ 固定时 $k_F\propto n^{1/3}\propto V^{-1/3}$，故 $E_F\propto V^{-2/3}$，$U_0\propto V^{-2/3}$：

$$P = \frac{2}{3}\frac{U_0}{V} = \frac{2}{3}\times\frac{3}{5}nE_F = \frac{2}{5}nE_F.$$

（对比经典气体 $P = \tfrac23 u$：简并气体因能谱 $\propto k^2$ 换成 $\tfrac25$。）

**数量级**：Na：$P = 0.4\times2.5\times10^{28}\times3.2\times1.6\times10^{-19}\ \mathrm{J\,m^{-3}} \approx 5\times10^9\ \mathrm{Pa} \approx 5\times10^4$ 大气压。

**为什么金属安然无恙**：这个压强不是热运动，而是 **Pauli 原理强制的零点运动**——把 $10^{28}$/m³ 个费米子塞进盒子，即使 $T=0$，海里绝大部分电子也必须带着 $E_F$ 量级的动能（这是 $T=0$ 的基态性质，与温度无关）。它不炸开金属，是因为离子的正电荷笼子（凝胶模型里的正背景）提供等量的库仑内聚力与之平衡；拿走引力对手时它就成为主角——白矮星正是靠电子简并压扛住自引力（质量过大则相对论软化简并压，顶不住坍缩，Chandrasekhar 极限 $\approx1.4\,M_\odot$）。同一个物理在金属与恒星里只差十个数量级的密度。

</details>

**5.** 解释为什么换成 Fermi–Dirac 统计后 $\sigma = ne^2\tau/m$ 原样幸存；并说明 Drude 的 Wiedemann–Franz "成功"如何从记错因子 2 的巧合变成 $\pi^2/3$ 的精确结果。

<details markdown="1"><summary>点击显示答案</summary>

**$\sigma$ 幸存**：稳态图像是整块费米球被电场整体漂移——每次碰撞把某个电子的 $\vec k$ 随机化（球面附近的散射把漂移动量卸掉），两次碰撞间全体电子都以 $\dot{\vec k} = -e\vec E/\hbar$ 回复漂移。漂移速度 $v_d = -(eE/m)\tau$ **与无规速度的大小无关**：快如 $v_F$ 的电子对漂移的贡献和慢电子一样只有 $v_d$ 那一份。电流 $j = -nev_d$ 中的 $n$ 仍是全部电子数——Pauli 限制的是"散射往哪去"（球内深处无空态），不限制"全体一起挪"。于是 $\sigma = ne^2\tau/m$ 分毫不动；Drude 在这一项上的成功从来与统计无关。

**WF 转正**：热导不是全体平移，而是"费米面附近电子带着能量差跑"，于是 Pauli 限制真刀真枪地砍进来：参与热输运的电子份额 $\sim T/T_F$，每个的比热换成 $\gamma T$ 线性律，速度按 $v_F$ 取。定量地，动理学给 $\kappa = \tfrac13 C_V v_F^2\tau$，与 $\sigma$ 共用同一个 $\tau$：

$$L = \frac{\kappa}{\sigma T} = \frac{\tfrac13\,\gamma T\, v_F^2\,\tau}{\dfrac{ne^2\tau}{m}\,T} = \frac{1}{3}\,\frac{\gamma\, m v_F^2}{ne^2} = \frac{1}{3}\,\frac{\gamma\cdot 2E_F}{ne^2}.$$

代入 $\gamma = \tfrac{\pi^2}{3}g(E_F)k_B^2$ 与 $g(E_F)E_F = \tfrac32 n$：

$$L = \frac{1}{3}\cdot\frac{\pi^2}{3}\,k_B^2\cdot\frac{2\,g(E_F)E_F}{ne^2} = \frac{1}{3}\cdot\frac{\pi^2}{3}\cdot\frac{3\,k_B^2}{e^2} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^{\!2} = 2.44\times10^{-8}\ \mathrm{W\Omega K^{-2}}.$$

经典 Drude 若不算错，应得 $\tfrac32(k_B/e)^2 = 1.11\times10^{-8}$；他当年把热导多记了一倍因子，得 $2.2\times10^{-8}$，恰好砸中实验——所以经典版本是**错误互相抵消的巧合**，Sommerfeld 版本则每个因子都有出处。顺带：$\kappa$ 与 $\sigma$ 共享 $\tau$ 意味着 WF 定律只在"热与电被同一批散射主导"时严格成立（高温声子散射区最好），低温下非弹性散射差异会让它偏离——这本身又成了区分散射机制的探针。

</details>

## 参考

- Kittel《固体物理导论》（第 8 版）第 6 章：自由电子费米气——费米能、态密度、 Sommerfeld 比热与费米面，本章主线。
- Ashcroft & Mermin《Solid State Physics》第 1–3 章：Drude 模型及其失败清单（第 1 章）、Sommerfeld 模型与比热/输运的完整推导（第 2 章）、失败项的逐条清算（第 3 章）——Wiedemann–Franz 巧合的历史注记也在其中。
- 黄昆《固体物理学》相应章节：中文教材视角的自由电子气与态密度。
- Coleman《Introduction to Many-Body Physics》第 1 章：费米海作为多体物理起点的现代讲法（衔接第 6 章）。
