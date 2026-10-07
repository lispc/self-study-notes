# 补充材料：Fermi–Dirac 分布从哪来——对称化公设、系综假设与逻辑地基

> 路线图位置：量子力学书 · 第四部分（多体语言）· 第 09 篇（[二次量子化](09-second-quantization.md)）的补充材料（第 09s 篇），建议在第 10 篇（[线性响应与 Kubo 公式](10-linear-response-kubo.md)）之前读——那里把 Boltzmann 权重 $\rho_0=e^{-\beta H_0}/Z$ 作为定义直接取用，本篇交代它的来历。
> 前置知识：第 09 篇（占据数表象、产生湮灭算符、Fock 空间）；[第 05s 篇](05s-identical-particles.md)（全同粒子与对称化公设——本篇第 3 节是它的延伸）；[第 03 篇](03-formalism-hilbert-dirac.md)第 8 节（密度矩阵与约化描述）。
> 学习目标：说清 Fermi–Dirac 分布的"成分表"——能谱来自薛定谔方程、$n_i\in\{0,1\}$ 来自对称化公设、Boltzmann 权重来自平衡态系综假设，后两者都不是薛定谔方程的逻辑推论；会用巨正则系综一行推出 FD 分布（顺手得到 BE 分布），并用微正则组合计数独立复核；知道相互作用如何把占据数的 0/1 阶跃软化成幅度 $Z<1$ 的跃变；知道"孤立量子系统为什么热化"至今是开放问题（ETH、典型性、多体局域化）。
>
> 记号约定：本篇取自然单位 $\hbar=1$（首次出现特此说明），保留 $k_B$ 显式，$\beta\equiv 1/(k_BT)$。凝聚态一侧的应用见凝聚态书[第 3 章](../../condensed-matter/docs/03-free-electron-gas.md)（费米海）——那里"直接取用"的 Fermi–Dirac 分布，推导在本篇兑现。

---

## 1. 一句话总结

**Fermi–Dirac 分布 $f(\varepsilon)=1/(e^{\beta(\varepsilon-\mu)}+1)$ 不是薛定谔方程的推论，而是三块独立输入的合取：薛定谔方程给出能谱 $\{\varepsilon_i\}$ 与幺正演化；对称化公设（相对论根基是 Pauli 的自旋-统计定理）把每个轨道的占据数限制在 $n_i\in\{0,1\}$；平衡态系综假设——温度是统计概念，不存在于单条薛定谔方程之内——给出权重 $e^{-\beta(\varepsilon_i-\mu)}$。三者齐备后一行代数即得分布，分母里的 $+1$ 是 Pauli 原理的代数指纹（玻色子是 $-1$）；拿掉任何一块都推不出来——这正是"量子统计"作为独立学科存在的原因。**

## 2. 薛定谔方程给什么、不给什么

先清点库存。薛定谔方程（单粒子的，或多体的 $i\partial_t\Psi=\hat H\Psi$）只做两件事：

- **给能谱**：$\hat H\lvert n\rangle=E_n\lvert n\rangle$ 决定允许的能量；
- **给动力学**：态按 $\lvert\psi(t)\rangle=e^{-i\hat Ht}\lvert\psi(0)\rangle$ 幺正演化。

但有两样东西它原则上给不出。

**第一，温度与混态。** 幺正演化保持纯度：纯态永远演化成纯态；von Neumann 熵 $S=-\mathrm{Tr}(\rho\ln\rho)$ 只依赖密度矩阵的本征值谱，而幺正共轭保持谱（完整证明见自检问题 4）。热平衡态却是混态 $\rho=e^{-\beta\hat H}/Z$——从任何纯初态出发，单靠 $\hat H$ 的演化**永远到不了**它。"温度""熵""平衡"这些词在单条薛定谔方程里根本没有定义。

**第二，统计。** 单粒子薛定谔方程对"两个电子能否占据同一个态"完全无话可说——它连"粒子不可分辨"都表达不了：给两个电子贴上编号本身就是多余的自由度（[第 05s 篇](05s-identical-particles.md)第 2 节）。Fermi 与 Bose 的分野藏在哪里，方程本身保持沉默。

所以"从薛定谔方程推出 Fermi–Dirac 分布"在逻辑上不可能，必须补两块基石。

## 3. 基石一：对称化公设——从公设到代数

第一块基石在[第 05s 篇](05s-identical-particles.md)已经立好：全同粒子的物理态空间不是整个张量积空间，而是其全对称（玻色子）或全反对称（费米子）子空间。这是**独立于运动方程的公设**——薛定谔方程只给出交换简并（置换得到的所有态能量相同），但挑不出该取哪个组合。

[第 09 篇](09-second-quantization.md)第 4 节把这条公设转写成代数：费米子算符满足反对易关系 $\{c_\alpha,c_\beta^\dagger\}=\delta_{\alpha\beta}$，直接推论是 $(c_\alpha^\dagger)^2=0$ 与 $\hat n_\alpha^2=\hat n_\alpha$——**每个轨道的占据数只能是 0 或 1**。Pauli 不相容原理从"外加禁令"变成代数恒等式。这是本篇推导所需的全部量子统计输入。

为什么半整数自旋必须反对易？非相对论量子力学只把它当公设与实验事实接受；真正的证明需要相对论性量子场论——**自旋-统计定理**（Pauli, 1940）：在洛伦兹不变性、局域性（类空间隔的可观测量对易）、因果性与正能量谱的条件下，整数自旋场必须用对易子量子化、半整数自旋场必须用反对易子量子化，否则因果性被破坏。这是费米统计最深的理论根基，属 QFT 书第 4–5 阶段的主题（笔记待写）。

## 4. 基石二：平衡态系综——温度是统计概念

第二块基石回答"体系处于哪个态"。温度不是动力学量，而是**系综**的性质：必须声明体系与温度为 $T$、化学势为 $\mu$ 的热库达到平衡（可交换能量与粒子），或等价地直接假设平衡密度算符的巨正则形式：

$$\hat\rho = \frac{e^{-\beta(\hat H-\mu\hat N)}}{\Xi}, \qquad \Xi = \mathrm{Tr}\,e^{-\beta(\hat H-\mu\hat N)},$$

化学势 $\mu$ 由平均粒子数方程固定（见第 5 节）。这个假设有几条独立的辩护路线：

- **微正则 + 热库**：把"体系 + 热库"当作等能量壳层上等概率的孤立整体，对热库自由度求迹，体系呈巨正则分布——统计力学教科书的标准论证；
- **最大熵**：在固定 $\langle\hat H\rangle$、$\langle\hat N\rangle$ 下最大化 $S=-\mathrm{Tr}(\rho\ln\rho)$，Lagrange 乘子即 $\beta$ 与 $-\beta\mu$——Jaynes 的信息论读法；
- **现代路线**：正则典型性（单个随机多体纯态的约化密度矩阵就近似正则）与本征态热化假说（ETH），试图绕开"系综"概念、直接从大系统的量子力学得到热平衡——第 7 节展开。

无论走哪条路线，结论都一样：**系综是统计假设，不是动力学定理**——第 2 节已经证明它不可能从幺正演化导出。

## 5. 推导：一行代数

设无相互作用（或已平均场化）的费米气体，单粒子能级 $\{\varepsilon_i\}$ 由薛定谔方程给出。二次量子化下

$$\hat H-\mu\hat N = \sum_i(\varepsilon_i-\mu)\,\hat n_i, \qquad n_i\in\{0,1\},$$

不同轨道彼此独立，巨配分函数对轨道因子化——每个轨道只有两个 Fock 态：

$$\Xi = \prod_i\Big(\sum_{n_i=0,1}e^{-\beta(\varepsilon_i-\mu)n_i}\Big) = \prod_i\Big(1+e^{-\beta(\varepsilon_i-\mu)}\Big),$$

于是轨道 $i$ 的平均占据数（分子上只有 $n_i=1$ 一项）：

$$\langle\hat n_i\rangle = \frac{0\cdot 1+1\cdot e^{-\beta(\varepsilon_i-\mu)}}{1+e^{-\beta(\varepsilon_i-\mu)}} = \frac{1}{e^{\beta(\varepsilon_i-\mu)}+1}. \qquad\blacksquare$$

这就是 Fermi–Dirac 分布。同样的三行换成玻色子（$n_i$ 不受限，几何级数求和）给出 Bose–Einstein 分布 $1/(e^{\beta(\varepsilon-\mu)}-1)$（自检问题 2）——**分母里的 $\pm1$ 就是两种统计在代数上的全部差别**。

$\mu$ 不是自由参数：它由 $\sum_i f(\varepsilon_i)=N$ 反解。$T\to0$ 时 $f$ 退化为阶跃 $\theta(\mu-\varepsilon)$，$\mu$ 钉死在费米能；有限温度的移动（$\sim(T/T_F)^2$）与 Sommerfeld 展开的账见凝聚态书[第 3 章](../../condensed-matter/docs/03-free-electron-gas.md) §3.3、§4.1。

**独立复核：微正则组合计数。** 不引入系综，直接数微观状态：把 $n_i$ 个不可分辨、遵守不相容原理的粒子放进简并度 $g_i$ 的能级，放法有 $\binom{g_i}{n_i}$ 种，总微观状态数 $W=\prod_i\binom{g_i}{n_i}$；在固定 $N=\sum_in_i$ 与 $E=\sum_in_i\varepsilon_i$ 下最大化 $\ln W$（Stirling 近似 + Lagrange 乘子），得到同一个分布——分母的 $+1$ 直接来自组合数 $\binom{g_i}{n_i}$ 里的"空位记账"（玻色子来自 $\binom{n_i+g_i-1}{n_i}$，给 $-1$）。完整推导留作自检问题 3。两条路线（系综与计数）收敛到同一公式，是这条公理链可靠性的内部检查。

## 6. 相互作用修正：阶跃软化成 $Z$

必须说清 Fermi–Dirac 分布的**适用边界**：它严格只对无相互作用体系（或二次型平均场）成立——第 5 节的因子化 $\Xi=\prod_i\Xi_i$ 要求轨道彼此独立。真实金属里库仑相互作用始终开着，严格基态的动量分布

$$n(\vec k) = \langle\mathrm{GS}\rvert\,c_{\vec k}^\dagger c_{\vec k}\,\lvert\mathrm{GS}\rangle$$

不再是 0/1 阶跃：$k\gt k_F$ 的态有了部分占据（拖尾），$k\lt k_F$ 的态被部分掏空。Fermi 液体理论（凝聚态书[第 6 章](../../condensed-matter/docs/06-interacting-electron-gas.md) §7–8）给出救赎：只要相互作用绝热开启且不触发相变，费米面附近的激发仍是**准粒子**，动量分布在费米面上保留一个跃变，只是幅度从 1 降为**准粒子权重 $Z\lt 1$**（Migdal：$n(k_F^-)-n(k_F^+)=Z$）——其余 $1-Z$ 的谱权重摊进非相干背景。$Z$ 度量"电子里还剩多少成分像自由电子"，ARPES 直接测它（[06s](../../condensed-matter/docs/06s-fermi-liquid-toolbox.md) §6 的体检表）。跃变的**位置**则完全不动：Luttinger 定理把费米面包围的体积钉死在电子密度上（[06s](../../condensed-matter/docs/06s-fermi-liquid-toolbox.md) §5）。

越出 Fermi 液体的标本：一维相互作用电子气（[20s](../../condensed-matter/docs/20s-luttinger-liquid.md)）没有准粒子极点，$n(\vec k)$ 在 $k_F$ 处只剩幂律奇性，阶跃彻底消失。所以金属"看起来像自由电子气"，靠的不是 Fermi–Dirac 分布的字面成立，而是绝热连续 + $Z>0$。

## 7. 温度从何而来：开放问题

回到第 2 节埋下的刺：幺正演化不产生混态，那么**孤立量子系统为什么仍然热化**？这不是本篇能回答的问题——它是活跃的研究前沿，但值得知道路标：

- **ETH（本征态热化假说）**：对非可积（"量子混沌"）多体系统，猜想每个能量本征态对少体可观测量而言"看起来就是热的"：$\langle n\rvert\hat A\lvert n\rangle\approx$ 以 $E_n$ 为温度的热平均值。若成立，任何弱非平衡初态在幺正演化后，**局域地**与热平衡不可区分——全局仍是纯态，信息被藏进不可观的多体关联与纠缠中（与[第 03 篇](03-formalism-hilbert-dirac.md) §8 的约化密度矩阵一脉相承）。
- **典型性**：高维 Hilbert 空间中 Haar 随机的纯态，其小子系统的约化态以压倒性概率接近正则分布——"热"不是特殊初态的性质，而是高维几何的通性（Goldstein–Lebowitz–Tumulka–Zanghì；Popescu–Short–Winter）。
- **反例与边界**：多体局域化（MBL，强无序孤立系统）不热化，可观测量长期保留初态记忆——"热化定理"的适用边界本身就是研究对象。

对实用而言（本书与凝聚态全书），巨正则假设的经验正确性是压倒性的；但承认它的公设地位，比假装它能被推导出来更诚实。

## 小结

Fermi–Dirac 分布的成分表：

| 成分 | 提供什么 | 逻辑地位 |
|---|---|---|
| 薛定谔方程 | 能谱 $\{\varepsilon_i\}$、幺正演化 | 动力学：必要但不充分 |
| 对称化公设 | $n_i\in\{0,1\}$（Pauli 不相容） | 独立公设；相对论根基 = 自旋-统计定理（QFT） |
| 平衡态系综假设 | 权重 $e^{-\beta(\varepsilon_i-\mu)}$、温度与化学势 | 统计假设：微正则/最大熵/典型性多路线辩护 |

- 巨正则推导一行：$\Xi=\prod_i(1+e^{-\beta(\varepsilon_i-\mu)})$，故 $f=1/(e^{\beta(\varepsilon-\mu)}+1)$；玻色版分母为 $-1$；占据数 $\ll1$ 时两家汇合于 Maxwell–Boltzmann。
- 微正则组合计数（$W=\prod_i\binom{g_i}{n_i}$ + Stirling）独立复核同一公式，$\pm1$ 有明确的组合学出处。
- 相互作用把 0/1 阶跃软化成幅度 $Z$ 的跃变（Fermi 液体），位置被 Luttinger 定理钉死；一维连阶跃都没有。
- "温度从幺正演化里长不出来"是被证明的；"真实系统为什么仍然热化"（ETH、典型性、MBL）是活的前沿。

## 自检问题

**1.** 从巨正则密度算符出发完整推导 Fermi–Dirac 分布：写出巨配分函数的因子化、平均占据数的计算，并说明化学势如何确定。

<details markdown="1"><summary>点击显示答案</summary>

在占据数表象中 $\hat H-\mu\hat N=\sum_i(\varepsilon_i-\mu)\hat n_i$ 已经对角，多体态由构型 $\{n_i\}$（$n_i\in\{0,1\}$）标记。巨配分函数

$$\Xi = \sum_{\{n_i\}}e^{-\beta\sum_i(\varepsilon_i-\mu)n_i} = \prod_i\sum_{n_i=0,1}e^{-\beta(\varepsilon_i-\mu)n_i} = \prod_i\Big(1+e^{-\beta(\varepsilon_i-\mu)}\Big),$$

关键一步是"对构型求和 = 对逐轨道因子求积"——独立性来自哈密顿量的二次型结构（无相互作用）。

平均占据数直接数：分子只允许 $n_i=1$ 的构型，

$$\langle\hat n_i\rangle = \frac{1}{\Xi}\,e^{-\beta(\varepsilon_i-\mu)}\prod_{j\neq i}\Big(1+e^{-\beta(\varepsilon_j-\mu)}\Big) = \frac{e^{-\beta(\varepsilon_i-\mu)}}{1+e^{-\beta(\varepsilon_i-\mu)}} = \frac{1}{e^{\beta(\varepsilon_i-\mu)}+1}.$$

等价地 $\langle\hat n_i\rangle = -\frac{1}{\beta}\frac{\partial\ln\Xi}{\partial\varepsilon_i}$（热力学算法定理），代入 $\ln\Xi=\sum_i\ln(1+e^{-\beta(\varepsilon_i-\mu)})$ 逐字验证同一结果。

化学势由粒子数守恒反解：$\sum_i f(\varepsilon_i;\mu,T)=N$ 是 $\mu(T)$ 的隐式方程。$T\to0$ 时 $f\to\theta(\mu-\varepsilon)$，方程退化为"填满 $N$ 个最低轨道"，即 $\mu(0)=E_F$；有限 $T$ 的修正用 Sommerfeld 展开，$\mu(T)=E_F\big[1-\frac{\pi^2}{12}(T/T_F)^2+\cdots\big]$（凝聚态书[第 3 章](../../condensed-matter/docs/03-free-electron-gas.md)自检问题 2）。

</details>

**2.** 用同一套巨正则机器推导 Bose–Einstein 分布；指出两条推导中唯一的代数分歧点；并证明：当每个轨道的平均占据数远小于 1 时两种分布都退化为 Maxwell–Boltzmann 分布，然后用费米温度论证金属电子气在任何温度下都达不到这个经典极限。

<details markdown="1"><summary>点击显示答案</summary>

玻色子每轨道占据数不受限：$n_i\in\{0,1,2,\cdots\}$。单轨道因子是几何级数

$$\Xi_i = \sum_{n=0}^{\infty}e^{-\beta(\varepsilon_i-\mu)n} = \frac{1}{1-e^{-\beta(\varepsilon_i-\mu)}},$$

（收敛要求 $\mu<\min_i\varepsilon_i$）。于是

$$\langle\hat n_i\rangle = -\frac{1}{\beta}\frac{\partial\ln\Xi_i}{\partial\varepsilon_i} = \frac{e^{-\beta(\varepsilon_i-\mu)}}{1-e^{-\beta(\varepsilon_i-\mu)}} = \frac{1}{e^{\beta(\varepsilon_i-\mu)}-1}.$$

**唯一的代数分歧点是占据数的取值集合**：$\{0,1\}$ 对 $\{0,1,2,\cdots\}$——也就是 $(c^\dagger)^2=0$（反对易）对 $[a,a^\dagger]=1$（对易）。除此之外两步推导逐行相同。

**经典极限**：若对所有相关轨道 $e^{\beta(\varepsilon-\mu)}\gg1$（等价于 $\langle n\rangle\ll1$，轨道几乎总是空着），则分母里的 $\pm1$ 相对 $e^{\beta(\varepsilon-\mu)}$ 可忽略，两种分布汇合为

$$f(\varepsilon)\approx e^{-\beta(\varepsilon-\mu)} = e^{\beta\mu}\,e^{-\varepsilon/k_BT},$$

即 Maxwell–Boltzmann 分布：量子统计的 $\pm1$ 只在占据数 $O(1)$ 时显形；稀释极限下粒子几乎从不抢同一个轨道，不可分辨性失去后果。

**金属到不了这个极限**：简并条件恰恰相反——$\mu\approx E_F\gt0$ 且 $T\ll T_F$，对 $\varepsilon\lt E_F$ 的轨道 $e^{\beta(\varepsilon-\mu)}\sim e^{-E_F/k_BT}\sim e^{-T_F/T}$，室温下 $T_F/T\sim40$，即 $e^{-40}\sim10^{-17}\ll1$：占据数钉死在 $\approx1$，与"轨道几乎总空着"的经典条件背道而驰。$T_F\sim10^4$–$10^5$ K 高于一切熔点，这个不等式在金属存在的全部温区内不可能翻转——Drude 灾难的统计学根源正在于此。经典极限属于相反的一角：高温稀薄气体（$n\lambda_{\rm dB}^3\ll1$），如热等离子体中的电子。

</details>

**3.** 用微正则组合计数独立推导 Fermi–Dirac 分布：设能级 $i$ 的简并度为 $g_i$、占据 $n_i$ 个粒子，写出微观状态数 $W$，用 Stirling 近似与 Lagrange 乘子（固定 $N$ 与 $E$）导出 $n_i/g_i=1/(e^{\alpha+\beta\varepsilon_i}+1)$，并指出分母中 $+1$ 的组合学出处。

<details markdown="1"><summary>点击显示答案</summary>

费米子不可分辨且每个单粒子态至多占一个：能级 $i$ 的 $g_i$ 个态里选 $n_i$ 个占据，放法有 $\binom{g_i}{n_i}$ 种，故

$$W = \prod_i\binom{g_i}{n_i} = \prod_i\frac{g_i!}{n_i!\,(g_i-n_i)!}.$$

Stirling 近似（$\ln m!\approx m\ln m-m$，线性项恰相消）：

$$\ln W \approx \sum_i\Big[g_i\ln g_i - n_i\ln n_i - (g_i-n_i)\ln(g_i-n_i)\Big].$$

在约束 $\sum_in_i=N$、$\sum_in_i\varepsilon_i=E$ 下变分（Lagrange 乘子 $\alpha,\beta$）：

$$\frac{\partial}{\partial n_i}\big[\ln W-\alpha N-\beta E\big] = \ln\frac{g_i-n_i}{n_i}-\alpha-\beta\varepsilon_i = 0,$$

解出

$$\frac{g_i-n_i}{n_i} = e^{\alpha+\beta\varepsilon_i} \qquad\Longrightarrow\qquad \frac{n_i}{g_i} = \frac{1}{e^{\alpha+\beta\varepsilon_i}+1},$$

与巨正则结果同一形式（$\beta=1/k_BT$、$\alpha=-\beta\mu$ 由热力学关系 $\partial S/\partial E=1/T$ 等固定）。

**$+1$ 的出处**：来自组合数 $\binom{g_i}{n_i}$ 里的 $(g_i-n_i)!$——"空位"的记账；变分后它给出 $g_i-n_i$（而非 $g_i+n_i$），于是 $e^{\alpha+\beta\varepsilon}$ 加上的是 $+1$。玻色子放法为 $\binom{n_i+g_i-1}{n_i}$，Stirling 后出现 $g_i+n_i$，同样推导给出 $-1$。最可几分布的相对涨落 $\sim N^{-1/2}$，热力学极限下微正则与巨正则等价——两条路线的汇合是第 5 节的内部检查。

</details>

**4.** 证明幺正演化保持 von Neumann 熵（从而纯态永远演化成纯态），据此说明"孤立系统热化"为什么需要超出薛定谔方程的输入；并简述 ETH 补上的正是哪一环。

<details markdown="1"><summary>点击显示答案</summary>

**熵守恒**：von Neumann 方程（薛定谔方程对混态的直接改写，见[第 10 篇](10-linear-response-kubo.md) §3）给出 $\rho(t)=U(t)\,\rho(0)\,U^\dagger(t)$，$U=e^{-iHt}$。谱分解 $\rho(0)=\sum_np_n\lvert n\rangle\langle n\rvert$，则 $\rho(t)=\sum_np_n\lvert n(t)\rangle\langle n(t)\rvert$（$\lvert n(t)\rangle=U\lvert n\rangle$ 仍正交归一）——**本征值谱 $\{p_n\}$ 不变**。而

$$S = -\mathrm{Tr}(\rho\ln\rho) = -\sum_np_n\ln p_n$$

只依赖谱，故 $S(t)=S(0)$。特例：纯态谱 $\{1,0,0,\cdots\}$（$S=0$）在演化下永远是纯态谱——从纯初态到热平衡混态，靠 $\hat H$ 的幺正演化**原则上到不了**。

**需要什么输入**：要么承认平衡态密度算符是独立假设（系综路线，第 4 节），要么弱化和细化"热化"的含义。**ETH 补的一环**正是后者：放弃"全局变混"，只要求**少体可观测量的本征态期待值**等于微正则值，$\langle n\rvert\hat A\lvert n\rangle\approx A_{\rm mc}(E_n)$（本征态本身带热性）。于是能量壳层内任取的初态演化后，$\hat A$ 的期待值都收敛到同一个"热"值；全局仍纯、$S$ 仍守恒，丢失的信息流入实验够不到的多体关联与纠缠——热的是**约化密度矩阵**（[第 03 篇](03-formalism-hilbert-dirac.md) §8）。ETH 在强无序系统里失效（多体局域化不热化），说明它是关于哈密顿量性质的猜想而非逻辑必然。

</details>

**5.** 相互作用电子气的基态动量分布 $n(\vec k)$ 与自由情形的 0/1 阶跃有什么差别？解释 $Z$ 因子的意义、Luttinger 定理钉住了什么，以及 ARPES 如何同时"看见"这两件事。

<details markdown="1"><summary>点击显示答案</summary>

**自由情形**：$n(\vec k)=\theta(k_F-k)$，阶跃高度恰为 1。

**相互作用情形**：关联把基态变成多 Slater 行列式的叠加，$k\gt k_F$ 的平面波分量获得非零占据（拖尾），$k\lt k_F$ 被部分掏空；但只要体系留在 Fermi 液体相（凝聚态书[第 6 章](../../condensed-matter/docs/06-interacting-electron-gas.md) §7–8 的绝热连续），$k_F$ 处仍保留有限跃变，幅度由自能决定：

$$n(k_F^-)-n(k_F^+) = Z, \qquad Z = \Big(1-\frac{\partial\,\mathrm{Re}\,\Sigma(\vec k_F,\omega)}{\partial\omega}\Big)^{-1}_{\omega=0} \in (0,1].$$

$Z$ 是单粒子格林函数准粒子极点的留数（$G=Z/(\omega-\varepsilon_k+i/2\tau_k)+\text{非相干背景}$），物理上是"准粒子中裸电子的成分"。

**Luttinger 定理**：跃变的**位置**与相互作用无关——费米面包围的体积恒等于 $n/2$（单位体积电子数，自旋二重；[06s](../../condensed-matter/docs/06s-fermi-liquid-toolbox.md) §5 的 Oshikawa 磁通论证）。一句话：**幅度由动力学（$Z$）决定，位置由拓扑（粒子数）钉死**。

**ARPES**：角分辨光电子能谱直接成像谱函数 $A(\vec k,\omega)$，其能量积分正比于 $n(\vec k)$：沿跨越费米面的动量切线，谱权重的台阶高度量出 $\approx Z$，准粒子色散的斜率量出 $m^\ast/m$，峰宽量出寿命。正常金属 $Z\sim0.5$–$0.9$；重费米子 $Z\sim10^{-3}$–$10^{-2}$（[第 13 章](../../condensed-matter/docs/13-strong-correlations.md)）；一维 Luttinger 液体（[20s](../../condensed-matter/docs/20s-luttinger-liquid.md)）连台阶都没有：$n(k)-n(k_F)\propto-\mathrm{sgn}(k-k_F)\,\lvert k-k_F\rvert^{2\alpha}$，幂律连续——准粒子图像的坟场。

</details>

## 参考

- Landau & Lifshitz《统计物理学 I》§53–55：巨正则系综推导 Fermi/Bose 分布的经典表述（本篇主线）；§35（微正则与组合计数）。
- Pathria & Beale《Statistical Mechanics》第 6 章（理想量子气体的系综推导与经典极限）与附录（Stirling 与最可几法）。
- Pauli, Phys. Rev. 58, 716 (1940)：自旋-统计定理原文；Duck & Sudarshan《Pauli and the Spin-Statistics Theorem》：证明谱系与历史；Streater & Wightman《PCT, Spin and Statistics, and All That》：公理化版本。
- 热化与 ETH：Deutsch, Phys. Rev. A 43, 2046 (1991)；Srednicki, Phys. Rev. E 50, 888 (1994)；Rigol, Dunjko & Olshanii, Nature 452, 854 (2008)；综述 D'Alessio, Kafri, Polkovnikov & Rigol, Adv. Phys. 65, 239 (2016)；典型性 Goldstein et al., Phys. Rev. Lett. 96, 050403 (2006) 与 Popescu, Short & Winter, Nat. Phys. 2, 754 (2006)。
- 交叉参考：本书[第 05s 篇](05s-identical-particles.md)（对称化公设）、[第 09 篇](09-second-quantization.md)（反对易代数）、[第 10 篇](10-linear-response-kubo.md)（系综在响应理论中的取用）；凝聚态书[第 3 章](../../condensed-matter/docs/03-free-electron-gas.md)（FD 分布的应用现场）、[第 6 章](../../condensed-matter/docs/06-interacting-electron-gas.md)与 [06s](../../condensed-matter/docs/06s-fermi-liquid-toolbox.md)（$Z$ 与 Luttinger 定理）、[20s](../../condensed-matter/docs/20s-luttinger-liquid.md)（一维反例）。
