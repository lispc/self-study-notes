# 补充材料：路径积分也能解氢原子——Duru–Kleinert 变换

> 路线图位置：量子力学书 · 第二部分（可精确求解的体系）· 第 06s3 篇——QFT 书第 4 阶段 [路径积分表述](../../qft-sm/docs/stage-04-qft-core/07-path-integral.md) 篇（下称"第 07 篇"）的姊妹篇
> 前置知识：第 07 篇（传播子、时间切片、$\int\mathcal{D}x\,e^{iS/\hbar}$ 的记号全部沿用它的约定）；氢原子的波动力学解（[第 06 篇 氢原子与电子亚层](06-hydrogen-and-subshells.md)，用来对照最终能谱）；经典力学的中心势运动（有效势、第一积分）。
> 学习目标：说清库仑势的路径积分为什么病态、正确对象为什么是定能格林函数；掌握 Sundman 赝时 $dt = r\,ds$ 与 Levi-Civita / Kustaanheimo–Stiefel 变换如何把 Kepler 问题映成谐振子；走通 Duru–Kleinert 推导主线，从振子传播子的极点读出束缚态谱；明确知道哪几步是严格推导、哪几步本篇承认引用。
>
> 记号约定：本篇保留 $\hbar$（非相对论量子力学，与氢原子各篇一致），$m_e$ 为电子质量（折合质量近似）。库仑势写作 $V(r) = -e^2/r$，其中 $e^2 \equiv e_{\mathrm{SI}}^2/(4\pi\varepsilon_0)$，于是基态 $E_1 = -m_ee^4/(2\hbar^2) = -13.6$ eV，自然单位下 $e^2 = 4\pi\alpha$。撇号 $' \equiv d/ds$ 专指对赝时 $s$ 的导数。

---

## 1. 一句话总结

**库仑势的 $1/r$ 奇点使朴素时间切片的路径积分病态——经典上存在有限时间内坠入中心的轨道，量子上布朗型路径总会擦过原点并捡起不受控的相位——但只要改问定能格林函数 $G(E) = \int_0^\infty dT\,e^{iET/\hbar}K(T)$，再做一次经典力学的老手术（Sundman 赝时 $dt = r\,ds$ + Levi-Civita / Kustaanheimo–Stiefel"平方根坐标" $r = u^2$），库仑势就退化成常数、$-E\,r$ 变成谐振子势，路径积分化为已知的振子传播子，其极点条件精确还原玻尔能级 $E_n = -m_ee^4/(2\hbar^2n^2)$ 与 $n^2$ 简并——Feynman 当年没能积出的库仑传播子，本质上是"用对了时间的谐振子"。**

下面按"病根 → 经典手术 → 量子通关"的次序展开。二维 Levi-Civita 版本做透，三维 Kustaanheimo–Stiefel 版本给出映射与结论，并诚实标注哪一步是承认的。

## 2. 库仑势为什么难倒路径积分

### 2.1 经典病根：坠入中心的轨道

中心势径向运动由有效势控制：

$$\frac{m_e}{2}\dot r^2 + V_{\mathrm{eff}}(r) = E, \qquad V_{\mathrm{eff}}(r) = \frac{L^2}{2m_er^2} - \frac{e^2}{r}.$$

$L \neq 0$ 时离心垒 $L^2/2m_er^2$ 在近处压倒库仑井，轨道有近日点 $r_{\min} > 0$。但 $L = 0$ 时没有垒：$\dot r = -\sqrt{(2/m_e)(E + e^2/r)}$，粒子在**有限时间**内到达 $r = 0$——近原点处被积函数 $\sim \sqrt{r}$，积分收敛：

$$\tau = \int_0^{r_0} \frac{dr}{\sqrt{\frac{2}{m_e}\big(E + \frac{e^2}{r}\big)}} < \infty \qquad \Big(E=0\text{ 时 } \tau = \frac{2}{3}\sqrt{\frac{m_e}{2e^2}}\,r_0^{3/2}\Big),$$

且速度以 $r^{-1/2}$ 发散。到达中心之后该怎么办，牛顿方程自己回答不了——经典力学在碰撞点**不完备**。天体力学处理三体碰撞奇点（Sundman，1912）和发展 Kepler 问题正则化（Levi-Civita、Kustaanheimo–Stiefel）的全部动机就在这里，第 3 节会把这套经典手术搬过来。

### 2.2 切片病根：$1/r$ 奇点对阵布朗路径

第 07 篇 2.2 节的时间切片之所以可控，是因为对光滑有界的 $V$，单个切片贡献的相位 $\epsilon V/\hbar$ 在 $\epsilon \to 0$ 时一致地趋于零，BCH 拆分的误差 $O(\epsilon^2)$ 也被 $N = T/\epsilon$ 个切片安全地摊薄。库仑势两条都破坏：

- 路径积分里的典型路径是布朗型的，$|\Delta x| \sim \sqrt{\epsilon}$，它们以不为零的权重穿过原点附近。一个停留在 $r$ 处的切片捡起相位 $\epsilon e^2/(\hbar r)$，当 $r \sim \epsilon e^2/\hbar$ 时相位是 $O(1)$ 的——**不随 $\epsilon$ 消失**。
- 单个切片命中细管的概率 $\sim \epsilon$，但切片数 $N \sim 1/\epsilon$，于是 $O(1)$ 比例的路径带着不受控的相位贡献进入 $N \to \infty$ 极限。同时 $V$ 的各阶导数在原点发散，BCH 的误差估计就地作废。

结论：朴素测度在库仑势下没有受控的连续极限。这正是 Feynman–Hibbs 书里只处理了二次型体系与微扰展开、库仑传播子始终缺位的原因——不是计算懒惰，是框架本身漏了。量子力学的算符 $H$ 本身其实没病（$1/r$ 吸引势的哈密顿量有下界、自伴），**病的是路径积分的构造方式**，而治病的是换问题 + 换变量。

### 2.3 正确的对象：定能格林函数

Duru–Kleinert 的第一招是换一个问法。不直接算 $K(T)$，而是算它的能量变换——**定能格林函数**（resolvent 的坐标矩阵元）：

$$G(\vec x_b, \vec x_a; E) \equiv \int_0^\infty dT\,e^{iET/\hbar}\,K(\vec x_b, \vec x_a; T) = \Big\langle \vec x_b \Big| \frac{i\hbar}{E - H + i0} \Big| \vec x_a \Big\rangle .$$

（收敛性由 $E \to E + i0$ 保证；逐字积分 $\int_0^\infty dT\,e^{i(E-H)T/\hbar} = i\hbar/(E-H+i0)$。）用谱分解 $K = \sum_n \psi_n(\vec x_b)\psi_n^*(\vec x_a)\,e^{-iE_nT/\hbar}$ 代入：

$$G = \sum_n \frac{i\hbar\,\psi_n(\vec x_b)\psi_n^*(\vec x_a)}{E - E_n + i0},$$

**束缚态能谱 = $G(E)$ 在负实轴上的极点**，留数还给波函数。所以对能谱感兴趣的话，$G(E)$ 是比 $K(T)$ 更直接的对象；而且下面会看到，固定 $E$ 之后 $H - E$ 可以被整体吸进赝时变换——这正是定能实现而定时不能的手术。

## 3. 正则化的经典根源

### 3.1 Sundman 赝时：$dt = r\,ds$

Sundman 的想法（1912 年，为三体碰撞奇点而发明）：在接近碰撞时把时钟调慢——引入新参数 $s$，

$$dt = r\,ds .$$

沿任何 $r > 0$ 的轨道，$dt/ds = r > 0$，所以 $t \leftrightarrow s$ 是单调重参数化，**轨道的几何内容不变**（自检问题 4 严格证明这一点）。收益在近原点处立刻可见：径向能量第一积分 $(m_e/2)\dot r^2 - e^2/r = E$ 两边乘 $r$，用 $\dot r = r'/r$ 改写：

$$\frac{m_e}{2r}\,r'^2 - e^2 = E\,r \qquad\Longleftrightarrow\qquad r'^2 = \frac{2r}{m_e}\big(e^2 + Er\big),$$

$r \to 0$ 时 $r' \to 0$，$s$ 参数下的运动在碰撞点光滑——奇点被"时间膨胀"吸收了。这还只是径向的预演；真正的魔法要和坐标变换联手。

### 3.2 二维 Levi-Civita：Kepler 问题就是振子问题

二维里引入复坐标的平方映射（Levi-Civita 变换）：

$$z = x_1 + ix_2 = w^2, \qquad w = u_1 + iu_2, \qquad r = |z| = |w|^2 = u_1^2 + u_2^2.$$

动能项的变换一步验证：$dz = 2w\,dw$，故

$$|dz|^2 = 4|w|^2\,|dw|^2 = 4r\,\big(du_1^2 + du_2^2\big).$$

现在把 Sundman 与 Levi-Civita 叠加到**固定能量**的轨道上。能量守恒 $(m_e/2)|\dot z|^2 - e^2/r = E$ 中，$|\dot z|^2 = |z'|^2/r^2 = 4|w'|^2/r$，代入并两边乘 $r$：

$$2m_e\,|\vec u\,'|^2 - e^2 = E\,|\vec u|^2 \qquad\Longleftrightarrow\qquad 2m_e\,|\vec u\,'|^2 - E\,\vec u^{\,2} = e^2 .$$

对 $E < 0$（束缚态），这正是一个**二维各向同性谐振子**的能量第一积分：质量 $\mu = 4m_e$，形式频率 $\omega^2 = -E/(2m_e)$，"能量"扮演者是常数 $e^2$。对 $s$ 求导得运动方程 $\vec u\,'' = (E/2m_e)\,\vec u$——每个固定 $E$ 的 Kepler 轨道，逐字是一个振子轨道。代价是变换依赖 $E$（每个能量配一个频率），所以我们注定要在定能的对象上工作——与 2.3 节的换问题正好咬合。

### 3.3 三维 Kustaanheimo–Stiefel：没有三维平方根，就上四维

三维不存在逐点的"平方根坐标"（没有三维的除代数），Kustaanheimo–Stiefel（1965）的办法是多维化：取 $\vec u \in \mathbb{R}^4$，记 $w_1 = u_1 + iu_2$、$w_2 = u_3 + iu_4$，定义

$$x_1 + ix_2 = 2w_1^* w_2, \qquad x_3 = |w_1|^2 - |w_2|^2 .$$

两个关键恒等式（第一个两行可验，第二个是直接但冗长的展开）：

$$r = |\vec x| = |\vec u|^2 = u_1^2 + u_2^2 + u_3^2 + u_4^2,$$

$$|d\vec x|^2 = 4|\vec u|^2\,|d\vec u|^2 - 4\ell^2, \qquad \ell \equiv u_4\,du_1 - u_3\,du_2 + u_2\,du_3 - u_1\,du_4 .$$

第一条：$x_1^2 + x_2^2 = 4|w_1|^2|w_2|^2$，加 $x_3^2$ 配方即得 $(|w_1|^2 + |w_2|^2)^2$。第二条里的 $\ell$ 是一个双线性约束：物理路径要求 $\ell = 0$（不可积约束），在此约束上动能变换与二维完全一样：$|d\vec x|^2 = 4r\,|d\vec u|^2$。代价是多出来的第四维：变换 $w_i \to e^{i\theta}w_i$（两平面同向旋转）保持 $\vec x$ 不变，所以每个 $\vec x$ 的原像是一个圆周——**三维 Kepler 问题 $\equiv$ 带一个 U(1) 约束的四维各向同性谐振子**。约束在量子版本里如何处理，第 4.5 节按结论使用（承认的一步之一）。

## 4. Duru–Kleinert（1979）：量子通关

### 4.1 把 $E$ 塞进指数

传播子（第 07 篇 2.2 节，$V = -e^2/r$）：

$$K(\vec x_b, \vec x_a; T) = \int \mathcal{D}x\ \exp\Big\{ \frac{i}{\hbar}\int_0^T dt\ \Big[ \frac{m_e}{2}\dot{\vec x}^{\,2} + \frac{e^2}{r} \Big] \Big\} .$$

代入定能格林函数的定义，把 $e^{iET/\hbar} = \exp\{(i/\hbar)\int_0^T dt\,E\}$ 并进作用量：

$$G(E) = \int_0^\infty dT \int \mathcal{D}x\ \exp\Big\{ \frac{i}{\hbar}\int_0^T dt\ \Big[ \frac{m_e}{2}\dot{\vec x}^{\,2} + \frac{e^2}{r} + E \Big] \Big\} .$$

指数现在是 "$H \to H - E$" 的作用量，三项各就各位：动能、常数乘 $1/r$、常数。手术开始。

### 4.2 赝时 + 平方根坐标：逐项变换

对每条路径引入它自己的赝时 $dt = r\,ds$，总赝时长 $S = \int_0^T dt/r$。逐路径 $T \leftrightarrow S$ 单调，且 $dT/dS = r(S) = r_b$——终点固定，所以 $T$ 积分换成 $S$ 积分只多一个常数因子 $r_b$。三项的变换（二维，用 3.2 节的 Levi-Civita）：

- **动能**：$\dfrac{m_e}{2}|\dot{\vec x}|^2\,dt = \dfrac{m_e}{2}\dfrac{|\vec x\,'|^2}{r^2}\,r\,ds = \dfrac{m_e}{2r}\cdot 4r\,|\vec u\,'|^2\,ds = 2m_e|\vec u\,'|^2\,ds$；
- **库仑项**：$\dfrac{e^2}{r}\,dt = e^2\,ds$——奇异的势变成了**常数**；
- **能量项**：$E\,dt = E\,r\,ds = E\,\vec u^{\,2}\,ds$——常数变成了**二次型势**。

合起来：

$$G(E) \;\propto\; \int_0^\infty dS\ e^{ie^2S/\hbar}\,K_{\mathrm{osc}}(\vec u_b, \vec u_a; S),$$

$$K_{\mathrm{osc}}(S) = \int \mathcal{D}u\ \exp\Big\{ \frac{i}{\hbar}\int_0^S ds\ \Big[ \frac{\mu}{2}|\vec u\,'|^2 - \frac{1}{2}\mu\omega^2 \vec u^{\,2} \Big] \Big\}, \qquad \mu = 4m_e,\quad \omega^2 = -\frac{E}{2m_e} .$$

库仑路径积分变成了谐振子路径积分——第 07 篇第 5 节意义上完全已知的高斯对象。注意一个免费的副产品：$E < 0$ 时 $\omega$ 为实数（正常振子，有离散谱），$E > 0$ 时 $\omega^2 < 0$（倒摆，无极点）——**束缚谱与连续谱的分野自动出现**。

### 4.3 承认的一步：Duru–Kleinert 恒等式

上面把 4.2 的形式结果写成

$$G(\vec x_b, \vec x_a; E) = (\text{端点因子})\times\int_0^\infty dS\ e^{ie^2S/\hbar}\,K_{\mathrm{osc}}(\vec u_b, \vec u_a; S)\ (\text{并对原像求和})$$

时，有两处本篇**承认引用**、不在此证明：

1. **测度变换**：$\mathcal{D}x \to \mathcal{D}u$ 在格点上要做中点处方（midpoint prescription），会产出额外的 $O(\hbar^2)$ 有效势项。著名的结论是：三维库仑问题中这一项恰好为零；二维情形则被下面"覆盖空间求和"的严格处理自动吸收。
2. **端点因子**：$r_a$、$r_b$ 的幂次（来自 $dT/dS$ 与测度雅可比）。它们影响留数（波函数），**不影响极点位置**——而本篇只提取谱。

此外二维映射是二对一的：$\vec u$ 与 $-\vec u$ 是同一个 $\vec x$。坐标空间传播子是两张"叶"之和 $K_x = K_u(\vec u_b, \vec u_a) + K_u(\vec u_b, -\vec u_a)$，即只保留振子的**偶宇称态**。完整的格点证明见 Kleinert 书的库仑系统专章；从这里往下的一切推导都是严格的。

### 4.4 极点读谱：二维做透

振子传播子有谱分解（二维各向同性振子，$\epsilon_{n_1n_2} = \hbar\omega(n_1 + n_2 + 1)$）：

$$K_{\mathrm{osc}}(S) = \sum_{n_1, n_2} \phi_{n_1n_2}(\vec u_b)\,\phi_{n_1n_2}^*(\vec u_a)\,e^{-i\epsilon_{n_1n_2}S/\hbar} .$$

原像求和 $\phi(\vec u) \to \phi(\vec u) + \phi(-\vec u)$ 投影掉奇宇称态：$\vec u \to -\vec u$ 的宇称为 $(-1)^{n_1+n_2}$，故只有 $n_1 + n_2$ 为偶的项存活，即 $N \equiv n_1 + n_2 + 1$ 为**奇数**。对 $S$ 积分（用 2.3 节同一积分）：

$$\int_0^\infty dS\ e^{i(e^2 - \epsilon_N)S/\hbar} = \frac{i\hbar}{e^2 - \epsilon_N + i0},$$

极点条件 $e^2 = \hbar\omega(E)\,N$。代入 $\omega^2 = -E/(2m_e)$ 解出 $E = -2m_e\omega^2$：

$$e^2 = \hbar N\sqrt{\frac{-E}{2m_e}} \qquad\Longrightarrow\qquad E_N = -\frac{2m_ee^4}{\hbar^2N^2}, \qquad N = 1, 3, 5, \dots$$

写 $N = 2n - 1$：

$$\boxed{E_n = -\frac{2m_ee^4}{\hbar^2(2n-1)^2} = -\frac{m_ee^4}{2\hbar^2\big(n - \tfrac12\big)^2}, \qquad n = 1, 2, 3, \dots}$$

**不要慌——这正是二维氢原子的正确谱**（二维库仑束缚态本来就是半整数的，简并度 $2n-1$；我们的计数：$n_1+n_2 = 2n-2$ 层全部偶宇称，共 $2n-1$ 个态，也对上）。二维计算至此完全做透，且每一步都严格。三维的整数谱藏在 Kustaanheimo–Stiefel 里。

### 4.5 三维：结论与 $n^2$ 简并

同样的机器装上 KS 变换（3.3 节）：动能变换相同，$\mu = 4m_e$、$\omega^2 = -E/(2m_e)$ 不变，只是振子升为四维各向同性，$\epsilon_{N'} = \hbar\omega(N' + 2)$，$N' = n_1 + n_2 + n_3 + n_4$。约束的量子化版本（承认按结论使用）：每个 $\vec x$ 的原像圆周由 U(1) 相位 $w_i \to e^{i\theta}w_i$ 扫出，对圆周积分把物理振幅投影到该 U(1) 的**零电荷扇区**。电荷是圆偏振量子的计数：$Q = m_A + m_B$，其中 $m_A$、$m_B$ 分别是 $(u_1, u_2)$ 与 $(u_3, u_4)$ 两个二维振子的角动量量子数。由于 $m_A \equiv n_A \pmod 2$ 等，$Q \equiv N' \pmod 2$，所以 $Q = 0$ **自动只放行偶数** $N'$：

$$N' = 2n - 2, \qquad n = 1, 2, 3, \dots$$

极点条件 $e^2 = \hbar\omega\,(N' + 2) = 2n\,\hbar\omega$，于是 $E = -2m_e\omega^2$ 给出

$$\boxed{E_n = -\frac{2m_ee^4}{\hbar^2(2n)^2} = -\frac{m_ee^4}{2\hbar^2n^2}}$$

玻尔能级，一个系数都不差（对照 第 06 篇 的 $E_n = -Z^2\hbar^2/(2m_ea_0^2n^2)$ 取 $Z=1$、$a_0 = \hbar^2/(m_ee^2)$）。简并计数：$N' = 2n-2$ 层里满足 $m_A + m_B = 0$ 的态数恰好是 $n^2$（组合细节留自检问题 5）——库仑隐藏对称性的 $n^2$ 简并，在这里是四维振子的简并被约束筛剩下的部分，与 第 06 篇 的 SO(4) 账本是同一笔账。

## 5. 收尾：同一谱的第四种推法

氢原子能谱现在是本仓库里被推导次数最多的公式：

- **波动力学**（[第 06 篇](06-hydrogen-and-subshells.md)）：径向级数的归一化截断给出 $n$；
- **矩阵力学**（[第 06s 篇](06s-hydrogen-matrix-mechanics.md)，与本篇同期）：Runge–Lenz 矢量的 SO(4) 代数直接读出谱；
- **路径积分**（本篇）：定能格林函数 + Duru–Kleinert 变换，振子极点给出谱；
- **相对论**：本书 [第 06s2 篇](06s2-dirac-hydrogen.md) 给出含精细结构修正 $\alpha^4$ 的精确谱。

每种新表述都拿氢原子当验收测试，这不是巧合：库仑谱是量子理论最精确已知的非平凡数据。但四种推法的地位不平等——**只有路径积分这一种能原样推广到场论**。库仑传播子本身此后几乎不再出现，真正的遗产是方法论：用时间重参数化加变量替换驯服奇异相互作用（这个思想后来在弦论的世界线表述和各类非微扰路径积分里反复转世），以及"$G(E)$ 的极点 = 谱"这条从路径积分提取物理的标准流水线。第 07 篇第 9 节说路径积分是 QFT 的母语——本篇是它的第一份艰难但完整的口译作业。

## 小结

| 步骤 | 操作 | 效果 |
| --- | --- | --- |
| 定能化 | $G(E) = \int_0^\infty dT\,e^{iET/\hbar}K(T)$ | $H \to H - E$；束缚谱 = $G$ 的极点 |
| Sundman | $dt = r\,ds$ | 库仑项变常数 $e^2$；$E$ 项变 $r$ 型势 |
| Levi-Civita / KS | $r = \lvert\vec u\rvert^2$（2D/4D） | 动能变标准二次型；$-E\vec u^{\,2}$ = 振子势 |
| 极点条件 | $\hbar\omega\,\nu = e^2$，$\omega^2 = -E/(2m_e)$ | $\nu$ 由约束筛选：2D 奇 $N$，3D $N'+2 = 2n$ |

- 病根：$1/r$ 奇点 + 布朗路径 $\Rightarrow$ 朴素切片测度不受控；算符 $H$ 本身没病，病在路径积分构造。
- 二维严格做透：$E_n = -m_ee^4/\big(2\hbar^2(n-\tfrac12)^2\big)$，正是二维氢原子的正确半整数谱。
- 三维玻尔谱 $E_n = -m_ee^4/(2\hbar^2n^2)$ 与 $n^2$ 简并全部还原；承认引用的只有测度/端点因子与 KS 约束投影两处，均不影响极点位置。
- 这是同一能谱的第四种推法，也是唯一能带进量子场论的一种。

## 自检问题

**1.** 用有效势分析说明为什么经典上存在坠入 $r = 0$ 的轨道（定量证明坠落时间有限），并解释朴素路径积分的病态究竟出在哪一步——为什么对光滑势成立的切片论证在库仑势下失效？

<details markdown="1"><summary>点击显示答案</summary>

**经典部分**：$L = 0$ 时 $V_{\mathrm{eff}} = -e^2/r$，无离心垒，径向方程给出 $\dot r = -\sqrt{(2/m_e)(E + e^2/r)}$。坠落时间

$$\tau = \int_0^{r_0} \frac{dr}{\sqrt{\frac{2}{m_e}\big(E + \frac{e^2}{r}\big)}}$$

在 $r \to 0$ 处被积函数 $\sim \sqrt{m_er/(2e^2)}$，$\sqrt{r}$ 可积，故 $\tau$ 有限（$E = 0$ 时 $\tau = \tfrac{2}{3}\sqrt{m_e/(2e^2)}\,r_0^{3/2}$）。同时 $\lvert\dot r\rvert \sim r^{-1/2} \to \infty$：轨道在有限时间内以无穷速度到达奇点，牛顿方程无法续接——经典动力学不完备。

**路径积分部分**：切片论证的两个支柱都断了。其一，单个切片的势相位 $\epsilon V/\hbar = -\epsilon e^2/(\hbar r)$ 对光滑势随 $\epsilon \to 0$ 一致消失，但典型路径是布朗型的（$\lvert\Delta x\rvert \sim \sqrt{\epsilon}$），以不为零的权重穿过 $r \sim \epsilon e^2/\hbar$ 的细管，那里相位是 $O(1)$；其二，命中概率每切片 $\sim \epsilon$，乘以 $N \sim 1/\epsilon$ 个切片后，$O(1)$ 比例的路径带着不受控的贡献进入连续极限。此外 $V$ 的导数在原点发散，BCH 拆分 $e^{-i\epsilon H} \approx e^{-i\epsilon T}e^{-i\epsilon V}$ 的 $O(\epsilon^2)$ 误差估计失效。所以病态不在"积分难算"，而在**测度的连续极限根本不受控**——必须换对象（$G(E)$）加换变量（DK 变换）。

</details>

**2.** 逐步验证二维 Levi-Civita 变换与 Sundman 赝时的组合，把定能作用量映成谐振子形式：即从 $(i/\hbar)\int dt\,\big[\tfrac{m_e}{2}\lvert\dot{\vec x}\rvert^2 + e^2/r + E\big]$ 推出 $(i/\hbar)\int ds\,\big[2m_e\lvert\vec u\,'\rvert^2 + E\vec u^{\,2} + e^2\big]$，并读出振子的质量与频率。

<details markdown="1"><summary>点击显示答案</summary>

**Levi-Civita 动能**：$z = w^2 \Rightarrow dz = 2w\,dw$，故

$$|dz|^2 = 4|w|^2|dw|^2 = 4r\,\big(du_1^2 + du_2^2\big).$$

**Sundman**：$dt = r\,ds$，故 $\dot{\vec x} = \vec x\,'/r$。三项分别变换：

$$\frac{m_e}{2}|\dot{\vec x}|^2\,dt = \frac{m_e}{2}\cdot\frac{|\vec x\,'|^2}{r^2}\cdot r\,ds = \frac{m_e}{2r}\cdot 4r\,|\vec u\,'|^2\,ds = 2m_e\,|\vec u\,'|^2\,ds,$$

$$\frac{e^2}{r}\,dt = \frac{e^2}{r}\cdot r\,ds = e^2\,ds,$$

$$E\,dt = E\,r\,ds = E\,\vec u^{\,2}\,ds .$$

求和即得 $(i/\hbar)\int ds\,\big[2m_e\lvert\vec u\,'\rvert^2 + E\vec u^{\,2} + e^2\big]$。与标准振子拉氏量 $\tfrac{\mu}{2}\lvert\vec u\,'\rvert^2 - \tfrac12\mu\omega^2\vec u^{\,2}$ 对照：$\mu = 4m_e$，$\tfrac12\mu\omega^2 = -E$，即

$$\omega^2 = -\frac{2E}{\mu} = -\frac{E}{2m_e},$$

束缚态 $E < 0$ 给出实频率；常数 $e^2$ 作为整体相位 $e^{ie^2S/\hbar}$ 提出。注意这个"频率"量纲古怪（$u$ 的量纲是长度的平方根）——它是形式参数，只有乘积 $\hbar\omega$（量纲：能量 × 长度，与 $e^2$ 相同）进入物理条件。

</details>

**3.** 从四维振子传播子的谱分解出发，补全由极点结构推出三维玻尔能级的推导：写出 $G(E)$ 的极点条件，代入频率与能量的关系，并说明约束如何把 $N'$ 筛成 $2n-2$。

<details markdown="1"><summary>点击显示答案</summary>

**谱分解**：四维各向同性振子 $K_{\mathrm{osc}}(S) = \sum_{\{n_i\}} \phi(\vec u_b)\phi^*(\vec u_a)\,e^{-i\epsilon S/\hbar}$，$\epsilon_{N'} = \hbar\omega\big(\sum_{i=1}^4 n_i + 2\big) = \hbar\omega(N'+2)$。

**约束筛选**：物理振幅对 KS 原像圆周（U(1) 相位 $w_i \to e^{i\theta}w_i$）积分，只保留电荷 $Q = m_A + m_B = 0$ 的态，其中 $m_A, m_B$ 是两对平面的圆偏振角动量。圆偏振量子数满足 $m_A = n_+^A - n_-^A \equiv n_A \pmod 2$，同理 $m_B \equiv n_B \pmod 2$，故 $Q \equiv n_A + n_B = N' \pmod 2$：$Q = 0$ 迫使 $N'$ 为偶数，写 $N' = 2n - 2$（$n = 1, 2, \dots$）。

**极点条件**：$G(E) \propto \int_0^\infty dS\,e^{i(e^2-\epsilon)S/\hbar} = i\hbar/(e^2 - \epsilon + i0)$，极点在

$$e^2 = \hbar\omega(E)\,(N'+2) = 2n\,\hbar\omega .$$

**解出能量**：由 $\omega^2 = -E/(2m_e)$ 得 $E = -2m_e\omega^2$，而 $\omega = e^2/(2n\hbar)$，故

$$E_n = -2m_e\cdot\frac{e^4}{4n^2\hbar^2} = -\frac{m_ee^4}{2\hbar^2n^2} = -\frac{13.6\ \text{eV}}{n^2}.$$

与 第 06 篇 的波动力学结果逐系数一致——$Z=1$、$a_0 = \hbar^2/(m_ee^2)$ 代入即见。

</details>

**4.** 证明 Sundman 重参数化 $dt = r\,ds$ 不改变经典运动方程的轨道内容：同一批空间曲线，只是时间表不同。

<details markdown="1"><summary>点击显示答案</summary>

**双射性**：沿任何 $r > 0$ 的轨道 $dt/ds = r > 0$，故 $t(s)$ 严格单调、可逆——两条参数化描出**同一条几何曲线**，只是行经各点的时刻不同。

**第一积分对应**：角动量在两种参数下是同一个量，

$$L = m_er^2\dot\varphi = m_er^2\cdot\frac{\varphi'}{r} = m_e r\,\varphi',$$

守恒性不因参数化改变。能量第一积分 $(m_e/2)\dot r^2 + V_{\mathrm{eff}} = E$ 在 $s$ 参数下变为 $(m_e/2r)r'^2 + V_{\mathrm{eff}} = E$——同一方程乘 $r$ 后的重写。

**轨道方程**：轨道内容指 $r(\varphi)$。消去参数：

$$\frac{dr}{d\varphi}\Big|_t = \frac{\dot r}{\dot\varphi}, \qquad \frac{dr}{d\varphi}\Big|_s = \frac{r'}{\varphi'} = \frac{r\dot r}{r\dot\varphi} = \frac{\dot r}{\dot\varphi},$$

两者逐点相同，故 $r(\varphi)$ 满足同一微分方程、给出同一批圆锥曲线。改变的是**时间表**：$s$ 时钟在近日点走得慢，把 2.1 节的碰撞奇点（$t$ 参数下有限时间、无穷速度）拉成 $s$ 参数下的光滑经过（$r' \sim \sqrt{r} \to 0$）。这正是"正则化"一词的经典含义：运动方程的解集不变，奇点从参数化里消失。

</details>

**5.** 从四维各向同性振子出发做简并计数：证明 $N' = 2n-2$ 能级中满足 KS 约束 $Q = m_A + m_B = 0$ 的态数恰好是 $n^2$，并指出这与 第 06 篇 里 $n^2$ 简并的关系。

<details markdown="1"><summary>点击显示答案</summary>

**设定**：把四维振子分成两个二维振子 $A = (u_1,u_2)$（$n_A$ 个量子）与 $B = (u_3,u_4)$（$n_B$ 个量子），$n_A + n_B = N' = 2n-2$。二维振子 $k$ 个量子的角动量取值为 $m = -k, -k+2, \dots, k$（共 $k+1$ 个，步长 2 来自圆偏振分解 $m = n_+ - n_-$）。约束要求 $m_A = -m_B$。

**计数**：固定 $n_A = k$（则 $n_B = 2n-2-k$），可行的 $m_A$ 需同时满足 $\lvert m_A\rvert \le k$ 与 $\lvert m_A\rvert \le n_B$，且奇偶性与两者相容（$m_A \equiv k \equiv n_B \pmod 2$，自动满足）——共 $\min(k, 2n-2-k) + 1$ 个。对 $k$ 求和：

$$\sum_{k=0}^{2n-2}\big[\min(k,\,2n-2-k) + 1\big] = \underbrace{\big[1 + 2 + \cdots + n\big]}_{k = 0 \dots n-1} + \underbrace{\big[(n-1) + \cdots + 1\big]}_{k = n \dots 2n-2} = \frac{n(n+1)}{2} + \frac{n(n-1)}{2} = n^2.$$

**群论读法**：四维振子的旋转对称性是 $\mathrm{SO}(4) \simeq \mathrm{SU}(2)\times\mathrm{SU}(2)$；$N' = 2n-2$ 层的约束本征态正好组成表示 $(j, j)$，$j = (n-1)/2$，维数 $(2j+1)^2 = n^2$。这就是 第 06 篇 里由 Runge–Lenz 矢量保证的库仑 $n^2$ 简并——那里它是隐藏对称性的结论，这里它是振子简并被 KS 约束筛剩下的部分，两笔账完全对上（第 06s 篇则从代数侧给出第三份对账）。

</details>

## 参考

- Kleinert《Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets》库仑系统专章（第五版第 13 章）：Duru–Kleinert 变换的完整格点证明、测度修正与任意维处理——本篇"承认"的两步都在这里补齐。
- Duru & Kleinert, Phys. Lett. B 84, 185 (1979)：原始论文（定能格林函数 + 赝时变换的首秀）；后续详述见 Fortschr. Phys. 30, 401 (1982)。
- Feynman & Hibbs《Quantum Mechanics and Path Integrals》：只含二次型体系与微扰展开——库仑传播子缺位的现场，对应本篇第 2 节。
- Schulman《Techniques and Applications of Path Integration》库仑问题相关章：格林函数技术与 Kustaanheimo–Stiefel 变换的另一表述。
- 经典正则化原始文献：Sundman (1912) 碰撞奇点；Kustaanheimo & Stiefel, J. Reine Angew. Math. 218, 204 (1965)。
