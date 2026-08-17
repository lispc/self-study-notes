# 散射理论基本概念：截面、分波与 Born 近似

> 路线图位置：第 2 阶段（量子力学）· 散射理论基本概念
> 前置知识：定态薛定谔方程、概率流、角动量理论与球谐函数（见 [SO(3)/SU(2) 与角动量](../stage-00-math/01-so3-su2-and-angular-momentum.md)）、含时微扰论与费米黄金定则。
> 学习目标：掌握截面与散射振幅的定义和关系；会用分波展开与 Born 近似这两种主力方法算截面；理解光学定理、散射长度与共振；亲手从 Yukawa 势推出卢瑟福公式。

---

## 1. 一句话总结

**微观客体的内部结构无法直接"看见"，实验物理的全部手段就是把粒子扔过去、数它弹到哪个方向——散射截面是理论与实验的接口；在定态描述中，一切散射信息都封装在散射振幅 $f(\theta)$ 里，而计算 $f$ 的两大主力方法是分波展开（低能、中心势、可精确）和 Born 近似（弱势或高能、微扰）。**

## 2. 为什么散射是实验物理的探针

经典物理里你可以"看"一个物体的形状；微观世界里任何探测器本身也由原子构成，唯一可行的探测方式就是**碰撞**：

- **卢瑟福（1911）**：$\alpha$ 粒子轰击金箔，发现偶有大角度反弹。这与"原子是均匀正电荷球"的图像矛盾——要产生大偏转，正电荷必须集中在极小的核里。卢瑟福据此写下著名的散射公式（本篇第 7 节会用量子力学重新推出它），原子的核式模型就此确立。
- **现代对撞机**：LHC 上一切"发现"，实验上都是同一句话：某类末态事件数 $N = \mathcal L\,\sigma$，其中 $\mathcal L$ 是亮度（机器参数），$\sigma$ 是截面（物理）。理论家的全部工作归结为预言各种过程的 $\sigma$。
- **分辨率由动量转移决定**：动量转移 $q$ 对应的探测尺度是 $\sim 1/q$（自然单位下就是约化德布罗意波长）。要看清越小的结构，就要越大的 $q$——这就是对撞机能量越做越高的根本原因，也是第 8 节"形状因子"的物理。

散射理论因此不是量子力学的一个"应用题"，而是整个粒子物理的语言原型。你在本篇见到的每一个概念——截面、振幅、分波、共振——都会在 QFT 里原样重现。

## 3. 截面：实验与理论的接口

**约定**：本篇为非相对论量子力学笔记，全程保留 $\hbar$（$E=\hbar^2k^2/2m$），不做 $\hbar=1$ 的约定；第 8 节对比 QFT 公式时会改用自然单位并当场说明。

### 3.1 微分截面与总截面

实验设置：一束均匀的入射粒子，流强 $j_{\rm in}$（单位时间穿过单位横截面积的粒子数），打到靶上；探测器放在 $(\theta,\varphi)$ 方向、张立体角 ${\rm d}\Omega$。单位时间收到的粒子数正比于这两者：

$${\rm d}N = j_{\rm in}\,\frac{{\rm d}\sigma}{{\rm d}\Omega}\,{\rm d}\Omega.$$

比例系数 $\dfrac{{\rm d}\sigma}{{\rm d}\Omega}$ 就是**微分截面**。两边量纲：左边是 1/时间，右边是 (1/面积/时间)×面积，所以截面的量纲是**面积**——直观上它就是靶粒子对每个入射粒子呈现的"有效靶面积"。常用单位是 barn：$1\ {\rm b} = 10^{-28}\ {\rm m}^2$。

**总截面**是对所有方向积分：

$$\sigma_{\rm tot} = \int \frac{{\rm d}\sigma}{{\rm d}\Omega}\,{\rm d}\Omega.$$

### 3.2 截面与跃迁率的关系

从含时微扰论看，散射是一个跃迁过程：初态（动量 $\hbar\vec k$）→ 末态（动量 $\hbar\vec k'$）。费米黄金定则给出跃迁率

$$W_{i\to f} = \frac{2\pi}{\hbar}\,|\langle f|V|i\rangle|^2\,\rho(E_f),$$

其中 $\rho(E_f)$ 是末态密度。**截面 = 跃迁率 ÷ 入射流强**：$\sigma = W/j_{\rm in}$。这条"率除以流"的关系在 QFT 里完全一样，只是矩阵元从 $\langle f|V|i\rangle$ 升级为不变量振幅 $\mathcal M$（第 8 节）。

### 3.3 实验室系与质心系

理论计算在**质心系**最干净：两体散射化为约化质量 $\mu = m_1m_2/(m_1+m_2)$ 的单体在势中的运动；实验常在实验室系做，两系之间只是运动学重标定（角度、能量的变换），不含量子力学的新物理。本篇一律在质心系（等价地，靶无穷重的固定势散射）下书写，$m$ 应理解为约化质量。

## 4. 定态形式理论：散射振幅 $f(\theta)$

### 4.1 渐近形式

用定态薛定谔方程处理散射：能量 $E=\hbar^2k^2/2m>0$ 是连续谱。设势 $V(r)$ 在 $r\to\infty$ 足够快地趋于零（比 $1/r$ 快；库仑势是临界情形，见第 7 节），则远离靶的解取**散射渐近形式**

$$\psi(\vec r)\ \xrightarrow[r\to\infty]{}\ e^{ikz} + f(\theta)\,\frac{e^{ikr}}{r},$$

其中入射方向取为 $z$ 轴。第一项是不受扰动的入射平面波；第二项是**出射球面波**，其角分布由**散射振幅** $f(\theta)$ 描述（中心势下与 $\varphi$ 无关）。$f$ 有长度量纲，包含散射问题的全部物理。

<details markdown="1"><summary>补充说明：渐近形式不是方程的严格解，而是边界条件</summary>

渐近形式只在 $r\to\infty$、$V(r)$ 可忽略的区域成立。在势的作用区内 $\psi$ 是完整的薛定谔方程解，没有"平面波 + 球面波"的分解。正确的理解是：散射态由**无穷远处的边界条件**（入射条件 + 只含出射波的 Sommerfeld 辐射条件）唯一确定，解这个"带散射边界条件的定态问题"就是在求 $f(\theta)$。

另外，入射平面波 $e^{ikz}$ 在全空间存在，包括靶所在处——这看似奇怪，其实是因为真实实验的入射束很宽（横向尺度远大于靶），平面波是对它的理想化；严格的波包处理证明理想化不影响截面的结果。

</details>

### 4.2 从通量比推出 ${\rm d}\sigma/{\rm d}\Omega = |f(\theta)|^2$

概率流密度为

$$\vec j = \frac{\hbar}{m}\,\mathrm{Im}\big(\psi^*\,\vec\nabla\psi\big).$$

**入射波**：对 $\psi_{\rm in}=e^{ikz}$，$\vec\nabla\psi_{\rm in}=ik\,\hat z\,e^{ikz}$，故

$$\vec j_{\rm in} = \frac{\hbar k}{m}\,\hat z.$$

**散射波**：对 $\psi_{\rm sc}=f(\theta)e^{ikr}/r$，大 $r$ 处梯度取径向主项（$\partial_r$ 作用在 $e^{ikr}$ 上；对 $f(\theta)$ 和 $1/r$ 求导的项以 $1/r^2$ 压下去），

$$\vec j_{\rm sc} \simeq \frac{\hbar k}{m}\,\frac{|f(\theta)|^2}{r^2}\,\hat r.$$

单位时间流入立体角 ${\rm d}\Omega$（对应面积元 ${\rm d}A=r^2{\rm d}\Omega$）的粒子数为

$${\rm d}N = \vec j_{\rm sc}\cdot\hat r\;{\rm d}A = \frac{\hbar k}{m}\,|f(\theta)|^2\,{\rm d}\Omega.$$

$r^2$ 恰好抵消（球面波几何稀释），这正是 $1/r$ 形式的用意。代入截面定义 ${\rm d}N = j_{\rm in}\,{\rm d}\sigma$：

$$\boxed{\ \frac{{\rm d}\sigma}{{\rm d}\Omega} = |f(\theta)|^2\ }$$

（入射流与散射波之间的干涉项只在前向 $\theta=0$ 的无穷小锥内不可忽略——它正是光学定理的内容，见第 5.4 节。）

至此问题归结为：**求 $f(\theta)$**。下面两条路线：分波展开（精确，适合低能）与 Born 近似（微扰，适合高能/弱势）。

## 5. 分波展开（中心势的精确武器）

### 5.1 按角动量分波

设 $V=V(r)$ 为中心势，则轨道角动量 $\vec L$ 守恒，$[H, \vec L]=0$，每个角动量分波独立演化。散射问题关于 $z$ 轴旋转对称，波函数只需按 $Y_l^0 \propto P_l(\cos\theta)$ 展开：

$$\psi(r,\theta) = \sum_{l=0}^{\infty} R_l(r)\,P_l(\cos\theta).$$

入射平面波本身也有标准展开（瑞利展开）

$$e^{ikz} = \sum_{l=0}^{\infty} (2l+1)\,i^l\,j_l(kr)\,P_l(\cos\theta),$$

其中 $j_l$ 是球贝塞尔函数，$j_l(x)\to \sin(x - l\pi/2)/x$（$x\to\infty$）。

### 5.2 径向方程与相移 $\delta_l$

令 $u_l(r) = rR_l(r)$，径向薛定谔方程为

$$u_l'' + \left[k^2 - \frac{2mV(r)}{\hbar^2} - \frac{l(l+1)}{r^2}\right]u_l = 0.$$

在势区之外（$V\to 0$），通解是 $j_l$ 与 $n_l$（球诺依曼函数）的组合，其大 $r$ 渐近必然可以写成

$$R_l(r)\ \xrightarrow[r\to\infty]{}\ A_l\,\frac{\sin\big(kr - \tfrac{l\pi}{2} + \delta_l\big)}{kr}.$$

与自由解 $j_l$（上式中 $\delta_l=0$）相比，唯一的差别是**相位整体移动了 $\delta_l$**——这就是**相移（phase shift）**。物理图像：

- **吸引势**把波函数"拉进来"，势区内曲率（局域波数）更大，波积累更多相位，出射波相位**超前**：$\delta_l > 0$；
- **排斥势**把波函数"推出去"，相位**落后**：$\delta_l < 0$。

每个分波的全部散射信息就是一个实数 $\delta_l$。散射不改变该分波的径向通量（概率守恒，弹性散射下 $|\text{出射波}|=|\text{入射波}|$），唯一能改变的就是相位——这就是为什么一个实数就够了。

### 5.3 $f(\theta)$ 与总截面的分波表达式

把 5.2 的渐近式按入射/出射球面波分解：

$$\sin\big(kr - \tfrac{l\pi}{2} + \delta_l\big) = \frac{1}{2i}\Big[e^{i(kr - l\pi/2 + \delta_l)} - e^{-i(kr - l\pi/2 + \delta_l)}\Big],$$

第二项是**入射**球面波（$e^{-ikr}$），第一项是**出射**球面波。要求总波函数的入射球面波部分与平面波展开中的入射部分完全相同（靶只产生出射波），逐分波比较即可定出 $A_l = (2l+1)i^l e^{i\delta_l}/k$ 型的系数；多出来的出射部分就是 $f(\theta)e^{ikr}/r$。整理得

$$\boxed{\ f(\theta) = \frac{1}{k}\sum_{l=0}^{\infty}(2l+1)\,e^{i\delta_l}\sin\delta_l\,P_l(\cos\theta) = \frac{1}{2ik}\sum_{l=0}^{\infty}(2l+1)\big(e^{2i\delta_l}-1\big)P_l(\cos\theta)\ }$$

注意 $e^{2i\delta_l}$ 就是第 $l$ 分波的 $S$ 矩阵元 $S_l$——弹性散射中 $S$ 矩阵在每个分波里就是个纯相位，$|S_l|=1$ 正是概率守恒。

对角度积分，利用勒让德多项式正交性 $\int P_lP_{l'}\,{\rm d}\Omega = \frac{4\pi}{2l+1}\delta_{ll'}$，得**总截面**

$$\boxed{\ \sigma_{\rm tot} = \frac{4\pi}{k^2}\sum_{l=0}^{\infty}(2l+1)\sin^2\delta_l\ }$$

由于 $\sin^2\delta_l\le 1$，每个分波的贡献有上限 $\sigma_l \le \frac{4\pi(2l+1)}{k^2}$，称为**幺正性极限**——再高就违反概率守恒。

### 5.4 光学定理：前向干涉 = 概率守恒

取 $f(\theta)$ 的前向值。由 $P_l(1)=1$：

$$\mathrm{Im}\,f(0) = \frac{1}{k}\sum_l (2l+1)\sin^2\delta_l = \frac{k}{4\pi}\,\sigma_{\rm tot},$$

即**光学定理**

$$\boxed{\ \sigma_{\rm tot} = \frac{4\pi}{k}\,\mathrm{Im}\,f(0)\ }$$

物理含义：入射束经过靶后在前向上被**减弱**（散射掉的粒子不再沿原方向前进），减弱的方式是出射前向波与入射平面波**相消干涉**，在靶后形成"影子"。干涉项 $\propto \mathrm{Im}\,f(0)$，而影子消耗掉的流量必须等于所有方向散射流量的总和——总截面。所以光学定理不是巧合，它是**概率守恒（$S$ 矩阵幺正性）**的直接表达。它在 QFT 中依然成立，且推广到非弹性过程：那时 $\sigma_{\rm tot}$ 包含所有可能的末态。

### 5.5 低能极限：s 波、散射长度、共振

**s 波主导**。分波 $l$ 感受到的是有效势 $V(r) + \dfrac{\hbar^2 l(l+1)}{2mr^2}$，第二项是**离心势垒**。量级估计：能量 $E=\hbar^2k^2/2m$ 的粒子要翻过 $l$ 波的势垒到达力程 $a$ 之内，需 $k \gtrsim \sqrt{l(l+1)}/a$，即只有

$$l \lesssim ka$$

的分波参与散射（更仔细的分析给出 $\tan\delta_l \propto k^{2l+1}$，见自检第 4 题）。$k\to 0$ 时只剩 $l=0$（s 波），散射**各向同性**。

**散射长度**。$k\to 0$ 时 $f$ 趋于常数，定义散射长度

$$a_s \equiv -\lim_{k\to 0} f(\theta) = -\lim_{k\to 0}\frac{\delta_0(k)}{k},$$

于是低能总截面 $\sigma \to 4\pi a_s^2$。一个实数 $a_s$ 概括了任意复杂短程势的全部低能散射——"势是吸引还是排斥、多深，低能粒子只关心 $a_s$"。这是**有效理论**思想的萌芽：低能探针看不到短程细节，只看到少数几个低能常数。原子物理中正是靠调节 $a_s$（Feshbach 共振）控制冷原子气。

**共振**。若某个 $\delta_l(E)$ 随能量增大连续扫过 $\pi/2$，则 $\sin^2\delta_l = 1$，该分波打到幺正性极限。在 $\delta_l = \pi/2$ 的能量 $E_R$ 附近令 $\tan\delta_l \approx \dfrac{\Gamma/2}{E_R - E}$，得

$$\sigma_l \approx \frac{4\pi(2l+1)}{k^2}\,\frac{(\Gamma/2)^2}{(E-E_R)^2 + (\Gamma/2)^2},$$

这就是 **Breit–Wigner 共振线型**。物理图像是粒子被势暂时"俘获"，形成寿命 $\sim \hbar/\Gamma$ 的准束缚态。对撞机上每一个共振峰（$Z$ 玻色子、希格斯、各种强子共振）都是这个形状——本篇的 $\delta_l$ 在那里换成了各分波道的 $S$ 矩阵相位。

## 6. Born 近似（微扰武器）

### 6.1 李普曼–施温格方程

把定态薛定谔方程 $(\nabla^2 + k^2)\psi = \frac{2m}{\hbar^2}V\psi$ 看成"自由亥姆霍兹方程 + 源项"，用出射格林函数 $G(\vec r) = -\frac{e^{ikr}}{4\pi r}$ 形式求解，得到**李普曼–施温格方程**

$$\psi(\vec r) = e^{i\vec k\cdot\vec r} - \frac{2m}{4\pi\hbar^2}\int \frac{e^{ik|\vec r - \vec r'|}}{|\vec r - \vec r'|}\,V(\vec r')\,\psi(\vec r')\,{\rm d}^3r',$$

它是一个积分方程（$\psi$ 两边都出现），与原方程 + 散射边界条件严格等价。取 $r\gg r'$ 的渐近极限可直接读出 $f(\theta)$。

### 6.2 一阶 Born 近似：振幅 = 势的傅里叶变换

迭代求解：把积分号内的 $\psi$ 换成入射波 $e^{i\vec k\cdot\vec r'}$（零阶），得到一阶 Born 振幅

$$\boxed{\ f^{(1)}(\theta) = -\frac{2m}{4\pi\hbar^2}\int e^{-i\vec q\cdot\vec r}\,V(\vec r)\,{\rm d}^3r\ }$$

其中 $\vec q = \vec k' - \vec k$ 是**动量转移**（以 $\hbar$ 为单位；弹性散射 $|\vec k'|=|\vec k|=k$，故 $q = 2k\sin\frac{\theta}{2}$）。

这一条结果值得停下来看：

- **散射振幅就是势的三维傅里叶变换** $\tilde V(\vec q)$。测 ${\rm d}\sigma/{\rm d}\Omega$ 对角度的依赖，就是在逐点测量 $V$ 的空间频率成分——散射实验是一台傅里叶变换显微镜。这与第 2 节"$q$ 决定分辨率"一脉相承。
- 对中心势，角向积分可先做掉，化为一维变换

$$f^{(1)}(\theta) = -\frac{2m}{\hbar^2 q}\int_0^\infty r\,V(r)\,\sin(qr)\,{\rm d}r.$$

### 6.3 适用条件

Born 近似的实质是把 $\psi$ 换成 $e^{i\vec k\cdot\vec r}$，要求**散射波在势区内相对入射波是小量**。由李普曼–施温格方程在 $r\sim 0$ 处估计，对半径 $a$、深度 $V_0$ 的势，大致判据为

$$\frac{m|V_0|a^2}{\hbar^2} \ll 1 \quad\text{（弱势）}\qquad\text{或}\qquad \frac{|V_0|a}{\hbar v} \ll 1 \quad\text{（高能，}v=\hbar k/m\text{）},$$

即：要么势本身弱到束缚不住东西，要么粒子快到来不及被明显偏转。**Born 近似与分波展开互补**：前者适合高能/弱势（任意能量下展开到一阶），后者适合低能（任意强度下只取几个分波）。

## 7. 例题算到底：Yukawa 势与卢瑟福公式

**题目**：$V(r) = g\,\dfrac{e^{-\mu r}}{r}$（汤川势，$g$ 为耦合常数，$1/\mu$ 为力程），求一阶 Born 截面，并取 $\mu\to 0$ 回到库仑散射。

**第一步**：代入中心势 Born 公式，

$$f^{(1)}(\theta) = -\frac{2m}{\hbar^2 q}\int_0^\infty r\cdot\frac{g\,e^{-\mu r}}{r}\,\sin(qr)\,{\rm d}r = -\frac{2mg}{\hbar^2 q}\int_0^\infty e^{-\mu r}\sin(qr)\,{\rm d}r.$$

**第二步**：标准积分 $\int_0^\infty e^{-\mu r}\sin(qr)\,{\rm d}r = \dfrac{q}{q^2+\mu^2}$（对 $e^{-\mu r + iqr}$ 取实部积分再取虚部即得），故

$$f^{(1)}(\theta) = -\frac{2mg}{\hbar^2\,(q^2+\mu^2)}, \qquad \frac{{\rm d}\sigma}{{\rm d}\Omega} = \frac{4m^2g^2}{\hbar^4\,(q^2+\mu^2)^2}.$$

注意 Yukawa 振幅正比于 $1/(q^2+\mu^2)$——这正是 QFT 中"交换质量 $\mu$ 的虚粒子"的传播子形状，此处已见雏形。

**第三步（库仑极限）**：令 $\mu\to 0$，$q^2 = 4k^2\sin^2\frac{\theta}{2}$，

$$\frac{{\rm d}\sigma}{{\rm d}\Omega} = \frac{4m^2g^2}{\hbar^4\cdot 16k^4\sin^4\frac{\theta}{2}} = \frac{m^2g^2}{4\hbar^4k^4\sin^4\frac{\theta}{2}}.$$

**第四步**：取库仑势的耦合 $g = Z_1Z_2 e^2$（高斯单位；SI 单位下 $g = Z_1Z_2e^2/4\pi\varepsilon_0$），并用 $E = \hbar^2k^2/2m$ 消去 $k$（$\hbar^4k^4 = 4m^2E^2$）：

$$\frac{{\rm d}\sigma}{{\rm d}\Omega} = \left(\frac{Z_1Z_2e^2}{4E}\right)^2\frac{1}{\sin^4\frac{\theta}{2}}\quad\text{——卢瑟福公式，逐字不差。}$$

**几点讨论**：

- **历史闭环**：卢瑟福 1911 年用经典力学推出此式；量子力学 Born 近似给出完全相同的结果。这是库仑势的特殊巧合（$1/r$ 势的经典、Born、精确量子截面一致；精确量子振幅只差一个与角度相关的相位，模方相同）。换任何别的势，三者都不同。
- **$\theta\to 0$ 发散**：截面在小角度发散，这是 $1/r$ 长程性的体现——无穷远的擦边碰撞也有偏转。真实的屏蔽（原子电子云，即有限的 $\mu$）截断了发散，所以保留 $\mu$ 不只是数学技巧。
- **Born 近似的合法性**：对库仑势，高能判据是 $Z_1Z_2e^2/\hbar v \ll 1$——$\alpha$ 粒子轰金箔其实**不满足**，结果对纯属巧合（见上一条）。这提醒我们：Born 截面对了不代表理论在细节上对。

## 8. 前瞻：从 $f(\theta)$ 到 $\mathcal M$

本篇的每个概念都有相对论升级版，在路线图后面几站等着：

- **散射振幅 → 不变量振幅 $\mathcal M$**：QFT 的质心系微分截面是 $\dfrac{{\rm d}\sigma}{{\rm d}\Omega}\Big|_{\rm CM} = \dfrac{|\mathcal M|^2}{64\pi^2 s}$（自然单位 $\hbar=c=1$，$s$ 为质心系能量平方）。$f$ 与 $\mathcal M$ 只差归一化约定：相对论归一化 ($2E$ 每粒子) 取代"每体积一个粒子"。截面的定义——率除以流——原封不动。
- **李普曼–施温格 → LSZ**：本篇用"入射平面波 + 出射球面波"的边界条件定义散射态；QFT 中没有单粒子波函数，对应物是 LSZ 约化公式——$S$ 矩阵元等于编时关联函数在外腿极点处的留数（见第 4 阶段 S 矩阵与截面笔记）。
- **傅里叶变换 → 形状因子**：本篇说"振幅是势的傅里叶变换"；在电子–质子弹性散射中，点粒子的卢瑟福/Mott 公式要乘上**形状因子** $F(q^2)$ 修正，$F$ 正是质子电荷分布的傅里叶变换——测量 $F(q^2)$ 就是在给质子"拍照"。$q^2$ 再大，$F$ 偏离点粒子行为的方式暴露了质子内部的点状组分（深度非弹性散射、夸克），见 [QCD 笔记](../stage-06-standard-model/03-qcd.md)。
- **共振线型**：第 5.5 节的 Breit–Wigner 形状在 QFT 中就是传播子在极点附近的形状，$Z$ 峰是最干净的实例。

## 9. 小结

| 概念 | 核心公式 | 适用场景/含义 |
| --- | --- | --- |
| 微分截面 | ${\rm d}N = j_{\rm in}\,\frac{{\rm d}\sigma}{{\rm d}\Omega}{\rm d}\Omega$ | 实验与理论的接口，量纲为面积 |
| 散射振幅 | $\psi \to e^{ikz} + f(\theta)\frac{e^{ikr}}{r}$ | $\frac{{\rm d}\sigma}{{\rm d}\Omega} = \lvert f(\theta)\rvert^2$（通量比） |
| 分波展开 | $f = \frac{1}{k}\sum(2l+1)e^{i\delta_l}\sin\delta_l P_l$ | 中心势精确方法，低能只需少数分波 |
| 总截面 | $\sigma = \frac{4\pi}{k^2}\sum(2l+1)\sin^2\delta_l$ | 幺正性极限 $\sigma_l \le 4\pi(2l+1)/k^2$ |
| 光学定理 | $\sigma_{\rm tot} = \frac{4\pi}{k}\,\mathrm{Im}\,f(0)$ | 前向相消干涉 = 概率守恒 |
| 低能极限 | $\sigma \to 4\pi a_s^2$ | 只有 s 波；散射长度 $a_s$ 概括短程细节 |
| 共振 | $\sigma_l \propto \frac{(\Gamma/2)^2}{(E-E_R)^2+(\Gamma/2)^2}$ | $\delta_l$ 过 $\pi/2$，Breit–Wigner 线型 |
| Born 近似 | $f^{(1)} = -\frac{2m}{4\pi\hbar^2}\tilde V(\vec q)$ | 弱势/高能；振幅 = 势的傅里叶变换 |
| Yukawa → 库仑 | $f \propto \frac{1}{q^2+\mu^2} \to$ 卢瑟福公式 | 历史闭环；$1/(q^2+\mu^2)$ 是传播子雏形 |

一句话收束：实验数截面，理论算振幅；低能用分波（$\delta_l$），高能用 Born（傅里叶变换）；光学定理保证概率守恒。到了 QFT，$f$ 换成 $\mathcal M$，其余思想原样保留。

## 自检问题

**1.** 从渐近形式 $\psi \to e^{ikz} + f(\theta)e^{ikr}/r$ 出发，用概率流密度推导 $\dfrac{{\rm d}\sigma}{{\rm d}\Omega} = \lvert f(\theta)\rvert^2$，并说明为什么梯度作用在 $1/r$ 上的项可以扔掉。

<details markdown="1"><summary>点击显示答案</summary>

概率流密度 $\vec j = \frac{\hbar}{m}\mathrm{Im}(\psi^*\vec\nabla\psi)$。

入射波 $\psi_{\rm in} = e^{ikz}$：$\vec j_{\rm in} = \frac{\hbar}{m}\mathrm{Im}(e^{-ikz}\cdot ik\,e^{ikz})\hat z = \frac{\hbar k}{m}\hat z$。

散射波 $\psi_{\rm sc} = f(\theta)e^{ikr}/r$：球坐标下 $\vec\nabla = \hat r\,\partial_r + (\text{角向，}\sim 1/r)$。

$$\partial_r\psi_{\rm sc} = f(\theta)\left(ik - \frac{1}{r}\right)\frac{e^{ikr}}{r}.$$

$1/r$ 项比 $ik$ 项多压一个 $1/r$，$r\to\infty$ 时贡献的流按 $1/r^3$ 衰减，对有限立体角的通量（要乘 $r^2$）趋于零，故扔掉；角向导数同理。于是

$$\vec j_{\rm sc} \simeq \frac{\hbar}{m}\mathrm{Im}\left[\frac{f^*e^{-ikr}}{r}\cdot ik f\frac{e^{ikr}}{r}\right]\hat r = \frac{\hbar k}{m}\frac{\lvert f(\theta)\rvert^2}{r^2}\hat r.$$

单位时间进入 ${\rm d}\Omega$ 的粒子数（面积元 $r^2{\rm d}\Omega$）：

$${\rm d}N = \frac{\hbar k}{m}\lvert f(\theta)\rvert^2{\rm d}\Omega \;\Rightarrow\; \frac{{\rm d}\sigma}{{\rm d}\Omega} = \frac{{\rm d}N}{j_{\rm in}\,{\rm d}\Omega} = \lvert f(\theta)\rvert^2.$$

$1/r$ 项可扔的深层原因：截面是 $r\to\infty$ 极限下的可观测量，只有通量随 $r$ 不变的项（$1/r^2$ 的流）有贡献。

</details>

**2.** 从分波公式出发推导光学定理 $\sigma_{\rm tot} = \dfrac{4\pi}{k}\mathrm{Im}\,f(0)$，并解释它的物理含义。

<details markdown="1"><summary>点击显示答案</summary>

分波展开 $f(\theta) = \frac{1}{k}\sum_l(2l+1)e^{i\delta_l}\sin\delta_l\,P_l(\cos\theta)$。取前向 $\theta=0$，由 $P_l(1)=1$：

$$f(0) = \frac{1}{k}\sum_l(2l+1)e^{i\delta_l}\sin\delta_l.$$

$e^{i\delta_l}\sin\delta_l = \sin\delta_l\cos\delta_l + i\sin^2\delta_l$，取虚部（$\delta_l$ 是实数）：

$$\mathrm{Im}\,f(0) = \frac{1}{k}\sum_l(2l+1)\sin^2\delta_l.$$

与总截面公式 $\sigma_{\rm tot} = \frac{4\pi}{k^2}\sum_l(2l+1)\sin^2\delta_l$ 比较，得

$$\sigma_{\rm tot} = \frac{4\pi}{k}\,\mathrm{Im}\,f(0).$$

**物理含义**：总截面量度"入射束被削弱了多厉害"；削弱的机制是前向出射波与入射平面波在靶后**相消干涉**形成影子，干涉强度由 $\mathrm{Im}\,f(0)$ 决定。影子从入射束里拿走的流量 = 散射到所有方向的流量，这正是概率守恒。数学上它是 $S$ 矩阵幺正性 $S^\dagger S = 1$（即 $|e^{2i\delta_l}|=1$，$\delta_l$ 为实数）的直接推论——只要理论是幺正的，光学定理就自动成立，QFT 中亦然（那时右边包括所有非弹性道）。

</details>

**3.** 对 Yukawa 势 $V(r) = g e^{-\mu r}/r$ 完整计算一阶 Born 振幅，取 $\mu\to 0$ 的库仑极限，推出卢瑟福公式，并说明小角度发散的物理来源。

<details markdown="1"><summary>点击显示答案</summary>

中心势 Born 公式 $f^{(1)} = -\frac{2m}{\hbar^2 q}\int_0^\infty rV(r)\sin(qr)\,{\rm d}r$，代入 $V$：

$$f^{(1)} = -\frac{2mg}{\hbar^2 q}\int_0^\infty e^{-\mu r}\sin(qr)\,{\rm d}r.$$

算积分：$\int_0^\infty e^{-\mu r}e^{iqr}{\rm d}r = \frac{1}{\mu - iq}$，取虚部 $\mathrm{Im}\frac{1}{\mu-iq} = \mathrm{Im}\frac{\mu + iq}{\mu^2+q^2} = \frac{q}{\mu^2+q^2}$。故

$$f^{(1)}(\theta) = -\frac{2mg}{\hbar^2(q^2+\mu^2)}, \qquad \frac{{\rm d}\sigma}{{\rm d}\Omega} = \frac{4m^2g^2}{\hbar^4(q^2+\mu^2)^2}.$$

库仑极限 $\mu\to 0$，弹性散射 $q = 2k\sin\frac{\theta}{2}$：

$$\frac{{\rm d}\sigma}{{\rm d}\Omega} = \frac{4m^2g^2}{\hbar^4\cdot 16k^4\sin^4\frac{\theta}{2}} = \frac{m^2g^2}{4\hbar^4k^4\sin^4\frac{\theta}{2}}.$$

代入 $g = Z_1Z_2e^2$（高斯单位）与 $\hbar^2k^2 = 2mE$：

$$\frac{{\rm d}\sigma}{{\rm d}\Omega} = \left(\frac{Z_1Z_2e^2}{4E}\right)^2\frac{1}{\sin^4\frac{\theta}{2}},$$

即卢瑟福公式。

**小角发散**：$\theta\to 0$ 对应 $q\to 0$，即长波长（大距离）成分。$1/r$ 势延伸到无穷远，任意大瞄准距离的粒子也受到小偏转，无穷多小角事件累积使前向截面发散。物理上它由屏蔽截断（有限 $\mu$，如原子电子云）：$\theta \lesssim \mu/k$ 时截面饱和在 $\sim (2mg/\hbar^2\mu^2)^2$。发散是长程力的签名，不是计算错误。

</details>

**4.** 用离心势垒论证 $k\to 0$ 时只有 $l=0$ 分波有贡献，并给出 $\tan\delta_l \propto k^{2l+1}$ 的推导要点。

<details markdown="1"><summary>点击显示答案</summary>

**离心势垒论证**。径向方程中分波 $l$ 感受有效势

$$V_{\rm eff}(r) = V(r) + \frac{\hbar^2 l(l+1)}{2mr^2}.$$

设势力程为 $a$。能量 $E = \hbar^2k^2/2m$ 的粒子要进入力程之内，必须在 $r\sim a$ 处越过离心势垒：

$$\frac{\hbar^2k^2}{2m} \gtrsim \frac{\hbar^2 l(l+1)}{2ma^2} \;\Longleftrightarrow\; ka \gtrsim \sqrt{l(l+1)} \approx l.$$

（经典对应：瞄准距离 $b$ 的粒子有 $L = \hbar k b$，进入力程需 $b\lesssim a$，即 $l \sim L/\hbar \lesssim ka$。）所以只有 $l \lesssim ka$ 的分波参与；$k\to 0$ 时只剩 $l=0$。

**$\tan\delta_l \propto k^{2l+1}$ 推导要点**。短程势（$r>a$ 处 $V=0$）的外解为

$$R_l \propto \cos\delta_l\,j_l(kr) - \sin\delta_l\,n_l(kr).$$

在 $r=a$ 处与内解做 log-derivative 匹配 $\gamma_l = aR_l'(a)/R_l(a)$（$\gamma_l$ 由内区决定，低能下趋于与 $k$ 无关的常数），解出

$$\tan\delta_l = \frac{ka\,j_l'(ka) - \gamma_l j_l(ka)}{ka\,n_l'(ka) - \gamma_l n_l(ka)}.$$

利用小宗量行为 $j_l(x) \sim \frac{x^l}{(2l+1)!!}$，$n_l(x) \sim -\frac{(2l-1)!!}{x^{l+1}}$：分子 $\sim (ka)^l$，分母 $\sim (ka)^{-(l+1)}$，故

$$\tan\delta_l \sim (ka)^{2l+1} \xrightarrow[k\to 0]{} 0 \quad (l\ge 1).$$

$l=0$ 时 $\tan\delta_0 \sim -ka_s$（散射长度），是唯一存活的项。这定量解释了 s 波主导，也给出各分波被压低的确切幂次。

</details>

**5.** 硬球散射（$V=\infty$，$r<a$；$V=0$，$r>a$）：求 s 波相移与低能总截面，并解释为什么 $\sigma \to 4\pi a^2$ 是几何截面 $\pi a^2$ 的 4 倍。

<details markdown="1"><summary>点击显示答案</summary>

**s 波相移**。$l=0$ 的径向方程在 $r>a$ 处是 $u_0'' + k^2u_0 = 0$，通解 $u_0 = C\sin(kr + \delta_0)$。硬球边界条件：波函数不能进入 $r<a$，故 $u_0(a) = 0$，即 $ka + \delta_0 = 0$（取主值）：

$$\delta_0 = -ka.$$

负号符合预期：排斥势把波推出去，相位落后。

**低能总截面**。高 $l$ 分波由第 4 题的 $\tan\delta_l\sim(ka)^{2l+1}$ 压掉，只剩 s 波：

$$\sigma = \frac{4\pi}{k^2}\sin^2\delta_0 = \frac{4\pi}{k^2}\sin^2(ka) \xrightarrow{k\to 0} \frac{4\pi}{k^2}(ka)^2 = 4\pi a^2.$$

（对照散射长度定义：$a_s = -\lim\delta_0/k = a$——硬球的散射长度就是半径，$\sigma\to 4\pi a_s^2$ 一致。）

**为什么是几何截面的 4 倍**。经典图像中粒子要么撞上（面积 $\pi a^2$）要么掠过，截面应为 $\pi a^2$。但 $k\to 0$ 意味着德布罗意波长 $\lambda = 2\pi/k \gg a$——波长远大于球，"粒子沿直线走"的经典图像彻底失效，散射是纯波动现象：球对整个入射波前产生衍射，s 波各向同性地向所有方向重新辐射。因子 4 的来源可以形式上看：$\sigma = \frac{4\pi}{k^2}\sin^2(ka)$ 中 $\frac{4\pi}{k^2}$ 是波长量级的平方（$\lambda^2/\pi$），是波"能感受到"的横向尺度，远大于几何尺寸 $a$ 时被 $\sin^2(ka)\approx(ka)^2$ 拉回到 $4\pi a^2$。同类现象在光学中叫"消光悖论"（extinction paradox）：短波长极限下硬球的总截面是 $2\pi a^2$（几何 + 衍射各一份），依然不是 $\pi a^2$——波动性从不允许截面简单地等于几何面积。

</details>

## 参考

- Griffiths《量子力学概论》第 11 章（散射）——与本篇主线对应最直接，含 Born 近似与分波展开的完整初等处理。
- Sakurai《现代量子力学》第 6 章（散射理论）——更形式化，李普曼–施温格方程与光学定理讲得透。
- Shankar《Principles of Quantum Mechanics》第 19 章（Scattering Theory）——分波法与低能散射讲得最细，硬球、共振均有完整演算。
