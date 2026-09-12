# 传播子与因果性：费曼传播子

> 路线图位置：第 4 阶段（QFT 核心）· 第 2 篇（紧随[标量场量子化](01-scalar-field-quantization.md)；[第 03 篇](03-interactions-and-feynman-rules.md)的"收缩 = $D_F$"在这里获得完整解释）。
> 前置知识：[标量场量子化](01-scalar-field-quantization.md)（§8 给出了 $D_F$ 的定义、微观因果性证明与三点说明——本篇把其中"细节见后续笔记"的全部欠账展开：$i\epsilon$ 怎么绕极点、为什么恰好这样绕）；复变函数留数法（物理数学必修内容）；[量子力学书·散射理论](../../../quantum-mechanics/docs/08-scattering-theory.md)（Born 近似——自检第 5 题用）。
> 学习目标：会从 $\theta$ 函数出发经围道积分组装出 $D_F$ 的四维动量积分，说清"$i\epsilon$ 处方是时序算符的解析化身"；能画出 $D_F, D_{\bar F}, D_R, D_A$ 四种格林函数的极点分布，逐条说出各自的光锥外行为与用途；能解释"$D_F$ 在类空间隔非零，但因果性毫发无损"这句话的精确含义；会用 $K_1$ 贝塞尔函数的渐近行为读出力程 $1/m$，并从单玻色子交换推出汤川势；知道 Wick 旋转与传播子解析结构的关系。

全文用自然单位 $\hbar = c = 1$，度规 $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$，$px \equiv p_\mu x^\mu = p^0 t - \vec p\cdot\vec x$。沿用第 01 篇的归一化 $[a_p, a_q^\dagger] = (2\pi)^3\,2\omega_p\,\delta^3(\vec p - \vec q)$。

---

## 1. 一句话总结

**KG 算符 $\partial^2 + m^2$ 有无穷多个格林函数，物理学挑出四个标准的（费曼、戴森、推迟、超前），它们的全部分别只在 $p^0$ 复平面上两个极点 $p^0 = \pm\omega_{\vec p}$ 如何绕行——$i\epsilon$ 处方不是任意的约定，而是编时算符里 $\theta$ 函数的解析化身：正能极点下移、负能极点上移，"正能粒子向未来传播 + 负能（反粒子）向过去传播"就成了同一个围道积分的两种闭合方式。费曼传播子在类空间隔非零，看似"超光速"，但它传的是真空关联振幅而非信号；真正承载因果性的是对易子函数——它严格只活在光锥上（无质量）或光锥内（有质量）。光锥外 $D_F$ 以 $e^{-m\rho}$ 指数衰减，力程 $1/m$ 正是康普顿波长——汤川势、核力程、弱作用的短程性都从这一个指数里读出来。**

## 2. 三件套：从场算符乘积读出的三个基本函数

第 01 篇 §8 算过 $[\phi(x),\phi(y)]$ 与 $\langle0\rvert T\phi\phi\rvert 0\rangle$；本篇把这两个对象连同它们的"母函数"放进一个系统。设 $x, y$ 任意，记 $t \equiv x^0 - y^0$。由模式展开（第 01 篇式（4））直接积分可得三个 $c$ 数函数：

**（i）Wightman 正频函数**——算符乘积（不编时）的真空期望：

$$D(x-y) \equiv \langle0\rvert\phi(x)\phi(y)\rvert0\rangle = \int\frac{d^3p}{(2\pi)^3\,2\omega_{\vec p}}\;e^{-ip\cdot(x-y)},\qquad p^0 = \omega_{\vec p}.$$

只有 $a\,a^\dagger$ 型项在真空期望中幸存，故只剩正频平面波。厄米性给出 $D(x-y)^* = D(y-x)$。

**（ii）Pauli–Jordan 对易子函数**——对易子本身：

$$\Delta(x-y) \equiv [\phi(x),\phi(y)] = D(x-y) - D(y-x).$$

这是**唯一携带因果性的对象**：第 01 篇 §8 证明了它在类空间隔严格为零。它是反厄米的（对易子的本性），故为纯虚。

**（iii）编时函数**——把上述两种时序按时间先后拼接（第 01 篇已定义 $T$）：

$$D_F(x-y) \equiv \langle0\rvert T\phi(x)\phi(y)\rvert0\rangle = \theta(t)\,D(x-y) + \theta(-t)\,D(y-x).$$

第 03 篇的核心事实"收缩 = $D_F$"就是这条定义。三件套的关系一目了然：$D_F$ 是 $D$ 与 $D(y-x)$ 的"时序拼接"，$\Delta$ 是两者之差。下面的任务：把这个带 $\theta$ 的三明治写成第 01 篇已引用的四维积分 $\int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip(x-y)}}{p^2-m^2+i\epsilon}$，并解释 $i\epsilon$ 为什么非这样不可。

## 3. $i\epsilon$ 处方：时序的解析化身

### 3.1 两个极点恒等式

一切从下面这对围道恒等式开始（这是本篇的核心计算，值得逐行过一遍）：

$$\int\frac{dp^0}{2\pi}\;\frac{i\,e^{-ip^0 t}}{p^0 - \omega + i\epsilon} = \theta(t)\,e^{-i\omega t},\qquad\quad \int\frac{dp^0}{2\pi}\;\frac{i\,e^{-ip^0 t}}{p^0 + \omega - i\epsilon} = -\theta(-t)\,e^{+i\omega t}.$$

**第一式**：极点在 $p^0 = \omega - i\epsilon$（实轴下方）。$t > 0$ 时 $e^{-ip^0t}$ 在下半平面指数衰减（$p^0 = \mathrm{Re}\,p^0 - i\,\mathrm{Im}\,p^0$ 给出因子 $e^{-\mathrm{Im}\,p^0\,t}$），实轴与下半圆弧围成顺时针闭合围道，只包住这一个极点：

$$\int\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{p^0-\omega+i\epsilon}\Big|_{t>0} = \frac{-2\pi i}{2\pi}\cdot i\,e^{-i(\omega-i\epsilon)t} \;\xrightarrow{\;\epsilon\to0^+\;}\; e^{-i\omega t}.$$

$t<0$ 时只能在上半平面闭合围道（那里才衰减），而极点在下方、围道内空空如也，积分为零。**一个下方极点 $= \theta(t)\times$ 留数**。第二式同理：极点 $-\omega+i\epsilon$ 在上方，只有 $t<0$（上方闭合、逆时针）才拾取它，给出 $\frac{+2\pi i}{2\pi}\cdot i\,e^{-i(-\omega+i\epsilon)t} = -e^{+i\omega t}$。**一个上方极点 $= -\theta(-t)\times$ 留数**。

一句话：**$\pm i\epsilon$ 是 $\theta(\pm t)$ 的解析化身**——把"时间方向的选择"翻译成"极点在实轴哪一侧"。

### 3.2 组装出 $D_F$

把分母因式分解（$\epsilon$ 的归属由 3.1 的需求定死）：

$$p^2 - m^2 + i\epsilon = (p^0)^2 - \omega_{\vec p}^2 + i\epsilon \simeq \big(p^0 - \omega_{\vec p} + i\epsilon\big)\big(p^0 + \omega_{\vec p} - i\epsilon\big),$$

部分分式 $\dfrac{i}{p^2-m^2+i\epsilon} = \dfrac{i}{2\omega_{\vec p}}\Big[\dfrac{1}{p^0-\omega_{\vec p}+i\epsilon} - \dfrac{1}{p^0+\omega_{\vec p}-i\epsilon}\Big]$，代入 $\int\frac{dp^0}{2\pi}$ 用 3.1 的两条恒等式：

$$\int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip(x-y)}}{p^2-m^2+i\epsilon} = \int\frac{d^3p}{(2\pi)^3\,2\omega_{\vec p}}\Big[\theta(t)\,e^{-i\omega t + i\vec p\cdot(\vec x-\vec y)} + \theta(-t)\,e^{+i\omega t - i\vec p\cdot(\vec x-\vec y)}\Big],$$

（第二项做了变量代换 $\vec p\to-\vec p$。）右边正是 $\theta(t)D(x-y) + \theta(-t)D(y-x) = D_F(x-y)$——第 01 篇 §8 引用的四维积分公式至此推导完毕（完整逐行版本是自检第 2 题）。

### 3.3 极点图景的物理：正能向未来，负能向过去

把 3.2 反着读一遍，就是 Feynman 传播子的"运行说明书"：

- $x^0 > y^0$：围道向下闭合，只拾取**正能极点** $p^0 = \omega - i\epsilon$——正能量子从 $y$ 传播到 $x$；
- $x^0 < y^0$：围道向上闭合，只拾取**负能极点** $p^0 = -\omega + i\epsilon$，因子 $e^{+i\omega t}$ 等价于**负能量子从 $x$ 传到 $y$，即反量子从 $y$ 传到 $x$**。

第 01 篇 §8 末尾那句"负能量解转世成反粒子"在此有了积分语言：$i\epsilon$ 处方就是 Feynman–Stueckelberg 解释的解析书写。这也是微扰论里"反粒子 = 逆着箭头传播的粒子"全部图像的源头——第 05 篇 QED 的费米子线箭头约定即源于此。

## 4. 格林函数全家福：四种绕极点的方式

$D_F$ 满足 $(\partial^2 + m^2)D_F = -i\delta^4(x)$（第 01 篇 §8），即它是 KG 算符的格林函数。同一算符还有三个标准搭档，区别全在极点绕法：

| 函数 | 极点处方（$p^0$ 平面） | 动量空间 | 光锥外 | 用途 |
| --- | --- | --- | --- | --- |
| $D_F$（费曼/编时） | $+\omega$ 下、$-\omega$ 上 | $\dfrac{i}{p^2-m^2+i\epsilon}$ | 非零 | 微扰论（第 03 篇的收缩） |
| $D_{\bar F}$（戴森/反编时） | $+\omega$ 上、$-\omega$ 下 | $\dfrac{-i}{p^2-m^2-i\epsilon}$ | 非零 | 反编时微扰论、复共轭 $D_{\bar F} = D_F^*$ |
| $D_R$（推迟） | 两极点都在下方 | $\dfrac{i}{(p^0+i\epsilon)^2-\omega_{\vec p}^2}$ | 恒为零 | 线性响应、信号 |
| $D_A$（超前） | 两极点都在上方 | $\dfrac{i}{(p^0-i\epsilon)^2-\omega_{\vec p}^2}$ | 恒为零 | $D_A(t) = D_R(-t)$ |

互相之间的关系紧凑而有用（$D^c \equiv D(y-x)$，$\epsilon(t)$ 为符号函数）：

$$\Delta = D - D^c = \epsilon(t)\,\big(D_F - D_{\bar F}\big),\qquad\quad D_R = \theta(t)\,\Delta = \theta(t)\big(D_F - D_{\bar F}\big),\qquad\quad D_A = -\theta(-t)\,\Delta.$$

$D_R$ 的因果性一眼可见：两个极点都在下半平面，$t<0$ 时只能在上半平面闭合围道——没有极点，积分严格为零；$t>0$ 拾取两极点之差 $D - D^c = \Delta$（推导见自检第 3 题）。$D_R$ 只活在未来光锥内，这正是"信号传播"应有的形状。

**为什么微扰论偏偏用"不因果"的 $D_F$？** 因为 Dyson 级数与 Wick 定理（第 03 篇）生成的是**编时**乘积——时序算符天然挑出混合处方。反过来，线性响应理论（Kubo 公式）关心"此刻的扰动如何影响彼处的响应"，天然需要 $D_R$——见[量子力学书·线性响应](../../../quantum-mechanics/docs/10-linear-response-kubo.md)与凝聚态书的对应篇目：两本书里的响应函数与本篇的 $D_R$ 是同一个对象的不同装扮。（约定提示：响应理论文献常取实归一化 $(\partial^2+m^2)G_R = -\delta^4$，与本篇的 $-i\delta^4$ 差一个 $i$；对表时留意。）

## 5. 因果性判据：谁负责传信号

**对易子函数 $\Delta$ 的支持严格落在光锥上（无质量）或光锥内（有质量）。** 无质量情形可显式算出（完整推导自检第 4 题）：

$$\Delta(x)\big|_{m=0} = -\frac{i}{4\pi r}\Big[\delta(t-r) - \delta(t+r)\Big] = -\frac{i}{2\pi}\,\epsilon(t)\,\delta(x^2),\qquad r\equiv\lvert\vec x\rvert.$$

两个 $\delta$ 分别贴在未来与过去光锥上，类空间隔（$t^2 < r^2$）上毫无支持。有质量时 $\Delta$ 在光锥**内部**多出一条贝塞尔尾巴，光锥**外部**仍严格为零——质量让信号"拖尾"，但不让信号超光速。

**那 $D_F$ 光锥外非零算什么？** 算关联，不算信号。类空间隔上 $\Delta = D - D^c = 0$ 只说明 $D = D^c$（两种时序的关联相等），并不要求关联本身为零——真空纠缠本来就让类空两点相关（Bell 不等式的教训：关联 ≠ 通信）。能被"用来发信号"的量必须由对易子构造（局域算符的对易关系决定测量干扰如何传播），而它严格为零。第 03 篇讲过同一件事的微扰论版本：$D_F$ 在光锥外非零，但一切可观测量不受影响。

**"虚粒子"语言检讨**：内线动量离壳（$p^2 \neq m^2$）、可以在光锥外"传播"——这是 $D_F$ 的性质被翻译成的图像语言。它对画图记账极有用，但记住两点纪律：虚粒子不出现在初末态（外线在壳）；它不是可探测的中间过程，而是微扰级数里一个积分因子的拟人化。更稳妥的读法：**图 = 积分的拓扑**，"虚粒子传播" = "一行传播子因子"。

## 6. 光锥外：指数衰减与力程

$D_F$ 是洛伦兹不变函数。类空间隔 $x^2 < 0$ 总可以 boost 到等时系（第 01 篇自检第 3 题用过同一招），在那里它退化为三维傅里叶积分 $\int\frac{d^3p}{(2\pi)^3\,2\omega_{\vec p}}e^{i\vec p\cdot\vec x}$，标准结果（Hankel 变换）：

$$D_F(x)\Big|_{x^2<0} = \frac{m}{4\pi^2}\;\frac{K_1\!\big(m\rho\big)}{\rho},\qquad \rho \equiv \sqrt{-x^2},$$

其中 $K_1$ 是第二类修正贝塞尔函数。两个极限各有物理：

- **短距离 $\rho \to 0$**：$K_1(z) \simeq 1/z$，故 $D_F \simeq \dfrac{1}{4\pi^2\rho^2}$——质量完全消失，短距离上的传播子就是无质量传播子。这也是 $D_F(0)$（第 03 篇蝌蚪图用的等点收缩）发散的原因：被积函数大 $p$ 处 $\sim 1/p^2$，$\int d^4p/p^2 \sim \Lambda^2$ 二次发散——紫外问题的第一颗种子，第 06 篇正片。
- **长距离 $\rho \gg 1/m$**：$K_1(z) \simeq \sqrt{\dfrac{\pi}{2z}}\,e^{-z}$，故 $D_F \propto \dfrac{e^{-m\rho}}{\rho^{3/2}}$——**指数衰减，力程 $1/m$**。用不确定性原理读：在距离 $\rho$ 上"赊借"能量 $m$ 躲过质壳，存活时间 $\sim 1/m$，传播距离 $\sim 1/m$。$1/m$ 正是约化康普顿波长。

力程 $1/m$ 的最重要应用是**单玻色子交换势**：静态源之间交换一个质量 $m$ 的玻色子，振幅里的传播子取静态极限，Born 近似（量子力学书第 08 篇）把它翻译成势：

$$V(r) = -\frac{g^2}{4\pi}\,\frac{e^{-mr}}{r}\qquad(\text{汤川势；完整推导自检第 5 题}).$$

同一指数决定三件事：核力程（$\pi$ 介子 $m \approx 135\,\mathrm{MeV}$ 给 $1/m \approx 1.5\,\mathrm{fm}$，正是原子核的尺寸）；弱作用的短程（$m_W \approx 80\,\mathrm{GeV}$ 给 $1/m \approx 0.002\,\mathrm{fm}$，比质子半径小三百多倍——弱作用"弱"的真正原因是重，不是耦合小，第 6 阶段电弱篇会回到这一点）；以及光子的 $m = 0$ 极限 $V \propto 1/r$——库仑长程力。**传播子的极点结构（有无质量隙）直接翻译成力的范围（短程还是长程）**——这是"读拉氏量知物理"最干净的一例。

## 7. 解析结构的两个接口

- **Wick 旋转**：$D_F$ 的两个极点分别在第二、第四象限（$-\omega+i\epsilon$ 与 $+\omega-i\epsilon$），第一、第三象限干净。于是可以把 $p^0$ 积分围道从实轴逆时针旋转 $90°$ 到虚轴（$p^0 \to ip^4_E$）而不扫过任何极点，得到欧氏空间的衰减积分——路径积分量子化的技术基石，[第 07 篇](07-path-integral.md)的地基之一。推迟/超前函数因为两个极点同侧，反而不能这样旋转——$D_F$ 的混合处方是唯一"旋转友好"的。
- **极点 = 粒子**：$D_F(p) = i/(p^2 - m^2 + i\epsilon)$ 的极点恰好在质壳 $p^2 = m^2$ 上，留数承载单粒子态的信息。第 03 篇 §6.2 的"截肢"（在外线极点处取留数）依赖的正是这件事；它的一般版本（传播子极点 ↔ 谱中的粒子，Källén–Lehmann 表示）属于 [S 矩阵与 LSZ 约化](04-s-matrix-lsz-cross-sections.md)与重整化（第 06 篇）的舞台。

## 8. 小结

| 对象 | 定义 | 极点处方 | 光锥外 | 一句话身份 |
| --- | --- | --- | --- | --- |
| $D(x-y)$ | $\langle0\rvert\phi(x)\phi(y)\rvert0\rangle$ | ——（只有 $p^0=+\omega$ 在壳） | 非零 | 正频关联 |
| $\Delta(x-y)$ | $[\phi(x),\phi(y)]$ | 两壳之差 | **严格为零** | 因果性的唯一载体 |
| $D_F(x-y)$ | $\langle0\rvert T\phi\phi\rvert0\rangle$ | $+\omega$ 下、$-\omega$ 上 | 非零，$\sim e^{-m\rho}$ | 微扰论的砖瓦（收缩） |
| $D_{\bar F}$ | $\langle0\rvert\bar T\phi\phi\rvert0\rangle$ | $+\omega$ 上、$-\omega$ 下 | 非零 | $D_F^*$ |
| $D_R$ | $\theta(t)\Delta$ | 两极点下方 | 严格为零 | 信号与响应 |
| $D_A$ | $-\theta(-t)\Delta$ | 两极点上方 | 严格为零 | $D_R$ 的时间反演 |

要点回顾：

- $i\epsilon$ 处方 = 时序算符的解析化身：下方极点给 $\theta(t)$，上方极点给 $-\theta(-t)$；
- 因果性由对易子 $\Delta$ 保证（类空间隔严格为零），$D_F$ 类空非零传的是真空关联，不是信号；
- 光锥外 $D_F \propto e^{-m\rho}$：力程 = 康普顿波长 $1/m$，汤川势、核力程、弱作用短程、库仑长程同出一源；
- 短距离 $D_F \to 1/(4\pi^2\rho^2)$：质量不再重要，等点收缩发散——重整化的种子（第 06 篇）；
- $D_F$ 是唯一允许 Wick 旋转的处方（第一、三象限无极点）——路径积分的地基（第 07 篇）。

## 自检问题

**1.** 证明两条极点恒等式 $\int\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{p^0-\omega+i\epsilon} = \theta(t)e^{-i\omega t}$ 与 $\int\frac{dp^0}{2\pi}\frac{i\,e^{-ip^0t}}{p^0+\omega-i\epsilon} = -\theta(-t)e^{+i\omega t}$，写出两种时间方向下围道的闭合方式、取向与留数，并解释大圆弧为何不贡献。

<details markdown="1"><summary>点击显示答案</summary>

**衰减方向**：设 $p^0 = \mathrm{Re}\,p^0 + i\,\mathrm{Im}\,p^0$，则 $e^{-ip^0t} = e^{-i\mathrm{Re}p^0\,t}\,e^{+\mathrm{Im}p^0\,t}$。$t>0$ 时需要 $\mathrm{Im}\,p^0 < 0$（下半平面）才衰减；$t<0$ 时需要上半平面。圆弧上指数衰减保证 Jordan 引理成立，弧积分趋于零。

**第一式**：极点 $p^0 = \omega - i\epsilon$ 在下方。$t>0$：下半平面顺时针闭合（负定向），围道内含该极点，

$$\int = \frac{-2\pi i}{2\pi}\cdot i\,e^{-i(\omega-i\epsilon)t} = (-i)(i)\,e^{-i\omega t}\,e^{-\epsilon t} \xrightarrow{\epsilon\to0^+} e^{-i\omega t}.$$

$t<0$：上半平面逆时针闭合，围道内无极点，积分 $= 0$。两支合并即 $\theta(t)e^{-i\omega t}$。

**第二式**：极点 $p^0 = -\omega+i\epsilon$ 在上方。$t>0$：下半闭合，无极点，$0$。$t<0$：上半逆时针闭合（正定向），

$$\int = \frac{+2\pi i}{2\pi}\cdot i\,e^{-i(-\omega+i\epsilon)t} = (i)(i)\,e^{+i\omega t}\,e^{\epsilon t}\Big|_{t<0} = -\,e^{+i\omega t}.$$

合并即 $-\theta(-t)e^{+i\omega t}$。两条各念一遍："下方极点只对未来时间发声，上方极点只对过去时间发声且带负号"——把它们按正确的相对符号组合起来，时序拼接就自动完成。

</details>

**2.** 从 $D_F = \theta(t)D(x-y) + \theta(-t)D(y-x)$ 出发，用第 3.1 节的恒等式与部分分式，完整组装出 $D_F(x-y) = \int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip(x-y)}}{p^2-m^2+i\epsilon}$（含 $\vec p \to -\vec p$ 变量代换的细节与 $i\epsilon$ 在两个因式中的归属）。

<details markdown="1"><summary>点击显示答案</summary>

**因式分解与 $i\epsilon$ 归属**：要求 $p^0 = +\omega$ 处下方极点、$p^0 = -\omega$ 处上方极点（第 3.3 节的运行说明书），必须写

$$p^2 - m^2 + i\epsilon = (p^0 - \omega_{\vec p} + i\epsilon)(p^0 + \omega_{\vec p} - i\epsilon) + \mathcal O(\epsilon^2),$$

（验证：两式相乘 $= (p^0)^2 - \omega^2 + 2i\epsilon\omega + \epsilon^2$，$2\omega\epsilon$ 吸收进 $\epsilon$。）部分分式：

$$\frac{i}{p^2-m^2+i\epsilon} = \frac{i}{2\omega_{\vec p}}\left[\frac{1}{p^0-\omega_{\vec p}+i\epsilon} - \frac{1}{p^0+\omega_{\vec p}-i\epsilon}\right].$$

**先做 $p^0$ 积分**（$e^{-ip(x-y)} = e^{-ip^0t+i\vec p\cdot(\vec x - \vec y)}$，因子 $e^{i\vec p\cdot\vec r}$ 与 $p^0$ 无关）：

$$\int\frac{dp^0}{2\pi}\,\frac{i\,e^{-ip(x-y)}}{p^2-m^2+i\epsilon} = \frac{1}{2\omega_{\vec p}}e^{i\vec p\cdot\vec r}\Big[\theta(t)\,e^{-i\omega t} - \big(-\theta(-t)e^{+i\omega t}\big)\Big].$$

**第二项的整理**：$\theta(-t)\,e^{+i\omega t}\,e^{+i\vec p\cdot\vec r}$，做代换 $\vec p \to -\vec p$（$\omega_{\vec p}$ 偶函数、测度不变）得 $\theta(-t)\,e^{+i\omega t}\,e^{-i\vec p\cdot\vec r} = e^{+ip\cdot(x-y)}$（$p^0 = +\omega$ 的负频方向相位）。

**合并**：

$$\int\frac{d^4p}{(2\pi)^4}\frac{i\,e^{-ip(x-y)}}{p^2-m^2+i\epsilon} = \theta(t)\int\frac{d^3p}{(2\pi)^3\,2\omega_{\vec p}}e^{-ip(x-y)} + \theta(-t)\int\frac{d^3p}{(2\pi)^3\,2\omega_{\vec p}}e^{+ip(x-y)}$$

$$= \theta(t)\,D(x-y) + \theta(-t)\,D(y-x) = D_F(x-y).\qquad\blacksquare$$

第二行的等式用厄米性 $D(y-x) = \langle0\rvert\phi(y)\phi(x)\rvert0\rangle$（指数 $e^{+ip(x-y)}$ 正是它的模式展开）。

</details>

**3.** 推导推迟函数的动量空间形式 $D_R(p) = \dfrac{i}{(p^0+i\epsilon)^2 - \omega_{\vec p}^2}$：从 $D_R = \theta(t)\,\Delta = \theta(t)[D - D^c]$ 出发，或直接对动量形式做 $p^0$ 围道积分验证（i）$t<0$ 时严格为零；（ii）$t>0$ 时拾取两极点之差。并验证 $(\partial^2+m^2)D_R = -i\delta^4(x)$。

<details markdown="1"><summary>点击显示答案</summary>

**构造**：要求"两个极点都在下方"，即 $p^0 = \pm\omega_{\vec p} - i\epsilon$，这等价于把分母写成 $(p^0 + i\epsilon)^2 - \omega_{\vec p}^2$（两根 $-i\epsilon \pm \omega$，都在下方）。定义动量形式 $D_R(p) \equiv \dfrac{i}{(p^0+i\epsilon)^2-\omega_{\vec p}^2}$。

**围道验证**：部分分式 $\dfrac{i}{(p^0+i\epsilon)^2-\omega^2} = \dfrac{i}{2\omega}\Big[\dfrac{1}{p^0-\omega+i\epsilon} - \dfrac{1}{p^0+\omega+i\epsilon}\Big]$，两极点均在下方。

$t < 0$：只能上半平面闭合，围道内无极点——积分严格为零（"推迟"的本义：响应不早于扰动）。

$t > 0$：下半顺时针闭合，包住两极点：

$$\int\frac{dp^0}{2\pi}\,D_R(p)\,e^{-ip^0t} = \frac{-2\pi i}{2\pi}\cdot\frac{i}{2\omega}\Big[e^{-i\omega t} - e^{+i\omega t}\Big] = \frac{1}{2\omega}\Big[e^{-i\omega t} - e^{+i\omega t}\Big].$$

乘 $e^{i\vec p\cdot\vec r}$ 并对 $\frac{d^3p}{(2\pi)^3}$ 积分，正是 $\theta(t)\,[D(x-y) - D(y-x)] = \theta(t)\,\Delta(x-y)$ ✓。

**微分方程**：$(\partial^2+m^2)\,e^{-ipx} = (m^2 - p^2)\,e^{-ipx}$，故

$$(\partial^2+m^2)D_R(x) = \int\frac{d^4p}{(2\pi)^4}\,i\,\frac{m^2-p^2}{(p^0+i\epsilon)^2-\omega^2}\;e^{-ipx} = -i\int\frac{d^4p}{(2\pi)^4}\,e^{-ipx} = -i\,\delta^4(x),$$

（分子分母在 $\epsilon\to0$ 下相消；与第 01 篇 $D_F$ 的同一验证一致。）格林函数性质与推迟支持性合起来：$D_R$ 是初值问题的因果基本解——经典场论里"源产生的场"用的就是它。

</details>

**4.** 对无质量标量场，从对易子公式 $[\phi(x),\phi(y)] = \int\frac{d^3p}{(2\pi)^3\,2\lvert\vec p\rvert}\big(e^{-ip(x-y)} - e^{+ip(x-y)}\big)$ 出发，证明 $\Delta(x) = -\frac{i}{2\pi}\,\epsilon(x^0)\,\delta(x^2)$。确认支持严格落在光锥上，并解释结果为何是纯虚。

<details markdown="1"><summary>点击显示答案</summary>

取 $y = 0$，记 $r = \lvert\vec x\rvert$，$p \equiv \lvert\vec p\rvert = \omega$。对第一项做角度积分（$\int d\Omega\,e^{i\vec p\cdot\vec x} = 4\pi\frac{\sin(pr)}{pr}$）：

$$D(x) = \int\frac{d^3p}{(2\pi)^3\,2p}\,e^{-ipt+i\vec p\cdot\vec x} = \frac{1}{4\pi^2 r}\int_0^\infty dp\;\sin(pr)\,e^{-ipt}.$$

用分布恒等式 $\int_0^\infty e^{\pm iqp}\,dp = \pi\delta(q) \pm i\,\mathcal P\frac{1}{q}$ 把正弦积分拆开：

$$\int_0^\infty \sin(pr)e^{-ipt}\,dp = \frac{1}{2i}\Big[\pi\delta(r-t) + i\,\mathcal P\tfrac{1}{r-t} - \pi\delta(r+t) + i\,\mathcal P\tfrac{1}{r+t}\Big].$$

第二项 $D(-x)$ 同式取 $t \to -t$。相减时**主值部分逐项相消**（$\mathcal P\frac{1}{r\mp t}$ 在 $t\to-t$ 下互换），$\delta$ 部分翻倍：

$$\Delta(x) = \frac{1}{4\pi^2 r}\cdot\frac{1}{2i}\cdot 2\pi\big[\delta(r-t) - \delta(r+t)\big] = -\frac{i}{4\pi r}\big[\delta(t-r) - \delta(t+r)\big].$$

与紧凑形式对表：$\delta(x^2) = \delta(t^2-r^2) = \frac{1}{2r}\big[\delta(t-r)+\delta(t+r)\big]$，而 $\epsilon(t)$ 在各自支撑上取 $\pm1$（$t=r$ 处 $+1$、$t=-r$ 处 $-1$），故 $-\frac{i}{2\pi}\epsilon(t)\delta(x^2) = -\frac{i}{4\pi r}[\delta(t-r)-\delta(t+r)]$ ✓。

**支持**：两个 $\delta$ 只在光锥面 $t = \pm r$ 上发声，类空间隔 $t^2 < r^2$ 上 $\Delta = 0$ 严格成立——无质量信号只在光锥上跑。有质量时光锥内多出 $J_1$ 贝塞尔尾，光锥外依旧为零。

**纯虚性**：$\phi$ 厄米 $\Rightarrow$ $[\phi(x),\phi(0)]$ 反厄米 $\Rightarrow$ 其 $c$ 数值为纯虚。上式右边的 $-i$ 正是这一结构性的 $i$——它也解释了第 01 篇 $D_F$ 定义里那个看似任意的 $i$ 因子的来历。

</details>

**5.** 从单标量玻色子交换出发推导汤川势 $V(r) = -\frac{g^2}{4\pi}\frac{e^{-mr}}{r}$：静态源的树图振幅经 Born 近似对应势的傅里叶变换；讨论 $m \to 0$ 极限，并计算 $\pi$ 介子（$m \approx 135\,\mathrm{MeV}$）与 $W$ 玻色子（$m \approx 80\,\mathrm{GeV}$）给出的力程（$\hbar c \approx 197\,\mathrm{MeV\cdot fm}$）。

<details markdown="1"><summary>点击显示答案</summary>

**交换振幅的静态极限**：两个静态标量源（耦合 $g$）之间交换一个玻色子，传播子携带四动量转移 $q$：

$$i\mathcal M \approx (-ig)^2\,\frac{i}{q^2 - m^2}\Big|_{q^0 = 0} = (-ig)^2\,\frac{i}{-\vec q^{\,2} - m^2}\;\;\Longrightarrow\;\;\mathcal M \propto -\frac{g^2}{\vec q^{\,2} + m^2}.$$

静态源不放能量（$q^0 = 0$），分母里只剩空间动量——这是"势"适用的非相对论情形。

**Born 对应**：量子力学书第 08 篇的 Born 近似里，散射振幅 $f(\vec q) = -\frac{2m}{4\pi}\tilde V(\vec q)$ 由势的傅里叶变换给出。倒过来读：微扰论的树图振幅与 Born 振幅逐项对应，于是

$$\tilde V(\vec q) = -\frac{g^2}{\vec q^{\,2} + m^2}.$$

**傅里叶逆变换**（标准三维结果）：

$$V(r) = \int\frac{d^3q}{(2\pi)^3}\,e^{i\vec q\cdot\vec r}\,\tilde V(\vec q) = -g^2\cdot\frac{e^{-mr}}{4\pi r}.\qquad\blacksquare$$

**极限与数值**：$m\to0$ 给 $V = -\frac{g^2}{4\pi r}$——库仑 $1/r$（光子交换，$\alpha = \frac{e^2}{4\pi}$）；质量的出现把 $1/r$ 乘上 $e^{-mr}$，力程 $\rho_0 = 1/m = \lambda_C/2\pi$（约化康普顿波长）。

换算 $\rho_0 = \hbar c / (mc^2)$：

- $\pi$ 介子：$\rho_0 = 197/135\,\mathrm{fm} \approx 1.5\,\mathrm{fm}$——原子核半径的量级，核力 = 交换 $\pi$ 介子的汤川图像（汤川 1935 正是反过来由核力程预言了 $\pi$ 的质量）；
- $W$ 玻色子：$\rho_0 = 197/8\times10^4\,\mathrm{fm} \approx 2.5\times10^{-3}\,\mathrm{fm}$——比质子半径（$0.84\,\mathrm{fm}$）小三百多倍。弱作用之所以"弱"于低能弱过程，主要不是耦合常数小（$g_w \sim e$ 量级），而是媒介粒子重——短程把力稀释了。这一账要到电弱统一（第 6 阶段第 2 篇）才能彻底算清：$W/Z$ 的质量本身来自希格斯机制。

</details>

## 参考

- Peskin & Schroeder《An Introduction to Quantum Field Theory》§2.4（微观因果性与 Feynman 传播子——第 01 篇 §8 与本篇的直接母本）。
- Srednicki《Quantum Field Theory》第 3、6 章（对易子函数、$Z[J]$ 中的传播子；记号与本篇一致）。
- Schwartz《Quantum Field Theory and the Standard Model》第 6 章附近（费曼传播子；从光子交换推出库仑势的标准练习——本篇第 6 节与自检第 5 题的母本）。
- Zee《Quantum Field Theory in a Nutshell》第 I 部分从交换推导库仑/牛顿势的章节（力程物理图像最生动的版本）。
- D. Tong 量子场论讲义（Cambridge，在线公开）第 2 章（传播子的编时定义与 $i\epsilon$ 的教学推导，节奏与本篇接近）。
