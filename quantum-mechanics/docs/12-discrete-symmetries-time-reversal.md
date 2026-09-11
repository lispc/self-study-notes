# 分立对称性与时间反演：宇称、Wigner 定理与 Kramers 简并

> 路线图位置：量子力学书 · 第五部分（外场、对称性与几何相位）· 第 12 篇
> 前置知识：第 02 篇（群与表示、SU(2) 双覆盖——$T^2=\pm1$ 的根源）；第 03 篇（幺正算符、平移算符、测量公设）；第 05 篇（角动量与自旋、选择定则）；第 07s3 篇（宇称与好量子数的实战预热）。
> 学习目标：会说清对称性在量子力学里的含义（射线上的变换 + Wigner 定理：幺正或反幺正）与"连续对称给守恒量、分立对称给好量子数与选择定则"的分工；会把平移/宇称/旋转写成算符并读出守恒律（含晶格平移 → Bloch 定理的接口）；会用宇称推电偶极选择定则（Laporte 定则）；会证明时间反演算符必须**反幺正**、对半整数自旋 $T^2 = -1$，并完整证明 Kramers 简并定理；会解释为什么中性粒子的永久电偶极矩同时需要宇称与时间反演破坏——新物理实验的理论根基。
>
> 记号约定：保留 $\hbar$。宇称算符 $\Pi$（避免与动量 $P$ 混淆），时间反演算符 $\Theta$；复共轭算符 $K$。

---

## 1. 一句话总结

**量子力学里的对称性是"射线"上的变换，Wigner 定理保证它由幺正（连续对称、含恒等分支）或反幺正（含复共轭，只有时间反演一个物理实例）算符实现；连续对称的生成元是守恒量（$p,J,H$），分立对称则给好量子数与选择定则（宇称守恒 → Laporte 定则）；时间反演 $\Theta$ 因必须同时翻转 $\vec p$ 与 $\vec J$ 而被迫反幺正，对半整数自旋 $\Theta^2 = -1$——与 $2\pi$ 旋转取 $-1$ 同源（SU(2) 双覆盖），由此 Kramers 定理：奇数个电子 + 时间反演不变的哈密顿量，每条能级至少双重简并，任何电场都拆不开；而永久电偶极矩需要宇称与时间反演**同时**破缺——中子/电子 EDM 实验由此成为搜寻超出标准模型新物理的探针。**

## 2. 对称性在量子力学中的含义：Wigner 定理

量子态是**射线**（$|\psi\rangle$ 与 $e^{i\alpha}|\psi\rangle$ 是同一个态）。对称变换是射线到射线的一一映射，保持全部跃迁概率：

$$|\langle\phi\vert\psi\rangle|^2 = |\langle\phi'\vert\psi'\rangle|^2.$$

**Wigner 定理**：满足上式的射线映射必由态矢空间上的**幺正或反幺正**算符实现（差一个相位）。反幺正 = 幺正 × 复共轭 $K$，它反线性（$U_\Theta(c_1\psi_1+c_2\psi_2) = c_1^*U_\Theta\psi_1 + c_2^*U_\Theta\psi_2$）且反幺正（$\langle U\phi\vert U\psi\rangle = \langle\phi\vert\psi\rangle^*$）。

为什么只有这两类：幺正保持内积，反幺正取复共轭——线性 + "内积取复共轭"会与平行四边形恒等式矛盾（骨架见自检问题 1 的讨论）。**物理里的反幺正对称只有一个实例：时间反演**——原因是它不含恒等元的连续分支（$\Theta$ 不能"连续地"从恒等转过去），Wigner 定理的另一支（连续群同调到恒等）只允许幺正。

对称性与哈密顿量的关系统一写成

$$UHU^{-1} = H\quad(\text{对称})\ \Longleftrightarrow\ [U,H] = 0,$$

$U$ 幺正且连续（$U = e^{-i\varepsilon G/\hbar}$）时给守恒量 $[G,H]=0$（量子版诺特定理，第 02 篇）；$U$ 分立（$\Pi$、晶格平移、$\Theta$）时哈密顿量按其本征值分块对角——**好量子数**，选择定则由"算符的分立对称性要匹配两侧"读出。

## 3. 平移、旋转、晶格平移：连续与分立的分工

**平移**（第 03 篇已推导）：$T(a) = e^{-ipa/\hbar}$，$\Pi$（此处指动量）守恒；$[H,T(a)]=0\ \forall a$ ⇔ 动量守恒。

**旋转**：$R = e^{-i\vec\theta\cdot\vec J/\hbar}$，角动量守恒（第 05 篇）。

**晶格平移**（分立）：周期势 $V(x+a) = V(x)$ 下只剩 $T(a)$ 这一个**分立**对称——$[H, T(a)] = 0$，$T(a)$ 本征值 $e^{ika}$（幺正 + 平方序列回到自身），好量子数 $k$（布里渊区内）。能量本征态同时是晶格平移本征态 $\psi_k(x) = e^{ikx}u_k(x)$——**Bloch 定理**的对称性原文（完整展开见凝聚态书[能带理论](../../condensed-matter/docs/04-band-theory.md)：动量"守恒"降格为"模倒格矢守恒"，因为群只剩分立的一支）。

**旋转的分立子集**：$n$ 重旋转轴同样给分立好量子数（分子光谱的 $C_n$ 对称）。一句总纲：**连续对称给守恒流，分立对称给选择定则**。

## 4. 宇称：选择定则与弱相互作用的一票

宇称算符 $\Pi$：$\Pi^\dagger x \Pi = -x$、$\Pi^\dagger p \Pi = -p$，$\Pi^2 = 1$，本征值 $\pi = \pm1$（偶/奇）。坐标表象 $(\Pi\psi)(\vec r) = \psi(-\vec r)$。

**宇称守恒 ⇔ 好量子数**：$[\Pi,H]=0$（中心势、分子、电磁相互作用都满足）时每个本征态有确定宇称——球对称势中 $\pi = (-1)^l$。

**选择定则（Laporte）**：电偶极算符 $\vec d = q\vec r$ 是宇称奇的（$\Pi^\dagger\vec d\Pi = -\vec d$），故

$$\langle f\vert\vec d\vert i\rangle eq 0\ \Rightarrow\ \pi_f\pi_i = -1\qquad(\text{电偶极跃迁必须连接相反宇称})，$$

原子轨道上即 $\Delta l = \pm1$（第 05 篇 7.3 节的角动量版选择定则在此添上宇称注脚）。07s3 的 Stark 效应（线性项只在含相反宇称的简并子空间存活）用的同一条。

**宇称不守恒**：弱相互作用破坏宇称（吴健雄实验 1957，$\beta$ 衰变的左右不对称）；QFT 书标准模型一章中它与 CP 破坏一起进入 CKM 矩阵的叙事。量子力学教材层面记住一句话就够：**宇称是近似对称**——电磁与强作用里严格，弱作用里破缺，破缺幅度正是探测弱作用本性的旋钮。

## 5. 时间反演：为什么必须反幺正

经典对应：$t\to-t$ 时 $\vec r\to\vec r$、$\vec p\to-\vec p$、$\vec J\to-\vec J$。量子力学要求

$$\Theta^\dagger\,\vec r\,\Theta = \vec r,\qquad \Theta^\dagger\vec p\,\Theta = -\vec p.$$

**幺正实现不可能**（自检问题 2 的两行证明）：若 $\Theta$ 幺正，则 $\Theta^\dagger[x,p]\Theta = \Theta^\dagger(i\hbar)\Theta = i\hbar$（幺正不碰常数），但按变换规则 $= [x,-p] = -i\hbar$——矛盾。反幺正救场：复共轭把 $i\hbar\to -i\hbar$，两边恰好都是 $-i\hbar$ ✓。这就是 Wigner 定理的用武之地——时间反演**必须**落在反幺正那一支。

**自旋零**：$\Theta = K$（坐标表象直接取复共轭）。验证：$K x K = x$，$K(-i\hbar\nabla)K = +i\hbar\nabla = -p$ ✓；不含磁场的薛定谔方程（$H$ 实）在 $K$ 下不变。

**一般自旋**：$\Theta = e^{-i\pi J_y/\hbar}K$（绕 $y$ 轴转 $\pi$ 再取复共轭——转 $\pi$ 把 $J_z\to-J_z$，复共轭把 $J_y$ 的虚矩阵元翻号）。对自旋 1/2：

$$\Theta = -i\sigma_y\,K,$$

（$e^{-i\pi\sigma_y/2} = -i\sigma_y$。）两条核心性质（自检问题 3 验证）：$\Theta^\dagger\vec\sigma\Theta = -\vec\sigma$，以及

$$\boxed{\ \Theta^2 = (-1)^{2j}\ }\qquad(\text{整数自旋}\ +1,\ \text{半整数}\ -1).$$

**与 SU(2) 双覆盖会师**：$\Theta^2 = -1$ 与"$2\pi$ 旋转作用 $-1$"（第 02 篇）是同一个非平庸拓扑的两张面孔——半整数自旋的态生活在 SO(3) 的双覆盖上，绕两圈才回家。这是 Kramers 简并的群论根源。

**含磁场时的注意**：$\vec B$ 在时间反演下应变号（它是"外参量"）；若把磁场当作给定背景，$H(B)$ 满足 $\Theta H(B)\Theta^{-1} = H(-B)$——Kramers 定理因此只在 $B=0$（且无其他 $T$ 破坏场）时成立。

## 6. Kramers 定理

**定理**：$\Theta^2 = -1$（奇数个电子）且 $[\Theta, H] = 0$，则每条能级至少二重简并。

**证明**（两行，自检问题 4 完整走）：设 $H\lvert\psi\rangle = E\lvert\psi\rangle$，则 $H(\Theta\lvert\psi\rangle) = \Theta H\lvert\psi\rangle = E(\Theta\lvert\psi\rangle)$——$\Theta\lvert\psi\rangle$ 同能量。而 $\Theta^2=-1$ 强制 $\langle\psi\vert\Theta\psi\rangle = 0$——**正交**，是另一个独立的态。∎

简并不是"意外"（不像氢的 SO(4)），是**拓扑保护**的：任何不破坏时间反演的微扰（无论多强）都拆不开这对 Kramers 双重态。物理出场率极高：

- **奇电子原子的能级**（如 Ce³⁺，4f¹）：晶格电场拆掉轨道简并，却拆不掉 Kramers 对——光谱线的最少条数由它兜底。
- **能带论**：自旋-轨道耦合一般拆自旋简并，但在时间反演不变的动量点（TRIM，$\vec k$ 与 $-\vec k+\vec G$ 等价处）能带必成对（Kramers 对）——拓扑绝缘体的"体-边对应"在边界上的保护性交叉态正是 Kramers 对的表面版本（凝聚态书[拓扑物态](../../condensed-matter/docs/12-topological-phases.md)）。
- **散射与响应**：$T$ 不变 ⇒ $S$ 矩阵对称（$S_{fi} = S_{if}$，倒易定理），细致平衡（第 10 篇 Kubo 笔记中子散射的 $1/(1-e^{-\beta\omega})$ 因子）也以它为前提。

**时间反演破坏的可观测签名**：永久电偶极矩（EDM，自检问题 5）：非简并态若有非零 $\vec d$，则必须同时破坏 $\Pi$ 与 $\Theta$。标准模型的 CP 破坏（CKM）预言的中子 EDM $\sim10^{-31}\ e\cdot$cm，实验上限已压到 $\sim10^{-26}$——中间隔着五个数量级的新物理窗口。EDM 实验是新物理搜索里"最便宜的对撞机"（QFT 书[标准模型](../../qft-sm/docs/stage-06-standard-model/04-standard-model-lagrangian.md)一章的反常与 CP 部分接手细节）。

## 7. 小结

| 对称 | 算符 | 类型 | 后果 |
| --- | --- | --- | --- |
| 平移 | $e^{-ipa/\hbar}$ | 幺正连续 | 动量守恒 |
| 旋转 | $e^{-i\vec\theta\cdot\vec J/\hbar}$ | 幺正连续 | 角动量守恒 |
| 晶格平移 | $T(a)$, 本征值 $e^{ika}$ | 幺正分立 | Bloch 定理 |
| 宇称 $\Pi$ | $\psi(\vec r)\to\psi(-\vec r)$ | 幺正分立 | 好宇称、Laporte 定则；弱作用破缺 |
| 时间反演 $\Theta$ | $e^{-i\pi J_y/\hbar}K$ | **反幺正** | $\Theta^2=(-1)^{2j}$；Kramers 简并 |

一句话收束：连续对称给守恒量，分立对称给选择定则，而时间反演独占反幺正一支——复共轭不是数学装饰，是"$\vec p$ 与 $\vec J$ 同时翻号还要保住 $[x,p]=i\hbar$"的唯一解；半整数自旋的 $\Theta^2=-1$ 顺流而下，给世界留下任何电场都拆不开的简并对。

## 自检问题

**1.** 论证为什么保持跃迁概率的射线变换只能由幺正或反幺正算符实现（给出骨架：先证一维子空间映到一维子空间，再在正交基上比较内积的相位自由度）；并说明为什么物理中反幺正对称几乎只有时间反演一个实例。

<details markdown="1"><summary>点击显示答案</summary>

骨架（Wigner 定理证明的轮廓，细节见 Weinberg《量子力学讲义》§2.2）：

第一步，归一化：跃迁概率 $|\langle\phi\vert\psi\rangle|^2$ 在 $\phi=\psi$ 时为 1，故映射保归一化，$U\psi$ 的模长不变——线性性暂未建立，先在"射线"层面工作。

第二步，正交保持：$\langle\phi\vert\psi\rangle = 0\iff|\langle\phi\vert\psi\rangle|^2 = 0$，故正交关系被保持；映射把正交基送到正交基（同维空间）。

第三步，相位选择：设基 $\{e_n\}\to\{e'_n\}$。对一般叠加 $\psi = \sum_n c_ne_n$，概率 $|\langle e_n\vert\psi\rangle|^2 = |c_n|^2$ 决定了 $U\psi$ 在 $e'_n$ 上的系数模长 $|c'_n| = |c_n|$，只剩相位自由。利用任意两基矢间的跃迁概率 $|c_n^*c_m|$ 的保持，可以论证存在统一的相位约定使 $c'_n = e^{i\alpha}c_n$（幺正情形）或 $c'_n = e^{i\alpha}c_n^*$（反幺正情形）——正交基逐对比较时相位必须一致，否则某对概率对不上（这一步是证明的核心，用三个矢量的"平行四边形" $\psi = e_m + e_n$ 反复夹逼）。

第四步，叠加原理封闭：按上述两种形式延拓到全空间，得到线性幺正或反线性反幺正的 $U$。

为什么反幺正实例唯一：若对称群含一个能连续变形到恒等的分支（平移、旋转生成元的连续路径），群元 $U(\varepsilon)\to\mathbb 1$ 时 $U(\varepsilon)$ 必须幺正（恒等是幺正的，反幺正算符 $UK$ 永远离 $\mathbb 1$ 有"距离"：它把 $i\mathbb 1$ 映到 $-i\mathbb 1$）。时间反演没有这样的连续分支（"反转时间方向"是离散操作，$\Theta^2 = \pm1$ 直接到头），所以它是唯一能落在反幺正支的物理对称。（粒子-反粒子共轭 C 也是分立的，但它在量子力学单粒子层面不是射线的对称——它是场论操作，见 QFT 书。）

</details>

**2.** 证明不存在幺正算符同时满足 $U^\dagger xU = x$、$U^\dagger pU = -p$；验证 $\Theta = K$（无自旋）和 $\Theta = -i\sigma_yK$（自旋 1/2）都做到，且后者 $\Theta^2 = -1$。

<details markdown="1"><summary>点击显示答案</summary>

反证：设 $U$ 幺正。则 $U^\dagger[x,p]U = [U^\dagger xU,\ U^\dagger pU] = [x,-p] = -i\hbar$。但另一边 $U^\dagger[x,p]U = U^\dagger(i\hbar\mathbb 1)U = i\hbar\mathbb 1$（幺正算符不改变常数算符）。$i\hbar = -i\hbar$ 矛盾——幺正出局。

无自旋 $\Theta = K$（坐标表象）：$KxK^{-1} = x$（$x$ 是实乘法算符）；$KpK^{-1} = K(-i\hbar\nabla)K^{-1} = +i\hbar\nabla = -p$ ✓。$K$ 是反线性反幺正：$\langle K\phi\vert K\psi\rangle = \langle\phi\vert\psi\rangle^*$，恰好把对易关系的 $i\hbar$ 翻成 $-i\hbar$，两边都是 $-i\hbar$，自洽。不含磁场的 $H$（实势）满足 $KHK^{-1} = H$（若 $H$ 含复项如磁场 $\vec B\cdot\vec L$ 或规范势，则 $K$ 把它映到 $H(-\vec B)$）。

自旋 1/2 $\Theta = -i\sigma_yK$：先看 $-i\sigma_y = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ 是**实**矩阵。验证 $\Theta^\dagger\sigma_z\Theta$：反幺正地算 $K\sigma_zK = \sigma_z$（$\sigma_z$ 实），再 $(-i\sigma_y)\sigma_z(i\sigma_y)^\dagger\cdot$——具体地 $\Theta^\dagger\sigma_z\Theta = K^\dagger(i\sigma_y)\sigma_z(-i\sigma_y)K = K\,(\sigma_y\sigma_z\sigma_y)\,K = K(-\sigma_z)K = -\sigma_z$（用了 $\sigma_y\sigma_z\sigma_y = -\sigma_z$，中间系数 $(-i)(i) = 1$）。同理 $\sigma_x$（实）被 $K$ 保住再被共轭翻转，$\sigma_y$（虚）被 $K$ 直接翻号再被相似变换保住——三个分量都变号 ✓。

$\Theta^2$：$\Theta^2 = (-i\sigma_yK)(-i\sigma_yK) = (-i\sigma_y)(+i\sigma_y^*)K^2 = (-i\sigma_y)(-i\sigma_y)$·（$\sigma_y^* = -\sigma_y$）$= (-i\sigma_y)^2 = -\sigma_y^2 = -\mathbb 1$ ✓。（注意反线性算符乘法中 $K$ 携带的共轭作用在 $-i$ 上：$K(-i) = +i$，即第二个因子前的系数取共轭后再乘。）整数自旋 $j$：表示矩阵可取实（三维转动群本身是实正交群），$\Theta = K$（或等价地 $e^{-i\pi J_y}K$ 中 $e^{-i\pi J_y}$ 实），$\Theta^2 = +1$——一般结论 $\Theta^2 = (-1)^{2j}$。

</details>

**3.** 从 $\Theta = e^{-i\pi J_y/\hbar}K$ 出发推导一般公式 $\Theta^2 = (-1)^{2j}$，并用第 02 篇 SU(2) 双覆盖的语言解释它为什么与"$2\pi$ 旋转 = $-1$"同源。

<details markdown="1"><summary>点击显示答案</summary>

计算：$\Theta^2 = e^{-i\pi J_y/\hbar}K\,e^{-i\pi J_y/\hbar}K$。关键在标准角动量表象（$\lvert j,m\rangle$ 基，$J_z$ 对角）：此基下 $J_y = (J_+ - J_-)/2i$ 的矩阵元全虚，故

$$\big(e^{-i\pi J_y/\hbar}\big)^* = e^{+i\pi J_y^*/\hbar} = e^{-i\pi J_y/\hbar},$$

且 $K^2 = \mathbb 1$。于是

$$\Theta^2 = e^{-i\pi J_y/\hbar}\,\big(e^{-i\pi J_y/\hbar}\big)^*\ K^2 = e^{-i\pi J_y/\hbar}\,e^{-i\pi J_y/\hbar} = e^{-2\pi iJ_y/\hbar}.$$

最后一步认出主角：$e^{-2\pi iJ_y/\hbar}$ 是绕 $y$ 轴转 $2\pi$——**正是第 02 篇里 SU(2) 双覆盖的非平庸元素**，作用在自旋 $j$ 表示上为 $(-1)^{2j}\mathbb 1$：

$$\Theta^2 = (-1)^{2j}\,\mathbb 1.$$

同源解释：第 02 篇证明了半整数自旋的态是 SO(3) 的**投影表示**，真正的群是 SU(2)；在 SU(2) 里转 $2\pi$ 的群元是 $-\mathbb 1\ne\mathbb 1$，要转 $4\pi$ 才回到单位元。$\Theta^2$ 对半整数恰好也是 $-\mathbb 1$——同一枚"非平庸覆盖"硬币的两面：$\Theta$ 里藏着一次绕 $y$ 的 $\pi$ 转动，做两遍 $\Theta$ 就积出一个 $2\pi$ 转动，态所处的 SU(2) 扇区决定它是 $+1$ 还是 $-1$。Kramers 简并于是可以读成：**$\Theta$ 配对的两个态合起来才是覆盖群下的完整对象，大自然不允许只留一半**。（自旋 1/2 的直接矩阵验证见自检问题 2：$\Theta = -i\sigma_yK$ 中 $-i\sigma_y$ 是实矩阵，$\Theta^2 = (-i\sigma_y)^2 = -\mathbb 1$。）

</details>

**4.** 完整证明 Kramers 定理：$\Theta^2 = -1$、$[\Theta,H]=0$ ⇒ 与 $\lvert\psi\rangle$ 正交且同能量的 $\Theta\lvert\psi\rangle$ 存在；并用反例说明 $\Theta^2 = +1$（整数自旋/偶电子数）时无此保护。

<details markdown="1"><summary>点击显示答案</summary>

同能量：由 $[\Theta,H]=0$（注意 $\Theta$ 反线性，$H\Theta = \Theta H$ 照常成立），

$$H(\Theta\lvert\psi\rangle) = \Theta(H\lvert\psi\rangle) = \Theta(E\lvert\psi\rangle) = E^*\,\Theta\lvert\psi\rangle = E\,\Theta\lvert\psi\rangle$$

（$E$ 实）。故 $\Theta\lvert\psi\rangle$ 是同能量本征态。

正交性：利用反幺正算符的内积性质 $\langle\Theta\phi\vert\Theta\chi\rangle = \langle\chi\vert\phi\rangle$（复共轭翻转次序），取 $\phi = \chi = \psi$：

$$\langle\psi\vert\Theta\psi\rangle = \langle\Theta\Theta\psi\vert\Theta\psi\rangle^*\quad\text{不对，直接用}\ \Theta^2\text{：}\ \langle\psi\vert\Theta\psi\rangle = \langle\Theta^2\psi\vert\Theta\psi\rangle\ (\text{把一个 }\psi\text{ 写成 }\Theta^{-1}\Theta\psi).$$

规范走法：$\langle\psi\vert\Theta\psi\rangle = \langle\Theta^2\psi\vert\Theta\psi\rangle^*$ 的形式要小心；最稳的是对称平方：定义 $c \equiv \langle\psi\vert\Theta\psi\rangle$。由反幺正性 $\langle\Theta\psi\vert\Theta^2\psi\rangle = \langle\psi\vert\Theta\psi\rangle^* = c^*$，即 $\langle\Theta\psi\vert-\psi\rangle = c^*$，故 $c = \langle\psi\vert\Theta\psi\rangle = -c^*$。又 $c^* = \langle\Theta\psi\vert\psi\rangle = c$（厄米性交换），代入得 $c = -c$，故 $c = 0$：$\Theta\lvert\psi\rangle$ 与 $\lvert\psi\rangle$ 正交。∎

$\Theta^2 = +1$ 反例：无自旋粒子在任意势中 $\Theta = K$，$K^2 = 1$——非简并实波函数（如一维束缚态）满足 $K\psi = \psi$，"配对"塌缩成自己，无简并。偶数电子：总自旋整数个 $1/2$ 配对，$\Theta^2 = (+1)(-1)^{2J_{\rm tot}}$ 按 $J_{\rm tot}$ 整数给出 $+1$，Kramers 保护消失——晶格电场可以把偶电子离子（如 Dy²⁺ vs Dy³⁺）的简并拆到非简并，奇电子则永远至少二重：稀土离子光谱与磁性（凝聚态书[磁性](../../condensed-matter/docs/07-magnetism.md)的自旋-轨道章）的经典对照。

</details>

**5.** 证明：宇称 $\Pi$ 与时间反演 $\Theta$ 都是好对称时，非简并态的永久电偶极矩 $\vec d = q\langle\vec r\rangle$ 必为零；并说明 EDM 实验为什么因此能探测新物理。

<details markdown="1"><summary>点击显示答案</summary>

非简并态 $\lvert\psi\rangle$ 在 $[\Pi,H]=0$、$[\Theta,H]=0$ 下自动是 $\Pi$ 与 $\Theta$ 的本征态（一维表示没有别的选择）：$\Pi\lvert\psi\rangle = \pi\lvert\psi\rangle$，$\Theta\lvert\psi\rangle = e^{i\alpha}\lvert\psi\rangle$。

宇称之刀：$\vec d = q\vec r$ 是极矢量，$\Pi^\dagger\vec d\Pi = -\vec d$。于是 $\langle\vec d\rangle = \langle\psi\vert\vec d\vert\psi\rangle = \langle\psi\vert\Pi^{-1}\Pi\vec d\Pi^{-1}\Pi\vert\psi\rangle = -\langle\vec d\rangle$（本征值提出后 $\pi^*\pi = 1$）⇒ $\langle\vec d\rangle = 0$。

时间反演之刀：$\vec r$ 是 $\Theta$-偶的（$\Theta^\dagger\vec r\Theta = \vec r$），单独这一条不杀 $\vec d$；但非简并态若要有非零 $\vec d$，唯一能定义方向的算子是体系的 $\vec J$（各向同性下 $\vec d\parallel\vec J$），而 $\vec J$ 是 $\Theta$-奇的：$\langle\vec J\rangle eq 0$ 与 $\Theta$ 对称矛盾（$\langle\Theta\psi\vert\vec J\vert\Theta\psi\rangle = -\langle\psi\vert\vec J\vert\psi\rangle$，但 $\Theta\lvert\psi\rangle \propto \lvert\psi\rangle$ 非简并 ⇒ 期望值等于自己的负值 ⇒ 零）。故 $\vec d = c\,\langle\vec J\rangle = 0$。两条合起来：**非零 EDM 需要 $\Pi$ 与 $\Theta$ 同时破缺**（严格论证走 $\vec d\parallel\vec J$ 时左右两边的对称性标签不匹配：左 $\Pi$ 奇 $\Theta$ 偶，右 $\Pi$ 偶 $\Theta$ 奇）。

EDM 实验的逻辑：中子/电子/原子的 EDM 与标准模型 CP 破坏（CKM，隐含 $T$ 破坏 via CPT）预言同量级或更小（中子 $\sim10^{-31}\ e\,$cm），而当前实验上限 $\sim10^{-26}\ e\,$cm。任何在灵敏度内看到信号，都直接指向新的 $T/\Pi$ 破坏源——超出标准模型的物理（超对称、新标量 sector 等，QFT 书标准模型一章的 CP 部分）。"最便宜的高能实验"：一台精密光谱仪，审的是基本对称性的案子。

</details>

## 参考

- Sakurai《现代量子力学》第 4 章（对称性：宇称、时间反演与 Kramers 定理的标准讨论）——本篇主线来源。
- Shankar《Principles of Quantum Mechanics》对称性章——平移/旋转/宇称的算符化最细。
- Weinberg《Lectures on Quantum Mechanics》§2.2（Wigner 定理的完整证明）与诠释章节。
- 朗道《量子力学》时间反演与 Kramers 简并章节。
- 凝聚态书[第 12 章 拓扑物态](../../condensed-matter/docs/12-topological-phases.md)（Kramers 对与拓扑绝缘体）、[磁性](../../condensed-matter/docs/07-magnetism.md)（稀土离子与自旋-轨道）。
- QFT 书[标准模型拉氏量](../../qft-sm/docs/stage-06-standard-model/04-standard-model-lagrangian.md)（CP 破坏与 EDM 的场论侧）。
