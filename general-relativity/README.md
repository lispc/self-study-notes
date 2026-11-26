# 广义相对论

> 面向学过[理论力学](../classical-mechanics/README.md)（拉格朗日/哈密顿形式与约束理论）与[电动力学](../electrodynamics/README.md)（张量记号与狭义相对论）的自学者，与[量子力学书](../quantum-mechanics/README.md)并行，无先后要求。主线观点：**广义相对论是"时空几何即引力"的实现，而它的约束/哈密顿结构是所有量子引力纲领的公共入口**——本书经典内容收尾于三件面向量子化的事：零超曲面几何（生成元、膨胀与剪切、Raychaudhuri 方程）、带边界的作用量（GHY/零边界/角点项）、约束与协变相空间（ADM、辛势、Wald 荷与边缘模）。终点定位：为[QFT 书](../qft-sm/README.md)第 8 阶段（量子引力导览）提供几何底座，并作为其第 9 阶段（代数量子引力专题）的直接前置。
>
> 参考主线教材：Carroll《Spacetime and Geometry》（入门主线）；Wald《General Relativity》（严格参考）；Poisson《A Relativist's Toolkit》（第 7–10 章零几何与边界专题的母本）。

---

## 目录

编号留有空位，便于日后插入；未挂链接的条目是待写章节。

**约定**：度规号差 $\eta = \mathrm{diag}(-,+,+,+)$（Wald/Carroll 及量子引力文献的惯例，与 QFT 书的 $(+1,-1,-1,-1)$ 相反，对照在首次出现处给出）；默认 $c = 1$、显式保留 $G_N$，涉及量子化时恢复 $\hbar$。

### 第一部分：微分几何工具

1. [流形与张量](docs/01-manifolds-and-tensors.md)：流形、曲线与切矢量、余矢量、度规张量——"引力 = 时空几何"的舞台；含 $(-,+,+,+)$ 与 QFT 书号差的翻译表、固有时作为时钟读数
2. [联络与测地线](docs/02-connection-and-geodesics.md)：克氏符的推导（度量相容 + 无挠 ⇒ 唯一）、平行移动与和乐（球面上的转角 = 所围面积）、测地线方程与仿射参数、"类时测地线使固有时极大"与等效原理
3. [曲率](docs/03-curvature.md)：$[\nabla,\nabla]$ 定义 Riemann、四条对称性与 20 个分量、第二 Bianchi ⇒ $\nabla_\mu G^{\mu\nu}=0$、Weyl 张量与潮汐力、测地偏离、Killing 矢量
4. [微分形式与积分](docs/04-differential-forms-and-integration.md)：外积与外微分（$\mathrm{d}$ 不需要联络）、体积形式与 Hodge 对偶（$\star^2=-1$ 于 2-形式）、Stokes、Maxwell 两行、作用量的形式语言——一阶引力与规范理论的书写语言

### 第二部分：动力学与解

5. [Einstein 方程与 Einstein–Hilbert 作用量](docs/05-einstein-equations-eh-action.md)：为什么左边必须是 $G_{\mu\nu}$（二阶/对称/恒无散/4 维唯一）、能动张量与理想流体、EH 变分与 GHY、弱场极限给 $\nabla^2\Phi=4\pi G_N\rho$、$\Lambda$ 的三种身份、10 = 6 + 4 的初值计数
5s. [一阶引力：标架、自旋联络与 Plebański 作用量](docs/05s-first-order-gravity.md)：度规换成 tetrad + 自旋联络，Palatini 作用量的两个变分（$T=0$ 与 Einstein 方程），BF + 简单性约束 $B=\star(e\wedge e)$——"约束不含导数 ⇒ 不加边界项 ⇒ 边界变量可缝合"，零锥量子化（QFT 书第 9 阶段）的出发点
6. [Schwarzschild 解与黑洞几何](docs/06-schwarzschild.md)：球对称 ansatz 解出 $f=1-2G_NM/r$、Birkhoff 定理、Kretschmann 判据（$r=2G_NM$ 非奇异）、Kruskal 延拓与四区域、有效势与 ISCO $6G_NM$、光线偏折 $4G_NM/b$、视界面积与 $T,S$ 预告
7. [因果结构](docs/07-causal-structure.md)：光锥与因果序、全局双曲与 Cauchy 面、因果菱形（两张零片 + caps + 角点 $S$）——$I^\pm$/$J^\pm$、依赖域、MOTS，"零锥量子化"的舞台为何是菱形
8. [零超曲面几何](docs/08-null-hypersurface-geometry.md)：零生成元与仿射参数、横向度规 $q_{ab}$、膨胀/剪切/扭转、Raychaudhuri 方程与聚焦、面积振幅 $\varrho$ 的 ODE ——"引力时钟"与"面积上界"的物理核心，全书面向量子化目标的第一块基石
9. 特征初值问题：零锥上的初始数据、double null 片、解的存在性与延拓——"在零锥上解约束"的存在性依据

### 第三部分：边界、约束与相空间（面向量子化）

10. [带边界的作用量](docs/10-boundary-terms-action.md)：GHY 边界项与 Dirichlet 变分原理、Brown–York 张量与 ADM 质量、零边界为什么没有 GHY（$\sqrt h=0$）、$\int\sqrt q\,\Theta$ 是全导数 ⇒ 角点项、缝合时 GHY 相消
11. ADM 哈密顿形式与约束：超哈密顿约束与动量约束、时间问题（与[QFT 书量子引力导览的自检题 4](../qft-sm/docs/stage-08-quantum-gravity/01-why-quantum-gravity-is-hard.md)的参数化粒子玩具模型对上）
12. [协变相空间与守恒荷](docs/12-covariant-phase-space.md)：预辛势 $\theta$、辛流形式 $\omega=\delta\theta$、$\Omega$ 与切片无关、$\delta H_\xi=\int_{\partial\Sigma}Q_\xi$、Komar 质量与 Wald 熵 $S=2\pi\oint Q=A/4G$、边缘模与角点 boost 荷 $K=\mathcal A/8\pi G$——经典侧收官章，QFT 书第 9 阶段的直接前置

### 第四部分：黑洞热力学（桥接量子）

13. 黑洞热力学初步：黑洞力学四定律、Hawking 温度与熵（概念级；量子细节见 QFT 书第 9 阶段的弯曲时空篇）
14. （选学）2+2 分解与 double null 叶层

## 与其他书的接口

- 上游是[理论力学书](../classical-mechanics/README.md)：第 9/10 章（哈密顿方程、Poisson 括号、辛结构）与第 12 章（约束系统与 Dirac 理论）是本书第三部分的直接前置。
- 上游是[电动力学书](../electrodynamics/README.md)：第 11–12 章（Lorentz 变换、四维矢量与张量）是本书第一部分的语言起点——狭义相对论就是"度规取 $\eta$ 的特例"，本书把 $\eta$ 换成动力学变量。
- 下游是[QFT 书](../qft-sm/README.md)：第 8 阶段导览只假定读者知道 $S_{\mathrm{EH}}$ 的样子；第 9 阶段（代数量子引力专题）假定读者读过本书第 7、8、10、11、12 章。
- 与[论文阅读专栏](../paper-reading/README.md)：首篇（arXiv:2611.34924）以本书第 5s、7、8、10、12 章为几何前置——五章已写完，构成"从一阶引力到角点荷"的完整经典链。
- 与[热统书](../thermal-physics/README.md)：第 13 章的黑洞熵是 $S = k_B\ln\Gamma$ 在引力系统里的化身，微观起源的量子计算留给 QFT 书第 9 阶段。
