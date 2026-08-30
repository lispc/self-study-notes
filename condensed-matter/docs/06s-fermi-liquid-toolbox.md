# 补充材料：费米液体补全——动理学方程、求和规则、不稳定性与 Luttinger 定理

> 本书位置：凝聚态物理入门导论 第 6 章补充材料（配套正文：[相互作用电子气](06-interacting-electron-gas.md)第 7–8 节，下文简称"第 6 章"——那里立起了绝热连续、准粒子寿命与 Landau 参数的骨架，本篇把其余零件补齐）。
> 前置知识：第 6 章 §7（Landau 能量泛函、$f$ 函数、$F_l^{s,a}$、寿命的相空间论证）；第 3 章（Drude/Sommerfeld 的输运与比热、$g(E_F)$）；[07s](07s-why-iron-magnetic.md)（Stoner 判据——本篇将把它认领为 Pomeranchuk 失稳的特例）；第 17 章（格林函数与 $Z$ 因子的语言）；[12s](12s-topological-order.md)（拓扑不变量——Luttinger 定理的现代读法用它的思维方式）。
> 学习目标：会写会解 Landau–Silin 动理学方程，推出**零声**的色散方程并讨论其极限；会从能量泛函推出 $\kappa$、$\chi$ 与 Galilean 恒等式 $m^\ast/m = 1+F_1^s/3$（背流）；理解 **Pomeranchuk 判据** $F_l > -(2l+1)$ 及费米液体的三种自毁方式（铁磁、向列、超导），并把 Stoner 判据翻译成 $F_0^a\to-1$；掌握 **Luttinger 定理**的内容、Oshikawa 磁通论证与其拓扑读法；认识费米液体的实验体检表（$\rho=\rho_0+AT^2$、Kadowaki–Woods 比值、ARPES 的 $Z$、量子振荡）与越界的信号（marginal 费米液体、一维）。
>
> 记号约定：沿用第 6 章（高斯单位制）。$\mu_B$ 为玻尔磁子；$n_{\vec k\sigma}$ 为准粒子占据数，$u_{\vec k} = n_{\vec k}-n_{\vec k}^{(0)}$ 为对平衡的偏离。

---

## 1. 一句话总结

**Landau 的框架在正文立了柱，本篇上梁：动理学方程 $\partial n/\partial t + \dot{\vec r}\cdot\nabla_{\vec r}n - \dot{\vec k}\cdot\nabla_{\vec k}n = I_{\text{coll}}$ 把准粒子组织成经典流体——无碰撞极限下它预言零声（费米面上以 $s\gtrsim v_F$ 传播的形状波），流体力学极限下回到普通第一声；能量泛函的变分给出三个守恒律包装的求和规则——压缩率 $\kappa$、磁化率 $\chi$ 含 $F_0$，而 Galilean 恒等式 $m^\ast/m = 1+F_1^s/3$ 是动量守恒逼出的"背流"；费米液体会自己诊断自己的死期——Pomeranchuk 判据 $F_l>-(2l+1)$，铁磁（$l=0$ 自旋道，恰是 07s 的 Stoner 判据 $F_0^a=-1$）与向列序（$l=2$）都在其上，Cooper 通道是判据之外的第三种死法；Luttinger 定理（费米体积对任意相互作用不动）有 Oshikawa 的穿磁通拓扑论证，把费米面升格为多体基态的拓扑量；实验体检表以 $\rho = \rho_0+AT^2$ 与 Kadowaki–Woods 比值为纲——一旦 $T$ 线性电阻或幂律谱函数现身，就是费米液体让位的讣告。**

## 2. Landau–Silin 动理学方程

第 6 章给了准粒子的**能量**，没给它们的**动力学**。Landau 的假设：准粒子占据数 $n_{\vec k\sigma}(\vec r, t)$ 遵守玻尔兹曼型方程（Silin 把它推广到含磁矩的液体）：

$$\frac{\partial n}{\partial t} + \frac{\partial\varepsilon}{\partial\vec k}\cdot\nabla_{\!\vec r}\,n - \frac{\partial\varepsilon}{\partial\vec r}\cdot\nabla_{\!\vec k}\,n = I_{\text{coll}}[n],$$

与第 3 章 Drude 的玻尔兹曼方程**形似而神不同**：这里的 $\varepsilon[\vec k; n]$ 本身是占据数的泛函——准粒子推挤会改变彼此的能量（$f$ 函数进场），碰撞积分 $I_{\text{coll}}$ 的弛豫时间由第 6 章的相空间论证 $\tau^{-1}\propto(\varepsilon-E_F)^2+\pi^2(k_BT)^2$ 提供。两个极限：

- **流体力学极限**（$\omega\tau\ll1$，碰撞频繁）：局域平衡，输运是扩散型的——普通声波（第一声）；
- **无碰撞极限**（$\omega\tau\gg1$，低温高频）：$I_{\text{coll}}\to0$，但方程依然非平凡——因为 $f$ 函数的**平均场回复力**独自支撑振荡。这就是零声。

**零声的物理**：费米面整体做微小的四极变形并传播——不是密度波（普通声），是**形状波**（frozen shape surfing at ~v_F）。推导（完整版见自检问题 1）落地为一个超越方程：

$$s\ln\frac{s+1}{s-1} = 2 + \frac{2}{F_0^s},\qquad s = \frac{\omega}{qv_F}\ \gt 1,$$

- $F_0^s\to0^+$：$s\to1^+$——极弱的形状波，速度贴着 $v_F$（与第 6 章"任意小斥力即有不衰减模式"的 RPA 精神一致）；
- $F_0^s\gg1$：$s\approx\sqrt{F_0^s/3}$——刚性液体快跑。

零声在 $\rm He^3$（$F_0^s\approx10$）中被直接观测到（1966 年声阻抗反常），是费米液体理论的招牌验证。更高 $l$ 的解（$u\propto P_l$）需要相应 $F_l$ 足够大——$l=2$ 的解正是向列相涨落（第 4 节）。顺带：这个"平均场自发振荡"与第 6 章 RPA 等离激元是**同一件事的两种介质**——那里长程库仑把振荡推到 $\omega_p$ 的高频，这里短程 $f$ 把它压在 $qv_F$ 量级。

## 3. 守恒律的账单：求和规则三连

第 6 章引用了三个公式，这里逐一兑现（完整推导见自检问题 2、3）：

**压缩率**（$l=0$ 的电荷形变——均匀膨胀费米球）：

$$\frac{\kappa}{\kappa_0} = \frac{m^\ast/m}{1+F_0^s}$$

**磁化率**（$l=0$ 的自旋形变——自旋上下两团费米球的相对位移）：

$$\frac{\chi}{\chi_0} = \frac{m^\ast/m}{1+F_0^a}$$

**Galilean 恒等式**（$l=1$ 的电荷形变——整体流动）：

$$\frac{m^\ast}{m} = 1 + \frac{F_1^s}{3}$$

前两个的机理一眼见底：均匀形变只涉及费米面态密度（$m^\ast$）与 $l=0$ 的相互作用修正——$F_0^s>0$（同种电荷挤压更贵）压低 $\kappa$；$F_0^a<0$（自旋反平行对更贵、平行倾向被奖励——07s 的 Stoner 交换正是这个符号）放大 $\chi$，因子 $(1+F_0^a)^{-1}$ 在 $F_0^a\to-1$ 处发散（³He 的 $F_0^a\approx-0.7$，磁化率增强三四倍，是液体理论的经典战果）。第三个最深刻：$m^\ast$ 本不该由 $f$ 函数决定（它是准粒子色散的定义），但**动量守恒**强迫它表达为 $F_1^s$——Galilean 不变的液体里，一个准粒子的运动必须拖曳周围的背流（backflow），使**总**动量恰为 $\hbar\vec k$；把电流用两种方式算（准粒子流 + 背流修正），就锁死了 $m^\ast/m = 1+F_1^s/3$。注意它顺带给出 Pomeranchuk 的第一条款：$m^\ast>0\Rightarrow F_1^s>-3$ **自动满足**——电荷 $l=1$ 形变（整体加速）永不失稳，守恒律护体。

## 4. Pomeranchuk 判据：费米液体的自我诊断

问能量泛函：把费米面做 $l$ 阶变形（半径 $k_F\to k_F+\delta k\,P_l(\cos\theta)$），能量是涨是跌？直接计算（自检问题 4）：形变能量 $\propto \big(1+\frac{F_l^{s,a}}{2l+1}\big)\,\delta k^2$。于是稳定性要求

$$\boxed{\;F_l^{s,a} > -(2l+1)\;\;(\text{Pomeranchuk 判据})\;}$$

**三种死法逐一认领**：

- **铁磁**（$l=0$，自旋道）：$F_0^a\to-1^- $ 时 $\chi$ 发散、费米球两旋分家——这正是 07s 的 Stoner 判据：$I\,N(E_F)>1$ 换算过来就是 $F_0^a = -N(0)I\lt-1$。07s 用能带语言绕的远路，在费米液体理论里是一行求和规则——**两条路线在同一处会师**（这也是检验两章自洽的好扣子）。
- **向列相**（$l=2$，电荷道）：$F_2^s\lt-5$ 时费米面自发变椭圆——破缺旋转而不破缺平移，电子液体版的液晶。Sr₃Ru₂O₇ 磁场下的中间相、铁基超导的上方"向列涨落"都是它的候选现场；零声一节说过，$l=2$ 的无碰撞振荡就是它的动态指纹。
- **超导**（Cooper 通道）：不属于 Pomeranchuk 家族——配对不是费米面的光滑形变，而是 $\pm k_F$ 两点的联合畸变；费米面重整化群（第 6 章 §8）里它与前向散射并列为仅有的两个不 irrelevant 的通道，第 8 章全程处理它。

加上非局域的第四种（Mott：绝热连续假设直接崩，第 13/17 章），费米液体的讣告簿就齐了。方法论要点：**这些失稳全部写在 $f$ 函数里**——宏观唯象参数（几个 $F_l$）预告了整个相图的边界，这是 Landau 理论"少胜多"的极致。

## 5. Luttinger 定理：费米面是拓扑量

第 3 章以来全书默认：相互作用再强（只要是费米液体），**费米面包围的体积不变**——电子数密度 $n$ 等于费米体积的两倍（自旋简并）。这句默认有名字：**Luttinger 定理**（1960；原始证明靠格林函数的解析性：微扰级数里费米体积的移动逐阶相消）。

**Oshikawa 的论证**（2000，现代化、不依赖微扰）骨架（细节见自检问题 5）：把体系放在环面上，沿一个环路绝热穿入一个磁通量子 $\Phi_0 = h/e$。规范变换把通量搬进边界条件：每个电子的晶体动量平移 $2\pi/L$，多体基态总动量平移 $N\cdot 2\pi/L$。另一方面，绝热过程（假设不关闭能隙、不碰简并）把基态带回基态——其动量只能改变晶格周期的整数倍。两本账相抵：

$$N = 2V_F + (\text{每个原胞的整数})\ \Longrightarrow\ \text{费米液体里（无奇异）取平凡整数：}\ n = 2V_F.$$

**拓扑读法**（与 12s 同一思维方式）：费米体积像拓扑序的不变量一样，是**基态的整体性质**，对局域扰动与连续的相互作用变形免疫；定理不问你任何动力学细节。同样地，它的失效也必须"整体地"发生：Mott 绝缘体（$U$ 打开电荷隙，费米面被整块吃掉却保持粒子数）、分数化的某些奇异金属（费米体积可以偏离整数电子数）——**Luttinger 定理的破口就是费米液体疆界的界碑**。一维的 Luttinger 液体（20s）没有准粒子，却仍服从"广义 Luttinger 定理"（体积意义上的费米面还在）——定理比准粒子更结实。

## 6. 实验体检表：怎么判断一块材料是不是费米液体

- **电阻的 $T^2$ 律**：第 6 章 $1/\tau\propto T^2$（电子–电子散射的 Pauli 相空间）经第 3 章的 Drude 框架直接翻成

$$\rho(T) = \rho_0 + AT^2\qquad(\rho_0\ \text{为杂质残留})，$$

电子–声子散射在低温（$T\ll\Theta_D$）只贡献 $T^5$（Bloch–Grüneisen），故极低温的 $T^2$ 主导就是费米液体的签名。偏离（最著名：铜氧化物奇异金属的 $T$ 线性电阻，第 13 章）即"非费米液体"的第一现场。
- **Kadowaki–Woods 比值**：$A\propto(m^\ast)^2$（散射率与态密度各带一个 $m^\ast$）与 $\gamma\propto m^\ast$ 合并预言 $A/\gamma^2\approx$ 普适常数——重费米子家族跨越三个数量级的 $m^\ast$ 仍近似踩在这条线上（第 13 章的重电子比热与这里的输运在同一杆秤上称量）。
- **ARPES**（第 17 章的语言）：费米液体 = 谱函数里一个尖锐准粒子峰（权重 $Z$）骑在非相干背景上；峰宽 $\propto(\omega^2+\pi^2T^2)$ 消失于费米面。$Z$、$m^\ast$（色散斜率）、峰–背景对比度三个数一次测齐。
- **量子振荡**（de Haas–van Alphen）：磁化率随 $1/B$ 振荡，频率 $F\propto$ 费米面极值截面积（Luttinger 定理的尺子：**测费米体积**），振幅的温度衰减（Lifshitz–Kosevich）**称 $m^\ast$**——既测体积又测质量，是检验费米液体（及其 Luttinger 定理）的黄金标准；Mott 邻域的"费米体积重构"由此现形。

体检结论的用法：$T^2$ 电阻 + Kadowaki–Woods 踩线 + ARPES 见极点 + 量子振荡给出合理的体积与质量——费米液体健康；任何一项异常（$T$ 线性、幂律谱、非整数费米体积）都是转诊单，目的地通常是第 13 章（强关联）或 20s（一维）。

## 7. 越界一览（收口）

- **Marginal 费米液体**：$1/\tau\propto\omega$（恰好踩线，"$\omega^2$" 的幂次退化到 1），电阻 $T$ 线性——奇异金属的唯象模板（第 13 章的高温超导正常态）。
- **一维**：费米液体**原则上不存在**——散射相空间论证在 1D 直接失效，任何相互作用都摧毁准粒子极点，接替者是 Luttinger 液体（自旋–电荷分离、分数化）：见[一维的无费米面世界](20s-luttinger-liquid.md)。
- **Mott 与超导**：第 13、8 章的老住户，此处只留一句话——Pomeranchuk 与 Luttinger 两道堤坝之外，还有两处决口。

## 小结

- 动理学方程：准粒子的玻尔兹曼方程 + 平均场自洽（$\varepsilon[n]$）；零声 = 无碰撞极限的形状波，$s\ln\frac{s+1}{s-1} = 2+\frac{2}{F_0^s}$。
- 求和规则三连：$\kappa$、$\chi$（含 $F_0$），$m^\ast/m = 1+F_1^s/3$（背流/动量守恒）；电荷 $l=1$ 永不失稳。
- Pomeranchak：$F_l>-(2l+1)$；铁磁（$F_0^a=-1$ = Stoner）与向列（$F_2^s=-5$）是费米液体自我诊断的死法，Cooper 与 Mott 是判据外的另两种。
- Luttinger 定理：$n = 2V_F$；Oshikawa 磁通论证给出拓扑读法；破口即非费米液体的界碑。
- 体检表：$\rho_0+AT^2$、$A/\gamma^2$、ARPES 的 $Z$ 与极点、量子振荡的体积与质量。

| 信物 | 费米液体值 | 越界信号 |
|---|---|---|
| $\rho(T)$ 低温 | $\rho_0 + AT^2$ | $T$ 线性（marginal/奇异金属） |
| 谱函数 $A(\vec k,\omega)$ | 极点 + $Z$ 背景 | 幂律分支割线（1D） |
| 费米体积 | $=n/2$（Luttinger） | 非整数/重构（Mott 邻域） |
| $A/\gamma^2$ | 近普适常数 | 系统性偏离 |
| 集体模 | 零声、等离激元 | 向列涨落、临界涨落 |

## 自检问题

**1.** 从 Landau–Silin 动理学方程出发推导零声：对 $l=0$ 相互作用求色散方程 $s\ln\frac{s+1}{s-1} = 2+\frac{2}{F_0^s}$，并验证 $F_0^s\gg1$ 时 $s\approx\sqrt{F_0^s/3}$、$F_0^s\to0^+$ 时 $s\to1^+$。

<details markdown="1"><summary>点击显示答案</summary>

**线性化**：$n = n_0(\varepsilon_{\vec k}^{(0)}) + u_{\vec k}e^{i(\vec q\cdot\vec r-\omega t)}$；能量随占据变化（平均场）：$\delta\varepsilon = \sum_{\vec k'}f_{\vec k\vec k'}u_{\vec k'}$。动理学方程（无碰撞）：

$$\big(\omega - \vec q\cdot\vec v_{\vec k}\big)u_{\vec k} = -\vec q\cdot\vec v_{\vec k}\,\delta(\varepsilon_{\vec k}-\mu)\,\delta\varepsilon$$

（用 $-\partial n_0/\partial\varepsilon = \delta(\varepsilon-\mu)$）。取 $\vec q$ 沿 $z$，$s\equiv\omega/(qv_F)$，$\mu_k = \cos\theta$：

$$u(\mu) = \frac{\mu}{\mu - s}\,\delta\varepsilon.$$

**自洽**：$l=0$ 时 $\delta\varepsilon = f_0\,u_0$ 与角度无关，$u_0 = N(0)\,f_0\cdot\langle u\rangle_\Omega\cdot\delta\varepsilon$ 的自洽化为 $1 = F_0^s\,\big\langle\frac{\mu}{\mu-s}\big\rangle$，其中球平均

$$\Big\langle\frac{\mu}{\mu-s}\Big\rangle = \frac12\int_{-1}^{1}\frac{\mu\,d\mu}{\mu-s} = \frac12\bigg[s\int_{-1}^{1}\frac{d\mu}{\mu-s} - 2\bigg] = \frac{s}{2}\ln\frac{s-1}{s+1} - 1.$$

（积分用 $\int d\mu/(\mu-s) = \ln\lvert\mu-s\rvert$；要求 $s>1$ 使分母无实轴零点——这正是"速度必须超过 $v_F$ 才能跑赢朗道阻尼"的来源，与第 6 章等离激元在连续区的命运同款。）代回：

$$1 = F_0^s\Big[\frac{s}{2}\ln\frac{s+1}{s-1} - 1\Big]\ \Longrightarrow\ s\ln\frac{s+1}{s-1} = 2 + \frac{2}{F_0^s}. ✓$$

**极限**：(i) $F_0^s\gg1$：右端 $\to2$；大 $s$ 展开 $\ln\frac{s+1}{s-1} = \frac{2}{s} + \frac{2}{3s^3}+\cdots$，故 $s\cdot\frac{2}{s}\big(1+\frac{1}{3s^2}\big) = 2+\frac{2}{3s^2} = 2 + \frac{2}{F_0^s}$，解得 $s = \sqrt{F_0^s/3}$ ✓。(ii) $F_0^s\to0^+$：需要 $s\ln\frac{s+1}{s-1}\to\infty$，即 $s\to1^+$（$\ln$ 发散）——极弱相互作用支起一个速度无限贴近 $v_F$ 的振荡 ✓。物理复述：这是**费米面的整体四极摆动**，位移场 $u(\mu)\propto\mu/(\mu-s)$ 在 $\mu=\pm1$（沿传播方向的前后缘）最强。

</details>

**2.** 推导磁化率公式 $\chi/\chi_0 = (m^\ast/m)/(1+F_0^a)$：对小自旋极化计算能量泛函的代价，说明 $F_0^a>0$（反铁磁型自旋通道作用）如何增强磁化率，并证明 Stoner 判据 $I\,N(0)>1$ 等价于 $F_0^a<-1$。

<details markdown="1"><summary>点击显示答案</summary>

**设置**：磁场 $B$ 使自旋上下两费米球错开化学势差 $\delta\mu$。占据数变化 $u_{\vec k\uparrow} = +\delta\mu\,\delta(\xi)$、$u_{\vec k\downarrow} = -\delta\mu\,\delta(\xi)$（$\xi = \varepsilon-\mu$；$N^\ast(0)$ 为准粒子每自旋态密度 $\propto m^\ast$）。

**能量账**（对 $\delta\mu$ 展开 $E[n]$，逐项算）：

- **动能项**：每支形如 $\tfrac12N^\ast\delta\mu^2$（把该支费米面向外压 $\delta\mu$ 的壳层代价），两支合计

$$\delta^2E_{\text{kin}} = N^\ast(0)\,\delta\mu^2.$$

- **相互作用项**：

$$\delta^2E_{\text{int}} = \frac12\sum_{\sigma\sigma'}f_{\sigma\sigma'}\sum_{\vec k\vec k'}u_{\vec k\sigma}u_{\vec k'\sigma'} = \frac12\,N^{\ast2}\delta\mu^2\big(f_{\uparrow\uparrow}+f_{\downarrow\downarrow}-2f_{\uparrow\downarrow}\big) = N^{\ast2}f^a\,\delta\mu^2,$$

其中**自旋反对称组合** $f^a\equiv f_{\uparrow\uparrow}-f_{\uparrow\downarrow}$，$F_0^a = N^\ast f^a$。符号方向：$f^a>0$（同自旋对更贵）抬升极化能量、压低 $\chi$；$f^a\lt0$（Stoner 交换：平行自旋受奖励）反之。
- **外场做的功**：$-2\mu_BB\,N^\ast\delta\mu$（两支占据各变化 $\pm N^\ast\delta\mu$，磁矩贡献同号）。

**平衡**（$\partial E/\partial\delta\mu=0$）：

$$2N^\ast\delta\mu\big(1+F_0^a\big) = 2\mu_BBN^\ast\;\Longrightarrow\;\delta\mu = \frac{\mu_BB}{1+F_0^a},$$

$$M = 2\mu_BN^\ast\delta\mu = \frac{2\mu_B^2N^\ast}{1+F_0^a}B\qquad\Longrightarrow\qquad \frac{\chi}{\chi_0} = \frac{m^\ast/m}{1+F_0^a}\qquad(\chi_0 = 2\mu_B^2N(0)). ✓$$

**Stoner 等价**：07s 的 Stoner 交换参数 $I>0$（平行自旋**降低**能量）在本篇符号下是 $f^a = -I$，即 $F_0^a = -N(0)I$。判据 $I\,N(E_F)>1 \Leftrightarrow F_0^a\lt-1 \Leftrightarrow 1+F_0^a\lt0$——分母过零、$\chi$ 发散、极化形变能量变负：**Stoner 铁磁 = Pomeranchuk 失稳在 $l=0$ 自旋道的字面实现**。两条路（能带论的 $I\,N(E_F)$ 与液体论的 $F_0^a$）是同一枚硬币：前者用巡游能带的货币、后者用费米面相互作用的货币记账，汇率 $F_0^a = -N(0)I$。³He 的 $F_0^a\approx-0.7$：增强但未过线——顺磁液体住在离铁磁一步之遥处。

</details>

**3.** 推导 Galilean 恒等式 $m^\ast/m = 1+F_1^s/3$：用"两种方式算同一个电流"的背流论证（提示：把整个液体以速度 $\vec u$ 平移，比较总能量的 Galilean 变换与准粒子描述）。

<details markdown="1"><summary>点击显示答案</summary>

**精确的靶子**：Galilean 不变的液体以速度 $\vec u$ 整体漂移时，能量严格为

$$E(\vec u) = E(0) + \tfrac12\,Nmu^2\qquad(\text{裸质量 } m\ \text{——Galilean 变换的强制结果}).$$

**准粒子账本**：漂移 = 费米面整体平移 $\delta k$，占据数变化 $\delta n_{\vec k} = -\delta k\cos\theta\,\partial n^{(0)}/\partial k_\parallel$，在费米面附近 $\partial n^{(0)}/\partial k_\parallel = -\delta(\xi)\,\hbar v_F\cos\theta$，故

$$\delta n_{\vec k} = \hbar v_F\,\delta k\,\cos^2\theta\,\delta(\xi).$$

（一阶能量 $\sum\varepsilon\,\delta n$ 因粒子数守恒为零；只算二次项。）

**动能项**：$\delta^2E_{\text{kin}} = \tfrac12\sum_{\vec k}\big(\partial^2\varepsilon/\partial k_\parallel^2\big)(\delta k_\parallel)^2$ 型的壳层积分整理为（等价地：每个 $\vec k$ 处费米面向外压 $\delta\mu_{\text{loc}} = \hbar v_F\delta k\cos\theta$ 的局部压缩代价，对球面积分）：

$$\delta^2E_{\text{kin}} = \frac{N^\ast(0)}{2}\,\hbar^2v_F^2\delta k^2\,\langle\cos^2\theta\rangle = \frac{N\hbar^2\delta k^2}{2m^\ast}.$$

（数值因子核对：$\langle\cos^2\theta\rangle = \tfrac13$，且 $N^\ast v_F^2/3N = 1/m^\ast$——由 $N^\ast/N = 3m^\ast/\hbar^2k_F^2$ 与 $v_F = \hbar k_F/m^\ast$ 即得。）

**相互作用项**：$\delta^2E_{\text{int}} = \tfrac12 N^{\ast2}\hbar^2v_F^2\delta k^2\,\langle\cos\theta\cos\theta'\,f(\chi)\rangle_{\theta\theta'}$。把 $f$ 按 Legendre 展开，加法定理给出**只有 $l=1$ 道存活**：

$$\langle\cos\theta\cos\theta'f(\chi)\rangle = \frac{f_1}{3}\ \Longrightarrow\ \delta^2E_{\text{int}} = \frac{N^\ast{}^2 f_1^s}{2}\hbar^2v_F^2\delta k^2\cdot\frac13 = \frac{N\hbar^2\delta k^2}{2m}\cdot\frac{F_1^s}{3}.$$

**匹配**：合计 $\delta^2E = \tfrac{N\hbar^2\delta k^2}{2}\big(\tfrac{1}{m^\ast} + \tfrac{F_1^s}{3m}\big)$。漂移速度与费米面平移的关系由**晶体动量的玻尔规则**锁定（与 $m^\ast$ 无关）：$\hbar\delta k = mu$。代入并要求 $\delta^2E\overset{!}{=}\tfrac12Nmu^2$：

$$\frac{m}{m^\ast} + \frac{F_1^s}{3} = 1\qquad\Longrightarrow\qquad\boxed{\ \frac{m^\ast}{m} = 1+\frac{F_1^s}{3}\ }$$

**背流的物理**：准粒子的动量必须是 $\hbar\vec k$（玻尔规则），但它跑得慢（$m^\ast$）——缺失的动量藏在**周围液体的背流**里（$l=1$ 形变正是背流的泛函面孔）。电流的两种算法——"准粒子电荷 × 准粒子速度"（带 $m^\ast$）与"总电荷 × 质心速度"（带 $m$）——必须一致，就锁出了这条恒等式。破 Galilean 的体系（晶格上的电子，第 4 章）没有此约束：$m^\ast$ 独立于 $F_1^s$，两者都是独立参数。

</details>

**4.** Pomeranchuk 判据的推导：计算费米面 $l$ 阶形变 $\delta k(\theta) = \delta k\,P_l(\cos\theta)$ 的能量至二阶，证明稳定性要求 $F_l^{s,a}>-(2l+1)$；说明 $l=0$ 电荷道为何等价于"压缩率为正"、$l=1$ 电荷道为何自动安全。

<details markdown="1"><summary>点击显示答案</summary>

**局部压缩的账法**：费米面第 $\vec{\hat k}$ 方向的一小块向外移动 $\delta k\,P_l(\mu)$，等价于该处的局部化学势抬升

$$\delta\mu_{\text{loc}}(\hat k) = \hbar v_F\,\delta k\,P_l(\mu).$$

- **动能项**：小面元的局部压缩代价 $=\tfrac12N^\ast(0)\,\langle\delta\mu_{\text{loc}}^2\rangle_\Omega$（壳层粒子数 $\propto\delta\mu_{\text{loc}}$、每个多付约 $\tfrac12\delta\mu_{\text{loc}}$）。用 $\langle P_l^2\rangle_\Omega = \tfrac{1}{2l+1}$：

$$\delta^2E_{\text{kin}} = \frac{N^\ast}{2}\,\hbar^2v_F^2\delta k^2\,\frac{1}{2l+1}\ >\ 0\qquad(\text{裸动能恒正}).$$

- **相互作用项**：$\tfrac12\sum f\,\delta n\,\delta n = \tfrac12 N^{\ast2}\,\big\langle\delta\mu_{\text{loc}}(\hat k)\,f(\chi)\,\delta\mu_{\text{loc}}(\hat k')\big\rangle$。加法定理（$P_l(\mu)P_l(\mu')$ 与 $P_l(\chi)$ 的耦合）让**只有第 $l$ 道存活**，结果与动能项同型：

$$\delta^2E_{\text{int}} = \delta^2E_{\text{kin}}\cdot\frac{F_l^{s,a}}{2l+1}.$$

**合计**：

$$\delta^2E = \delta^2E_{\text{kin}}\Big(1+\frac{F_l^{s,a}}{2l+1}\Big)\qquad\Longrightarrow\qquad \delta^2E>0\iff F_l^{s,a}>-(2l+1). ✓$$

**三个特例**：(i) $l=0$ 电荷道：均匀膨胀，判据 $F_0^s>-1$ 等价于 $\kappa>0$（第 3 节公式的分母不翻号）——热力学稳定性的液体论版本。(ii) $l=1$ 电荷道：判据 $F_1^s>-3$，而 Galilean 恒等式 $m^\ast/m = 1+F_1^s/3>0$（有效质量为正）恰好保证它**恒成立**——整体加速永不失稳，动量守恒护体 ✓。(iii) 危险户：$l=0$ 自旋（铁磁）、$l=2$ 电荷（向列）——都是"负相互作用在相应角动量道压过正动能"的同一剧本。

</details>

**5.** Oshikawa 论证：把 $N$ 个电子放进 $L\times L\times L$ 的环面，沿 $x$ 穿入一个磁通量子 $\Phi_0 = h/e$，证明"基态动量平移"的两种计数给出 $N\,\tfrac{2\pi}{L} = \tfrac{2\pi}{L}\,2V_F\,(L/2\pi)^3\cdots$ 型的关系，从而对费米液体读出 Luttinger 定理 $n = 2V_F$；说明论证在哪一步用掉了"费米液体"假设、Mott 绝缘体为何能违反它。

<details markdown="1"><summary>点击显示答案</summary>

**穿磁通的力学**：磁通 $\Phi$ 穿环等价于边界条件 twisted：$\psi(x+L) = e^{i2\pi\Phi/\Phi_0}\psi(x)$。规范变换 $\psi\to e^{i2\pi x\Phi/(L\Phi_0)}\psi$ 把相位吃进波函数，代价是每个单粒子态的晶体动量平移 $\delta k = \tfrac{2\pi}{L}\cdot\tfrac{\Phi}{\Phi_0}$。故 $\Phi:\ 0\to\Phi_0$ 的绝热过程中，多体态的**总**动量漂移

$$\Delta P = N\cdot\frac{2\pi}{L}.$$

**动量的量子化**：环面上晶体动量本征值为 $2\pi\times(\text{整数})/L$——多体动量只能跳 $2\pi/L$ 的整数倍。记基态在 $\Phi_0$ 处相对 $\Phi=0$ 获得的整数倍数为 $W$：

$$N\cdot\frac{2\pi}{L} = W\cdot\frac{2\pi}{L}\quad(\mathrm{mod}\ \tfrac{2\pi}{L}\ \text{的整数格})\qquad\Longrightarrow\qquad N - W\equiv0。$$

**$W$ 的另一本账（绝热跟随）**：假设（费米液体假设！）穿通量过程中能隙不闭、基态不简并——基态绝热演化到 $\Phi_0$ 处的基态。对非相互作用费米海，逐态跟踪给出 $W$ = 被推过布里渊区的电子数 = 费米体积的两倍（每穿过一个 $2\pi/L$ 的态计入一次）：

$$W = 2V_F\,(2\pi)^{-3}\cdot\frac{(2\pi)^3}{\cdots} = 2V_F\ \text{（按体积归一）}.$$

相互作用（费米液体）不改变绝热过程的拓扑结构（无隙闭、无简并），$W$ 作为绕数不变——故 $N = 2V_F + (\text{原胞数}\times\text{整数})$；费米液体取最平凡的分支（无奇异重排），得 $n = 2V_F$。✓

**假设用在哪**："绝热不关能隙、不遇简并"只在**每个自旋扇区有奇数电子每原胞**之类的拓扑保护情形自动成立；一般情形它是**费米液体性**的输入——正是定理的适用边界。**Mott 的违反**：电荷隙打开后，穿磁通的绝热路径可以安全地"原地踏步"（$W$ 与自由值脱钩），粒子数由整数化的局域矩/空穴承载——$n\neq2V_F$ 不再矛盾；费米体积的破缺（如某些欠掺杂铜氧化物的"小费米口袋"）因此成为 Mott 物理的实验证词（第 13 章、第 6 节的量子振荡体检）。**拓扑注记**：$W$ 是基态的绕数——与 12s 的任意子/简并一样，是"整体量对局域扰动的免疫"，费米面由此获得拓扑户口。

</details>

## 参考

- Pines & Nozières《The Theory of Quantum Liquids, Vol. I》第 1–4 章：动理学方程、零声、求和规则与 Pomeranchak 的经典陈述（本篇主线）。
- Leggett, Rev. Mod. Phys. 47, 331 (1975)（³He 中的费米液体）与《Lectures on condensed matter physics》（背流与 Galilean 恒等式的最清晰推导）。
- J. M. Luttinger, Phys. Rev. 119, 1153 (1960)：定理原始文献；Oshikawa, Phys. Rev. Lett. 84, 3370 (2000)：磁通论证；Oshikawa 的拓扑综述（2018–）。
- Kadowaki & Woods, Solid State Commun. 58, 507 (1986)：$A/\gamma^2$ 比值；Jacko et al., Nat. Phys. 5, 422 (2009)：现代重标度分析。
- Leggett《Quantum Liquids》第 5–6 章；Schofield 对 marginal FL 与奇异金属的讲义（衔接第 13 章）。
