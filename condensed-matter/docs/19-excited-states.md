# 激发态：线性响应、TD-DFT、EOM-CC 与 BSE

> 路线图位置：第四部分（多电子问题怎么算）· 第 19 章
> 前置知识：[第 15 章](15-post-hf-mp2-cc.md)（耦合簇与 $\bar H$ 机器）、[第 16 章](16-dft.md)（KS 框架与失灵清单）、[第 17 章](17-beyond-dft-gw-dmft.md)（格林函数、GW 与准粒子谱）；第 3 章[金属自由电子气](03-free-electron-gas.md)（费米海与响应的语言）；[QFT 书微扰论](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)（含时微扰与费米黄金定则——线性响应的经典母体）。
> 学习目标：理解激发态的正确语言是**响应函数**（微扰的极点 = 激发能），而非"基态方法的激发版"；会推 TDHF/RPA 的本征值结构并用它算出 H₂ 的单态激发能（交换修正抬高能隙的机制）；理解 EOM-CC 把 $\bar H$ 的激发本征值直接当成激发态（与第 15 章机器的无缝衔接）；掌握 TD-DFT 的 Runge–Gross 定位、Casida 方程与核 $f_{xc}$ 的地位、以及三大经典失败（电荷转移、双重激发、Rydberg 态）；认识 BSE = GW 准粒子 + 电子–空穴梯形图（固体光学的第三根支柱），并会画三大方法的分工表。
>
> 记号约定：原子单位（同第 14 章）。激发能记 $\omega$；$i,j$ 占据、$a,b$ 空轨道（沿第 15 章约定）。

---

## 1. 一句话总结

**激发态的计算不是"把基态方法的本征值往上数一格"，而是响应理论：对体系加一个频率为 $\omega$ 的微扰，响应函数的极点就是激发能——这条统一战线上有三支主力军。TDHF/RPA（与第 6 章环图同源）把 Slater 行列式的响应线性化成一个本征值问题，交换项在极点处把激发能从轨道能差抬高；EOM-CC 把耦合簇的 $\bar H = e^{-T}He^T$ 直接对角化到激发扇区，继承 CC 的精度与大小一致性（单参考区的激发能 ~0.1–0.3 eV）；TD-DFT 靠 Runge–Gross 定理（含时版 HK）把一切塞进核 $f_{xc} = \delta v_{xc}/\delta n$，绝热近似下便宜好用，但电荷转移激发（导数不连续缺席）、双重激发（需要频率依赖）、Rydberg 态（渐近势错误）是结构性翻车点。固体一侧的答案是 BSE：GW 准粒子能隙 + 电子–空穴梯形图，激子束缚把光学吸收带从带边拉低——四条路线合起来，"激发态"这枚硬币在分子与固体两面都可支付。**

## 2. 统一语言：线性响应

含时微扰论（[QFT 书](../../qft-sm/docs/stage-02-quantum-mechanics/03-perturbation-theory.md)第 4–5 节的费米黄金定则）的老结论：弱外场 $V(t) = v\,e^{-i\omega t}$ 下，跃迁速率 $\propto\lvert\langle n\rvert v\lvert0\rangle\vert^2\delta(\omega - \omega_{n0})$。系统化地把"对一切末态求和"后的可观测量写成

$$\delta\langle A\rangle(\omega) = \sum_B \chi_{AB}(\omega)\,v_B(\omega),$$

响应函数 $\chi$（推迟格林函数的虚部亲缘）是严格的物理对象；**它的极点在实轴 $\omega = E_n - E_0$ 处**——算激发态 = 算响应的极点。三种实现方式的差别只在"用什么近似的 $\chi$"。一个免费的严格约束是**Thomas–Reiche–Kuhn 求和规则** $\sum_n f_{n0} = N$（振荡强度总和 = 电子数，推导见自检问题 2）——任何近似响应函数的第一个体检项。

## 3. 波函数一侧：TDHF/RPA 与 EOM-CC

### 3.1 TDHF/RPA：行列式的响应

HF 基态上加振荡外场，单激发（占据 $i\to$ 空轨道 $a$）的振幅 $X_{ia}, Y_{ia}$ 耦合成线性方程组（无规相近似 RPA 的名字来自对响应函数的环图求和——第 6 章 6 节的同一台机器）：

$$\begin{pmatrix} A & B \\ -B & A \end{pmatrix}\binom{X}{Y} = \omega\binom{X}{Y},\qquad A_{ia,jb} = \delta_{ij}\delta_{ab}\Delta_{ia} + \langle aj\lVert ib\rangle,\ \ B_{ia,jb} = \langle ab\lVert ij\rangle,$$

$\Delta_{ia} = \varepsilon_a - \varepsilon_i$ 为轨道能差。**Tamm–Dancoff 近似**（TDA）扔掉 $B$ 块（退激发-再激发耦合），退化为 CIS 型本征问题；保留 $B$ 才有 RPA 的求和规则友好性。最简单的定量标本是 H₂ 最小基（自检问题 1）：

$$\omega_\text{RPA}^{S} = \sqrt{\Delta(\Delta + 2K)},\qquad K = (\sigma_g\sigma_u\lvert\sigma_g\sigma_u)\ \text{型交换积分},$$

——交换相互作用把单态激发能从裸能隙 $\Delta$ 抬高（同自旋电子互相回避，激发后体系要为"拥挤"付钱）；三态则压低。**分子激发谱的形状（单/三态劈裂）在最小模型里就是这两行**。

### 3.2 EOM-CC：把 $\bar H$ 对角化到激发扇区

第 15 章造好的相似变换哈密顿量 $\bar H = e^{-T}He^{T}$ 有个被埋没的身份：$H$ 与 $\bar H$ **谱相同**（相似变换保谱），而 $\bar H$ 的基态是 $\Phi_0$（$T$ 把基态"拉平"了）。于是激发态可以写成

$$\lvert\Psi_n\rangle = R_n\,e^{T}\Phi_0,\qquad R_n = \sum_{ia}r_i^a a_a^\dagger a_i + \frac12\sum_{ijab}r_{ij}^{ab}a_a^\dagger a_b^\dagger a_j a_i + \cdots,$$

代回薛定谔方程得到**本征值问题的线性化**（推导见自检问题 5）：

$$\boxed{\;[\bar H, R_n] = \omega_n R_n\;}$$

——谐振子代数的亲戚：$\bar H$ 扮演"数字算符"，激发算符 $R$ 是它的本征向量，本征值即激发能。EOM-CCSD 取 $R = R_1 + R_2$、$T = T_1 + T_2$：基态与激发态共享同一个 CC 波函数的相关，差值高度相消——单参考区激发能 ~0.1–0.3 eV，双激发天然由 $R_2$ 覆盖（截断要按"相对基态的秩"理解）。代价与 CCSD 同级（$N^6$），疆界也相同：静态相关面前无能为力（那里换第 18 章 CASSCF 的态平均）。

## 4. 密度一侧：TD-DFT

### 4.1 Runge–Gross 与 Casida

含时外场下 HK 的对应物是 **Runge–Gross 定理**（1984）：给定初态，密度 $n(\vec r, t)$ 与外势 $v(\vec r, t)$ 一一对应（至相差一个纯时间函数）——含时密度泛函理论（TD-DFT）的合法性地基。基态附近线性化：KS 体系的响应 + 交换相关核

$$f_{xc}(\vec r, \vec r';\ \omega) = \frac{\delta v_{xc}[n](\vec r, \omega)}{\delta n(\vec r', \omega)}$$

组装出 **Casida 方程**（推导骨架见自检问题 3）——结构与 3.1 节的 RPA 矩阵同形，只是 $A$ 里的轨道能差换成 KS 能隙、耦合换成 $f_{xc}$ 的直接+核项。**绝热近似**（$f_{xc}(\omega)\to f_{xc}[n_0]$，取基态泛函的导数）是实用的默认：便宜（$N^3$–$N^4$）、局域与半局域价激发的精度 ~0.2–0.4 eV。

### 4.2 三大结构性翻车

- **电荷转移（CT）激发**：给体→受体的跃迁距离大时，真实激发能 $\to I - A - 1/R$（随距离衰减）；绝热 TD-DFT 给出的是 KS 能隙——而第 16 章已经证明 KS 能隙缺 $\Delta_{xc}$ 且 GGA 把它抹平。模型解剖见自检问题 4：精确核 $f_{xc}$ 需要在给受体之间长出一个高度 $\sim\Delta_{xc}$ 的**空间台阶**——局域近似天生造不出。同一病根的另一张脸：第 16 章自相互作用误差。
- **双重激发**：两个电子同时跃迁（$R_2$ 型、$O(\omega^2)$ 虚拟耦合），绝热核是瞬时的、没有频率记忆，原理上无法产生这类态的非线性极点——需要频率依赖的核（双杂化、或干脆 EOM-CC/BSE）。
- **Rydberg 态**：激发电子离核远、密度低，LDA/GGA 的 $v_{xc}$ 渐近行为错误（指数衰减而非 $-1/r$），Rydberg 系列整体塌缩——渐势修正（LB94、CAM-B3LYP 的长程精确交换）是标准解药。

**共同病根**：三个失败都可追溯到"$f_{xc}$ 的非局域性与频率依赖"被绝热局域近似一笔勾销——TD-DFT 的失败清单与第 16 章基态清单严丝合缝地对应（CT ↔ 导数不连续/自相互作用；双重激发 ↔ 频率依赖；Rydberg ↔ 渐近势），同一台发动机的同一批隐患在不同路况下爆胎。

## 5. 固体一侧：Bethe–Salpeter 方程

固体的光学吸收不是"GW 准粒子能隙"就完事：光子打出电子–空穴对，**它们之间的库仑吸引**（梯形图）把激子束缚能压进谱——Si 的激子束缚 ~15 meV，而宽禁带与低维材料（二维半导体 ~0.5 eV）里大到不可忽略。**BSE** = GW 准粒子能量 + 屏蔽库仑作用下的电子–空穴本征值问题：

$$\big(\varepsilon_c^{\text{QP}} - \varepsilon_v^{\text{QP}}\big)A_{vc}^S + \sum_{v'c'}\langle vc\lvert K^{eh}\lvert v'c'\rangle A_{v'c'}^S = \Omega_S A_{vc}^S,$$

$K^{eh}$ 含屏蔽直接项（吸引）与裸交换项（排斥）——结构上正是 3.1 节 RPA 矩阵的"激发态版"，只是单粒子底座从 KS/DFT 换成了 GW（第 17 章）、相互作用换了屏蔽梯形图。BSE 是半导体光学、激子物理的标准工具；与 Casida 方程的深层同构（响应函数 + 梯形耦合 vs 极点结构）是"分子方法与固体方法在响应理论处会师"的漂亮注脚。

## 6. 分工表与选型

| 方法 | 单粒子底座 | 电子–空穴耦合 | 代价 | 强项 | 死穴 |
|---|---|---|---|---|---|
| TDHF/RPA | HF | 裸交换 | $N^4$ | 严格、教学标本 | 能隙高估 |
| CIS(TDA) | HF | 裸交换 | $N^4$ | 最便宜的波函数方案 | 无关联 |
| EOM-CCSD | CCSD | 精确（$\bar H$） | $N^6$ | ~0.1–0.3 eV、双激发 | 静态相关、固体 |
| TD-DFT（绝热） | KS | $f_{xc}$ 近似 | $N^3$–$N^4$ | 大体系日常 | CT/双重/Rydberg |
| BSE | GW | 屏蔽梯形图 | $N^4$ | 固体光学、激子 | 顶角、强关联 |

选型口语：分子价激发、几百原子 → TD-DFT（记得检查 CT 嫌疑）；要精度或双激发 → EOM-CCSD；光催化/光电器件材料 → BSE@GW；解离区或 d 壳层激发 → CASSCF 态平均（第 18 章）。

## 小结

- 激发态 = 响应函数的极点；TRK 求和规则是免费的体检器。
- TDHF/RPA：$\begin{pmatrix}A&B\\-B&A\end{pmatrix}$ 本征值；交换抬高单态能隙（$\omega^S = \sqrt{\Delta(\Delta+2K)}$）；与第 6 章环图同源。
- EOM-CC：$[\bar H, R] = \omega R$——激发算符是 $\bar H$ 的本征向量；继承 CC 的精度与大小一致性。
- TD-DFT：Runge–Gross + Casida；绝热核便宜，CT/双重/Rydberg 三大翻车对应基态失灵清单的镜像。
- BSE：GW 底座 + 屏蔽 e–h 梯形图，固体光学正主；与 Casida 同构。
- 分子方法（EOM-CC/TD-DFT）与固体方法（BSE）在响应理论处会师——第四部分的方法地图至此补上"激发态"一整块。

## 自检问题

**1.** 对 H₂ 最小基组推导 TDHF/RPA 的单态激发能 $\omega^S = \sqrt{\Delta(\Delta + 2K)}$（$\Delta = \varepsilon_u - \varepsilon_g$、$K$ 为 $g$–$u$ 交换型积分），并解释交换作用为何抬高单态、压低三态。

<details markdown="1"><summary>点击显示答案</summary>

**设置**：占据 $\sigma_g$、空 $\sigma_u$，单激发对唯一：$X, Y$ 两个振幅（激发与退激发）。RPA 矩阵在此退化为 $2\times2$：

$$\begin{pmatrix}\Delta + K & K' \\ -K' & -(\Delta + K)\end{pmatrix}\binom{X}{Y} = \omega\binom{X}{Y},$$

其中单态自旋耦合使对角含直接–交换组合 $A = \Delta + (gg\lvert uu) - (gu\lvert gu)$、$B$ 同类（记号细节各教材略异，收进一个耦合常数 $K$ 后结构相同）。本征值：

$$\omega = \pm\sqrt{(\Delta + K)^2 - K'^2}\ \xrightarrow{\ K' = K\ }\ \pm\sqrt{\Delta(\Delta + 2K)}\quad(\text{单态}).$$

（CIS/TDA 直接给 $\Delta + K$；RPA 的 $B$ 块把它开方修正——两者在 $\Delta\gg K$ 时一致。）

**物理解释**：单态中激发电子与基电子**同处对称空间波函数**，交换排斥 $K$ 抬高激发态能量（$\omega$ 增大）；三态空间部分反对称、交换项反号，$\omega^T = \sqrt{\Delta(\Delta - 2K)}$ 压低——**单–三态劈裂 $\approx 2K$，纯粹是交换作用**（第 6 章交换穴的激发态版）。对照第 18 章：$K$ 也正是决定单/三态次序（磁交换）的量——基态磁性、激发谱、响应函数三者在同一个积分上会师。

</details>

**2.** 用费米黄金定则推导 Thomas–Reiche–Kuhn 求和规则 $\sum_n f_{n0} = N$（$f_{n0} = \tfrac23\omega_{n0}\lvert\langle n\rvert\vec r\lvert0\rangle\vert^2$ 为偶极强度），并说明它如何被用作近似方法的体检器。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：取电场沿 $z$，振荡强度 $f_{n0} = 2\omega_{n0}\lvert\langle n\rvert z\lvert0\rangle\vert^2$。核心技巧是把能量差写成对易子的矩阵元：$\langle n\lvert[H, z]\lvert0\rangle = (E_n - E_0)\langle n\lvert z\lvert0\rangle$，配合完备关系 $\sum_n\lvert n\rangle\langle n\rvert = 1$：

$$\sum_n (E_n - E_0)\lvert\langle n\lvert z\lvert0\rangle\vert^2 = \langle 0\lvert z\,[H, z]\lvert0\rangle = -\langle0\lvert[H, z]\,z\lvert0\rangle,$$

（第二等号用同一关系对 $\langle0\rvert z\lvert n\rangle$ 反向展开；两个表达式相等即上面结果的两种读法。）两者平均：

$$\sum_n f_{n0} = \langle0\lvert z[H,z] - [H,z]z\lvert0\rangle = \langle0\lvert\big[z, [H, z]\big]\lvert0\rangle.$$

势能项与 $z$ 对易，只剩动能：$[H, z] = [\tfrac{p_z^2}{2}, z] = -i p_z$（原子单位），故

$$[z, [H, z]] = [z, -ip_z] = -i[z, p_z] = -i\cdot i = 1\qquad\Longrightarrow\qquad \sum_n f_{n0} = 1\ (\text{每个电子坐标}).$$

多电子体系对 $N$ 个电子坐标求和，每个坐标贡献同样的双重对易子，得 $\sum_n f_{n0} = N$。$\blacksquare$

**体检用途**：求和规则只依赖对易关系——**任何近似（泛函、截断、基组）算出的 $f$ 分布积分必须仍等于 $N$**。RPA 完整版保持它（$B$ 块的功劳——这正是 TDA 破坏的东西）；绝热 TD-DFT 在完整线性化下保持（Casida 方程的结构保证）；粗糙的组态平均或截断谱则违反。 violated 的幅度直接标定"谱重心偏了多少"——比逐态比较更稳健的体检。

</details>

**3.** Casida 方程的推导骨架：从 TDKS 方程出发做线性化，指明 $f_{xc}$ 在哪个环节进场、绝热近似砍掉了什么；说明 TDA 如何把问题化为本标准本征值。

<details markdown="1"><summary>点击显示答案</summary>

**步骤**：(i) TDKS 方程 $\big[-\tfrac12\nabla^2 + v_s[n](t)\big]\varphi_i(t) = i\dot\varphi_i(t)$，$v_s = v_\text{ext}(t) + v_H[n](t) + v_{xc}[n](t)$；(ii) 基态附近 $\varphi_i(t) = e^{-i\varepsilon_i t}\big[\varphi_i + \delta\varphi_i(t)\big]$，一阶展开；(iii) $\delta\varphi_i$ 用基态未占据轨道展开，系数 $P_{ia}(t), Q_{ia}(t)$；(iv) 一切密度扰动来自这些系数：$\delta n = \sum_{ia}\big(\varphi_i\varphi_a\big)(P + Q^*)$；(v) 自洽闭环：$\delta v_s$ 里的 $v_H$ 与 $v_{xc}$ 都是 $\delta n$ 的泛函——**$f_{xc} = \delta v_{xc}/\delta n$ 在这一环进场**（$v_H$ 那环给库仑核 $v_c(\vec r - \vec r')$，$f_{xc}$ 与之并联）。

**频率空间的本征值问题**：整理 $P, Q$ 的线性方程得

$$\begin{pmatrix} A & B \\ B^\* & A^\* \end{pmatrix}\binom{P}{Q^\*} = \omega\binom{P}{-Q^\*},\qquad A_{ia,jb} = \delta\delta\,\Delta_{ia}^{\text{KS}} + 2\!\int\!\!\int(\varphi_i\varphi_a)\big(v_c + f_{xc}\big)(\varphi_j\varphi_b),$$

（结构 = 3.1 节 RPA 矩阵 + $f_{xc}$ 染色）。**绝热近似**：$f_{xc}(\vec r,\vec r';\omega) \to f_{xc}(\vec r,\vec r';0)$（基态泛函导数）——砍掉的是核的**频率记忆**，换来：矩阵不含 $\omega$、本征值问题线性化。代价：双重激发的极点（需要 $\omega$ 依赖产生的高阶奇性）结构性消失。**TDA**：再扔 $B$ 块 → 标准厄米本征值问题 $AX = \omega X$（CIS 的 KS 版），好解、微破坏求和规则——多数生产计算采用。

</details>

**4.** 电荷转移失败的模型解剖：二位点单电子模型（给体 D、受体 A 相距 $R$），证明绝热 TD-DFT 的 CT 激发能随 $R$ 增大趋于常数（KS 能隙），而真实值含 $-1/R$ 衰减项；说明精确核的空间台阶如何修复。

<details markdown="1"><summary>点击显示答案</summary>

**真实 CT 能**：$\omega_\text{CT} = I_D - A_A - \tfrac{1}{R} + O(R^{-4})$——把电子从 D 搬到 A：花费电离能、收回亲合能、剩一对离子间的库仑吸引 $-1/R$。$R\to\infty$ 时 $\omega_\text{CT}\to I - A$（有限常数，但大 $R$ 下明显低于任何"分子内"能隙）。

**绝热 TD-DFT 的答案**：Casida 方程里单粒子底座是 KS 能隙 $\varepsilon_L^s - \varepsilon_H^s$，电子–空穴耦合项 $\propto\int\int\varphi_H\varphi_L(v_c + f_{xc})\varphi_H\varphi_L$——给受体轨道与给体轨道**空间不交叠**时积分趋零，得

$$\omega_\text{CT}^{\text{adia}} \to \varepsilon_L^s - \varepsilon_H^s\qquad(R\to\infty,\ \text{交叠}\to0).$$

而第 16 章自检问题 4 证明：KS 能隙 $= I - A - \Delta_{xc}$，近似泛函普遍 $\Delta_{xc}\to0$——**CT 能被系统性低估约一个导数不连续性**（GGA 上常见低估 1–2 eV）。

**精确核的修复**：$f_{xc}^{\text{exact}}$ 在基态密度由 D 区过渡到 A 区的地方长出一个**空间台阶**（高度 $\sim\Delta_{xc}/n$ 的脉冲型贡献），使电子–空穴耦合积分在零交叠极限下**不趋零**而趋 $\Delta_{xc}$，恰好补齐 $\omega_\text{CT} = (\varepsilon_L^s - \varepsilon_H^s) + \Delta_{xc} - 1/R = I - A - 1/R$ ✓。台阶是非局域的（依赖两端密度、跨整个分子），任何以局域密度泛函为核的近似天生没有——这就是"局域近似造不出 CT 激发"的定理式表述。工程绕道：长程修正泛函（CAM-B3LYR 把长程交换换成精确的）、或用范围分离的 $f_{xc}$。

</details>

**5.** EOM-CC：从 $H\lvert\Psi_n\rangle = E_n\lvert\Psi_n\rangle$ 与 $\lvert\Psi_n\rangle = R_ne^T\Phi_0$ 出发推导 $[\bar H, R_n] = \omega_n R_n$；解释为什么 $R$ 含双激发算符就能描述"双电子跃迁"、而基态的 $T_2$ 与激发的 $R_2$ 分工不同；并说明 EOM 激发能的大小一致性（size-intensivity）从何而来。

<details markdown="1"><summary>点击显示答案</summary>

**推导**：左乘 $e^{-T}$：

$$e^{-T}He^T R_n\Phi_0 = E_n R_n\Phi_0\;\Longrightarrow\;\bar H R_n\Phi_0 = E_n R_n\Phi_0.$$

基态方程 $\bar H\Phi_0 = E_0\Phi_0$（$\bar H$ 的 $\Phi_0$ 对角元定义）相减：

$$\bar H R_n\Phi_0 - R_n\Phi_0 E_0 = (E_n - E_0)R_n\Phi_0\;\Longrightarrow\;(\bar H - E_0)R_n\Phi_0 = \omega_n R_n\Phi_0.$$

由于 $R_n\Phi_0$ 张满激发扇区，等价于算符方程 $[\bar H, R_n] = \omega_n R_n$（$\bar H$ 中与激发数不对易的部分恰好生成谱）。求解时投影 $\langle\Phi_\mu\rvert$（$\mu$ = 单/双激发指标）得线性本征值问题——**非线性只在 $T$（基态解一次），激发谱是一次对角化**。

**$T_2$ 与 $R_2$ 的分工**：$T_2$ 描述**基态**里的动态相关（虚激发的相干叠加，第 15 章）；$R_n$ 描述**激发态相对于 CC 基态的组态内容**——$R_2\ne0$ 即"末态含双电子跃迁的实成分"（如 $\pi^2\to\pi^{\ast2}$ 态）。EOM 的结构红利：两态共享同一 $e^T$，动态相关在**差值**（激发能）里大幅相消——这就是精度来源。

**大小一致性（size-intensivity）**：远离子系统 A、B，激发定域在 A 上时，$R = R_A$（只含 A 的算符）、$T = T_A + T_B$，而 $[\bar H_B, R_A] = 0$（$\bar H_B$ 只作用于 B）：

$$\omega_n^{AB} = \omega_n^A\qquad(\text{与 } B \text{的存在无关}),$$

激发能严格可加/可分——相似变换的结构性质（第 15 章 $e^{T_A}e^{T_B}$ 因子化的直系后代），不依赖截断 rank。CI 型激发（在截断行列式空间对角化）没有这个保证——EOM 与截断 CI 的差距在激发态重演了第 15 章基态的故事。

</details>

## 参考

- Dreuw & Head-Gordon, Chem. Rev. 105, 4009 (2005)：TD-DFT 失败模式的权威综述（CT/Rydberg/双激发）。
- Casida, in Recent Advances in DFT (1995)：Casida 方程的标准推导。
- Stanton & Bartlett, J. Chem. Phys. 98, 7029 (1993)：EOM-CC 的奠基文献（含 $[\bar H, R] = \omega R$ 结构）。
- Runge & Gross, Phys. Rev. Lett. 52, 997 (1984)：TD-DFT 的合法性定理。
- Onida, Reining & Rubio, Rev. Mod. Phys. 74, 601 (2002)：BSE 与固体光学——第 5 节主线参考。
- Szabo & Ostlund 第 3 章习题：TDHF/RPA 的 H₂ 最小基标本。
