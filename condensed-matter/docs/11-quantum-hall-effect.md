# 量子 Hall 效应：精确量子化与拓扑的登场

> 本书位置：凝聚态物理入门导论第 11 章（第三部分：现代专题）
> 前置知识：本科量子力学（谐振子、电磁场中的带电粒子）、Drude 输运图像（[第 3 章](03-free-electron-gas.md)）、谐振子的代数解法（[QFT 书：谐振子的产生/湮灭算符解法](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)）。
> 学习目标：完整推导 Landau 能级与简并度；理解整数 Hall 平台 $\sigma_{xy}=\nu e^2/h$ 为什么必须靠无序才能存在；复现 Laughlin 规范论证；从边缘态看到"体-边对应"的前奏，为第 12 章（拓扑物态）铺路。

凝聚态笔记约定：**保留 $\hbar$ 与 $k_B$**（不取自然单位），电子电荷写作 $-e$（$e>0$ 为元电荷）。磁场沿 $z$ 方向，电子气限制在 $xy$ 平面内。

---

## 1. 一句话总结

**强磁场把二维电子气的连续能谱压成等间距的 Landau 能级，每个能级每单位面积恰好容纳 $eB/h$ 个电子；当无序把费米面钉在"不导电的局域态"里时，Hall 电导被锁定在填充数 $\nu$ 所决定的 $\sigma_{xy}=\nu e^2/h$ 上——一个只含基本常数、精度达 $10^{-9}$、与材料和样品细节完全无关的量子化。这不是巧合而是拓扑：Laughlin 的规范论证和边缘态图像都指向同一个事实——这个整数 $\nu$ 是一个拓扑不变量（Chern 数），是凝聚态中第一个被认识的拓扑物态。**

下面把这句话一层一层算出来。

## 2. 经典 Hall 效应回顾

1879 年 Hall 发现：电流沿 $x$ 方向流过导体、磁场 $B$ 垂直于导体平面时，横向会出现电压。Drude 图像下这事一句话就能说完：电子在电磁场中满足

$$m\dot{\vec v} = -e\big(\vec E + \vec v\times\vec B\big) - \frac{m\vec v}{\tau},$$

末项是弛豫时间 $\tau$ 的散射阻尼。稳态（$\dot{\vec v}=0$）下解出电流 $\vec j=-ne\vec v$ 与电场的关系 $\vec j = \sigma\vec E$，其中电导率张量（$\omega_c\equiv eB/m$ 为回旋频率，$\sigma_0=ne^2\tau/m$ 为 Drude 电导率）

$$\sigma_{xx} = \frac{\sigma_0}{1+\omega_c^2\tau^2}, \qquad \sigma_{xy} = -\frac{\sigma_0\,\omega_c\tau}{1+\omega_c^2\tau^2}.$$

对我们最重要的不是全套公式，而是**强场极限** $\omega_c\tau\gg 1$（磁场强、散射弱）：

$$\sigma_{xy}\;\longrightarrow\;\frac{ne}{B}, \qquad \sigma_{xx}\;\longrightarrow\;0.$$

<details markdown="1"><summary>补充说明：电导率与电阻率的张量互逆</summary>

实验直接测量的是电阻率 $\rho=\sigma^{-1}$。二维下张量求逆给出

$$\rho_{xx} = \frac{\sigma_{xx}}{\sigma_{xx}^2+\sigma_{xy}^2}, \qquad \rho_{xy} = -\frac{\sigma_{xy}}{\sigma_{xx}^2+\sigma_{xy}^2}.$$

注意一个反直觉但重要的推论：**$\sigma_{xx}=0$ 与 $\rho_{xx}=0$ 同时成立**（只要 $\sigma_{xy}\neq 0$）。量子 Hall 平台上"纵向电阻为零"与"纵向电导为零"是同一件事的两种说法：样品内部既不耗散，也没有纵向响应。而且此时 $\rho_{xy}=-1/\sigma_{xy}$，两者互为负倒数，量子化在两种语言里同样精确。

</details>

经典图像因此预言：**Hall 电阻率 $\rho_{xy}=B/(ne)$ 随磁场线性增长**，斜率给出载流子浓度 $n$——这至今仍是实验室测掺杂浓度的标准手段。1980 年之前，没有人会怀疑这条直线会有什么花样。

## 3. 二维电子气与强磁场：Landau 能级

### 3.1 问题设定

把电子约束在二维平面内（实验上用 Si MOSFET 反型层或 GaAs/AlGaAs 异质结量子阱，低温下 $z$ 方向只有基态被占据，是真正严格的二维系统）。加垂直磁场 $\vec B = B\hat z$。单电子哈密顿量为

$$H = \frac{1}{2m}\big(\vec p + e\vec A\big)^2, \qquad \vec B = \nabla\times\vec A.$$

（电子电荷 $-e$，故最小耦合里是 $\vec p+e\vec A$。）先不计自旋、不计无序、不计相互作用——单粒子问题，可以严格解。

### 3.2 Landau 规范：变成谐振子

选 Landau 规范 $\vec A = (0, Bx, 0)$，它给出 $\nabla\times\vec A = B\hat z$，且保持 $y$ 方向平移不变性。哈密顿量

$$H = \frac{1}{2m}\Big[p_x^2 + \big(p_y + eBx\big)^2\Big].$$

$H$ 不显含 $y$，所以 $p_y$ 守恒，取 $p_y = \hbar k$。代入：

$$H = \frac{p_x^2}{2m} + \frac{(eB)^2}{2m}\big(x + k l_B^2\big)^2,$$

其中引入了**磁长度**

$$l_B \equiv \sqrt{\frac{\hbar}{eB}}.$$

这是关于 $x$ 的一维谐振子：频率 $\omega_c = eB/m$，中心位置 $x_0 = -k l_B^2$。不需要再解方程——谐振子的谱我们早就用升降算符解透了（见[QFT 书：谐振子的产生/湮灭算符解法](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)，本篇取 $p_y$ 为参数后数学上就是那一篇的整页内容）。能谱为

$$\boxed{E_n = \hbar\omega_c\Big(n+\frac12\Big), \qquad n = 0, 1, 2, \dots}$$

这就是 **Landau 能级**：连续的二维动能被磁场"量子化"成等间距梯子，间距 $\hbar\omega_c$。波函数是 $y$ 方向平面波 $e^{iky}$ 乘上以 $x_0$ 为中心的谐振子本征函数。

### 3.3 规范无关的推导：升降算符再来一遍

上面的结果与规范选择无关，值得用更漂亮的办法确认。定义动力学动量 $\vec\pi = \vec p + e\vec A$，计算对易子：

$$[\pi_x, \pi_y] = -i\hbar\,e\big(\partial_x A_y - \partial_y A_x\big) = -i\hbar e B.$$

（差一个常数因子，这就是一对正则共轭变量。）构造

$$a = \frac{l_B}{\sqrt2\,\hbar}\big(\pi_x - i\pi_y\big), \qquad a^\dagger = \frac{l_B}{\sqrt2\,\hbar}\big(\pi_x + i\pi_y\big),$$

则 $[a,a^\dagger]=1$，且

$$H = \frac{\pi_x^2+\pi_y^2}{2m} = \hbar\omega_c\Big(a^\dagger a + \frac12\Big).$$

谐振子谱立刻读出，一行微分方程都没解。这套"磁场中 $= $ 每对动力学动量贡献一个谐振子"的代数结构，与声子、与自由场量子化是完全相同的机器。

### 3.4 简并度：每个 Landau 能级能装多少电子

上面有个显眼的结论：能量 $E_n$ **不依赖 $k$**——每个 Landau 能级内有巨量的态挤在同一能量上。数一下简并度。把样品取为 $L_x\times L_y$ 的矩形，$y$ 方向周期性边界条件使 $k = 2\pi n_y/L_y$ 分立取值；同时振子中心 $x_0=-kl_B^2$ 必须落在样品内，$0\le x_0\le L_x$，即 $k$ 的取值范围宽度为 $L_x/l_B^2$。于是每个 Landau 能级的态数

$$N_\varphi = \frac{L_y}{2\pi}\cdot\frac{L_x}{l_B^2} = \frac{A}{2\pi l_B^2} = \frac{BA}{h/e} \equiv \frac{\Phi}{\Phi_0}.$$

结果极其干净：**每单位面积简并度 $= 1/(2\pi l_B^2) = eB/h$**，等于穿过样品的磁通 $\Phi=BA$ 除以**磁通量子**

$$\Phi_0 = \frac{h}{e} \approx 4.14\times 10^{-15}\ \mathrm{Wb}.$$

物理图像：每个磁通量子"认领"一个量子态。定义**填充因子**

$$\nu \equiv \frac{n}{eB/h} = \frac{nh}{eB},$$

即电子总数除以每个 Landau 能级的容量。$\nu=1$ 意味着最低 Landau 能级恰好填满。填充因子是本篇后半的主角：量子 Hall 平台的台阶高度、Laughlin 论证里的整数，全都是它。

## 4. 整数量子 Hall 效应：观测与震惊

1980 年 von Klitzing 在 Si MOSFET 上、随后 GaAs 异质结上更干净地看到：固定载流子浓度 $n$、扫磁场 $B$（或固定 $B$、调栅压扫 $n$），Hall 电阻率 $\rho_{xy}$ **不是**经典预言的直线 $B/ne$，而是出现一系列台阶：

$$\rho_{xy} = \frac{h}{\nu e^2}, \qquad \nu = 1, 2, 3, \dots,$$

在平台的磁场区间内 $\rho_{xy}$ 钉在该值上不动，同时纵向电阻 $\rho_{xx}$ 掉到零（仪器测不出非零值）。离开平台，$\rho_{xy}$ 才在相邻台阶之间过渡。

三个事实使这个效应不可能"平凡"：

1. **精度离谱**：平台的 $\rho_{xy}$ 值与 $h/e^2$ 的整数分之一相符到 $10^{-9}$ 量级。不同实验室、不同材料体系（Si 与 GaAs）、不同样品形状、不同杂质浓度，给出同样的数。正常输运系数对杂质和温度的修正都是百分之几起步，这里的"误差"比电阻标准本身的校准精度还低。
2. **与材料无关**：数值里不出现 $m^*$、不出现 $\tau$、不出现 $n$——只有 $h$、$e$ 和一个整数。微观细节全部消失。
3. **同时 $\rho_{xx}=0$**：宏观样品里电流无耗散地流，散射时间无穷大似的，可样品明明满是杂质。

一句朴素的话总结这种震惊：**一个有杂质、有相互作用、有边缘、有温度涨落的脏兮兮真实样品，凭什么给出一个宇宙常数的整数倍，精确到小数点后九位？** 物理学里这种"细节全部洗不掉、只剩整数"的行为，过去只在一个地方见过——拓扑。平台值是整数这件事的强烈暗示是：存在一个不能连续改变的拓扑不变量在背后撑腰（TKNN 1982 年确认了这一点，$\sigma_{xy}$ 正比于占据带的 Chern 数，第 12 章展开）。本章先用更物理的两条路线理解它：无序 + Laughlin 论证。

## 5. 无序的关键作用：没有杂质，就没有平台

### 5.1 反证：干净样品的 $\sigma_{xy}$ 没有平台

回到第 2 节的强场极限：干净系统（$\omega_c\tau\gg 1$）里 $\sigma_{xy}=ne/B$，代入填充因子 $\nu=nh/(eB)$，得

$$\sigma_{xy} = \frac{ne}{B} = \nu\,\frac{e^2}{h}.$$

注意这**就是**量子化公式——但 $\nu$ 在这里随 $n$ 或 $B$ **连续变化**，不是整数！干净样品给的是一条过原点的直线（经典结果），整数只在离散点上"碰巧"被穿过，根本没有平台。所以：**精确量子化的公式在干净极限下已隐含，但平台——量子化公式在一个参数区间上纹丝不动——是杂质创造的。** 这是一个深刻的反转：通常无序破坏量子干涉效应，这里无序恰恰是量子化可见的必要条件。

### 5.2 局域态与扩展态

无序势 $V(\vec r)$ 把每个 Landau 能级的 $\delta$ 函数态密度展宽成一个带。带里的态分成两类：

- **带尾的局域态**：无序势的涨落把电子束缚在势谷里，波函数指数衰减 $\psi\sim e^{-r/\xi}$（Anderson 局域化，二维电子在任意弱无序下都局域化，只是长度 $\xi$ 可能很长）。局域态钉在原地，**不承载直流电流**。
- **带心的扩展态**：能量靠近未微扰 Landau 能级中心的态延展到整个样品，是唯一能携带电流的态。理论（标度论证与数值）表明每个 Landau 能级中心附近只剩一个（或一小簇）扩展态能量。

于是 $\nu$ 变化时发生的故事是：

- 费米能级 $E_F$ 扫过带尾的**局域态**时：往系统里加电子，只是填满一个又一个"陷阱"，扩展态的占据不变，电流不变，$\sigma_{xy}$ 不变——**平台**。同时 $E_F$ 处没有扩展态可散射进，$\sigma_{xx}=0$，$\rho_{xx}=0$。
- $E_F$ 扫过带心**扩展态**时：导电的态的占据数改变，$\sigma_{xy}$ 跳到下一个整数值，$\rho_{xx}$ 出现尖峰。

平台的宽度因此直接度量局域态的比例：样品越脏，局域态越多，平台越宽（但太脏则平台全毁，$\rho_{xx}$ 不再归零）。化学势钉在局域态区间这件事，是平台对 $n$、$B$、温度（在 $k_BT\ll\hbar\omega_c$ 范围内）统统不敏感的微观原因。

## 6. Laughlin 规范论证：量子化 = 拓扑的整性

无序解释平台的存在，但没解释平台的值**为什么恰好是整数倍**、凭什么精确到 $10^{-9}$。Laughlin（1981）给出一个漂亮的思想实验，把 $\sigma_{xy}$ 的整性直接钉在规范不变性上。

### 6.1 几何设定：Corbino 环带

把二维样品弯成一个 annulus（环带）：内外两个圆周边缘。沿环带的圆周方向测电压（取代通常的 Hall 电压），沿径向有 Hall 电流流过。现在让穿过环带中心孔的磁通 $\Phi$ 缓慢变化——这个磁通**不穿过样品本身**（样品处磁场不变），只是穿过洞。

### 6.2 两步论证

**第一步：磁通变化驱动径向电流。** 由 Faraday 定律，沿圆周的感应电动势

$$\mathcal E = \oint \vec E\cdot d\vec l = -\frac{\partial\Phi}{\partial t}.$$

方位角方向的电场通过 Hall 响应驱动径向电流密度 $j_r = \sigma_{xy}E_\varphi$，总径向电流

$$I = \sigma_{xy}\oint E_\varphi\,dl = -\sigma_{xy}\frac{\partial\Phi}{\partial t}.$$

泵浦过程转移的总电荷

$$\Delta Q = \int I\,dt = -\sigma_{xy}\,\Delta\Phi.$$

**第二步：泵浦一个磁通量子，哈密顿量回到自身。** 关键事实：当 $\Delta\Phi = \Phi_0 = h/e$ 时，变化前后的哈密顿量由规范变换联系，物理上等价（Byers–Yang 定理：只穿过洞的磁通以 $\Phi_0$ 为周期，正如同样的理由使 Aharonov–Bohm 相位 $e^{-ie\Phi/\hbar}$ 以 $\Phi_0$ 为周期）。绝热演化把一个本征态映到另一个本征态；对于绝缘的体（$E_F$ 在迁移率隙里，正是平台情形），唯一的改变是**有整数 $n$ 个电子从一个边缘被搬到另一个边缘**（体的态都填满了，动不了，能动的只有边缘——下一节的主角）。

### 6.3 合并

$\Delta Q = ne$（整数个电子）代入第一步：

$$ne = \sigma_{xy}\cdot\frac{h}{e} \quad\Longrightarrow\quad \boxed{\sigma_{xy} = n\,\frac{e^2}{h}, \qquad n\in\mathbb Z.}$$

注意这个论证里出现了什么、没出现什么：用了规范不变性（$\Phi_0$ 周期性）、用了绝热定理、用了"体是绝缘的"——**没有**出现材料参数、样品尺寸、杂质分布。泵浦一个磁通量子后"态回到自身"迫使转移电荷是 $e$ 的整数倍，$\sigma_{xy}$ 于是只能是 $e^2/h$ 的整数倍。整数 $n$ 是不能在连续形变下改变的量——这就是"拓扑"二字在此处的具体含义：只要体的能隙不闭合，任何光滑扰动都不能改变泵浦的电荷数。（用 Berry 曲率语言严格化，$n$ 就是占据带的 Chern 数，即 TKNN 不变量——第 12 章的主题。）

## 7. 边缘态：边界上流动的单向通道

Laughlin 论证里"能动的只有边缘"不是修辞。把第 3 节的 Landau 能级问题放到有边界的样品上：边界附近约束势 $V_{\rm conf}(x)$ 把能级"弯起"，

$$E_n(k) \approx \hbar\omega_c\Big(n+\frac12\Big) + V_{\rm conf}\big(x_0(k)\big), \qquad x_0 = -kl_B^2.$$

体内部 $V_{\rm conf}\approx$ 常数，能级平坦（无色散，群速度为零——体里电子打圈不走）；边界附近势陡升，能级向上弯。每条被弯起的能级与费米能级相交于某个 $k$，交点处态沿 $y$（边缘方向）有群速度

$$v_y = \frac{1}{\hbar}\frac{\partial E_n}{\partial k} = \frac{1}{\hbar}\frac{\partial E_n}{\partial x_0}\frac{\partial x_0}{\partial k} = -\frac{l_B^2}{\hbar}\frac{\partial V_{\rm conf}}{\partial x_0} \neq 0.$$

于是每条 Landau 能级在每个边缘给出一条**一维导电通道**，且：

- **单向（手征）**：$v_y$ 的符号由 $\partial V/\partial x_0$ 与 $B$ 的方向唯一决定，样品两侧边缘上的传播方向相反。同一边缘上不存在反向通道。
- **无背散射**：要背散射，电子得从样品一侧边缘横跨整个（绝缘的）体跳到另一侧的反向通道——宽度宏观时概率指数压低。这解释了 $\rho_{xx}=0$：不是"没有杂质"，而是"杂质想散射也找不到去处"。
- **通道数 = $\nu$**：$\nu$ 条 Landau 能级在费米面下，就有 $\nu$ 条边缘通道。每条一维手征通道贡献电导 $e^2/h$（Landauer 公式，第 10 章），总 Hall 电导 $\nu e^2/h$。第 6 节泵浦的整数 $n$，就是边缘通道数。

这是一个普遍模式的第一个实例：**体的拓扑不变量（整数 $n$/Chern 数）$\Longleftrightarrow$ 边界上必然存在受保护的态（手征边缘通道）**。"体-边对应"（bulk–boundary correspondence）是全部拓扑物态的标志结构，第 12 章会把它做成一般理论。

## 8. 分数化：一句超出单粒子图像的话

1982 年 Störmer、Tsui 在更高迁移率的样品、更低温度、更强磁场下，在 $\nu=1/3$ 处也看到平台：$\sigma_{xy}=\tfrac{1}{3}e^2/h$。单粒子图像对此无能为力——$\nu<1$ 时最低 Landau 能级没填满，无相互作用电子有天文数字的简并基态可选，没有什么东西能钉住电导。Laughlin 给出答案：电子间 Coulomb 相互作用在 $\nu=1/3$ 处凝聚出一个**强关联量子液体**（Laughlin 波函数），它有能隙、不可压缩，其元激发是电荷 $e/3$ 的准粒子，交换两个准粒子给出的统计相位既不是玻色也不是费米（分数统计/任意子）。分数量子 Hall 态是"拓扑序"这一概念的诞生地：态的差别不在对称性，而在长程纠缠的模式。本章只立此存照——它超出（也颠覆了）单粒子能带图像，是强关联与拓扑合流的起点（详见第 13 章的引子与专题文献）。

## 9. 数值、应用与意义

- **电阻标准**：$\sigma_{xy}$ 的台阶值只含 $h$ 与 $e$。定义 von Klitzing 常数 $R_K = h/e^2 = 25812.807\ \Omega$。1990 年起 $R_K$ 成为全球电阻校准标准；2019 年 SI 改革后 $h$ 与 $e$ 取定义值，量子 Hall 效应从"测量标准"升格为**欧姆的定义实现**。计量学是被一个凝聚态实验接管的。
- **典型量级**：GaAs 二维电子气 $n\sim(1\!-\!4)\times10^{15}\ \mathrm{m^{-2}}$，$\nu=1$ 要求 $B=nh/e\sim 4\!-\!17\ \mathrm T$；$l_B\approx 25.7\ \mathrm{nm}/\sqrt{B[\mathrm T]}\sim 10\ \mathrm{nm}$；GaAs 中 $m^*=0.067m_e$，$B=10\ \mathrm T$ 时 $\hbar\omega_c\approx 17\ \mathrm{meV}\approx 200\ \mathrm K\,k_B$，看到漂亮平台仍需液氦乃至稀释制冷机温度与高迁移率样品。
- **历史地位**：量子 Hall 效应（1985 年 Nobel，von Klitzing；1998 年 Nobel，Laughlin、Störmer、Tsui）是第一次有人意识到"绝缘体也有不同的相，差别在拓扑而非对称性"。TKNN 不变量、Haldane 模型、拓扑绝缘体（第 12 章）整条线都从这里长出。它是 Landau 范式之外的第一块大陆。

## 10. 小结

| 概念 | 公式/结论 | 物理角色 |
| --- | --- | --- |
| Landau 能级 | $E_n=\hbar\omega_c(n+\tfrac12)$，$\omega_c=eB/m$ | 磁场把连续谱量子化成梯子 |
| 磁长度 | $l_B=\sqrt{\hbar/eB}$ | 问题的唯一长度尺度 |
| 每能级简并度 | $eB/h$ 每单位面积 $=\Phi/\Phi_0$ | 一个磁通量子认领一个态 |
| 填充因子 | $\nu=nh/(eB)$ | 平台台阶的标签 |
| 整数平台 | $\sigma_{xy}=\nu e^2/h$，$\rho_{xx}=0$，精度 $10^{-9}$ | 与材料无关 $\Rightarrow$ 拓扑 |
| 无序 | 局域态不导电、扩展态导电 | 平台存在的必要条件 |
| Laughlin 泵浦 | $\Delta\Phi=\Phi_0\Rightarrow\Delta Q=ne$ | 量子化 $\Leftrightarrow$ 整数性（规范+绝热） |
| 边缘态 | $\nu$ 条手征一维通道，无背散射 | 体-边对应的前奏 |
| 分数 Hall | $\nu=1/3$：$e/3$ 准粒子、分数统计 | 相互作用拓扑液体，超出单粒子图像 |

## 自检问题

**1.** 取 Landau 规范 $\vec A=(0,Bx,0)$，从 $H=(\vec p+e\vec A)^2/2m$ 出发完整推出 Landau 能级 $E_n=\hbar\omega_c(n+\tfrac12)$，并写出相应的本征态结构。

<details markdown="1"><summary>点击显示答案</summary>

代入规范：

$$H = \frac{1}{2m}\Big[p_x^2 + \big(p_y+eBx\big)^2\Big].$$

$H$ 不显含 $y$，$p_y$ 守恒，取分离变量 $\psi(x,y)=e^{iky}\varphi(x)$（$p_y\to\hbar k$），则 $\varphi$ 满足

$$\Big[\frac{p_x^2}{2m} + \frac{(eB)^2}{2m}\big(x+kl_B^2\big)^2\Big]\varphi = E\varphi, \qquad l_B^2=\frac{\hbar}{eB}.$$

这是中心在 $x_0=-kl_B^2$、频率 $\omega_c=eB/m$ 的一维谐振子方程。谐振子谱（代数推导见[QFT 书谐振子笔记](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)）给出

$$E_n=\hbar\omega_c\Big(n+\frac12\Big), \qquad n=0,1,2,\dots$$

本征态 $\psi_{n,k}(x,y)\propto e^{iky}\,\phi_n\big((x-x_0)/l_B\big)$，其中 $\phi_n$ 是第 $n$ 个谐振子本征函数（Hermite 多项式乘高斯）。能量不依赖 $k$：每个能级宏观简并，简并度见第 2 题。

</details>

**2.** 证明每个 Landau 能级每单位面积的简并度为 $eB/h$，即穿过样品每 $\Phi_0=h/e$ 的磁通对应一个态。

<details markdown="1"><summary>点击显示答案</summary>

取 $L_x\times L_y$ 样品，$y$ 方向周期边界：$k=2\pi n_y/L_y$，相邻 $k$ 间隔 $\Delta k = 2\pi/L_y$。振子中心 $x_0=-kl_B^2$ 必须落在样品内，$0\le x_0\le L_x$，即 $k$ 落在宽度为

$$|k|_{\max} = \frac{L_x}{l_B^2}$$

的区间内。允许的 $k$ 值总数

$$N_\varphi = \frac{L_x/l_B^2}{2\pi/L_y} = \frac{L_xL_y}{2\pi l_B^2}.$$

每单位面积

$$\frac{N_\varphi}{A} = \frac{1}{2\pi l_B^2} = \frac{eB}{2\pi\hbar} = \frac{eB}{h}.$$

改写成磁通语言：总磁通 $\Phi=BA$，$N_\varphi = BA/(h/e) = \Phi/\Phi_0$。每个磁通量子对应一个态。计入自旋（强场下已劈裂，每条 Landau 能级单自旋）恰好如此；若忽略 Zeeman 劈裂则再乘 2。

</details>

**3.** 用反证法说明：为什么完全无杂质的理想样品不可能出现 Hall 平台？

<details markdown="1"><summary>点击显示答案</summary>

设样品无杂质。散射消失（$\tau\to\infty$），Drude 结果（或等价的干净极限输运计算）在 $\omega_c\tau\gg 1$ 下给出

$$\sigma_{xy} = \frac{ne}{B} = \nu\,\frac{e^2}{h}, \qquad \nu = \frac{nh}{eB}.$$

固定 $n$ 扫 $B$（或固定 $B$ 扫 $n$），$\nu$ **连续变化**，$\sigma_{xy}$ 是一条过原点的光滑曲线，只在 $\nu$ 恰好穿过整数的孤立点上取到 $e^2/h$ 的整数倍。任何声称"出现平台"的说法都要求 $\sigma_{xy}$ 在 $\nu$ 的一个有限区间上不变，即 $\partial\sigma_{xy}/\partial\nu=0$，与上式 $\partial\sigma_{xy}/\partial\nu = e^2/h\neq 0$ 矛盾。

所以干净样品里量子化公式虽对，但平台不存在。**平台的物理机制是**：无序把 Landau 能级展宽，带尾态局域化不载流；$E_F$ 扫过局域态区间时，扩展态占据数不变，$\sigma_{xy}$ 钉死在最近的整数值上。局域态的"蓄水池"效应把连续的 $\nu$ 吸收掉，只留下整数台阶。无杂质则无局域态，无蓄水池，无平台。

</details>

**4.** 复现 Laughlin 泵浦论证：在 Corbino 环带中把穿过中心孔的磁通绝热地增加一个磁通量子 $\Phi_0=h/e$，证明 Hall 电导必为 $\sigma_{xy}=ne^2/h$（$n$ 为整数）。

<details markdown="1"><summary>点击显示答案</summary>

设环带圆周方向的感应电场为 $\vec E$。Faraday 定律给出电动势

$$\oint\vec E\cdot d\vec l = -\frac{\partial\Phi}{\partial t}.$$

Hall 响应把这个圆周电场转成径向电流：$\vec j$ 与 $\vec E$ 垂直，$j_r=\sigma_{xy}E_\varphi$，对整个圆周积分得总径向电流

$$I = \sigma_{xy}\oint E_\varphi\,dl = -\sigma_{xy}\frac{\partial\Phi}{\partial t} \quad\Longrightarrow\quad \Delta Q = \int I\,dt = -\sigma_{xy}\,\Delta\Phi.$$

现在取 $\Delta\Phi=\Phi_0=h/e$。只穿过洞的磁通对样品电子的唯一作用是 Aharonov–Bohm 相位 $e^{-ie\Phi/\hbar}$；当 $\Phi$ 改变 $\Phi_0$ 时，相位改变 $2\pi$ 的整数倍，变化前后的哈密顿量差一个规范变换，**物理上完全等价**（Byers–Yang）。因此绝热泵浦一个 $\Phi_0$ 后，系统必须落在一个与初态能量相同（体有能隙时就是基态）或仅差"整数个电子在两边缘间转移"的态上：体是绝缘的，体态不可动，唯一允许的变化是整数 $n$ 个电子从内缘搬到外缘，即

$$|\Delta Q| = ne, \qquad n\in\mathbb Z.$$

两式合并：

$$ne = \sigma_{xy}\cdot\frac{h}{e} \quad\Longrightarrow\quad \sigma_{xy} = n\,\frac{e^2}{h}.$$

要点：结论只用规范不变性、绝热定理与体能隙，不含任何微观参数——$n$ 在能隙不闭合的任何连续形变下不变，这正是拓扑量子化的含义。

</details>

**5.** 估算 GaAs 二维电子气中 $\nu=1$ 平台中心对应的磁场量级与磁长度；并说明为什么需要低温与高迁移率。

<details markdown="1"><summary>点击显示答案</summary>

由填充因子定义 $\nu=nh/(eB)$，$\nu=1$ 时

$$B = \frac{nh}{e}.$$

取典型密度 $n=2\times10^{15}\ \mathrm{m^{-2}}$（$2\times10^{11}\ \mathrm{cm^{-2}}$）：

$$B = \frac{(2\times10^{15})\,(6.63\times10^{-34})}{1.60\times10^{-19}} \approx 8.3\ \mathrm T.$$

一般规律 $B[\mathrm T] \approx 4.14\,n[10^{15}\,\mathrm{m^{-2}}]/\nu$：几个到十几个特斯拉，超导磁体量级。

磁长度

$$l_B = \sqrt{\frac{\hbar}{eB}} = \frac{25.7\ \mathrm{nm}}{\sqrt{B[\mathrm T]}} \approx \frac{25.7}{\sqrt{8.3}}\ \mathrm{nm} \approx 9\ \mathrm{nm}.$$

**为什么低温**：平台要求热涨落不能把电子激发过 Landau 能级间隙，$k_BT\ll\hbar\omega_c$。GaAs 中 $m^*=0.067m_e$，$B=8.3\ \mathrm T$ 时

$$\hbar\omega_c = \frac{\hbar eB}{m^*} \approx 14\ \mathrm{meV}\ \Longleftrightarrow\ \frac{\hbar\omega_c}{k_B}\approx 170\ \mathrm K,$$

原则温度需远低于此（实际平台质量随温度持续改善到 $\sim 1\ \mathrm K$ 以下，且杂质辅助的跳跃输运在毫开尔文下才完全冻掉）。

**为什么高迁移率**：一方面 $\omega_c\tau\gg1$ 才有清晰的能级分立与 $\rho_{xx}=0$；另一方面迁移率高意味着无序弱而长程，局域态比例适中，平台宽而平。迁移率太低则 Landau 能级被无序彻底抹平，$\hbar\omega_c$ 小于能级展宽，什么平台都看不到。

</details>

## 参考

- Ashcroft & Mermin《固体物理》第 12、14 章——半经典输运与磁场中电子（Landau 能级的准经典背景）。
- Kittel《固体物理导论》第 6 章——自由电子气与经典 Hall 效应（第 2 节的背景）。
- D. Tong, *Lectures on the Quantum Hall Effect*（在线讲义）第 1–2 章——Landau 能级、整数效应与 Laughlin 论证，与本篇对应最直接。
- R. E. Prange & S. M. Girvin (eds.), *The Quantum Hall Effect*——经典专题文集，含原始文献重印。
- B. A. Bernevig & T. L. Hughes, *Topological Insulators and Topological Superconductors* 第 2–3 章——Chern 数与边缘态，直通本书第 12 章。
- D. Yoshioka, *The Quantum Hall Effect*（Springer）——分数效应与 Laughlin 态的系统教材。
