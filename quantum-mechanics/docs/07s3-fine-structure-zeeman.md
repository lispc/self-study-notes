# 补充材料：氢原子的精细结构与塞曼效应——简并微扰论的完整演练

> 路线图位置：量子力学书 · 第三部分（近似方法）· 第 07 篇[微扰论](07-perturbation-theory.md)的补充材料（第 07s3 篇；与第 06s2 篇 Dirac 精确解互为对照）
> 前置知识：第 07 篇（第 3–4 节定态与简并微扰论——本篇的引擎）；第 05 篇（自旋、角动量相加与 $\vec L\cdot\vec S$ 本征值、Wigner–Eckart 与选择定则）；第 06 篇（氢原子 $\lvert nlm\rangle$、能级与简并账本）；第 06s2 篇（Dirac 方程的 Sommerfeld–Dirac 精确谱，对照用）。
> 学习目标：会写出氢原子三项相对论修正（相对论动能、自旋-轨道耦合含 Thomas 因子、Darwin 项）并算出逐项期望值；会用好量子数 $j$ 在 $n^2$ 维简并子空间内完成对角化，得到 $E_{nj} = E_n\left[1 + \frac{(Z\alpha)^2}{n^2}\left(\frac{n}{j+1/2} - \frac34\right)\right]$，并与 06s2 的精确展开逐项对账；会用矢量模型推出 Landé $g$ 因子并算反常塞曼的谱线图样（钠 D 双线裂 4 条与 6 条）；会写强场 Paschen–Back 极限的能级公式，说清两个极限之间为什么没有解析解。
>
> 记号约定：库仑耦合沿用 $e^2 \equiv e_{\rm SI}^2/(4\pi\varepsilon_0)$（与 06s3 篇一致），$V(r) = -Ze^2/r$，$\alpha = e^2/\hbar c \approx 1/137$；保留 $\hbar$ 与 $c$ 出现处的量纲。玻尔半径 $a_0 = \hbar/(m\alpha c)$（折合质量近似取 $m = m_e$）。磁矩单位 $\mu_B = e\hbar/2m_e = 5.788\times10^{-5}\ \text{eV/T}$。

---

## 1. 一句话总结

**玻尔能级 $-13.6\,\text{eV}/n^2$ 是 $\alpha^2 mc^2$ 量级；下一阶 $\alpha^4 mc^2$ 的修正来自三项——相对论动能 $-p^4/8m^3c^2$、自旋-轨道耦合 $\frac{Ze^2}{2m^2c^2r^3}\vec L\cdot\vec S$（Thomas 因子 $1/2$ 已含）、以及只打 $s$ 态的 Darwin 项——逐项微扰后在 $j$ 好量子数下求和，能级只依赖 $(n,j)$，结果与 06s2 的 Dirac 精确解展开到 $(Z\alpha)^4$ 完全一致（$2s_{1/2}$ 与 $2p_{1/2}$ 的偶然简并依旧，留给 Lamb 位移）；再叠加外磁场，弱场下一切塞曼位移由 Landé $g$ 因子 $g_j = 1 + \frac{j(j+1)-l(l+1)+s(s+1)}{2j(j+1)}$ 编码（"反常"塞曼就是 $g_j \ne 1$），强场下自旋-轨道退耦成 Paschen–Back 极限——两极限之间好量子数换岗，只能数值对角化。**

本篇是第 07 篇简并微扰论的一场完整实战：微扰不是玩具，是氢原子的真实能谱。

## 2. 量级账单：为什么是 $\alpha^4$

氢原子基态的典型速度 $v \sim \alpha c$（Bohr 模型即已给出 $v = Z\alpha c$，见第 01 篇）。相对论修正的相对大小 $\sim (v/c)^2 \sim (Z\alpha)^2$，作用在 $E_n \sim (Z\alpha)^2 mc^2$ 上：

$$\Delta E_{\rm fs} \sim (Z\alpha)^4 mc^2 \approx Z^4 \times 1.45\times10^{-3}\ \text{eV},$$

比玻尔能级小 $(Z\alpha)^2 \sim 5\times10^{-5}$ 倍。方便的记账单位是

$$\frac{E_n^2}{2mc^2} = \frac{mc^2(Z\alpha)^4}{8n^4} \xrightarrow{\ n=2\ } 1.13\times10^{-5}\ \text{eV},$$

本篇所有数字都是它的整数倍。能量阶梯全景：玻尔能级 $\alpha^2 mc^2$（eV 量级）→ 精细结构 $\alpha^4 mc^2$（$10^{-4}$ eV）→ Lamb 位移 $\alpha^5 mc^2\ln$（$10^{-6}$ eV，QED）→ 超精细 $\alpha^4 (m_e/m_p)mc^2$（$10^{-6}$ eV）。本篇只管第二级。

## 3. 三项相对论修正

### 3.1 相对论动能

$$H_r = -\frac{p^4}{8m^3c^2}.$$

对 $\lvert nlm\rangle$ 求期望值用一条代数捷径（自检问题 1）：由 $p^2 = 2m(E_n - V)$ 得 $\langle p^4\rangle = 4m^2\langle(E_n-V)^2\rangle$，再用维里定理 $\langle V\rangle = 2E_n$ 与径向积分 $\langle r^{-2}\rangle = \frac{Z^2}{a_0^2n^3(l+1/2)}$：

$$\langle H_r\rangle_{nl} = -\frac{E_n^2}{2mc^2}\left[\frac{4n}{l+1/2} - 3\right].$$

它依赖 $l$（也通过 $E_n$ 依赖 $n$），但不碰自旋、不碰 $m$。

### 3.2 自旋-轨道耦合（含 Thomas 因子）

电子静止系里看到运动的原子核产生磁场 $\vec B' = -\vec v\times\vec E/c^2$，自旋磁矩 $\vec\mu_s = -g_s\frac{e}{2m}\vec S$（$g_s \approx 2$）在其中进动，给出 $-\vec\mu_s\cdot\vec B' \propto \vec L\cdot\vec S/r^3$。但电子静止系是非惯性系，**Thomas 进动**恰好把系数砍半（教材标准结果，此处引用；直觉见自检问题 2）：

$$H_{so} = \frac{Ze^2}{2m^2c^2}\,\frac{\vec L\cdot\vec S}{r^3}.$$

$\vec L\cdot\vec S = \frac12(\vec J^2 - \vec L^2 - \vec S^2)$ 只依赖 $(j,l)$，配合 $\langle r^{-3}\rangle = \frac{Z^3}{a_0^3n^3\,l(l+1/2)(l+1)}$（$l\ge1$；$l=0$ 时 $\vec L=0$，此项为零）：

$$\langle H_{so}\rangle_{nlj} = \frac{mc^2(Z\alpha)^4}{4n^3}\,\frac{j(j+1)-l(l+1)-\tfrac34}{l(l+\tfrac12)(l+1)}.$$

### 3.3 Darwin 项

$$H_D = \frac{\hbar^2}{8m^2c^2}\nabla^2 V = \frac{\pi\hbar^2 Ze^2}{2m^2c^2}\,\delta^3(\vec r).$$

来自 Dirac 方程的 zitterbewegung（位置的 $10^{-13}$ m 级抖动把奇点"抹平"，06s2 篇大小分量的低能影子），只打在 $l=0$（$s$ 态波函数在原点非零）：

$$\langle H_D\rangle_{n0} = \frac{\pi\hbar^2Ze^2}{2m^2c^2}\,\lvert\psi_{n00}(0)\rvert^2 = \frac{mc^2(Z\alpha)^4}{2n^3}\qquad\Big(\lvert\psi_{n00}(0)\rvert^2 = \frac{Z^3}{\pi a_0^3n^3}\Big).$$

### 3.4 对账：$n=2$ 的数字

以 $n=2$、$Z=1$ 为例（单位 $10^{-5}$ eV）：

| 态 | $\langle H_r\rangle$ | $\langle H_{so}\rangle$ | $\langle H_D\rangle$ | 合计 |
| --- | --- | --- | --- | --- |
| $2s_{1/2}$ | $-14.72$ | $0$ | $+9.06$ | $-5.66$ |
| $2p_{1/2}$ | $-2.64$ | $-3.02$ | $0$ | $-5.66$ |
| $2p_{3/2}$ | $-2.64$ | $+1.51$ | $0$ | $-1.13$ |

三件事直接读出：**$2p$ 裂成两条**，间距 $4.53\times10^{-5}\ \text{eV} = mc^2\alpha^4/32$；**Darwin 项恰好把 $2s_{1/2}$ 推到与 $2p_{1/2}$ 齐平**（偶然简并）；能级只依赖 $(n,j)$——这正是下面一般公式的预言。

## 4. 简并微扰：好量子数与总公式

三项微扰都不依赖 $m_j$，且 $\vec J^2,\vec L^2,\vec S^2$ 与它们全部对易——在耦合基 $\lvert n\,l\,s=\tfrac12\,j\,m_j\rangle$ 里微扰矩阵已经对角。简并微扰论的全部工作因此浓缩为"选对基"（第 07 篇 4.2 节"好态"的实战）：把 §3 三项加起来（计算见上），合并成

$$\boxed{\ E_{nj} = E_n\left[1 + \frac{(Z\alpha)^2}{n^2}\left(\frac{n}{j+1/2} - \frac34\right)\right],\qquad E_n = -\frac{13.6\,\text{eV}}{n^2}\,Z^2\ }$$

微扰论的适用性：修正 $\sim(Z\alpha)^2 E_n$，对 $Z\alpha \ll 1$ 自洽；重元素（$Z\alpha \to 1$）必须用 06s2 的精确谱。

**与 Dirac 精确解对账**（06s2 篇的 Sommerfeld–Dirac 公式展开到 $(Z\alpha)^4$）：逐项相同。这不是巧合：三项"相对论修正"本来就是 Dirac 方程非相对论展开的 $(v/c)^2$ 阶内容（Foldy–Wouthuysen 变换的产物），微扰论只是把它逐块算了一遍。微扰论多给不了的：$(Z\alpha)^6$ 项、以及 Lamb 位移（QED 真空极化与反常磁矩，把 $2s_{1/2}$ 抬到 $2p_{1/2}$ 之上 $4.4\ \mu$eV，即著名的 1057 MHz）——那是 QFT 书的领地。

## 5. 加磁场：Landé $g$ 因子

沿 $z$ 加均匀磁场 $B$，磁矩 $\vec\mu = -\mu_B(\vec L + g_s\vec S)/\hbar$，微扰

$$H_Z = -\vec\mu\cdot\vec B = \frac{\mu_B B}{\hbar}(L_z + g_s S_z),\qquad g_s = 2.0023\cdots\approx2.$$

**弱场**意味着 $H_Z \ll H_{so}$：总角动量 $j$ 仍是好量子数，$H_Z$ 在固定 $j$ 的多重态内投影。矢量模型（$\vec S$ 绕 $\vec J$ 进动，只有沿 $\vec J$ 的分量在多重态内平均后存活）：

$$\langle S_z\rangle = \frac{\langle\vec S\cdot\vec J\rangle}{j(j+1)\hbar^2}\,\langle J_z\rangle = m_j\,\frac{j(j+1)-l(l+1)+s(s+1)}{2j(j+1)},$$

（$\vec S\cdot\vec J = \frac12(\vec J^2-\vec L^2-\vec S^2)$ 的本征值代入。）于是

$$\boxed{\ \Delta E = \mu_B B\,g_j m_j,\qquad g_j = 1 + \frac{j(j+1)-l(l+1)+s(s+1)}{2j(j+1)}\ }$$

**Landé $g$ 因子**是 Wigner–Eckart 定理的一次轻量实战（矢量算符在多重态内只能平行于 $\vec J$，第 05 篇第 7 节）。速算：$2s_{1/2}: g = 2$；$2p_{1/2}: g = \tfrac23$；$2p_{3/2}: g = \tfrac43$。

- **正常塞曼**：$S = 0$ 的原子（或玻尔时代的轨道图像）$g_j = 1$，每条谱线裂成 $\Delta m = 0,\pm1$ 的等距三条——第 06 篇自检问题 5 已见过。
- **反常塞曼**：$g_j \ne 1$，谱线图样由上下能级的 $g_j$ 差决定，"反常"之名纯属历史（量子力学之前无法解释）。

## 6. 例题算到底：钠 D 双线的反常塞曼

钠的黄双线（$3p \to 3s$）是反常塞曼的标准样品：D$_1$：$3p\,^2P_{1/2}\to3s\,^2S_{1/2}$（$g = \tfrac23 \to 2$）；D$_2$：$3p\,^2P_{3/2}\to3s\,^2S_{1/2}$（$g = \tfrac43 \to 2$）。谱线位移（相对零场位置）：

$$\Delta\nu \propto \mu_B B\,(g_u m_{ju} - g_l m_{jl}),$$

只允许 $\Delta m_j = 0,\pm1$（电偶极选择定则，第 05 篇 7.3 节）。

**D$_1$**：上 $m_j = \pm\tfrac12$（$g_u m_j = \pm\tfrac13$），下 $m_j = \pm\tfrac12$（$g_l m_j = \pm1$）。允许跃迁的位移 $\mu_BB\cdot\{\pm\tfrac23,\ \pm\tfrac43\}$——**4 条线**。

**D$_2$**：上 $m_j = \pm\tfrac32,\pm\tfrac12$（$g_um_j = \pm2,\pm\tfrac23$），下同上。逐条排开位移为 $\mu_BB\cdot\{\pm\tfrac13,\ \pm1,\ \pm\tfrac53\}$——**6 条线**（完整清单见自检问题 4）。

四条对六条、间距不成比例——这就是 1920 年代"反常"的实验面貌，也是 Goudsmit 与 Uhlenbeck 提出电子自旋的原始动机之一。

## 7. 强场极限：Paschen–Back

**强场** $H_Z \gg H_{so}$：外磁场比原子内场强，$\vec L$ 与 $\vec S$ 各自绕 $\vec B$ 进动、彼此退耦，好量子数从 $m_j$ 换成 $(m_l, m_s)$：

$$\Delta E_{\rm PB} = \mu_B B\,(m_l + 2m_s) + \frac{mc^2(Z\alpha)^4}{4n^3}\,\frac{m_lm_s}{l(l+\tfrac12)(l+1)}\;\;(\text{残余自旋-轨道的一阶})，$$

第一条是主导项，第二条是退耦后 $\vec L\cdot\vec S \to \hbar^2 m_lm_s$ 的剩余修正。谱线：$\Delta m_l = 0,\pm1$、$\Delta m_s = 0$，位移主要由 $\mu_BB\,\Delta m_l$ 给出——**回归正常塞曼三重线**，自旋只贡献小修正。

两个极限之间（$H_Z \sim H_{so}$）：$H_Z$ 与 $H_{so}$ 不对易（前者挑 $L_z, S_z$，后者挑 $\vec J$），好量子数冲突，2×2 级别的矩阵没有解析对角化——数值解题（这一段与第 09 篇"两个表象各管一段"的思路同构）。同样的结构在共振电路、反交叉（avoided crossing）中反复出现：**两个微扰争夺好量子数时，中间地带没有解析解**。

## 8. 小结

| 修正/效应 | 公式 | 量级/备注 |
| --- | --- | --- |
| 相对论动能 | $-\frac{p^4}{8m^3c^2}$ | $\langle H_r\rangle = -\frac{E_n^2}{2mc^2}[\frac{4n}{l+1/2}-3]$ |
| 自旋-轨道 | $\frac{Ze^2}{2m^2c^2}\frac{\vec L\cdot\vec S}{r^3}$ | Thomas 因子 $\tfrac12$ 已含；只 $l\ge1$ |
| Darwin | $\frac{\pi\hbar^2Ze^2}{2m^2c^2}\delta^3(\vec r)$ | 只 $s$ 态；补齐 $2s_{1/2}$ |
| 精细结构总账 | $E_{nj} = E_n[1+\frac{(Z\alpha)^2}{n^2}(\frac{n}{j+1/2}-\frac34)]$ | 与 06s2 Dirac 展开一致 |
| Landé $g$ | $g_j = 1+\frac{j(j+1)-l(l+1)+s(s+1)}{2j(j+1)}$ | $2s:2$，$2p_{1/2}:\tfrac23$，$2p_{3/2}:\tfrac43$ |
| 反常塞曼 | $\Delta E = \mu_BB\,g_jm_j$ | D$_1$ 裂 4、D$_2$ 裂 6 |
| Paschen–Back | $\Delta E = \mu_BB(m_l+2m_s)+\cdots$ | 回归三重线；中间场数值解 |

一句话收束：$\alpha^4$ 阶的三项修正在 $j$ 基下自动对角，给出只依赖 $(n,j)$ 的精细结构；磁场一来，$g_j$ 把多重态的全部磁性压进一个数——弱场按 $m_j$ 拆、强场按 $(m_l,m_s)$ 拆，中间交给机器。微扰论在这里不是练习题，是氢原子光谱的逐条谱线。

## 自检问题

**1.** 用 $p^2 = 2m(E_n - V)$、维里定理与 $\langle r^{-2}\rangle = \frac{Z^2}{a_0^2n^3(l+1/2)}$ 推出 $\langle H_r\rangle_{nl} = -\frac{E_n^2}{2mc^2}\left[\frac{4n}{l+1/2}-3\right]$，并对 $2p$ 给出数值。

<details markdown="1"><summary>点击显示答案</summary>

$p^2\lvert\psi\rangle = 2m(E_n - V)\lvert\psi\rangle$ 两边平方取期望（$\psi$ 是 $H_0$ 本征态，$p^2$ 作用回本征值）：

$$\langle p^4\rangle = 4m^2\big\langle(E_n-V)^2\big\rangle = 4m^2\big[E_n^2 - 2E_n\langle V\rangle + \langle V^2\rangle\big].$$

库仑势维里定理：$\langle T\rangle = -E_n,\ \langle V\rangle = 2E_n$（$E_n<0$）。$\langle V^2\rangle = Z^2e^4\langle r^{-2}\rangle = Z^4e^4/(a_0^2n^3(l+\tfrac12))$。用 $e^2/a_0 = \alpha^2 mc^2$ 与 $E_n = -mc^2(Z\alpha)^2/2n^2$ 把它折成 $E_n$：$\langle V^2\rangle = \frac{4n^4E_n^2}{n^3(l+1/2)} = \frac{4nE_n^2}{l+1/2}$。代回：

$$\langle p^4\rangle = 4m^2E_n^2\Big[1 - 4 + \frac{4n}{l+1/2}\Big]\ \Rightarrow\ \langle H_r\rangle = -\frac{\langle p^4\rangle}{8m^3c^2} = -\frac{E_n^2}{2mc^2}\Big[\frac{4n}{l+1/2}-3\Big].$$

数值（$n=2,l=1$）：$E_2^2/2mc^2 = 1.13\times10^{-5}$ eV，方括号 $= \frac{8}{1.5}-3 = 2.33$，$\langle H_r\rangle_{2p} = -2.64\times10^{-5}$ eV。

</details>

**2.** 说明 Thomas 因子 $1/2$ 从哪来：给出"裸"自旋-轨道项与 Thomas 进动的结论；并算 $2p$ 自旋-轨道能移，验证与 §3.4 表中数值一致。

<details markdown="1"><summary>点击显示答案</summary>

电子静止系中原子核以 $-\vec v$ 运动，其电场变换出磁场 $\vec B' = -\vec v\times\vec E/c^2$。取 $\vec E = Ze^2\hat r/(4\pi\varepsilon_0r^2)$ 方向沿 $\hat r$（即 $V=-Ze^2/r$），$-\vec v\times\vec E \propto \vec v\times\hat r \cdot Ze^2/r^2 = -Ze^2(\vec r\times\vec v)/r^3 \cdot \frac{1}{4\pi\varepsilon_0}$，给出 $\vec B' = \frac{Ze^2}{mc^2r^3}\vec L$（高斯式简记）。$-\vec\mu_s\cdot\vec B'$ 用 $g_s=2$ 得"裸"耦合 $\frac{Ze^2}{m^2c^2r^3}\vec L\cdot\vec S$。但电子静止系相对实验室系在连续地转（速度方向变化 = 一系列无穷小 Lorentz 转动），其坐标系携带的 Thomas–Wigner 旋转角速度 $\vec\omega_T = \frac{\gamma^2}{\gamma+1}\frac{\vec a\times\vec v}{c^2} \approx \frac{1}{2c^2}\vec v\times\vec a$（$\gamma\approx1$），对圆轨道恰好贡献一项与裸耦合同形、系数 $-\tfrac12$ 的抵消项：净结果系数砍半。结论（引用标准推导）：

$$H_{so} = \frac{Ze^2}{2m^2c^2}\frac{\vec L\cdot\vec S}{r^3}.$$

数值：$\langle H_{so}\rangle = \frac{Ze^2}{2m^2c^2}\cdot\frac{Z^3}{a_0^3n^3l(l+1/2)(l+1)}\cdot\frac{\hbar^2}{2}\big[j(j+1)-l(l+1)-\tfrac34\big]$。$2p$：$\langle r^{-3}\rangle = \frac{1}{24a_0^3}$；$j=\tfrac12$：括号 $= \tfrac34-2-\tfrac34 = -2$；$j=\tfrac32$：括号 $= \tfrac{15}{4}-2-\tfrac34 = +1$。代 $\langle H_{so}\rangle = \frac{mc^2\alpha^4}{4n^3}\cdot\frac{\text{括号}}{l(l+1/2)(l+1)}$：$j=\tfrac12$ 得 $-\frac{mc^2\alpha^4}{48} = -3.02\times10^{-5}$ eV，$j=\tfrac32$ 得 $+\frac{mc^2\alpha^4}{96} = +1.51\times10^{-5}$ eV——与 §3.4 表一致，且差值 $4.53\times10^{-5}\ \text{eV} = mc^2\alpha^4/32$ 正是 $2p$ 精细结构裂距。

</details>

**3.** 用矢量模型投影推导 Landé $g$ 因子，并解释为什么 $2s_{1/2}$ 的 $g\approx2$ 直接暴露了 $g_s\approx2$ 这一纯自旋磁矩的"反常"。

<details markdown="1"><summary>点击显示答案</summary>

固定 $j$ 的多重态内，任何矢量算符的矩阵元都平行于 $\vec J$（Wigner–Eckart 的矢量版）。把 $\vec S$ 投影到 $\vec J$ 上：$\vec S_{\parallel} = \frac{\vec S\cdot\vec J}{J^2}\vec J$。磁场项取多重态内平均：

$$\langle H_Z\rangle = \frac{\mu_BB}{\hbar}\Big\langle L_z + g_sS_z\Big\rangle = \frac{\mu_BB}{\hbar}\Big\langle J_z + (g_s-1)S_z\Big\rangle = \frac{\mu_BB\,m_j}{\hbar^2 j(j+1)}\Big[\hbar^2j(j+1) + (g_s-1)\langle\vec S\cdot\vec J\rangle\Big],$$

其中 $\langle\vec S\cdot\vec J\rangle = \frac{\hbar^2}{2}[j(j+1)+s(s+1)-l(l+1)]$。整理：

$$g_j = 1 + (g_s-1)\,\frac{j(j+1)-l(l+1)+s(s+1)}{2j(j+1)} \xrightarrow{\ g_s\approx2\ } 1 + \frac{j(j+1)-l(l+1)+s(s+1)}{2j(j+1)}.$$

数值：$2s_{1/2}$：$l=0,\ j=s=\tfrac12$：第二项分子 $= \tfrac34+\tfrac34 = \tfrac32$，分母 $\tfrac32$，$g=2$；$2p_{1/2}$：$1+\frac{\tfrac34-2+\tfrac34}{\tfrac32} = 1-\tfrac13 = \tfrac23$；$2p_{3/2}$：$1+\frac{\tfrac{15}{4}-2+\tfrac34}{\tfrac{15}{2}} = 1+\tfrac13 = \tfrac43$。

$l=0$ 时 $\vec L = 0$，磁矩纯由自旋承担：$g = g_s \approx 2$——对电子这条"反常"值（Dirac 方程预言恰好 2，QED 修正为 2.0023）的最直接光谱读数，正是 $s$ 态 $g$ 因子的实验内容。

</details>

**4.** 列全钠 D$_2$ 线（$3p\,^2P_{3/2}\to3s\,^2S_{1/2}$）弱场中的全部允许跃迁，证明它裂成 6 条、位移为 $\mu_BB\cdot\{\pm\tfrac13,\pm1,\pm\tfrac53\}$；对比 D$_1$ 的 4 条。

<details markdown="1"><summary>点击显示答案</summary>

上能级 $g_u = \tfrac43$，$m_{ju} = \pm\tfrac32,\pm\tfrac12 \Rightarrow g_um_{ju} = \pm2,\pm\tfrac23$；下能级 $g_l = 2$，$m_{jl} = \pm\tfrac12 \Rightarrow g_lm_{jl} = \pm1$。位移 $\propto g_um_{ju} - g_lm_{jl}$，允许 $\Delta m_j = 0,\pm1$：

| $m_{ju}$ | $m_{jl}$ | $\Delta m_j$ | 位移（$\mu_BB$ 单位） |
| --- | --- | --- | --- |
| $+\tfrac32$ | $+\tfrac12$ | $-1$ | $2-1 = +1$ |
| $+\tfrac12$ | $+\tfrac12$ | $0$ | $\tfrac23-1 = -\tfrac13$ |
| $+\tfrac12$ | $-\tfrac12$ | $-1$ | $\tfrac23+1 = +\tfrac53$ |
| $-\tfrac12$ | $+\tfrac12$ | $+1$ | $-\tfrac23-1 = -\tfrac53$ |
| $-\tfrac12$ | $-\tfrac12$ | $0$ | $-\tfrac23+1 = +\tfrac13$ |
| $-\tfrac32$ | $-\tfrac12$ | $+1$ | $-2+1 = -1$ |

六个位移 $\{\pm\tfrac13,\pm1,\pm\tfrac53\}$，6 条线。D$_1$（$g_u = \tfrac23$，$m_{ju} = \pm\tfrac12$）：位移 $\pm\tfrac13\mp1 = \{\pm\tfrac23,\pm\tfrac43\}$，4 条。注意两组图样都不是正常塞曼的等距三条——"反常"的定量含义就是 $g_u\ne g_l\ne1$ 且随 $j,l$ 变化。

</details>

**5.** 写出 $2p$ 在强场（Paschen–Back）极限的能级公式，证明谱线回归正常塞曼三重线；并说明弱场与强场之间为什么必须数值对角化。

<details markdown="1"><summary>点击显示答案</summary>

强场下好量子数 $(m_l, m_s)$，$m_l = -1,0,1$，$m_s = \pm\tfrac12$：

$$E = E_2 + \mu_BB(m_l + 2m_s) + \zeta\,m_lm_s\hbar^2,\qquad \zeta = \frac{e^2}{2m^2c^2}\langle r^{-3}\rangle_{2p} = \frac{e^2}{48m^2c^2a_0^3}\ (\text{即}\ H_{so}\ \text{的系数}).$$

末态 $2s$：$m_l = 0$，能级 $E_2 + 2\mu_BBm_s$（自旋-轨道为零）。允许 $\Delta m_l = 0,\pm1,\ \Delta m_s = 0$，位移 $= \mu_BB\,\Delta m_l + \zeta\hbar^2 m_s(m_l - 0)$：主导部分就是 $\mu_BB\{0,\pm1\}$ 的**等距三条**（正常塞曼），每条再被自旋-轨道残余 $\zeta\hbar^2m_sm_l$ 轻推（每条裂两个自旋分量，间隔 $2\zeta\hbar^2\lvert m_l\rvert$，弱到常被滤掉）。

中间场强：$H_{so}$ 挑 $\vec J$ 基、$H_Z$ 挑 $(m_l,m_s)$ 基，两者不对易；固定 $m_j = m_l + m_s$ 的子空间（最多二维，如 $m_j = \tfrac12$ 含 $\lvert m_l0\,m_s{+}\tfrac12\rangle$ 与 $\lvert m_l1\,m_s{-}\tfrac12\rangle$）内要解 $2\times2$ 矩阵 $\begin{pmatrix}\mu_BB\Delta & \zeta' \\ \zeta' & -\mu_BB\Delta'\end{pmatrix}$ 型方程，本征值含平方根 $\sqrt{(\mu_BB\Delta)^2+\lvert\zeta'\rvert^2}$——两个极限各是它的近似分支，中间是反交叉式的光滑过渡，无解析闭式（数值对角化一秒钟的事）。同一结构即量子霍尔与分子光谱里反复出现的"好量子数换岗"。

</details>

## 参考

- Griffiths《量子力学概论》§6.3（精细结构：三项修正、Thomas 因子与逐项微扰）、§6.4（Zeeman 效应与 Paschen–Back）——本篇主线的标准来源。
- Shankar《Principles of Quantum Mechanics》精细结构与 Zeeman 相关章——矢量模型投影讲得细。
- 朗道《量子力学》精细结构章节——$j$ 依赖性与相对论修正的紧凑处理。
- 本书第 06s2 篇（[Dirac 方程精确解氢原子](06s2-dirac-hydrogen.md)）——精确谱与 $(Z\alpha)^4$ 展开的对账对象。
- 本书第 05 篇第 7 节（Wigner–Eckart 与选择定则）——Landé 投影与 $\Delta m_j$ 规则的群论地基。
