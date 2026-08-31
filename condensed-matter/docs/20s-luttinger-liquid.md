# 补充材料：一维的无费米面世界——Luttinger 液体与玻色化

> 本书位置：凝聚态物理入门导论 第 20 章补充材料（配套正文：[DMRG 与张量网络](20-dmrg-tensor-networks.md)，下文简称"第 20 章"——那里的一维是"可算的"，本篇讲它"算出来长什么样"：没有准粒子，只有分数化的集体模）。
> 前置知识：第 3 章（费米海与费米面）、[第 6 章](06-interacting-electron-gas.md)第 7 节（费米液体：本篇要拆的正是它的地基）、[06s](06s-fermi-liquid-toolbox.md)（费米液体的体检表——本篇给出体检不及格的标本）、[第 7 章](07-magnetism.md)（Heisenberg 链与自旋波：一维的激发不是它）、[12s](12s-topological-order.md)（分数化的语言亲戚）、第 20 章（纠缠与 $c = 1$）。
> 学习目标：理解一维里费米液体**原则上不存在**（两体散射无法弛豫 + 费米面只有两个点，$2k_F$ 背散射失去曲率保护）；掌握 Luttinger 液体的低能普适结构（右手/左手费米子 + 玻色化的密度振荡，哈密顿量两个共轭场 $\phi,\theta$ 与参数 $K$）；会推电子格林函数的幂律衰减 $G\propto x^{-(K+K^{-1})/2}$ 与态密度的幂律消失——准粒子极点被分支割线取代；理解**自旋–电荷分离**（电荷模与自旋模以不同速度 $u_\rho\ne u_\sigma$ 传播，电子裂解为空穴子与自旋子）；会做 Kane–Fisher 杂质重整化群（$d\lambda/dl = (1-K)\lambda$：斥力下导线被单个杂质切成两段）与半满 Umklapp（一维 Mott 相变）；把 XXZ/Heisenberg 链认领为自旋子的 Luttinger 液体（$K$ 与各向异性的一一对应、自旋旋连谱对自旋波极点的取代）。
>
> 记号约定：沿第四部分原子单位；晶格常数 $a$。自旋指标明确写出时为自旋费米子（spinful），简化公式时用无自旋（spinless）版本并注明。$r = \pm1$ 标记右/左手。

---

## 1. 一句话总结

**一维是没有费米面的世界：费米面缩成 $\pm k_F$ 两个点，能量动量守恒把两体散射锁死成"交换或整体平移"（无弛豫），第 6 章"寿命发散快于能量"的自洽论证连同准粒子概念一起失效——任何相互作用都摧毁费米液体。接替者是 Luttinger 液体：低能自由度是费米海的密度振荡（玻色化后是一对共轭场 $\phi,\theta$），哈密顿量 $H = \frac{u}{2\pi}\int[K(\partial_x\theta)^2 + K^{-1}(\partial_x\phi)^2]$ 严格二次、参数只有速度 $u$ 与标度 $K$；电子算符是场的指数（顶点算符），格林函数按幂律衰减 $G\propto x^{-(K+K^{-1})/2}$——极点变分支割线，态密度按幂律消失；电荷与自旋解耦成两支独立声速的模（自旋–电荷分离），电子在谱上裂解为空穴子 + 自旋子——与 12s 的任意子同属"分数化"家族。一维物理由此全家改写：Heisenberg 链的激发是自旋子旋连谱而非自旋波极点，单个杂质在斥力下把导线切成两段（Kane–Fisher），半满的任意排斥都打开 Mott 隙（Umklapp 相关算符）；而这一切正好是 DMRG 的主场——第 20 章算的临界链（$c=1$）就是本章的 Luttinger 液体。**

## 2. 为什么一维没有费米液体

第 6 章 §7 的相空间论证在三维靠"球面有曲率"撑腰；一维把它拆掉：

**两体散射不弛豫**（完整证明见自检问题 1）：一维弹性碰撞中能量与动量守恒联立，末态动量只能是 $(p_1,p_2)$ 或 $(p_2,p_1)$——粒子只是互换标签（玻色视角）或穿过（费米视角），分布函数**不变**。弛豫只能靠三体以上过程，而费米面附近的相空间让它们更弱。于是准粒子的"$1/\tau\to0$ 快于 $\xi\to0$"失去了机理来源——**不是寿命不够长，是没有可散射的方向**。

**费米面没有软方向**：三维费米面的形变有无数"切向"自由度（第 6 章 §8 的 RG 把大多数通道洗成 irrelevant）；一维费米面只有 $\pm k_F$ 两点，连接两点与点的算符——背散射（$2k_F$：$\psi^\dagger_R\psi_L$）——**没有任何曲率去抑制它**，在 RG 下保持边缘（marginal）甚至相关。Shankar 式的"费米面普适不动点"在一维坍塌。

结论：一维金属的低能理论**必须**重新搭。答案是：不要费米子，要密度。

## 3. 玻色化：把费米海翻译成玻色场

**线性化与左右手**：费米面附近色散线性化 $\varepsilon_{\pm k_F+q}\approx \pm v_Fq$，低能希尔伯特空间 = 右手 $\psi_R$ + 左手 $\psi_L$ 的费米子（第 3 章费米海的 1D 版）。关键观察（1950 年代 Tomonaga–Luttinger 的起点）：这个空间里**唯一**的玻色型集体激发是密度振荡，而它的代数恰好封闭——

$$\rho(x) = \rho_0 - \frac{1}{\pi}\partial_x\varphi + \big[\rho_{2k_F}(x) + \text{h.c.}\big],\qquad \rho_{2k_F} \propto \psi_L^\dagger\psi_R \propto e^{2i\phi(x)}.$$

引入共轭场 $\phi$（密度相位）与 $\theta$（共轭动量，$[\phi(x),\partial_{x'}\theta(x')] = i\pi\delta(x-x')$），相互作用的低能拉格朗日**精确地**化为两个自由玻色场（Haldane 的普适形式）：

$$H = \frac{u}{2\pi}\int\text dx\ \Big[K\,(\partial_x\theta)^2 + \frac{1}{K}(\partial_x\phi)^2\Big],\qquad \rho(x) = -\frac{1}{\pi}\partial_x\phi\ (+\ 2k_F\ \text{振荡部分})，$$

两个参数：速度 $u$ 与**标度维数** $K$（自由无自旋费米子：$K=1$、$u=v_F$；短程斥力使 $K\lt1$，引力使 $K\gt1$；自旋费米子拆成电荷与自旋两套，各有 $u_{\rho,\sigma}$ 与 $K_\rho$——SU(2) 对称把自旋扇区锁死 $K_\sigma=1$）。电子算符变成**顶点算符**：

$$\psi_r(x)\ \propto\ e^{-i(r\phi(x)-\theta(x))}\qquad(r=\pm1)，$$

指数里的半整数系数由对易代数硬性决定（自检问题 2 对自由情形逐项验证这本"词典"）。

**这句话的含义要掂量**：玻色化不是近似，是**精确对偶**——一维的费米自由度与玻色自由度在低能扇区互为镜像。原因深植于费米海的几何：1D 费米海的激发只有"在 $\pm k_F$ 附近注入/移出粒子"，这恰好一一对应于密度波的量子——**海面上除了波浪没有别的东西**（三维则不然：粒子–空穴激发有横向动量自由度，玻色化不完备）。

## 4. 没有准粒子的谱：幂律与分支割线

把顶点算符的关联函数在自由玻色（高斯）理论里算出来（自检问题 3 的标准手艺：$\langle e^{i\alpha\phi(x)}e^{-i\alpha\phi(0)}\rangle\propto x^{-\alpha^2K/2}$ 型）：

**电子格林函数**（无自旋体材料）：

$$G(x) = \langle\psi(x)\psi^\dagger(0)\rangle\ \propto\ \frac{1}{x^{(K+K^{-1})/2}}；\qquad\text{边界处（开链端点）指数换为 } \frac{1}{K}\ (\text{更强的幂律}).$$

自由点 $K=1$ 回到 $G\propto1/x$ ✓。**没有极点**：傅里叶到 $(k,\omega)$，格林函数是**分支割线**而非极点——准粒子的谱权重不是 $Z$ 的尖峰，而是按幂律摊开：

$$\text{局域态密度}\qquad N(\omega)\ \propto\ \lvert\omega\rvert^{(K+K^{-1}-2)/2}\qquad(\text{边界}:\ \lvert\omega\rvert^{K^{-1}-1})，$$

**低温下按幂律趋零**——隧道实验进入一维导线的电导被压低（"隧穿隙"），是与费米液体 $N(E_F)$ 常数值对决的判据（扫描隧道实验在金属性碳纳米管、原子链上看到幂律抑制，指数符合 Luttinger 标度）。

**密度关联**：

$$\langle\rho(x)\rho(0)\rangle\ =\ -\frac{K}{2\pi^2x^2}\ +\ A\,\frac{\cos 2k_Fx}{\lvert x\rvert^{2K}}\ +\ \cdots$$

第一项是自由费米海就有的（$K$ 修正其幅度），第二项是 $2k_F$ 振荡——**指数 $2K$ 可被相互作用连续调节**（费米液体里它是固定的"2 + 对数修正"）。这是"标度维数被相互作用重整"的活标本：1D 里不存在普适指数，$K$ 是新的低能参数（对应 06s 的 $F_l$——每个维度有自己的一套"少胜多"）。

## 5. 自旋–电荷分离：电子裂解

自旋费米子的 Luttinger 液体拆成**两支独立的玻色模**：

$$H = H_\rho[\phi_\rho,\theta_\rho;\ u_\rho,\ K_\rho] + H_\sigma[\phi_\sigma,\theta_\sigma;\ u_\sigma,\ K_\sigma]，\qquad u_\rho \ne u_\sigma\ (\text{只要相互作用非零：电荷扇区被重整，自旋扇区被 SU(2) 锁死}).$$

电子算符同时携带两个标签（$\psi \sim e^{-i(\cdots\phi_\rho\cdots)}\times e^{-i(\cdots\phi_\sigma\cdots)}$），它的格林函数是两支模关联函数的**乘积**——谱函数的支持区域是两条"翅膀"：注入一个电子，其电荷成分以 $u_\rho$ 跑掉、自旋成分以 $u_\sigma$ 跑掉，**永远不再合体**（自检问题 4 把两翼结构算清楚）。空穴子（holon，电荷无自旋）与自旋子（spinon，自旋无电荷）由此获得谱学身份。

**Hubbard 链的账单**（Bethe ansatz 给出全程精确、弱耦合玻色化给出普适形式）：半满 Hubbard 链 $U\to\infty$ 极限

$$u_\rho = 2t,\qquad u_\sigma = \frac{2\pi t^2}{U}\qquad\bigg(K_\rho\to\frac12\bigg)，$$

电荷近乎自由飞奔（空穴互避不耗 $U$），自旋靠 $J = 4t^2/U$ 的超交换缓行（第 13 章 5 节的公式在 1D 开出精确的速度）——**分离可以达到数量级**。自旋子的实验脸：一维自旋链的中子散射看到**旋连谱**（连续分布的强度）而非自旋波极点——Heisenberg 链的 $S=1$ 磁振子（第 7 章的高维图像）裂解为两个 $S=1/2$ 自旋子，$\mathrm{KCuF_3}$ 等材料的中子数据与双自旋子旋连的计算精确吻合。

## 6. 杂质与 Mott：一维的脆弱性

**Kane–Fisher（1992）**：在无自旋 Luttinger 导线里放一个弱杂质（背散射振幅 $\lambda$）。它的 RG 方程：

$$\frac{d\lambda}{dl} = (1-K)\lambda$$

——**斥力（$K\lt1$）下杂质是相关算符**，弱杂质在粗粒化下指数增强：低温导线被切成两段，电导趋于零。反过来看：强杂质（两段导线）的透射是无关扰动——**一维金属被一个原子级的缺陷杀死**，与三维金属对杂质的从容（第 3 章 Drude 的 $\tau$ 顺滑吸收）形成惨烈对照。 $K\gt1$（吸引）时杂质被冲刷干净、导线自愈。物理根源仍在 $2k_F$ 关联的增强（$\cos2k_F$ 关联按 $x^{-2K}$ 慢衰减，长程"回忆"帮助背散射相干叠加）。

**Umklapp 与一维 Mott**：半满时 $4k_F = 2\pi/a$，两个右手费米子背对着撞进晶格倒格矢——玻色语言里这是 $\cos4\phi$ 型项，标度维数 $4K$（自旋情形 $\sqrt8\phi_\rho$，维数 $2K_\rho$）。**相关判据**：

$$\text{无自旋}：K\lt\tfrac12\quad(\text{BKT 型相变})；\qquad\text{自旋}：K_\rho\lt1\ (\text{即任何斥力})\ \Longrightarrow\ \text{半满一维 Hubbard 是 Mott 绝缘体}.$$

第 13 章"半满大 $U$ 出 Mott 隙"的图像在 1D 加码成"**任意** $U>0$ 即绝缘"（隙 $\Delta\propto e^{-2\pi t/U} = e^{-\pi v_F/U}$，半满 $v_F = 2t$；弱耦合指数小）——一维是 Mott 物理的放大镜，也是第 20 章 DMRG 校准的首选标本（Hubbard 链的隙、$K$、自旋–电荷速度全部可从基态数值提取）。

## 7. 与全书的接口

- **第 6 章/06s**：费米液体的三件信物在一维逐一失效（寿命论证坍塌、谱函数无极点、Luttinger 定理只剩"广义"版本——费米体积意义上的 $k_F$ 还在，准粒子没了）。
- **第 7 章**：Heisenberg 链的激发不是自旋波（那是高维/铁磁的语言），是自旋子对的旋连谱——一维磁性的正确语言在本篇。
- **第 13 章**：一维 Mott（任意 $U$）、超交换速度 $u_\sigma = \pi J/2a$ 的精确兑现、RVB/分数化思想的 1D 严格实例。
- **12s**：自旋子/空穴子与任意子同属分数化——一维是"拓扑荷分数化"的最低维现场（差别：一维分数化不需要拓扑序，只要玻色化的乘积结构）。
- **第 20 章**：临界链 $c=1$、$\chi\propto L^{c/3}$ 的纠缠账——Luttinger 液体就是 $c=1$ 的 CFT；DMRG 提取 $K$（从 $\langle\rho\rho\rangle$ 的 $2k_F$ 指数）与 $u$ 是现代标准操作。
- **第 10 章（待写）**：Landauer 电导在一维的修正是 $G = Ke^2/h$（无自旋；接到费米液体导线后两端测量另有 $e^2/h$ 的精妙）——量子输运的一维开门题。

## 小结

| | 费米液体（3D） | Luttinger 液体（1D） |
|---|---|---|
| 低能载体 | 准粒子（极点，权重 $Z$） | 集体玻色模（分支割线） |
| 两体散射 | 相空间指数压低 | 能量动量守恒禁止弛豫 |
| 电子格林函数 | $G\approx Z/(\omega-v^\ast k+i/2\tau)$ | $G\propto x^{-(K+K^{-1})/2}$ 幂律 |
| 局域态密度 | $N(E_F)$ 有限 | $N(\omega)\propto\lvert\omega\rvert^{(K+K^{-1}-2)/2}$ 归零 |
| 关联指数 | 普适（+对数修正） | 由 $K$ 连续调节 |
| 自旋/电荷 | 同一准粒子携带 | 分离：$u_\rho\ne u_\sigma$，空穴子 + 自旋子 |
| 杂质 | 弱效应（$\tau$ 吸收） | 斥力下导线被切断（Kane–Fisher） |
| 半满排斥 | 金属（除非 $U$ 大开隙） | 任意 $U>0$ 皆 Mott |

- 玻色化是精确对偶：$\psi\propto e^{-i(r\phi-\theta)}$，相互作用全部收进 $(u, K)$。
- 幂律与 $K$：$G\propto x^{-(K+K^{-1})/2}$、$N(\omega)$ 幂律归零、$2k_F$ 关联 $\propto x^{-2K}$。
- 自旋–电荷分离是分数化：Hubbard 链 $u_\rho = 2t$、$u_\sigma = 2\pi t^2/U$（$U\to\infty$）。
- Heisenberg 链 = 自旋子的 Luttinger 液体（$K=\tfrac12$）；自旋波极点 → 自旋子旋连谱。
- Kane–Fisher 与 Umklapp：一维金属的两重脆弱性。

## 自检问题

**1.** 证明一维弹性两体散射不改变单粒子分布：由能量与动量守恒推出末态动量只能是初态的置换；对比三维费米面附近的相空间计数（第 6 章 §7.2），说明为什么费米液体的寿命论证在一维坍塌。

<details markdown="1"><summary>点击显示答案</summary>

**一维**：两个动量 $p_1\ne p_2$ 的粒子弹性碰撞（交换不变振幅），末态 $(p_3,p_4)$ 满足

$$p_1+p_2 = p_3+p_4,\qquad \varepsilon(p_1)+\varepsilon(p_2) = \varepsilon(p_3)+\varepsilon(p_4).$$

第二个方程改写：$\varepsilon(p_1)-\varepsilon(p_3) = \varepsilon(p_4)-\varepsilon(p_2)$。利用第一个方程把 $p_4 = p_1+p_2-p_3$ 代入：$\varepsilon(p_1)+\varepsilon(p_2) = \varepsilon(p_3)+\varepsilon(p_1+p_2-p_3)$。对 $p_3$ 微分找极值：$\varepsilon'(p_3) = \varepsilon'(p_1+p_2-p_3)$——由于 $\varepsilon'$ 单调（凸色散），解只有 $p_3 = p_1+p_2-p_3$ 型的边界解或 $p_3 = p_1$ / $p_3 = p_2$：

$$(p_3,p_4) = (p_1,p_2)\ \text{或}\ (p_2,p_1).$$

**分布函数的后果**：占据数 $n(p)$ 在 $(p_1,p_2)\to(p_2,p_1)$ 下不变（玻色子直接置换；费米子按直通图像解释）。碰撞积分 $\partial n/\partial t\vert_{\text{coll}}$ 严格为零——**分布函数是碰撞不动点**，任何非平衡分布都不弛豫。

**对比三维**：$\varepsilon'$ 是矢量（群速度），守恒只约束其两个分量，末态仍有连续单参数族（碰撞改变 $p$ 的**方向**）——第 6 章 §7.2 的窗口计数 $\int d\xi_2d\xi_3\propto\xi_1^2$ 全靠这些"侧向"自由度。一维把窗口数到零：**不是 $1/\tau$ 太长，是可数的弛豫通道不存在**——准粒子"寿命"的提法在一维失去对象，费米液体的第一块地基（准粒子是好的激发）直接抽走。

</details>

**2.** 验证玻色化词典（自由无自旋情形，$K=1$、$u=v_F$）：由高斯关联 $\langle\phi(x)\phi(0)\rangle = -\tfrac{1}{2}\ln(x/a)$、$\langle\theta(x)\theta(0)\rangle = -\tfrac{1}{2}\ln(x/a)$ 证明 (a) $\psi_r(x)\propto e^{-i(r\phi-\theta)}$ 的关联 $\langle\psi_R(x)\psi_R^\dagger(0)\rangle\propto 1/x$——正是自由费米子；(b) 密度 $\rho = -\tfrac{1}{\pi}\partial_x\phi + \rho_{2k_F}$ 的均匀部分给出 $\langle\rho\rho\rangle\propto -1/x^2$；(c) 反对易关系由顶点算符的对数相位差保证（Klein 因子的角色一句话）。

<details markdown="1"><summary>点击显示答案</summary>

**(a)**：高斯理论里顶点算符关联是初等指数（Wick 定理对指数直接生效）。记 $A = \phi - \theta$：

$$\langle e^{-iA(x)}\,e^{iA(0)}\rangle = e^{-\frac12\big\langle\big(A(x) - A(0)\big)^2\big\rangle}.$$

等时情形 $\langle\phi(x)\theta(0)\rangle = \tfrac{i\pi}{2}\,\mathrm{sgn}(x)$ 型的交叉项是**常数相位**（不含 $x$ 依赖，它只负责第 (c) 问的反对易号），$A$ 的自关联由 $\phi$ 与 $\theta$ 两个场各贡献 $-\tfrac12\ln(x/a)$ **相加**：

$$\big\langle A(x)A(0)\big\rangle = -\ln(x/a)\ \Longrightarrow\ \big\langle\big(A(x)-A(0)\big)^2\big\rangle = 2\big\langle A^2(0)\big\rangle - 2\big\langle A(x)A(0)\big\rangle = 2\ln(x/a) + \text{常数}.$$

常数部分只影响归一化，于是

$$\langle\psi_R(x)\psi_R^\dagger(0)\rangle\propto e^{-\frac12\cdot 2\ln(x/a)} = e^{-\ln(x/a)} = \frac{a}{x}\ \propto\ \frac{1}{x},$$

恰是自由费米子 $G(x) \sim \sin(k_Fx)/\pi x$ 的包络（$k_F$ 振荡由左右手标签 $r = \pm1$ 携带）✓。

**(b)**：$\partial_x\phi$ 的关联由 $\langle\phi\phi\rangle$ 求两次导：$\langle\partial_x\phi(x)\partial_{x'}\phi(x')\rangle = -\tfrac12\big/(x-x')^2$（对 $-\tfrac12\ln\lvert x-x'\rvert$ 先对 $x$ 再对 $x'$ 求导，两次链式法则各带一个符号），故

$$\langle\rho(x)\rho(0)\rangle_{\text{均匀}} = \frac{1}{\pi^2}\cdot\Big(-\frac{1}{2x^2}\Big) = -\frac{1}{2\pi^2x^2}\qquad(K=1\ \text{时自由值}).$$

——自由费米海的 $\langle\rho\rho\rangle$ 精确复现 ✓（负号是费米压强：密度涨落反关联）。

**(c)**：两个顶点算符的乘积携带相位 $e^{-i\pi r\cdots}$：把 $\langle\phi\theta\rangle$ 的常数相位差算进 $e^{i(\phi-\theta)(x)}e^{i(\phi-\theta)(0)}$ 的重排，右手与左手场交换时多出 $e^{i\pi}$——反对易自动出现。不同支（$R$ 与 $L$）之间的反对易则由 **Klein 因子**（全局马约拉纳型常算符）补齐——它们保证 $\{\psi_R,\psi_L\} = 0$，是词典的"语法补丁"（细节不影响关联函数的指数，本篇不展开）。

</details>

**3.** 幂律指数的来源：在高斯理论里证明 $\langle e^{i\alpha\phi(x)}e^{-i\alpha\phi(0)}\rangle\propto\lvert x\rvert^{-\alpha^2K/2}$（相互作用后的 $\langle\phi\phi\rangle = -\tfrac{K}{2}\ln\lvert x\rvert$）；用它导出 (a) 电子格林函数 $G\propto\lvert x\rvert^{-(K+K^{-1})/2}$；(b) $2k_F$ 密度关联 $\langle\rho_{2k_F}(x)\rho_{2k_F}^\dagger(0)\rangle\propto\cos(2k_Fx)/\lvert x\rvert^{2K}$；(c) 局域态密度 $N(\omega)\propto\lvert\omega\rvert^{(K+K^{-1}-2)/2}$。

<details markdown="1"><summary>点击显示答案</summary>

**通用公式**：$\psi\propto e^{-i(r\phi-\theta)}$ 中 $\phi$ 与 $\theta$ 的关联分别带 $K$ 与 $K^{-1}$：

$$\langle\phi(x)\phi(0)\rangle = -\frac{K}{2}\ln\lvert x\rvert,\qquad \langle\theta(x)\theta(0)\rangle = -\frac{1}{2K}\ln\lvert x\rvert，$$

（$K\to1$ 回到自检问题 2）。顶点关联 = 指数化：$\langle e^{i\alpha\phi(x)}e^{-i\alpha\phi(0)}\rangle = e^{\alpha^2\langle\phi(x)\phi(0)\rangle/2}\cdots = \lvert x\rvert^{-\alpha^2K/2}$ ✓（对 $\theta$ 同理带 $K^{-1}$）。

**(a)** 电子 = $\phi$ 与 $\theta$ 的乘积顶点，两个场的贡献相加：

$$G(x)\propto\lvert x\rvert^{-\frac12(K + K^{-1})}\qquad\text{（体材料）}.$$

$K=1$ 检验：$x^{-1}$ ✓。边界情形只有一个独立场组合存活，指数换为 $K^{-1}$（正文第 4 节）。

**(b)** $\rho_{2k_F}\propto e^{2i\phi} + \text{c.c.}$（$\alpha = 2$）：

$$\langle\rho_{2k_F}(x)\rho_{2k_F}^\dagger(0)\rangle\propto\lvert x\rvert^{-2K}，$$

乘上 $\cos2k_Fx$ 的振荡 ✓——**指数由 $K$ 连续调节**：强斥力（$K\ll1$）下 $2k_F$ 关联衰减极慢，电荷序的长程倾向被放大（与第 6 章 Peierls/CDW 的 $2k_F$ 物理同源；一维在任意排斥下 $2k_F$ 响应发散——Peierls 不稳定性，本篇未展开的支线）。

**(c)** $N(\omega) = -\tfrac1\pi\mathrm{Im}\,G^R(\omega)|_{x=0}$：对 $G(x)\propto x^{-\eta}$（$\eta = \tfrac12(K+K^{-1})$）做傅里叶/Abel 变换到时间域再取边界值，标准幂律变换给

$$N(\omega)\ \propto\ \lvert\omega\rvert^{\eta-1} = \lvert\omega\rvert^{\frac{K+K^{-1}}{2}-1}\qquad\text{（体材料；边界换成 }K^{-1}-1\text{）}，$$

$K=1$ 检验：指数为零，$N$ = 常数——回到费米液体 ✓。任何 $K\ne1$ 都给出**幂律归零**的态密度：准粒子概念在谱上的墓碑。

</details>

**4.** 自旋–电荷分离的谱学：把自旋费米子的格林函数写成 $G = G_\rho\times G_\sigma$（两支模关联的乘积，速度 $u_\rho\ne u_\sigma$），证明动量空间里谱函数的支持区分裂为两条"翅膀"（在 $\omega = u_\rho q$ 与 $\omega = u_\sigma q$ 附近各自的幂律奇性），并说明为什么光电子能谱看到的是双分支割线而非单极点；给 Hubbard 链 $U\to\infty$ 的 $u_\rho/u_\sigma$ 数字对比。

<details markdown="1"><summary>点击显示答案</summary>

**结构**：自旋费米子 $\psi_\sigma \propto e^{i(\pm\phi_\rho-\theta_\rho)}\times e^{i(\pm\phi_\sigma-\theta_\sigma)}$——两个**独立**高斯场的顶点之积。时空关联：

$$G(x,t) = G_\rho(x,t)\cdot G_\sigma(x,t)\ \propto\ \prod_{\nu=\rho,\sigma}\Big[u_\nu^2t^2-x^2\Big]^{-\eta_\nu/2}\cdot(\text{阈值因子})，$$

每支模的关联在光锥 $x = \pm u_\nu t$ 上有幂律奇性。傅里叶到 $(q,\omega)$（$q$ 相对 $k_F$）：乘积的傅里叶是卷积——谱权重分布在两支光锥投出的区域，**幂律密度的峰**分别在 $\omega\approx u_\rho q$ 与 $\omega\approx u_\sigma q$：

$$A(q,\omega)\ \text{在}\ \omega = u_\rho q\ \text{与}\ \omega = u_\sigma q\ \text{各有一条分支割线型奇性}.$$

**谱学含义**：注入的电子（ARPES）按两支速度分离——在 $\omega\approx u_\rho q$ 处看到的是"电荷先到"，其谱函数幂律尾一路延伸到自旋翼；**没有共同的极点**意味着没有"完整电子"的准粒子峰。实验在解链的 1D 化合物（如蓝青铜、1D 铜氧化物周边的表面链体系）与光电子能谱的分支结构比较——双速分离是 Luttinger 液体的第二判据（第一是幂律态密度）。

**数字**：半满 Hubbard、$U\to\infty$：

$$u_\rho = 2t\ (\text{电荷自由奔跑})，\qquad u_\sigma = \frac{2\pi t^2}{U}\ (\text{自旋靠 }J = 4t^2/U\text{ 缓行})，$$

比值 $u_\rho/u_\sigma = U/\pi t$——大 $U$ 时两个"翅膀"相距数量级，分离在谱上肉眼可辨（Bethe ansatz 的精确结果与玻色化的普适形式在此重合）。

</details>

**5.** Kane–Fisher 与 Umklapp 的 RG：从 $2k_F$ 密度算符的标度维数出发，推导杂质背散射的 $d\lambda/dl = (1-K)\lambda$ 与半满 Umklapp $\cos4\phi$ 的相关性判据 $K\lt\tfrac12$（无自旋）；说明两条结论合起来刻画了"一维金属的两重脆弱性"。

<details markdown="1"><summary>点击显示答案</summary>

**标度维数表**（高斯理论，无自旋）：$\rho_{2k_F}\propto e^{2i\phi}$ 的维数 $= K$（自检问题 3 的关联指数 $2K$ 对应维数 $K$）；$e^{i4\phi}$（双倍）维数 $= 4K$。

**杂质**：弱杂质产生的背散射项 $H_{\text{imp}} = \lambda\,\delta(x)\big[\rho_{2k_F} + \text{c.c.}\big]$——作用在一点上的 $\rho_{2k_F}$ 算符。耦合 $\lambda$ 在标度变换下的流由算符维数决定（作用量无量纲计数：$d\lambda/dl = (1-\Delta)\lambda$，$\Delta$ 为开边界处 $e^{2i\phi}$ 的维数，等于 $K$ 的边界值）：

$$\frac{d\lambda}{dl} = (1-K)\lambda\qquad\Longrightarrow\ K\lt1\ \text{相关（增强）},\ K\gt1\ \text{无关（冲刷）}.$$

**物理结论**：任何斥力导线，$T\to0$ 时弱杂质指数长大为强杂质——导线切成两段（中间形成电荷蓄积区，$G\to0$）；反之路端费米液体接触测到的"表观 $e^2/h$"是接触阻抗效应（第 10 章的接口）。

**Umklapp**：半满时晶格提供 $2\pi/a = 4k_F$ 的倒格矢，允许两右两左的集体转移，玻色形式 $g_u\cos4\phi$。体积算符相关性判据：维数 $4K\lt2$（耦合维数为负即增强）：

$$K\lt\frac12\quad\Longleftrightarrow\quad g_u\ \text{相关}\ \Longrightarrow\ \phi\ \text{被钉扎到 }\cos4\phi\text{ 的极小、电荷隙打开（BKT 型）。}$$

自旋情形：$\cos\sqrt8\,\phi_\rho$ 维数 $2K_\rho$，判据 $K_\rho\lt1$——**任何**斥力即满足，半满自旋 Hubbard 链对任意 $U>0$ 都是 Mott 绝缘体（隙 $\Delta\propto e^{-2\pi t/U} = e^{-\pi v_F/U}$，半满 $v_F = 2t$；弱耦合指数小）。$K=\tfrac12$ 处的无自旋 BKT 点对应 XXZ 链 $\Delta = 1$（Heisenberg）——XXZ 的各向异性与 $K$ 有 Bethe ansatz 的精确映射

$$K = \frac{\pi}{2(\pi - \arccos\Delta)}\qquad(\Delta = 1\to\tfrac12;\ \Delta = 0\to1)，$$

磁学与玻色化在此合流。

**两重脆弱性**：一个原子缺陷杀导线（Kane–Fisher）、一个晶格常数杀金属（Umklapp/Mott）——根源同源：**$2k_F$ 背散射没有曲率可怕**（第 2 节），一维的"金属"是最不设防的金属相。

</details>

## 参考

- T. Giamarchi《Quantum Physics in One Dimension》(2004)：Luttinger 液体的标准教科书（本篇第 3–6 节主线；g-ology、Kane–Fisher、Umklapp 的完整版）。
- F. D. M. Haldane, J. Phys. C 14, 2585 (1981)：'Luttinger liquid' 术语与普适形式的出处。
- C. L. Kane & M. P. A. Fisher, Phys. Rev. Lett. 68, 1220 (1992)：杂质 RG 原始文献。
- J. Voit, Rep. Prog. Phys. 57, 977 (1995)：一维电子体系的综述讲义（玻色化的最清晰教学版之一）。
- A. O. Gogolin, A. A. Nersesyan & A. M. Tsvelik《Bosonization and Strongly Correlated Systems》：技术版全文。
- C. Kim 等（Nat. Phys. 2006 附近）与蓝青铜/1D 铜氧的 ARPES 工作：幂律态密度与双分支谱的实验面。
