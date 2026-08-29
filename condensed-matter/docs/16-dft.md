# 密度泛函理论：Hohenberg–Kohn、Kohn–Sham 与泛函阶梯

> 路线图位置：第四部分（多电子问题怎么算）· 第 16 章
> 前置知识：[第 14 章](14-exact-methods-fci-ed.md)（基组与严格解的框架）；第 6 章[相互作用电子气](06-interacting-electron-gas.md)（Hartree–Fock、均匀电子气的交换能——LDA 的原料）；[第 3 章](03-free-electron-gas.md)（费米海与态密度）；[第 4 章](04-band-theory.md)（能带——KS 能带的解读语言）。
> 学习目标：会证 Hohenberg–Kohn 定理（两条，第一条三行反证法）；理解 Kohn–Sham 构造的逻辑（借非相互作用体系复现密度）与 $E_{xc}$ 吸收了什么；认识泛函阶梯（LDA → GGA → 杂化）及其"经验试错"性质；会用第 6 章结果亲手导出 LDA 交换能；说清能隙问题（导数不连续）、自相互作用误差与强关联失灵的机理；了解固体能带计算的日常工作流（平面波赝势 + 自洽循环）。
>
> 记号约定：原子单位（同第 14 章）。$n(\vec r)$ 为电子密度，$\int n = N$；KS 量带下标 s。

---

## 1. 一句话总结

**DFT 的赌注是一次彻底的换元：基态能量不是 $3N$ 维波函数的泛函，而是 3 维密度 $n(\vec r)$ 的泛函——Hohenberg–Kohn 定理保证这个泛函存在且变分原理成立；Kohn–Sham 再造一个"非相互作用的替身"，让它复现真实密度，把全部无知装进交换相关泛函 $E_{xc}[n]$ 一项里。精确泛函无人知晓，于是五十年的历史就是一部泛函试错史（LDA → GGA → meta-GGA → 杂化，"Jacob 阶梯"），换来了 $N^3$ 的代价与惊人的平均精度——固体能带、结构、振动谱的日常计算全部姓 DFT。代价同样清楚且不因调参消失：KS 能隙系统性偏小（导数不连续性缺席）、自相互作用误差把电子抹糊、强关联体系（Mott 绝缘体）判成金属。DFT 不是"低配量子力学"，它是另一套原则上精确的框架——近似的方式从"微扰截断"换成了"泛函猜形式"。**

## 2. 换变量：HK 定理

### 2.1 第一条：密度决定一切（反证法三行）

**定理（HK1）**：外势 $v(\vec r)$（从而整个哈密顿量、基态波函数与一切基态性质）由基态密度 $n(\vec r)$ 唯一确定。

**证明**：设两个外势 $v \ne v'$（相差不止一个常数）有共同基态密度 $n$，基态波函数 $\Psi \ne \Psi'$。用对方的波函数做变分试探（严格不等，因为基态不简并时波函数不同必不能同为本征态）：

$$E_0 < \langle\Psi'\lvert H\lvert\Psi'\rangle = \langle\Psi'\lvert H'\lvert\Psi'\rangle + \int(v - v')\,n\,\text d\vec r = E_0' + \int(v - v')\,n\,\text d\vec r,$$

$$E_0' < \langle\Psi\lvert H'\lvert\Psi\rangle = E_0 + \int(v' - v)\,n\,\text d\vec r.$$

两式相加得 $E_0 + E_0' < E_0 + E_0'$，矛盾。$\blacksquare$

（简并基态需要 Levy 的约束搜索表述绕一下，结论不变。）注意定理的惊人之处：$3N$ 个变量的波函数被 3 个变量的密度**完全**编码——不是近似，是定理。当然"原理上可编码"不等于"知道怎么解码"：解码器就是 $E_{xc}[n]$，未知。

### 2.2 第二条：变分原理

**定理（HK2）**：$E_v[n] = F[n] + \int v n$（$F[n] = \langle\Psi[n]\lvert T + V_{ee}\lvert\Psi[n]\rangle$ 与外势无关）满足 $E_v[n] \ge E_0$，等号当且仅当 $n = n_0$。

于是在密度空间里做变分即得基态——**如果**知道 $F[n]$。整个 DFT 的实践史就是给 $F$ 造近似。与 HF 变分（第 6 章）的平行关系立刻可见：一样的自洽循环结构，不一样的变量（轨道 vs 密度）与不一样的近似对象（$F[n]$ 的整体 vs 单行列式限制）。

## 3. Kohn–Sham：借一个替身体系

### 3.1 构造

非相互作用的电子没有关联 woes，但**密度**是可观测量，替身完全可能复现它。Kohn–Sham（1965）引入一组轨道 $\{\varphi_i\}$，令

$$n(\vec r) = \sum_i^{\text{occ}}\lvert\varphi_i(\vec r)\rvert^2,$$

并把能量拆成（拆法本身就是定义，见自检问题 3）：

$$E[n] = T_s[n] + \int v_\text{ext}\,n\,\text d\vec r + E_H[n] + E_{xc}[n],\qquad E_H[n] = \frac12\iint\frac{n(\vec r)n(\vec r')}{\lvert\vec r - \vec r'\rvert},$$

$T_s$ 是替身的动能，$E_H$ 是熟悉的 Hartree 双重计数（第 6 章），而 $E_{xc}$ 定义为**一切剩下的**：

$$E_{xc}[n] \equiv F[n] - T_s[n] - E_H[n] = \underbrace{(T[n] - T_s[n])}_{\text{动能相关}} + \underbrace{(V_{ee}[n] - E_H[n])}_{\text{交换 + 势相关}}.$$

对 $n$ 变分给出 KS 方程——形式上就是"单电子薛定谔方程"：

$$\left(-\frac12\nabla^2 + v_\text{ext} + v_H[n] + v_{xc}[n]\right)\varphi_i = \varepsilon_i\varphi_i,\qquad v_{xc}(\vec r) = \frac{\delta E_{xc}}{\delta n(\vec r)}.$$

自洽循环与 HF 完全同构：猜密度 → 解方程 → 新密度 → 循环至收敛。

### 3.2 与 HF 的对照（一句话版放在表里）

两者都是平均场单电子方程，但：HF 的势是非局域的精确交换、完全无关联；KS 的势是局域近似 $v_{xc}$、原则上关联全含。HF 变分严格但空间小（单行列式）；KS 无变分保证（近似泛函会破坏变分界）但空间不受限。**KS 轨道不是准粒子轨道**（除了 HOMO 有严格解释，见 6.1），KS 本征值 $\varepsilon_i$ 不该直接当电离能/带隙读——但实践里当能带读常常出奇地好（第 17 章解释为什么这种"好"部分是误差相消）。第 4 章的能带图，现代的出身正是这里。

## 4. 泛函阶梯（Jacob 的梯子）

精确的 $E_{xc}[n]$ 无人知道，但有一个天然的零阶近似：**密度缓变的体系**应该接近均匀电子气——而均匀电子气我们算得动（第 6 章 HF 交换 + QMC 关联）。

### 4.1 LDA：从第 6 章直接进货

**局域密度近似**：拿均匀电子气的结果逐点填充：

$$E_{xc}^{\text{LDA}}[n] = \int n(\vec r)\,\varepsilon_{xc}^{\text{unif}}\big(n(\vec r)\big)\,\text d\vec r,$$

其中交换部分可从第 6 章的均匀气 HF 结果**一步导出**（完整推导见自检问题 2）：

$$E_x^{\text{LDA}}[n] = -\frac34\left(\frac{3}{\pi}\right)^{1/3}\int n(\vec r)^{4/3}\,\text d\vec r.$$

关联部分无解析式，来自 Ceperley–Alder 对均匀电子气的量子蒙特卡洛 + 参数化（LSDA 表示自旋分开处理）。LDA 在密度缓变的近均匀体系（简单金属）上好得超出预期——误差相消的礼物：交换低估了的部分被关联的高估抵掉大半。

### 4.2 阶梯：GGA、meta-GGA、杂化

| 台阶 | 依赖量 | 代表泛函 | 典型改进 |
|---|---|---|---|
| LDA | $n$ | VWN/PW92 | 结构好、键能高估 ~20–30% |
| GGA | $n, \lvert\nabla n\rvert$ | PBE、BLYP | 键能误差降到 ~0.3 eV 量级 |
| meta-GGA | $+\tau$（动能密度） | TPSS、SCAN | 阶梯描述更细 |
| 杂化 | 混入精确交换 | PBE0（25%）、B3LYP（20%） | 反应势垒、分子能量逼近化学精度 |

这条"Jacob 阶梯"的隐喻：从 LDA 的"均匀气地狱"爬向"精确泛函天堂"，每上一阶多要一个变量、多一批参数。**必须清醒的一点**：与 CC 的 rank 阶梯不同（那里误差随截断 rank 严格单调下降、渐近可控），泛函阶梯**不保证系统性改进**——某个 GGA 在反应能上打败某个杂化是家常便饭；泛函的进步更像药物研发（针对病症调结构），不像数学截断（逼近论）。这是 DFT 与波函数方法在方法论气质上的根本差异，也是它被戏称为"部署机器"而非"推导机器"的原因。

## 5. 固体能带的日常：工作流

现代计算材料学的一天的样子（概念流程）：

1. **建模**：原胞 + 原子位置（赝势替换芯电子，第 14 章 3.2 节）；
2. **自洽**：平面波基（$E_\text{cut} \sim$ 数百 eV）+ BZ 内 $\vec k$ 网格 → 解 KS 方程循环至密度收敛（每步的子程序：FFT、对角化、密度更新）；
3. **产出**：总能量与力（弛豫结构）、KS 本征值沿高对称路径（=第 4 章那种能带图）、态密度（第 3 章 $g(E)$ 的带版本）、声子（密度对原子位移的二阶导，第 2 章）。

**可信区**：晶格常数（误差 ~1%）、形成能与构型排序、声子谱、弹性常数——几何与能量学基本可靠。**半信半疑区**：能隙（系统性偏小，见下）、激发能、电荷分布细节。为什么固体世界归 DFT 而不是 CC？代价 $N^3$、没有指数墙（KS 方程个数随体系线性增长，每条的本征值问题用迭代法只取低能态）、平面波基的 FFT 加成——百原子胞日常、千原子可行。

## 6. 诚实账本：系统性失灵

### 6.1 能隙问题

KS 能隙

$$E_g^{s} = \varepsilon_{N+1} - \varepsilon_N$$

系统性偏小：Si 的实验能隙 1.17 eV，LDA 给 ~0.5 eV；Ge 被算成金属。**这不是泛函不够好，是概念性的**：精确泛函下 KS 能隙也不等于真能隙（自检问题 4）——基态能量 $E(N)$ 作为粒子数（分数）的函数是分段线性的，斜率在整数处跳变（**导数不连续性** $\Delta_{xc}$）：

$$E_g^{\text{true}} = E_g^{s}\big\vert_{\text{精确}} + \Delta_{xc},$$

近似泛函普遍丢失 $\Delta_{xc}$。要激发态，得离开"基态 DFT"的地基——第 17 章的 GW。

### 6.2 自相互作用误差

单电子体系（H 原子、拉长的 H₂⁺）里，精确理论要求 $E_x$ 严格抵消 $E_H$ 的自能。LDA/GGA 的局域近似做不到：H 原子上 $E_H = \tfrac{5}{16}$ Ha，而 $E_x^{\text{LDA}}$ 只还得上 ~0.21 Ha——**净剩 ~0.1 Ha ≈ 2.7 eV 的虚假自排斥**（完整计算见自检问题 5）。后果是系统性的：电子被"抹糊"、过度离域、电荷转移倾向被夸大、分数电荷的假稳定态。杂化泛函混入精确交换正是最直接的解毒剂。

### 6.3 强关联：DFT 的 Mott 车祸

第 13 章的主角——过渡金属氧化物 NiO、CoO：实验是良好的 Mott 绝缘体，能带论（独立电子）预言金属；**DFT（LDA/GGA）同样预言金属**——因为 KS 图像仍是"每个电子独立占领轨道"，Mott 能隙是关联劈裂（Hubbard U），单电子替身天生画不出来。实用补丁 DFT+U：在 d/f 子空间手工加上占位排斥 $U$，把能隙砸出来——介于第一性原理与唯象之间。彻底的修法是第 17 章的 DMFT。

### 6.4 色散力

局域/半局域泛函看不见 $-C_6/R^6$ 的长程范德华尾巴（密度不交叠就没有作用），分子晶体、层状材料（石墨烯堆叠）的结合能系统性缺失——需要非局域修正（vdW-DF、DFT-D 系列经验色散校正）。

**账本的读法**：DFT 的错误不是随机的，而是结构性的（能隙偏小、离域偏高、强关联失效），且**加交换精确度不解决**——因为病根在关联部分的近似方式。知道错误长什么样，与知道答案同样重要。

## 小结

- HK1（密度 → 外势 → 一切）+ HK2（变分）= 原则上严格的密度理论；全部实践困难收进 $E_{xc}[n]$。
- KS：非相互作用替身复现密度；$E_{xc} = (T - T_s) + (V_{ee} - E_H)$，动能的相关部分也归它管（常被遗忘的一半）。
- 阶梯：LDA（第 6 章均匀气直接进货）→ GGA → meta-GGA → 杂化；**精度进步靠试错，不保证系统性**——与 CC 阶梯的方法论对照是本部分的主线之一。
- 工作流：平面波 + 赝势 + 自洽 → 能带/结构/声子；可信区在能量学与几何。
- 失灵清单：能隙（导数不连续性 $\Delta_{xc}$，概念性）、自相互作用（H 原子残余 ~2.7 eV）、强关联（Mott → 金属）、色散。
- HF 与 KS 的对照表：

| | HF | KS-DFT |
|---|---|---|
| 变量 | 轨道（非局域交换） | 密度（局域 $v_{xc}$） |
| 关联 | 无 | 全部塞进 $E_{xc}$（近似） |
| 代价 | $N^4$ | $N^3$ |
| 能隙 | 高估（无屏蔽） | 低估（无 $\Delta_{xc}$） |
| 变分界 | 严格 | 近似泛函下无 |

## 自检问题

**1.** 完整证明 HK1 定理（含"两外势不同"条件的必要性），并解释为什么简并基态需要 Levy 约束搜索表述。

<details markdown="1"><summary>点击显示答案</summary>

**证明**：设 $v \ne v' + C$，基态分别为 $(\Psi, E_0)$、$(\Psi', E_0')$，假设 $n_\Psi = n_{\Psi'} \equiv n$。用 $\Psi'$ 作为 $H = T + V_{ee} + \int v\,\hat n$ 的变分试探态。若 $\Psi'$ 不是 $H$ 的基态，则严格不等：

$$E_0 < \langle\Psi'\lvert H\lvert\Psi'\rangle = \underbrace{\langle\Psi'\lvert T + V_{ee}\lvert\Psi'\rangle}_{F\text{，仅依赖 }\Psi'} + \int v\,n = E_0' - \int v'\,n + \int v\,n = E_0' + \int(v - v')\,n.$$

对称地用 $\Psi$ 试探 $H'$：

$$E_0' < E_0 + \int(v' - v)\,n.$$

相加：$E_0 + E_0' < E_0 + E_0'$，矛盾。故共同密度不可能——$v$ 由 $n$ 单一决定，随之 $H$、$\Psi$（作为 $H$ 的基态）及一切基态可观测量都被 $n$ 决定。$\blacksquare$

**条件的必要性**：若 $v' = v + C$，两哈密顿量只差常数，波函数相同、密度相同——"外势决定一切"必须模去常数，这正是表述里 $v \ne v' + C$ 的含义。

**简并基态的漏洞**：反证法里"$\Psi'$ 不是 $H$ 的基态 ⇒ 严格不等"一步失效——$\Psi'$ 完全可能同时是两个哈密顿量的基态（不同外势共享简并基态波函数的构造存在）。**Levy 约束搜索**绕过：定义

$$F[n] = \min_{\Psi\to n}\langle\Psi\lvert T + V_{ee}\lvert\Psi\rangle$$

（在所有产生密度 $n$ 的反对称波函数中取最小），$E_0 = \min_n\big[F[n] + \int vn\big]$ 对简并与否一律成立——HK 定理的功能（密度足够）被保留，证明绕开波函数唯一性。这个表述还顺便暴露了 $F[n]$ 的真实身份：**波函数空间的约束最小化**——近似 $F$ 的难度正在于此。

</details>

**2.** 从第 6 章的均匀电子气 HF 结果导出 LDA 交换能 $E_x^{\text{LDA}}[n] = -\tfrac34(3/\pi)^{1/3}\int n^{4/3}$，并算出每电子交换能 $\varepsilon_x = -\tfrac34(3/\pi)^{1/3}n^{1/3}$ 的数值系数。

<details markdown="1"><summary>点击显示答案</summary>

**原料**（第 6 章 3 节）：均匀电子气 HF 给出每电子平均交换能 $\varepsilon_x^{\text{unif}} = -\dfrac{3}{4\pi}e^2 k_F$（高斯单位；原子单位即 $-\tfrac{3k_F}{4\pi}$），其中 $k_F = (3\pi^2 n)^{1/3}$。

**LDA 操作**：把非均匀体系每个体积元当作密度为局域值 $n(\vec r)$ 的均匀气：

$$E_x^{\text{LDA}} = \int n(\vec r)\,\varepsilon_x^{\text{unif}}\big(n(\vec r)\big)\,\text d\vec r = -\frac{3}{4\pi}\int n\,(3\pi^2 n)^{1/3}\,\text d\vec r = -\frac34\left(\frac{3}{\pi}\right)^{1/3}\int n^{4/3}\,\text d\vec r,$$

最后一步用了 $\tfrac{1}{4\pi}\,(3\pi^2)^{1/3} = \tfrac{3^{1/3}}{4}\pi^{-1/3}\cdot\tfrac13\cdot 3 = \tfrac13\left(\tfrac3\pi\right)^{1/3}$，与 $\tfrac34\cdot\tfrac13 = \tfrac14$ 合并整理（核对：$\tfrac{1}{4\pi}(3\pi^2)^{1/3} = \tfrac{(3)^{1/3}}{4\pi^{1/3}} = \tfrac14(3/\pi)^{1/3}$ ✓）。

**数值**：$(3/\pi)^{1/3} = 0.985$，故 $\varepsilon_x \approx -0.739\,n^{1/3}$ Ha（$n$ 单位 Bohr⁻³）。金属密度 $n \sim 10^{-2}$–$10^{-3}$ Bohr⁻³ 对应 $\lvert\varepsilon_x\rvert \sim$ 数 eV——与费米能同量级（当然：都由 $k_F$ 决定，第 3 章）。

**顺带的洞察**：$n^{4/3}$ 标度意味着 $v_x \propto n^{1/3}$——交换势随密度只开三次方根，缓慢、有界；对比 Hartree 势在密度局域堆积时线性飙升。这个"温和的非线性"是 LDA 在固体里好用的深层原因之一；也是第 7 章 07s 里 Stoner 参数 $I$ 温和行为在 LDA 里的影子。

</details>

**3.** 从 $E[n] = T_s[n] + \int v_\text{ext}n + E_H[n] + E_{xc}[n]$ 出发对 $n$ 变分导出 KS 方程；说明 $E_{xc}$ 里动能部分 $(T - T_s)$ 的存在为什么常被低估它的人忽略、以及它有多大。

<details markdown="1"><summary>点击显示答案</summary>

**变分**：以轨道为独立变量（$n = \sum^{\text{occ}}\lvert\varphi_i\rvert^2$，约束正交归一，拉氏乘子 $\varepsilon_i$）：

$$\delta\left[E - \sum_i\varepsilon_i(\langle\varphi_i\lvert\varphi_i\rangle - 1)\right] = 0\;\Longrightarrow\;\left(-\frac12\nabla^2 + v_\text{ext} + v_H + v_{xc}\right)\varphi_i = \varepsilon_i\varphi_i,$$

其中 $v_H(\vec r) = \int n(\vec r')/\lvert\vec r - \vec r'\rvert\,\text d\vec r'$（$E_H$ 的变分没有 ½——**双重计数的一半正是抵消"每个电子都感到全密度包括自己"的自能的那一半**，与 HF 推导同款对消），$v_{xc} = \delta E_{xc}/\delta n$。替身非相互作用、泡利填充——单电子方程组成立。

**动能相关 $(T - T_s)$**：把相互作用体系的动能硬拆成"替身轨道动能 $T_s$"与余项。两项各自都很大（~数十 Ha），余项 $T - T_s > 0$ 且不小——He 原子上约 $+0.035$ Ha，与 $(V_{ee} - E_H - E_x)$ 同量级。**常被忽略的原因**：直觉把 $E_{xc}$ 当成"修正一点势能"，实际它一半是动能性质——库仑相关让电子互相绕开，绕路就是额外动能。这也解释了为什么纯拟合库仑形式的泛函原型会系统性跑偏：**$E_{xc}$ 的工作描述里写着"替你把动能的相关部分也补上"**。

</details>

**4.** 证明精确泛函下 $-\varepsilon_\text{HOMO} = I$（第一电离能），并由此导出真能隙 = 精确 KS 能隙 + 导数不连续性 $\Delta_{xc}$；解释为什么近似泛函普遍丢掉 $\Delta_{xc}$。

<details markdown="1"><summary>点击显示答案</summary>

**分段线性**：对分数粒子数 $N + \delta$（$0\le\delta\le1$），精确基态是 $N$ 电子态与 $N+1$ 电子态的密度凸组合（系综 DFT：能量在整数之间是线性连接，弯曲会违反凸性——Janak 定理加凸性论证）：

$$E(N + \delta) = (1-\delta)E(N) + \delta E(N+1).$$

**HOMO**：$\mu = \partial E/\partial N = E(N) - E(N-1) = I$ 在 $(N-1, N)$ 区间上；另一方面 KS 轨道的占据数连续可调（Janak：$\partial E/\partial n_i = \varepsilon_i$），最高占据轨道在区间内被占满，故

$$-\varepsilon_\text{HOMO} = I\qquad(\text{精确泛函}).$$

（这是 KS 本征值唯一的严格解读；LUMO 没有对应荣誉。）

**能隙**：$I = E(N-1) - E(N)$，$A = E(N) - E(N+1)$（电子亲合能），真能隙 $E_g = I - A$。而 KS 能隙是斜率的差：

$$E_g^s = \varepsilon_{N+1} - \varepsilon_N = \mu^+(N) - \mu^-(N),$$

其中 $\mu^\pm$ 是 $E(N)$ 在整数两侧的左/右导数。分段线性的导数在整数处**跳变**，跳变量即导数不连续性

$$\Delta_{xc} = \mu^+ - \mu^- \big\vert_{\text{斜率跳跃中 }v_{xc}\text{ 的贡献}},\qquad E_g = E_g^s + \Delta_{xc}.$$

**近似泛函为什么丢**：LDA/GGA 是 $n(\vec r)$ 的光滑泛函，$E(N)$ 对 $N$ 光滑可微——分段线性连同它的斜率跳变一起被抹平（曲线被"圆过弯"），$\Delta_{xc} \to 0$。于是 KS 能隙系统性缺一块（Si：缺 ~0.7 eV）。这不是参数问题而是**函数形式问题**：要恢复跳变，泛函必须对整数粒子数有奇性（杂化部分恢复、精确交换完全恢复）。

</details>

**5.** 自相互作用的定量账：对 H 原子基态密度 $n = \pi^{-1}e^{-2r}$，计算 $E_H[n]$ 与 $E_x^{\text{LDA}}[n]$，证明两者不抵消、残余 $\approx 0.1$ Ha（~2.7 eV），并说明这个误差如何在拉伸的 H₂⁺ 与电荷转移问题上显形。

<details markdown="1"><summary>点击显示答案</summary>

**Hartree 自能**：$E_H = \tfrac12\iint n(1)n(2)/r_{12}$。$\iint$ 正是氢 1s 的库仑积分 $\tfrac12\times\tfrac58 = \tfrac{5}{16}$ Ha = 0.3125 Ha。

**LDA 交换**：

$$E_x^{\text{LDA}} = -\frac34\left(\frac{3}{\pi}\right)^{1/3}\int n^{4/3}\,\text d\vec r,\qquad n^{4/3} = \pi^{-4/3}e^{-8r/3},$$

$$\int n^{4/3}\,\text d\vec r = \frac{4\pi}{\pi^{4/3}}\int_0^\infty r^2 e^{-8r/3}\,\text dr = \frac{4\pi}{\pi^{4/3}}\cdot\frac{2}{(8/3)^3} = \frac{4\pi\times54}{\pi^{4/3}\times512} \approx 0.288,$$

$$E_x^{\text{LDA}} \approx -0.739\times0.288 \approx -0.213\ \text{Ha}.$$

**残余**：$E_H + E_x^{\text{LDA}} = 0.3125 - 0.213 \approx +0.10$ Ha ≈ 2.7 eV——单电子体系应严格为零的"电子对自己的排斥"只剩九成抵消不完。（关联泛函再补 ~ −0.02 Ha，救不回量级。）精确要求 $E_x[n_1] = -E_H[n_1]$ 对任何单电子密度成立——局域近似在原理上就做不到：它连"这里只有一个电子"都看不见。

**显形现场**：(i) **H₂⁺ / 拉伸的 H₂⁺**：自能未除净，电子在两核间被虚假地"摊开"反而受益，离域化能错、解离曲线错误；(ii) **电荷转移**：带分数电荷的"原子"因凸性被破坏而假性稳定，异核分子被算成不真实的离子性；(iii) **反应势垒**：过渡态电荷更离域，误差偏向低估势垒。解毒剂按彻底程度：自相互作用修正（SIC）、杂化泛函（精确交换自带正确自能抵消）、纯精确交换（OEP）。

</details>

## 参考

- Parr & Yang《Density-Functional Theory of Atoms and Molecules》第 3 章（HK 定理与 Levy 约束搜索）、第 7 章（KS 方程）；第 8–10 章（近似泛函）。
- Martin《Electronic Structure》第 3 章（HK/KS）与平面波赝势方法章节；同书 GW 与响应函数章节衔接第 17 章。
- Sholl & Steckel《DFT: A Practical Introduction》：工作流与"该信什么"的实用主义指南。
- Koch & Holthausen《A Chemist's Guide to Density Functional Theory》：失灵清单与泛函试错史。
- Perdew, in "Density Functional Methods in Physics"（1985，Jacob 阶梯与导数不连续性的原始讨论）；Ceperley & Alder, Phys. Rev. Lett. 45, 566 (1980)（LDA 关联的 QMC 数据源）。
