# 凝聚态物理入门导论

> 面向有本科量子力学基础的自学者。主线观点：**凝聚态物理是场论思想的应用现场**——声子是场量子化、Fermi 液体是准粒子、超导是自发对称性破缺、临界现象是重整化群。本书与[量子场论路线图](../qft-sm/README.md)的笔记大量互相引用。
>
> 参考书主线：Kittel《固体物理导论》打底 + Ashcroft & Mermin 查细节；拓扑部分参考 Asbóth 短讲义、Bernevig《Topological Insulators》。

---

## 目录

### 第一部分：结构与无相互作用电子（骨架）

1. 晶体结构：晶格与基元、倒格子、Brillouin 区、X 射线衍射 *(待写)*
2. [晶格振动与声子](docs/02-lattice-vibrations-phonons.md)：单/双原子链、声子量子化、热容（Einstein/Debye）
3. [金属自由电子气](docs/03-free-electron-gas.md)：Drude、Sommerfeld、费米海与态密度
4. [能带论](docs/04-band-theory.md)：Bloch 定理、近自由电子、紧束缚、金属/绝缘体判据
5. 半导体浅尝：有效质量、载流子统计、pn 结 *(待写)*

### 第二部分：相互作用、序与相变（核心物理）

6. [相互作用电子气](docs/06-interacting-electron-gas.md)：Hartree–Fock、屏蔽与等离激元、Fermi 液体
7. [磁性](docs/07-magnetism.md)：交换作用、Ising/Heisenberg 模型、平均场、自旋波（[补充材料：为什么铁有磁性而铜、铝没有](docs/07s-why-iron-magnetic.md)）
8. [超导](docs/08-superconductivity.md)：London 方程、Cooper 对、BCS、作为"光子获质量"的迈斯纳效应
9. [相变与临界现象](docs/09-phase-transitions-criticality.md)：Landau 理论、临界指数、普适性、Wilson 重整化群（[补充阅读：二维 Ising 模型——最简单的相变系统及其数学](docs/09s-2d-ising-model.md)）

### 第三部分：现代专题

10. 量子输运浅尝：Landauer 公式、电导量子化 *(待写)*
11. [量子 Hall 效应](docs/11-quantum-hall-effect.md)：Landau 能级、精确量子化、边缘态、Laughlin 论证（[补充材料：分数量子霍尔效应与任意子](docs/11s-fractional-quantum-hall.md)）
12. [拓扑物态入门](docs/12-topological-phases.md)：Berry 相、SSH 模型、TKNN/Chern 数、拓扑绝缘体（[补充材料：拓扑序——长程纠缠、规范结构与弦网](docs/12s-topological-order.md)）
13. [强关联浅尝](docs/13-strong-correlations.md)：Mott 绝缘体、Hubbard 模型、超交换、高温超导悬案

### 第四部分：多电子问题怎么算——近似阶梯（计算方法）

14. [多电子问题与精确解](docs/14-exact-methods-fci-ed.md)：基组、Slater–Condon 规则、FCI 与指数墙、H₂ 显微镜、ED 与符号问题（[补充材料：高斯基组与双体积分求值](docs/14s-gaussian-integrals.md)）
15. [HF 之后](docs/15-post-hf-mp2-cc.md)：相关能、Brillouin 定理与 MP2、Goldstone 图、大小一致性、耦合簇 CCSD(T)
16. [密度泛函理论](docs/16-dft.md)：Hohenberg–Kohn、Kohn–Sham、泛函阶梯、能隙问题与失灵清单
17. [超越 DFT](docs/17-beyond-dft-gw-dmft.md)：格林函数与 Dyson 方程、屏蔽自能 GW、动力学平均场 DMFT、方法地图
18. [多参考与 CASSCF](docs/18-multireference-casscf.md)：活性空间、静态相关的正面强攻、CASPT2/NEVPT2、磁交换常数接口
19. [激发态方法](docs/19-excited-states.md)：线性响应与 RPA、EOM-CC、TD-DFT 与 Casida 方程、Bethe–Salpeter
20. [DMRG 与张量网络](docs/20-dmrg-tensor-networks.md)：纠缠面积律、矩阵乘积态、扫掠变分、化学活性空间
21. [嵌入方法](docs/21-embedding-methods.md)：QM/MM、DFT+U、子系统 DFT、DMET——分而治之收官

## 与 QFT 书的接口

- 第 2 章（声子）←→ [谐振子代数解法](../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)、[标量场量子化](../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)
- 第 6 章（Fermi 液体）←→ [一圈修正与重整化](../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)（准粒子与穿衣粒子）
- 第 7、8 章（磁性、超导）←→ 自发对称性破缺、Goldstone、希格斯机制（[电弱统一](../qft-sm/docs/stage-06-standard-model/02-electroweak-unification.md)）
- 第 9 章（重整化群）←→ [Wilson 有效理论视角](../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)
- 第 15、17 章（微扰图、Dyson 方程与自能）←→ [一圈修正与重整化](../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)（Goldstone/连接簇定理 ↔ 费曼图；自能 ↔ 传播子重整化）
