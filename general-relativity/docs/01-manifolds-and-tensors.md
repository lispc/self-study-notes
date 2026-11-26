# 流形与张量：时空作为"舞台"

> 路线图位置：第 1 部分（微分几何工具）· 第 1 章
> 前置知识：多元微积分（偏导、链式法则、隐函数）、线性代数（基、对偶空间、双线性型）；狭义相对论的四维语言（[电动力学书](../../electrodynamics/README.md)相对论章，或先接受 $x^\mu=(t,\vec x)$ 与 $\eta_{\mu\nu}$ 的写法）。
> 学习目标：能说清为什么"时空是流形"而不是 $\mathbb{R}^4$；会用"曲线等价类 / 方向导数"两种方式定义切矢量并证明坐标变换律；会用对偶配对定义余矢量与任意阶张量；会验证张量方程在换坐标下保持形式；会用度规算固有时，并能在 $(-,+,+,+)$ 与 QFT 书的 $(+,-,-,-)$ 之间翻译公式。

---

**单位约定**：本章 $c=1$，暂不出现 $G_N$。度规号差

$$\eta_{ab}=\mathrm{diag}(-,+,+,+).$$

**这是本书与 [QFT 书](../../qft-sm/README.md)相反、与 Wald/Carroll 相同的约定。** 对照规则见 §6，第一次遇到具体公式时也会标注。索引：$\mu,\nu,\rho,\sigma$ 为坐标指标，$a,b,c$ 为标架指标（第 5s 章起大量使用）。

## 1. 一句话总结

**时空是一个四维光滑流形，上面放一个洛伦兹号差的度规。** "流形"保证每一小块都像 $\mathbb{R}^4$、但没有全局优选坐标；"张量"是把"坐标无关的几何对象"写成"分量 + 变换律"的技术；度规把切空间与余切空间配对，给出长度、角度与因果结构。本章建立的全部语言只做一件事：**让"引力 = 时空几何"这句话有精确含义**——几何对象不依赖坐标，方程在换坐标下保持形式，于是"物理定律对所有观测者相同"成为一条数学定理而不是口号。

## 2. 为什么不能就用 $\mathbb{R}^4$

$\mathbb{R}^4$ 自带全局坐标 $(t,x,y,z)$ 与全局平直度规。广义相对论要允许时空弯曲，弯曲的流形**不可能**被一张图卡全局覆盖（球面就不能）。更实际的三条理由：

1. **坐标只是标签**。同一个物理事件在不同观测者眼里有不同坐标；物理定律不能依赖标签。
2. **拓扑可能不平凡**。黑洞时空的 $r=0$ 奇点、Kruskal 延拓的四个区域（第 6 章）都不是 $\mathbb{R}^4$ 的全局图像。
3. **"弯曲"要能与"坐标系选得怪"区分开**。$r=2GM$ 处的"奇异"是坐标造成的（曲率有限），$r=0$ 才是几何奇异（曲率发散）——这个区分只有在"流形 + 张量"的语言里才能说清。

### 2.1 流形的定义（够用版）

四维光滑流形 $M$ 是：一个集合，配一族**图卡** $\{(U_\alpha,\varphi_\alpha)\}$，$\varphi_\alpha:U_\alpha\to\mathbb{R}^4$ 是双射，且

- $\bigcup_\alpha U_\alpha=M$（覆盖）；
- 重叠区 $U_\alpha\cap U_\beta\neq\varnothing$ 上，过渡映射 $\varphi_\beta\circ\varphi_\alpha^{-1}$ 是 $C^\infty$ 的（光滑相容）。

**过渡映射光滑**这一条是关键：它保证"在哪个图卡里做微积分都行"，且结果可以通过链式法则翻译。

### 2.2 坐标与变换

在图卡里写 $x^\mu=(x^0,x^1,x^2,x^3)$。换到另一图卡 $x'^\mu$ 时，

$$x'^\mu=x'^\mu(x^0,\dots,x^3),\qquad
J^\mu{}_\nu\equiv\frac{\partial x'^\mu}{\partial x^\nu},\qquad
\det J\neq0 .$$

之后所有"变换律"都是这条链式法则的化身。

## 3. 曲线与切矢量

### 3.1 两条定义路线

**路线 A（等价类）**：过 $p$ 的两条曲线 $\gamma,\tilde\gamma$（$\gamma(0)=\tilde\gamma(0)=p$）等价，若在某图卡里

$$\left.\frac{\mathrm{d}x^\mu(\gamma(\lambda))}{\mathrm{d}\lambda}\right|_{\lambda=0}
=\left.\frac{\mathrm{d}x^\mu(\tilde\gamma(\lambda))}{\mathrm{d}\lambda}\right|_{\lambda=0}.$$

等价类叫 $p$ 处的**切矢量**。$T_pM$ 是四维矢量空间。

**路线 B（方向导数）**：切矢量 $v$ 是一个作用在光滑函数上的算子

$$v(f)\equiv\left.\frac{\mathrm{d}}{\mathrm{d}\lambda}f(\gamma(\lambda))\right|_{\lambda=0}
=v^\mu\frac{\partial f}{\partial x^\mu},\qquad v^\mu\equiv\left.\frac{\mathrm{d}x^\mu}{\mathrm{d}\lambda}\right|_{\lambda=0}.$$

两条路线等价：$v$ 由分量 $v^\mu$ 唯一确定，而 $v^\mu$ 正是路线 A 的等价类数据。

**路线 B 的好处**：它立刻说明切矢量是坐标无关的对象——"沿这条曲线求方向导数"不需要坐标。分量只是它在某组基下的系数。

### 3.2 坐标基与变换律

$$\boxed{\;e_\mu\equiv\partial_\mu=\frac{\partial}{\partial x^\mu},\qquad v=v^\mu\partial_\mu .\;}$$

换坐标：

$$v'^\mu=\frac{\partial x'^\mu}{\partial x^\nu}v^\nu .$$

**这就是"逆变矢量"**（上指标、用 $J$ 变换）。物理图像：矢量的分量与坐标基"反向"变化——基被拉伸时分量收缩，矢量本身不变。

## 4. 余矢量与张量

### 4.1 余切空间

$T_p^*M$ 是 $T_pM$ 的对偶空间：线性映射 $\omega:T_pM\to\mathbb{R}$。最自然的例子是函数的微分：

$$\mathrm{d}f(v)\equiv v(f)=v^\mu\partial_\mu f .$$

坐标函数的微分 $\mathrm{d}x^\mu$ 构成对偶基：

$$\boxed{\;\mathrm{d}x^\mu\left(\partial_\nu\right)=\delta^\mu{}_\nu .\;}$$

任何余矢量写成 $\omega=\omega_\mu\mathrm{d}x^\mu$，变换律是"协变"：

$$\omega'_\mu=\frac{\partial x^\nu}{\partial x'^\mu}\omega_\nu .$$

### 4.2 配对不变性

$$\omega(v)=\omega_\mu v^\mu=\omega'_\mu v'^\mu .$$

这不是巧合，是 $\mathrm{d}x^\mu(\partial_\nu)=\delta^\mu_\nu$ 与两条变换律互逆（$J^{-1}J=1$）的代数结果。自检 2 给出显式验证。

### 4.3 张量

一个 $(k,l)$ 型张量是多重线性映射

$$T:\underbrace{T_p^*M\times\cdots\times T_p^*M}_{k}\times\underbrace{T_pM\times\cdots\times T_pM}_{l}\to\mathbb{R},$$

分量 $T^{\mu_1\dots\mu_k}{}_{\nu_1\dots\nu_l}$，每个上指标带一个 $J$、每个下指标带一个 $J^{-1}$。

**三条操作**：

- **缩并**：上下指标求和，$T^\mu{}_{\mu}$。
- **对称化/反对称化**：$T_{(\mu\nu)}=\frac12(T_{\mu\nu}+T_{\nu\mu})$、$T_{[\mu\nu]}=\frac12(T_{\mu\nu}-T_{\nu\mu})$。
- **张量积**：$(\alpha\otimes\beta)_{\mu\nu}=\alpha_\mu\beta_\nu$。

**为什么这个"分量 + 变换律"的定义好用**：它把"坐标无关"变成一个可检验的判据——**只要用正确的变换律构造出来的东西就是张量，张量方程在换坐标下自动保持形式**（自检 4）。

## 5. 度规：把切空间与余切空间缝在一起

### 5.1 定义

度规是一个对称、非退化的 $(0,2)$ 张量：

$$g=g_{\mu\nu}\mathrm{d}x^\mu\otimes\mathrm{d}x^\nu,\qquad g_{\mu\nu}=g_{\nu\mu},\qquad \det g\neq0 .$$

**洛伦兹号差**：在每点可以做正交归一化，使 $g$ 的矩阵等于 $\eta=\mathrm{diag}(-,+,+,+)$（本书记为 $\eta_{ab}$，标架指标）。这等价于说"每点有一个光锥"。号差的符号约定是**约定**，不改变物理；$(-,+,+,+)$ 与 $(+,-,-,-)$ 的区别只是把"类时"定义为 $g(v,v)\lt0$ 还是 $\gt0$。

### 5.2 升降指标

$$v_\mu=g_{\mu\nu}v^\nu,\qquad v^\mu=g^{\mu\nu}v_\nu,\qquad g^{\mu\rho}g_{\rho\nu}=\delta^\mu{}_\nu .$$

有了度规，切空间与余切空间可以互相识别，于是"矢量"与"余矢量"在计算中可以混用——但记号上要记住谁原本是谁（梯度 $\partial_\mu f$ 天生是余矢量）。

### 5.3 内积与因果类型

对矢量 $v,w$：

- $g(v,v)\lt0$：**类时**（有质量粒子、观测者）；
- $g(v,v)=0$ 且 $v\neq0$：**类光**（光）；
- $g(v,v)\gt0$：**类空**（同时刻的空间位移）。

$g(v,w)=0$ 叫正交。**注意洛伦兹号差的反直觉之处**：类光矢量与自己正交，且正交于自己的矢量构成的三维空间里还含着自己（第 8 章整章都在处理这个退化性）。

## 6. 与 QFT 书号差的翻译表

QFT 书用 $\eta^{+}=\mathrm{diag}(+1,-1,-1,-1)$。两套约定的关系是 $g^{\rm QFT}=-g^{\rm GR}$。翻译规则（**不是**简单的整体加负号）：

| 对象 | 变换 |
|---|---|
| $g_{\mu\nu}$、$g^{\mu\nu}$ | 乘 $-1$ |
| $\Gamma^\mu_{\nu\rho}$ | **不变**（$g^{-1}$ 与 $\partial g$ 各变号，相消） |
| $R^\mu{}_{\nu\rho\sigma}$、$R_{\mu\nu}$、$G_{\mu\nu}$ | **不变** |
| 标量曲率 $R=g^{\mu\nu}R_{\mu\nu}$ | 乘 $-1$ |
| $\Box=g^{\mu\nu}\nabla_\mu\nabla_\nu$ | 乘 $-1$ |
| $T_{\mu\nu}$ | **不变**（$G_{\mu\nu}=8\pi GT_{\mu\nu}$ 两边一致） |
| 质量壳条件 | $p^\mu p_\mu=-m^2$（GR） vs $p^\mu p_\mu=+m^2$（QFT） |
| 类时条件 | $v^2\lt0$（GR） vs $v^2\gt0$（QFT） |

**记忆法**：只含"一个度规"的量变号；含"两个度规"或"度规与其逆各一次"的量不变。$R=g^{\mu\nu}R_{\mu\nu}$ 是"一个逆度规" ⇒ 变号；$G_{\mu\nu}=R_{\mu\nu}-\frac12Rg_{\mu\nu}$ 是"$R$ 变号 × $g$ 变号" ⇒ 不变。

## 7. 固有时：时钟读数的几何定义

### 7.1 定义

沿类时曲线 $\gamma(\lambda)$，**固有时**

$$\boxed{\;\mathrm{d}\tau^2=-g_{\mu\nu}\frac{\mathrm{d}x^\mu}{\mathrm{d}\lambda}\frac{\mathrm{d}x^\nu}{\mathrm{d}\lambda}\mathrm{d}\lambda^2
=-g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu .\;}$$

它等于随曲线运动的钟所读的时间。**这是广义相对论里"时间"的全部内容**：没有全局时间，只有沿世界线的固有时。

### 7.2 例子：匀速圆周运动

在 Minkowski 中，角速度 $\omega$、半径 $R$ 的圆周运动：

$$x^\mu(t)=(t,R\cos\omega t,R\sin\omega t,0),\qquad
\mathrm{d}\tau^2=\left(1-\omega^2R^2\right)\mathrm{d}t^2 .$$

所以

$$\tau=\sqrt{1-v^2}\,t,\qquad v=\omega R .$$

**"运动的钟走得慢"** 在这里是纯几何：$\mathrm{d}\tau/\mathrm{d}t=\sqrt{1-v^2}\lt1$。

### 7.3 与论文的接口

论文的"引力时钟"就是这条定义的推广：在零锥上，仿射参数 $u$ 沿生成元从 cap 走到角点，读数就是固有时的一种（对零曲线用仿射参数而非 $\tau$）。第 8 章的 $\varrho\le u$ 与第 12 章的 boost 荷，都建立在"时钟读数 = 沿曲线的几何量"这个第 1 章的定义上。

## 8. 张量方程为什么"处处成立"

这是本章最实用的一条技能。设 $T^{\mu\nu}$ 是张量，在某图卡里 $T^{\mu\nu}=0$。换到另一图卡：

$$T'^{\mu\nu}=J^\mu{}_\alpha J^\nu{}_\beta T^{\alpha\beta}=0 .$$

所以"在某组坐标里为零"等价于"在这个张量有定义的每点为零"。推论：

1. **方程只要在一组坐标里成立，就在所有坐标里成立**——这就是"物理定律与坐标系无关"的数学内容。
2. **可以挑最方便的坐标证明**（例如取局部正交归一架，使 $g_{\mu\nu}=\eta_{\mu\nu}$、$\Gamma=0$），结论自动对一般坐标成立。第 3 章算曲率、第 5 章推 Einstein 方程都靠这一招。
3. **反过来**：如果一个"方程"只在某组坐标里成立、换坐标后多出项，那它就不是张量方程（$\partial_\nu v^\mu=0$ 是典型例子，第 2 章会看到）。

## 9. 小结

- 时空 = 四维光滑流形 + 洛伦兹度规；图卡与过渡映射让"局部像 $\mathbb{R}^4$"精确化。
- 切矢量 = 曲线的等价类 = 方向导数 $v^\mu\partial_\mu$；变换律 $v'^\mu=J^\mu{}_\nu v^\nu$。
- 余矢量 = 线性函数，对偶基 $\mathrm{d}x^\mu(\partial_\nu)=\delta^\mu{}_\nu$；变换律用 $J^{-1}$。
- 张量 = 多重线性映射；缩并、对称化、张量积；张量方程换坐标不变。
- 度规 $g_{\mu\nu}$ 对称非退化，号差 $(-,+,+,+)$；升降指标、内积、因果分类。
- 与 QFT 书翻译：只含一个度规的量变号，含"度规 × 逆度规"的量不变。
- 固有时 $\mathrm{d}\tau^2=-g_{\mu\nu}\mathrm{d}x^\mu\mathrm{d}x^\nu$ 是时钟读数的几何定义；圆周运动给出 $\mathrm{d}\tau=\sqrt{1-v^2}\mathrm{d}t$。
- "在某组坐标里为零 ⇒ 处处为零"是广义相对论里最常用的证明技巧。

## 自检问题

**1.** 用"方向导数"定义切矢量，证明分量变换律 $v'^\mu=\frac{\partial x'^\mu}{\partial x^\nu}v^\nu$；并说明为什么这个证明说明切矢量是坐标无关的对象。

<details markdown="1"><summary>点击显示答案</summary>

设 $v$ 是 $p$ 处的切矢量，沿曲线 $\gamma(\lambda)$，$v^\mu=\mathrm{d}x^\mu/\mathrm{d}\lambda|_0$。在另一组坐标 $x'$ 里，同一条曲线写成 $x'^\mu(\lambda)=x'^\mu(x(\lambda))$，故

$$v'^\mu=\left.\frac{\mathrm{d}x'^\mu(\gamma(\lambda))}{\mathrm{d}\lambda}\right|_{0}
=\left.\frac{\partial x'^\mu}{\partial x^\nu}\right|_{\gamma(0)}\left.\frac{\mathrm{d}x^\nu}{\mathrm{d}\lambda}\right|_{0}
=\frac{\partial x'^\mu}{\partial x^\nu}v^\nu .\qquad\square$$

（链式法则，一步到位。）

**为什么这说明坐标无关**：换一个角度——把 $v$ 看作算子 $v=v^\mu\partial_\mu$，作用在函数 $f$ 上：

$$v(f)=v^\mu\frac{\partial f}{\partial x^\mu}=v'^\mu\frac{\partial f}{\partial x'^\mu} .$$

右边是同一个数（沿曲线求导不依赖坐标）。于是

$$v'^\mu\frac{\partial f}{\partial x'^\mu}
=v^\mu\frac{\partial x'^\nu}{\partial x^\mu}\frac{\partial f}{\partial x'^\nu}
\;\Longrightarrow\;
v'^\nu=v^\mu\frac{\partial x'^\nu}{\partial x^\mu},$$

因为上式对所有 $f$ 成立，故 $\partial f/\partial x'^\nu$ 的系数必须相等。

**两层含义**：

1. **对象是坐标无关的**：$v(f)$ 是一个数，与坐标无关；$v$ 作为"求方向导数"的规则也是坐标无关的。
2. **分量是坐标相关的**：$(v^\mu)$ 随坐标按 $J$ 变换，但整体对象不变。这就是"张量 = 几何对象 + 分量变换律"的含义。

**反过来检验**：如果某个数组 $w^\mu$ 换坐标时不按 $J$ 变换（比如 $w^\mu=\partial^\mu f$ 在某些约定下），它就不是矢量。第 2 章会用这个判据证明"偏导数 $\partial_\nu v^\mu$ 不是张量"。$\square$

</details>

**2.** 证明对偶配对 $\omega(v)=\omega_\mu v^\mu$ 在换坐标下不变，并写出 $\omega_\mu$ 的变换律。

<details markdown="1"><summary>点击显示答案</summary>

**变换律**：$\omega=\omega_\mu\mathrm{d}x^\mu$ 是坐标无关的对象，而 $\mathrm{d}x'^\mu=\frac{\partial x'^\mu}{\partial x^\nu}\mathrm{d}x^\nu$。于是

$$\omega=\omega'_\mu\mathrm{d}x'^\mu=\omega'_\mu\frac{\partial x'^\mu}{\partial x^\nu}\mathrm{d}x^\nu
\;\Longrightarrow\;
\omega_\nu=\omega'_\mu\frac{\partial x'^\mu}{\partial x^\nu},$$

解出（用 $J$ 与 $J^{-1}$ 互逆）

$$\boxed{\;\omega'_\mu=\frac{\partial x^\nu}{\partial x'^\mu}\omega_\nu\;.}\qquad\square$$

**配对不变**：

$$\omega'(v')=\omega'_\mu v'^\mu
=\frac{\partial x^\nu}{\partial x'^\mu}\omega_\nu\cdot\frac{\partial x'^\mu}{\partial x^\rho}v^\rho
=\delta^\nu{}_\rho\,\omega_\nu v^\rho
=\omega_\nu v^\nu=\omega(v).\qquad\square$$

（用了 $\frac{\partial x^\nu}{\partial x'^\mu}\frac{\partial x'^\mu}{\partial x^\rho}=\frac{\partial x^\nu}{\partial x^\rho}=\delta^\nu{}_\rho$。）

**要点**：配对的"不变性"与两条变换律的"互逆性"是同一件事。这就是为什么余矢量的变换律必须是 $J^{-1}$ 而不是 $J$——否则 $\omega(v)$ 会随坐标变化，那它就不是"线性函数"而是一个依赖于坐标的数组。

**一个常见陷阱**：梯度 $\partial_\mu f$ 的变换律是

$$\partial'_\mu f=\frac{\partial x^\nu}{\partial x'^\mu}\partial_\nu f,$$

恰好是协变的。但它**不是**余矢量的"构造"，而是余矢量的一个例子：$\mathrm{d}f=\partial_\mu f\,\mathrm{d}x^\mu$ 是坐标无关的 1-形式，$\partial_\mu f$ 只是它的分量。这两句话的区别在计算里会救命（第 2 章的 $\partial_\nu v^\mu$ 正是把"分量"误当"张量"）。$\square$

</details>

**3.** 在 Minkowski 中，一个观测者沿半径 $R$ 的圆以角速度 $\omega$ 运动。算出他的固有时与坐标时的关系；再算出他绕一圈回到原处时，与留在原点的钟相比慢了多少。取 $R=1$、$\omega=0.6$（$c=1$），给数值。

<details markdown="1"><summary>点击显示答案</summary>

**世界线**：

$$t=\lambda,\quad x=R\cos\omega\lambda,\quad y=R\sin\omega\lambda .$$

速度 $\dot x=-\omega R\sin\omega t$、$\dot y=\omega R\cos\omega t$，故 $\dot x^2+\dot y^2=\omega^2R^2$，而

$$\mathrm{d}\tau^2=-\left(-\mathrm{d}t^2+\mathrm{d}x^2+\mathrm{d}y^2\right)=\left(1-\omega^2R^2\right)\mathrm{d}t^2 .$$

所以

$$\boxed{\frac{\mathrm{d}\tau}{\mathrm{d}t}=\sqrt{1-\omega^2R^2}
=\sqrt{1-v^2},\qquad v=\omega R .}\qquad\square$$

**一圈的对比**：坐标时一圈 $T=2\pi/\omega$，固有时 $\tau=\sqrt{1-v^2}\,T$。差值

$$\Delta=T-\tau=T\left(1-\sqrt{1-v^2}\right)\approx T\cdot\frac{v^2}{2}\quad(v\ll1).$$

**数值**：$R=1$、$\omega=0.6$ ⇒ $v=0.6$，$\sqrt{1-0.36}=0.8$。一圈坐标时 $T=2\pi/0.6\approx10.472$，固有时 $\tau=0.8T\approx8.377$，所以运动的钟比原点的钟**少走** $2.095$（同样的时间单位）。$\square$

**物理解读与警告**：

- 这不是"运动使钟变慢"的动力学效应，而是两条世界线在 Minkowski 度规下的**长度不同**：圆周世界线的"长度"（固有时）比直线的短。
- 圆周运动的观测者有加速度（向心加速度 $v^2/R$），而原点的观测者没有。所以这不是"对称的双生子佯谬"——两个观测者的处境本来就不对称，谁加速谁的世界线短。
- 在广义相对论里，这个几何事实会与引力红移合流：**固有时沿世界线积分**，没有"全局时间"可以比较（第 6 章的 Schwarzschild 里，$r$ 不同的静止观测者有不同的 $\mathrm{d}\tau/\mathrm{d}t$）。

</details>

**4.** 说明"若张量 $T^{\mu\nu}$ 在某组坐标里全为零，则在任意坐标里全为零"，并用它证明：如果 $g_{\mu\nu}$ 在某点可以化为 $\eta_{\mu\nu}$，那么 $g^{\mu\nu}$ 在同一点就是 $\eta^{\mu\nu}$。

<details markdown="1"><summary>点击显示答案</summary>

**第一部分**：$T'^{\mu\nu}=\frac{\partial x'^\mu}{\partial x^\alpha}\frac{\partial x'^\nu}{\partial x^\beta}T^{\alpha\beta}$。若 $T^{\alpha\beta}=0$（所有分量），右边是零的和，故 $T'^{\mu\nu}=0$。逆命题同理（用 $J^{-1}$）。$\square$

**第二部分**：设某点存在坐标使 $g_{\mu\nu}=\eta_{\mu\nu}$。矩阵等式 $g^{\mu\rho}g_{\rho\nu}=\delta^\mu{}_\nu$ 是张量方程（两边都是张量）。在这组坐标里，它变成矩阵方程

$$g^{\mu\rho}\eta_{\rho\nu}=\delta^\mu{}_\nu .$$

记矩阵 $G=(g^{\mu\rho})$、$H=(\eta_{\rho\nu})$，则 $GH=I$，故 $G=H^{-1}=\eta^{-1}$。而 $\eta^{-1}$ 的分量恰好是 $\eta^{\mu\nu}$（因为 $\eta^{\mu\rho}\eta_{\rho\nu}=\delta^\mu{}_\nu$）。所以

$$g^{\mu\nu}=\eta^{\mu\nu}\quad\text{在这组坐标里}.$$

由于"$g^{\mu\nu}-\eta^{\mu\nu}=0$"在**某一组**坐标里成立，而 $g^{\mu\nu}-\eta^{\mu\nu}$ 是张量（两个张量之差），由第一部分知它在任意坐标里为零——但要注意 $\eta^{\mu\nu}$ 是**常张量**还是**坐标相关的数组**：在这里 $\eta^{\mu\nu}$ 指"在选定标架下的分量"，所以正确的表述是"$g^{\mu\nu}$ 的矩阵是 $\eta$ 的逆矩阵"，与坐标无关。$\square$

**这个技巧的用途**：

1. **局部惯性系**：每点都能选标架使 $g=\eta$、$\Gamma=0$（黎曼法坐标），于是"曲率是二阶导数"这件事在这一点上看得最清楚（第 3 章）。
2. **张量方程的"点wise"证明**：想证明某个张量恒等式，只需在一点取局部惯性系验证，结论对所有点成立。
3. **反面**：如果一个等式只在特定坐标里成立（比如 $\Gamma^\mu_{\nu\rho}=0$），它不构成张量方程，换坐标就破坏——这是"局部惯性系不能全局化"的精确含义。

</details>

**5.** 用 §6 的规则，把 QFT 书里的 Klein–Gordon 方程 $(\Box+m^2)\phi=0$（$\eta^{+}=\mathrm{diag}(+,-,-,-)$）翻译成本书的号差，并验证在本书约定下平面波解 $e^{-ip\cdot x}$ 满足的色散关系。

<details markdown="1"><summary>点击显示答案</summary>

**翻译**：$\Box^{+}=g_+^{\mu\nu}\partial_\mu\partial_\nu$。因为 $g_+=-g_{\rm GR}$，有

$$\Box^{+}=-\Box^{\rm GR}.$$

所以 $(\Box^{+}+m^2)\phi=0$ 翻译成

$$\boxed{\left(-\Box^{\rm GR}+m^2\right)\phi=0
\;\Longleftrightarrow\;
\left(\Box^{\rm GR}-m^2\right)\phi=0\;}$$

即 $\Box\phi=m^2\phi$。$\square$

**验证平面波**：取 $\phi=e^{-ip_\mu x^\mu}=e^{-i(p_0t-\vec p\cdot\vec x)}$，$\partial_\mu\phi=-ip_\mu\phi$，故

$$\Box^{\rm GR}\phi=g^{\mu\nu}(-ip_\mu)(-ip_\nu)\phi=-p^\mu p_\mu\,\phi .$$

方程 $\Box\phi=m^2\phi$ 给

$$-p^\mu p_\mu=m^2\;\Longleftrightarrow\;p^\mu p_\mu=-m^2 .$$

在 $(-,+,+,+)$ 下，$p^\mu=(E,\vec p)$，$p^\mu p_\mu=-E^2+\vec p^2$，于是

$$-E^2+\vec p^2=-m^2\;\Longleftrightarrow\;E^2=\vec p^2+m^2 .\qquad\square$$

**与 QFT 书对照**：QFT 书里 $p^\mu p_\mu=+m^2$ 且 $p^2=E^2-\vec p^2$，同样给 $E^2=\vec p^2+m^2$。**同一个物理，两种写法。**

**三个容易踩的点**：

1. **$\Box$ 变号，$m^2$ 不变号**：质量是标量参数，与号差无关。
2. **$p^\mu p_\mu$ 的符号**：类时动量在 GR 约定下 $p^2\lt0$，在 QFT 约定下 $p^2\gt0$。读到"$p^2=-m^2$"时先看号差约定，不要以为出了错。
3. **传播子**：$1/(p^2+m^2)$ vs $1/(p^2-m^2)$——两种约定下形式不同，但极点位置（$E=\pm\sqrt{\vec p^2+m^2}$）相同。第 5 章的 Einstein 方程与第 9 阶段的单圈计算都要求先对齐这一条。

**一条元规则**：换号差时，逐个公式数"度规出现了几次"——奇数次的量变号，偶数次的不变。这条规则对 $\epsilon$ 张量、$\star$、$\delta$ 函数都成立（$\epsilon$ 的号随 $\sqrt{-g}$ 变，第 4 章会用到）。$\square$

</details>

## 参考

- Wald《General Relativity》第 2 章（流形、矢量、张量、度规）、附录 B（号差与符号约定的对照）。
- Carroll《Spacetime and Geometry》第 1–2 章（最平易的入门；本章的叙述节奏与它接近）、附录 G（号差约定）。
- Hawking & Ellis《The Large Scale Structure of Space-Time》第 2 章（流形的严格处理，选读）。
- Nakahara《Geometry, Topology and Physics》第 5 章（流形与切丛的数学细节，选读）。
- [电动力学书](../../electrodynamics/README.md)相对论章（四维语言的第一步）；[QFT 书 stage-03](../../qft-sm/docs/stage-03-relativistic-qm/01-klein-gordon-and-dirac.md)（Klein–Gordon 与号差约定的源头）。
- 论文 arXiv:2611.34924 §3.1（时空指标与内部指标的分工，第 5s 章展开）。
