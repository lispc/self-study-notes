# 相互作用电子气：屏蔽、等离激元与 Fermi 液体

> 本书位置：凝聚态物理入门导论 · 第 6 章（第二部分：相互作用、序与相变）
> 前置知识：金属自由电子气（[第 3 章](03-free-electron-gas.md)：费米球、态密度、$E_F$ 与 $k_F$）；量子力学的二次量子化形式与傅里叶变换；有[声子](02-lattice-vibrations-phonons.md)一章"集体激发量子化"的经验更好。
> 学习目标：理解处理库仑相互作用电子气的四个层次——Hartree–Fock、Thomas–Fermi 屏蔽、RPA 与等离激元、Landau Fermi 液体——并看清"屏蔽"与"准粒子"这两个凝聚态核心概念与量子场论的对应关系。

---

**单位约定**：本章保留 $\hbar$ 与 $k_B$（不做自然单位约定）；库仑相互作用采用高斯制记号，即 $e^2$ 代表 SI 制中的 $e^2/4\pi\varepsilon_0$，库仑势为 $e^2/r$。

## 1. 一句话总结

**金属里的电子虽然以 $e^2/r$ 的长程库仑力强烈相互作用，但两件事拯救了"近独立电子"图像：一是屏蔽——每个电子拖着一团电荷云，把库仑力截断到 Å 量级尺度，并催生集体振荡（等离激元）；二是 Pauli 不相容原理——它把费米面附近准粒子的散射相空间压到 $(\varepsilon-E_F)^2$，使准粒子在费米面附近任意长寿。这就是 Landau 的 Fermi 液体理论：强相互作用系统的低能物理，等价于一个"换了参数"的弱相互作用费米气体。**

## 2. 凝胶（jellium）模型

真实金属太复杂：有晶格、有能带、有杂质。要干净地研究**库仑相互作用本身**的后果，先把一切次要结构磨平——这就是凝胶模型：

- $N$ 个电子，密度 $n=N/V$，带电 $-e$；
- 均匀分布的正电荷背景，密度 $+en$（离子实的涂抹版），保证整体电中性；
- 无晶格周期性、无杂质、无磁场。

哈密顿量为

$$H = \sum_i \frac{\vec p_i^{\,2}}{2m} + \frac12\sum_{i\neq j}\frac{e^2}{\lvert\vec r_i-\vec r_j\rvert} + H_{\text{背景}} + H_{\text{电子-背景}}.$$

用一个数刻画密度：每个电子平均占一个半径 $\bar r$ 的球，

$$\frac{4\pi}{3}\bar r^{3} = \frac{1}{n}, \qquad r_s \equiv \frac{\bar r}{a_B}, \qquad a_B = \frac{\hbar^2}{me^2},$$

其中 $r_s$ 是无量纲密度参数（$a_B$ 是 Bohr 半径）。费米波矢

$$k_F = (3\pi^2 n)^{1/3} = \left(\frac{9\pi}{4}\right)^{1/3}\frac{1}{\bar r}.$$

**$r_s$ 的物理**：量纲分析给出动能 $\sim \hbar^2/m\bar r^2 \propto r_s^{-2}$，势能 $\sim e^2/\bar r \propto r_s^{-1}$，于是

$$\frac{\text{势能}}{\text{动能}} \propto r_s.$$

反直觉的结论：**密度越高（$r_s$ 越小），相互作用越不重要**。$r_s\to 0$ 的高密度极限里库仑作用只是微扰；而真实金属 $r_s \approx 2\sim 6$（如 Al $\approx 2$，Na $\approx 4$，Cs $\approx 5.6$），恰好卡在两者相争的中间地带——这正是金属物理难而有趣的原因。

正背景的首要作用是抵消平均场：电子–背景、背景–背景与电子–电子的 Hartree 项（$q=0$ 傅里叶分量）精确相消。所以凡是用平面波 Slater 行列式描述的均匀态，Hartree 项恒为零——第一个非平凡的相互作用效应来自交换。

## 3. Hartree–Fock：交换能与交换穴

### 3.1 交换自能

取单 Slater 行列式（双占据平面波填满费米球）做变分，单粒子能量为动能加 Fock 项：

$$\varepsilon(\vec k) = \frac{\hbar^2 k^2}{2m} - \sum_{\lvert\vec k'\rvert<k_F} v(\vec k-\vec k'), \qquad v(\vec q) = \frac{4\pi e^2}{q^2},$$

第二项中 $v(\vec q)$ 是库仑势的傅里叶变换，求和只包括**同自旋**电子（交换要求自旋平行）。把求和换成积分 $\sum_{\vec k'}\to V\int d^3k'/(2\pi)^3$，令 $\vec q=\vec k-\vec k'$，对费米球积分：

$$\Sigma_x(k) = -\int_{\lvert\vec k'\rvert<k_F}\frac{d^3k'}{(2\pi)^3}\frac{4\pi e^2}{\lvert\vec k-\vec k'\rvert^2} = -\frac{e^2k_F}{\pi}\left[1+\frac{k_F^2-k^2}{2kk_F}\ln\left\lvert\frac{k_F+k}{k_F-k}\right\rvert\right].$$

这就是大纲里那条著名的色散关系。在费米面上方括号趋于 2，故 $\Sigma_x(k_F) = -2e^2k_F/\pi$。对所有占据态取平均，得**每个电子的交换能**

$$\frac{E_x}{N} = -\frac{3e^2k_F}{4\pi} = -\frac{0.916}{r_s}\ \text{Ry},$$

与动能 $3E_F/5 = 2.21/r_s^2\ \text{Ry}$ 相加即凝胶基态能量的 HF 结果。注意交换能是**负**的，且在 $r_s$ 大时相对动能越来越重要——它是金属结合能的重要来源。

### 3.2 交换穴

交换能的几何图像是**交换穴（exchange hole）**：计算同自旋电子对的关联函数，得

$$g_{\uparrow\uparrow}(r) = 1 - 9\,\frac{\big(\sin k_F r - k_F r\cos k_F r\big)^2}{(k_F r)^6}.$$

$g_{\uparrow\uparrow}(0)=0$：Pauli 原理禁止同自旋电子重合，每个电子周围被"挖掉"一个半径 $\sim k_F^{-1}$ 的禁区，$r\to\infty$ 时 $g\to 1$（无关联）。把挖掉的电荷积分，恰好是 $+e$：

$$n\int d^3r\,\big[1-g_{\uparrow\uparrow}(r)\big] = 1 \quad (\text{单位电荷}).$$

每个电子拖着这个"正电荷空穴"运动，有效电荷减小，能量降低——这就是交换能的来源。**交换穴来自量子统计，不是库仑力的动力学结果**；后面会看到，库仑力自己也会挖一个"关联穴"，那才是屏蔽。

### 3.3 HF 的定性失败

HF 概念上很漂亮，定量上却翻车。看费米面处的群速度：

$$\frac{d\varepsilon}{dk} = \frac{\hbar^2 k}{m} + \frac{e^2}{\pi}\left[\frac{k_F^2+k^2}{2kk_F}\ln\left\lvert\frac{k_F+k}{k_F-k}\right\rvert - 1\right] \xrightarrow{k\to k_F} +\infty\ (\text{对数发散}).$$

$d\varepsilon/dk$ 发散意味着费米面处态密度 $N(E_F)\propto (d\varepsilon/dk)^{-1}\to 0$——预言低温比热线性系数 $\gamma\to 0$、无 Pauli 顺磁，与实验（金属 $\gamma$ 非零，量级同自由电子）直接矛盾。

**病根**：发散来自积分中小 $q$ 区域，即 $v(q)=4\pi e^2/q^2$ 的 $q\to 0$ 奇异性——**库仑力的长程尾巴**。HF 把它原封不动地保留了。而物理上，电子气会自己把这根尾巴屏蔽掉（下节）。所以 HF 的失败不是"近似不够高阶"，而是**定性地丢了屏蔽这个物理**。治病先查病因：我们下一节就处理长程问题。

## 4. 屏蔽：Thomas–Fermi 理论

### 4.1 线性响应与自洽方程

在电子气中放入一个外电荷分布 $\rho_{\text{ext}}(\vec r)$（比如一个 $+Ze$ 的杂质核）。电子会重新排布，产生感应电荷 $\rho_{\text{ind}}$，总静电势 $\varphi$ 满足 Poisson 方程：

$$-\nabla^2\varphi = 4\pi\big(\rho_{\text{ext}} + \rho_{\text{ind}}\big).$$

**关键假设（Thomas–Fermi）**：$\varphi$ 在费米波长尺度上缓变，于是局部看来电子气仍是均匀的，只是化学势被静电能 $-e\varphi$ 抬升。热平衡要求**电化学势处处相等**：

$$\mu\big(n(\vec r)\big) - e\varphi(\vec r) = \text{常数}.$$

对弱 $\varphi$ 做线性展开，$\delta n = n(\vec r)-n = e\varphi\cdot dn/d\mu$。自由电子气 $dn/d\mu$ 就是费米面态密度（含两种自旋、单位体积）

$$N(E_F) = \frac{mk_F}{\pi^2\hbar^2},$$

于是感应电荷 $\rho_{\text{ind}} = -e\,\delta n = -e^2 N(E_F)\,\varphi$。代回 Poisson 方程：

$$\big(-\nabla^2 + k_{TF}^2\big)\varphi = 4\pi\rho_{\text{ext}}, \qquad \boxed{k_{TF}^2 = 4\pi e^2 N(E_F) = \frac{4k_F}{\pi a_B}}$$

### 4.2 屏蔽库仑势

对点电荷 $\rho_{\text{ext}} = Ze\,\delta(\vec r)$，傅里叶空间立即给出

$$\varphi(\vec q) = \frac{4\pi Ze}{q^2 + k_{TF}^2} \;\xrightarrow{\text{反变换}}\; \varphi(r) = \frac{Ze}{r}\,e^{-k_{TF}r}.$$

**库仑势变成了 Yukawa 势**：裸 $1/r$ 被指数因子在屏蔽长度 $k_{TF}^{-1}$ 外截断。等价地，相互作用被"穿衣"：

$$v(q) = \frac{4\pi e^2}{q^2} \;\longrightarrow\; v_{\text{scr}}(q) = \frac{4\pi e^2}{q^2+k_{TF}^2}.$$

$q\to 0$ 处不再发散——这正是上一节 HF 病根的药。把 $v_{\text{scr}}$ 代回交换积分，$d\varepsilon/dk$ 的发散消失（自检题 5）。

**数量级**：$k_{TF}\sim k_F$（因 $k_F a_B\sim 1/r_s$，$k_{TF}/k_F \approx 0.66\sqrt{r_s}$），金属中 $k_{TF}^{-1}\sim 0.5\sim 1$ Å——**屏蔽发生在原子尺度**。这解释了为什么金属对静电场"刀枪不入"（场穿不进导体），也解释了为什么金属内部的电子感受到的是短程力。

**TF 的适用条件与局限**：要求势在 $k_F^{-1}$ 尺度缓变，即 $k_{TF}\lesssim k_F$，也就是 $r_s$ 不能太大；且 TF 只保留**静态**响应，完全不含频率依赖——动力学屏蔽要等 RPA（第 6 节）。

## 5. 等离激元：电子气的集体振荡

### 5.1 经典推导

把电子气相对正背景整体平移一小段 $\xi$（想象一块平板电容器状的位移）。两端出现面电荷 $\sigma = \pm ne\xi$，内部产生均匀电场 $E = 4\pi ne\xi$。每个电子受力 $-eE$，于是

$$m\ddot\xi = -eE = -4\pi ne^2\xi \;\Longrightarrow\; \boxed{\omega_p^2 = \frac{4\pi ne^2}{m}}$$

$\omega_p$ 叫**等离子体频率**。代入金属密度 $n\sim 10^{23}\ \mathrm{cm^{-3}}$：

$$\omega_p \sim 1.8\times 10^{16}\ \mathrm{s^{-1}}, \qquad \hbar\omega_p \sim 10\ \text{eV}.$$

落在紫外区。这就是为什么碱金属对可见光透明以下的频段强烈反射（频率低于 $\omega_p$ 的光激起电子集体响应把场屏蔽掉）、而紫外透明的现象。

### 5.2 集体模式 vs 单粒子激发

更细致的处理（Lindhard 介电函数，见第 6 节）给出长波色散

$$\omega^2(q) \approx \omega_p^2 + \frac35 v_F^2 q^2 + O(q^4).$$

长波极限频率不趋于零——这是一个**有能隙的集体模式**，与声波（声子，$\omega=cq$）形成对照。物理原因：库仑力是长程的，$q\to 0$ 时 $v(q)\propto q^{-2}$ 发散，恰好抵消了密度振荡恢复力中的 $q^2$。

与之相对的是**单粒子（电子–空穴对）激发**：把一个电子从费米球内搬到球外，动量转移 $q$，能量在

$$0 \le \hbar\omega \le \frac{\hbar^2}{m}\left(k_F q + \frac{q^2}{2}\right)$$

的连续谱内。两条激发谱在小 $q$ 处分离：等离激元高高在上，电子–空穴连续区低低在下；当 $q$ 大到 $q_c\sim \omega_p/v_F$，等离激元色散曲线**扎进连续区**，集体模式衰变为电子–空穴对（Landau 阻尼），不再是无阻尼模式。

把集体振荡量子化，$\hbar\omega_p$ 一份一份的能量量子叫**等离激元（plasmon）**——与声子完全平行：经典波动方程的正则模式量子化（参见[声子一章](02-lattice-vibrations-phonons.md)）。它是玻色型元激发，已被电子能量损失谱（EELS）直接观测。

<details markdown="1"><summary>补充说明：与 QFT 中集体模式的类比</summary>

等离激元的存在方式在 QFT 里有精确的对应物：拉氏量里没有"等离激元场"，它是库仑相互作用+费米海的**动力学产物**，像 QFT 里由基本场复合出来的束缚态或共振。更漂亮的对应在超导里：规范对称性破缺后，等离激元（相位模式）被规范场"吃掉"，光子获得质量——迈斯纳效应，这正是 Anderson–Higgs 机制的凝聚态原版（见[超导](08-superconductivity.md)一章）。可以说：**金属中等离子体频率 $\omega_p$ 就是"介质中光子的质量"**。

</details>

## 6. RPA：环图求和，与真空极化是同一个物理

Thomas–Fermi 只处理了静态极限。完整的线性响应要允许 $\varphi$ 含时：电子感受到的不是外势 $\varphi_{\text{ext}}$，而是**外势加所有其他电子的感应势**这个自洽总势 $\varphi$。对总势做响应：

$$\rho_{\text{ind}} = \chi_0\,\varphi = \chi_0\big(\varphi_{\text{ext}} + v\,\rho_{\text{ind}}\big),$$

其中 $\chi_0(q,\omega)$ 是自由电子气的密度响应函数（Lindhard 函数）。解出

$$\chi(q,\omega) = \frac{\chi_0}{1-v(q)\chi_0}, \qquad \varepsilon_{RPA}(q,\omega) = 1 - v(q)\chi_0(q,\omega).$$

分母是一个几何级数：电子极化一次、极化的势再极化……逐项正是**一环套一环的"气泡图"求和**。这个近似叫**无规相近似（RPA，random phase approximation）**，名字来自 Bohm–Pines 早期处理中"不同 $q$ 分量相位无规、交叉项相消"的论证。

RPA 统一了前两节：

- 静态长波极限 $\omega=0,\ q\to 0$：$\chi_0\to -N(E_F)$，$\varepsilon \to 1+k_{TF}^2/q^2$——回到 Thomas–Fermi；
- $\varepsilon(q,\omega)=0$ 的零点：总势可以不依赖外势自持振荡——这就是等离激元极点，$\omega\to\omega_p$。

学过[一圈重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)的读者应立即认出这个结构：那里 QED 光子的**真空极化**也是电子–正电子气泡插进光子传播子，几何级数求和给出跑动耦合 $e^2(q^2)$。两边是**逐字对应的同一个物理**：

- 真空极化 $\Pi(q^2)$ ↔ 电子气极化 $\chi_0(q,\omega)$；
- 跑动耦合 ↔ 屏蔽库仑势 $v(q)/\varepsilon(q,\omega)$；
- "裸电荷被虚粒子云包围" ↔ "电子被交换穴/关联穴包围"。

QED 中电荷在短距离变大（反屏蔽，因真空极化）；电子气中电荷在长距离被截断（屏蔽，因可极化的费米海而非真空）。一个理论机器，两种介质。

## 7. Landau Fermi 液体理论

### 7.1 绝热连续假设与准粒子

现在面对真问题：$r_s\sim 2\sim 6$，微扰论不可靠，但实验上金属的比热、磁化率、输运全都**定性地像自由电子气**，只是系数变了。Landau（1956）把这反常的"像"提升为原理。

**绝热连续假设**：把相互作用 $v$ 换成 $\lambda v$，让 $\lambda$ 从 0 绝热地升到 1。假设过程中不发生相变（无能隙闭合、无对称性破缺），则自由电子气的态与相互作用系统的态**一一对应**：$N$ 个电子占据费米球的基态，绝热演化为相互作用基态；在 $\vec k$ 处加一个电子的激发态，演化为一个**准粒子（quasiparticle）**激发态——同样带电荷 $-e$、自旋 $1/2$、动量 $\hbar\vec k$，但它已是"电子 + 周围扰动云"的复合对象。

准粒子的能量泛函写作

$$E = E_0 + \sum_{\vec k\sigma}\varepsilon_{\vec k}\,\delta n_{\vec k\sigma} + \frac12\sum_{\vec k\sigma,\vec k'\sigma'} f_{\vec k\sigma,\vec k'\sigma'}\,\delta n_{\vec k\sigma}\,\delta n_{\vec k'\sigma'} + \cdots$$

$\varepsilon_{\vec k}$ 是准粒子能量（费米面上 $\varepsilon=E_F$，$\vec\nabla_{\vec k}\varepsilon\rvert_{k_F} = \hbar\vec k_F/m^*$ 定义**有效质量** $m^*$）；$f$ 函数刻画准粒子之间的剩余相互作用，是 Landau 参数的来源。

这套图像要能自洽，前提是**准粒子确实是好的激发**：它的能量不确定性 $\hbar/\tau$ 必须远小于它相对费米面的能量 $\varepsilon-E_F$，否则"粒子"概念本身糊掉。这个条件是否成立，全看寿命。

### 7.2 准粒子寿命：相空间论证（关键推导）

考虑费米球上方一个准粒子，$\varepsilon_1>E_F$。它要衰变，只能与球内一个粒子（$\varepsilon_2<E_F$）散射，把两者都踢到球外（$\varepsilon_3,\varepsilon_4>E_F$）——Pauli 原理禁止任何末态落在已占据的球内。能量守恒：

$$\varepsilon_1+\varepsilon_2 = \varepsilon_3+\varepsilon_4.$$

以费米能为零点记 $\xi_i\equiv\varepsilon_i-E_F$，则 $\xi_1>0$，$\xi_2<0$，$\xi_3,\xi_4>0$，且 $\xi_1+\xi_2=\xi_3+\xi_4$。逐个数可用的能量窗口：

1. $\xi_3>0$ 且 $\xi_4=\xi_1+\xi_2-\xi_3>0$，要求 $0<\xi_3<\xi_1+\xi_2$——宽度至多 $\sim\xi_1$；
2. 而 $\xi_1+\xi_2>0$ 要求 $-\xi_1<\xi_2<0$——初态粒子的能量窗口也只有宽度 $\xi_1$。

两个独立能量变量各自贡献一个因子 $\xi_1$。黄金规则的散射率对初态能量与末态能量积分（矩阵元 $M$ 在窗口内近似常数，动量约束不改变能量幂次）：

$$\frac{1}{\tau} \propto \lvert M\rvert^2\int_{-\xi_1}^{0}d\xi_2\int_0^{\xi_1+\xi_2}d\xi_3 = \lvert M\rvert^2\,\frac{\xi_1^2}{2}.$$

即

$$\boxed{\frac{1}{\tau} \propto (\varepsilon-E_F)^2}, \qquad \text{有限温度：}\ \frac{1}{\tau}\propto (\varepsilon-E_F)^2 + \pi^2(k_BT)^2,$$

量纲由唯一可用的能量尺度补齐：$1/\tau\sim (\varepsilon-E_F)^2/\hbar E_F$（相差量级为 1 的数值系数）。

**自洽性立刻兑现**：

$$\frac{\hbar/\tau}{\varepsilon-E_F} \sim \frac{\varepsilon-E_F}{E_F} \xrightarrow{\varepsilon\to E_F} 0.$$

越靠近费米面，准粒子越"纯"：寿命发散得比能量趋于零更快。**这不是因为相互作用弱，而是因为 Pauli 原理掐死了散射相空间**——这就是 Fermi 液体理论对"为什么强相互作用金属仍可用单粒子图像"的回答。数值估算见自检题 4：室温下 $\tau\sim$ 皮秒量级，$\hbar/\tau\ll k_BT$，条件非常宽裕。

### 7.3 Landau 参数与可测量

$f$ 函数在费米面上只依赖 $\vec k\cdot\vec k'$ 的夹角，按 Legendre 多项式展开并无量纲化：

$$N(E_F)\,f^{s,a}(\cos\theta) = \sum_l F_l^{s,a}\,P_l(\cos\theta),$$

$F_l^s$（自旋对称）与 $F_l^a$（自旋反对称）即 **Landau 参数**。它们不是微观可算的免费午餐——要由实验或更微观的理论输入——但一旦给定，可测量被逐一锁定。Galilei 不变体系（凝胶）有恒等式

$$\frac{m^*}{m} = 1 + \frac{F_1^s}{3};$$

比热线性系数 $\gamma/\gamma_0 = m^*/m$；Pauli 磁化率 $\chi/\chi_0 = (m^*/m)/(1+F_0^a)$；压缩率、零声（zero sound，$F_0^s>0$ 时存在的无碰撞集体模式）等都有类似表达式。弱相互作用极限下 $F$ 全趋于零，$m^*\to m$，回到自由气体——Fermi 液体包含而非替代了旧理论。

**有效性的本质**：相互作用再强，只要不引发相变，其全部低能后果只重组进 $m^*$ 与有限个 Landau 参数；高能量、短时标的细节不可分辨，也不需要分辨。这个陈述在下一节会被认出是一个深刻得多的原理。

## 8. 与 QFT 对照：准粒子、穿衣粒子与有效理论

把本章与 QFT 并排看，对应关系是系统的而非修辞的：

- **准粒子 = 穿衣粒子**。QFT 里裸电子被虚光子云穿成物理电子，传播子极点移动、留数 $Z<1$（见[一圈修正与重整化](../../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)）；Fermi 液体里裸电子被关联云穿成准粒子，单粒子 Green 函数 $G(k,\omega) = Z_k/(\omega-\varepsilon_k+i/2\tau_k)+\text{非相干部分}$，同样在极点处有能量、寿命与权重 $Z$。两边衡量"还有多少成分是原来的粒子"的都是谱权重 $Z$。
- **Fermi 液体 = 可重整低能有效理论的凝聚态版**。Wilson 的重整化群视角（同见上述笔记后半部分）说：低能物理只依赖少数**相关与边缘**算符，其余算符随标度变换衰减，细节被洗掉。Shankar 与 Polchinski 在 1990 年代把这句话在费米面重写了一遍：向费米面标度时，准粒子间的四费米相互作用中除少数通道（前向散射——即 Landau 参数；以及 Cooper 通道——超导的种子）外**全部 irrelevant**。于是"Fermi 液体行为普适"不再是经验奇迹，而是标度律的推论：$1/\tau\propto\xi^2$ 正是边缘算符在低能下的幂次计数。
- **屏蔽 = 跑动耦合**，已在第 6 节说过：RPA 环图就是真空极化气泡。

所以本章的标题物——屏蔽、等离激元、Fermi 液体——其实是同一台场论机器在有限密度介质中的三档读数。这个视角将在[超导](08-superconductivity.md)（Cooper 不稳定性：Fermi 液体唯一的普遍失败模式）与[强关联](13-strong-correlations.md)（Mott 物理：绝热连续假设真正崩溃的地方）两章继续展开。

## 9. 小结

| 层次 | 近似 | 关键结果 | 局限 |
|---|---|---|---|
| Hartree–Fock | 单 Slater 行列式变分 | 交换能 $-3e^2k_F/4\pi$、交换穴 | 未屏蔽长程库仑，费米面态密度发散 |
| Thomas–Fermi | 静态线性响应 | $k_{TF}^2=4\pi e^2N(E_F)$、Yukawa 屏蔽势 | 无动力学、$r_s$ 大时不自洽 |
| RPA | 环图几何级数求和 | $\varepsilon(q,\omega)=1-v\chi_0$、等离激元 $\omega_p^2=4\pi ne^2/m$ | 忽略高阶关联修正 |
| Fermi 液体 | 绝热连续 + Landau 参数 | 准粒子 $1/\tau\propto(\varepsilon-E_F)^2$、$m^*/m=1+F_1^s/3$ | 相变处失效（超导、Mott） |

- 凝胶模型唯一的参数是 $r_s$；相互作用的重要性随 $r_s$ 增大。
- HF 的失败不是技术问题而是物理缺失：**屏蔽**是电子气的自身免疫反应，必须把 $1/q^2$ 换成 $1/(q^2+k_{TF}^2)$。
- 等离激元是有能隙的玻色型集体模式，长程库仑所致；$q$ 大时被电子–空穴连续区 Landau 阻尼。
- Landau 范式的核心不等式：$\hbar/\tau\ll\varepsilon-E_F$ 在费米面附近由 Pauli 原理自动保证，与耦合强弱无关。
- 用 Wilson 的话说：Fermi 液体是金属的普适低能不动点。

## 自检问题

**1.** 从零推导 Thomas–Fermi 屏蔽：证明 $k_{TF}^2 = 4\pi e^2 N(E_F)$，并求点电荷 $Ze$ 在电子气中的屏蔽势。

<details markdown="1"><summary>点击显示答案</summary>

设外电荷 $\rho_{\text{ext}}$ 产生总静电势 $\varphi$。平衡时电化学势均匀：$\mu(n(\vec r)) - e\varphi(\vec r) = \text{const}$。线性化得

$$\delta n = \frac{dn}{d\mu}\,e\varphi = N(E_F)\,e\varphi,$$

感应电荷 $\rho_{\text{ind}} = -e\delta n = -e^2 N(E_F)\varphi$。代入 Poisson 方程 $-\nabla^2\varphi = 4\pi(\rho_{\text{ext}}+\rho_{\text{ind}})$：

$$\big(-\nabla^2 + k_{TF}^2\big)\varphi = 4\pi\rho_{\text{ext}}, \qquad k_{TF}^2 \equiv 4\pi e^2 N(E_F).$$

对自由电子气，$n = k_F^3/3\pi^2$ 与 $E_F=\hbar^2k_F^2/2m$ 给出

$$N(E_F) = \frac{dn}{dE_F} = \frac{k_F^2}{\pi^2}\frac{m}{\hbar^2 k_F} = \frac{mk_F}{\pi^2\hbar^2},$$

故 $k_{TF}^2 = 4e^2mk_F/(\pi\hbar^2) = 4k_F/(\pi a_B)$。取 $\rho_{\text{ext}} = Ze\,\delta(\vec r)$，傅里叶变换给出 $\varphi(q) = 4\pi Ze/(q^2+k_{TF}^2)$，反变换：

$$\varphi(r) = Ze\int\frac{d^3q}{(2\pi)^3}\frac{4\pi e^{i\vec q\cdot\vec r}}{q^2+k_{TF}^2} = \frac{Ze}{r}e^{-k_{TF}r}.$$

（用围道积分或已知 Yukawa 势的 Green 函数。）库仑长程尾巴被屏蔽长度 $k_{TF}^{-1}\sim$ Å 指数截断。

</details>

**2.** 推导等离激元频率 $\omega_p^2 = 4\pi ne^2/m$，并说明它为何在 $q\to 0$ 时不趋于零（与声子对比）。

<details markdown="1"><summary>点击显示答案</summary>

把电子气整体相对正背景位移 $\xi$。取一块垂直于位移方向、面积 $A$、厚度 $\xi$ 的平板：它被扫出的电荷在两端形成面密度 $\sigma = \pm ne\xi$。由高斯定理，两"板"间电场为

$$E = 4\pi\sigma = 4\pi ne\xi,$$

方向指向把电子拉回原位。单个电子的运动方程：

$$m\ddot\xi = -eE = -4\pi ne^2\xi \;\Longrightarrow\; \ddot\xi = -\omega_p^2\xi, \qquad \omega_p^2 = \frac{4\pi ne^2}{m}.$$

这是简谐振子方程，频率与振幅无关。

**为何不趋于零**：声子的恢复力来自短程弹性，$q\to 0$ 时应变能 $\propto q^2$，故 $\omega\propto q$。等离激元的恢复力来自库仑场，$q\to 0$ 时 $v(q) = 4\pi e^2/q^2$ 发散，恰好补偿密度振荡中的 $q^2$ 因子，留下有限的 $\omega_p$。换句话说，**长程力把声学模式提升成了有能隙模式**。量子化后，等离激元能量为 $\hbar\omega_p\sim 10$ eV。

</details>

**3.** 给出准粒子寿命 $1/\tau\propto(\varepsilon-E_F)^2$ 的完整相空间论证，并说明为什么动量约束不改变这个幂次。

<details markdown="1"><summary>点击显示答案</summary>

设准粒子 1 能量 $\varepsilon_1>E_F$（记 $\xi_i=\varepsilon_i-E_F$）。散射通道 $1+2\to 3+4$：Pauli 原理要求初态 2 在费米海内（$\xi_2<0$），末态 3、4 在费米海外（$\xi_3,\xi_4>0$）。能量守恒 $\xi_1+\xi_2=\xi_3+\xi_4$。

黄金规则（设矩阵元 $M$ 在窄窗口内缓变，近似为常数）：

$$\frac{1}{\tau} \sim \frac{2\pi}{\hbar}\lvert M\rvert^2\!\!\int\! d\xi_2\,d\xi_3\,d\xi_4\; N(E_F)^3\;\delta(\xi_1+\xi_2-\xi_3-\xi_4)\;\times(\text{占有数约束}).$$

用 $\delta$ 函数积掉 $\xi_4$，约束化为 $-\xi_1<\xi_2<0$ 与 $0<\xi_3<\xi_1+\xi_2$：

$$\frac{1}{\tau} \propto \lvert M\rvert^2\int_{-\xi_1}^{0}\!d\xi_2\int_0^{\xi_1+\xi_2}\!d\xi_3 = \lvert M\rvert^2\int_{-\xi_1}^{0}(\xi_1+\xi_2)\,d\xi_2 = \frac{\lvert M\rvert^2}{2}\,\xi_1^2.$$

**动量约束**：三重动量守恒 $\vec k_1+\vec k_2=\vec k_3+\vec k_4$ 把四体散射限制在费米面上的特定几何，只改变前因子（角平均），不引入新的能量尺度——两个独立的能量积分窗口各被 Pauli 原理压到 $\xi_1$，幂次 $\xi_1^2$ 不变。有限温度下费米面软化宽度 $k_BT$，得 $1/\tau\propto\xi_1^2+\pi^2(k_BT)^2$，即著名的 $T^2$ 电阻率项的来源。

</details>

**4.** 估算室温下金属中准粒子（电子）的寿命量级，并验证准粒子图像自洽。

<details markdown="1"><summary>点击显示答案</summary>

取典型值 $E_F = 5$ eV，$T = 300$ K，$k_BT = 1/40$ eV $= 0.025$ eV。热激发准粒子的 $\varepsilon-E_F\sim k_BT$，代入第 7 节的标度估计：

$$\frac{1}{\tau} \sim \frac{(k_BT)^2}{\hbar E_F} \;\Longrightarrow\; \tau \sim \frac{\hbar E_F}{(k_BT)^2} = \frac{(6.6\times10^{-16}\ \text{eV·s})(5\ \text{eV})}{(0.025\ \text{eV})^2} \approx 5\times10^{-12}\ \text{s}.$$

即室温下 $\tau\sim$ 几皮秒（$10^{-12}$ s 量级）。自洽性检验：

$$\hbar/\tau \sim \frac{(k_BT)^2}{E_F} \approx \frac{(0.025)^2}{5}\ \text{eV} \approx 1.3\times10^{-4}\ \text{eV} \ll k_BT = 0.025\ \text{eV},$$

能量展宽比激发能本身小约 200 倍——准粒子极其"锐利"。低温下更夸张：$T\to 4$ K 时 $\tau$ 再增 $(300/4)^2\sim 6\times10^3$ 倍，达纳秒量级。这就是低温输运实验（如 de Haas–van Alphen 振荡）能看到干净费米面的原因。

</details>

**5.** 解释 HF 理论在费米面处态密度发散（$N(E_F)\to 0$）的病根，并说明屏蔽如何治愈它。

<details markdown="1"><summary>点击显示答案</summary>

HF 交换自能（第 3 节）

$$\Sigma_x(k) = -\frac{e^2k_F}{\pi}\left[1+\frac{k_F^2-k^2}{2kk_F}\ln\left\lvert\frac{k_F+k}{k_F-k}\right\rvert\right]$$

在 $k\to k_F$ 处，对数因子 $\ln\lvert k_F-k\rvert\to-\infty$。群速度

$$\frac{d\varepsilon}{dk} = \frac{\hbar^2k}{m} + \frac{d\Sigma_x}{dk}, \qquad \frac{d\Sigma_x}{dk}\xrightarrow{k\to k_F} -\infty\ (\text{对数发散}),$$

于是 $N(E_F)\propto\lvert d\varepsilon/dk\rvert^{-1}\to 0$。

**病根定位**：发散来自交换积分

$$\Sigma_x \propto -\int d^3k'\,\frac{1}{\lvert\vec k-\vec k'\rvert^2}$$

中被积函数 $v(q)=4\pi e^2/q^2$ 在**动量转移 $q\to 0$** 处的奇异性——即实空间库仑势的长程尾巴。HF 用裸库仑势，假设电子气对外场毫无反应。

**屏蔽的治疗**：物理上，电子气对任何缓变势都会响应，把裸势换成屏蔽势

$$v(q) \to \frac{4\pi e^2}{q^2+k_{TF}^2},$$

$q=0$ 处取有限值 $4\pi e^2/k_{TF}^2$。交换积分中小 $q$ 区域不再奇异，$\ln\lvert k_F-k\rvert$ 被截断为 $\ln(k_{TF})$，$d\varepsilon/dk$ 有限，$N(E_F)$ 恢复为正常量级（再被高阶修正重整化）。一句话：**HF 的病不是算错，而是丢了屏蔽这个物理；RPA/屏蔽库仑相互作用才是正确的低能起点**。这正是 Fermi 液体理论绕开微扰论、直接以唯象参数起步的动机。

</details>

## 参考

- Ashcroft & Mermin《Solid State Physics》第 2 章（Sommerfeld 理论回顾）与第 17 章（相互作用电子气：HF、屏蔽、Fermi 液体初步）——与本章对应最直接。
- Kittel《固体物理导论》第 6 章（自由电子 Fermi 气）与第 10 章（等离激元、介电函数、EELS）。
- Fetter & Walecka《Quantum Theory of Many-Particle Systems》§3–5（凝胶模型与 HF）、§12–15（RPA、Lindhard 函数与等离激元）——推导最系统的参考书。
- Pines & Nozières《The Theory of Quantum Liquids, Vol. I: Normal Fermi Liquids》第 1–4 章——Fermi 液体与集体模式的经典专著。
- Landau 原始论文：L. D. Landau, "The Theory of a Fermi Liquid", Sov. Phys. JETP **3**, 920 (1957)。
- Wilson 视角的现代化表述：R. Shankar, "Renormalization-group approach to interacting fermions", Rev. Mod. Phys. **66**, 129 (1994)。
