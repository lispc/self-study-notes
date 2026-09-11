# 线性响应与 Kubo 公式：理论与实验之间的桥

> 路线图位置：量子力学书 · 第四部分（多体语言）· 第 10 篇。本篇是"理论计算"与"实验测量"之间的通用接口，也是凝聚态书多章的直接前置：[凝聚态书第 6 章 相互作用电子气](../../condensed-matter/docs/06-interacting-electron-gas.md)（屏蔽与 RPA）、凝聚态书第 10 章（量子输运，待写）、[第 11 章 量子 Hall 效应](../../condensed-matter/docs/11-quantum-hall-effect.md)与[第 12 章 拓扑物态](../../condensed-matter/docs/12-topological-phases.md)（电导的 Kubo 表达式是 TKNN 的入口）、[第 19 章 激发态方法](../../condensed-matter/docs/19-excited-states.md)（响应函数的极点 = 激发能）。
> 前置知识：[第 09 篇 二次量子化](09-second-quantization.md)（产生湮灭算符与多体算符的语言）；含时微扰论（[第 07 篇 微扰论](07-perturbation-theory.md)，尤其是费米黄金定则）。不需要先修统计力学：密度矩阵与系综的概念在第 3 节自备。
> 学习目标：说清为什么凝聚态实验测的都是响应函数；掌握密度矩阵与热平均的最小工具箱；完整推导 Kubo 公式（迟滞响应函数 = 平衡态对易子关联函数）；理解因果性如何推出 Kramers–Kronig 关系与谱（Lehmann）表示、虚部为何是耗散；掌握涨落–耗散定理及其经典极限；在四个例子（Drude 电导、自旋磁化率、介电函数与 Thomas–Fermi 屏蔽、中子散射与动态结构因子）中认出同一台机器。

---

**单位约定**：本章取自然单位 $\hbar = 1$（首次出现特此说明），并记 $\beta \equiv 1/(k_BT)$、保留 $k_B$ 显式；讨论经典极限与数值估算时恢复 $\hbar$。库仑势沿用第 6 章的高斯制记号 $v(q) = 4\pi e^2/q^2$。

## 1. 一句话总结

**对一个热平衡体系轻轻"踢一脚"（弱外场），它"怎么晃"（观测量的线性改变）完全由未受扰体系的平衡态涨落决定——这就是 Kubo 公式：响应函数 $\chi^R_{AB}(t) = -i\theta(t)\langle[A(t),B(0)]\rangle_0$。因果性把响应的实部与虚部锁死（Kramers–Kronig 关系），虚部度量体系从外场吸收的能量（耗散）；而耗散与平衡涨落被涨落–耗散定理绑成同一枚硬币的两面。电导率、磁化率、介电函数、动态结构因子——凝聚态实验测量的几乎全部对象——都是这一台机器的不同读数。**

## 2. 实验测的都是响应函数

凝聚态实验从不直接测量波函数或能级——测量方案的逻辑永远是"踢一下，看怎么晃"：

- 输运实验：加电场 $\vec E(t)$，测电流 $\vec j$；
- 磁测量：加磁场 $h(t)$，测磁化 $M$（NMR 里看自旋对射频场的吸收）；
- 光学与介电测量：加电磁场，测极化与吸收；
- 散射实验（中子、X 射线、电子能量损失谱）：入射粒子充当探针，与体系的密度或自旋耦合，测微分散射截面。

弱场极限下，观测量的改变 $\delta\langle A\rangle$ 与外场 $F$ 成线性关系，比例系数就是响应函数：

$$\delta\langle A\rangle(\omega) = \chi_{AB}(\omega)\,F(\omega).$$

观测量与响应的对应表：

| 实验 | "踢法"（外场耦合） | 观测量 | 对应的响应函数 |
|---|---|---|---|
| 直流/交流输运 | 电场 $\vec E$ 耦合电子位置/电流 | 电流密度 $\vec j$ | 电导率 $\sigma(\omega)$（电流–电流响应） |
| 磁化测量、NMR | 磁场 $h$ 耦合磁化 $M_z$ | 磁化强度、吸收功率 | 自旋磁化率 $\chi_s(q,\omega)$ |
| 光吸收、介电测量 | 标量势 $\varphi_{\mathrm{ext}}$ 耦合电荷密度 | 感应电荷、吸收系数 | 介电函数 $\varepsilon(q,\omega)$（密度–密度响应） |
| 中子散射 | 核势/磁偶极耦合密度与自旋 | 微分散射截面 | 动态结构因子 $S(q,\omega)$ |
| ARPES | 光子把电子逐出固体 | 光电子能量–动量谱 | 单粒子谱函数 $A(\vec k,\omega)$（单粒子格林函数，见第 17 章） |

本章任务就是给这张表建立严格的理论基础：$\chi$ 是什么、怎么算、有哪些不依赖具体模型的普遍性质。

## 3. 最小工具箱：密度矩阵与热平均

本节自备"密度矩阵与量子统计"的入门，不需要先修统计力学。

有限温度下体系不处于某个确定的量子态，而是以概率 $p_n$ 处于能量本征态 $\lvert n\rangle$。这种"经典概率 + 量子叠加"混杂的情形由**密度矩阵**描述：

$$\rho = \sum_n p_n\,\lvert n\rangle\langle n\rvert, \qquad \mathrm{Tr}\,\rho = 1.$$

任意算符的期望值是"量子平均之外再套经典平均"：

$$\langle A\rangle = \sum_n p_n\,\langle n\rvert A\lvert n\rangle = \mathrm{Tr}(\rho A).$$

热平衡（温度 $T$）下的正则系综取 Boltzmann 权重 $p_n = e^{-\beta E_n}/Z$，即

$$\rho_0 = \frac{e^{-\beta H_0}}{Z}, \qquad Z = \mathrm{Tr}\,e^{-\beta H_0}.$$

零温极限 $\beta\to\infty$ 只保留基态，$\rho_0\to\lvert0\rangle\langle0\rvert$，本章一切公式退化为基态期待值的形式。

密度矩阵的演化由 von Neumann 方程 $i\partial_t\rho = [H,\rho]$ 给出（薛定谔方程的直接推论；注意它与 Heisenberg 算符方程 $i\partial_t A = -[H,A]$ 差一个符号）。平衡态 $\rho_0$ 与 $H_0$ 对易，因而是定态——这正是下节微扰展开的支点。

## 4. Kubo 公式的推导

### 4.1 设置：弱外场耦合

把哈密顿量分成平衡部分与含时微扰：

$$H(t) = H_0 + H'(t), \qquad H'(t) = B\,F(t),$$

其中 $F(t)$ 是经典外场（广义力），$B$ 是与它耦合的算符。例：电场中的电子 $H' = e\vec E\cdot\sum_i\vec r_i$；塞曼耦合 $H' = -\vec M\cdot\vec h$（负号只是 $F$ 的重新定义）。设 $t\to-\infty$ 时 $F\to0$（操作上乘绝热开关因子 $e^{\eta t}$、最后取 $\eta\to0^+$），体系彼时处于热平衡 $\rho_0$。

### 4.2 相互作用绘景下的一阶展开

对 $H_0$ 取相互作用绘景：算符 $O_I(t) = e^{iH_0 t}Oe^{-iH_0 t}$，密度矩阵 $\rho_I(t) = e^{iH_0 t}\rho(t)e^{-iH_0 t}$ 满足

$$i\partial_t\rho_I = [H'_I(t),\,\rho_I(t)], \qquad \rho_I(-\infty) = \rho_0,$$

（$[\rho_0,H_0]=0$ 保证 $\rho_0$ 不随 $H_0$ 演化）。迭代到 $H'$ 的一阶：

$$\rho_I(t) = \rho_0 - i\int_{-\infty}^{t}dt'\,[H'_I(t'),\rho_0] + O(H'^2).$$

观测量 $A$ 的期望值 $\langle A\rangle(t) = \mathrm{Tr}[\rho_I(t)A_I(t)]$ 相对平衡值的改变为

$$\delta\langle A\rangle(t) \equiv \langle A\rangle(t) - \langle A\rangle_0 = -i\int_{-\infty}^{t}dt'\,\mathrm{Tr}\big\{[H'_I(t'),\rho_0]\,A_I(t)\big\}.$$

用迹的循环性 $\mathrm{Tr}\{[X,\rho]Y\} = \mathrm{Tr}\{\rho[Y,X]\}$（两边直接展开即见相等），再代入 $H'_I = B_I F$：

$$\delta\langle A\rangle(t) = -i\int_{-\infty}^{t}dt'\,\big\langle[A_I(t),B_I(t')]\big\rangle_0\,F(t').$$

把它写成线性响应的标准形 $\delta\langle A\rangle(t) = \int_{-\infty}^{\infty}dt'\,\chi^R_{AB}(t-t')F(t')$，读出 **Kubo 公式**（迟滞响应函数）：

$$\boxed{\;\chi^R_{AB}(t-t') = -i\,\theta(t-t')\,\big\langle[A(t),B(t')]\big\rangle_0\;}$$

此后省略下标 $I$：式中算符均按未微扰的 $H_0$ 做 Heisenberg 演化，期待值 $\langle\cdots\rangle_0$ 对未微扰平衡系综取。三点注记：

- **全部信息在平衡涨落里**：右边只含未受扰体系的关联函数——线性响应不需要知道微扰后的新定态，只需要知道平衡态怎样"自发地晃"。
- $\theta(t-t')$ 是**因果性**：结果不能先于原因。它是第 5 节一切解析性质的根源。
- 符号约定：本笔记把耦合写成 $H' = +BF$，与 Mahan、Bruus & Flensberg 一致；若写成 $H' = -BF$（Landau–Lifshitz 等书的约定），Kubo 公式整体变号为 $\chi = +i\theta\langle[A,B]\rangle$。两种约定物理内容相同，下文固定用前者。

### 4.3 频率空间

对单色场 $F(t) = F_\omega e^{-i\omega t}e^{\eta t}$（含绝热开关），响应以同频率振荡：$\delta\langle A\rangle(t) = \chi^R_{AB}(\omega)F(t)$，其中

$$\chi^R_{AB}(\omega) = \int_{-\infty}^{\infty}dt\,e^{i\omega t}e^{-\eta t}\,\chi^R_{AB}(t) = \int_0^{\infty}dt\,e^{i\omega t}\chi^R_{AB}(t).$$

最后一个等号用了因果性。从此"响应"是频率的复函数：实部与虚部各有物理，且彼此锁死——下一节的主题。

## 5. 解析性质：因果性的数学后果

### 5.1 Kramers–Kronig 关系

由于 $t<0$ 时 $\chi^R(t) = 0$，傅里叶积分在 $\mathrm{Im}\,\omega > 0$ 时随 $t\to+\infty$ 指数收敛：**$\chi^R(\omega)$ 在上半复平面解析**——这就是因果性的复分析表述。再设 $|\omega|\to\infty$ 时 $\chi^R(\omega)\to0$（物理响应总如此，高频外场体系跟不上），对 $\chi^R(z)/(z-\omega)$ 沿上半平面大半圆做围道积分（推导见自检问题 2），得 **Kramers–Kronig 关系**：

$$\mathrm{Re}\,\chi^R(\omega) = \frac{1}{\pi}\,\mathrm{P}\!\int_{-\infty}^{\infty}d\omega'\,\frac{\mathrm{Im}\,\chi^R(\omega')}{\omega'-\omega}, \qquad \mathrm{Im}\,\chi^R(\omega) = -\frac{1}{\pi}\,\mathrm{P}\!\int_{-\infty}^{\infty}d\omega'\,\frac{\mathrm{Re}\,\chi^R(\omega')}{\omega'-\omega}.$$

**色散（实部）与吸收（虚部）不是两次独立的实验：测出一条就能算出另一条。** 这也是理论计算与实验数据的免费体检器。

### 5.2 谱（Lehmann）表示

在 $\langle[A(t),B(0)]\rangle_0$ 中插入能量本征态完备集 $\sum_n\lvert n\rangle\langle n\rvert$，逐项做傅里叶变换（含 $i\eta$），得

$$\chi^R_{AB}(\omega) = \frac{1}{Z}\sum_{m,n}\frac{\big(e^{-\beta E_m}-e^{-\beta E_n}\big)\,A_{mn}B_{nm}}{\omega + E_m - E_n + i\eta}, \qquad A_{mn} \equiv \langle m\rvert A\lvert n\rangle.$$

响应函数是 $\omega$ 的有理函数，**极点在激发能 $\omega = E_n - E_m$ 处**（实轴下方无穷小）。这就是"算响应 = 算激发谱"的严格版，也是[第 19 章](../../condensed-matter/docs/19-excited-states.md)激发态方法的统一出发点：那里用 TDHF/RPA、EOM-CC、TD-DFT、BSE 算的都是这个对象在不同近似下的极点。

取虚部（用 $1/(x+i\eta) = \mathrm{P}(1/x) - i\pi\delta(x)$）：

$$\mathrm{Im}\,\chi^R_{AB}(\omega) = -\frac{\pi}{Z}\sum_{m,n}\big(e^{-\beta E_m}-e^{-\beta E_n}\big)\,A_{mn}B_{nm}\,\delta(\omega + E_m - E_n).$$

对厄米算符 $B = A$（实外场的情形）：$A_{mn}B_{nm} = \lvert A_{mn}\rvert^2 \ge 0$。$\omega > 0$ 时 $\delta$ 函数强制 $E_n = E_m + \omega > E_m$，因子 $e^{-\beta E_m}-e^{-\beta E_n} > 0$，故 $\mathrm{Im}\,\chi^R(\omega) < 0$（$\omega>0$）；由同样结构可见 $\mathrm{Im}\,\chi^R$ 是 $\omega$ 的奇函数，$\mathrm{Re}\,\chi^R$ 是偶函数。定义非负的**吸收谱**

$$\chi''(\omega) \equiv -\mathrm{Im}\,\chi^R(\omega) = \frac{\pi}{Z}\sum_{m,n}\big(e^{-\beta E_m}-e^{-\beta E_n}\big)\,\lvert A_{mn}\rvert^2\,\delta(\omega + E_m - E_n)\ \ge\ 0 \quad (\omega>0).$$

### 5.3 χ'' 度量耗散

含时哈密顿量 $H(t) = H_0 + BF(t)$ 的能量变化率为 $\dot E = \langle\partial H/\partial t\rangle = \langle B\rangle\dot F(t)$。对单色场 $F(t) = F_0\cos\omega t$ 做周期平均（完整推导、以及与费米黄金定则的逐项对照，见自检问题 5）：

$$\overline{P} = \frac{\omega}{2}\,\chi''(\omega)\,F_0^2\ \ge\ 0.$$

**外场对体系做的净功（= 体系吸收的能量）正比于响应函数的虚部。** 实部给出跟得上外场的弹性（色散）响应，不耗散能量。这就是"$\chi''$ 是耗散/吸收的度量"的精确含义。

## 6. 涨落–耗散定理

定义平衡涨落的谱（动态关联函数）：

$$S_{AB}(\omega) = \int_{-\infty}^{\infty}dt\,e^{i\omega t}\langle A(t)B(0)\rangle_0 = \frac{2\pi}{Z}\sum_{m,n}e^{-\beta E_m}\,A_{mn}B_{nm}\,\delta(\omega + E_m - E_n).$$

与 $\chi''$ 的 Lehmann 和逐项比对：差别只在热因子——$\chi''$ 里是 $(e^{-\beta E_m}-e^{-\beta E_n})$，$S$ 里是 $e^{-\beta E_m}$。在 $\delta$ 函数的约束 $E_n - E_m = \omega$ 下，$e^{-\beta E_m}-e^{-\beta E_n} = e^{-\beta E_m}(1-e^{-\beta\omega})$，于是（$A = B$ 厄米）得**涨落–耗散定理**的量子形式：

$$\boxed{\;S(\omega) = \frac{2\,\chi''(\omega)}{1-e^{-\beta\omega}}\;}\qquad\Longleftrightarrow\qquad \chi''(\omega) = \frac12\big(1-e^{-\beta\omega}\big)\,S(\omega).$$

对称化涨落谱 $\bar S(\omega) = \tfrac12\int dt\,e^{i\omega t}\langle\{A(t),A(0)\}\rangle$ 的版本是 $\bar S(\omega) = \coth(\beta\omega/2)\,\chi''(\omega)$。

**经典极限**：恢复 $\hbar$ 后，$\chi^R$ 本身携带一个 $\hbar$（对易子是 $O(\hbar)$ 的量），定义经典响应 $\chi_{\mathrm{cl}} \equiv \chi^R/\hbar$；条件 $\hbar\omega \ll k_BT$ 下 $1-e^{-\beta\hbar\omega} \approx \beta\hbar\omega$，于是

$$S(\omega) = \frac{2k_BT}{\omega}\,\chi''_{\mathrm{cl}}(\omega).$$

——涨落谱正比于"温度 × 单位频率的耗散"。Johnson–Nyquist 噪声（电阻两端的热噪声电压谱正比于 $k_BT$ 乘电阻）是它的日常化身：**有耗散必有涨落，有涨落必有耗散**。物理图像：耗散是体系对外场不可逆的吸收，涨落是同一体系在平衡态的自发晃动；Kubo 公式早已宣布二者由同一个关联函数描述，FDT 只是把这句话翻译成谱语言。

## 7. 四个例子

### 7.1 直流电导与 Drude 形式

取电场沿 $x$，$H' = eE\hat X$（$\hat X = \sum_i x_i$，电子电荷 $-e$），电流算符 $\hat j = -e\dot{\hat X}$（取单位体积）。Kubo 公式给出电导率

$$\sigma(\omega) = \frac{i}{\omega+i\eta}\left[\frac{ne^2}{m} + \chi^R_{jj}(\omega)\right],$$

括号里 $ne^2/m$ 是抗磁（质量）项，$\chi^R_{jj}$ 是电流–电流迟滞响应。实部 $\mathrm{Re}\,\sigma(\omega) = \chi''_{jj}(\omega)/\omega \ge 0$——焦耳热 $\overline{P} = \tfrac12\mathrm{Re}\,\sigma\,E_0^2$ 非负，与 5.3 节一致。严格无散射的电子气有 $\chi^R_{jj}(0) = -ne^2/m$（f 求和规则的推论），$\sigma$ 退化为 $\omega=0$ 处的 $\delta$ 峰——没有散射就没有电阻；杂质与声子把电流关联函数的衰减时间 $\tau$ 引进来，$\delta$ 峰展宽为洛伦兹型，即 **Drude 形式**

$$\sigma(\omega) = \frac{ne^2}{m}\,\frac{1}{\tau^{-1}-i\omega}, \qquad \sigma_{dc} = \frac{ne^2\tau}{m}, \qquad \mathrm{Re}\,\sigma(\omega) = \frac{ne^2}{m}\,\frac{\tau}{1+\omega^2\tau^2}.$$

第 3 章的 Drude 唯象公式从此有了微观出处：一切归结为算一个平衡态电流关联函数。第 10 章的 Landauer 图景与第 11 章的 Hall 电导都是这台机器的读数。

### 7.2 自旋磁化率

磁场 $h$ 沿 $z$：$H' = -M_z h$。磁化率 $\chi(\omega)$ 由 $\delta\langle M_z\rangle = \chi(\omega)\,h$ 定义。静态均匀极限化为**涨落公式**

$$\chi(0,0) = \frac{\partial\langle M_z\rangle}{\partial h} = \beta\big(\langle M_z^2\rangle - \langle M_z\rangle^2\big)\ \ge\ 0,$$

（对 $\ln Z$ 求两次导即得；$[M_z, H_0]=0$ 时严格成立）。磁化率非负 = 平衡涨落非负——热力学稳定性的微观面孔。$N$ 个自由自旋 $1/2$ 给出 Curie 定律 $\chi = N(g\mu_B)^2/(4k_BT)$（计算见自检问题 4）。动力学磁化率的吸收谱 $\chi''(q,\omega)$ 的峰给出磁激发（自旋波、顺磁振子）的色散与寿命，是中子磁散射的直接测量对象（→ 第 7 章磁性）。

### 7.3 密度响应、介电函数与 Thomas–Fermi 屏蔽

外标量势耦合电子密度：$H' = -e\int d^3r\,\varphi_{\mathrm{ext}}(\vec r)\,n(\vec r)$。密度–密度响应 $\chi^R_{nn}(q,\omega)$ 决定介电函数：

$$\varepsilon^{-1}(q,\omega) = 1 + v(q)\,\chi^R_{nn}(q,\omega), \qquad v(q) = \frac{4\pi e^2}{q^2},$$

RPA 层级（只保留电子气对总势的独立响应）$\chi = \chi_0/(1-v\chi_0)$，即 $\varepsilon_{\mathrm{RPA}} = 1 - v(q)\chi_0$。静态长波极限由**压缩率求和规则** $\chi_0(q\to0,0) = -\partial n/\partial\mu = -N(E_F)$ 给出

$$\varepsilon(q,0) = 1 + \frac{k_{TF}^2}{q^2}, \qquad k_{TF}^2 = 4\pi e^2 N(E_F),$$

屏蔽势 $v/\varepsilon = 4\pi e^2/(q^2+k_{TF}^2)$——正是[第 6 章](../../condensed-matter/docs/06-interacting-electron-gas.md) §4 的 Thomas–Fermi 屏蔽（Yukawa 势）。换句话说：**Thomas–Fermi 理论 = 密度线性响应的静态长波极限**；而第 6 章 §6 的等离激元是同一响应函数在 $\varepsilon(q,\omega)=0$ 处的动力学极点。静态与动力学、屏蔽与集体振荡，统一在 $\chi^R_{nn}(q,\omega)$ 一个对象里。

### 7.4 动态结构因子与中子散射

中子经核力与体系密度耦合，微分散射截面（van Hove 公式）正比于密度涨落谱：

$$\frac{d^2\sigma}{d\Omega\,dE'} = \frac{k'}{k}\,b^2\,S(q,\omega), \qquad S(q,\omega) = \frac{1}{N}\int dt\,e^{i\omega t}\big\langle n(\vec q,t)\,n(-\vec q,0)\big\rangle_0,$$

由涨落–耗散定理 $S(q,\omega) = 2\chi''_{nn}(q,\omega)/(1-e^{-\beta\omega})$：**散射实验直接"看见"密度响应的吸收谱**。因子 $1/(1-e^{-\beta\omega})$ 是细致平衡：$\omega<0$（中子从体系取能）一侧被 $e^{-\beta\omega}$ 压低——低温下体系没有热涨落可以上交能量。磁散射截面同理正比于自旋–自旋关联函数 $S^{zz}(q,\omega)$。

**一个预告**：把 Kubo 公式用于横向电导 $\sigma_{xy}$（$\vec j$ 对垂直方向 $\vec E$ 的响应），对有能隙体系可把电流–电流关联改写成占据态 Berry 曲率在 Brillouin 区上的积分——$\sigma_{xy}$ 精确量子化为整数乘 $e^2/h$，这个整数就是陈数（TKNN）。响应函数不只是"近似计算的工具"，它自身的拓扑性质就是物理：Berry 曲率的量子力学地基在本书[第 13 篇 绝热定理与 Berry 相位](13-adiabatic-berry-phase.md)，多体的下半场是凝聚态书[第 11 章](../../condensed-matter/docs/11-quantum-hall-effect.md)与[第 12 章](../../condensed-matter/docs/12-topological-phases.md)。

## 小结

- 凝聚态实验测的是响应函数：弱场下 $\delta\langle A\rangle = \chi F$，$\chi$ 是严格的物理对象。
- Kubo 公式 $\chi^R_{AB}(t) = -i\theta(t)\langle[A(t),B(0)]\rangle_0$：线性响应 = 平衡态对易子关联函数；推导只做了一件事——相互作用绘景下把密度矩阵展开到微扰一阶。
- 因果性 $\Rightarrow$ 上半平面解析 $\Rightarrow$ Kramers–Kronig 关系；Lehmann 表示 $\Rightarrow$ 极点 = 激发能（第 19 章的出发点）；$\chi'' \equiv -\mathrm{Im}\,\chi^R \ge 0$ 度量吸收功率 $\overline{P} = \omega\chi''F_0^2/2$。
- 涨落–耗散定理 $S(\omega) = 2\chi''(\omega)/(1-e^{-\beta\omega})$，经典极限（$\hbar\omega\ll k_BT$）下 $S(\omega) = 2k_BT\chi''_{\mathrm{cl}}(\omega)/\omega$。
- 四个化身：$\sigma(\omega)$（Drude）、$\chi_s$（Curie 定律）、$\varepsilon(q,\omega)$（Thomas–Fermi 屏蔽 = 静态极限，→ 第 6 章）、$S(q,\omega)$（中子截面）；$\sigma_{xy}$ 的 Kubo 表达式是 TKNN 整数与拓扑物态的入口（→ 第 11、12 章）。

## 自检问题

**1.** 从 $H(t) = H_0 + BF(t)$ 出发，在相互作用绘景下把密度矩阵演化展开到微扰一阶，完整推导 Kubo 公式 $\chi^R_{AB}(t-t') = -i\theta(t-t')\langle[A(t),B(t')]\rangle_0$，并说明 $\theta$ 函数与"对未微扰系综取平均"各从哪一步来。

<details markdown="1"><summary>点击显示答案</summary>

**第一步（演化方程）**：相互作用绘景 $\rho_I = e^{iH_0t}\rho\,e^{-iH_0t}$ 满足 $i\partial_t\rho_I = [H'_I(t),\rho_I(t)]$（由 von Neumann 方程 $i\partial_t\rho = [H,\rho]$ 两边代入即得）。

**第二步（一阶迭代）**：以 $\rho_I(-\infty) = \rho_0$ 为初条件逐阶迭代，零阶项是 $\rho_0$ 本身（因 $[\rho_0,H_0]=0$，它在相互作用绘景中不动），一阶项为

$$\rho_I^{(1)}(t) = -i\int_{-\infty}^{t}dt'\,[H'_I(t'),\rho_0].$$

积分上限 $t$ 是因果性的来源——它后来变成 $\theta(t-t')$。

**第三步（取期望值）**：$\langle A\rangle(t) = \mathrm{Tr}[\rho_I(t)A_I(t)]$，减去平衡值 $\mathrm{Tr}[\rho_0 A]$（零阶项），得

$$\delta\langle A\rangle(t) = -i\int_{-\infty}^{t}dt'\,\mathrm{Tr}\big\{[H'_I(t'),\rho_0]\,A_I(t)\big\}.$$

**第四步（循环置换）**：$\mathrm{Tr}\{[X,\rho]Y\} = \mathrm{Tr}\{X\rho Y\} - \mathrm{Tr}\{\rho XY\} = \mathrm{Tr}\{\rho YX\} - \mathrm{Tr}\{\rho XY\} = \mathrm{Tr}\{\rho[Y,X]\}$，于是

$$\delta\langle A\rangle(t) = -i\int_{-\infty}^{t}dt'\,\langle[A_I(t),H'_I(t')]\rangle_0 = -i\int_{-\infty}^{t}dt'\,F(t')\langle[A_I(t),B_I(t')]\rangle_0,$$

即 $\delta\langle A\rangle(t) = \int dt'\,\chi^R_{AB}(t-t')F(t')$ 且 $\chi^R_{AB}(t-t') = -i\theta(t-t')\langle[A(t),B(t')]\rangle_0$。$\blacksquare$

两个要点各有出处：$\theta(t-t')$ 来自第二步积分的上限（扰动在 $t'$、观测在 $t$，只有 $t>t'$ 有贡献）；$\langle\cdots\rangle_0$ 来自第四步——一阶项里 $\rho_0$ 与两个算符并排，期望值天然是对**未微扰**系综取的。高阶项给出非线性响应（二阶 = 三算符嵌套对易子），本章不要。

</details>

**2.** 用因果性推导 Kramers–Kronig 关系，并对模型响应函数 $\chi^R(\omega) = \dfrac{1}{2m\omega_0}\left[\dfrac{1}{\omega-\omega_0+i\eta} - \dfrac{1}{\omega+\omega_0+i\eta}\right]$（阻尼谐振子的精确形式）验证之。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：因果性给出 $t<0$ 时 $\chi^R(t)=0$，故 $\chi^R(\omega) = \int_0^\infty dt\,e^{i\omega t}\chi^R(t)$ 在 $\mathrm{Im}\,\omega>0$ 解析。取围道：实轴（在 $z=\omega$ 处以上方小半圆绕过）加上半平面大半圆。大圆贡献随 $\chi^R(z)\to0$（$|z|\to\infty$）消失；围道内无极点，故

$$0 = \mathrm{P}\!\int_{-\infty}^{\infty}d\omega'\,\frac{\chi^R(\omega')}{\omega'-\omega} - i\pi\chi^R(\omega),$$

（小半圆是顺时针的半圈，贡献 $-i\pi$ 乘留数）。分离实虚部：

$$\mathrm{Re}\,\chi^R(\omega) = \frac{1}{\pi}\mathrm{P}\!\int d\omega'\,\frac{\mathrm{Im}\,\chi^R(\omega')}{\omega'-\omega}, \qquad \mathrm{Im}\,\chi^R(\omega) = -\frac{1}{\pi}\mathrm{P}\!\int d\omega'\,\frac{\mathrm{Re}\,\chi^R(\omega')}{\omega'-\omega}.\ \blacksquare$$

**验证**：模型的虚部 $\mathrm{Im}\,\chi^R(\omega) = \dfrac{\pi}{2m\omega_0}\big[-\delta(\omega-\omega_0) + \delta(\omega+\omega_0)\big]$。代入第一条 KK：

$$\frac{1}{\pi}\mathrm{P}\!\int d\omega'\,\frac{\mathrm{Im}\,\chi^R(\omega')}{\omega'-\omega} = \frac{1}{2m\omega_0}\left[\frac{-1}{\omega_0-\omega} + \frac{1}{-\omega_0-\omega}\right] = \frac{1}{2m\omega_0}\left[\frac{1}{\omega-\omega_0} - \frac{1}{\omega+\omega_0}\right] = \mathrm{Re}\,\chi^R(\omega).\ \checkmark$$

注意该模型两个极点 $\omega = \pm\omega_0 - i\eta$ 都在下半平面，与"上半平面解析"自洽；若把 $i\eta$ 符号写反（超前响应），KK 关系整体变号——解析性所在半平面由因果性唯一决定。

</details>

**3.** 从量子涨落–耗散定理取经典极限 $\hbar\omega\ll k_BT$，并用谐振子验证它给出正确的能量均分 $\langle x^2\rangle = k_BT/(m\omega_0^2)$。

<details markdown="1"><summary>点击显示答案</summary>

**取极限**：恢复 $\hbar$。量子 FDT 为 $S(\omega) = 2\chi''(\omega)/(1-e^{-\beta\hbar\omega})$。$\chi^R \propto \hbar$（对易子 $[A(t),B(0)]$ 是 $O(\hbar)$），定义经典响应 $\chi_{\mathrm{cl}} = \chi^R/\hbar$（$\hbar\to0$ 有限，即泊松括号版本）。$\beta\hbar\omega\ll1$ 时 $1-e^{-\beta\hbar\omega}\approx\beta\hbar\omega$：

$$S(\omega) = \frac{2\,\hbar\chi''_{\mathrm{cl}}(\omega)}{\beta\hbar\omega} = \frac{2k_BT}{\omega}\,\chi''_{\mathrm{cl}}(\omega).\ \blacksquare$$

**均分检验**：经典谐振子（$H' = -xF$）的响应 $\chi_{\mathrm{cl}}(\omega) = 1/\big[m(\omega_0^2-(\omega+i\eta)^2)\big]$，虚部

$$\chi''_{\mathrm{cl}}(\omega) = \frac{\pi}{2m\omega_0}\big[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\big].$$

均方涨落是（对称化）涨落谱的频率积分，经典极限下 $\bar S = S$：

$$\langle x^2\rangle = \int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\,S(\omega) = \int\frac{d\omega}{2\pi}\,\frac{2k_BT}{\omega}\,\frac{\pi}{2m\omega_0}\big[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)\big] = \frac{k_BT}{2m\omega_0}\left(\frac{1}{\omega_0}+\frac{1}{\omega_0}\right) = \frac{k_BT}{m\omega_0^2}.$$

于是势能 $\tfrac12 m\omega_0^2\langle x^2\rangle = \tfrac12 k_BT$——能量均分定理精确重现。注意量子版会给 $\tfrac12\omega_0\coth(\beta\omega_0/2)$（含零点能），经典极限恰好把 $\coth$ 展开成 $2/\beta\hbar\omega$。涨落的温度依赖性（$\propto T$）整个来自 FDT 里的 $(1-e^{-\beta\hbar\omega})^{-1}$——没有它，谱里只剩与 $T$ 无关的零点运动。

</details>

**4.** 单个自旋 $1/2$ 置于磁场 $h$（沿 $z$）中，$H_0 = -\mu h S_z$（$\mu = g\mu_B$），分别用涨落公式与直接求导计算零场磁化率，并与居里定律对比。

<details markdown="1"><summary>点击显示答案</summary>

**直接求导**：两能级 $E_\pm = \mp\mu h/2$，配分函数 $Z = e^{\beta\mu h/2}+e^{-\beta\mu h/2} = 2\cosh(\beta\mu h/2)$，

$$\langle M_z\rangle = \mu\langle S_z\rangle = \frac{\mu}{2}\tanh\frac{\beta\mu h}{2} \;\Longrightarrow\; \chi = \left.\frac{\partial\langle M_z\rangle}{\partial h}\right|_{h=0} = \frac{\beta\mu^2}{4}.$$

**涨落公式**：$[M_z,H_0]=0$，故 $\chi = \beta\big(\langle M_z^2\rangle - \langle M_z\rangle^2\big)$。$h=0$ 时 $\langle M_z\rangle = 0$、$M_z^2 = \mu^2/4$ 是常数（$S_z^2 = 1/4$），得

$$\chi = \beta\cdot\frac{\mu^2}{4} = \frac{\mu^2}{4k_BT},$$

两法一致。注意这里 Kubo 的 Lehmann 形式"沉默"了：$M_z$ 与 $H_0$ 对易，$\chi''(\omega)$ 在 $\omega\neq0$ 处处为零，全部谱权重压在零频——静态磁化率的信息在 $\chi'(0)$ 里，经 KK 由零频权重给出。

**与居里定律对比**：$\chi \propto 1/T$，正是 Curie 定律 $\chi = C/T$。$N$ 个独立自旋 $1/2$：$C = N\mu^2/(4k_B) = N(g\mu_B)^2S(S+1)/(3k_B)$（$S=1/2$：$S(S+1)/3 = 1/4$ ✓）。物理：零场下自旋取向完全无规，磁化全靠外场对 Boltzmann 权重的极化；温度越高权重越平，极化越难——这就是 $1/T$。高温展开 $\tanh x\approx x$ 是同一句话的另一面：$\langle M_z\rangle \approx \mu^2h/(4k_BT)$。

</details>

**5.** 证明单色场 $F(t) = F_0\cos\omega t$ 下体系的平均吸收功率 $\overline{P} = \frac{\omega}{2}\chi''(\omega)F_0^2$（耗散 = 吸收），并用费米黄金定则逐项核对。

<details markdown="1"><summary>点击显示答案</summary>

**线性响应一侧**：$H(t) = H_0 + BF(t)$ 的能量变化率 $\dot E = \langle\partial H/\partial t\rangle = \langle B\rangle(t)\,\dot F(t)$。单色场的响应 $\delta\langle B\rangle(t) = \mathrm{Re}\big[\chi^R(\omega)F_0 e^{-i\omega t}\big] = F_0\big[\chi'(\omega)\cos\omega t + \mathrm{Im}\,\chi^R(\omega)\sin\omega t\big]$，而 $\dot F = -\omega F_0\sin\omega t$。相乘并周期平均（$\overline{\sin\cos}=0$、$\overline{\sin^2}=1/2$；常数项 $\langle B\rangle_0\dot F$ 平均为零）：

$$\overline{P} = -\omega F_0^2\,\mathrm{Im}\,\chi^R(\omega)\cdot\frac12 = \frac{\omega}{2}\,\chi''(\omega)\,F_0^2\ \ge\ 0,$$

（用了 $\chi'' \equiv -\mathrm{Im}\,\chi^R$ 及 5.2 节的非负性）。实部 $\chi'$ 的贡献正比 $\sin\cos$，整周期平均为零——弹性响应不耗散。

**黄金规则一侧**：$F(t) = \frac{F_0}{2}(e^{i\omega t}+e^{-i\omega t})$，跃迁 $m\to n$（$E_n = E_m+\omega$ 吸能）的速率为 $2\pi\lvert B_{mn}\rvert^2(F_0/2)^2\,\delta(E_n-E_m-\omega)$；$e^{+i\omega t}$ 项对应放能的逆跃迁。净吸收功率

$$\overline{P} = \frac{\pi F_0^2}{2}\,\frac{1}{Z}\sum_{m,n}\big(e^{-\beta E_m}-e^{-\beta E_n}\big)\,\lvert B_{mn}\rvert^2\,\omega\,\delta(\omega+E_m-E_n) = \frac{\omega}{2}\,F_0^2\,\chi''(\omega),$$

末等号正是 5.2 节 $\chi''$ 的 Lehmann 和。两侧逐项相同 $\blacksquare$——这也把本章与 [第 07 篇 微扰论](07-perturbation-theory.md)的黄金定则接上了：Kubo 公式 = 对所有末态求和、对初态做热平均的黄金定则。

</details>

## 参考

- Mahan《Many-Particle Physics》第 3 章（§3.7–3.8：有限温度格林函数与 Kubo 公式）——与本章符号约定一致。
- Bruus & Flensberg《Many-Body Quantum Theory in Condensed Matter Physics》第 6 章（线性响应理论）——推导风格与本章最接近。
- Fetter & Walecka《Quantum Theory of Many-Particle Systems》§31–32（迟滞响应函数与解析性质）。
- Coleman《Introduction to Many-Body Physics》响应函数章节（Kubo 公式与涨落–耗散定理）。
- Landau & Lifshitz《统计物理学 I》§123–126（广义磁化率与涨落–耗散定理的经典表述，注意其 $H'=-BF$ 约定与本章差一个符号）。
