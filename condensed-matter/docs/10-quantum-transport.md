# 量子输运浅尝：Landauer 公式、电导量子化与局域化

> 路线图位置：第三部分（现代专题）· 第 10 章
> 前置知识：[第 3 章](03-free-electron-gas.md)（自由电子气；尤其是 §4.5 的玻尔兹曼方程与 $k_Fl\gg1$ 判据——本章从那条边界接着走）；[第 4 章](04-band-theory.md)（能带与 Bloch 波）；量子力学书[第 10 篇](../../quantum-mechanics/docs/10-linear-response-kubo.md)（Kubo 公式——同一物理的另一套语言）。
> 学习目标：会用三个长度尺度（平均自由程 $l$、样品尺寸 $L$、相位相干长度 $L_\varphi$）给输运问题分类；会推导两端口 Landauer 公式 $G=(2e^2/h)\sum_n T_n$，说清"1D 流强与色散无关"这个支点；理解接触电阻（Sharvin）与两端口/四端口电阻之差；会解释量子点接触的电导量子化平台（van Wees, 1988）并估算通道数与温度要求；知道弱局域化（相干背散射）、AB 振荡与普适电导涨落是相位相干的实验指纹；会用 Thouless 数与标度函数 $\beta(g)$ 说明一维/二维总是局域化、三维有无序驱动的金属–绝缘体转变（Anderson）；知道 Landauer–Büttiker 公式如何把量子霍尔电导读成边缘通道计数（第 11 章）。
>
> 记号约定：沿用本书（保留 $\hbar$ 与 $k_B$；电磁量用高斯单位制）。本章 $G$ 一律是电导（不是格林函数）；$T_n$ 为第 $n$ 个通道的透射概率，$R_n=1-T_n$。

---

## 1. 一句话总结

**当样品小到电子跑完全程不失相位记忆（$L\lt L_\varphi$），电阻就不再是"材料的性质"而是"散射体 + 接线方式"的性质：Landauer 把电导改写成透射概率的账本 $G=(2e^2/h)\sum_n T_n$——每个横向量子模式是一条通道，每通道满透射贡献普适值 $2e^2/h$。这个公式贯通三个介观地标：弹道点接触的电导量子化平台（每开放一条通道跳 $2e^2/h$）、扩散区的弱局域化修正（相位相干的 $\sim e^2/h$ 级压低）、以及 $k_Fl\to1$ 处的 Anderson 局域化（透射指数坍缩，电导失去自平均性）；量子霍尔效应的 $\sigma_{xy}=\nu e^2/h$ 则是它在手征边缘通道上最纯粹的胜利。**

## 2. 三个长度尺度：输运的版图

[第 3 章](03-free-electron-gas.md) §4.5 在 $k_Fl\sim1$ 处把玻尔兹曼方程封存，本章从那里接着走。先把版图钉在三个长度尺度上：

- **弹性平均自由程 $l=v_F\tau$**：动量弛豫的尺度。低温下由杂质与缺陷主导——弹性散射改变方向但不洗牌相位；
- **相位相干长度 $L_\varphi=\sqrt{D\tau_\varphi}$**：波函数保持相位记忆的尺度，由非弹性过程（电子–声子、电子–电子）决定。$\tau_\varphi\propto T^{-p}$（$p$ 量级为 1）随降温变长，故 $L_\varphi$ 随 $T\to0$ 发散——低温是介观物理的引擎；
- **样品尺寸 $L$**。

三个尺量的排序给出四个输运区域：

| 区域 | 尺度关系 | 理论框架 | 招牌现象 |
|---|---|---|---|
| 经典（欧姆）扩散 | $l\ll L$ 且 $L_\varphi\ll L$ | 玻尔兹曼（第 3 章） | 欧姆律、电阻串并联 |
| 弹道 | $L\ll l,\ L_\varphi$ | Landauer（纯透射） | 电导量子化、Sharvin 电阻 |
| 介观扩散（相干） | $l\ll L\ll L_\varphi$ | Landauer + 干涉 | 弱局域化、UCF、AB 振荡 |
| 强局域 | $k_Fl\sim1$ | 标度理论 / 局域化 | Anderson 金属–绝缘体转变 |

统一视角：**量子输运 = 电子的波动性直接参与导电**。玻尔兹曼理论已经把电子当波（$\vec k$ 态、费米面），但把路径之间的相位平均掉了；当 $L_\varphi$ 超过样品尺寸，这个平均不再合法，基本对象从透射**概率**变成透射**振幅**。

## 3. Landauer 公式：电导 = 透射

### 3.1 设置：散射体 + 库

理想导线连接两个大库（reservoir）：左库化学势 $\mu_L$、右库 $\mu_R$，偏压窗口 $\mu_L-\mu_R=eV$。库的定义性性质：进入库的电子在其中非弹性弛豫到热平衡——相位记忆在库里被洗掉，库就是 $L_\varphi$ 的终点。导线中间可以放任意散射体（势垒、无序区、点接触），它对第 $n$ 个横向模式的透射概率为 $T_n$。整个装置的电流只由"库往通道里注什么、通道放过去多少"决定。

### 3.2 1D 单通道：流强与色散无关

取一条 1D 通道，色散 $\varepsilon(k)$ 任意。左库注入的右行电子占据到 $\mu_L$，右库注入的左行电子占据到 $\mu_R$。净电流（自旋因子 2）：

$$I = 2e\int_{k\gt0}\frac{dk}{2\pi}\,v(k)\,T(\varepsilon)\,f_L(\varepsilon)\;-\;2e\int_{k\lt0}\frac{dk}{2\pi}\,\lvert v(k)\rvert\,T(\varepsilon)\,f_R(\varepsilon), \qquad v(k) = \frac{1}{\hbar}\frac{d\varepsilon}{dk}.$$

关键一步：换元 $dk\,v = d\varepsilon/\hbar$——**1D 里态密度 $dk/d\varepsilon\propto1/v$ 与群速度恰好相消**，每单位能量贡献的流强是与色散完全无关的常数：

$$I = \frac{2e}{h}\int d\varepsilon\;T(\varepsilon)\,\big[f_L(\varepsilon)-f_R(\varepsilon)\big].$$

线性响应极限（小 $V$、$T(\varepsilon)$ 在窗口内缓变）：$f_L-f_R\approx(-\partial f/\partial\varepsilon)\,eV$，零温下 $(-\partial f/\partial\varepsilon)=\delta(\varepsilon-E_F)$，于是

$$\boxed{\;G = \frac{I}{V} = \frac{2e^2}{h}\,T(E_F)\;}$$

多通道推广直截了当：横向（垂直于电流）的束缚把模式量子化，每条子带是一条独立的 1D 通道：

$$G = \frac{2e^2}{h}\sum_{n=1}^{M}T_n \qquad(\text{Landauer 公式}).$$

注意这个公式里**没有材料参数**：载流子浓度、有效质量、色散关系全部被 1D 流强的普适性吸收，剩下的只有通道数与透射概率。完整的逐步推导见自检问题 1。

### 3.3 接触电阻：$T=1$ 时电阻不是零

即使完美透射（$T_n=1$），$G=(2e^2/h)M$ 也有限——**每通道电阻 $h/2e^2\approx12.9$ kΩ**。这不是散射造成的，而是**接触电阻**（Sharvin 电阻）：宽库里横着天文数字个模式，窄导线只放行 $M$ 条，载流子必须"挤进"有限的通道，电压降因此落在导线与库的接口处，而不在导线内部。

两端口与四端口测量的差别把这一点说透（推导留作自检问题 2）：单通道散射体（透射 $T$、反射 $R=1-T$），

$$R_{\rm 2t} = \frac{h}{2e^2}\frac{1}{T}, \qquad R_{\rm 4t} = \frac{h}{2e^2}\frac{R}{T},$$

即

$$R_{\rm 2t} = \underbrace{\frac{h}{2e^2}}_{\text{接触（弹道也有）}} + \underbrace{\frac{h}{2e^2}\frac{R}{T}}_{\text{散射（四端口测的是它）}}.$$

四端口的电压探针不取电流，把接口压降从测量中剔除。这是介观测量最深刻的方法论教训：**电导不是体材料属性，而是"散射体 + 库 + 探针"整个装置的属性**——追问"这段导线的电阻"而不说明接线方式，在介观尺度上没有意义。

### 3.4 回到欧姆律：扩散极限的对接

Landauer 与第 3 章的玻尔兹曼必须在大尺度上汇合。对接如下（完整代数见自检问题 3）：宽 $W$、长 $L$ 的二维无序导体有 $M=k_FW/\pi$ 条通道，扩散区的无序平均透射为 $\sum_nT_n=(\pi/2)M\,l/L$，于是

$$G = \frac{2e^2}{h}\cdot\frac{\pi}{2}M\,\frac{l}{L} = \frac{ne^2\tau}{m}\,\frac{W}{L} = \sigma\,\frac{W}{L},$$

正是欧姆律。**电阻的串并联加性不是公理，而是透射概率在扩散无序平均下的涌现性质**——相位在 $L\gg L_\varphi$ 时被洗掉，概率（而非振幅）相加，$R\propto L$ 才成立。这同时给了 $l$ 一个 Landauer 语言的操作定义：它就是"透射概率随长度线性下降的斜率"。

## 4. 电导量子化：量子点接触

最干净的弹道器件是**量子点接触（QPC）**：在二维电子气（GaAs/AlGaAs 异质结，典型 $n\sim3\times10^{15}$ m$^{-2}$、$m^\ast=0.067m_e$、$l$ 可达 $10\ \mu$m 量级）上，用分裂门电极的耗尽区挤出一条宽度 $W\sim10^2$ nm 的可调窄口。$W$ 与费米波长可比（$\lambda_F\approx46$ nm），横向束缚把能谱切成 1D 子带——每条子带就是一条 Landauer 通道。

绝热（波导）近似下，通道开否由最窄处决定：第 $n$ 条子带的横向束缚能 $E_n(W)$ 低于 $E_F$ 则开放且 $T_n\approx1$（绝热通过，反射可忽略），高于 $E_F$ 则关闭。扫门电压 = 扫 $W$ = 扫开放通道数 $N$：

$$G = \frac{2e^2}{h}\,N, \qquad N = 0,1,2,\cdots$$

——**电导本身是量子化的**，平台间隔 $2e^2/h\approx(12.9\ \mathrm{k\Omega})^{-1}$。van Wees 与 Wharam 两个组 1988 年同时观测到这组平台，是介观物理的开门实验。数值账（通道数、子带间距、所需温度）见自检问题 4。

三个注记：

- 看清平台的条件：$k_BT\ll$ 子带间距（典型在 $4$ K 以下，最好稀释制冷机）且弹道 $L\ll l$；
- 与第 3 章 §4.5 的漂移图像对照：那里电流是费米球的微小倾斜，这里电流是"左右库化学势差打开的透射窗口"——同一金属导电的两种语言，在扩散极限（§3.4）汇合；
- 实验上 $0.7\times(2e^2/h)$ 处有个著名的"0.7 反常"肩结构，涉及相互作用与自旋，至今没有完全一致的解释——本章的独立电子框架不覆盖它，留作第 6/13 章相互作用话题的悬案注脚。

## 5. 相位相干的指纹：AB 振荡、弱局域化、普适涨落

介观区（$l\ll L\ll L_\varphi$）里电子是扩散的，但相位活着，干涉直接改写电导：

- **Aharonov–Bohm 振荡**：金属环的电导随穿过环的磁通以 $h/e$ 为周期振荡——绕环两臂的路径相位差被磁通调制（Webb 等 1985 年在金环上观测到；要求 $L_\varphi$ 大于环周长）；
- **弱局域化（WL）**：扩散电子回到出发点的量子概率是**时间反演路径对振幅之和的模方**。零动量转移处两条路径相位精确相同，干涉相长：

$$P_{\rm qm} = \lvert A_+ + A_-\rvert^2 = 4\lvert A\rvert^2 = 2P_{\rm cl},$$

返回概率被相干倍增——电子"更容易迷路回头"，扩散变慢，电导被压低 $\sim e^2/h$ 量级（二维下是对数修正 $\delta\sigma\approx-(e^2/2\pi^2\hbar)\ln(L_\varphi/l)$）。垂直磁场给两条路径相反的 AB 相位、杀掉干涉——电阻随磁场**下降**（负磁阻），这是 WL 的招牌，也是下节 $\beta(g)$ 在 $g\gg1$ 端的第一项修正。环的磁阻里周期为 $h/2e$ 的 Altshuler–Aronov–Spivak 谐波与 WL 同源。
- **普适电导涨落（UCF）**：具体样品的杂质位形决定具体干涉图样，电导随磁场或门电压跑出**可重复但对样品特异**的涨落，量级恒为 $\sim e^2/h$，与平均电导和尺寸无关——"介观指纹"。它同时宣告：这个区域里电导失去自平均性，涨落与均值同级，系综平均不再是好描述。

## 6. 无序的终点：Anderson 局域化与标度理论

把无序调强到 $k_Fl\to1$（Ioffe–Regel 判据，第 3 章 §4.5 埋的线在此收）：平均自由程短到接近波长，"两次散射之间自由飞行"的图像瓦解，干涉不再是修正而是主导。Anderson（1958）的判决：强无序下本征波函数**空间指数局域**（包络 $\sim e^{-\lvert\vec r\rvert/\xi}$，$\xi$ 为局域化长度），$T=0$ 电导率严格为零——这是一种**没有能隙的绝缘体**（态密度连续，但态是局域的），与第 4 章的能带绝缘体、第 13 章的 Mott 绝缘体（相互作用驱动）并列为第三种绝缘机制：无序驱动。

有限无序下是否局域化，由**标度理论**（Abrahams–Anderson–Licciardello–Ramakrishnan, 1979）回答。定义 Thouless 数

$$g(L) = \frac{E_{\rm Th}}{\delta E}, \qquad E_{\rm Th} = \frac{\hbar D}{L^2}\ (\text{扩散穿越能}),\quad \delta E = \frac{1}{\nu L^d}\ (\text{能级间距}),$$

它正比于无量纲电导 $G/(e^2/h)$（自检问题 5）：$g\gg1$ 时电子在能级间自由穿行（金属），$g\ll1$ 时走不出局域邻域（绝缘体）。假设 $g$ 的标度流只由 $g$ 自身决定：$\beta(g)\equiv d\ln g/d\ln L$。两个渐近区钉死曲线：

- $g\gg1$（金属端）：欧姆律 $g\propto L^{d-2}$ 加 WL 修正，$\beta(g)\to d-2-a/g$（$a\gt0$）；
- $g\ll1$（局域端）：透射指数坍缩 $g\propto e^{-L/\xi}$，$\beta(g)\approx\ln(g/g_c)\lt0$。

逐维读出命运：

- **$d=1$**：$\beta$ 处处为负——任意弱无序都局域化（与 [20s](20s-luttinger-liquid.md) 的 Luttinger 液体结论遥相呼应：一维电子系统没有真正的金属态）；
- **$d=2$**：$\beta\lt0$ 但从零负起——所有态技术上都是局域的，只是 $k_Fl$ 大时 $\xi\sim l\,e^{\pi k_Fl/2}$ 天文数字般大，弱局域化的对数修正正是它的先兆。"（退火无序、$T=0$ 的）二维金属不存在"曾是定理级结论；2DEG 中表观的金属–绝缘体转变至今是研究前沿；
- **$d=3$**：$\beta$ 穿过零点——$g\gt g_c$ 是金属、$g\lt g_c$ 局域，$g_c$ 是不稳定不动点：**无序驱动的金属–绝缘体转变**（Anderson 转变），临界行为 $\sigma\propto(n-n_c)^\mu$、$\xi\propto\lvert n-n_c\rvert^{-\nu}$，一参数标度给出 $\mu=\nu$（$\epsilon$ 展开估计 $\nu\approx1$，现代数值给 $\nu\approx1.57$，框架存活）。

## 7. 接口：边缘通道与量子霍尔

Landauer 框架最辉煌的战果在磁场里。[第 11 章](11-quantum-hall-effect.md)会看到：量子霍尔样品的手征边缘态就是理想 1D 通道——单向传播、背散射被手征性禁戒，$T=1$ 严格成立。多端口推广（Landauer–Büttiker 公式 $I_i=(e^2/h)\sum_j(T_{ji}\mu_i-T_{ij}\mu_j)$）把 Hall 平台的精确量子化读成**边缘通道计数**：$\sigma_{xy}=\nu e^2/h$，每个填充的 Landau 能级贡献一条通道（详见第 11 章 §7）。第 12 章会把"通道数 = 体的拓扑不变量"提升为体–边对应的一般结构。

本章刻意没展开的两个方向：相互作用下的透射理论（Meir–Wingreen 公式，需要 Keldysh 格林函数——语言在[第 17 章](17-beyond-dft-gw-dmft.md)备好），以及库仑阻塞与人造原子（介观的另一半江湖，与[第 13 章](13-strong-correlations.md)强关联相接）。

## 小结

- 版图：$l$、$L$、$L_\varphi$ 三个长度尺度分出院落（经典扩散 / 弹道 / 介观相干 / 强局域）；$L_\varphi$ 随降温发散，是低温物理的引擎。
- Landauer 公式 $G=(2e^2/h)\sum_nT_n$：支点是 1D 流强与色散无关（态密度 × 群速度相消），材料参数全部隐去。
- 接触电阻 $h/2e^2\approx12.9$ kΩ/通道是模式数失配的几何电阻；两端口含它、四端口剔它——**电阻是装置的属性**。
- 弹道点接触：通道逐条开放，$G=(2e^2/h)N$ 平台（van Wees/Wharam 1988）；0.7 反常是相互作用留下的悬案。
- 介观干涉三指纹：AB 振荡（$h/e$）、弱局域化（返回概率相干倍增 → 负磁阻）、UCF（$\sim e^2/h$ 的样品指纹，电导不自平均）。
- Anderson 局域化：$k_Fl\sim1$ 后波函数指数局域，是没有能隙的绝缘体；标度理论 $\beta(g)$ 逐维判决——1D/2D 总局域化，3D 有真正的无序驱动转变（$\mu=\nu$）。
- 边缘态 = $T=1$ 的手征通道，$\sigma_{xy}=\nu e^2/h$ 是通道计数（第 11 章）；相互作用版本（Keldysh/Meir–Wingreen）留给第 17 章之后。

## 自检问题

**1.** 从 1D 通道的电流积分出发推导 Landauer 公式：证明任意色散下单通道单位能量流强是常数，并在线性响应、零温极限给出 $G=(2e^2/h)T(E_F)$。

<details markdown="1"><summary>点击显示答案</summary>

自旋因子 2。左库注入的右行态占据到 $\mu_L$，贡献电流

$$I_+ = 2e\int_{k\gt0}\frac{dk}{2\pi}\,v(k)\,T(\varepsilon)\,f_L(\varepsilon),$$

右库注入的左行态同理给出 $I_-$。对右行支换积分变量：$dk\,v = d\varepsilon/\hbar$（由 $v=\hbar^{-1}d\varepsilon/dk$），态密度与速度的乘积

$$\frac{dk}{d\varepsilon}\,v = \frac{1}{\hbar v}\,v = \frac{1}{\hbar}$$

是与色散**完全无关**的常数——这就是整个 Landauer 公式的支点（三维里这个对消不存在，所以必须先把横向模式量子化成独立的 1D 通道）。于是

$$I = \frac{2e}{2\pi\hbar}\int d\varepsilon\;T(\varepsilon)\,[f_L-f_R] = \frac{2e}{h}\int d\varepsilon\;T(\varepsilon)\,[f_L-f_R].$$

线性响应：$f_L-f_R = f(\varepsilon-\mu_L)-f(\varepsilon-\mu_R)\approx(-\partial f/\partial\varepsilon)(\mu_L-\mu_R) = (-\partial f/\partial\varepsilon)\,eV$。零温下 $-\partial f/\partial\varepsilon = \delta(\varepsilon-E_F)$，积分直接读出

$$I = \frac{2e}{h}T(E_F)\,eV \qquad\Longrightarrow\qquad G = \frac{2e^2}{h}T(E_F).\qquad\blacksquare$$

有限温度下 $G=(2e^2/h)\int d\varepsilon\,T(\varepsilon)(-\partial f/\partial\varepsilon)$——透射概率被 $k_BT$ 宽度的窗口平均，这正是平台边沿被温度抹圆的机制（自检问题 4）。

</details>

**2.** 两端口与四端口：对单通道散射体（透射 $T$、反射 $R=1-T$），用"电压探针不取电流、化学势浮动到两侧来流的加权平均"的条件，推导 $R_{\rm 2t}=(h/2e^2)(1/T)$ 与 $R_{\rm 4t}=(h/2e^2)(R/T)$，并说明接触电阻的物理位置。

<details markdown="1"><summary>点击显示答案</summary>

**两端口**：直接由 Landauer 公式，$G=(2e^2/h)T$，故

$$R_{\rm 2t} = \frac{1}{G} = \frac{h}{2e^2}\frac{1}{T}.$$

$T=1$ 时 $R_{\rm 2t}=h/2e^2\neq0$——电阻不来自散射体而来自接口。

**四端口**：在散射体两侧各接一个电压探针（探针 = 不取净电流的第三个库）。看散射体左侧：右行流直接来自左库，化学势 $\mu_L$；左行流是"被反射回来的左库电子（份额 $R$，化学势 $\mu_L$）+ 从右库透射过来的电子（份额 $T$，化学势 $\mu_R$）"的混合，故其化学势为 $R\mu_L+T\mu_R$。探针把两个方向来流的平均作为自己的化学势：

$$\mu_A = \frac{\mu_L+(R\mu_L+T\mu_R)}{2} = \mu_L-\frac{T}{2}(\mu_L-\mu_R),$$

同理右侧探针 $\mu_B = \mu_R+\frac{T}{2}(\mu_L-\mu_R)$。于是

$$eV_{\rm 4t} = \mu_A-\mu_B = (1-T)(\mu_L-\mu_R) = R\,\Delta\mu,$$

而电流仍是 $I=(2e/h)T\Delta\mu$，故

$$R_{\rm 4t} = \frac{V_{\rm 4t}}{I} = \frac{h}{2e^2}\frac{R}{T}.\qquad\blacksquare$$

**对照**：$R_{\rm 2t} = \frac{h}{2e^2}\frac{T+R}{T} = \frac{h}{2e^2} + R_{\rm 4t}$——两端口电阻 = 接触电阻 + 散射电阻。接触电阻的物理位置在导线–库接口（模式数失配处），不在散射体上；弹道导线（$T=1$）的四端口电阻为零而两端口电阻不为零，这曾经让 Landauer 公式被质疑（"没有散射哪来的电阻"），答案就是：电阻的耗散发生在库里（注入的非平衡载流子在库中非弹性弛豫放热），但**压降的位置**由公式忠实记录在接口上。

</details>

**3.** 扩散对接：二维宽 $W$、长 $L$（$L\gg l$）的无序导体，取通道数 $M=k_FW/\pi$ 与无序平均透射 $\sum_nT_n=(\pi/2)M(l/L)$，证明 Landauer 公式化为欧姆律 $G=\sigma W/L$（$\sigma=ne^2\tau/m$），从而说明电阻的加性（串联相加）在扩散极限涌现。

<details markdown="1"><summary>点击显示答案</summary>

代入 Landauer 公式：

$$G = \frac{2e^2}{h}\cdot\frac{\pi}{2}\cdot\frac{k_FW}{\pi}\cdot\frac{l}{L} = \frac{e^2k_Fl}{2\pi\hbar}\cdot\frac{W}{L},$$

（用了 $h=2\pi\hbar$）。另一侧，二维自由电子气（自旋 2 重）：$n = k_F^2/2\pi$，故 Drude 电导率

$$\sigma = \frac{ne^2\tau}{m} = \frac{k_F^2e^2\tau}{2\pi m} = \frac{k_F^2e^2}{2\pi m}\cdot\frac{l}{v_F} = \frac{k_F^2e^2l}{2\pi\hbar k_F} = \frac{e^2k_Fl}{2\pi\hbar},$$

（用了 $l=v_F\tau$ 与 $mv_F=\hbar k_F$）。两式逐项相同：

$$G = \sigma\,\frac{W}{L}.\qquad\blacksquare$$

**物理**：无序平均透射 $\propto l/L$ 正是扩散的指纹（透射概率随厚度反比下降——随机行走 $\langle x^2\rangle=2Dt$ 的另一面）。$G\propto1/L$ 即"串联电阻相加"、$G\propto W$ 即"并联相加"——欧姆律的全部几何内容，都被 Landauer 公式在 $L\gg l$、$L\gg L_\varphi$（相位已洗）的极限里重现。反过来，$l$ 的操作定义可以从透射斜率读出：$\sum_nT_n = (\pi/2)M\,l/L$。

</details>

**4.** 数值账：GaAs 2DEG（$n=3\times10^{15}\ \mathrm{m^{-2}}$、$m^\ast=0.067m_e$）的点接触最窄处 $W\approx100$ nm。估算 $k_F$、$\lambda_F$ 与开放通道数 $N$；用硬壁模型估计子带间距，给出观测平台所需的温度量级。

<details markdown="1"><summary>点击显示答案</summary>

**费米波矢**（2D、自旋 2 重，$n=k_F^2/2\pi$）：

$$k_F = \sqrt{2\pi n} = \sqrt{2\pi\times3\times10^{15}} \approx 1.37\times10^{8}\ \mathrm{m^{-1}}, \qquad \lambda_F = \frac{2\pi}{k_F} \approx 46\ \mathrm{nm}.$$

**通道数**：横向动量量子化 $k_y=m\pi/W$，开放条件 $\lvert k_y\rvert\lt k_F$：

$$N = \frac{k_FW}{\pi} = \frac{1.37\times10^{8}\times10^{-7}}{\pi} \approx 4.4 \quad\Rightarrow\quad N=4\ \text{条开放}.$$

门电压把 $W$ 从 0 扫到数百 nm，$N$ 逐条增加——平台上 $G = 2e^2/h,\ 4e^2/h,\ 6e^2/h\cdots$

**子带间距与温度**：硬壁 $E_m = m^2\pi^2\hbar^2/(2m^\ast W^2)$。基尺

$$E_1 = \frac{\pi^2\hbar^2}{2m^\ast W^2} = \frac{9.87\times(1.055\times10^{-34})^2}{2\times0.067\times9.11\times10^{-31}\times10^{-14}} \approx 9.0\times10^{-23}\ \mathrm J \approx 0.56\ \mathrm{meV} \approx 6.5\ \mathrm K.$$

费米能 $E_F = \hbar^2k_F^2/2m^\ast \approx 10.7$ meV（核对：$E_4 = 16E_1\approx9.0$ meV $\lt E_F \lt E_5\approx14$ meV，自洽于 $N=4$）。最顶通道附近的间距 $\Delta E = E_5-E_4\approx5$ meV$\approx58$ K（硬壁偏陡，真实抛物型约束更软，实际间距小几倍）。平台要锐利需 $k_BT\ll\Delta E$，即 **$T$ 在 4 K 以下、最好稀释制冷机**；同时要求弹道 $L\ll l$——该迁移率（$\mu\sim10^6\ \mathrm{cm^2/Vs}$）下 $l=\mu\hbar k_F/e\sim10\ \mu\mathrm m$，对 $100$ nm 的窄口绰绰有余。

</details>

**5.** Thouless 数与标度函数：证明 $g=E_{\rm Th}/\delta E$ 正比于无量纲电导 $G/(e^2/h)$（用 Einstein 关系 $\sigma=e^2\nu D$）；写出 $\beta(g)$ 在两个渐近区的形式，并据此说明 $d=1,2,3$ 各自的命运与 $d=3$ 的临界行为。

<details markdown="1"><summary>点击显示答案</summary>

**Thouless 数 ∝ 电导**：

$$g = \frac{E_{\rm Th}}{\delta E} = \frac{\hbar D}{L^2}\cdot\nu L^d = \hbar\nu D\,L^{d-2} = \frac{\hbar}{e^2}\,\sigma L^{d-2} = \frac{\hbar}{e^2}G = \frac{1}{2\pi}\cdot\frac{G}{e^2/h},$$

第三步用了 Einstein 关系 $\sigma=e^2\nu D$（与第 3 章 §4.5 的 $\sigma=\tfrac{e^2\tau}{3}g(E_F)v_F^2$ 是同一式：$D=\tfrac13v_F^2\tau$）。物理读法：$E_{\rm Th}$ 是电子扩散穿越样品的能量代价，$\delta E$ 是能级间距；$g\gg1$ 时一个波包里叠着许多能级、电子走得出去（金属），$g\ll1$ 时走不出去（绝缘体）。

**渐近**：金属端欧姆律 $G\propto L^{d-2}$（加弱局域化修正 $-a/g$），$\beta\to d-2-a/g$；局域端 $g\propto e^{-L/\xi}$，$\beta = \ln(g/g_c)\lt0$。

**逐维判决**（设 $\beta$ 单调连接两端）：

- $d=1$：$\beta \le -1-a/g\lt0$ 恒成立——$g$ 随 $L$ 单调衰减，任意弱无序都流向局域；
- $d=2$：$\beta = -a/g\lt0$ 恒成立——同上，但衰减慢（对数）；从 WL 修正反解出 $\xi\sim l\,e^{\pi k_Fl/2}$，$k_Fl$ 稍大就天文数字，故"二维总是绝缘体"在实验尺度上可能永远看不见；
- $d=3$：$\beta(+\infty)=+1\gt0$ 而 $\beta(0^+)\to-\infty$，必有零点 $g_c$：$g\gt g_c$ 流向金属、$g\lt g_c$ 流向局域——**$g_c$ 就是无序驱动的金属–绝缘体转变**。在 $g_c$ 附近线性化 $\beta\approx\beta'(g_c)\ln(g/g_c)$，积分给出 $\xi\propto\lvert g-g_0\rvert^{-\nu}$、$\nu = 1/\beta'(g_c)$；由 $G=\sigma L$ 与 $\sigma\propto\xi^{-1}$（标度上唯一的长度是 $\xi$）得 $\mu=\nu$。$\epsilon=d-2$ 展开给 $\nu\approx1$，数值对角化（转移矩阵）给 $\nu\approx1.57$。

</details>

## 参考

- Datta《Electronic Transport in Mesoscopic Systems》第 1–3 章：Landauer 图景、接触电阻与电导量子化——本章主线参考。
- Beenakker & van Houten, Solid State Physics 44, 1 (1991)：弹道输运与量子点接触的系统综述。
- 原始文献：Landauer, IBM J. Res. Dev. 1, 223 (1957) 与 Philos. Mag. 21, 863 (1970)；van Wees et al., Phys. Rev. Lett. 60, 848 (1988) 与 Wharam et al., J. Phys. C 21, L209 (1988)（电导量子化）；Büttiker, Phys. Rev. Lett. 57, 1761 (1986)（多端口公式）。
- Imry《Introduction to Mesoscopic Physics》第 2–5 章：AB 振荡、弱局域化、UCF；Lee & Ramakrishnan, Rev. Mod. Phys. 57, 287 (1985)：无序电子系统综述。
- Anderson, Phys. Rev. 109, 1492 (1958)（局域化原文）；Thouless, Phys. Rep. 13, 93 (1974)（Thouless 数）；Abrahams, Anderson, Licciardello & Ramakrishnan, Phys. Rev. Lett. 42, 673 (1979)（标度理论）；Wegner, Z. Phys. B 25, 327 (1976)（$\epsilon$ 展开）。
- 交叉参考：本书[第 3 章](03-free-electron-gas.md) §4.5（半经典边界与 Ioffe–Regel）、[第 11 章](11-quantum-hall-effect.md)（边缘通道与 Hall 平台）、[20s](20s-luttinger-liquid.md)（一维无金属世界）、量子力学书[第 10 篇](../../quantum-mechanics/docs/10-linear-response-kubo.md)（Kubo 语言：同一电导的平衡涨落读法）。
