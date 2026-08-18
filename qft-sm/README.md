# 量子场论与标准模型自学路线图

> 面向已有**本科理工科数学物理基础**（微积分、线性代数、常微分/偏微分方程、复变函数、普物）的自学者。
> 目标：达到能真正"理解"量子场论（QFT）与标准模型（SM）的水平——即能独立完成标志性计算、读懂相关论文的物理内容。
>
> **总时间预算**：全职约 1.5–2 年；业余每周 10 小时约 3–4 年。这是正常速度，不必因此沮丧。

---

## 目录

- [第 0 阶段：数学补课（与物理并行）](#第-0-阶段数学补课与物理并行)
- [第 1 阶段：分析力学 + 狭义相对论](#第-1-阶段分析力学--狭义相对论12-个月)
- [第 2 阶段：量子力学（最关键的一关）](#第-2-阶段量子力学36-个月最关键的一关)
- [第 3 阶段：经典场论 + 相对论量子力学（过渡桥梁）](#第-3-阶段经典场论--相对论量子力学12-个月过渡桥梁)
- [第 4 阶段：量子场论核心（主战场）](#第-4-阶段量子场论核心612-个月主战场)
- [第 5 阶段：对称性与群论补课](#第-5-阶段对称性与群论补课与第-4-阶段后期并行)
- [第 6 阶段：标准模型本身](#第-6-阶段标准模型本身36-个月)
- [实用建议](#实用建议)
- [最小书单](#最小书单)
- [终点自测](#终点自测)

---

## 第 0 阶段：数学补课（与物理并行）

不要单独憋半年学数学，按需补：

- **群论基础**：群的定义、[SO(3)/SU(2) 与角动量的关系](docs/stage-00-math/01-so3-su2-and-angular-momentum.md)、李群/李代数的概念。初期只需"会用"，严格的表示论后面再补。
- **张量与指标运算**：爱因斯坦求和约定、闵可夫斯基度规 η_μν、逆变/协变指标。这是 QFT 的日常书写语言，一周就能上手。
- **变分原理**：泛函导数、欧拉–拉格朗日方程（在经典力学的拉格朗日形式里自然学到）。

## 第 1 阶段：分析力学 + 狭义相对论（1–2 个月）

内容：

- 拉格朗日/哈密顿形式
- **诺特定理**（对称性 ↔ 守恒律——这是整个标准模型的思想骨架）
- 洛伦兹变换、四维矢量、相对论性运动学

教材：Goldstein《经典力学》前几章，或朗道《力学》、梁昆淼。

**自检**：能从作用量推出运动方程；能说清诺特定理在讲什么。

## 第 2 阶段：量子力学（3–6 个月，最关键的一关）

QFT = 量子力学 + 狭义相对论。量子力学不过关，后面全是空中楼阁。需要达到：

- 希尔伯特空间、算符、狄拉克记号烂熟
- 角动量理论（SU(2) 的物理化身）（[笔记](docs/stage-02-quantum-mechanics/02-angular-momentum.md)）
- 微扰论（含时微扰论、费米黄金定则——QFT 里算截面就是它的推广）（[笔记](docs/stage-02-quantum-mechanics/03-perturbation-theory.md)）
- 散射理论基本概念（[笔记](docs/stage-02-quantum-mechanics/04-scattering-theory.md)）
- 谐振子的产生/湮灭算符解法（**QFT 本质上是无穷多个谐振子**）（[笔记](docs/stage-02-quantum-mechanics/05-harmonic-oscillator-ladder.md)）

教材：Griffiths《量子力学概论》入门，之后 Shankar 或 Sakurai《现代量子力学》。

**自检**：会算氢原子；会用产生湮灭算符；会推跃迁概率。

## 第 3 阶段：经典场论 + 相对论量子力学（1–2 个月，过渡桥梁）

- 场的拉格朗日形式：从弦的振动推广到场；诺特流、能动张量（[笔记](docs/stage-03-relativistic-qm/02-lagrangian-field-theory.md)）
- Klein–Gordon 方程、Dirac 方程（作为"相对论量子力学的尝试"引入；理解它们的困难——负能量解、多粒子问题——正是 QFT 存在的理由）（[笔记](docs/stage-03-relativistic-qm/01-klein-gordon-and-dirac.md)）
- 电磁学的协变形式（F_μν、规范势）（[笔记](docs/stage-03-relativistic-qm/03-covariant-electromagnetism.md)）

这一阶段一般已并入 QFT 教材的前几章（如 Peskin 第 2–3 章），不必单独啃书。

## 第 4 阶段：量子场论核心（6–12 个月，主战场）

主线逻辑：

1. **标量场量子化**：自由场 = 无穷多谐振子，粒子是场的激发（[笔记](docs/stage-04-qft-core/01-scalar-field-quantization.md)）
2. **传播子与因果性**：费曼传播子
3. **相互作用 + 微扰论**：Wick 定理、**费曼图与费曼规则**（从这里开始你会"算"了）
4. **S 矩阵与截面**：LSZ 约化公式，算出第一个真实物理量——散射截面
5. **QED**：旋量场 + 光子场 + 规范不变性；算康普顿散射、e⁺e⁻ → μ⁺μ⁻（[笔记](docs/stage-04-qft-core/05-qed.md)）
6. **一圈修正**：发散、正规化、**重整化**（QFT 思想上最深的部分；Wilson 的有效理论视角是现代的正确理解）（[笔记](docs/stage-04-qft-core/06-one-loop-renormalization.md)）
7. **路径积分表述**（可与传统算符形式平行学）（[笔记](docs/stage-04-qft-core/07-path-integral.md)）

教材（按难度排）：

- **入门**：Schwartz《Quantum Field Theory and the Standard Model》——现代、清楚、直奔计算；或 Srednicki（结构干净）
- **标准参考**：Peskin & Schroeder——必读，但别从第一页线性死磕，配合 Schwartz 看
- **补充读物**：Zee《QFT in a Nutshell》——物理直觉极好，适合保持兴趣

**自检里程碑**：能从费曼规则出发，独立算出 e⁺e⁻ → μ⁺μ⁻ 的树图截面并与实验公式对上；能解释一圈发散为什么不可怕、重整化到底"减"掉了什么。到这一步，电子反常磁矩的一圈修正（Schwinger 项 α/2π）你也可以亲手算出来——这是标准的研究生习题。

## 第 5 阶段：对称性与群论补课（与第 4 阶段后期并行）

- 李群/李代数，SU(2)、SU(3) 的表示论
- [整体对称 vs 规范对称](docs/stage-05-symmetry-group-theory/02-global-vs-gauge-symmetry.md)
- 自发对称性破缺、Goldstone 定理、Higgs 机制

教材：Georgi《Lie Algebras in Particle Physics》，或 Schwartz/Peskin 相关章节。

## 第 6 阶段：标准模型本身（3–6 个月）

到这里是"组装"阶段，每一块都是前面零件的组合：

1. **非阿贝尔规范理论**（Yang–Mills）：协变导数、场强、渐近自由（QCD 的招牌性质）（[笔记](docs/stage-06-standard-model/01-yang-mills.md)）
2. **电弱统一**：SU(2)×U(1)、希格斯机制、W/Z/光子质量谱、费米子质量来自 Yukawa 耦合（[笔记](docs/stage-06-standard-model/02-electroweak-unification.md)）
3. **QCD**：色 SU(3)、夸克禁闭、部分子模型、跑动耦合（[笔记](docs/stage-06-standard-model/03-qcd.md)）
4. **标准模型拉氏量**：三部分拼起来，逐项读懂那一页著名的公式（[笔记](docs/stage-06-standard-model/04-standard-model-lagrangian.md)）
5. 选学深化：反常（anomaly）与相消、CKM 矩阵与 CP 破坏、中微子质量、超出标准模型的问题

教材：Schwartz 后半本；Cheng & Li《Gauge Theory of Elementary Particle Physics》；Griffiths《Introduction to Elementary Particles》（偏现象学，可当先导读物）。

---

## 实用建议

- **习题必须动手**。QFT 是算出来的，不是看出来的。Schwinger 项、e⁺e⁻ 截面、跑动耦合这些"经典曲目"亲手算一遍，理解会完全不同。
- **不要死磕一本教材**。卡住时换一本看同一章（Peskin 卡住看 Schwartz，再不行看 Zee 的直觉版），三个角度基本能解开。
- **数学别超前囤**。学到哪补哪——学角动量时补 SU(2)，学 Yang–Mills 时补纤维丛的直觉（不必先啃微分几何专著）。
- **学习顺序总览**：

```text
数学按需补课（群论/张量/变分）
        ↓
分析力学 + 狭义相对论
        ↓
量子力学  ←—— 最关键，不过关则后面全是空中楼阁
        ↓
经典场论 + 相对论量子力学（桥梁）
        ↓
QFT 核心（量子化 → 费曼图 → QED → 重整化）
        ↓
群论/对称性补课（并行）
        ↓
标准模型（Yang–Mills → 电弱 → QCD → 组装）
```

## 学习笔记与本地预览

学习笔记在 `docs/` 下，按阶段组织（`docs/stage-XX-主题/NN-文档名.md`，编号按路线图阶段内的学习顺序，留有空位便于插入）。已完成的笔记链接已直接挂在上面的路线图条目上（条目标注"笔记"的即是）。

笔记含 LaTeX 公式（MathJax 渲染）和可折叠的自检答案，建议用自带的服务器在浏览器中阅读：

```bash
python3 -m venv .venv
.venv/bin/pip install markdown pymdown-extensions
.venv/bin/python serve.py        # 打开 http://localhost:9000
```

## 最小书单

四本就够，其余都是辅助：

| 阶段 | 书 |
|---|---|
| 量子力学 | Griffiths《量子力学概论》 |
| QFT 主线 | Schwartz《Quantum Field Theory and the Standard Model》 |
| QFT 参考 | Peskin & Schroeder《An Introduction to Quantum Field Theory》 |
| 群论 | Georgi《Lie Algebras in Particle Physics》 |

## 终点自测

达到以下三条，就算真正"理解标准模型"了：

1. 能读懂 μ 子 g-2 的强子真空极化为什么难算；
2. 能看懂 LHC 论文里"NNLO 截面"在说什么；
3. 能向人解释希格斯机制不是"给粒子质量的糖浆"。
