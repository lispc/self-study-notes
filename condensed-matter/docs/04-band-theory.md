# 能带论：Bloch 定理与金属/绝缘体之分

> 本书位置：第一部分「结构与无相互作用电子」· 第 4 章
> 前置知识：定态薛定谔方程、定态微扰论（尤其简并微扰论，见 QFT 书的[微扰论笔记](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)）；晶格、倒格子与 Brillouin 区的基本概念（本书第 1 章，待写——本篇对用到的事实做最小回顾，不妨碍阅读）。
> 学习目标：能从平移对称性出发证明 Bloch 定理；在近自由电子与紧束缚两个相反极限下分别推出能带与能隙；用"每带 2N 个态"的计数判断金属与绝缘体，并理解二价金属为何例外；掌握有效质量与空穴的概念。

本篇保留 $\hbar$ 与 $k_B$（本书约定，与 QFT 书的自然单位不同）。三维与一维记号混用，转到一维处会注明。

---

## 1. 一句话总结

**晶体的平移对称性迫使单电子本征态取 Bloch 形式 $\psi_{n\vec k}(\vec r)=e^{i\vec k\cdot\vec r}u_{n\vec k}(\vec r)$——晶格动量 $\vec k$ 被限制在第一 Brillouin 区内，$n$ 是能带指标；周期势在区边界的简并处打开大小为 $2\lvert V_G\rvert$ 的能隙，而"每条能带恰好容纳 $2N$ 个电子"这一计数把固体分成金属（存在部分填充的带）与绝缘体（带全满且与空带间有能隙），有效质量与空穴则把"电子在带中如何运动"压缩成两个参数。**

下面把这句话逐层拆开。

## 2. 问题设置：周期势中的单电子

真实固体是 $\sim 10^{23}$ 个电子与原子核的多体问题，无从下手。能带论的出发点是**独立电子近似**：每个电子只在其他所有粒子产生的某个平均周期势中运动，

$$H = \frac{\vec p^{\,2}}{2m} + V(\vec r), \qquad V(\vec r + \vec R) = V(\vec r),$$

其中 $\vec R$ 取遍 Bravais 晶格的所有格矢。这个近似为何常常有效（屏蔽、Pauli 原理压低散射）是深刻的问题，留到本书第 6 章（相互作用电子气）；本篇先接受它，看看单电子在周期势中的谱长什么样。

先回顾三个第 1 章的概念（只需定义）：

- **正格子**：$\vec R = n_1\vec a_1 + n_2\vec a_2 + n_3\vec a_3$，$n_i$ 为整数；
- **倒格子**：满足 $\vec G\cdot\vec R = 2\pi\times\text{整数}$ 的全部 $\vec G$；一维点阵常数 $a$ 的链上 $G = 2\pi m/a$；
- **第一 Brillouin 区（BZ）**：倒格子的 Wigner–Seitz 原胞，即倒空间中以某个倒格点为中心、离它比离其他倒格点更近的区域。一维情形就是 $(-\pi/a,\, \pi/a]$。

中心问题：**$H$ 的本征值与本征态如何被平移对称性组织起来？** 答案（Bloch 定理）将给出"能带"这一整个学科的骨架。

## 3. Bloch 定理

### 3.1 平移算符与哈密顿量对易

对每个格矢 $\vec R$ 定义平移算符

$$\hat T_{\vec R}\,\psi(\vec r) = \psi(\vec r + \vec R).$$

它作用在哈密顿量上：动能项只含导数，常数平移不改变导数，$\hat T_{\vec R}\,\vec p^{\,2} = \vec p^{\,2}\,\hat T_{\vec R}$；势能项由周期性，$\hat T_{\vec R}\,V(\vec r)\,\psi(\vec r) = V(\vec r+\vec R)\psi(\vec r+\vec R) = V(\vec r)\,\hat T_{\vec R}\psi(\vec r)$。于是

$$[\hat T_{\vec R},\, H] = 0 \qquad \text{对所有 } \vec R.$$

同时，平移群是**阿贝尔群**：$\hat T_{\vec R}\hat T_{\vec R'} = \hat T_{\vec R+\vec R'} = \hat T_{\vec R'}\hat T_{\vec R}$。一组互相对易的算符 $\{H, \hat T_{\vec R}\}$ 存在共同本征基——这就是 Bloch 定理的全部输入。

### 3.2 本征值结构与 Bloch 形式

设 $\psi$ 是所有平移算符的共同本征态：$\hat T_{\vec R}\psi = \lambda(\vec R)\,\psi$。两条约束把 $\lambda$ 完全钉死：

1. **幺正性**：平移不改变归一化，$\hat T_{\vec R}$ 幺正，故 $\lvert\lambda(\vec R)\rvert = 1$；
2. **群乘法**：$\lambda(\vec R + \vec R') = \lambda(\vec R)\,\lambda(\vec R')$。

模为 1 且对 $\vec R$ 可加的函数只能是指数：$\lambda(\vec R) = e^{i\vec k\cdot\vec R}$，其中 $\vec k$ 是某个实矢量（$\lambda$ 对 $\vec R$ 的线性依赖由乘法规则保证）。于是

$$\psi(\vec r + \vec R) = e^{i\vec k\cdot\vec R}\,\psi(\vec r).$$

定义 $u_{\vec k}(\vec r) = e^{-i\vec k\cdot\vec r}\psi(\vec r)$，直接验证：

$$u_{\vec k}(\vec r + \vec R) = e^{-i\vec k\cdot(\vec r+\vec R)}\,e^{i\vec k\cdot\vec R}\psi(\vec r) = u_{\vec k}(\vec r).$$

即 $u_{\vec k}$ 具有晶格周期性。这就是 **Bloch 定理**：

$$\boxed{\;\psi_{\vec k}(\vec r) = e^{i\vec k\cdot\vec r}\,u_{\vec k}(\vec r), \qquad u_{\vec k}(\vec r+\vec R) = u_{\vec k}(\vec r)\;}$$

物理图像：$\psi$ 是一个被晶格周期函数调制的平面波。$e^{i\vec k\cdot\vec R}$ 携带"原胞之间"的相位信息，$u_{\vec k}$ 携带"原胞之内"的结构细节——前者由对称性钉死，后者要解方程才知道。

$\hbar\vec k$ 称为**晶格动量（crystal momentum）**。它不是真实动量：一般 $\hat{\vec p}\,\psi_{\vec k} \neq \text{常数}\times\psi_{\vec k}$（除非 $u$ 为常数）。但它是动力学里的"好量子数"：外场改变 $\vec k$，晶格整体可以吸收 $\hbar\vec G$ 整数倍的动量（倒格矢的意义正在于此）。

### 3.3 Brillouin 区与能带指标

**$\vec k$ 与 $\vec k + \vec G$ 是同一个量子数**：因为 $e^{i(\vec k+\vec G)\cdot\vec R} = e^{i\vec k\cdot\vec R}$，两者给出所有 $\hat T_{\vec R}$ 的同一组本征值，无法区分。所以只需把 $\vec k$ 限制在第一 BZ 内——这和"晶格振动中只有 BZ 内的波矢是独立的"（本书第 2 章，待写）是同一个道理。

对边长 $Na$、Born–von Karman 周期边界条件 $\psi(x+Na)=\psi(x)$ 的一维环，$e^{ikNa}=1$ 给出 $N$ 个离散的允许 $k$ 值，均匀分布在 $(-\pi/a,\pi/a]$ 中，间距 $2\pi/(Na)$。$N\to\infty$ 时 $k$ 成为连续变量。

固定一个 $\vec k$，$u_{\vec k}$ 要满足什么方程？把 $\psi = e^{i\vec k\cdot\vec r}u$ 代入薛定谔方程，利用 $\hat{\vec p}\,e^{i\vec k\cdot\vec r}u = e^{i\vec k\cdot\vec r}(\hat{\vec p}+\hbar\vec k)u$，得到

$$\left[\frac{(\hat{\vec p}+\hbar\vec k)^2}{2m} + V(\vec r)\right]u_{\vec k}(\vec r) = E\,u_{\vec k}(\vec r),$$

定义域缩小为**一个原胞**、边界条件是周期性边界条件。紧致区域上的厄米算符有离散谱：对每个 $\vec k$ 有一列本征值 $E_1(\vec k) < E_2(\vec k) < \cdots$，$n$ 就是**能带指标**。当 $\vec k$ 在 BZ 内连续变化时，每条 $E_n(\vec k)$ 描出一条连续的带——**能带**。整条带的能量范围（带宽）有限，带与带之间可以出现任何 $E_n(\vec k)$ 都取不到的能量区间——**能隙（band gap）**。

<details markdown="1"><summary>补充说明：空格子检验——能带图像在 V=0 时退化成什么</summary>

把上面的机器开到 $V(\vec r)\equiv 0$ 的极限做个自检。此时 $u_{\vec k}$ 满足自由粒子方程，周期边界条件下的解是 $u \propto e^{i\vec G\cdot\vec r}$（$\vec G$ 为倒格矢，保证原胞周期性），于是

$$\psi = e^{i(\vec k+\vec G)\cdot\vec r}, \qquad E_{\vec G}(\vec k) = \frac{\hbar^2\lvert\vec k+\vec G\rvert^2}{2m}.$$

这不过是把自由电子的抛物线**折叠**进第一 BZ：每个 $\vec G$ 给出一条"带"，不同带在区边界处简并相交（例如一维中 $k=\pi/a$ 处，$G=0$ 与 $G=-2\pi/a$ 两支能量相等）。**能带结构在自由极限下已经存在"带"的骨架；周期势的作用是在这些简并点打开能隙**——这正是第 4 节近自由电子近似的出发点。这个极限也解释了为什么 BZ 边界的简并对能隙的形成如此关键。

</details>

## 4. 近自由电子近似：弱周期势打开能隙

### 4.1 设定：傅里叶分量与选择定则

近自由电子近似适用于周期势很弱的情形（简单金属的价电子是好例子）：把 $H_0 = \vec p^{\,2}/2m$ 当作已解的零级，$V$ 当作微扰。周期势可以作傅里叶展开

$$V(\vec r) = \sum_{\vec G} V_{\vec G}\,e^{i\vec G\cdot\vec r}, \qquad V_{-\vec G} = V_{\vec G}^{*}\ \ (\text{势能是实函数}).$$

常数项 $V_{\vec 0}$ 只是能量零点的平移，以下略去。平面波基 $\lvert\vec k\rangle$（零级本征态，$E^0(\vec k)=\hbar^2k^2/2m$）下，微扰的矩阵元有严格的选择定则：

$$\langle\vec k'\rvert V\lvert\vec k\rangle = \begin{cases} V_{\vec k'-\vec k}, & \vec k'-\vec k = \vec G,\\ 0, & \text{其他}.\end{cases}$$

即 $V$ 只把相差一个倒格矢的平面波耦合起来。一维情形 $G = 2\pi m/a$，本节余下部分用一维书写（三维推理相同）。

### 4.2 非简并修正与区边界简并

对一般的 $k$，$E^0(k)$ 与所有 $E^0(k-G)$ 都相差 $O(1)$，非简并微扰论适用（公式见[微扰论笔记](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)第 3 节）：一阶修正为零（$V_{\vec 0}$ 已去掉），二阶修正

$$E^{(2)}(k) = \sum_{G\neq 0}\frac{\lvert V_G\rvert^2}{E^0(k)-E^0(k-G)} = O\!\left(\frac{\lvert V_G\rvert^2}{E}\right),$$

只给出微小移动。**但分母可以为零**：当

$$E^0(k) = E^0(k-G) \iff \lvert k\rvert = \lvert k-G\rvert,$$

即 $k$ 落在某个倒格矢的垂直平分面上——这正好是 **BZ 边界**（一维：$k = \pm G/2$，离原点最近的是 $k=\pm\pi/a$）。几何上这也是 Bragg 衍射条件，不是巧合：区边界的电子波正好被晶格相干背散射。

简并处非简并公式发散，必须改用**简并微扰论**：在简并子空间 $\{\lvert k\rangle, \lvert k-G\rangle\}$ 内把 $H$ 精确对角化（框架见微扰论笔记第 4 节）。利用上面的矩阵元，

$$H_{\mathrm{eff}} = \begin{pmatrix} E^0(k) & V_G \\ V_G^{*} & E^0(k-G) \end{pmatrix},$$

本征值为

$$E_{\pm}(k) = \frac{E^0(k)+E^0(k-G)}{2} \pm \sqrt{\left[\frac{E^0(k)-E^0(k-G)}{2}\right]^2 + \lvert V_G\rvert^2}\;.$$

在区边界 $k = G/2$ 处 $E^0(k)=E^0(k-G)$，平方根退化为 $\lvert V_G\rvert$，两个能级劈裂为

$$E_{\pm} = E^0\!\left(\tfrac{G}{2}\right) \pm \lvert V_G\rvert,$$

$$\boxed{\;E_{\text{gap}} = 2\,\lvert V_G\rvert\;}$$

**能隙的大小直接量度周期势相应傅里叶分量的强度。** 偏离区边界后，平方根内两项竞争：靠近边界处能谱被"压平"（$\mathrm{d}E/\mathrm{d}k=0$，因为 $E_\pm$ 关于 $k=G/2$ 对称且光滑），远离边界回到微扰的小修正。把折叠的空格子抛物线（第 3 节补充说明）的每个交点都这样"掰开"，就得到完整的近自由电子能带。

相应的本征态是 $\big(\lvert k\rangle \pm \lvert k-G\rangle\big)/\sqrt{2}$，即驻波 $\cos(Gx/2)$ 与 $\sin(Gx/2)$：一个把电子概率密度堆在势能低处（能量降低），另一个堆在势能高处（能量升高）。行波在区边界被迫变成驻波——群速度为零，这正是 Bragg 反射的波动图像。

## 5. 紧束缚近似：从原子轨道交叠出发

### 5.1 相反的极限

近自由电子把电子想成"几乎自由、被弱周期势轻轻扰动"。对内层电子、过渡金属的 $d$ 电子、分子晶体，更自然的起点恰恰相反：**原子相距无穷远时**，每个电子束缚在自己的原子上，每条原子能级是 $N$ 重简并的（$N$ 个原子任选一个）；**原子靠近后**，波函数交叠使简并解除，每条原子能级展宽成一条能带，带宽正比于交叠程度。这就是紧束缚近似（tight-binding），又称 LCAO（原子轨道线性组合）。

### 5.2 一维单轨道模型：余弦带

考虑一维链，每个格点 $n$ 上放一个原子轨道 $\lvert n\rangle$（设为正交归一，$\langle n|n'\rangle=\delta_{nn'}$）。只保留最近邻之间的跃迁，哈密顿量为

$$\hat H = \sum_n E_0\,\lvert n\rangle\langle n\rvert \;-\; t\sum_n\Big(\lvert n\rangle\langle n+1\rvert + \lvert n+1\rangle\langle n\rvert\Big),$$

其中 $E_0 = \langle n\rvert H\lvert n\rangle$ 是原子能级（含邻近原子的平移修正），$t = -\langle n\rvert H\lvert n+1\rvert > 0$ 是**跃迁（hopping）振幅**，量度相邻轨道的交叠。

Bloch 定理告诉我们本征态在不同原胞间只差相位 $e^{ika}$，因此设

$$\lvert\psi_k\rangle = \frac{1}{\sqrt N}\sum_n e^{ikna}\,\lvert n\rangle, \qquad k\in(-\pi/a,\,\pi/a].$$

代入 $\hat H$：

$$\hat H\lvert\psi_k\rangle = \frac{1}{\sqrt N}\sum_n e^{ikna}\Big[E_0\lvert n\rangle - t\lvert n+1\rangle - t\lvert n-1\rangle\Big].$$

对后两项分别平移求和指标（$n+1\to m$ 与 $n-1\to m$，周期边界条件保证边界项无虞）：$\sum_n e^{ikna}\lvert n+1\rangle = e^{-ika}\sum_m e^{ikma}\lvert m\rangle$，另一项给出 $e^{+ika}$。于是

$$\hat H\lvert\psi_k\rangle = \Big(E_0 - t\,e^{ika} - t\,e^{-ika}\Big)\lvert\psi_k\rangle,$$

即 $\lvert\psi_k\rangle$ 确实是本征态，色散关系为

$$\boxed{\;E(k) = E_0 - 2t\cos(ka)\;}$$

- 带底 $E_0-2t$（$k=0$），带顶 $E_0+2t$（$k=\pm\pi/a$），**带宽 $4t$**；
- $t\to 0$（原子拉远）时带收缩回原子能级 $E_0$——原子极限自然回归；
- 每条原子能级给一条带；不同能级的轨道交叠不同，$t$ 不同，带宽各异。

这与近自由电子图像是互补的同一枚硬币：那里能隙来自区边界简并的解除，这里能隙是"相邻原子能级展成的两条带之间没被填上的能量区间"。

### 5.3 方格子推广

同样的推导搬到二维方格子（每格点一个轨道、最近邻 hopping $t$），只是对两个方向的邻居分别求和：

$$E(\vec k) = E_0 - 2t\big(\cos k_xa + \cos k_ya\big),$$

带宽 $8t$。一般规律：$E(\vec k) = E_0 - t\sum_{\vec\delta}e^{i\vec k\cdot\vec\delta}$，$\vec\delta$ 取遍最近邻格矢——色散关系完全由晶格几何决定。

## 6. 有效质量与空穴

### 6.1 群速度与有效质量

Bloch 态是扩展态，电子的实际运动要用波包描述。波包分析（标准结论，此处引用）给出**群速度**

$$\vec v(\vec k) = \frac{1}{\hbar}\,\nabla_{\vec k}\,E_n(\vec k),$$

以及半经典加速度定理：外场 $\vec F$ 下 $\hbar\,\dot{\vec k} = \vec F$（晶格动量的变化率 = 外力）。两式复合：

$$\dot{\vec v} = \frac{1}{\hbar}\nabla_{\vec k}\,E\ \Rightarrow\ \dot v_i = \frac{1}{\hbar^2}\sum_j\frac{\partial^2 E}{\partial k_i\partial k_j}\,F_j \equiv \sum_j \left(m^{*-1}\right)_{ij}F_j.$$

**有效质量张量**就是能带曲率的倒数。一维情形简化为标量：

$$\boxed{\;m^{*} = \hbar^2\left(\frac{\mathrm{d}^2E}{\mathrm{d}k^2}\right)^{-1}\;}$$

物理含义：周期势对电子的全部影响被"打包"进 $m^{*}$——对外场而言，电子就像质量为 $m^{*}$ 的自由粒子。带底附近 $E \approx E_{\min} + \hbar^2(k-k_0)^2/2m^{*}$，曲率为正，$m^{*}>0$，行为正常；曲率大（带窄）则 $m^{*}$ 小，曲率小（带宽）则 $m^{*}$ 大——窄带电子"重"，因为轨道交叠小、难以移动，直觉自洽。

### 6.2 带顶的负有效质量与空穴

带顶附近曲率为负，$m^{*}<0$：电子加速度与外力**反向**。与其跟踪"负质量电子"，更方便的语言是**空穴（hole）**。论证分两步：

1. **满带不导电**：对一维满带，总电流 $j \propto \sum_{k\in\text{BZ}}v(k)$。由 $E(k)=E(-k)$（时间反演对称）有 $v(-k)=-v(k)$，BZ 内成对抵消，$j=0$。所以满带里那 $2N$ 个电子对外场集体"免疫"（想加速就得有电子跃过能隙）。
2. **缺一个电子 = 一个空穴**：从满带中拿走 $k_e$ 处的电子，剩余体系的电流为 $0 - (-e)v(k_e) = +e\,v(k_e)$——等效于一个**电荷 $+e$、速度 $v(k_e)$** 的粒子。又空穴能量定义为缺失电子能量的负值，$E_h(k) = -E_e(k)$，带顶（电子曲率负）对应空穴的能带底（曲率正），故**空穴的有效质量为正**。

空穴不是新粒子，是"满带缺一个电子"的集体描述——但它有确定的电荷、速度和正有效质量，半导体物理（本书第 5 章，待写）里 p 型导电全靠它。

## 7. 金属还是绝缘体：能带填充计数

设晶体有 $N$ 个原胞。每条能带含 $N$ 个 $k$ 点，每个 $k$ 可容纳自旋上、下两个电子（Pauli 原理），故

$$\text{每条能带} = 2N \text{ 个态}.$$

$T=0$ 时电子从最低能量往上填。**判据**：

- **最上面的被占据带部分填充**（费米能 $E_F$ 穿过某条带的内部）→ 紧挨着 $E_F$ 上方就有无穷多空态，任意小的电场都能加速电子 → **金属**。
- **整数条带被恰好填满**，且最高满带（价带）与最低空带（导带）之间隔着有限能隙 $E_g$ → 电场无法移动满带电子，热激发需 $k_BT \sim E_g$ → **绝缘体**（$E_g$ 较小时称半导体，$\lesssim 2\,\text{eV}$ 量级）。

计数规则：**每个原胞的价电子数为奇数 ⇒ 必有一条带半满 ⇒ 金属**（在能带论框架内）；**偶数 ⇒ 可能是绝缘体，也可能因能带交叠仍是金属**（见下）。

- **碱金属**（Na、K……）：bcc，每原胞 1 个原子、1 个价电子，s 带恰半满 → 金属。
- **贵金属**（Cu、Ag、Au）：电子组态如 $3d^{10}4s^1$，5 条 d 带（每原胞 10 个态）恰好被 10 个 d 电子填满，剩下 1 个 s 电子使 s 带半满 → 金属。d 带虽满，却抬高了 s 带底的能量背景，造就了它们与碱金属不同的光学性质（颜色）。
- **金刚石**（C）：fcc 加双原子基元，每原胞 $2\times 4 = 8$ 个价电子；sp³ 杂化形成 4 条成键带（共 $8N$ 个态）恰好填满，导带隔着约 $5.5\,\text{eV}$ 的能隙 → 典型绝缘体。
- **二价元素为何仍是金属**（Mg、Ca、Zn……）：每原胞偶数个价电子，"填满 s 带"似乎是绝缘体——但这是在三维里，各条带的能量极值在 **k 空间不同点**达到。若 s 带顶的极大值高于 p 带底的极小值（**能带交叠**），电子就从 s 带顶溢出到 p 带底，两条带都部分填充 → 金属。交叠量很小的（如 Bi）称**半金属**。所以"偶数价 ⇒ 绝缘体"不成立；正确命题是"无交叠时偶数价 ⇒ 绝缘体"。

一句警告：以上全部建立在独立电子近似上。强关联体系中电子间的库仑排斥可以把"能带论预言的金属"变成绝缘体（Mott 绝缘体，如 NiO），见本书第 13 章（待写）——计数规则本身没有错，错的是"单电子能带"这个前提。

## 8. 费米面与态密度（浅述）

金属的占据区与空区在 k 空间的分界面称**费米面**（Fermi surface）——自由电子气的费米球（本书第 3 章，待写）被周期势扭曲后的样子。两点定性事实：

- **只有费米面附近的电子参与物理**。Pauli 原理把深处的电子锁死：热激发只搅动 $E_F$ 上下 $\sim k_BT$ 的一层，外场只能加速费米面上的电子。因此电导、热容、磁化率……几乎一切可测量都是费米面的几何性质（形状、速度、曲率）。测量并重建费米面（de Haas–van Alphen 效应等）是实验固体物理的一大篇章。
- **态密度**（density of states）把能带压成一维曲线：

$$g(E) = \sum_n \int_{\text{BZ}}\frac{\mathrm{d}^3k}{(2\pi)^3}\,\delta\!\big(E - E_n(\vec k)\big),$$

它数出单位能量区间内的态数。$g(E)$ 在 $\nabla_{\vec k}E = 0$ 处出现**van Hove 奇点**（一维中能带边缘 $g \sim \lvert\mathrm{d}E/\mathrm{d}k\rvert^{-1}\sim 1/\sqrt{\lvert E-E_{\text{边}}\rvert}$ 发散）。自由电子极限 $g(E)\propto\sqrt{E}$（第 3 章）；周期势在能隙处把 $g(E)$ 清零、在带边堆出奇点——费米能落在奇点附近往往酝酿着不稳定性（磁性、超导的温床），这是后续章节反复出现的主题。

## 9. 真实材料的能带计算（存在性声明）

本篇的两个极限模型给出了能带的"为什么"，而工程上"算出一条真实能带"靠两类方法，此处只声明其存在：

- **$\vec k\cdot\vec p$ 方法**：把 $u_{n\vec k}$ 满足的方程（第 3.3 节）里的 $\hbar\vec k\cdot\hat{\vec p}/m$ 当作微扰，用带极值点处的少数几条带的波函数做基，能把带边附近的色散（即有效质量）与其他带的跃迁矩阵元联系起来——是半导体多带模型与有效质量理论的骨架。
- **密度泛函理论（DFT）**：Hohenberg–Kohn 定理保证基态能量由电子密度唯一决定；Kohn–Sham 方案把相互作用多体问题映射回一个自洽有效周期势中的单电子问题——正是本篇开头那个 $V(\vec r)$ 的操作性定义。DFT（常用 LDA/GGA 泛函）已成为计算真实材料能带的标准工具，其著名软肋是系统性低估半导体能隙。

细节属于计算物理课程；对本书而言，记住"周期势不是假设，是可以算出来的"即可。

## 10. 小结

本篇的骨架：平移对称性 ⇒ Bloch 定理 ⇒ 能带与能隙 ⇒ 填充计数 ⇒ 金属/绝缘体。

| | 近自由电子近似 | 紧束缚近似 |
| --- | --- | --- |
| 出发点 | 自由电子气 + 弱周期势微扰 | 孤立原子轨道 + 弱交叠 |
| 适用对象 | 简单金属的 s/p 价电子 | 内层电子、d 带、分子晶体 |
| 能带如何出现 | 折叠抛物线在区边界的简并被解除 | 原子能级因 hopping $t$ 展宽 |
| 能隙的起源 | 区边界劈裂 $2\lvert V_G\rvert$ | 相邻两条带之间未覆盖的能量区间 |
| 标志公式 | $E_\pm$（简并 $2\times2$ 对角化） | $E(k)=E_0-2t\cos(ka)$（一维） |

- Bloch 定理：$\psi_{n\vec k}=e^{i\vec k\cdot\vec r}u_{n\vec k}$；$\vec k$ 限在第一 BZ，$n$ 为能带指标；$\hbar\vec k$ 是晶格动量，不是真实动量。
- 能隙大小直接量度周期势的傅里叶分量：$E_{\text{gap}}=2\lvert V_G\rvert$。
- 群速度 $\vec v=\hbar^{-1}\nabla_{\vec k}E$；有效质量 $m^{*}=\hbar^2(\mathrm{d}^2E/\mathrm{d}k^2)^{-1}$，带顶为负 → 空穴（电荷 $+e$、正有效质量）。
- 每条带 $2N$ 个态：半满 → 金属；全满且有能隙 → 绝缘体；能带交叠使二价元素（Mg 等）仍是金属。
- 独立电子近似是全部结论的地基；强关联（Mott 物理）会掀掉这块地基（第 13 章）。

## 自检问题

**1.** 从一维平移算符出发，完整证明 Bloch 定理：周期势中 $H$ 的本征态必可写成 $\psi(x)=e^{ikx}u(x)$，其中 $u(x+a)=u(x)$；并说明 $k$ 为何只需取在 $(-\pi/a,\,\pi/a]$ 内。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：$[\hat T_a, H]=0$。** 定义 $\hat T_a\psi(x)=\psi(x+a)$。动能：$\hat T_a\,\hat p^2\psi = -\hbar^2\partial_x^2\psi(x+a) = \hat p^2\hat T_a\psi$（导数与常数平移对易）；势能：$\hat T_a V(x)\psi(x) = V(x+a)\psi(x+a) = V(x)\,\hat T_a\psi(x)$（用了 $V(x+a)=V(x)$）。故 $[\hat T_a,H]=0$。

**第二步：定出 $\hat T_a$ 的本征值。** $\hat T_a$ 幺正（平移保持内积），本征值模为 1；又 $\hat T_a^m = \hat T_{ma}$，本征值须满足 $\lambda^m$ 自洽，故 $\lambda = e^{ika}$，$k\in\mathbb{R}$。于是

$$\psi(x+a) = e^{ika}\psi(x).$$

**第三步：凑出周期函数。** 令 $u(x) = e^{-ikx}\psi(x)$，则

$$u(x+a) = e^{-ik(x+a)}\,e^{ika}\psi(x) = e^{-ikx}\psi(x) = u(x),$$

即 $\psi = e^{ikx}u(x)$，$u$ 以 $a$ 为周期。由于 $H$ 与 $\hat T_a$ 对易，$H$ 的本征态总可取成这个形式（共同本征基定理）。

**$k$ 的范围**：$k$ 与 $k+2\pi m/a$ 给出同一个本征值 $e^{ika}$（因为 $e^{i(2\pi m/a)a}=1$），物理上不可区分，故把 $k$ 限制在长度为一个倒格矢的区间内，习惯取 $(-\pi/a,\,\pi/a]$。

</details>

**2.** 用简并微扰论推导一维近自由电子模型在区边界 $k=\pi/a$ 处的能隙 $E_{\text{gap}}=2\lvert V_G\rvert$（$G=2\pi/a$），并给出两个本征态的物理图像。

<details markdown="1"><summary>点击显示答案</summary>

零级谱 $E^0(k)=\hbar^2k^2/2m$。在 $k=\pi/a=G/2$ 处，

$$E^0\!\left(\tfrac{G}{2}\right) = \frac{\hbar^2(G/2)^2}{2m} = \frac{\hbar^2(G/2-G)^2}{2m} = E^0\!\left(-\tfrac{G}{2}\right),$$

即 $\lvert G/2\rangle$ 与 $\lvert -G/2\rangle = \lvert G/2 - G\rangle$ 简并，且被 $V$ 直接耦合：$\langle G/2\rvert V\lvert -G/2\rangle = V_{G}$（由 $V(x)=\sum_G V_G e^{iGx}$ 的选择定则）。按简并微扰论，在该子空间对角化

$$H_{\mathrm{eff}} = \begin{pmatrix} E^0 & V_G \\ V_G^{*} & E^0 \end{pmatrix}, \qquad E^0 \equiv \frac{\hbar^2(G/2)^2}{2m}.$$

久期方程 $(E^0-E)^2 - \lvert V_G\rvert^2 = 0$ 给出

$$E_\pm = E^0 \pm \lvert V_G\rvert \quad\Rightarrow\quad E_{\text{gap}} = E_+ - E_- = 2\lvert V_G\rvert.$$

**本征态**：设 $V_G$ 为实数（总可选能量原点与相位使然），$E_-$ 对应 $(\lvert G/2\rangle + \lvert -G/2\rangle)/\sqrt2 \propto \cos(Gx/2)$，$E_+$ 对应正弦组合。$V_G<0$ 时（吸引势，离子实位于 $x=na$），$\cos^2(Gx/2)$ 把电子密度堆在离子实上、能量低；$\sin^2$ 把密度堆在离子之间、能量高。两个驻波密度分布不同正是劈裂的来源——区边界上的行波被 Bragg 反射锁定成驻波。

</details>

**3.** 推导一维紧束缚模型的色散关系 $E(k)=E_0-2t\cos(ka)$，并求电子群速度的最大值及其出现位置。

<details markdown="1"><summary>点击显示答案</summary>

哈密顿量 $\hat H = \sum_n E_0\lvert n\rangle\langle n\rvert - t\sum_n(\lvert n\rangle\langle n+1\rvert + \lvert n+1\rangle\langle n\rvert)$，取 Bloch 试探态

$$\lvert\psi_k\rangle = \frac{1}{\sqrt N}\sum_n e^{ikna}\lvert n\rangle.$$

作用 $\hat H$：

$$\hat H\lvert\psi_k\rangle = \frac{1}{\sqrt N}\sum_n e^{ikna}\left[E_0\lvert n\rangle - t\lvert n+1\rangle - t\lvert n-1\rangle\right].$$

对第二项令 $m=n+1$：$\sum_n e^{ikna}\lvert n+1\rangle = e^{-ika}\sum_m e^{ikma}\lvert m\rangle = e^{-ika}\sqrt N\lvert\psi_k\rangle$；第三项同理给出 $e^{+ika}\sqrt N\lvert\psi_k\rangle$。于是

$$\hat H\lvert\psi_k\rangle = \left[E_0 - t\left(e^{ika}+e^{-ika}\right)\right]\lvert\psi_k\rangle = \left(E_0 - 2t\cos ka\right)\lvert\psi_k\rangle,$$

即 $E(k) = E_0 - 2t\cos(ka)$。

**群速度**：$v(k) = \hbar^{-1}\mathrm{d}E/\mathrm{d}k = \dfrac{2ta}{\hbar}\sin(ka)$。最大值出现在 $\lvert\sin(ka)\rvert = 1$ 即 $ka = \pm\pi/2$：

$$v_{\max} = \frac{2ta}{\hbar}.$$

物理检查：$t$ 越大（交叠越强）、$a$ 越大（一步跳得越远），电子跑得越快；区边界 $k=\pm\pi/a$ 处 $v=0$，与近自由电子图像中"驻波群速度为零"一致。

</details>

**4.** 对上题的一维余弦带，求有效质量 $m^{*}(k)$，给出带底与带顶的值，并指出 $m^{*}$ 在何处、以何种方式失效（发散）。

<details markdown="1"><summary>点击显示答案</summary>

由 $E(k) = E_0 - 2t\cos(ka)$：

$$\frac{\mathrm{d}^2E}{\mathrm{d}k^2} = 2ta^2\cos(ka) \quad\Rightarrow\quad m^{*}(k) = \frac{\hbar^2}{2ta^2\cos(ka)}.$$

- **带底** $k=0$：$\cos=1$，$m^{*} = \dfrac{\hbar^2}{2ta^2} > 0$。检验：带底展开 $E \approx (E_0-2t) + ta^2k^2$，与 $\hbar^2k^2/2m^{*}$ 对比得同一结果。
- **带顶** $k=\pm\pi/a$：$\cos=-1$，$m^{*} = -\dfrac{\hbar^2}{2ta^2} < 0$——负有效质量，空穴语言的用武之地（空穴质量为 $+\hbar^2/2ta^2$）。
- **发散点** $ka=\pm\pi/2$（恰是群速度最大处）：此处 $\mathrm{d}^2E/\mathrm{d}k^2=0$，$m^{*}\to\pm\infty$ 并变号。含义：能带在该点是拐点，二阶近似失效，$m^{*}$ 不再是个有用的参数——电子既不像自由正质量粒子也不像空穴，需要用更高阶的色散描述。这说明有效质量本质上是**带极值附近**的局域概念，不是一个全带通用的常数。

</details>

**5.** 镁（Mg）每个原子有 2 个价电子。按"每带 $2N$ 个态"的计数，它们似乎恰好填满一条带，应当是绝缘体——但 Mg 是金属。解释原因，并说明这一论证为什么对金刚石不成立（金刚石每个原胞 8 个价电子，是绝缘体）。

<details markdown="1"><summary>点击显示答案</summary>

**计数本身没错，缺的是"能带不交叠"这个隐含假设。** "偶数价 ⇒ 填满整数条带 ⇒ 绝缘体"要成为金属/绝缘体判据，必须额外要求：被填满的带的最高能量，处处低于下一条带的最低能量，即两带之间存在**全局能隙**。

在一维模型里每条带的能量区间互不重叠是常见情形；但在**三维**中，能带是定义在整个 BZ 上的函数 $E_n(\vec k)$，不同带的极值点在 k 空间不同位置达到。s 带在某个方向达到带顶时，p 带在另一个方向可能早已降到更低。Mg（3s²）的情形：3s 带顶的能量**高于** 3p 带底的能量——若电子全留在 s 带，把带顶附近的电子搬到 p 带底能降低总能量。于是 s 带顶部腾空、p 带底部部分填充，**两条带都部分占据**，费米面穿过两条带 → 金属。这叫**能带交叠**；交叠极小的材料（如 Bi）称半金属。

**金刚石为何不交叠**：碳的 2s、2p 轨道先发生 sp³ 杂化，形成成键态与反键态两组（各 4 条带），成键与反键之间隔着一个很大的、**在整个 BZ 上都成立**的能隙（约 5.5 eV）——这不是"s 带 p 带各自宽窄"的问题，而是杂化把谱劈成上下两簇。每原胞 8 个价电子恰好填满下簇 4 条成键带（共 $8N$ 个态），上簇全空且够不着 → 绝缘体。

一句话：判据的完整形式是"**整数条带被填满且最高满带与最低空带在 k 空间处处分离（有全局能隙）⇒ 绝缘体**"；二价金属输在第一句的"且"字上。

</details>

## 参考

- Kittel《固体物理导论》（第 8 版）第 7 章 "Energy Bands"（Bloch 函数、近自由电子模型、能隙的起源）与第 9 章 "Fermi Surfaces and Metals"（紧束缚法计算能带、费米面构造）。
- Ashcroft & Mermin《Solid State Physics》第 8–10 章（周期势中电子的一般性质、弱周期势近似、紧束缚方法）与第 12 章（半经典动力学、有效质量与空穴）、第 15 章（具体金属的能带，含二价金属的交叠讨论）。
- Singleton《Band Theory and Electronic Properties of Solids》第 2–4 章（Bloch 定理、近自由电子模型、紧束缚模型）——专题教材，推导节奏适合自学。
- 黄昆原著、韩汝琦改编《固体物理学》第 4 章（能带理论：Bloch 定理、近自由电子与紧束缚近似）与第 5 章（晶体中电子在电场磁场中的运动：准经典运动、有效质量、金属与绝缘体）。
