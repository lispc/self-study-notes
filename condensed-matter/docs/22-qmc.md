# 量子蒙特卡洛：用随机行走解多体薛定谔方程

> 路线图位置：第四部分（多电子问题怎么算——近似阶梯）· 第 22 章
> 前置知识：[第 14 章](14-exact-methods-fci-ed.md)（基组、FCI、指数墙与符号问题——QMC 是同一魔王对面那条路）；量子力学书[变分法](../../quantum-mechanics/docs/07s-variational-and-wkb.md)（VMC 就是会变分的蒙特卡洛）；[第 15 章](15-post-hf-mp2-cc.md)（相关能的账本，QMC 要还的是同一笔）。
> 学习目标：会说清 QMC 在近似阶梯上的位置（与 DFT、CC 的分工）；会从虚时投影推出 DMC 的扩散–分支过程，并推出重要性采样后的漂移–扩散–分支方程；会解释费米子符号问题与固定节点近似；知道 Ceperley–Alder 电子气数据与 LDA 泛函参数化的关系。
>
> 记号约定：原子单位（同第 14 章）。$\vec R = (\vec r_1, \dots, \vec r_N)$ 记 $3N$ 维电子构型，$\tau$ 为虚时，$\psi_T$ 为试探波函数，$E_L(\vec R) = \psi_T^{-1}H\psi_T$ 为局域能量。

---

## 1. 一句话总结

**第 14 章的指数墙说：任何把多体波函数显式展开的方法都注定只够得着小体系。量子蒙特卡洛的回答是：干脆不展开——把波函数（或它参与的某个正函数）当作概率分布，用随机行走在 $3N$ 维构型空间里采样。VMC 用变分原理 + Metropolis 采样 $\lvert\psi_T\rvert^2$，把能量变成局域能量的统计平均；DMC 更进一步，用虚时演化算符 $e^{-\tau H}$ 把任意试探态谱投影到基态，这个投影过程数学上正是一群"行走者"的漂移–扩散–分支过程。实空间连续坐标直接采样，没有基组误差；拿回 ~95% 的关联能，比 DFT 准、比 CC 能上大体系与强关联；统计误差按 $1/\sqrt{N}$ 缩小，精度可以用计算量直接购买。代价的名字叫符号问题：费米波函数必须变号，直接采样指数失稳——固定节点近似冻结试探函数的节点面换取稳定，能量仍是变分上界，精度由节点面质量说了算。它的标志性战果早已渗入每个 DFT 计算：Ceperley–Alder 1980 年对均匀电子气的 DMC 数据，就是 LDA 关联泛函参数化的来源。**

## 2. 阶梯上的位置：第四条路

第四部分已经见过三条路：展开（FCI/CC，第 14、15 章）、换变量（DFT，第 16 章）、换对象（GW/DMFT，第 17 章）。QMC 是第四条：**抽样**。它的坐标系与前三者都不同：

| | DFT | CC | QMC（本篇） |
|---|---|---|---|
| 近似对象 | 泛函形式 | 簇振幅的截断 rank | 试探波函数（节点面） |
| 误差性质 | 不可系统控制 | 随 rank 系统性收敛 | 变分上界 + 统计误差 |
| 代价标度 | $N^3$ | $N^6$–$N^7$ | 约 $N^3$ 每步 × 采样数 |
| 基组 | 需要 | 需要（另有基组误差） | 无（实空间连续坐标） |
| 强关联 | 结构性失灵 | 多参考失效 | 由节点面质量决定 |

三条结构性优点值得单独点出：

- **没有基组误差**。波函数是 $3N$ 维实空间里的连续函数，采样点直接打在构型空间上——第 14 章那套 cc-pVnZ 阶梯、基组极限外推、平面波截断，整条供应链都不需要。电子尖点（cusp）这类基组最难收敛的特征，在 QMC 里用一个解析因子就解决（3.3 节）。
- **精度可用计算量购买**。统计误差 $\sigma \propto 1/\sqrt{N_\text{sample}}$，要小数点后多一位就多投一百倍机时——误差条的缩小规律是已知的，这在整个第四部分独树一帜（DFT 的误差根本不可控，CC 的收敛依赖能隙）。
- **关联能回收率高**。典型的 Slater–Jastrow 试探函数做 VMC 拿回 ~80% 关联能，固定节点 DMC 拿回 ~95%——对照第 15 章的账本：MP2 数 kcal/mol、CCSD(T) ~1 kcal/mol，DMC 的能量精度介于两者之间，但适用体系大得多（数百电子的分子、周期体系），且对强关联不挑食（节点面好就行，不需要"能隙氧气"）。

## 3. VMC：会变分的蒙特卡洛

### 3.1 变分原理的积分形式

变分原理（[量子力学书变分法](../../quantum-mechanics/docs/07s-variational-and-wkb.md)）：任意归一化试探态的能量期望值是基态能量的上界，

$$E_T = \frac{\langle\psi_T\lvert H\lvert\psi_T\rangle}{\langle\psi_T\lvert\psi_T\rangle} \ge E_0.$$

第 6 章与第 15 章见到这个式子时，做法是把 $\psi_T$ 展开成行列式（的组合），把积分变成代数。VMC 的做法相反：把矩阵元**改写回积分**，再对积分做蒙特卡洛。插入构型表象的完备性关系，

$$E_T = \frac{\displaystyle\int \lvert\psi_T(\vec R)\rvert^2\,\frac{H\psi_T(\vec R)}{\psi_T(\vec R)}\,\text d\vec R}{\displaystyle\int \lvert\psi_T(\vec R)\rvert^2\,\text d\vec R} \equiv \int P(\vec R)\,E_L(\vec R)\,\text d\vec R,$$

其中 $P(\vec R) = \lvert\psi_T\rvert^2\big/\int\lvert\psi_T\rvert^2$ 是归一的概率密度，$E_L(\vec R) = \psi_T^{-1}H\psi_T$ 是**局域能量**。于是变分能量 = 局域能量在分布 $\lvert\psi_T\rvert^2$ 下的平均值——一个标准的蒙特卡洛求积分问题：用 Metropolis 算法从 $P(\vec R)$ 抽样（提议移动、按 $\min(1, P'/P)$ 接受），对样本平均 $E_L$ 即得 $E_T$ 与误差条。注意 $E_L$ 里只出现 $\psi_T$ 的**比值**与导数（$H\psi_T/\psi_T$），永远不需要计算归一化常数——这正是 Metropolis 能干活的原因。

### 3.2 一个好性质：零方差原理

局域能量有一个教科书级的性质：若 $\psi_T$ 恰是某个本征态，则 $E_L(\vec R) = E$ 处处为常数——**方差为零**。试探函数越好，$E_L$ 的涨落越小，同样的采样数给出越小的误差条。方差本身因此也成了优化目标（variance minimization）：调参数让 $E_L$ 尽量"平"，既改进能量上界又改进统计效率。

### 3.3 Slater–Jastrow：尖点交给解析因子

标准试探函数是 Slater–Jastrow 形式：

$$\psi_T(\vec R) = e^{J(\vec R)}\,D_\uparrow\,D_\downarrow,$$

$D_\uparrow, D_\downarrow$ 是两个自旋种类的 Slater 行列式（通常取自 DFT 或 HF 轨道），$J$ 是 Jastrow 关联因子，典型含两体项 $J = \sum_{i<j} u(r_{ij})$（可加三体、电子–核项）。分工极其干净：**行列式管反对称性与节点面，Jastrow 管短程关联**。

短程关联的核心是**电子尖点条件**：两个电子靠近时库仑势 $1/r_{ij}$ 发散，局域能量要有限，动能算符必须产生一个精确抵消的发散——这要求波函数在 $r_{ij} \to 0$ 处有非解析的线性斜率（尖点）。Gaussian 基组展开要无数高角动量函数才能拼出这个非解析点（第 14 章基组收敛慢的根源之一），而一个 Jastrow 因子 $u(r_{ij}) \sim \tfrac12 r_{ij}$ 解析地、一次性地满足它（完整推导见自检问题 3）。**这正是显关联思想的延续**——把 $r_{ij}$ 坐标直接写进波函数（[量子力学书显关联波函数篇](../../quantum-mechanics/docs/07s2-explicitly-correlated.md)），Slater 行列式部分从此只需描述光滑的轨道结构，不必操心尖点。

参数（Jastrow 系数、轨道系数、行列式组合系数）用能量最小化或方差最小化在采样中优化——VMC 的全部手艺就是"拟设设计 + 参数优化"，这与第 20 章张量网络的精神相通：**波函数方法的生命力在于找到一个能装下物理的可变分参数族**。

## 4. DMC：把虚时投影变成随机行走

VMC 的天花板是拟设的表达能力。DMC（扩散蒙特卡洛）的突破：不再依赖拟设本身，而是用哈密顿量**把试探态投影到基态**，采样这个投影过程。

### 4.1 虚时投影

把薛定谔方程的时间换成虚时 $\tau = it$（Wick 转动）：

$$-\frac{\partial\psi}{\partial\tau} = (H - E_T)\,\psi \qquad\Longrightarrow\qquad \psi(\tau) = e^{-\tau(H - E_T)}\psi(0),$$

$E_T$ 是暂定参考能量。按 $H$ 的本征态展开 $\psi(0) = \sum_n c_n\phi_n$：

$$\psi(\tau) = \sum_n c_n\,e^{-\tau(E_n - E_T)}\phi_n \;\xrightarrow{\;\tau\to\infty\;}\; c_0\,\phi_0 \qquad(\text{只要 } c_0 \ne 0,\ E_T \approx E_0),$$

激发态成分以 $e^{-(E_n - E_0)\tau}$ 指数消亡（收敛速率与能隙的关系见自检问题 1）。**虚时演化算符是一台基态滤波器**——这正是 QFT 里 $e^{-HT}$ 提取基态、以及第 20 章 DMRG 之外另一条"投影制胜"的路线。

### 4.2 裸投影为什么难采样

把虚时方程写出来（动能项是扩散、势能项是生灭）：

$$\frac{\partial\psi}{\partial\tau} = \underbrace{\frac12\nabla^2\psi}_{\text{扩散}} - \underbrace{(V(\vec R) - E_T)\,\psi}_{\text{分支}}.$$

这正是带生灭项的扩散方程：若 $\psi$ 是概率密度，可以用一群随机行走者（walkers）模拟——每个行走者做布朗运动，并按 $-(V - E_T)$ 的速率繁殖或消亡。两个障碍：(i) 费米波函数**有正有负**，不能直接当概率密度（第 5 节的主题）；(ii) 势能无界（库仑奇点），生灭速率涨落巨大，群体要么爆炸要么死光。解法：**重要性采样**。

### 4.3 重要性采样：乘上 $\psi_T$

定义混合分布 $f(\vec R, \tau) = \psi_T(\vec R)\,\psi(\vec R, \tau)$（取 $\psi_T$ 实、非负区域为正）。把 $\psi = f/\psi_T$ 代入虚时方程，乘开并整理（完整代数见自检问题 2），得到**漂移–扩散–分支方程**：

$$\frac{\partial f}{\partial\tau} = \frac12\nabla^2 f - \nabla\cdot\big(\vec v\,f\big) - \big(E_L(\vec R) - E_T\big)f,\qquad \vec v(\vec R) = \nabla\ln\psi_T = \frac{\nabla\psi_T}{\psi_T}.$$

与裸方程相比，两个脱胎换骨的变化：

- **漂移项**：行走者除了扩散，还沿 $\nabla\ln\psi_T$ 被引导——被推向 $\psi_T$ 大的区域、推离节点面（$\psi_T \to 0$ 处漂移速度发散、方向向外，节点面成为不可逾越的墙）。好试探函数的全部知识都进了动力学；
- **生灭项换成 $E_L - E_T$**：由零方差原理（3.2 节），$\psi_T$ 越好 $E_L$ 越平，分支速率涨落越小——库仑奇点的发散被 Jastrow 因子事先抵消，群体数温顺可控。调整 $E_T$ 使群体数稳定，$E_T$ 即收敛到基态能量（能量估计 = 群体平均的 $E_L$，即混合估计量 $\langle\psi_T\lvert H\lvert\psi(\tau)\rangle/\langle\psi_T\lvert\psi(\tau)\rangle$）。

算法落地：固定小时间步 $\Delta\tau$，每步每个行走者先漂移 $\vec v\,\Delta\tau$、再扩散（高斯随机位移，含 Metropolis 接受步修正 $\Delta\tau$ 误差）、最后按权重 $e^{-(E_L - E_T)\Delta\tau}$ 分支（复制或删除）。$\tau \to \infty$ 时行走者群体的稳态分布就是 $f(\vec R) = \psi_T(\vec R)\psi_0(\vec R)$——**基态被一群随机行走者"活"了出来**。

## 5. 符号问题与固定节点近似

### 5.1 同一魔王的第二种化身

费米统计要求波函数在交换两个同自旋电子时变号，所以 $\psi$ 必然有正有负，不能直接作概率密度。若硬把 $\lvert\psi\rvert$ 当密度采样、把符号记在权重里，正负样本的贡献近乎相消：信号 $\propto e^{-(E_0 - E_0^{(\text{玻色})})\tau}$ 随虚时与体系尺寸指数衰减，而噪声不衰减——信噪比指数崩塌。这与第 14 章 ED/QMC 在格点上撞见的**符号问题是同一个魔王的两种化身**（Troyer–Wiese：一般符号问题 NP-hard）：那里是行列式权重正负相消，这里是构型权重正负相消。玻色子没有此病（基态处处非负），液氦的 DMC 因此干净漂亮；费米子必须绕行。

### 5.2 固定节点：冻结节点面，换回变分性

绕行方案是**固定节点近似**（fixed-node DMC）：强制 DMC 的解与试探函数 $\psi_T$ 共享同一套节点面（$\psi = 0$ 的 $3N - 1$ 维超曲面）。在每个节点口袋（nodal pocket）内部，波函数不变号，$f = \psi_T\psi$ 非负，采样合法；口袋之间的泄漏由漂移项的发散天然阻挡。

关键性质（证明见自检问题 4）：固定节点 DMC 在**每个口袋内部是严格的**——它精确解出"以该节点面为 Dirichlet 边界的薛定谔方程"的最低态；拼起来的整体波函数是一个合法的反对称试探态，故

$$E_{\text{FN-DMC}} \ge E_0,$$

**能量仍是变分上界**。于是整个近似的误差被压缩进一个几何对象：节点面。节点面对、能量严格；节点面差一点、能量略高且仍是上界——误差对节点面质量是二阶敏感的（节点面的一阶误差只引起能量的二阶误差），这就是为什么"还不错的"Slater–Jastrow 节点面能拿回 ~95% 关联能。改进节点面的路线：多行列式、backflow（轨道里掺入其他电子坐标的依赖）、以及第 23 章的神经网络波函数。

## 6. 品格、战果与疆界

**工程品格**。DMC 单步能量的求值代价约 $N^3$（行列式更新用 Sherman–Morrison 公式），与 DFT 同级但常数大得多；行走者之间天然独立，是"令人尴尬的并行"——超算上的宠儿。芯电子用赝势替换（与平面波方法同款冻芯思想，第 14 章 3.2 节），非局域赝势在实空间 QMC 里需要额外的局域化近似。短板也清楚：力（能量对核坐标的导数）与激发态比基态能量难得多；周期体系要处理有限尺寸误差。

**标志性战果：LDA 的地基**。第 6 章留下的悬案：真实金属 $r_s \approx 2$–$6$ 卡在动能与势能相争的中间地带，HF 只有交换、RPA 只是环图——均匀电子气的关联能到底多大？Ceperley 与 Alder（1980）用固定节点 DMC 给出了一批不同 $r_s$ 下的高精度能量，后人将其参数化成解析形式（VWN、PW92 等）。第 16 章 4.1 节已经交代：LDA 的交换部分可从均匀气 HF 解析导出，而**关联部分无解析式、全部来自这批 QMC 数据的参数化**——换句话说，今天每一个 LDA/GGA 计算的交换相关泛函里，都沉睡着 1980 年那群随机行走者。QMC 不只是一个方法，它还是整个 DFT 帝国的校准实验。

**外延（各一句话）**。

- **GFMC**（格林函数蒙特卡洛）：格点/离散空间的投影 QMC，核物理与晶格模型主力；
- **路径积分蒙特卡洛（PIMC）**：有限温度、把配分函数写成路径积分采样，玻色体系（超流氦）的黄金标准，费米体系同样撞符号问题；
- **实材料中的 DMC**：二维材料、过渡金属化合物、高压氢的能量学都在用，定位是"比 DFT 贵三个量级、准一个量级"的仲裁者；
- **FermiNet 等神经网络波函数**（Pfau et al., 2020）：用深度网络直接参数化 $\psi_T$（含节点面），VMC 框架不变、拟设表达力暴涨——这是第 23 章的主题，本篇不展开。

## 小结

- 阶梯坐标：QMC = 抽样；无基组误差、统计误差 $1/\sqrt{N}$ 可购买、拿回 ~95% 关联能；夹在 DFT 与 CC 之间，且不怕强关联（只怕坏节点面）。
- VMC：变分原理写成 $E_L$ 在 $\lvert\psi_T\rvert^2$ 下的平均；Slater–Jastrow 分工——行列式管节点、Jastrow 管尖点（显关联思想）。
- DMC：虚时投影 $e^{-\tau H}$ 是基态滤波器；重要性采样 $f = \psi_T\psi$ 把它变成漂移（$\vec v = \nabla\ln\psi_T$）–扩散–分支方程；行走者群体的稳态分布 $= \psi_T\psi_0$。
- 符号问题 = 第 14 章魔王的采样化身；固定节点近似冻结 $\psi_T$ 的节点面，能量保持变分上界，精度由节点面质量决定。
- 战果与接口：Ceperley–Alder 电子气数据 → LDA 参数化（第 6、16 章的闭环）；神经网络波函数 → 第 23 章。

## 自检问题

**1.** 虚时投影：用谱展开证明 $e^{-\tau H}$ 把任意与基态不正交的初态压到基态；给出激发态污染衰减的特征时间，并说明"混合估计量" $\langle\psi_T\lvert H\lvert\psi(\tau)\rangle/\langle\psi_T\lvert\psi(\tau)\rangle$ 为什么收敛到 $E_0$ 以及收敛速率由谁决定。

<details markdown="1"><summary>点击显示答案</summary>

**谱展开**：$H$ 完备本征系 $\{\phi_n\}$（$E_0 < E_1 \le \cdots$），初态 $\psi(0) = \sum_n c_n\phi_n$，$c_0 = \langle\phi_0\lvert\psi(0)\rangle \ne 0$。则

$$\psi(\tau) = e^{-\tau H}\psi(0) = \sum_n c_n e^{-E_n\tau}\phi_n = c_0 e^{-E_0\tau}\left[\phi_0 + \sum_{n\ge1}\frac{c_n}{c_0}e^{-(E_n - E_0)\tau}\phi_n\right].$$

括号里第 $n$ 项的相对权重按 $e^{-(E_n - E_0)\tau}$ 消亡，$\tau\to\infty$ 时只剩 $\phi_0$（$c_0 \ne 0$ 是"与基态不正交"的精确含义）。主导污染来自第一激发态：特征时间

$$\tau^* \sim \frac{1}{E_1 - E_0} = \frac{1}{\Delta},$$

**能隙越小投影越慢**——第 15 章"能隙是氧气"在 QMC 的翻版（这里不发散，只是等得久）。

**混合估计量**：分子 $\langle\psi_T\lvert H\lvert\psi(\tau)\rangle = \sum_n c_n E_n e^{-E_n\tau}\langle\psi_T\lvert\phi_n\rangle$，分母 $\sum_n c_n e^{-E_n\tau}\langle\psi_T\lvert\phi_n\rangle$。$\tau\to\infty$ 时两者都被 $n = 0$ 项主导：

$$E(\tau) = \frac{c_0 E_0 e^{-E_0\tau}\langle\psi_T\lvert\phi_0\rangle\,[1 + O(e^{-\Delta\tau})]}{c_0 e^{-E_0\tau}\langle\psi_T\lvert\phi_0\rangle\,[1 + O(e^{-\Delta\tau})]} = E_0 + O(e^{-\Delta\tau}).$$

收敛速率同样由 $\Delta = E_1 - E_0$ 决定。两点注意：(i) 只要 $\langle\psi_T\lvert\phi_0\rangle \ne 0$ 就收敛到 $E_0$——对试探函数的"重叠"要求而不是"精度"要求；(ii) 实际算法里 $E_T$ 反馈调节使群体数稳定，$E_T$ 的自洽值正是这个 $E_0$。

</details>

**2.** 重要性采样变换：从虚时方程 $\partial_\tau\psi = \tfrac12\nabla^2\psi - (V - E_T)\psi$ 出发，令 $f = \psi_T\psi$，推出漂移–扩散–分支方程 $\partial_\tau f = \tfrac12\nabla^2 f - \nabla\cdot(\vec v f) - (E_L - E_T)f$，并给出漂移速度 $\vec v$ 与局域能量 $E_L$ 的表达式。

<details markdown="1"><summary>点击显示答案</summary>

设 $\psi_T$ 实。$f = \psi_T\psi \Rightarrow \psi = f/\psi_T$，代入（$\psi_T$ 不含 $\tau$，故 $\partial_\tau f = \psi_T\partial_\tau\psi$）：

$$\frac{\partial f}{\partial\tau} = \frac12\psi_T\nabla^2\!\left(\frac{f}{\psi_T}\right) - (V - E_T)f.$$

展开拉普拉斯（逐项用乘积法则）：

$$\nabla^2\!\left(\frac{f}{\psi_T}\right) = \frac{\nabla^2 f}{\psi_T} - 2\,\frac{\nabla f\cdot\nabla\psi_T}{\psi_T^2} + f\left(\frac{2\lvert\nabla\psi_T\rvert^2}{\psi_T^3} - \frac{\nabla^2\psi_T}{\psi_T^2}\right).$$

乘以 $\psi_T/2$，并定义 $\vec v = \nabla\ln\psi_T = \nabla\psi_T/\psi_T$：

$$\frac{\partial f}{\partial\tau} = \frac12\nabla^2 f - \nabla f\cdot\vec v + f\left(\frac{\lvert\nabla\psi_T\rvert^2}{\psi_T^2} - \frac12\frac{\nabla^2\psi_T}{\psi_T}\right) - (V - E_T)f.$$

把漂移写成守恒流形式。注意 $\nabla\cdot\vec v = \nabla^2\psi_T/\psi_T - \lvert\nabla\psi_T\rvert^2/\psi_T^2$，故

$$-\nabla f\cdot\vec v = -\nabla\cdot(\vec v f) + f\,\nabla\cdot\vec v = -\nabla\cdot(\vec v f) + f\left(\frac{\nabla^2\psi_T}{\psi_T} - \frac{\lvert\nabla\psi_T\rvert^2}{\psi_T^2}\right).$$

代回，$\lvert\nabla\psi_T\rvert^2/\psi_T^2$ 项精确相消，剩

$$\frac{\partial f}{\partial\tau} = \frac12\nabla^2 f - \nabla\cdot(\vec v f) + \frac12\frac{\nabla^2\psi_T}{\psi_T}f - (V - E_T)f = \frac12\nabla^2 f - \nabla\cdot(\vec v f) - \big(E_L(\vec R) - E_T\big)f,$$

其中 $E_L = \psi_T^{-1}H\psi_T = -\tfrac12\psi_T^{-1}\nabla^2\psi_T + V$ 正是 VMC 的局域能量。$\blacksquare$ 三项的物理：扩散（动能）照旧；漂移把行走者推向 $\psi_T$ 大处；生灭率 $E_L - E_T$ 由零方差原理近乎常数——坏 $\psi_T$ 的所有野性（库仑奇点、剧烈涨落）都被事先吸收进解析因子里。（复 $\psi_T$ 时 $\vec v = \text{Re}[\nabla\psi_T/\psi_T]$，还多一个规范流项，本篇从略。）

</details>

**3.** 电子尖点条件：设两个反自旋电子靠近，$r_{ij} \to 0$，波函数含 Jastrow 因子 $e^{u(r_{ij})}$ 乘一个光滑非零因子。证明局域能量有限要求 $u'(0) = \tfrac12$（原子单位）；说明同自旋对为什么改成 $u'(0) = \tfrac14$；并解释为什么这让 Slater 行列式部分无需操心尖点。

<details markdown="1"><summary>点击显示答案</summary>

**两体约化**：把质心分出，相对坐标 $\vec r = \vec r_i - \vec r_j$，折合质量 $\mu = 1/2$（两个单位质量粒子），哈密顿的相对部分（原子单位）

$$H_{\text{rel}} = -\frac{1}{2\mu}\nabla_r^2 + \frac{1}{r} = -\nabla_r^2 + \frac{1}{r}.$$

**反自旋对**：波函数在 $r \to 0$ 不必为零，写 $\psi = e^{u(r)}\phi(\vec r)$，$\phi(0) \ne 0$ 且光滑。计算 $-\nabla^2\psi/\psi$：径向部分 $\nabla^2 u = u'' + \tfrac{2}{r}u'$，于是

$$\frac{-\nabla^2\psi}{\psi} = -\Big(u'' + \frac{2}{r}u' + \lvert\nabla u\rvert^2 + 2\nabla u\cdot\frac{\nabla\phi}{\phi} + \frac{\nabla^2\phi}{\phi}\Big).$$

$r \to 0$ 时唯一的发散项是 $-\tfrac{2}{r}u'(0)$（其余各项有限：$\phi$ 光滑非零，$u'$ 有限）；势能贡献 $+\tfrac{1}{r}$。局域能量有限要求发散相消：

$$-\frac{2u'(0)}{r} + \frac{1}{r} = 0 \qquad\Longrightarrow\qquad u'(0) = \frac12.$$

**同自旋对**：泡利原理强迫波函数在 $r = 0$ 处为零，小 $r$ 时 $\psi \sim r\,e^{u(r)}\tilde\phi$（$p$ 波型节点）。重复同样的展开，$r$ 因子自己贡献一个 $-\tfrac{2}{r}\cdot\tfrac{1}{r}\cdot r$ 型的动能项，抵消部分势能后剩余条件给出 $u'(0) = \tfrac14$（交换穴已替尖点干了一半活——同自旋电子本来就互相回避，第 6 章）。

**分工的含义**：尖点是 $r_{ij}$ 坐标的**非解析**特征，任何单粒子基组（高斯、平面波）都要用大量基底才能拼出来（基组误差收敛慢的病根，第 14 章）；而 $u(r_{ij}) \approx \tfrac12 r_{ij}$（短程）把这个非解析性解析地装进两体因子——Slater 行列式乘上 $e^J$ 后自动满足尖点条件，轨道部分只管光滑结构。这正是[量子力学书显关联波函数篇](../../quantum-mechanics/docs/07s2-explicitly-correlated.md)的主题思想：与其让基组硬拼 $r_{ij}$ 依赖，不如把它写进拟设。

</details>

**4.** 证明固定节点 DMC 的能量是基态能量的变分上界；并说明"在每个节点口袋内部它是严格基态"与"误差对节点面质量二阶敏感"这两条性质为什么不矛盾。

<details markdown="1"><summary>点击显示答案</summary>

**口袋内的严格性**：固定节点 DMC 的漂移项 $\vec v = \nabla\ln\psi_T$ 在节点面上发散（方向离开面），行走者从不穿面；分支–扩散过程在每个口袋内部独立演化到稳态。稳态解满足的正是"以节点面为 Dirichlet 边界（$\psi = 0$）的薛定谔方程"在该口袋内的最低本征态——扩散–分支方程是该约束问题的虚时投影，而虚时投影收敛到约束本征问题的基态（自检问题 1 的论证对约束算符照样成立）。所以在**给定节点面**的前提下，FN-DMC 无近似（仅剩 $\Delta\tau$ 时间步误差与统计误差，都可系统缩小）。

**变分上界**：把各口袋的解拼成整体波函数 $\psi_{\text{FN}}$——反对称（沿用了 $\psi_T$ 的节点拓扑）、在每个口袋内是约束基态、在节点面上为零（函数连续；法向导数在面两侧可以跳变，但这是平方可积波函数允许的——动能期望值仍有限）。$\psi_{\text{FN}}$ 是一个**合法的试探态**，对它用变分原理（[量子力学书变分法](../../quantum-mechanics/docs/07s-variational-and-wkb.md)）：

$$E_{\text{FN-DMC}} = \frac{\langle\psi_{\text{FN}}\lvert H\lvert\psi_{\text{FN}}\rangle}{\langle\psi_{\text{FN}}\lvert\psi_{\text{FN}}\rangle} \ge E_0.$$

（更细的论证：约束问题的最低能量对任意节点面取遍时的最小值恰在真实节点面上达到，且处处 $\ge E_0$。）

**两条性质的一致性**：严格性是"给定节点面"条件下的，变分性是"所有节点面"之间的。固定了正确节点面，约束基态 = 真基态，等号成立；固定了错误节点面，得到一个偏高但仍合法的上界——FN-DMC 把"波函数难"的问题精确兑换成了"节点面难"的问题。

**二阶敏感性**：能量对波函数误差的响应是二阶的（变分原理的标准推论：若 $\psi_{\text{FN}} = \psi_0 + \delta\psi$，则 $E_{\text{FN}} - E_0 = O(\lVert\delta\psi\rVert^2)$，一阶项被变分驻点性杀死）；而波函数误差本身受节点面误差驱动，节点面差 $O(\epsilon)$ 只让能量差 $O(\epsilon^2)$。这就是为什么"DFT 轨道 + Jastrow"这种粗糙节点面也能拿回 ~95% 关联能——能量对节点面是宽容的。

</details>

**5.** 统计误差与自相关：DMC 沿马尔可夫链产生 $N$ 个样本，样本间相关（相关时间 $\tau_c$）。证明均值的标准误不是 $\sigma/\sqrt{N}$ 而是 $\sigma\sqrt{2\tau_c/N}$（定义有效样本数 $N_{\text{eff}} = N/(2\tau_c)$）；并说明 blocking 分析如何在不已知 $\tau_c$ 的情况下给出可靠误差条。

<details markdown="1"><summary>点击显示答案</summary>

**相关样本的方差**：设样本 $x_1, \dots, x_N$ 平稳、均值 $\mu$、方差 $\sigma^2$、归一化自相关 $\rho_k = \text{Cov}(x_i, x_{i+k})/\sigma^2$。样本均值 $\bar x$ 的方差：

$$\text{Var}(\bar x) = \frac{1}{N^2}\sum_{i,j}\text{Cov}(x_i, x_j) = \frac{\sigma^2}{N}\left[1 + 2\sum_{k=1}^{N-1}\Big(1 - \frac{k}{N}\Big)\rho_k\right].$$

$N \gg \tau_c$ 时求和近似为积分：$\sum_k\rho_k \approx \int_0^\infty \rho(t)\,\text dt \equiv \tau_c$（指数衰减 $\rho_k = e^{-k/\tau_c}$ 时严格成立）。于是

$$\text{Var}(\bar x) \approx \frac{\sigma^2}{N}(1 + 2\tau_c) \approx \frac{2\tau_c\,\sigma^2}{N} = \frac{\sigma^2}{N_{\text{eff}}},\qquad N_{\text{eff}} \equiv \frac{N}{2\tau_c}.$$

**物理**：马尔可夫链上相邻样本不是独立实验——链要花 $\sim\tau_c$ 步才"忘记"自己。百万步采样若 $\tau_c \sim 10^3$，有效样本只有几百个：$1/\sqrt{N}$ 里的 $N$ 必须打相关时间折扣。相关时间在相变点附近、在节点面附近、在大时间步下都会变长——光看样本数会系统性低估误差条，这是蒙特卡洛报告里最常见的自欺。

**Blocking 分析**：不知道 $\rho_k$ 也能估计 $\text{Var}(\bar x)$。把 $N$ 个样本切成 $N_B$ 个长度 $B$ 的块，算每块均值 $\bar x_b$；块长大于相关时间（$B \gg \tau_c$）时块均值之间近似独立，于是

$$\text{Var}(\bar x) \approx \frac{\text{Var}(\{\bar x_b\})}{N_B}.$$

操作：画"误差条估计 vs 块长 $B$"曲线——$B$ 小时块均值仍相关、误差被低估；$B$ 超过 $\tau_c$ 后曲线进入**平台**，平台值即真误差条。平台同时给出 $\tau_c$ 的读数（平台起点 $\sim$ 数倍 $\tau_c$）。这是 QMC 论文里误差条的标准产生方式；任何只报 $\sigma/\sqrt{N}$ 的蒙特卡洛结果都应被打回重算。

</details>

## 参考

- W. M. C. Foulkes, L. Mitas, R. J. Needs & G. Rajagopal, Rev. Mod. Phys. **73**, 33 (2001)：QMC 标准综述——VMC/DMC、固定节点、赝势与有限尺寸修正的全部细节（本篇 3–6 节的骨干）。
- D. M. Ceperley & B. J. Alder, Phys. Rev. Lett. **45**, 566 (1980)：均匀电子气的固定节点 DMC 能量——LDA 关联参数化的数据源（第 6 节；接口见本书[第 6 章](06-interacting-electron-gas.md)与[第 16 章](16-dft.md) 4.1 节）。
- B. L. Hammond, W. A. Lester & P. J. Reynolds《Monte Carlo Methods in Ab Initio Quantum Chemistry》：实空间 QMC 的专著级处理，推导细、拟设设计讲得透。
- D. Pfau, J. S. Spencer, A. G. D. G. Matthews & W. M. C. Foulkes, Phys. Rev. Research **2**, 033429 (2020)（FermiNet）：神经网络波函数的 VMC——第 23 章的入口文献。
