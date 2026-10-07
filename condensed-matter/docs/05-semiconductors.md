# 半导体浅尝：有效质量、载流子统计与 pn 结

> 路线图位置：第一部分（结构与无相互作用电子）· 第 5 章
> 前置知识：[第 4 章](04-band-theory.md)（能带与能隙、有效质量与空穴、金属/绝缘体判据——本章全部建立在其 §6–§7 之上）；[第 3 章](03-free-electron-gas.md)（Fermi–Dirac 分布与态密度积分的手艺）；量子力学书[第 09s 篇](../../quantum-mechanics/docs/09s-fermi-dirac-derivation.md)（FD 分布的推导与经典极限）。
> 学习目标：记住半导体的能隙窗口（$0.1$–$3$ eV）与 Si/Ge/GaAs 的带隙数值，说清直接带隙与间接带隙对光学性质的分野；会在非简并近似下推出 $n=N_ce^{-(E_c-E_F)/k_BT}$、$p=N_ve^{-(E_F-E_v)/k_BT}$、本征浓度 $n_i$ 与质量作用定律 $np=n_i^2$；会用类氢模型估算施主/受主结合能（$\sim25$ meV 量级）并说明室温全电离；会由电中性条件定 $E_F(T)$ 并划分冻结、饱和、本征三个温区；会推内建电势 $eV_{\rm bi}=k_BT\ln(N_AN_D/n_i^2)$、耗尽宽度 $W$ 与 Shockley 二极管方程，并解释整流的方向性。
>
> 记号约定：沿用本书（保留 $\hbar$ 与 $k_B$；电磁量用高斯单位制——本章 Coulomb 势写 $-e^2/\varepsilon_r r$、Poisson 方程写 $\nabla^2\phi=-4\pi\rho/\varepsilon_r$，均不出现 $\varepsilon_0$；数值估算换算到 V、cm 等实用单位，数值结论与单位制无关）。$E_c$、$E_v$ 为导带底与价带顶能量，$E_g=E_c-E_v$；$m_n^*$、$m_p^*$ 为电子与空穴的（态密度）有效质量；$n$、$p$、$n_i$ 为电子、空穴与本征载流子浓度；$N_D$、$N_A$ 为施主、受主浓度；$e\gt0$ 为元电荷。

---

## 1. 一句话总结

**半导体是能隙恰好落在"室温能翻动它"的窗口（$0.1$–$3$ eV，即几倍到几十倍 $k_BT$）里的绝缘体：隙再小，本征载流子泛滥成半金属，可控性丧失；隙再大，室温下一个载流子也没有、杂质也电离不动，与绝缘体无别。窗口之内，载流子浓度低到 $10^{10}$–$10^{18}$ cm$^{-3}$（金属的百万分之一到万亿分之一），这带来两件定义性事实：一是统计敏感——载流子数目本身随温度指数变化，FD 分布的非简并尾巴（Maxwell–Boltzmann 极限）取代费米海成为工作语言；二是费米能级成为工程旋钮——百万分之一的掺杂就能把 $E_F$ 从隙中央推到带边附近，而把 p 型与 n 型拼在一起，$E_F$ 必须对齐这一件事就自动造出内建电势、耗尽层与整流特性。半导体器件物理的全部内容，都是这两个事实的展开。**

## 2. 半导体是什么：能隙窗口与载流子的两个来源

### 2.1 能隙窗口：$0.1$–$3$ eV

第 4 章 §7 的填充计数说：整数条带被填满且与空带间有全局能隙 = 绝缘体。半导体没有新的定义性结构——它就是**能隙大小合适的绝缘体**。窗口的两端各有物理理由（300 K 时 $k_BT\approx25.9$ meV）：

- **下界 $\sim$几倍 $k_BT$（$\sim0.1$ eV）**：隙太小，热激发失控。$E_g\sim0.1$ eV 意味着 $e^{-E_g/2k_BT}\sim e^{-2}\sim0.1$，本征载流子遍地都是，与半金属无别——"半导体"的可控性丧失。
- **上界 $\sim3$ eV**：隙太大，$e^{-E_g/2k_BT}\lesssim e^{-58}\sim10^{-25}$，室温下一个本征载流子也没有；杂质能级随之变深、难以电离。可见光光子（$1.7$–$3.1$ eV）穿隙而过——材料透明，是光学意义上的绝缘体。

窗口内的代表（数值均为 300 K 值）：

| 材料 | $E_g$（eV） | 带隙类型 | 一句话角色 |
|---|---|---|---|
| Ge | 0.67 | 间接 | 第一代晶体管材料；隙偏小、$n_i$ 大，器件怕热 |
| Si | 1.11 | 间接 | 现代电子工业的地基 |
| GaAs | 1.43 | 直接 | 发光与高速器件 |
| GaN | 3.4 | 直接 | 蓝光 LED 与功率电子（宽禁带一侧） |
| 金刚石 | 5.5 | 间接 | 对照组：已是绝缘体 |

### 2.2 直接带隙与间接带隙：光学性质的分野

eV 量级光子的波矢 $k_\gamma=E/\hbar c\sim10^{-3}$ Å$^{-1}$，只有 Brillouin 区尺度（$\sim$ Å$^{-1}$）的千分之一——**光跃迁在 k 空间是竖直的**（动量守恒近似为 $\vec k$ 不变）。

- **直接带隙**（GaAs、GaN）：导带底与价带顶在同一 $\vec k$ 点（都在 $\Gamma$）。竖直跃迁直接发生，吸收与发光都是强的一阶过程。
- **间接带隙**（Si：导带底在 $\Delta$ 线上靠近 X 点，价带顶在 $\Gamma$；Ge：导带底在 L 点）：带顶到带底的跃迁必须同时改变动量，需要一个声子提供或带走 $\hbar\vec q$——三体过程，概率低几个数量级。

工程分野一句话：**发光用直接隙**（LED、激光二极管全是 GaAs、GaN、InP 一族；Si 发光效率极低，硅基光源至今是难题）；**逻辑与功率器件用 Si**，靠的是别的优点（SiO$_2$ 界面近乎完美、工艺成熟、便宜）。间接隙的弱吸收也直接体现在器件尺寸上：Si 太阳能电池需要 $\sim100\ \mu$m 厚的吸收层，GaAs 薄膜几微米就够。

### 2.3 载流子的两个来源

半导体里的载流子远比金属少，来源只有两条路：

1. **热激发**：价带电子翻过能隙进入导带、留下空穴——成对产生，浓度 $n_i$ 随温度指数变化（§3.3）。这是本征（intrinsic）情形。
2. **掺杂**：百万分之一量级的杂质原子（Si 中掺 P、B）提供浅能级，室温下基本全电离，单方面供应电子或空穴（§4）。这是非本征（extrinsic）情形，也是一切器件的工作方式。

两条路都不经过"费米面穿过能带"——$E_F$ 始终留在隙内，这是半导体统计与金属（第 3 章）质的不同之根源。

## 3. 载流子统计：FD 分布的非简并极限

### 3.1 非简并近似：MB 尾巴接管

$E_F$ 在隙中、离两个带边都远（$E_c-E_F\gg k_BT$ 且 $E_F-E_v\gg k_BT$）时，导带每个态的占据数都远小于 1：

$$f(E) = \frac{1}{e^{(E-E_F)/k_BT}+1}\approx e^{-(E-E_F)/k_BT}\qquad(E\ge E_c).$$

这正是量子力学书[第 09s 篇](../../quantum-mechanics/docs/09s-fermi-dirac-derivation.md)的经典极限结论：每个轨道的平均占据数 $\ll1$ 时，FD 与 BE 分布都退化为 Maxwell–Boltzmann 分布。物理图像：导带电子稀薄到几乎从不抢同一个轨道，Pauli 原理失去后果，量子统计退回经典统计。价带侧对称处理——空穴的占据函数

$$1-f(E) = \frac{1}{e^{(E_F-E)/k_BT}+1}\approx e^{-(E_F-E)/k_BT}\qquad(E\le E_v).$$

注意这与金属是**同一个 FD 函数的两个渐近区**：金属里 $E_F$ 深埋带内（$E_F\gg k_BT$，强简并，零温阶跃），半导体里 $E_F$ 悬在隙中（非简并，指数尾巴）。第 3 章"只有费米面薄层参与、粒子数固定"的整套图像在此失效——这里**参与导电的载流子数目本身就是温度的函数**。

适用条件：掺杂不太重（Si 中 $\lesssim10^{18}$ cm$^{-3}$，换算见 §4.2）。再重则 $E_F$ 顶进带内，回到简并统计——"简并半导体"（如 MOSFET 的重掺源漏区）。

### 3.2 有效态密度：把整条带压缩成一个数

带边抛物化（第 4 章 §6）：导带底 $E(\vec k)=E_c+\hbar^2k^2/2m_n^*$，于是从带边量起的态密度就是第 3 章 §3.1 的自由电子公式换掉质量与能量零点：

$$g_c(E) = \frac{1}{2\pi^2}\left(\frac{2m_n^*}{\hbar^2}\right)^{3/2}\sqrt{E-E_c}\qquad(E\gt E_c).$$

导带电子浓度 = 态密度乘 MB 权重的积分：

$$n = \int_{E_c}^{\infty}g_c(E)\,e^{-(E-E_F)/k_BT}\,dE = N_c\,e^{-(E_c-E_F)/k_BT},\qquad N_c = 2\left(\frac{m_n^*k_BT}{2\pi\hbar^2}\right)^{3/2}.$$

（高斯积分 $\int_0^\infty\sqrt{x}\,e^{-x}dx=\sqrt\pi/2$ 收尾，完整代数见自检问题 1。）$N_c$ 称**导带有效态密度**：整条导带的热力学效果等价于"带边 $E_c$ 处堆着 $N_c$ 个态"。数值标尺：

$$N_c \approx 2.5\times10^{19}\left(\frac{m_n^*}{m}\right)^{3/2}\left(\frac{T}{300\ \mathrm K}\right)^{3/2}\ \mathrm{cm^{-3}}.$$

非简并条件翻译成浓度语言就是 $n\ll N_c$——电子浓度远小于有效态密度，轨道才"几乎总是空着"。价带侧镜像：

$$p = N_v\,e^{-(E_F-E_v)/k_BT},\qquad N_v = 2\left(\frac{m_p^*k_BT}{2\pi\hbar^2}\right)^{3/2}.$$

### 3.3 本征浓度与质量作用定律

两式相乘，$E_F$ 恰好消掉：

$$np = N_cN_v\,e^{-(E_c-E_v)/k_BT} = N_cN_v\,e^{-E_g/k_BT} \equiv n_i^2.$$

**质量作用定律**：$np$ 之积只由材料与温度决定，与掺杂无关——掺施主抬高 $n$，必然按同一比例压低 $p$，正如水里加酸压低 OH$^-$ 浓度而离子积不变。本征情形 $n=p=n_i$：

$$n_i = \sqrt{N_cN_v}\,e^{-E_g/2k_BT}.$$

Si、300 K：$N_c\approx2.8\times10^{19}$、$N_v\approx1.0\times10^{19}$ cm$^{-3}$、$E_g/2k_BT\approx21.5$，得 $n_i\approx10^{10}$ cm$^{-3}$（数值细节见自检问题 1）。对照 Si 原子密度 $5\times10^{22}$ cm$^{-3}$：**万亿个原子里才摊到一个载流子**。这一句话解释了两件事：半导体为什么对纯度极端敏感（ppm 级杂质即可压倒本征载流子），以及 pn 结反向电流为何天生极小（§5.3）。

### 3.4 本征费米能级：隙中央加一个小修正

本征条件 $n=p$：

$$N_c\,e^{-(E_c-E_i)/k_BT} = N_v\,e^{-(E_i-E_v)/k_BT} \;\Rightarrow\; E_i = \frac{E_c+E_v}{2} + \frac{1}{2}k_BT\ln\frac{N_v}{N_c} = \frac{E_c+E_v}{2} + \frac{3}{4}k_BT\ln\frac{m_p^*}{m_n^*}.$$

修正项通常只有十几 meV（Si：$m_p^*/m_n^*\sim0.5$，修正 $\approx-13$ meV）——**$E_F$ 基本钉在隙中央**。直观：有效质量大的一侧态密度大、更容易装载流子，$E_F$ 要稍稍向另一侧挪动来平衡两边计数。

## 4. 掺杂：把费米能级变成工程旋钮

### 4.1 施主与受主：类氢模型

Si 是四价：金刚石结构里每个原子四条共价键。换上一个五价原子（P、As、Sb——**施主**）：四个电子成键，第五个电子多余，只受 P$^+$ 核心的微弱束缚。把晶体当作介电常数 $\varepsilon_r$ 的连续介质、电子带有效质量 $m_n^*$，问题化为**屏蔽库仑势中的氢原子**（高斯单位制）：

$$\left[-\frac{\hbar^2}{2m_n^*}\nabla^2 - \frac{e^2}{\varepsilon_r r}\right]\psi = E\psi.$$

氢原子公式做两处替换 $m\to m_n^*$、$e^2\to e^2/\varepsilon_r$：

$$E_d = \frac{m_n^*e^4}{2\varepsilon_r^2\hbar^2} = 13.6\ \mathrm{eV}\times\frac{m_n^*/m}{\varepsilon_r^2},\qquad a^* = \varepsilon_r\,\frac{m}{m_n^*}\,a_0.$$

代入 Si 的参数（$\varepsilon_r=11.7$、电导有效质量 $m_n^*\approx0.26m$）：

$$E_d \approx 13.6\times\frac{0.26}{11.7^2}\ \mathrm{eV}\approx26\ \mathrm{meV},\qquad a^*\approx\frac{11.7}{0.26}\times0.53\ \text{Å}\approx2.4\ \mathrm{nm}.$$

三点评注：

- **$E_d$ 与室温 $k_BT$ 同级**（300 K 时 26 meV）——"浅"杂质的含义：室温下施主基本全部电离（定量判据见 §4.3 与自检问题 3）。实测值 P 45、As 54、Sb 43 meV：类氢模型抓对了量级与材料系统学，剩下的因子约 2 来自杂质原胞处的势偏离 $1/r$（中心元胞修正）与有效质量各向异性。
- **$a^*\sim2$ nm，轨道覆盖约 $10^3$ 个原子**——这正是模型自洽之处：束缚轨道远大于格点间距，用宏观 $\varepsilon_r$ 与带边 $m^*$ 的连续介质处理才合法。整个估算只用有效质量概念就把氢原子缩放进了晶体，是第 4 章 §6"$m^*$ 打包周期势"最便宜的胜利。
- 受主（B、Al，三价）镜像：从价带抓一个电子来成键、留下一个空穴，受主能级钉在 $E_v$ 上方几十 meV 处（B in Si：45 meV）。

### 4.2 n 型、p 型与电中性条件

掺施主为 **n 型**（电子是**多数载流子**，空穴是少数载流子），掺受主为 **p 型**（反之）。给定 $N_D$、$N_A$ 后，$E_F$ 由**电中性条件**锁定：

$$n + N_A^- = p + N_D^+,$$

其中 $N_D^+ = N_D\big[1+2e^{(E_F-E_D)/k_BT}\big]^{-1}$ 为电离施主浓度（因子 2 是施主基态的自旋简并），$N_A^-$ 同理。室温饱和区里杂质全电离（$N_D^+\approx N_D$）且多子压倒本征浓度（$N_D\gg n_i$），n 型：

$$n \approx N_D,\qquad p = \frac{n_i^2}{N_D},\qquad E_F = E_c - k_BT\ln\frac{N_c}{N_D}.$$

Si、$N_D=10^{16}$ cm$^{-3}$、300 K：$n=10^{16}$ cm$^{-3}$，$p\approx10^{20}/10^{16}=10^4$ cm$^{-3}$——少子浓度被质量作用定律压到微乎其微，但它是 §5 二极管反向电流与双极晶体管的全部工作物质；$E_c-E_F\approx0.21$ eV。

工程观点：$10^{16}$ cm$^{-3}$ 的掺杂相当于**五百万个 Si 原子里换掉一个**，却把 $E_F$ 从隙中央（本征）推到了距导带底 0.2 eV 处。金属里 $E_F$ 被 $10^{23}$ cm$^{-3}$ 个电子钉死在带内，掺什么都挪不动；半导体里 $E_F$ 是可随意摆放的旋钮——这是半导体与金属最深刻的使用差别。

### 4.3 三个温区：冻结、饱和、本征

固定 $N_D$，升温时 $n(T)$ 依次穿过三个区域（Arrhenius 图 $\ln n$ 对 $1/T$ 是经典实验图谱，两个指数段的斜率分别量出 $E_d$ 与 $E_g$）：

1. **冻结区**（低温，$k_BT\lesssim E_d$）：电子凝回施主上，弱电离极限下电中性条件给出 $n\approx\sqrt{N_cN_D/2}\,e^{-E_d/2k_BT}$（推导见自检问题 3）——随 $T$ 下降指数暴跌。Si、$N_D=10^{16}$ cm$^{-3}$ 时半电离点约在 90 K 附近。
2. **非本征（饱和）区**（中温，$E_d\ll k_BT$ 且 $n_i\ll N_D$）：施主全电离而本征激发尚未起来，$n\approx N_D$ 不随温度变——器件的工作窗口。对 $N_D=10^{16}$ cm$^{-3}$ 的 Si，约从 100 K 延伸到 $\sim750$ K（本征浓度追上 $N_D$ 处，数值见自检问题 3）。
3. **本征区**（高温，$n_i(T)\gg N_D$）：热激发压过掺杂，$n\approx p\approx n_i\propto e^{-E_g/2k_BT}$，材料"忘记"自己被掺过，$E_F$ 回到隙中央附近。这是器件结漏电失控的温区；Si 器件的工作上限（$\sim400$ K）远在窗口之内，而 GaN、SiC 这类宽禁带材料的价值正在于把本征区推向更高的温度。

$E_F(T)$ 的轨迹串起三区：$T\to0$ 时停在施主能级与 $E_c$ 之间（施主半占据），饱和区按 $E_c-E_F=k_BT\ln(N_c/N_D)$ 缓慢下沉，本征区奔向 $E_i$。

## 5. pn 结：费米能级对齐造出的器件

### 5.1 形成的本质：一条 $E_F$ 拉平两块材料

p 型与 n 型接触的瞬间，两侧 $E_F$ 不等（n 侧近 $E_c$、p 侧近 $E_v$）。电子从 n 侧涌向 p 侧（浓度梯度驱动），在界面附近留下电离施主的正电荷；空穴反向，留下电离受主的负电荷——界面处出现**空间电荷区**，其电场（方向由 n 指向 p）恰好阻止进一步的扩散。平衡的判据只有一个：**电流由 $E_F$ 的梯度驱动，无净电流 ⟺ 全体系 $E_F$ 处处相等**。两侧能带因此整体错开一个**内建电势**（built-in potential）$V_{\rm bi}$，其数值等于接触前两 $E_F$ 之差。用 $n=n_ie^{(E_F-E_i)/k_BT}$（由 $n=N_ce^{-(E_c-E_F)/k_BT}$ 与 $n_i$ 的定义相除即得），n 侧 $E_F^n-E_i=k_BT\ln(N_D/n_i)$，p 侧 $E_i-E_F^p=k_BT\ln(N_A/n_i)$，相加：

$$eV_{\rm bi} = k_BT\ln\frac{N_D}{n_i} + k_BT\ln\frac{N_A}{n_i} = k_BT\ln\frac{N_AN_D}{n_i^2}.$$

Si、$N_A=N_D=10^{16}$ cm$^{-3}$：$eV_{\rm bi}=k_BT\ln(10^{32}/10^{20})=12k_BT\ln10\approx0.72$ eV。注意 $V_{\rm bi}$ 不是外加可测的电压——它被接触电势差吸收，其物理作用是弯折能带、挡住多子扩散。

### 5.2 耗尽近似：Poisson 方程的分段积分

空间电荷区里能带弯曲 $\sim eV_{\rm bi}\gg k_BT$，可动载流子被电场扫光——**耗尽近似**：区内只剩固定的电离杂质电荷，区外完全中性。取冶金结界面为 $x=0$，耗尽区 $-x_p\lt x\lt x_n$，电荷密度分段常数（高斯单位制的 Poisson 方程）：

$$\frac{d^2\phi}{dx^2} = -\frac{4\pi\rho}{\varepsilon_r},\qquad \rho(x) = \begin{cases}-eN_A, & -x_p\lt x\lt0,\\ +eN_D, & 0\lt x\lt x_n.\end{cases}$$

边界条件：电场在耗尽层边界处为零（区外中性），整体电荷平衡 $N_Ax_p=N_Dx_n$。逐段积分（完整代数见自检问题 4）：电场是分段线性的三角形、峰值在界面处；电势是分段抛物线，两侧降落各为

$$\Delta V_n = \frac{2\pi eN_D}{\varepsilon_r}\,x_n^2,\qquad \Delta V_p = \frac{2\pi eN_A}{\varepsilon_r}\,x_p^2,\qquad \Delta V_n+\Delta V_p = V_{\rm bi}.$$

消去 $x_n$、$x_p$ 得**耗尽宽度**

$$W = x_n+x_p = \sqrt{\frac{\varepsilon_r}{2\pi e}\,\frac{N_A+N_D}{N_AN_D}\,V_{\rm bi}},$$

换回 SI 单位（$\varepsilon_r/4\pi\to\varepsilon_0\varepsilon_r$）即常见教科书形式 $W=\sqrt{\frac{2\varepsilon_0\varepsilon_r}{e}\big(\frac{1}{N_A}+\frac{1}{N_D}\big)V_{\rm bi}}$，数值与单位制无关。峰电场 $\mathcal{E}_{\max}=2V_{\rm bi}/W$。

数值（Si、$N_A=N_D=10^{16}$ cm$^{-3}$、300 K）：$V_{\rm bi}\approx0.72$ V，$W\approx0.43\ \mu$m，$\mathcal{E}_{\max}\approx3.3\times10^4$ V/cm。由 $x_n/x_p=N_A/N_D$，掺杂越重的一侧耗尽层越窄——单边突变结（p$^+$n 等）的耗尽层几乎全长在轻掺杂一侧。加偏压 $V$ 后结两端势垒变为 $V_{\rm bi}-V$（正偏降压），上面所有公式把 $V_{\rm bi}$ 换成 $V_{\rm bi}-V$ 即得偏压下的结果：耗尽宽度随反偏展宽（$W\propto\sqrt{V_{\rm bi}-V}$），这正是变容二极管的工作原理。

### 5.3 I–V 特性：Shockley 二极管方程

推导骨架（完整版是自检问题 5）由三个部件拼成：

1. **结律（边界条件）**：耗尽层薄、其内复合可忽略，两侧各自准平衡，跨越势垒的 Boltzmann 因子锁住边界浓度：n 区耗尽边界处的空穴浓度 $p_n(x_n)=p_{n0}e^{eV/k_BT}$（$p_{n0}=n_i^2/N_D$ 为平衡值）。正偏 $V\gt0$ 把边界浓度指数抬高，反偏把它压向零——整流的种子已经埋在边界条件里。
2. **扩散方程**：注入中性区的少子边扩散边复合，$D_p\frac{d^2\delta p}{dx^2}=\frac{\delta p}{\tau_p}$，解为指数衰减，特征长度是扩散长度 $L_p=\sqrt{D_p\tau_p}$（典型几十 $\mu$m）。
3. **电流 = 耗尽边界处的少子扩散流**：$J_p=-eD_p\frac{d\delta p}{dx}\Big|_{x_n}=\frac{eD_pp_{n0}}{L_p}\big(e^{eV/k_BT}-1\big)$；n 侧电子注入 p 区的贡献镜像相加：

$$I = I_s\left(e^{eV/k_BT}-1\right),\qquad I_s = eA\,n_i^2\left(\frac{D_p}{L_pN_D} + \frac{D_n}{L_nN_A}\right).$$

这就是 **Shockley 二极管方程**；$-1$ 项保证 $V=0$ 时无电流——热力学一致性。

整流的方向性一目了然：**正偏**降低势垒，多子（n 侧电子、p 侧空穴，浓度 $\sim N$）源源注入对方，供给无限，电流随 $e^{eV/k_BT}$ 爆炸（Si 管 0.6–0.7 V 即导通）；**反偏**升高势垒，电流只剩"把两侧的少子扫过结"，而少子浓度被质量作用定律钉在 $n_i^2/N$ 的地板上——供给封顶，电流饱和在 $-I_s$。不对称的定量幅度：$V=\pm0.7$ V 时 $e^{eV/k_BT}\sim e^{27}\sim5\times10^{11}$，十二个数位级的单向性。且 $I_s\propto n_i^2$：Si 二极管 $J_s\sim10^{-11}$ A/cm$^2$（自检问题 5），而 Ge 的 $n_i$（$2.4\times10^{13}$ cm$^{-3}$）约 Si 的两千多倍，结漏电同比例放大——**这是 Si 取代 Ge 赢下半导体工业的深层物理原因之一**（另一个是 SiO$_2$ 的界面质量）。

### 5.4 击穿与应用（各一句话）

反向电压加到尽头有两条击穿路径：**齐纳击穿**（重掺杂、耗尽层薄，带间隧穿，低电压）与**雪崩击穿**（载流子在峰电场中碰撞电离、连锁增殖，高电压）；利用击穿电压的稳定性做成稳压二极管。应用家族：整流（§5.3 的不对称性本身）；LED（正偏注入的载流子在直接隙材料里辐射复合——§2.2 的分野在此兑现）；太阳能电池与光电探测器（光生电子–空穴对被内建电场扫向两侧，零偏压即可发电）；以及作为一切现代晶体管（BJT、MOSFET）的母结构——pn 结是半导体器件的原子。

## 6. 接口

- **有效质量**（[第 4 章](04-band-theory.md) §6）：本章把"带边抛物化、周期势打包进 $m^*$"用到极致——$N_c$、$N_v$、类氢杂质的 $E_d$ 与 $a^*$ 全部只是 $m^*$ 与 $\varepsilon_r$ 的函数；空穴概念则是 p 型导电与 pn 结两侧对称语言的来源。
- **载流子统计**（[第 3 章](03-free-electron-gas.md)）：同一个 FD 分布的两个渐近区——金属是 $E_F$ 深埋带内的简并极限（费米海、Sommerfeld 展开），半导体是 $E_F$ 悬在隙中的非简并极限（MB 尾巴、指数温度依赖），第 3 章近满带处埋下的空穴概念在此成为一等公民。量子力学书[第 09s 篇](../../quantum-mechanics/docs/09s-fermi-dirac-derivation.md)的经典极限论证（占据数 $\ll1$ 时量子统计退化为 MB）在这里找到了产业规模最大的应用。
- **光电子学与激发态**（[第 19 章](19-excited-states.md)）：§2.2 说"发光用直接隙"，定量的发光效率与吸收谱涉及电子–空穴束缚态（激子）与 Bethe–Salpeter 方程——激发态方法一章的 BSE 部分直接从本章的带边出发。
- **器件地基**：pn 结向上是 BJT 与 MOSFET（全部现代电子学），向外是 LED、激光器与太阳能电池（全部现代光电子学）。半导体也是本书后续讨论"真实材料"时默认的样品平台——第 6 章的屏蔽、第 10 章介观输运的 2DEG、第 12 章的拓扑绝缘体（本质是特殊能隙的半导体）都站在本章的能带语言上。

## 小结

- 半导体 = 能隙落在 $0.1$–$3$ eV 窗口的绝缘体：下界由"隙必须远大于 $k_BT$，否则本征载流子泛滥"设定，上界由"隙太大则室温无载流子、杂质也难电离"设定。直接隙（GaAs、GaN）发光强；间接隙（Si、Ge）光跃迁需声子协助、弱——发光用直接隙，逻辑用 Si。
- 非简并近似（$E_F$ 离两个带边都 $\gg k_BT$）下 FD 退化为 MB：$n=N_ce^{-(E_c-E_F)/k_BT}$，$p=N_ve^{-(E_F-E_v)/k_BT}$，$N_{c,v}=2(m_{n,p}^*k_BT/2\pi\hbar^2)^{3/2}\sim10^{19}$ cm$^{-3}$。
- 质量作用定律 $np=n_i^2$ 与掺杂无关；$n_i=\sqrt{N_cN_v}\,e^{-E_g/2k_BT}$（Si、300 K：$\sim10^{10}$ cm$^{-3}$，万亿原子摊一个载流子）；$E_i$ 在隙中央加 $\tfrac34 k_BT\ln(m_p^*/m_n^*)$ 修正。
- 类氢杂质：$E_d=13.6\ \mathrm{eV}\times(m^*/m)/\varepsilon_r^2\sim25$ meV（Si），$a^*\sim2$ nm——与室温 $k_BT$ 同级，室温全电离。三个温区：冻结（$n\propto e^{-E_d/2k_BT}$）→ 饱和（$n\approx N_D$，器件窗口）→ 本征（$n\approx n_i\propto e^{-E_g/2k_BT}$）。
- pn 结 = $E_F$ 对齐的产物：$eV_{\rm bi}=k_BT\ln(N_AN_D/n_i^2)$；耗尽近似给出 $W=\sqrt{\frac{\varepsilon_r}{2\pi e}\frac{N_A+N_D}{N_AN_D}V_{\rm bi}}$（Si 典型 $0.4\ \mu$m）；Shockley 方程 $I=I_s(e^{eV/k_BT}-1)$ 的整流不对称来自"正偏放多子过闸（供给无限）对反偏收少子（供给封顶在 $n_i^2/N$）"，且 $I_s\propto n_i^2$。

三类半导体对照：

| | 本征 | n 型 | p 型 |
|---|---|---|---|
| 掺杂 | 无 | 施主（P、As 等五价） | 受主（B、Al 等三价） |
| 多数载流子 | 电子与空穴等量，$n=p=n_i$ | 电子，$n\approx N_D$ | 空穴，$p\approx N_A$ |
| 少数载流子 | 同左（无多子/少子之分） | 空穴，$p=n_i^2/N_D$ | 电子，$n=n_i^2/N_A$ |
| $E_F$ 位置 | 隙中央附近（$E_i$） | 近 $E_c$：$E_c-E_F=k_BT\ln(N_c/N_D)$ | 近 $E_v$：$E_F-E_v=k_BT\ln(N_v/N_A)$ |
| Si、300 K 典型浓度 | $10^{10}$ cm$^{-3}$ | $n\sim10^{16}$、$p\sim10^{4}$ cm$^{-3}$ | $p\sim10^{16}$、$n\sim10^{4}$ cm$^{-3}$ |

## 自检问题

**1.** 载流子统计的主积分：从抛物带边的态密度与 MB 分布出发，完成积分推出 $n=N_ce^{-(E_c-E_F)/k_BT}$ 与 $N_c=2(m_n^*k_BT/2\pi\hbar^2)^{3/2}$；写出 $p$ 的对应结果；由此推出质量作用定律与 $n_i$ 的表达式，并计算 Si 在 300 K 的 $N_c$（取 $m_n^*=1.08m$）与 $n_i$（取 $N_v=1.0\times10^{19}$ cm$^{-3}$、$E_g=1.11$ eV）。

<details markdown="1"><summary>点击显示答案</summary>

导带底抛物化 $E(\vec k)=E_c+\hbar^2k^2/2m_n^*$，从带边量起的态密度（自旋二重，第 3 章 §3.1 的公式换质量与能量零点）

$$g_c(E) = \frac{1}{2\pi^2}\left(\frac{2m_n^*}{\hbar^2}\right)^{3/2}\sqrt{E-E_c}\,\theta(E-E_c).$$

非简并近似 $f\approx e^{-(E-E_F)/k_BT}$ 下

$$n = \int_{E_c}^{\infty}g_c(E)\,e^{-(E-E_F)/k_BT}dE = \frac{1}{2\pi^2}\left(\frac{2m_n^*}{\hbar^2}\right)^{3/2}e^{-(E_c-E_F)/k_BT}\int_0^{\infty}\sqrt{\varepsilon}\,e^{-\varepsilon/k_BT}d\varepsilon,$$

其中 $\varepsilon=E-E_c$。换元 $x=\varepsilon/k_BT$，积分变为 $(k_BT)^{3/2}\Gamma(3/2)=(k_BT)^{3/2}\sqrt\pi/2$：

$$n = \frac{1}{2\pi^2}\left(\frac{2m_n^*}{\hbar^2}\right)^{3/2}(k_BT)^{3/2}\frac{\sqrt\pi}{2}\,e^{-(E_c-E_F)/k_BT} = 2\left(\frac{m_n^*k_BT}{2\pi\hbar^2}\right)^{3/2}e^{-(E_c-E_F)/k_BT},$$

（系数核对：$\frac{2^{3/2}\sqrt\pi}{4\pi^2}=\frac{2}{(2\pi)^{3/2}}$。）价带侧对空穴占据函数 $1-f$ 做同一积分，得 $p=N_ve^{-(E_F-E_v)/k_BT}$，$N_v=2(m_p^*k_BT/2\pi\hbar^2)^{3/2}$。

相乘：$np=N_cN_ve^{-(E_c-E_v)/k_BT}=N_cN_ve^{-E_g/k_BT}$——$E_F$ 消失，与掺杂无关，这就是质量作用定律。本征情形 $n=p\equiv n_i$，故 $n_i^2=N_cN_ve^{-E_g/k_BT}$，即 $n_i=\sqrt{N_cN_v}\,e^{-E_g/2k_BT}$。

数值：$m^*=m$、$T=300$ K 时

$$N_c = 2\left(\frac{9.11\times10^{-31}\times4.14\times10^{-21}}{2\pi\times(1.055\times10^{-34})^2}\right)^{3/2}\ \mathrm{m^{-3}} = 2.5\times10^{25}\ \mathrm{m^{-3}} = 2.5\times10^{19}\ \mathrm{cm^{-3}};$$

Si 取 $m_n^*=1.08m$：$N_c=2.5\times10^{19}\times1.08^{3/2}\approx2.8\times10^{19}$ cm$^{-3}$。又 $E_g/2k_BT=1.11/(2\times0.0259)\approx21.4$，$e^{-21.4}\approx5.1\times10^{-10}$，故

$$n_i = \sqrt{2.8\times10^{19}\times1.0\times10^{19}}\times5.1\times10^{-10} \approx 1.67\times10^{19}\times5.1\times10^{-10} \approx 9\times10^{9}\ \mathrm{cm^{-3}}\sim10^{10}\ \mathrm{cm^{-3}}.\qquad\blacksquare$$

</details>

**2.** 类氢施主的数值估算：用 Si 的参数（$\varepsilon_r=11.7$、$m_n^*\approx0.26m$）估算施主结合能 $E_d$ 与有效 Bohr 半径 $a^*$；说明为什么室温下施主基本全电离，以及为什么这个模型是自洽的（提示：把 $a^*$ 与晶格常数比较）；再对照实测值（P：45 meV）指出差异的来源。

<details markdown="1"><summary>点击显示答案</summary>

$$E_d = 13.6\ \mathrm{eV}\times\frac{0.26}{11.7^2} = 13.6\times\frac{0.26}{136.9}\ \mathrm{eV} = 13.6\times1.90\times10^{-3}\ \mathrm{eV}\approx26\ \mathrm{meV},$$

$$a^* = \frac{11.7}{0.26}\times0.529\ \text{Å} = 45\times0.529\ \text{Å}\approx23.8\ \text{Å}\approx2.4\ \mathrm{nm}.$$

**室温电离**：$E_d\approx26$ meV 与 $k_BT(300\ \mathrm K)=25.9$ meV 同级，热涨落足以把电子从施主上撕下来；更定量地说，自检问题 3 的判据给出半电离温度仅 $\sim90$ K，300 K 远在饱和区深处，电离率 $\approx100\%$。

**自洽性**：Si 的晶格常数 $a=0.543$ nm，$a^*/a\approx4.4$，束缚轨道内约含 $(2a^*/a)^3\sim340$ 个原胞、即 $\sim10^3$ 个 Si 原子——波函数在许多个原胞上平滑展开，把晶体当连续介质（宏观 $\varepsilon_r$、带边 $m_n^*$）的近似因此合法；若算出的 $a^*$ 只有格点间距量级，这套处理就自我推翻了（深能级正是如此，类氢模型对它们失效）。

**与实测的差**：P 45、As 54、Sb 43 meV，估算小了约一倍。来源有二：杂质所在原胞附近，势偏离裸的屏蔽库仑形式（中心元胞修正，与杂质种类有关——这正是三种施主数值互不相同的原因）；Si 导带底有效质量各向异性（$m_l=0.98m$、$m_t=0.19m$），标量平均只是粗近似。模型的价值在量级与材料系统学：GaAs（$m^*=0.067m$、$\varepsilon_r=12.9$）给出 $E_d\approx13.6\times0.067/12.9^2\approx6$ meV，与实测一致——它甚至太浅，GaAs 器件到低温就冻结。

</details>

**3.** n 型半导体的 $E_F(T)$ 与三个温区：从电中性条件出发，推导冻结区的弱电离公式 $n\approx\sqrt{N_cN_D/2}\,e^{-E_d/2k_BT}$ 与饱和区的 $E_F$ 位置；对 Si、$N_D=10^{16}$ cm$^{-3}$（取 $E_d=45$ meV），估算冻结转变温度与本征交叉温度，圈出器件工作窗口。

<details markdown="1"><summary>点击显示答案</summary>

n 型（$N_A=0$）电中性：$n=N_D^++p$，联立 $n=N_ce^{-(E_c-E_F)/k_BT}$、$N_D^+=N_D\big[1+2e^{(E_F-E_D)/k_BT}\big]^{-1}$、$p=n_i^2/n$。

**冻结区**（$n_i$ 可忽略，弱电离 $N_D^+\ll N_D$）：此时 $2e^{(E_F-E_D)/k_BT}\gg1$，故 $N_D^+\approx\frac{N_D}{2}e^{-(E_F-E_D)/k_BT}$；而 $n=N_ce^{-(E_c-E_F)/k_BT}=N_ce^{-E_d/k_BT}e^{(E_F-E_D)/k_BT}$（用了 $E_c-E_D=E_d$）。两式相等解出 $e^{(E_F-E_D)/k_BT}=\sqrt{N_D/(2N_c)}\,e^{E_d/2k_BT}$，回代：

$$n = \sqrt{\frac{N_cN_D}{2}}\,e^{-E_d/2k_BT},$$

Arrhenius 图上斜率为 $E_d/2k_B$。半电离点（$n=N_D/2$，等价于 $N_ce^{-E_d/k_BT}=N_D$）：$N_c(T)=2.8\times10^{19}(T/300)^{3/2}$ cm$^{-3}$，$E_d/k_B=522$ K，方程 $522/T=\ln\big[2800(T/300)^{3/2}\big]$ 迭代求解（$T=90$ K：左 $5.8$、右 $6.1$；$T=85$ K：左 $6.1$、右 $6.0$）得 $T\approx86$ K——**冻结转变约在 100 K 以下**。

**饱和区**：$N_D^+\approx N_D$、$n\approx N_D$，故

$$E_F = E_c - k_BT\ln\frac{N_c}{N_D}.$$

300 K：$N_c/N_D=2.8\times10^{19}/10^{16}=2800$，$E_c-E_F=25.9\times\ln2800\approx25.9\times7.94\approx0.21$ eV——离导带底约 8 个 $k_BT$，非简并近似仍成立。（掺到 $10^{19}$ cm$^{-3}$ 量级 $E_F$ 就顶进导带，进入简并半导体。）

**本征交叉**：保留 $p$ 的完整电中性 $n=N_D+n_i^2/n$ 是二次方程，解为

$$n = \frac{N_D+\sqrt{N_D^2+4n_i^2(T)}}{2}\;\longrightarrow\;\begin{cases}N_D, & n_i\ll N_D\ (\text{饱和区}),\\ n_i(T), & n_i\gg N_D\ (\text{本征区}).\end{cases}$$

交叉点 $n_i(T)=N_D$：$1.67\times10^{19}(T/300)^{3/2}e^{-6441/T}=10^{16}$（$E_g/2k_B=6441$ K），迭代（$T=750$ K 左端 $\approx7.4\times10^{15}$、$T=730$ K $\approx5.6\times10^{15}$）得 $T\approx740$ K $\approx470\ ^\circ$C。

**结论**：$N_D=10^{16}$ cm$^{-3}$ 的 Si，器件窗口约为 **100 K $\lesssim T\lesssim$ 750 K**；$E_F(T)$ 从 $T\to0$ 时的 $E_D$ 与 $E_c$ 之间出发，饱和区缓慢下沉（300 K 时在 $E_c$ 下 0.21 eV），高温奔向隙中央的 $E_i$。

</details>

**4.** 耗尽近似下解 Poisson 方程：从分段常数的电荷密度出发，推出电场分布、两侧电势降落、耗尽宽度 $W$ 与峰电场；对 Si、$N_A=N_D=10^{16}$ cm$^{-3}$ 给出 $V_{\rm bi}$、$W$、$\mathcal{E}_{\max}$ 的数值，并说明为什么重掺杂一侧的耗尽层更窄。

<details markdown="1"><summary>点击显示答案</summary>

取界面 $x=0$，电场 $\mathcal{E}=-d\phi/dx$，Poisson 方程（高斯制）写为 $d\mathcal{E}/dx=4\pi\rho/\varepsilon_r$。分段积分，用边界条件 $\mathcal{E}(-x_p)=\mathcal{E}(x_n)=0$（中性区无电场）：

$$\mathcal{E}(x) = -\frac{4\pi eN_A}{\varepsilon_r}(x+x_p)\quad(-x_p\lt x\lt0),\qquad \mathcal{E}(x) = -\frac{4\pi eN_D}{\varepsilon_r}(x_n-x)\quad(0\lt x\lt x_n).$$

$x=0$ 处电场连续 ⟺ $N_Ax_p=N_Dx_n$——这正是"耗尽层总电荷为零"（整体电中性）的要求。电势是分段抛物线，两侧降落

$$\Delta V_p = -\int_{-x_p}^{0}\mathcal{E}\,dx = \frac{2\pi eN_A}{\varepsilon_r}x_p^2,\qquad \Delta V_n = \frac{2\pi eN_D}{\varepsilon_r}x_n^2,\qquad \Delta V_n+\Delta V_p = V_{\rm bi}.$$

由电荷平衡与 $W=x_n+x_p$ 得 $x_n=\frac{N_A}{N_A+N_D}W$、$x_p=\frac{N_D}{N_A+N_D}W$，代入：

$$V_{\rm bi} = \frac{2\pi e}{\varepsilon_r}\cdot\frac{N_DN_A^2+N_AN_D^2}{(N_A+N_D)^2}W^2 = \frac{2\pi e}{\varepsilon_r}\cdot\frac{N_AN_D}{N_A+N_D}W^2 \;\Rightarrow\; W = \sqrt{\frac{\varepsilon_r}{2\pi e}\,\frac{N_A+N_D}{N_AN_D}\,V_{\rm bi}}.$$

峰电场在界面处：$\mathcal{E}_{\max}=\frac{4\pi eN_D}{\varepsilon_r}x_n=\frac{2V_{\rm bi}}{W}$（三角形面积 = 高 × 底 / 2 = 电势降落）。

**数值**（代入 SI 形式 $\frac{\varepsilon_r}{4\pi}\to\varepsilon_0\varepsilon_r$，数值与单位制无关）：$N_A=N_D=10^{16}$ cm$^{-3}=10^{22}$ m$^{-3}$，$V_{\rm bi}=0.0259\times\ln(10^{32}/10^{20})\approx0.72$ V，

$$W = \sqrt{\frac{2\times8.85\times10^{-12}\times11.7}{1.6\times10^{-19}}\times\frac{2}{10^{22}}\times0.72}\ \mathrm m = \sqrt{1.85\times10^{-13}}\ \mathrm m \approx 0.43\ \mu\mathrm m,$$

$$\mathcal{E}_{\max} = \frac{2\times0.72}{0.43\times10^{-6}} \approx 3.3\times10^6\ \mathrm{V/m} = 33\ \mathrm{kV/cm}.$$

**不对称性**：$x_n/x_p=N_A/N_D$——掺杂浓度反过来分配宽度。单边突变结（如 p$^+$n，$N_A\gg N_D$）的耗尽层几乎全长在轻掺杂一侧：重掺杂侧电荷密度大，薄薄一层就够提供匹配的面电荷。这就是"用重掺杂换窄层、由轻掺杂侧承受耐压"的设计空间。

</details>

**5.** Shockley 二极管方程：写出一维稳态少数载流子扩散方程并求解（边界：耗尽边界处满足结律、远处回到平衡值），推出 $I=I_s(e^{eV/k_BT}-1)$ 与 $I_s$ 的表达式；估算 Si 二极管（$N_A=N_D=10^{16}$ cm$^{-3}$、$D=10$ cm$^2$/s、$\tau=1\ \mu$s、面积 $A=1$ mm$^2$）的 $I_s$ 量级；并解释正、反偏置不对称的物理来源。

<details markdown="1"><summary>点击显示答案</summary>

**边界条件（结律）**：耗尽层内复合可忽略、两侧各自准平衡，跨越势垒的 Boltzmann 关系把两侧空穴浓度锁住：加偏压 $V$ 后势垒降为 $V_{\rm bi}-V$，故 $p_n(x_n)=p_{p0}e^{-e(V_{\rm bi}-V)/k_BT}$；零偏平衡时 $p_{n0}=p_{p0}e^{-eV_{\rm bi}/k_BT}$。两式相除：

$$p_n(x_n) = p_{n0}\,e^{eV/k_BT},\qquad p_{n0} = \frac{n_i^2}{N_D}.$$

**扩散方程**：n 区中性区内，空穴的稳态连续性方程为"扩散流的散度 = 复合率"：$\frac{dJ_p}{dx}=-e\,\frac{\delta p}{\tau_p}$（$\delta p=p-p_{n0}$，$\tau_p$ 为少子寿命），代入扩散流 $J_p=-eD_p\frac{dp}{dx}$：

$$D_p\frac{d^2\delta p}{dx^2} = \frac{\delta p}{\tau_p}.$$

边界 $\delta p(x_n)=p_{n0}\big(e^{eV/k_BT}-1\big)$、$\delta p(\infty)=0$，解为

$$\delta p(x) = p_{n0}\left(e^{eV/k_BT}-1\right)e^{-(x-x_n)/L_p},\qquad L_p=\sqrt{D_p\tau_p}.$$

**电流**：$J_p(x_n)=-eD_p\,\delta p'(x_n)=\frac{eD_pp_{n0}}{L_p}\big(e^{eV/k_BT}-1\big)$。空穴电流沿程因复合衰减，但总电流处处连续——衰减的部分恰好由 n 侧多子（电子）电流补上；因此总电流 = 两侧耗尽边界处少子扩散电流之和，电子注入 p 区的贡献镜像相同：

$$I = I_s\left(e^{eV/k_BT}-1\right),\qquad I_s = eA\left(\frac{D_pp_{n0}}{L_p}+\frac{D_nn_{p0}}{L_n}\right) = eA\,n_i^2\left(\frac{D_p}{L_pN_D}+\frac{D_n}{L_nN_A}\right),$$

其中 $n_{p0}=n_i^2/N_A$。$-1$ 项保证 $V=0$ 时 $I=0$——热力学一致性。

**数值**：$L_p=\sqrt{10\ \mathrm{cm^2/s}\times10^{-6}\ \mathrm s}=3.2\times10^{-3}$ cm（$32\ \mu$m）；$p_{n0}=n_{p0}=10^{20}/10^{16}=10^4$ cm$^{-3}$；两侧贡献相等：

$$J_s = 2\times\frac{1.6\times10^{-19}\times10\times10^4}{3.2\times10^{-3}} \approx 10^{-11}\ \mathrm{A/cm^2},\qquad I_s\sim10^{-13}\ \mathrm A\quad(A=1\ \mathrm{mm^2}=10^{-2}\ \mathrm{cm^2}).$$

正偏 0.7 V：$e^{0.7/0.0259}=e^{27}\approx5\times10^{11}$，$I\sim50\ \mu$A——正反向相差十一到十二个数量级。

**不对称的物理来源**：正偏降低势垒，放行的是**多子**（n 侧电子、p 侧空穴，浓度 $\sim N$）——供给无限，电流只受 Boltzmann 因子控制而指数爆炸；反偏升高势垒，收集的是**少子**（浓度被质量作用定律钉在 $n_i^2/N$ 的地板上）——抽走一个少一个，电流封顶在产生速率决定的 $I_s$。**不对称的根源是质量作用定律把少子浓度压到了地板上**，因此 $I_s\propto n_i^2$：Ge 的 $n_i$ 约 Si 的两千多倍，同结构 Ge 二极管的反向漏电同比例放大——Si 赢下半导体工业，材料的 $n_i$ 小是深层原因之一（另一个是 SiO$_2$ 的界面质量）。

</details>

## 参考

- Ashcroft & Mermin《Solid State Physics》第 28 章（Homogeneous Semiconductors：载流子统计、有效态密度、掺杂与温区）与第 29 章（Inhomogeneous Semiconductors：pn 结、耗尽层与整流）——本章主线参考。
- Kittel《固体物理导论》（第 8 版）第 8 章 "Semiconductor Crystals"：带隙数据表、直接与间接带隙、类氢杂质与载流子统计——配合主线查阅。
- Sze & Ng《Physics of Semiconductor Devices》（第 3 版）第 1 章（半导体物理基础：能带与载流子统计）与第 2 章（p–n Junction：耗尽近似、I–V 特性、击穿）——器件侧的权威展开，本章 §5 的完整版在此。
- 黄昆原著、韩汝琦改编《固体物理学》第 7 章（半导体电子论：杂质能级、载流子统计、非平衡载流子与 pn 结）——中文教材视角。
