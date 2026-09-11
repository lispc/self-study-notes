# 测量、EPR 与 Bell 不等式：叠加、纠缠与定域隐变量的出局

> 路线图位置：量子力学书 · 尾声（测量与诠释）· 第 14 篇
> 前置知识：第 03 篇（测量公设、密度矩阵与约化密度矩阵、张量积——本篇全程在用）；第 05 篇（自旋 1/2 与泡利矩阵）；第 05s 篇（自旋单态——Bell 实验的标准载体）。
> 学习目标：会把测量公设的"边界问题"说成明确的物理问题（冯诺依曼链与为何退相干解释了"看起来坍缩"却没解决"单一结果"）；会重构 EPR 论证的逻辑（定域性 + 实在性判据 ⇒ 量子力学不完备）；会完整推导 CHSH 不等式并证明自旋单态违反它达 $2\sqrt2$ 倍（Tsirelson 界）；会用 no-signaling 论证说明这不与相对论冲突；会按时间线陈述实验闭环（Aspect 1982 → 无漏洞检验 2015 → 2022 年诺贝尔奖）；能一句话说清各诠释（坍缩/多世界/导航波/客观坍缩）分别答的是哪个问题、哪些可检验。
>
> 记号约定：保留 $\hbar$。自旋沿单位矢 $\vec a$ 的测量记 $A(\vec a) = \vec\sigma\cdot\vec a$（本征值 $\pm1$）；关联函数 $E(\vec a,\vec b) = \langle(\vec\sigma\cdot\vec a)\otimes(\vec\sigma\cdot\vec b)\rangle$。

---

## 1. 一句话总结

**测量公设让"演化幺正"与"读出确定值"共存，但没说测量装置为何/何时获得豁免——把装置也写进薛定谔方程就得到冯诺依曼链与"猫"，环境纠缠（退相干）解释了为什么宏观叠加在实践中从不可见，却仍不回答"为何是这一个结果"；EPR（1935）用定域性 + 实在性判据论证"量子力学不完备、必有隐变量"，Bell（1964）把这个哲学论断变成实验室里的不等式：任何定域隐变量理论必须满足 $\lvert S\rvert\le2$，而自旋单态量子力学给出 $2\sqrt2$——Aspect 及其后的实验（2022 年诺贝尔物理学奖）以高置信度判定量子力学赢：自然界不存在定域隐变量，纠缠的非定域关联是实在的属性而非诠释偏好；"坍缩何时发生"仍是开放问题，但"定域实在论已死"是每个物理学家都该知道的事实。**

## 2. 测量公设与"边界问题"

第 03 篇的公设拼图里有一块与众不同：其余公设（态、可观测量、演化、复合）都是平滑与幺正的，唯独**测量公设**引入了两件非幺正的事——本征值随机跳变 + 波函数坍缩。如果量子力学是普适的，测量装置也是量子系统，也该服从薛定谔方程。于是著名的链式推论（冯诺依曼链）：

$$\big(\lvert\uparrow\rangle + \lvert\downarrow\rangle\big)\otimes\lvert{\rm 就绪}\rangle\ \xrightarrow{\ \text{相互作用}\ }\ \lvert\uparrow\rangle\lvert{\rm 指针\uparrow}\rangle + \lvert\downarrow\rangle\lvert{\rm 指针\downarrow}\rangle$$

——装置被"感染"进叠加态（薛定谔的猫就是把指针换成猫的思想实验）。幺正演化**从不**产生唯一结果；而每次看实验记录，只有**一个**结果。矛盾出现在哪里？三种可能的出口：

1. 量子力学不适用于宏观/测量装置（边界划在某处——但划在哪？多热的探测器算宏观？超导量子干涉器件里几百亿电子明明好好服从叠加）；
2. 幺正演化需要修正（客观坍缩理论，§7——可检验！）；
3. 唯一结果本来就是幻觉或派生的（多世界/退相干纲领，§3、§7）。

量子力学教材止步于公设，本篇把问题的形状画清楚——它是物理问题，不是哲学粉饰。

## 3. 退相干：为什么坍缩"看起来"发生

**环境也是量子系统**，测量装置无法与光子、空气分子、声子隔绝。指针的两个宏观可分辨态 $\lvert\uparrow\rangle,\ \lvert\downarrow\rangle$ 与环境的相互作用方式必然不同（否则不可分辨），最简模型：

$$H_{\rm int} = \hbar\chi\,\lvert\downarrow\rangle\langle\downarrow\vert\otimes B\qquad(\lvert\uparrow\rangle\text{ 不踢环境，}\ \lvert\downarrow\rangle\text{ 踢}),$$

环境初态 $\lvert E_0\rangle$ 时，短时间后联合态

$$\big(c_\uparrow\lvert\uparrow\rangle + c_\downarrow\lvert\downarrow\rangle\big)\lvert E_0\rangle\ \to\ c_\uparrow\lvert\uparrow\rangle\lvert E_0\rangle + c_\downarrow\lvert\downarrow\rangle\lvert E_1\rangle,\qquad \lvert E_1\rangle = e^{-iBt}\lvert E_0\rangle.$$

对环境求迹（第 03 篇 §8 的约化密度矩阵），装置的相干项被压上重叠因子（自检问题 4 的具体计算）：

$$\rho_{\uparrow\downarrow}(t) = \rho_{\uparrow\downarrow}(0)\,\langle E_0\vert E_1(t)\rangle\ \xrightarrow{\ \text{环境自由度多}\ }\ 0\quad(\text{指数快}).$$

**退相干**的三个要点：

- 它是幺正、普适、定域的动力学过程——不需要新公设，实验室里可调控（腔 QED、离子阱里能看着叠加"变脏"）；
- 它解释了**为什么经典世界没有干涉**：宏观叠加的环境纠缠快到（时间尺度 $\sim10^{-20}$ s 量级）任何仪器都追不上，退相干把密度矩阵变成了经典概率分布的模样（指针态成为稳定的基，"量子达尔文主义"的冗余记录让多位观察者看见同一世界）；
- 它**没有**解决边界问题：$\rho$ 对角化后仍是混态（"↑ 以概率 $\lvert c_\uparrow\rvert^2$、↓ 以概率 …"），**哪一次运行出现哪个结果**依然是幺正演化说不出的那句。退相干把"看起来坍缩"讲透了，把"实际坍缩"留在原地。

## 4. EPR 论证（1935）：定域实在 vs 量子力学

Einstein–Podolsky–Rosen 的原始论证用位置–动量对，Bohm 的自旋版本更干净（也直接通向实验）。取第 05s 篇的自旋单态

$$\lvert\Psi^-\rangle = \frac{1}{\sqrt2}\big(\lvert\uparrow\rangle_A\lvert\downarrow\rangle_B - \lvert\downarrow\rangle_A\lvert\uparrow\rangle_B\big),$$

两粒子飞向远处的 Alice 与 Bob。量子力学预言：沿**任何**方向 $\vec a$ 测 A，结果 $\pm1$ 随机，但 B 沿同方向必得相反结果（单态各向同性，自检问题 2）。

EPR 的两块基石：

- **实在性判据**："若能在不以任何方式扰动一个系统的前提下确定地预言它的某个量的值，则存在一个实在要素对应于这个量。"
- **定域性**：远处的测量选择不扰动此处的系统（相对论精神）。

推论：Alice 可以任选方向 $\vec a$ 测 A，从而**预言** B 沿 $\vec a$ 的自旋值——按判据，B 的每个自旋分量都是"实在要素"（具备确定值），无论 Alice 测不测、测什么。但量子力学的态 $\lvert\Psi^-\rangle$ 不包含这些确定值（单态对每个方向的测量都只给概率）。EPR 的结论：**量子力学对实在的描述不完备**——存在更深层的"隐变量"理论，量子概率只是对它的无知。

这个论证在逻辑上无懈可击——前提是那两块基石。接下来三十年，"隐变量是否存在"被当成哲学问题挂起，直到 Bell 把它变成实验可判定。

## 5. Bell 不等式（CHSH 形式）：定域隐变量的天花板

**设定**：Alice 在 $\vec a$ 或 $\vec a'$ 中选一个方向测自旋，得 $A = \pm1$；Bob 在 $\vec b$ 或 $\vec b'$ 中选，得 $B = \pm1$。**定域隐变量理论**：结果由携带的隐变量 $\lambda$（分布 $\rho(\lambda)$）决定，且**各自只依赖本地设置**：

$$A(\vec a,\lambda) = \pm1,\quad A(\vec a',\lambda) = \pm1,\quad B(\vec b,\lambda) = \pm1,\quad B(\vec b',\lambda) = \pm1,$$

定域性就藏在这里：$A$ 不依赖 Bob 的选择，$B$ 不依赖 Alice 的选择。定义关联

$$E(\vec a,\vec b) = \int d\lambda\,\rho(\lambda)\,A(\vec a,\lambda)B(\vec b,\lambda),$$

组合（CHSH）

$$S \equiv E(\vec a,\vec b) + E(\vec a,\vec b') + E(\vec a',\vec b) - E(\vec a',\vec b'),$$

**对一切定域隐变量理论**（自检问题 1 的三行证明）：

$$\boxed{\ \lvert S\rvert \le 2\ }$$

**量子力学的答案**：单态给出（自检问题 2，泡利代数直算）

$$E(\vec a,\vec b) = -\vec a\cdot\vec b = -\cos\theta_{ab}.$$

选共面配置 $\vec a = \hat z,\ \vec a' = \hat x,\ \vec b = (\hat z+\hat x)/\sqrt2,\ \vec b' = (\hat z-\hat x)/\sqrt2$（自检问题 3）：

$$S_{\rm QM} = -\frac{1}{\sqrt2}-\frac{1}{\sqrt2}-\frac{1}{\sqrt2}-\frac{1}{\sqrt2} = -2\sqrt2\quad\Rightarrow\quad \lvert S_{\rm QM}\rvert = 2\sqrt2 > 2.$$

$2\sqrt2$ 是量子力学能到达的最大值（**Tsirelson 界**——量子非定域有天花板，自然界没有放开到逻辑极限）。量子力学与**所有**定域隐变量理论在此正面冲突：测 $S$，两者必错一个。

**澄清三个常见误解**：

- **违反 Bell ≠ 否定因果律**：no-signaling 定理（自检问题 3 后半）保证 Alice 单侧的统计永远均匀 $\frac12$，与 Bob 的设置无关——非定域"关联"不能用来传信息，相对论安然无恙。
- **纠缠 ≠ "测量 A 改变 B 的态"的操作性陈述**：约化密度矩阵不受远处测量的影响（测量的是关联，不是遥控）。
- **Bell 不排除非定域隐变量**：Bohm 力学（§7）非定域，与 Bell 相安无事。出局的是"定域 + 实在"的组合。

## 6. 实验：从 Aspect 到无漏洞检验（2022 诺奖）

判定 $S > 2$ 需要同时堵住两个漏洞：

- **定域性漏洞**：测量选择要在"信息来得及到达对端"之前做出（光锥分离）——否则隐变量可以"知道"两边设置；
- **探测漏洞**：被探测的子样本必须代表全体——否则探测偏置可以伪造关联。

时间线：

- **1972 Freedman–Clauser**：首次 Bell 实验，违反。
- **1982 Aspect–Dalibard–Roger**：声光开关快速切换测量方向（准光锥分离），违反达 5 个标准差——决定性一击。
- **2015 三组无漏洞实验**（Delft/Hensen 等，Vienna/Giustina 等，NIST/Shalm 等）：同时关闭两类漏洞，全部违反（Delft 用电子自旋纠缠 + 相距 1.3 km， loophole-free 的标志）。
- **2022 诺贝尔物理学奖**：Aspect, Clauser, Zeilinger。

统计上：现代实验违反定域隐变量界**超过 10 个标准差**。剩下的理论退路只有逻辑体操（超决定论 superdeterminism："实验者的选择也是隐变量安排的"——不可证伪，多数人不买账）。**结论写进教科书：定域隐变量理论被实验排除。**

**顺带的工业革命**：为 Bell 实验发展的纠缠光源与单光子探测技术，加上 no-signaling 保证的安全性，催生了量子密钥分发（Ekert E91：窃听者介入会破坏纠缠、拉低 Bell 违反量从而暴露自己）与量子信息科学——本篇的"纯原理"问题直接长成了工程领域，延续阅读见[第 14s 篇 量子信息初步](14s-quantum-information.md)与[第 14s2 篇 量子计算初步](14s2-quantum-computing.md)。

## 7. 诠释清单与本书立场

边界问题（§2 的"哪一次运行出现哪个结果"）没有共识答案。主流候选各答一块：

| 诠释 | 对"唯一结果"的回答 | 可检验性 |
| --- | --- | --- |
| 哥本哈根/坍缩 | 测量是经典-量子边界上的基本过程（实用主义：别问边界外的事） | 与标准 QM 同预言 |
| 多世界（Everett） | 没有坍缩；每次测量分支，所有结果都在（"唯一感"是分支内的自我定位） | 与标准 QM 同预言（分支不可通信） |
| 导航波（de Broglie–Bohm） | 粒子始终有确定轨迹，波函数导航；非定域隐变量的忠实实现 | 与标准 QM 同预言（非定域性被 Bell 容留） |
| 客观坍缩（GRW/CSL） | 幺正演化本身带微小坍缩项，宏观叠加自发衰变 | **可检验**：干涉实验正在压缩其参数空间 |

两点立场（本篇的，也是主流计算物理的）：

1. **到今天为止，所有实验与标准量子力学一致**。无论你偏爱哪个诠释，能算的预言一模一样（除客观坍缩外）——诠释之争不影响本书其余 13 篇的任何一个公式。
2. **但 Bell 的教训是"问哲学问题要挑能做实验的问法"**。EPR 问"完备吗"（问不出），Bell 问"$S$ 超得过 2 吗"（问出了诺贝尔奖）。退相干与量子信息正是这条路线的延续。

**与全书的接口**：纠缠是本篇的主角，也是多体物理的核心资源——凝聚态书拓扑序一章的拓扑纠缠熵（用纠缠谱区分物相）把它从"疑难"翻转为"序参量"。量子力学教材的"尾声问题"在下游书里变成"工作语言"；它的信息论定量刻画（Schmidt 分解、纠缠熵、no-cloning 与三张名片协议）见第 14s、14s2 两篇。

## 小结

| 概念 | 内容 | 判定 |
| --- | --- | --- |
| 冯诺依曼链 | 幺正演化不产生唯一结果 | 边界问题是物理问题 |
| 退相干 | 环境纠缠压掉相干项（指数快） | 解释"看起来坍缩"，不解释"哪一个" |
| EPR | 定域性 + 实在判据 ⇒ 隐变量 | 前提可被实验检验 |
| CHSH | 定域隐变量 $\lvert S\rvert\le2$ | 三行代数，无假设漏洞 |
| 量子单态 | $E = -\cos\theta$，$\lvert S\rvert = 2\sqrt2$ | Tsirelson 界，违反 |
| no-signaling | 单侧统计均匀 $\frac12$ | 不违反相对论 |
| 实验 | 1982 Aspect → 2015 无漏洞 → 2022 诺奖 | 定域隐变量出局（$>10\sigma$） |
| 诠释 | 哥本哈根/多世界/Bohm/GRW | 除 GRW 外预言相同 |

一句话收束：测量的"为何唯一"仍开放，但"定域实在论"已被判死刑——量子力学保持全胜，而追问它边界的每一步（Bell、退相干、量子信息）都长出了新的物理学。能把这三句话讲清楚的人，才算真正修完了一门量子力学。

## 自检问题

**1.** 推导 CHSH 不等式：从 $A,B = \pm1$ 与定域性（结果只依赖本地设置与 $\lambda$）证明 $\lvert S\rvert\le2$。

<details markdown="1"><summary>点击显示答案</summary>

对每个固定的 $\lambda$，考察组合

$$s(\lambda) = A(\vec a,\lambda)\big[B(\vec b,\lambda) + B(\vec b',\lambda)\big] + A(\vec a',\lambda)\big[B(\vec b,\lambda) - B(\vec b',\lambda)\big].$$

关键观察：$B(\vec b,\lambda), B(\vec b',\lambda)\in\{+1,-1\}$，故两括号一实一零——若 $B(\vec b) = B(\vec b')$，第一括号 $= \pm2$、第二括号 $= 0$；若 $B(\vec b) = -B(\vec b')$，则第一括号 $= 0$、第二括号 $= \pm2$。无论哪种情形

$$\lvert s(\lambda)\rvert = 2\qquad(\text{对每个 }\lambda\text{ 都是恰好 }2).$$

于是

$$\lvert S\rvert = \Big\lvert\int d\lambda\,\rho(\lambda)\,s(\lambda)\Big\lvert \le \int d\lambda\,\rho(\lambda)\,\lvert s(\lambda)\rvert = 2\int d\lambda\,\rho(\lambda) = 2.$$

只用了三样东西：结果二值、隐变量分布正定、**定域性**（$A$ 不依赖 Bob 的设置——否则 $s(\lambda)$ 无法对每个 $\lambda$ 单独写出来）。哪一步是量子力学破坏的？量子力学里不存在同时取值的 $A(\vec a,\lambda)$ 与 $A(\vec a',\lambda)$（非对易可观测量无联合分布）——定域隐变量的"实在要素表"本身不成立。

</details>

**2.** 对自旋单态计算 $E(\vec a,\vec b) = \langle\Psi^-\vert(\vec\sigma\cdot\vec a)\otimes(\vec\sigma\cdot\vec b)\vert\Psi^-\rangle$，证明 $= -\cos\theta_{ab}$。

<details markdown="1"><summary>点击显示答案</summary>

用泡利代数 $(\vec\sigma\cdot\vec a)(\vec\sigma\cdot\vec b) = \vec a\cdot\vec b + i\vec\sigma\cdot(\vec a\times\vec b)$ 不方便直接张量积；换直算法。记 $M = (\vec\sigma\cdot\vec a)\otimes(\vec\sigma\cdot\vec b) = \sum_{ij}a_ib_j\,\sigma_i\otimes\sigma_j$。对单态逐项求期望：

- $\langle\sigma_i\otimes\sigma_j\rangle = -\delta_{ij}$。验证 $i=j=z$：$\sigma_z\otimes\sigma_z$ 作用在 $\lvert\uparrow\downarrow\rangle$ 上得 $(+1)(-1)\lvert\uparrow\downarrow\rangle = -\lvert\uparrow\downarrow\rangle$，在 $\lvert\downarrow\uparrow\rangle$ 上得 $(-1)(+1) = -1$——两项本征值都是 $-1$，期望 $\langle\sigma_z\otimes\sigma_z\rangle = -1 = -\delta_{zz}$ ✓。
- $i\ne j$（如 $\sigma_z\otimes\sigma_x$）：$\sigma_x$ 翻转 B 的自旋，把 $\lvert\uparrow\downarrow\rangle$ 映到 $\lvert\uparrow\uparrow\rangle$——与单态正交，期望为零 ✓。

于是

$$E(\vec a,\vec b) = \sum_{ij}a_ib_j\langle\sigma_i\otimes\sigma_j\rangle = -\sum_{ij}a_ib_j\delta_{ij} = -\vec a\cdot\vec b = -\cos\theta_{ab}.$$

物理读法：单态总自旋为零（各向同性），关联张量只能正比于 $\delta_{ij}$，比例由 $\sigma_z\otimes\sigma_z$ 的 $-1$ 钉死——完美的反相关沿一切方向。

</details>

**3.** 验证最优配置 $\vec a = \hat z,\ \vec a' = \hat x,\ \vec b = (\hat z+\hat x)/\sqrt2,\ \vec b' = (\hat z-\hat x)/\sqrt2$ 下 $\lvert S\rvert = 2\sqrt2$；然后证明 no-signaling：Alice 单侧测 $\vec\sigma\cdot\vec a$ 得 $\pm$ 的概率恒为 $\frac12$，与 Bob 测什么（甚至测不测）无关。

<details markdown="1"><summary>点击显示答案</summary>

各关联（用 $E = -\vec a\cdot\vec b$）：

$$E(\vec a,\vec b) = -\frac{1}{\sqrt2},\quad E(\vec a,\vec b') = -\frac{1}{\sqrt2},\quad E(\vec a',\vec b) = -\frac{1}{\sqrt2},\quad E(\vec a',\vec b') = +\frac{1}{\sqrt2}.$$

$$S = E(\vec a,\vec b)+E(\vec a,\vec b')+E(\vec a',\vec b)-E(\vec a',\vec b') = -\frac{3}{\sqrt2}-\frac{1}{\sqrt2} = -2\sqrt2,\qquad \lvert S\rvert = 2\sqrt2 > 2.$$

no-signaling：单态的联合概率 $P(s_a,s_b\vert\vec a,\vec b) = \frac14\big(1 - s_as_b\,\vec a\cdot\vec b\big)$（$s = \pm1$；与 $E = -\vec a\cdot\vec b$ 及归一自洽）。Alice 侧边际：

$$P(s_a\vert\vec a,\vec b) = \sum_{s_b}P(s_a,s_b) = \frac14\sum_{s_b}\big(1 - s_as_b\cos\theta\big) = \frac14\cdot 2 = \frac12,$$

$s_b = \pm1$ 两项相加时 $\cos\theta$ 项抵消——**与 $\vec b$ 完全无关**（也与 Bob 是否测量无关：不测时 B 的约化密度矩阵 $\rho_B = \frac12\mathbb 1$，任何方向的期望都是零）。所以 Bob 改设置不能改变 Alice 的计数率——非定域关联无法编码信号，光锥内因果照旧。违反的只是"关联的结构"：经典关联函数（任意 $\rho(\lambda)$ 的凸组合）被 CHSH 锁在 2 以内，量子的到了 $2\sqrt2$。

</details>

**4.** 退相干玩具模型：系统（自旋）与环境（$N$ 个自旋 $\frac12$）耦合 $H_{\rm int} = \hbar\chi\lvert\downarrow\rangle\langle\downarrow\vert\otimes\sum_{k=1}^N\sigma_x^{(k)}$，环境初态全 $\lvert\uparrow\cdots\uparrow\rangle$。计算系统约化密度矩阵非对角元的时间演化，证明其以 $\cos^{N}(\chi t)$ 衰减并在 $N\to\infty$ 时趋于零。

<details markdown="1"><summary>点击显示答案</summary>

相互作用只在系统处于 $\lvert\downarrow\rangle$ 时激活。环境演化算符：系统 $\lvert\uparrow\rangle$ 支上环境自由演化（$U_\uparrow = \mathbb 1$，取 $\chi$ 只作用于 $\downarrow$ 支），$\lvert\downarrow\rangle$ 支上 $U_\downarrow = \prod_k e^{-i\chi t\sigma_x^{(k)}}$。初始 $\lvert\psi\rangle = c_\uparrow\lvert\uparrow\rangle + c_\downarrow\lvert\downarrow\rangle$，环境 $\lvert E_0\rangle = \lvert\uparrow\cdots\uparrow\rangle$：

$$\lvert\Psi(t)\rangle = c_\uparrow\lvert\uparrow\rangle\lvert E_0\rangle + c_\downarrow\lvert\downarrow\rangle\,U_\downarrow(t)\lvert E_0\rangle \equiv c_\uparrow\lvert\uparrow\rangle\lvert E_0\rangle + c_\downarrow\lvert\downarrow\rangle\lvert E_1(t)\rangle.$$

单因子 $e^{-i\chi t\sigma_x}$ 作用在 $\lvert\uparrow\rangle$ 上：$e^{-i\chi t\sigma_x} = \cos\chi t\,\mathbb 1 - i\sin\chi t\,\sigma_x$，故

$$\lvert E_1(t)\rangle = \big(\cos\chi t - i\sin\chi t\,\lvert\downarrow\rangle\big)^{\otimes N},\qquad \langle E_0\vert E_1(t)\rangle = \cos^N\chi t\cdot(\text{相因子})^{0} = \cos^N\chi t\ \ (\text{每因子重叠 } \cos\chi t).$$

对环境求迹（第 03 篇 §8），系统约化密度矩阵的非对角元乘上环境态的重叠：

$$\rho_{\uparrow\downarrow}(t) = c_\uparrow c_\downarrow^*\,\langle E_1(t)\vert E_0\rangle = c_\uparrow c_\downarrow^*\,\cos^N\chi t,$$

（重叠为实数：每因子 $\lvert\uparrow\rangle$ 与 $\cos\chi t\lvert\uparrow\rangle - i\sin\chi t\lvert\downarrow\rangle$ 的内积是 $\cos\chi t$。）$N$ 大时 $\cos^N\chi t \approx e^{-N\chi^2t^2}$（$\ln\cos$ 展开首阶，高斯型超快衰减），$N\sim10^{23}$ 个环境自由度使退相干时间比任何弛豫时间短十几个数量级——宏观叠加在实验上"从来不存在"。对角元 $\lvert c_\uparrow\rvert^2,\ \lvert c_\downarrow\rvert^2$ 纹丝不动：退相干不选出结果，只抹掉相干——§3 的"解释了一半"在此定量落地。

</details>

**5.** 重构 EPR 论证：从定域性 + 实在性判据推出"B 的每个自旋分量都是实在要素"；然后指出 Bell 的哪一步把"不完备"的结论变成了可实验判定的不等式。

<details markdown="1"><summary>点击显示答案</summary>

重构（以 $\hat z$ 分量为例）：Alice 沿 $\hat z$ 测 A，由单态反相关，可**确定预言** B 沿 $\hat z$ 的结果（必与 A 相反）。定域性：Alice 的测量（与 B 类空分离，或至少无相互作用）不扰动 B。实在性判据：能在不扰动 B 的前提下确定预言其值 ⇒ 存在对应 B 的 $\sigma_z$ 的实在要素 $v_z^B$。同样的论证对 $\hat x$、$\hat y$、乃至任意方向 $\vec a$ 都成立——**B 的所有自旋分量同时具有确定值** $v^B(\vec a)$（对每个 $\vec a$）。但 $\sigma_x,\sigma_y,\sigma_z$ 非对易，量子态不能同时指定这些值（$\lvert\Psi^-\rangle$ 对每个方向都给 $\frac12$ 概率）。EPR 结论：量子态不是对物理实在的完备描述——那些 $v^B(\vec a)$ 就是"隐变量"应在而未在的描述。

从论证到实验的关键一跳（Bell 1964）：EPR 的隐变量世界要求每个粒子自带一张方向-结果表 $\big\{v(\vec a)\big\}_{\vec a}$。**测量只能翻开一格**（选一个方向），单次实验看不出破绽；但**关联统计**翻动两张表的组合——$E(\vec a,\vec b)$ 把 Alice 选 $\vec a$ 与 Bob 选 $\vec b$ 的表项配对求平均，而 $S$ 把四种配置的关联线性组合。隐变量表的"预先存在 + 定域"（每格在测量前写好、只读本地格）经自检问题 1 的三行代数锁死 $\lvert S\rvert\le2$；量子单态的 $2\sqrt2$ 越狱成功。于是"完备性"之争变成"$S$ 的实测值"——哲学问题以实验收场，这正是 §7 立场第 2 条的原始案例。

</details>

## 参考

- Griffiths《量子力学概论》（第 3 版）第 12 章（Afterword：EPR 佯谬、Bell 定理与测量问题）——本篇主线的本科版。
- Nielsen & Chuang《量子计算与量子信息》§2.6（Bell 不等式）与第 8 章（退相干与量子噪声）。
- Bell, *Speakable and Unspeakable in Quantum Mechanics*（论文集）——原始思想的一手来源。
- Aspect, Dalibard & Roger, *Phys. Rev. Lett.* **49**, 1804 (1982)；Hensen et al., *Nature* **526**, 682 (2015)——判定性实验。
- Weinberg《Lectures on Quantum Mechanics》测量与诠释章节——边界问题的清醒梳理。
- 本篇全程依赖第 03 篇（[形式体系](03-formalism-hilbert-dirac.md)：测量公设、密度矩阵）与第 05s 篇（[全同粒子](05s-identical-particles.md)：自旋单态）。
