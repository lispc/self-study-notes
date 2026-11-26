# 带边界的作用量：GHY 项、零边界项与角点项

> 路线图位置：第 3 部分（边界、约束与相空间）· 第 10 章
> 前置知识：第 3 章（外曲率）、第 5 章（EH 作用量与变分）、第 7–8 章（类空超曲面、零超曲面、$\Theta$）、第 5s 章（一阶引力）。
> 学习目标：会推导 EH 作用量的边界项并说明 GHY 项如何抵消它；会算 Brown–York 张量并验证它给出 ADM 质量；能说清零边界上为什么没有 GHY 项、替代物 $\int\sqrt q\,\Theta$ 为什么是"全导数"、以及为什么零锥问题的一切边界物理都集中在角点 $S$；理解"时间合成 = gluing"对边界项与角点项的要求。

---

**单位约定**：$\eta_{ab}=\mathrm{diag}(-,+,+,+)$，$c=1$，保留 $G_N$。边界 $\partial M$ 的单位法矢 $n$：类空边界 $n^2=-1$、类时边界 $n^2=+1$；$h_{\mu\nu}=g_{\mu\nu}+n_\mu n_\nu$（$n^2=-1$）或 $g_{\mu\nu}-n_\mu n_\nu$（$n^2=+1$）。外曲率统一定义为 $K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma$，$K=h^{\mu\nu}K_{\mu\nu}$。**本章只用到"$K$ 与 $n$ 的符号约定一致"这一点**，具体号差在自检中检验。

## 1. 一句话总结

**区域上的作用量在变分时，法向导数会跑到边界上变成一项"不能由固定边界数据消掉"的项；GHY 项 $+\frac{1}{8\pi G}\int\sqrt h\,K$ 的任务就是抵消它，使"固定诱导度规"的 Dirichlet 原理成立。零边界上 $h$ 退化、$K$ 不存在，替代物是 $\frac{1}{8\pi G}\int\sqrt q\,\Theta$——而 $\sqrt q\,\Theta=\partial_u\sqrt q$，所以这个边界项是沿生成元的全导数，它的变分只在角点 $S$ 上有支撑。于是零锥问题的全部边界物理（面积、boost 荷、引力时钟、熵）都集中在角点上，这正是论文把可观测量都"描"到角点标架上的原因。**

## 2. 边界项从哪里来

### 2.1 Palatini 恒等式

Einstein–Hilbert 作用量

$$S_{\rm EH}=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\,R\,\mathrm{d}^4x .$$

变分 $g$ 时，$\delta R$ 不是代数项。用 Palatini 恒等式

$$\delta R_{\mu\nu}=\nabla_\rho\left(\delta\Gamma^\rho_{\nu\mu}\right)-\nabla_\nu\left(\delta\Gamma^\rho_{\rho\mu}\right)
\;\Longrightarrow\;
\delta R=\nabla_\mu v^\mu,$$

$$\boxed{\;v^\mu\equiv g^{\alpha\beta}\delta\Gamma^\mu_{\alpha\beta}-g^{\mu\alpha}\delta\Gamma^\beta_{\alpha\beta}.\;}$$

于是

$$\delta S_{\rm EH}=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\left(G_{\mu\nu}\delta g^{\mu\nu}+\nabla_\mu v^\mu\right)
=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}
+\frac{1}{16\pi G_N}\int_{\partial M}\sqrt{|h|}\;n_\mu v^\mu .$$

**第一项给出运动方程，第二项是障碍**：如果只固定 $\delta g$ 在边界上为零（Dirichlet），$n_\mu v^\mu$ 一般不为零，因为 $\delta g$ 的法向导数没有被固定。

### 2.2 在 Gaussian normal 坐标里算 $n_\mu v^\mu$

取边界附近

$$\mathrm{d}s^2=\epsilon\,\mathrm{d}r^2+h_{ij}(r,x)\mathrm{d}x^i\mathrm{d}x^j,\qquad \epsilon=n^2=\pm1,$$

法矢 $n=\partial_r$。克里斯托费尔符号

$$\Gamma^r_{ij}=-\tfrac12\partial_r h_{ij},\qquad n_r=\epsilon .$$

在 $\delta h_{ij}=0$（边界上）但 $\partial_r\delta h_{ij}\neq0$ 的变分下，$v^r$ 有两项：

$$v^r=\underbrace{g^{ij}\delta\Gamma^r_{ij}}_{-\frac12\epsilon h^{ij}\partial_r\delta h_{ij}}
-\underbrace{g^{rr}\delta\Gamma^\beta_{r\beta}}_{\frac12\epsilon h^{ij}\partial_r\delta h_{ij}}
=-\epsilon\,h^{ij}\partial_r\delta h_{ij},$$

（第二项用 $\Gamma^\beta_{r\beta}=\partial_r\ln\sqrt h$）。于是

$$n_r v^r=\epsilon\cdot\left(-\epsilon\,h^{ij}\partial_r\delta h_{ij}\right)=-h^{ij}\partial_r\delta h_{ij}=-2\delta K,$$

最后一步用 $\delta K=\frac12h^{ij}\partial_r\delta h_{ij}$（见下）。**两项都必须算**：第一项来自 $\delta\Gamma^r_{ij}$，第二项来自 $v^\mu$ 的第二个结构；漏掉第二项会让结果差一个因子 2。

而

$$K_{ij}=\nabla_i n_j=-\Gamma^r_{ij}n_r=\epsilon\cdot\tfrac12\partial_r h_{ij},
\qquad
\delta K=\tfrac12 h^{ij}\partial_r\delta h_{ij}+\tfrac12\delta h^{ij}\partial_r h_{ij}
=\tfrac12 h^{ij}\partial_r\delta h_{ij}$$

（第二项因 $\delta h^{ij}=0$ 而消失）。所以

$$\boxed{\;n_\mu v^\mu=-2\,\delta K\;}$$

**与 $\epsilon$ 无关**——类空边界与类时边界用同一个公式。（自检 1 给完整推导。）

### 2.3 GHY 项

$$\boxed{\;S_{\rm GHY}=\frac{1}{8\pi G_N}\int_{\partial M}\sqrt{|h|}\,K\;}$$

$$\delta\left(S_{\rm EH}+S_{\rm GHY}\right)
=\frac{1}{16\pi G_N}\int_M\sqrt{-g}\,G_{\mu\nu}\delta g^{\mu\nu}
+\frac{1}{16\pi G_N}\int_{\partial M}\sqrt{|h|}\left(-2\delta K+2\delta K\right).$$

边界项**精确抵消**。于是：固定 $\delta g|_{\partial M}=0$ 时，$\delta(S_{\rm EH}+S_{\rm GHY})=0$ 给出真空 Einstein 方程。这就是**Dirichlet 变分原理**。

**物理读法**：$S_{\rm EH}$ 单独不是"好的"作用量——它依赖于你把边界放在哪里、边界附近怎么延拓。加上 GHY 后，改变边界附近的延拓（保持诱导度规不变）不改变作用量。这与热力学里"用自由能而不是内能"是同一类操作：**换一个在边界上固定的量，就要换一个作用量。**

## 3. Brown–York 张量与 ADM 质量

把边界项对 $\delta h^{ab}$ 的系数读出来，就得到边界上的"能量密度"：

$$\delta S=\frac{1}{16\pi G_N}\int_M\sqrt{-g}G_{ab}\delta g^{ab}
+\frac{1}{16\pi G_N}\int_{\partial M}\sqrt h\left(Kh_{ab}-K_{ab}\right)\delta h^{ab},$$

$$\boxed{\;T^{\rm BY}_{ab}\equiv-\frac{2}{\sqrt h}\frac{\delta S}{\delta h^{ab}}
=\frac{1}{8\pi G_N}\left(K_{ab}-Kh_{ab}\right).\;}$$

$T^{\rm BY}$ 叫**Brown–York 张量**。它在渐近平坦时空的大半径球面上积分，给出 ADM 质量（自检 5 用 Schwarzschild 验证）：

$$M_{\rm ADM}=\frac{1}{8\pi G_N}\int_S\sqrt{\sigma}\left(k_0-k\right)\mathrm{d}^2x,$$

$k$ 是二维曲面 $S$ 在类空切片 $\Sigma$ 内的外曲率，$k_0$ 是同一曲面嵌入平坦空间的外曲率。**减去 $k_0$ 是必要的**：Minkowski 的 $k$ 不为零（球面在平直空间里有 $2/r$），不减掉它就会得到"真空有质量"。

## 4. 零边界：为什么 GHY 不存在

### 4.1 退化

在零边界上，诱导度规 $h_{ab}=g_{ab}$ 限制在 $H$ 上，秩为 2（第 8 章 §2）。行列式为零：

$$\sqrt{|h|}=0 .$$

GHY 项直接**消失**——不是"很小"，而是恒等于零。同时 $K=\nabla\cdot n$ 无法定义：没有类时/类空的单位法矢，$h$ 又不能用来缩并。

**这就是为什么论文必须用一阶变量与 $q_{AB}$ 重做整套边界分析**（App A、B）。你不能把类空边界的公式"连续形变"到零边界：极限是奇异的。

### 4.2 替代物：$\Theta$ 而不是 $K$

零边界上能固定的几何量是 cut 上的二维度规 $q_{AB}$（或它的共形类）。与它共轭的量是膨胀 $\Theta$（确切说是 $\frac12\Theta q_{AB}+\sigma_{AB}=K_{AB}$）。标准形式的零边界项是

$$\boxed{\;S_{\rm null}=\frac{1}{8\pi G_N}\int_{u_-}^{u_+}\mathrm{d}u\int_S\mathrm{d}^2y\;\sqrt q\;\Theta_{(\ell)}\;}$$

（$\ell$ 取仿射参数；非仿射时有 $\Theta+\kappa$ 的修正，$\kappa$ 的重参数化与该项的变换必须一起看。）

### 4.3 关键事实：它是全导数

$$\sqrt q\,\Theta_{(\ell)}=\partial_u\sqrt q .$$

所以

$$S_{\rm null}=\frac{1}{8\pi G_N}\left[\int_S\sqrt q\,\mathrm{d}^2y\right]_{u_-}^{u_+}
=\frac{1}{8\pi G_N}\left(A_+-A_-\right),$$

**零边界项 = 两端 cut 的面积差 ÷ $8\pi G_N$**。变分它：

$$\delta S_{\rm null}=\frac{1}{8\pi G_N}\left(\delta A_+-\delta A_-\right),$$

只有**角点**（cut 的端点 $u_\pm$）上的贡献，没有 bulk 沿生成元的积分。

**这条事实是整篇论文的骨架**：

- 零锥区域的作用量，bulk 项在约束面上消去，边界项是面积差，**全部信息压在角点**；
- 角点上的共轭结构 = 面积 × boost 相位；
- 把 boost 解析延拓到 $i\pi$（半转）得到 $e^{-2\pi K}=e^{-A/4G_N\hbar}$——**Gibbs 权重**；
- 熵 $S=\langle A\rangle/4G_N+\log Z$ 的第一项就是它（第 13 章、[QFT 书第 9 阶段 04 篇](../../qft-sm/docs/stage-09-algebraic-quantum-gravity/04-null-canonical-gravity-black-hole-entropy.md)）。

## 5. 角点项与"时间合成"

### 5.1 角点项的必要性

当区域有两个以上的边界片（例如两张零锥 + 两个 cap），变分时每片的边界项在交线（角点）上会产生额外的项。这些项不能由任何一片单独吸收，必须显式加一个**角点作用量**（joint/corner term）。

论文的写法（3.53a）把它整理成

$$I=\int_{t_i}^{t_f}\left(p_k\dot q^k-H_c\right)\mathrm{d}t+\left[\chi_t\right]_{t_i}^{t_f},$$

$\chi_t$ 是角点项打包出来的全导数，$H_c$ 是"修正后的哈密顿量"：

$$H_c(\phi,t)=H(\iota_t(\phi),t)-\Theta_t(\partial_t\iota_t)+\partial_t\chi_t .$$

**读法**：把作用量写成"正则形式 + 一个全导数"是任何带边界系统的一般结构。全导数不影响运动方程，但它**决定量子力学里的相位**——而相位正是论文用来定义振幅与迹的东西。

### 5.2 时间合成 = gluing

论文的核心一致性要求是：

$$\text{先在时间上分成两段再合成}\quad=\quad\text{先在空间上分成两块再缝合}$$

用公式说，若 $M=M_2\circ_{\Sigma}M_1$（沿中间切片 $\Sigma$ 粘起来），则

$$U_{M_2\circ M_1}=U_{M_2}U_{M_1},\qquad
\langle\phi|U_{M_2}U_{M_1}|\psi\rangle=\sum_\alpha\langle\phi|U_{M_2}|e_\alpha\rangle\langle e_\alpha|U_{M_1}|\psi\rangle .$$

这个等式要成立，需要三件事同时对上：

1. **cap 上的项相消**：两段的 cap 定向相反（一段的出射面 = 另一段的入射面），作用量里的 cap 项相加为零。
2. **角点项相加**：两段在 $\Sigma$ 的边界（同一条 $S$）上各有一个角点项，它们必须合成整体的角点项。
3. **边界项在公共面上相消**：见 §6。

论文 §4.4 用这个等式证明中间态求和的绝对收敛（Cauchy–Schwarz），并在 App C.1 验证"改变 cut 或改变边界标架只给两端的幺正变换，求和里相消"。

## 6. 缝合：GHY 为什么相消而不是相加

设 $M=M_1\cup M_2$，公共边界 $\Sigma$。$M_1$ 的外法矢 $n_1$ 与 $M_2$ 的外法矢 $n_2$ 满足 $n_2=-n_1$。于是

$$K^{(2)}=-K^{(1)},\qquad \sqrt{h^{(2)}}=\sqrt{h^{(1)}},$$

（$h$ 是同一个诱导度规，与法矢取向无关）所以

$$\int_\Sigma\sqrt h\,K^{(1)}+\int_\Sigma\sqrt h\,K^{(2)}=0 .$$

**公共边界上的 GHY 项相消，剩下的只有整体外边界上的 GHY 项**——作用量可加：

$$S[M_1]+S[M_2]=S[M_1\cup M_2]+\text{角点项}.$$

这就是"缝合时不需要在内部边界上额外加东西"的技术内容。反过来说，如果边界项写错了（比如少了因子 2 或符号反了），缝合就不会给出正确的作用量——这是检验边界项最灵敏的试纸。

## 7. 三种边界条件与"系综"

同一个体作用量，配不同的边界项 = 固定不同的边界量 = 不同的热力学系综：

| 边界上固定 | 需要加的边界项 | 类比 |
|---|---|---|
| $h_{ab}$（Dirichlet） | $+\frac{1}{8\pi G}\int\sqrt hK$（GHY） | 正则系综（固定"形状"） |
| $K_{ab}$（Neumann） | 不加（或加 $-S_{\rm GHY}$） | 微正则（固定"共轭量"） |
| 零边界：$q_{AB}$（共形类） | $+\frac{1}{8\pi G}\int\sqrt q\,\Theta$ | 固定"面积元" |
| 零边界：$\Theta$ | 不加 | 固定"膨胀" |

论文 §3.2 用的是**组合**：(3.18) 在 cap 上固定面积元与膨胀的比例（$dA|_{\partial\Sigma_i}=\epsilon^2dA|_S$），在角点固定面积（§5.2 的 $P_D\hat{\mathcal A}P_D$）。这正是"零锥 + 角点"这套边界条件与类空 Dirichlet 的本质区别：**角点上的面积是一个独立的、可被算符化的量**。

## 8. 与论文 App B 的接口

论文用坐标 (B.1)

$$\mathrm{d}s^2=-F\,\mathrm{d}t^2-2N\,\mathrm{d}t\,\mathrm{d}v+q_{AB}\left(\mathrm{d}y^A+V^A\mathrm{d}t\right)\left(\mathrm{d}y^B+V^B\mathrm{d}t\right)$$

把边界项算成 Hamiltonian。两个值得记住的式子：

- (B.2a)：$\frac12\partial_v q_{AB}=\frac12\Theta_{(\ell)}q_{AB}+\sigma_{AB}$——就是第 8 章的 (3.25a)，在坐标里的样子。
- (B.3)：$\partial_v f=-\dfrac{\sigma_{AB}\sigma^{AB}}{\Theta_{(\ell)}}$，$f\equiv-\log N$。**剪切使 lapse 沿生成元减小**——这就是第 8 章 §5.3 "固定面积下剪切增大时钟读数"的哈密顿形式。$N$ 是 lapse，$f$ 是它的对数，$\partial_v f<0$ 意味着沿光走 $N$ 越来越小，同一个坐标位移对应的固有时（时钟读数）越来越大。

**一句话**：第 8 章的几何不等式 $\varrho\le u$，在 Hamiltonian 语言里就是 (B.3) 的 $\partial_v\log N=-\sigma^2/\Theta\le0$。两条路给出同一个结论，这是论文最扎实的地方。

## 9. 小结

- $\delta S_{\rm EH}$ 的边界项来自 $\delta R=\nabla\cdot v$；在 Gaussian normal 坐标里 $n\cdot v=-2\delta K$。
- $S_{\rm GHY}=+\frac{1}{8\pi G}\int\sqrt hK$ 精确抵消它 ⇒ 固定诱导度规的 Dirichlet 原理成立。
- Brown–York 张量 $T^{\rm BY}_{ab}=\frac{1}{8\pi G}(K_{ab}-Kh_{ab})$；渐近球面积分给 ADM 质量（减掉平直背景 $k_0$）。
- 零边界：$\sqrt h=0$、$K$ 不存在；替代物 $S_{\rm null}=\frac{1}{8\pi G}\int\sqrt q\Theta$，而 $\sqrt q\Theta=\partial_u\sqrt q$ ⇒ 它是全导数 ⇒ 变分只在角点有支撑 ⇒ $S_{\rm null}=\frac{1}{8\pi G}(A_+-A_-)$。
- 角点项打包成 (3.53a) 的 $[\chi_t]_{t_i}^{t_f}$；它不影响运动方程但决定量子相位。
- 缝合时公共边界的 GHY 项因 $n_2=-n_1$ 而相消，作用量可加；cap 项相消 + 角点项相加，才使"时间合成 = gluing"。
- 边界条件的选择 = 系综的选择；论文用"零锥固定 $q_{AB}$ + 角点固定面积"这套组合，使面积成为可算符化的量。

## 自检问题

**1.** 在 Gaussian normal 坐标 $\mathrm{d}s^2=\epsilon\,\mathrm{d}r^2+h_{ij}\mathrm{d}x^i\mathrm{d}x^j$ 中，用 $\delta h_{ij}|_{\partial M}=0$ 推出 $n_\mu v^\mu=-2\delta K$，并说明为什么这个结果与 $\epsilon=n^2=\pm1$ 无关。

<details markdown="1"><summary>点击显示答案</summary>

**度规与法矢**：$g_{rr}=\epsilon$，$g_{ri}=0$，$g_{ij}=h_{ij}$；$n^\mu=\delta^\mu_r$，$n_\mu=g_{\mu r}=\epsilon\,\delta_r$.

**克里斯托费尔符号**：

$$\Gamma^r_{ij}=\tfrac12 g^{rr}\left(\partial_i g_{jr}+\partial_j g_{ir}-\partial_r g_{ij}\right)=-\tfrac12\epsilon\,\partial_r h_{ij},$$

$$\Gamma^k_{ir}=\tfrac12 h^{kl}\partial_r h_{il},\qquad \Gamma^r_{rr}=0,\quad \Gamma^r_{ri}=0 .$$

**$v^r$**：$v^r=g^{\alpha\beta}\delta\Gamma^r_{\alpha\beta}-g^{r\alpha}\delta\Gamma^\beta_{\alpha\beta}$。两项都要算。

*第一项*：$\delta g_{rr}=\delta g_{ri}=0$ 与 $\delta h_{ij}|_{\partial M}=0$ 给出

$$\delta\Gamma^r_{ij}=-\tfrac12\epsilon\,\partial_r\delta h_{ij},\qquad
\delta\Gamma^r_{rr}=\delta\Gamma^r_{ri}=0,$$

故 $g^{\alpha\beta}\delta\Gamma^r_{\alpha\beta}=g^{ij}\delta\Gamma^r_{ij}=-\tfrac12\epsilon\,h^{ij}\partial_r\delta h_{ij}$。

*第二项*：$g^{r\alpha}$ 只有 $\alpha=r$ 存活，$g^{rr}=\epsilon$；而 $\Gamma^\beta_{r\beta}=\frac12g^{\beta\sigma}\partial_r g_{\beta\sigma}=\partial_r\ln\sqrt{|\det g|}=\partial_r\ln\sqrt h$（$\det g=\epsilon\det h$，$\epsilon$ 为常数）。于是

$$\delta\Gamma^\beta_{r\beta}=\partial_r\left(\tfrac12 h^{ij}\delta h_{ij}\right)=\tfrac12 h^{ij}\partial_r\delta h_{ij},$$

第二步把 $h^{ij}$ 挪进导数内用了 $\delta h|_{\partial M}=0$。所以第二项 $=-g^{rr}\delta\Gamma^\beta_{r\beta}=-\tfrac12\epsilon\,h^{ij}\partial_r\delta h_{ij}$。

*合并*：

$$v^r=-\tfrac12\epsilon\,h^{ij}\partial_r\delta h_{ij}-\tfrac12\epsilon\,h^{ij}\partial_r\delta h_{ij}
=-\epsilon\,h^{ij}\partial_r\delta h_{ij}.$$

**$K$**：

$$K_{ij}=\nabla_i n_j=\partial_i n_j-\Gamma^\rho_{ij}n_\rho=-\Gamma^r_{ij}n_r=-\left(-\tfrac12\epsilon\partial_r h_{ij}\right)\epsilon=\tfrac12\partial_r h_{ij},$$

$$K=h^{ij}K_{ij}=\tfrac12 h^{ij}\partial_r h_{ij}=\partial_r\ln\sqrt h .$$

变分（边界上 $\delta h_{ij}=0$，故 $\delta h^{ij}=0$）：

$$\delta K=\tfrac12 h^{ij}\partial_r\delta h_{ij}+\tfrac12\delta h^{ij}\partial_r h_{ij}=\tfrac12 h^{ij}\partial_r\delta h_{ij}.$$

**合并**：

$$n_r v^r=\epsilon\cdot\left(-\epsilon\,h^{ij}\partial_r\delta h_{ij}\right)
=-h^{ij}\partial_r\delta h_{ij}=-2\delta K .\qquad\square$$

**为什么必须算第二项**：$v^\mu$ 的定义本身就是"两个结构的差"；只用第一项会得到 $-n_rv^r=\delta K$（差因子 2），从而误判 GHY 项需要系数 $\frac{1}{4\pi G}$ 而不是 $\frac{1}{8\pi G}$。检验办法：两区域缝合时 GHY 必须精确相消（§6），这只有在系数为 $\frac{1}{8\pi G}$ 时成立。

**与 $\epsilon$ 无关的原因**：$n_r=\epsilon$ 与 $v^r\propto\epsilon$ 的两个 $\epsilon$ 相乘为 $\epsilon^2=1$。几何上，$n\cdot v$ 与 $K$ 都是"法矢方向的导数"，与法矢的归一化符号无关；改变 $n\to-n$ 时 $K\to-K$、$n\cdot v\to-n\cdot v$，比值不变。

**边界项**：

$$\delta S_{\rm EH}\supset\frac{1}{16\pi G}\int_{\partial M}\sqrt h\,n\cdot v
=-\frac{1}{8\pi G}\int_{\partial M}\sqrt h\,\delta K,$$

与 $\delta S_{\rm GHY}=+\frac{1}{8\pi G}\int\sqrt h\delta K$ 精确抵消。$\square$

</details>

**2.** 说明为什么零边界上不存在 GHY 项：从 $\sqrt h=0$ 与 $K$ 的定义两方面讲；再说明 $\int\sqrt q\,\Theta$ 为什么是合适的替代（它固定的是什么）。

<details markdown="1"><summary>点击显示答案</summary>

**$\sqrt h=0$**：零边界上 $h_{ab}=g_{ab}|_H$。$H$ 的切空间包含零矢 $\ell^a$，而 $h_{ab}\ell^b=0$。所以 $h$ 作为 $3\times3$ 矩阵有一个零特征值，$\det h=0$，$\sqrt{|h|}=0$。GHY 项恒等于零。

**$K$ 无法定义**：$K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma$ 需要单位法矢 $n$。零边界上：

- 法矢是 $\ell$，它零，不能归一化为 $\pm1$；
- 若强行用 $q^{ab}$ 缩并，得到的不是"三维迹"而是"二维迹"，量纲与含义都变了；
- 把类空边界连续形变到零边界（$n^2\to0$）时，$K\sim1/\sqrt{n^2}\to\infty$，GHY 项的极限是奇异的。

**替代物固定什么**：$\int\sqrt q\,\Theta$ 里只有 cut 度规 $q_{AB}$ 与它的 $u$ 导数。变分它时，边界上固定的是 $q_{AB}$（相对固定的参考面积元 $\epsilon_0$，即固定共形类 + 面积振幅的初值）。所以它是**零边界的 Dirichlet 项**：固定"每张 cut 上距离怎么量"，不固定"距离怎么随 $u$ 变"。

**为什么它能替代**：因为 $\sqrt q\,\Theta=\partial_u\sqrt q$，所以

$$\int_{u_-}^{u_+}\sqrt q\,\Theta\,\mathrm{d}u=\sqrt q(u_+)-\sqrt q(u_-) .$$

边界项变成"两端 cut 的面积差"。这与 GHY 的"边界上的外曲率积分"是同一角色的东西：**都是把体作用量里跑出去的导数收回来，代价是把边界数据固定下来**。区别在于：类空边界的 GHY 是边界上的积分，零边界的项在变分后只留下角点上的项。

**这也解释了为什么零锥文献里到处是"corner term"**：不是人们喜欢加项，而是零边界的 Dirichlet 项本身就把所有动力学压到了角点上。$\square$

</details>

**3.** 用一维类比说明"零边界项的变分只在角点有支撑"：对 $S=\int_{u_-}^{u_+}f\,\dot g\,\mathrm{d}u$ 变分 $g$（固定端点），写出边界项；再把 $f=\sqrt q$、$g=\ln\sqrt q$ 对应到 $\int\sqrt q\Theta$。

<details markdown="1"><summary>点击显示答案</summary>

**一维类比**：

$$S=\int_{u_-}^{u_+}f\,\dot g\,\mathrm{d}u .$$

变分：

$$\delta S=\int f\,\delta\dot g\,\mathrm{d}u=\left[f\,\delta g\right]_{u_-}^{u_+}-\int\dot f\,\delta g\,\mathrm{d}u .$$

固定端点（$\delta g(u_\pm)=0$）时边界项为零，得到运动方程 $\dot f=0$。**若端点不固定**（零锥问题里 cut 的位置是动力学变量），边界项

$$\left[f\,\delta g\right]_{u_-}^{u_+}$$

就是角点项：它只在 $u=u_\pm$ 处有支撑。

**对应到零边界**：$\Theta=\partial_u\ln\sqrt q$，所以

$$\int\sqrt q\,\Theta\,\mathrm{d}u=\int f\,\dot g\,\mathrm{d}u,\qquad f=\sqrt q,\quad g=\ln\sqrt q .$$

于是 $\delta S_{\rm null}\propto[\sqrt q\,\delta\ln\sqrt q]_{u_-}^{u_+}=\left[\delta\sqrt q\right]_{u_-}^{u_+}$，即两端 cut 的面积变分——**角点项就是"面积的变化"**。

**为什么这正是论文需要的**：

1. 角点上的共轭变量是面积（或其对数），所以面积可以被提升为算符 $\hat{\mathcal A}$（论文 (4.12b)、(5.21)）。
2. 角点的 boost 荷是 $K=\mathcal A/(8\pi G)$（论文 (3.41)、(5.22)），而面积正是 $f=\sqrt q$ 在 cut 上的积分。
3. 把 boost 解析延拓 $i\pi$，角点项给相位 $e^{-2\pi K}=e^{-\mathcal A/(4G\hbar)}$——**Gibbs 权重**。

**一句话**：类空边界的物理在边界上，零边界的物理在角点上。这是本章最值得记住的一句。$\square$

</details>

**4.** 两个区域沿公共边界 $\Sigma$ 粘合时，证明 GHY 项在 $\Sigma$ 上相消、作用量可加；再说明为什么"cap 项相消"与"角点项相加"是时间合成 $U_{M_2}U_{M_1}$ 的必要条件。

<details markdown="1"><summary>点击显示答案</summary>

**GHY 相消**：$M_1$、$M_2$ 在 $\Sigma$ 上的外法矢相反：$n_2=-n_1$。外曲率是 $n$ 的线性函数（$K_{\mu\nu}=h_\mu{}^\rho h_\nu{}^\sigma\nabla_\rho n_\sigma$，$h$ 只依赖 $n^2$），故

$$K^{(2)}=-K^{(1)} .$$

诱导度规相同（$h$ 与法矢取向无关），所以

$$\int_\Sigma\sqrt h\,K^{(1)}+\int_\Sigma\sqrt h\,K^{(2)}=0 .$$

两份 GHY 项相加时，公共面上的贡献为零，只剩整体外边界：

$$S_{\rm GHY}[M_1]+S_{\rm GHY}[M_2]=S_{\rm GHY}[M_1\cup M_2].\qquad\square$$

**cap 项相消**：$M_1$ 的出射 cap 与 $M_2$ 的入射 cap 是同一点集，但定向相反。作用量里的 cap 项（若写成 $\int_{\rm cap}\sqrt h K$ 之类的定向积分）因此相加为零。这样两段拼接后没有"双份"的 cap 贡献。

**为什么这是必要条件**：

1. 若 cap 项不相消，$S[M_1]+S[M_2]$ 就会多出正比于中间切片的项，而 $S[M]$ 里没有这一项 ⇒ $e^{iS_1}e^{iS_2}\neq e^{iS}$ ⇒ 时间合成失败。
2. 若角点项不相加，两段各带一个"半个角点项"，拼起来会得到 2 倍（或 0 倍）的角点相位 ⇒ 振幅差一个相位 ⇒ 幺正性被破坏。
3. 三件事（cap 相消、GHY 相消、角点相加）一起，才使

$$U_{M_2\circ M_1}=U_{M_2}U_{M_1}$$

成立。论文 (4.2e) 把它当作公理（causal factorization）之一，并在 App C.1 验证改变 cut 不改变振幅。

**检验技巧**：拿到任何一个带边界作用量，先做"两段粘合"的算术。若多出或少了边界项，符号一定错了。这比逐项核对系数快得多。$\square$

</details>

**5.** 计算 Schwarzschild（$\mathrm{d}s^2=-f\mathrm{d}t^2+f^{-1}\mathrm{d}r^2+r^2\mathrm{d}\Omega^2$，$f=1-2G_NM/r$）中 $t=\text{const}$ 切片内二维球面 $S_r$ 的外曲率 $k$，并用 $M_{\rm ADM}=\frac{1}{8\pi G_N}\int\sqrt\sigma(k_0-k)$ 验证它给出 $M$。

<details markdown="1"><summary>点击显示答案</summary>

**切片内的诱导度规**：

$$h_{ij}\mathrm{d}x^i\mathrm{d}x^j=f^{-1}\mathrm{d}r^2+r^2\mathrm{d}\Omega^2 .$$

**单位法矢（在三维切片内，指向 $r$ 增大方向）**：

$$n^i=\sqrt{f}\;\delta^i_r,\qquad h_{ij}n^in^j=f^{-1}\cdot f=1 .$$

**外曲率**：

$$k=\nabla_i n^i=\partial_r n^r+\Gamma^i_{ir}n^r .$$

三维 $\Gamma^i_{ir}=\partial_r\ln\sqrt h$，$\sqrt h=r^2\sqrt{f^{-1}}=r^2/\sqrt f$。于是

$$k=\partial_r\sqrt f+\sqrt f\;\partial_r\ln\frac{r^2}{\sqrt f}
=\frac{f'}{2\sqrt f}+\sqrt f\left(\frac{2}{r}-\frac{f'}{2f}\right)
=\frac{2\sqrt f}{r},$$

其中 $f'=2G_NM/r^2$，两个 $f'$ 项精确相消。

**平直背景**：$M=0$，$f=1$，$k_0=2/r$。

**差值**：

$$k_0-k=\frac{2}{r}\left(1-\sqrt{1-\frac{2G_NM}{r}}\right)
\approx\frac{2}{r}\cdot\frac{G_NM}{r}=\frac{2G_NM}{r^2}\quad(r\gg G_NM).$$

**积分**：$\sqrt\sigma=r^2\sin\theta$，$\int_{S^2}\sqrt\sigma\,\mathrm{d}^2x=4\pi r^2$，

$$M_{\rm ADM}=\frac{1}{8\pi G_N}\cdot4\pi r^2\cdot\frac{2G_NM}{r^2}=M .\qquad\square$$

（严格计算用 $1-\sqrt f$ 的精确值，大 $r$ 极限给 $M$；有限 $r$ 的修正对应 $S_r$ 内包含的引力能量。）

**三个值得记住的点**：

1. **必须减 $k_0$**：$k_0=2/r\neq0$，不减就会得到"平直空间也有质量"。
2. **$k=\frac{2}{r}\sqrt f$ 的形式**：$\sqrt f$ 是"红移因子"，它把固有距离与坐标距离联系起来。这个因子在论文里以 lapse $N$ 的形式出现（(B.1)、(B.3)）。
3. **系数 $\frac{1}{8\pi G_N}$**：与 GHY 项的系数一致。这不是巧合——Brown–York 质量就是 GHY 项在渐近边界上的"变分"，两者是同一个东西的两种写法。

</details>

## 参考

- Wald《General Relativity》附录 E（GHY 项与 Dirichlet 变分原理的严格处理）、第 11 章（ADM 质量）。
- Carroll《Spacetime and Geometry》第 4 章（边界项）、第 6 章（ADM 质量与 Brown–York）。
- Poisson《A Relativist's Toolkit》第 3 章（零边界与 $\Theta$ 的边界项）、第 4 章（Brown–York）。
- Hawking & Horowitz 的 GHY 原始论文（作用量的边界项与量子引力配分函数）。
- Lehner, Myers, Poisson, Sorkin《Null Surfaces and the Action Principle》（零边界项与角点项的标准参考）。
- 论文 arXiv:2611.34924 §3（(3.49)–(3.53) 的 Hamiltonian 形式与角点项）、App B（(B.1)–(B.3)）；第 8 章（$\Theta$ 的几何）、第 12 章（角点荷）、第 13 章（熵）。
