# 补充材料：变分法与 WKB——不依赖小参数的两种近似武器

> 路线图位置：量子力学书 · 第三部分（近似方法）· 第 07 篇[微扰论](07-perturbation-theory.md)的补充材料（第 07s 篇）
> 前置知识：第 03 篇（[形式体系：希尔伯特空间与 Dirac 记号](03-formalism-hilbert-dirac.md)，期望值、本征展开）；第 06 篇（[氢原子与电子亚层](06-hydrogen-and-subshells.md)，类氢 1s 波函数与能级——氦原子例题要用）；第 07 篇（[微扰论](07-perturbation-theory.md)，作为全程对照）。
> 学习目标：会用变分原理估基态能量，并理解其误差是波函数误差的二阶这一深层原因；会从 $\hbar$ 半经典展开推出 WKB 波函数、连接公式与量子化条件；会把隧穿指数 $e^{-2\gamma}$ 用到方势垒、双阱与 $\alpha$ 衰变问题。
>
> 记号约定：本篇保留 $\hbar$（量子力学阶段惯例，不取自然单位；$h = 2\pi\hbar$ 只在量子化条件中出现一次）。$e^2/(4\pi\varepsilon_0)$ 在氦原子计算中出现，玻尔半径 $a_0 = 4\pi\varepsilon_0\hbar^2/(m_e e^2) \approx 0.529$ Å，哈特里能量 $e^2/(4\pi\varepsilon_0 a_0) = 27.2$ eV $= 2\times13.6$ eV，均在文中出现处使用。

---

## 1. 一句话总结

**微扰论的全部威力来自"有一个小参数可以展开"，可许多物理恰恰活在小参数之外：强耦合系统没有可拆的 $H_0$，隧穿振幅 $e^{-S/\hbar}$ 对任何耦合常数都展不出幂级数；这时两件非微扰武器登场——变分法不求精确解，直接利用"基态是能量泛函的最小值"这一变分原理，用带参数的试探波函数压出基态能量的上限，且能量误差是波函数误差的二阶，所以粗糙的猜测也能交出像样的数字；WKB 则反其道而行，把 $\hbar$ 本身当作小参数展开，$\psi \sim p(x)^{-1/2}e^{\pm i\int p\,dx/\hbar}$ 把波函数写成"局域动量 + 缓变振幅"，转折点处用 Airy 函数缝出连接公式，于是量子化条件 $\oint p\,dx = (n+\tfrac12)h$ 里多出的那个 $+\tfrac12$（Maslov 指标）恰好补回旧量子论丢掉的零点能，禁区的指数衰减则给出一切隧穿问题的通用答案 $T \sim e^{-2\gamma}$。**

## 2. 为什么需要非微扰武器

第 07 篇的机器有一个隐蔽的前提：$H = H_0 + \lambda V$ 必须**可拆**——存在一个会解的 $H_0$，且 $\lambda V$ 足够小，使得按 $\lambda$ 的幂级数展开有意义。大量真实问题不满足这一条：

- **强耦合**：氦原子的电子–电子排斥 $e^2/(4\pi\varepsilon_0 r_{12})$ 与电子–核吸引同量级（都在几十 eV），把它当"微扰"在数学上能算（第 07 篇风格的算给 $-74.8$ eV），但级数从一开始就收敛得勉勉强强；多电子原子、强关联电子系统更不必说。
- **隧穿与衰变**：粒子穿过经典禁区的概率形如 $e^{-2\gamma}$，其中 $\gamma \propto 1/\hbar$ 或正比于势垒宽。这样的函数在"小参数"原点处的所有阶导数都是零——**它对任何微扰级数都是隐形的**，可它偏偏就是 $\alpha$ 衰变、扫描隧道显微镜、双阱劈裂的全部物理。
- **根本没有 $H_0$**：有些势阱形状古怪，连"主要部分"都挑不出来，微扰论无处下手。

本篇的两件武器对应两条出路：变分法放弃"逐级逼近精确解"，改为直接利用**基态的极值性质**做有方向（只高不低）的估计；WKB 则换一个展开参数——不展开耦合常数，展开 $\hbar$ 本身，得到的是半经典世界（$\hbar \to 0$）附近的系统性近似。两者都不需要 $H$ 可拆。

## 3. 变分原理：基态能量是个最小值

### 3.1 变分原理的完整证明

设 $H$ 有下界（基态存在），其本征值排序 $E_0 \le E_1 \le \cdots$，对应本征态 $\lvert n\rangle$ 构成完备正交归一基。任取可归一化态 $\lvert\psi\rangle$（不要求归一），按本征基展开 $\lvert\psi\rangle = \sum_n c_n\lvert n\rangle$，则

$$\frac{\langle\psi\rvert H\lvert\psi\rangle}{\langle\psi\vert\psi\rangle} = \frac{\sum_n E_n\lvert c_n\rvert^2}{\sum_n\lvert c_n\rvert^2} \ge \frac{\sum_n E_0\lvert c_n\rvert^2}{\sum_n\lvert c_n\rvert^2} = E_0.$$

即**任何态的能量期望值都是基态能量的上限**：

$$\boxed{E_0 \le \frac{\langle\psi\rvert H\lvert\psi\rangle}{\langle\psi\vert\psi\rangle}}$$

等号成立当且仅当 $\lvert\psi\rangle$ 完全落在基态子空间里（所有 $E_n > E_0$ 的分量 $c_n = 0$）。证明只有一行不等式，但它把"求基态能量"这个本征值问题变成了**最小化问题**：在所有试探态上找期望值的最小值。

实操（Rayleigh–Ritz 程序）：选一个含参数 $\alpha_1, \alpha_2, \dots$ 的试探函数族 $\psi(\vec r; \alpha_i)$，计算

$$E(\alpha_i) = \frac{\langle\psi(\alpha_i)\rvert H\lvert\psi(\alpha_i)\rangle}{\langle\psi(\alpha_i)\vert\psi(\alpha_i)\rangle},$$

对参数极小化 $\partial E/\partial\alpha_i = 0$。最小值 $E_{\min}$ 是 $E_0$ 的上限，且**永远只高不低**——这与微扰论的结果方向不定形成鲜明对比（第 07 篇的一阶修正可正可负）。

### 3.2 激发态推广：正交约束下的 Rayleigh–Ritz

同样的逻辑可以逐层向上爬。若试探态被强制与真实基态正交，$\langle\psi_0\vert\psi\rangle = 0$，则展开式中 $c_0 = 0$，同样的不等式给出

$$\frac{\langle\psi\rvert H\lvert\psi\rangle}{\langle\psi\vert\psi\rangle} \ge E_1.$$

问题在于我们不知道 $\lvert\psi_0\rangle$。替代方案有二：(i) 用**对称性**保证正交——例如中心势中 $l=1$ 的试探态自动与 $l=0$ 基态正交，宇称奇的试探态自动与宇称偶基态正交，于是可以放心估最低 $p$ 态、最低奇宇称态的能量；(ii) 用已得到的最优近似基态 $\lvert\tilde\psi_0\rangle$ 代替真实基态做正交化，误差受控但更微妙。更系统的版本是 Rayleigh–Ritz 矩阵法：取 $N$ 个线性无关试探函数张成子空间，在其中把 $H$ 的 $N\times N$ 矩阵对角化，得到的 $N$ 个本征值**从上方**逼近真实的前 $N$ 个本征值（这是 minimax 原理/Hylleraas–Undheim 定理的内容，本篇不证）——量子化学里的 Hartree–Fock 与组态相互作用本质上都是这一句话的大规模执行。

### 3.3 深层原因：能量误差是波函数误差的二阶

变分法好用得近乎不讲道理：粗糙的试探函数常交出百分位精度的能量。原因是**能量泛函在本征态处是平稳的**。设真实基态 $\lvert\psi_0\rangle$（已归一），试探态写成 $\lvert\psi\rangle = \lvert\psi_0\rangle + \varepsilon\lvert\varphi\rangle$，其中 $\langle\psi_0\vert\varphi\rangle = 0$（总可以通过调整相位与归一化做到，归一化差异只贡献二阶以上），$\varepsilon$ 衡量波函数的误差。则

$$\langle\psi\vert\psi\rangle = 1 + \varepsilon^2\langle\varphi\vert\varphi\rangle,$$

$$\langle\psi\rvert H\lvert\psi\rangle = E_0 + \varepsilon\,\big(\langle\varphi\rvert H\lvert\psi_0\rangle + \langle\psi_0\rvert H\lvert\varphi\rangle\big) + \varepsilon^2\langle\varphi\rvert H\lvert\varphi\rangle = E_0 + \varepsilon^2\langle\varphi\rvert H\lvert\varphi\rangle,$$

一阶项因 $H\lvert\psi_0\rangle = E_0\lvert\psi_0\rangle$ 与正交条件而消失。相除得

$$E[\psi] = E_0 + \varepsilon^2\,\langle\varphi\rvert (H - E_0)\lvert\varphi\rangle + O(\varepsilon^3).$$

两点读法：(i) **一阶误差为零**——波函数差 $O(\varepsilon)$，能量只差 $O(\varepsilon^2)$；(ii) 修正项是正定算符 $H - E_0$ 的期望值，**恒非负**——这从泛函层面再次解释了"只高不低"。第一条是变分法精度的来源，第二条是它可靠性的来源。对照第 07 篇：微扰论里能量修正与波函数修正是**同阶**的（一阶能量对一阶波函数），变分法在这个意义上"白赚一阶"。

## 4. 例题一：高斯试探函数估氢原子基态

流程演示题。氢原子 $H = -\dfrac{\hbar^2}{2m_e}\nabla^2 - \dfrac{e^2}{4\pi\varepsilon_0 r}$，精确解 $E_0 = -13.6$ eV、$\psi_0 \propto e^{-r/a_0}$（第 06 篇）。**假装不会解**，取球对称高斯试探族

$$\psi(r; \alpha) = \left(\frac{2\alpha}{\pi}\right)^{3/4}e^{-\alpha r^2},$$

参数 $\alpha > 0$ 控制宽度（系数已归一）。逐项算期望值：

- **动能**：由 $-\nabla^2\psi = (6\alpha - 4\alpha^2 r^2)\psi$ 与高斯矩 $\langle r^2\rangle = 3/(4\alpha)$，得

$$\langle T\rangle = \frac{\hbar^2}{2m_e}\big(6\alpha - 4\alpha^2\cdot\tfrac{3}{4\alpha}\big) = \frac{3\hbar^2\alpha}{2m_e}.$$

- **势能**：高斯矩 $\langle 1/r\rangle = 2\sqrt{2\alpha/\pi}$，得

$$\langle V\rangle = -\frac{e^2}{4\pi\varepsilon_0}\,2\sqrt{\frac{2\alpha}{\pi}}.$$

能量函数

$$E(\alpha) = \frac{3\hbar^2}{2m_e}\,\alpha - \frac{2e^2}{4\pi\varepsilon_0}\sqrt{\frac{2\alpha}{\pi}}.$$

第一项（动能）随 $\alpha$ 增大而升——波函数越窄曲率越大；第二项（吸引能）随 $\alpha$ 增大而降——越靠近核越划算。极小化 $dE/d\alpha = 0$ 给出两者竞争的最优宽度

$$\alpha_{\min} = \frac{8}{9\pi a_0^2}\qquad\Longleftrightarrow\qquad \text{特征宽度}\ \alpha_{\min}^{-1/2} = \sqrt{\frac{9\pi}{8}}\,a_0 \approx 1.88\,a_0,$$

代回（注意极小点处动能恰为总能量绝对值、势能为其两倍——位力定理的变分版）：

$$E_{\min} = -\frac{4}{3\pi}\cdot\frac{\hbar^2}{m_e a_0^2} = -\frac{8}{3\pi}\times 13.6\ \text{eV} \approx -11.5\ \text{eV}.$$

对照精确值 $-13.6$ eV：上限确实成立（$-11.5 > -13.6$），相对误差 $15\%$。这个例子的教育意义正在于误差不算小：高斯在 $r\to0$ 处太平滑（真实波函数在核处有尖点 $d\psi/dr \neq 0$）、在远处衰减过快，**波函数形状差得很**，可能量只差 $15\%$——这正是 3.3 节"能量误差是波函数误差二阶"的现场演示。若改用正确函数形 $e^{-\beta r}$ 做试探族，变分程序会直接命中精确解（自检问题 2 的对照组）。

## 5. 例题二：氦原子基态——有效电荷变分

这道题做透，它是变分法的第一枚历史性勋章。氦原子哈密顿量（核 $Z=2$ 固定于原点，无限质量近似）：

$$H = \underbrace{-\frac{\hbar^2}{2m_e}\nabla_1^2 - \frac{2e^2}{4\pi\varepsilon_0 r_1} - \frac{\hbar^2}{2m_e}\nabla_2^2 - \frac{2e^2}{4\pi\varepsilon_0 r_2}}_{H_0\ \text{（两个独立类氢离子）}} + \underbrace{\frac{e^2}{4\pi\varepsilon_0\,\lvert\vec r_1 - \vec r_2\rvert}}_{V_{ee}\ \text{（电子–电子排斥）}}.$$

### 5.1 物理图像与试探函数

每个电子都被核吸引，同时被另一个电子**屏蔽**——站在电子 1 的位置看，电子 2 的电子云平均抵消掉一部分核电荷，等效核电荷介于 1 与 2 之间。干脆把这个物理图像直接做成试探函数：取两个**有效电荷 $Z_{\mathrm{eff}}$ 的类氢 1s 轨道**之积

$$\psi(\vec r_1, \vec r_2; Z_{\mathrm{eff}}) = \frac{Z_{\mathrm{eff}}^3}{\pi a_0^3}\,e^{-Z_{\mathrm{eff}}(r_1+r_2)/a_0},$$

以 $Z_{\mathrm{eff}}$ 为变分参数（空间部分对称，自旋部分取反对称单态，Pauli 原理自动满足）。$Z_{\mathrm{eff}} = 2$ 对应无屏蔽，$Z_{\mathrm{eff}} = 1$ 对应完全屏蔽，最优值由能量自己挑。

### 5.2 $\langle H\rangle(Z_{\mathrm{eff}})$ 的各项

把 $H$ 按"动能 + 核吸引 + 电子排斥"三块算。技巧：动能项只对**试探函数自己的动能算符**对角，核吸引项里的电荷是真实的 2，不是 $Z_{\mathrm{eff}}$。

- **动能**（每个电子）：类氢 1s 的动能期望值为 $Z_{\mathrm{eff}}^2\times13.6$ eV（由 $E = -Z^2\cdot13.6$ eV 与库仑位力 $T = -E$ 读出），两个电子共

$$\langle T\rangle = 2\times 13.6\,Z_{\mathrm{eff}}^2\ \text{eV}.$$

- **核吸引**（每个电子）：$\langle 1/r\rangle = Z_{\mathrm{eff}}/a_0$，真实核电荷 2，故

$$\langle V_{\mathrm{nuc}}\rangle = -2\times\frac{2e^2}{4\pi\varepsilon_0}\cdot\frac{Z_{\mathrm{eff}}}{a_0} = -4Z_{\mathrm{eff}}\times 27.2\ \text{eV}.$$

- **电子–电子排斥**：对两个电荷密度各为 $e\lvert\psi_{1s}\rvert^2$ 的球对称指数云做经典静电能积分（先算一个云在另一个云产生的势中的能量，球壳定理分层积分），结果是 Griffiths 第 7 章的标准积分

$$\left\langle\frac{e^2}{4\pi\varepsilon_0\,r_{12}}\right\rangle = \frac{5}{8}Z_{\mathrm{eff}}\cdot\frac{e^2}{4\pi\varepsilon_0 a_0} = \frac{5}{4}Z_{\mathrm{eff}}\times 13.6\ \text{eV}.$$

三项相加（以 13.6 eV 为单位）：

$$E(Z_{\mathrm{eff}}) = \Big(2Z_{\mathrm{eff}}^2 - 8Z_{\mathrm{eff}} + \tfrac54 Z_{\mathrm{eff}}\Big)\times 13.6\ \text{eV} = \Big(2Z_{\mathrm{eff}}^2 - \tfrac{27}{4}Z_{\mathrm{eff}}\Big)\times 13.6\ \text{eV}.$$

### 5.3 极小化与数值

$$\frac{dE}{dZ_{\mathrm{eff}}} = \Big(4Z_{\mathrm{eff}} - \tfrac{27}{4}\Big)\times 13.6\ \text{eV} = 0 \quad\Longrightarrow\quad Z_{\mathrm{eff}} = \frac{27}{16} = 1.69.$$

最优有效电荷 1.69：每个电子平均被屏蔽掉约 0.31 份核电荷——物理图像定量兑现。代回：

$$E_{\min} = \Big(2\cdot\tfrac{729}{256} - \tfrac{27}{4}\cdot\tfrac{27}{16}\Big)\times 13.6\ \text{eV} = -\frac{729}{128}\times 13.6\ \text{eV} \approx -77.5\ \text{eV}.$$

对照表（实验值取自氦的双重电离能之和）：

| 方法 | $E_0$（eV） | 与实验的偏差 |
| --- | --- | --- |
| 微扰论一阶（$Z_{\mathrm{eff}}$ 固定为 2） | $-74.8$ | 4.2 eV（5.3%） |
| 单参数变分（$Z_{\mathrm{eff}} = 27/16$） | $-77.5$ | 1.5 eV（1.9%） |
| 实验 | $-79.0$ | — |

一句话对照：微扰论把 $V_{ee}$ 当小修正、一步不动波函数；变分法只是把波函数的宽度交给能量自己决定，就把误差砍掉近三分之二——而且保证只高不低。继续加码参数（Hylleraas 用含 $r_{12}$ 的关联坐标试探族，6 参数即达 $-79.01$ eV）可以无限逼近实验，变分法是多电子问题从定性到定量的主干道。

## 6. 变分法的品格与失效清单

变分法不是万能药，用之前先认清它的脾气：

- **只给上限，不给误差棒**。$E_{\min} \ge E_0$ 恒成立，但"离 $E_0$ 多近"原则上不知道——只能说"加参数后能量降不动了，大概收敛了"。两个不同试探族给出两个上限，较低者胜，仅此而已。
- **能量准不等于一切都准**。变分优化的是能量泛函，波函数的其他性质（远端渐近、偶极矩、其他算符的期望值）精度没有保证——它们是一阶误差，不像能量那样享受二阶保护。氦例中 $Z_{\mathrm{eff}} = 1.69$ 的乘积波函数完全不含电子关联（$r_{12}$ 依赖），用它算双电子同时近核的性质会错得离谱。
- **激发态需要正交化**（3.2 节），而正交化依赖已得的近似低能态，误差会逐层累积；没有对称性保驾护航时，估激发态远比估基态心虚。
- **试探族选错会被严重误导**。变分法只能在你给的函数族里找最优，族里若没有正确物理（比如用实函数去描述携带电流的态、用无节点函数去估第一激发态），再卖力极小化也只是在错误的方向上精益求精。试探函数是物理直觉的载体——氦例之所以漂亮，是因为"有效电荷"这个图像本身就是对的。

## 7. WKB：把 $\hbar$ 当小参数展开

### 7.1 半经典展开到前两阶

一维定态薛定谔方程

$$-\frac{\hbar^2}{2m}\psi'' + V(x)\psi = E\psi \qquad\Longleftrightarrow\qquad \psi'' = -\frac{p(x)^2}{\hbar^2}\psi,\quad p(x) \equiv \sqrt{2m\big(E - V(x)\big)}.$$

$p(x)$ 是经典粒子在该点的局域动量（经典允许区 $E > V$ 时为实）。作指数 ansatz（对振荡与衰减同样适用）：

$$\psi(x) = e^{iS(x)/\hbar},$$

代入得 $S$ 的方程

$$-i\hbar S'' + (S')^2 = p(x)^2.$$

到目前为止严格，一步近似没做。现在展开 $S = S_0 + \hbar S_1 + \hbar^2 S_2 + \cdots$（把 $\hbar$ 本身当小参数），逐阶比较：

- **$\hbar^0$ 阶**：$(S_0')^2 = p^2$，即 $S_0 = \pm\displaystyle\int^x p(x')\,dx'$——相位就是经典作用量；
- **$\hbar^1$ 阶**：$-iS_0'' + 2S_0'S_1' = 0$，即 $S_1' = \dfrac{iS_0''}{2S_0'} = \dfrac{i}{2}\dfrac{p'}{p}$，积分得 $S_1 = \dfrac{i}{2}\ln p$。

代回 $\psi = e^{iS_0/\hbar}\,e^{iS_1} = p^{-1/2}e^{\pm i\int p\,dx/\hbar}$，即 **WKB 波函数**

$$\boxed{\psi_{\mathrm{WKB}}(x) = \frac{A}{\sqrt{p(x)}}\,e^{\pm\frac{i}{\hbar}\int^x p(x')\,dx'}}\qquad (E > V)$$

振幅 $\propto p^{-1/2}$ 有直接的经典读法：$\lvert\psi\rvert^2 \propto 1/p \propto 1/v$——粒子在动量小（速度慢）处停留时间长，被发现概率大，这正是经典力学"在区域内随机时刻观察"的概率密度。量子波函数在半经典极限下记住了经典的停留时间。经典禁区（$E < V$）里 $p = i\lvert p\rvert$ 为纯虚，同一公式给出指数涨落

$$\psi_{\mathrm{WKB}}(x) = \frac{C}{\sqrt{\lvert p(x)\rvert}}\,e^{\pm\frac{1}{\hbar}\int^x \lvert p(x')\rvert\,dx'}.$$

### 7.2 适用条件与转折点失效

展开合法的判据：被丢掉的 $\hbar^2$ 阶远小于保留项，等价于

$$\left\lvert\frac{d\bar{\lambda}}{dx}\right\rvert \ll 1,\qquad \bar{\lambda}(x) = \frac{\hbar}{p(x)},$$

即**约化德布罗意波长在一个波长的距离内变化很小**——势 $V(x)$ 在局域波长尺度上缓变。这个条件在**转折点**（$E = V(x)$，$p \to 0$）处必然失效：波长发散，无论 $\hbar$ 多小。转折点是经典允许区与禁区的接缝，WKB 解在两侧各自成立，必须另想办法把它们缝起来。

### 7.3 连接公式：Airy 函数一句话

缝合办法一句话交代：在转折点 $x = a$ 附近把势线性化，$V(x) - E \approx F(x - a)$，薛定谔方程严格化为 **Airy 方程** $u'' = \xi u$（$\xi \propto x - a$），其解 Airy 函数 $\mathrm{Ai}(\xi)$、$\mathrm{Bi}(\xi)$ 一侧振荡、一侧指数；把 Airy 解的渐近形式与两侧 WKB 解匹配（这一步严格做要走复平面绕过转折点，即 Stokes 现象），得到**连接公式**。以右转折点（允许区在左 $x < a$）为例：

$$\frac{2A}{\sqrt{p(x)}}\cos\left(\frac{1}{\hbar}\int_x^a p\,dx' - \frac{\pi}{4}\right) \;\longleftrightarrow\; \frac{A}{\sqrt{\lvert p(x)\rvert}}\,e^{-\frac{1}{\hbar}\int_a^x \lvert p\rvert\,dx'},$$

$$\frac{A}{\sqrt{p(x)}}\sin\left(\frac{1}{\hbar}\int_x^a p\,dx' - \frac{\pi}{4}\right) \;\longleftrightarrow\; -\frac{A}{\sqrt{\lvert p(x)\rvert}}\,e^{+\frac{1}{\hbar}\int_a^x \lvert p\rvert\,dx'}.$$

记忆要点：禁区里衰减的解接到允许区里**相移 $-\pi/4$ 的余弦**上，且衰减解对应系数 2 倍的余弦；增长的指数对应正弦。左转折点公式镜像对称（$\int_a^x$ 换成 $\int_x^a$，相位同样 $-\pi/4$）。推导细节见朗道 §47 或 Griffiths 第 8 章，本篇直接用。

### 7.4 束缚态量子化条件：$\oint p\,dx = (n+\tfrac12)h$

考虑双转折点势阱 $a < b$（阱内允许、两外侧禁区）。物理上可接受的波函数在两个禁区都必须衰减，于是

- 从右转折点 $b$ 连接回来：$\psi \approx \dfrac{2C}{\sqrt p}\cos\left(\dfrac{1}{\hbar}\displaystyle\int_x^b p\,dx' - \dfrac{\pi}{4}\right)$；
- 从左转折点 $a$ 连接过去：$\psi \approx \dfrac{2C'}{\sqrt p}\cos\left(\dfrac{1}{\hbar}\displaystyle\int_a^x p\,dx' - \dfrac{\pi}{4}\right)$。

两式描述阱内同一个波函数。把第二式的相位改写：$\displaystyle\int_a^x = \int_a^b - \int_x^b$，记 $\Phi \equiv \dfrac{1}{\hbar}\displaystyle\int_a^b p\,dx$，则第二式 $\propto \cos\left(\Phi - \dfrac{\pi}{2} - \theta\right)$，其中 $\theta = \dfrac{1}{\hbar}\displaystyle\int_x^b p\,dx - \dfrac{\pi}{4}$ 是第一式的相位。要求 $\cos\theta = \pm\cos(\Phi - \pi/2 - \theta)$ 对所有 $x$ 成立，当且仅当

$$\Phi - \frac{\pi}{2} = n\pi,\qquad n = 0, 1, 2, \dots$$

即 $\displaystyle\int_a^b p\,dx = (n + \tfrac12)\pi\hbar$。往返一趟（去程加回程）相空间中轨道所围面积为两倍：

$$\boxed{\oint p\,dx = \left(n + \tfrac12\right)h}$$

**重点强调那个 $+\tfrac12$**：第 01 篇[旧量子论](01-old-quantum-theory.md)的 Bohr–Sommerfeld 条件是 $\oint p\,dx = nh$，谐振子给出 $E_n = nh\omega$——缺了零点能 $\hbar\omega/2$，这是旧量子论著名的硬伤之一。WKB 把同一形式的量子化条件找回来，但每个转折点的连接贡献 $-\pi/4$ 的相位损失，两个转折点共 $-\pi/2$，折算成相空间积分里的 $+\tfrac12$（这个整数叫作 **Maslov 指标**）。零点能不是"量子力学额外塞进来的"，而是**波在转折点上反射时的相位亏损**——半经典分析把旧量子论缺的那一半精确补上，首尾呼应。

## 8. 应用

### 8.1 验证：谐振子能级精确复现

谐振子 $V = \tfrac12 m\omega^2x^2$，能量 $E$ 的转折点在 $x_0 = \sqrt{2E/(m\omega^2)}$。相空间积分：

$$\oint p\,dx = 2\int_{-x_0}^{x_0}\sqrt{2mE - m^2\omega^2x^2}\,dx = 2\pi\frac{E}{\omega}$$

（椭圆面积：相空间轨道是半轴 $\sqrt{2mE}$ 与 $\sqrt{2E/(m\omega^2)}$ 的椭圆，面积 $\pi$ 乘两半轴）。量子化条件 $2\pi E/\omega = (n+\tfrac12)2\pi\hbar$ 给出

$$E_n = \left(n + \tfrac12\right)\hbar\omega,$$

与第 04 篇升降算符的精确解**完全一致**。这不是巧合的偶然：谐振子的 WKB 高阶修正（$\hbar^2$ 阶及以上）逐项相消，半经典近似对二次势是严格的。对一般势阱 WKB 能级只是近似，但对"墙不太陡"的阱，低能级精度常优于 1%。

### 8.2 势垒透射：$T \sim e^{-2\gamma}$

能量 $E$ 的粒子射向高度宽度任意的势垒 $V(x) > E$（$a < x < b$ 为经典禁区）。贯穿垒区的 WKB 波函数以衰减为主，振幅从入射侧到出射侧缩水 $e^{-\gamma}$，概率缩水其平方：

$$\boxed{T \approx e^{-2\gamma},\qquad \gamma = \frac{1}{\hbar}\int_a^b \lvert p(x)\rvert\,dx = \frac{1}{\hbar}\int_a^b\sqrt{2m\big(V(x) - E\big)}\,dx}$$

这个"指数压死一切"的结构与势垒形状无关，是 WKB 对隧穿问题的通用答案。与精确结果的对照：宽度 $a$、高度 $V_0$ 的**方势垒**有严格解（见第 03s 篇[波动力学基础](03s-wave-mechanics-basics.md)的势垒散射一节）

$$T = \left[1 + \frac{V_0^2\,\sinh^2(\kappa a)}{4E(V_0 - E)}\right]^{-1},\qquad \kappa = \frac{\sqrt{2m(V_0-E)}}{\hbar}.$$

厚垒极限 $\kappa a \gg 1$：$\sinh\kappa a \to \tfrac12 e^{\kappa a}$，于是

$$T \;\longrightarrow\; \frac{16E(V_0 - E)}{V_0^2}\,e^{-2\kappa a}.$$

WKB 给出 $\gamma = \kappa a$、$T \sim e^{-2\kappa a}$——**指数部分精确一致**，只差一个量级为 1 的前置因子。指数决定数量级，前置因子只动百分数：这就是"WKB 抓指数"的含义。注意 $T \sim e^{-2\gamma}$ 在 $\gamma \gtrsim 1$（厚垒）时才自洽；$\gamma \to 0$ 时 $T \to 1$ 被正确内置于"近似只在指数大时有效"这句话里。

### 8.3 双阱劈裂与 Gamow 的 $\alpha$ 衰变（各一句话）

- **双阱**：对称双阱中，粒子在两阱间隧穿使每个能级劈成对称/反对称双重态，劈裂 $\Delta E \propto e^{-\gamma}$（$\gamma$ 是中间垒区的衰减指数）——NH₃ 反转频率、Josephson 结、奇异核的形变同质异能态都是这个指数在唱主角，而它对微扰论完全隐形（8 节开头的问题在此闭环）。
- **$\alpha$ 衰变**：Gamow（1928）把 $\alpha$ 粒子在核外的库仑垒透射指数算出，$\gamma \propto Z/\sqrt{E}$，于是寿命 $\ln\tau = A + B Z/\sqrt{E}$——正是经验上的 Geiger–Nuttall 定律，同位素间寿命差 20 多个数量级全由一个指数积分解释。这是 WKB 思想（准经典近似）在核物理的处女秀，也是量子隧穿第一次被实验定量确认。

## 小结

- 变分原理：任意态的能量期望值 $\ge E_0$，等号仅当基态；证明是一行谱分解不等式。实操即 Rayleigh–Ritz：带参数试探函数、算 $\langle H\rangle$、极小化，结果只高不低。
- 变分法好用的深层原因：能量泛函在本征态处平稳，能量误差是波函数误差的**二阶**且正定；激发态须靠对称性或正交化逐层推进。
- 例题账本：高斯试探函数给氢基态 $-11.5$ eV（误差 15%，波函数差但能量不太差）；氦原子 $Z_{\mathrm{eff}} = 27/16$ 给出 $-77.5$ eV，介于微扰论 $-74.8$ eV 与实验 $-79.0$ eV 之间且方向确定。
- 失效清单：只给上限无误差棒；非能量量不享二阶保护；激发态心虚；试探族选错会被系统性误导。
- WKB：$\psi = e^{iS/\hbar}$ 展开到两阶给 $\psi \sim p^{-1/2}e^{\pm i\int p\,dx/\hbar}$，适用条件 $\lvert d\bar{\lambda}/dx\rvert \ll 1$，转折点必失效；转折点邻域严格解是 Airy 函数，渐近匹配给出带 $-\pi/4$ 相移的连接公式。
- 双转折点势阱的量子化条件 $\oint p\,dx = (n+\tfrac12)h$：Maslov 指标 $+\tfrac12$ 来自两个转折点各亏 $\pi/4$ 相位，恰好补回旧量子论丢掉的零点能；谐振子能级被 WKB 精确复现。
- 隧穿：$T \sim e^{-2\gamma}$，$\gamma = \int\lvert p\rvert dx/\hbar$；方势垒厚垒极限与精确解指数一致；双阱劈裂与 Gamow $\alpha$ 衰变（Geiger–Nuttall 定律）都是这个指数的天下。

| 公式 | 内容 | 要害 |
| --- | --- | --- |
| $E_0 \le \langle\psi\rvert H\lvert\psi\rangle/\langle\psi\vert\psi\rangle$ | 变分原理 | 谱分解一行得证；只高不低 |
| $E[\psi_0 + \varepsilon\varphi] = E_0 + O(\varepsilon^2)$ | 平稳性 | 能量误差是波函数误差的二阶 |
| $E(Z_{\mathrm{eff}}) = (2Z_{\mathrm{eff}}^2 - \tfrac{27}{4}Z_{\mathrm{eff}})\times 13.6$ eV | 氦基态 | $Z_{\mathrm{eff}} = 27/16$ |
| $\psi \sim p^{-1/2}e^{\pm i\int p\,dx/\hbar}$ | WKB 波函数 | $\lvert\psi\rvert^2 \propto 1/v$（停留时间） |
| $\oint p\,dx = (n+\tfrac12)h$ | 量子化条件 | Maslov $+\tfrac12$ = 零点能 |
| $T \sim e^{-2\gamma}$ | 隧穿指数 | 厚垒极限与精确解指数一致 |

## 自检问题

**1.** 证明变分原理 $E_0 \le \langle\psi\rvert H\lvert\psi\rangle/\langle\psi\vert\psi\rangle$，并推导能量误差是波函数误差的二阶。

<details markdown="1"><summary>点击显示答案</summary>

**变分原理**：设 $H\lvert n\rangle = E_n\lvert n\rangle$，本征值排序 $E_0 \le E_1 \le \cdots$，$\{\lvert n\rangle\}$ 完备正交归一。任意可归一化态展开 $\lvert\psi\rangle = \sum_n c_n\lvert n\rangle$，则 $\langle\psi\rvert H\lvert\psi\rangle = \sum_n E_n\lvert c_n\rvert^2$，$\langle\psi\vert\psi\rangle = \sum_n\lvert c_n\rvert^2$。用 $E_n \ge E_0$ 逐项放缩：

$$\frac{\langle\psi\rvert H\lvert\psi\rangle}{\langle\psi\vert\psi\rangle} = \frac{\sum_n E_n\lvert c_n\rvert^2}{\sum_n \lvert c_n\rvert^2} \ge E_0\,\frac{\sum_n\lvert c_n\rvert^2}{\sum_n\lvert c_n\rvert^2} = E_0.$$

等号要求所有 $E_n > E_0$ 的分量为零，即 $\lvert\psi\rangle$ 落在基态子空间。

**二阶性**：写 $\lvert\psi\rangle = \lvert\psi_0\rangle + \varepsilon\lvert\varphi\rangle$，$\lvert\psi_0\rangle$ 为归一化真基态，且取 $\langle\psi_0\vert\varphi\rangle = 0$（$\lvert\psi\rangle$ 沿 $\lvert\psi_0\rangle$ 方向的分量差异只是归一化问题，可归入定义）。则

$$\langle\psi\rvert H\lvert\psi\rangle = E_0 + \varepsilon\langle\varphi\rvert H\lvert\psi_0\rangle + \varepsilon\langle\psi_0\rvert H\lvert\varphi\rangle + \varepsilon^2\langle\varphi\rvert H\lvert\varphi\rangle.$$

中间两项用 $H\lvert\psi_0\rangle = E_0\lvert\psi_0\rangle$ 化为 $\varepsilon E_0(\langle\varphi\vert\psi_0\rangle + \langle\psi_0\vert\varphi\rangle) = 0$。又 $\langle\psi\vert\psi\rangle = 1 + \varepsilon^2\langle\varphi\vert\varphi\rangle$，相除（展开 $(1+x)^{-1} \approx 1 - x$）：

$$E[\psi] = \frac{E_0 + \varepsilon^2\langle\varphi\rvert H\lvert\varphi\rangle}{1 + \varepsilon^2\langle\varphi\vert\varphi\rangle} = E_0 + \varepsilon^2\langle\varphi\rvert(H - E_0)\lvert\varphi\rangle + O(\varepsilon^3).$$

一阶项消失：能量误差是波函数误差 $\varepsilon$ 的二阶。且 $H - E_0$ 在基态正交补上是正定算符，故修正 $\ge 0$——二阶性与"只高不低"是同一条定理的两面。

</details>

**2.** 用归一化高斯试探函数 $\psi(r) = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$ 估氢原子基态：算出最优 $\alpha$、对应能量，与精确值比较；若改用指数试探族 $e^{-\beta r}$ 会发生什么？

<details markdown="1"><summary>点击显示答案</summary>

**期望值**：高斯矩 $\langle r^2\rangle = \dfrac{\int_0^\infty r^4 e^{-2\alpha r^2}dr}{\int_0^\infty r^2 e^{-2\alpha r^2}dr} = \dfrac{3}{4\alpha}$，$\langle 1/r\rangle = \dfrac{\int_0^\infty r e^{-2\alpha r^2}dr}{\int_0^\infty r^2 e^{-2\alpha r^2}dr} = 2\sqrt{\dfrac{2\alpha}{\pi}}$。动能用 $-\nabla^2\psi = (6\alpha - 4\alpha^2r^2)\psi$：

$$\langle T\rangle = \frac{\hbar^2}{2m_e}\left(6\alpha - 4\alpha^2\cdot\frac{3}{4\alpha}\right) = \frac{3\hbar^2\alpha}{2m_e},\qquad \langle V\rangle = -\frac{2e^2}{4\pi\varepsilon_0}\sqrt{\frac{2\alpha}{\pi}}.$$

**极小化**：$E(\alpha) = \dfrac{3\hbar^2}{2m_e}\alpha - \dfrac{2e^2}{4\pi\varepsilon_0}\sqrt{\dfrac{2\alpha}{\pi}}$，令 $dE/d\alpha = 0$：

$$\frac{3\hbar^2}{2m_e} = \frac{e^2}{4\pi\varepsilon_0}\sqrt{\frac{2}{\pi\alpha}} \;\Longrightarrow\; \sqrt{\frac{2}{\pi\alpha}} = \frac{3a_0}{2} \;\Longrightarrow\; \alpha_{\min} = \frac{8}{9\pi a_0^2}.$$

代回（用 $\hbar^2/(m_ea_0^2) = e^2/(4\pi\varepsilon_0a_0) = 27.2$ eV）：

$$E_{\min} = \frac{3\hbar^2}{2m_e}\cdot\frac{8}{9\pi a_0^2} - \frac{2e^2}{4\pi\varepsilon_0}\cdot\frac{4}{3\pi a_0} = \frac{4}{3\pi}\cdot27.2 - \frac{8}{3\pi}\cdot27.2 = -\frac{4}{3\pi}\times 27.2\ \text{eV} \approx -11.5\ \text{eV}$$

（势能项用了 $\sqrt{2\alpha_{\min}/\pi} = 4/(3\pi a_0)$；动能项 $\dfrac{3}{2}\cdot\dfrac{8}{9\pi} = \dfrac{4}{3\pi}$。）对照精确值 $-13.6$ eV：$-11.5 > -13.6$，上限成立，误差 $15\%$。

**改用 $e^{-\beta r}$**：试探族 $e^{-\beta r}$ 包含真实基态波函数（$\beta = 1/a_0$）。同样的程序给出 $E(\beta) = \dfrac{\hbar^2\beta^2}{2m_e} - \dfrac{e^2\beta}{4\pi\varepsilon_0}$，极小化得 $\beta = 1/a_0$、$E_{\min} = -13.6$ eV——**变分法命中精确解**。教训：变分结果的精度上限由试探族的物理质量决定，不在计算技巧。

</details>

**3.** 氦原子基态的有效电荷变分：写出 $\langle H\rangle(Z_{\mathrm{eff}})$ 的动能、核吸引、电子排斥各项并求和，极小化求 $Z_{\mathrm{eff}}$ 与 $E_{\min}$，与微扰论和实验对照。

<details markdown="1"><summary>点击显示答案</summary>

试探函数为两个电荷 $Z_{\mathrm{eff}}$ 的类氢 1s 之积（已归一）。三块期望值（以 13.6 eV 为单位，记 $e^2/(4\pi\varepsilon_0a_0) = 27.2$ eV）：

**动能**：类氢 1s 动能期望值 $= Z_{\mathrm{eff}}^2 \times 13.6$ eV（位力定理 $T = -E$），两个电子：

$$\langle T\rangle = 2Z_{\mathrm{eff}}^2 \times 13.6\ \text{eV}.$$

**核吸引**：$\langle 1/r\rangle = Z_{\mathrm{eff}}/a_0$，真实核电荷 $Z = 2$（注意不是 $Z_{\mathrm{eff}}$）：

$$\langle V_{\mathrm{nuc}}\rangle = 2\times\left(-\frac{2e^2}{4\pi\varepsilon_0}\right)\frac{Z_{\mathrm{eff}}}{a_0} = -8Z_{\mathrm{eff}}\times 13.6\ \text{eV}.$$

**电子排斥**：两个球对称指数云的静电能（Griffiths 式 7.20 的标准积分）：

$$\langle V_{ee}\rangle = \frac{5}{8}Z_{\mathrm{eff}}\cdot\frac{e^2}{4\pi\varepsilon_0a_0} = \frac{5}{4}Z_{\mathrm{eff}}\times 13.6\ \text{eV}.$$

求和：

$$E(Z_{\mathrm{eff}}) = \left(2Z_{\mathrm{eff}}^2 - 8Z_{\mathrm{eff}} + \frac54 Z_{\mathrm{eff}}\right)\times 13.6\ \text{eV} = \left(2Z_{\mathrm{eff}}^2 - \frac{27}{4}Z_{\mathrm{eff}}\right)\times 13.6\ \text{eV}.$$

**极小化**：$dE/dZ_{\mathrm{eff}} = (4Z_{\mathrm{eff}} - 27/4)\times13.6 = 0$，得

$$Z_{\mathrm{eff}} = \frac{27}{16} = 1.6875,\qquad E_{\min} = -\frac{729}{128}\times 13.6\ \text{eV} \approx -77.5\ \text{eV}.$$

**对照**：微扰论一阶相当于取 $Z_{\mathrm{eff}} = 2$ 不动波函数：$E = (8 - 27/2)\times13.6 = -74.8$ eV；实验 $-79.0$ eV。变分值恰在两者之间且保证是上限：$-74.8$（微扰）$> -77.5$（变分）$> -79.0$（实验）。物理读数：屏蔽使每个电子只见 $1.69$ 份电荷，电子云比无屏蔽时胀大约 $18\%$（$a_0/1.69$ vs $a_0/2$）。

</details>

**4.** 从连接公式出发推导束缚态量子化条件 $\oint p\,dx = (n+\tfrac12)h$，并对谐振子验证它精确复现 $E_n = (n+\tfrac12)\hbar\omega$。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：双转折点势阱 $a < b$，两禁区波函数须衰减。右转折点 $b$ 的连接公式给出阱内

$$\psi(x) \approx \frac{2C}{\sqrt{p}}\cos\left(\frac{1}{\hbar}\int_x^b p\,dx' - \frac{\pi}{4}\right) \equiv \frac{2C}{\sqrt p}\cos\theta(x).$$

左转折点 $a$ 的连接公式（镜像版）给出

$$\psi(x) \approx \frac{2C'}{\sqrt{p}}\cos\left(\frac{1}{\hbar}\int_a^x p\,dx' - \frac{\pi}{4}\right).$$

用 $\displaystyle\int_a^x = \int_a^b - \int_x^b$ 改写第二式相位：记 $\Phi = \dfrac{1}{\hbar}\displaystyle\int_a^b p\,dx$，则

$$\frac{1}{\hbar}\int_a^x p\,dx' - \frac{\pi}{4} = \Phi - \frac{\pi}{2} - \theta(x).$$

同一个波函数的两种写法必须处处相等：$\cos\theta = \pm\cos(\Phi - \pi/2 - \theta)$ 对所有 $x$ 成立（$\theta$ 随 $x$ 连续变化），唯一可能是两个相位相差常数 $n\pi$：

$$\Phi - \frac{\pi}{2} = n\pi \;\Longrightarrow\; \int_a^b p\,dx = \left(n + \tfrac12\right)\pi\hbar,\qquad n = 0, 1, 2, \dots$$

相空间闭合轨道积分是去程回程两倍：$\oint p\,dx = 2\int_a^b p\,dx = (n+\tfrac12)h$。那个 $+\tfrac12$ 来自两个转折点各贡献的 $-\pi/4$（共 $-\pi/2$）——Maslov 指标。

**谐振子验证**：转折点 $x_0 = \sqrt{2E/(m\omega^2)}$，

$$\oint p\,dx = 2\int_{-x_0}^{x_0}\sqrt{2mE - m^2\omega^2x^2}\,dx.$$

换元 $x = x_0\sin\vartheta$：$\sqrt{2mE}\cos\vartheta\cdot x_0\cos\vartheta\,d\vartheta$，积分 $= 2\cdot\sqrt{2mE}\,x_0\displaystyle\int_{-\pi/2}^{\pi/2}\cos^2\vartheta\,d\vartheta = 2\sqrt{2mE}\,x_0\cdot\frac{\pi}{2} = \pi x_0\sqrt{2mE} = \frac{2\pi E}{\omega}$。令 $2\pi E/\omega = (n+\tfrac12)2\pi\hbar$：

$$E_n = \left(n + \tfrac12\right)\hbar\omega$$

——与升降算符精确解逐字一致。若用旧量子论的 $\oint p\,dx = nh$，会得到 $E_n = n\hbar\omega$，零点能 $\hbar\omega/2$ 不翼而飞：这正是连接公式的相位亏损补回来的东西。

</details>

**5.** 推导方势垒（高 $V_0$、宽 $a$，$E < V_0$）的 WKB 透射指数，并从精确透射公式出发取厚垒极限对照。

<details markdown="1"><summary>点击显示答案</summary>

**WKB**：方势垒内 $\lvert p\rvert = \sqrt{2m(V_0 - E)} = \hbar\kappa$ 为常数，衰减指数

$$\gamma = \frac{1}{\hbar}\int_0^a \lvert p\rvert\,dx = \kappa a,\qquad T_{\mathrm{WKB}} \sim e^{-2\kappa a}.$$

更仔细地沿入射区–垒区–出射区逐段写 WKB 解并在两个（非经典转折的）势阶处匹配，可得前置因子，但指数部分就是 $\gamma = \kappa a$。

**精确解**（第 03s 篇的分区平面波匹配结果）：

$$T = \left[1 + \frac{V_0^2\,\sinh^2(\kappa a)}{4E(V_0 - E)}\right]^{-1}.$$

**厚垒极限** $\kappa a \gg 1$：$\sinh(\kappa a) = \tfrac12 e^{\kappa a}(1 - e^{-2\kappa a}) \approx \tfrac12 e^{\kappa a}$，故方括号内第二项 $\approx \dfrac{V_0^2}{16E(V_0-E)}e^{2\kappa a} \gg 1$，1 可略：

$$T \approx \frac{16E(V_0-E)}{V_0^2}\,e^{-2\kappa a}.$$

**对照**：指数 $e^{-2\kappa a}$ 与 WKB 完全一致；差别只在前置因子 $\dfrac{16E(V_0-E)}{V_0^2}$（量级 1，例如 $E = V_0/2$ 时为 4）。由于 $\kappa a \gg 1$ 时 $e^{-2\kappa a}$ 本身动辄 $10^{-10}$，前置因子的修正微不足道——**WKB 抓的是指数，而隧穿问题里指数就是物理**。这也解释了适用窗口：$\kappa a \sim 1$（薄垒）时 WKB 与精确解差很远，必须用分区匹配；另外注意方势垒的两壁是势的跳变而非经典转折点（$p \neq 0$ 处突变），此例中 WKB 的失效模式与 7.2 节转折点的失效不同，但厚垒极限下结论殊途同归。

</details>

## 参考

- Griffiths《量子力学概论》（第 3 版）第 7 章（变分原理、氦原子基态——本篇第 3–6 节主线）与第 8 章（WKB 近似、连接公式、隧穿——第 7–8 节主线）。
- Shankar《Principles of Quantum Mechanics》第 16 章（变分法与 WKB）——半经典展开的更紧凑推导。
- Sakurai《现代量子力学》第 5 章（近似方法中的变分法一节）——氦原子与 Rayleigh–Ritz 的另一讲法。
- 朗道、栗弗席兹《量子力学（非相对论理论）》§§ 48–51（准经典近似）——连接公式的复平面推导与 Maslov 指标的源头，进阶阅读。
