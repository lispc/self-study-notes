# 晶格振动与声子

> 本书位置：凝聚态物理入门导论 · 第 2 章
> 前置知识：经典力学的简正模概念；本科量子力学，尤其是[谐振子的产生/湮灭算符解法](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)（本篇的量子化部分整段是它的直接应用）。
> 学习目标：从一维单原子链的运动方程出发，完整推导色散关系 $\omega(k) = 2\sqrt{\kappa/m}\,\lvert\sin(ka/2)\rvert$；理解 Brillouin 区、群速度与长波极限的声速；把格波正则量子化，看清声子作为"格波量子"的精确含义；说清楚准动量 $\hbar k$ 为什么不是真动量。

约定：本篇**保留 $\hbar$ 与玻尔兹曼常数 $k_B$**（不取自然单位），这样所有公式都可以直接代入数值估算。$k_B$ 在热容一节首次出场。

---

## 1. 一句话总结

**把晶体看成由弹簧拴在晶格上的原子阵列，其微振动可严格分解为 $N$ 个独立的简正模（格波）；每个简正模是一个谐振子，量子化后其激发量子就是声子——携带能量 $\hbar\omega(k)$ 与准动量 $\hbar k$ 的玻色型准粒子。声子是你在凝聚态里遇到的第一个"场量子"，也是整本书"集体激发"叙事的起点。**

下面把这句话逐层拆开。

## 2. 为什么从晶格振动开始

一块固体约有 $10^{23}$ 个原子。直接解 $10^{23}$ 体 Schrödinger 方程毫无希望，所以全部固体物理都是"分层近似"的艺术，而晶格振动是自然的第二层：

- **第零层**：原子固定在平衡位置上——这就是晶体结构（第 1 章）。它解释了衍射图样，但解释不了任何随温度变化的现象。
- **第一层**：允许原子在平衡位置附近做微振动。总势能 $V(\{u_n\})$ 在平衡位置做 Taylor 展开，一阶项因平衡条件为零，领头项是位移的二次型——**简谐近似**。于是问题化为"一堆耦合谐振子"，这是固体物理中第一个可以严格求解的多体问题。

这一步的物理回报极其丰厚：

- **热容**：Dulong–Petit 经典值 $3Nk_B$ 在低温下崩溃，正是晶格振动量子化的直接证据（Einstein 1907 年的工作是量子论首次走出黑体辐射）；
- **弹性与声速**：长波格波就是声波，色散关系的斜率给出声速；
- **往后的一切**：电阻的温度依赖、热导、乃至超导的电声耦合（第 8 章），全部以声子为基本语言。

方法论上还有一层意义：简正模就是傅里叶模，"格波量子化"就是"场的正则量子化"的离散格点版本。学完本篇再去看[标量场量子化：从无穷多谐振子到粒子](../../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)，你会发现两边是同构的——那边只是把格点指标 $n$ 换成连续坐标 $\vec x$。

## 3. 一维单原子链：经典理论

三维晶体在数学上没有本质新内容（只是每个格点多了三个方向的位移、每个 $k$ 有三支偏振），所有核心物理在一维链上就能干净地看到。我们从这里开始。

### 3.1 模型与运动方程

考虑 $N$ 个质量为 $m$ 的全同原子排在一条线上，平衡间距为 $a$，第 $n$ 个原子的平衡位置是 $x_n^{(0)} = na$。令 $u_n(t)$ 为第 $n$ 个原子相对平衡位置的纵向位移。只保留最近邻原子间的相互作用，等效为弹性系数 $\kappa$ 的弹簧。哈密顿量为

$$H = \sum_{n=1}^{N} \frac{p_n^2}{2m} + \frac{\kappa}{2}\sum_{n=1}^{N}\big(u_{n+1} - u_n\big)^2.$$

对 $u_n$ 求力的负梯度：含 $u_n$ 的项来自第 $n$ 根和第 $n-1$ 根弹簧，

$$-\frac{\partial H}{\partial u_n} = \kappa\,(u_{n+1} - u_n) - \kappa\,(u_n - u_{n-1}),$$

于是运动方程为

$$m\,\ddot u_n = \kappa\,(u_{n+1} + u_{n-1} - 2u_n).$$

这是 $N$ 个耦合的线性常微分方程。右边是离散化的二阶导数（差分格式），这提示解应该是某种"离散格点上的波"。

### 3.2 行波解与色散关系

取行波试探解

$$u_n(t) = A\,e^{i(kna - \omega t)}.$$

它自动把耦合方程化为代数方程：代入后 $e^{ikna}$ 是公共因子，两边约去，得

$$-m\omega^2 = \kappa\big(e^{ika} + e^{-ika} - 2\big) = -4\kappa\,\sin^2\!\frac{ka}{2}.$$

于是

$$\boxed{\;\omega(k) = 2\sqrt{\frac{\kappa}{m}}\;\Big\lvert \sin\frac{ka}{2} \Big\rvert\;}$$

这就是单原子链的**色散关系**。几点直接的观察：

- 频率有上限 $\omega_{\max} = 2\sqrt{\kappa/m}$，在 $k = \pm\pi/a$ 处达到。晶格上不存在任意高频的振动——离散性天然提供了一个紫外截断，这一点与连续场论形成鲜明对比（见第 9 节）。
- $\omega(k)$ 是 $k$ 的周期函数，周期 $2\pi/a$。这不是偶然，见下一小节。
- 取负 $k$ 得到反向行波；$\pm k$ 简并是时间反演（$m\ddot u_n$ 方程含二阶时间导数）的体现。

### 3.3 周期性边界条件与模式计数

有限链需要边界条件。方便的做法是 **Born–von Kármán 周期性边界条件**：把链弯成环，要求

$$u_{n+N} = u_n \;\Longrightarrow\; e^{ikNa} = 1 \;\Longrightarrow\; k = \frac{2\pi l}{Na},\quad l \in \mathbb{Z}.$$

相邻 $k$ 的间隔为 $2\pi/(Na)$，$N$ 很大时 $k$ 准连续。但 $l$ 并不能取无穷多个值：若 $k' = k + 2\pi/a$，则

$$e^{ik'na} = e^{ikna}\,e^{i2\pi n} = e^{ikna},$$

两个波在**所有格点上取值完全相同**——物理上是同一个格波。所以独立的 $k$ 只需取一个周期，习惯取

$$-\frac{\pi}{a} < k \le \frac{\pi}{a},$$

称为**第一 Brillouin 区**（BZ）。在这个区间里 $l$ 恰好取 $N$ 个值——$N$ 个原子的链恰好有 $N$ 个纵向简正模，自由度数守恒，账对上了。

这里"格点上取值相同即同一波"的观察值得停下来体会：波长 $\lambda = 2\pi/\lvert k\rvert$ 小于 $2a$ 的波，在离散格点上与某个 $\lambda > 2a$ 的波无法区分（这就是信号处理里的 aliasing）。晶格只"采样"格点处的位移，自然分辨不出更短的波长。

## 4. 群速度与长波极限：声速

色散关系里藏着两类速度：

- **相速度** $v_p = \omega/k$，单个波峰的移动速度；
- **群速度** $v_g = \mathrm d\omega/\mathrm d k$，波包（也就是能量与信息）的传播速度。对 $0 < k < \pi/a$，

$$v_g(k) = \frac{\mathrm d\omega}{\mathrm d k} = a\sqrt{\frac{\kappa}{m}}\,\cos\frac{ka}{2}.$$

在 BZ 边界 $k \to \pm\pi/a$ 处 $v_g \to 0$：色散曲线在此取极大、斜率为零。物理上这是因为半整数倍格距的波满足 Bragg 条件，正反两个方向的行波强耦合成立驻波，波包被"挡停"。这件事在第 4 章能带论里会以电子波的形式原样重演——BZ 边界打开能隙的机制与此同源。

**长波极限** $ka \ll 1$（波长远大于格距）时 $\sin(ka/2) \approx ka/2$，色散线性化：

$$\omega \approx v_s\,\lvert k\rvert, \qquad v_s = a\sqrt{\frac{\kappa}{m}}.$$

线性色散 + 常数速度，这正是弹性连续介质中的声波。也可以直接从运动方程看这个极限：把 $u_n(t)$ 换成光滑场 $u(x,t)$，Taylor 展开

$$u_{n\pm1} \approx u \pm a\,\partial_x u + \frac{a^2}{2}\,\partial_x^2 u \;\Longrightarrow\; u_{n+1} + u_{n-1} - 2u_n \approx a^2\,\partial_x^2 u,$$

运动方程化为波动方程 $m\,\partial_t^2 u = \kappa a^2\,\partial_x^2 u$，声速 $v_s^2 = \kappa a^2/m$ 与上面一致。用线密度 $\rho = m/a$ 与一维弹性模量 $C = \kappa a$ 改写即 $v_s = \sqrt{C/\rho}$——连续介质弹性力学的标准公式。

**量级估算**：典型固体 $\kappa \sim$ 数十 N/m，$m \sim 10^{-26}$ kg，$a \sim 3\times10^{-10}$ m，得 $v_s \sim 10^3\text{–}10^4$ m/s，与实测声速吻合。相应的最大频率 $\omega_{\max} \sim 10^{13}$ Hz 落在红外，这就是声子谱可用中子散射（非弹性散射直接测 $\omega(k)$）与红外/拉曼谱学测量的原因。

<details markdown="1"><summary>补充说明：双原子链——声学支与光学支</summary>

把链换成每个原胞含两个原子（质量 $M_1$、$M_2$，近邻间距 $a$，原胞长 $2a$），同样的手续给出两支色散：

$$\omega^2_{\pm}(k) = \kappa\Big(\frac{1}{M_1} + \frac{1}{M_2}\Big) \pm \kappa\sqrt{\Big(\frac{1}{M_1} + \frac{1}{M_2}\Big)^2 - \frac{4\cos^2(ka)}{M_1 M_2}},$$

其中独立 $k$ 区间缩小为 $\lvert k\rvert \le \pi/(2a)$（原胞加倍，BZ 减半——格波"折叠"了）。两支的物理截然不同：

- **声学支** $\omega_-$：$k \to 0$ 时 $\omega_- \approx v_s\lvert k\rvert \to 0$，同原胞内两原子同相运动，就是普通声波。$\omega(k{=}0)=0$ 不是巧合：$k=0$ 模是整体平移，不消耗任何弹性能——这是连续平移对称性的反映，后面学 Goldstone 定理时会认出这是同一个故事的离散版。
- **光学支** $\omega_+$：$k \to 0$ 时 $\omega_+ \to \sqrt{2\kappa(M_1+M_2)/(M_1M_2)} \neq 0$，同原胞内两原子反相运动。若两原子带异号电荷（如离子晶体），这个振动携带振荡电偶极矩，可与红外光直接耦合——"光学支"由此得名。

两条支之间、以及光学支上方可能出现频率禁区（带隙），这是周期结构谱的普遍特征。三维晶体的规则：**每个原胞 $p$ 个原子 $\Rightarrow$ 3 支声学 + $3(p{-}1)$ 支光学**。

</details>

## 5. 量子化：从简正模到声子

### 5.1 简正坐标

经典力学告诉我们：耦合谐振子体系总可以通过简正变换对角化。对链做离散傅里叶变换，

$$Q_k = \frac{1}{\sqrt N}\sum_n u_n\,e^{-ikna}, \qquad P_k = \frac{1}{\sqrt N}\sum_n p_n\,e^{-ikna},$$

$u_n$、$p_n$ 为实量意味着 $Q_k^\dagger = Q_{-k}$、$P_k^\dagger = P_{-k}$。代回哈密顿量，利用正交关系 $\sum_n e^{i(k-k')na} = N\delta_{kk'}$，交叉项全部消失：

$$H = \sum_k \left[\frac{P_k P_{-k}}{2m} + \frac{m\omega_k^2}{2}\,Q_k Q_{-k}\right], \qquad \omega_k \equiv 2\sqrt{\frac{\kappa}{m}}\,\Big\lvert\sin\frac{ka}{2}\Big\rvert.$$

即 $N$ 个耦合振子严格等价于 $N$ 个**独立的**简正模振子（$k$ 与 $-k$ 配对是一个复振子的实部虚部）。如果你做过 QFT 笔记里[耦合振子链对角化](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)那一节，这一步应该完全眼熟——连公式都是同一套。

### 5.2 正则量子化与产生/湮灭算符

量子化手续是标准的：把 $u_n, p_n$ 提升为算符，施加正则对易关系

$$[u_n, p_{n'}] = i\hbar\,\delta_{nn'}, \qquad [u_n, u_{n'}] = [p_n, p_{n'}] = 0,$$

由此推出 $[Q_k, P_{k'}] = i\hbar\,\delta_{k,-k'}$。对每个模定义

$$b_k = \sqrt{\frac{m\omega_k}{2\hbar}}\left(Q_k + \frac{i}{m\omega_k}P_{-k}\right),$$

则 $[b_k, b_{k'}^\dagger] = \delta_{kk'}$，其余对易子为零。反解出简正坐标并代回位移算符，得到本篇最常用的表达式：

$$\hat u_n = \frac{1}{\sqrt N}\sum_k \sqrt{\frac{\hbar}{2m\omega_k}}\left(b_k\,e^{ikna} + b_k^\dagger\,e^{-ikna}\right),$$

$$\hat p_n = -\frac{i}{\sqrt N}\sum_k \sqrt{\frac{\hbar m\omega_k}{2}}\left(b_k\,e^{ikna} - b_k^\dagger\,e^{-ikna}\right).$$

哈密顿量对角化为

$$\boxed{\;H = \sum_k \hbar\omega_k\left(b_k^\dagger b_k + \frac12\right)\;}$$

### 5.3 声子

上式就是 $N$ 个独立谐振子的能量和。态由每个模的占据数 $\{n_k\}$ 标记，$n_k = b_k^\dagger b_k$ 的本征值取 $0, 1, 2, \dots$，能量

$$E(\{n_k\}) = \sum_k \hbar\omega_k\left(n_k + \frac12\right).$$

于是：

- **声子（phonon）= 格波模 $k$ 的一个激发量子**，携带能量 $\hbar\omega_k$。$b_k^\dagger$ 创造一个声子，$b_k$ 湮灭一个。
- 占据数任意 $\Rightarrow$ 声子是**玻色子**；而且声子数不守恒（热激发可以随意增减声子），化学势为零。
- 基态有**零点能** $E_0 = \frac12\sum_k\hbar\omega_k$。它本身不可测，但零点运动导致原子即使在 $T=0$ 也在抖动，可测后果包括 X 射线衍射强度的 Debye–Waller 因子衰减，以及轻元素晶体（如氦）零点涨落大到阻止固化这样的极端例子。

请停下来对比一下[标量场量子化](../../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)：那边是把 $\varphi(\vec x)$ 按平面波展开、每个 $\vec k$ 一个振子、"粒子 = 场的激发量子"。这里把 $\vec x$ 换成格点 $na$、把无界的 $\vec k$ 换成 BZ 内 $N$ 个离散 $k$，其余一字不差。**声子就是晶格位移场的场量子**——QFT 那套机器第一次在凝聚态里跑通，就是在这一节。

## 6. 准动量 $\hbar k$：为什么不是真动量

每个声子还携带一个标签 $\hbar k$，习惯叫**晶体动量**或**准动量（crystal momentum）**。它在声子–电子、声子–声子散射中表现得像动量（散射前后 $\hbar k$ 之和在某种意义下守恒），但它**不是牛顿力学意义上的总动量**。这两点都值得动手验证。

**真动量只有 $k=0$ 模携带。** 链的总动量算符

$$\hat P = \sum_n \hat p_n = -\frac{i}{\sqrt N}\sum_k\sqrt{\frac{\hbar m\omega_k}{2}}\,(b_k - b_k^\dagger)\sum_n e^{ikna} = -i\sqrt{\frac{N\hbar m\omega_0}{2}}\,(b_0 - b_0^\dagger),$$

因为 $\sum_n e^{ikna} = N\delta_{k,0}$。只有 $k=0$ 模出现——而 $k=0$ 模就是链的刚性整体平移（$\omega_0 = 0$ 的那个模）。任何 $k \neq 0$ 的声子对总动量的贡献严格为零。直观地说：行波 $e^{ikna}$ 里一半原子向左、一半向右，质心动量为零。

**准动量只定义到相差一个倒格矢。** 第 3.3 节已看到 $k$ 与 $k + G$（$G = 2\pi l/a$ 为一维倒格矢）描述同一个格波，所以 $\hbar k$ 本质上只定义在模 $\hbar G$ 的意义下。根源是晶格的平移对称性是**离散的**（平移 $a$ 的整数倍才是不变性）：根据 Noether 定理的对应逻辑，连续平移对称 $\Rightarrow$ 动量严格守恒；离散平移对称 $\Rightarrow$ 动量只守恒到 $\hbar G$ 的整数倍。多出来的部分由晶格整体（作为可以反冲的刚体）吸收。

**物理后果**：两个声子碰撞可以产生一个 $k_3 = k_1 + k_2 - G$ 的声子——当 $k_1 + k_2$ 越出第一 BZ 时，差值 $\hbar G$ 交给晶格。这类过程叫 **Umklapp 过程（翻转过程）**，它是有限热导的根源之一（没有 Umklapp，声子流的准动量严格守恒，理想晶体的热阻会消失）。等你学到能带论（第 4 章），同样的"$\hbar k$ 模 $\hbar G$"结构会在电子身上再出现一次，名字都不换。

## 7. 声子统计与固体热容

声子是化学势为零的玻色子，平衡态占据数由 Planck 分布给出（$\beta = 1/(k_B T)$，$k_B$ 为玻尔兹曼常数）：

$$\langle n_k\rangle = \frac{1}{e^{\beta\hbar\omega_k} - 1}, \qquad U(T) = \sum_k \hbar\omega_k\left(\langle n_k\rangle + \frac12\right).$$

热容 $C_V = \partial U/\partial T$ 的计算只剩对 $k$ 求和，结果取决于你往求和里填什么色散：

- **Einstein 模型（1907）**：假定所有模同频率 $\omega_E$（相当于只保留光学支的粗糙版）。高温极限回到 Dulong–Petit 值 $3Nk_B$；低温下 $C_V \sim e^{-\hbar\omega_E/k_B T}$ 指数压灭。定性上对（热容确实量子化地"冻出"），定量上错——实验看到的是幂律。
- **Debye 模型（1912）**：尊重长波极限的真实色散 $\omega = v_s k$，对三维晶体取线性谱并加一个截断 $k_D$（Debye 波矢）以保证总模数为 $3N$。低温下只有 $\hbar\omega \lesssim k_B T$ 的模被激发，三维 $k$ 空间中这些模的数目 $\propto T^3$，每个模平均能量 $\sim k_B T$，于是

$$C_V = \frac{12\pi^4}{5}\,Nk_B\left(\frac{T}{\Theta_D}\right)^3 \quad (T \ll \Theta_D),$$

其中 Debye 温度 $\Theta_D = \hbar v_s k_D/k_B$。$T^3$ 律与实验精确吻合。

这一节的方法论要点：**低温热容就是声子色散关系与空间维数的一台测量仪器**（一维链的 Debye 模型给出 $C_V \propto T$，读者可在自检问题里推三维版本的结构）。后面遇到任何玻色型元激发（磁振子、等离激元……），第一步永远是同样的：写下色散，数模，积出热力学量。

## 8. 往前看：声子在本书里的回响

- **第 3 章**：自由电子气的热容 $\propto T$，与声子的 $T^3$ 在极低温交汇，两者的比值是常规实验定 $\Theta_D$ 与 Sommerfeld 系数的入口。
- **第 4 章**：Bloch 电子与格波共享同一个 BZ 几何；"BZ 边界群速度为零/开能隙"从机械振动推广到电子波。
- **第 8 章**：超导的微观根源是电子通过交换虚声子产生有效吸引——声子不只是热学配角，而是相互作用的中介者，与 QED 里光子传递电磁相互作用完全同构。
- **第 9 章**：声学声子在 $k\to0$ 处 $\omega\to0$（无能隙）是自发破缺连续平移对称性的 Goldstone 模——同一个概念会贯穿相变与临界现象。

## 9. 小结

| 概念 | 单原子链结果 | 备注 |
|---|---|---|
| 运动方程 | $m\ddot u_n = \kappa(u_{n+1} + u_{n-1} - 2u_n)$ | 最近邻简谐近似 |
| 色散关系 | $\omega(k) = 2\sqrt{\kappa/m}\,\lvert\sin(ka/2)\rvert$ | $\omega_{\max} = 2\sqrt{\kappa/m}$，天然紫外截断 |
| Brillouin 区 | $-\pi/a < k \le \pi/a$，恰含 $N$ 个模 | $k$ 与 $k+2\pi/a$ 是同一格波 |
| 群速度 | $v_g = a\sqrt{\kappa/m}\cos(ka/2)$ | BZ 边界 $v_g \to 0$（驻波、Bragg 反射） |
| 长波极限 | $\omega \approx v_s k$，$v_s = a\sqrt{\kappa/m}$ | 即连续介质声波，$v_s \sim 10^3$–$10^4$ m/s |
| 量子化 | $H = \sum_k \hbar\omega_k(b_k^\dagger b_k + \tfrac12)$ | 与标量场量子化同一套手续 |
| 声子 | 能量 $\hbar\omega_k$，准动量 $\hbar k$ | 玻色子，化学势为零 |
| 准动量 | 守恒模 $\hbar G$，$G = 2\pi/a$ | 真动量只有 $k=0$ 模携带；Umklapp 过程 |
| 热容 | Einstein：定性；Debye：$C_V \propto T^3$（三维） | 低温热容 = 色散与维数的探针 |

一句话收束：**简谐晶格 = 一堆独立谐振子；声子 = 振子的激发量子；准动量的模 $\hbar G$ 守恒是离散平移对称性的签名。**

## 自检问题

**1.** 从单原子链运动方程出发推导色散关系，并求最大频率 $\omega_{\max}$ 及其对应的 $k$。该 $k$ 处的格波长什么样？

<details markdown="1"><summary>点击显示答案</summary>

将 $u_n = A e^{i(kna-\omega t)}$ 代入 $m\ddot u_n = \kappa(u_{n+1} + u_{n-1} - 2u_n)$，左边给出 $-m\omega^2$，右边给出

$$\kappa\big(e^{ika} + e^{-ika} - 2\big) = \kappa\big(2\cos ka - 2\big) = -4\kappa\sin^2\frac{ka}{2},$$

约去公共因子 $A e^{i(kna-\omega t)}$ 得 $\omega^2 = (4\kappa/m)\sin^2(ka/2)$，即

$$\omega(k) = 2\sqrt{\kappa/m}\;\lvert\sin(ka/2)\rvert.$$

$\lvert\sin\rvert$ 最大值为 1，在 $ka/2 = \pi/2$ 即 $k = \pm\pi/a$（BZ 边界）达到，故 $\omega_{\max} = 2\sqrt{\kappa/m}$。此时相邻原子的相位差为 $ka = \pi$，即 $u_{n+1} = -u_n$：相邻原子严格反向运动，波长 $\lambda = 2a$，是晶格能支持的最短波长。群速度 $v_g \propto \cos(ka/2) = 0$，这是一个不传播能量的驻波（Bragg 反射的结果）。

</details>

**2.** 用周期性边界条件证明第一 Brillouin 区内恰好有 $N$ 个允许的 $k$ 值，并显式验证 $k$ 与 $k + 2\pi/a$ 在格点上给出完全相同的位移图样。

<details markdown="1"><summary>点击显示答案</summary>

Born–von Kármán 条件 $u_{n+N} = u_n$ 作用在行波上给出 $e^{ikNa} = 1$，故

$$k = \frac{2\pi l}{Na}, \qquad l \in \mathbb{Z}.$$

第一 BZ 为 $-\pi/a < k \le \pi/a$，宽度 $2\pi/a$。其中允许值的个数为

$$\frac{2\pi/a}{2\pi/(Na)} = N.$$

（对应 $l = -N/2 + 1, \dots, N/2$，共 $N$ 个整数值。）

再验证等价性：取 $k' = k + 2\pi/a$，对任意格点 $n$，

$$e^{ik'na} = e^{ikna}\cdot e^{i(2\pi/a)na} = e^{ikna}\cdot e^{i2\pi n} = e^{ikna},$$

因为 $n$ 是整数、$e^{i2\pi n} = 1$。两个波在**每一个**格点上的位移都相同，而晶格只有格点处才有原子——所以它们是同一个物理格波，不是两个模。这正是"独立的 $k$ 只需取一个 BZ"的原因，也是倒格矢 $G = 2\pi/a$ 进入全部晶格物理的入口。

</details>

**3.** 推导长波极限的声速 $v_s = a\sqrt{\kappa/m}$，并用 $\kappa \sim 30\ \mathrm{N/m}$、$m \sim 5\times10^{-26}\ \mathrm{kg}$、$a \sim 3\times10^{-10}\ \mathrm{m}$ 估算其量级。

<details markdown="1"><summary>点击显示答案</summary>

长波极限 $ka \ll 1$ 时 $\sin(ka/2) \approx ka/2$，代入色散关系：

$$\omega \approx 2\sqrt{\frac{\kappa}{m}}\cdot\frac{ka}{2} = a\sqrt{\frac{\kappa}{m}}\;k \equiv v_s\,k,$$

所以 $v_s = a\sqrt{\kappa/m}$。（等价地，把运动方程中的差分 $u_{n+1} + u_{n-1} - 2u_n$ 换成 $a^2\partial_x^2 u$，波动方程 $m\,\partial_t^2 u = \kappa a^2\,\partial_x^2 u$ 给出同样的 $v_s^2 = \kappa a^2/m$。）

代入数值：

$$v_s = 3\times10^{-10}\ \mathrm{m}\times\sqrt{\frac{30\ \mathrm{N/m}}{5\times10^{-26}\ \mathrm{kg}}} = 3\times10^{-10}\times\sqrt{6\times10^{26}}\ \frac{\mathrm{m}}{\mathrm s} \approx 3\times10^{-10}\times 2.4\times10^{13}\ \frac{\mathrm m}{\mathrm s} \approx 7\times10^3\ \mathrm{m/s}.$$

典型固体声速确实在 $10^3$–$10^4$ m/s 量级（如铜约 4700 m/s，硅约 8400 m/s）。注意声速比费米速度（第 3 章，$\sim 10^6$ m/s）小两个数量级以上——这个巨大尺度分离是 Born–Oppenheimer 近似（电子瞬时跟随离子）成立的物理基础。

</details>

**4.** 利用位移与动量算符的模展开式，验证 $[b_k, b_{k'}^\dagger] = \delta_{kk'}$ 蕴含正则对易关系 $[\hat u_n, \hat p_{n'}] = i\hbar\,\delta_{nn'}$。

<details markdown="1"><summary>点击显示答案</summary>

记 $\mathcal N_k = \sqrt{\hbar/(2m\omega_k)}$、$\mathcal M_k = \sqrt{\hbar m\omega_k/2}$。展开

$$[\hat u_n, \hat p_{n'}] = -\frac{i}{N}\sum_{k,k'}\mathcal N_k \mathcal M_{k'} \Big[ b_k e^{ikna} + b_k^\dagger e^{-ikna},\; b_{k'} e^{ik'n'a} - b_{k'}^\dagger e^{-ik'n'a}\Big].$$

四个对易子中只有 $[b_k, -b_{k'}^\dagger]$ 与 $[b_k^\dagger, b_{k'}]$ 非零，分别给出 $-\delta_{kk'}$ 与 $-\delta_{kk'}$，故

$$[\hat u_n, \hat p_{n'}] = -\frac{i}{N}\sum_k \mathcal N_k\mathcal M_k\,\big(-e^{ik(n-n')a} - e^{-ik(n-n')a}\big) = \frac{2i}{N}\sum_k \mathcal N_k\mathcal M_k \cos\big(k(n-n')a\big).$$

注意 $\mathcal N_k \mathcal M_k = \hbar/2$（$\omega_k$ 恰好消掉——这是正则结构不依赖色散细节的原因），于是

$$[\hat u_n, \hat p_{n'}] = \frac{i\hbar}{N}\sum_k \cos\big(k(n-n')a\big) = \frac{i\hbar}{N}\sum_k e^{ik(n-n')a} = i\hbar\,\delta_{nn'},$$

最后一步用了 BZ 内 $N$ 个 $k$ 值的完备关系 $\sum_k e^{ikna} = N\delta_{n,0}$（对 $n \in \{-N/2,\dots,N/2\}$）。（$\sum_k \sin(kna)$ 类奇函数部分对 $k \to -k$ 抵消，故余弦可换成指数。）

</details>

**5.** 证明链的总动量算符只含 $k=0$ 分量，并据此解释：(a) 为什么单个 $k\neq0$ 的声子不携带真动量；(b) 双声子散射 $k_1 + k_2 \to k_3$ 中"动量守恒"的准确表述是什么。

<details markdown="1"><summary>点击显示答案</summary>

对 $\hat p_n$ 的模展开式直接对 $n$ 求和：

$$\hat P = \sum_n \hat p_n = -\frac{i}{\sqrt N}\sum_k \sqrt{\frac{\hbar m\omega_k}{2}}\,(b_k - b_k^\dagger)\underbrace{\sum_n e^{ikna}}_{N\delta_{k,0}} = -i\sqrt{\frac{N\hbar m\omega_0}{2}}\,(b_0 - b_0^\dagger).$$

只有 $k=0$ 模存活。$k=0$ 模是全体原子的刚性平移（$u_n$ 与 $n$ 无关），质心运动的动量——这才是牛顿意义的真动量，而它携带零声子（$\omega_0 = 0$，无激发能）。

**(a)** 对任意 $k\neq0$ 的声子态 $\lvert n_k\rangle$，$\hat P$ 只作用在 $k=0$ 模上，期望值为零（且与声子数 $n_k$ 无关）。行波中左移与右移的原子恰好对称，质心不动。

**(b)** 准确的守恒律是**准动量守恒模倒格矢**：

$$k_1 + k_2 = k_3 + G, \qquad G = \frac{2\pi l}{a}.$$

若 $k_1 + k_2$ 落在第一 BZ 内，$G=0$（正常过程，N 过程）；若越出 BZ，则必须把 $G \neq 0$ 的准动量交给晶格整体（Umklapp 过程，U 过程），$k_3 = k_1 + k_2 - G$ 折回 BZ。根源：晶格只有离散平移对称性，Noether 对应的守恒量只定义到 $\hbar G$。U 过程是有限热阻的关键机制——它让声子总准动量得以弛豫，热流才能耗散。

</details>

## 参考

- Kittel《固体物理导论》：第 4 章（晶体振动：单/双原子链、色散、量子化）、第 5 章（声子热学性质：Einstein 与 Debye 模型）——与本篇一一对应，推导风格最接近。
- Ashcroft & Mermin《Solid State Physics》：第 22 章（经典简谐晶体）、第 23 章（量子简谐晶体与热力学）——更严谨的正则量子化处理，含三维推广与简正模计数的一般理论。
- 专题深入：Marder《Condensed Matter Physics》第 13 章（声子）——含非弹性中子散射测声子谱的完整讨论；Ziman《Electrons and Phonons》前几章——声子作为"相互作用载体"的经典视角，为第 8 章超导热身。
