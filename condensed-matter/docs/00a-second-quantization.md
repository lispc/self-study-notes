# 二次量子化：多体问题的母语

> 本书位置：凝聚态物理入门导论 · 第〇部分（多体量子力学工具箱）· 第 1 章。本章是全书后续几乎所有章节的语言基础，直接前置：[第 2 章 晶格振动与声子](02-lattice-vibrations-phonons.md)、[第 6 章 相互作用电子气](06-interacting-electron-gas.md)、[第 13 章 强关联](13-strong-correlations.md)、[第 14 章 精确方法](14-exact-methods-fci-ed.md)。
> 前置知识：单粒子量子力学（态矢、算符、表象变换）；谐振子的代数解法（升降算符 $a,a^\dagger$，见 QFT 书笔记[谐振子阶梯算符](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)）。
> 学习目标：理解为什么多体问题必须放弃 $N$ 体波函数语言；掌握 Fock 空间、产生湮灭算符与场算符的构造及（反）对易代数；会把任意单体、两体算符翻译成二次量子化形式；在三个贯穿全书的例子（凝胶模型、Hubbard 模型、晶格振动）中认出这套语言。

---

**单位约定**：本章按本书笔记惯例取自然单位 $\hbar = 1$（首次出现特此说明），涉及具体数值估算时再恢复 $\hbar$。

## 1. 一句话总结

**二次量子化不引入任何新物理——它是把多体量子力学从"$N$ 体对称化波函数"翻译成"占据数态 + 产生湮灭算符"的一套语言：全同粒子统计自动内置于代数关系（对易 = 玻色，反对易 = 费米），算符对所有粒子数 $N$ 一劳永逸地写成同一形式，粒子数可变的过程（声子发射、空穴激发、超导配对）第一次有了自然的描述。它是凝聚态多体理论的母语，也是通往量子场论的桥。**

## 2. 为什么一次量子化不够用

单粒子量子力学里，一个粒子由波函数 $\varphi(\vec x)$ 描述。推广到 $N$ 个全同粒子，教科书的标准答案是（费米子情形）反对称化波函数，即 Slater 行列式：

$$\Psi(\vec x_1,\cdots,\vec x_N) = \frac{1}{\sqrt{N!}}\sum_{P}(\pm1)^{P}\,\varphi_{\alpha_1}(\vec x_{P1})\cdots\varphi_{\alpha_N}(\vec x_{PN}).$$

这个形式在原理上完备，在实践上却是灾难，原因有二。

**灾难一：随 $N$ 指数膨胀。** 行列式展开有 $N!$ 项；更根本地，若在 $M$ 个单粒子轨道里放 $N$ 个费米子，独立的反对称态有 $\binom{M}{N}$ 个。取 $M=2N$（一个很穷的基组），$\binom{2N}{N}\sim 4^N/\sqrt{\pi N}$——$N=50$ 时已达 $10^{29}$ 量级。一摩尔电子的体系（$N\sim 10^{23}$）连写下波函数都是奢望。这就是[第 14 章](14-exact-methods-fci-ed.md)精确对角化方法永远打不破的"指数墙"。

**灾难二：粒子数可变的系统根本没有固定 $N$ 的波函数。** 晶体里的声子可以被晶格热激发源源不断地产生和吸收；金属被光照后电子–空穴对成对出现；超导体的 BCS 基态是不同库珀对数态的相干叠加，粒子数本身有涨落。对这些系统，"先固定 $N$ 再写波函数"的第一步就走不通。

出路是换一个记账方式：不再问"第 $i$ 个粒子在哪个轨道"（全同粒子这个问题本来就没有意义），改问"每个轨道上**有几个**粒子"。这个视角转换就是二次量子化。名字叫"二次"纯属历史偶然——没有任何东西被量子化了两次，只是一次量子化里波函数是对象，而在新语言里波函数的展开系数被提升成了算符。

## 3. Fock 空间与粒子数表象

选定一组完备单粒子基 $\{\varphi_\alpha\}$（平面波、Wannier 轨道、格点轨道均可），用一个**占据数列表**标记多体态：

$$\lvert n_1, n_2, \cdots, n_\alpha, \cdots\rangle, \qquad n_\alpha = \text{轨道 } \alpha \text{ 上的粒子数}.$$

所有这样的态（对所有 $n_\alpha$ 的合法取值、所有 $N=\sum_\alpha n_\alpha$）张成 **Fock 空间**，它是各固定粒子数 Hilbert 空间的直和：

$$\mathcal F = \mathcal H_0 \oplus \mathcal H_1 \oplus \mathcal H_2^{(s/a)} \oplus \cdots \oplus \mathcal H_N^{(s/a)} \oplus \cdots$$

其中 $\mathcal H_0$ 是一维的**真空态** $\lvert 0\rangle$（一个粒子也没有），上标 $s/a$ 表示对称化（玻色子）或反对称化（费米子）。占据数态取为正交归一的。两种统计的区别只在于占据数的合法取值：

| 统计 | $n_\alpha$ 取值 | 代数关系 | 本书中的例子 |
|---|---|---|---|
| 玻色子 | $0,1,2,\cdots$（无上限） | 对易关系 | 声子、等离激元、光子 |
| 费米子 | $0,1$（Pauli 不相容） | 反对易关系 | 电子、空穴 |

Fock 空间的结构已经回应了第 2 节的灾难二：不同 $N$ 的扇区被装进同一个空间，粒子数改变只是在这个空间里从一层跳到另一层。剩下的问题是：如何实现"跳"？这就是产生湮灭算符。

## 4. 产生湮灭算符

### 4.1 玻色子：谐振子代数的自然推广

回忆[谐振子的阶梯算符](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)：$[a,a^\dagger]=1$，$\hat n=a^\dagger a$ 的本征态 $\lvert n\rangle$ 满足 $a^\dagger\lvert n\rangle=\sqrt{n+1}\,\lvert n+1\rangle$、$a\lvert n\rangle=\sqrt n\,\lvert n-1\rangle$。二次量子化做的只是宣布：**每个单粒子模 $\alpha$ 都是一个独立的"谐振子"，其"激发量子数"就是该轨道上的粒子数**。于是对每个模定义 $a_\alpha, a_\alpha^\dagger$，满足

$$[a_\alpha, a_\beta^\dagger] = \delta_{\alpha\beta}, \qquad [a_\alpha, a_\beta] = [a_\alpha^\dagger, a_\beta^\dagger] = 0,$$

作用在占据数态上：

$$a_\alpha^\dagger\lvert\cdots,n_\alpha,\cdots\rangle = \sqrt{n_\alpha+1}\,\lvert\cdots,n_\alpha+1,\cdots\rangle, \qquad a_\alpha\lvert\cdots,n_\alpha,\cdots\rangle = \sqrt{n_\alpha}\,\lvert\cdots,n_\alpha-1,\cdots\rangle.$$

粒子数算符 $\hat n_\alpha = a_\alpha^\dagger a_\alpha$ 的本征值就是 $n_\alpha$，总粒子数 $\hat N = \sum_\alpha \hat n_\alpha$。任何多体态都可以从真空造出来：$\lvert n_1,n_2,\cdots\rangle = \prod_\alpha (a_\alpha^\dagger)^{n_\alpha}/\sqrt{n_\alpha!}\;\lvert0\rangle$。$\sqrt{n+1}$ 的增强因子不是技术细节——它就是玻色子的**受激辐射**（向已有 $n$ 个量子的模里再放一个，矩阵元放大 $\sqrt{n+1}$），激光和玻色–爱因斯坦凝聚的微观根源。

### 4.2 费米子：反对易关系与自动出现的 Pauli 原理

费米子把对易子换成反对易子 $\{A,B\}\equiv AB+BA$：

$$\{c_\alpha, c_\beta^\dagger\} = \delta_{\alpha\beta}, \qquad \{c_\alpha, c_\beta\} = \{c_\alpha^\dagger, c_\beta^\dagger\} = 0.$$

取第二条的 $\alpha=\beta$：$2(c_\alpha^\dagger)^2 = 0$，即**$(c_\alpha^\dagger)^2 = 0$——试图在同一轨道上放两个费米子，得到的是零矢量**。Pauli 不相容原理不再是外加假设，而是代数的直接推论。相应地 $n_\alpha\in\{0,1\}$，$\hat n_\alpha = c_\alpha^\dagger c_\alpha$ 满足 $\hat n_\alpha^2=\hat n_\alpha$（自检题 1）。

费米子独有的技术细节是**符号**：因为不同轨道的算符反对易，态的定义依赖轨道排列顺序。约定 $c_\alpha^\dagger$ 按固定顺序依次作用构造态，则

$$c_\alpha\lvert\cdots,n_\alpha,\cdots\rangle = (-1)^{S_\alpha}\,n_\alpha\,\lvert\cdots,0,\cdots\rangle, \qquad S_\alpha = \sum_{\beta<\alpha}n_\beta,$$

即把 $\alpha$ 轨道上的粒子"取出来"要越过它前面的 $S_\alpha$ 个粒子，每越过一个费米子贡献一个负号（这条符号链在一维系统里就是 Jordan–Wigner 弦，[第 20 章](20-dmrg-tensor-networks.md)的 Luttinger 液体部分会再遇到）。以后凡涉及费米子算符的交换次序，符号都不能丢——本书大量推导的全部"艺术性"就在于伺候好这些负号。

## 5. 场算符：连续空间的产生湮灭算符

以上都是相对某个离散基 $\{\varphi_\alpha\}$ 写的。把基取成位置本征态，得到**场算符**：

$$\hat\psi(\vec x) = \sum_\alpha \varphi_\alpha(\vec x)\,c_\alpha, \qquad \hat\psi^\dagger(\vec x) = \sum_\alpha \varphi_\alpha^*(\vec x)\,c_\alpha^\dagger.$$

$\hat\psi^\dagger(\vec x)$ 在位置 $\vec x$ 处产生一个粒子（波函数是 $\delta$ 型），$\hat\psi(\vec x)$ 湮灭一个。利用单粒子基的完备性 $\sum_\alpha\varphi_\alpha(\vec x)\varphi_\alpha^*(\vec x') = \delta(\vec x-\vec x')$，（反）对易关系直接继承下来：

$$[\hat\psi(\vec x),\hat\psi^\dagger(\vec x')]_\mp = \delta(\vec x-\vec x'), \qquad [\hat\psi(\vec x),\hat\psi(\vec x')]_\mp = 0,$$

其中 $\mp$ 的上号（对易子）对应玻色子、下号（反对易子）对应费米子。场算符是"万能基"：换基只是对 $\hat\psi$ 做展开，例如动量空间的平面波基 $\varphi_{\vec k}(\vec x)=e^{i\vec k\cdot\vec x}/\sqrt V$ 给出

$$\hat\psi(\vec x) = \frac{1}{\sqrt V}\sum_{\vec k} e^{i\vec k\cdot\vec x}\,c_{\vec k}, \qquad c_{\vec k} = \frac{1}{\sqrt V}\int d^3x\, e^{-i\vec k\cdot\vec x}\,\hat\psi(\vec x),$$

$c_{\vec k}$ 与 $\hat\psi(\vec x)$ 互为傅里叶变换，（反）对易关系在两边形式不变（自检题 5）。

两个常用的场算符组合：密度算符 $\hat n(\vec x) = \hat\psi^\dagger(\vec x)\hat\psi(\vec x)$，其积分 $\int d^3x\,\hat n(\vec x) = \sum_\alpha c_\alpha^\dagger c_\alpha = \hat N$ 正是总粒子数；密度涨落 $\delta\hat n(\vec x) = \hat n(\vec x) - \langle\hat n(\vec x)\rangle$ 的傅里叶分量将是[第 6 章](06-interacting-electron-gas.md)里屏蔽与等离激元理论的主角。

## 6. 算符的二次量子化翻译

Fock 空间建好后，物理算符必须从"$N$ 体形式"翻译成"产生湮灭算符形式"。规则只有两条。

### 6.1 单体算符

一次量子化中的单体算符 $\hat T^{(N)} = \sum_{i=1}^N t(\vec x_i)$（动能、外势等）翻译为

$$\hat T = \sum_{\alpha\beta} \langle\alpha\lvert t\rvert\beta\rangle\,c_\alpha^\dagger c_\beta = \int d^3x\;\hat\psi^\dagger(\vec x)\,t(\vec x)\,\hat\psi(\vec x).$$

直觉很清楚：$c_\beta$ 把粒子从轨道 $\beta$ 拿走，$c_\alpha^\dagger$ 放进轨道 $\alpha$，矩阵元 $\langle\alpha|t|\beta\rangle$ 是权重——这正是 $t$ 在单粒子态上做的事情，只是由算符自动对"所有粒子"求和。两个最重要的例子：动能（用动量基，$t=-\nabla^2/2m$ 对角）

$$\hat T_{\text{kin}} = \sum_{\vec k}\varepsilon_{\vec k}\,c_{\vec k}^\dagger c_{\vec k}, \qquad \varepsilon_{\vec k} = \frac{k^2}{2m};$$

外势（用位置基，$t = V(\vec x)$ 对角）

$$\hat V_{\text{ext}} = \int d^3x\;V(\vec x)\,\hat n(\vec x).$$

### 6.2 两体算符

两体相互作用 $\hat V^{(N)} = \frac12\sum_{i\neq j} v(\vec x_i-\vec x_j)$ 翻译为

$$\hat V = \frac12\sum_{\alpha\beta\gamma\delta}\langle\alpha\beta\lvert v\rvert\gamma\delta\rangle\,c_\alpha^\dagger c_\beta^\dagger c_\delta c_\gamma = \frac12\int d^3x\,d^3x'\;\hat\psi^\dagger(\vec x)\hat\psi^\dagger(\vec x')\,v(\vec x-\vec x')\,\hat\psi(\vec x')\hat\psi(\vec x),$$

其中 $\langle\alpha\beta|v|\gamma\delta\rangle = \int d^3x\,d^3x'\,\varphi_\alpha^*(\vec x)\varphi_\beta^*(\vec x')\,v(\vec x-\vec x')\,\varphi_\gamma(\vec x)\varphi_\delta(\vec x')$。**注意湮灭算符的顺序 $c_\delta c_\gamma$ 与产生算符 $\alpha\beta$ 是反序的**——对费米子这个顺序差一个负号，写错全篇皆错。直觉：从 $\gamma,\delta$ 两个轨道各取走一个粒子，再放进 $\alpha,\beta$，权重是二体矩阵元。

### 6.3 关键优点：算符不携带 $N$

对比两种语言：

- 一次量子化：$\hat H^{(N)} = \sum_{i=1}^N t_i + \frac12\sum_{i\neq j}v_{ij}$，**求和上限 $N$ 写在算符里**。$N$ 变了，哈密顿量就要重写；问"$N$ 和 $N+1$ 的系统什么关系"无从谈起。
- 二次量子化：$\hat H$ 由 $c,c^\dagger$ 构成，**与 $N$ 无关**——同一个 $\hat H$ 作用在 Fock 空间的任何扇区都合法。粒子数信息全部在**态**里携带。

这一结构带来的红利随处可见：粒子数不守恒的过程（声子发射、超导配对）有算符可以写；巨正则系综里 $\hat H - \mu\hat N$ 是良定义的单个算符；微扰论可以对同一台机器在所有 $N$ 下统一展开。自检题 3 将验证：二次量子化算符在两粒子态上的矩阵元与一次量子化 Slater 行列式的结果精确一致——新语言包含旧语言，只是更好用。

## 7. 三个贯穿全书的例子

### 7.1 凝胶模型：动量空间的电子气

均匀电子气（凝胶模型，正电荷背景抵消库仑相互作用的 $q=0$ 分量）在动量空间写成

$$\hat H = \sum_{\vec k\sigma}\varepsilon_{\vec k}\,c_{\vec k\sigma}^\dagger c_{\vec k\sigma} + \frac{1}{2V}\sum_{\vec q\neq 0}\sum_{\vec k\vec k'}\sum_{\sigma\sigma'} v(\vec q)\;c_{\vec k+\vec q,\sigma}^\dagger c_{\vec k'-\vec q,\sigma'}^\dagger c_{\vec k'\sigma'} c_{\vec k\sigma}, \qquad v(\vec q) = \frac{4\pi e^2}{q^2}.$$

相互作用项的图像：两个电子 $\vec k,\vec k'$ 散射，转移动量 $\vec q$（自旋在库仑散射中不变）。相互作用**在动量空间对角化**（每个 $\vec q$ 分量独立），这正是平面波基的威力。[第 6 章](06-interacting-electron-gas.md)的全部工作——Hartree–Fock、RPA、等离激元——就是对这个哈密顿量的逐级近似。

### 7.2 紧束缚模型与 Hubbard 模型

换到实空间格点基：$c_{i\sigma}^\dagger$ 在格点 $i$ 上产生一个自旋 $\sigma$ 的电子。动能（格点间跳跃）加在位库仑排斥：

$$\hat H_{\text{tb}} = -t\sum_{\langle ij\rangle,\sigma}\left(c_{i\sigma}^\dagger c_{j\sigma} + c_{j\sigma}^\dagger c_{i\sigma}\right), \qquad \hat H_{\text{Hubbard}} = \hat H_{\text{tb}} + U\sum_i \hat n_{i\uparrow}\hat n_{i\downarrow}.$$

紧束缚模型的基态（半满时是金属）可由能带理论完全解出；加上 Hubbard $U$ 项后，$t\ll U$ 时电子被钉在格点上形成 Mott 绝缘体——[第 13 章](13-strong-correlations.md)的主题。注意这个模型只有"两个参数 $t,U$"，却是凝聚态物理至今未解决的最难问题之一；它同时也是[第 14 章](14-exact-methods-fci-ed.md)精确对角化和[第 20 章](20-dmrg-tensor-networks.md)张量网络方法的试金石。

### 7.3 晶格振动：一堆玻色模

离子实偏离平衡位置的小振动，经简正模变换后，哈密顿量是**独立玻色模的直和**：

$$\hat H_{\text{ph}} = \sum_{\vec q\lambda}\omega_{\vec q\lambda}\left(a_{\vec q\lambda}^\dagger a_{\vec q\lambda} + \frac12\right), \qquad [a_{\vec q\lambda}, a_{\vec q'\lambda'}^\dagger] = \delta_{\vec q\vec q'}\delta_{\lambda\lambda'},$$

每个模 $(\vec q,\lambda)$ 就是一个谐振子，其量子就是声子。声子数不守恒（热激发随意产生），所以玻色型产生湮灭算符不是选择而是必须——[第 2 章](02-lattice-vibrations-phonons.md)将从头推导这个式子。

三个例子合起来传达一个信息：**二次量子化哈密顿量是"模型"的标准书写格式**。剩下整本书的工作，都可以概括为对这样的 $\hat H$ 求基态、激发谱与响应函数。

## 8. 预告：Wick 定理的一点思想

二次量子化给了语言，微扰论给了算法，而把两者缝起来的核心工具是 **Wick 定理**。思想一句话：对自由（二次型）哈密顿量，任意多个算符的真空期望值可以全部化简为**两两配对（收缩）的乘积之和**，费米子带交换符号。例如

$$\langle 0\rvert\,\hat\psi_1\hat\psi_2^\dagger\hat\psi_3\hat\psi_4^\dagger\,\rvert0\rangle = \langle 0\rvert\hat\psi_1\hat\psi_2^\dagger\rvert0\rangle\langle 0\rvert\hat\psi_3\hat\psi_4^\dagger\rvert0\rangle \mp \langle 0\rvert\hat\psi_1\hat\psi_4^\dagger\rvert0\rangle\langle 0\rvert\hat\psi_3\hat\psi_2^\dagger\rvert0\rangle.$$

每个收缩就是一个自由传播子。于是"算微扰展开"变成"数配对方式"，而配对方式与 Feynman 图一一对应——多体微扰论的整套图技术由此而来。本章不展开，等 Green 函数正式登场时再证明和使用它（QFT 书的[标量场正则量子化](../../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)有同一代数的场论版本）。

## 9. 小结

| 对象 | 一次量子化 | 二次量子化 |
|---|---|---|
| 态 | $N$ 体（反）对称波函数，$N!$ 项 | 占据数态 $\lvert n_1 n_2 \cdots\rangle$ |
| 粒子数 | 固定，写死在波函数里 | 由态携带，算符不含 $N$ |
| 单体算符 | $\sum_{i=1}^N t_i$ | $\sum_{\alpha\beta}t_{\alpha\beta}\,c_\alpha^\dagger c_\beta$ |
| 两体算符 | $\frac12\sum_{i\neq j}v_{ij}$ | $\frac12\sum v_{\alpha\beta\gamma\delta}\,c_\alpha^\dagger c_\beta^\dagger c_\delta c_\gamma$ |
| 统计 | 手动（反）对称化 | 对易/反对易关系自动实现 |
| 粒子数可变 | 无法描述 | Fock 空间直和各 $N$ 扇区，天然支持 |

- 全同粒子的对称化波函数随 $N$ 指数膨胀，且对粒子数可变系统失效——这是换语言的两条独立动机。
- 玻色子每个模是一个谐振子（对易关系，$n_\alpha$ 无上限）；费米子满足反对易关系，$(c^\dagger)^2=0$ 把 Pauli 原理内置进代数，代价是处处留心交换符号。
- 场算符 $\hat\psi(\vec x)=\sum_\alpha\varphi_\alpha(\vec x)c_\alpha$ 是位置空间的产生湮灭算符；换基 = 对 $\hat\psi$ 换展开，（反）对易关系形式不变。
- 算符翻译规则：单体 $\to c^\dagger c$，两体 $\to c^\dagger c^\dagger cc$（湮灭端反序）。算符不依赖 $N$，态才携带 $N$。
- 凝胶模型、Hubbard 模型、晶格振动分别示范了动量基、格点基、玻色模三种典型用法，它们是第 6、13、2 章的入口。

## 自检问题

**1.** 仅从费米子反对易关系出发，证明每个轨道的占据数只能是 0 或 1。

<details markdown="1"><summary>点击显示答案</summary>

分两步。**第一步**，Pauli 不相容：反对易关系 $\{c_\alpha^\dagger,c_\alpha^\dagger\}=0$ 展开即

$$\{c_\alpha^\dagger,c_\alpha^\dagger\} = c_\alpha^\dagger c_\alpha^\dagger + c_\alpha^\dagger c_\alpha^\dagger = 2(c_\alpha^\dagger)^2 = 0 \;\Longrightarrow\; (c_\alpha^\dagger)^2 = 0.$$

对任何态 $\lvert\Phi\rangle$，$(c_\alpha^\dagger)^2\lvert\Phi\rangle = 0$：在同一轨道放两个费米子得到零矢量，双占据态不存在。**第二步**，占据数算符的谱：利用 $\{c,c^\dagger\}=1$ 即 $cc^\dagger = 1 - c^\dagger c$，

$$\hat n^2 = c^\dagger c\,c^\dagger c = c^\dagger(1 - c^\dagger c)c = c^\dagger c - (c^\dagger)^2 c^2 = c^\dagger c = \hat n,$$

其中用了 $(c^\dagger)^2 = c^2 = 0$。设 $\hat n\lvert n\rangle = n\lvert n\rangle$，则 $\hat n^2\lvert n\rangle = n^2\lvert n\rangle$，而 $\hat n^2 = \hat n$ 给出 $n^2 = n$，故 $n=0$ 或 $n=1$。两个本征态都存在：$\lvert0\rangle$（真空）与 $\lvert1\rangle = c^\dagger\lvert0\rangle$，且 $\hat n\lvert1\rangle = c^\dagger c c^\dagger\lvert0\rangle = c^\dagger(1-c^\dagger c)\lvert0\rangle = c^\dagger\lvert0\rangle = \lvert1\rangle$。费米子单模 Hilbert 空间是二维的，与玻色子（无限维谐振子）形成对照。

</details>

**2.** 证明粒子数算符满足 $[\hat n, c^\dagger] = c^\dagger$、$[\hat n, c] = -c$，并解释这对易关系的物理意义。

<details markdown="1"><summary>点击显示答案</summary>

费米子情形用恒等式 $[AB,C] = A\{B,C\} - \{A,C\}B$：

$$[\hat n, c^\dagger] = [c^\dagger c, c^\dagger] = c^\dagger\{c,c^\dagger\} - \{c^\dagger,c^\dagger\}c = c^\dagger\cdot 1 - 0\cdot c = c^\dagger,$$

$$[\hat n, c] = [c^\dagger c, c] = c^\dagger\{c,c\} - \{c^\dagger,c\}c = 0 - 1\cdot c = -c.$$

玻色子情形用 $[AB,C]=A[B,C]+[A,C]B$ 与 $[a,a^\dagger]=1$，结果相同：$[\hat n,a^\dagger]=a^\dagger$，$[\hat n,a]=-a$。

**物理意义**：设 $\hat n\lvert n\rangle = n\lvert n\rangle$，则

$$\hat n\,(c^\dagger\lvert n\rangle) = \big([\hat n,c^\dagger] + c^\dagger\hat n\big)\lvert n\rangle = (1 + n)\,c^\dagger\lvert n\rangle,$$

即 $c^\dagger\lvert n\rangle$ 是 $\hat n$ 的本征态、本征值 $n+1$——$c^\dagger$ 把粒子数精确地**提升 1**。同理 $c$ 降低 1。这不是"碰巧如此"，而是产生湮灭算符的**定义性性质**：它们就是 $\hat n$（从而也是自由哈密顿量 $\hat H_0 = \sum_\alpha\varepsilon_\alpha\hat n_\alpha$）谱之间的升降梯，与谐振子里 $a^\dagger$ 爬升能级阶梯完全同构。同样方法可证 $[\hat N, c_\alpha^\dagger] = c_\alpha^\dagger$（$\hat N = \sum_\beta\hat n_\beta$），即每个产生算符把总粒子数提升 1。

</details>

**3.** 取两个电子的态 $\lvert\Phi\rangle = c_\alpha^\dagger c_\beta^\dagger\lvert0\rangle$ 与 $\lvert\Phi'\rangle = c_\gamma^\dagger c_\beta^\dagger\lvert0\rangle$（$\alpha,\beta,\gamma$ 互不相同），验证二次量子化单体算符 $\hat T = \sum_{\mu\nu}t_{\mu\nu}c_\mu^\dagger c_\nu$ 给出 $\langle\Phi|\hat T|\Phi\rangle = t_{\alpha\alpha}+t_{\beta\beta}$ 与 $\langle\Phi'|\hat T|\Phi\rangle = t_{\gamma\alpha}$，即一次量子化 Slater 行列式的 Slater–Condon 规则。

<details markdown="1"><summary>点击显示答案</summary>

核心是算真空期望值 $\langle0|c_\beta c_\alpha c_\mu^\dagger c_\nu c_\alpha^\dagger c_\beta^\dagger|0\rangle$。从最右边开始，反复用 $c_\nu c_\rho^\dagger = \delta_{\nu\rho} - c_\rho^\dagger c_\nu$ 与 $c_\rho\lvert0\rangle = 0$ 把湮灭算符逐个"搬"到真空上：

$$c_\nu c_\alpha^\dagger c_\beta^\dagger\lvert0\rangle = \delta_{\nu\alpha}c_\beta^\dagger\lvert0\rangle - \delta_{\nu\beta}c_\alpha^\dagger\lvert0\rangle.$$

再作用 $c_\alpha c_\mu^\dagger$：注意

$$c_\alpha c_\mu^\dagger c_\beta^\dagger\lvert0\rangle = \delta_{\alpha\mu}c_\beta^\dagger\lvert0\rangle - \delta_{\alpha\beta}c_\mu^\dagger\lvert0\rangle = \delta_{\alpha\mu}c_\beta^\dagger\lvert0\rangle,$$

（因 $\alpha\neq\beta$），同理 $c_\alpha c_\mu^\dagger c_\alpha^\dagger\lvert0\rangle = \delta_{\alpha\mu}c_\alpha^\dagger\lvert0\rangle - c_\mu^\dagger\lvert0\rangle$。合起来：

$$c_\alpha c_\mu^\dagger c_\nu c_\alpha^\dagger c_\beta^\dagger\lvert0\rangle = \delta_{\nu\alpha}\delta_{\alpha\mu}c_\beta^\dagger\lvert0\rangle - \delta_{\nu\beta}\delta_{\alpha\mu}c_\alpha^\dagger\lvert0\rangle + \delta_{\nu\beta}c_\mu^\dagger\lvert0\rangle.$$

最后作用 $c_\beta$ 并与 $\langle0|$ 收缩，用 $c_\beta c_\beta^\dagger\lvert0\rangle = \lvert0\rangle$、$c_\beta c_\alpha^\dagger\lvert0\rangle = 0$、$c_\beta c_\mu^\dagger\lvert0\rangle = \delta_{\beta\mu}\lvert0\rangle$：

$$\langle0|c_\beta c_\alpha c_\mu^\dagger c_\nu c_\alpha^\dagger c_\beta^\dagger|0\rangle = \delta_{\nu\alpha}\delta_{\mu\alpha} + \delta_{\nu\beta}\delta_{\mu\beta}.$$

代入得 $\langle\Phi|\hat T|\Phi\rangle = t_{\alpha\alpha} + t_{\beta\beta}$——正是 Slater 行列式 $\langle\alpha(1)\beta(2)|t_1+t_2|\alpha(1)\beta(2)\rangle$ 的结果（单体算符无交换项）。

对 $\langle\Phi'|\hat T|\Phi\rangle$，同样的搬运（把 $\alpha$ 换成 $\gamma$）给出

$$\langle0|c_\beta c_\gamma c_\mu^\dagger c_\nu c_\alpha^\dagger c_\beta^\dagger|0\rangle = \delta_{\nu\alpha}\delta_{\mu\gamma},$$

（其余三项因 $\gamma\neq\alpha,\beta$ 全部消失），故 $\langle\Phi'|\hat T|\Phi\rangle = t_{\gamma\alpha} = \langle\gamma|t|\alpha\rangle$。

**这就是 Slater–Condon 规则的雏形**：两个行列式只差一个自旋轨道（$\alpha\to\gamma$）时，单体算符矩阵元等于该替换轨道的单粒子矩阵元，"旁观"轨道 $\beta$ 无贡献；相差两个及以上轨道时矩阵元为零（同法可证）。这条规则是[第 14 章](14-exact-methods-fci-ed.md) FCI/ED 在行列式基下组装哈密顿量矩阵的基本构件——那里每个矩阵元都是这样一场产生湮灭算符的搬运游戏。

</details>

**4.** 用二次量子化语言计算自由电子气（$\hat H_0 = \sum_{\vec k\sigma}\varepsilon_{\vec k}\hat n_{\vec k\sigma}$，$\varepsilon_{\vec k}=k^2/2m$）的基态总能量，证明 $E_0 = \frac35 N\varepsilon_F$。

<details markdown="1"><summary>点击显示答案</summary>

$\hat H_0$ 与所有 $\hat n_{\vec k\sigma}$ 对易，基态就是占据数本征态中能量最低者。由 Pauli 原理每个 $(\vec k,\sigma)$ 至多占一个电子，故从能量最低的模开始向上填，直到填完 $N$ 个电子——在动量空间填满半径 $k_F$ 的费米球：

$$\lvert\text{FS}\rangle = \prod_{\lvert\vec k\rvert<k_F,\;\sigma}c_{\vec k\sigma}^\dagger\lvert0\rangle, \qquad \hat H_0\lvert\text{FS}\rangle = E_0\lvert\text{FS}\rangle, \qquad E_0 = \sum_{\lvert\vec k\rvert<k_F,\;\sigma}\frac{k^2}{2m}.$$

热力学极限下把求和换积分，$\sum_{\vec k} \to V\displaystyle\int\frac{d^3k}{(2\pi)^3}$，自旋因子 2：

$$E_0 = 2V\int_{\lvert\vec k\rvert<k_F}\frac{d^3k}{(2\pi)^3}\,\frac{k^2}{2m} = \frac{2V}{(2\pi)^3}\cdot\frac{4\pi}{2m}\int_0^{k_F}k^4\,dk = \frac{V k_F^5}{10\pi^2 m}.$$

电子总数同理：

$$N = 2V\int_{\lvert\vec k\rvert<k_F}\frac{d^3k}{(2\pi)^3} = \frac{V k_F^3}{3\pi^2} \qquad\Big(\text{即 } k_F = (3\pi^2 n)^{1/3}\Big).$$

两式相除：

$$\frac{E_0}{N} = \frac{k_F^5/(10\pi^2 m)}{k_F^3/(3\pi^2)} = \frac{3k_F^2}{10m} = \frac35\cdot\frac{k_F^2}{2m} = \frac35\,\varepsilon_F, \qquad \varepsilon_F \equiv \frac{k_F^2}{2m}.$$

平均每个电子的能量是费米能的 $3/5$——不是 0！这就是[第 3 章](03-free-electron-gas.md) Sommerfeld 理论的出发点：Pauli 原理迫使电子堆到 $\varepsilon_F$（典型金属几个 eV，对应 $T_F\sim 10^4$ K），自由电子气是高度简并的量子液体。恢复 $\hbar$ 只需 $\varepsilon_F = \hbar^2 k_F^2/2m$。整个推导里"填费米球"这个一次量子化里需要论证一步的操作，在二次量子化中只是"能量最低的占据数构型"一句废话——新语言的记账优势可见一斑。

</details>

**5.** 写出箱归一化（体积 $V$）下场算符与动量空间算符的互变关系，并证明（反）对易关系在两个表象之间互相蕴含。

<details markdown="1"><summary>点击显示答案</summary>

平面波基 $\varphi_{\vec k}(\vec x) = e^{i\vec k\cdot\vec x}/\sqrt V$（周期边界条件，$\vec k = 2\pi\vec n/V^{1/3}$ 离散取值），互变关系为一对傅里叶变换：

$$\hat\psi(\vec x) = \frac{1}{\sqrt V}\sum_{\vec k}e^{i\vec k\cdot\vec x}\,c_{\vec k}, \qquad c_{\vec k} = \frac{1}{\sqrt V}\int d^3x\;e^{-i\vec k\cdot\vec x}\,\hat\psi(\vec x).$$

**从场算符代数到动量代数**：设 $[\hat\psi(\vec x),\hat\psi^\dagger(\vec x')]_\mp = \delta(\vec x-\vec x')$，则

$$[c_{\vec k}, c_{\vec k'}^\dagger]_\mp = \frac{1}{V}\int d^3x\,d^3x'\;e^{-i\vec k\cdot\vec x + i\vec k'\cdot\vec x'}[\hat\psi(\vec x),\hat\psi^\dagger(\vec x')]_\mp = \frac{1}{V}\int d^3x\;e^{-i(\vec k-\vec k')\cdot\vec x} = \delta_{\vec k\vec k'},$$

末步用了正交性 $\frac1V\int_V d^3x\,e^{i\vec q\cdot\vec x} = \delta_{\vec q,0}$（离散 $\vec k$）。**反过来**，设 $[c_{\vec k},c_{\vec k'}^\dagger]_\mp = \delta_{\vec k\vec k'}$，则

$$[\hat\psi(\vec x),\hat\psi^\dagger(\vec x')]_\mp = \frac{1}{V}\sum_{\vec k\vec k'}e^{i\vec k\cdot\vec x - i\vec k'\cdot\vec x'}[c_{\vec k},c_{\vec k'}^\dagger]_\mp = \frac{1}{V}\sum_{\vec k}e^{i\vec k\cdot(\vec x-\vec x')} = \delta(\vec x-\vec x'),$$

末步用了完备性 $\frac1V\sum_{\vec k}e^{i\vec k\cdot\vec r} = \delta(\vec r)$（$V\to\infty$ 时 $\frac1V\sum_{\vec k}\to\int\frac{d^3k}{(2\pi)^3}$，化为标准的 $\delta$ 函数傅里叶表示）。

**要点**：对易（玻色）还是反对易（费米）这个"统计标签"在表象变换下不变——它属于粒子本身，不属于基。正因如此，任何表象的选择都只是为方便服务：动能对角的动量基（凝胶模型）、相互作用对角的格点基（Hubbard 模型），随时傅里叶变换切换，代数结构原封不动。这也是"二次量子化算符与 $N$ 无关、只与基无关的代数有关"这一精神的体现。

</details>

## 参考

- Fetter & Walecka《Quantum Theory of Many-Particle Systems》第 1 章（Second Quantization）——Fock 空间、产生湮灭算符与算符翻译规则的系统推导，本章的主参考。
- Mahan《Many-Particle Physics》第 3 版第 1 章（Introductory Material）——二次量子化与 Green 函数的衔接，风格直截了当。
- Bruus & Flensberg《Many-Body Quantum Theory in Condensed Matter Physics》第 1–2 章——凝聚态导向的现代表述，电子、声子、光子的产生湮灭算符统一处理。
- Schrieffer《Theory of Superconductivity》附录——场算符形式的 BCS 理论原文用法，可与[超导](08-superconductivity.md)一章对照。
- 交叉参考：QFT 书笔记[谐振子阶梯算符](../../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)（代数方法的单模热身）、[标量场正则量子化](../../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)（同一代数在场论中的再次出现）。
