# 零锥正则引力与黑洞熵：论文的伴读

> 路线图位置：第 9 阶段（代数量子引力专题）· 第 4 篇（收官）
> 前置知识：广义相对论书[第 5s 章](../../../general-relativity/docs/05s-first-order-gravity.md)（一阶引力）、[第 7 章](../../../general-relativity/docs/07-causal-structure.md)（因果结构）、[第 8 章](../../../general-relativity/docs/08-null-hypersurface-geometry.md)（零超曲面）、[第 10 章](../../../general-relativity/docs/10-boundary-terms-action.md)（带边界作用量）、[第 12 章](../../../general-relativity/docs/12-covariant-phase-space.md)（协变相空间）已写完，第 11 章（ADM）待写；理论力学书第 9、10、12 章；第 9 阶段 01–03 篇。论文的整体读法见[论文阅读专栏首篇](../../../paper-reading/docs/01-null-cone-quantum-gravity.md)。
> 学习目标：复述"一阶引力 → 零初始数据 → 约化相空间 → 量子化 → 时钟投影 → 有限维 → 熵"的完整链条；能写出含边缘模的辛形式并认出 boost 荷 $K = A/8\pi G$；能推出时钟读数对面积的界；能复现熵的对数修正系数 $106/45$；知道半经典极限如何从微分同胚不变性出来。

---

**单位约定**：本篇取自然单位 $\hbar = c = 1$（首次说明）；度规号差沿用本书 $(+,-,-,-)$。括号中的编号（如 (3.42)）是论文 arXiv:2611.34924 的公式号，方便对照原文。

## 1. 一句话总结

**这篇论文把四维真空引力当成约束系统，在"两片相交零锥围成的因果菱形"上完成非微扰量子化：一阶引力（Plebański）在零锥上解掉全部约束，剩下的自由数据是各截面的共形度规（两个引力子偏振）与角点边缘模；先定义可观测量代数，再选纯高斯态经 GNS 得到 $I$ 型因子；"引力时钟"的上限同时限制角点面积，从而证明有界菱形的 Hilbert 空间有限维；迹给出 $\rho\propto e^{-A/4G}$ 与 $S = \langle A\rangle/4G + \ln Z$，对数修正系数 $106/45$ 与 Sen 的欧氏结果一致；半经典极限给出一圈阶的 Einstein 方程。**

## 2. 一阶引力与零锥边界

### 2.1 Plebański 作用量

把标架 $e^\mu{}_a$、自旋联络 $\omega^{\mu\nu}{}_a$ 与二形式 $B^{\mu\nu}$ 独立变分：

$$I[B,\omega,\Phi] = \frac{1}{16\pi G}\int_M\left[B_{\mu\nu}\wedge F^{\mu\nu} - \frac12\Phi_{\mu\nu\rho\sigma}B^{\mu\nu}\wedge B^{\rho\sigma}\right] + I_{\partial M},$$

$F^{\mu\nu} = 2\nabla_{[a}\omega_{b]}{}^{\mu\nu} + 2\omega_{[a}{}^{\mu}{}_\rho\,\omega_{b]}{}^{\rho\nu}$ 是曲率二形式，$\Phi_{\mu\nu\rho\sigma}$ 是拉格朗日乘子（与 $B\wedge B$ 全缩并给出宇宙学常数）。

- 变分 $\Phi$（无迹部分）给出**简单性约束** $S_{\mu\nu\rho\sigma} = 0$，其解为
  $$B^{\mu\nu} = \frac12\epsilon^{\mu\nu}{}_{\rho\sigma}\,e^\rho\wedge e^\sigma;$$
- 变分 $\omega$ 给出 $\nabla_{[a}B^{\mu\nu}{}_{bc]} = 0$，配合上式即**挠率为零**，$\omega = \omega(e)$；
- 变分 $B$ 给出 $F^{\mu\nu} = \Phi^{\mu\nu}{}_{\rho\sigma}B^{\rho\sigma}$，取迹部分（$\epsilon^{\mu\nu\rho\sigma}\Phi_{\mu\nu\rho\sigma} = 4\Lambda$）后即 Einstein 方程。

一句话：**简单性约束把拓扑的 BF 理论变成广义相对论，且它不含导数，不产生新的边界项**——这是论文选择一阶形式的理由。

### 2.2 边界项

区域 $M$ 的边界由两片零锥 $H_p,H_q$ 与两个小盖 $\Sigma_0,\Sigma_1$ 组成。边界作用量（3.15a）包含三类项：

$$I_{\partial M}\supset\frac{1}{8\pi G}\left[\int_{\Sigma_i}\epsilon_\Sigma K_i + \int_{H_s}\eta_s\,\kappa_s + \int_S\mu\log\left(-\ell_p\cdot\ell_q/2\right)\right],$$

分别是 GHY 项（盖的外曲率）、零边界项（inaffinity $\kappa_s$）与**角点项**（两个零法向的内积的对数）。角点项不是装饰：它保证变分原理良定，并在粘合时给出 boost 荷（§3.3）。

### 2.3 辛势

边界变分定义辛势 $\theta = \frac{1}{16\pi G}B_{\mu\nu}\wedge\delta\omega^{\mu\nu}$（3.34），加上恰当的改进项后，在零边界上化为（3.39）

$$\Theta_H = \frac{1}{16\pi G}\int_H\eta\left[\sigma^{AB}\delta q_{AB} - \left(2\kappa + \Theta_{(\ell)}\right)\delta\log\varrho^2\right],$$

**剪切 $\sigma^{AB}$ 与共形度规共轭、膨胀与面积共轭**——这就是"引力子的两个偏振住在零锥上"的相空间表述。

## 3. 零初始数据与约化相空间

### 3.1 自由数据

在入射零锥 $H_p$ 上，可以自由指定：

- 各截面的**共形度规** $\bar q_{AB}$（单位行列式，两个偏振）；
- 角点 $S$ 上的**面积密度** $\varrho_S(y)$、**相对 boost 角** $\gamma$ 与**角度嵌入** $Y^A$（边缘模）。

其余量（膨胀、面积随仿射参数的变化）由约束决定。

### 3.2 Raychaudhuri 方程决定面积，面积决定时钟

剪切使相邻零生成元汇聚。Raychaudhuri 方程（3.25f）为

$$\frac{\mathrm{d}^2\varrho}{\mathrm{d}u^2} + \frac{\varrho}{8}\left(\partial_u\bar q\right)^{AB}\left(\partial_u\bar q\right)_{AB} = 0.$$

以 $v = \varrho/\varrho_S$ 为坐标（$v$ 从盖上的 $\epsilon$ 到角点的 $1$），令 $N = \partial_u\varrho$，可化为

$$\frac{\partial_v N}{N} = -\frac{v}{8}\left(\partial_v\bar q\right)^{AB}\left(\partial_v\bar q\right)_{AB} \;\Longrightarrow\; \partial_u\varrho = p_{\epsilon,y}\,e^{-\Xi_y(v)},\qquad \Xi_y(v) = \frac18\int_\epsilon^v s\left(\partial_s\bar q\right)^2\mathrm{d}s.$$

（自检 1 给出完整推导。）由于 $\Xi \ge 0$，**剪切使达到同一面积所需的仿射参数变长**。时钟定义为

$$u_*(y) = p_{\epsilon,y}\left[u(1,y) - u(\epsilon,y)\right] = \varrho_S(y)\int_\epsilon^1 e^{\Xi_y(v)}\,\mathrm{d}v,$$

它与零生成元的重新参数化无关，只依赖共形度规与面积。**这是全篇的物理核心：时钟读数 $\ge$ 无剪切时的读数，剪切越大时钟越慢。**

### 3.3 辛形式与 boost 荷

在固定角点、令 $K(y) = \varrho_S(y)^2/(8\pi G)$（角点面积密度除以 $8\pi G$），辛形式（3.42b）为

$$\Omega = \int_S\epsilon_0\left[K(y)\,\delta\alpha + K(y)\,\delta\Upsilon + \delta K(y)\wedge\left(\alpha - 2\delta J + \delta\Gamma + \Upsilon\right)\right],$$

其中 $\alpha$ 是剪切对共形度规的共轭（辐射），$J$ 是剪切平方的累积（聚焦），$\Upsilon$ 是零法向归一化的变化，$\Gamma$ 是角点快度。总 boost 荷是面积：

$$K = \int_S\epsilon_0\,K(y) = \frac{A}{8\pi G}.$$

**面积就是 boost 的生成元**：$\alpha_\eta(\cdot) = e^{\mathrm{i}\eta K}(\cdot)e^{-\mathrm{i}\eta K}$。这与 JT 的"角点 dilaton 生成 boost"是同一句话（第 3 篇），只是荷换成了面积。

### 3.4 缝合与相对 boost

两个子区域在共享角点 $S$ 处对接时，各自诱导的定向相反。匹配诱导度规与法向导数后，共同的 boost 荷相消，只剩**相对 boost** $\gamma = \Gamma_R - \Gamma_L$ 与平均面积密度 $\bar K(y)$ 共轭（3.64）。角点因此成为一个"规范荷中性"的界面；第 4 篇的全部求和与粘合都建立在这个结构上。

## 4. 量子化：代数、态、型

### 4.1 可观测量代数

不先选 Hilbert 空间，而是用"对约化作用量加源"定义代数（§4.1）：

- 源的变形 $F[j]$ 定义一个相对 S 矩阵 $S_I(F) = U_I^\dagger U_{I+F}$（4.1）；
- 变形的相容性（变量平移不变、因果因子化）给出代数关系（4.2）；
- 对有限个生成元的乘积取算子范数上确界、商去核、完备化，得到 C*-代数 $\mathcal A$。

这是 Haag–Kastler / Buchholz–Fredenhagen 的"代数先于表示"路线（第 2 篇）。

### 4.2 高斯态 → Fock → GNS → $I$ 型

固定角点面积 $A$，把辐射与角点变量展开成可数多组正则对 $(q_j,p_j)$，取高斯态（4.7）：

$$\langle q_j|\Omega_j\rangle = \frac{1}{[2\pi(\Delta q_j)^2]^{1/4}}\exp\left[-\frac{(q_j-q_j^0)^2}{4(\Delta q_j)^2} + \frac{\mathrm{i}}{\hbar}p_j^0(q_j-q_j^0)\right].$$

激发给出 Fock 空间 $K_A \cong \bigoplus_m\mathrm{Sym}^m\ell^2(\mathbb N)$（4.10）。边界源可生成任意秩一投影，故固定面积子代数满足

$$\mathcal M_A = B(K_A)$$

（4.11）。再把纯态延拓到全代数并取 GNS（4.16）：

$$\langle a|b\rangle_\omega = \omega(a^\dagger b),\qquad \pi_\omega(\mathcal A)'' = B(\mathcal H_\omega).$$

纯态 ⇒ 不可约表示 ⇒ $I$ 型因子（第 2 篇自检 3 的定理）。**这一步不依赖动力学细节，是纯态的一般性质。**

### 4.3 时钟投影与绝对收敛

时钟算符（4.27）是一个闭二次型：

$$\big\lVert \hat{\bar u}_*^{1/2}|\psi\rangle\big\rVert^2 = \int_S\epsilon_0(y)\left\lVert\int_\epsilon^1\mathrm{d}v\;e^{\hat\Xi_y(v)/2}\,\hat\varrho_S(y)\,\hat a^{-1/2}|\psi\rangle\right\rVert^2.$$

因果菱形取 $\mathcal H_D = P_D\mathcal H_\omega$，$P_D = \mathbf 1_{[0,\ell(D)]}(\hat{\bar u}_*)$。路径积分的中间态求和（4.29）逐项绝对收敛：

$$\sum_\alpha\left|\langle\phi|U_{M_2}|e_\alpha\rangle\langle e_\alpha|U_{M_1}|\psi\rangle\right| \le \sqrt{\langle\phi|\phi\rangle\langle\psi|\psi\rangle},$$

因为两个因子分别是同一基下的系数（自检 2）。**这是"有限 $G_N$ 下振幅良定"的精确含义。**

### 4.4 引力子对产生：先求和还是先展开

单个入射零锥上的连通两点函数（图 20）：径向模式 $k$ 的方差 $(\Delta q_k)^2 = 1/(2sk)$，$s = A/(4G)$。求和（4.33）

$$\lim_{N\to\infty}2\sum_{k=1}^N(\Delta q_k)^4e^{-2\mathrm{i}k/s} = \frac{\operatorname{Li}_2\!\left(e^{-2\mathrm{i}/s}\right)}{2s^2}$$

有限；而先把相位按 $1/s$（即 $G$）展开再求和（4.34）会得到

$$-\frac{\mathrm{i}}{s^3}\sum_{k=1}^N\frac1k \sim -\frac{\mathrm{i}}{s^3}\ln N$$

——对数发散。**"先求和、后展开"与"先展开、后求和"不等价**：这是论文对"非微扰定义"的最清楚展示，也是它与微扰量子引力（第 8 阶段 01 篇）的分水岭。

## 5. 有限维与面积谱

### 5.1 时钟下界 ⇒ 面积上界

由 $u_* = \varrho_S\int_\epsilon^1 e^{\Xi}\mathrm{d}v \ge (1-\epsilon)\varrho_S$，取角点平均并用 Cauchy–Schwarz：

$$\bar u_* \ge (1-\epsilon)\left(\frac{A}{4\pi}\right)^{1/2} \;\Longrightarrow\; P_D\,\hat A\,P_D \le \frac{4\pi\ell(D)^2}{(1-\epsilon)^2}P_D.$$

（自检 5 推导。）**限制时钟读数 = 限制面积**：有界菱形的面积谱被压在一个紧区间里。

### 5.2 相对 boost 改变跨角点的引力子两点函数

在光滑背景上，剪切的自由真空两点函数（5.28d）为

$$G_{\sigma,0}(u,u') = -\frac{c_\perp}{(u-u')^2}.$$

把右侧零法向做一次相对 boost（$\ell_R\mapsto e^\eta\ell_R$，左侧不动），插入点从 $-d,d$ 移到 $-d,e^\eta d$：

$$\frac{e^\eta G_{\sigma,0}(-d,e^\eta d)}{G_{\sigma,0}(-d,d)} = \frac{4e^\eta}{(1+e^\eta)^2} = 1 - \tanh^2\frac{\eta}{2}.$$

**boost 显著改变两点函数**（不是只乘一个相位）。这是下一个小节反证的关键。

### 5.3 反证：$\mathcal H_D$ 有限维

假设 $\dim\mathcal H_D = \infty$。把允许的面积区间分成有限多个窄带，至少一个窄带 $I$ 含无限维子空间。在 $I$ 内，boost 相位 $e^{\mathrm{i}\eta\hat s/(2\pi)}$ 几乎相同；但 §5.2 说 boost 必须显著改变两点函数。把两者放进同一个振幅比较：

- 一方面，用受 boost 影响的观测量 $\hat O = \sin(j_L\hat\sigma_{f_L})\sin(j_R\hat\sigma_{f_R})$（5.33），其期望值在 boost 下改变 $\delta_\eta$；
- 另一方面，若中间态全部来自 $I$，广义相对论振幅的 boost 相位几乎相同，改变量被压到 $\delta_\eta/2$ 以下（用迹距离估计（5.32）与附录 D.2 的界）；
- 用"闭合切割"（把未来半部与时间反射粘合，图 30）比较"不切割的振幅"与"切割后按圈求和的部分和"，前者为正、后者为负（5.37–5.38）——矛盾。

故 $\dim\mathcal H_D \lt \infty$：**面积算符有分立谱，简并度有限**。

## 6. 熵与对数修正

### 6.1 密度矩阵与熵

由 §5 的有限维与 §3.3 的 boost 荷，迹给出

$$\rho_D = \frac{e^{-\hat A/(4G)}}{Z_{D,1}},\qquad Z_{D,1} = \operatorname{Tr}_{\mathcal H_D}e^{-\hat A/(4G)},$$

$$S(\rho_D) = -\operatorname{Tr}\rho_D\ln\rho_D = \frac{\langle\hat A\rangle}{4G} + \ln Z_{D,1}.$$

第一项是 Bekenstein–Hawking 熵；第二项是对数修正的来源（自检 4 的前半）。

### 6.2 单圈行列式：Gauss–Bonnet 与锥奇点

在 Schwarzschild 背景、固定质量下，微扰行列式的对数正比于曲率平方的积分。在壳 $R_{ab} = 0$ 时它化成四维 Gauss–Bonnet 组合：

$$\int_D R_{abcd}R^{abcd}\epsilon_g = \int_D\left(R_{abcd}R^{abcd} - 4R_{ab}R^{ab} + R^2\right)\epsilon_g.$$

把热圆的开角从 $2\pi n$ 变化，$\delta n$ 的项局域在角点 $S$ 上（锥奇点的分布几何）。用 Gauss 方程与边缘性 $\Theta_{(\ell)} = 0$、$\Theta_{(n)} \lt 0$：

$$2K^{(n)}_{ab}K_{(n)}^{ab} - 2R_{abcd}\ell^a n^b\ell^c n^d = R[q] + 2\Theta_{(\ell)}\Theta_{(n)} = R[q],$$

于是

$$\ln\operatorname{Tr}\left(C_b^\dagger C_b\right) = \frac{53}{45(4\pi)^2}\cdot 8\pi\cdot 8\pi\cdot\frac12\ln s_b + O(1) = \frac{106}{45}\ln s_b + O(1),$$

其中用了 Gauss–Bonnet $\int_S R[q]\mathrm{d}A = 8\pi$ 与 $s_b = A/(4G)$。

### 6.3 $q = 257/302$ 与固定质量系数

$Z(\ell) = \int\mathrm{d}s_b/(4\pi s_b)^{1/2}\operatorname{Tr}(C_b^\dagger C_b)$：被积函数 $\propto s_b^{106/45}$，测度再抬一阶（$\int s^{a-1/2}\mathrm{d}s \propto s^{a+1/2}$），故

$$\ln Z(\ell) \sim \left(\frac{106}{45}+\frac12\right)\ln s_b = \frac{257}{90}\ln s_b.$$

与 $s_b \propto \ell^2$、论文 (5.58) 的 $\ln Z_{D,1} = \frac{q}{1-q}\ln(\ell/\ell_0)$ 比较：

$$\frac{q}{1-q} = \frac{257}{45} \;\Longrightarrow\; q = \frac{257}{302}.$$

代回 (5.65) 的系数并换到固定质量的系综（减去 $\frac12$）：

$$\frac{q}{2(1-q)} - \frac12 = \frac{257}{90} - \frac12 = \frac{212}{90} = \frac{106}{45},$$

与 Sen 的欧氏路径积分结果一致。**注意这个系数来自"固定面积 → 固定质量"的系综变换**，不是又算了一遍行列式。

## 7. 半经典极限

### 7.1 相干态与经典轨迹

取相干态（中心 $q^0,p^0$，宽度 $O(\hbar)$）。期望值满足（6.1）–（6.2）：

$$\frac{\mathrm{i}}{\hbar}\left[Q(H_c),Q(O)\right] = Q(\{O,H_c\}) + O(\hbar^2),\qquad \dot q^k = \{q^k,H_c\},\quad \dot p_k = \{p_k,H_c\}.$$

即**期望值走经典哈密顿轨迹**。对变形 $I_M \to I_M + \hbar f$，期望值 $= e^{\mathrm{i}f[\phi]}(1+O(\hbar))$。

### 7.2 Einstein 方程从微分同胚不变性出来

在经典轨迹上，对内部场做平移 $\phi\mapsto\phi+rs$（$s$ 支撑在内部），振幅不变（4.2d）：

$$\langle\delta_s I_M\rangle = 0 \;\Longrightarrow\; \delta_s I_M[\phi] = 0.$$

在约束面 $S = T = 0$ 上，这就是场方程。代入 $B^{\mu\nu} = \frac12\epsilon^{\mu\nu}{}_{\rho\sigma}e^\rho\wedge e^\sigma$ 与 $\epsilon^{\mu\nu\rho\sigma}\Phi_{\mu\nu\rho\sigma} = 4\Lambda$：

$$R_{ab} - \frac12Rg_{ab} + \Lambda g_{ab} = 0.$$

**Einstein 方程不是"额外的假设"，而是路径积分在内部变形下不变的直接推论**——这是背景独立理论里"动力学 = 规范不变性"的标准逻辑。

### 7.3 反作用：二阶 Einstein 张量与推迟 Green 函数

一圈阶，引力子的涨落虽然期望值为零，但通过二阶项反作用（6.13）：

$$E_{ab}[\bar g] + \left\langle E^{(2)}_{ab}[h,h]\right\rangle_G = O(\hbar^2),$$

$\bar g = g_0 + \Delta g$。二阶源守恒（6.15）：

$$\nabla^aE^{(2)}_{ab}[h,h] = 0,$$

（由缩并 Bianchi 恒等式 $\nabla^aE_{ab}[g_0+\epsilon h] = 0$ 逐阶展开：$\epsilon^0$ 与 $\epsilon^1$ 由背景与线性化方程消去，$\epsilon^2$ 给出上式。）于是解可由推迟 Green 函数写出：

$$\Delta g = \Delta g_0 - G_R\left\langle E^{(2)}[h,h]\right\rangle_G + O(\hbar^2).$$

这正是第 1 篇 §6 的 in-in 语言：**反作用 = 引力子两点函数当作源 + 推迟传播子**。

## 8. 评价与边界

**已证的部分**：代数构造、GNS 与 $I$ 型、$P_D$ 的存在与绝对收敛、面积上界、有限维定理（在 §5.2 的输入下）、熵的领头项与对数修正、半经典极限的领头阶。

**作者自己标注的缺口**（读原文时值得留意）：

- §5.1 论证"高斯态在允许时钟读数上有非零投影"时，有一步用经典量的估计代替非对易算符的矩阵元；作者在脚注 18 称之为**启发式**，正文说"提供了强有力的证据"；
- 脚注 20：不同纯态 $\omega$ 是否给出幺正等价的 GNS 表示，**留作未来工作**——这直接关系到"代数与态的选择是否唯一决定理论"；
- 附录 D 的一圈检查（行列式、聚焦界）是"独立核对"，不是对 §5 反证的替代；
- 与四条验收标准（第 8 阶段 01 篇 §5）对照：**背景独立**✓（构造本身）、**低能一致**✓（§7）、**黑洞账目**部分✓（熵与对数修正；但没有处理蒸发与 Page 曲线）、**紫外完成**只到"中间态求和绝对收敛"，没有讨论普朗克能标散射的幺正性。

**与前作的差别**：论文 §1 与脚注 21 明确对比了"在经典背景上量子化微扰"的路线（如 Ciambelli–Klinger 的零超曲面量子化）：那些构造里代数的型与迹的存在性是开放的；本文把"非线性约化相空间 + 纯态"作为前提，才得到 $I$ 型与可定义的熵。

## 小结

- 一阶引力（Plebański）：$B$ 的简单性约束把 BF 理论变成 GR；边界项（GHY + 零 + 角点）保证变分良定并给出辛势。
- 零初始数据：共形度规（两个偏振）+ 角点边缘模；Raychaudhuri 决定"面积–仿射参数"关系，剪切使时钟变慢；辛形式中面积密度 $K = A/8\pi G$ 是 boost 荷。
- 量子化：代数 → 高斯态 → Fock → GNS；纯态给出不可约表示与 $I$ 型因子；时钟投影 $P_D$；中间态求和绝对收敛；先求和与先展开不等价（$\operatorname{Li}_2$ vs $\ln N$）。
- 有限维：时钟下界 $\Rightarrow$ 面积上界；boost 改变跨角点两点函数 $\Rightarrow$ 反证 $\dim\mathcal H_D\lt\infty$；面积谱分立。
- 熵：$\rho_D = e^{-\hat A/4G}/Z$，$S = \langle A\rangle/4G + \ln Z$；Gauss–Bonnet + 锥奇点给 $\operatorname{Tr}\propto s^{106/45}$；测度抬阶 → $q = 257/302$；固定质量系数 $106/45$，与 Sen 一致。
- 半经典：相干态走经典轨迹；内部平移不变性给出 Einstein 方程；反作用由二阶 Einstein 张量的期望值与推迟 Green 函数组织。

## 自检问题

**1.** 从 Raychaudhuri 方程 (3.25f) 推出 $\partial_v\ln N = -\frac{v}{8}(\partial_v\bar q)^2$、$N = p_\epsilon e^{-\Xi}$ 与时钟公式 (3.27)。

<details markdown='1'><summary>点击显示答案</summary>

记 $\varrho = \varrho_S v$（$v\in[\epsilon,1]$），$N\equiv\partial_u\varrho$。由 $v = \varrho/\varrho_S$ 得 $\partial_u = (\partial_u\varrho/\varrho_S)\partial_v = (N/\varrho_S)\partial_v$。

先把 (3.25f) 与剪切联系：由 (3.25d) $\sigma_{AB} = \frac{\varrho^2}{2}\partial_u\bar q_{AB}$ 与 $\Theta = 2\partial_u\varrho/\varrho$，

$$\sigma_{AB}\sigma^{AB} = \frac{\varrho^4}{4}\left(\partial_u\bar q\right)_{AB}\left(\partial_u\bar q\right)^{AB} = \frac14\left(\partial_u\bar q\right)^2,$$

（指数用 $q^{AB} = \varrho^{-2}\bar q^{AB}$ 升降，$\varrho$ 的幂正好抵消）。代入 (3.25e)：

$$\partial_u\Theta + \frac12\Theta^2 + \sigma^2 = 0 \;\Longrightarrow\; \frac{2\varrho''}{\varrho} - \frac{2(\varrho')^2}{\varrho^2} + \frac{2(\varrho')^2}{\varrho^2} + \frac14\left(\partial_u\bar q\right)^2 = 0,$$

即 $\varrho'' = -\frac{\varrho}{8}(\partial_u\bar q)^2$。

现在换到 $v$：$\varrho'' = \partial_u N = (N/\varrho_S)\partial_v N = (N/\varrho_S)N'$，且 $(\partial_u\bar q)^2 = (N^2/\varrho_S^2)(\partial_v\bar q)^2$。代入：

$$\frac{N}{\varrho_S}N' = -\frac{\varrho_S v}{8}\cdot\frac{N^2}{\varrho_S^2}\left(\partial_v\bar q\right)^2 \;\Longrightarrow\; \frac{N'}{N} = -\frac{v}{8}\left(\partial_v\bar q\right)^2.$$

积分：

$$N(v) = N(\epsilon)\exp\left[-\frac18\int_\epsilon^v s\left(\partial_s\bar q\right)^2\mathrm{d}s\right] \equiv p_{\epsilon,y}\,e^{-\Xi_y(v)}.\qquad\square$$

时钟：$u(v)-u(\epsilon) = \int_\epsilon^v\varrho_S\,\frac{\mathrm{d}v'}{N(v')} = \frac{\varrho_S}{p_\epsilon}\int_\epsilon^v e^{\Xi_y(v')}\mathrm{d}v'$。在 $\epsilon$ 处归一化切矢，定义 $p_\epsilon[u(1)-u(\epsilon)]$：

$$u_*(y) = \varrho_S(y)\int_\epsilon^1 e^{\Xi_y(v)}\,\mathrm{d}v.\qquad\square$$

由于 $\Xi\ge0$，$u_*\ge(1-\epsilon)\varrho_S$——剪切只会让时钟变慢，这是 §5 面积上界的起点。

</details>

**2.** 证明中间态求和的绝对收敛：对任意正交基 $\{|e_\alpha\rangle\}$，

$$\sum_\alpha\left|\langle\phi|U_2|e_\alpha\rangle\langle e_\alpha|U_1|\psi\rangle\right| \le \sqrt{\langle\phi|\phi\rangle\langle\psi|\psi\rangle}.$$

<details markdown="1"><summary>点击显示答案</summary>

$U_1,U_2$ 是幺正的，故 $\{U_1|\psi\rangle$ 的系数 $\}$ 与 $\{U_2^\dagger|\phi\rangle$ 的系数 $\}$ 都是平方可和的。把两个因子写成同一组基下的系数：

$$a_\alpha \equiv \langle e_\alpha|U_1|\psi\rangle,\qquad b_\alpha \equiv \langle\phi|U_2|e_\alpha\rangle = \langle U_2^\dagger\phi|e_\alpha\rangle.$$

由 Parseval：

$$\sum_\alpha|a_\alpha|^2 = \|U_1\psi\|^2 = \langle\psi|\psi\rangle,\qquad \sum_\alpha|b_\alpha|^2 = \|U_2^\dagger\phi\|^2 = \langle\phi|\phi\rangle.$$

对乘积用 Cauchy–Schwarz：

$$\sum_\alpha|a_\alpha b_\alpha| \le \left(\sum_\alpha|a_\alpha|^2\right)^{1/2}\left(\sum_\alpha|b_\alpha|^2\right)^{1/2} = \sqrt{\langle\psi|\psi\rangle\langle\phi|\phi\rangle}.\qquad\square$$

结论：**中间态求和绝对收敛，与基的选取无关**。注意这个论证只用幺正性与 Cauchy–Schwarz，对无穷维基也成立——它正是"有限 $G_N$ 下振幅有限"的数学内容（论文 (4.30)）。与微扰论的对比：微扰展开先按 $G$ 截断、再求和，两个极限不可交换（§4.4 的 $\operatorname{Li}_2$ vs $\ln N$）。

</details>

**3.** 由 boost 协变性推出面积的本征值差为 $8\pi G\hbar k$：从 (4.12) 出发。

<details markdown='1'><summary>点击显示答案</summary>

boost 由 $\hat K = \hat A/(8\pi G)$ 生成：

$$\alpha_\eta(a) = e^{\mathrm{i}\eta\hat A/(8\pi G\hbar)}\,a\,e^{-\mathrm{i}\eta\hat A/(8\pi G\hbar)}.$$

对面积本征态 $|i\rangle$（$\hat A|i\rangle = A_i|i\rangle$）与 $|j\rangle$（$A_j$），矩阵元

$$\langle j|\alpha_\eta(a)|i\rangle = e^{\mathrm{i}\eta(A_j-A_i)/(8\pi G\hbar)}\langle j|a|i\rangle.$$

另一方面，若 $a$ 把 $|i\rangle$ 变成"面积改变 $\Delta A$"的态，相位必须匹配。论文的选择是：$a|i\rangle$ 具有确定的 boost 频率 $k$，即

$$\alpha_\eta(a)|i\rangle = e^{\mathrm{i}\eta k}\,a|i\rangle.$$

比较两式的 $\eta$ 系数：

$$\frac{A_j - A_i}{8\pi G\hbar} = k \;\Longrightarrow\; A_j = A_i + 8\pi G\hbar\,k.$$

在有限维 $\mathcal H_D$ 里，$\hat A$ 的谱有限、步长由上式给出（$k$ 取离散值）；再配合 §5.3 的"面积区间有限"，得到**有限个面积本征值、每个简并度有限**的分立谱。$\square$

物理读法：$\hbar$ 的系数里出现了 $G$——**面积的量子化步长是 $8\pi G\hbar$（量级为普朗克面积的 $8\pi$ 倍）**。这与圈量子引力面积谱（第 8 阶段 02 篇）形式不同（那里是 $\sum\sqrt{j(j+1)}$），但"几何量有分立谱"的结论一致。

</details>

**4.** 由 $\rho_D = e^{-\hat A/(4G)}/Z_{D,1}$ 推出 $S = \langle A\rangle/4G + \ln Z_{D,1}$；再由 $\operatorname{Tr}(C_b^\dagger C_b)\propto s_b^{106/45}$ 与配分函数测度推出 $q = 257/302$ 与固定质量系数 $106/45$。

<details markdown='1'><summary>点击显示答案</summary>

**熵**：

$$S = -\operatorname{Tr}\rho_D\ln\rho_D = -\operatorname{Tr}\left[\frac{e^{-A/4G}}{Z}\left(-\frac{A}{4G}-\ln Z\right)\right] = \frac{\langle A\rangle}{4G} + \ln Z.\qquad\square$$

**$q$ 的算术**：设 $\operatorname{Tr}(C_b^\dagger C_b) = s_b^{106/45}$（忽略 $O(1)$）。配分函数

$$Z(\ell) = \int\frac{\mathrm{d}s_b}{(4\pi s_b)^{1/2}}\,s_b^{106/45} \propto \int\mathrm{d}s_b\,s_b^{106/45 - 1/2} \propto s_b^{106/45+1/2} = s_b^{257/90}.$$

（积分把幂次抬一阶：$\int s^{a-1/2}\mathrm{d}s \propto s^{a+1/2}$。）用 $s_b\propto\ell^2$：

$$\ln Z(\ell) = \frac{257}{90}\ln s_b = \frac{257}{45}\ln\ell + \text{const}.$$

与 (5.58) 的 $\ln Z_{D,1} = \frac{q}{1-q}\ln(\ell/\ell_0) + O(1)$ 比较：

$$\frac{q}{1-q} = \frac{257}{45} \;\Longrightarrow\; q = \frac{257}{45+257} = \frac{257}{302}.\qquad\square$$

**固定质量系数**：从固定面积换到固定质量（对 $\mathrm{d}M$ 积分，$\mathrm{d}s_b/\sqrt{s_b}\propto\mathrm{d}M$）时，熵的系数减去 $1/2$：

$$\frac{q}{2(1-q)} - \frac12 = \frac{257}{90} - \frac{45}{90} = \frac{212}{90} = \frac{106}{45}.\qquad\square$$

这正是 Sen 的欧氏结果。两个容易混淆的点：$q$ 是"时钟截断下迹的增长指数"，不是热力学系数；$106/45$ 是"固定质量熵的对数修正"，两者差一次系综变换与一个 $1/2$。

</details>

**5.** 证明时钟下界 $\bar u_* \ge (1-\epsilon)(A/4\pi)^{1/2}$，并由此写出 $P_D\hat A P_D$ 的上界。

<details markdown='1'><summary>点击显示答案</summary>

由 $u_*(y) = \varrho_S(y)\int_\epsilon^1 e^{\Xi_y(v)}\mathrm{d}v \ge (1-\epsilon)\varrho_S(y)$（$\Xi\ge0$）。角点平均定义

$$\bar u_* = \frac{\int_S\epsilon_0\,\varrho_S\,u_*}{\int_S\epsilon_0\,\varrho_S} \ge (1-\epsilon)\,\frac{\int_S\epsilon_0\,\varrho_S^2}{\int_S\epsilon_0\,\varrho_S}.$$

用 Cauchy–Schwarz（取 $\epsilon_0$ 为测度，$S$ 的总测度为 $4\pi$）：

$$\left(\int_S\epsilon_0\,\varrho_S\right)^2 \le \left(\int_S\epsilon_0\right)\left(\int_S\epsilon_0\,\varrho_S^2\right) = 4\pi\,A,$$

故

$$\frac{\int\epsilon_0\varrho_S^2}{\int\epsilon_0\varrho_S} \ge \left(\frac{A}{4\pi}\right)^{1/2} \;\Longrightarrow\; \bar u_* \ge (1-\epsilon)\left(\frac{A}{4\pi}\right)^{1/2}.\qquad\square$$

面积上界：在 $\mathcal H_D$ 上 $P_D\bar u_*P_D \le \ell(D)P_D$，与上式联立：

$$\ell(D) \ge (1-\epsilon)\left(\frac{A}{4\pi}\right)^{1/2} \;\Longrightarrow\; P_D\hat A\,P_D \le \frac{4\pi\ell(D)^2}{(1-\epsilon)^2}P_D.$$

物理含义：**时钟读数上限 = 面积上限**。这是 §5.3 反证的前提——若 $\mathcal H_D$ 无限维，面积谱就必须在紧区间里塞下无限多个正交态，而 boost 在窄区间上的相位近似相同，与"boost 改变两点函数"冲突。

</details>

## 参考

- 论文：V. Chandrasekaran, "An algebraic quantization of gravity from the null cone", arXiv:2611.34924（本篇按论文的公式编号对照）。
- Reisenberger, Phys. Rev. Lett. 101 (2008) 211101（arXiv:0712.2541）、Class. Quantum Grav. 30 (2013) 155022（arXiv:1211.3880）：零初始数据的辛形式与 Poisson 括号。
- Chandrasekaran & Flanagan, "Horizon phase spaces in general relativity"（arXiv:2309.03871）：视界相空间与边缘模。
- Donnelly & Freidel, JHEP 09 (2016) 102（arXiv:1601.04744）；Speranza, JHEP 02 (2018) 021（arXiv:1706.05061）：局域子系统、边缘模与表面荷。
- Harlow & Wu, JHEP 10 (2020) 146（arXiv:1906.08616）：带边界的协变相空间（辛势与边界项的系统处理）。
- Regge & Teitelboim, Ann. Phys. 88 (1974) 286：哈密顿量化为表面荷；Plebański, J. Math. Phys. 18 (1977) 2511：一阶引力。
- Sen, JHEP 04 (2013) 156（arXiv:1205.0971）：Schwarzschild 熵的对数修正（固定质量、$106/45$）。
