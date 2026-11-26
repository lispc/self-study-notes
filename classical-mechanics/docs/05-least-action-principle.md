# 最小作用量原理：从 Galileo 相对性推出拉氏量

> 路线图位置：第 1 部分（拉格朗日力学：对称性第一性原理）· 第 5 章
> 前置知识：第 1 章（约束、广义坐标、虚功原理）；多元微积分（变分法的基础：分部积分与边界条件）。
> 学习目标：能说清"作用量原理"与牛顿方程的关系（谁是第一性原理）；会复述 Landau 式推导——从 Galileo 相对性原理与时空均匀、各向同性推出自由粒子的 $L = \frac12 mv^2$；会从 $\delta S = 0$ 完整推出 Euler–Lagrange 方程；理解拉氏量非唯一性（$L \to L + \mathrm{d}F/\mathrm{d}t$）的含义与边界。

---

**单位约定**：本篇保留通常单位（$\hbar$、$c$ 不入场）；作用量的量纲是"能量 × 时间"，量子的作用量单位是 $\hbar$——这一点在第 6 章之后会反复用到。

## 1. 一句话总结

**最小作用量原理说：真实运动使作用量 $S = \int L\,\mathrm{d}t$ 取驻值。它的力量不在"等价于牛顿方程"（这容易证明），而在"用对称性确定 $L$"：时空的均匀性与各向同性、Galileo 相对性原理三者合起来，把自由粒子的拉氏量锁定为 $\frac12 mv^2$（只差一个整体常数）。从此，物理学的出发点从"力"换成了"作用量 + 对称性"——这条路线在 QFT 里长成"写出最一般的、满足对称性的拉氏量"的标准操作。**

## 2. 从"力"到"作用量"

### 2.1 牛顿力学的三个不满

第 1 章已经列出：约束要靠"约束力"硬算、坐标系变换后方程变形、守恒律是"碰巧"（每条守恒律都要单独用牛顿定律证明）。作用量原理对这三件事给出了统一的处理：

- 约束用广义坐标吸收（完整约束下约束力自动不做虚功）；
- 拉氏量是标量，坐标变换下形式不变（Euler–Lagrange 方程是协变的）；
- 守恒律来自拉氏量的对称性（第 6 章的 Noether 定理）。

### 2.2 作用量与变分原理

**作用量**是轨道 $q(t)$ 的泛函：

$$S[q] = \int_{t_1}^{t_2}L\left(q(t),\dot q(t),t\right)\mathrm{d}t.$$

**最小作用量原理**（更准确的名字是"驻定作用量原理"）：在固定端点 $q(t_1) = q_1$、$q(t_2) = q_2$ 的所有轨道中，真实轨道使 $S$ 取驻值：

$$\delta S = 0\quad\text{（对满足 }\delta q(t_1) = \delta q(t_2) = 0\text{ 的变分）}.$$

"最小"是历史名称：多数情形是极小，但鞍点也可能（例如某些高能轨道）。

### 2.3 历史一句话

Maupertuis（1744）提出"最小作用量"的模糊版本；Euler 与 Lagrange 把它变成变分法；Hamilton（1834）把它提升为与光学费马原理并列的力学原理。Landau 的贡献是反过来用：**不假设 $L$ 的形式，而从对称性推出它**（§3）。

## 3. Landau 式推导：自由粒子的 $L = \frac12 mv^2$

### 3.1 出发点

取惯性系。自由粒子（无外场、无相互作用）的拉氏量要满足：

1. **时空均匀**：$L$ 不显含 $t$，也不显含 $\mathbf r$（否则空间中有特殊点）；
2. **各向同性**：$L$ 只依赖速度的大小，即 $L = L(v^2)$；
3. **Galileo 相对性**：在 $v\to v + V$（$V$ 为任意常矢量）下，运动方程形式不变。这要求 $L$ 的变化最多是一个全导数：

$$L\left((\mathbf v + \mathbf V)^2\right) = L(v^2) + \frac{\mathrm{d}}{\mathrm{d}t}F(\mathbf r,t).$$

### 3.2 展开与匹配

对小的 $V$ 展开：

$$L(v^2 + 2\mathbf v\cdot\mathbf V + V^2) = L(v^2) + 2L'(v^2)\,\mathbf v\cdot\mathbf V + O(V^2).$$

线性项 $2L'(v^2)\,\mathbf v\cdot\mathbf V$ 必须能写成全导数。注意 $\mathbf v\cdot\mathbf V = \mathrm{d}(\mathbf r\cdot\mathbf V)/\mathrm{d}t$，于是

$$2L'(v^2)\,\mathbf v\cdot\mathbf V = \frac{\mathrm{d}}{\mathrm{d}t}\left[2L'(v^2)\,\mathbf r\cdot\mathbf V\right] - 2\,\mathbf r\cdot\mathbf V\,\frac{\mathrm{d}}{\mathrm{d}t}L'(v^2).$$

第二项含 $\mathbf r$ 的显式依赖，**不可能对任意 $V$ 都是全导数**（除非它为零）。因此

$$\frac{\mathrm{d}}{\mathrm{d}t}L'(v^2) = 0 \;\Longrightarrow\; L'(v^2) = \text{常数} \;\Longrightarrow\; L(v^2) = a\,v^2 + b.$$

常数 $b$ 不影响运动方程，丢掉；$a$ 由质量的定义固定：取 $a = \frac12 m$，使动量 $p = \partial L/\partial v = mv$ 与牛顿动量一致。于是

$$\boxed{\;L = \frac12 m v^2.\;}$$

### 3.3 验证：Galileo boost 下只差全导数

$$L' = \frac12 m(\mathbf v + \mathbf V)^2 = \frac12 mv^2 + m\mathbf v\cdot\mathbf V + \frac12 mV^2 = L + \frac{\mathrm{d}}{\mathrm{d}t}\left(m\,\mathbf r\cdot\mathbf V + \frac12 mV^2 t\right).$$

全导数不影响 Euler–Lagrange 方程——**运动方程在 Galileo boost 下形式不变**（自检 1）。

### 3.4 这条推导的"含金量"

它没有用到任何动力学细节，只用了对称性；换一组对称性（例如相对论性的 Lorentz 群），同样的逻辑会给出不同的 $L$（相对论粒子 $L = -mc^2\sqrt{1-v^2/c^2}$，第 9 章）。**"对称性定拉氏量"是 QFT 里写出标准模型拉氏量的同一条逻辑**（QFT 书第 5、6 阶段）。

## 4. 质点系与相互作用

### 4.1 封闭系统

对多质点系统，各向同性 + Galileo 不变性把 $L$ 推成

$$L = \sum_i\frac12 m_i v_i^2 - V\left(\{\mathbf r_i\}\right).$$

动能部分是单粒子结果的相加；相互作用只能以势能形式出现（如果依赖速度，会破坏 Galileo 不变性或导致任意性——辐射反作用就是经典电动力学的著名困难，见电动力学书第 15 章）。

### 4.2 相互作用势的对称性约束

对封闭系统，$V$ 只能依赖相对坐标 $\mathbf r_i - \mathbf r_j$（空间均匀性），并且：

- 各向同性 ⇒ 只依赖 $|\mathbf r_i - \mathbf r_j|$ 与夹角不变量；
- 若进一步要求"只依赖距离"，即得中心力势 $V = \sum_{i \lt j} V_{ij}(|\mathbf r_i - \mathbf r_j|)$——这正是第 2 章中心力场的出发点。

### 4.3 外场中的粒子

外场破坏平移不变性（场本身选了一个参考系/源），$L$ 可以显含 $\mathbf r$：

$$L = \frac12 m\dot{\mathbf r}^2 - V(\mathbf r,t).$$

电磁场是例外：它用矢势以速度依赖的方式耦合，$L = \frac12 m\dot{\mathbf r}^2 + q\dot{\mathbf r}\cdot\mathbf A - q\varphi$——电动力学书第 12 章与 QFT 书第 3 阶段 03 篇。

## 5. Euler–Lagrange 方程

### 5.1 变分推导

$$\delta S = \int_{t_1}^{t_2}\left[\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial \dot q^i}\delta\dot q^i\right]\mathrm{d}t.$$

第二项分部积分（$\delta\dot q = \mathrm{d}(\delta q)/\mathrm{d}t$）：

$$\int\frac{\partial L}{\partial\dot q^i}\frac{\mathrm{d}}{\mathrm{d}t}\delta q^i\,\mathrm{d}t = \left[\frac{\partial L}{\partial\dot q^i}\delta q^i\right]_{t_1}^{t_2} - \int\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot q^i}\right)\delta q^i\,\mathrm{d}t.$$

边界项因 $\delta q(t_{1,2}) = 0$ 消失。$\delta q^i$ 任意，故

$$\boxed{\;\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot q^i} - \frac{\partial L}{\partial q^i} = 0.\;}$$

这是**Euler–Lagrange 方程**；对 $L = \frac12 m\dot q^2 - V(q)$ 它就是 $m\ddot q = -V'(q)$。

### 5.2 广义坐标与约束

完整约束可以用广义坐标 $q^a$ 吸收（第 1 章）：把 $L$ 用 $q^a,\dot q^a$ 写出，Euler–Lagrange 方程自动只含独立方向——**约束力不必出现**。这是拉格朗日形式对牛顿形式的第一场胜利。

### 5.3 非保守力

若存在与速度成正比的耗散，可以写 Rayleigh 耗散函数 $\mathcal F = \frac12\sum\gamma_{ij}\dot q^i\dot q^j$，方程改为

$$\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot q^i} - \frac{\partial L}{\partial q^i} = -\frac{\partial\mathcal F}{\partial\dot q^i}.$$

更一般的非保守力没有作用量原理（或需要双倍变量/开系统框架）——"作用量原理只对保守系统直接成立"是它的边界。

## 6. 拉氏量的非唯一性

### 6.1 全导数不变性

若 $F(q,t)$ 是任意光滑函数，则

$$L' = L + \frac{\mathrm{d}F(q,t)}{\mathrm{d}t} = L + \frac{\partial F}{\partial q^i}\dot q^i + \frac{\partial F}{\partial t}$$

给出与 $L$ 完全相同的 Euler–Lagrange 方程（自检 3）。证明：$\delta\int \mathrm{d}F = [\delta F]_{t_1}^{t_2} = 0$，因为端点固定。

### 6.2 物理含义

- 拉氏量不是"能量"，差一个全导数不改变任何可观测；
- 常数项 $L\to L + c$ 改变作用量的零点，不改变运动；
- 但**作用量的绝对值**在量子力学里有意义：路径积分的相位是 $e^{\mathrm{i}S/\hbar}$，全导数项给出一个与路径端点有关的相位，在闭合路径上才是严格不可观测的（Aharonov–Bohm 的教训，量子力学书第 11 篇）。

### 6.3 与量子力学的接口

路径积分

$$\int\mathcal{D}q\;e^{\frac{\mathrm{i}}{\hbar}S[q]}$$

把"作用量"推到了量子理论的核心：$\hbar\to0$ 时稳相近似挑出 $\delta S = 0$ 的经典轨道（QFT 书第 4 阶段 07 篇）。**经典力学是量子力学的稳相极限**——这句话的全部技术内容就是本章的 $\delta S = 0$。

## 7. 小结

- 作用量原理：真实轨道使 $S = \int L\,\mathrm{d}t$ 驻定；$\delta S = 0$（端点固定）推出 Euler–Lagrange 方程。
- Landau 式推导：时空均匀 + 各向同性 + Galileo 不变性 ⇒ $L = L(v^2)$ 且 $L'\ = $ 常数 ⇒ $L = \frac12 mv^2$。
- 质点系：$L = \sum\frac12 m_iv_i^2 - V$；封闭系统的 $V$ 只依赖相对坐标；中心力势是进一步要求"只依赖距离"的结果。
- 拉氏量非唯一：$L\to L + \mathrm{d}F/\mathrm{d}t$ 不改变运动方程；但作用量的绝对值在量子相位 $e^{\mathrm{i}S/\hbar}$ 里可见。
- 边界：非保守力需要推广（Rayleigh 函数或开系统框架）；约束用广义坐标吸收。

## 自检问题

**1.** 验证 $L = \frac12 mv^2$ 在 Galileo boost $\mathbf v\to\mathbf v+\mathbf V$ 下只变一个全导数，并说明为什么这保证运动方程不变。

<details markdown="1"><summary>点击显示答案</summary>

$$L' = \frac12 m(\mathbf v+\mathbf V)^2 = \frac12 mv^2 + m\mathbf v\cdot\mathbf V + \frac12 mV^2.$$

把后两项写成全导数：

$$m\mathbf v\cdot\mathbf V + \frac12 mV^2 = \frac{\mathrm{d}}{\mathrm{d}t}\left(m\,\mathbf r\cdot\mathbf V + \frac12 mV^2t\right).$$

验证：$\frac{\mathrm{d}}{\mathrm{d}t}(m\mathbf r\cdot\mathbf V) = m\mathbf v\cdot\mathbf V$，$\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac12mV^2t\right) = \frac12mV^2$ ✓。故 $L' = L + \mathrm{d}F/\mathrm{d}t$，$F = m\mathbf r\cdot\mathbf V + \frac12mV^2t$。

运动方程不变：$\delta\int L'\mathrm{d}t = \delta\int L\,\mathrm{d}t + [\delta F]_{t_1}^{t_2} = \delta\int L\,\mathrm{d}t$（端点固定使 $\delta F$ 在端点为零）。所以两套拉氏量的驻定轨道相同——**Galileo 相对性原理在经典力学里是作用量的"全导数不变性"**。$\square$

（这也解释了 §3.2 的论证为什么必须要求"只差全导数"而不是"严格不变"：$\frac12mv^2$ 本身在 boost 下并不严格不变。）

</details>

**2.** 从 $\delta S = 0$ 完整推出 Euler–Lagrange 方程，并指出"端点固定"这一条件用在哪里。

<details markdown="1"><summary>点击显示答案</summary>

$$\delta S = \int_{t_1}^{t_2}\left[\frac{\partial L}{\partial q^i}\delta q^i + \frac{\partial L}{\partial\dot q^i}\delta\dot q^i\right]\mathrm{d}t,\qquad \delta\dot q^i = \frac{\mathrm{d}}{\mathrm{d}t}\delta q^i.$$

对第二项分部积分：

$$\int_{t_1}^{t_2}\frac{\partial L}{\partial\dot q^i}\frac{\mathrm{d}}{\mathrm{d}t}\delta q^i\,\mathrm{d}t = \left[\frac{\partial L}{\partial\dot q^i}\delta q^i\right]_{t_1}^{t_2} - \int_{t_1}^{t_2}\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial\dot q^i}\right)\delta q^i\,\mathrm{d}t.$$

**边界项为零**正是"端点固定"（$\delta q^i(t_1) = \delta q^i(t_2) = 0$）用到的唯一地方。于是

$$\delta S = \int_{t_1}^{t_2}\left[\frac{\partial L}{\partial q^i} - \frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot q^i}\right]\delta q^i\,\mathrm{d}t = 0.$$

$\delta q^i(t)$ 在区间内部任意（可以取只在某点附近非零的"尖峰"变分），故方括号必须逐点为零：

$$\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial L}{\partial\dot q^i} - \frac{\partial L}{\partial q^i} = 0.\qquad\square$$

若端点不固定，边界项会给出额外的自然边界条件 $\left.\partial L/\partial\dot q^i\right|_{t_{1,2}} = 0$——这是变分原理的"自然边界条件"，在路径积分与场论边界项里会再次出现（第 9 阶段）。

</details>

**3.** 证明 $L' = L + \mathrm{d}F(q,t)/\mathrm{d}t$ 给出同一 Euler–Lagrange 方程，并举一个具体例子。

<details markdown="1"><summary>点击显示答案</summary>

$$\delta\int \frac{\mathrm{d}F}{\mathrm{d}t}\mathrm{d}t = \delta\left[F(q(t_2),t_2) - F(q(t_1),t_1)\right] = 0,$$

因为端点的 $q$ 固定。故 $\delta\int L'\mathrm{d}t = \delta\int L\,\mathrm{d}t$，两者的驻定轨道相同，Euler–Lagrange 方程相同。$\square$

**具体例子**：$L = \frac12 m\dot x^2$（自由粒子），取 $F = \frac12 kx^2$，$\dot F = kx\dot x$：

$$L' = \frac12 m\dot x^2 + kx\dot x.$$

Euler–Lagrange：$\partial L'/\partial\dot x = m\dot x + kx$，$\frac{\mathrm{d}}{\mathrm{d}t}(\cdots) = m\ddot x + k\dot x$；$\partial L'/\partial x = k\dot x$。方程：

$$m\ddot x + k\dot x - k\dot x = m\ddot x = 0,$$

与自由粒子相同 ✓。注意 $L'$ 的"能量" $p\dot x - L' = (m\dot x + kx)\dot x - \frac12m\dot x^2 - kx\dot x = \frac12m\dot x^2$ 仍正确（因为 $F$ 不显含 $t$ 时，全导数项不改变能量），但正则动量 $p = m\dot x + kx$ 已经变了——**"正则动量依赖拉氏量的选取"是规范自由度的一部分**，量子化时必须用正确的正则对（第 9 章）。

</details>

**4.** 加速参考系：设惯性系中 $L = \frac12 m\dot x^2$，令 $X = x - \frac12 gt^2$。求出 $X$ 系的拉氏量，说明它等价于一个均匀引力场。

<details markdown="1"><summary>点击显示答案</summary>

$\dot x = \dot X + gt$，代入：

$$L = \frac12 m(\dot X + gt)^2 = \frac12 m\dot X^2 + mgt\dot X + \frac12 mg^2t^2.$$

把后两项凑成全导数：

$$mgt\dot X = \frac{\mathrm{d}}{\mathrm{d}t}(mgtX) - mgX,\qquad \frac12 mg^2t^2 = \frac{\mathrm{d}}{\mathrm{d}t}\left(\frac16 mg^2t^3\right).$$

于是

$$L = \left[\frac12 m\dot X^2 - mgX\right] + \frac{\mathrm{d}}{\mathrm{d}t}\left(mgtX + \frac16mg^2t^3\right).$$

丢掉全导数，等效拉氏量

$$L_{\mathrm{eff}} = \frac12 m\dot X^2 - mgX,$$

即**势能 $V = mgX$、力 $F = -mg$（沿 $-X$ 方向）的均匀引力场**。$\square$

这就是等效原理的经典版本：加速参考系与均匀引力场在力学上不可区分。注意这里 $L$ 显含 $t$（通过全导数项），所以"能量"的定义与惯性系不同——但运动方程（$m\ddot X = -mg$）是确定的。广义相对论的等效原理（广义相对论书第 5 章）把这一观察推广到一切物理过程。

</details>

**5.** 证明多质点封闭系统的 $L = \sum_i\frac12m_iv_i^2 - V(\{\mathbf r_i\})$ 在 Galileo boost 下只差全导数，并说明 $V$ 必须只依赖相对坐标。

<details markdown="1"><summary>点击显示答案</summary>

boost：$\mathbf r_i\to\mathbf r_i + \mathbf Vt$，$\mathbf v_i\to\mathbf v_i + \mathbf V$。动能部分：

$$\sum_i\frac12m_i(\mathbf v_i+\mathbf V)^2 = \sum_i\frac12m_iv_i^2 + \mathbf V\cdot\sum_i m_i\mathbf v_i + \frac12M V^2,$$

$M = \sum_i m_i$。后两项是全导数：

$$\mathbf V\cdot\sum_i m_i\mathbf v_i + \frac12MV^2 = \frac{\mathrm{d}}{\mathrm{d}t}\left(\mathbf V\cdot\sum_i m_i\mathbf r_i + \frac12MV^2t\right).$$

所以动能部分满足 Galileo 不变性（差全导数）。势能部分必须**严格不变**：$V(\{\mathbf r_i + \mathbf Vt\}) = V(\{\mathbf r_i\})$ 对任意 $V,t$ 成立，当且仅当 $V$ 只依赖相对坐标 $\mathbf r_i - \mathbf r_j$。$\square$

进一步：若要求 $V$ 在各向同性下只依赖距离，则 $V = V(\{|\mathbf r_i-\mathbf r_j|\})$；再要求"两两相加"，即得中心力势 $V = \sum_{i \lt j}V_{ij}(|\mathbf r_i-\mathbf r_j|)$——第 2 章 Kepler 问题的出发点。

这个练习展示了对对称性论证的完整用法：**先定动能（boost 不变性），再定势能（平移/转动不变性）**，两步都把"可能的拉氏量"压缩到极小。

</details>

## 参考

- Landau & Lifshitz《力学》§1–5：作用量原理与自由粒子拉氏量的推导（本篇 §3 的母本）；§2（Galileo 相对性原理）。
- Goldstein《Classical Mechanics》第 1–2 章：变分原理与 Euler–Lagrange 方程的标准处理。
- 第 1 章（约束与广义坐标）、第 6 章（Noether 定理）、第 9 章（正则形式）；相对论性推广见 QFT 书第 3 阶段 01 篇。
