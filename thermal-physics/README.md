# 热力学与统计力学

> 面向有本科量子力学基础的自学者（量子力学见[量子力学书](../quantum-mechanics/README.md)）。主线观点：**热力学与统计力学是同一理论的两种读法**——宏观唯象给出定律，微观统计给出定律的理由，公理化给出定律的最终形态。结构据此安排：现象热力学压成薄层开路（只讲宏观可测量的东西，并留下宏观理论答不了的问题）→ 微观统计为主体（量子为本、经典统计作为高温低密度极限，直接复用量子力学书的密度矩阵语言）→ 公理化与基础问题封顶（熵公设、各态历经、时间之箭）。本书是[凝聚态物理导论](../condensed-matter/README.md)与[QFT 路线图](../qft-sm/README.md)中全部统计工具的源头。
>
> 参考主线教材：Schroeder《An Introduction to Thermal Physics》打底 + Pathria & Beale《Statistical Mechanics》查细节；公理化部分参考 Callen《Thermodynamics and an Introduction to Thermostatistics》；基础问题部分参考 Jaynes 文集与 Lebowitz 综述（Rev. Mod. Phys. 71, S346 (1999)）。

---

## 目录

编号留有空位，便于日后插入；未挂链接的条目是待写章节。

### 第一部分：现象热力学（宏观唯象，薄层开路）

1. 热平衡与温度：第零定律、状态量与过程、理想气体与 van der Waals 状态方程
2. 第一定律：功、热与内能——Joule 实验、热容、绝热过程
3. 第二定律：热机与 Carnot 循环、Clausius 不等式、熵作为态函数
4. 热力学势与 Maxwell 关系：自由能、焓、化学势、响应函数——宏观层面能说的说完，盘点它答不了的三个问题

### 第二部分：统计力学基础（微观主体）

6. 概率与计数：大数定律、二项分布与 Stirling 公式、相空间与态密度
7. 微正则系综：Boltzmann 熵 $S = k_B \ln \Gamma$、温度的微观定义、热接触与熵增原理
8. 正则系综：Boltzmann 因子、配分函数、能量涨落与系综等价
9. 经典理想气体：Maxwell 速度分布、能量均分及其失败、Gibbs 佯谬
10. 巨正则系综与化学势：开放系统、巨势、粒子数涨落
11. 量子系综：密度矩阵与正则密度算符（语言准备见[量子力学书第 10 篇](../quantum-mechanics/docs/10-linear-response-kubo.md)）
12. 量子统计：Fermi–Dirac 与 Bose–Einstein 分布的正面推导与初步应用（逻辑地基见[量子力学书 9s](../quantum-mechanics/docs/09s-fermi-dirac-derivation.md)）
13. 光子气体与黑体辐射：Planck 定律、Stefan–Boltzmann 定律、宇宙微波背景
14. Bose–Einstein 凝聚：凝聚温度、宏观占据、序参量图像

### 第三部分：公理化与基础问题（封顶）

16. 热力学的公理化重构：Callen 熵公设、凸性、勒让德变换与稳定性——第一部分的严格重读（附 Lieb–Yngvason 现代公理化简介）
17. 涨落理论：Einstein 涨落公式、高斯涨落、涨落与响应函数的对照
18. 平衡从何而来：各态历经问题、混合、典型性、本征态热化假说（ETH）
19. 不可逆性与时间之箭：Loschmidt 可逆性佯谬、Zermelo 回归佯谬、Boltzmann 的概率解答与低熵过去假设
20. 信息热力学：Maxwell 妖、Szilard 引擎、Landauer 原理、Jarzynski 等式与涨落定理

### 第四部分：相互作用与相变入门

22. 相互作用经典气体：van der Waals 方程的微观推导、virial 展开
23. Ising 模型与平均场：一维传递矩阵精确解、平均场近似、关联与涨落（二维 Onsager 解见[凝聚态书 9s](../condensed-matter/docs/09s-2d-ising-model.md)）
24. 临界现象与普适性：序参量、临界指数、标度假说（重整化群见[凝聚态书第 9 章](../condensed-matter/docs/09-phase-transitions-criticality.md)）

### 第五部分：非平衡浅尝

26. Boltzmann 输运方程：碰撞项与分子混沌假设、H 定理、弛豫时间近似（在金属中的应用见[凝聚态书第 3 章](../condensed-matter/docs/03-free-electron-gas.md)）
27. 线性响应与涨落–耗散：Onsager 倒易关系、Brown 运动与 Einstein 关系（严格量子形式见[量子力学书第 10 篇](../quantum-mechanics/docs/10-linear-response-kubo.md)，量子输运见[凝聚态书第 10 章](../condensed-matter/docs/10-quantum-transport.md)）

## 与其他书的接口

- 上游是[量子力学书](../quantum-mechanics/README.md)：第 11 章复用其密度矩阵语言；第 12 章的费米/玻色分布与 [9s](../quantum-mechanics/docs/09s-fermi-dirac-derivation.md) 互补——那里问"凭什么"，这里算"怎么用"。
- 下游是[凝聚态书](../condensed-matter/README.md)：Fermi–Dirac 分布在[第 3 章](../condensed-matter/docs/03-free-electron-gas.md)投入使用；声子热容（Einstein/Debye）留在凝聚态书[第 2 章](../condensed-matter/docs/02-lattice-vibrations-phonons.md)，本书不重复；相变写到临界指数为止，重整化群在[第 9 章](../condensed-matter/docs/09-phase-transitions-criticality.md)；Boltzmann 方程的金属应用与量子输运分别在[第 3 章](../condensed-matter/docs/03-free-electron-gas.md)与[第 10 章](../condensed-matter/docs/10-quantum-transport.md)。
- 与[QFT 书](../qft-sm/README.md)的接口：配分函数 $Z$ 与路径积分的虚时形式是同一对象（Wick 转动后温度对应虚时周期），见[路径积分笔记](../qft-sm/docs/stage-04-qft-core/07-path-integral.md)——QFT 与临界现象共享同一套数学。
- 第 20 章的 Landauer 原理与[数字电路书](../digital-design/README.md)联动：计算能耗的物理下限。
