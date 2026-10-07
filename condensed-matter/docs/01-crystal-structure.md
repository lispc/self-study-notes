# 晶体结构：晶格、倒格子与 X 射线衍射

> 路线图位置：第一部分（结构与无相互作用电子）· 第 1 章
> 前置知识：矢量运算（点乘、叉乘、混合积）与傅里叶级数的基本概念。不需要量子力学——本章是全书唯一几乎纯经典（几何 + 波动光学）的一章。
> 学习目标：会用 $\vec R=n_1\vec a_1+n_2\vec a_2+n_3\vec a_3$ 描述 Bravais 点阵，分清原胞、惯用晶胞与 Wigner–Seitz 原胞，记住 sc/bcc/fcc/hcp/金刚石/NaCl/CsCl/钙钛矿八个标准结构的关键数字（胞内点数、配位数、致密度）；会从 $\vec a_i\cdot\vec b_j=2\pi\delta_{ij}$ 构造倒格子，证明"倒格子的倒格子是原格子"与"bcc 与 fcc 互倒"；理解周期函数的傅里叶分量只活在倒格矢上；会用 Laue 条件 $\Delta\vec k=\vec G$ 与结构因子 $S_{\vec G}$ 预言衍射峰的位置与系统消光，并读懂粉末衍射图。
>
> 记号约定：沿用本书（保留 $\hbar$ 与 $k_B$，电磁量用高斯单位制）。本章 $\vec R$ 一律指正格矢、$\vec G$ 一律指倒格矢；$\hbar$ 只在"准动量 $\hbar\vec k$"这类前瞻说法里露面。

---

## 1. 一句话总结

**晶体 = 点阵（数学上的重复清单）+ 基元（贴在每个格点上的原子配方），全部周期性压缩在三个基矢 $\vec a_1,\vec a_2,\vec a_3$ 里。倒格子——满足 $e^{i\vec G\cdot\vec R}=1$ 的全部波矢——是把"周期性"翻译成波矢空间的语言：周期函数的傅里叶分量只活在 $\vec G$ 上，而 X 射线衍射的 Laue 条件 $\Delta\vec k=\vec G$ 让每个衍射斑点对应一个倒格点，衍射图样就是倒格子的照片。这套正/倒对偶是全书舞台：第 2 章的声子色散 $\omega(\vec k)$ 与第 4 章的 Bloch 电子都住在倒格子的 Wigner–Seitz 原胞——第一 Brillouin 区里。**

## 2. 晶格与基元

### 2.1 Bravais 点阵：纯粹的重复

晶体的定义性对称性是**离散平移对称性**，其数学抽象为 **Bravais 点阵（Bravais lattice）**：

$$\vec R = n_1\vec a_1 + n_2\vec a_2 + n_3\vec a_3, \qquad n_1,n_2,n_3\in\mathbb{Z},$$

三个不共面的**初基矢量（primitive vectors）** $\vec a_1,\vec a_2,\vec a_3$ 张出全部格点。等价判据：从任一格点看出去，周围格点的排布与朝向完全相同——点阵处处"风景相同"。三维中只有 14 种不等价的 Bravais 点阵（二维 5 种），这是对称性分类的定理，本章只用结论。

真实晶体 = Bravais 点阵 + **基元（basis）**，即每个格点上重复粘贴的一组原子：

$$\text{晶体结构} \;=\; \text{点阵} \;+\; \text{基元}.$$

格点是数学点，不是原子——这是新手最容易翻船的地方。标准反例是二维蜂窝格子（石墨烯）：每个碳原子都有三个最近邻，但相邻两个原子周围键的取向相差 60°，"风景"不全同，所以蜂窝格子**不是** Bravais 点阵，它是"二维三角点阵 + 双原子基元"。三维版同款例子是金刚石（§2.3）。

### 2.2 三种"胞"：原胞、惯用晶胞、Wigner–Seitz 原胞

"重复单元"的取法不唯一，三种胞各有用途：

- **原胞（primitive cell）**：体积最小的重复单元，恰含 **1 个格点**。由初基矢量张成的平行六面体是最常用的原胞，体积

$$V_c = \vec a_1\cdot(\vec a_2\times\vec a_3).$$

原胞形状可以换（初基矢量的取法不唯一），但体积唯一：$V_c=$ 晶体总体积 $/$ 格点数。
- **惯用晶胞（conventional cell）**：为了让对称性显眼而故意取大的胞，可含多个格点。bcc 的立方胞含 2 个格点（8 顶点 $\times\frac18$ + 1 体心），fcc 含 4 个（8 顶点 $\times\frac18$ + 6 面心 $\times\frac12$）。文献中的晶格常数 $a$ 默认指惯用立方胞边长。
- **Wigner–Seitz 原胞（WS 原胞）**：取一格点，作它与所有近邻格点连线的垂直平分面，围出的区域——"离它比离任何其他格点更近的点的集合"。WS 原胞恰含 1 个格点、不依赖基矢选取、且保持点阵的全部点对称性。这个构造搬到倒格子里就是第一 Brillouin 区（§3.3），是全书最常用的"胞"。

另记一个常用数字：**配位数（coordination number）** = 最近邻格点数。

### 2.3 八个标准结构

本书以后会反复点名的八个结构（$a$ 为惯用立方胞边长；"点数"指惯用胞内的 Bravais 格点数，括号内为原子数）：

| 结构 | 点阵 + 基元 | 惯用胞点数（原子数） | 配位数 | 致密度 | 实例 |
|---|---|---|---|---|---|
| sc（简单立方） | sc + 单原子 | 1（1） | 6 | $\pi/6\approx0.52$ | Po |
| bcc（体心立方） | bcc + 单原子 | 2（2） | 8 | $\sqrt3\pi/8\approx0.68$ | Na、W、α-Fe |
| fcc（面心立方） | fcc + 单原子 | 4（4） | 12 | $\pi/(3\sqrt2)\approx0.74$ | Cu、Al、Au |
| hcp（六角密堆） | 简单六角 + 双原子 $\{0,(\tfrac13,\tfrac23,\tfrac12)\}$ | 3（6） | 12 | $0.74$（理想 $c/a$） | Mg、Zn、Ti |
| 金刚石 | fcc + 双原子 $\{0,\tfrac a4(1,1,1)\}$ | 4（8） | 4 | $\sqrt3\pi/16\approx0.34$ | C、Si、Ge |
| NaCl 型 | fcc + 双原子（Na 在 $0$、Cl 在 $\tfrac a2(1,0,0)$） | 4（4+4） | 6 | — | NaCl、KBr、NiO |
| CsCl 型 | sc + 双原子（Cl 在 $0$、Cs 在 $\tfrac a2(1,1,1)$） | 1（1+1） | 8 | — | CsCl、β-CuZn |
| 钙钛矿 ABO$_3$ | sc + 五原子基元（A 顶点、B 体心、O 面心） | 1（1+1+3） | — | — | SrTiO$_3$、BaTiO$_3$ |

几条注记：

- **致密度（packing fraction）** = 硬球模型下原子球体积占晶胞体积的比例。fcc 与理想 hcp（$c/a=\sqrt{8/3}\approx1.633$）同为最密堆积 $0.74$——两者都是二维密排层的堆垛，只是层序不同（fcc 是 ABCABC…、hcp 是 ABAB…）。bcc 的 $0.68$ 略松；金刚石的 $0.34$ 是共价键四面体方向性撑出来的空旷骨架（最近邻沿体对角线，距离 $\sqrt3\,a/4$）。sc 配位数只有 6、致密度 $\pi/6$，单质里只有 Po 赏脸。
- hcp 基元中 $(\tfrac13,\tfrac23,\tfrac12)$ 是 120° 夹角六角轴下的分数坐标，第二个原子坐在第一层三角形的空位正上方。
- **判断点阵先问"所有位置的环境是否全同"**：金刚石基元的两个原子是同种原子，但键取向相差 109.5°，所以点阵是 fcc 而非 sc；CsCl 看着像 bcc，但体心与顶点不是同种原子，点阵其实是 sc（"bcc + 单原子基元"与"sc + 双原子基元"在衍射上如何区分见 §4.3）；NaCl 则是两套 fcc 沿棱错开 $a/2$。
- 钙钛矿 SrTiO$_3$：Sr 在顶点、Ti 在体心、O 在三个面心。这个家族是铁电体（BaTiO$_3$）与铜基超导母体这类层状钙钛矿衍生物的舞台，第 8 章会回来。

自检问题 1 用 Cu 把 fcc 这一行的数字账完整走一遍（由 $a$ 算密度，对到实验值的 0.2%）。

## 3. 倒格子：周期性的波矢语言

### 3.1 定义与显式构造

对正格子提一个波动问题：哪些波矢 $\vec G$ 的平面波在所有格点上取值相同，即 $e^{i\vec G\cdot\vec R}=1$？满足条件的全部 $\vec G$ 构成**倒格子（reciprocal lattice）**：

$$\vec G\cdot\vec R = 2\pi\times\text{整数} \qquad \forall\ \vec R.$$

倒格子自己也是 Bravais 点阵，其基矢由对偶条件唯一确定：

$$\vec a_i\cdot\vec b_j = 2\pi\,\delta_{ij},$$

显式构造（三维的叉乘版本）：

$$\vec b_1 = 2\pi\,\frac{\vec a_2\times\vec a_3}{V_c}, \qquad \vec b_2 = 2\pi\,\frac{\vec a_3\times\vec a_1}{V_c}, \qquad \vec b_3 = 2\pi\,\frac{\vec a_1\times\vec a_2}{V_c}.$$

一眼可见 $\vec a_1\cdot\vec b_1=2\pi$（分子分母是同一个混合积）、$\vec a_2\cdot\vec b_1=0$（混合积中两矢量重复即零）。"构造唯一"与"倒格子的倒格子 = 原格子"的证明留作自检问题 2，那里还算出二维三角点阵的倒格子——仍是三角点阵，但整体旋转 30°。

两个常用事实：

- 一维格距 $a$ 的链，倒格子是 $G=2\pi m/a$（[第 2 章](02-lattice-vibrations-phonons.md)的一维链用的就是它）；
- 倒格子原胞体积 $V_c^\ast = \vec b_1\cdot(\vec b_2\times\vec b_3) = (2\pi)^3/V_c$——**正空间越疏，倒空间越密**，倒格矢尺度 $\sim 2\pi/a$。

### 3.2 物理意义：周期函数的傅里叶分量只活在倒格矢上

倒格子不是数学装饰。设 $V(\vec r)$ 是晶体中任何周期函数（电子感受到的离子势、X 射线看到的电子密度），$V(\vec r+\vec R)=V(\vec r)$。做傅里叶展开 $V(\vec r)=\sum_{\vec k}V_{\vec k}\,e^{i\vec k\cdot\vec r}$，周期性要求

$$\sum_{\vec k}V_{\vec k}\,e^{i\vec k\cdot\vec R}\,e^{i\vec k\cdot\vec r} = \sum_{\vec k}V_{\vec k}\,e^{i\vec k\cdot\vec r} \qquad \forall\ \vec R,$$

这对所有 $\vec R$ 成立，当且仅当每个实际出现的 $\vec k$ 都满足 $e^{i\vec k\cdot\vec R}=1$——即 $\vec k$ 必须是倒格矢。于是

$$\boxed{\;V(\vec r) = \sum_{\vec G}V_{\vec G}\,e^{i\vec G\cdot\vec r}\;}$$

**周期函数的谱是离散的，支撑集就是倒格子。** [第 4 章](04-band-theory.md)里在 BZ 边界打开能隙的周期势傅里叶分量 $V_{\vec G}$ 正是这里的对象；§4 的衍射振幅测的也是它们。一句话：倒格子是"周期性"的谱表示。

### 3.3 第一 Brillouin 区

对倒格子做 §2.2 的 WS 构造，得到的原胞叫**第一 Brillouin 区（BZ）**：倒空间中以某倒格点为中心、离它比离其他倒格点更近的区域。先记两条，其物理身份到第 2、4 章完全显明：

- BZ 体积 $=V_c^\ast=(2\pi)^3/V_c$；
- 格波或电子波的波矢 $\vec k$ 与 $\vec k+\vec G$ 在离散格点上不可区分（波长小于两倍格距的波被晶格"采样"混叠，即 aliasing），故独立的 $\vec k$ 恰好取满一个 BZ。[第 2 章](02-lattice-vibrations-phonons.md) §3.3 会在一维链上把这笔账数清楚：$N$ 个原胞 ↔ BZ 内恰好 $N$ 个允许的 $k$。

BZ 内高对称点（$\Gamma$、X、L……）是能带图横轴的语言，见[第 4 章](04-band-theory.md)。

### 3.4 bcc 与 fcc 互倒

最常用的一组对偶：**bcc 点阵的倒格子是 fcc，fcc 的倒格子是 bcc**。推导要点：取 bcc 的初基矢量

$$\vec a_1 = \frac a2(-1,1,1), \qquad \vec a_2 = \frac a2(1,-1,1), \qquad \vec a_3 = \frac a2(1,1,-1),$$

体积 $V_c=a^3/2$。代入叉乘公式，例如 $\vec a_2\times\vec a_3 = \frac{a^2}{2}(0,1,1)$，得

$$\vec b_1 = \frac{2\pi}{a}(0,1,1), \qquad \vec b_2 = \frac{2\pi}{a}(1,0,1), \qquad \vec b_3 = \frac{2\pi}{a}(1,1,0),$$

即立方边 $4\pi/a$ 的 fcc 的初基矢量（指向各面心）；对 fcc 初基矢量做同一套叉乘则回到 bcc。于是 **bcc 晶体的第一 BZ 是菱形十二面体（fcc 点阵的 WS 原胞），fcc 晶体（如 Cu）的第一 BZ 是截角八面体（bcc 点阵的 WS 原胞）**——第 4 章画 Cu 的能带时，横轴就住在截角八面体里。

## 4. X 射线衍射：倒格子的实验照片

倒格子讲完，还差实验上的读法。波长 $\sim1$ Å 的 X 射线与晶格常数同量级，晶体对它就是三维衍射光栅（von Laue 1912 年首证，Bragg 父子随即给出实用公式——两代人分获 1914、1915 年诺贝尔物理学奖）。

### 4.1 Bragg 定律与 Laue 条件：一个条件的两种说法

**Bragg 图像**：把晶体分解为一族族平行晶面，用 **Miller 指数（Miller indices）** $(hkl)$ 标记，面间距 $d_{hkl}$。X 射线在晶面上"镜面反射"，相邻面的光程差 $2d\sin\theta$（$\theta$ 为掠射角），相长条件

$$n\lambda = 2d\,\sin\theta \qquad \text{(Bragg 定律)}.$$

**Laue 图像**：所有格点的散射波振幅求和 $\sum_{\vec R}e^{i\Delta\vec k\cdot\vec R}$（$\Delta\vec k=\vec k'-\vec k$ 为波矢转移），要对 $N\sim10^{23}$ 个格点相干相长，必须

$$\boxed{\;\Delta\vec k \equiv \vec k'-\vec k = \vec G\;}\qquad \text{(Laue 条件)},$$

外加弹性散射条件 $\lvert\vec k'\rvert=\lvert\vec k\rvert=2\pi/\lambda$。

两者严格等价（两个方向的推导都留作自检问题 3）：由 $\vec k'=\vec k+\vec G$ 与等模长得 $2\vec k\cdot\vec G=-G^2$；取 $\vec G=n\vec G_0$（$\vec G_0$ 为垂直 $(hkl)$ 面族的最短倒格矢，$\lvert\vec G_0\rvert=2\pi/d_{hkl}$），化出的正是 $n\lambda=2d\sin\theta$。**所以衍射斑点 = 倒格点**：底片上每个亮斑可直接标定一个 $\vec G=h\vec b_1+k\vec b_2+l\vec b_3$；"$(hkl)$ 的 $n$ 级反射"就是倒格点 $(nh,nk,nl)$。这就是"XRD 是倒格子的照片"的准确含义。

### 4.2 散射振幅与结构因子

峰位由 Laue 条件钉死，峰的亮度则藏着基元的信息。X 射线被电子密度 $n(\vec r)$ 散射（高斯单位制下 Thomson 散射的经典电子半径 $r_0=e^2/mc^2$ 只进总强度，本章不追绝对强度），晶体总振幅是各体积元散射波的相干叠加：

$$F(\vec G) = \int_{\text{晶体}} n(\vec r)\,e^{i\vec G\cdot\vec r}\,d^3r.$$

把电子密度按晶胞分解：$n(\vec r)=\sum_{\vec R}\sum_j n_j(\vec r-\vec R-\vec r_j)$（$\vec r_j$ 为基元内第 $j$ 个原子在原胞中的位置），代入后求和因子化：

$$F = \underbrace{\sum_{\vec R}e^{i\vec G\cdot\vec R}}_{=\,N}\;\times\;\underbrace{\sum_j f_j(\vec G)\,e^{i\vec G\cdot\vec r_j}}_{S_{\vec G}\ \text{结构因子（structure factor）}},$$

其中**原子形状因子（atomic form factor）**

$$f_j(\vec G) = \int n_j(\vec\rho)\,e^{i\vec G\cdot\vec\rho}\,d^3\rho$$

是第 $j$ 个原子电子密度的傅里叶变换：$f_j(0)=Z_j$（电子数）；$\vec G$ 增大时电子云内部相互消光，$f_j$ 单调下降——这是衍射强度随角度衰减的原因之一。**结构因子 $S_{\vec G}$** 打包了基元内各原子的相位差，是基元的指纹，也是下一小节的主角。

### 4.3 系统消光：基元留下的空位

把 bcc 写成 sc 点阵 + 双原子基元 $\{0,\frac a2(1,1,1)\}$（同种原子，形状因子 $f$）。对 sc 的倒格矢 $\vec G=\frac{2\pi}{a}(h,k,l)$（$h,k,l$ 任意整数），

$$S_{\vec G} = f\big[1+e^{i\pi(h+k+l)}\big] = f\big[1+(-1)^{h+k+l}\big],$$

$h+k+l$ 为奇数时 $S_{\vec G}=0$——**(100)、(111) 等反射整体消失**：体心原子的散射波与顶点原子恰好反相。同理 fcc（基元 $\{0,\frac a2(0,1,1),\frac a2(1,0,1),\frac a2(1,1,0)\}$）：

$$S_{\vec G} = f\big[1+(-1)^{h+k}+(-1)^{h+l}+(-1)^{k+l}\big],$$

$h,k,l$ 全奇或全偶时 $S_{\vec G}=4f$，奇偶混杂时 $S_{\vec G}=0$。金刚石在 fcc 之上再乘基元因子 $1+e^{i\pi(h+k+l)/2}$，于是全偶但 $h+k+l=4n+2$ 的反射（如 (200)）额外消失——共价四面体配位在衍射图上的签名。这些**系统消光（systematic absences）**是结构鉴定的第一把钥匙：看一眼缺哪些峰，点阵类型就筛掉大半。完整推导（含强度对比）见自检问题 4。

### 4.4 热振动：Debye–Waller 因子

真实原子在平衡位置附近抖动（[第 2 章](02-lattice-vibrations-phonons.md)的声子），瞬时位置是 $\vec r_j+\vec u_j$。对热涨落平均后，衍射强度被乘上

$$I = I_0\,e^{-\frac13\langle u^2\rangle G^2} \equiv I_0\,e^{-2W},$$

即 **Debye–Waller 因子**：热运动压低强度（$G$ 越大压得越狠，高温下高角度峰先消失），但**不移动、不展宽峰位**——周期性没被破坏，只是"衬度"变差。所以低温下衍射峰更亮；即使 $T=0$，零点振动也残留这份压低。

### 4.5 粉末衍射：方向信息换成一维谱

单晶衍射给三维信息（每个斑点一个 $\vec G$），但先得长出单晶。**粉末衍射（powder diffraction）**把样品磨成随机取向的微晶：对每一族 $(hkl)$，总有一部分晶粒的取向恰好满足 Bragg 条件，反射束绕入射方向张成顶角 $4\theta$ 的 **Debye–Scherrer 锥**，底片上是一组同心环；现代衍射仪扫 $2\theta$ 角给出一维峰谱。方向信息被平均掉了（不同 $(hkl)$ 的峰可能重叠），但保留的 $d$ 值序列已经够用：立方晶系 $d_{hkl}=a/\sqrt{h^2+k^2+l^2}$，峰位比值直接鉴定点阵类型，配上密度还能定晶格常数乃至指认化学物种。自检问题 5 给一组真实数据走一遍完整流程。

## 5. 接口：本章在全书的位置

- **[第 2 章](02-lattice-vibrations-phonons.md)**：格波色散 $\omega(\vec k)$ 是倒格子的周期函数，$\omega(\vec k+\vec G)=\omega(\vec k)$；准动量"模 $\hbar\vec G$ 守恒"与 Umklapp 过程，根源就是本章的离散平移对称性。
- **[第 3 章](03-free-electron-gas.md)**：自由电子气先把离子抹平成均匀正电背景，但费米球与 BZ 边界的几何关系（相切还是相交）已经预告了能带结构。
- **[第 4 章](04-band-theory.md)**：Bloch 定理把单电子态按 $\vec k\in$ BZ 组织，§3.2 的傅里叶分量 $V_{\vec G}$ 在区边界打开能隙 $2\lvert V_{\vec G}\rvert$——能带论是本章几何的动力学化身。
- 衍射语言还会回访：第 8 章超导体的涡旋格子、第 13 章关联体系的电荷序，都靠散射实验"看见"周期结构。**周期结构的谱分析是贯穿全书的语法。**

## 小结

正格子与倒格子对照表：

| | 正格子 | 倒格子 |
|---|---|---|
| 基矢 | $\vec a_1,\vec a_2,\vec a_3$ | $\vec b_i$，由 $\vec a_i\cdot\vec b_j=2\pi\delta_{ij}$ 唯一确定 |
| 格矢 | $\vec R=\sum_i n_i\vec a_i$ | $\vec G=\sum_i m_i\vec b_i$，满足 $e^{i\vec G\cdot\vec R}=1$ |
| 原胞体积 | $V_c=\vec a_1\cdot(\vec a_2\times\vec a_3)$ | $V_c^\ast=(2\pi)^3/V_c$ |
| WS 原胞 | 普通 Wigner–Seitz 原胞 | 第一 Brillouin 区（声子与 Bloch 电子的家） |
| 对偶关系 | bcc ↔ fcc（立方边 $a$ ↔ $4\pi/a$） | 倒格子的倒格子 = 原格子 |
| 实验读出 | 形貌与成分的间接推断 | XRD：斑点 = 倒格点，强度 $\propto\lvert S_{\vec G}\rvert^2$ |

要点回顾：

- 晶体 = 点阵 + 基元。三种胞：原胞最小（恰 1 格点）、惯用胞显摆对称、WS 原胞最物理——搬到倒格子就是第一 Brillouin 区。
- 周期函数的傅里叶分量只活在倒格矢上：倒格子是周期性的谱。
- Laue 条件 $\Delta\vec k=\vec G$ ⟺ Bragg 定律 $n\lambda=2d\sin\theta$；结构因子 $S_{\vec G}$ 携带基元信息，产生系统消光（bcc：$h+k+l$ 为奇；fcc：奇偶混杂；金刚石：全偶但 $h+k+l=4n+2$）。
- Debye–Waller 因子压低强度但不动峰位；粉末衍射把三维倒格子压成一维 $d$ 值序列，仍足以鉴定 sc/bcc/fcc。

## 自检问题

**1.** Cu 为 fcc 结构，晶格常数 $a=3.61$ Å。计算：(a) 最近邻距离与硬球原子半径；(b) 致密度；(c) 质量密度（Cu 原子量 63.5），并与实验值 8.96 g/cm³ 对比。

<details markdown="1"><summary>点击显示答案</summary>

**(a)** fcc 最近邻沿面对角线方向（顶点原子与面心原子相切）：面对角线长 $\sqrt2\,a$ 上排 4 个半径，故

$$r = \frac{\sqrt2\,a}{4} = \frac{a}{2\sqrt2} \approx 1.28\ \text{Å}, \qquad \text{最近邻距离} = 2r = \frac{a}{\sqrt2} \approx 2.55\ \text{Å}.$$

**(b)** 惯用胞含 4 个原子，致密度

$$\eta = \frac{4\times\frac43\pi r^3}{a^3} = \frac{4\times\frac43\pi}{a^3}\left(\frac{\sqrt2\,a}{4}\right)^3 = \frac{\pi}{3\sqrt2} \approx 0.740,$$

与理想 hcp 并列最密堆积。

**(c)** 胞质量 $m = 4\times63.5/N_A = 254/(6.022\times10^{23}) = 4.22\times10^{-22}$ g，胞体积 $a^3 = (3.61\times10^{-8}\ \mathrm{cm})^3 = 4.70\times10^{-23}\ \mathrm{cm^3}$，故

$$\rho = \frac{m}{a^3} = \frac{4.22\times10^{-22}}{4.70\times10^{-23}} \approx 8.97\ \mathrm{g/cm^3},$$

与实验值 8.96 g/cm³ 吻合到 0.2%——"点阵 + 基元 + 硬球"语言经受住了数值检验。历史上这正是由 XRD 定 $a$、再由密度定 $N_A$ 的路线。

</details>

**2.** (a) 验证 §3.1 的叉乘构造满足 $\vec a_i\cdot\vec b_j=2\pi\delta_{ij}$，并证明满足该对偶条件的 $\vec b_j$ 唯一；(b) 证明倒格子的倒格子是原格子；(c) 求二维三角点阵 $\vec a_1=a(1,0)$、$\vec a_2=a(\tfrac12,\tfrac{\sqrt3}{2})$ 的倒格子基矢，说明它仍是三角点阵但相对正格子旋转了 30°。

<details markdown="1"><summary>点击显示答案</summary>

**(a)** 以 $j=1$ 为例：$\vec a_1\cdot\vec b_1 = 2\pi\,\vec a_1\cdot(\vec a_2\times\vec a_3)/V_c = 2\pi$（分子分母是同一个混合积）；$\vec a_2\cdot\vec b_1 \propto \vec a_2\cdot(\vec a_2\times\vec a_3) = 0$（混合积中两矢量重复），同理 $\vec a_3\cdot\vec b_1=0$。唯一性：设 $\vec b_1$ 与 $\vec b_1'$ 均满足条件，则差 $\Delta\vec b$ 与 $\vec a_1,\vec a_2,\vec a_3$ 全部正交；三者不共面、张满三维空间，故 $\Delta\vec b=0$。

**(b)** 对倒格子基矢再做一次叉乘构造：$\vec c_1 = 2\pi\,\vec b_2\times\vec b_3/V_c^\ast$，其中 $V_c^\ast=(2\pi)^3/V_c$。把定义代入并用二重叉积恒等式 $\vec u\times(\vec v\times\vec w)=\vec v(\vec u\cdot\vec w)-\vec w(\vec u\cdot\vec v)$：

$$\vec b_2\times\vec b_3 = \frac{(2\pi)^2}{V_c^2}\,(\vec a_3\times\vec a_1)\times(\vec a_1\times\vec a_2) = \frac{(2\pi)^2}{V_c^2}\,\vec a_1\,\big[(\vec a_3\times\vec a_1)\cdot\vec a_2\big] = \frac{(2\pi)^2}{V_c}\,\vec a_1,$$

最后一步用了 $(\vec a_3\times\vec a_1)\cdot\vec a_2 = V_c$ 与 $(\vec a_3\times\vec a_1)\cdot\vec a_1=0$。于是 $\vec c_1=\vec a_1$，循环得 $\vec c_2=\vec a_2$、$\vec c_3=\vec a_3$。更概念的说法：满足 $\vec c\cdot\vec G=2\pi\times$整数（对所有 $\vec G$）的 $\vec c$ 恰好就是全体 $\vec R$——对偶的对偶回到自身。

**(c)** 二维没有叉乘公式，直接解对偶条件 $\vec a_i\cdot\vec b_j=2\pi\delta_{ij}$。试

$$\vec b_1 = \frac{2\pi}{a}\left(1,-\frac{1}{\sqrt3}\right), \qquad \vec b_2 = \frac{2\pi}{a}\left(0,\frac{2}{\sqrt3}\right),$$

逐条验证：

$$\vec a_1\cdot\vec b_1 = 2\pi, \quad \vec a_1\cdot\vec b_2 = 0, \quad \vec a_2\cdot\vec b_1 = 2\pi\left(\frac12-\frac{\sqrt3}{2}\cdot\frac{1}{\sqrt3}\right) = 0, \quad \vec a_2\cdot\vec b_2 = 2\pi\cdot\frac{\sqrt3}{2}\cdot\frac{2}{\sqrt3} = 2\pi.\ \checkmark$$

几何读出：$\lvert\vec b_1\rvert=\lvert\vec b_2\rvert=4\pi/(\sqrt3\,a)$，夹角 $\cos\theta=\vec b_1\cdot\vec b_2/\lvert\vec b\rvert^2=-\tfrac12$ 即 $\theta=120°$（取 $-\vec b_1$ 即得 60° 夹角的标准基矢对）——仍是三角（六角）点阵；但 $\vec b_1$ 与 $x$ 轴夹角为 $-30°$，而 $\vec a_1$ 沿 $x$ 轴，**倒格子整体旋转了 30°**。石墨烯的第一 BZ 是六角形、顶点记 $K$ 与 $K'$，用的正是这套几何。

</details>

**3.** 证明 Bragg 定律 $n\lambda=2d\sin\theta$ 与 Laue 条件 $\Delta\vec k=\vec G$（配合弹性散射 $\lvert\vec k'\rvert=\lvert\vec k\rvert$）等价（两个方向都要证）。

<details markdown="1"><summary>点击显示答案</summary>

先备一个几何事实：倒格矢 $\vec G_0=h\vec b_1+k\vec b_2+l\vec b_3$（$h,k,l$ 互素）垂直于 $(hkl)$ 晶面族，且所有格点落在等距平面族 $\vec G_0\cdot\vec r=2\pi m$ 上，故面间距 $d=2\pi/\lvert\vec G_0\rvert$。

**Laue ⇒ Bragg**：$\vec k'=\vec k+\vec G$ 与 $\lvert\vec k'\rvert^2=\lvert\vec k\rvert^2$ 相减得

$$2\vec k\cdot\vec G = -G^2.$$

写 $\vec G=n\vec G_0$（$\vec G_0$ 为该方向最短倒格矢，$n$ 为正整数）。设 $\theta$ 为 $\vec k$ 与晶面的夹角（掠射角），则 $\vec k$ 与 $\hat G$ 的夹角为 $90°+\theta$，即 $\vec k\cdot\vec G=-\lvert\vec k\rvert\lvert\vec G\rvert\sin\theta$。代入上式：

$$2\lvert\vec k\rvert\sin\theta = \lvert\vec G\rvert = \frac{2\pi n}{d}.$$

再代入 $\lvert\vec k\rvert=2\pi/\lambda$：

$$n\lambda = 2d\sin\theta.\qquad\blacksquare$$

**Bragg ⇒ Laue**：给定 $(hkl)$ 面族的 $n$ 级反射，取 $\vec G=n\vec G_0$（长 $2\pi n/d$、沿面法线）。镜面反射使波矢平行于面的分量不变、法向分量反号，故 $\Delta\vec k$ 沿法线，大小

$$\lvert\Delta\vec k\rvert = 2\lvert\vec k\rvert\sin\theta = 2\cdot\frac{2\pi}{\lambda}\cdot\frac{n\lambda}{2d} = \frac{2\pi n}{d} = \lvert\vec G\rvert,$$

方向与大小都吻合，即 $\Delta\vec k=\vec G$。$\blacksquare$

物理注记：Bragg 的级次 $n$ 在 Laue 语言里被吸收进倒格矢——"$(hkl)$ 的 $n$ 级反射"就是倒格点 $(nh,nk,nl)$ 的反射。所以衍射理论只需一句话：斑点 = 倒格点。

</details>

**4.** 推导 bcc、fcc 的系统消光规则，并推出金刚石的额外消光（$h,k,l$ 全偶但 $h+k+l=4n+2$ 时消失，如 (200)）。

<details markdown="1"><summary>点击显示答案</summary>

**bcc** = sc 点阵 + 基元 $\{\vec r_1=0,\ \vec r_2=\frac a2(1,1,1)\}$（同种原子，形状因子 $f$）。对 $\vec G=\frac{2\pi}{a}(h,k,l)$：

$$\vec G\cdot\vec r_2 = \pi(h+k+l) \;\Longrightarrow\; S_{\vec G} = f\big[1+e^{i\pi(h+k+l)}\big] = f\big[1+(-1)^{h+k+l}\big].$$

$h+k+l$ 偶：$S_{\vec G}=2f$；奇：$S_{\vec G}=0$——(100)、(111)、(210)…… 整体消失。衍射强度 $\propto\lvert S_{\vec G}\rvert^2$，这些位置没有峰。

**fcc** = sc 点阵 + 基元 $\{0,\frac a2(0,1,1),\frac a2(1,0,1),\frac a2(1,1,0)\}$：

$$S_{\vec G} = f\big[1+e^{i\pi(k+l)}+e^{i\pi(h+l)}+e^{i\pi(h+k)}\big] = f\big[1+(-1)^{k+l}+(-1)^{h+l}+(-1)^{h+k}\big].$$

$h,k,l$ 全偶或全奇：三个指数全偶，$S_{\vec G}=4f$。奇偶混杂：三项中恰一项为 $+1$、两项为 $-1$（如 $h$ 奇 $k,l$ 偶：$(-1)^{k+l}=+1$，另两项为 $-1$），$S_{\vec G}=f[1+1-1-1]=0$。消光规则：**奇偶混杂消失**。

**金刚石** = fcc 点阵 + 双原子基元 $\{0,\frac a4(1,1,1)\}$，结构因子 = fcc 的晶格和 × 基元因子：

$$S^{\mathrm{dia}}_{\vec G} = S^{\mathrm{fcc}}_{\vec G}\times\big[1+e^{i\pi(h+k+l)/2}\big].$$

记 $s=h+k+l$，分情形：混合奇偶——$S^{\mathrm{fcc}}=0$，照旧消失；全奇——$e^{i\pi s/2}=\pm i$，$\lvert1\pm i\rvert^2=2$，故 $\lvert S\rvert^2=32f^2$；全偶 $s=4n$——因子为 $2$，$S=8f$；全偶 $s=4n+2$——$e^{i\pi(2n+1)}=-1$，因子为 $0$，**(200)、(222) 等消失**。成因直观：基元两原子沿体对角线错开 $a/4$，对 $s=4n+2$ 的 $\vec G$，两者散射波相位差 $\pi s/2=(2n+1)\pi$，恰好反相。实验上 Si 的粉末图缺 (200) 峰，一眼可辨金刚石结构。

</details>

**5.** 某立方晶系金属的粉末 XRD 前五个峰的 $d$ 值为 2.338、2.024、1.431、1.221、1.169 Å。鉴定其点阵类型并定出晶格常数；已知原子量 27.0，算密度并指认元素。

<details markdown="1"><summary>点击显示答案</summary>

**第一步：算 $1/d^2$ 的比值。** 立方晶系 $d_{hkl}=a/\sqrt N$（$N=h^2+k^2+l^2$），故 $1/d^2\propto N$：

$$\frac{1}{d^2} = 0.1829,\ 0.2439,\ 0.4879,\ 0.6708,\ 0.7318\ \text{Å}^{-2} \;\Longrightarrow\; \text{比值}\ 1 : 1.334 : 2.667 : 3.667 : 4.000,$$

乘 3 化为整数序列 $3:4:8:11:12$。

**第二步：比对三种立方点阵允许的 $N$ 序列。**

- sc（无消光）：$N=1,2,3,4,5,6,8,\dots$（$N=7$ 不能写成三整数平方和，天生缺失），比值 $1:2:3:4:5:6$；
- bcc（$h+k+l$ 偶）：$N=2,4,6,8,10,12,\dots$，比值同样是 $1:2:3:4:5:6$——**前五峰与 sc 不可区分**，要靠第七峰（bcc 有 $N=14$，sc 无 $N=7$）或密度区分；
- fcc（全奇或全偶）：$N=3,4,8,11,12,16,\dots$，比值 $3:4:8:11:12$。

实验序列 $3:4:8:11:12$ 精确命中 **fcc**（sc/bcc 的第二峰比值应为 2 而非 4/3，直接排除）。五峰依次标定为 (111)、(200)、(220)、(311)、(222)。

**第三步：定 $a$。** $a=d_{111}\sqrt3=2.338\times1.732=4.05$ Å；交叉验证：$2d_{200}=4.05$ Å、$\sqrt8\,d_{220}=1.431\times2.828=4.05$ Å，一致。

**第四步：密度认人。** fcc 惯用胞含 4 个原子：

$$\rho = \frac{4\times27.0}{N_A\,a^3} = \frac{108}{6.022\times10^{23}\times(4.05\times10^{-8})^3} = \frac{108}{40.0} \approx 2.70\ \mathrm{g/cm^3},$$

正是 Al（$a=4.05$ Å、$\rho=2.70$ g/cm³）。若误把首峰当 sc 的 (100)，会得 $a=2.34$ Å、$\rho\approx0.35$ g/cm³——不存在这样的金属，密度账立刻纠错。

</details>

## 参考

- Kittel《固体物理导论》第 1 章（晶体结构：点阵、基元、标准结构与计数）、第 2 章（晶体衍射与倒格子：Bragg/von Laue、结构因子与消光）——本章主线。
- Ashcroft & Mermin《Solid State Physics》第 4 章（Bravais 点阵与晶体结构分类）、第 5 章（倒格子）、第 6 章（X 射线与中子衍射）——更系统的推导与实验细节。
- 黄昆原著、韩汝琦改编《固体物理学》第 1 章（晶体结构、倒格子与晶体衍射）——中文教材中推导最紧凑的版本。
