# 旧量子论：氢原子的第一次"解出"与 Bohr–Sommerfeld 量子化

> 路线图位置：量子力学书 · 第〇部分（前史与数学准备）· 第 01 篇，是[第 06 篇 氢原子与电子亚层](06-hydrogen-and-subshells.md)（波动力学解）的前史
> 前置知识：[第 06 篇](06-hydrogen-and-subshells.md)（氢原子的波动力学解与简并账本——本篇讲它诞生之前人们算到了什么、卡在哪里）；分析力学的作用量–角度变量（只引用结论，见参考）；狭义相对论能量–动量关系（第 6 节用）。
> 学习目标：会从 Bohr 两条假设完整推出 $r_n$、$E_n$ 与 Rydberg 公式；会用 Bohr–Sommerfeld 条件 $\oint p\,dq = nh$ 处理一维谐振子与氢原子椭圆轨道；会由 $J_r$ 的积分结果看出能量只依赖 $n = n_r + n_\phi$；会把 Sommerfeld 精细结构公式展开到 $(Z\alpha)^4$ 并算出 H$\alpha$ 分裂量级；能列清旧量子论的成就与失败，说清对应原理如何搭桥通向 Heisenberg 矩阵力学。
>
> 记号约定：本篇保留 $\hbar$ 与 $c$（与第 06 篇一致；旧量子论处处是 $h$ 与 $\nu$）。库仑势写 $-Ze^2/(4\pi\varepsilon_0 r)$，简记 $k \equiv Ze^2/(4\pi\varepsilon_0)$；玻尔半径 $a_0 = 4\pi\varepsilon_0\hbar^2/(m_e e^2) \approx 0.529$ Å、精细结构常数 $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137$，均在出现处定义。

---

## 1. 一句话总结

**旧量子论（1900–1925）是一套"经典力学 + 量子化补丁"的临时体制：Bohr 用定态与跃迁两条假设第一次从基本常数推出 $E_n = -13.6\,\text{eV}/n^2$ 与 Rydberg 公式，Sommerfeld 把补丁升级为对一切可分离周期体系的量子化规则 $\oint p_i\,dq_i = n_i h$，并借此算出椭圆轨道（能量只依赖 $n = n_r + n_\phi$，与后来的 $l$ 简并暗合）和精细结构（第一次写出 $\alpha$，公式竟与 Dirac 理论形式雷同）；但它没有动力学、没有零点能、对付不了氦原子这个不可积体系，谱线强度只能靠对应原理打补丁——正是这些结构性失败逼出了 1925 年 Heisenberg 的矩阵力学。**

## 2. 历史定位：1900–1925 的二十五年

19 世纪末的原子物理是一堆光谱经验公式（Balmer 1885、Rydberg 1890）加一个不稳定模型（Rutherford 1911 的行星模型：按经典电动力学，绕核电子必辐射、约 $10^{-10}$ s 内坠入核内）。旧量子论的二十五年就是把这堆废墟逐步建成半座理论的过程：

| 年份 | 事件 | 一句话意义 |
| --- | --- | --- |
| 1900 | Planck 量子假说 $E = h\nu$ | 为黑体辐射引入作用量量子 $h$ |
| 1905 | Einstein 光量子 | 量子从"数学技巧"变成物理实体 |
| 1913 | Bohr 氢原子模型（Phil. Mag. 26, 1） | 第一次从基本常数算出 $-13.6\,\text{eV}/n^2$ |
| 1914 | Franck–Hertz 实验 | 定态能级的直接实验证据 |
| 1915 | Wilson、Ishiwara 各自独立提出 $\oint p\,dq = nh$ | 量子化从氢原子推广为一般规则 |
| 1916 | Sommerfeld 椭圆轨道 + 精细结构 | 引入 $\alpha$；旧量子论的精度巅峰 |
| 1922 | Stern–Gerlach 实验 | 空间量子化的证据 |
| 1924 | Bohr–Kramers–Slater 理论失败 | 打补丁路线走到尽头 |
| 1925 | Heisenberg 矩阵力学（Z. Phys. 33, 879） | 旧量子论终结 |

两条主线贯穿全篇：**它是历史上第一个推出正确氢光谱的理论**（第 3 节）；**它的失败方式直接规定了矩阵力学的长相**（第 7 节，[第 06s 篇 氢原子的矩阵力学解法](06s-hydrogen-matrix-mechanics.md) 从这里接棒）。

## 3. Bohr 模型（1913）：两条假设与完整推导

### 3.1 两条假设

Bohr 对 Rutherford 模型的经典灾难开出的药方是两条反经典的公设：

1. **定态假设**：电子只能在若干离散的经典轨道上运动，在定态上**不辐射**（直接宣布经典电动力学在原子尺度失效）；
2. **跃迁假设**：电子在定态 $m \to n$ 间跃迁时吸收/发射单色光，$h\nu = \lvert E_m - E_n \rvert$。

第三条"技术性"条件是**角动量量子化**：$L = m_e v r = n\hbar$，$n = 1, 2, \dots$。Bohr 本人是从对应原理（大 $n$ 处量子结果必须回到经典辐射频率，第 7.3 节）反推出它的；1924 年 de Broglie 给了它物质波驻波的解释（周长 $= n\lambda$）。

### 3.2 推导：$r_n$、$v_n$、$E_n$、Rydberg 公式

库仑力提供向心力（$k \equiv Ze^2/(4\pi\varepsilon_0)$）：

$$\frac{m_e v^2}{r} = \frac{k}{r^2},$$

与 $m_e v r = n\hbar$ 联立。由后者 $v = n\hbar/(m_e r)$，代入前者：

$$\frac{n^2\hbar^2}{m_e r^3} = \frac{k}{r^2} \;\Longrightarrow\; r_n = \frac{n^2\hbar^2}{m_e k} = \frac{n^2 a_0}{Z}, \qquad a_0 \equiv \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} \approx 0.529\ \text{\AA}.$$

回代速度：

$$v_n = \frac{k}{n\hbar} = \frac{Z\alpha c}{n}, \qquad \alpha \equiv \frac{e^2}{4\pi\varepsilon_0\hbar c} \approx \frac{1}{137},$$

基态电子速度只有 $\alpha c \approx c/137$——原子物理天生非相对论，这句判断后面一直用到。能量由力平衡得动能 $= k/(2r)$（位力定理），故

$$E_n = \frac{k}{2r_n} - \frac{k}{r_n} = -\frac{k}{2r_n} = -\frac{m_e k^2}{2n^2\hbar^2} = -\frac{m_e c^2 (Z\alpha)^2}{2n^2} = -\frac{Z^2 \times 13.6\ \text{eV}}{n^2},$$

其中 $m_e c^2\alpha^2/2 = 511\ \text{keV}/(2\times137^2) = 13.6$ eV。跃迁 $m \to n$（$m > n$）的波数：

$$\frac{1}{\lambda} = \frac{E_m - E_n}{hc} = R_\infty Z^2\left(\frac{1}{n^2} - \frac{1}{m^2}\right), \qquad R_\infty \equiv \frac{m_e e^4}{8\varepsilon_0^2 h^3 c} \approx 1.097\times10^7\ \text{m}^{-1}.$$

### 3.3 第一批战果

- **Rydberg 常数从天上掉下来**：此前 $R$ 是纯拟合参数，Bohr 第一次用 $m_e, e, h, c$ 把它**算**了出来，与光谱值吻合到千分之一（折合质量修正后再好一个量级）——1913 年物理学界最轰动的一击；
- **Pickering 线系之谜**：星体光谱里一组"半整数位置"的谱线曾被当成氢的新线系，Bohr 指出那是 $Z = 2$ 的 He$^+$（$1/\lambda = 4R(1/n^2 - 1/m^2)$，偶数项恰落在氢线之间）——理论与天文观测当场互认；
- **Franck–Hertz（1914）**：汞蒸气中电子在 4.9 V 处阶梯式损失动能——定态存在、能量只能离散转移的直接证据；
- **Moseley 定律（1913）**：特征 X 射线频率 $\sqrt{\nu} \propto (Z - 1)$，正是 $n = 2 \to 1$ 的类氢公式套上屏蔽——元素周期表的 $Z$ 从此有了物理含义。

## 4. Bohr–Sommerfeld 量子化条件

### 4.1 从"角动量取整"到一般规则

Bohr 的 $L = n\hbar$ 只适用于圆轨道。1915 年 Wilson 与 Ishiwara 独立指出，对任何**可分离的周期体系**（每个自由度做周期运动、哈密顿量可按该自由度分离变量），量子化条件应写为作用量积分取整：

$$\oint p_i\,dq_i = n_i h, \qquad n_i = 0, 1, 2, \dots,$$

积分沿该自由度的一个完整周期。分析力学的语言（作用量–角度变量，见参考中的 Goldstein）：$\oint p_i\,dq_i = 2\pi J_i$，$J_i$ 是绝热不变量（Ehrenfest：缓慢变化外参量时它不变，所以"哪些量可以量子化"有唯一好答案），条件即 $J_i = n_i\hbar$。圆轨道只是特例：$J_\phi = \oint L\,d\phi = 2\pi L = nh$ 即 $L = n\hbar$。

### 4.2 例：一维谐振子——第一个"症状"

$H = p^2/(2m) + \tfrac12 m\omega^2 q^2 = E$，动量 $p = \pm\sqrt{2mE - m^2\omega^2 q^2}$，转折点 $q = \pm A$，$A = \sqrt{2E/(m\omega^2)}$。作用量积分（去程回程各一半）：

$$\oint p\,dq = 2\int_{-A}^{A}\sqrt{2mE\left(1 - \frac{q^2}{A^2}\right)}\,dq = 2\sqrt{2mE}\,A\cdot\frac{\pi}{2} = \frac{2\pi E}{\omega} = \frac{E}{\nu},$$

（用了 $\int_{-1}^1\sqrt{1-x^2}\,dx = \pi/2$）。量子化条件给出

$$E_n = nh\nu, \qquad n = 0, 1, 2, \dots$$

——**没有零点能**。而波动力学的答案是 $E_n = (n + \tfrac12)\hbar\omega$（第 04 篇[谐振子升降算符](04-harmonic-oscillator-ladder.md)）。零点能不是小修正：液氦不凝固、Casimir 效应都是它的宏观签名。事后人们给 $\oint p\,dq$ 加上半整数补丁（$\oint p\,dq = (n + \tfrac12)h$，即后来 WKB 的 Maslov 指标），能蒙对谐振子——但这恰恰说明旧量子论的规则本身不完整，补丁没有一个统一来源。

## 5. Sommerfeld 椭圆轨道（1916）：氢原子的两个作用量

放开"圆轨道"限制，电子在库仑场中走 Kepler 椭圆。平面运动有两个自由度，量子化条件也有两条。

**角向**：$\phi$ 是循环坐标，$p_\phi = L$ 守恒，

$$J_\phi = \oint L\,d\phi = 2\pi L = n_\phi h \;\Longrightarrow\; L = n_\phi\hbar.$$

**径向**：$p_r = \sqrt{2m_e E + 2m_e k/r - L^2/r^2}$，根号内是 $r$ 的二次函数，两转折点之间往返积分。这是 Hamilton–Jacobi 理论的标准围道积分（推导见自检问题 3 的引用），结果为

$$J_r = \oint p_r\,dr = \frac{2\pi m_e k}{\sqrt{-2m_e E}} - 2\pi L = n_r h.$$

两式相加，$2\pi L = n_\phi h$ 恰好消掉：

$$\frac{2\pi m_e k}{\sqrt{-2m_e E}} = (n_r + n_\phi)\,h \;\Longrightarrow\; E = -\frac{2\pi^2 m_e k^2}{(n_r + n_\phi)^2 h^2} = -\frac{m_e c^2(Z\alpha)^2}{2n^2}, \qquad n \equiv n_r + n_\phi.$$

**能量只依赖 $n = n_r + n_\phi$**——椭圆轨道的形状不同（半轴比 $b/a = n_\phi/n$），能量却相同。这正是第 06 篇里波动力学 $l$ 简并（库仑 SO(4)）在旧量子论里的影子：经典来源是 Kepler 问题的 Runge–Lenz 矢量守恒。记账对照（固定 $n$）：

| 旧量子论 | 波动力学（第 06 篇） | 关系 |
| --- | --- | --- |
| $n_\phi = 1, \dots, n$ | $l = 0, \dots, n-1$ | $n_\phi \leftrightarrow l + 1$ |
| $n_r = n - n_\phi$ | $n_r = n - l - 1$ | 同一计数 |
| 每 $n$ 共 $n$ 条轨道 | 每 $n$ 共 $n$ 个 $l$ | 简并对得上 |

两条结构性的人为痕迹值得记住：

- **$n_\phi = 0$ 被手工排除**：它对应 $L = 0$ 的直线轨道，电子径向穿过原子核——"撞核轨道"在物理上必须扔，但旧量子论内部给不出排除它的原理，只能靠一句"不允许"。波动力学里 $L^2 = l(l+1)\hbar^2$ 自动消灭了这条轨道；
- **空间量子化**：加上第三个条件（$L_z$ 取整，Sommerfeld–Debye 1916）后每条椭圆按取向再分裂。取 $m = -l, \dots, l$ 的波动力学计数 $2l+1 = 2n_\phi - 1$，于是每 $n$ 的总态数 $\sum_{n_\phi=1}^{n}(2n_\phi - 1) = n^2$，与第 06 篇的账本严丝合缝。Stern–Gerlach（1922）银原子束在不均匀磁场中劈成两条，被视为空间量子化的直接证据（事后来看测到的是自旋——旧量子论又一次"结果对、理由错"）。

## 6. Sommerfeld 精细结构（1916）：$\alpha$ 的诞生

第 3.2 节算出 $v_1/c = Z\alpha \sim 10^{-2}$，相对论修正虽小但可测。Sommerfeld 把哈密顿量换成相对论的

$$H = \sqrt{p^2c^2 + m_e^2c^4} - m_e c^2 - \frac{k}{r} \approx \frac{p^2}{2m_e} - \frac{p^4}{8m_e^3c^2} - \frac{k}{r},$$

$-p^4$ 项使径向频率与角向频率不再锁死，椭圆轨道缓慢进动，能量于是**同时依赖 $n$ 与 $n_\phi$**。在作用量–角度变量里做完（推导冗长，见 Sommerfeld 原书），得到精确的封闭公式：

$$E = m_e c^2\left[1 + \frac{(Z\alpha)^2}{\left(n - n_\phi + \sqrt{n_\phi^2 - (Z\alpha)^2}\right)^2}\right]^{-1/2}.$$

展开到 $(Z\alpha)^4$ 阶（完整代数在自检问题 4）：

$$E_n = -m_e c^2\frac{(Z\alpha)^2}{2n^2}\left[1 + \frac{(Z\alpha)^2}{n}\left(\frac{1}{n_\phi} - \frac{3}{4n}\right) + \cdots\right].$$

同一 $n$ 内不同 $n_\phi$ 的轨道裂开了，裂距 $\sim m_ec^2(Z\alpha)^4$——比主能级小 $\alpha^2 \sim 5\times10^{-5}$ 倍，故称"精细结构"。三件事要记住：

- **$\alpha$ 就是在这里登场的**：Sommerfeld 1916 年把 $e^2/(4\pi\varepsilon_0\hbar c)$ 定义为基态速度与光速之比 $v_1/c$，"精细结构常数"这个名字就来自这个公式；它是电磁相互作用强度的无量纲度量，此后一路走进 QED（QFT 书第 4 阶段的主角）；
- **实验当场兑现**：Paschen 1916 年精密测量 He$^+$ 的 4686 Å 线精细分裂，与公式吻合——旧量子论的精度巅峰，爱因斯坦称之为"缪斯的启示"；
- **与 Dirac 理论的形式巧合**：把上式中的 $n_\phi$ 换成 $j + \tfrac12$，就是 Dirac 方程的精确氢原子能谱（[第 06s2 篇 Dirac 氢原子](06s2-dirac-hydrogen.md) 会专门解这个对照）。能级数值全对，但量子数的身份、取值范围与简并结构完全不同（Dirac 里 $2s_{1/2}$ 与 $2p_{1/2}$ 简并，Sommerfeld 里没有这回事）——旧量子论像一只蒙对答案的半瞎眼睛，看得清光谱，看不清力学。

## 7. 成就与失败清单

### 7.1 成就

- 氢与类氢离子光谱：$E_n$、Rydberg 常数、Pickering 线系，全部从基本常数算出；
- 精细结构的**量级**：$\alpha^4$ 裂距与 Paschen 测量吻合；
- 定态概念被 Franck–Hertz 直接证实；空间量子化被 Stern–Gerlach 证实（解释上张冠李戴，但"取向离散"这件事是对的）；
- X 射线与 Moseley 定律、Stark 效应的定性处理（Epstein 1916）；
- 留下了三笔永久遗产：$\alpha$、对应原理、"作用量取整"的几何直觉（后来在 WKB 与 Gutzwiller 半经典理论里还魂）。

### 7.2 失败——每一条都指向新力学

- **氦原子**：两电子 + 核是不可积三体问题，轨道不可分离、不存在好作用量变量，$\oint p\,dq$ 根本无处下笔；1916–1923 年间最优秀的一批人（Born、Pauli、van Vleck）算基态能全部失败。旧量子论只在"可积"的温室里存活（自检问题 5）；
- **谱线强度与偏振**：理论只给频率不给强度，只能靠对应原理半定量打补丁；
- **反常塞曼效应**：谱线分裂数目对不上任何整数量子化方案，被迫引入半整数量子数（事后看是自旋）；
- **零点能缺失**（第 4.2 节）与 $n_\phi = 0$ 的人为排除（第 5 节）：规则内部的补丁没有统一来源；
- **没有跃迁动力学**：理论说不清电子"何时、以多大概率"跃迁——爱因斯坦 1917 年的 $A$、$B$ 系数只是现象学。

### 7.3 对应原理：通往 Heisenberg 的桥

旧量子论手里最锋利的工具是 Bohr 的**对应原理**：大量子数极限下，量子预言必须回到经典预言。第 3 节的一个漂亮检查（自检材料）：$n \to n-1$ 跃迁频率在大 $n$ 处恰等于经典轨道频率 $f = v/(2\pi r) = m_ec^2Z^2\alpha^2/(n^3h)$。Bohr 进一步主张：经典轨道的 Fourier 分量的**振幅**应对应量子跃迁的**强度**——用经典傅里叶系数去猜谱线强度与选择定则。1924 年 Bohr–Kramers–Slater 放弃微观能量守恒的孤注一掷被 Bothe–Geiger 实验否决，补丁路线破产；Kramers 把对应原理用于色散取得局部成功。1925 年 7 月 Heisenberg 索性掀桌：轨道本身不可观测，理论只应谈论跃迁——把经典 Fourier 分量 $x_n(t) = \sum_\alpha x_\alpha e^{i\alpha\omega t}$ 的"频率 + 振幅"对换成跃迁矩阵元 $x_{nm}$ 与频率 $\omega_{nm}$，乘法规则自动变成矩阵乘法。旧量子论死了，它的对应原理被完整收编进新力学——这就是[第 06s 篇 氢原子的矩阵力学解法](06s-hydrogen-matrix-mechanics.md) 的开场。

## 小结

| 阶段 | 规则 | 代表结果 | 命门 |
| --- | --- | --- | --- |
| Bohr 1913 | $L = n\hbar$（圆轨道） | $E_n = -Z^2\,13.6\,\text{eV}/n^2$，$R_\infty$ | 只适用于氢，无推广规则 |
| Wilson–Ishiwara 1915 | $\oint p_i\,dq_i = n_i h$ | 谐振子 $E = nh\nu$ | 无零点能；只适用于可积体系 |
| Sommerfeld 1916 | 多自由度 + 相对论修正 | 椭圆轨道简并、精细结构、$\alpha$ | $n_\phi = 0$ 手工排除；量子数身份错误 |

- 氢的两次"解出"：Bohr 推出 $E_n$（对），Sommerfeld 推出精细结构（数值对、简并错）；能量只依赖 $n = n_r + n_\phi$ 是库仑隐藏对称性的旧量子论化身。
- 失败清单的每一项都是新力学的订单：氦 → 需要真正的多体动力学；强度 → 跃迁矩阵元；半整数量子数 → 自旋；零点能 → 非对易代数。
- 对应原理是唯一完好的遗产，1925 年被 Heisenberg 直接升级为矩阵力学的构造原则。

## 自检问题

**1.** 从 $L = n\hbar$ 与库仑向心力平衡出发，完整推出 $r_n$、$v_n$、$E_n$，并把 $E_n$ 写成 $-m_ec^2(Z\alpha)^2/(2n^2)$ 与 $-Z^2\,13.6\,\text{eV}/n^2$ 两种形式。

<details markdown="1"><summary>点击显示答案</summary>

记 $k = Ze^2/(4\pi\varepsilon_0)$。两方程：

$$m_e v r = n\hbar, \qquad \frac{m_e v^2}{r} = \frac{k}{r^2}.$$

由第一式 $v = n\hbar/(m_er)$，代入第二式左端：$m_e v^2/r = n^2\hbar^2/(m_er^3) = k/r^2$，两边乘 $r^3$：

$$r_n = \frac{n^2\hbar^2}{m_e k} = \frac{n^2}{Z}\cdot\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2} = \frac{n^2a_0}{Z}.$$

回代 $v_n = n\hbar/(m_er_n) = k/(n\hbar) = Ze^2/(4\pi\varepsilon_0n\hbar) = Z\alpha c/n$（用 $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$）。能量：由力平衡 $m_ev^2 = k/r$，动能 $T = k/(2r)$，故

$$E = T - \frac{k}{r} = -\frac{k}{2r_n} = -\frac{m_ek^2}{2n^2\hbar^2}.$$

把 $k = Z\alpha\hbar c$ 代入：$E_n = -m_eZ^2\alpha^2\hbar^2c^2/(2n^2\hbar^2) = -m_ec^2(Z\alpha)^2/(2n^2)$。数值：$m_ec^2 = 5.11\times10^5$ eV，$\alpha^2 = 1/137^2 = 5.33\times10^{-5}$，故 $E_1 = -5.11\times10^5\times5.33\times10^{-5}/2 \approx -13.6$ eV，即 $E_n = -Z^2\,13.6\,\text{eV}/n^2$。

</details>

**2.** 对一维谐振子计算 $\oint p\,dq$，推出 $E = nh\nu$；指出它与波动力学答案差了什么，以及这个差别为什么是"症状"而非小误差。

<details markdown="1"><summary>点击显示答案</summary>

$E = p^2/(2m) + \tfrac12m\omega^2q^2$，转折点在 $\tfrac12m\omega^2A^2 = E$，即 $A = \sqrt{2E/(m\omega^2)}$。一周期内 $q$ 从 $-A$ 到 $A$ 再返回，去程 $p > 0$、回程 $p < 0$ 且 $dq < 0$，两段贡献相等：

$$\oint p\,dq = 2\int_{-A}^{A}\sqrt{2mE - m^2\omega^2q^2}\,dq = 2\sqrt{2mE}\int_{-A}^{A}\sqrt{1 - q^2/A^2}\,dq.$$

换元 $q = Ax$，$\int_{-1}^{1}\sqrt{1-x^2}dx = \pi/2$（半圆面积），得

$$\oint p\,dq = 2\sqrt{2mE}\cdot A\cdot\frac{\pi}{2} = \pi\sqrt{2mE}\cdot\sqrt{\frac{2E}{m\omega^2}} = \frac{2\pi E}{\omega} = \frac{E}{\nu}.$$

量子化条件 $\oint p\,dq = nh$ 给出 $E_n = nh\nu$。波动力学答案（第 04 篇升降算符）是 $E_n = (n + \tfrac12)\hbar\omega$——差一个零点能 $\tfrac12\hbar\omega$。这是症状：零点能来自 $[x, p] \neq 0$（不确定关系禁止相空间轨迹缩到一点），而旧量子论的全部输入是经典轨道，框架内不存在产生 $\tfrac12$ 的机制；半整数补丁（$\oint p\,dq = (n+\tfrac12)h$）能蒙对这个例子，却对别的体系时灵时不灵——规则本身缺了一块。

</details>

**3.** 已知椭圆轨道的径向作用量积分结果为 $J_r = 2\pi m_e k/\sqrt{-2m_eE} - 2\pi L$（$k = Ze^2/4\pi\varepsilon_0$），推出能量只依赖 $n = n_r + n_\phi$ 并写出 $E_n$；用圆轨道检验 $J_r = 0$ 这一端点。

<details markdown="1"><summary>点击显示答案</summary>

角向条件：$J_\phi = \oint L\,d\phi = 2\pi L = n_\phi h$，故 $2\pi L = n_\phi h$。与 $J_r = n_r h$ 相加：

$$J_r + J_\phi = \frac{2\pi m_e k}{\sqrt{-2m_eE}} = (n_r + n_\phi)h.$$

左边只含能量不含形状——这就是"能量只依赖 $n \equiv n_r + n_\phi$"的全部来源。解出 $E$：

$$\sqrt{-2m_eE} = \frac{2\pi m_e k}{nh} \;\Longrightarrow\; -2m_eE = \frac{4\pi^2m_e^2k^2}{n^2h^2} \;\Longrightarrow\; E_n = -\frac{2\pi^2m_ek^2}{n^2h^2} = -\frac{m_ek^2}{2n^2\hbar^2} = -\frac{m_ec^2(Z\alpha)^2}{2n^2},$$

与 Bohr 圆轨道结果一致（用 $k = Z\alpha\hbar c$）。

**圆轨道端点检验**：圆轨道 $L = m_evr$、$k/r = m_ev^2$，得 $L^2 = m_e k r$，$E = -k/(2r) = -m_ek^2/(2L^2)$。代入 $J_r$：

$$\frac{2\pi m_e k}{\sqrt{-2m_eE}} = \frac{2\pi m_e k}{\sqrt{m_e^2k^2/L^2}} = 2\pi L \;\Longrightarrow\; J_r = 2\pi L - 2\pi L = 0,$$

即 $n_r = 0$、$n_\phi = n$——最圆的轨道径向无振荡，账平。另一端 $n_\phi = n$ 固定、$n_r$ 增大则 $b/a = n_\phi/n$ 减小，轨道越扁；$n_\phi = 0$ 是直线撞核轨道，被人为排除。

</details>

**4.** 把 Sommerfeld 精细结构公式展开到 $(Z\alpha)^4$ 阶，推出 $\Delta E$；计算氢 $n = 2$ 壳层 $n_\phi = 1$ 与 $n_\phi = 2$ 两条轨道的裂距（用 eV、GHz、cm$^{-1}$ 三种单位），并与 H$\alpha$（656.3 nm）比较。

<details markdown="1"><summary>点击显示答案</summary>

令 $\gamma \equiv (Z\alpha)^2$。先展开根号：$\sqrt{n_\phi^2 - \gamma} = n_\phi\sqrt{1 - \gamma/n_\phi^2} \approx n_\phi - \gamma/(2n_\phi)$。分母：

$$\left(n - n_\phi + \sqrt{n_\phi^2 - \gamma}\right)^2 \approx \left(n - \frac{\gamma}{2n_\phi}\right)^2 \approx n^2\left(1 - \frac{\gamma}{nn_\phi}\right).$$

于是

$$\frac{\gamma}{(\cdots)^2} \approx \frac{\gamma}{n^2}\left(1 + \frac{\gamma}{nn_\phi}\right) = \frac{\gamma}{n^2} + \frac{\gamma^2}{n^3n_\phi}.$$

对 $f = 1 + x$ 用 $f^{-1/2} \approx 1 - x/2 + 3x^2/8$，$x = \gamma/n^2 + \gamma^2/(n^3n_\phi)$，$x^2 \approx \gamma^2/n^4$：

$$E \approx m_ec^2\left[1 - \frac{\gamma}{2n^2} - \frac{\gamma^2}{2n^3n_\phi} + \frac{3\gamma^2}{8n^4}\right].$$

减去静止能：

$$E - m_ec^2 = -\frac{m_ec^2(Z\alpha)^2}{2n^2} - \frac{m_ec^2(Z\alpha)^4}{2n^3}\left(\frac{1}{n_\phi} - \frac{3}{4n}\right).$$

**$n = 2$ 裂距**：$n_\phi = 1$ 与 $n_\phi = 2$ 之差（$3/(4n)$ 项抵消）：

$$\Delta E = \frac{m_ec^2\alpha^4}{2\cdot 2^3}\left(1 - \frac12\right) = \frac{m_ec^2\alpha^4}{32}.$$

数值：$m_ec^2 = 5.11\times10^5$ eV，$\alpha^4 = (1/137)^4 = 2.84\times10^{-9}$，故 $\Delta E \approx 5.11\times10^5\times2.84\times10^{-9}/32 \approx 4.5\times10^{-5}$ eV。换算：$\Delta E/h \approx 4.5\times10^{-5}\times2.42\times10^{14} \approx 1.1\times10^{10}$ Hz $\approx 11$ GHz；$\Delta E/(hc) \approx 0.37$ cm$^{-1}$。对 H$\alpha$（光子能量 $1240/656.3 \approx 1.89$ eV）相对裂距 $\sim 2.4\times10^{-5}$，波长裂距 $\Delta\lambda \approx 656.3\ \text{nm}\times2.4\times10^{-5} \approx 0.16$ Å——1916 年的光谱仪刚好看得见，Paschen 对 He$^+$ 的测量证实了这个量级。

</details>

**5.** 为什么旧量子论在氦原子上"必然"失败，而不是"暂时算不动"？

<details markdown="1"><summary>点击显示答案</summary>

**结构性原因**：Bohr–Sommerfeld 规则 $\oint p_i\,dq_i = n_ih$ 有两个隐藏前提——哈密顿量可对每个自由度**分离变量**，且每个自由度的运动是（准）周期的。只有这时 $p_i(q_i)$ 才是单值函数、闭合积分才有意义，作用量–角度变量才存在。氢原子（Kepler 问题）是可积体系的样板：两个自由度两个运动常数（$E$、$L$），分离变量一次到底。

**氦为什么不行**：两电子 + 核是三体问题，电子–电子排斥 $e^2/(4\pi\varepsilon_0\lvert\vec r_1 - \vec r_2\rvert)$（此处 $\lvert\cdot\rvert$ 为矢量模长）把一切搅在一起。Poincaré 早在 1890 年代就证明受扰三体问题一般**不可积**：不存在足够多的运动常数，轨道在相空间里混沌游荡，没有不变环面，$p_i$ 不是 $q_i$ 的周期函数——$\oint p_i\,dq_i$ 连定义都写不出来，更谈不上令其等于 $n_ih$。这不是计算量大，是规则的前提条件不存在。1916–1923 年间 Born、Heisenberg、Pauli 等人用各种近似方案算氦基态能，结果全部偏离实验（Pauli 1922 年的博士论文工作得到的电离能误差数倍于实验），成为旧量子论危机的核心证据。

**对照波动力学**：薛定谔方程不要求可积性——氦的基态能 1927 年起由变分法（Hylleraas）一路算到与实验吻合；而"可积体系的半经典量子化"这一旧量子论直觉，后来以 EBK/WKB 的形式在波动力学框架内复活，成为有理有据的近似而非基本规则。旧量子论死在它唯一的适用范围（可积体系）太窄——新力学必须从不假设轨道的地方重建，这正是 Heisenberg 只保留跃迁量的动机（见第 7.3 节与[第 06s 篇](06s-hydrogen-matrix-mechanics.md)）。

</details>

## 参考

- A. Sommerfeld《Atomic Structure and Spectral Lines》（Atombau und Spektrallinien 英译本，Methuen 1923）：椭圆轨道量子化与精细结构公式的原始完整推导（本篇第 5、6 节）。
- N. Bohr, *On the Constitution of Atoms and Molecules*, Phil. Mag. 26, 1 (1913)：两条假设与 Rydberg 常数推导的原始论文（第 3 节）。
- W. Heisenberg, Z. Phys. 33, 879 (1925)：矩阵力学创始论文，开篇即声明只使用可观测跃迁量（第 7.3 节）。
- S. Weinberg《Lectures on Quantum Mechanics》第 1 章：旧量子论的历史梳理与 Bohr 推导的现代重述。
- A. Pais《Inward Bound》第 9–11 章：Bohr 模型的接受史、Sommerfeld 学派与 1925 年转折的史料。
- H. Goldstein《Classical Mechanics》第 10 章：作用量–角度变量与 Kepler 问题的 $J_r$ 积分（第 5 节所引用的分析力学结论）。
