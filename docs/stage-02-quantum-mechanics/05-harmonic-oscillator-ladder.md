# 谐振子的产生/湮灭算符解法：QFT 的全部家当

> 路线图位置：第 2 阶段（量子力学）· 谐振子专题
> 前置知识：量子力学公设（态矢、算符、对易关系 $[x,p]=i\hbar$）、一维定态薛定谔方程。
> 学习目标：用纯代数方法（不碰微分方程）完整解出谐振子的能谱与态；掌握升降算符、数表象、相干态；把 $N$ 个耦合谐振子对角化成独立简正模——这一步做完，量子场论的自由场就只剩"把模指标换成连续动量"这一个动作（[标量场量子化：从无穷多谐振子到粒子](../stage-04-qft-core/01-scalar-field-quantization.md) 整篇就是本篇的连续极限版）。

全文在代数推导部分取 $\hbar = m = \omega = 1$ 的无量纲单位（首次出现时交代恢复方法）；涉及具体数值估算（Casimir 效应）时恢复 $\hbar$ 与 $c$。

---

## 1. 一句话总结

**任何稳定平衡点附近的小振动都是谐振子，而谐振子的全部量子性质——能谱 $E_n = (n+\tfrac12)\hbar\omega$、本征态、矩阵元——都可以从一条对易关系 $[a, a^\dagger] = 1$ 纯代数地推出来；$N$ 个耦合谐振子经简正模分解后就是 $N$ 个互不说话的独立谐振子，把"第 $i$ 个模激发到第 $n_i$ 级"读作"有 $n_i$ 个声子"，再把模的指标从分立换成连续，声子换成粒子，就是整个自由量子场论。**

下面把这句话一层一层算出来。

## 2. 为什么谐振子是物理中最重要的可解模型

量子力学里能严格解出的系统屈指可数（自由粒子、谐振子、氢原子，基本就这些），但谐振子的地位远超"一个可解习题"，原因是两条普遍事实。

**第一，任何稳定平衡点附近都是谐振子。** 设粒子在一维势 $V(x)$ 中运动，$x_0$ 是稳定平衡点（$V'(x_0) = 0$，$V''(x_0) > 0$）。在 $x_0$ 附近泰勒展开：

$$V(x) = V(x_0) + \underbrace{V'(x_0)}_{=\,0}(x - x_0) + \frac12 V''(x_0)\,(x - x_0)^2 + \mathcal O\big((x-x_0)^3\big).$$

常数项 $V(x_0)$ 可以吸收进能量零点，线性项消失，于是只要振幅足够小（高阶项可忽略），任何势阱里的运动都近似是频率 $\omega = \sqrt{V''(x_0)/m}$ 的谐振子。多维情形同理：稳定平衡点附近势能的二次型可以正交对角化，化为一组独立谐振子——这就是第 6 节简正模分析的雏形。

**第二，宏观物质几乎都是"一堆耦合谐振子"。** 固体中原子在平衡位置附近振动（声子）、电磁场在真空附近振荡（光子）、分子振动、LC 电路……量子多体与量子场论的很大一部分，就是"谐振子 + 微小非谐修正（微扰）"。

所以物理学的标准战术是：**把谐振子解到滚瓜烂熟，然后把真实系统写成谐振子加微扰。** 本篇负责前半句。

## 3. 代数解法：从一条对易关系到整个谱

### 3.1 无量纲化

谐振子哈密顿量

$$H = \frac{p^2}{2m} + \frac12 m\omega^2 x^2, \qquad [x, p] = i\hbar.$$

由量纲分析，$x$ 的自然尺度是 $\sqrt{\hbar/(m\omega)}$，$p$ 的自然尺度是 $\sqrt{\hbar m\omega}$。本节起取

$$\hbar = m = \omega = 1,$$

即所有坐标都以各自的自然尺度为单位；恢复量纲的规则是：把 $x$ 换成 $x\,\sqrt{m\omega/\hbar}$、$p$ 换成 $p/\sqrt{\hbar m\omega}$、$H$ 换成 $H/(\hbar\omega)$，最后乘回去即可（自检题 1 会练到）。无量纲化后：

$$H = \frac12\left(p^2 + x^2\right), \qquad [x, p] = i.$$

### 3.2 定义 $a$ 与 $a^\dagger$

代数解法的动机：$H$ 是"平方和"，想起复数分解 $u^2 + v^2 = (u - iv)(u + iv)$。但 $x, p$ 不对易，分解出来会差一个对易子——正是这个差额给出全部物理。定义

$$a = \frac{1}{\sqrt2}\left(x + ip\right), \qquad a^\dagger = \frac{1}{\sqrt2}\left(x - ip\right).$$

注意 $a$ **不是**厄米算符（$a \neq a^\dagger$），它不对应任何可观测量；它是"制造态的机器"。反解出

$$x = \frac{1}{\sqrt2}\left(a + a^\dagger\right), \qquad p = \frac{1}{i\sqrt2}\left(a - a^\dagger\right).$$

**基本对易关系**（由 $[x,p]=i$ 直接计算）：

$$[a, a^\dagger] = \frac12\,[x+ip,\, x-ip] = \frac12\big(-i[x,p] + i[p,x]\big) = \frac12\big(-i\cdot i + i\cdot(-i)\big) = 1.$$

**哈密顿量**。计算乘积：

$$a^\dagger a = \frac12(x - ip)(x + ip) = \frac12\left(x^2 + p^2 + i[x,p]\right) = \frac12\left(x^2 + p^2\right) - \frac12 = H - \frac12,$$

即

$$\boxed{H = a^\dagger a + \frac12 \equiv N + \frac12}$$

其中 $N \equiv a^\dagger a$ 叫**粒子数算符**（眼下先理解成"激发级数算符"，第 6 节它会真的开始数粒子）。由此 $H$ 的本征值问题完全等价于 $N$ 的本征值问题。

### 3.3 谱的代数论证

只用两条输入：$[a, a^\dagger] = 1$ 和**内积的正定性**。由此推出（这是标准推导，每一步都值得亲手做一遍）：

**引理 1（$a$ 降能、$a^\dagger$ 升能）。** 由 $[a, a^\dagger]=1$ 得 $[N, a] = [a^\dagger a, a] = -a$，$[N, a^\dagger] = +a^\dagger$。设 $N|n\rangle = n|n\rangle$（本征值 $n$ 暂且是任意实数），则

$$N\big(a|n\rangle\big) = \big(aN + [N,a]\big)|n\rangle = (n-1)\,a|n\rangle,$$

即 $a|n\rangle$ 是 $N$ 的本征值为 $n-1$ 的本征态（除非它是零矢量）。同理 $a^\dagger|n\rangle$ 的本征值是 $n+1$。

**引理 2（本征值非负）。** $N$ 是厄米算符且半正定：对任意态 $|\psi\rangle$,

$$\langle\psi|N|\psi\rangle = \langle\psi|a^\dagger a|\psi\rangle = \lVert\,a|\psi\rangle\,\rVert^2 \;\geq\; 0,$$

等号当且仅当 $a|\psi\rangle = 0$。所以 $N$ 的一切本征值 $n \geq 0$。

**引理 3（降链必须触底）。** 从某本征态 $|n\rangle$ 出发反复作用 $a$：$n, n-1, n-2, \dots$。若 $n$ 不是整数，这条链会越过 $0$ 进入负本征值，与引理 2 矛盾。唯一的出路是链在某一步被零矢量截断：$a|0\rangle = 0$，即存在本征值恰为 $0$ 的"真空态"，且 $n$ 本身必须是非负整数。

**结论**：

$$N|n\rangle = n|n\rangle, \qquad E_n = n + \frac12 \qquad (n = 0, 1, 2, \dots),$$

恢复量纲即 $E_n = \left(n + \tfrac12\right)\hbar\omega$。**能谱等间隔、基态能量不为零**——这两条后面都有大用。

### 3.4 矩阵元与升降算符公式表

$a|n\rangle$ 正比于 $|n-1\rangle$，比例系数由归一化定出：

$$\lVert\,a|n\rangle\,\rVert^2 = \langle n|a^\dagger a|n\rangle = n \quad\Longrightarrow\quad a|n\rangle = \sqrt{n}\,|n-1\rangle.$$

同理（用 $aa^\dagger = N + 1$）$a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$。从真空态可逐级造出整个塔：

$$|n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}}\,|0\rangle.$$

汇总成表（本篇的"全部家当"）：

| 对象 | 公式 | 读法 |
|---|---|---|
| 湮灭算符 | $a\lvert n\rangle = \sqrt{n}\,\lvert n-1\rangle$ | 拿走一份激发 |
| 产生算符 | $a^\dagger\lvert n\rangle = \sqrt{n+1}\,\lvert n+1\rangle$ | 添上一份激发 |
| 数算符 | $N = a^\dagger a,\ \ N\lvert n\rangle = n\lvert n\rangle$ | 数有几份激发 |
| 哈密顿量 | $H = N + \tfrac12$ | 每份激发携带能量 $1$（即 $\hbar\omega$） |
| 真空条件 | $a\lvert 0\rangle = 0$ | 没有激发可拿 |
| 基本对易子 | $[a, a^\dagger] = 1$ | 一切由此推出 |
| 位置 | $x = (a + a^\dagger)/\sqrt2$ | 每次升或降一级 |
| 动量 | $p = (a - a^\dagger)/(i\sqrt2)$ | 同上 |

注意 $\sqrt{n}$ 因子：拿走激发越容易拿空（$n=0$ 时为零），添加激发则随 $n$ 增强（$\sqrt{n+1}$）——这个不对称的 $\sqrt{n+1}$ 在 QFT 里就是玻色子的"受激辐射增强"因子的根源。

## 4. 波函数对照：代数与解析两种视角对上

同一个系统也可以用位置表象硬解：$a|0\rangle = 0$ 写成微分方程（$p = -i\,d/dx$）

$$\frac{1}{\sqrt2}\left(x + \frac{d}{dx}\right)\psi_0(x) = 0 \quad\Longrightarrow\quad \psi_0(x) \propto e^{-x^2/2},$$

是高斯函数。激发态由 $|n\rangle = (a^\dagger)^n|0\rangle/\sqrt{n!}$ 生成：

$$\psi_n(x) = \frac{1}{\sqrt{2^n n!}}\left(x - \frac{d}{dx}\right)^n e^{-x^2/2} \cdot \pi^{-1/4} = \frac{1}{\sqrt{2^n n!}\,\pi^{1/4}}\,H_n(x)\,e^{-x^2/2},$$

其中 $H_n(x)$ 正是 **Hermite 多项式**（$H_0 = 1$，$H_1 = 2x$，$H_2 = 4x^2 - 2, \dots$）——微分方程解法里查表查出来的特殊函数，在代数法里只是"反复作用 $a^\dagger$"的副产品。

两种视角给出的定性图像完全一致，可以直接对照检查：

- **节点数 = $n$**：$H_n$ 是 $n$ 次多项式，有 $n$ 个实零点，故 $\psi_n$ 有 $n$ 个节点。激发越高，波函数摆动越密（曲率越大，动能越高），与 $E_n$ 递增吻合。
- **宇称交错**：$H_n(-x) = (-1)^n H_n(x)$，所以 $\psi_n$ 的宇称为 $(-1)^n$，偶奇交替。从代数看也显然：$x, p$ 都是奇宇称算符，$a^\dagger$ 每作用一次翻转一次宇称。
- **$\sqrt{n}$ 因子**：升降公式里的 $\sqrt{n}$、$\sqrt{n+1}$ 与 Hermite 多项式的递推关系 $H_n' = 2n H_{n-1}$、$H_{n+1} = 2xH_n - H_n'$ 是同一件事的两种写法。

教学习惯上先学波函数解法再学代数解法，但**在通往 QFT 的路上，代数视角是本体的**：到了场论，"波函数"是场位形空间上的泛函，几乎无法操作，而 $a, a^\dagger$ 的代数纹丝不动。

## 5. 数表象中的 $x, p$ 与相干态

### 5.1 矩阵元

由 $x = (a + a^\dagger)/\sqrt2$ 和升降公式，$x$ 在数表象中只有相邻矩阵元非零：

$$\langle n-1|x|n\rangle = \sqrt{\frac{n}{2}}, \qquad \langle n+1|x|n\rangle = \sqrt{\frac{n+1}{2}},$$

$p$ 同理（差 $i$ 与符号）。也就是说 $x, p$ 的矩阵是**三对角**的。两个马上有用的推论：

- 在能量本征态里 $\langle n|x|n\rangle = \langle n|p|n\rangle = 0$（对角元为零）——定态不"振荡"，这与经典振子来回运动完全不同；
- $\langle n|x^2|n\rangle = n + \tfrac12$，$\langle n|p^2|n\rangle = n + \tfrac12$（自检题 3），于是 $(\Delta x)_n(\Delta p)_n = n + \tfrac12 \geq \tfrac12$，基态恰好达到不确定度关系的下限。

### 5.2 相干态：最像经典的量子态

数本征态 $|n\rangle$ 的能量确定但毫无经典运动图像。要找回"振子来回振荡"，需要 $a$ 自己的本征态——**相干态** $|\alpha\rangle$：

$$a|\alpha\rangle = \alpha|\alpha\rangle, \qquad \alpha \in \mathbb C.$$

$a$ 不是厄米算符，所以本征值 $\alpha$ 可以是任意复数，不构成正交基——相干态是**超完备**的。在数表象中展开 $|\alpha\rangle = \sum_n c_n|n\rangle$，代入 $a|\alpha\rangle = \alpha|\alpha\rangle$ 得递推 $\sqrt{n+1}\,c_{n+1} = \alpha\, c_n$，归一化后：

$$\boxed{\;|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=0}^{\infty}\frac{\alpha^n}{\sqrt{n!}}\,|n\rangle\;}$$

由此读出三条核心性质：

**（1）粒子数服从泊松分布。** $P(n) = |\langle n|\alpha\rangle|^2 = e^{-|\alpha|^2}|\alpha|^{2n}/n!$，平均激发数 $\langle N\rangle = |\alpha|^2$，涨落 $\Delta N = |\alpha|$。

**（2）最小不确定度。** 由 $a|\alpha\rangle = \alpha|\alpha\rangle$ 及 $\langle\alpha|a^\dagger = \langle\alpha|\alpha^*$ 直接算：

$$\langle x\rangle = \frac{\alpha + \alpha^*}{\sqrt2}, \qquad \Delta x = \frac{1}{\sqrt2}, \qquad \Delta p = \frac{1}{\sqrt2}, \qquad \Delta x\,\Delta p = \frac12,$$

与基态完全一样——相干态就是把真空态**平移**到相空间点 $\big(\sqrt2\,\mathrm{Re}\,\alpha,\ \sqrt2\,\mathrm{Im}\,\alpha\big)$ 而不改变形状（不"散架"的波包）。

**（3）时间演化 = 经典振荡。** 海森堡绘景中 $a(t) = a\,e^{-it}$（由 $\dot a = i[H, a] = -ia$），所以 $\alpha(t) = \alpha\,e^{-it}$：复平面上绕原点以单位角速度（即 $\omega$）旋转。于是

$$\langle x(t)\rangle = \sqrt2\,\mathrm{Re}\big(\alpha e^{-it}\big) = \sqrt2\,|\alpha|\cos\big(t - \arg\alpha\big),$$

正是经典谐振子的解，振幅 $\sqrt2|\alpha|$、相位 $\arg\alpha$。期望值严格走经典轨道（这其实也是 Ehrenfest 定理对线性势的特例），波包形状还不变。

相干态不是数学玩物：激光的输出光就是（近似的）相干态。对路线图而言它埋的伏笔是——**场的经典极限**。QFT 里场算符的相干态（每个模式一个 $\alpha_p$）期望值满足经典场方程，麦克斯韦电磁波就是光子场的相干态。"经典物理如何从量子中浮现"，相干态是最干净的样板间。

<details markdown="1"><summary>补充说明：相干态为什么也叫"位移真空态"</summary>

定义位移算符 $D(\alpha) = e^{\alpha a^\dagger - \alpha^* a}$。用 BCH 公式（$[A,B]$ 与两者都对易时 $e^{A+B} = e^A e^B e^{-[A,B]/2}$，这里 $[\alpha a^\dagger, -\alpha^* a] = |\alpha|^2$ 是数）：

$$D(\alpha) = e^{-|\alpha|^2/2}\,e^{\alpha a^\dagger}\,e^{-\alpha^* a}.$$

作用在真空上：$e^{-\alpha^* a}|0\rangle = |0\rangle$（展开后除首项外全被 $a|0\rangle = 0$ 杀掉），$e^{\alpha a^\dagger}|0\rangle = \sum_n \alpha^n (a^\dagger)^n|0\rangle/n! = \sum_n \alpha^n |n\rangle/\sqrt{n!}$，合起来正是上文的 $|\alpha\rangle = D(\alpha)|0\rangle$。所以相干态字面上就是"被平移的真空"。$D(\alpha)$ 幺正，且 $D^\dagger(\alpha)\, a\, D(\alpha) = a + \alpha$——相空间平移的算符实现。这套位移算符语言在 QFT 讨论场的经典极限时原样复用。

</details>

## 6. 从 $N$ 个耦合谐振子到简正模：通往 QFT 的桥

### 6.1 两个耦合振子：详细算一遍

两个全同振子（质量 $m$、各自频率 $\omega$）用一根弹性系数 $K$ 的弹簧耦合：

$$H = \frac{p_1^2}{2m} + \frac{p_2^2}{2m} + \frac12 m\omega^2\left(x_1^2 + x_2^2\right) + \frac12 K\left(x_1 - x_2\right)^2.$$

耦合项 $K(x_1 - x_2)^2/2$ 只依赖相对位移。这提示换成**质心/相对坐标**——为保持对易关系标准形式，取归一化的组合

$$x_\pm = \frac{x_1 \pm x_2}{\sqrt2}, \qquad p_\pm = \frac{p_1 \pm p_2}{\sqrt2},$$

则 $[x_\pm, p_\pm] = i$，交叉对易子为零（直接展开验证），且 $x_1^2 + x_2^2 = x_+^2 + x_-^2$，$(x_1 - x_2)^2 = 2x_-^2$。代入：

$$H = \left[\frac{p_+^2}{2m} + \frac12 m\omega^2 x_+^2\right] + \left[\frac{p_-^2}{2m} + \frac12\left(m\omega^2 + 2K\right) x_-^2\right].$$

**耦合哈密顿量精确地分解成两个独立谐振子**：

- 对称模 $x_+$（两体同向运动，质心平移）：频率 $\Omega_+ = \omega$（耦合弹簧不形变，不起作用）；
- 反对称模 $x_-$（两体反向挤压，弹簧形变）：频率 $\Omega_- = \sqrt{\omega^2 + 2K/m}$。

两个模各配一套升降算符 $a_\pm = \sqrt{m\Omega_\pm/2}\,x_\pm + i\,p_\pm/\sqrt{2m\Omega_\pm}$，满足 $[a_i, a_j^\dagger] = \delta_{ij}$（$i, j \in \{+,-\}$），哈密顿量为

$$H = \Omega_+\left(a_+^\dagger a_+ + \tfrac12\right) + \Omega_-\left(a_-^\dagger a_- + \tfrac12\right),$$

本征态 $|n_+, n_-\rangle$，能量 $E = (n_+ + \tfrac12)\Omega_+ + (n_- + \tfrac12)\Omega_-$。**两个对易的产生算符作用次序无关**：$a_+^\dagger a_-^\dagger|0\rangle = a_-^\dagger a_+^\dagger|0\rangle$——这是玻色对称性的雏形。

### 6.2 一维原子链：无穷多个模

把上一步推广：$N$ 个质量 $m$ 的原子排成周期为 $a$ 的链，相邻原子以弹性系数 $\kappa$ 的弹簧连接（取周期性边界条件）。位移记为 $u_n$，则

$$H = \sum_n \frac{p_n^2}{2m} + \frac{\kappa}{2}\sum_n \left(u_{n+1} - u_n\right)^2.$$

平移对称性提示做傅里叶变换（简正坐标就是动量空间的模）：

$$u_n = \frac{1}{\sqrt N}\sum_k \tilde u_k\, e^{ikna}, \qquad k = \frac{2\pi}{Na}\,j,\ \ j = 0, 1, \dots, N-1.$$

最近邻耦合项变为（利用 $\sum_n e^{i(k-k')na} = N\delta_{kk'}$）

$$\sum_n\left(u_{n+1} - u_n\right)^2 = \sum_k \big|e^{ika} - 1\big|^2\,|\tilde u_k|^2 = \sum_k 4\sin^2\!\frac{ka}{2}\;|\tilde u_k|^2,$$

于是 $H$ 对角化成以 $k$ 标记的独立振子之和，色散关系为

$$\boxed{\;\omega_k = 2\sqrt{\frac{\kappa}{m}}\;\Big|\sin\frac{ka}{2}\Big|\;}$$

长波极限 $ka \ll 1$ 时 $\omega_k \approx a\sqrt{\kappa/m}\,|k|$，**线性色散**——斜率就是固体中的声速。每个模 $k$ 配一对 $a_k, a_k^\dagger$，$[a_k, a_{k'}^\dagger] = \delta_{kk'}$，

$$H = \sum_k \omega_k\left(a_k^\dagger a_k + \tfrac12\right).$$

### 6.3 声子：把激发数读成粒子数

现在做那个改变视角的重新解读。模 $k$ 的态 $|n_k\rangle$ 不再读作"第 $k$ 个振子被激发了 $n_k$ 次"，而读作：

$$\text{态 } |\{n_k\}\rangle \;=\; \text{“有 } n_{k_1} \text{ 个动量为 } k_1 \text{ 的声子，} n_{k_2} \text{ 个动量为 } k_2 \text{ 的声子，……”}$$

每个"声子"携带能量 $\omega_k$、（准）动量 $k$，$a_k^\dagger$ 创造一个声子，$a_k$ 消灭一个。总能量就是各声子能量之和（再加零点能）。同一个希尔伯特空间，换个读法，"振子激发谱"就变成了"多粒子态空间"（Fock 空间）。

### 6.4 宣布：这就是 QFT 的自由场

把上面构造里的三个要素逐一替换：

| 原子链（本篇） | 换成 | 自由标量场（QFT） |
|---|---|---|
| 分立格点 $n$ | 连续空间 $\vec x$ | 场 $\phi(\vec x, t)$ |
| 分立的模指标 $k$ | 连续动量 $\vec p$ | $\delta_{kk'} \to (2\pi)^3\delta^3(\vec p - \vec p')$ |
| 色散 $\omega_k = 2\sqrt{\kappa/m}\,\lvert\sin(ka/2)\rvert$ | 相对论色散 | $\omega_p = \sqrt{\vec p^2 + m^2}$ |
| 声子 | 粒子 | $a^\dagger_{\vec p}$ 创造一个动量 $\vec p$ 的粒子 |
| 零点能 $\tfrac12\sum_k\omega_k$ | 每模式 $\tfrac12\omega_p$ | 真空能（发散，见第 7 节与 QFT 篇的正规序） |

除此之外**一个公式都不用改**：$[a_p, a_{p'}^\dagger]$、$H = \sum (\text{或}\int) \omega_p(a_p^\dagger a_p + \tfrac12)$、$|n\rangle$ 的构造、$\sqrt{n}$ 因子，全部原样照搬。这正是 [标量场量子化：从无穷多谐振子到粒子](../stage-04-qft-core/01-scalar-field-quantization.md) 一篇干的事——那篇开头说"本篇后面没有任何新的量子力学"，字面意思就是它只用本篇第 3、6 节的代数。固体物理的声子是先于 QFT 粒子被这样理解的；反过来学会 QFT 后，固体理论就是"低能、非相对论色散"的场论。

## 7. 零点能与 Casimir 效应：真空涨落是真实的

谐振子基态能量 $\tfrac12\hbar\omega \neq 0$。单个振子的零点能只是能量零点的约定，无法测量；但**零点能的"变化"是可测的**。

Casimir 效应（1948）：两块平行的理想导体板，面积 $A$、间距 $d$，置于真空中。板间的电磁场模式受边界条件约束（波矢垂直分量 $k_z = n\pi/d$，只有半波长的整数倍能存在），板外则不受约束。两边真空零点能之差随 $d$ 变化，对电磁场（两种偏振、相对论色散 $\omega = ck$）做求和并正规化后，单位面积的吸引力为

$$\frac{F}{A} = -\frac{\pi^2}{240}\,\frac{\hbar c}{d^4}.$$

量级估算：取 $d = 1\,\mu\mathrm{m}$,

$$\frac{|F|}{A} = \frac{\pi^2}{240}\times\frac{1.05\times10^{-34}\times 3\times10^{8}}{(10^{-6})^4}\;\approx\; 1.3\times10^{-3}\ \mathrm{N/m^2},$$

即约 $1.3\ \mathrm{mN/m^2}$——很小但宏观可测，1997 年 Lamoreaux 的实验（以及此后更精密的测量）在百分之几精度内确认了理论预言。

对本篇与路线图的意义：

- 零点能不是数学赝品。"真空在涨落"——$\langle 0|x^2|0\rangle = \tfrac12 \neq 0$，场论里对应 $\langle 0|\phi^2|0\rangle$ 发散但涨落真实存在——它有可测量的物理后果。
- 同时它暴露了 QFT 的一个脓疮：自由场真空能 $\tfrac12\sum_p \omega_p$ 对无穷多模式**发散**。场论的处理是正规序 $\colon\!H\!\colon$（把产生算符全部排到湮灭算符左边，甩掉这个常数），它对散射振幅无影响；但引力对总能量敏感，真空能的引力效应就是著名的"宇宙学常数问题"，理论预言与观测差约 120 个数量级——物理学中最难看的失败之一，至今未解。

## 小结

一句话：谐振子被 $[a, a^\dagger] = 1$ 一条对易关系完全解决；耦合振子经简正模化归为独立振子之和；把"激发级数"重读为"粒子数"，连续极限就是自由 QFT。

| 代数对象 | 物理意义 | 在 QFT 里的对应 |
|---|---|---|
| $a,\ a^\dagger$ | 降/升一份激发 | 湮灭/产生一个粒子 |
| $[a, a^\dagger] = 1$ | 玻色代数 | $[a_{\vec p}, a^\dagger_{\vec p'}] = (2\pi)^3\delta^3(\vec p-\vec p')$ |
| $N = a^\dagger a$ | 激发级数 | 粒子数算符 |
| $H = N + \tfrac12$ | 等间隔能谱 + 零点能 | 自由场哈密顿量 + 真空能发散 |
| $\lvert n\rangle = (a^\dagger)^n\lvert 0\rangle/\sqrt{n!}$ | 第 $n$ 激发态 | $n$ 粒子态（Fock 空间） |
| $\sqrt{n+1}$ 因子 | 升容易降有底 | 玻色增强（受激辐射） |
| 简正模分解 | 耦合振子 → 独立模 | 场的傅里叶模式展开 |
| 声子（$\omega_k$ 线性色散） | 固体元激发 | 粒子（$\omega_p = \sqrt{p^2+m^2}$） |
| 相干态 $\lvert\alpha\rangle$ | 最像经典的量子态 | 经典场 = 场的相干态 |
| 零点能 $\tfrac12\hbar\omega$ | Casimir 效应可测 | 真空能 / 正规序 / 宇宙学常数问题 |

## 自检问题

**1.** 从 $[x, p] = i\hbar$ 出发（不取无量纲单位），定义合适的 $a$，验证 $[a, a^\dagger] = 1$ 并推出 $H = \hbar\omega\left(a^\dagger a + \tfrac12\right)$。

<details markdown="1"><summary>点击显示答案</summary>

量纲分析给出 $x$ 的尺度 $\sqrt{\hbar/(m\omega)}$、$p$ 的尺度 $\sqrt{\hbar m\omega}$，于是定义无量纲组合

$$a = \sqrt{\frac{m\omega}{2\hbar}}\,x + \frac{i}{\sqrt{2\hbar m\omega}}\,p.$$

计算对易子：

$$[a, a^\dagger] = \left[\sqrt{\frac{m\omega}{2\hbar}}\,x + \frac{i}{\sqrt{2\hbar m\omega}}\,p,\ \ \sqrt{\frac{m\omega}{2\hbar}}\,x - \frac{i}{\sqrt{2\hbar m\omega}}\,p\right]$$

$$= -\frac{i}{2\hbar}[x, p] + \frac{i}{2\hbar}[p, x] = -\frac{i}{2\hbar}(i\hbar) + \frac{i}{2\hbar}(-i\hbar) = \frac12 + \frac12 = 1.$$

再算乘积：

$$a^\dagger a = \left(\sqrt{\frac{m\omega}{2\hbar}}\,x - \frac{i}{\sqrt{2\hbar m\omega}}\,p\right)\left(\sqrt{\frac{m\omega}{2\hbar}}\,x + \frac{i}{\sqrt{2\hbar m\omega}}\,p\right)$$

$$= \frac{m\omega}{2\hbar}x^2 + \frac{p^2}{2\hbar m\omega} + \frac{i}{2\hbar}[x, p] = \frac{1}{\hbar\omega}\left(\frac{p^2}{2m} + \frac12 m\omega^2 x^2\right) - \frac12 = \frac{H}{\hbar\omega} - \frac12,$$

即 $H = \hbar\omega\left(a^\dagger a + \tfrac12\right)$。关键一步就是交叉项里的 $[x, p] = i\hbar$ 贡献了那个 $-\tfrac12$，零点能由此而来。

</details>

**2.** 只用 $[a, a^\dagger] = 1$ 与内积正定性，证明 $N = a^\dagger a$ 的本征值只能是 $n = 0, 1, 2, \dots$，且基态被 $a|0\rangle = 0$ 唯一刻画。

<details markdown="1"><summary>点击显示答案</summary>

**非负性**：对任意本征态 $N|n\rangle = n|n\rangle$（$\langle n|n\rangle = 1$），

$$n = \langle n|a^\dagger a|n\rangle = \lVert\,a|n\rangle\,\rVert^2 \geq 0.$$

**降一步**：由 $[N, a] = -a$，$N\big(a|n\rangle\big) = (n-1)\,a|n\rangle$，所以 $a|n\rangle$ 若非零就是本征值 $n-1$ 的本征态。

**链必终止**：反复作用 $a$ 得到本征值序列 $n, n-1, n-2, \dots$。若非整数，足够多步后本征值变负，与非负性矛盾。因此必须存在某一步 $k$ 使 $a^{k+1}|n\rangle = 0$ 而 $a^k|n\rangle \neq 0$；记 $|\Omega\rangle \propto a^k|n\rangle$，则 $a|\Omega\rangle = 0$，从而 $N|\Omega\rangle = a^\dagger a|\Omega\rangle = 0$，即 $|\Omega\rangle$ 是本征值 $0$ 的态，且 $n = k$ 为非负整数。

**基态刻画**：$N|\psi\rangle = 0 \iff \lVert a|\psi\rangle\rVert^2 = 0 \iff a|\psi\rangle = 0$（内积正定）。位置表象下这是一阶方程 $(x + d/dx)\psi_0 = 0$，归一化解 $\psi_0 \propto e^{-x^2/2}$ 唯一，故基态（从而整条塔）非简并。

</details>

**3.** 用代数法计算 $\langle n|x^2|n\rangle$ 与 $\langle n|p^2|n\rangle$，并验证能量均分：$\langle n|T|n\rangle = \langle n|V|n\rangle = E_n/2$（取 $\hbar = m = \omega = 1$）。

<details markdown="1"><summary>点击显示答案</summary>

由 $x = (a + a^\dagger)/\sqrt2$：

$$x^2 = \frac12\left(a^2 + a^{\dagger 2} + aa^\dagger + a^\dagger a\right) = \frac12\left(a^2 + a^{\dagger 2} + 2N + 1\right),$$

用到 $aa^\dagger = a^\dagger a + 1$。在 $|n\rangle$ 中取期望：$a^2|n\rangle \propto |n-2\rangle$、$a^{\dagger 2}|n\rangle \propto |n+2\rangle$，均与 $\langle n|$ 正交，对角元为零。于是

$$\langle n|x^2|n\rangle = \frac12(2n + 1) = n + \frac12.$$

同理 $p = (a - a^\dagger)/(i\sqrt2)$，$p^2 = -\tfrac12(a^2 + a^{\dagger 2} - 2N - 1)$，故

$$\langle n|p^2|n\rangle = n + \frac12.$$

能量均分：$\langle V\rangle = \tfrac12\langle x^2\rangle = \tfrac12(n+\tfrac12) = E_n/2$，$\langle T\rangle = \tfrac12\langle p^2\rangle = E_n/2$，二者相等——这是位力定理对二次势的结论（$2\langle T\rangle = \langle x\,dV/dx\rangle = 2\langle V\rangle$），代数法一行就看到了。

</details>

**4.** 两个全同振子（质量 $m$、频率 $\omega$）以弹性系数 $K$ 耦合：$H = \tfrac{p_1^2 + p_2^2}{2m} + \tfrac12 m\omega^2(x_1^2 + x_2^2) + \tfrac12 K(x_1 - x_2)^2$。求简正模、频率与基态能量，并解释为什么 $K \to \infty$ 时一个模的频率发散而另一个不变。

<details markdown="1"><summary>点击显示答案</summary>

取 $x_\pm = (x_1 \pm x_2)/\sqrt2$，$p_\pm = (p_1 \pm p_2)/\sqrt2$。验证：$[x_+, p_+] = \tfrac12[x_1 + x_2, p_1 + p_2] = \tfrac12(i\hbar + i\hbar) = i\hbar$，交叉项 $[x_+, p_-] = \tfrac12[x_1 + x_2, p_1 - p_2] = 0$。且 $x_1^2 + x_2^2 = x_+^2 + x_-^2$，$(x_1 - x_2)^2 = 2x_-^2$。代入得

$$H = \left[\frac{p_+^2}{2m} + \frac12 m\omega^2 x_+^2\right] + \left[\frac{p_-^2}{2m} + \frac12\big(m\omega^2 + 2K\big) x_-^2\right],$$

两个独立振子，频率

$$\Omega_+ = \omega, \qquad \Omega_- = \sqrt{\omega^2 + \frac{2K}{m}}.$$

基态能量 $E_0 = \tfrac12\hbar(\Omega_+ + \Omega_-)$。

**物理解释**：$x_+$ 模两振子同向等幅运动，耦合弹簧长度不变，$K$ 完全不参与，故 $\Omega_+ = \omega$ 与 $K$ 无关；$x_-$ 模两振子对挤，弹簧形变最大，$K \to \infty$ 相当于把两体刚性锁死在固定间距上，相对振动的恢复力无穷大，$\Omega_- \to \infty$。这也是一切"软模/硬模"图像的原型：对称性决定的模不受耦合影响（推广到场论里就是"零模"与 Goldstone 模的远亲）。

</details>

**5.** 对相干态 $|\alpha\rangle = e^{-|\alpha|^2/2}\sum_n \alpha^n|n\rangle/\sqrt{n!}$：验证 $a|\alpha\rangle = \alpha|\alpha\rangle$，并计算 $\langle\alpha|x(t)|\alpha\rangle$（$\hbar = m = \omega = 1$），说明它与经典解的关系。

<details markdown="1"><summary>点击显示答案</summary>

**验证本征值方程**：用 $a|n\rangle = \sqrt{n}|n-1\rangle$，

$$a|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=1}^{\infty}\frac{\alpha^n}{\sqrt{n!}}\sqrt{n}\,|n-1\rangle = e^{-|\alpha|^2/2}\sum_{n=1}^{\infty}\frac{\alpha^n}{\sqrt{(n-1)!}}|n-1\rangle.$$

提出一个 $\alpha$ 并换求和指标 $m = n - 1$：

$$= \alpha\, e^{-|\alpha|^2/2}\sum_{m=0}^{\infty}\frac{\alpha^m}{\sqrt{m!}}|m\rangle = \alpha|\alpha\rangle.$$

（$n=0$ 项被 $a|0\rangle = 0$ 杀掉，这正是求和能从 $n=1$ 起的原因。）

**时间演化**：海森堡绘景下 $\dot a = i[H, a]$，由 $H = N + \tfrac12$ 与 $[N, a] = -a$ 得 $\dot a = -ia$，故 $a(t) = a(0)e^{-it}$，于是 $\alpha(t) = \alpha e^{-it}$。而

$$x(t) = \frac{a(t) + a^\dagger(t)}{\sqrt2} \quad\Longrightarrow\quad \langle x(t)\rangle = \frac{\alpha e^{-it} + \alpha^* e^{it}}{\sqrt2} = \sqrt2\,\mathrm{Re}\big(\alpha e^{-it}\big).$$

写 $\alpha = |\alpha|e^{i\varphi}$，则 $\langle x(t)\rangle = \sqrt2\,|\alpha|\cos(t - \varphi)$——振幅 $\sqrt2|\alpha|$、初相 $\varphi$ 的余弦振荡，**正是经典谐振子 $x_{\mathrm{cl}}(t) = A\cos(\omega t - \varphi)$ 的解**（恢复 $\omega$ 即 $\cos(\omega t - \varphi)$）。复本征值 $\alpha$ 的模与辐角恰好编码经典振幅与初相，期望值严格走经典轨道，这就是"相干态是最像经典的量子态"的精确含义。

</details>

## 参考

- Griffiths《量子力学概论》第 2.3 节（谐振子的代数解法与级数解法对照）——本篇第 3、4 节与之对应。
- Sakurai《现代量子力学》第 2.3 节（谐振子，含相干态的简洁处理）与第 2.5 节相关部分。
- Shankar《Principles of Quantum Mechanics》第 7 章（谐振子，代数法讲得最透）与第 7.5 节（简正模 / 耦合振子）。
- （Casimir 效应）Lamoreaux, Phys. Rev. Lett. 78, 5 (1997)（实验）；Casimir 力公式的推导见多数 QFT 教材第一章，如 Peskin & Schroeder 前的入门讨论。
