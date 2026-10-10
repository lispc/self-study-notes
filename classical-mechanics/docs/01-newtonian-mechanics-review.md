# 牛顿力学回顾与批判

> 路线图位置：理论力学书 · 第〇部分（牛顿力学的重审）· 第 1 章，全书开篇；本章清点旧力学的资产与负债，后续第 5 章（最小作用量原理）将从 Galileo 相对性原理与时空对称性出发重建整套力学
> 前置知识：普通物理力学（质点动力学、质点系、保守力与势能）；微积分与常微分方程
> 学习目标：能把牛顿三定律按"惯性系存在性＋力的操作定义兼动力学方程＋相互作用结构"三重角色拆开，说清第三定律强弱两版各自支撑哪条守恒律；会数完整约束、选广义坐标、区分虚位移与实位移；会从 d'Alembert 原理完整推出广义坐标形式的运动方程，并指出牛顿形式三个结构性缺陷各自的出路

---

## 1. 一句话总结

**牛顿力学 = 惯性系的存在性断言（第一定律）＋ 力的操作定义与动力学方程（第二定律 $\vec F = \mathrm d\vec p/\mathrm dt$）＋ 相互作用结构（第三定律），质点系的动量、角动量、能量守恒律都是它的推论；这套"力语言"对自由质点是完备的，但一遇到约束立刻暴露三个结构性缺陷：约束力事先未知、只能列完全部方程再事后消去，坐标被约束捆绑、不能独立变分，守恒律的真正来源（时空对称性）完全被遮蔽——广义坐标＋虚位移＋d'Alembert 原理回答前两个，第三个留给第 6 章的 Noether 定理；而 $L = T - V$ 将在本章末尾第一次现身。**

## 2. 牛顿三定律的批判性重读

### 2.1 第一定律：不是第二定律的特例，而是惯性系的存在性断言

若把第一定律（不受力的物体保持静止或匀速直线运动）看成第二定律在 $\vec F = \vec 0$ 时的特例，它就冗余了。但第二定律里的加速度是相对**哪个参考系**的？只有在惯性系里它才成立——**第一定律的真正内容是断言惯性系存在**：存在一类参考系，其中（充分远离其他物体的）自由质点做匀速直线运动；任何两个惯性系之间只差一个 Galileo 变换（平移、转动、匀速 boost）。没有这句断言，第二定律连表述的对象都没有，"$\vec F = \vec 0 \Rightarrow \vec a = \vec 0$"就成了循环论证。Newton 本人用"绝对空间"填这个空位，Mach 后来批评应改为"由远方物质的平均分布决定"；本课程采用操作性读法：惯性系的存在性是公理，具体惯性系由实验逐级逼近（地面系 → 太阳–恒星系 → ……），逼近的精度由观测说了算。

### 2.2 第二定律：操作定义与动力学方程的双重身份

第二定律 $\vec F = \mathrm d\vec p/\mathrm dt$ 扮演两个角色，拆开看才清楚：

- **作为"力"的操作定义**：取一只标准物体和一套标准操作（弹簧拉到固定伸长量），用它赋予标准物体的加速度定义单位力，加速度的几倍即几倍力，再用校准过的弹簧秤把这条测量链铺开——力是被测量程序定义出来的；
- **作为动力学定律**：物理内容是存在**简单的力律** $\vec F = \vec F(\vec r, \dot{\vec r}, t)$（引力、弹性力、洛伦兹力……），使第二定律成为二阶常微分方程组，给定初位置与初速度唯一决定轨道。

两个角色缺一不可：只有前者，定律是同义反复；只有后者，"力"没有测量意义——正是"定义＋方程"的缝合让牛顿体系运转起来。写成 $\dot{\vec p} = \vec F$ 而不是 $m\vec a = \vec F$ 则是为了**推广能力**：变质量体系（火箭，须把喷出物的动量一并记账）与狭义相对论（动量形式 $\dot{\vec p} = \vec F$ 在 $\vec p = \gamma m\vec v$ 下依然成立，见[电动力学书](../../electrodynamics/README.md)）里 $m\vec a$ 形式失效而动量形式存活。

### 2.3 第三定律：强弱两版与适用边界

"作用力与反作用力大小相等、方向相反"其实有两个版本：

- **弱版**：$\vec F_{ij} = -\vec F_{ji}$（质点 $j$ 对 $i$ 的力与 $i$ 对 $j$ 的力等值反向）——足以推出质点系总动量守恒；
- **强版**：弱版之外还要求力沿两质点连线，即 $(\vec r_i - \vec r_j)\times\vec F_{ij} = \vec 0$——总角动量守恒必须用它（推导见自检问题 1：弱版管不住一对不共线的等值反向力组成的力偶）。

第三定律并非普适：**两个运动带电粒子之间的电磁力一般既不满足弱版也不满足强版**（磁力部分不沿连线、也不等值反向）。这不是牛顿力学的逻辑漏洞，而是适用边界：漏掉的动量在电磁场里——场本身携带动量与角动量，把场计入账本后总量依然守恒。这个故事属于[电动力学书](../../electrodynamics/README.md)，此处只记一句：第三定律的失效暴露了"物体间超距接触作用"世界观的边界，而牛顿体系内部对此无计可施。一句话收束：三定律不是三条并列的经验陈述，而是"惯性系搭台＋动力学方程立规＋相互作用结构约束"的三位一体；后面会看到（第 5、6 章），拉格朗日体系把这三块重新组织为"时空对称性＋最小作用量"，守恒律从碰巧的推论升格为出发点。

## 3. 质点系与守恒律

### 3.1 内力/外力分解与三大定理

$N$ 个质点：$m_i$、$\vec r_i$、$\vec p_i = m_i\dot{\vec r}_i$，受力分解为外力与内力之和

$$\vec F_i = \vec F_i^{(\text{外})} + \sum_{j\neq i}\vec F_{ji}.$$

**动量**：总动量 $\vec P = \sum_i\vec p_i$。对第二定律逐质点求和，内力由弱版第三定律成对抵消，得质心动量定理

$$\dot{\vec P} = \vec F^{(\text{外})}, \qquad \vec F^{(\text{外})} \equiv \sum_i\vec F_i^{(\text{外})}.$$

**角动量**：总角动量 $\vec L = \sum_i\vec r_i\times\vec p_i$。由 $\dot{\vec r}_i\times\vec p_i = \vec 0$（二者平行）与强版第三定律（内力力矩成对抵消）得（两条守恒律的完整推导见自检问题 1）：

$$\dot{\vec L} = \vec\tau^{(\text{外})}, \qquad \vec\tau^{(\text{外})} \equiv \sum_i\vec r_i\times\vec F_i^{(\text{外})}.$$

**能量**：用 $\mathrm d\vec r_i$ 点乘各方程再求和，得动能定理 $\mathrm dT = \sum_i\vec F_i\cdot\mathrm d\vec r_i$，其中 $T = \frac12\sum_i m_i\dot{\vec r}_i^{\,2}$；若所有的力保守（$\vec F_i = -\nabla_i V$），机械能 $E = T + V$ 守恒。注意一处不对称：动量、角动量守恒**只**靠第三定律，能量守恒还要追加"力保守"的假设——而一对中心保守内力的势 $V = \sum_{i \lt j}V_{ij}\bigl(\lvert\vec r_i - \vec r_j\rvert\bigr)$ 本身已经预设了强版第三定律。

### 3.2 König 定理：质心运动的分离

定义质心 $\vec R = \sum_i m_i\vec r_i/M$（$M = \sum_i m_i$），相对坐标 $\vec r_i' = \vec r_i - \vec R$ 恒满足 $\sum_i m_i\vec r_i' = \vec 0$。代入动能：

$$T = \frac12\sum_i m_i\bigl(\dot{\vec R} + \dot{\vec r}_i'\bigr)^2 = \frac12 M\dot{\vec R}^{\,2} + \frac12\sum_i m_i\dot{\vec r}_i'^{\,2},$$

交叉项 $\dot{\vec R}\cdot\sum_i m_i\dot{\vec r}_i'$ 由质心定义恒为零。同理 $\vec L = \vec R\times M\dot{\vec R} + \sum_i\vec r_i'\times m_i\dot{\vec r}_i'$。**整体运动与内部运动干净分离**——这是质点系力学最好用的分解，第 3 章刚体的"平动＋绕质心转动"全靠它。

### 3.3 批判：守恒律的来源被遮蔽

在牛顿体系里，三条守恒律是"碰巧"由第三定律（外加保守性假设）推出的推论。但它们真正的来源——**时间平移不变性给能量、空间平移不变性给动量、转动不变性给角动量**——在力语言里从头到尾不露面：牛顿方程没有任何一处写着"时空是均匀且各向同性的"。一个理论把最深的原因藏成偶然，这是缺陷三。把它扶正的是 Noether 定理（1918）；本书第 6 章将在拉格朗日框架内给出力学版，届时逻辑倒置：对称性在先，守恒律只是影子。

### 3.4 两体问题化简

两个质点只受内力作用：质心做匀速直线运动，相对坐标 $\vec r = \vec r_1 - \vec r_2$ 满足

$$\mu\ddot{\vec r} = \vec F_{21}, \qquad \mu \equiv \frac{m_1 m_2}{m_1 + m_2}\ \ (\text{约化质量}),$$

由 $\ddot{\vec r} = \ddot{\vec r}_1 - \ddot{\vec r}_2 = \vec F_{21}/m_1 - \vec F_{12}/m_2 = \vec F_{21}\,(1/m_1 + 1/m_2)$ 立得（末步用弱版第三定律 $\vec F_{12} = -\vec F_{21}$；按第 3.1 节的记号约定，$\vec F_{ji}$ 是 $j$ 对 $i$ 的力）。两体问题于是**严格**化为单体问题——这是第 2 章中心力场与 Kepler 问题的入口。

## 4. 约束与广义坐标

### 4.1 约束的分类

真实力学体系很少有"全部自由的质点"：杆长固定、珠子穿在丝上、圆盘贴地滚动……约束就是对位置（乃至速度）的事先限制。分类如下：

| 分类轴 | 类型 | 定义与例子 |
| --- | --- | --- |
| 数学形式 | 完整约束（holonomic） | 只含坐标（与时间）的方程：$f_\alpha(\vec r_1,\dots,\vec r_N,t) = 0$；例：刚性杆 $\lvert\vec r_i - \vec r_j\rvert = l_{ij}$、质点限于某曲面 |
| 数学形式 | 非完整约束 | 不可积的微分约束；例：冰刀 $\sin\theta\,\mathrm dx - \cos\theta\,\mathrm dy = 0$（$\theta$ 本身是独立自由度，积不出 $f(x,y,\theta) = 0$）、竖直圆盘的纯滚动 |
| 时间依赖 | 定常约束（scleronomic） | $f$ 不显含 $t$ |
| 时间依赖 | 非定常约束（rheonomic） | $f$ 显含 $t$；例：电机驱动下匀速转动的圆环上的珠子（自检问题 3） |

另有双侧（$f = 0$）与单侧（$f \geq 0$，如可脱离的球面）之分。**本书只系统处理双侧完整约束**；非完整约束需要准坐标等额外工具，超出本课程范围。

### 4.2 自由度计数与例子

$N$ 个质点共 $3N$ 个直角坐标，$k$ 个**独立**完整约束把自由度削减为

$$n = 3N - k.$$

**例：平面双摆**。$m_1$ 由长 $l_1$ 的轻杆挂在固定点，$m_2$ 由长 $l_2$ 的轻杆挂在 $m_1$ 上，运动限于竖直平面。约束共 $k = 4$ 条：$z_1 = 0$、$z_2 = 0$（平面化两条）加两杆长度各一条，故 $n = 3\times 2 - 4 = 2$；广义坐标取两杆相对竖直方向的偏角 $\theta_1, \theta_2$（完整处理见自检问题 2）。**例：刚体**。$N$ 个质点两两距离固定：前三个不共线质点占 $9 - 3 = 6$ 个自由度，此后每加一个质点添 3 个坐标、也添 3 条独立距离约束（到前三个质点），净增为零——刚体自由度恒为 6（$N \geq 3$）。这是第 3 章的对象。

### 4.3 广义坐标与位形空间

完整约束下，位形由 $n = 3N - k$ 个**广义坐标** $q_1, \dots, q_n$ 唯一指定：

$$\vec r_i = \vec r_i(q_1, q_2, \dots, q_n, t), \qquad i = 1, \dots, N,$$

约束已自动消化在这组参数化里。要点：

- 广义坐标只需"完备且独立"，不必有长度量纲（角度是常客），也不必可直接测量；
- $(q_1, \dots, q_n)$ 张成**位形空间**（configuration space），体系的一段历史是位形空间中的一条曲线——$3N$ 个坐标的纷杂运动被压缩成单点的运动，几何化观点由此开始；
- 对时间求导得广义速度展开：$\dot{\vec r}_i = \sum_j \frac{\partial\vec r_i}{\partial q_j}\dot q_j + \frac{\partial\vec r_i}{\partial t}$。它对 $\dot q_j$ 是**线性**的——第 5.4 节两个引理全靠这一条。

### 4.4 约束力的麻烦：缺陷一、二正式登场

约束力（杆的张力、面的支持力、丝对珠子的力）与主动力有本质区别：**它事先未知**。它的大小方向由"必须维持约束"倒推出来，只能先解出运动才知道。牛顿解法是诚实的笨办法：把约束力当未知量引入，$3N$ 条方程连同 $k$ 条约束一起列，然后消去不感兴趣的约束力；质点一多（想想刚体每对质点之间都有内力）便是灾难。两个结构性缺陷现在可以精确陈述：

- **缺陷一**：形式体系强迫你携带一批事先未知、事后也不关心的量（约束力）；
- **缺陷二**：$3N$ 个坐标被 $k$ 条约束捆绑，不能独立变动——"每个坐标分量各写一条 $m\vec a = \vec F$"的图像与约束条件纠缠不清，动力学无法表述为对独立变分的干净断言。

出路分两步：广义坐标解除捆绑（缺陷二，已备）；再找一条约束力自动消失的原理（缺陷一）。这就是下一节。

## 5. 虚位移与 d'Alembert 原理

### 5.1 虚位移：冻结时间的假想位移

**虚位移** $\delta\vec r_i$ 是想象在**同一时刻**（$\delta t = 0$，时间冻结）给体系的一组无穷小位移，只要求**瞬时满足约束**：

$$\sum_i \frac{\partial f_\alpha}{\partial\vec r_i}\cdot\delta\vec r_i = 0, \qquad \alpha = 1, \dots, k.$$

用广义坐标写就是

$$\delta\vec r_i = \sum_{j=1}^{n}\frac{\partial\vec r_i}{\partial q_j}\,\delta q_j,$$

注意其中**没有** $\frac{\partial\vec r_i}{\partial t}\delta t$ 项——这正是它与实位移

$$\mathrm d\vec r_i = \sum_j \frac{\partial\vec r_i}{\partial q_j}\,\mathrm dq_j + \frac{\partial\vec r_i}{\partial t}\,\mathrm dt$$

的差别所在。定常约束下两者一致；**非定常约束下虚位移与实位移是两种东西**（自检问题 3 的旋转圆环演示得淋漓尽致：虚位移只有沿环切向的分量，实位移还含环转动拖曳的分量）。

### 5.2 理想约束：一条公设

**理想约束**定义为：约束力对任意虚位移的总虚功为零，

$$\sum_i \vec F_i^{(\text{约束})}\cdot\delta\vec r_i = 0.$$

标准成员：刚体内力（强版第三定律＋距离不变给出 $(\vec r_i - \vec r_j)\cdot(\delta\vec r_i - \delta\vec r_j) = 0$，虚功成对抵消）；光滑面的支持力（垂直于面内一切虚位移）；纯滚动接触点的静摩擦（约束使接触点虚位移为零；光滑丝对珠子是同类，见自检问题 3）。必须强调：**这是公设/定义，不是定理**——它就是"光滑""刚性""理想"这些词的精确含义。失效之处（滑动摩擦）必须把摩擦力改挂到主动力名下才能继续用这套理论。

### 5.3 d'Alembert 原理

把牛顿方程改写成"失效力平衡"（d'Alembert 1743 的视角）：

$$\vec F_i^{(\text{主})} + \vec F_i^{(\text{约束})} - \dot{\vec p}_i = \vec 0,$$

以任意虚位移点乘并对 $i$ 求和，理想约束使约束力项整个消失：

$$\sum_i\Bigl(\vec F_i^{(\text{主})} - \dot{\vec p}_i\Bigr)\cdot\delta\vec r_i = 0 \qquad \text{对一切虚位移成立}.$$

这就是 **d'Alembert 原理**：动力学被改写为**一条对标量的断言**——主动力与惯性力的虚功之和恒为零，约束力从方程中彻底蒸发（缺陷一解决）；静力学情形退化为虚功原理。它是通往拉格朗日力学的门，剩下的只是把坐标换成广义坐标。

### 5.4 主线推导：广义坐标形式的运动方程

目标：把 d'Alembert 原理中的直角坐标全部换成 $q, \dot q$，得到显式方程。需要两个引理，二者都源于 $\dot{\vec r}_i$ 对广义速度的线性结构（第 4.3 节末式）。

**引理 A（点的消去）**：$\dfrac{\partial\dot{\vec r}_i}{\partial\dot q_j} = \dfrac{\partial\vec r_i}{\partial q_j}$。证明：$\dot{\vec r}_i = \sum_k \frac{\partial\vec r_i}{\partial q_k}\dot q_k + \frac{\partial\vec r_i}{\partial t}$ 中，系数 $\partial\vec r_i/\partial q_k$ 与 $\partial\vec r_i/\partial t$ 只依赖 $(q, t)$，对 $\dot q_j$ 求偏导即得。

**引理 B（$\mathrm d/\mathrm dt$ 与 $\partial/\partial q_j$ 换序）**：$\dfrac{\mathrm d}{\mathrm dt}\frac{\partial\vec r_i}{\partial q_j} = \dfrac{\partial\dot{\vec r}_i}{\partial q_j}$。证明：左边 $= \sum_k\frac{\partial^2\vec r_i}{\partial q_k\,\partial q_j}\dot q_k + \frac{\partial^2\vec r_i}{\partial t\,\partial q_j} = \frac{\partial}{\partial q_j}\Bigl(\sum_k\frac{\partial\vec r_i}{\partial q_k}\dot q_k + \frac{\partial\vec r_i}{\partial t}\Bigr) = \frac{\partial\dot{\vec r}_i}{\partial q_j}$。

现在代入。虚位移用广义坐标展开，主动力项定义**广义力**：

$$\sum_i\vec F_i^{(\text{主})}\cdot\delta\vec r_i = \sum_j Q_j\,\delta q_j, \qquad Q_j \equiv \sum_i\vec F_i^{(\text{主})}\cdot\frac{\partial\vec r_i}{\partial q_j}.$$

惯性项用乘积法则拆开：

$$\dot{\vec p}_i\cdot\frac{\partial\vec r_i}{\partial q_j} = \frac{\mathrm d}{\mathrm dt}\Bigl(\vec p_i\cdot\frac{\partial\vec r_i}{\partial q_j}\Bigr) - \vec p_i\cdot\frac{\mathrm d}{\mathrm dt}\frac{\partial\vec r_i}{\partial q_j}.$$

第一项用引理 A：$\vec p_i\cdot\frac{\partial\vec r_i}{\partial q_j} = m_i\dot{\vec r}_i\cdot\frac{\partial\dot{\vec r}_i}{\partial\dot q_j} = \frac{\partial}{\partial\dot q_j}\Bigl(\frac12 m_i\dot{\vec r}_i^{\,2}\Bigr)$；第二项用引理 B：$\vec p_i\cdot\frac{\mathrm d}{\mathrm dt}\frac{\partial\vec r_i}{\partial q_j} = m_i\dot{\vec r}_i\cdot\frac{\partial\dot{\vec r}_i}{\partial q_j} = \frac{\partial}{\partial q_j}\Bigl(\frac12 m_i\dot{\vec r}_i^{\,2}\Bigr)$。对 $i$ 求和，动能 $T = \frac12\sum_i m_i\dot{\vec r}_i^{\,2}$ 浮现：

$$\sum_i\dot{\vec p}_i\cdot\delta\vec r_i = \sum_j\Bigl[\frac{\mathrm d}{\mathrm dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j}\Bigr]\delta q_j.$$

代回 d'Alembert 原理：

$$\sum_j\Bigl[\frac{\mathrm d}{\mathrm dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j} - Q_j\Bigr]\delta q_j = 0.$$

**收尾的关键一步**：完整约束下 $\delta q_1, \dots, \delta q_n$ 互相独立、各自任意，故每个方括号必须分别为零：

$$\boxed{\ \frac{\mathrm d}{\mathrm dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j} = Q_j\ }, \qquad j = 1, \dots, n.$$

$n$ 条二阶方程，约束力无踪，坐标独立——缺陷一、二同时解决。独立复算一遍是自检问题 5；Atwood 机的数值热身是自检问题 4。

### 5.5 $L = T - V$ 第一次现身

若主动力有势且势不含速度，$\vec F_i^{(\text{主})} = -\nabla_i V(\vec r_1, \dots, \vec r_N)$，链式法则给出

$$Q_j = -\sum_i\nabla_i V\cdot\frac{\partial\vec r_i}{\partial q_j} = -\frac{\partial V}{\partial q_j},$$

而 $V$ 与 $\dot q$ 无关（$\partial V/\partial\dot q_j = 0$），可以把 $V$ 同时并进两项：

$$\frac{\mathrm d}{\mathrm dt}\frac{\partial(T - V)}{\partial\dot q_j} - \frac{\partial(T - V)}{\partial q_j} = 0.$$

定义 $L \equiv T - V$，方程立刻压缩成 $\frac{\mathrm d}{\mathrm dt}\partial_{\dot q_j}L - \partial_{q_j}L = 0$——**Euler–Lagrange 方程的外形已经完整出现**。在牛顿–d'Alembert 路线里，$L = T - V$ 目前只是一次漂亮的合并同类项；本书第 5 章将改走 Landau 路线，从 Galileo 相对性原理与时空的均匀、各向同性**推出**自由粒子的 $L = \frac12 mv^2$ 和最小作用量原理，届时会看到 $T - V$ 不是技巧而是时空对称性的必然产物；缺陷三（守恒律的来源）则由第 6 章 Noether 定理补账。

## 小结

- 牛顿三定律是"惯性系存在性＋力的操作定义兼动力学方程＋相互作用结构"的三位一体，不是三条并列经验；第一定律若被当成第二定律的特例，整个体系便失去地基。
- 第三定律分强弱：弱版（等值反向）支撑总动量守恒，强版（再要求沿连线）支撑总角动量守恒；运动电荷间的电磁力两版皆不满足——动量藏在场里，这是适用边界而非逻辑漏洞。
- 质点系三大定理（$\dot{\vec P} = \vec F^{(\text{外})}$、$\dot{\vec L} = \vec\tau^{(\text{外})}$、$\mathrm dT = \sum_i\vec F_i\cdot\mathrm d\vec r_i$）加 König 分解 $T = T_{\text{质心}} + T_{\text{相对}}$ 是牛顿力学的最高成就；但守恒律的真正来源（时空对称性）在力语言中不可见——缺陷三，第 6 章 Noether 定理的动机。
- 完整约束下自由度 $n = 3N - k$，广义坐标 $q_1, \dots, q_n$ 唯一指定位形并自动消化约束；位形空间观点把 $N$ 质点的历史压缩成一条曲线。
- 约束力事先未知（缺陷一）与坐标不独立（缺陷二）逼出虚位移（$\delta t = 0$、瞬时满足约束）与理想约束公设（约束力虚功为零）；d'Alembert 原理把动力学压缩成一条对标量虚功的断言，约束力彻底消失。
- 由 d'Alembert 原理经"点的消去"与"换序"两引理推出 $\frac{\mathrm d}{\mathrm dt}\partial_{\dot q_j}T - \partial_{q_j}T = Q_j$；主动力有势时 $L = T - V$ 第一次现身——第 5 章将证明它是时空对称性的产物而非技巧。

## 自检问题

**1.** 从牛顿第二定律与第三定律出发，推导质点系总动量守恒（$\vec F^{(\text{外})} = \vec 0$ 时 $\vec P$ 守恒）；再推导总角动量方程 $\dot{\vec L} = \vec\tau^{(\text{外})}$，明确指出哪一步必须动用第三定律的强版。

<details markdown="1"><summary>点击显示答案</summary>

**动量**：$\dot{\vec P} = \sum_i\dot{\vec p}_i = \sum_i\vec F_i^{(\text{外})} + \sum_i\sum_{j\neq i}\vec F_{ji}$。把双重求和按 $(i, j)$ 与 $(j, i)$ 成对归组：

$$\sum_{i\neq j}\vec F_{ji} = \frac12\sum_{i\neq j}\bigl(\vec F_{ji} + \vec F_{ij}\bigr) = \vec 0,$$

用的正是弱版第三定律 $\vec F_{ij} = -\vec F_{ji}$。于是 $\dot{\vec P} = \vec F^{(\text{外})}$，合外力为零时总动量守恒。

**角动量**：$\vec L = \sum_i\vec r_i\times\vec p_i$，逐项求导：

$$\dot{\vec L} = \sum_i\dot{\vec r}_i\times m_i\dot{\vec r}_i + \sum_i\vec r_i\times\dot{\vec p}_i = \sum_i\vec r_i\times\vec F_i,$$

第一项因 $\dot{\vec r}_i$ 与 $m_i\dot{\vec r}_i$ 平行而为零。代入力的分解，内力力矩部分成对归组（再用一次弱版把 $\vec F_{ij}$ 换成 $-\vec F_{ji}$）：

$$\sum_{i\neq j}\vec r_i\times\vec F_{ji} = \frac12\sum_{i\neq j}\bigl(\vec r_i\times\vec F_{ji} + \vec r_j\times\vec F_{ij}\bigr) = \frac12\sum_{i\neq j}\bigl(\vec r_i - \vec r_j\bigr)\times\vec F_{ji}.$$

**强版在此登场**：$(\vec r_i - \vec r_j)\times\vec F_{ji} = \vec 0$ 当且仅当内力沿两质点连线；弱版对此无能为力——一对等值反向但不共线的内力组成力偶，总动量不变而总角动量凭空改变（哑铃形物体被内力矩带着自旋加速）。强版保证求和逐项为零，于是 $\dot{\vec L} = \sum_i\vec r_i\times\vec F_i^{(\text{外})} = \vec\tau^{(\text{外})}$。

</details>

**2.** 平面双摆：数清约束与自由度，选取广义坐标，写出两质点直角坐标用广义坐标的表达式。

<details markdown="1"><summary>点击显示答案</summary>

两质点共 6 个直角坐标 $(x_1, y_1, z_1, x_2, y_2, z_2)$，悬挂点取为原点，运动平面取 $z = 0$。约束共四条：

$$z_1 = 0, \qquad z_2 = 0, \qquad x_1^2 + y_1^2 = l_1^2, \qquad (x_2 - x_1)^2 + (y_2 - y_1)^2 = l_2^2,$$

前两条来自"限于平面"，后两条是两杆长度固定（均为完整、定常约束）。故 $k = 4$，自由度 $n = 3\times 2 - 4 = 2$。

取广义坐标为两杆相对竖直向下方向的偏角 $\theta_1, \theta_2$：

$$\begin{aligned} x_1 &= l_1\sin\theta_1, & y_1 &= -l_1\cos\theta_1,\\ x_2 &= l_1\sin\theta_1 + l_2\sin\theta_2, & y_2 &= -l_1\cos\theta_1 - l_2\cos\theta_2. \end{aligned}$$

直接代入可验四条约束成为恒等式——这就是"约束已被参数化自动消化"的含义。注意广义坐标的量纲是角度而非长度；两个角度各以 $2\pi$ 为周期，$(\theta_1, \theta_2)$ 的位形空间是一个二维环面。

</details>

**3.** 珠子穿在半径 $R$ 的光滑圆环上，圆环以角速度 $\omega$ 绕竖直直径匀速转动。写出约束；区分虚位移与实位移；取广义坐标 $\theta$（相对转轴的极角），验证环对珠子支持力的虚功为零，并说明其实功为何不为零。

<details markdown="1"><summary>点击显示答案</summary>

以环心为原点、转轴为 $z$ 轴取球坐标。珠子在时刻 $t$ 被限制在环面上且在环丝所在的旋转子午面内，两条约束：

$$r = R, \qquad \varphi = \omega t,$$

第二条显含时间——非定常约束。自由度 $3 - 2 = 1$，取 $q = \theta$：

$$\vec r = R\bigl(\sin\theta\cos\omega t\,\hat{\vec e}_x + \sin\theta\sin\omega t\,\hat{\vec e}_y + \cos\theta\,\hat{\vec e}_z\bigr).$$

**实位移**：把时间放开，

$$\mathrm d\vec r = R\,\mathrm d\theta\,\hat{\vec e}_\theta + R\omega\sin\theta\,\mathrm dt\,\hat{\vec e}_\varphi,$$

第二项是环丝转动对珠子的拖曳——即使珠子相对环不动（$\mathrm d\theta = 0$），也被环带着绕轴转。

**虚位移**：冻结时间（$\delta t = 0$），环丝就地凝固，珠子只能沿丝的瞬时切向滑动：

$$\delta\vec r = R\,\delta\theta\,\hat{\vec e}_\theta,$$

没有 $\hat{\vec e}_\varphi$ 分量。这就是非定常约束下"虚位移 $\neq$ 实位移"的标准实例。

**理想约束验证**：环丝光滑意味着支持力垂直于丝，即无 $\hat{\vec e}_\theta$ 分量，$\vec N = N_r\hat{\vec e}_r + N_\varphi\hat{\vec e}_\varphi$。虚功

$$\vec N\cdot\delta\vec r = \bigl(N_r\hat{\vec e}_r + N_\varphi\hat{\vec e}_\varphi\bigr)\cdot R\,\delta\theta\,\hat{\vec e}_\theta = 0$$

恒成立。但**实功率** $\vec N\cdot\dot{\vec r} = N_\varphi\,R\omega\sin\theta \neq 0$：正是这个 $\varphi$ 向分量维持珠子随环转动，能量由驱动电机经约束力灌入（或抽出）珠子。所以"理想约束不做功"的准确说法是**虚功为零**；非定常理想约束的实功可以非零，珠子的机械能不守恒。

</details>

**4.** Atwood 机：轻滑轮两侧挂 $m_1, m_2$，绳不可伸长。用 d'Alembert 原理求运动方程，全程不得引入张力。

<details markdown="1"><summary>点击显示答案</summary>

取 $x_1, x_2$ 为两质量自滑轮竖直向下的坐标。绳不可伸长给出约束

$$x_1 + x_2 = \ell \;\Longrightarrow\; \delta x_2 = -\delta x_1, \qquad \ddot x_2 = -\ddot x_1.$$

先验理想约束：绳对两质量的约束力均为张力 $-T$（向上），总虚功

$$(-T)\,\delta x_1 + (-T)\,\delta x_2 = -T\bigl(\delta x_1 + \delta x_2\bigr) = 0,$$

约束力自动退场。主动力只有重力 $m_1 g$、$m_2 g$（向下为正）。d'Alembert 原理给出

$$\bigl(m_1 g - m_1\ddot x_1\bigr)\,\delta x_1 + \bigl(m_2 g - m_2\ddot x_2\bigr)\,\delta x_2 = 0.$$

代入 $\delta x_2 = -\delta x_1$ 与 $\ddot x_2 = -\ddot x_1$：

$$\Bigl[\bigl(m_1 g - m_1\ddot x_1\bigr) - \bigl(m_2 g + m_2\ddot x_1\bigr)\Bigr]\delta x_1 = 0.$$

$\delta x_1$ 任意，方括号必须为零：

$$(m_1 + m_2)\,\ddot x_1 = (m_1 - m_2)\,g \;\Longrightarrow\; \ddot x_1 = \frac{m_1 - m_2}{m_1 + m_2}\,g.$$

检验：$m_1 = m_2$ 时 $\ddot x_1 = 0$（平衡）；$m_2 = 0$ 时 $\ddot x_1 = g$（自由落体）。对照牛顿解法（两条方程加未知张力 $T$ 再消去），d'Alembert 路线一步到结果——$T$ 从头到尾没有出场。

</details>

**5.** 完成 d'Alembert 原理到广义坐标运动方程的完整推导，并指出"$\delta q_j$ 相互独立"在收尾一步的作用。

<details markdown="1"><summary>点击显示答案</summary>

从 d'Alembert 原理出发（理想约束已使约束力退场，$\vec F_i$ 均指主动力）：

$$\sum_i\bigl(\vec F_i - \dot{\vec p}_i\bigr)\cdot\delta\vec r_i = 0, \qquad \delta\vec r_i = \sum_j\frac{\partial\vec r_i}{\partial q_j}\,\delta q_j.$$

**主动力项**：$\sum_i\vec F_i\cdot\delta\vec r_i = \sum_j Q_j\,\delta q_j$，其中 $Q_j = \sum_i\vec F_i\cdot\partial\vec r_i/\partial q_j$。

**惯性项**：固定 $j$，用乘积法则把 $\dot{\vec p}_i$ 拆开：

$$\dot{\vec p}_i\cdot\frac{\partial\vec r_i}{\partial q_j} = \frac{\mathrm d}{\mathrm dt}\Bigl(\vec p_i\cdot\frac{\partial\vec r_i}{\partial q_j}\Bigr) - \vec p_i\cdot\frac{\mathrm d}{\mathrm dt}\frac{\partial\vec r_i}{\partial q_j}.$$

由 $\vec r_i = \vec r_i(q, t)$ 得 $\dot{\vec r}_i = \sum_k\frac{\partial\vec r_i}{\partial q_k}\dot q_k + \frac{\partial\vec r_i}{\partial t}$，它对 $\dot q$ 线性，系数只含 $(q, t)$，于是两个引理成立：

（引理 A）$\dfrac{\partial\dot{\vec r}_i}{\partial\dot q_j} = \dfrac{\partial\vec r_i}{\partial q_j}$；（引理 B）$\dfrac{\mathrm d}{\mathrm dt}\dfrac{\partial\vec r_i}{\partial q_j} = \sum_k\dfrac{\partial^2\vec r_i}{\partial q_k\,\partial q_j}\dot q_k + \dfrac{\partial^2\vec r_i}{\partial t\,\partial q_j} = \dfrac{\partial\dot{\vec r}_i}{\partial q_j}$。

代入（记 $\vec p_i = m_i\dot{\vec r}_i$）：

$$\begin{aligned} \vec p_i\cdot\frac{\partial\vec r_i}{\partial q_j} &\overset{A}{=} m_i\dot{\vec r}_i\cdot\frac{\partial\dot{\vec r}_i}{\partial\dot q_j} = \frac{\partial}{\partial\dot q_j}\Bigl(\frac12 m_i\dot{\vec r}_i^{\,2}\Bigr),\\ \vec p_i\cdot\frac{\mathrm d}{\mathrm dt}\frac{\partial\vec r_i}{\partial q_j} &\overset{B}{=} m_i\dot{\vec r}_i\cdot\frac{\partial\dot{\vec r}_i}{\partial q_j} = \frac{\partial}{\partial q_j}\Bigl(\frac12 m_i\dot{\vec r}_i^{\,2}\Bigr). \end{aligned}$$

对 $i$ 求和，动能 $T = \frac12\sum_i m_i\dot{\vec r}_i^{\,2}$ 浮现：

$$\sum_i\dot{\vec p}_i\cdot\delta\vec r_i = \sum_j\Bigl[\frac{\mathrm d}{\mathrm dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j}\Bigr]\delta q_j.$$

**合并与收尾**：

$$\sum_j\Bigl[\frac{\mathrm d}{\mathrm dt}\frac{\partial T}{\partial\dot q_j} - \frac{\partial T}{\partial q_j} - Q_j\Bigr]\delta q_j = 0 \qquad \text{对一切}\ \delta q_j\ \text{成立}.$$

独立性在这一步**不可替代**：完整约束下 $q_1, \dots, q_n$ 是把约束消化干净后的独立参数，$\delta q_j$ 可以各自独立取值——先只变动 $\delta q_1$ 而令其余为零，得第一个方括号为零，依此类推，$n$ 条方程全部到手。若坐标仍被约束捆绑（非完整约束或用了多余坐标），就只有系数整体为零，得不到逐条方程——那时须引入 Lagrange 乘子，而那恰恰是把约束力重新请回方程的方法。

</details>

## 参考

- L. D. Landau & E. M. Lifshitz《力学》（卷 1）§1–§5：广义坐标、最小作用量与 Galileo 相对性原理——本书第 5 章 Landau 路线的原本，对照本章第 5.5 节读。
- H. Goldstein《Classical Mechanics》（3rd ed.）第 1 章：质点系、约束分类、虚位移与 d'Alembert 原理、广义坐标方程推导——本章第 3–5 节的主参考。
- 梁昆淼《力学（下册）理论力学》第 1 章：牛顿力学的回顾、d'Alembert 原理与广义坐标的中文对照表述。
- V. I. Arnold《经典力学的数学方法》§1–§2：位形空间与约束的几何观点（进阶，本章第 4.3 节的深化）。
