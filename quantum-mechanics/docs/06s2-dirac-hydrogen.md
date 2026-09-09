# Dirac 方程精确解氢原子——精细结构从哪来

> 路线图位置：量子力学书 · 第二部分（可精确求解的体系）· 第 06s2 篇——QFT 书 [Klein–Gordon 方程与 Dirac 方程](../../qft-sm/docs/stage-03-relativistic-qm/01-klein-gordon-and-dirac.md) 篇（下称"KG/Dirac 篇"）的兑现篇——那里（4.4 节）说 Dirac 方程"自动给出正确的氢原子精细结构"，本篇把这句话算出来。
> 前置知识：KG/Dirac 篇（Dirac 方程、$\gamma$ 矩阵、旋量）；[第 05 篇](05-angular-momentum.md)（角动量相加）；[第 06 篇 氢原子与电子亚层](06-hydrogen-and-subshells.md)（非相对论库仑问题、$\alpha^2$ 能标）；[第 07 篇 微扰论](07-perturbation-theory.md)（第 6 节对照用）。
> 学习目标：会写库仑场中的 Dirac 哈密顿量并找出全部好量子数（$\vec J$、$K$ 取代 $\vec L$）；会从两个耦合径向方程出发，经级数截断推出精确谱（Sommerfeld–Dirac 公式）；会把它展开到 $(Z\alpha)^4$ 阶并逐项读出 Bohr 能级与精细结构；说清楚 Dirac 理论里 $2s_{1/2}$ 与 $2p_{1/2}$ 为何仍简并、这扇留给 Lamb 位移的门在哪。
>
> 记号约定：本篇用自然单位 $\hbar = c = 1$（首次出现，见下方说明），度规 $\eta = \mathrm{diag}(+1,-1,-1,-1)$，与KG/Dirac 篇一致。**记号冲突警告**：Dirac 矩阵 $\alpha^i$ 与精细结构常数 $\alpha$ 撞名——本篇 Dirac 矩阵一律写粗体 $\boldsymbol\alpha = (\alpha^1,\alpha^2,\alpha^3)$，精细结构常数写细体 $\alpha \approx 1/137$；库仑势 $V(r) = -Z\alpha/r$。

<details markdown="1"><summary>补充说明：自然单位制</summary>

本篇设 $\hbar = c = 1$：能量、动量、质量同量纲，长度是能量的倒数。恢复常数的窍门：组合 $mc^2$（静能）、$\hbar/mc$（康普顿波长）、$e^2/(4\pi\varepsilon_0\hbar c) = \alpha$。例如谱公式里的 $m(Z\alpha)^2/2$ 恢复后是 $mc^2(Z\alpha)^2/2 = Z^2 \times 13.6$ eV（$Z=1$ 时），与 第 06 篇 的记号接上。

</details>

---

## 1. 一句话总结

**把电子放进库仑势 $V = -Z\alpha/r$ 的 Dirac 方程可以精确求解：轨道角动量 $\vec L$ 不再守恒，守恒的是总角动量 $\vec J = \vec L + \vec S$ 和一个新算符 $K = \beta(\vec\Sigma\cdot\vec L + 1)$（本征值 $k = \mp(j+\tfrac12)$），态按 $(n, j, k)$ 分类；径向波函数分成大小两个分量 $F, G$，满足两个耦合的一阶方程，束缚态边界条件再次以"级数必须截断"的形式出现，截断条件直接给出精确谱 $E = m\big[1 + (Z\alpha)^2/\big(n_r + \sqrt{(j+\frac12)^2 - (Z\alpha)^2}\big)^2\big]^{-1/2}$——展开到 $(Z\alpha)^4$ 阶，前两项正是 Bohr 能级加精细结构分裂，且能量只依赖 $(n, j)$，$2s_{1/2}$ 与 $2p_{1/2}$ 依然简并，这道裂缝要等 QED 的 Lamb 位移来撬开。**

## 2. 问题的设置：库仑场中的 Dirac 哈密顿量

KG/Dirac 篇的自由 Dirac 哈密顿量加上中心库仑势（原子核电荷 $+Ze$，电子电荷 $-e$，高斯单位下 $e^2 = 4\pi\alpha$）：

$$H = \boldsymbol\alpha\cdot\vec p + \beta m + V(r), \qquad V(r) = -\frac{Z\alpha}{r}, \qquad \vec p = -i\nabla,$$

其中 $\boldsymbol\alpha^i = \begin{pmatrix} 0 & \sigma^i \\ \sigma^i & 0 \end{pmatrix}$、$\beta = \begin{pmatrix} I & 0 \\ 0 & -I \end{pmatrix}$（Dirac 基，见KG/Dirac 篇 4.2 节），$\sigma^i$ 是泡利矩阵。任务：解定态方程 $H\psi = E\psi$ 的束缚态。

**为什么不用 KG 方程？** 两个理由。其一，电子是自旋 $1/2$ 粒子，KG 方程描述无自旋场，氢光谱里自旋效应（谱线双线）就在实验数据里摆着；其二，KG 方程解库仑问题的确也给出一个 $\alpha^4$ 阶的 $l$ 相关分裂，但它没有自旋轨道耦合，分裂结构对不上实验——这正是 第 06 篇 末尾"精细结构留给 Dirac 方程"那句欠账的内容。第 06 篇 还给了能标账本：Bohr 能级 $\sim m\alpha^2 \approx 13.6$ eV，相对修正 $\sim v^2 \sim \alpha^2$ 即 $(Z\alpha)^4 m \sim 10^{-3}$ eV——要算这个量级，非相对论框架不够，必须让 Dirac 方程亲自上场。

## 3. 好量子数：$\vec L$ 死了，$\vec J$ 与 $K$ 活着

### 3.1 $\vec L$ 单独不守恒：自旋轨道耦合的起源

非相对论库仑问题里 $\vec L$ 守恒是分离变量的地基（第 06 篇 第 2.1 节）。现在地基塌了：用 $[p_j, L_i] = -i\epsilon_{jim}p_m$ 直接算（自检问题 1），

$$[H, L_i] = -i(\boldsymbol\alpha\times\vec p)_i \neq 0.$$

物理意义：Dirac 哈密顿量里速度算符是 $\boldsymbol\alpha$ 而不是 $\vec p/m$，电子的"运动"自带内禀结构，轨道角动量不再单独守恒。但定义自旋 $\vec S = \vec\Sigma/2$，$\vec\Sigma = \begin{pmatrix} \vec\sigma & 0 \\ 0 & \vec\sigma \end{pmatrix}$，则

$$[H, \vec S] = +i\,\boldsymbol\alpha\times\vec p, \qquad\Longrightarrow\qquad [H, \vec J] = 0, \quad \vec J = \vec L + \vec S.$$

**总角动量守恒，轨道与自旋各自不守恒、互相吞吐**——这就是自旋轨道耦合在 Dirac 理论里的原初形态：它不是外加的修正项，而是哈密顿量对称性的直接陈述。于是 $j, m_j$ 是好量子数，$l$ 只是近似好量子数。

### 3.2 算符 $K$：把 $(l, j)$ 打包成一个数

中心势问题还差一个径向量子数的"标签"。定义

$$K = \beta\big(\vec\Sigma\cdot\vec L + 1\big).$$

两条关键性质（推导见自检问题 2）：

$$[H, K] = 0, \qquad K^2 = J^2 + \frac14.$$

第二条立刻给出本征值：$K^2$ 的本征值是 $j(j+1) + \tfrac14 = (j+\tfrac12)^2$，所以

$$k = \mp\left(j + \frac12\right), \qquad \lvert k\rvert = j + \frac12 = 1, 2, 3, \dots$$

$k$ 是非零整数，一个数同时编码 $j$ 和 $l$（从而编码宇称与"自旋顺着还是逆着轨道"）。对应关系：

| 态 | $l$ | $j$ | $k$ | 解读 |
| --- | --- | --- | --- | --- |
| $s_{1/2}$ | 0 | 1/2 | $-1$ | $j = l + 1/2$ |
| $p_{1/2}$ | 1 | 1/2 | $+1$ | $j = l - 1/2$ |
| $p_{3/2}$ | 1 | 3/2 | $-2$ | $j = l + 1/2$ |
| $d_{3/2}$ | 2 | 3/2 | $+2$ | $j = l - 1/2$ |
| $d_{5/2}$ | 2 | 5/2 | $-3$ | $j = l + 1/2$ |

规律：$k < 0$ 即 $j = l + \tfrac12$（自旋与轨道"平行"），此时 $k = -(l+1)$；$k > 0$ 即 $j = l - \tfrac12$，此时 $k = l$。两条公式合成 $k(k+1) = l(l+1)$——第 4.3 节非相对论极限里它会现身说法。以后态就按 $(E, j, m_j, k)$ 标记。

## 4. 径向方程：大小分量

### 4.1 球面旋量分离变量

角向部分用"球面旋量" $\Omega_{jlm}(\hat r)$：$Y_l^m$ 与两分量自旋按角动量相加耦合成 $J^2, J_z$ 本征态（第 05 篇的 Clebsch–Gordan 机器）。四分量旋量取如下形式：

$$\psi = \begin{pmatrix} \dfrac{F(r)}{r}\,\Omega_{j l m} \\[6pt] i\,\dfrac{G(r)}{r}\,\Omega_{j l' m} \end{pmatrix},$$

其中上下两个分量的轨道角动量 $l, l'$ 相差 1（$\boldsymbol\alpha$ 是宇称奇的，必然把两个宇称相反的分量耦合起来）；对给定的 $k$，一个分量取 $l$、另一个取 $l' = 2j - l$。$F, G$ 是无量纲的**约化径向函数**（对应 第 06 篇 里 $u = rR$ 的角色）。

### 4.2 两个耦合的一阶径向方程

把上式代入 $H\psi = E\psi$，用 $\vec\sigma\cdot\vec p$ 对球面旋量的标准作用（$\vec\sigma\cdot\vec p = \vec\sigma\cdot\hat r\,\big(\partial_r - \vec\sigma\cdot\vec L/r\big)$ 之类的恒等式，角向代数全部吃进 $k$），得到：

$$\frac{dF}{dr} = -\frac{k}{r}F + \big(E + m - V\big)\,G,$$

$$\frac{dG}{dr} = +\frac{k}{r}G - \big(E - m - V\big)\,F,$$

其中 $V = -Z\alpha/r$。两个一阶方程取代了一个二阶方程——Dirac 方程"时空都只要一阶"的代价在这里变现：$F$ 与 $G$ 互为对方的"源"。注意 $E+m$ 乘 $G$、$E-m$ 乘 $F$ 的不对称：正能态 $E \approx m$ 时 $E - m$ 很小，$G$ 被压小——**$F$ 是大分量，$G$ 是小分量**，比例 $\sim v$。

### 4.3 非相对论极限：回到 第 06 篇

写 $E = m + E_{\text{NR}}$（$\lvert E_{\text{NR}}\rvert \ll m$），则 $E + m - V \approx 2m$，第一个方程给出

$$G \approx \frac{1}{2m}\left(\frac{d}{dr} + \frac{k}{r}\right)F \;\sim\; \frac{1}{2m}\,\vec\sigma\cdot\vec p\,F,$$

即小分量是大分量的 $p/2m \sim v$ 倍。代入第二个方程消去 $G$（详细代数见自检问题 5）：

$$-\frac{1}{2m}\frac{d^2F}{dr^2} + \left[\frac{k(k+1)}{2mr^2} + V(r)\right]F = E_{\text{NR}}\,F.$$

由第 3.2 节的账本 $k(k+1) = l(l+1)$，这正是 第 06 篇 第 2.1 节对 $u = rR$ 的薛定谔径向方程，离心垒原样归还。**Dirac 理论的非相对论极限不是"丢掉 $G$"，而是"小分量由大分量微分生成"**——$G \approx \vec\sigma\cdot\vec p\,F/2m$ 这个关系后面在 QED 里还有长远影响（如电磁耦合的 $g=2$）。

## 5. 级数解与量子化：截断再现

结构与 第 06 篇 第 2.2 节完全平行：两端渐近 → 级数递推 → 不截断就发散 → 截断条件即谱公式。

### 5.1 两端渐近

**$r \to \infty$**：束缚态 $E < m$，方程中常数项主导，$F, G \sim e^{-\lambda r}$，其中

$$\lambda = \sqrt{m^2 - E^2} \;>\; 0.$$

**$r \to 0$**：$1/r$ 项（离心项与库仑项）主导。设 $F, G \sim r^s$，代入径向方程只留 $1/r$ 阶，得线性方程组

$$(s + k)\,F_0 - Z\alpha\,G_0 = 0, \qquad Z\alpha\,F_0 + (s - k)\,G_0 = 0,$$

有非零解要求行列式为零：

$$s^2 = k^2 - (Z\alpha)^2, \qquad s = +\sqrt{k^2 - (Z\alpha)^2}$$

（取正根保证 $r \to 0$ 温和；$\lvert k\rvert = 1$ 的负根其实平方可积，但那里方程的解不自伴，物理上仍取正根，这里不展开）。**注意 $(Z\alpha)^2$ 混进了有效离心项**——库仑奇性被相对论"软化"，这正是第 6.3 节 $Z\alpha > 1$ 病态的源头。

### 5.2 级数递推与截断条件

提掉渐近因子，记 $\rho = 2\lambda r$，设

$$F = e^{-\rho/2}\rho^{\,s}\sum_{j\ge0} a_j\rho^j, \qquad G = e^{-\rho/2}\rho^{\,s}\sum_{j\ge0} b_j\rho^j.$$

代入径向方程，比较 $\rho^{s+j-1}$ 的系数，得联立递推（$a_{-1} = b_{-1} = 0$）：

$$(s + j + k)\,a_j - Z\alpha\,b_j = \tfrac12 a_{j-1} + \frac{E+m}{2\lambda}\,b_{j-1},$$

$$Z\alpha\,a_j + (s + j - k)\,b_j = \frac{m - E}{2\lambda}\,a_{j-1} + \tfrac12 b_{j-1}.$$

**发散论证**（与 第 06 篇 同一句台词）：大 $j$ 时左边系数阵的行列式 $= j(2s + j) \sim j^2$，解出 $a_j \sim \tfrac{1}{2j}\big(a_{j-1} + \sqrt{\tfrac{m+E}{m-E}}\,b_{j-1}\big)$，两个级数都按 $1/j$ 递推——正是 $e^{+\rho}$ 的系数行为，$F, G \sim e^{+\rho/2}$ 指数发散，不可归一化。

**截断条件**：唯一活路是两个级数在同一阶 $j = n_r$ 同时终止：$a_{n_r+1} = b_{n_r+1} = 0$。把终止条件代回递推（组合两式消去 $a_{n_r-1}, b_{n_r-1}$，代数见自检问题 3 的提示与 第 06 篇 的平行结构），得到干净的量子化条件：

$$\frac{Z\alpha\,E}{\lambda} = n_r + s, \qquad n_r = 0, 1, 2, \dots$$

### 5.3 精确谱：Sommerfeld–Dirac 公式

由 $\lambda^2 = m^2 - E^2$ 解出 $E$：

$$\boxed{E = m\left[1 + \frac{(Z\alpha)^2}{\left(n_r + \sqrt{k^2 - (Z\alpha)^2}\right)^2}\right]^{-1/2}}, \qquad k^2 = \left(j + \tfrac12\right)^2.$$

定义**主量子数**

$$n = n_r + \lvert k\rvert = 1, 2, 3, \dots$$

（一个附注：$n_r = 0$ 只允许 $k < 0$——截断关系与指标方程联立会要求 $s + k < 0$，这只在 $k<0$ 时成立；所以"无径向节点"的态恰好是 $j = n - \tfrac12$ 的那一串：$1s_{1/2}, 2p_{3/2}, 3d_{5/2}, \dots$，对应旧量子论的"圆轨道"。）

$E$ 只通过 $k^2$ 依赖角动量——**只依赖 $j$，不单独依赖 $l$**。这一条就是精细结构简并的精确陈述，第 6 节展开看。

## 6. 展开与物理：$\alpha^2$、$\alpha^4$、以及 $\alpha^4$ 的裂缝

### 6.1 展开到 $(Z\alpha)^4$

令 $x = (Z\alpha)^2$，展开 $\sqrt{k^2 - x} = \lvert k\rvert\big(1 - \frac{x}{2k^2} + \cdots\big)$，则 $n_r + s = n - \frac{x}{2\lvert k\rvert} + O(x^2)$，$(n_r+s)^{-2} = \frac{1}{n^2}\big(1 + \frac{x}{n\lvert k\rvert} + \cdots\big)$，再对总式用 $(1+y)^{-1/2} = 1 - \frac{y}{2} + \frac{3y^2}{8} - \cdots$：

$$E_{nj} = m - \frac{m(Z\alpha)^2}{2n^2} - \frac{m(Z\alpha)^4}{2n^3}\left[\frac{1}{j+\frac12} - \frac{3}{4n}\right] + O\big((Z\alpha)^6\big).$$

逐项解读：

- **第 0 项 $m$**：静能，第 06 篇 里被当作能量零点藏了起来。
- **$(Z\alpha)^2$ 项**：Bohr 能级 $-m(Z\alpha)^2/2n^2 = -Z^2 \times 13.6$ eV$/n^2$，与 第 06 篇 的 $E_n$ 精确对接（恢复 $c$ 即 $-mc^2(Z\alpha)^2/2n^2$）。
- **$(Z\alpha)^4$ 项**：**精细结构**。能量从只依赖 $n$ 升级为依赖 $(n, j)$——同一 $n$ 内不同 $j$ 裂开，量级 $\sim 10^{-3}$ eV，与 第 06 篇 末尾的能标账本分毫不差。

### 6.2 三本账对上

- **与微扰论对上**：用非相对论微扰论分三项计算——相对论动能修正 $-p^4/8m^3$、自旋轨道耦合、Darwin 项——分别依赖不同的 $(l, j)$ 组合，加起来却正好拼成同一个只含 $j$ 的结果 $\propto \big[\frac{1}{j+1/2} - \frac{3}{4n}\big]$（标准推导见 Griffiths 第 7 章；微扰论的机器本身见 [第 07 篇](07-perturbation-theory.md)，该篇提供工具但未算此例）。Dirac 方程一步给出三项之和，不多不少——这就是KG/Dirac 篇 4.4 节那句"自动给出正确的精细结构"的兑现。
- **与实验对上**：$n=2$ 内 $2p_{3/2}$ 与 $2p_{1/2}$（$=2s_{1/2}$）裂开 $m\alpha^4/32 \approx 4.53\times10^{-5}$ eV（约 10.9 GHz），与氢光谱吻合（数值计算见自检问题 4）。这是 Dirac 方程作为单粒子理论最辉煌的战果。
- **与 Sommerfeld 1916 对上**：把精确谱里的 $\lvert k\rvert = j + \tfrac12$ 换成整数方位量子数，就是 Sommerfeld 在旧量子论里用相对论椭圆轨道推出的同一个公式——半整数与整数"错位重合"，是理论史上最著名的形式巧合（来龙去脉见 [第 01 篇 旧量子论](01-old-quantum-theory.md)）。

### 6.3 两条边界：Lamb 位移与 $Z\alpha > 1$

**能量只依赖 $(n, j)$**，所以 $2s_{1/2}$ 与 $2p_{1/2}$（同 $n$、同 $j$、不同 $l$，即 $k = \mp1$）在 Dirac 理论里**严格简并**。1947 年 Lamb 测到它们裂开约 1057 MHz（$\sim \alpha^5 m$，比精细结构再小一个 $\alpha$）——库仑场中的 Dirac 方程到此为止，剩下的账属于电磁场的量子涨落：Lamb 位移是 QED 的第一场精度表演，见 QFT 书第 4 阶段的 [QED](../../qft-sm/docs/stage-04-qft-core/05-qed.md) 与 [单圈重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)。第 06 篇 那句"每破一层对称，理论就前进一个时代"，这里又破了一层。

**$Z\alpha > 1$ 的病态**（一句话带过）：$Z > 137$ 时 $\lvert k\rvert = 1$ 的态有 $s = \sqrt{1 - (Z\alpha)^2}$ 变虚，波函数在原点振荡、点核库仑势下"坠向中心"，谱公式失效——物理上由原子核有限尺寸（$\sim$ 几 fm 处势被截断）救场，这正是超重离子物理的入口。

## 小结

- 哈密顿量 $H = \boldsymbol\alpha\cdot\vec p + \beta m - Z\alpha/r$；$[H,\vec L] \neq 0$、$[H,\vec J] = 0$，自旋轨道耦合是内禀的；$K = \beta(\vec\Sigma\cdot\vec L + 1)$ 守恒，$K^2 = J^2 + \tfrac14$，$k = \mp(j+\tfrac12)$。
- 态按 $(n, j, k)$ 分类：$k<0 \Leftrightarrow j = l + \tfrac12$，$k>0 \Leftrightarrow j = l - \tfrac12$，$k(k+1) = l(l+1)$。
- 径向：大小分量 $F, G$ 两个一阶耦合方程；非相对论极限 $G \approx \vec\sigma\cdot\vec p\,F/2m$ 回到 第 06 篇 的薛定谔径向方程。

| 步骤 | 条件 | 结果 |
| --- | --- | --- |
| $r\to0$ 渐近 | 行列式为零 | $s = \sqrt{k^2 - (Z\alpha)^2}$ |
| $r\to\infty$ 渐近 | 束缚态衰减 | $\lambda = \sqrt{m^2 - E^2}$ |
| 级数截断 | $n_r + s = Z\alpha E/\lambda$ | 精确谱（Sommerfeld–Dirac 公式） |
| 展开 $(Z\alpha)^2$ | — | Bohr 能级（对接 第 06 篇） |
| 展开 $(Z\alpha)^4$ | — | 精细结构，只依赖 $(n,j)$ |

- $E$ 只依赖 $(n, j)$：$2s_{1/2}$–$2p_{1/2}$ 简并留给 Lamb 位移（QED，QFT 书第 4 阶段）；$Z\alpha > 1$ 时 $s$ 变虚，点核近似破产。

## 自检问题

**1.** 证明 $[H, \vec L] = -i\,\boldsymbol\alpha\times\vec p \neq 0$ 而 $[H, \vec J] = 0$，并说明这和"自旋轨道耦合"是什么关系。

<details markdown="1"><summary>点击显示答案</summary>

只需算 $[H, L_i] = [\boldsymbol\alpha^j p_j, L_i]$（$\beta m$ 与 $V(r)$ 都与 $\vec L$ 对易）。用 $[p_j, L_i] = [p_j, \epsilon_{ilm}x_lp_m] = -i\epsilon_{ijm}p_m$：

$$[H, L_i] = \boldsymbol\alpha^j[p_j, L_i] = -i\epsilon_{ijm}\boldsymbol\alpha^j p_m = -i(\boldsymbol\alpha\times\vec p)_i \neq 0.$$

再算自旋：$[\boldsymbol\alpha^j, \Sigma^i] = \begin{pmatrix} 0 & [\sigma^j,\sigma^i] \\ [\sigma^j,\sigma^i] & 0 \end{pmatrix} = 2i\epsilon_{jik}\boldsymbol\alpha^k$，故

$$[H, S_i] = \tfrac12 p_j[\boldsymbol\alpha^j, \Sigma^i] = i\epsilon_{jik}p_j\boldsymbol\alpha^k = +i(\boldsymbol\alpha\times\vec p)_i.$$

两式相加：$[H, J_i] = [H, L_i] + [H, S_i] = 0$。**关系**：$\vec L$ 与 $\vec S$ 的变化率恰好相反——角动量在轨道与自旋两个"账户"之间转移，只有总和守恒。非相对论语言里这叫自旋轨道耦合能；在 Dirac 理论里它不是一项额外的相互作用，而是 $H$ 的对称性结构本身（守恒荷是 $\vec J$ 而非 $\vec L$）的直接推论。

</details>

**2.** 验证 $[H, K] = 0$ 与 $K^2 = J^2 + \frac14$，其中 $K = \beta(\vec\Sigma\cdot\vec L + 1)$。

<details markdown="1"><summary>点击显示答案</summary>

**关键引理**：$\{\boldsymbol\alpha\cdot\vec p,\ \vec\Sigma\cdot\vec L + 1\} = 0$。证明：用分块乘法，$\boldsymbol\alpha^j\Sigma^i = \delta_{ji}\Gamma + i\epsilon_{jik}\boldsymbol\alpha^k$，其中 $\Gamma = \begin{pmatrix} 0 & I \\ I & 0 \end{pmatrix}$；又 $\vec p\cdot\vec L = \vec L\cdot\vec p = 0$（$\vec L = \vec r\times\vec p$ 与 $\vec p$ 垂直），故

$$\boldsymbol\alpha\cdot\vec p\;\vec\Sigma\cdot\vec L = i\epsilon_{jik}\boldsymbol\alpha^k p_jL_i, \qquad \vec\Sigma\cdot\vec L\;\boldsymbol\alpha\cdot\vec p = i\epsilon_{ijk}\boldsymbol\alpha^k L_ip_j = -i\epsilon_{jik}\boldsymbol\alpha^k L_ip_j,$$

相加得 $i\epsilon_{jik}\boldsymbol\alpha^k[p_j, L_i] = i\epsilon_{jik}\boldsymbol\alpha^k(-i\epsilon_{ijm}p_m) = -2\boldsymbol\alpha\cdot\vec p$，即引理成立。

**$[H,K]$**：$[\beta m, K] = 0$（$\beta$ 与 $\vec\Sigma\cdot\vec L$ 对易）、$[V, K] = 0$，只剩

$$[H, K] = [\boldsymbol\alpha\cdot\vec p, \beta](\vec\Sigma\cdot\vec L + 1) + \beta[\boldsymbol\alpha\cdot\vec p, \vec\Sigma\cdot\vec L] = -2\beta\,\boldsymbol\alpha\cdot\vec p\,(\vec\Sigma\cdot\vec L + 1) + \beta\cdot 2\boldsymbol\alpha\cdot\vec p\,(\vec\Sigma\cdot\vec L + 1) = 0,$$

其中第一步用了 $[\boldsymbol\alpha\cdot\vec p, \beta] = -2\beta\,\boldsymbol\alpha\cdot\vec p$，第二步用引理把对易子改写为 $2\boldsymbol\alpha\cdot\vec p(\vec\Sigma\cdot\vec L+1)$。

**$K^2$**：先算 $(\vec\Sigma\cdot\vec L)^2 = \Sigma^i\Sigma^jL_iL_j = (\delta_{ij} + i\epsilon_{ijk}\Sigma^k)L_iL_j = L^2 + i\vec\Sigma\cdot(\vec L\times\vec L) = L^2 - \vec\Sigma\cdot\vec L$（用了 $\vec L\times\vec L = i\vec L$）。又 $\beta$ 与 $\vec\Sigma\cdot\vec L$ 对易、$\beta^2 = 1$，故

$$K^2 = (\vec\Sigma\cdot\vec L + 1)^2 = L^2 + \vec\Sigma\cdot\vec L + 1 = \underbrace{L^2 + \vec\Sigma\cdot\vec L + \tfrac34}_{J^2 = (\vec L + \vec\Sigma/2)^2} + \frac14 = J^2 + \frac14.$$

于是 $K^2$ 本征值为 $j(j+1) + \tfrac14 = (j+\tfrac12)^2$，$k = \mp(j+\tfrac12)$。

</details>

**3.** 从截断条件 $n_r + s = Z\alpha E/\lambda$ 出发，把精确谱展开到 $O\big((Z\alpha)^4\big)$，读出 Bohr 能级与精细结构修正。

<details markdown="1"><summary>点击显示答案</summary>

记 $x = (Z\alpha)^2$。截断条件平方：$(Z\alpha)^2E^2 = (n_r+s)^2(m^2 - E^2)$，解得

$$E = m\left[1 + \frac{x}{(n_r+s)^2}\right]^{-1/2}, \qquad s = \sqrt{k^2 - x} = \lvert k\rvert - \frac{x}{2\lvert k\rvert} + O(x^2).$$

于是 $n_r + s = n - \dfrac{x}{2\lvert k\rvert} + O(x^2)$（用 $n = n_r + \lvert k\rvert$），平方取倒数：

$$\frac{1}{(n_r+s)^2} = \frac{1}{n^2}\left(1 - \frac{x}{n\lvert k\rvert}\right)^{-1} = \frac{1}{n^2}\left(1 + \frac{x}{n\lvert k\rvert} + O(x^2)\right).$$

代回并对 $(1+y)^{-1/2} = 1 - \frac{y}{2} + \frac{3y^2}{8} - \cdots$ 展开，$y = \frac{x}{n^2} + \frac{x^2}{n^3\lvert k\rvert}$：

$$E = m\left[1 - \frac{x}{2n^2} - \frac{x^2}{2n^3\lvert k\rvert} + \frac{3x^2}{8n^4} + O(x^3)\right] = m - \frac{m(Z\alpha)^2}{2n^2} - \frac{m(Z\alpha)^4}{2n^3}\left[\frac{1}{j+\frac12} - \frac{3}{4n}\right] + O\big((Z\alpha)^6\big),$$

最后一步代入 $\lvert k\rvert = j + \tfrac12$。**读数**：$-\frac{m(Z\alpha)^2}{2n^2}$ 即 Bohr 能级（$Z=1$：$-13.6/n^2$ eV，对接 第 06 篇）；$(Z\alpha)^4$ 项即精细结构，只含 $j$ 不单独含 $l$——这正是微扰论三项之和的形状（Griffiths 第 7 章），但这里是一次性精确结果的展开系数。

</details>

**4.** 用精确公式计算氢（$Z=1$）$n=2$ 壳层内 $2p_{3/2}$ 与 $2s_{1/2}$ 的能量分裂（以 eV 为单位），并与展开式对照。

<details markdown="1"><summary>点击显示答案</summary>

两个态的量子数：$2p_{3/2}$：$k = -2$，$n_r = n - \lvert k\rvert = 0$，$s = \sqrt{4 - \alpha^2}$；$2s_{1/2}$：$k = -1$，$n_r = 1$，$s = \sqrt{1 - \alpha^2}$。取 $\alpha^2 = 5.325\times10^{-5}$：

$$E(2p_{3/2}) = m\left[1 + \frac{\alpha^2}{4 - \alpha^2}\right]^{-1/2} \approx m\big(1 - 6.6564\times10^{-6}\big),$$

$$E(2s_{1/2}) = m\left[1 + \frac{\alpha^2}{\big(1 + \sqrt{1-\alpha^2}\big)^2}\right]^{-1/2} \approx m\big(1 - 6.65654\times10^{-6}\big).$$

两者之差（注意 $\big(1+\sqrt{1-\alpha^2}\big)^2 = 4 - 2\alpha^2 + O(\alpha^4)$，与 $4 - \alpha^2$ 差在 $\alpha^2$ 阶，除以 16 后成为 $\alpha^4$ 阶贡献）：

$$\Delta E = E(2p_{3/2}) - E(2s_{1/2}) \approx \frac{m\alpha^4}{32} = \frac{511\ \text{keV}\times(5.325\times10^{-5})^2}{32} \approx 4.53\times10^{-5}\ \text{eV},$$

约 10.9 GHz，$2p_{3/2}$ 在上（束缚更弱）。**对照展开式**：由第 6.1 节，$\Delta E = -\frac{m\alpha^4}{2\cdot 8}\Big[\big(\frac{1}{2} - \frac{3}{8}\big) - \big(1 - \frac{3}{8}\big)\Big] = \frac{m\alpha^4}{32}$，与精确计算完全一致（差别从 $\alpha^6$ 阶才开始）。附带一句：Dirac 理论里 $2s_{1/2}$ 与 $2p_{1/2}$ 严格同能，所以这同时也是 $2p_{3/2}$–$2p_{1/2}$ 的精细分裂；Lamb 位移再把 $2s_{1/2}$ 抬升约 1057 MHz，是 $\alpha^5$ 阶的下一层故事。

</details>

**5.** 从两个耦合径向方程出发，在非相对论极限下消去 $G$，推出 第 06 篇 的薛定谔径向方程。

<details markdown="1"><summary>点击显示答案</summary>

写 $E = m + E_{\text{NR}}$，$\lvert E_{\text{NR}}\rvert, \lvert V\rvert \ll m$，故 $E + m - V \approx 2m$、$E - m - V = E_{\text{NR}} - V$。第一个径向方程给出小分量由大分量生成：

$$G = \frac{1}{E + m - V}\left(\frac{d}{dr} + \frac{k}{r}\right)F \approx \frac{1}{2m}\left(F' + \frac{k}{r}F\right),$$

振幅比 $G/F \sim p/2m \sim v$——"小分量"名副其实。代入第二个方程 $G' = \frac{k}{r}G - (E_{\text{NR}} - V)F$：

$$\frac{1}{2m}\left(F'' + \frac{k}{r}F' - \frac{k}{r^2}F\right) = \frac{k}{2mr}\left(F' + \frac{k}{r}F\right) - (E_{\text{NR}} - V)F,$$

左边 $F'$ 项与右边 $F'$ 项相消，整理得

$$\frac{1}{2m}\left(F'' - \frac{k(k+1)}{r^2}F\right) = -(E_{\text{NR}} - V)F,$$

即

$$-\frac{1}{2m}\frac{d^2F}{dr^2} + \left[\frac{k(k+1)}{2mr^2} - \frac{Z\alpha}{r}\right]F = E_{\text{NR}}\,F.$$

最后用第 3.2 节的恒等式 $k(k+1) = l(l+1)$（$k=-1$：$0 = l(l+1)$ 得 $l=0$；$k=+1$：$2$，$l=1$；$k=-2$：$2$，$l=1$；$k=+2$：$6$，$l=2$……恰是 3.2 节的表），方程逐字变成 第 06 篇 第 2.1 节对 $u = rR$ 的径向方程（恢复 $\hbar$ 即离心垒 $l(l+1)\hbar^2/2mr^2$）。**所以 第 06 篇 的全部结果——$n = n_r + l + 1$、Bohr 能级、径向节点计数——都是 Dirac 理论在 $v \sim \alpha \ll 1$ 时的低能截面；本篇的新物理全部装在 $G$ 分量与 $k^2$ 里的 $-(Z\alpha)^2$ 中。**

</details>

## 参考

- Bjorken & Drell《Relativistic Quantum Mechanics》第 4 章：库仑场中的 Dirac 方程、$K$ 算符与氢原子精确解（本篇主线）。
- Sakurai《Advanced Quantum Mechanics》第 3 章：库仑场中 Dirac 方程的径向分解与能谱。
- Greiner《Relativistic Quantum Mechanics: Wave Equations》氢原子章：级数解、截断条件与径向波函数的完整推导（本篇第 5 节的细节来源）。
- Dirac《The Principles of Quantum Mechanics》§72–74：氢原子相对论理论的原始讲法。
- Griffiths《量子力学概论》第 7 章：精细结构的微扰论三项推导（第 6.2 节的对照对象）。
