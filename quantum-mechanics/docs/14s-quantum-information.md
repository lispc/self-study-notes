# 补充材料：量子信息初步——纠缠作为资源

> 路线图位置：量子力学书 · 尾声（测量、诠释与量子信息）· 第 14 篇（[测量、EPR 与 Bell](14-measurement-epr-bell.md)）的补充材料（第 14s 篇）
> 前置知识：第 03 篇（测量公设、第 8 节密度矩阵与约化密度矩阵、第 9 节张量积）；第 05 篇（泡利矩阵）；第 05s 篇（自旋单态——本篇的标准纠缠载体）；第 14 篇（Bell 不等式与 no-signaling——本篇把它当工具用）。
> 学习目标：会把一般量子比特态画在 Bloch 球上、用 $\operatorname{Tr}\rho^2$ 区分纯混态；会陈述并证明 Schmidt 分解，用纠缠熵 $S = -\operatorname{Tr}\rho_A\log_2\rho_A$ 给二分纯态的纠缠记账；会证明 no-cloning 定理并说清它与 no-signaling 的互锁；会完整推导密集编码、隐形传态两个协议的代数，并论证隐形传态不违反 no-cloning 也不超光速；会按 BB84 与 E91 两个协议解释量子密钥分发的安全性来源。
>
> 记号约定：保留 $\hbar$（本篇几乎不用）。熵取 $\log_2$，单位比特。两比特 Bell 基：$\lvert\Phi^\pm\rangle = (\lvert00\rangle\pm\lvert11\rangle)/\sqrt2$，$\lvert\Psi^\pm\rangle = (\lvert01\rangle\pm\lvert10\rangle)/\sqrt2$；$\lvert\pm\rangle = (\lvert0\rangle\pm\lvert1\rangle)/\sqrt2$。

---

## 1. 一句话总结

**把量子态当作信息载体，叠加原理与张量积结构立刻制造出经典信息论里没有的两件事：未知量子态不能复制（no-cloning——线性性的直系结论），而复合系统的纠缠不能分解成各方的局域属性（Bell 判定，第 14 篇）；于是纠缠升格为一种可以计量（Schmidt 分解与纠缠熵）、可以转移（隐形传态）、可以放大带宽（密集编码）、也最怕被人偷看（QKD）的"资源"——三张名片协议每个都是十几行代数，但每张都只在一件事上动真格：把"纠缠是物理实在"这句哲学断言换成可运行的技术。**

本篇不讲工程（探测器、光纤、单光子源），只讲量子力学自己长出来的信息论骨架。

## 2. 量子比特与 Bloch 球

**量子比特**（qubit）= 二维希尔伯特空间：$\mathcal H_2$。计算基 $\{\lvert0\rangle, \lvert1\rangle\}$（任何物理二能级：自旋、偏振、能级……）。一般纯态

$$\lvert\psi\rangle = \cos\tfrac\theta2\,\lvert0\rangle + e^{i\varphi}\sin\tfrac\theta2\,\lvert1\rangle\quad\Longleftrightarrow\quad \rho = \tfrac12\big(\mathbb 1 + \vec r\cdot\vec\sigma\big),\ \ \lvert\vec r\rvert = 1,\ (\theta,\varphi)\ \text{球坐标}.$$

三个读法：

- **纯态 = Bloch 球面，混态 = 球内**：判据 $\operatorname{Tr}\rho^2 = \tfrac12(1+\lvert\vec r\rvert^2)$，纯态取 1、混态小于 1（第 03 篇 §8 的" indispensable"判据在此几何化）。正交的两态是**对径点**（$\lvert0\rangle$ 与 $\lvert1\rangle$、$\lvert+\rangle$ 与 $\lvert-\rangle$ 各为一对）——注意"对径"而不是"垂直"，与直觉图像的区别本身就是量子几何的第一课。
- **测量 = 沿某轴投影**：测 $\vec a\cdot\vec\sigma$，得 $\pm1$ 的概率 $\tfrac12(1\pm\vec a\cdot\vec r)$；测后态坍缩到该轴上。非正交态（球面上不正对径的两点）**不可靠地区分**——单次测量不可能同时以概率 1 判别两个非正交态，这条"朴素"事实是 QKD 安全性的全部来源（§5）。
- **操作 = 旋转**：幺正变换把 $\vec r$ 绕某轴转某角（$\rho$ 与 $\vec\sigma$ 的伴随作用即 $\mathrm{SO}(3)$ 旋转，第 05 篇）。单比特门=转动，是第 14s2 篇线路模型的几何底座。

$n$ 个量子比特：$\mathcal H_2^{\otimes n}$，维数 $2^n$，基矢 $\lvert x\rangle$（$x\in\{0,1\}^n$）——指数大的态空间，指数大的麻烦与机遇（14s2 §2）。

## 3. Schmidt 分解与纠缠熵：给纠缠记账

第 03 篇 §9 说过：一般二分态不能写成乘积——纠缠。现在给它一把**尺子**。

**Schmidt 分解**（证明见自检问题 1）：任何二分纯态 $\lvert\psi\rangle\in\mathcal H_A\otimes\mathcal H_B$ 都可选基写成

$$\lvert\psi\rangle = \sum_k \sqrt{\lambda_k}\,\lvert k\rangle_A\lvert k'\rangle_B,\qquad \lambda_k \ge 0,\ \ \sum_k\lambda_k = 1,$$

其中 $\lambda_k$ 恰是约化密度矩阵 $\rho_A = \operatorname{Tr}_B\lvert\psi\rangle\langle\psi\rvert$ 的本征值（也是 $\rho_B$ 的本征值——**纠缠对双方对称**）。**纠缠熵**：

$$\boxed{\ S(\lvert\psi\rangle) \equiv S(\rho_A) = -\sum_k\lambda_k\log_2\lambda_k = -\operatorname{Tr}\rho_A\log_2\rho_A\ }$$

三条性质立即可读：

1. $S = 0 \iff$ 只有一个 $\lambda_k = 1$ $\iff$ 直积态（无纠缠）；
2. $d_A = d_B = 2$ 时最大 $S = 1$ 比特，取遍 $\lambda = (\tfrac12,\tfrac12)$——**Bell 态是最大纠缠态**（05s 的单态正是其一）；
3. 整体纯态（$\operatorname{Tr}\rho_{AB}^2 = 1$）而局部混态（$S>0$）——纠缠的签名。"局域看见的混度 = 全局藏着的纠缠"，这句话在多体物理里长成面积律与拓扑纠缠熵（凝聚态书[拓扑序](../../condensed-matter/docs/12s-topological-order.md)：纠缠熵从"疑难"变"序参量"）。

**关联 ≠ 纠缠**（自检问题 5 的主角）：混态 $\rho_{\rm corr} = \tfrac12\lvert00\rangle\langle00\rvert + \tfrac12\lvert11\rangle\langle11\rvert$ 与 Bell 态 $\lvert\Phi^+\rangle$ 的约化密度矩阵**一模一样**（都是 $\tfrac12\mathbb 1$），局域统计完全无法区分；但前者整体是混态、不违反 Bell，后者整体纯态、违反 Bell。纠缠的定义性特征是"局域的混度 + 全局的纯度 + Bell 违反"三件套。

多体注记：两体纯态的纠缠由 $S$ 完全刻画；三体以上没有单一标量能胜任（出现"单态可织入三体"等结构），纠缠度量本身是研究课题——本篇止步于两体。

## 4. No-cloning 定理

**定理**：不存在幺正算符 $U$ 与固定"空白"态 $\lvert b\rangle$，使 $U\lvert\psi\rangle\lvert b\rangle = \lvert\psi\rangle\lvert\psi\rangle$ 对**所有** $\lvert\psi\rangle$ 成立。

**证明**（三行，自检问题 2）：若对 $\lvert\psi\rangle$ 与 $\lvert\phi\rangle$ 都成立，取内积

$$\langle\psi\vert\phi\rangle\langle b\vert b\rangle = \langle\psi\vert\phi\rangle^2\ \Rightarrow\ \langle\psi\vert\phi\rangle = \langle\psi\vert\phi\rangle^2\ \Rightarrow\ \langle\psi\vert\phi\rangle = 0\ \text{或}\ 1.$$

只有互相正交（或相同）的态可被同一台机器克隆——**任意未知态不行**。注意证明只用了线性性（幺正），测量公设、坍缩都没出场：no-cloning 与叠加原理同根。

**三层后果**：

1. **与 no-signaling 互锁**（自检问题 2 后半）：若能克隆，把未知态复制 $N$ 份就能统计区分非正交态（每份换基测，投票），而"能区分非正交态"直接破坏 no-signaling——Alice 用基选择编码比特（$\lvert0\rangle/\lvert1\rangle$ vs $\lvert+\rangle/\lvert-\rangle$），Bob 靠克隆投票读出，超光速电报开通。第 14 篇自检 3 证明单份不可区分，本篇补上"多份也不可得"——两条定理咬合成一个闭环。
2. **它是祝福不是咒诅**：正因 Eve 不能复制在途光子（BB84），也不能不动声色地分走纠缠（E91），量子密码才有立足点（§5）。
3. **它划定纠错的路线**：量子纠错不能靠"备份"（经典奇偶校验的思路），只能把信息编码进**关联**里——第 14s2 篇 §4 的全部出发点。

## 5. 三张名片：纠缠作为资源

以下每个协议都以"共享一份 Bell 态"为资本（$\lvert\Phi^+\rangle_{AB}$，Alice 持 1 号比特、Bob 持 2 号）。

### 5.1 密集编码：1 个量子比特捎 2 个经典比特

Alice 想发两个经典比特（00/01/10/11）。她对自己那半边施加四个 Pauli 之一再发给 Bob：

$$I\to\lvert\Phi^+\rangle,\quad X\to\lvert\Psi^+\rangle,\quad Z\to\lvert\Phi^-\rangle,\quad XZ\to\lvert\Psi^-\rangle$$

（直接验证：$X$ 翻转 1 号比特把 $\Phi^+\to\Psi^+$，$Z$ 打相位把 $\Phi^+\to\Phi^-$，$XZ$ 合成 $\Psi^-$。四个态两两正交。）Bob 收到后做 **Bell 基测量**（投影到 Bell 基，四结果之一）——确定读出 Alice 的 2 比特。**1 个量子比特 + 预共享纠缠 = 2 经典比特**；没有预共享纠缠时 Holevo 界锁死 1 量子比特最多送 1 经典比特。纠缠是提前存进去的带宽。

### 5.2 隐形传态：把态"寄"出去

Alice 有个未知态 $\lvert\psi\rangle_1 = a\lvert0\rangle + b\lvert1\rangle$（不能克隆——不能复制一份直接寄），两人共享 $\lvert\Phi^+\rangle_{23}$。**恒等式**（自检问题 3 完整展开）：

$$\lvert\psi\rangle_1\lvert\Phi^+\rangle_{23} = \tfrac12\Big[\lvert\Phi^+\rangle_{12}\lvert\psi\rangle_3 + \lvert\Phi^-\rangle_{12}\,Z\lvert\psi\rangle_3 + \lvert\Psi^+\rangle_{12}\,X\lvert\psi\rangle_3 + \lvert\Psi^-\rangle_{12}\,XZ\lvert\psi\rangle_3\Big].$$

协议三步：Alice 对比特 1、2 做 Bell 测量（四结果等概率 $\tfrac14$）→ 2 经典比特经**经典信道**告诉 Bob → Bob 按结果施加 $I/Z/X/XZ$ 的逆变换（Pauli 自逆），比特 3 精确落在 $\lvert\psi\rangle$ 上。

三件事必须说死：

- **不违反 no-cloning**：Alice 的 Bell 测量之后，比特 1 的原态已经**销毁**（坍缩进 Bell 基）——世界上自始至终只有一份 $\lvert\psi\rangle$，它换了个宿主。
- **不超光速**：Bob 收到 2 经典比特之前手里是什么？对 Alice 四个结果取平均（twirl，自检问题 3）：$\rho_3 = \tfrac14\sum_i \sigma_i\lvert\psi\rangle\langle\psi\rvert\sigma_i = \tfrac12\mathbb 1$——**与 $\lvert\psi\rangle$ 无关的最大混态**。没有经典指令，纠缠什么都递不过去。信息分两半：量子相干关系（提前铺好）+ 经典指令（光速传递）。
- **资源记账**：每传一个量子比特消耗一份 Bell 态（纠缠是不可再生资本，定量资源观——§3 的熵就是它的记账单位）。

### 5.3 量子密钥分发：BB84 与 E91

目标不是传密文（密文走经典信道即可），而是让双方**共享同一串随机密钥且确信无人偷听**——经典世界做不到（窃听者可完美复制在途信息），量子的"不可复制 + 不可偷看不留痕"恰好对症。

**BB84**（1984）：Alice 随机选基（$Z$ 基 $\{\lvert0\rangle,\lvert1\rangle\}$ 或 $X$ 基 $\{\lvert+\rangle,\lvert-\rangle\}$）随机选比特，发相应态；Bob 每次随机选基测量。公开比对**基**（不泄漏比特值）：基一致的（约一半）保留为原始密钥。**窃听的代价**：Eve 不能克隆（§4），只能测量-转发；她不知道基，测错基（概率 $\tfrac12$）就把随机结果转发，Bob 在正确基下读到错误（再乘 $\tfrac12$）——**拦截-重发策略下原始密钥错误率 $25\%$**（自检问题 4 推导）。双方抽一小段公开对账：错误率超过阈值即弃重来。安全性定理（Shor–Preskill 2000）：错误率足够低时可以从剩余密钥蒸馏出信息论安全的密钥。**一句话：BB84 的安全性 = no-cloning + 测量必留痕。**

**E91**（1991，Ekert）：分发的是第 05s/14 篇的自旋单态对（Bell 态），双方随机选三个预设方向测量：同向的对（反相关）生成密钥；不同向的拿去算第 14 篇的 CHSH 量 $S$。Eve 想分一杯羹必须与粒子纠缠——这立刻压低单态的关联，**Bell 违反量从 $2\sqrt2$ 跌落就是窃听警报**。14 篇 §6 那句"拉低 Bell 违反量从而暴露自己"在此兑现：**E91 的安全性 = Bell 违反的可监测性**，量子力学最"哲学"的定理当了保安。

两个协议对照着记：BB84 从"不可克隆"出发，E91 从"纠缠不可无痕分赃"出发——同一个物理（线性 + 张量积）的两种兑现。

## 6. 接口

- **第 14s2 篇（量子计算）**：Bell 测量、Pauli 门、纠缠资源在本篇的代数原封不动地成为线路的零件；纠错的"编码进关联而非复制"直接承接本篇 §4 第 3 条。
- **凝聚态书**：纠缠熵 → [拓扑序](../../condensed-matter/docs/12s-topological-order.md)的拓扑纠缠熵（基态简并的纠缠判据）；[第 12 章 拓扑物态](../../condensed-matter/docs/12-topological-phases.md)。
- **第 03 篇 §8/§9**：密度矩阵与张量积是本篇的全部语法；本篇是它们的"第二遍"——从公设变成工具。
- **第 08s 篇**：Mott 极化仪（自旋的量子干涉当仪器）与本篇 QKD（单光子的量子不可克隆当锁）是同一类"基本定理变工程"的故事。

## 小结

| 概念 | 公式/事实 | 后果 |
| --- | --- | --- |
| Bloch 球 | $\rho = \tfrac12(\mathbb 1+\vec r\cdot\vec\sigma)$ | 纯=球面；非正交不可靠区分 |
| Schmidt 分解 | $\lvert\psi\rangle = \sum\sqrt{\lambda_k}\lvert k\rangle\lvert k'\rangle$ | 纠缠有谱、对双方对称 |
| 纠缠熵 | $S = -\operatorname{Tr}\rho_A\log_2\rho_A$ | Bell 态 = 1 比特；多体接口 |
| No-cloning | $\langle\psi\vert\phi\rangle = \langle\psi\vert\phi\rangle^2$ | 与 no-signaling 互锁 |
| 密集编码 | $I/X/Z/XZ \to$ 四 Bell 态 | 1 qubit + 纠缠 = 2 bits |
| 隐形传态 | Bell 测量 + 2 bits + Pauli 修正 | 不克隆、不超光速 |
| BB84 / E91 | 错误率 25% / $S$ 跌落 = 警报 | no-cloning 与 Bell 当保安 |

一句话收束：把纠缠当资源记账（Schmidt 谱是账本），no-cloning 与 no-signaling 是物理给信息划的两条宪法边界，而密集编码、隐形传态、QKD 是在这两条边界内做成生意的三家公司——每家都用第 14 篇的"哲学定理"当了生产资料。

## 自检问题

**1.** 从 $\rho_A$ 的谱分解出发证明 Schmidt 分解；对 Bell 态 $\lvert\Phi^+\rangle$ 与直积态 $\lvert00\rangle$ 各算纠缠熵。

<details markdown="1"><summary>点击显示答案</summary>

设 $\rho_A = \operatorname{Tr}_B\lvert\psi\rangle\langle\psi\rvert$，谱分解 $\rho_A = \sum_k\lambda_k\lvert k\rangle_A\langle k\rvert$（$\lambda_k \ge 0$，$\operatorname{Tr}\rho_A = 1 \Rightarrow \sum\lambda_k = 1$）。在 A 侧插入单位算符 $\mathbb 1_A = \sum_k\lvert k\rangle\langle k\rvert$：

$$\lvert\psi\rangle = \sum_k \lvert k\rangle_A\otimes\lvert b_k\rangle_B,\qquad \lvert b_k\rangle_B \equiv \big(\langle k\rvert_A\otimes\mathbb 1_B\big)\lvert\psi\rangle.$$

用 $\rho_A$ 的定义反算交叉项：$\rho_A = \sum_{kk'}\langle b_{k'}\vert b_k\rangle\,\lvert k\rangle\langle k'\rvert$，与谱分解比较得 $\langle b_{k'}\vert b_k\rangle = \lambda_k\delta_{kk'}$。故 $\lvert b_k\rangle = \sqrt{\lambda_k}\,\lvert k'\rangle_B$（$\{\lvert k'\rangle\}$ 正交归一；$\lambda_k = 0$ 的项恒为零）：

$$\lvert\psi\rangle = \sum_k\sqrt{\lambda_k}\,\lvert k\rangle_A\lvert k'\rangle_B.\ \blacksquare$$

顺带 $\rho_B = \sum_k\lambda_k\lvert k'\rangle\langle k'\rvert$——两边谱相同，纠缠对称。

Bell 态 $\lvert\Phi^+\rangle = \tfrac1{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$：已是 Schmidt 形式，$\lambda = (\tfrac12,\tfrac12)$，$S = -2\times\tfrac12\log_2\tfrac12 = 1$ 比特（最大）。直积态 $\lvert00\rangle$：$\lambda = (1)$，$S = 0$（无纠缠）。

</details>

**2.** 证明 no-cloning 定理；再证明"一组相互正交的未知态"可以被同一台机器克隆（说明定理的边界在哪里）；最后补全链条：若克隆可能 ⇒ 可区分非正交态 ⇒ no-signaling 破坏。

<details markdown="1"><summary>点击显示答案</summary>

定理：设 $U\lvert\psi\rangle\lvert b\rangle = \lvert\psi\rangle\lvert\psi\rangle$ 与 $U\lvert\phi\rangle\lvert b\rangle = \lvert\phi\rangle\lvert\phi\rangle$。取两式内积（幺正保内积）：左边 $= \langle\psi\vert\phi\rangle\langle b\vert b\rangle = \langle\psi\vert\phi\rangle$，右边 $= \langle\psi\vert\phi\rangle^2$。故 $\langle\psi\vert\phi\rangle = 0$ 或 $1$：即两态要么相同要么正交——对任意一对态成立的克隆机不存在。

正交集可克隆：设 $\{\lvert e_i\rangle\}$ 正交归一，空白态固定为 $\lvert b\rangle$，在子空间 $\{\lvert e_i\rangle\lvert b\rangle\}$ 上定义 $U\lvert e_i\rangle\lvert b\rangle = \lvert e_i\rangle\lvert e_i\rangle$：输入集与输出集都正交归一（$\langle e_ie_i\vert e_ke_k\rangle = \delta_{ik}$），故这是两个同维子空间之间的等距映射，而**任何等距都能延拓成全空间的幺正**（正交补上任意补齐）——对这组正交基矢克隆成立且无矛盾。**边界在于叠加**：对态 $\tfrac{1}{\sqrt2}(\lvert e_1\rangle+\lvert e_2\rangle)$，线性性强制

$$U\,\frac{\lvert e_1\rangle+\lvert e_2\rangle}{\sqrt2}\,\lvert b\rangle = \frac{1}{\sqrt2}\big(\lvert e_1\rangle\lvert e_1\rangle + \lvert e_2\rangle\lvert e_2\rangle\big)\ \ne\ \frac{\lvert e_1\rangle+\lvert e_2\rangle}{\sqrt2}\otimes\frac{\lvert e_1\rangle+\lvert e_2\rangle}{\sqrt2},$$

左边是**纠缠态**，右边（真克隆的输出）是乘积态——克隆机的输出必须是乘积态，而线性演化对叠加给出纠缠态。no-cloning 的本质：**克隆是非线性操作，量子力学线性**。

链条：若有克隆机，对单份不可区分的非正交态 $\lvert\psi\rangle,\lvert\phi\rangle$（$\langle\psi\vert\phi\rangleeq0$）复制 $N$ 份，对每份轮流在几个基下测量做统计层析，$N$ 大时以任意置信度区分两者。于是 Alice 编码：发 $\lvert0\rangle/\lvert1\rangle$ 表示比特 0，发 $\lvert+\rangle/\lvert-\rangle$ 表示比特 1；Bob 克隆后区分"是 Z 基还是 X 基"即可读出 Alice 的**基选择**本身——而基选择可以是 Alice 临时随机定的、与 Bob 类空间隔：超光速信道开通，与第 14 篇自检 3 的 no-signaling 矛盾。所以三个定理连环：线性 ⇒ no-cloning ⇒ no-signaling 安然。

</details>

**3.** 逐步展开验证隐形传态恒等式；然后计算 Alice 测量后（Bob 收到经典比特前）比特 3 的约化密度矩阵，证明它是与 $\lvert\psi\rangle$ 无关的 $\tfrac12\mathbb 1$。

<details markdown="1"><summary>点击显示答案</summary>

展开：$\lvert\psi\rangle_1\lvert\Phi^+\rangle_{23} = \frac{1}{\sqrt2}\big[a\lvert00\rangle_{12}\lvert0\rangle_3 + a\lvert01\rangle_{12}\lvert1\rangle_3 + b\lvert10\rangle_{12}\lvert0\rangle_3 + b\lvert11\rangle_{12}\lvert1\rangle_3\big]$。用逆替换 $\lvert00\rangle = \tfrac1{\sqrt2}(\lvert\Phi^+\rangle+\lvert\Phi^-\rangle)$、$\lvert01\rangle = \tfrac1{\sqrt2}(\lvert\Psi^+\rangle+\lvert\Psi^-\rangle)$、$\lvert10\rangle = \tfrac1{\sqrt2}(\lvert\Psi^+\rangle-\lvert\Psi^-\rangle)$、$\lvert11\rangle = \tfrac1{\sqrt2}(\lvert\Phi^+\rangle-\lvert\Phi^-\rangle)$，逐项归并 Bell 基：

- $\lvert\Phi^+\rangle_{12}$ 系数：$\tfrac12(a\lvert0\rangle_3 + b\lvert1\rangle_3) = \tfrac12\lvert\psi\rangle_3$；
- $\lvert\Phi^-\rangle_{12}$：$\tfrac12(a\lvert0\rangle_3 - b\lvert1\rangle_3) = \tfrac12Z\lvert\psi\rangle_3$；
- $\lvert\Psi^+\rangle_{12}$：$\tfrac12(b\lvert0\rangle_3 + a\lvert1\rangle_3) = \tfrac12X\lvert\psi\rangle_3$；
- $\lvert\Psi^-\rangle_{12}$：$\tfrac12(b\lvert0\rangle_3 - a\lvert1\rangle_3) = \tfrac12XZ\lvert\psi\rangle_3$（$XZ\lvert\psi\rangle = X(a\lvert0\rangle - b\lvert1\rangle) = a\lvert1\rangle - b\lvert0\rangle$，差一整体符号 $-1$，即 $-XZ$ 或改用 $iY$——同一射线）。恒等式得证。

Bob 的约化密度矩阵（对 Alice 的测量结果取平均，四个 Pauli 通道等权）：

$$\rho_3 = \tfrac14\big[\lvert\psi\rangle\langle\psi\rvert + Z\lvert\psi\rangle\langle\psi\rvert Z + X\lvert\psi\rangle\langle\psi\rvert X + XZ\lvert\psi\rangle\langle\psi\rvert ZX\big].$$

写 $\rho = \begin{pmatrix}\lvert a\rvert^2 & ab^*\\ a^*b & \lvert b\rvert^2\end{pmatrix}$：四个 Pauli 共轭分别保持/翻转对角元、以四种符号组合翻转非对角元，求和后非对角全消、对角相加为 $4\times\tfrac12\lvert a\rvert^2$ 级：$\rho_3 = \tfrac12\mathbb 1$（twirl 恒等式，$\tfrac14\sum_{i=0}^3\sigma_i\rho\sigma_i = \tfrac12\mathbb 1\operatorname{Tr}\rho$ 对任何 $2\times2$ 的 $\rho$ 成立）。结论：经典比特到达前，Bob 手里的态**不含任何** $\lvert\psi\rangle$ 的信息——隐形传态的全部"瞬时部分"只是把态藏进关联，解码钥匙必须走光速以下的经典信道。这与第 14 篇自检 3 的 no-signaling 计算是同一枚硬币。

</details>

**4.** BB84 中 Eve 采用全程"拦截-重发"（每光子随机选基测量、按测量结果重发）：推导保留密钥（基一致部分）的错误率 25%；并解释 no-cloning 如何封死 Eve 的更优策略。

<details markdown="1"><summary>点击显示答案</summary>

分账：Alice 发比特用基 $B_A$，Bob 选基 $B_B$，Eve 选基 $B_E$，三者独立均匀。保留下来的事件是 $B_B = B_A$（概率 $\tfrac12$）。在此条件下 Eve 选错的概率 $P(B_E eq B_A) = \tfrac12$：

- $B_E = B_A$（$\tfrac12$）：Eve 测得正确比特，重发无伤——Bob 读对；
- $B_E eq B_A$（$\tfrac12$）：Eve 在错误基下测得**均匀随机**的比特，按它重发一个错误基的态。Bob 在正确基 $B_A$ 下测这个随机基的态：结果仍均匀随机，与 Alice 原比特有 $\tfrac12$ 概率不同。

故保留密钥错误率 $= \tfrac12\times\tfrac12 = 25\%$。Alice/Bob 公开抽样对账即可在统计上否决这条信道。

Eve 的"更优策略"想象：先复制一份留档、原样放行，事后再慢慢测（"存储后测"）。这正是 no-cloning 封死的路：在途的四态 $\{\lvert0\rangle,\lvert1\rangle,\lvert+\rangle,\lvert-\rangle\}$ 两两非正交，**不存在**复制它们的物理操作（自检问题 2），"完美放行的同时留下副本"直接违反线性性。Eve 剩下的选择都要碰系统（测量或纠缠），而任何触碰都按上面的账单留痕——安全性的物理根源不是"技术不够好"，是量子力学自身的定理（严格的信息论安全证明见 Shor–Preskill 2000，超出本篇）。

</details>

**5.** 比较 $\rho_1 = \lvert\Phi^+\rangle\langle\Phi^+\rvert$ 与 $\rho_2 = \tfrac12\lvert00\rangle\langle00\rvert + \tfrac12\lvert11\rangle\langle11\rvert$：计算各自的 $\operatorname{Tr}\rho^2$ 与两边的约化密度矩阵；设计一个全局测量区分它们；说明为什么 Bell 违反量也能区分。

<details markdown="1"><summary>点击显示答案</summary>

纯度：$\rho_1$ 是纯态投影，$\operatorname{Tr}\rho_1^2 = 1$；$\rho_2^2 = \tfrac14(\lvert00\rangle\langle00\rvert + \lvert11\rangle\langle11\rvert)$（交叉项因正交消失），$\operatorname{Tr}\rho_2^2 = \tfrac12$——混态。局域：两边都 $\rho_A = \rho_B = \tfrac12\mathbb 1$——**局域统计完全相同**（这就是"关联 ≠ 纠缠"的定量版：局域测一切积都一样）。但两态都能在局域基下给出完全关联的 $(0,0)/(1,1)$ 结果——经典关联 $\rho_2$ 一样有，纠缠的判据必须去全局找。

全局区分：投影测量 $\{\lvert\Phi^+\rangle\langle\Phi^+\rvert,\ \mathbb 1 - \lvert\Phi^+\rangle\langle\Phi^+\rvert\}$：$\rho_1$ 以概率 1 落在第一支；$\rho_2$ 的概率 $= \langle\Phi^+\rvert\rho_2\lvert\Phi^+\rangle = \tfrac12(\lvert\langle\Phi^+\vert00\rangle\rvert^2 + \lvert\langle\Phi^+\vert11\rangle\rvert^2) = \tfrac12\cdot(\tfrac12+\tfrac12) = \tfrac12$——单次测量半猜半准，几轮复制样本即高置信区分。（前提：手里有**多份**同种态的系综——单份混态与单份纯态无操作差别，密度矩阵本来就是系综语言，第 03 篇 §8。）

Bell 区分：$\rho_1$ 是最大纠缠纯态，关联 $E(\vec a,\vec b) = -\vec a\cdot\vec b$，CHSH 达 $2\sqrt2$（第 14 篇自检 2/3）；$\rho_2$ 是显式局域隐变量系综（"半程 $|00\rangle$ 半程 $|11\rangle$"的凸组合，隐变量就是那一半的选择），CHSH $\le 2$——违反与否一测便知。三件套收口：**局域相同（都 $\tfrac12\mathbb 1$）、全局可分（纯度、投影）、定域性可分（Bell）**——纠缠不是"更强的关联"，是另一种结构的关联。

</details>

## 参考

- Nielsen & Chuang《Quantum Computation and Quantum Information》第 1–2 章（量子比特、测量、密度矩阵、Schmidt 分解）、§2.3（Bell 基与超密编码/隐形传态的线路版）、第 12 章（QKD 与安全性）。
- Preskill《Quantum Information》讲义（Caltech Ph219）第 2–4 章——物理味最正的免费参考。
- Bennett & Brassard, *Proc. IEEE ICCSSP* (1984)（BB84）；Ekert, *Phys. Rev. Lett.* **67**, 661 (1991)（E91）；Shor & Preskill, *Phys. Rev. Lett.* **85**, 441 (2000)（安全性证明）。
- 本书第 14 篇（[测量、EPR 与 Bell](14-measurement-epr-bell.md)：CHSH、no-signaling）；第 03 篇 §8–9（密度矩阵、张量积）；第 05s 篇（[全同粒子](05s-identical-particles.md)：单态）。
