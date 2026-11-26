# 相空间路径积分与算符排序：中点规则的来历

> 路线图位置：第 4 阶段（QFT 核心）· 第 7 篇（路径积分）的补充材料（第 07s 篇），在 07 篇与量子力学书 03s2 之后读
> 前置知识：07 篇（切片推导、$Z[J]$、高斯积分、Wick 定理）；量子力学书 03s2（Weyl 排序、Wigner 函数、Moyal 星积）、03 篇（传播子与路径积分的量子力学版）。
> 学习目标：会写出相空间路径积分的格点定义并说明"为什么必须指定离散化"；能证明中点规则对应 Weyl 排序、端点规则对应另一种排序；会从路径积分的变量平移推出 Schwinger–Dyson 方程并识别其中的接触项；知道场论版与论文 (4.20)–(4.28) 的对应。

---

**单位约定**：本篇保留 $\hbar$（它是主角，排序问题只在 $\hbar \neq 0$ 时有意义）；其余记号与第 4 阶段一致。

## 1. 一句话总结

**路径积分不是一条公式，而是一族定义：相空间形式 $\int\mathcal{D}q\,\mathcal{D}p\,e^{\frac{\mathrm{i}}{\hbar}\int(p\dot q - H)}$ 在格点上必须指定 $H$ 取在路径的哪一点，不同取法给出不同的算符排序——中点规则对应 Weyl 排序，端点规则对应 $f(q)p$ 或 $p f(q)$。排序的差异在 $\hbar\to0$ 时消失，在有限 $\hbar$ 时表现为 $O(\hbar)$ 的有效势；而路径积分对场的平移不变性给出 Schwinger–Dyson 方程，其右端的 $\delta$ 函数就是算符形式里的接触项（等时对易子）。这两件事是"路径积分 = 算符量子化"的全部内容。**

## 2. 为什么路径积分需要"排序说明书"

### 2.1 07 篇的推导回顾

07 篇从量子力学的切片出发：

$$\langle q_f|e^{-\mathrm{i}\hat Ht/\hbar}|q_i\rangle = \lim_{N\to\infty}\int\prod_{k=1}^{N-1}\mathrm{d}q_k\prod_{k=1}^{N}\frac{\mathrm{d}p_k}{2\pi\hbar}\;e^{\frac{\mathrm{i}}{\hbar}\sum_k\left[p_k(q_k-q_{k-1}) - \epsilon H(p_k,\bar q_k)\right]}.$$

那里 $\bar q_k$ 取的是中点 $(q_k+q_{k-1})/2$——但推导里**没有解释为什么**。对 $H = p^2/2m + V(q)$，这一步无关紧要（理由见 §4.3）；对一般的 $H(q,p)$，它是**量子理论的唯一选择点**。

### 2.2 排序问题藏在哪里

算符形式里，$\hat H$ 是 $q,p$ 的何种排序，决定了传播子。路径积分把 $\hat H$ 换成了 c-数函数 $H(q,p)$——**这个替换丢掉了排序信息**。要把它恢复，就必须指定"用路径上的哪个点去取 $H$ 的值"：

- 取左端点 $q_{k-1}$：对应一种排序；
- 取右端点 $q_k$：对应另一种排序；
- 取中点 $\bar q_k$：对应 Weyl 排序。

三种规则在 $\epsilon\to0$ 时的差别是 $O(\hbar)$ 的势——恰恰是排序的物理内容。

### 2.3 一个立刻能感到不对的例子

设 $H = f(q)p$（例如带电粒子在矢势中的 $p\cdot A(q)$ 项）。经典上 $f(q)p = p f(q)$；量子上

$$\hat f\hat p - \hat p\hat f = \mathrm{i}\hbar f'(q) \neq 0.$$

若路径积分不指定离散化，"$\int\mathcal{D}q\mathcal{D}p\,e^{\mathrm{i}\int f(q)p}$"这句话就没有定义。**相空间路径积分的定义必须包含离散化方案。**

## 3. 相空间路径积分的格点定义

### 3.1 定义

$$\langle q_f|e^{-\mathrm{i}\hat Ht/\hbar}|q_i\rangle = \lim_{N\to\infty}\int\prod_{k=1}^{N-1}\mathrm{d}q_k\prod_{k=1}^{N}\frac{\mathrm{d}p_k}{2\pi\hbar}\;\exp\left\{\frac{\mathrm{i}\epsilon}{\hbar}\sum_{k=1}^{N}\left[\frac{p_k(q_k-q_{k-1})}{\epsilon} - H\left(p_k,\bar q_k\right)\right]\right\},$$

其中 $\bar q_k$ 是离散化规则指定的点。相空间体积元 $\mathrm{d}q\,\mathrm{d}p/(2\pi\hbar)$ 本身由"每个量子态占 $2\pi\hbar$ 的相面积"固定（第 10 章作用量–角变量），不随离散化改变。

### 3.2 三种规则

$$\bar q_k = q_{k-1}\ (\text{左}),\qquad \bar q_k = q_k\ (\text{右}),\qquad \bar q_k = \frac{q_k+q_{k-1}}{2}\ (\text{中点}).$$

### 3.3 为什么中点是"自然"的

三条理由，层层递进：

1. **对称性**：$p$ 与 $q$ 在相空间里地位对等，中点不偏向任何一端；
2. **几何**：$p_k(q_k-q_{k-1})$ 是相图上小线段的"面积"，中点是这条线段的中点；
3. **量子**：只有中点规则能在所有阶上复现 Weyl 排序（§4）——而 Weyl 排序正是保持相空间对称性的排序（量子力学书 03s2）。

## 4. 三种规则 ↔ 三种排序

### 4.1 工具：算符的坐标核

对 $H = f(q)p$，三种排序的核（用 $\langle q'|p|q\rangle = -\mathrm{i}\hbar\,\partial_{q'}\delta(q'-q)$）：

$$H = f p:\quad \langle q'|H|q\rangle = -\mathrm{i}\hbar\,f(q')\partial_{q'}\delta,$$

$$H = p f:\quad \langle q'|H|q\rangle = -\mathrm{i}\hbar\,\partial_{q'}\left[f(q')\delta\right] = -\mathrm{i}\hbar\left[f'\delta + f\partial_{q'}\delta\right],$$

$$H_{\mathrm{Weyl}} = \tfrac12(fp+pf):\quad \langle q'|H_{\mathrm{Weyl}}|q\rangle = -\mathrm{i}\hbar\left[f\partial_{q'}\delta + \tfrac12 f'\delta\right].$$

### 4.2 规则与核的对应

路径积分的一阶核是

$$\langle q'|e^{-\mathrm{i}\epsilon\hat H/\hbar}|q\rangle \approx \delta(q'-q) - \frac{\mathrm{i}\epsilon}{\hbar}\langle q'|H|q\rangle,$$

而格点积分的一阶展开是

$$\int\frac{\mathrm{d}p}{2\pi\hbar}\,e^{\mathrm{i}p(q'-q)/\hbar}\left[1 - \frac{\mathrm{i}\epsilon}{\hbar}H(p,\bar q)\right].$$

对 $H = f(q)p$，$\int\frac{\mathrm{d}p}{2\pi\hbar}e^{\mathrm{i}p\eta}p = -\mathrm{i}\hbar\partial_\eta\delta(\eta)$（$\eta = q'-q$）。三种规则的区别只在 $f$ 的取值点：

- 中点：$f(\bar q) = f(q') - \frac{\eta}{2}f'(q')$，而 $\eta\,\partial_\eta\delta = -\delta$，故核 $= -\mathrm{i}\hbar[f\partial\delta + \frac12f'\delta]$——**正是 Weyl 排序**；
- 左端点 $\bar q = q = q' - \eta$：$f = f(q') - \eta f'$，核 $= -\mathrm{i}\hbar[f\partial\delta + f'\delta]$——**正是 $p f$**；
- 右端点 $\bar q = q'$：核 $= -\mathrm{i}\hbar f\partial\delta$——**正是 $f p$**。

（完整一阶计算见自检 2。）结论：

| 离散化 | 排序 |
|---|---|
| 中点 $\frac{q_k+q_{k-1}}{2}$ | Weyl $\frac12(fp+pf)$ |
| 左端点 $q_{k-1}$ | $pf$ |
| 右端点 $q_k$ | $fp$ |

### 4.3 一般定理与"什么时候无所谓"

**定理**（陈述）：对多项式 $H(q,p)$，中点规则逐阶（在 $\epsilon\to0$ 的极限中）复现 Weyl 排序的算符；端点规则复现相应的左/右排序。证明思路是对 BCH 逐阶匹配——每一阶的偏差都被下一阶的 $p$ 积分抵消（自检 2 是一阶的完整演示）。

**可分离的 $H = \frac{p^2}{2m} + V(q)$ 为什么无所谓**：$V$ 与 $p$ 无关，三种规则取 $V(\bar q)$ 的差别是

$$\epsilon\sum_k\left[V(q_k) - V(q_{k-1})\right] \approx \int\mathrm{d}t\;\dot q\,V'(q) = \int\mathrm{d}t\;\frac{\mathrm{d}V}{\mathrm{d}t},$$

一个**全导数**，不改变运动方程与振幅（自检 3）。所以标准教材里"路径积分"从不提排序——它们只处理可分离的 $H$；一旦出现 $f(q)p$（规范场的 $p\cdot A$、引力里的交叉项），排序就必须交代。

### 4.4 物理后果

三种量子理论差一个 $O(\hbar)$ 的势。对 $H = f(q)p$，Weyl 与 $fp$ 的哈密顿量相差 $-\frac{\mathrm{i}\hbar}{2}f'$（厄米化后是 $-\frac{\hbar^2}{4}f''$ 型修正）——**能谱会移动**。这不是"数学细节"，是可以被实验区分的物理：不同的离散化 = 不同的量子理论。

## 5. 积掉 $p$：回到构型空间

### 5.1 高斯积分

对 $H = p^2/2m + V(q)$，对每个 $p_k$ 做 Fresnel 积分：

$$\int\frac{\mathrm{d}p}{2\pi\hbar}\exp\left\{\frac{\mathrm{i}}{\hbar}\left[p\,\Delta q - \frac{\epsilon p^2}{2m}\right]\right\} = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\epsilon}}\;\exp\left\{\frac{\mathrm{i}m(\Delta q)^2}{2\hbar\epsilon}\right\}.$$

代回格点式，得到标准的构型空间路径积分（自检 1）：

$$\langle q_f|e^{-\mathrm{i}\hat Ht/\hbar}|q_i\rangle = \int\mathcal{D}q\;\exp\left\{\frac{\mathrm{i}}{\hbar}\int\mathrm{d}t\left[\frac{m\dot q^2}{2} - V(q)\right]\right\},$$

测度里的 $\sqrt{m/(2\pi\mathrm{i}\hbar\epsilon)}$ 每层一个，拼成路径积分的归一化因子。

### 5.2 测度与 van Vleck 行列式

多层高斯积分的 prefactor 在一般情形下是 van Vleck–Morette 行列式 $\left(\det\frac{\partial^2S}{\partial q_f\partial q_i}\right)^{1/2}$——它是"半经典传播子的振幅"，也是第 11 章 $S$ 的二哥。对自由粒子直接可算（自检 1）。

### 5.3 什么时候不能积掉 $p$

- $H$ 对 $p$ 非二次：如相对论粒子 $H = \sqrt{p^2+m^2}$，积掉 $p$ 得到的是一个非局域的、没有简单形式的"拉氏量"；
- 费米子：Grassmann 变量没有"高斯积分到构型空间"的简单版本，相空间形式更自然；
- 约束系统：规范理论的一类约束、$p_0$ 缺失等，只有相空间形式能正确处理（理论力学书第 12 章）；
- 引力：没有全局时间，"$\int\mathcal{D}g\,\mathcal{D}\pi$"的相空间形式是唯一能定义哈密顿约束量子化的语言（第 9 阶段）。

## 6. 变分与接触项

### 6.1 变量平移不变性

路径积分的测度在平移 $\varphi\to\varphi+\delta\varphi$ 下不变（形式上），因此全导数积分为零：

$$0 = \int\mathcal{D}\varphi\;\frac{\delta}{\delta\varphi(x)}\left[e^{\mathrm{i}S[\varphi]+\mathrm{i}\int J\varphi}\right].$$

这里"全导数积分为零"就是**路径积分版的边界条件为零**；如果平移在边界上不为零，就会留下边界项——这正是第 9 阶段边缘模的来源。

### 6.2 Schwinger–Dyson 方程

把导数算出来：

$$0 = \int\mathcal{D}\varphi\;\mathrm{i}\left[\frac{\delta S}{\delta\varphi(x)} + J(x)\right]e^{\mathrm{i}S+\mathrm{i}\int J\varphi} \;\Longrightarrow\; \left\langle\frac{\delta S}{\delta\varphi(x)} + J(x)\right\rangle_J = 0.$$

这就是 **Schwinger–Dyson 方程**。它是"路径积分 = 算符运动方程"的精确表达：期望值满足运动方程，右端多一个源。

对自由标量场 $S = \int\left[\frac12(\partial\varphi)^2 - \frac12m^2\varphi^2\right]$，$\delta S/\delta\varphi = -(\Box+m^2)\varphi$：

$$(\Box+m^2)\langle\varphi(x)\rangle_J = J(x).$$

对 $J$ 再求一次变分，得到两点函数满足

$$(\Box_x+m^2)\langle T\varphi(x)\varphi(y)\rangle = -\mathrm{i}\delta^4(x-y)$$

（本书传播子约定，见 02 篇；完整推导见自检 4）。右端的 $\delta^4$ 不是"发散"，是**接触项**。

### 6.3 接触项的两种读法

- **算符读法**：$\langle T\varphi(x)\varphi(y)\rangle$ 的时间导数在 $t_x = t_y$ 处有跳跃，跳跃值 = 等时对易子 $[\varphi,\dot\varphi] = \mathrm{i}\delta^3$，于是二阶导数出现 $\delta(t_x-t_y)\delta^3 = \delta^4$（自检 5）；
- **路径积分读法**：源 $J$ 的二阶变分直接产生 $\delta$（因为 $\delta J(x)/\delta J(y) = \delta^4(x-y)$），无需单独讨论等时对易子。

两种读法给出同一个结果——**路径积分把等时对易子"自动"包含进了接触项**。这就是为什么在路径积分里算关联函数时"不用管算符排序"：排序信息全部藏在离散化与接触项里。

## 7. 场论版与论文接口

### 7.1 场的相空间积分

把 $(q,p)$ 换成 $(\varphi,\pi)$：

$$\int\mathcal{D}\varphi\,\mathcal{D}\pi\;e^{\frac{\mathrm{i}}{\hbar}\int\mathrm{d}^4x\left[\pi\dot\varphi - \mathcal H(\pi,\varphi)\right]}.$$

中点规则在每一点、每个方向上取 $\bar\varphi = (\varphi_k+\varphi_{k-1})/2$，对应**场的 Weyl 排序**。源与算符插入的排序由此固定。

### 7.2 Weyl 关系与论文 (4.20)

场的 Weyl 算符满足

$$D(\lambda)D(\lambda') = e^{-\frac{\mathrm{i}\hbar}{2}\lambda_I J^{IJ}\lambda'_J}\,D(\lambda+\lambda'),$$

其中 $J^{IJ}$ 是约化辛形式的逆。这正是论文 (4.20) 的 Weyl 关系；它保证"先加源、再变分"与"先排序、再算符"给出同一结果。

### 7.3 双重源变分与接触项；论文 (4.28)

论文 (4.28) 把 $\partial_j^2(U_0^\dagger U_j)|_{j=0}$ 写成两项：

$$\frac{\mathrm{i}}{\hbar}\int\mathrm{d}t\;\hat O_{2,I}(t) - \frac{1}{\hbar^2}\int_{t \gt s}\mathrm{d}t\,\mathrm{d}s\;\hat O_{1,I}(t)\hat O_{1,I}(s),$$

第一项 $\hat O_2 = Q(\partial_j^2H_c)|_0$ 就是**接触项**：源在同一个时刻变分两次。路径积分里它是 $\delta^4(x-y)$ 型项，算符形式里它是排序修正（Weyl 的 $O(\hbar^2)$ 项）。附录 C.2 用 $\star$ 积的展开逐阶组织这些项——与本篇 §6 的两种读法完全对应。

## 8. 小结

- 相空间路径积分的定义必须指定 $H$ 的取值点：中点 → Weyl 排序，左端点 → $pf$，右端点 → $fp$；三种理论差 $O(\hbar)$ 有效势。
- 可分离的 $H = p^2/2m + V$ 对离散化不敏感（差别是全导数）；一旦有 $f(q)p$ 型交叉项，排序就是物理。
- 积掉 $p$ 得到构型空间路径积分与 van Vleck 行列式；非二次 $H$、费米子、约束系统与引力只能留在相空间形式里。
- 变量平移不变性给出 Schwinger–Dyson 方程 $\langle\delta S/\delta\varphi + J\rangle = 0$；自由场给出 $(\Box+m^2)\langle T\varphi\varphi\rangle = -\mathrm{i}\delta^4$。
- 接触项有两种等价读法：等时对易子的跳跃（算符）与源的二阶变分（路径积分）；论文 (4.28) 的 $\hat O_2$ 就是它。

## 自检问题

**1.** 从相空间格点积分积掉 $p$，推出构型空间路径积分与测度；对自由粒子算出 van Vleck 行列式。

<details markdown="1"><summary>点击显示答案</summary>

单层积分：

$$\int\frac{\mathrm{d}p}{2\pi\hbar}\exp\left\{\frac{\mathrm{i}}{\hbar}\left[p(q_k-q_{k-1}) - \frac{\epsilon p^2}{2m}\right]\right\}.$$

配方：$-\frac{\epsilon}{2m}p^2 + \Delta q\,p = -\frac{\epsilon}{2m}\left(p - \frac{m\Delta q}{\epsilon}\right)^2 + \frac{m(\Delta q)^2}{2\epsilon}$。于是

$$= e^{\frac{\mathrm{i}m(\Delta q)^2}{2\hbar\epsilon}}\int\frac{\mathrm{d}p}{2\pi\hbar}\exp\left[-\frac{\mathrm{i}\epsilon}{2m\hbar}\left(p-\frac{m\Delta q}{\epsilon}\right)^2\right].$$

Fresnel 积分 $\int\mathrm{d}u\,e^{-\mathrm{i}\alpha u^2} = \sqrt{\frac{\pi}{\mathrm{i}\alpha}}$（$\alpha = \epsilon/(2m\hbar)$）：

$$= \sqrt{\frac{m}{2\pi\mathrm{i}\hbar\epsilon}}\;e^{\frac{\mathrm{i}m(\Delta q)^2}{2\hbar\epsilon}}.$$

每层贡献一个因子；$\sum_k\frac{m(\Delta q_k)^2}{2\epsilon} \to \int\frac{m\dot q^2}{2}\mathrm{d}t$。把 $\sqrt{m/(2\pi\mathrm{i}\hbar\epsilon)}$ 的乘积吸收进测度 $\mathcal Dq$，即得

$$\int\mathcal Dq\;\exp\left\{\frac{\mathrm{i}}{\hbar}\int\left[\frac{m\dot q^2}{2} - V(q)\right]\mathrm{d}t\right\}.$$

**自由粒子的 van Vleck 行列式**：自由粒子 $S_{\mathrm{cl}} = \frac{m(q_f-q_i)^2}{2t}$，

$$\frac{\partial^2S_{\mathrm{cl}}}{\partial q_f\,\partial q_i} = -\frac{m}{t},\qquad \left|\det\right|^{1/2} = \sqrt{\frac{m}{t}}.$$

而精确传播子

$$\langle q_f|e^{-\mathrm{i}\hat Ht/\hbar}|q_i\rangle = \sqrt{\frac{m}{2\pi\mathrm{i}\hbar t}}\;e^{\frac{\mathrm{i}m(q_f-q_i)^2}{2\hbar t}},$$

振幅正是 $\sqrt{m/(2\pi\mathrm{i}\hbar t)} = (2\pi\mathrm{i}\hbar)^{-1/2}\left|\det\frac{\partial^2S}{\partial q_f\partial q_i}\right|^{1/2}$——半经典传播子的标准形式。

</details>

**2.** 对 $H = f(q)p$，比较中点、左端点、右端点三种格点规则到 $O(\epsilon)$，证明中点 = Weyl 排序，并定出端点规则对应的排序。

<details markdown="1"><summary>点击显示答案</summary>

记 $\eta = q'-q$。一阶核：

$$K \approx \int\frac{\mathrm{d}p}{2\pi\hbar}e^{\mathrm{i}p\eta/\hbar}\left[1 - \frac{\mathrm{i}\epsilon}{\hbar}H(p,\bar q)\right] = \delta(\eta) - \frac{\mathrm{i}\epsilon}{\hbar}\int\frac{\mathrm{d}p}{2\pi\hbar}e^{\mathrm{i}p\eta/\hbar}\,f(\bar q)\,p.$$

用 $\int\frac{\mathrm{d}p}{2\pi\hbar}e^{\mathrm{i}p\eta/\hbar} = \delta(\eta)$ 与 $\int\frac{\mathrm{d}p}{2\pi\hbar}e^{\mathrm{i}p\eta/\hbar}p = -\mathrm{i}\hbar\partial_\eta\delta(\eta)$：

$$K = \delta(\eta) - \frac{\mathrm{i}\epsilon}{\hbar}f(\bar q)\left(-\mathrm{i}\hbar\partial_\eta\delta\right) = \delta - \epsilon f(\bar q)\,\partial_\eta\delta.$$

**中点**：$\bar q = q + \eta/2$，$f(\bar q) = f(q) + \frac{\eta}{2}f'(q) + O(\eta^2)$。用 $\eta\,\partial_\eta\delta = -\delta$：

$$K_{\mathrm{mid}} = \delta - \epsilon\left[f(q)\partial_\eta\delta + \frac12 f'(q)\,\eta\partial_\eta\delta\right] = \delta - \epsilon\left[f(q)\partial_\eta\delta - \frac12 f'(q)\delta\right].$$

现在算 Weyl 排序的核：

$$\langle q'|H_{\mathrm{Weyl}}|q\rangle = \tfrac12\left[f(q')(-\mathrm{i}\hbar\partial_\eta\delta) + (-\mathrm{i}\hbar\partial_\eta)(f\delta)\right] = -\mathrm{i}\hbar\left[f(q')\partial_\eta\delta + \tfrac12 f'(q')\delta\right].$$

一阶核 $\delta - \frac{\mathrm{i}\epsilon}{\hbar}\langle H_{\mathrm{Weyl}}\rangle = \delta - \epsilon\left[f(q')\partial_\eta\delta + \frac12 f'(q')\delta\right]$。用 $f(q') = f(q) + \eta f'$ 与 $\eta\partial_\eta\delta = -\delta$ 化简方括号：

$$f(q')\partial_\eta\delta + \tfrac12 f'(q')\delta = f(q)\partial_\eta\delta - f'(q)\delta + \tfrac12 f'(q)\delta = f(q)\partial_\eta\delta - \tfrac12 f'(q)\delta,$$

与 $K_{\mathrm{mid}}$ 逐项相同 ✓。**中点规则 = Weyl 排序**（一阶；高阶由 BCH 逐阶匹配）。

**左端点**：$\bar q = q$，$f(\bar q) = f(q)$：

$$K_{\mathrm{left}} = \delta - \epsilon f\partial_\eta\delta.$$

算符核 $\langle q'|pf|q\rangle = -\mathrm{i}\hbar\partial_\eta(f\delta) = -\mathrm{i}\hbar[f'\delta + f\partial_\eta\delta]$，即 $K = \delta - \epsilon[f\partial\delta + f'\delta]$。这与 $K_{\mathrm{left}}$ 差一个 $-\epsilon f'\delta$。再用 $f(q) = f(q') - \eta f'$：$f(q)\partial\delta = f(q')\partial\delta - f'\eta\partial\delta = f(q')\partial\delta + f'\delta$。故

$$K_{\mathrm{left}} = \delta - \epsilon\left[f(q')\partial_\eta\delta + f'\delta\right],$$

正对应 $pf$ ✓。

**右端点**：$\bar q = q'$，$K_{\mathrm{right}} = \delta - \epsilon f(q')\partial_\eta\delta$，正对应 $fp$ ✓。

三种规则确实给出三种排序；中点与 Weyl 匹配。$\square$

</details>

**3.** 证明对 $H = \frac{p^2}{2m} + V(q)$，左端点与右端点规则的差别是全导数（因此三种规则给出同一量子理论）。

<details markdown="1"><summary>点击显示答案</summary>

两种规则的格点作用量只差 $V$ 的取值点：

$$\Delta S = \epsilon\sum_k\left[V(q_k) - V(q_{k-1})\right].$$

把 $V(q_k) - V(q_{k-1}) \approx (q_k - q_{k-1})V'(\bar q_k)$ 代入，并注意 $\dot q_k \approx (q_k-q_{k-1})/\epsilon$：

$$\Delta S \approx \epsilon\sum_k \epsilon\dot q_k V'(q) = \int\mathrm{d}t\;\epsilon\,\dot q\,V'(q) \xrightarrow{\epsilon\to0} 0.$$

更准确地：$\epsilon\sum_k[V(q_k)-V(q_{k-1})] = \epsilon\left[V(q_N)-V(q_0)\right] = \epsilon\left[V(q_f)-V(q_i)\right]$——**telescoping**，与路径无关，只是端点常数的差。在 $\epsilon\to0$ 时它给出一个与路径无关的整体相位（可被归一化吸收），不改变任何物理。

物理原因：$V(q)$ 与 $p$ 不对易，但 $[p^2, V]$ 的效应在每一步是 $O(\epsilon^2)$，累积 $N = t/\epsilon$ 步仍是 $O(\epsilon)$，且被吸收进测度/端点项。**只有当 $H$ 含 $f(q)p$ 型交叉项时，一阶差异才是 $O(\epsilon)\times O(1)$，在极限中存活为 $O(\hbar)$ 的势。** 这就是"可分离系统无排序问题"的精确含义。

</details>

**4.** 从路径积分的变量平移推出自由标量场的 Schwinger–Dyson 方程与 $(\Box+m^2)\langle T\varphi(x)\varphi(y)\rangle = -\mathrm{i}\delta^4(x-y)$。

<details markdown="1"><summary>点击显示答案</summary>

平移不变性：

$$0 = \int\mathcal D\varphi\;\frac{\delta}{\delta\varphi(x)}e^{\mathrm{i}S+\mathrm{i}\int J\varphi} = \int\mathcal D\varphi\;\mathrm{i}\left[\frac{\delta S}{\delta\varphi(x)}+J(x)\right]e^{\mathrm{i}S+\mathrm{i}\int J\varphi}.$$

除以 $Z[J]$：

$$\left\langle\frac{\delta S}{\delta\varphi(x)}\right\rangle_J + J(x) = 0.$$

自由场 $\delta S/\delta\varphi = -(\Box+m^2)\varphi$：

$$(\Box+m^2)\langle\varphi(x)\rangle_J = J(x).$$

对 $J(y)$ 变分：左端 $(\Box_x+m^2)\frac{\delta\langle\varphi(x)\rangle_J}{\delta J(y)}$，右端 $\delta^4(x-y)$。而由 $Z$ 的定义，

$$\frac{\delta\langle\varphi(x)\rangle_J}{\delta J(y)} = \frac{\delta}{\delta J(y)}\left(\frac{1}{\mathrm{i}}\frac{\delta\ln Z}{\delta J(x)}\right) = \frac{1}{\mathrm{i}}\frac{\delta^2\ln Z}{\delta J(x)\delta J(y)} = \mathrm{i}\left[\langle T\varphi(x)\varphi(y)\rangle_J - \langle\varphi(x)\rangle_J\langle\varphi(y)\rangle_J\right].$$

（最后一步：由 $\langle T\varphi\varphi\rangle = (1/\mathrm{i})^2\delta^2\ln Z/\delta J\delta J + \langle\varphi\rangle\langle\varphi\rangle$ 得连通部分 $G_c = -\mathrm{i}\,\delta\langle\varphi\rangle/\delta J$，即 $\delta\langle\varphi\rangle/\delta J = \mathrm{i}\,G_c$。）

在 $J=0$ 时连通部分就是 $\langle T\varphi\varphi\rangle$：

$$(\Box+m^2)\langle T\varphi(x)\varphi(y)\rangle = -\mathrm{i}\,\delta^4(x-y).\qquad\square$$

关键点：右端的 $\delta$ 来自 $\delta J(x)/\delta J(y)$，是**源的变分**，不是运动方程的输入。换句话说，**接触项是"源是局域的"这件事的必然产物**——它与传播子的紫外行为无关。

</details>

**5.** 证明路径积分给出的接触项等于等时对易子：从 $D_F(x) = \theta(t)D(x) + \theta(-t)D(-x)$ 出发，说明 $\partial_t^2D_F$ 的 $\delta(t)$ 项系数是 $-[\varphi(t,\mathbf x),\dot\varphi(t,\mathbf y)]$。

<details markdown="1"><summary>点击显示答案</summary>

记 $D(x) = \langle 0|\varphi(x)\varphi(0)|0\rangle$（02 篇的 Wightman 函数）。费曼传播子

$$D_F(x) = \theta(t)D(x) + \theta(-t)D(-x).$$

一阶导数：

$$\partial_tD_F = \delta(t)\left[D(x) - D(-x)\right] + \theta(t)\partial_tD(x) - \theta(-t)\partial_tD(-x).$$

方括号 $D(x) - D(-x) = \langle0|[\varphi(x),\varphi(0)]|0\rangle$ 在 $t=0$ 时为零（类空间隔对易子为零，等时也是类空），故 $\delta(t)$ 项消失。

二阶导数：

$$\partial_t^2D_F = \delta(t)\left[\partial_tD - \partial_tD(-x)\right]_{t=0} + (\text{含 }\theta\text{ 的平滑项}).$$

在 $t=0$：$\partial_tD = \langle0|\dot\varphi(0,\mathbf x)\varphi(0)|0\rangle$，$\partial_tD(-x)|_{t=0} = -\langle0|\varphi(0)\dot\varphi(0,\mathbf x)|0\rangle$。故方括号

$$= \langle0|\dot\varphi\varphi|0\rangle + \langle0|\varphi\dot\varphi|0\rangle = \langle0|\{\dot\varphi(0,\mathbf x),\varphi(0)\}|0\rangle.$$

对 $[\varphi,\dot\varphi] = \mathrm{i}\delta^3$，等时反对易子就是 $\mathrm{i}\delta^3(\mathbf x)$（自由场中另一项在等时也给出同值；用 $\dot\varphi = \pi$ 与 $[\varphi,\pi] = \mathrm{i}\delta^3$）。于是

$$\partial_t^2D_F \supset \delta(t)\,\mathrm{i}\delta^3(\mathbf x) = \mathrm{i}\delta^4(x).$$

与 $(\Box+m^2)D_F = -\mathrm{i}\delta^4$ 的符号约定一致（空间导数项无 $\delta$）。$\square$

结论：**传播子二阶导数的 $\delta$ 项 = 等时对易子**。路径积分的源变分与算符形式的等时对易子，是同一个接触项的两张脸。

</details>

## 参考

- Feynman & Hibbs《Quantum Mechanics and Path Integrals》：相空间路径积分与中点规则的原始讨论（第 4–5 章）。
- Schulman《Techniques and Applications of Path Integration》：离散化与算符排序的系统处理（第 4、8 章）。
- 量子力学书 03s2（Weyl 排序与 Moyal 星积）、07s（路径积分的量子力学构造与"中点处方"的承认引用）。
- 07 篇（切片推导、$Z[J]$、高斯积分、Wick 定理）；Schwinger–Dyson 与接触项在 QFT 中的使用见第 9 阶段 01 篇（in-in）与 04 篇（论文 (4.28)）。
