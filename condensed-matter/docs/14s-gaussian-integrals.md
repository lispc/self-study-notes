# 补充材料：高斯基组与双体积分求值——量子化学的手艺层

> 本书位置：凝聚态物理入门导论 第 14 章补充材料（配套正文：[多电子问题与精确解](14-exact-methods-fci-ed.md)，下文简称"第 14 章"）。
> 前置知识：第 14 章（基组两大家族、$O(M^4)$ 双体积分的账）；多维高斯积分的基本手艺。
> 学习目标：理解为什么全世界的量子化学都用高斯型轨道（高斯乘积定理）；会推最简单的 $(ss\lvert ss)$ 积分闭式；知道压缩（contraction）、Schwarz 筛选与密度拟合（RI）如何把 $M^4$ 的账压到能付得起；认识 Kato 尖点条件——高斯基组天生缺陷与收敛律的来源。
>
> 记号约定：原子单位（同第 14 章）。$\lvert\vec r - \vec A\rvert$ 记与中心 $\vec A$ 的距离。

---

## 1. 一句话总结

**量子化学的底层手艺是选高斯：高斯乘积定理把"两个不同中心上的高斯之积"约化成"第三个中心上的一个高斯"，于是从重叠积分到四中心库仑积分全部有闭式、可递推——这是 Slater 指数轨道（物理上更正确）永远给不了的工程红利；代价是高斯在原子核处没有尖点（Kato 条件失效），收敛律因此从指数退化为幂律，需要外推。工程上的三件省钱工具——收缩基组（原语打包）、Schwarz 筛选（柯西–施瓦茨砍掉微小积分）、密度拟合（四指标拆三指标）——合起来把 $M^4$ 的账付到了几百轨道的日常计算。**

## 2. 为什么是高斯：乘积定理

原始驱动物理的轨道形状是 Slater 型 $e^{-\zeta r}$（有核尖点、有正确的 $r$ 尾巴），但它的双体积分没有闭式。高斯型轨道（GTO）

$$g_{\alpha\vec A}(\vec r) = e^{-\alpha\lvert\vec r - \vec A\rvert^2}$$

换来一条代数性质——**高斯乘积定理**（推导见自检问题 1）：

$$e^{-\alpha\lvert\vec r-\vec A\rvert^2}\,e^{-\beta\lvert\vec r-\vec B\rvert^2} = e^{-\mu\lvert\vec A-\vec B\rvert^2}\cdot e^{-p\lvert\vec r-\vec P\rvert^2},\qquad p = \alpha+\beta,\ \ \vec P = \frac{\alpha\vec A + \beta\vec B}{p},\ \ \mu = \frac{\alpha\beta}{p}.$$

两个中心合成一个：**一切多中心积分逐步塌缩为单中心高斯积分**。最典型的成品是四个 s 型原语的双体积分（推导见自检问题 5）：

$$(ab\lvert cd) = \frac{2\pi^{5/2}}{pq\sqrt{p+q}}\,e^{-\mu\lvert\vec A-\vec B\rvert^2 - \nu\lvert\vec C-\vec D\rvert^2},$$

$p,\mu$ 属于 $(a,b)$ 对、$q,\nu$ 属于 $(c,d)$ 对——一个初等函数，没有数值积分。更高角动量（p、d、f……）的积分由 s 型出发用**递推关系**（Obara–Saika、McMurchie–Davidson）逐级升角生成：机器做微商，人不用画图。

## 3. 收缩：把原语打包成"轨道"

单个高斯尾巴塌得太快（$e^{-\alpha r^2}$ vs $e^{-\zeta r}$），逼近一条原子轨道需要若干原语线性组合——**收缩**：

$$\phi_i(\vec r) = \sum_\mu d_{i\mu}\,g_{\mu}(\vec r)\qquad(\text{收缩系数 } d \text{ 固定，来自原子拟合}).$$

cc-pVnZ 家族（第 14 章 3.1 节）的每个"轨道"都是 3–10 个原语的包。代价透明：原语层积分个数 $\sim(\text{原语总数})^4$，收缩只是把求和权重固定——**精度按层（DZ/TZ/QZ）指数上升，成本按层 $2^4\sim$ 十六倍地涨**，这笔交换在 cc-系列的设计里被调到接近最优。

## 4. 三件省钱工具

**账单回顾**（第 14 章 2.2 节）：双体积分 $(pq\lvert rs)$ 共 $O(M^4)$ 个。三个杠杆：

- **Schwarz 筛选**：柯西–施瓦茨不等式（证明见自检问题 2）给出

$$\lvert(pq\lvert rs)\rvert\ \le\ \sqrt{(pq\lvert pq)}\,\sqrt{(rs\lvert rs)}\ \equiv\ Q_{pq}Q_{rs},$$

右边的对角量预计算一次（$O(M^2)$ 个）。阈值以下直接置零——真实分子里远距离轨道对的双体积分指数小，**筛选后实际要算的积分往往只有名义 $M^4$ 的百分之几**。
- **密度拟合 / RI**（resolution of the identity）：把乘积密度塞进辅助基 $\{J\}$，

$$(pq\lvert rs)\ \approx\ \sum_{JK}(pq\lvert J)\,V^{JK}\,(K\lvert rs),\qquad V^{JK} = \big[(J\lvert K)\big]^{-1},$$

四指标积分变成三个三指标组的收缩（证明与误差的二阶性见自检问题 4）：存储与变换从 $O(M^4)$ 降到 $O(M^3)$——MP2（第 15 章）与 DF-HF 的日常形态都靠它。
- **积分变换的账**：AO → MO 的四指标变换是 $O(M^5)$（第 15 章 MP2 一节已点账），半定域轨道（Pipek–Mezey 局域化）可以把有效标度压向线性——"局域相关方法"（LMP2/LCCSD）的出发点，思路一句话：**动态相关是短程的，长程积分不必精算**。

## 5. 高斯的原罪：Kato 尖点

薛定谔方程在库仑奇点附近有严格的行为（推导见自检问题 3）：波函数对电子–核距离的导数满足

$$\frac{\partial\psi}{\partial r}\bigg|_{r=0} = -Z\,\psi(0)\qquad(\text{电子–核尖点，原子单位}),$$

（电子–电子尖点是它的一半，$-\tfrac12$。）精确轨道在核处有**尖角**；高斯处处光滑、核处斜率为零——**原理上不可能**重现尖点。后果不是灾难而是税单：相关能随基组层次 $n$ 的收敛从指数律退化为 $n^{-4}$ 型幂律，于是 cc-pVnZ 外推公式（用 n 与 n+1 两层外推到基组极限）成为标准操作。这条"物理正确性换工程可行性"的交换，贯穿整个量子化学史。

## 小结

- 高斯乘积定理 = 多中心积分闭式化的钥匙；$(ss\lvert ss)$ 一个初等函数搞定。
- 收缩基组（cc-pVnZ）：原语打包、层间指数收敛；Schwarz 筛选 + RI 把 $M^4$ 压到实际可付。
- Kato 尖点：高斯的原罪，幂律收敛 + 外推的根源。
- 本篇是手艺层：正文的方法论（FCI → CC → DFT）全部骑在这套积分机器上。

## 自检问题

**1.** 证明高斯乘积定理（配方平方），并解释 $e^{-\mu\lvert\vec A-\vec B\rvert^2}$ 因子的物理含义。

<details markdown="1"><summary>点击显示答案</summary>

展开指数部分并配方：

$$\alpha\lvert\vec r-\vec A\rvert^2 + \beta\lvert\vec r-\vec B\rvert^2 = (\alpha+\beta)\left\lvert\vec r - \frac{\alpha\vec A+\beta\vec B}{\alpha+\beta}\right\rvert^2 + \frac{\alpha\beta}{\alpha+\beta}\lvert\vec A-\vec B\rvert^2.$$

验证：交叉项系数 $-2\vec r\cdot(\alpha\vec A+\beta\vec B)$ 两侧一致；常数项左 $=\alpha A^2+\beta B^2$，右 $= \tfrac{\lvert\alpha A+\beta B\rvert^2}{\alpha+\beta} + \tfrac{\alpha\beta}{\alpha+\beta}\lvert A-B\rvert^2$，展开即 $\alpha A^2+\beta B^2$ ✓。于是

$$e^{-\alpha\lvert\vec r-A\rvert^2}e^{-\beta\lvert\vec r-B\rvert^2} = e^{-\mu\lvert A-B\rvert^2}\,e^{-p\lvert\vec r-P\rvert^2}.$$

**物理**：$e^{-\mu\lvert\vec A - \vec B\rvert^2}$ 是"两中心交叠折扣"——中心相距远时积分为零的来源全在这一因子；$P$ 是质量加权中心，新宽度 $1/\sqrt p$ 比原来两个都窄（高斯越乘越瘦）。**递归的本钱**：任何包含"同一电子坐标的两个中心"的积分先做一次乘积定理，中心数减一——四中心双体积分做两次（每个电子一次），剩下两团高斯之间的库仑积分有 erf 闭式。

</details>

**2.** 证明 Schwarz 不等式 $\lvert(pq\lvert rs)\rvert \le \sqrt{(pq\lvert pq)}\sqrt{(rs\lvert rs)}$，并说明为什么对角量只需要 $O(M^2)$ 个、却能筛掉绝大多数积分。

<details markdown="1"><summary>点击显示答案</summary>

把双体积分看成密度的内积：记乘积函数 $\varphi_{pq}(\vec r) = \phi_p(\vec r)\phi_q(\vec r)$（及 $\varphi_{rs}$），库仑算符下定义内积

$$\langle f\lvert g\rangle_C \equiv \iint\frac{f(\vec r_1)g(\vec r_2)}{r_{12}}\ \text d\vec r_1\text d\vec r_2.$$

该内积正定（对任意 $f$，$\langle f\lvert f\rangle_C \ge 0$，等于两个密度分布的静电互作用能）。柯西–施瓦茨：

$$\lvert\langle\varphi_{pq}\lvert\varphi_{rs}\rangle_C\rvert^2 \le \langle\varphi_{pq}\lvert\varphi_{pq}\rangle_C\,\langle\varphi_{rs}\lvert\varphi_{rs}\rangle_C = (pq\lvert pq)(rs\lvert rs).$$

**筛选用法**：对角量 $(pq\lvert pq)$ 只有 $O(M^2)$ 个，预计算后作"积分大小的上界尺"。设阈值 $\tau$：若 $Q_{pq}Q_{rs} < \tau$，则 $(pq\lvert rs)$ 必小于 $\tau$，不必计算。**为什么多数积分微小**：$Q_{pq}$ 本身含乘积密度的总电荷 $\sim$ 轨道对重叠——两个在空间中不相邻的局域轨道（尤其收缩基下）乘积密度近乎为零，其一切积分都被上界压死。真实大分子的"有效非零积分"比例随尺寸下降——线性标度方法的入口。

</details>

**3.** 从薛定谔方程出发推导电子–核 Kato 尖点条件 $\psi'(0)/\psi(0) = -Z$，并证明任何有限个高斯的线性组合在核处斜率为零、从而不可能满足它。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：在核（取为原点）附近，s 对称分量主导（角向部分有限），哈密顿量取

$$-\frac12\nabla^2\psi - \frac{Z}{r}\psi = E\psi \;\Longrightarrow\; -\frac{1}{2r^2}\frac{\text d}{\text dr}\left(r^2\frac{\text d\psi}{\text dr}\right) - \frac{Z}{r}\psi = E\psi.$$

乘 $r$、取 $r\to0$：设 $\psi = \psi(0) + \psi'(0)r + O(r^2)$。逐项：左边第一项 $\sim -\tfrac{1}{2r^2}\tfrac{d}{dr}(r^2\psi') = -\tfrac{1}{r^2}(2r\psi' + r^2\psi'') \sim -\tfrac{2\psi'}{r}$，乘 $r$ 后 $\to -2\psi'(0)$；库仑项 $-\tfrac{Z}{r}\psi$ 乘 $r$ 后 $\to -Z\psi(0)$；右边 $E\psi r \to 0$。故

$$-2\psi'(0) - Z\psi(0) = 0\;\Longrightarrow\;\frac{\psi'(0)}{\psi(0)} = -\frac{Z}{2}\cdot\frac{2}{1}\cdot\frac{1}{1} = -Z.$$

（电子–电子尖点同理，电荷换 1、约化质量换 $\tfrac12$，得 $-\tfrac12$。）

**高斯的无能**：每个 $g_\alpha(\vec r) = e^{-\alpha r^2}$ 在 $r = 0$ 处 $g'(0) = 0$（偶函数光滑极值）；线性组合 $\sum d_i e^{-\alpha_i r^2}$ 仍满足 $\phi'(0) = \sum d_i\cdot 0 = 0$——除非 $\phi(0)=0$（无意义），条件 $\phi'/\phi = -Z$ 无法满足。核附近的密度形状系统性偏差，是基组收敛幂律化的根源；Slater 型 $e^{-\zeta r}$ 的导数 $= -\zeta e^{-\zeta r}$，恰好能配出尖点——**物理形状与代数便利在这里正面冲突，量子化学选择了后者并付了收敛律的税**。

</details>

**4.** 写出密度拟合（RI）的构造与拟合误差对总能量的影响阶数；数一数四指标存储如何降为三指标。

<details markdown="1"><summary>点击显示答案</summary>

**构造**：选辅助基 $\{J\}$（比轨道基略大），把每个乘积密度向它投影：

$$\varphi_{pq}(\vec r) \approx \tilde\varphi_{pq} = \sum_J C_{pq}^{J}\,J(\vec r),\qquad C = \arg\min\ \langle\varphi_{pq}-\tilde\varphi_{pq}\lvert\ \tfrac{1}{r}\ \lvert\ \varphi_{pq}-\tilde\varphi_{pq}\rangle_C,$$

（在库仑度量下做最小二乘——度量的选择本身就是一门小手艺）解出 $C_{pq}^J = \sum_K (pq\lvert K)[(K\lvert K')]^{-1}$ 型，于是

$$(pq\lvert rs) \approx \sum_{JK}(pq\lvert J)\,V^{JK}\,(K\lvert rs),\qquad V = (J\lvert K)^{-1}.$$

**误差阶**：被拟合的对象是 $(pq\lvert rs)$ 的**密度差**的静电能——对拟合残差 $\delta\varphi$ 是**二阶**（$\langle\delta\varphi\lvert\tfrac1r\lvert\varphi\rangle$ 型一阶项在最优投影下为零）。能量对积分是线性泛函，故能量误差也是残差的二阶——辅助基只需"够好"不必"同尺寸"，实际精度损失 $10^{-4}$–$10^{-5}$ Ha 量级，远小于化学精度。

**账**：三指标组 $(pq\lvert J)$ 共 $O(M^2M_\text{aux}) \sim O(M^3)$ 个，$(J\lvert K)$ $O(M_\text{aux}^2)$；原 $O(M^4)$ 的四指标阵列不再需要显式存在。RI 的代价是每次用积分都要做一次中间收缩（矩阵乘 $O(N_o^2M^3)$）——标度仍是三次，但常数变大：**空间换算力**，对 MP2/DF-SCF 这类积分反复使用的场合是净赢。

</details>

**5.** 推导四个 s 型原语的双体积分闭式 $(ab\lvert cd) = \dfrac{2\pi^{5/2}}{pq\sqrt{p+q}}e^{-\mu\lvert\vec A-\vec B\rvert^2-\nu\lvert\vec C-\vec D\rvert^2}$ 的骨架（允许引用一个标准高斯位形积分）。

<details markdown="1"><summary>点击显示答案</summary>

**第一步（乘积定理两次）**：对电子 1 把 $a,b$ 合并为中心 $\vec P$、指数 $p$；对电子 2 把 $c,d$ 合并为 $\vec Q$、指数 $q$：

$$(ab\lvert cd) = E_{ab}E_{cd}\iint\frac{e^{-p\lvert\vec r_1-\vec P\rvert^2}\,e^{-q\lvert\vec r_2-\vec Q\rvert^2}}{r_{12}}\,\text d\vec r_1\text d\vec r_2,\qquad E_{ab} = e^{-\mu\lvert\vec A-\vec B\rvert^2},\ E_{cd} = e^{-\nu\lvert\vec C-\vec D\rvert^2}.$$

**第二步（两个标准辅助结果）**：

(A) 高斯密度的静电势：$\displaystyle\int\frac{e^{-q\lvert\vec r_2-\vec Q\rvert^2}}{\lvert\vec r_1-\vec r_2\rvert}\text d\vec r_2 = \left(\frac{\pi}{q}\right)^{3/2}\frac{\mathrm{erf}\big(\sqrt q\,R\big)}{R}$，其中 $R = \lvert\vec r_1 - \vec Q\rvert$；

(B) erf 的积分表示：$\displaystyle\frac{\mathrm{erf}(\sqrt q\,R)}{R} = \frac{2}{\sqrt\pi}\int_0^{\sqrt q}e^{-s^2R^2}\,\text ds$（两边对 $s$ 求导即证）。

代入 (A)(B)，$s$ 切片的被积函数是**两个高斯的乘积**——再一次乘积定理：

$$\int e^{-p\lvert\vec r_1-\vec P\rvert^2}\,e^{-s^2\lvert\vec r_1-\vec Q\rvert^2}\,\text d\vec r_1 = \frac{\pi^{3/2}}{(p+s^2)^{3/2}}\,e^{-\frac{ps^2}{p+s^2}\lvert\vec P-\vec Q\rvert^2}.$$

**第三步（收进 Boys 函数）**：合并常数并换元，被积函数恰好组装成 $e^{-T u^2}$（$T = \tfrac{pq}{p+q}\lvert\vec P-\vec Q\rvert^2$）对 $u\in[0,1]$ 的积分——按定义这就是 $F_0(T)$：

$$(ab\lvert cd) = E_{ab}E_{cd}\,\frac{2\pi^{5/2}}{pq\sqrt{p+q}}\;F_0\!\left(\frac{pq}{p+q}\lvert\vec P-\vec Q\rvert^2\right),\qquad F_0(T) = \int_0^1 e^{-Tu^2}\,\text du.$$

**极限核对**：$\vec P\to\vec Q$ 时 $T\to0$、$F_0(0) = 1$，回到正文引用的闭式；再取单中心全同（$p = q = 2a$、四中心重合）得 $\pi^{5/2}/4a^{3/2}$，与高斯密度的静电自能直接积分一致——闭式可信。

**收尾**：更高角动量通过 $F_n(T) = \int_0^1u^{2n}e^{-Tu^2}\text du$ 与其递推 $F_{n+1} = \dfrac{(2n+1)F_n - e^{-T}}{2T}$（对 $u^{2n+1}e^{-Tu^2}$ 求导再积分即得）以及对 $A$、$B$、$C$、$D$ 的坐标微商，从 $(ss\lvert ss)$ 机械生成——这就是第 2 节"机器做微商"的确切含义。

</details>

## 参考

- Helgaker, Jørgensen & Olsen《Molecular Electronic-Structure Theory》第 8–9 章：高斯积分的完整机器（乘积定理、Obara–Saika 递推、Boys 函数）。
- Szabo & Ostlund 第 3 章附录：$(ss\lvert ss)$ 与收缩基组的教科书版推导。
- T. Kato, Commun. Pure Appl. Math. 10, 151 (1957)：尖点条件的原始文献。
- F. Weigend & R. Ahlrichs, PCCP 7, 3297 (2005)：RI 辅助基（def2 系）的设计与精度账。
