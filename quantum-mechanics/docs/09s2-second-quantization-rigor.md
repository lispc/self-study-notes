# 补充材料：二次量子化严格吗——表示唯一性、有界性与无穷自由度的坑

> 路线图位置：量子力学书 · 第四部分（多体语言）· 第 09 篇（[二次量子化](09-second-quantization.md)）的补充材料（第 09s2 篇），在第 09 篇与[第 09s 篇](09s-fermi-dirac-derivation.md)之后读。
> 前置知识：第 09 篇（Fock 空间构造、产生湮灭算符、CAR/CCR 与算符翻译规则）；[第 05s 篇](05s-identical-particles.md)（全同粒子与对称化公设）。
> 学习目标：会从 CAR/CCR 出发计算产生湮灭算符的范数，说清"费米子有界、玻色子无界但受控"的确切含义；能陈述 Stone–von Neumann 定理与 Jordan–Wigner 定理并指出各自依赖的条件；能说清无穷自由度下表示唯一性为何失效（van Hove 现象、Haag 定理），以及为什么这些坑属于 QFT 而不属于有限 $N$ 多体物理。

---

**单位约定**：本篇按本书笔记惯例取自然单位 $\hbar = c = 1$（首次出现特此说明）。

## 1. 一句话总结

**有限自由度下，二次量子化的全部内容都是定理：Fock 空间是从单粒子 Hilbert 空间出发的显式构造（不是假设），产生湮灭算符是其上良定的线性算符（费米子情形还是有界算符），且满足 CAR/CCR 的有限自由度不可约表示在幺正等价意义下唯一（玻色子靠 Stone–von Neumann 定理，费米子靠 Jordan–Wigner 定理）——所以"多体 ≡ 满足（反）对易关系的算符代数"不是约定而是定理，教科书从代数关系出发推导一切完全合法；"把波函数变成算符"只是启发性口诀，从来不是定义。真正不严格的只有无穷自由度（连续场论）：不等价表示泛滥、Haag 定理禁止相互作用绘景——"胡编感"唯一有正当理由的地方在 QFT（见 QFT 书[构造性场论与四维 $\phi^4$ 的平凡性](../../qft-sm/docs/stage-04-qft-core/08-constructive-qft-triviality.md)），而不在有限 $N$ 的多体量子力学。**

## 2. 已经是定理的部分：构造与良定性

先回顾[第 09 篇](09-second-quantization.md)第 3 节做过的事（这里不重复细节）：给定单粒子 Hilbert 空间 $\mathcal H_1$ 与一组完备基，Fock 空间被**显式地定义**为各粒子数扇区的直和

$$\mathcal F = \mathcal H_0 \oplus \mathcal H_1 \oplus \mathcal H_2^{(s/a)} \oplus \cdots \oplus \mathcal H_N^{(s/a)} \oplus \cdots,$$

其中 $\mathcal H_N^{(s/a)}$ 是 $N$ 重张量积的（反）对称化子空间，产生湮灭算符被显式地定义为这些扇区之间的线性映射。整个构造的输入只有两条：单粒子量子力学，以及[对称化公设](05s-identical-particles.md)。没有任何一步依赖"类比""启发"或"再量子化一次"。怀疑论者能质疑的只剩两件事：这些算符作为 Hilbert 空间上的线性算符是否**良定**（本节），以及这套代数是否还有别的、物理上不同的实现（第 3 节）。

### 2.1 涂抹记号

为把两种统计写得整齐，引入**涂抹（smeared）记号**：$a^\dagger(f)$ 表示"在单粒子态 $\lvert f\rangle \in \mathcal H_1$ 上产生一个粒子"，它对 $f$ 线性；其伴算符 $a(f)$ 湮灭该态上的粒子，对 $f$ 反线性。在任意基 $\{\varphi_\alpha\}$ 下 $a^\dagger(f) = \sum_\alpha\langle\varphi_\alpha\rvert f\rangle\,a_\alpha^\dagger$。两种统计的代数关系写成

$$\{a(f), a^\dagger(g)\} = \langle f\rvert g\rangle \quad(\text{CAR}), \qquad [a(f), a^\dagger(g)] = \langle f\rvert g\rangle \quad(\text{CCR}),$$

其余组合的（反）对易子为零。分立记号 $a_\alpha = a(\varphi_\alpha)$ 只是 $\lVert\varphi_\alpha\rVert = 1$ 的特例。

### 2.2 费米子：有界算符

由 CAR 取 $g = f$：

$$a(f)a^\dagger(f) + a^\dagger(f)a(f) = \lVert f\rVert^2 \;\Longrightarrow\; a(f)a^\dagger(f) = \lVert f\rVert^2 - a^\dagger(f)a(f) \le \lVert f\rVert^2,$$

最后一步是正算符意义下的不等式：$a^\dagger(f)a(f) \ge 0$（伴算符与自身的乘积恒非负），减掉一个正算符只会更小。两边取算符范数（正算符 $B \le c\,\mathbb 1$ 蕴含 $\lVert B\rVert \le c$），并用 **C*-恒等式** $\lVert A^\dagger A\rVert = \lVert A\rVert^2$（任意有界算符成立）：

$$\lVert a(f)\rVert^2 = \lVert a(f)a^\dagger(f)\rVert \le \lVert f\rVert^2 \;\Longrightarrow\; \lVert a(f)\rVert \le \lVert f\rVert.$$

等号在真空上取得：由 $a(f)\lvert0\rangle = 0$ 有 $a(f)a^\dagger(f)\lvert0\rangle = \lVert f\rVert^2\,\lvert0\rangle$，于是

$$\lVert a^\dagger(f)\lvert0\rangle\rVert^2 = \langle0\rvert a(f)a^\dagger(f)\lvert0\rangle = \lVert f\rVert^2,$$

即 $\lVert a^\dagger(f)\rVert \ge \lVert f\rVert$。结合上界与 $\lVert A^\dagger\rVert = \lVert A\rVert$，得到干净的结果

$$\lVert a(f)\rVert = \lVert a^\dagger(f)\rVert = \lVert f\rVert.$$

**费米子的产生湮灭算符是有界算符**，定义在整个 Fock 空间上，没有任何定义域麻烦。正因如此，有限模费米子代数（CAR 代数）是一个货真价实的 C*-代数，范数估计、取极限、谱理论的全套工具随意使用——这是有限 $N$ 费米子问题在数学上温顺的根本原因之一。

### 2.3 玻色子：无界，但受数算符控制

玻色子情形不同。取归一单模 $\lVert f\rVert = 1$，在其 $n$ 粒子态 $\lvert n_f\rangle = (a^\dagger(f))^n/\sqrt{n!}\,\lvert0\rangle$ 上

$$\lVert a^\dagger(f)\lvert n_f\rangle\rVert = \sqrt{n+1},$$

随 $n$ 无界增长，故 $a(f), a^\dagger(f)$ **无界**——不存在对所有态一致成立的范数上界。无界不等于病态：单粒子量子力学里的 $\hat x, \hat p$ 同样无界，要紧的是定义域受控。玻色算符的控制工具是**数算符界**

$$a^\dagger(f)a(f) \le \lVert f\rVert^2\,\hat N \;\Longrightarrow\; \lVert a(f)\psi\rVert \le \lVert f\rVert\,\lVert\hat N^{1/2}\psi\rVert$$

（推导概要：把 $f/\lVert f\rVert$ 取作基的第一个矢量，则 $a^\dagger(f)a(f) = \lVert f\rVert^2\,\hat n_1 \le \lVert f\rVert^2\,\hat N$；详细版见自检问题 2）。配合 CCR $a(f)a^\dagger(f) = a^\dagger(f)a(f) + \lVert f\rVert^2$ 还有对偶估计 $\lVert a^\dagger(f)\psi\rVert \le \lVert f\rVert\,\lVert(\hat N+1)^{1/2}\psi\rVert$。于是在**有限粒子数态构成的稠密集**上，一切乘积、交换子、真空期望值都良定——物理上关心的态（有限能量、有限粒子数的任意叠加）都躺在这个稠密集里。

| | 费米子 | 玻色子 |
|---|---|---|
| 代数关系 | $\{a(f),a^\dagger(g)\} = \langle f\rvert g\rangle$ | $[a(f),a^\dagger(g)] = \langle f\rvert g\rangle$ |
| 范数 | $\lVert a(f)\rVert = \lVert f\rVert$，有界 | $\lvert n_f\rangle$ 上 $\sim\sqrt n$，无一致上界 |
| 定义域 | 整个 Fock 空间 | 有限粒子数态的稠密集 |
| 控制工具 | 不需要（本身就是 C*-代数元） | 数算符界 $\lVert a(f)\psi\rVert \le \lVert f\rVert\,\lVert\hat N^{1/2}\psi\rVert$ |

最后正名一句："二次量子化"这个名字是历史偶然——[第 09 篇](09-second-quantization.md)第 2 节已经点破，没有任何东西被量子化了两次，只是一次量子化波函数的展开系数被提升为算符。本篇关心的不是名字，而是代数层面的严格性：构造已良定，下一个问题是**唯一性**。

## 3. 唯一性定理："对易关系定全部"

[第 09 篇](09-second-quantization.md)把 Fock 表示当作定义来用。一个合理的怀疑是：CAR/CCR 会不会还有别的、不等价的表示，使得"从（反）对易关系出发推导一切"暗中依赖了表示的选择，从而沦为循环论证？有限自由度下，两个定理给出干脆的否定回答。

### 3.1 Stone–von Neumann 定理（正则对易关系）

先把对易关系改写成 **Weyl 形式**。$n$ 个自由度的 $\hat x_j, \hat p_j$ 满足 $[\hat x_j, \hat p_k] = i\delta_{jk}$，定义酉算符

$$U(\vec a) = e^{i\vec a\cdot\hat{\vec x}}, \qquad V(\vec b) = e^{i\vec b\cdot\hat{\vec p}},$$

由 Baker–Campbell–Hausdorff 公式（对易子是中心元，级数两项即截断）得 Weyl 关系

$$U(\vec a)\,V(\vec b) = e^{-i\vec a\cdot\vec b}\,V(\vec b)\,U(\vec a).$$

**Stone–von Neumann 定理**：有限 $n$ 个自由度的 Weyl 关系的任意两个不可约、强连续（即 $\vec a\to0$ 时 $U(\vec a)$ 连续地趋于恒等）酉表示都幺正等价；特别地，它们都等价于 $L^2(\mathbb R^n)$ 上的 Schrödinger 表示 $(\hat x_j\psi)(\vec x) = x_j\psi(\vec x)$、$(\hat p_j\psi)(\vec x) = -i\partial_j\psi(\vec x)$。

两个物理推论：

- **表象自由**：坐标表象与动量表象是同一 Weyl 代数的两个不可约表示，定理保证它们之间只差一个幺正变换（正是傅里叶变换），选哪个都不含物理。多体理论里"换基只是方便"的底气来自同一逻辑。
- **正则量子化的唯一性**："正则对易关系 $[\hat x,\hat p]=i$ 唯一确定量子力学"这句话，在有限自由度是**定理**而非信仰——代数关系给定后，表示在幺正等价意义下没有选择余地，而幺正等价的表示给出逐字相同的物理预言。

**为什么必须用 Weyl 形式**：裸对易关系 $[\hat x,\hat p]=i$ 强迫至少一个算符无界——若两者都有界，由 $[\hat x,\hat p^n] = in\,\hat p^{n-1}$ 取范数得 $n\lVert\hat p^{n-1}\rVert \le 2\lVert\hat x\rVert\,\lVert\hat p\rVert\,\lVert\hat p^{n-1}\rVert$，即 $n \le 2\lVert\hat x\rVert\,\lVert\hat p\rVert$ 对一切 $n$ 成立，矛盾。无界算符带来定义域病态：确实存在满足裸对易关系却不等价于 Schrödinger 表示的"怪表示"。指数化成有界酉算符、再要求强连续性（正则性），这些病态被全部排除。唯一性定理的真正前提是：**Weyl 形式 + 正则性 + 有限自由度**。记住最后一条，它是通往第 4 节的钩子。

### 3.2 Jordan–Wigner 定理（反对易关系）

**Jordan–Wigner 定理**：有限 $n$ 个模的 CAR 的不可约表示在幺正等价意义下唯一，就是 Fock 表示。

证明思路（三步）：

1. **正规序化**：用 CAR $\{a_\alpha, a_\beta^\dagger\} = \delta_{\alpha\beta}$，任意由 $a_\alpha, a_\alpha^\dagger$ 组成的单项式都可重排为正规序（产生算符全在左）单项式的线性组合，系数完全由代数关系决定。
2. **矩阵元全部归于真空**：在任何带真空（被所有 $a_\alpha$ 湮灭的态 $\lvert0\rangle$）的不可约表示里，基矢 $\prod_\alpha(a_\alpha^\dagger)^{n_\alpha}\lvert0\rangle$ 之间的任意矩阵元，经正规序化后只剩恒等项的真空期望值存活，而它被归一化钉死在 $\langle0\rvert0\rangle = 1$。**一切矩阵元由代数关系唯一算出，与表示无关。**
3. **建立保持矩阵元的酉映射**：给定两个不可约表示 $(\mathcal H,\pi)$ 与 $(\mathcal H',\pi')$，把 $\pi(a_{\alpha_1}^\dagger\cdots a_{\alpha_k}^\dagger)\lvert0\rangle$ 映到 $\pi'(a_{\alpha_1}^\dagger\cdots a_{\alpha_k}^\dagger)\lvert0'\rangle$。两边内积由同一代数算出、逐字相同，故此映射保内积，延拓为酉算符 $U$；不可约性保证这些基矢张满，且按构造 $U\,\pi(A) = \pi'(A)\,U$ 对代数中一切 $A$ 成立——两个表示幺正等价。$\square$

一个等价看法：有限 $n$ 模的 CAR 代数其实是有限维的——Jordan–Wigner 弦构造把它实现为 $n$ 个量子比特上全体 $2^n\times2^n$ 矩阵的代数 $M_{2^n}(\mathbb C)$，而全矩阵代数的不可约表示唯一。玻色子没有这条捷径（哪怕单模 Weyl 代数也是无穷维的），所以 Stone–von Neumann 定理才需要正则性这个分析条件。

### 3.3 物理含义与条件清单

唯一性定理为教科书写法背书：从（反）对易关系出发推导一切（占据数、矩阵元、统计、算符翻译规则）在有限自由度下**不是循环论证**，因为根本不存在第二种表示；选择表象（坐标/动量/Fock）纯粹是方便。条件清单再强调一遍：Weyl 形式（绕开无界定义域病态）、正则性、**自由度有限**。前两条是技术性的，第三条是物理的——把它撤掉，下一节就是事故现场。

## 4. 无穷自由度：唯一性死亡现场

模数从有限变成可数无穷的那一刻，唯一性定理的前提失效，不等价的不可约表示立刻泛滥——对无穷多模的 CCR/CAR，存在不可数无穷多个两两幺正不等价的不可约表示。这不是抽象恐吓，一个玩具模型就能看清全部机理。

### 4.1 van Hove 现象：两个"真空"正交

单模相干态（位移真空）$\lvert\alpha\rangle = e^{-\lvert\alpha\rvert^2/2}\,e^{\alpha a^\dagger}\lvert0\rangle$ 与真空的内积是 $e^{-\lvert\alpha\rvert^2/2}$（自检问题 4 逐步读出）。取 $M$ 个模、每个模做位移 $\alpha_k$，多模相干态与真空的重叠是各模之积：

$$\langle0\rvert\{\alpha_k\}\rangle = \exp\Big(-\frac12\sum_{k=1}^{M}\lvert\alpha_k\rvert^2\Big).$$

有限 $M$ 时这只是个很小的数；极限 $M\to\infty$ 见分晓：

- 若 $\sum_k\lvert\alpha_k\rvert^2 \lt \infty$（例如 $\alpha_k = \lambda/k$），重叠趋于一个**非零**常数——位移"温和"，两个表示等价（这正是位移型变换可被幺正实现的判据）；
- 若 $\sum_k\lvert\alpha_k\rvert^2 = \infty$（例如 $\alpha_k = \lambda/\sqrt k$），重叠**严格为零**——新"真空"与旧真空正交；更有甚者，建立在新真空上的整个激发态塔与旧 Fock 空间的每个态都正交。两个表示活在互不相交的 Hilbert 空间里，任何幺正映射（它必须保内积）都不可能把真空映过去。

这就是 **van Hove 现象**（van Hove, 1952）：无穷自由度系统中，"另一个哈密顿量的基态"可以根本不在你原来的 Fock 空间里。它不是奇谈，而是反复出现的物理：

- **Anderson 正交灾难**（1967）：金属费米海在有、无一个杂质势两种情形下的基态重叠随电子数幂次衰减，$\sim N^{-\eta}$（$\eta$ 由各分波费米面相移决定，s 波情形 $\eta = (\delta_0/\pi)^2$）——热力学极限下严格正交，尽管每个单粒子态几乎没变。
- **红外灾难**：带电粒子散射辐射无穷多个软光子，每个软模被轻微位移——正是上面的玩具；累积位移平方和在红外端发散（量级估计 $\sum_k\lvert\alpha_k\rvert^2 \sim \alpha\int_0 dk/k$），所以严格的渐近态不在裸 Fock 空间里，而是裹着相干光子云的态（Bloch–Nordsieck 处理）。

### 4.2 Haag 定理：相互作用绘景不存在

无穷自由度最锋利的一刀是 **Haag 定理**（1955）。精确陈述：

> 在满足标准公理（庞加莱协变性、唯一真空、正能量谱、局域性）的相对论性量子场论中，若某一时刻的场 $\phi(\vec x,t)$ 经幺正变换与同一时刻的自由场相联系，$\phi(\vec x,t) = U\,\phi_0(\vec x,t)\,U^{-1}$，则 $\phi$ 本身就是自由场——它的一切真空期望值与自由场相同，$S$ 矩阵平凡。

而"某时刻的相互作用场与自由场幺正相联"正是**相互作用绘景**（微扰论的脚手架）的基本要求。结论因而是毁灭性的：**严格意义下，非平凡的相对论性场论里相互作用绘景不存在**；教科书里的微扰展开是在带截断的理论上逐阶操作的形式级数，"取连续极限"那一跃没有任何存在性定理担保。

注意 Haag 定理的前提一条条都不可或缺，绕开它的标准办法是**截断**：有限体积（动量离散化）加紫外截断（格点）使自由度有限，Stone–von Neumann 定理重新生效，相互作用绘景完全合法——所以格点场论是良定的数学对象，全部困难被推到"取连续极限"这一步。这与第 4.1 节是同一枚硬币的两面：有限自由度万事大吉，无穷自由度群魔乱舞。

### 4.3 严格化的语言：C*-代数与 GNS 构造

面对表示不唯一，数学物理的答案是**把代数与表示分家**：

- **代数是绝对的**：CCR/CAR（更一般地，各时空区域的局域可观测量的 C*-代数）是唯一给定的对象，不依赖任何表示。
- **表示依赖于态**：每个态（正归一线性泛函 $\omega$，即一套自洽的期望值规则）经 **GNS 构造**生成自己的 Hilbert 空间、表示与循环矢量。真空给一个表示，有限温度平衡态（KMS 态）给另一个，不同的相再给别的——它们一般互不等价，但**每一个都合法**。热力学极限 $N,V\to\infty$（$N/V$ 固定）必须在代数与关联函数的层面取，而不是抱着一个固定的 Fock 空间不撒手——这正是 van Hove 现象的教训。

这条路线的标准参考书是 Bratteli–Robinson 两卷（见文末参考）。对本书读者，最值得记住的推论是正面的：**有限格点上的模型（如有限格点 Hubbard 模型）自由度永远有限，二次量子化语言连同唯一性定理全套适用，完全严格**——精确对角化、DMRG 之类方法立足于此。需要小心的只有两件事：连续极限与无穷体积极限。

### 4.4 指针：哪些场论真的存在

Haag 定理关上一扇门，构造性场论问的是反向的问题：连续相对论性场论里到底哪些理论**真的存在**？二维、三维的 $\phi^4$ 被严格构造出来，四维 $\phi^4$ 反而被证明不存在（平凡性），四维 Yang–Mills 的存在性与质量间隙则是千禧年难题——这条完整故事线是 QFT 书第 4 阶段 [08 篇：构造性场论与四维 $\phi^4$ 的平凡性](../../qft-sm/docs/stage-04-qft-core/08-constructive-qft-triviality.md) 的主题。本篇只需带走结论：**二次量子化"不严格"的指控，唯一成立的部分属于连续场论，不属于有限 $N$ 的多体量子力学。**

## 小结

- Fock 空间与产生湮灭算符是显式构造；由 CAR 可证费米子算符有界，$\lVert a(f)\rVert = \lVert a^\dagger(f)\rVert = \lVert f\rVert$，CAR 代数是货真价实的 C*-代数。
- 玻色子算符无界（$\lvert n_f\rangle$ 上范数 $\sim\sqrt n$），但有数算符界 $\lVert a(f)\psi\rVert \le \lVert f\rVert\,\lVert\hat N^{1/2}\psi\rVert$，在有限粒子数态的稠密集上良定——无界不是病态，定义域受控即可。
- 有限自由度下表示唯一：玻色子靠 Stone–von Neumann 定理（Weyl 形式 + 正则性），费米子靠 Jordan–Wigner 定理（正规序化把一切矩阵元归于真空）——"从对易关系推一切"是定理不是约定，表象选择只是方便。
- 无穷自由度唯一性死亡：van Hove 现象（位移平方和发散时两真空正交、Fock 空间互不相交）；Anderson 正交灾难与红外灾难是同一机理的物理化身。
- Haag 定理：相对论性场论中相互作用绘景严格不存在；有限体积 + 紫外截断使自由度有限、定理前提失效，故格点理论合法，困难只在连续极限。
- 严格化语言是 C*-代数 + GNS 构造（代数绝对、表示随态、热力学极限在代数层面取）；有限 $N$、有限格点的多体物理全套严格，"不严格"只属于连续场论——见 QFT 书 [08 篇](../../qft-sm/docs/stage-04-qft-core/08-constructive-qft-triviality.md)。

## 自检问题

**1.** 仅从 CAR 出发，证明费米子湮灭算符是有界算符，且范数恰为 $\lVert a(f)\rVert = \lVert f\rVert$。

<details markdown="1"><summary>点击显示答案</summary>

**上界**：CAR 取 $g = f$ 得 $a(f)a^\dagger(f) + a^\dagger(f)a(f) = \lVert f\rVert^2$，移项

$$a(f)a^\dagger(f) = \lVert f\rVert^2 - a^\dagger(f)a(f) \le \lVert f\rVert^2,$$

不等式在正算符意义下成立（$a^\dagger(f)a(f) \ge 0$）。取算符范数，用 C*-恒等式 $\lVert A^\dagger A\rVert = \lVert A\rVert^2$（取 $A = a^\dagger(f)$）与 $\lVert A^\dagger\rVert = \lVert A\rVert$：

$$\lVert a(f)\rVert^2 = \lVert a^\dagger(f)\rVert^2 = \lVert a(f)a^\dagger(f)\rVert \le \lVert f\rVert^2.$$

**等号**：真空上 $a(f)\lvert0\rangle = 0$，故 $a(f)a^\dagger(f)\lvert0\rangle = \lVert f\rVert^2\,\lvert0\rangle$，于是

$$\lVert a^\dagger(f)\lvert0\rangle\rVert^2 = \langle0\rvert a(f)a^\dagger(f)\lvert0\rangle = \lVert f\rVert^2 \;\Longrightarrow\; \lVert a^\dagger(f)\rVert \ge \lVert f\rVert.$$

两方向合并即 $\lVert a(f)\rVert = \lVert a^\dagger(f)\rVert = \lVert f\rVert$。

**对照玻色子**：同法在 CCR 下会卡住——$a(f)a^\dagger(f) = a^\dagger(f)a(f) + \lVert f\rVert^2$ 右端两项**相加**，得不到上界。这个符号差别（反对易子移项相减、对易子移项相加）正是"费米子有界、玻色子无界"的代数根源。

</details>

**2.** 证明玻色子的数算符界 $\lVert a(f)\psi\rVert \le \lVert f\rVert\,\lVert\hat N^{1/2}\psi\rVert$，并解释为什么玻色算符只能在稠密集上定义。

<details markdown="1"><summary>点击显示答案</summary>

**证明**：把 $\varphi_1 = f/\lVert f\rVert$ 取作正交归一基的第一个矢量（任一单位矢量都可扩成完备正交基）。$a(f)$ 对 $f$ 反线性而 $\lVert f\rVert$ 为实数，故 $a(f) = \lVert f\rVert\,a_1$（$a_1 \equiv a(\varphi_1)$），于是

$$a^\dagger(f)a(f) = \lVert f\rVert^2\,a_1^\dagger a_1 = \lVert f\rVert^2\,\hat n_1 \le \lVert f\rVert^2\,\hat N,$$

因为 $\hat N = \sum_\alpha\hat n_\alpha$ 的各项非负，在共同本征态上逐项比较即得 $\hat n_1 \le \hat N$。因此

$$\lVert a(f)\psi\rVert^2 = \langle\psi\rvert a^\dagger(f)a(f)\lvert\psi\rangle \le \lVert f\rVert^2\,\langle\psi\rvert\hat N\lvert\psi\rangle = \lVert f\rVert^2\,\lVert\hat N^{1/2}\psi\rVert^2,$$

开方即所证。等价地，可在 $\hat N$ 的本征态上用 CCR 重排 $a(f)a^\dagger(f) = a^\dagger(f)a(f) + \lVert f\rVert^2$ 配合"$a$ 精确降一个粒子"来估计，结论相同；对偶地还有 $\lVert a^\dagger(f)\psi\rVert \le \lVert f\rVert\,\lVert(\hat N+1)^{1/2}\psi\rVert$。

**为何只能稠密定义**：取单模 $n$ 粒子态 $\lvert n_f\rangle$，有 $\lVert a^\dagger(f)\lvert n_f\rangle\rVert = \sqrt{n+1}\,\lVert f\rVert$，随 $n$ 无界增长——不存在常数 $C$ 使 $\lVert a^\dagger(f)\psi\rVert \le C\lVert\psi\rVert$ 对一切 $\psi$ 成立，故算符无界、不能定义在整个 Fock 空间上。但数算符界表明：只要 $\lVert\hat N^{1/2}\psi\rVert \lt \infty$（粒子数分布衰减足够快），$a(f)\psi$ 就良定。有限粒子数态的有限线性组合全体就是这样的定义域，而它在 Fock 空间中稠密（任意态可被"只保留前 $N$ 个粒子"的截断态任意逼近）。与 $\hat x, \hat p$ 在 $L^2$ 中只能稠密定义完全同类——无界算符的常规生态，不是病态。

</details>

**3.** 用 Stone–von Neumann 定理解释：(a) 为什么坐标表象与动量表象给出相同物理；(b) 为什么"正则量子化规则 $[\hat x,\hat p]=i$ 唯一确定量子理论"在有限自由度是定理、在场论中失效。

<details markdown="1"><summary>点击显示答案</summary>

**(a)** 坐标表象（$\hat x$ 为乘法、$\hat p = -i\partial_x$）与动量表象（$\hat p$ 为乘法、$\hat x = i\partial_p$）都是同一 $n$ 自由度 Weyl 关系 $U(\vec a)V(\vec b) = e^{-i\vec a\cdot\vec b}V(\vec b)U(\vec a)$ 的不可约正则表示（不可约：与全体 $U, V$ 都对易的算符只能是常数；正则：表示显然强连续）。Stone–von Neumann 定理断言这类表示唯一，故存在幺正映射联系两者——正是傅里叶变换 $\mathcal F$。幺正等价的表示保持一切内积、矩阵元与谱，物理预言逐字相同，选表象只是计算方便。依赖的条件：Weyl 形式（有界酉算符）、正则性、有限自由度。

**(b) 有限自由度**：$[\hat x,\hat p]=i$ 经 Weyl 指数化后等价于 Weyl 关系，而定理说其不可约正则表示唯一——所以"正则对易关系唯一确定量子理论"（在幺正等价、即物理等价意义下）是**定理**。依赖条件同上，缺一不可：丢 Weyl 形式就有无界算符的定义域怪表示；丢正则性定理失效；丢有限自由度则见下。

**场论（无穷自由度）**：第三个条件——自由度有限——失效。CCR/CAR 出现不可数多个幺正不等价的不可约表示（§4.1 的 van Hove 玩具演示了机理），裸对易关系本身不再能选定物理：还必须额外指定**表示**，等价于指定真空或态，而这是动力学问题，不同哈密顿量的基态可以落在不同表示里。极端形式就是 Haag 定理：相对论性场论中相互作用场与自由场的表示必然不等价，相互作用绘景不存在。一句话：有限自由度时"对易关系 = 全部"，无穷自由度时"对易关系 + 态的选择 = 全部"。

</details>

**4.** 单模相干态定义为 $\lvert\alpha\rangle = e^{-\lvert\alpha\rvert^2/2}\,e^{\alpha a^\dagger}\lvert0\rangle$。(a) 计算 $\lvert\langle0\rvert\alpha\rangle\rvert^2$；(b) 推广到 $M$ 个模，取 $\alpha_k = \lambda/k$ 与 $\alpha_k = \lambda/\sqrt k$ 两种位移，说明 $M\to\infty$ 时两种情形的本质差别；(c) 一句话联系红外灾难。

<details markdown="1"><summary>点击显示答案</summary>

**(a)** 展开指数级数：

$$\langle0\rvert\alpha\rangle = e^{-\lvert\alpha\rvert^2/2}\sum_{n=0}^{\infty}\frac{\alpha^n}{n!}\,\langle0\rvert(a^\dagger)^n\lvert0\rangle = e^{-\lvert\alpha\rvert^2/2},$$

因为 $\langle0\rvert a^\dagger = (a\lvert0\rangle)^\dagger = 0$ 使 $n \ge 1$ 项全部湮灭，只有 $n = 0$ 项存活。故

$$\lvert\langle0\rvert\alpha\rangle\rvert^2 = e^{-\lvert\alpha\rvert^2}.$$

**(b)** $M$ 个独立模（不同模算符对易、真空为张量积），内积因子化：

$$\langle0\rvert\{\alpha_k\}\rangle = \prod_{k=1}^{M}e^{-\lvert\alpha_k\rvert^2/2} = \exp\Big(-\frac12\sum_{k=1}^{M}\lvert\alpha_k\rvert^2\Big), \qquad \big\lvert\langle0\rvert\{\alpha_k\}\rangle\big\rvert^2 = \exp\Big(-\sum_{k=1}^{M}\lvert\alpha_k\rvert^2\Big).$$

- $\alpha_k = \lambda/k$：$\sum_{k=1}^{M}\lvert\alpha_k\rvert^2 = \lvert\lambda\rvert^2\sum_{k=1}^M 1/k^2 \to \pi^2\lvert\lambda\rvert^2/6 \lt \infty$，重叠趋于 $e^{-\pi^2\lvert\lambda\rvert^2/6} \gt 0$——两真空保持非零重叠，两个 Fock 表示**等价**；
- $\alpha_k = \lambda/\sqrt k$：$\sum_{k=1}^{M}\lvert\alpha_k\rvert^2 = \lvert\lambda\rvert^2\sum_{k=1}^M 1/k \sim \lvert\lambda\rvert^2\ln M \to \infty$，重叠 $\sim M^{-\lvert\lambda\rvert^2} \to 0$——两真空**严格正交**，新真空上的整个激发态塔都与旧 Fock 空间正交，两个表示**幺正不等价**（幺正映射保内积，不可能把真空映成正交）。

**(c)** 红外灾难正是情形二：带电粒子散射使每个软光子模获得小位移 $\lvert\alpha_{\vec k}\rvert^2 \sim e^2/(V\omega_k^3)$，单模位移微不足道，但模密度 $V\,d^3k/(2\pi)^3$ 累积后 $\sum_k\lvert\alpha_k\rvert^2 \sim \alpha\int_0 dk/k$ 在红外端对数发散——无穷多软模的累积位移把物理渐近态推出裸 Fock 空间，这就是 Bloch–Nordsieck 必须用相干态（光子云）代替裸带电粒子态的原因。

</details>

**5.** 写出 Haag 定理的陈述，并判断以下两个说法的正误：(a) "有限体积加紫外截断的格点场论中，相互作用绘景是合法的"；(b) "Haag 定理说明微扰 QFT 算出的截面是错的"。

<details markdown="1"><summary>点击显示答案</summary>

**Haag 定理（1955）**：在满足标准公理（庞加莱协变性、唯一真空、正能量谱、局域性）的相对论性量子场论中，若某一时刻的场 $\phi(\vec x,t)$ 经幺正变换与同一时刻的自由场相联系，$\phi(\vec x,t) = U\,\phi_0(\vec x,t)\,U^{-1}$，则 $\phi$ 本身就是自由场（一切真空期望值与自由场相同，$S$ 矩阵平凡）。推论：非平凡相对论性场论中，相互作用绘景在严格意义下不存在。

**(a) 对。** 有限体积把动量离散化，紫外截断（格点）砍掉高频模，单粒子模数变为有限，总自由度有限——Haag 定理的前提（无穷自由度、连续时空平移不变的协变场论）不再成立；相反 Stone–von Neumann / Jordan–Wigner 定理重新生效，表示唯一，相互作用绘景是普通量子力学的合法操作。截断理论的一切计算（微扰展开、费曼图逐阶求值）都是良定的。

**(b) 错。** Haag 定理禁止的是"连续、无穷体积的相对论性理论里相互作用绘景作为严格对象存在"，它**不**宣判微扰展开的数值错误。微扰论的每一步都在带截断的理论上进行——那里由 (a) 一切合法——算出的逐阶形式级数配合重整化取极限，给出与实验精度吻合的截面（如 QED 反常磁矩）。严格性缺口只在一个**存在性**问题：截断取掉后的连续极限是否存在、级数是否收敛到某个真理论。哪些四维场论真的存在，是构造性场论的主题，见 QFT 书 [08 篇：构造性场论与四维 $\phi^4$ 的平凡性](../../qft-sm/docs/stage-04-qft-core/08-constructive-qft-triviality.md)。

</details>

## 参考

- Bratteli & Robinson《Operator Algebras and Quantum Statistical Mechanics 2》§5.2（CAR/CCR 代数、Fock 表示及其唯一性定理——本篇第 2、3 节的严格版本）；卷 1 第 2–3 章（C*-代数、态与 GNS 构造——第 4.3 节）。
- Reed & Simon《Methods of Modern Mathematical Physics》卷 II《Fourier Analysis, Self-Adjointness》§X.7（Fock 空间与二次量子化的泛函分析基础）；卷 I《Functional Analysis》§VIII.4（Stone–von Neumann 定理）。
- Haag《Local Quantum Physics》第 I–II 章（场论公理与 Haag 定理）；原始论文 Haag, Dan. Mat. Fys. Medd. 29 (12) (1955)。
- Thirring《Quantum Mathematical Physics: Atoms, Molecules and Large Systems》第 3 章（Fock 空间、CCR/CAR 与热力学极限的代数表述、KMS 态）。
- van Hove, Physica 18, 145 (1952)（不等价表示的第一个玩具模型，§4.1 出处）；Anderson, Phys. Rev. Lett. 18, 1049 (1967)（正交灾难原文）；Bloch & Nordsieck, Phys. Rev. 52, 54 (1937)（红外灾难的相干态处理）。
- 交叉参考：本书[第 09 篇](09-second-quantization.md)（二次量子化的构造与代数本身）、[第 09s 篇](09s-fermi-dirac-derivation.md)（对称化公设的逻辑地位）；QFT 书[标量场正则量子化](../../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)（同一代数在场论中的出场）与 [08 篇：构造性场论与四维 $\phi^4$ 的平凡性](../../qft-sm/docs/stage-04-qft-core/08-constructive-qft-triviality.md)（连续场论存在性的完整故事）。
