# 补充材料：散射的形式理论——T 矩阵、库仑精确解与全同粒子散射

> 路线图位置：量子力学书 · 第三部分（近似方法）· 第 08 篇[散射理论基本概念](08-scattering-theory.md)的补充材料（第 08s 篇）
> 前置知识：第 08 篇（截面与振幅、分波展开、Born 近似、Lippmann–Schwinger 积分方程——本篇把它的方程升级成算符语言）；第 03 篇（算符、幺正性、格林函数式思考：$(z-H)^{-1}$）；第 05s 篇（全同粒子与对称化——末节要用）；第 04 篇（升降算符——共振极点类比 propagator 时用到语言）。
> 学习目标：会把散射问题写成算符方程 $T = V + VG_0^\pm T$ 并说清 $G_0^\pm$ 的边值条件如何编码"出射波"；会从 $T$ 的迭代得到玻恩级数、指出第 08 篇的一阶 Born 是第一项；会从 $S$ 矩阵幺正性推出光学定理的算符版本；会用 $T$ 的极点读出束缚态与共振；理解库仑势为什么让分波求和失效（相移对数增长）并写下精确振幅与 Coulomb 相移 $\sigma_l = \arg\Gamma(l+1+i\eta)$；会对全同粒子做末态（反）对称化，算出 Mott 散射与电子–电子散射的截面公式。
>
> 记号约定：与第 08 篇一致保留 $\hbar$；平面波归一 $\langle\vec r\vert\vec k\rangle = e^{i\vec k\cdot\vec r}$（每 $(2\pi)^3$ 体积一个态），动量表象的正交归一 $\langle\vec k'\vert\vec k\rangle = (2\pi)^3\delta^3(\vec k'-\vec k)$。

---

## 1. 一句话总结

**第 08 篇的 Lippmann–Schwinger 积分方程可以整体打包成一条算符关系 $T(E\pm i0) = V + V(z-H_0)^{-1}T$：格林算符的 $\pm i0$ 边值条件就是"出射/入射球面波"，迭代展开就是玻恩级数（一阶 Born 是第一项），$T$ 在实轴下方的极点是束缚态、第二叶上的复极点是共振（Breit–Wigner 的来源），$S^\dagger S=1$ 直接给出光学定理；库仑势因长程性（$\delta_l$ 对数增长）逃出这套框架，但有抛物线坐标下的精确解 $f_C\propto e^{-i\eta\ln\sin^2(\theta/2)}$、模方回到卢瑟福；而全同粒子的末态必须（反）对称化——截面里出现 $f(\theta)\pm f(\pi-\theta)$ 的干涉项，$90^\circ$ 处玻色子增强 4 倍、同自旋费米子归零（Mott 极化仪的原理）。**

## 2. 从积分方程到算符：格林算符与 T 矩阵

第 08 篇 §6.1 把定态薛定谔方程改写成积分方程。现在把它写成算符语言。定义**自由格林算符**

$$G_0(z) \equiv (z - H_0)^{-1},\qquad z = E \pm i0,$$

以及**散射算符（T 矩阵）**

$$T(z) \equiv V + VG_0(z)\,T(z).$$

形式迭代立刻给出（用 $(1-A)^{-1} = 1+A+A^2+\cdots$ 的算符版）：

$$T = V + VG_0V + VG_0VG_0V + \cdots\qquad(\text{玻恩级数})，$$

而散射态与振幅是

$$\lvert\psi^\pm\rangle = \lvert\vec k\rangle + G_0(E\pm i0)\,T(E\pm i0)\,\lvert\vec k\rangle,\qquad f(\theta) = -\frac{m}{2\pi\hbar^2}\,\langle\vec k'\vert T(E+i0)\vert\vec k\rangle,$$

（$\vec k'$ 取 $\vec k$ 转过 $\theta$ 的方向；一阶截断 $T\approx V$ 精确还原第 08 篇的 $f^{(1)} = -\frac{m}{2\pi\hbar^2}\tilde V(\vec q)$。）

**$\pm i0$ 的物理**：坐标表象里（自检问题 1）

$$\langle\vec r\vert G_0(E\pm i0)\vert\vec r'\rangle = -\frac{m}{2\pi\hbar^2}\,\frac{e^{\pm i k\lvert\vec r-\vec r'\rvert}}{\lvert\vec r-\vec r'\rvert},$$

$+i0$ 挑出**出射**球面波——这正是散射边界条件。$i0$ 不是技巧，是辐射条件。

**记号接口**：QFT 书里的**传播子**就是场论的格林函数（[路径积分表述](../../qft-sm/docs/stage-04-qft-core/07-path-integral.md)），$T$ 矩阵则升级为不变振幅 $\mathcal M$（第 08 篇 §8）——结构一一对应。

## 3. 幺正性：光学定理的算符版本

弹性散射的 $S$ 矩阵按定义与 $T$ 相连：

$$S = \mathbb 1 - 2\pi i\,\delta(E - H_0)\,T.$$

幺正性 $S^\dagger S = \mathbb 1$ 经过一条两行的代数（自检问题 2，关键是恒等式 $G_0^+ - G_0^- = -2\pi i\,\delta(E-H_0)$）给出

$$T - T^\dagger = -2\pi i\,T^\dagger\delta(E-H_0)\,T.$$

取 $\langle\vec k\vert\cdot\vert\vec k\rangle$ 并与 $f(\theta)$ 的定义对表（自检问题 2 走完全程）：

$$\operatorname{Im} f(0) = \frac{k}{4\pi}\,\sigma_{\rm tot}.$$

第 08 篇 §5.4 用分波求和"碰巧"得到的光学定理，在算符层面是**概率守恒的逐字翻译**，连分波都不需要。开放通道（非弹性）时把 $V$ 换成光学势，同样的推导给出 $\sigma_{\rm tot} \ge \sigma_{\rm elastic}$——"影子"总比弹性阴影大。

## 4. T 的极点：束缚态与共振

全 GREEN 函数 $G(z) = (z-H)^{-1}$ 与 $T$ 由 $G = G_0 + G_0TG_0$ 相连，二者的奇点结构相同：

- **实轴下方的实极点 = 束缚态**：$T(z)$ 在 $z = E_B < 0$ 处有极点，留数正比束缚态波函数的乘积 $\varphi_B(\vec k')\varphi_B^*(\vec k)$。散射态的理论"免费"知道束缚态——同一台机器。
- **第二叶上的复极点 = 共振**：$z = E_R - i\Gamma/2$。在 $E_R$ 附近单极点主导，$T \sim \frac{\gamma\gamma^\dagger}{E - E_R + i\Gamma/2}$，代入截面公式就是第 08 篇 §5.5 的 Breit–Wigner 线型——原来 $\delta_l$ 扫过 $\pi/2$ 的背后是复平面上的一个极点。QFT 书里粒子的"质量–宽度"（$Z$ 玻色子 $M - i\Gamma_Z/2$）是同一句话的场论版（[QCD 笔记](../../qft-sm/docs/stage-06-standard-model/03-qcd.md)的共振峰）。

**分波与 S 矩阵的接口**：短程势下 $S_l = e^{2i\delta_l}$，幺正性 $|S_l| = 1$（弹性）；共振附近 $S_l$ 在复 $k$ 平面上画过单位圆——$\delta_l = \pi/2$ 正是离实轴最近的时刻。

## 5. 库仑势：长程的麻烦与精确解

第 08 篇假设 $V$ 比 $1/r$ 衰减得快。库仑势恰恰不满足：长程力使无穷远处仍有相位积累，后果有两个：

1. **总截面发散**（前向 $\theta\to0$ 库仑截面 $\propto 1/\theta^4$ 已见）；
2. **分波求和不收敛**：库仑"相移"随 $l$ 对数增长，$\delta_l^{\rm Coulomb}\sim \eta\ln l$，无穷多分波同量级参与——第 08 篇的 $f = \frac1k\sum(2l+1)e^{i\delta_l}\sin\delta_l$ 失去意义。

出路是**换坐标直接解**：抛物线坐标 $(\xi,\eta,\varphi)$ 下薛定谔方程可分离，出射波解给出精确振幅

$$\boxed{\ f_C(\theta) = -\frac{\eta}{2k\sin^2(\theta/2)}\;e^{-i\eta\ln\sin^2(\theta/2)\,+\,2i\sigma_0},\qquad \eta = \frac{Z_1Z_2e^2}{4\pi\varepsilon_0\hbar v}\ }$$

其中 $\sigma_l = \arg\Gamma(l+1+i\eta)$ 是 **Coulomb 相移**。三件事值得读出：

- 模方 $\lvert f_C\rvert^2 = \frac{\eta^2}{4k^2\sin^4(\theta/2)}$ **逐字回到卢瑟福公式**（第 08 篇 §7 的 Born 近似在库仑情形"算对"的深层原因：库仑是少数 Born 与精确一致的势——只差一个纯相位）；
- 那个纯相位 $-i\eta\ln\sin^2(\theta/2)$ 无经典对应，在干涉实验里真实可测；
- $\eta\to0$（中性粒子或高能）时 $\sigma_l\to0$，平滑退化回短程理论——长程性被 $\eta$ 参数化。

**实用细节**：核物理里"库仑 + 短程核力"的处理是把径向波函数换成库仑函数 $F_l(\eta,kr),G_l(\eta,kr)$（渐近 $\sin$/$\cos$ 的库仑版），核相移叠加在 $\sigma_l$ 之上；固体里电子-杂质散射则常先屏蔽（Yukawa 截断，第 08 篇的 $\mu$），算完再小心取极限——两套操作都是"先把长程摘出去"的同一种谨慎。

## 6. 全同粒子的散射

两个**可分辨**粒子的质心系截面是 $\frac{d\sigma}{d\Omega} = \lvert f(\theta)\rvert^2$，探测器放在 $\theta$ 只数一个方向。若两粒子**全同**，质心系里"甲弹到 $\theta$、乙弹到 $\pi-\theta$"与"甲弹到 $\pi-\theta$、乙弹到 $\theta$"是**同一个末态**——末态波函数必须（反）对称化（第 05s 篇），振幅直接相加/相减：

$$\boxed{\ \frac{d\sigma}{d\Omega} = \big\lvert f(\theta) \pm f(\pi-\theta)\big\rvert^2\ }\qquad(+\ \text{玻色子}，\ -\ \text{无自旋费米子}).$$

注意**没有** $1/2$ 因子：对称化后的末态在 $(\theta, \pi-\theta)$ 两处各贡献一次计数，恰好补偿"角空间减半"。

**自旋 1/2 费米子（电子–电子）**：总波函数反对称——自旋单态（反对称，权重 $\tfrac14$）配空间对称 $\lvert f+f'\rvert^2$，三重态（对称，权重 $\tfrac34$）配空间反对称 $\lvert f-f'\rvert^2$：

$$\frac{d\sigma}{d\Omega} = \tfrac14\big\lvert f(\theta)+f(\pi-\theta)\big\rvert^2 + \tfrac34\big\lvert f(\theta)-f(\pi-\theta)\big\rvert^2 \qquad(\text{非极化}).$$

极化束流（自旋态制备确定，如 $\lvert\uparrow\uparrow\rangle$，纯三重态 $m=1$）截面是 $\lvert f-f'\rvert^2$。

**$90^\circ$ 处的戏剧**：$\theta = \pi/2$ 时 $f = f'$——

| 体系 | $\frac{d\sigma}{d\Omega}\big(90^\circ\big)$ | 与可分辨粒子（两方向计数 $2\lvert f\rvert^2$）之比 |
| --- | --- | --- |
| 自旋 0 玻色子（如 $\alpha$–$\alpha$） | $\lvert 2f\rvert^2 = 4\lvert f\rvert^2$ | 2 倍 |
| 同向自旋电子（$\uparrow\uparrow$） | $0$ | 0（Pauli 节点） |
| 非极化电子 | $\lvert f\rvert^2$ | $\tfrac12$ |

玻色子的 4 倍增强与费米子的归零是**统计的干涉签名**。**Mott 极化仪**用的正是后者：自旋极化的电子打薄箔，$90^\circ$ 两侧计数不对称度直接读出束流极化——Pauli 不相容原理变成一台工程仪器（自旋-轨道型分析器的原型）。

**可分辨极限**：质量相近但不全同（如 $e^+$–$e^-$），两方向是不同末态，各自计数 $\lvert f(\theta)\rvert^2$ 与 $\lvert f(\pi-\theta)\rvert^2$，无干涉项——连续地检验统计性的实验（核子–核子散射中质子-中子 vs 质子-质子）就是这么做的。

## 7. 接口

- **QFT**：$T\to\mathcal M$、$G_0\to$ 费曼传播子、极点→粒子的质量与宽度、**末态全同粒子→费曼图对称因子**（Feynman rules 里那些 $1/2!$ 的来源就是本篇的末态对称化，[QED 笔记](../../qft-sm/docs/stage-04-qft-core/05-qed.md)）。
- **凝聚态**：电子被杂质/声子散射的输运理论全套用 $T$ 矩阵语言（[自由电子气](../../condensed-matter/docs/03-free-electron-gas.md)的弛豫时间）；杂质散射的共振（虚束缚态）即 $\delta=\pi/2$ 共振。
- **本篇与第 08 篇的分工**：08 篇管"算"（分波 + Born 两件武器与本篇完全兼容），本篇管"形式"（算符、幺正性、极点、统计）。

## 小结

| 工具 | 公式 | 用途 |
| --- | --- | --- |
| 格林算符 | $G_0^\pm = (E\pm i0-H_0)^{-1}$ | 边值条件 $=$ 出射波 |
| T 矩阵 | $T = V + VG_0T$，$f = -\frac{m}{2\pi\hbar^2}\langle k'\vert T\vert k\rangle$ | 微扰展开的总机 |
| 玻恩级数 | $T = V + VG_0V + \cdots$ | 08 篇 Born 是首项 |
| 幺正性 | $T-T^\dagger = -2\pi iT^\dagger\delta T$ | 光学定理的根源 |
| 极点 | $E_B<0$ 束缚态；$E_R-i\Gamma/2$ 共振 | Breit–Wigner 的来源 |
| 库仑 | $f_C\propto e^{-i\eta\ln\sin^2(\theta/2)}$，$\sigma_l = \arg\Gamma(l+1+i\eta)$ | 长程使分波失效 |
| 全同粒子 | $\lvert f(\theta)\pm f(\pi-\theta)\rvert^2$ | 90°：玻色 4 倍、费米归零 |

一句话收束：把 Lippmann–Schwinger 写成 $T = V+VG_0T$，散射理论的三大件——微扰展开、幺正性约束、解析（极点）结构——就各就各位；库仑势是长程的例外但可精确解；末态统计不是修正项，是截面的结构性成分。

## 自检问题

**1.** 用傅里叶表示证明 $\langle\vec r\vert G_0(E\pm i0)\vert\vec r'\rangle = -\frac{m}{2\pi\hbar^2}\frac{e^{\pm ik\lvert\vec r-\vec r'\rvert}}{\lvert\vec r-\vec r'\rvert}$，并说明 $i0$ 如何挑出出射波。

<details markdown="1"><summary>点击显示答案</summary>

谱表示：$\langle r\vert G_0\vert r'\rangle = \int\frac{d^3q}{(2\pi)^3}\,\frac{e^{i\vec q\cdot(\vec r-\vec r')}}{E\pm i0 - \hbar^2q^2/2m}$。记 $\rho = \lvert\vec r-\vec r'\rvert$，角向积出 $\frac{1}{4\pi\rho}\int_{-\infty}^\infty dq\,q\,\frac{e^{iq\rho}-e^{-iq\rho}}{E\pm i0-\hbar^2q^2/2m}\cdot\frac{1}{i}$ 化为对 $e^{iq\rho}$ 的单边积分：

$$\langle r\vert G_0\vert r'\rangle = \frac{1}{(2\pi)^3\,4\pi\rho}\cdot 4\pi \int_{-\infty}^{\infty} dq\,\frac{q\sin(q\rho)}{E\pm i0 - \hbar^2q^2/2m}\cdot(\text{角度因子})\ \to\ \frac{m}{\pi^2\hbar^2\rho}\int_0^\infty dq\,\frac{q\sin q\rho}{k^2 - q^2 \pm i0'\,2m/\hbar^2}\cdot\frac{1}{2}，$$

其中用了 $k^2 = 2mE/\hbar^2$ 并把分母乘 $2m/\hbar^2$。关键在围道：$e^{iq\rho}$ 因子（$\rho>0$）要求上半平面闭合，分母 $k^2 - q^2 \pm i0$ 的极点在 $\pm k \pm i0''$——$+i0$ 把 $+k$ 处的极点抬到上半平面（贡献留数），$-k$ 处压到下半平面（不贡献）。留数给出 $\propto e^{ik\rho}$；$-i0$ 相反，留下半平面的 $e^{-ik\rho}$。合并系数（把 $\sin$ 拆成两个指数分别处理，两个半平面各闭合一次）：

$$G_0^\pm(\rho) = -\frac{m}{2\pi\hbar^2}\,\frac{e^{\pm ik\rho}}{\rho}.$$

负号来自绕极点的方向。物理读法：$\frac{e^{ik\rho}}{\rho}$ 是从 $\vec r'$ 发出的**出射**球面波——源项 $V\psi$ 经 $G_0^+$ 传播出去，就是辐射条件。这也解释了第 08 篇 §6.1 里那个"凭空出现"的 $-\frac{e^{ikr}}{4\pi r}$：它是亥姆霍兹算符的出射格林函数，乘 $2m/\hbar^2$ 正是 $G_0^+$。

</details>

**2.** 从 $G_0^+ - G_0^- = -2\pi i\,\delta(E-H_0)$ 出发推导 $T - T^\dagger = -2\pi i\,T^\dagger\delta(E-H_0)\,T$，再取 $\langle\vec k\vert\cdot\vert\vec k\rangle$ 完整导出光学定理 $\sigma_{\rm tot} = \frac{4\pi}{k}\operatorname{Im}f(0)$。

<details markdown="1"><summary>点击显示答案</summary>

第一步（分布恒等式）：$\frac{1}{x+i0}-\frac{1}{x-i0} \to -2\pi i\,\delta(x)$，对算符函数同样成立，给出 $G_0^+ - G_0^- = -2\pi i\,\delta(E-H_0)$。

第二步（幺正性关系）：$T = V + VG_0^+T$ 与其镜像 $T = V + T^\dagger G_0^- V$（两边取厄米共轭再用 $V^\dagger = V$）相减：

$$T - T^\dagger = V G_0^+ T - T^\dagger G_0^- V.$$

把镜像方程移项 $VG_0^+T = T - V$、$T^\dagger G_0^-V = T^\dagger - V$ 代入右边，两项相减得恒等式 $T - T^\dagger = T - T^\dagger$——一阶代入只给出自洽性，不产生内容。内容来自把任一边裸露的 $V$ 按玻恩级数逐阶升级（每阶用一次 $G_0^+ - G_0^-$）。二阶验证：

$$T - T^\dagger \supset V(G_0^+ - G_0^-)V = -2\pi i\,V\,\delta(E-H_0)\,V,$$

恰是 $-2\pi i\,T^\dagger\delta T$ 展开到同阶的首项；逐阶堆叠全部闭合（严格证明见 Taylor, *Scattering Theory*）：

$$T - T^\dagger = -2\pi i\,T^\dagger\,\delta(E-H_0)\,T.$$

第三步（取矩阵元）：左边 $\langle k\vert T-T^\dagger\vert k\rangle = 2i\operatorname{Im}T_{kk}$。右边插入动量完备基：

$$\langle k\vert T^\dagger\delta(E-H_0)T\vert k\rangle = \int\frac{d^3k'}{(2\pi)^3}\,\delta(E-E_{k'})\,\lvert T_{k'k}\rvert^2 = \frac{1}{(2\pi)^3}\cdot\frac{mk}{\hbar^2}\int d\Omega\,\lvert T_{k'k}\rvert^2,$$

（径向积分 $\int k'^2dk'\,\delta(E-\hbar^2k'^2/2m) = mk/\hbar^2$，壳上 $k'=k$。）代入 $\lvert T_{k'k}\rvert^2 = (2\pi\hbar^2/m)^2\lvert f(\theta)\rvert^2$ 与 $\sigma_{\rm tot} = \int d\Omega\lvert f\rvert^2$：

$$\langle k\vert T^\dagger\delta T\vert k\rangle = \frac{1}{8\pi^3}\cdot\frac{mk}{\hbar^2}\cdot\frac{4\pi^2\hbar^4}{m^2}\,\sigma_{\rm tot} = \frac{k\hbar^2}{2\pi m}\,\sigma_{\rm tot}.$$

于是 $2i\operatorname{Im}T_{kk} = -2\pi i\cdot\frac{k\hbar^2}{2\pi m}\sigma_{\rm tot}$，即

$$\operatorname{Im}T_{kk} = -\frac{k\hbar^2}{2m}\,\sigma_{\rm tot}.$$

最后代入 $f(0) = -\frac{m}{2\pi\hbar^2}T_{kk}$：

$$\operatorname{Im}f(0) = \frac{m}{2\pi\hbar^2}\cdot\frac{k\hbar^2}{2m}\,\sigma_{\rm tot} = \frac{k}{4\pi}\,\sigma_{\rm tot}\;\;\Longleftrightarrow\;\; \sigma_{\rm tot} = \frac{4\pi}{k}\operatorname{Im}f(0).$$

与第 08 篇 §5.4 的分波版独立对表一致——这次连中心势都没用。

</details>

**3.** 解释库仑势为什么使分波展开失效；验证 $\lvert f_C\rvert^2$ 给出卢瑟福公式；并说明 $\eta\to0$ 时如何平滑回到短程理论。

<details markdown="1"><summary>点击显示答案</summary>

失效机制：分波展开的有效性依赖"每个分波只积累有限相位"。短程势下 $l \gtrsim ka$ 的分波几乎不受影响（离心势垒，第 08 篇 §5.5），求和实际截断。库仑力程无穷：第 $l$ 个分波在 $r\sim l/k$ 处仍感受到 $\sim 1/r$ 的势，累积相位 $\delta_l^{\rm Coulomb} = \sigma_l \approx \eta\ln l + O(1)$ **对数增长**——任何 $l$ 都不小，$\sum(2l+1)e^{i\delta_l}\sin\delta_l$ 发散；同时总截面被前向 $1/\theta^4$ 积分发散拖垮。根源一句话：**渐近态不再是自由平面波**。

模方验证：$\lvert f_C\rvert^2 = \frac{\eta^2}{4k^2\sin^4(\theta/2)}$。代 $\eta = \frac{Z_1Z_2e^2}{4\pi\varepsilon_0\hbar v}$、$k = mv/\hbar$：$\frac{\eta}{2k} = \frac{Z_1Z_2e^2}{4\pi\varepsilon_0\cdot 2\hbar v\cdot mv/\hbar} = \frac{Z_1Z_2e^2}{4\pi\varepsilon_0\cdot 4E}$（$E = \tfrac12mv^2$），即 $\frac{d\sigma}{d\Omega} = \Big(\frac{Z_1Z_2e^2}{16\pi\varepsilon_0 E}\Big)^2\frac{1}{\sin^4(\theta/2)}$——卢瑟福公式，与第 08 篇 §7 Born 版逐字相同（库仑势的 Born 近似恰好给出精确模方，差在不可测的单角度纯相位）。

$\eta\to0$：$\Gamma(l+1+i\eta) \to \Gamma(l+1)$ 为正实数，$\sigma_l\to0$；振幅里 $\eta$ 前因子也 $\to0$，库仑效应整体消失，分波 $\delta_l\to0$ 回到自由或纯短程情形。可见 $\eta$（耦合除以速度）是"长程性"的定量旋钮：高能或弱耦合下库仑可当微扰，低能强耦合必须用 $F_l, G_l$ 库仑函数。

</details>

**4.** 对自旋 0 的全同玻色子（如 $\alpha$ 粒子对撞），推导 $\frac{d\sigma}{d\Omega} = \lvert f(\theta)+f(\pi-\theta)\rvert^2$；证明 $90^\circ$ 处截面是可分辨粒子"两方向计数"的两倍。

<details markdown="1"><summary>点击显示答案</summary>

质心系中两全同玻色子的末态空间波函数必须对称：$f(\theta) + f(\pi-\theta)$（$\theta$ 与 $\pi-\theta$ 的散射末态互换粒子后是同一物理构型，对称化即振幅相加）。截面 $\propto\lvert f(\theta)+f(\pi-\theta)\rvert^2$，无 $1/2$：末态对称化后 $(\theta,\pi-\theta)$ 是同一个立体角对的重复计数，立体角 $4\pi$ 只数一遍，而探测器在 $\theta$ 与 $\pi-\theta$ 处各看到全部粒子流——归一化自洽。

$90^\circ$：$\pi-\theta = \theta$，$f(\pi-\theta) = f(\theta)$：截面 $= 4\lvert f(90^\circ)\rvert^2$。可分辨粒子同条件：$\theta$ 方向计数 $\lvert f(\theta)\rvert^2$，加上"互换末态"在 $\theta$ 处的计数 $\lvert f(\pi-\theta)\rvert^2 = \lvert f(\theta)\rvert^2$，共 $2\lvert f\rvert^2$。比值 $4/2 = 2$：**玻色子在 $90^\circ$ 有 2 倍增强**——相长干涉的直接观测（$\alpha$–$\alpha$ 散射的经典实验，Chadwick 时代已知，量子统计的早期证据）。

</details>

**5.** 对非极化电子–电子散射，从单态/三重态权重推出 $\frac{d\sigma}{d\Omega} = \tfrac14\lvert f+f'\rvert^2 + \tfrac34\lvert f-f'\rvert^2$；证明同向自旋（$\uparrow\uparrow$）在 $90^\circ$ 截面为零、非极化是可分辨情形的 $\tfrac12$，并说明 Mott 极化仪如何利用这个零点。

<details markdown="1"><summary>点击显示答案</summary>

电子是费米子，总波函数反对称：自旋单态（反对称）配空间对称振幅 $f+f'$，三重态（对称）配 $f-f'$。非极化束流的自旋态均匀分布：单态占 $\tfrac14$（4 维自旋空间中的 1 维），三重态占 $\tfrac34$——截面是权重平均。展开整理：

$$\frac{d\sigma}{d\Omega} = \tfrac14\lvert f+f'\rvert^2 + \tfrac34\lvert f-f'\rvert^2 = \lvert f\rvert^2 + \lvert f'\rvert^2 - \operatorname{Re}\!\big(f^*\,f'\big)\qquad(f'\equiv f(\pi-\theta))，$$

（交叉项系数 $\tfrac14\cdot2 - \tfrac34\cdot2 = -1$。）干涉项 $\operatorname{Re}(f^*f')$ 就是"统计的可观测签名"。

$90^\circ$：$f=f'$。$\uparrow\uparrow$（纯三重态 $m=+1$）：截面 $\lvert f-f\rvert^2 = 0$——两个同自旋投影的电子不能散射到同一角度，Pauli 原理的干涉表达（不是"被弹开"，是两振幅严格相消）。非极化：$\tfrac14\cdot4\lvert f\rvert^2 + \tfrac34\cdot0 = \lvert f\rvert^2$，而可分辨情形 $2\lvert f\rvert^2$，比值 $\tfrac12$。

Mott 极化仪：横向极化电子束（自旋 $\uparrow$ 占多）打无自旋薄靶（实际用金箔，弹性散射；相对论下自旋-轨道耦合把"自旋投影"耦合到散射平面），散射后 $90^\circ$ 左右两探测器的计数差正比于束流极化度——其非相对论内核就是本篇的统计干涉：三重态分量在 $90^\circ$ 被压低、单态增强，左右不对称读出自旋。固定装置、只读计数比：Pauli 不相容原理成为测量仪器。

</details>

## 参考

- Sakurai《现代量子力学》第 6 章（散射理论）——T 矩阵与算符形式的标准推导（与本篇归一约定一致，注意其对 $G_0$ 的符号约定）。
- Taylor, *Scattering Theory*——玻恩级数、极点与共振的最系统参考。
- 朗道《量子力学》库仑散射章节——抛物线坐标与库仑函数。
- Griffiths《量子力学概论》习题（全同粒子散射、Mott 散射）。
- 第 05s 篇（[全同粒子与对称化公设](05s-identical-particles.md)）——末态对称化的公设来源。
