# 补充材料：量子计算初步——线路、算法与纠错

> 路线图位置：量子力学书 · 尾声（测量、诠释与量子信息）· 第 14s 篇（[量子信息初步](14s-quantum-information.md)）的续篇（第 14s2 篇）
> 前置知识：第 14s 篇（Bloch 球、Bell 基、Pauli 门、no-cloning——本篇的零件库）；第 03 篇（幺正演化、测量）；第 05 篇（泡利矩阵的对易关系）；第 14 篇（退相干——噪声的物理来源）；第 13 篇（相位语言——QFT 一节的措辞基础）。
> 学习目标：会读写量子线路（门序列记号）、说明通用门集 $\{H,T,\mathrm{CNOT}\}$ 的地位；会完整推导 Deutsch–Jozsa 与 Grover（几何版）两个算法、给出 Shor 的结构地图（相位估计 + QFT，不逐门展开）；会说清"量子并行不是免费午餐"的确切含义；会推 3 比特纠错码的纠错子并解释"冗余编码进纠缠而非复制"；能把表面码认成凝聚态书的 toric code；会用 Trotter 分解解释量子模拟为什么是多体物理（而非密码学）的天然出口。
>
> 记号约定：$n$ 量子比特，计算基 $\lvert x\rangle$，$x\in\{0,1\}^n$，$N = 2^n$。线路无图（仓库约定），按**门序列从左到右作用**书写；$\mathrm{CNOT}(c\to t)$ 记控制位 $c$、目标位 $t$（目标位 $y\to y\oplus x$）；$\mathrm{H}$ 为 Hadamard 门；$x\cdot z$ 为比特串按位内积（mod 2）。

---

## 1. 一句话总结

**量子计算机 = 把问题编码进干涉结构的机器：线路模型（幺正门序列 + 末端测量）里唯一的非酉资源是测量，唯一的经典对应物是可逆逻辑；指数大的态空间 $2^n$ 并不自动有用——读出瓶颈逼着所有加速走同一条路：先把答案搬进相位（相位反演/相位估计），再用干涉把它读出来（Grover 平方加速、Shor 对周期结构指数加速）；噪声与退相干（第 14 篇）不是死刑，纠错把冗余编码进**关联**而非复制（no-cloning 禁止备份），表面码——当前硬件主流——正是凝聚态书里的 toric code；而 Feynman 发明它的原始动机从来不是分解大数，是模拟量子多体：给第 09 篇的指数墙开一扇门。**

## 2. 线路模型

**寄存器与门**：$n$ 比特态 $\sum_x c_x\lvert x\rangle$（$2^n$ 个幅度）；量子门 = 幺正算符，串联 = 矩阵乘积。三类积木：

- **单比特门 = Bloch 球旋转**（14s §2）：Pauli $X,Y,Z$（转 $\pi$）、$H = \tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$（基变换：$Z$ 基 $\leftrightarrow X$ 基，即 $\lvert0\rangle\leftrightarrow\lvert+\rangle$）、相位门 $S = \mathrm{diag}(1,i)$、$T = \mathrm{diag}(1,e^{i\pi/4})$。
- **双比特门 CNOT**：$\mathrm{CNOT}(1\to2)\lvert x\rangle_1\lvert y\rangle_2 = \lvert x\rangle_1\lvert y\oplus x\rangle_2$——唯一能造纠缠的门。

```text
制备 Bell 态 Φ⁺：
  |0⟩ ──H──●──   （控制位）
  |0⟩ ─────⊕──   （目标位）
终态 = (|00⟩ + |11⟩)/√2
```

- **测量**：非酉、不可逆、只在需要时用（末端或中途）——第 14 篇的坍缩公设在这里是算法资源。

**与经典计算的两处对表**：CNOT + 单比特门可以搭出 Toffoli（三比特受控受控非 = 可逆的 AND），而任意经典组合逻辑都能可逆化——量子线路的"经典子集"就是可逆逻辑（组合逻辑与可综合性的讨论见[数字电路书](../../digital-design/README.md)；量子线路多出来的只有一件事：**允许叠加存活**）。**通用性**：$\{H, T, \mathrm{CNOT}\}$ 以任意精度 $\varepsilon$ 逼近任何 $2^n$ 维幺正，门数仅多 $\mathrm{polylog}(1/\varepsilon)$（Solovay–Kitaev 定理，引用）——离散门集够用，这是硬件可实现性的前提。

**读出瓶颈**：测量 $n$ 比特只得 $n$ 经典比特。$2^n$ 个幅度是"描述的富"，不是"读出的富"——量子加速的全部艺术在于让不想要的幅度相消、想要的相长。下一节三个算法是这门艺术的三课。

## 3. 三个算法：按"读出机制"递进

### 3.1 Deutsch–Jozsa：全局性质压进一次干涉

**问题**：黑盒 $f:\{0,1\}^n\to\{0,1\}$，承诺是**常函数**（全 0 或全 1）或**平衡函数**（一半 0 一半 1），判定哪个。经典最坏要查 $2^{n-1}+1$ 次；量子 **1 次**。

**线路**：$\lvert0\rangle^{\otimes n}\lvert1\rangle\ \xrightarrow{\ H^{\otimes(n+1)}\ }\ \lvert\psi_0\rangle = \tfrac{1}{\sqrt{2^n}}\sum_x\lvert x\rangle\,\lvert-\rangle$；调用一次黑盒 $U_f\lvert x\rangle\lvert y\rangle = \lvert x\rangle\lvert y\oplus f(x)\rangle$，利用 $\lvert-\rangle$ 的相位反演技巧（自检问题 1）得 $\tfrac{1}{\sqrt{2^n}}\sum_x(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$；再对前 $n$ 比特施加 $H^{\otimes n}$，用

$$H^{\otimes n}\lvert x\rangle = \frac{1}{\sqrt{2^n}}\sum_z (-1)^{x\cdot z}\lvert z\rangle$$

算出全零基矢 $\lvert0\cdots0\rangle$ 的幅度：

$$a_0 = \frac{1}{2^n}\sum_x (-1)^{f(x)} = \begin{cases}\pm1 & f\ \text{常}\\[2pt] 0 & f\ \text{平衡}\end{cases}$$

（平衡时一半 $+1$ 一半 $-1$ 严格相消）。**测前 $n$ 比特：得全零 ⇔ 常函数**——单次查询、零误差。机制看清：黑盒把 $f$ 的信息写进**相位** $(-1)^{f(x)}$，Hadamard 变换把"相位里求和是否为零"变成"位置上是否测到全零"——干涉是相位到位置的翻译器。

### 3.2 Grover：二维子空间里的几何

**问题**：$N = 2^n$ 个条目，无结构（黑盒只告诉你"是不是目标 $\lvert w\rangle$"）。经典平均 $N/2$ 次查询；量子 $O(\sqrt N)$。

**两个反射**：初态 $\lvert\psi\rangle = H^{\otimes n}\lvert0\rangle = \tfrac{1}{\sqrt N}\sum_x\lvert x\rangle$。黑盒（相位反演）$O_w = \mathbb 1 - 2\lvert w\rangle\langle w\rvert$；扩散算子 $D = 2\lvert\psi\rangle\langle\psi\rvert - \mathbb 1$。 Grover 迭代 $G = D\,O_w$。整个演化被锁死在二维不变子空间 $\mathrm{span}\{\lvert w\rangle,\ \lvert w_\perp\rangle\}$（$\lvert w_\perp\rangle$ 为其余条目的均匀叠加）：

$$\lvert\psi\rangle = \sin\theta\,\lvert w\rangle + \cos\theta\,\lvert w_\perp\rangle,\qquad \sin\theta = \frac{1}{\sqrt N}.$$

**几何**（自检问题 2 完整走）：$O_w$ = 关于 $\lvert w_\perp\rangle$ 轴的镜面反射，$D$ = 关于 $\lvert\psi\rangle$ 的镜面反射；两次反射之积 = 旋转 $2\theta$。于是

$$G^k\lvert\psi\rangle = \sin\big((2k+1)\theta\big)\lvert w\rangle + \cos\big((2k+1)\theta\big)\lvert w_\perp\rangle,$$

转到 $\lvert w\rangle$ 上需要 $(2k+1)\theta \approx \pi/2$，即 $k \approx \dfrac{\pi}{4\sqrt N}$ 次——**平方加速**。

**诚实条款**：无结构搜索的查询复杂度下界是 $\Theta(\sqrt N)$（BBBV 定理，引用）——Grover 已是最优；平方加速把 $10^{16}$ 降到 $10^8$，但不把指数变多项式，**解不了 NP 完全问题**。"量子计算机擅长搜索"是流行读物最常越界的一句话。

### 3.3 Shor：结构地图（不逐门展开）

**分解 $N$ = 求阶**：随机取 $a$，找 $r$ 使 $a^r \equiv 1\ (\mathrm{mod}\ N)$（阶），则 $\gcd(a^{r/2}\pm1, N)$ 有概率给出非平凡因子（欧几里得算法收尾——全经典）。求阶是**周期问题**：函数 $a^x\bmod N$ 以 $r$ 为周期，经典只能逐点查。

**量子相位估计**（引擎）：$\lvert u_s\rangle = \tfrac{1}{\sqrt r}\sum_{k=0}^{r-1} e^{-2\pi isk/r}\lvert a^k\bmod N\rangle$ 是乘法算符 $U_a\lvert y\rangle = \lvert ay\bmod N\rangle$ 的本征态，本征值 $e^{2\pi is/r}$（$s = 0,\ldots,r-1$）——**阶 $r$ 藏在相位里**。线路：$n$ 比特寄存器 $\xrightarrow{H^{\otimes n}}$ 均匀叠加，受控 $U_a^{2^j}$ 把本征相位逐一乘上寄存器分量（相位打上），$\mathrm{QFT}^{\dagger}$ 把相位差翻译成寄存器位置（$\mathrm{QFT}\lvert j\rangle = \tfrac{1}{\sqrt{2^n}}\sum_k e^{2\pi ijk/2^n}\lvert k\rangle$ 的可逆使用，与 3.1 的 Hadamard 是同一门手艺的高维版；"相位语言"与第 13 篇 Berry 相位一脉相承——可观测的都是相位，读出的手段都是干涉）。测量得 $k_0 \approx 2^n s/r$，**连分数展开**（经典）恢复 $s/r$，即得 $r$。指数加速的来源：周期结构能被 QFT 压缩，而经典模拟必须逐点铺满 $2^n$。

**诚实的边界**：Shor 是对**有结构问题**（本征值/周期）的指数加速，不是对一般难解问题的通行证（§6）。

## 4. 噪声、纠错：把冗余编码进关联

**噪声模型**：环境耦合（第 14 篇 §3 的退相干）在算法视角下是**随机 Pauli 通道**：比特翻转 $X$（经典也有：0↔1）、相位翻转 $Z$（纯量子：叠加的仇家——退相干干的就是它，第 14 篇自检 4 的非对角元衰减）、以及 $Y\propto XZ$。

**两条绝路**：备份？no-cloning 禁止（14s §4）。多数表决（经典奇偶校验的思路）？测量会毁掉叠加——而叠加正是量子计算的资本。

**3 比特翻转码**：$\lvert0_L\rangle = \lvert000\rangle$，$\lvert1_L\rangle = \lvert111\rangle$（信息藏在**三者一致**这个关联里，不在任何单比特上）。纠错子（syndrome）：测集体观测量

$$S_1 = Z_1Z_2,\qquad S_2 = Z_2Z_3,$$

| $S_1S_2$ 读数 | 诊断 | 处置 |
| --- | --- | --- |
| $+1\,+1$ | 无错 | 不动 |
| $-1\,+1$ | 比特 1 被翻转 | 施加 $X_1$ |
| $-1\,-1$ | 比特 2 被翻转 | 施加 $X_2$ |
| $+1\,-1$ | 比特 3 被翻转 | 施加 $X_3$ |

关键机制（自检问题 4）：$\lvert0_L\rangle,\lvert1_L\rangle$ 都是 $S_1,S_2$ 的 $+1$ 本征态——**纠错子测量不区分逻辑 0/1**，叠加 $\alpha\lvert0_L\rangle+\beta\lvert1_L\rangle$ 安然无恙；错误（某个 $X_i$）才把态推出码空间，被 syndrome 精确定位、用 Pauli 修正拉回。**信息既没被测量（保护叠加）也没被复制（遵守 no-cloning），它住在关联里。** 相位错误 $Z$：把全线路套一层 $H$（$HZH = X$）即可复用同一套码；两害兼防的 9 比特 Shor 码是两层嵌套（一句话带过）。一般理论是 **stabilizer 形式**：码空间 = 一组对易 Pauli 算符（stabilizer 生成元）的公共 $+1$ 本征空间，纠错子读数 = 破坏者的指纹。

**表面码 = toric code**：把 stabilizer 铺到二维网格上——顶点星算符 $A_v = \prod_{e\supset v}\sigma^x_e$、面算符 $B_p = \prod_{e\subset\partial p}\sigma^z_e$——这**正是**凝聚态书[拓扑序](../../condensed-matter/docs/12s-topological-order.md)里的 toric code（Kitaev）。逻辑量子比特编码在网格的拓扑里：逻辑 $\bar Z$（$\bar X$）是不可收缩的 $\sigma^z$（$\sigma^x$）链，任意**局域**错误（有限个 Pauli）只能产生可收缩链 = stabilizer 等价类，动不了逻辑态；码距 = 系统尺寸，错误率低于阈值（数值 $\sim1\%$）时增大网格**指数**压制逻辑错误率。两条书线在此会师：凝聚态书用 toric code 讲拓扑序与任意子，本篇用同一只猫护住量子比特——**拓扑保护**是"体-边对应"的工程方言。阈值定理（一句话）：物理错误率低于阈值时，任意长计算可被 $\mathrm{polylog}$ 开销的纠错保护——量子计算的工程可行性判据。

## 5. 量子模拟：Feynman 的原始动机

1982 年 Feynman 的问题：模拟一般 $n$ 自旋系统要存 $2^n$ 个复数（第 09 篇的 $\binom{M}{N}$ 指数墙，凝聚态书精确方法一章的 "$N=50$ 已 $10^{29}$"）——**经典计算机跟不上量子力学**。反过来：量子系统的自由度天生就是指数的，**用量子系统模拟量子系统**只欠"可编程"。

**Trotter 分解**：演化算符按哈密顿量拆项轮流实现，

$$e^{-i(A+B)t} = \lim_{n\to\infty}\Big(e^{-iAt/n}e^{-iBt/n}\Big)^{n},$$

把 $H = \sum_k h_k$（各项都是"简单"的两比特项，如 Hubbard 模型的跳迁与在位排斥，第 09 篇 §7）逐项转成短门序列，误差随步数多项式收窄。**实现现场**：冷原子光晶格里的玻色/费米 Hubbard 模拟、离子阱的自旋链——凝聚态书[强关联](../../condensed-matter/docs/13-strong-correlations.md)一章梦寐以求的"实验台上的模型系统"。

**变分量子本征求值器（VQE）**：把第 07s 篇的变分原理原样搬上量子线路——ansatz $\lvert\psi(\theta)\rangle$ 由参数化门序列携带，能量 $E(\theta) = \langle\psi(\theta)\rvert H\lvert\psi(\theta)\rangle$ 由线路测量（$H$ 展开成 Pauli 字符串逐项测，正是第 10 篇"可观测量都是关联函数"的有限维版），经典优化器调 $\theta$。Ritz 方法 + 线路 ansatz：量子计算的第一批化学应用（分子基态）就长在本书 07s 的地基上。

## 6. 边界与诚实清单

- **不超光速**：线路全程幺正 + 局域测量，no-signaling 照常生效（14s 自检 3）。
- **量子并行 ≠ 免费午餐**：$2^n$ 条支路同时演化，但读出只有 $n$ 比特——有用的算法必须构造性相消（DJ/Grover/Shor 的全部技巧）。"量子计算机同时试所有答案"是流行说法的头号错误。
- **BQP 与 NP**：量子多项式时间类 BQP 与 NP-complete 的包含关系**未知**；已知 factoring ∈ BQP，Grover 最优且只是平方加速。任何"量子计算机将攻克一切难解问题"的句子都应触发警报。
- **指数加速需要结构**：周期/本征值（QFT 能压缩的东西）。无结构问题至多平方加速。
- **工程现状**：噪声、纠错开销、阈值以下的物理错误率是当下的军备竞赛——原理已清（阈值定理），工程在路上。

## 7. 接口

- **第 14s 篇**：Bloch 球、Bell 基、Pauli、no-cloning 是本篇的全部零件。
- **第 14 篇**：退相干的微观机制（自检 4）就是本篇的相位噪声通道；测量的边界问题被工程化为"测量资源"。
- **第 13 篇**：相位估计与 Berry 相位共享"物理在相位里、读出靠干涉"的世界观。
- **第 07s / 10 / 09 篇**：VQE = 变分法的线路版；可观测量测量 = Kubo 的有限维表亲；Trotter 模拟的对象 = 二次量子化的标准哈密顿量。
- **凝聚态书**：表面码 ↔ toric code（12s）；拓扑保护 ↔ 体-边对应（12）；量子模拟器 ↔ 强关联（13）、精确方法的指数墙（14）。
- **数字电路书**：可逆逻辑是量子线路的经典子集——"可综合"的量子版边界。

## 小结

| 概念 | 内容 | 备注 |
| --- | --- | --- |
| 线路模型 | 幺正门 + 末端测量；$\{H,T,\mathrm{CNOT}\}$ 通用 | Solovay–Kitaev |
| 读出瓶颈 | $2^n$ 幅度 → $n$ 比特 | 加速必须靠干涉 |
| Deutsch–Jozsa | 相位求和 $\to$ 全零测量 | 1 次查询定全局性质 |
| Grover | 两次反射 = 旋转 $2\theta$，$k\approx\tfrac{\pi}{4}\sqrt N$ | 平方加速且最优 |
| Shor | 阶 $\to$ 本征相位 $\to$ QFT 读出 $\to$ 连分数 | 结构性指数加速 |
| 纠错 | 冗余编码进关联（$S_1S_2$ 纠错子） | no-cloning 之下的唯一路 |
| 表面码 | 星/面 stabilizer = toric code | 拓扑保护，阈值 $\sim1\%$ |
| 量子模拟 | Trotter + VQE | Feynman 的原始动机 |

一句话收束：量子计算的物理内核只有一句话——**答案住进相位，干涉负责搬家**；其余全是工程：把相位护住（纠错，编码进关联）、把相位列队（线路，通用门集）、把相位用对地方（算法，找有结构的问题）。而它最初与最终的理由，都是让量子力学模拟它自己。

## 自检问题

**1.** 推导 Deutsch–Jozsa：证明相位反演技巧 $U_f(\lvert x\rangle\lvert-\rangle) = (-1)^{f(x)}\lvert x\rangle\lvert-\rangle$；从 $\lvert0\rangle^{\otimes n}\lvert1\rangle$ 出发走完全部线路，证明测得全零 ⇔ 常函数（概率 1）。

<details markdown="1"><summary>点击显示答案</summary>

相位反演：$\lvert-\rangle = (\lvert0\rangle-\lvert1\rangle)/\sqrt2$。

$$U_f\lvert x\rangle\lvert-\rangle = \tfrac{1}{\sqrt2}\big(\lvert x\rangle\lvert f(x)\rangle - \lvert x\rangle\lvert f(x)\oplus1\rangle\big) = \tfrac{1}{\sqrt2}\lvert x\rangle\big(\lvert f(x)\rangle - \lvert f(x)\oplus1\rangle\big).$$

若 $f(x) = 0$：括号 $= \lvert0\rangle-\lvert1\rangle = \lvert-\rangle$；若 $f(x) = 1$：括号 $= \lvert1\rangle-\lvert0\rangle = -\lvert-\rangle$。统一为 $(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$ ✓——辅助比特把函数值"踢进相位"（相位反演，phase kickback）。

全流程：$H$ 把辅助比特置 $\lvert-\rangle$（$H\lvert1\rangle = \lvert-\rangle$）、前 $n$ 比特置均匀叠加；一次 $U_f$ 后前 $n$ 比特为 $\tfrac{1}{\sqrt{2^n}}\sum_x(-1)^{f(x)}\lvert x\rangle$。再施 $H^{\otimes n}$，用 $H^{\otimes n}\lvert x\rangle = 2^{-n/2}\sum_z(-1)^{x\cdot z}\lvert z\rangle$：

$$\lvert\psi_{\rm out}\rangle = \sum_z\Big(\frac{1}{2^n}\sum_x(-1)^{f(x)+x\cdot z}\Big)\lvert z\rangle,\qquad a_{z} = \frac{1}{2^n}\sum_x(-1)^{f(x)+x\cdot z}.$$

$z = 0$ 时 $a_0 = 2^{-n}\sum_x(-1)^{f(x)}$：常函数（全 0 或全 1）时 $a_0 = \pm1$，其余幅度为零（幺正保归一，全概率集中在 $\lvert0\cdots0\rangle$）；平衡时一半 $+$ 一半 $-$，$a_0 = 0$，全零概率为零。单次测量零误差判定 ✓。物理要点：判定的是**全局性质**（函数值整体求和），量子一次拿到，经典必须抽样 $2^{n-1}+1$ 个点才能排除另一种可能。

</details>

**2.** Grover 几何：证明 $O_w$ 与 $D = 2\lvert\psi\rangle\langle\psi\rvert-\mathbb1$ 各是二维子空间里的镜面反射、$G = DO_w$ 为旋转 $2\theta$；推导迭代次数 $k\approx\tfrac{\pi}{4}\sqrt N$；并验证 $N=4$ 时一次迭代精确成功。

<details markdown="1"><summary>点击显示答案</summary>

反射判据：算符 $R_{\lvert v\rangle} = \mathbb1 - 2\lvert v\rangle\langle v\rvert$ 满足 $R\lvert v\rangle = -\lvert v\rangle$、对与 $\lvert v\rangle$ 正交的矢量不动——镜面（法向 $\lvert v\rangle$）反射。$O_w = \mathbb1 - 2\lvert w\rangle\langle w\rvert$：镜面法向 $\lvert w\rangle$，即"关于 $\lvert w_\perp\rangle$ 轴反射"。$D = 2\lvert\psi\rangle\langle\psi\rvert - \mathbb1 = -(\mathbb1 - 2\lvert\psi\rangle\langle\psi\rvert)$：差一个整体 $-1$（全局相位不可观），即关于 $\lvert\psi\rangle$ 为法向的镜面反射，镜面过 $\lvert\psi\rvert$ 与原点的"平面"。

几何定理：两镜面夹角 $\alpha$ 的两次反射复合 = 旋转 $2\alpha$。这里第一镜面法向 $\lvert w\rangle$、第二镜面法向 $\lvert\psi\rangle$，$\lvert\psi\rangle$ 与 $\lvert w\rangle$ 夹角 $\tfrac\pi2-\theta$，故 $G = DO_w$ = 旋转 $2(\tfrac\pi2-\theta)\equiv -2\theta\bmod 2\pi$——即向 $\lvert w\rangle$ 方向转 $2\theta$。每迭代一次转 $2\theta$，$k$ 次后幅角 $(2k+1)\theta$。

转到 $\lvert w\rangle$：$(2k+1)\theta = \tfrac\pi2 \Rightarrow k = \tfrac{\pi}{4\theta} - \tfrac12 \approx \tfrac{\pi}{4}\sqrt N$（小 $\theta \approx \sin\theta = 1/\sqrt N$）。

$N=4$：$\sin\theta = \tfrac12$，$\theta = \tfrac\pi6$；$k=1$：$(2\cdot1+1)\cdot\tfrac\pi6 = \tfrac\pi2$——态精确落在 $\lvert w\rangle$ 上，成功概率 1（著名的最巧配置，双比特两格搜索一次命中）。大 $N$ 时不能精确到 $\tfrac\pi2$，多算半步过冲、少算欠步，最优停点附近失败概率 $O(1/N)$。

</details>

**3.** 相位估计核心：证明若 $U\lvert u\rangle = e^{2\pi i\varphi}\lvert u\rangle$ 且 $\varphi = j_*/2^n$（$n$ 比特可精确表示），则"均匀叠加 + 受控 $U^{2^k}$ + $\mathrm{QFT}^{\dagger}$"线路以概率 1 测得 $j_*$。

<details markdown="1"><summary>点击显示答案</summary>

三步态矢量：寄存器 $\xrightarrow{H^{\otimes n}}\ \tfrac{1}{\sqrt{2^n}}\sum_{j=0}^{2^n-1}\lvert j\rangle\otimes\lvert u\rangle$；受控 $U^{j}$（按二进制位 $2^k$ 的受控门叠加而成，$j = \sum_k j_k2^k$）逐位积累相位：$\tfrac{1}{\sqrt{2^n}}\sum_j e^{2\pi ij\varphi}\lvert j\rangle\otimes\lvert u\rangle$（本征态纹丝不动，只捡相位）；末态对第一寄存器施 $\mathrm{QFT}^{\dagger}$。代入 $\varphi = j_*/2^n$：

$$\sum_j e^{2\pi ijj_*/2^n}\lvert j\rangle = \sqrt{2^n}\;\mathrm{QFT}\lvert j_*\rangle\qquad\Big(\mathrm{QFT}\lvert j_*\rangle = \tfrac{1}{\sqrt{2^n}}\sum_j e^{2\pi ij_*j/2^n}\lvert j\rangle\Big)，$$

故 $\mathrm{QFT}^{\dagger}$ 把它精确映回 $\lvert j_*\rangle$——概率 1 读出。一般 $\varphi = s/r$ 不能整除 $2^n$ 时输出集中在最近的整数附近（宽度 $O(1)$），测得 $k_0$ 后用连分数展开恢复 $s/r$（经典后处理），Shor 的阶 $r$ 到手。与 3.1 的 Hadamard 对照：$\mathrm{QFT}$ 就是"多比特傅里叶基变换"，Hadamard 是它的 $n=1$ 情形——把相位差翻译成位置，是全篇反复出现的那一手。

</details>

**4.** 3 比特码：验证 $\lvert0_L\rangle = \lvert000\rangle$ 与 $\lvert1_L\rangle = \lvert111\rangle$ 都是 $S_1 = Z_1Z_2$、$S_2 = Z_2Z_3$ 的 $+1$ 本征态；列出单比特翻转后四组 $(S_1,S_2)$ 读数；证明 syndrome 测量不破坏叠加 $\alpha\lvert0_L\rangle+\beta\lvert1_L\rangle$，且纠错后的态（含可能的翻转与修正）与初态完全一致。

<details markdown="1"><summary>点击显示答案</summary>

本征值：$Z_iZ_j$ 对三同号比特恒 $+1$：$000$（每个 $Z$ 本征值 $+1$）与 $111$（每个 $-1$，乘积仍 $+1$）都给 $S_1 = S_2 = +1$ ✓。

错误后的 syndrome（以翻转后的态为准，$Z$ 作用在翻转比特上变号）：$X_1$：态 $\lvert100\rangle$ 类，$S_1 = (-1)(+1) = -1$、$S_2 = +1$；$X_2$：$S_1 = -1$、$S_2 = -1$；$X_3$：$S_1 = +1$、$S_2 = -1$；无错：$(+,+)$。四组读数两两不同——精确定位（即正文表格）。

叠加保护：设初态 $\alpha\lvert0_L\rangle+\beta\lvert1_L\rangle$，发生 $X_1$：

$$\alpha\lvert100\rangle + \beta\lvert011\rangle = \big(\alpha\lvert0_L\rangle+\beta\lvert1_L\rangle\big)\text{ 经 } X_1.$$

$S_1,S_2$ 对 $\lvert100\rangle,\lvert011\rangle$ 给出**相同**读数 $(-,+)$（错误是集体观测量可看见的，逻辑信息是它看不见的）——测量投影到整个"错误子空间"而非劈开 $\alpha,\beta$，测后态不变（已是 $(S_1,S_2)$ 本征态组合）。按 syndrome 施 $X_1$：$\alpha\lvert000\rangle+\beta\lvert111\rangle$ 完整回归，$\alpha\beta$ 相干无损。两个码字的 Hamming 距离 3 = 单错后的态仍在各自"错误球"内、互不混淆（距离 $2t+1$ 可纠 $t$ 个错，与经典码同账）。最后把 no-cloning 线连上：若试图用"备份"纠错（$\lvert\psi\rangle\to\lvert\psi\rangle\lvert\psi\rvert$）对任意 $\alpha,\beta$ 成立，正是 14s 自检 2 排除的操作；3 比特码绕开它——逻辑比特信息在**三个比特的关联**里，每个单比特的约化密度矩阵都是 $\tfrac12\mathbb1$，与 14s 的纠缠熵语言严丝合缝：**备份是复制态，编码是共享关联**。

</details>

**5.** 从 stabilizer 定义出发说明 toric code（表面码）的逻辑比特：码空间 = 所有星算符 $A_v$ 与面算符 $B_p$ 的公共 $+1$ 本征空间；证明沿两条不可收缩道路的链算符 $W_z$（$\sigma_z$ 链）与 $W_x$（对偶 $\sigma^x$ 链）相互反对易，而任何有限个局域 Pauli 错误都无法实现 $W_z$ 的作用——逻辑态被拓扑保护。

<details markdown="1"><summary>点击显示答案</summary>

码空间：$A_v = \prod_{e\supset v}\sigma^x_e$、$B_p = \prod_{e\subset\partial p}\sigma^z_e$ 相互对易（每对 $A_vB_p$ 共享偶数条边，$\sigma^x\sigma^z$ 的反号成对出现），公共本征空间良定义；取全体 $+1$ 的分支为码空间（网格上每条边一个自旋 $\tfrac12$）。

链算符：$W_z(\gamma) = \prod_{e\in\gamma}\sigma^z_e$（$\gamma$ 为格上一条闭合/开放道路），$W_x(\gamma^*) = \prod_{e\in\gamma^*}\sigma^x_e$（$\gamma^*$ 为对偶格道路）。两条**不可收缩**道路（环面上两个手柄方向；平面表面码换成连接两类边界的道路）$\gamma_1,\gamma_2^*$ 恰好**相交奇数次**：每相交一条边贡献一对 $\sigma^z\sigma^x\cdots\sigma^x\sigma^z \to -1$，奇数次相交总反号——$W_x(\gamma_2^*)W_z(\gamma_1) = -W_z(\gamma_1)W_x(\gamma_2^*)$，两者都不是 stabilizer（stabilizer 与一切码内算符对易），却都保持码空间（$W$ 与每个 $A_v,B_p$ 对易：闭合链穿过每个顶点/面偶数次）。结论：$W_z$ 与 $W_x$ 是一对作用在码空间上的"逻辑 Pauli"——环面上 $4 = 2^2$ 维简并 = 两个逻辑量子比特（凝聚态书 12s 从拓扑序角度讲同一简并）。

拓扑保护：任何局域错误 = 有限个 Pauli 的乘积 = "短链"。短 $\sigma^x$ 链要么闭合（= 面算符乘积，stabilizer，码内恒等），要么端点落在两个格点——它是开链，端点即 $A_v = -1$ 的**任意子激发**（12s 的电荷激发），不与 $W_z$ 反对易（与 $W_z$ 相交次数为偶）；要实现逻辑翻转必须让 $\sigma^x$ 链与 $W_z$ 相交奇数次，即**横穿整个系统**——长度 $\sim L$ 的错误链，概率随 $L$ 指数压低（每比特独立错误率 $\varepsilon$ 时 $\sim\varepsilon^{L/2}$ 级）。码距随尺寸增长、逻辑错误率指数下降：这就是"拓扑保护"，与凝聚态书第 12 章"体-边对应"共享同一个拓扑骨架——一边护量子比特，一边护物态边界。

</details>

## 参考

- Nielsen & Chuang 第 4 章（量子线路与通用性）、第 5–6 章（QFT、相位估计、Shor、Grover）、第 10 章（量子纠错与 stabilizer 码）。
- Preskill《Quantum Computation》讲义（Caltech Ph219）第 5–7 章——Grover 几何与纠错的物理讲法。
- Feynman, *Int. J. Theor. Phys.* **21**, 467 (1982)——量子模拟的原始动机。
- Kitaev, *Ann. Phys.* **303**, 2 (2003)（toric code）；Fowler et al., *Phys. Rev. A* **86**, 032324 (2012)（表面码工程）。
- 本书第 14s 篇（[量子信息初步](14s-quantum-information.md)）、第 14 篇（退相干）、第 13 篇（相位语言）；凝聚态书[拓扑序](../../condensed-matter/docs/12s-topological-order.md)（toric code 的拓扑序叙事）、[精确方法](../../condensed-matter/docs/14-exact-methods-fci-ed.md)（指数墙）；[数字电路书](../../digital-design/README.md)（可逆逻辑的经典侧）。
