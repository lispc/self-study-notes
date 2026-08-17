# 凝聚态物理入门导论

> 面向有本科量子力学基础的自学者。主线观点：**凝聚态物理是场论思想的应用现场**——声子是场量子化、Fermi 液体是准粒子、超导是自发对称性破缺、临界现象是重整化群。本书与[量子场论路线图](../qft-sm/README.md)的笔记大量互相引用。
>
> 参考书主线：Kittel《固体物理导论》打底 + Ashcroft & Mermin 查细节；拓扑部分参考 Asbóth 短讲义、Bernevig《Topological Insulators》。

---

## 目录

### 第一部分：结构与无相互作用电子（骨架）

1. 晶体结构：晶格与基元、倒格子、Brillouin 区、X 射线衍射 *(待写)*
2. [晶格振动与声子](docs/02-lattice-vibrations-phonons.md)：单/双原子链、声子量子化、热容（Einstein/Debye）
3. 金属自由电子气：Drude、Sommerfeld、费米面与态密度 *(待写)*
4. [能带论](docs/04-band-theory.md)：Bloch 定理、近自由电子、紧束缚、金属/绝缘体判据
5. 半导体浅尝：有效质量、载流子统计、pn 结 *(待写)*

### 第二部分：相互作用、序与相变（核心物理）

6. [相互作用电子气](docs/06-interacting-electron-gas.md)：Hartree–Fock、屏蔽与等离激元、Fermi 液体
7. [磁性](docs/07-magnetism.md)：交换作用、Ising/Heisenberg 模型、平均场、自旋波
8. [超导](docs/08-superconductivity.md)：London 方程、Cooper 对、BCS、作为"光子获质量"的迈斯纳效应
9. [相变与临界现象](docs/09-phase-transitions-criticality.md)：Landau 理论、临界指数、普适性、Wilson 重整化群（[补充阅读：二维 Ising 模型——最简单的相变系统及其数学](docs/09s-2d-ising-model.md)）

### 第三部分：现代专题

10. 量子输运浅尝：Landauer 公式、电导量子化 *(待写)*
11. [量子 Hall 效应](docs/11-quantum-hall-effect.md)：Landau 能级、精确量子化、边缘态、Laughlin 论证
12. [拓扑物态入门](docs/12-topological-phases.md)：Berry 相、SSH 模型、TKNN/Chern 数、拓扑绝缘体
13. [强关联浅尝](docs/13-strong-correlations.md)：Mott 绝缘体、Hubbard 模型、超交换、高温超导悬案

## 与 QFT 书的接口

- 第 2 章（声子）←→ [谐振子代数解法](../qft-sm/docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)、[标量场量子化](../qft-sm/docs/stage-04-qft-core/01-scalar-field-quantization.md)
- 第 6 章（Fermi 液体）←→ [一圈修正与重整化](../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)（准粒子与穿衣粒子）
- 第 7、8 章（磁性、超导）←→ 自发对称性破缺、Goldstone、希格斯机制（[电弱统一](../qft-sm/docs/stage-06-standard-model/02-electroweak-unification.md)）
- 第 9 章（重整化群）←→ [Wilson 有效理论视角](../qft-sm/docs/stage-04-qft-core/06-one-loop-renormalization.md)
