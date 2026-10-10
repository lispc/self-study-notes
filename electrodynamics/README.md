# 电动力学

> 面向学过普物电磁学与理论力学的自学者（力学前置见[理论力学书](../classical-mechanics/README.md)）。主线观点：**电动力学是"场"概念与狭义相对论的诞生地**——从平方反比定律长出场，从场长出一组自治的方程，而从这组方程与 Galileo 相对性的冲突里长出狭义相对论；本书以 Maxwell 方程组的建立为中场、以协变电动力学收官，把接力棒交给 [QFT 书的协变电磁学](../qft-sm/docs/stage-03-relativistic-qm/03-covariant-electromagnetism.md)。单位制：**高斯制为主线**（Maxwell 方程组最干净的形式，与 QFT/凝聚态两书无缝衔接），SI 对照收进附录章。
>
> 参考主线教材：Griffiths《Introduction to Electrodynamics》（入门主线）；Jackson《Classical Electrodynamics》（查细节与严格推导）；Landau & Lifshitz 卷 2《场论》（相对论与辐射部分的骨架）。

---

## 目录

编号留有空位，便于日后插入；未挂链接的条目是待写章节。

### 第一部分：静电与静磁（场的数学）

1. 库仑定律与电场：叠加原理、Gauss 定理、静电势与"旋度为零"的含义
2. 静电边值问题：唯一性定理、镜像法、分离变量与特殊函数浅尝
3. 多极展开与电介质：电偶极、极化、束缚电荷的图像
4. 静磁场：Biot–Savart 定律、Ampère 定律、矢势与规范自由的初现、磁介质

### 第二部分：Maxwell 方程组

6. 电磁感应与位移电流：Faraday 定律、Ampère–Maxwell 修正——方程组在此闭合
7. 场的守恒律：Poynting 矢量、场的能量、动量与角动量、Maxwell 应力张量
8. 电磁波：真空与介质中的平面波、偏振、界面反射折射；波导浅尝

### 第三部分：狭义相对论（方程组的裁判）

10. Maxwell 理论与 Galileo 相对性的冲突：以太假说、Michelson–Morley 实验、Einstein 的两条公设
11. 狭义相对论运动学：Lorentz 变换、四维矢量与张量记号、时钟与量杆的物理
12. 电动力学的协变形式：$F_{\mu\nu}$ 与规范势 $A_\mu$、Maxwell 方程组的四维写法、带电粒子的拉格朗日形式——[QFT 书协变电磁学](../qft-sm/docs/stage-03-relativistic-qm/03-covariant-electromagnetism.md)从这里接手

### 第四部分：辐射与场的反作用

14. 推迟势与 Liénard–Wiechert 势：运动电荷的场——"速度的场"与"加速度的场"
15. 辐射：电偶极辐射、Larmor 公式、轫致辐射浅尝；辐射反作用与自力的困难——经典电动力学的边界，也是 QED 存在的理由（[QFT 书第 4 阶段](../qft-sm/README.md)）

### 附录

16. 单位制对照：高斯制 ↔ SI 的公式翻译与量纲检查；与 [QFT 书](../qft-sm/README.md)自然单位（$\hbar = c = 1$）的衔接

## 与其他书的接口

- 上游是[理论力学书](../classical-mechanics/README.md)：第 12 章的带电粒子拉格朗日形式是力学书框架的直接应用。
- 下游第一站是[量子力学书](../quantum-mechanics/README.md)：经典电动力学预言黑体辐射的紫外灾难，正是[旧量子论](../quantum-mechanics/docs/01-old-quantum-theory.md)（以及[热统书](../thermal-physics/README.md)光子气体一章）的开场；氢原子的经典辐射坍缩同样是量子力学的接生婆。
- 通向[QFT 书](../qft-sm/README.md)：[协变电磁学](../qft-sm/docs/stage-03-relativistic-qm/03-covariant-electromagnetism.md)与本书第 12 章衔接；规范自由在那里升级为规范原理（[整体对称与规范对称](../qft-sm/docs/stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)、[Yang–Mills](../qft-sm/docs/stage-06-standard-model/01-yang-mills.md)）；第 15 章辐射反作用的经典困难是 QED 的存在理由。
- 与[热统书](../thermal-physics/README.md)：黑体辐射是经典统计与经典场的碰撞现场。
