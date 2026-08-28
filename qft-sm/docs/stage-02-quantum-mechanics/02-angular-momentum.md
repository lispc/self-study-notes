# 角动量理论：SU(2) 的物理化身

> 路线图位置：第 2 阶段（量子力学）· 角动量理论
> 前置知识：量子力学基础（态矢、算符、对易关系、中心势薛定谔方程）；群论一侧的严格讨论见 [SO(3)/SU(2) 与角动量的关系](../stage-00-math/01-so3-su2-and-angular-momentum.md)（本篇引用其结论，不重复证明）。
> 学习目标：会算——从 $[x,p]$ 验证角动量代数、用升降算符理解 $\lvert j,m\rangle$、写球谐函数、处理自旋 1/2 旋量、手把手做角动量相加（CG 系数）、用 Wigner–Eckart 定理推出跃迁选择定则。

---

## 1. 一句话总结

**角动量是旋转的生成元；量子力学中它的全部"允许取值"由对易关系 $[J_i,J_j]=i\hbar\epsilon_{ijk}J_k$（即 $\mathfrak{su}(2)$ 李代数）决定——轨道角动量只取整数 $l$（波函数单值性），自旋可以取半整数（SU(2) 的投影表示），而两个角动量的合成就是表示的张量积分解，其系数（CG 系数）进一步决定了原子跃迁的选择定则。**

**单位约定**：本篇保留 $\hbar$ 不显式取 1（方便对照 Griffiths、Sakurai 等教材；stage-00 篇用 $\hbar=1$，换算时把 $J$ 换成 $J/\hbar$ 即可）。

## 2. 从经典角动量到算符

经典力学中质点的角动量是 $\vec L = \vec r \times \vec p$。量子化就是把 $\vec r, \vec p$ 换成算符（满足 $[x_i, p_j] = i\hbar\delta_{ij}$，其余对易子为零）：

$$L_i = \epsilon_{ijk}\, x_j p_k \qquad (\text{重复指标求和}),$$

即 $L_x = y p_z - z p_y$ 及其循环置换。注意 $x$ 与 $p$ 在叉乘中天然"错开"（$L_i$ 里相乘的总是不同分量），不存在排序 ambiguity，$L_i$ 自动厄米。

**从基本对易关系验证角动量代数**。以 $[L_x, L_y]$ 为例，直接展开：

$$[L_x, L_y] = [y p_z - z p_y,\; z p_x - x p_z].$$

四项中 $[y p_z,\, x p_z] = 0$（$p_z$ 与 $x$ 对易）、$[z p_y,\, z p_x] = 0$（$z$ 与 $p_y$ 对易），只剩交叉项：

$$[y p_z,\, z p_x] = y\,[p_z, z]\,p_x = -i\hbar\, y p_x, \qquad
[z p_y,\, x p_z] = x\,[z, p_z]\,p_y = +i\hbar\, x p_y,$$

合起来

$$[L_x, L_y] = -i\hbar\, y p_x + i\hbar\, x p_y = i\hbar\,(x p_y - y p_x) = i\hbar L_z.$$

同理得一般形式

$$\boxed{[L_i, L_j] = i\hbar\,\epsilon_{ijk}\, L_k}$$

这与旋转群生成元的李代数完全一致——不是巧合：$\vec L$ 正是作用在波函数上的无穷小旋转生成元（stage-00 篇第 4 节）。

**中心势中的好量子数**。设

$$H = \frac{p^2}{2m} + V(r).$$

由 $[L_i, p_j] = i\hbar\epsilon_{ijk}p_k$ 可得

$$[L_i, p^2] = i\hbar\,\epsilon_{ijk}\,(p_j p_k + p_k p_j) = 0$$

（对称张量 $p_jp_k+p_kp_j$ 与反对称的 $\epsilon_{ijk}$ 收缩为零）；同理 $[L_i, x^2] = 0$，从而 $[L_i, V(r)] = 0$。再定义 $L^2 = L_x^2 + L_y^2 + L_z^2$，易证 $[L^2, L_i] = 0$（见 stage-00 篇自检第 2 题的同型计算）。于是

$$[H, L^2] = [H, L_z] = [L^2, L_z] = 0,$$

三个算符存在共同本征态，记为 $\lvert n, l, m\rangle$（$n$ 标记能量）。物理含义：**中心势中角动量守恒**（Noether 定理：旋转对称 ↔ 角动量守恒），$l, m$ 是"好量子数"——态随时间演化时它们不变。这就是为什么原子态可以用 $(n, l, m)$ 贴标签。

## 3. 代数解法骨架：$\lvert j, m\rangle$ 与升降算符

现在脱离 $\vec r\times\vec p$ 的具体实现，只从对易关系 $[J_i, J_j] = i\hbar\epsilon_{ijk}J_k$ 出发，求全部可能的角动量。定义

$$J^2 = J_x^2 + J_y^2 + J_z^2, \qquad J_\pm = J_x \pm i J_y,$$

由对易关系推出

$$[J^2, J_z] = 0, \qquad [J_z, J_\pm] = \pm\hbar J_\pm, \qquad [J_+, J_-] = 2\hbar J_z.$$

取 $J^2, J_z$ 的共同本征态 $\lvert j, m\rangle$：

$$J^2\lvert j,m\rangle = \hbar^2 j(j+1)\lvert j,m\rangle, \qquad J_z\lvert j,m\rangle = \hbar m\lvert j,m\rangle.$$

$[J_z, J_\pm] = \pm\hbar J_\pm$ 意味着 $J_\pm\lvert j,m\rangle$ 仍是 $J_z$ 的本征态、本征值 $\hbar(m\pm1)$——升降算符把 $m$ 一格一格移动。归一化后是

$$J_\pm\lvert j,m\rangle = \hbar\sqrt{j(j+1) - m(m\pm1)}\;\lvert j, m\pm1\rangle.$$

**关键约束**：$J^2 - J_z^2 = \tfrac12(J_+J_- + J_-J_+)$ 是半正定算符，所以 $m^2 \le j(j+1)$，升降链必须在两端终止：存在 $m_{\max}$ 使 $J_+\lvert j, m_{\max}\rangle = 0$。由上面的系数公式，终止要求 $j(j+1) = m_{\max}(m_{\max}+1)$，即 $m_{\max} = j$；同理 $m_{\min} = -j$。链长 $m_{\max} - m_{\min} = 2j$ 必须是非负整数，于是

$$j = 0,\ \tfrac12,\ 1,\ \tfrac32,\ \dots, \qquad m = -j, -j+1, \dots, j \quad (\text{共 } 2j+1 \text{ 个}).$$

**到这一步只用了李代数，整数和半整数一律合法**。完整推导见 stage-00 篇第 6 节；那里还证明了：整数 $j$ 是 SO(3) 的普通表示，半整数 $j$ 只是 SU(2) 的表示（转 $2\pi$ 变号）。本篇关心的是：这两类解分别由什么物理对象实现。

## 4. 轨道角动量：球谐函数

把 $\vec p = -i\hbar\nabla$ 代入 $\vec L = \vec r\times\vec p$，用球坐标 $(r,\theta,\varphi)$ 写出各算符：

$$L_z = -i\hbar\frac{\partial}{\partial\varphi},$$

$$L_\pm = \hbar e^{\pm i\varphi}\left(\pm\frac{\partial}{\partial\theta} + i\cot\theta\,\frac{\partial}{\partial\varphi}\right),$$

$$L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\varphi^2}\right].$$

中心势薛定谔方程因此可以分离变量：$\psi(r,\theta,\varphi) = R(r)\,Y(\theta,\varphi)$，角向部分正是 $L^2, L_z$ 的共同本征函数——**球谐函数**

$$Y_l^m(\theta,\varphi) = (-1)^m\sqrt{\frac{(2l+1)\,(l-m)!}{4\pi\,(l+m)!}}\;P_l^m(\cos\theta)\,e^{im\varphi},$$

其中 $P_l^m$ 是缔合 Legendre 函数。最低几个显式写出（值得眼熟）：

$$Y_0^0 = \frac{1}{\sqrt{4\pi}}, \qquad Y_1^0 = \sqrt{\frac{3}{4\pi}}\cos\theta, \qquad Y_1^{\pm1} = \mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\varphi},$$

$$Y_2^0 = \sqrt{\frac{5}{16\pi}}\left(3\cos^2\theta - 1\right).$$

**宇称**。空间反演 $\vec r \to -\vec r$ 在球坐标中是 $(\theta,\varphi) \to (\pi-\theta,\ \varphi+\pi)$。由 $e^{im(\varphi+\pi)} = (-1)^m e^{im\varphi}$ 与 $P_l^m(-x) = (-1)^{l+m}P_l^m(x)$，得

$$Y_l^m(\pi-\theta,\varphi+\pi) = (-1)^l\, Y_l^m(\theta,\varphi),$$

即 $l$ 为偶数时宇称偶、为奇数时宇称奇。第 7 节的选择定则要用到这个结论。

**为什么 $l$ 只取整数**。波函数必须单值：绕 $z$ 轴转一圈是同一点，

$$\psi(\varphi + 2\pi) = \psi(\varphi) \;\Longrightarrow\; e^{i2\pi m} = 1 \;\Longrightarrow\; m \in \mathbb Z,$$

于是 $l$ 也只能取整数 $0, 1, 2, \dots$。群论语言（stage-00 篇第 6.2、7 节）：波函数是空间中的普通函数，转 $2\pi$ 必须严格等于自身，不允许投影表示的 $\pm1$ 自由度，所以轨道角动量只携带 SO(3) 的普通表示——整数 $l$。半整数的"另一半"表示要靠自旋实现。

## 5. 自旋 1/2：泡利矩阵与旋量

**Stern–Gerlach 实验（1922）**：让银原子束通过非均匀磁场。银原子轨道角动量为零（$^2S_{1/2}$ 基态），磁矩全部来自最外层那个电子。若磁矩取向连续分布，屏上应是一条连续的带；实验却看到**清晰分裂成两条斑纹**。沿任意方向测量，角动量分量都只有两个取值 $\pm\hbar/2$——电子携带 $s = 1/2$ 的内禀角动量：**自旋**。

自旋没有轨道对应（第 4 节：单值性禁止半整数 $m$），它是粒子的内禀属性，如同质量、电荷。其态空间是二维复空间 $\mathbb C^2$，态矢写成两分量的**旋量**

$$\chi = \begin{pmatrix} a \\ b \end{pmatrix}, \qquad |a|^2 + |b|^2 = 1,$$

基矢取 $S_z$ 的本征态 $\chi_+ = \binom{1}{0}$（$m=+\tfrac12$）与 $\chi_- = \binom{0}{1}$（$m=-\tfrac12$）。自旋算符为

$$\vec S = \frac{\hbar}{2}\,\vec\sigma,$$

其中泡利矩阵

$$\sigma_1 = \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_3 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

满足 $\sigma_i\sigma_j = \delta_{ij}I + i\epsilon_{ijk}\sigma_k$，从而 $(\hat n\cdot\vec\sigma)^2 = I$，且 $[S_i, S_j] = i\hbar\epsilon_{ijk}S_k$ 自动成立。

**转动算符**。绕 $\hat n$ 转 $\theta$ 角的算符是 $U = e^{-i\theta\,\hat n\cdot\vec S/\hbar} = e^{-i\theta\,\hat n\cdot\vec\sigma/2}$。利用 $(\hat n\cdot\vec\sigma)^2 = I$ 把指数级数分成偶、奇两部分求和，得显式

$$U(\theta,\hat n) = \cos\frac{\theta}{2}\,I - i\sin\frac{\theta}{2}\,(\hat n\cdot\vec\sigma).$$

注意角度被除了 2——这是旋量与矢量的本质差别。**$2\pi$ 旋转的显式计算**：代入 $\theta = 2\pi$，$\cos\pi = -1$、$\sin\pi = 0$，得

$$U(2\pi, \hat n) = -I, \qquad \chi \;\longrightarrow\; -\chi,$$

与转轴无关；要转 $4\pi$ 才回到 $+I$。作为对照，绕 $z$ 轴：$U_z(\theta) = \mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$，于是 $\chi_+ \to e^{-i\theta/2}\chi_+$，$\theta=2\pi$ 时得 $-\chi_+$。单个态的整体符号不可观测，但两路干涉能暴露这个 $-1$——中子干涉实验已精确证实（见 stage-00 篇第 7 节）。

另一个值得记住的事实：旋量转"半角"，但期望值 $\langle\vec\sigma\rangle$ 作为普通矢量转满 $\theta$（即 $U\,\vec\sigma\,U^\dagger$ 给出角度 $\theta$ 的 SO(3) 旋转）——这正是 SU(2) → SO(3) 二对一映射在具体计算中的样子。

## 6. 角动量相加与 Clebsch–Gordan 系数

**重点小节**。两个角动量 $\vec J_1, \vec J_2$（如轨道 + 自旋，或两个粒子的自旋）互相对易（$[J_{1i}, J_{2j}] = 0$，作用在不同自由度上），总角动量

$$\vec J = \vec J_1 + \vec J_2$$

仍满足角动量代数 $[J_i, J_j] = i\hbar\epsilon_{ijk}J_k$。于是有两套自然基：

- **非耦合表象** $\lvert j_1 m_1\rangle\otimes\lvert j_2 m_2\rangle$：$J_1^2, J_{1z}, J_2^2, J_{2z}$ 的共同本征态，共 $(2j_1+1)(2j_2+1)$ 个；
- **耦合表象** $\lvert J M\rangle$：$J_1^2, J_2^2, J^2, J_z$ 的共同本征态（$M = m_1 + m_2$）。

两套基之间的展开系数就是 **Clebsch–Gordan（CG）系数**：

$$\lvert J M\rangle = \sum_{m_1+m_2=M} C^{JM}_{j_1 m_1\, j_2 m_2}\;\lvert j_1 m_1\rangle\lvert j_2 m_2\rangle.$$

**手把手算 $\tfrac12\otimes\tfrac12$（两个自旋 1/2）**。非耦合基 4 个：$\lvert\uparrow\uparrow\rangle, \lvert\uparrow\downarrow\rangle, \lvert\downarrow\uparrow\rangle, \lvert\downarrow\downarrow\rangle$（箭头依次指粒子 1、2 的 $S_z$）。

第一步，找最高权态。$M = m_1 + m_2$ 的最大值是 $+1$，只有 $\lvert\uparrow\uparrow\rangle$ 一个态达到，它必是 $J=1$ 多重态的 $\lvert 1, 1\rangle$：

$$\lvert 1, 1\rangle = \lvert\uparrow\uparrow\rangle.$$

第二步，用总降算符 $J_- = S_{1-} + S_{2-}$ 逐级下降。左边（用第 3 节公式，$j=1, m=1$）：

$$J_-\lvert 1,1\rangle = \hbar\sqrt{1\cdot2 - 1\cdot0}\;\lvert 1,0\rangle = \hbar\sqrt2\,\lvert 1,0\rangle;$$

右边（$S_-\lvert\uparrow\rangle = \hbar\lvert\downarrow\rangle$）：

$$(S_{1-}+S_{2-})\lvert\uparrow\uparrow\rangle = \hbar\lvert\downarrow\uparrow\rangle + \hbar\lvert\uparrow\downarrow\rangle.$$

两式相等，得

$$\lvert 1, 0\rangle = \frac{1}{\sqrt2}\left(\lvert\uparrow\downarrow\rangle + \lvert\downarrow\uparrow\rangle\right).$$

再降一次（或直接由 $M=-1$ 的唯一性）：

$$\lvert 1, -1\rangle = \lvert\downarrow\downarrow\rangle.$$

这三个态构成**三重态**（$J=1$，对交换两粒子对称）。剩下的一维子空间与 $\lvert 1,0\rangle$ 正交：

$$\lvert 0, 0\rangle = \frac{1}{\sqrt2}\left(\lvert\uparrow\downarrow\rangle - \lvert\downarrow\uparrow\rangle\right),$$

即**单态**（$J=0$，交换反对称）。验证：$J_+\lvert 0,0\rangle = 0$、$J^2\lvert 0,0\rangle = 0$。维数检查 $2\times2 = 4 = 3 + 1$，即

$$\tfrac12 \otimes \tfrac12 = 1 \oplus 0.$$

**一般规则**：$j_1 \otimes j_2$ 分解为

$$J = |j_1 - j_2|,\ |j_1 - j_2| + 1,\ \dots,\ j_1 + j_2,$$

每个 $J$ 恰好出现一次；维数自动吻合：$\sum_{J}(2J+1) = (2j_1+1)(2j_2+1)$。CG 系数有一套高度对称的重新包装叫 **Wigner 3j 符号**，只是把 CG 系数乘上对称化因子，物理内容相同。群论视角：这就是 SU(2) 不可约表示的张量积分解（stage-00 篇第 8 节）。

## 7. Wigner–Eckart 定理与选择定则

**不可约张量算符**：一组 $2k+1$ 个算符 $T^k_q$（$q = -k,\dots,k$）若在转动下像 $\lvert k, q\rangle$ 那样变换（等价地，$[J_z, T^k_q] = \hbar q\, T^k_q$ 等），就叫秩 $k$ 的不可约张量算符。位置 $\vec r$、动量 $\vec p$、电偶极算符都是秩 1（矢量）；哈密顿量是秩 0（标量）。

**Wigner–Eckart 定理（物理陈述）**：张量算符在角动量本征态之间的矩阵元分解为

$$\langle j m\,\rvert\, T^k_q \,\rvert\, j' m'\rangle = C^{jm}_{j' m'\, k q}\times \langle j \lVert T^k \rVert j'\rangle\,,$$

即**矩阵元 = CG 系数 × 约化矩阵元**。全部对磁量子数 $(m, m', q)$ 的依赖都装在 CG 系数里（纯几何、查表可得），约化矩阵元 $\langle j \lVert T^k \rVert j'\rangle$ 与 $m$ 无关，包含全部动力学信息。定理的证明就是把"算符 × 态" $T^k_q\lvert j'm'\rangle$ 当成 $k \otimes j'$ 的乘积态做角动量相加——第 6 节的机器原样搬过来。

**电偶极（E1）跃迁选择定则的直觉推导**。原子与光的相互作用在偶极近似下是 $H' = -e\,\vec r\cdot\vec E$，微扰算符是 $\vec r$：秩 1、宇称奇。跃迁振幅正比于 $\langle n' l' m'\rvert\, r_q\,\rvert n l m\rangle$。由 Wigner–Eckart，非零要求两件事：

1. **CG 系数不为零**：$l \otimes 1$ 只含 $l' = l-1, l, l+1$，且 $m' = m + q$，即 $\Delta m = 0, \pm 1$；
2. **宇称**：$\vec r$ 是奇的，初末态宇称必须相反。球谐函数宇称为 $(-1)^l$（第 4 节），所以 $l + l'$ 必须是奇数——排除 $l' = l$，只剩 $\Delta l = \pm 1$。

合起来就是 E1 选择定则 $\boxed{\Delta l = \pm 1,\ \Delta m = 0, \pm 1}$。物理图像：光子携带一个单位的角动量（自旋 1），吸收/发射一个光子，原子的角动量必须相应地改变一格——选择定则是角动量守恒的记账方式。

## 8. 应用与前瞻

**氢原子的简并结构**。库仑势的能级 $E_n = -13.6\,\mathrm{eV}/n^2$ 只依赖主量子数 $n$（径向方程的求解与 $n$ 的来历见补充材料[氢原子与电子亚层](02s-hydrogen-and-subshells.md)）。对每个 $n$，$l = 0, 1, \dots, n-1$，每个 $l$ 有 $2l+1$ 个 $m$，简并度

$$\sum_{l=0}^{n-1}(2l+1) = n^2 \quad \xrightarrow{\ \text{乘自旋}\ }\ 2n^2.$$

$l$ 简并是库仑势特有的（隐藏 SO(4) 对称性，Laplace–Runge–Lenz 矢量），$m$ 简并则是任何中心势都有的旋转对称性结果——加外磁场（Zeeman 效应）就把 $m$ 简并拆掉，谱线按 $\Delta m$ 分裂，与本篇的选择定则直接呼应。

**自旋轨道耦合（一句）**。原子实中电子感受到 $H_{SO} \propto \vec L\cdot\vec S$，此时 $L_z, S_z$ 不再是好量子数，但 $\vec J = \vec L + \vec S$ 是：$\vec L\cdot\vec S = \tfrac12(J^2 - L^2 - S^2)$，能级按 $j$ 分裂为精细结构。这正是第 6 节角动量相加的用武之地；严格而自动地给出它要靠 Dirac 方程（第 3、4 阶段）。

**QFT 前瞻**。本篇的全部语言——"对象按对称群的不可约表示分类、乘积态按 CG 系数分解、矩阵元按 Wigner–Eckart 分解"——在量子场论里整体升级：把旋转群换成 Lorentz 群（其双重覆盖 $\mathrm{SL}(2,\mathbb C)$ 对应这里的 SU(2)，见 stage-00 篇第 9 节），场算符按不可约表示分类为标量、旋量、矢量场；粒子的自旋就是其在旋转群下的表示标签；散射振幅、衰变角分布的分析用的仍是 CG 系数与 Wigner–Eckart 这一套。把本篇练熟，后面全是同构的套路。

## 小结

| 主题 | 关键结果 |
| --- | --- |
| 角动量算符 | $L_i = \epsilon_{ijk}x_jp_k$，由 $[x_i,p_j]=i\hbar\delta_{ij}$ 得 $[L_i,L_j]=i\hbar\epsilon_{ijk}L_k$ |
| 中心势 | $[H,L^2]=[H,L_z]=[L^2,L_z]=0$，$l, m$ 是好量子数 |
| 代数解法 | $j = 0, \tfrac12, 1, \dots$；$m=-j,\dots,j$；升降算符在链端终止 |
| 轨道角动量 | 本征函数 $Y_l^m$，单值性强制 $l$ 取整数；宇称 $(-1)^l$ |
| 自旋 1/2 | 旋量 $\chi\in\mathbb C^2$，$U=e^{-i\theta\hat n\cdot\vec\sigma/2}$，转 $2\pi$ 变号 |
| 角动量相加 | $\lvert JM\rangle = \sum C^{JM}_{j_1m_1j_2m_2}\lvert j_1m_1\rangle\lvert j_2m_2\rangle$；$\tfrac12\otimes\tfrac12 = 1\oplus0$ |
| Wigner–Eckart | 矩阵元 = CG 系数 × 约化矩阵元；E1 选择定则 $\Delta l=\pm1$，$\Delta m=0,\pm1$ |

## 自检问题

**1.** 只使用基本对易关系 $[x_i, p_j] = i\hbar\delta_{ij}$，验证 $[L_x, L_y] = i\hbar L_z$。

<details markdown="1"><summary>点击显示答案</summary>

写出 $L_x = yp_z - zp_y$、$L_y = zp_x - xp_z$，展开对易子：

$$[L_x, L_y] = [yp_z, zp_x] - [yp_z, xp_z] - [zp_y, zp_x] + [zp_y, xp_z].$$

逐项检查：$[yp_z, xp_z] = 0$（$p_z$ 与 $x$ 对易，$y$ 与所有项对易）；$[zp_y, zp_x] = 0$（$z$ 与 $p_y$ 对易，$p_x$ 与所有项对易）。剩下两项：

$$[yp_z, zp_x] = y\,[p_z, z]\,p_x = y(-i\hbar)p_x = -i\hbar\,yp_x,$$

$$[zp_y, xp_z] = x\,[z, p_z]\,p_y = x(i\hbar)p_y = +i\hbar\,xp_y.$$

代回（注意第二项前面带负号）：

$$[L_x, L_y] = -i\hbar\,yp_x + i\hbar\,xp_y = i\hbar\,(xp_y - yp_x) = i\hbar L_z. \qquad \blacksquare$$

</details>

**2.** 显式计算：$j=1$ 的三个态在绕 $z$ 轴转 $2\pi$ 下不变，而 $j=\tfrac12$ 的两个态变号。

<details markdown="1"><summary>点击显示答案</summary>

绕 $z$ 轴的转动算符为 $U_z(\theta) = e^{-i\theta J_z/\hbar}$。在 $J_z$ 本征态 $\lvert j,m\rangle$ 上：

$$U_z(\theta)\lvert j,m\rangle = e^{-i\theta m}\lvert j,m\rangle.$$

代入 $\theta = 2\pi$，相位因子为 $e^{-i2\pi m} = (-1)^{2m}$。

$j = 1$（$m = -1, 0, +1$，全为整数）：

$$e^{-i2\pi m} = e^{\pm i2\pi} = 1, \qquad e^{0} = 1,$$

三个态全部不变：$U_z(2\pi)\lvert 1,m\rangle = +\lvert 1,m\rangle$。

$j = \tfrac12$（$m = \pm\tfrac12$）：

$$e^{-i2\pi\cdot(1/2)} = e^{-i\pi} = -1, \qquad e^{-i2\pi\cdot(-1/2)} = e^{i\pi} = -1,$$

两个态都变号：$U_z(2\pi)\lvert\tfrac12, \pm\tfrac12\rangle = -\lvert\tfrac12, \pm\tfrac12\rangle$。一般结论：整数 $j$ 转 $2\pi$ 得 $+1$，半整数 $j$ 得 $-1$（与 stage-00 篇第 6.2 节的整体拓扑论证一致）。

</details>

**3.** 推导两个自旋 1/2 的耦合：$\tfrac12\otimes\tfrac12 = 1\oplus0$，把四个耦合态全部写出（即算出全部 CG 系数）。

<details markdown="1"><summary>点击显示答案</summary>

非耦合基：$\lvert\uparrow\uparrow\rangle$、$\lvert\uparrow\downarrow\rangle$、$\lvert\downarrow\uparrow\rangle$、$\lvert\downarrow\downarrow\rangle$，总 $S_z$ 本征值 $M = m_1+m_2$ 分别为 $+1, 0, 0, -1$。

最高权：$M=+1$ 唯一，故 $\lvert 1,1\rangle = \lvert\uparrow\uparrow\rangle$。

作用 $J_- = S_{1-}+S_{2-}$。由 $J_-\lvert j,m\rangle = \hbar\sqrt{j(j+1)-m(m-1)}\lvert j,m-1\rangle$：

$$J_-\lvert 1,1\rangle = \hbar\sqrt2\,\lvert 1,0\rangle = (S_{1-}+S_{2-})\lvert\uparrow\uparrow\rangle = \hbar\big(\lvert\downarrow\uparrow\rangle + \lvert\uparrow\downarrow\rangle\big),$$

得 $\lvert 1,0\rangle = \tfrac{1}{\sqrt2}\big(\lvert\uparrow\downarrow\rangle + \lvert\downarrow\uparrow\rangle\big)$。再降一次：

$$J_-\lvert 1,0\rangle = \hbar\sqrt2\,\lvert 1,-1\rangle = \frac{\hbar}{\sqrt2}\big(2\lvert\downarrow\downarrow\rangle\big) = \hbar\sqrt2\,\lvert\downarrow\downarrow\rangle,$$

即 $\lvert 1,-1\rangle = \lvert\downarrow\downarrow\rangle$。$M=0$ 子空间中与 $\lvert 1,0\rangle$ 正交的组合：

$$\lvert 0,0\rangle = \frac{1}{\sqrt2}\big(\lvert\uparrow\downarrow\rangle - \lvert\downarrow\uparrow\rangle\big).$$

验证 $J_+\lvert 0,0\rangle = \tfrac{\hbar}{\sqrt2}\big(\lvert\uparrow\uparrow\rangle - \lvert\uparrow\uparrow\rangle\big) = 0$，确为 $J=0$。全部 CG 系数：$C^{11}_{++}=1$；$C^{10}_{+-}=C^{10}_{-+}=\tfrac{1}{\sqrt2}$；$C^{1,-1}_{--}=1$；$C^{00}_{+-}=\tfrac{1}{\sqrt2}$、$C^{00}_{-+}=-\tfrac{1}{\sqrt2}$。维数 $4 = 3 + 1$。

</details>

**4.** 用 Wigner–Eckart 定理解释：为什么 $\sigma^-$ 偏振的光只驱动 $\Delta m = -1$ 的跃迁？

<details markdown="1"><summary>点击显示答案</summary>

光的圆偏振按携带的角动量分类：$\sigma^-$ 光沿传播方向（取 $z$ 轴）携带 $J_z = -\hbar$，对应电偶极算符的球分量 $q = -1$（$\sigma^+$ 对应 $q=+1$，线偏振 $\pi$ 对应 $q=0$）。偶极相互作用 $\vec r\cdot\vec E$ 中的相关算符是秩 1 张量分量 $r_{q=-1}$。

由 Wigner–Eckart 定理，吸收跃迁 $\lvert nlm\rangle \to \lvert n'l'm'\rangle$ 的振幅正比于

$$\langle n'l'm'\rvert\, r_{-1}\,\rvert nlm\rangle = C^{\,l'm'}_{l\,m\;1,-1}\times\langle n'l'\lVert r\rVert nl\rangle,$$

其中 CG 系数 $C^{\,l'm'}_{l\,m\;1,-1}$ 非零的必要条件是磁量子数"相加守恒"：

$$m' = m + q = m - 1, \qquad \text{即 } \Delta m = -1.$$

物理图像：$\sigma^-$ 光子带一个 $z$ 向 $-\hbar$ 的角动量，被原子吸收后总角动量守恒，原子的 $m$ 必须减少 1。同理 $\sigma^+$ 只驱动 $\Delta m = +1$、$\pi$ 偏振只驱动 $\Delta m = 0$。这是原子物理中选态、光抽运（optical pumping）的基础。

</details>

**5.** 用 $L_\pm$ 作用于 $Y_l^l$，证明 $L^2$ 在球谐函数 $Y_l^m$ 上的本征值是 $\hbar^2 l(l+1)$。

<details markdown="1"><summary>点击显示答案</summary>

先把 $L^2$ 用升降算符改写。由 $L_\pm = L_x \pm iL_y$ 及 $[L_x, L_y] = i\hbar L_z$：

$$L_-L_+ = L_x^2 + L_y^2 + i[L_x, L_y] = L^2 - L_z^2 - \hbar L_z,$$

即

$$L^2 = L_-L_+ + L_z^2 + \hbar L_z.$$

$Y_l^l$ 是 $L_z$ 本征值 $\hbar l$ 的态；又因为 $m=l$ 已是该多重态的最高值，升算符必须把它湮灭（这也可由第 4 节 $L_+$ 的坐标表示对 $Y_l^l \propto \sin^l\theta\,e^{il\varphi}$ 直接验证）：

$$L_+ Y_l^l = 0.$$

于是

$$L^2 Y_l^l = \underbrace{L_-L_+ Y_l^l}_{=\,0} + L_z^2 Y_l^l + \hbar L_z Y_l^l = \big(\hbar^2 l^2 + \hbar^2 l\big)\,Y_l^l = \hbar^2 l(l+1)\,Y_l^l.$$

而 $L^2$ 与 $L_\pm$ 对易（$[L^2, L_\pm]=0$），用 $L_-$ 把 $Y_l^l$ 逐级降到 $Y_l^m$ 不改变 $L^2$ 本征值，故对所有 $m = -l,\dots,l$：

$$L^2 Y_l^m = \hbar^2 l(l+1)\,Y_l^m. \qquad \blacksquare$$

注意本征值是 $l(l+1)$ 而非 $l^2$：因为 $L_x, L_y$ 与 $L_z$ 不对易，即使 $m=l$ 的态也有 $\langle L_x^2 + L_y^2\rangle = \hbar^2 l > 0$——角动量不可能完全"对准"某个轴，这是不确定性原理的体现。

</details>

## 参考

- Griffiths《量子力学概论》第 4 章：4.1（薛定谔方程分离变量）、4.3（角动量）、4.4.1–4.4.3（自旋 1/2、角动量相加）——本篇主线对应。
- Sakurai《现代量子力学》（修订版）第 3 章：3.1–3.3（对易关系、自旋 1/2、SO(3)/SU(2)）、3.5–3.8（CG 系数、张量算符与 Wigner–Eckart 定理）。
- Shankar《Principles of Quantum Mechanics》第 12 章（旋转不变性与角动量）、第 15 章（角动量相加）。
