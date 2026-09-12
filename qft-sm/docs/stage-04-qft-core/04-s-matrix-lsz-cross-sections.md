# S 矩阵、LSZ 约化与截面：从关联函数到可测量的最后一步

> 路线图位置：第 4 阶段（QFT 核心）· 第 4 篇（主线的收口：[第 03 篇](03-interactions-and-feynman-rules.md)算出费曼图，本篇把图变成实验室里的数）。
> 前置知识：[相互作用与微扰论](03-interactions-and-feynman-rules.md)（Dyson 级数、连接图、$i\mathcal M$ 的树图示例）；[传播子与因果性](02-propagators-and-causality.md)（极点 = 粒子——LSZ 截肢的根据）；[标量场量子化](01-scalar-field-quantization.md)（单粒子态的洛伦兹协变归一化）；[量子力学书·微扰理论](../../../quantum-mechanics/docs/07-perturbation-theory.md)（费米黄金定则——截面/衰变率公式是它的相对论版）与[散射的形式理论](../../../quantum-mechanics/docs/08s-scattering-formalism.md)（$T$ 矩阵与光学定理——本篇给出它们的场论对应物）。
> 学习目标：会从平移不变性论证 $S = \mathbb 1 + iT$ 并定义不变振幅 $\mathcal M$；会用"单粒子极点 + 截肢"的 LSZ 约化把关联函数变成振幅（含 $Z$ 因子的来历与树图 $Z=1$）；会完成 $\lvert S_{fi}\rvert^2$ 到截面的全部记账（$\delta^4(0) = VT$、态归一化、流强因子）；能推出 $2\to2$ 质心系公式与 $1\to2$ 衰变率并实算 $\phi^4$ 角分布；会从 $S^\dagger S = \mathbb 1$ 推光学定理并与量子力学书的版本逐项对表。

全文用自然单位 $\hbar = c = 1$，度规 $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$。单粒子态用第 01 篇的洛伦兹协变归一化 $\langle p'\rvert p\rangle = (2\pi)^3\,2E_{\vec p}\,\delta^3(\vec p - \vec p')$。

---

## 1. 一句话总结

**微扰论产出的是关联函数（第 03 篇），实验测量的是截面与衰变率，中间隔着三步标准工序：LSZ 约化在外线动量趋于质壳时把关联函数"截肢"，留下不变振幅 $\mathcal M$——它的合法性来自传播子的单粒子极点（第 02 篇"极点 = 粒子"）；把 $\lvert\langle f\rvert S\rvert i\rangle\rvert^2$ 除以时间与入射流强，配上洛伦兹不变的相空间体积元，得到截面与衰变率公式——结构与量子力学的费米黄金定则完全同构，只是态归一化与"态密度"换成了相对论版本；最后 $S^\dagger S = \mathbb 1$ 把概率守恒写成光学定理，振幅的虚部被锁定为总截面——三步打通后，"拉氏量 → 费曼图 → 实验数"的全链条正式合龙。**

## 2. S 矩阵与不变振幅

### 2.1 收掉上一篇的账单

第 03 篇 §3.4 留下一句承诺：绝热开关（相互作用在 $t\to\pm\infty$ 缓慢关闭）的严格化是散射形式理论的职责。本篇的立场：微扰论里每一阶都能验证它自洽，我们按标准物理教材的方式使用 $S = U_I(+\infty,-\infty)$，把公理化场论层面的细节（Haag 定理、渐近态的严格构造）留在门外——这不是遮掩，而是划界：本篇给出的公式在微扰意义下逐阶良定义。

### 2.2 平移不变性固定了 $S$ 的形状

$S$ 与全部守恒量对易。特别地它与四维平移算符对易，而平移算符在单粒子态上只把相位挪动（$e^{i(P_f - P_i)\cdot a}$ 对任意 $a$）——$S_{fi}$ 要对所有 $a$ 不变，只有两种可能：$P_f = P_i$（对角部分），或矩阵元为零。于是：

$$S = \mathbb 1 + iT, \qquad\qquad \langle f\rvert iT\rvert i\rangle = i\,(2\pi)^4\,\delta^4(P_f - P_i)\,\mathcal M(f \leftarrow i).$$

$\mathbb 1$ 是"没人散射"的部分（第 03 篇 §5.3 的非连接图归它管）；$\delta^4$ 是四动量守恒的声明；**剥掉 $\delta^4$ 之后剩下的 $\mathcal M$ 就是不变振幅**——一个洛伦兹不变的数（标量理论），微扰论的全部产品。第 03 篇 §6.2 已经"朴素地"这样用过；§3 把朴素升级成定理。

### 2.3 幂正性（留给 06 篇的伏笔）

$S$ 是概率守恒的幺正演化，$S^\dagger S = \mathbb 1$。第 06 篇会看到这条约束在圈图水平强制"虚部 = 吸收"；本篇 §6 先兑现它的最低阶推论——光学定理。

## 3. LSZ 约化：把关联函数截肢成振幅

### 3.1 关联函数在极点附近长什么样

自由理论的两点函数 $\tilde G_0(p) = \dfrac{i}{p^2-m^2+i\epsilon}$ 在 $p^2 = m^2$ 有单极点、留数 $i$（第 02 篇）。相互作用理论的两点函数（Källén–Lehmann 谱表示的结论，本篇直接引用）仍是

$$\tilde G(p) \;\xrightarrow{\;p^2\to m^2\;}\; \frac{i\,Z}{p^2 - m^2 + i\epsilon} + (\text{多粒子连续谱，无极点})，$$

其中**场造出单粒子的能力** $\;\langle\Omega\rvert\varphi(0)\rvert p\rangle = \sqrt{Z}$ 定义了 $Z$（自由场 $Z=1$；$Z$ 的重整化命运是第 06 篇的事）。四点函数在四条外线同时趋近质壳时因子化：

$$\tilde G^{(4)} \;\xrightarrow{\;p_i^2\to m^2\;}\; (2\pi)^4\delta^4(\textstyle\sum p)\;\Big[\prod_{i=1}^4 \frac{i\sqrt{Z}}{p_i^2 - m^2 + i\epsilon}\Big]\; i\mathcal M.$$

**外线传播子 × 振幅**——第 03 篇 §6.2 树图计算里看到的结构（那里 $Z=1$）原来是普遍定理。

### 3.2 抽取引理：把 $a_p^\dagger$ 从场里拉出来

LSZ 的技术核心是一条初等引理。在第 01 篇的归一化下，定义 $a_p^\dagger(t) = -i\int d^3x\; e^{-ipx}\,\overset{\leftrightarrow}{\partial_0}\,\varphi(t,\vec x)$（$p^0 = \omega_{\vec p}$ 在壳；对自由场这就是常义的 $a_p^\dagger$）。对时间积分，$\leftrightarrow$ 导数在乘积求导时交叉项相消，空间部分用 $\nabla^2 e^{-ipx} = -\vec p^{\,2} e^{-ipx}$ 归并：

$$a_p^\dagger(+\infty) - a_p^\dagger(-\infty) = -i\int d^4x\; e^{-ipx}\,\big(\partial^2 + m^2\big)\varphi(x).$$

自由场 $(\partial^2+m^2)\varphi = 0$，右边为零——产生算符不随时间变，符合自由理论。**有相互作用时 $(\partial^2+m^2)\varphi = J$ 是"源"**（$\phi^4$ 理论里 $J = -\frac{\lambda}{3!}\varphi^3$，即运动方程把相互作用项挪到左边）：产生算符在穿越相互作用区域的途中被源修正。把这条引理逐条用于外线粒子，把 $a_p^\dagger(\mp\infty)$ 认作入射/出射态（$a_p^\dagger(-\infty)\rvert\Omega\rangle = \lvert p,\,\mathrm{in}\rangle$ 等——这正是绝热开关的算符语言），$T$ 乘积自动把 $\pm\infty$ 极限接好，就得到：

### 3.3 LSZ 公式

$$\boxed{\;i\,\mathcal M(f\leftarrow i) \;=\; \lim_{\{p_j^2\to m^2\}}\ \prod_{\text{外线 } j}\Big[\,i\sqrt{Z_j^{-1}}\,\big(p_j^2 - m^2\big)\Big]\;\tilde G^{(n)}(\{p_j\})\;}$$

（$\tilde G^{(n)}$ 已剥掉总 $\delta^4$；每条外线乘一个 $(p_j^2 - m^2)$ 把极点约掉、除一个 $\sqrt{Z_j}$ 把"场的造粒能力"归一。）**"截肢"的朴素操作从此有了定理地位**：外线传播子不是物理，物理是它的极点留数。

验算（树图、$Z=1$）：第 03 篇的 $\phi^4$ 树图关联函数代入，每条腿 $i(p^2-m^2)\times\frac{i}{p^2-m^2} = i\cdot i \to$ 约净，剩 $-i\lambda$：

$$i\mathcal M = -i\lambda\qquad\Longrightarrow\qquad \mathcal M = -\lambda,$$

与第 03 篇 §6.2 逐字一致（完整逐行代换是自检第 2 题）。

### 3.4 LSZ 顺手回答的两个问题

- **为什么第 03 篇只数连接图**：非连接图的 $\delta^4$ 结构是两个独立过程的 $\delta^4$ 之积，与 $(2\pi)^4\delta^4(P_f - P_i)$ 的形状对不上——属于 $\mathbb 1$ 的部分或不对应任何单一路径的散射。LSZ 的留数只从单粒子极点的连通因子化里产生。
- **为什么外线在壳而内线离壳**：截肢极限 $p_j^2 \to m^2$ 把外线钉在质壳上（渐近态是真实粒子）；内线是积分变量，从不取极限（第 02 篇的"虚粒子纪律"）。

## 4. 从 $\mathcal M$ 到截面与衰变率：相空间记账

### 4.1 跃迁概率、$\delta^4(0)$ 与流强

对固定的末态 $\lvert f\rangle$，微扰论给出 $\langle f\rvert S\rvert i\rangle = i(2\pi)^4\delta^4(P_f - P_i)\mathcal M$。取模方时 $\delta$ 函数平方，用盒子量子化的读法 $\,(2\pi)^4\delta^4(0) = VT\,$（时间 × 体积）：

$$\lvert\langle f\rvert S\rvert i\rangle\rvert^2 = (2\pi)^4\delta^4(P_f - P_i)\;VT\;\lvert\mathcal M\rvert^2.$$

除以初态归一化 $\langle i\rvert i\rangle = 4E_1E_2\,V^2$（两个单粒子态各贡献 $(2\pi)^3 2E\,\delta^3(0) = 2EV$）得到单位时间的跃迁概率；再除以入射流强 $v_{\rm rel}/V$（一个粒子穿过单位体积、以相对速度掠过靶）。三步合并，$V$ 与 $T$ 全部消干净：

$$\boxed\;{\;d\sigma \;=\; \frac{1}{4E_1E_2\,v_{\rm rel}}\;\lvert\mathcal M\rvert^2\;(2\pi)^4\delta^4\Big(p_1 + p_2 - \textstyle\sum_j p_j\Big)\;\prod_j \frac{d^3p_j}{(2\pi)^3\,2E_j}\;}$$

分母 $4E_1E_2v_{\rm rel} = 4\sqrt{(p_1\!\cdot\!p_2)^2 - m_1^2m_2^2}$ 是**洛伦兹不变流强**（用 Källén 函数 $\lambda(x,y,z) = x^2+y^2+z^2-2xy-2xz-2yz$ 写就是 $2\lambda^{1/2}(s, m_1^2, m_2^2)$）。相空间测度

$$d\Phi_n \;\equiv\; (2\pi)^4\delta^4\Big(P_{\rm ini} - \textstyle\sum_j p_j\Big)\prod_{j=1}^n \frac{d^3p_j}{(2\pi)^3\,2E_j}$$

也是不变的——整个公式的协变性一目了然。衰变只需换掉分母：没有流强，初态只有一个质量 $M$ 的粒子（归一化给出 $2M$）：

$$\boxed{\;d\Gamma \;=\; \frac{1}{2M}\,\lvert\mathcal M\rvert^2\;d\Phi_n\;}\qquad\quad \mathrm{BR}_i = \Gamma_i/\Gamma_{\rm tot}\ (\text{分支比}).$$

### 4.2 与费米黄金定则的对表

量子力学书第 07 篇的黄金定则 $w = 2\pi\lvert V_{fi}\rvert^2\rho(E_f)$：跃迁率 = 耦合平方 × 末态密度。本篇公式完全同构——$\lvert\mathcal M\rvert^2$ 是耦合平方，$d\Phi_n$ 是相对论化的态密度（$\frac{d^3p}{2E}$ 正是协变测度，第 01 篇 §4 补充说明），$\frac{1}{2M}$、$\frac{1}{4E_1E_2v_{\rm rel}}$ 是相对论态归一化的零头。**黄金定则没有被推翻，只是换了一身洛伦兹协变的衣服。**

### 4.3 $2\to2$ 质心系与 $1\to2$ 衰变

相空间积分的标准结果（推导见自检第 3 题）：$2\to2$ 在质心系（$s = E_{\rm cm}^2$，$p_i, p_f$ 为初、末态质心动量大小）

$$\boxed\;{\;\frac{d\sigma}{d\Omega} = \frac{1}{64\pi^2\,s}\;\frac{p_f}{p_i}\;\lvert\mathcal M(s,t,u)\rvert^2\;}\qquad\qquad d\Phi_2 = \frac{p_f}{16\pi^2\sqrt{s}}\,d\Omega.$$

弹性等质量情形 $p_f = p_i$。$1\to2$ 衰变（$p^\ast$ 为末态质心动量，$\lambda^{1/2}(M^2,m_1^2,m_2^2) = 2M p^\ast$）：

$$\Gamma_{1\to2} = \frac{p^\ast}{8\pi M^2}\,\lvert\mathcal M\rvert^2\qquad(\text{角度积分后，}\ \mathcal M\text{ 不依赖角度；末态全同时再除统计因子}\ \textstyle\prod_a 1/n_a!).$$

## 5. 第一次实战：标量理论的角分布

全链条合龙——拉氏量 → 费曼规则 → $\mathcal M$ → 截面——在标量理论上先跑一遍热身（QED 大戏在第 05 篇）。

**$\phi^4$**：$\mathcal M = -\lambda$（接触相互作用，与角度无关），等质量弹性 $p_f = p_i$：

$$\frac{d\sigma}{d\Omega} = \frac{\lambda^2}{64\pi^2 s}\;\;\Longrightarrow\;\;\sigma_{\rm tot} = \frac{\lambda^2}{16\pi\,s}\quad(\text{无质量极限}).$$

角分布平坦——第 03 篇"接触相互作用 → 平坦角分布"的定量兑现。量纲自检：$\lambda$ 无量纲、$[\sigma] = [s^{-1}] = \mathrm{长度}^2$ ✓。

**$\phi^3$（无质量极限）**：$\mathcal M = g^2\big(\tfrac1s + \tfrac1t + \tfrac1u\big)$（第 03 篇 §8；符号对截面无关）。质心系 $t = -\tfrac{s}{2}(1-\cos\theta)$，$u = -\tfrac{s}{2}(1+\cos\theta)$，$s+t+u = 0$：

$$\frac{1}{s}+\frac{1}{t}+\frac{1}{u} = \frac{1}{s}\Big[1 - \frac{4}{\sin^2\theta}\Big]\qquad\Longrightarrow\qquad \frac{d\sigma}{d\Omega} = \frac{g^4}{64\pi^2\,s^3}\Big[1 - \frac{4}{\sin^2\theta}\Big]^2.$$

角分布强烈各向异性，且在 $\theta\to0,\pi$ 处发散——$t\to0$、$u\to0$ 时的传播子极点（"共线发散"）。这不是灾难而是诊断：真实理论里质量（$t$ 沟分母 $t - m^2$）或更高阶修正会把极点移开。要记住的物理是：**有内线的理论角分布由传播子形状决定，前向增强是长程相互作用的普遍签名**——第 02 篇力程讨论的截面版。

## 6. 光学定理：概率守恒的振幅表述

$S^\dagger S = \mathbb 1$ 塞进 $\langle i\rvert\cdots\rvert i\rangle$ 之间并对中间态插入完备基，与 §4.1 同一套 $\delta^4(0) = VT$ 记账（完整推导自检第 5 题）给出：

$$\boxed\;{\;\mathrm{Im}\,\mathcal M\big(s,\,t=0\big) \;=\; 2\,p_{\rm cm}\,\sqrt{s}\;\sigma_{\rm tot}\;}$$

——**前向振幅的虚部被总截面锁定**。三点立刻接上：

- 与量子力学书对表：那里有 $\sigma_{\rm tot} = \frac{4\pi}{k}\,\mathrm{Im}\,f(0)$（[08s 篇](../../../quantum-mechanics/docs/08s-scattering-formalism.md)由幺正性 $T - T^\dagger = -2\pi i T^\dagger\delta T$ 推出）。两者的关系由 $f(\theta) = \mathcal M/8\pi\sqrt{s}$（把 $d\sigma/d\Omega = \lvert f\rvert^2$ 与 §4.3 对齐即得）缝合：代入本篇公式，$\mathrm{Im}\,f(0) = \frac{2p\sqrt{s}}{8\pi\sqrt{s}}\sigma = \frac{p}{4\pi}\sigma$，移项正是量子力学版 ✓——同一件事的非相对论与协变写法（自检第 5 题完成逐项核对）。
- 振幅虚部的微扰论来源：树图振幅是实的（顶点、传播子皆实），虚部从**一圈**开始——切开的圈图（把一条内线放上质壳）恰好给出 $\int d\Phi\,\lvert\mathcal M\rvert^2$ 的形状。第 06 篇计算一圈修正时，光学定理成为最强的一致性检查。
- 它是"丢了多少概率"的守恒账：弹性前向散射的 imaginary 部分补偿一切非弹性通道的流失。

## 7. 小结

| 工序 | 公式 | 来源 |
| --- | --- | --- |
| 分解 | $S = \mathbb 1 + iT$，$\langle f\rvert iT\rvert i\rangle = i(2\pi)^4\delta^4\,\mathcal M$ | 平移不变性 + 幺正性 |
| 截肢 | $i\mathcal M = \lim\prod_j\big[i(p_j^2 - m^2)/\sqrt{Z_j}\big]\tilde G^{(n)}$ | 单粒子极点 + 抽取引理（LSZ） |
| 截面 | $d\sigma = \dfrac{\lvert\mathcal M\rvert^2\,d\Phi_n}{4E_1E_2 v_{\rm rel}}$ | $\delta^4(0) = VT$ 记账 + 流强 |
| 衰变 | $d\Gamma = \dfrac{\lvert\mathcal M\rvert^2\,d\Phi_n}{2M}$ | 同上，无流强 |
| $2\to2$ CM | $d\sigma/d\Omega = \dfrac{p_f}{64\pi^2 s\,p_i}\lvert\mathcal M\rvert^2$ | $d\Phi_2$ 积分 |
| $1\to2$ | $\Gamma = \dfrac{p^\ast}{8\pi M^2}\lvert\mathcal M\rvert^2$ | 同上 |
| 幺正性 | $\mathrm{Im}\,\mathcal M(s,0) = 2p_{\rm cm}\sqrt{s}\,\sigma_{\rm tot}$ | $S^\dagger S = \mathbb 1$（光学定理） |

主线的拼图至此完整：**量子化（01）→ 传播子（02）→ 微扰论与费曼图（03）→ 振幅与截面（本篇）**。第 05 篇立刻用 QED 把全链条跑在真实物理上（$e^+e^-\to\mu^+\mu^-$、康普顿），第 06 篇在一圈水平上检验幺正性（光学定理）并处理发散。

## 自检问题

**1.** 证明抽取引理 $a_p^\dagger(+\infty) - a_p^\dagger(-\infty) = -i\int d^4x\,e^{-ipx}(\partial^2+m^2)\varphi(x)$：从 $a_p^\dagger(t) = -i\int d^3x\,e^{-ipx}\overset{\leftrightarrow}{\partial_0}\varphi$ 出发完成全部求导与空间归并，并验证自由场情形右边为零。

<details markdown="1"><summary>点击显示答案</summary>

对时间积分：$a_p^\dagger(+\infty) - a_p^\dagger(-\infty) = -i\int dt\int d^3x\;\partial_0\big[e^{-ipx}\overset{\leftrightarrow}{\partial_0}\varphi\big]$。

**核心一步**（$\leftrightarrow$ 导数的乘积求导）：记 $X \equiv e^{-ipx}$（$p^0 = \omega_{\vec p}$ 在壳），

$$\partial_0\big[X\,\overset{\leftrightarrow}{\partial_0}\,\varphi\big] = \partial_0\big[X\,\partial_0\varphi - (\partial_0 X)\,\varphi\big] = X\,\partial_0^2\varphi - (\partial_0^2 X)\,\varphi,$$

交叉项 $X'\varphi' + X'\varphi'$? 逐项验证：$\partial_0[X\partial_0\varphi] = (\partial_0X)(\partial_0\varphi) + X\partial_0^2\varphi$；$\partial_0[(\partial_0X)\varphi] = (\partial_0^2X)\varphi + (\partial_0X)(\partial_0\varphi)$。相减，交叉项消去，得上式，且 $\partial_0^2 X = -\omega_{\vec p}^2 X$：

$$a_p^\dagger(+\infty) - a_p^\dagger(-\infty) = -i\int d^4x\;X\,\big(\partial_0^2 + \omega_{\vec p}^2\big)\varphi .$$

**空间归并**：$X = e^{-i\omega t}e^{+i\vec p\cdot\vec x}$ 满足 $\nabla^2 X = -\vec p^{\,2}X$，故 $X\,\vec p^{\,2}\varphi = -X\nabla^2\varphi + \big(\nabla^2X + \vec p^{\,2}X\big)\varphi = -X\nabla^2\varphi$。而 $\omega_{\vec p}^2 = \vec p^{\,2} + m^2$：

$$X\big(\partial_0^2 + \omega^2\big)\varphi = X\big(\partial_0^2 + \vec p^{\,2} + m^2\big)\varphi = X\big(\partial_0^2 - \nabla^2 + m^2\big)\varphi = X\,\big(\partial^2 + m^2\big)\varphi.\qquad\blacksquare$$

**自由场**：$(\partial^2+m^2)\varphi = 0$（KG 方程），右边为零，$a_p^\dagger$ 与时间无关——回到第 01 篇的守恒产生算符。**相互作用场**：把运动方程 $(\partial^2+m^2)\varphi = \mathcal{J}_{\rm int}$（对 $\phi^4$：$\mathcal{J}_{\rm int} = -\frac{\lambda}{3!}\varphi^3$）代入，产生算符在时间演化中被源"充放电"——这正是 LSZ 把相互作用信息从关联函数里抽出来的抓手。

</details>

**2.** 用 LSZ 公式对第 03 篇的两条树图关联函数截肢：（i）$\phi^4$ 接触图，恢复 $\mathcal M = -\lambda$；（ii）$\phi^3$ 的 $s$ 道图，恢复 $\mathcal M_s = -g^2/(s-m^2)$。明确每条外线的 $(p_j^2 - m^2)$ 如何约掉对应传播子。

<details markdown="1"><summary>点击显示答案</summary>

**（i）** 第 03 篇 §5.2 的连接树图关联函数（动量空间，剥掉总 $\delta^4$）：

$$\tilde G^{(4)}_{\text{树}} = (-i\lambda)\prod_{j=1}^4\frac{i}{p_j^2 - m^2 + i\epsilon}.$$

LSZ 代入（$Z=1$）：每条外线贡献 $i(p_j^2 - m^2)$，与传播子 $\frac{i}{p_j^2 - m^2}$ 相乘：$i(p_j^2-m^2)\cdot\frac{i}{p_j^2-m^2+i\epsilon} \to i\cdot i = -1$（在壳极限 $\epsilon\to0$）。四条腿共 $(−1)^4 = +1$：

$$i\mathcal M = (-i\lambda)\times(+1) = -i\lambda\;\;\Longrightarrow\;\;\mathcal M = -\lambda.\qquad\checkmark$$

**（ii）** $\phi^3$ 的 $s$ 道（两顶点、一条内线 $q = p_1 + p_2$）：树图关联函数

$$\tilde G^{(4)}_{s} = (-ig)^2\,\frac{i}{q^2 - m^2 + i\epsilon}\Big|_{q = p_1+p_2}\;\prod_{j=1}^4\frac{i}{p_j^2 - m^2 + i\epsilon}.$$

四条外线同样约净，内线不动（LSZ 只取外线极限）：

$$i\mathcal M_s = (-ig)^2\,\frac{i}{s - m^2 + i\epsilon} = \frac{-g^2\,i}{s-m^2}\;\;\Longrightarrow\;\;\mathcal M_s = \frac{-g^2}{s-m^2}.\qquad\checkmark$$

与第 03 篇 §8 直接按规则抄出的结果逐字一致。两个验算合起来说明：**费曼规则的"外线因子取 1"约定 = LSZ 截肢 + $Z=1$**，树图水平完全等价；$Z \neq 1$ 的修正到第 06 篇（波函数重整化）才进场。

</details>

**3.** 推导 $d\Phi_2 = \frac{p_f}{16\pi^2\sqrt{s}}d\Omega$（质心系），并由此完成 $d\sigma/d\Omega = \frac{p_f}{64\pi^2s\,p_i}\lvert\mathcal M\rvert^2$。

<details markdown="1"><summary>点击显示答案</summary>

质心系：$\vec p_1 = -\vec p_2 = \vec p_i\,\hat z$，末态 $\vec k_1 = -\vec k_2 \equiv \vec k$，$p_f = \lvert\vec k\rvert$，$E_1 + E_2 = \sqrt{s} = E_{k_1} + E_{k_2}$。

$$d\Phi_2 = (2\pi)^4\delta^4(P - k_1 - k_2)\,\frac{d^3k_1}{(2\pi)^3 2E_{k_1}}\cdot\frac{d^3k_2}{(2\pi)^3 2E_{k_2}}.$$

**先积 $k_2$**：$\delta^3$ 直接锁定 $\vec k_2 = -\vec k_1$：

$$d\Phi_2 = \frac{(2\pi)^4}{(2\pi)^6}\cdot\frac{d^3k}{4E_{k_1}E_{k_2}}\;\delta\big(\sqrt{s} - E_1' - E_2'\big).$$

**球坐标** $d^3k = p_f^2\,dp_f\,d\Omega$，能量依赖只在 $E_{1,2}'(p_f)$：

$$d\Phi_2 = \frac{d\Omega}{16\pi^2}\int_0^\infty \frac{p_f^2\,dp_f}{E_1'E_2'}\;\delta\big(g(p_f)\big),\qquad g(p) \equiv \sqrt{s} - E_1'(p) - E_2'(p).$$

**$\delta$ 函数定根**：$g(p_f) = 0$ 即能量守恒，解出 $E_1' + E_2' = \sqrt s$ 的动量 $p_f = \lambda^{1/2}(s, m_1^2, m_2^2)/2\sqrt{s}$。雅可比 $g'(p) = -p/E_1' - p/E_2' = -p\,\frac{E_1'+E_2'}{E_1'E_2'} = -\frac{p\sqrt{s}}{E_1'E_2'}$，故 $\frac{p_f^2}{E_1'E_2'}\cdot\frac{1}{\lvert g'\rvert} = \frac{p_f^2}{E_1'E_2'}\cdot\frac{E_1'E_2'}{p_f\sqrt{s}} = \frac{p_f}{\sqrt{s}}$：

$$d\Phi_2 = \frac{p_f}{16\pi^2\sqrt{s}}\;d\Omega.\qquad\blacksquare$$

**拼装截面**：$d\sigma = \frac{\lvert\mathcal M\rvert^2}{4E_1E_2v_{\rm rel}}d\Phi_2$；质心系 $E_1E_2v_{\rm rel} = p_i(E_1+E_2) = p_i\sqrt{s}$（$v_{\rm rel} = p_i\frac{1}{E_1} + p_i\frac{1}{E_2}$），于是

$$d\sigma = \frac{\lvert\mathcal M\rvert^2}{4p_i\sqrt{s}}\cdot\frac{p_f}{16\pi^2\sqrt{s}}d\Omega\;\;\Longrightarrow\;\;\frac{d\sigma}{d\Omega} = \frac{p_f}{64\pi^2 s\,p_i}\,\lvert\mathcal M\rvert^2.\qquad\checkmark$$

弹性等质量时 $p_f = p_i$，因子化为 $\frac{\lvert\mathcal M\rvert^2}{64\pi^2 s}$。

</details>

**4.** 推导 $1\to2$ 衰变率公式 $\Gamma = \frac{p^\ast}{8\pi M^2}\lvert\mathcal M\rvert^2$（末态可分辨、$\mathcal M$ 不依赖角度），并实算无质量 $\phi^3$ 理论中粒子的自衰变宽度 $\Gamma(\varphi\to\varphi\varphi)$。

<details markdown="1"><summary>点击显示答案</summary>

**一般公式**：$d\Gamma = \frac{\lvert\mathcal M\rvert^2}{2M}d\Phi_2$，粒子静止系即质心系（$\sqrt{s} = M$），自检第 3 题的 $d\Phi_2 = \frac{p^\ast}{16\pi^2 M}d\Omega$ 直接搬来。对全立体角积分：

$$\Gamma = \frac{\lvert\mathcal M\rvert^2}{2M}\cdot\frac{p^\ast}{16\pi^2 M}\cdot 4\pi = \frac{p^\ast}{8\pi M^2}\,\lvert\mathcal M\rvert^2,\qquad p^\ast = \frac{\lambda^{1/2}(M^2, m_1^2, m_2^2)}{2M}.$$

无质量末态 $p^\ast = M/2$，若 $\lvert\mathcal M\rvert = g$ 且末态可分辨，则 $\Gamma = g^2/16\pi M$。

**$\varphi\to\varphi\varphi$（全同末态）**分两步，各有一个陷阱：

（i）**振幅没有额外因子**：单顶点图的关联函数系数由 Wick 计数给出——三条外线接三条顶点腿共 $3! = 6$ 种缩并，顶点自带 $1/3!$，恰好约净，$\mathcal M = -g$。对比第 03 篇 §7：顶点阶乘因子存在的意义就是消化腿的排列——**不要**再给振幅乘任何对称化因子。

（ii）**相空间要除 $2!$**：$d\Phi_2$ 让 $\vec k_1, \vec k_2$ 独立跑遍全部动量空间，但全同玻色子的物理末态不分 $(\vec k_1, \vec k_2)$ 与 $(\vec k_2, \vec k_1)$——同一末态被数了两遍，除以 $2!$：

$$\Gamma(\varphi\to\varphi\varphi) = \frac{1}{2!}\cdot\frac{M/2}{8\pi M^2}\,g^2 = \frac{g^2}{32\pi M}.$$

要点：**全同末态的重复计数只在相空间里除一次（$\div\prod_a n_a!$），振幅端顶点的 $1/3!$ 已经管过腿的排列**——两边各自记账、互不重叠，这正是第 03 篇对称因子"长得一样的东西只数一遍"原则的末态版。与可分辨情形的 $g^2/16\pi M$ 相比恰好减半：纯粹的玻色统计效应，实验上可直接测量。

</details>

**5.** 从 $S^\dagger S = \mathbb 1$ 推导光学定理 $\mathrm{Im}\,\mathcal M(s, t=0) = 2p_{\rm cm}\sqrt{s}\,\sigma_{\rm tot}$；再用 $f(\theta) = \mathcal M/8\pi\sqrt{s}$ 把它翻译成量子力学书 08s 篇的形式 $\sigma_{\rm tot} = \frac{4\pi}{k}\mathrm{Im}\,f(0)$，逐项核对。

<details markdown="1"><summary>点击显示答案</summary>

**第一步（幺正性的对角元）**：$\langle i\rvert S^\dagger S\rvert i\rangle = 1$，插入完备基 $\sum_f\int d\Phi_f\,\lvert f\rangle\langle f\rvert$：

$$\sum_f \lvert\langle f\rvert S\rvert i\rangle\rvert^2 = 1,\qquad \langle f\rvert S\rvert i\rangle = \delta_{fi} + i(2\pi)^4\delta^4(P_f - P_i)\,\mathcal M_{fi}.$$

取 $f \neq i$ 的通道逐项平方（$\delta^4$ 平方用 $(2\pi)^4\delta^4(0) = VT$，与正文 §4.1 同一记账），保留到 $\mathcal M$ 的一阶与 $\lvert\mathcal M\rvert^2$ 阶（$VT^2$ 型的 $\delta^4(0)^2\lvert\mathcal M_{ii}\rvert^2$ 项是恒等元部分的重复计数，微扰展开始终取 $VT$ 的线性阶即可）：

$$-2\,VT\,\mathrm{Im}\,\mathcal M_{ii} + VT\sum_{f\neq i}\int d\Phi_f\;\lvert\mathcal M_{fi}\rvert^2 = 0\qquad\Longrightarrow\qquad 2\,\mathrm{Im}\,\mathcal M_{ii} = \sum_f\int d\Phi_f\;\lvert\mathcal M_{fi}\rvert^2.$$

（$\delta_{fi}$ 项贡献 1 与右边抵消；$\mathrm{Re}$ 部分两阶相消——概率守恒的线性部分自动成立。）

**第二步（右边认出总截面）**：正文 §4.1 已算出 $\sigma_{\rm tot} = \sum_f\int d\Phi_f\,\lvert\mathcal M_{fi}\rvert^2/(4E_1E_2 v_{\rm rel})$。质心系 $4E_1E_2v_{\rm rel} = 4p_{\rm cm}\sqrt{s}$：

$$2\,\mathrm{Im}\,\mathcal M(s, 0) = 4p_{\rm cm}\sqrt{s}\;\sigma_{\rm tot}\;\;\Longrightarrow\;\;\mathrm{Im}\,\mathcal M(s,0) = 2p_{\rm cm}\sqrt{s}\,\sigma_{\rm tot}.\qquad\blacksquare$$

**第三步（翻译）**：量子力学的散射振幅由 $d\sigma/d\Omega = \lvert f(\theta)\rvert^2$ 定义（08 篇），与 §4.3 的 $d\sigma/d\Omega = \lvert\mathcal M\rvert^2/64\pi^2 s$（弹性）对齐：

$$f(\theta) = \frac{\mathcal M(s,t)}{8\pi\sqrt{s}}\qquad\Longrightarrow\qquad \mathrm{Im}\,f(0) = \frac{2p_{\rm cm}\sqrt{s}\,\sigma_{\rm tot}}{8\pi\sqrt{s}} = \frac{p_{\rm cm}}{4\pi}\,\sigma_{\rm tot},$$

移项即 $\sigma_{\rm tot} = \frac{4\pi}{k}\,\mathrm{Im}\,f(0)$（$k = p_{\rm cm}$）——与 08s 篇由 $T - T^\dagger = -2\pi i\,T^\dagger\delta(E - H_0)T$ 推出的形式逐字相同 ✓。两套推导的对应：量子力学的能量守恒 $\delta(E_f - E_i)$ ↔ 场论的四动量 $\delta^4$；态密度 $\rho(E_f)$ ↔ 洛伦兹不变相空间 $d\Phi$；$T$ 矩阵 ↔ $\mathcal M$。**幺正性在两代散射理论里写的是同一本账。**

</details>

## 参考

- Srednicki《Quantum Field Theory》第 5 章（LSZ 约化的完整推导，归一化与本篇一致，最适合逐行对照）及相空间与截面各章。
- Peskin & Schroeder《An Introduction to Quantum Field Theory》§4.5–4.7（费曼规则 → 截面公式的标准记账）与 §5.1（$e^+e^-\to\mu^+\mu^-$——第 05 篇的母本）。
- Schwartz《Quantum Field Theory and the Standard Model》截面与衰变率一章（流强因子的两种推导：波包法与盒子法）。
- Weinberg《The Quantum Theory of Fields》第一卷第 3 章（$S$ 矩阵的一般性质与解析性——本篇 §2 的公理化底座）。
- D. Tong 量子场论讲义（Cambridge，在线公开）截面与 LSZ 部分（推导节奏与本篇接近，配习题）。
