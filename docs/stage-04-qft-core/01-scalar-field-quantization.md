# 标量场量子化：从无穷多谐振子到粒子

> 路线图位置：第 4 阶段（QFT 核心）· 第 1 篇（主战场开篇）
> 前置知识：量子力学谐振子的产生/湮灭算符解法；[KG 方程与 Dirac 方程：相对论量子力学的尝试及其失败](../stage-03-relativistic-qm/01-klein-gordon-and-dirac.md)（负能量、多粒子与因果性三大困难）；[场的拉格朗日形式：从弦的振动到诺特定理](../stage-03-relativistic-qm/02-lagrangian-field-theory.md)（珠链连续极限、正则动量、诺特定理）。
> 学习目标：亲手走完"把 Klein–Gordon 场当成无穷多个谐振子来量子化"的每一步；说清楚"粒子是场的激发"的精确含义；看到 KG 篇的三大困难如何在同一套构造里被一并解决。

全文用自然单位 $\hbar = c = 1$，度规 $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$，$px \equiv p_\mu x^\mu = \omega_p t - \vec p\cdot\vec x$，其中 $\omega_p \equiv \sqrt{\vec p^2 + m^2}$。

---

## 1. 一句话总结

**Klein–Gordon 场不是"某个粒子的波函数"，而是无穷多个谐振子的集合——每个动量模式 $\vec p$ 一个。把这些谐振子按量子力学的老办法量子化，产生算符 $a^\dagger_p$ 创造一个动量为 $\vec p$、能量 $\omega_p=\sqrt{\vec p^2+m^2}$（恒正）的粒子：KG 篇的负能量灾难就此消失；多粒子态（Fock 空间）自动出现，粒子数可变不是外加的假设，而是这套构造的天生特性。**

下面把这句话一层一层算出来。

## 2. 复习：单个谐振子的代数解法——本篇的全部武器

取单位质量的谐振子，$H = \tfrac12 p^2 + \tfrac12\omega^2 q^2$，$[q, p] = i$。定义

$$a = \frac{1}{\sqrt{2\omega}}\left(\omega q + ip\right), \qquad a^\dagger = \frac{1}{\sqrt{2\omega}}\left(\omega q - ip\right),$$

由 $[q,p]=i$ 立刻得到

$$[a, a^\dagger] = 1, \qquad H = \omega\left(a^\dagger a + \tfrac12\right).$$

粒子数算符 $N \equiv a^\dagger a$ 的本征值是 $n = 0, 1, 2, \dots$，本征态 $|n\rangle$ 的能量是 $(n+\tfrac12)\omega$，且

$$a|n\rangle = \sqrt{n}\,|n-1\rangle, \qquad a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle, \qquad a|0\rangle = 0.$$

三点提醒，后面全部用得上：

- **谱和态全部来自对易关系一条**（外加 $N$ 的正定性），没有解任何微分方程。这是纯代数构造。
- 基态 $|0\rangle$ 的能量是 $\omega/2$ 而非零——零点振动；基态不是"静止"。
- $|n\rangle$ 是**激发态**：$n$ 不是"系统里有几个东西"，而是振子被激发了几次。

本篇后面没有任何新的量子力学——只是把这套代数复制无穷多份，下标从振子编号换成动量 $\vec p$。

## 3. 经典场的模式分解：每个动量模式是一个谐振子

实标量场的拉氏量与 KG 方程：

$$\mathcal L = \frac12\,\partial_\mu\phi\,\partial^\mu\phi - \frac12 m^2\phi^2 \quad\Longrightarrow\quad \left(\partial^2 + m^2\right)\phi = 0.$$

平面波 $e^{\pm ipx}$（取 $p^0 = \omega_p$，即在壳）是解。实场的一般解是所有模式的叠加，且实条件 $\phi = \phi^*$ 强制负频部分是正频部分的复共轭：

$$\phi(x) = \int\frac{d^3p}{(2\pi)^3}\,\frac{1}{2\omega_p}\left(a_p\,e^{-ipx} + a_p^{*}\,e^{ipx}\right), \qquad p^0 = \omega_p.$$

眼下 $a_p$ 只是复数（$c$ 数），写成 $a_p^*$；量子化之后它会被替换成 $a_p^\dagger$。两点说明：

- $\frac{1}{2\omega_p}$ 是**相对论归一化**：$d^3p/(2\omega_p)$ 是洛伦兹不变测度（第 4 节补充说明里证明）。不同教材在这里差一个 $2\omega_p$ 因子，第 4 节还会回来对账。
- 每个模式的时间依赖是 $e^{\mp i\omega_p t}$，即系数 $\alpha_p(t) = a_p e^{-i\omega_p t}$ 满足

$$\ddot\alpha_p + \omega_p^2\,\alpha_p = 0,$$

这正是频率 $\omega_p$ 的谐振子方程。

这正是[场的拉格朗日形式](../stage-03-relativistic-qm/02-lagrangian-field-theory.md)一篇里珠链连续极限的相对论版本：珠链的每个简正模式是一个独立振子，场的每个动量模式也是。**结论：自由 KG 场 = 无穷多个互不耦合的谐振子，由动量 $\vec p$ 标记，频率为 $\omega_p$；场值 $\phi(\vec x, t)$ 只是这无穷多个振子坐标的傅里叶叠加。**量子化它不需要任何新发明。

## 4. 正则量子化：场变成算符

正则动量在 02 篇第 5 节已经备好：

$$\pi(x) = \frac{\partial\mathcal L}{\partial\dot\phi} = \dot\phi(x).$$

量子化处方 = 把泊松括号换成等时对易子（对照 $[\hat q_i, \hat p_j] = i\delta_{ij}$，空间点 $\vec x$ 是自由度的连续标签）：

$$[\phi(\vec x, t),\, \pi(\vec y, t)] = i\,\delta^3(\vec x - \vec y),$$

$$[\phi(\vec x, t),\, \phi(\vec y, t)] = [\pi(\vec x, t),\, \pi(\vec y, t)] = 0.$$

把展开式里的 $a_p$ 提升为算符、$a_p^*$ 换成 $a_p^\dagger$：

$$\phi(x) = \int\frac{d^3p}{(2\pi)^3}\,\frac{1}{2\omega_p}\left(a_p\,e^{-ipx} + a_p^\dagger\,e^{ipx}\right),$$

$\phi$ 从此是厄米算符。反演公式（直接代入即可验证，右边的 $t$ 依赖恰好相消，所以 $a_p$ 是守恒量）：

$$a_p = \int d^3x\; e^{ipx}\left(\omega_p\,\phi(x) + i\,\pi(x)\right).$$

现在从等时对易关系反推产生湮灭算符的对易关系，给出关键步骤：

$$[a_p, a_q^\dagger] = \int d^3x\,d^3y\; e^{ipx - iqy}\left[\omega_p\phi(x) + i\pi(x),\; \omega_q\phi(y) - i\pi(y)\right].$$

同类算符的对易子为零，只剩两个交叉项，代入 $[\phi,\pi]=i\delta^3$ 与 $[\pi,\phi]=-i\delta^3$：

$$= \int d^3x\,d^3y\; e^{ipx-iqy}\left(\omega_p + \omega_q\right)\delta^3(\vec x - \vec y) = \int d^3x\; e^{i(\omega_p-\omega_q)t}\,e^{-i(\vec p-\vec q)\cdot\vec x}\left(\omega_p + \omega_q\right).$$

对 $\vec x$ 积分给出 $(2\pi)^3\delta^3(\vec p-\vec q)$；$\delta$ 函数强制 $\vec p = \vec q$，从而 $\omega_p = \omega_q$，时间因子变 1：

$$\boxed{[a_p, a_q^\dagger] = (2\pi)^3\,2\omega_p\,\delta^3(\vec p - \vec q)}, \qquad [a_p, a_q] = [a_p^\dagger, a_q^\dagger] = 0.$$

这就是第 2 节的 $[a, a^\dagger]=1$ 的无穷多份拷贝——对易子的形式稍有不同，纯粹是归一化选择：我们的展开带 $1/(2\omega_p)$（Srednicki、Schwartz 风格），对易子右边就带 $2\omega_p$；Peskin 的展开带 $1/\sqrt{2\omega_p}$，对易子是 $(2\pi)^3\delta^3(\vec p-\vec q)$。物理完全相同，只是给每个振子选的"尺子"不同；我们的归一化让单粒子态有洛伦兹协变的归一化（自检第 5 题）。

<details markdown="1"><summary>补充说明：为什么 $d^3p/(2\omega_p)$ 是洛伦兹不变测度</summary>

断言：

$$\int\frac{d^3p}{2\omega_p} = \int d^4p\;\delta(p^2 - m^2)\,\theta(p^0).$$

验证：对 $p^0$ 积分。$\delta(p^2 - m^2) = \delta\big((p^0)^2 - \omega_p^2\big)$，利用 $\delta(f(x)) = \sum_i \delta(x-x_i)/|f'(x_i)|$，正根 $p^0 = \omega_p$ 处贡献 $1/(2\omega_p)$，$\theta(p^0)$ 剔掉负根，正好回到左边。

右边整体是洛伦兹不变的（限正常正时变换）：$d^4p$ 的雅可比 $|\det\Lambda| = 1$，$\delta(p^2-m^2)$ 是标量，$\theta(p^0)$ 对质壳上的正能模式在正常正时变换下不变。所以模式展开中的 $\frac{d^3p}{(2\pi)^3\,2\omega_p}$ 是协变测度，$(2\pi)^3$ 只是傅里叶变换的约定。

</details>

## 5. 哈密顿量与零点能

哈密顿量是

$$H = \int d^3x\;\frac12\left[\pi^2 + (\nabla\phi)^2 + m^2\phi^2\right].$$

把模式展开代入。$\int d^3x$ 把动量锁定为 $\vec q = \pm\vec p$；$\vec q = -\vec p$ 的时间依赖项（正比于 $a_p a_{-p}e^{-2i\omega_p t}$ 及其厄米共轭）系数恰为 $-\omega_p^2 + \vec p^2 + m^2 = 0$（在壳条件）而消去，只剩对角项：

$$H = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\frac{\omega_p}{2}\left(a_p^\dagger a_p + a_p a_p^\dagger\right).$$

用对易关系把 $a_p a_p^\dagger$ 换成 $a_p^\dagger a_p + (2\pi)^3\,2\omega_p\,\delta^3(0)$，并注意 $(2\pi)^3\delta^3(0) = \int d^3x = V$（体积，自检第 2 题）：

$$H = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\omega_p\,a_p^\dagger a_p \;+\; V\int\frac{d^3p}{(2\pi)^3}\;\frac{\omega_p}{2}.$$

第二项就是零点能 $E_0$：每个振子贡献 $\omega_p/2$，无穷多个振子求和给出无穷大——连能量密度都发散。处理方式与物理评注：

- **正规序（normal ordering）**：定义 $:\ :$ 为"把所有 $a$ 排到所有 $a^\dagger$ 右边"的操作，并宣布物理哈密顿量是

$$\colon\!H\!\colon = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\omega_p\,a_p^\dagger a_p.$$

- 物理辩护：在不涉及引力的物理里只有**能量差**可测，给 $H$ 整体加一个常数（哪怕无穷大）不改变任何预言。正规序就是把能量原点取在真空。
- **例外是引力**：能动张量的绝对值要进爱因斯坦方程，真空能量等效于一个宇宙学常数。观测值与"Planck 尺度截断"的自然估计差约 $10^{120}$ 个数量级——这就是宇宙学常数问题，本篇只需知道它存在。
- 真空 $|0\rangle$ 由 $a_p|0\rangle = 0$（所有 $\vec p$）定义。它不是"什么都没有"，而是所有振子的基态：$\langle0|\phi(x)\phi(y)|0\rangle \neq 0$——真空有零点涨落，只是涨落的平均能量被我们重新归零了。

同样可得总动量算符（正规序；零点动量因 $\vec p \to -\vec p$ 对称自动为零）：

$$\vec P = -\int d^3x\;\pi\,\nabla\phi \;=\; \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\vec p\;a_p^\dagger a_p.$$

## 6. 粒子诠释：粒子是场的激发

本章的思想高潮。定义单粒子态

$$|p\rangle \equiv a_p^\dagger|0\rangle.$$

它携带什么能量和动量？先算（用 $[a_q^\dagger a_q,\, a_p^\dagger] = a_q^\dagger[a_q, a_p^\dagger]$ 再对 $\vec q$ 积分）：

$$[H, a_p^\dagger] = \omega_p\,a_p^\dagger, \qquad [\vec P, a_p^\dagger] = \vec p\,a_p^\dagger,$$

于是（正规序后 $H|0\rangle = 0$）

$$H|p\rangle = [H, a_p^\dagger]|0\rangle = \omega_p\,|p\rangle, \qquad \vec P|p\rangle = \vec p\,|p\rangle.$$

即 $|p\rangle$ 有能量 $\omega_p = \sqrt{\vec p^2 + m^2} > 0$、动量 $\vec p$，满足相对论性色散关系——**这就是一个质量 $m$ 的自由粒子**。逐条清点 KG 篇的困难是如何被治好的：

- **负能量灾难**：$H$ 是正算符之和（$\omega_p a_p^\dagger a_p \geq 0$），谱自动有下界。KG 篇里 $E = -\omega_p$ 的解不再对应任何态；负频部分 $e^{+ipx}$ 挂着的是产生算符 $a^\dagger$——它把能量**抬高** $\omega_p$。负能量解没有被删掉，而是被重新解释成了升算符。
- **多粒子困难**：$|p_1, \dots, p_n\rangle = a_{p_1}^\dagger\cdots a_{p_n}^\dagger|0\rangle$ 是合法的态，能量动量逐项相加。波函数 $\psi(\vec x)$ 的自变量只有一个 $\vec x$，天生写不下两个粒子；场算符的态空间没有这个限制。
- **玻色统计**：$[a_p^\dagger, a_q^\dagger] = 0$ 直接给出 $|p_1, p_2\rangle = |p_2, p_1\rangle$——交换对称性是**对易关系的推论**，不是外加的对称化假设。"全同粒子"也不再神秘：它们不是两个恰好不可分辨的东西，而是同一场的两个量子。

全部态构成 **Fock 空间**：

$$\mathcal H = \mathcal H_0 \oplus \mathcal H_1 \oplus \mathcal H_2 \oplus \cdots, \qquad \mathcal H_n = \{a_{p_1}^\dagger\cdots a_{p_n}^\dagger|0\rangle\ \text{的叠加}\}.$$

粒子数算符 $N = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}a_p^\dagger a_p$ 在自由理论中与 $H$ 对易；一旦加入相互作用（见后续相互作用/费曼图笔记），$N$ 不再守恒，粒子产生与湮灭成为日常——粒子数可变是这套构造的天生特性。

于是"什么是粒子"有了全新的、可操作的答案：

$$\boxed{\text{粒子 = 场的量子化激发；量子化的是场，粒子是结果。}}$$

一个附注：$\phi(\vec x, 0)|0\rangle$ 大致是"在 $\vec x$ 处造一个粒子"，但这类态彼此不正交，定域性在康普顿波长 $\sim 1/m$ 以下失效——这正是 KG 篇康普顿波长论证在场论中的回响。QFT 干脆放弃了"单个粒子的位置表象"，换来的是粒子数的自由。

## 7. 复标量场与反粒子

复标量场有两个实自由度，$\mathcal L = \partial_\mu\phi^\dagger\partial^\mu\phi - m^2\phi^\dagger\phi$。$\phi$ 不再受实条件约束，正频与负频部分是独立的两套算符：

$$\phi(x) = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(a_p\,e^{-ipx} + b_p^\dagger\,e^{ipx}\right),$$

$$\phi^\dagger(x) = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(b_p\,e^{-ipx} + a_p^\dagger\,e^{ipx}\right),$$

$$[a_p, a_q^\dagger] = [b_p, b_q^\dagger] = (2\pi)^3\,2\omega_p\,\delta^3(\vec p-\vec q), \qquad \text{其余对易子全为零}.$$

诠释：$\phi$ 的正频部分**湮灭一个粒子**（$a_p$），负频部分**产生一个反粒子**（$b_p^\dagger$）。注意措辞：不是"湮灭一个负能量粒子"，而是创造一个正能量 $\omega_p$ 的反粒子。

这个理论有整体 U(1) 对称性 $\phi \to e^{i\alpha}\phi$，诺特流在 02 篇第 7 节已经算过：$j^\mu = i\left[\phi^\dagger\partial^\mu\phi - (\partial^\mu\phi^\dagger)\phi\right]$。守恒荷（正规序后；推导见自检第 4 题）：

$$Q = \int d^3x\; j^0 = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(a_p^\dagger a_p - b_p^\dagger b_p\right) = N_a - N_b.$$

两条物理解读：

- **KG 篇那个"不能当概率"的流正式平反。**当年 $j^0$ 因可正可负被判了"不是概率密度"的死刑——它确实不是概率密度，它是**电荷密度**：粒子带 $+1$ 单位荷、反粒子带 $-1$，$Q = N_a - N_b$ 可正可负天经地义。当年的"病"是误把电荷当成了概率。
- **反粒子与粒子平权。**对玻色子没有泡利不相容原理，没有"Dirac 海"可填；反粒子不是海里的洞，而是与粒子完全对称的另一套激发。只要坚持"能量恒正 + 因果性"（下一节），反粒子就是理论强制要求的居民。

## 8. 因果性与 Feynman 传播子

KG 篇看到：相对论性单粒子波函数有超光速的"因果性尾巴"。QFT 里正确的提问方式是：**类空间隔上的两个测量能否互相干扰？**可观测量由 $\phi$（及其函数）构成，所以微观因果性要求

$$[\phi(x), \phi(y)] = 0, \qquad (x-y)^2 < 0.$$

直接计算：只有 $[a, a^\dagger]$ 与 $[a^\dagger, a]$ 两类项幸存，得

$$[\phi(x), \phi(y)] = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(e^{-ip(x-y)} - e^{ip(x-y)}\right).$$

相消论证分两步：

1. 测度与相位都是洛伦兹不变的，所以右边是 $x-y$ 的洛伦兹不变函数。对类空间隔，总可以 boost 到 $x^0 = y^0$ 的参考系。
2. 在该参考系中

$$[\phi(x), \phi(y)]\big|_{x^0 = y^0} = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(e^{i\vec p\cdot(\vec x-\vec y)} - e^{-i\vec p\cdot(\vec x-\vec y)}\right) = 0,$$

第二项换变量 $\vec p \to -\vec p$（$\omega_p$ 是 $\vec p$ 的偶函数，测度不变）后与第一项严格相消。故类空间隔上对易子恒为零，**微观因果性成立**。对类时间隔不存在这样的参考系，对易子一般非零——因果影响该传就传。

注意相消的机制：它是 $y\to x$ 的正频（粒子）传播与 $x\to y$ 的负频（反粒子）传播之间的**严格对消**。KG 篇的负能量解没有死——它转世成了反粒子，而"两套过程相消"正是治好因果性尾巴的机制。

接下来定义**编时乘积**（time-ordered product）与 **Feynman 传播子**：

$$T\phi(x)\phi(y) = \theta(x^0 - y^0)\,\phi(x)\phi(y) + \theta(y^0 - x^0)\,\phi(y)\phi(x).$$

分两种时序计算真空期望值（只有 $a a^\dagger$ 项对 $\langle0|\cdots|0\rangle$ 有贡献），再合并成一个四维积分：

$$\boxed{D_F(x-y) \equiv \langle0|T\phi(x)\phi(y)|0\rangle = \int\frac{d^4p}{(2\pi)^4}\;\frac{i}{p^2 - m^2 + i\epsilon}\;e^{-ip(x-y)}}.$$

三点说明：

- $i\epsilon$（无穷小正数）规定了 $p^0$ 积分如何绕开 $p^0 = \pm\omega_p$ 两个极点，使得沿实轴的积分自动给出"先产生后湮灭"的两种时序；极点绕法的细节见后续传播子笔记。
- $(\partial^2 + m^2)D_F(x-y) = -i\delta^4(x-y)$：它是 KG 算符的格林函数。
- 物理图像：$D_F$ 是"在 $y$ 处产生一个量子、在 $x$ 处湮灭"的振幅；被积动量不必在壳（$p^2$ 可以 $\neq m^2$）——这就是"虚粒子"离壳传播的数学含义。$D_F$ 在光锥外不为零，但一切可观测量（对易子）在类空间隔上严格为零，因果性安然无恙。

预告：相互作用加进来之后，微扰论就是把顶点用一条条 $D_F$ 连起来——费曼图的"内线"就是它。$D_F$ 是整个微扰论的砖瓦（见后续相互作用/费曼图笔记）。

## 9. 小结

谐振子与自由标量场的完整对照：

| 单个谐振子 | 自由标量场 |
|---|---|
| 坐标 $q$、动量 $p$，$[q,p]=i$ | 场 $\phi(\vec x)$、正则动量 $\pi(\vec x)$，$[\phi(\vec x),\pi(\vec y)]=i\delta^3(\vec x-\vec y)$ |
| 一个频率 $\omega$ | 每个 $\vec p$ 一个频率 $\omega_p=\sqrt{\vec p^2+m^2}$ |
| $a,\ a^\dagger$，$[a,a^\dagger]=1$ | $a_p,\ a_p^\dagger$，$[a_p,a_q^\dagger]=(2\pi)^3\,2\omega_p\,\delta^3(\vec p-\vec q)$ |
| $H=\omega(a^\dagger a + \tfrac12)$ | $\colon\!H\!\colon\,=\int\frac{d^3p}{(2\pi)^3\,2\omega_p}\,\omega_p\,a_p^\dagger a_p$ |
| 基态 $\lvert 0\rangle$，零点能 $\omega/2$ | 真空 $\lvert 0\rangle$，零点能 $=\infty$，正规序减掉（能量差才可测；引力除外） |
| 激发态 $\lvert n\rangle$，能量 $(n+\tfrac12)\omega$ | 多粒子态 $a_{p_1}^\dagger\cdots a_{p_n}^\dagger\lvert 0\rangle$，能量 $\sum_i\omega_{p_i}$ |
| 激发次数 $n$ 可任意 | 粒子数可变：Fock 空间；玻色统计自动成立 |

要点回顾：

- **量子化的是场，粒子是结果**：粒子 = 场这个无穷维谐振子集合的激发量子，一一对应于 $a_p^\dagger$ 的作用。
- 负能量灾难的解决：负频解不是负能粒子，而是（反）粒子的产生算符；哈密顿量自动有下界。
- 多粒子困难的解决：Fock 空间天生粒子数可变；全同性与玻色统计是对易关系的推论。
- 因果性的解决：类空间隔对易子严格为零，机制是正频/负频（粒子/反粒子）贡献相消；编时乘积给出 Feynman 传播子，是微扰论的砖瓦。

## 自检问题

**1.** 从等时对易关系 $[\phi(\vec x,t),\pi(\vec y,t)]=i\delta^3(\vec x-\vec y)$ 出发，完整推出 $[a_p, a_q^\dagger] = (2\pi)^3\,2\omega_p\,\delta^3(\vec p-\vec q)$。

<details markdown="1"><summary>点击显示答案</summary>

从反演公式出发：

$$a_p = \int d^3x\;e^{ipx}\left(\omega_p\phi(x) + i\pi(x)\right), \qquad a_q^\dagger = \int d^3y\;e^{-iqy}\left(\omega_q\phi(y) - i\pi(y)\right),$$

其中 $p^0 = \omega_p$、$q^0 = \omega_q$，两边取同一时刻 $t$。代入对易子：

$$[a_p, a_q^\dagger] = \int d^3x\,d^3y\;e^{ipx-iqy}\left[\omega_p\phi(x) + i\pi(x),\ \omega_q\phi(y) - i\pi(y)\right].$$

展开四项：$[\phi,\phi]=[\pi,\pi]=0$ 消去两项；剩下

$$= \int d^3x\,d^3y\;e^{ipx-iqy}\Big(-i\omega_p\,[\phi(x),\pi(y)] + i\omega_q\,[\pi(x),\phi(y)]\Big)$$

$$= \int d^3x\,d^3y\;e^{ipx-iqy}\Big(-i\omega_p\cdot i\delta^3(\vec x-\vec y) + i\omega_q\cdot(-i)\delta^3(\vec x-\vec y)\Big)$$

$$= (\omega_p + \omega_q)\int d^3x\;e^{i(\omega_p-\omega_q)t}\,e^{-i(\vec p-\vec q)\cdot\vec x} = (\omega_p+\omega_q)\,(2\pi)^3\,\delta^3(\vec p-\vec q)\,e^{i(\omega_p-\omega_q)t}.$$

$\delta^3(\vec p-\vec q)$ 强制 $\vec p=\vec q$，从而 $\omega_p=\omega_q$，时间因子为 1、系数变 $2\omega_p$：

$$[a_p, a_q^\dagger] = (2\pi)^3\,2\omega_p\,\delta^3(\vec p-\vec q). \qquad \blacksquare$$

顺带验证反演公式本身：把 $\phi, \pi=\dot\phi$ 的模式展开代入，$\int d^3x\,e^{-i\vec p\cdot\vec x}$ 把动量锁成 $\vec q=\vec p$（$a_p$ 项）与 $\vec q=-\vec p$（$a^\dagger_{-p}$ 项），$\omega_p\phi$ 与 $i\pi$ 对后者的贡献恰好相消、对前者恰好加倍，即得 $a_p$。

</details>

**2.** 计算真空零点能 $E_0$，解释其中 $\delta^3(0)$ 的含义，说明为什么连能量密度都发散，以及正规序如何处理。

<details markdown="1"><summary>点击显示答案</summary>

由第 5 节，零点能来自对易子项：

$$E_0 = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\frac{\omega_p}{2}\;(2\pi)^3\,2\omega_p\,\delta^3(0) = \delta^3(0)\int d^3p\;\frac{\omega_p}{2}.$$

**$\delta^3(0)$ 是体积**。用箱归一化看清它：把场放进体积 $V$ 的箱子，$\delta$ 函数的定义式给出

$$(2\pi)^3\delta^3(\vec p - \vec q) = \int d^3x\;e^{-i(\vec p-\vec q)\cdot\vec x} \;\xrightarrow{\ \vec p=\vec q\ }\; \int d^3x = V,$$

即 $(2\pi)^3\delta^3(0) = V$。所以 $E_0 = V\int\frac{d^3p}{(2\pi)^3}\frac{\omega_p}{2}$：零点能正比于体积，这很自然（均匀充满空间的真空能）。坏消息是**能量密度**仍发散——用动量截断 $\Lambda$ 估计：

$$\rho_0 = \frac{E_0}{V} = \frac{1}{2}\int\frac{d^3p}{(2\pi)^3}\;\omega_p \simeq \frac{4\pi}{2(2\pi)^3}\int_0^\Lambda dp\;p^2\sqrt{p^2+m^2} \sim \frac{\Lambda^4}{16\pi^2},$$

四次发散，截断越高越糟。**正规序**的处理：重新定义哈密顿量为 $\colon\!H\!\colon$（所有 $a$ 排在 $a^\dagger$ 右边），等价于把能量原点平移到真空。辩护理由：非引力物理中只有能量差可测。例外是引力——真空能作为宇宙学常数进爱因斯坦方程，那里这个无穷大（或截断后的巨大有限值）是真实的疑难，即宇宙学常数问题。

</details>

**3.** 证明类空间隔下 $[\phi(x),\phi(y)] = 0$（给出关键步骤即可）。

<details markdown="1"><summary>点击显示答案</summary>

把模式展开代入对易子。$\phi(x)\phi(y)$ 中有四类算符乘积，取对易子后只有 $[a_p, a_q^\dagger]$ 与 $[a_p^\dagger, a_q]$ 两类幸存：

$$[\phi(x),\phi(y)] = \int\frac{d^3p\,d^3q}{(2\pi)^6\,4\omega_p\omega_q}\Big([a_p,a_q^\dagger]\,e^{-ipx+iqy} + [a_p^\dagger, a_q]\,e^{ipx-iqy}\Big)$$

$$= \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(e^{-ip(x-y)} - e^{ip(x-y)}\right).$$

**第一步：洛伦兹不变性。**测度 $d^3p/(2\omega_p)$ 与相位 $p(x-y)$ 都是洛伦兹不变的，故整个积分是 $z \equiv x-y$ 的洛伦兹不变函数。

**第二步：选取特殊参考系。**若 $z$ 类空（$z^2<0$），存在正常正时洛伦兹变换把它变到 $z^0 = 0$（类空间隔两点的时序不是绝对的）。在该系中

$$[\phi(x),\phi(y)] = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(e^{i\vec p\cdot\vec z} - e^{-i\vec p\cdot\vec z}\right).$$

**第三步：相消。**第二项做变量代换 $\vec p\to-\vec p$（$\omega_p$ 是偶函数，测度不变），变成与第一项相同的积分，两者严格相消，得零。由于结果是洛伦兹不变的，它在**所有**参考系中对所有类空间隔为零。$\blacksquare$

对类时间隔，第二步的参考系不存在（时序是绝对的），上述相消论证失效，对易子一般非零——这正是因果影响可以传播的区域。

</details>

**4.** 复标量场：写出 $\phi$ 的算符展开，用 $a, b$ 表示诺特荷 $Q = i\int d^3x\left(\phi^\dagger\dot\phi - \dot\phi^\dagger\phi\right)$，并说明 $Q$ 可正可负为什么现在天经地义。

<details markdown="1"><summary>点击显示答案</summary>

展开式（$\phi$ 无实条件，正、负频部分独立）：

$$\phi(x) = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(a_p e^{-ipx} + b_p^\dagger e^{ipx}\right), \qquad \dot\phi(x) = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(-i\omega_p\right)\left(a_p e^{-ipx} - b_p^\dagger e^{ipx}\right).$$

代入 $Q$。$\int d^3x$ 把动量锁成 $\vec q = \pm\vec p$。先看对角项（$\vec q = \vec p$），两个结构分别给出：

$$\int d^3x\;\phi^\dagger\dot\phi = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\frac{i}{2}\left(b_p b_p^\dagger - a_p^\dagger a_p\right) + (\text{含时交叉项}),$$

$$\int d^3x\;\dot\phi^\dagger\phi = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;\frac{i}{2}\left(a_p^\dagger a_p - b_p b_p^\dagger\right) + (\text{同样的含时交叉项}).$$

$\vec q = -\vec p$ 的含时交叉项（$b_p a_{-p}e^{-2i\omega_p t}$ 与 $a_p^\dagger b_{-p}^\dagger e^{2i\omega_p t}$）在两式中完全相同，相减时严格消去。对角项相减后翻倍，再乘以外面的 $i$（$i\cdot i = -1$ 翻转符号）：

$$Q = i\int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;i\left(b_p b_p^\dagger - a_p^\dagger a_p\right) = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(a_p^\dagger a_p - b_p b_p^\dagger\right).$$

把 $b_p b_p^\dagger = b_p^\dagger b_p + (2\pi)^3\,2\omega_p\,\delta^3(0)$ 代入，常数项与零点能同性质（无限大），正规序去掉：

$$\colon\!Q\!\colon = \int\frac{d^3p}{(2\pi)^3\,2\omega_p}\left(a_p^\dagger a_p - b_p^\dagger b_p\right) = N_a - N_b.$$

最后一项与零点能同性质，正规序去掉，得

$$\colon\!Q\!\colon = N_a - N_b.$$

**为什么可正可负天经地义**：$Q$ 是 U(1) 对称性的诺特荷，物理身份是**电荷**（粒子 $+1$、反粒子 $-1$），不是概率。KG 篇的困境来自把 $j^0$ 误读为概率密度——概率必须正定，而电荷本来就有两种符号。$Q$ 与 $H$ 对易，是守恒量；态的 $Q$ 值就是"粒子数减反粒子数"。$\blacksquare$

</details>

**5.** 计算单粒子态的内积 $\langle p|q\rangle$，说明这种归一化为什么是"相对论性"的，并与 Peskin 的归一化对照。

<details markdown="1"><summary>点击显示答案</summary>

$|p\rangle = a_p^\dagger|0\rangle$，$\langle p| = \langle0|a_p$。用对易关系：

$$\langle p|q\rangle = \langle0|a_p a_q^\dagger|0\rangle = \langle0|\left([a_p, a_q^\dagger] + a_q^\dagger a_p\right)|0\rangle.$$

第二项中 $a_p|0\rangle = 0$（或 $\langle0|a_q^\dagger = 0$），只剩对易子：

$$\boxed{\langle p|q\rangle = (2\pi)^3\,2\omega_p\,\delta^3(\vec p - \vec q)}.$$

态不是 $\delta$ 归一而是 $\delta^3$ 归一（连续谱的标准情况），且多了一个因子 $2\omega_p$。

**为什么这是相对论性的**：关键在于 $\omega_p\,\delta^3(\vec p-\vec q)$ 这个组合是洛伦兹不变的。最直接的看法是单粒子子空间上的完备性关系

$$\int\frac{d^3p}{(2\pi)^3\,2\omega_p}\;|p\rangle\langle p| = \mathbb 1_{\mathcal H_1},$$

左边测度 $d^3p/(2\omega_p)$ 洛伦兹不变（第 4 节补充说明），所以右边的单位分解协变；这要求 $|p\rangle$ 的归一化恰好携带 $2\omega_p$，使得 boost 后的态仍满足同样的关系（$2\omega_p\delta^3(\vec p-\vec q)$ 在沿 $\vec p-\vec q$ 方向的 boost 下不变，可由 $\delta$ 函数的雅可比与 $\omega_p$ 的变换相消验证）。

**对照 Peskin**：Peskin 的展开带 $1/\sqrt{2\omega_p}$，其对易子为 $[a^{\rm P}_p, a^{\rm P\dagger}_q] = (2\pi)^3\delta^3(\vec p-\vec q)$，对应 $a_p = \sqrt{2\omega_p}\,a^{\rm P}_p$，故 $|p\rangle_{\rm P}$ 的内积没有 $2\omega_p$ 因子——简单，但 boost 时态的归一化会变，做协变计算时要随时补因子。两种约定给出完全相同的 $S$ 矩阵，只是中间步骤的"尺子"不同。$\blacksquare$

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》第 2 章（2.2–2.4：KG 场的正则量子化、粒子诠释、因果性与传播子）——本篇主线；注意其归一化与本篇差 $2\omega_p$ 因子（见第 4 节与自检第 5 题）。
- Schwartz《Quantum Field Theory and the Standard Model》第 2 章（二次量子化的视角：先有场还是先有粒子）。
- Srednicki《Quantum Field Theory》第 3 章（实标量场的正则量子化，归一化与本篇一致，最适合逐行对照验算）。
- Zee《Quantum Field Theory in a Nutshell》I.8（含真空能量与宇宙学常数的物理讨论，直觉极佳）。
