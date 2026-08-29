# 补充材料：分数量子霍尔效应与任意子

> 本书位置：凝聚态物理入门导论 第 11 章补充材料（配套正文：[量子 Hall 效应](11-quantum-hall-effect.md)，下文简称"第 11 章"——其第 8 节的"立此存照"在此兑现）。
> 前置知识：第 11 章（Landau 能级与简并度、填充因子、Laughlin 规范泵浦论证、边缘态）；第 12 章[拓扑物态入门](12-topological-phases.md)的 Berry 相位语言（本篇的统计相位推导全程用它）；第 3 章（费米海语言在"不可压缩液体"处的延伸）。
> 学习目标：理解部分填充为何必须靠相互作用出相（简并泥潭）；会写 Laughlin 波函数并用**等离子体类比**论证均匀密度 $\nu = 1/m$ 与不可压缩性；会推准粒子的分数电荷 $e/m$（高斯定律数出来）与分数统计 $\theta = \pi/m$（Arovas–Schrieffer–Wilczek 的 Berry 相位完整推导）；知道环面上的 $m$ 重简并与规范论证给出的 $\sigma_{xy} = \nu e^2/h$；认识复合费米子与非阿贝尔方向（下一站）。
>
> 记号约定：本书保留 $\hbar$。磁长度 $\ell_B = \sqrt{\hbar/eB}$（第 11 章），复坐标 $z = x + iy$，最低 Landau 能级（LLL）的轨道隐含高斯因子 $e^{-\lvert z\rvert^2/4\ell_B^2}$。

---

## 1. 一句话总结

**$\nu = 1/m$ 的平台不是单粒子填出来的，而是相互作用凝聚出的不可压缩量子液体：Laughlin 波函数 $\prod_{i\lt j}(z_i - z_j)^m$ 用"每个电子在同伴处强制安放 $m$ 阶零点"的代数办法让库仑排斥最优化，等离子体类比证明它密度均匀、有能隙；液体的元激发携带分数电荷 $e/m$、交换相位 $\theta = \pi/m$（既非玻色也非费米——任意子的第一个实例），环面基态 $m$ 重简并且局域测量无法区分——这三件"分数化信物"标志着一类全新的序。文小刚把它命名为拓扑序：相的区别不在对称性，而在长程纠缠的模式（展开见[拓扑序](12s-topological-order.md)）；本篇则把每件信物亲手推一遍。**

## 2. 从简并泥潭到量子液体

$\nu < 1$：最低 Landau 能级只部分填充。无相互作用时，$N$ 个电子在 $N_\Phi \gg N$ 个轨道里的每个 Slater 行列式都严格简并——**没有能隙、没有不变的密度、没有任何东西能钉住电导**（第 11 章 8 节的困境）。出路是库仑相互作用：它把简并泥潭凝聚成一个新基态。问题是：基态长什么样？

LLL 内波函数的一般形状（解析函数 × 公共高斯因子）。电子是费米子，多项式须反对称——交换两电子必须变号，而交换即 $z_i \leftrightarrow z_j$，所以**每对电子之间至少一个零点**。最经济的选择：每个坐标对只放一个零点，$m = 1$——这恰是 $\nu = 1$ 的满 LLL 行列式（Vandermonde）。**Laughlin 的洞见（1983）**：零点放多一点，$m = 3, 5, 7, \dots$（奇数，保反对称）：

$$\boxed{\;\Psi_m(z_1,\dots,z_N) = \prod_{i\lt j}(z_i - z_j)^m\, e^{-\sum_i \lvert z_i\rvert^2/4\ell_B^2}\;}$$

每个电子在其他电子处有 $m$ 阶零点——同伴靠近时波函数被压成 $r^m$，**排斥被"预付"进了波函数的解析结构**。这是第 14 章"变分猜形式"哲学最辉煌的一例：不解方程，猜一个具有全部对称性与正确渐近行为的波函数，让能量说话——对 $\nu = 1/3$ 的库仑问题，$\Psi_3$ 与后来的精确对角化基态重叠度超过 99%。

## 3. 等离子体类比：密度、屏蔽与不可压缩

怎么证明这个猜想态是均匀且不可压缩的？**Girard–Jastrow 到 plasma 的翻译**：把概率密度写成统计力学的配分函数。取模平方：

$$\lvert\Psi_m\rvert^2 \propto \exp\Big[-\beta V(\{z_i\})\Big],\qquad V = -\sum_{i\lt j}q^2\ln\lvert z_i - z_j\rvert + \sum_i \frac{q^2\,\lvert z_i\rvert^2}{4m\ell_B^2},\qquad \beta q^2 = 2m.$$

逐项读：$-\ln r$ 是**二维**库仑势（$\nabla^2(-\ln r) = -2\pi\delta(r)$，二维点电荷的解）；$r^2$ 势等价于一个均匀的**中性化正电背景**，其密度由高斯定律定出（自检问题 2）：

$$\rho_{\text{bg}} = \frac{1}{2\pi m\,\ell_B^2}\qquad\Longleftrightarrow\qquad \nu = \frac{\rho}{1/2\pi\ell_B^2} = \frac{1}{m}.$$

于是 $|\Psi_m|^2$ = 一盒二维单成分等离子体的玻尔兹曼权重。**屏蔽**（$m \ge 2$ 时耦合足够强）是等离子体的铁律：任何局域电荷涨落都被周围反号云瞬时中和——电子密度处处精确抵消背景，**均匀、不可压缩**。能隙的开出（激发谱的严格论证超出本篇，数值与理论一致：$\nu = 1/3$ 处 $\Delta \sim 0.1\,e^2/\epsilon\ell_B$）把"液体"钉成有刚性的相。$m = 1$ 是无相互作用的精确极限（$2m = 2$，正好 Slater 行列式），等离子体类比对它也是精确的。

## 4. 准孔：分数电荷

在 $z_0$ 处"扎一个洞"：

$$\Psi_{z_0} = \prod_i (z_i - z_0)\,\Psi_m.$$

解析结构：电子在 $z_0$ 处获得零点——密度在那里被压低。压低多少？等离子体类比直接回答（自检问题 3）：$\prod_i(z_i - z_0)$ 在配分函数里扮演**检验电荷** $q/m$；屏蔽云为中和它而在 $z_0$ 周围积起等量反号电荷——按电子电荷折算，密度亏损恰好

$$\delta Q = +\frac{e}{m}\qquad(\text{准孔电荷；准电子对应 } -\tfrac{e}{m}).$$

分数电荷不是假设而是计数：$m$ 个电子分享 $m$ 个磁通量子的地皮，扎走一个通量的洞，就欠下一份 $e/m$。它已被shot-noise 实验（1995–97）直接称量：$\nu = 1/3$ 平台上输运电荷的颗粒是 $e/3$。

## 5. 分数统计：ASW 推导

交换两个准孔，得到的相位既非 0（玻色）也非 $\pi$（费米）。完整推导（Arovas–Schrieffer–Wilczek 1984，按 Berry 相位的标准流程）是本篇的技术高潮，骨架在此、细节在自检问题 4：

1. **绝热输运**：让 $z_0$ 沿闭合回路 $C$ 缓慢移动，态始终停留在归一化的 $|\Psi_{z_0}\rangle$，积累 Berry 相位

$$\gamma_C = \oint_C \mathrm{Im}\,\Big\langle\Psi_{z_0}\Big\lvert\,\nabla_{z_0}\,\Big\lvert\Psi_{z_0}\Big\rangle\cdot d\vec z_0.$$

2. **LLL 积分恒等式**（全纯波函数 + 高斯测度的分部积分）：$\big\langle\sum_i \partial_{z_i}G\big\rangle = \frac{1}{2\ell_B^2}\big\langle\sum_i z_i^*\,G\big\rangle$。取 $G = \ln\prod_i(z_i - z_0)$ 得 $\big\langle\sum_i (z_i - z_0)^{-1}\big\rangle = \frac{1}{2\ell_B^2}\langle\sum_i z_i^*\rangle$。
3. **密度亏损进场**：均匀盘内 $\int \bar z\,\rho_0\,d^2z = 0$，只有 $z_0$ 处的亏损（$1/m$ 个电子）贡献——给出 $\gamma_C = \dfrac{A(C)}{m\,\ell_B^2} = 2\pi\times(\text{围住的电子数})$。
4. **统计相位**：绕行一圈若围住**另一个准孔**，它自身携带 $1/m$ 个电子的亏损——围住的电子数比空区域少 $1/m$，Berry 相位差 $\delta\gamma = -\frac{2\pi}{m}$。绕一圈 = 交换两次，**交换一次的统计角**

$$\boxed{\;\theta = \frac{\pi}{m}\;}$$

$m = 1$ 回到费米的 $\pi$（准孔即空穴）；$m = 3$ 给 $\theta = \pi/3$。统计角的连续取值（0 到 π 之间任意）就是**任意子（anyon）**——二维世界独有的自由度（三维里编织群的拓扑只有 0/π 两档，二维的辫群给了连续谱，见 12s）。

## 6. 环面上的 $m$ 重简并：拓扑信物之三

把体系放到环面（周期边界）上，Landau 能级的磁平移代数（$T_1T_2 = e^{2\pi i/N_\Phi}T_2T_1$，第 11 章 3.4 节的同族结构）与 Laughlin 波函数的质心结构合谋：基态不是一重而是 **$m$ 重简并**（计数见自检问题 5）。要点不在简并本身，而在它的性质：

- **局域扰动拆不动它**：简并态在局域算符下的矩阵元完全相同（密度分布无法区分），能级分裂只能由绕环面的非局域过程诱导、随体系尺寸指数衰减（12s 把这做成定理级的表述）；
- 简并度 $m$ 与波函数细节无关，只挂在"液体属于哪个 $\nu$"上——**一个非局域的、鲁棒的分类标签**。这正是"序"该干的事，但它不是第 7 章的对称性破缺：$m$ 不同的液体对称性完全相同。

## 7. 收口：$\sigma_{xy}$、层级与下一站

**电导的规范论证**：把第 11 章 Laughlin 泵浦论证（穿过体系中心插一个磁通量子，电荷被泵到边缘）原样重跑，只是泵的颗粒从 $e$ 换成 $e/m$：每插入一个 $\Phi_0$，径向输运电荷 $e/m$，$\sigma_{xy} = \dfrac{e/m}{\Phi_0} = \dfrac{e/m}{h/e} = \dfrac{1}{m}\dfrac{e^2}{h}$（自检问题 1 把完整账算平）。分数平台与分数电荷是同一件事的两面。

**层级与复合费米子**（一段话）：$\nu = 1/3$ 之外的平台（$2/5, 3/7, \dots$）由 Jain 的复合费米子图像统一：给每个电子绑上 $2k$ 个磁通量子，剩下的"复合粒子"在有效场 $B^* = B - 2k n\Phi_0$ 里填整数 Landau 能级 $\nu^* = p$，换算回去

$$\nu = \frac{p}{2kp + 1}\qquad(1/3 = \tfrac{1}{2\cdot1+1},\ 2/5 = \tfrac{2}{2+1},\dots)$$

——分数态 = 复合费米子的整数态，第 11 章的全部机器在新的"粒子"上重演。非阿贝尔的下一站在 $\nu = 5/2$：那里的准孔是**非阿贝尔任意子**（交换 = 融合空间里的矩阵而非相位），属于 12s 的领土。

至此三件信物齐了：**分数电荷、分数统计、拓扑简并**。它们没有一样能用对称性语言描述——文小刚由此提出：这类相的序住在纠缠里，不在群论里。展开见[拓扑序：长程纠缠、规范结构与弦网](12s-topological-order.md)。

## 小结

- Laughlin $\Psi_m$：零点 = 预付的排斥；等离子体类比 $\Rightarrow$ 均匀密度 $\nu = 1/m$、屏蔽即不可压缩。
- 三件信物：$e/m$（高斯定律计数）、$\theta = \pi/m$（ASW：LLL 恒等式 + 密度亏损）、环面 $m$ 重简并（局域不可分）。
- $\sigma_{xy} = \nu e^2/h$：泵浦论证在分数电荷版下的重演。
- 层级 $\nu = p/(2kp+1)$：复合费米子把分数世界编译回整数机器。
- 分数统计只在二维合法：辫群 vs 置换群（12s 接力）。

| | 整数 QH（第 11 章） | 分数 QH（本篇） |
|---|---|---|
| 平台机制 | 单粒子能级填满 | 相互作用凝聚 |
| 载流子 | 电子 $e$ | 准粒子 $\pm e/m$ |
| 交换相位 | $\pi$（费米） | $\pi/m$（任意子） |
| 环面简并 | 1 | $m$ |
| 序的类型 | 能带拓扑（SPT） | 内禀拓扑序（12s） |

## 自检问题

**1.** 规范泵浦的分数账：在 Laughlin 态的环面/圆环上绝热插入一个磁通量子，用准孔电荷 $e/m$ 重跑第 11 章的论证，推出 $\sigma_{xy} = \frac{1}{m}\frac{e^2}{h}$，并核对 Faraday 感应电场做的功与化学功的平衡。

<details markdown="1"><summary>点击显示答案</summary>

**泵浦**：插入磁通 $\delta\Phi$ 的过程在径向感应出环形电场 $E_\theta$；准孔（电荷 $q = e/m$）受感应场作用被径向输运——第 11 章已证：对不可压缩的量子液体，插满一个 $\Phi_0$ 恰好把一个**最小组态单元**从内边搬到外边。单元的电荷：$\nu = 1/m$ 态中，一个磁通量子对应 $1/m$ 个电子的密度份额，故

$$\Delta Q = \frac{e}{m}\qquad(\text{每 }\Phi_0).$$

**电导**：由 $\sigma_{xy} = \frac{\Delta Q}{\Delta t}/\frac{\Delta\Phi}{\Delta t} = \frac{e/m}{\Phi_0} = \frac{e/m}{h/e} = \frac{e^2}{mh}$。✓

**能量账**：Faraday 场对输运电流做的功 $W = I\,\delta\Phi$（每秒每磁通）；这份功以霍尔电压的形式存进化学势差：$W = \Delta Q\,V_H$。两账相等即 $V_H = I\,\Phi_0/\Delta Q\cdot\cdots = I/(\nu e^2/h)$——$R_{xy} = h/\nu e^2$，平台电阻的倒数正是 $\sigma_{xy}$。**注意论证的骨架全部来自第 11 章**（规范不变 + 绝热 + 不可压缩），唯一的分数输入是"最小组态单元 $= e/m$"——规范论证自己不产生分数化，它忠实记账。

</details>

**2.** 等离子体类比的完整推导：把 $|\Psi_m|^2$ 写成二维单成分等离子体的配分函数，由高斯定律定出中性化背景密度，证明屏蔽给出均匀电子密度 $\nu = 1/m$；并说明 $m=1$ 时该类比精确、$m \ge 2$ 时需要什么条件。

<details markdown="1"><summary>点击显示答案</summary>

**配分函数**：取 $\lvert\Psi_m\rvert^2 = \prod_{i\lt j}\lvert z_i - z_j\rvert^{2m}e^{-\sum\lvert z_i\rvert^2/2\ell_B^2}$，写为 $e^{-\beta V}$：

$$V = -\underbrace{\sum_{i\lt j}q^2\ln\lvert z_i - z_j\rvert}_{\text{二维库仑排斥}} + \underbrace{\sum_i \frac{q^2\,\lvert z_i\rvert^2}{4m\ell_B^2}}_{\text{背景吸引}}，\qquad \beta q^2 = 2m.$$

核对第二项：$e^{-\beta q^2\lvert z\rvert^2/4m\ell_B^2} = e^{-2m\lvert z\rvert^2/4m\ell_B^2} = e^{-\lvert z\rvert^2/2\ell_B^2}$ ✓。

**背景密度**：二维中密度 $\rho_{\rm bg}$ 的均匀圆盘在其内部产生的库仑势（$\nabla^2\phi = -2\pi\rho$，$\phi \sim -\pi\rho r^2/2$ 型）：一个检验电荷 $q$ 在盘内的势能 $= q^2\pi\rho_{\rm bg}\lvert z\rvert^2/2$（把常数与单位折进定义）。与 $V$ 的第二项比对：

$$\frac{q^2\pi\rho_{\rm bg}}{2} = \frac{q^2}{4m\ell_B^2}\ \Longrightarrow\ \rho_{\rm bg} = \frac{1}{2\pi m\ell_B^2}.$$

**屏蔽 $\Rightarrow$ 均匀**：等离子体是完美导体——内部任何过剩电荷被屏蔽云中和，体内静电场为零。电子密度必须处处精确抵消背景：$\rho_e = \rho_{\rm bg}$，即

$$\nu = \frac{\rho_e}{\text{每通量一个态}} = \frac{1/(2\pi m\ell_B^2)}{1/(2\pi\ell_B^2)} = \frac{1}{m}. ✓$$

**条件**：$m = 1$（$\Gamma \equiv \beta q^2 = 2$）：等式实际上是恒等式——$\Psi_1$ 就是满 LLL 行列式，密度均匀是精确的（Vandermonde）。$m \ge 3$（$\Gamma = 2m \ge 6$）：二维 OCP 在强耦合区处于屏蔽相，类比有据；严格性靠数值模拟（经典 OCP 的关联函数）与精确对角化背书，典型的"物理严格 + 数值确认"结构。

</details>

**3.** 用等离子体屏蔽论证准孔电荷 $e/m$：写出 $\Psi_{z_0}$ 对应的检验电荷，数出屏蔽云的电子亏损。

<details markdown="1"><summary>点击显示答案</summary>

**检验电荷**：$\lvert\Psi_{z_0}\rvert^2$ 比 $\lvert\Psi_m\rvert^2$ 多出因子 $\prod_i\lvert z_i - z_0\rvert^2 = e^{2\sum_i\ln\lvert z_i - z_0\rvert} = e^{-\beta V_{\text{imp}}}$，其中

$$V_{\text{imp}} = -\sum_i q_{\text{imp}}q\,\ln\lvert z_i - z_0\rvert\Big\lvert_{\beta q_{\text{imp}}q = 2}\ \Longrightarrow\ q_{\text{imp}} = \frac{q}{m}.$$

即：在 $z_0$ 处放了一个电荷 $q/m$ 的**检验粒子**（注意比电子电荷 $q$ 小 $m$ 倍）。

**屏蔽云**：等离子体为中和检验电荷，在 $z_0$ 周围积起一团总电荷 $-q/m$ 的屏蔽云；云由电子（电荷 $q$）密度**降低**构成——等效于"挖走" $1/m$ 个电子：

$$\delta n_e = -\frac{1}{m}\quad\Longleftrightarrow\quad \delta Q = +\frac{e}{m}\ (\text{以电子电荷缺失计}).$$

**一致性核对**：整块液体的总电荷守恒——准孔是"$1/m$ 个电子的空位"；$m$ 个准孔 = 缺一个电子。另一头核对磁通：$\nu = 1/m$ 意味着每 $m$ 个磁通量子配 $1$ 个电子，故一个磁通量子的地皮恰好供养 $1/m$ 个电子——准孔（绑定一个磁通量子的洞）带走 $e/m$，两本账吻合。

</details>

**4.** 完成 ASW 推导：从 LLL 积分恒等式出发，证明绕回路 $C$ 的 Berry 相位 $\gamma_C = A(C)/m\ell_B^2 = 2\pi N_{\text{enc}}$（$N_{\text{enc}}$ 为围住的电子数），并由此导出交换两个准孔的统计角 $\theta = \pi/m$。

<details markdown="1"><summary>点击显示答案</summary>

**恒等式**：LLL 态形如 $\psi = f(\{z_i\})e^{-\sum\lvert z_i\rvert^2/4\ell_B^2}$。对任一全纯函数 $G$，$\int d^2z_i\,\partial_{\bar z_i}(\lvert\psi\rvert^2 G) = 0$（全平面边界为零）分部积分给出

$$\Big\langle\sum_i \partial_{z_i}G\Big\rangle = \frac{1}{2\ell_B^2}\Big\langle\sum_i z_i^* G\Big\rangle.$$

取 $G = \ln\prod_i(z_i - z_0)$（准孔因子）：$\partial_{z_i}G = (z_i - z_0)^{-1}$，

$$\Big\langle\sum_i \frac{1}{z_i - z_0}\Big\rangle = \frac{1}{2\ell_B^2}\Big\langle\sum_i z_i^*\Big\rangle.$$

**右边的账**：$\langle\sum_i z_i^*\rangle = \int \bar z\,\rho(\vec z)\,d^2z$。密度 = 均匀 $\rho_0$（盘对称，积分为零）+ $z_0$ 处的亏损（$1/m$ 个电子，局域在 $z_0$）：$= -\frac{1}{m}\,\bar z_0$。故

$$\Big\langle\sum_i \frac{1}{z_i - z_0}\Big\rangle = -\frac{\bar z_0}{2m\ell_B^2}.$$

**Berry 相位**：$\gamma_C = \oint \mathrm{Im}\big\langle\sum_i (z_i - z_0)^{-1}\big\rangle\,dz_0$。圆形回路 $z_0 = re^{i\theta'}$（包围均匀密度面积 $A = \pi r^2$）：

$$\gamma = \int_0^{2\pi}\mathrm{Im}\Big[-\frac{re^{-i\theta'}}{2m\ell_B^2}\Big]\,i\,re^{i\theta'}d\theta' = \int_0^{2\pi}\frac{r^2}{2m\ell_B^2}d\theta' = \frac{\pi r^2}{m\ell_B^2} = \frac{A}{m\ell_B^2}.$$

用 $N_{\text{enc}} = \rho_0 A = A/(2\pi m\ell_B^2)$ 改写：$\gamma = 2\pi N_{\text{enc}}$ ✓（数值上恰是"围住 $N$ 个电子相位 $2\pi N$"——单个电子的整数相位不携带分数信息）。

**统计角**：回路若围住另一个准孔，该处密度亏损 $1/m$ 个电子：$N_{\text{enc}} \to N_{\text{enc}} - 1/m$，

$$\delta\gamma = 2\pi\times\Big(-\frac{1}{m}\Big) = -\frac{2\pi}{m}.$$

绕行一圈 = 准孔甲绕乙一周 = **交换两次**；交换一次（半圈）：

$$\theta = \frac{\delta\gamma}{2} = \frac{\pi}{m}. ✓$$

核对极限：$m = 1$：$\theta = \pi$，准孔 = 满能级中的空穴 = 费米子 ✓。**方法论注记**：整个推导只用 (i) LLL 全纯结构、(ii) 密度均匀 + 屏蔽——没有一个字涉及相互作用的细节，分数统计是**拓扑性的**（这也是它对样品 disorder 免疫的原因）。

</details>

**5.** 环面简并计数：利用磁平移代数 $T_1T_2 = e^{2\pi i/N_\Phi}T_2T_1$ 与 Laughlin 态在环面上的构造，论证基态简并度恰为 $m$。

<details markdown="1"><summary>点击显示答案</summary>

**磁平移代数**：环面上两方向的基本平移各移一个格距，由于磁通，$T_1T_2 = e^{2\pi i/N_\Phi}T_2T_1$（第 11 章 3.4 节的亲代数）。

**Laughlin 态的平移性质**：$\Psi_m$ 可分解为"质心部分 × 相对部分"。相对部分由 $\prod_{i\lt j}(z_i - z_j)^m$ 承担（平移不变地跟质心走）；质心部分在环面上的边界条件允许**恰好 $m$ 个互不等价的动量扇区**：把体系整体平移 $m$ 次单胞长度后相位复原 $e^{2\pi i mN/N_\Phi}\cdot\cdots = 1$（用 $N_\Phi = mN$），中间经过 $m$ 个不同的质心动量 $K = 0, 1, \dots, m-1$（以 $2\pi/mL$ 为单位）。

**代数核对**：局域哈密顿量（库仑作用 + 均匀背景）与两个**大平移** $T_1^m\ell_0$、$T_2^m\ell_0$（移 $m$ 个磁元胞）对易——它们作用在基态子空间上给出 $m$ 维表示；而这些大平移自身的对易结构 $T_1^mT_2^m = e^{2\pi i m\cdot m/N_\Phi}\cdots = e^{2\pi i m/N}$ 生成 $\mathbb{Z}_m$ 型交换对称。不可约表示分析（或直接构造 $m$ 个质心动量波函数）给出

$$\dim\{\text{基态}\} = m.$$

**要点**：简并度 = 波函数零点阶数 = 分母 = 拓扑标签，与体系尺寸、相互作用强度、甚至波函数的具体形状**全部无关**——微扰只能以指数小的量分裂它（分裂来自绕环面的虚拟隧穿，12s 把这个机制做成普适定理）。这正是 12s 拓扑简并的定义性实例。

</details>

## 参考

- R. B. Laughlin, Phys. Rev. Lett. 50, 1395 (1983)：波函数原始文献。
- S. M. Girvin 的 Les Houches 讲义与 D. Tong《Lectures on the Quantum Hall Effect》(2016) 第 3 章：等离子体类比与 ASW 推导的标准讲法。
- D. Arovas, J. R. Schrieffer & F. Wilczek, Phys. Rev. Lett. 53, 722 (1984)：分数统计的 Berry 相位推导。
- J. K. Jain, "Composite-fermion approach" (1989) 与《Composite Fermions》(2007)：层级态的统一图像。
- 文小刚《Quantum Field Theory of Many-Body Systems》(2004)：拓扑序概念与有效场论的原始阵地（衔接 12s）。
