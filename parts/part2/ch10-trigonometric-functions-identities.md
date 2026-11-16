# 第10章 三角函数：单位圆、图像与恒等变换

> **定位：★高考核心｜◆强基常考｜▲竞赛基础**　建议 14 课时  
> 三角函数不是一张公式表，而是“旋转在坐标轴上的投影”。从单位圆出发，定义、符号、周期、图像与公式会连成一个系统。

## 学习地图

本章将建立以下主线：

1. 角的推广、弧度制与扇形量；
2. 用单位圆定义任意角三角函数；
3. 诱导公式与同角关系；
4. 正弦、余弦、正切函数的图像和性质；
5. $y=A\sin(\omega x+\varphi)$ 的参数意义；
6. 和差角、倍角、半角与辅助角公式；
7. 三角恒等变换、求值、最值和方程；
8. 三角代换、复数观点与竞赛迁移。

## 课前诊断

1. $180^\circ$ 等于多少弧度？
2. $-30^\circ$ 与哪个 $0^\circ$ 到 $360^\circ$ 的角终边相同？
3. 若点 $P(x,y)$ 在单位圆上，$\cos\alpha,\sin\alpha$ 分别是什么？
4. 为什么 $\tan(\pi/2)$ 没有定义？
5. $\sin x$ 的最小正周期是多少？
6. $2\sin x\cos x$ 可化为什么？

**答案：** 1. $\pi$；2. $330^\circ$；3. $x,y$；4. $\cos(\pi/2)=0$，不能作商；5. $2\pi$；6. $\sin2x$。

---

## 10.1 任意角与弧度制

### 10.1.1 为什么角可以超过一周、也可以为负

现实中的转动不止一圈，方向也有正反。规定逆时针为正、顺时针为负。若两个角终边相同，则它们相差整数个整周：
$$\beta=\alpha+2k\pi\quad(k\in\mathbb Z).$$

这里“终边相同”不表示角相等；它只表示旋转结束的位置相同。

### 10.1.2 弧度制的定义

半径为 $r$ 的圆中，圆心角所对弧长为 $l$，则
$$\boxed{\alpha=\frac lr}$$
称为角的弧度数。整圆弧长为 $2\pi r$，故
$$360^\circ=2\pi,
\qquad180^\circ=\pi.$$
于是
$$1^\circ=\frac\pi{180},
\qquad1\text{ rad}=\frac{180^\circ}{\pi}.$$

弧度本质是长度之比，所以通常不写单位。微积分公式如 $(\sin x)'=\cos x$ 只有在 $x$ 用弧度时才保持最简形式。

### 例1【高考题型改编】角度与弧度互化

将 $150^\circ$ 化为弧度，将 $-7\pi/6$ 化为角度。

$$150^\circ=150\cdot\frac\pi{180}=\frac{5\pi}6,$$
$$-\frac{7\pi}6=-\frac76\cdot180^\circ=-210^\circ.$$

### 10.1.3 弧长与扇形面积

当 $\alpha$ 用弧度且 $\alpha\ge0$ 时，
$$l=r\alpha,$$
$$S=\frac12rl=\frac12r^2\alpha.$$
有向角为负时，实际弧长和面积仍取非负量，通常使用 $|\alpha|$。

### 例2【高考题型改编】扇形最优化

周长为 $L$ 的扇形，半径为 $r$，弧长为 $l=L-2r$，面积
$$S=\frac12r(L-2r)
=-\left(r-\frac L4\right)^2+\frac{L^2}{16}.$$
因此 $r=L/4,l=L/2$ 时面积最大，为 $L^2/16$。

### 即时训练

1. 化简与 $17\pi/6$ 终边相同且在 $[0,2\pi)$ 内的角。
2. 半径3、圆心角 $2\pi/3$ 的弧长与扇形面积。
3. $-765^\circ$ 的终边位于第几象限？

**答案：** 1. $5\pi/6$；2. $2\pi,3\pi$；3. 加 $1080^\circ$ 得 $315^\circ$，第四象限。

---

## 10.2 单位圆定义任意角三角函数

角 $\alpha$ 的终边与单位圆交于 $P(x,y)$，定义
$$\boxed{\cos\alpha=x,
\qquad\sin\alpha=y}.$$
若 $x\ne0$，定义
$$\tan\alpha=\frac yx=\frac{\sin\alpha}{\cos\alpha}.$$

这一定义立刻给出：

- $-1\le\sin\alpha,\cos\alpha\le1$；
- $\sin^2\alpha+\cos^2\alpha=1$；
- 正弦看纵坐标，余弦看横坐标；
- 符号由点所在象限决定，而不是由“锐角公式”死记。

### 10.2.1 象限符号

| 象限 | $\sin$ | $\cos$ | $\tan$ |
|---|---:|---:|---:|
| I | $+$ | $+$ | $+$ |
| II | $+$ | $-$ | $-$ |
| III | $-$ | $-$ | $+$ |
| IV | $-$ | $+$ | $-$ |

坐标轴上的角须单独判断，不能说属于某一象限。

### 例3【高考题型改编】由终边上一点求三角函数

角 $\alpha$ 终边经过点 $Q(-3,4)$。令
$$r=\sqrt{(-3)^2+4^2}=5.$$
则单位方向向量为 $(-3/5,4/5)$，所以
$$\sin\alpha=\frac45,
\quad\cos\alpha=-\frac35,
\quad\tan\alpha=-\frac43.$$

### 例4【易错辨析】由平方关系开方

若 $\sin\alpha=3/5$，则
$$\cos\alpha=\pm\frac45,$$
不能直接写正号。若再知 $\alpha$ 在第二象限，才有
$$\cos\alpha=-\frac45.$$

### 例5【强基题型改编】斜率与正切

终边不是纵轴时，其斜率为
$$k=\frac yx=\tan\alpha.$$
但“直线的倾斜角”通常限制在 $[0,\pi)$，而一般角可相差 $k\pi$；应区分直线方向与有向旋转次数。

### 即时训练

1. 终边过 $(5,-12)$，求三角函数值。
2. 若 $\cos\alpha=-4/5$ 且 $\alpha$ 在第三象限，求 $\sin\alpha,\tan\alpha$。
3. 哪些角没有正切值？

**答案：** 1. $\sin=-12/13,\cos=5/13,\tan=-12/5$；2. $-3/5,3/4$；3. $\pi/2+k\pi$。

---

## 10.3 诱导公式：把任意角归约到基本角

诱导公式不宜逐条背诵。统一策略是：

1. 在单位圆上判断变换后的点；
2. 先确定函数名是否改变；
3. 再依据象限确定符号。

### 10.3.1 周期与对称

$$\sin(\alpha+2k\pi)=\sin\alpha,$$
$$\cos(\alpha+2k\pi)=\cos\alpha,$$
$$\tan(\alpha+k\pi)=\tan\alpha.$$

关于 $x$ 轴反射：
$$\sin(-\alpha)=-\sin\alpha,
\qquad\cos(-\alpha)=\cos\alpha.$$
因此正弦是奇函数，余弦是偶函数。

关于 $y$ 轴反射：
$$\sin(\pi-\alpha)=\sin\alpha,$$
$$\cos(\pi-\alpha)=-\cos\alpha.$$

旋转半周：
$$\sin(\pi+\alpha)=-\sin\alpha,$$
$$\cos(\pi+\alpha)=-\cos\alpha.$$

余角互换：
$$\sin\left(\frac\pi2-\alpha\right)=\cos\alpha,$$
$$\cos\left(\frac\pi2-\alpha\right)=\sin\alpha.$$

### 例6【高考题型改编】求特殊角值

$$\sin\frac{13\pi}6
=\sin\frac\pi6=\frac12.$$
$$\cos\frac{5\pi}6
=\cos\left(\pi-\frac\pi6\right)
=-\frac{\sqrt3}{2}.$$
$$\tan\left(-\frac{3\pi}4\right)=1.$$

### 例7【多方法比较】化简对称表达式

化简
$$\sin(\pi-x)+\cos(-x)-\sin(x+2\pi).$$
分别使用诱导公式：
$$\sin x+\cos x-\sin x=\cos x.$$

图像法也能解释：第一个点是关于 $y$ 轴反射，第二个是关于 $x$ 轴反射后的横坐标，第三个是整周平移。

### 即时训练

1. 求 $\sin(-7\pi/6)$。
2. 化简 $\cos(2\pi-x)$。
3. 化简 $\sin(\pi/2+x)$。

**答案：** 1. $1/2$；2. $\cos x$；3. $\cos x$。

---

## 10.4 同角三角函数基本关系

### 10.4.1 平方关系

单位圆方程 $x^2+y^2=1$ 直接给出
$$\boxed{\sin^2\alpha+\cos^2\alpha=1}.$$

### 10.4.2 商数关系

当 $\cos\alpha\ne0$ 时，
$$\boxed{\tan\alpha=\frac{\sin\alpha}{\cos\alpha}}.$$
由平方关系除以 $\cos^2\alpha$，还得
$$1+\tan^2\alpha=\frac1{\cos^2\alpha}.$$
使用时必须保留定义域条件。

### 例8【高考题型改编】齐次式求值

已知 $\tan\alpha=2$，求
$$\frac{3\sin\alpha+\cos\alpha}{\sin\alpha-2\cos\alpha}.$$
分子分母同除以 $\cos\alpha$：
$$\frac{3\tan\alpha+1}{\tan\alpha-2}.$$
分母为0，因此原式无意义。这个例子提醒：代入前先检查条件；已知恰使分母为零。

若题目改为分母 $2\sin\alpha+\cos\alpha$，则值为
$$\frac{3\tan\alpha+1}{2\tan\alpha+1}=\frac75.$$

### 例9【强基题型改编】不求角求表达式

若 $\sin\alpha+\cos\alpha=1/3$，则平方得
$$1+2\sin\alpha\cos\alpha=\frac19,$$
所以
$$\sin\alpha\cos\alpha=-\frac49.$$
进一步
$$(\sin\alpha-\cos\alpha)^2
=1-2\sin\alpha\cos\alpha=\frac{17}{9}.$$
故差为 $\pm\sqrt{17}/3$，符号仍需额外象限信息。

### 例10【易错辨析】平方导致的信息丢失

从 $u^2=v^2$ 只能得到 $u=\pm v$。三角求值中，平方、开方、由 $\sin^2$ 求 $\sin$ 都必须补符号判断。

### 即时训练

1. 已知 $\tan\alpha=-3$，求 $(\sin\alpha+\cos\alpha)/(\sin\alpha-\cos\alpha)$。
2. 若 $\sin\alpha\cos\alpha=1/4$，求 $(\sin\alpha+\cos\alpha)^2$。
3. $1+\tan^2x=1/\cos^2x$ 在哪些 $x$ 上成立？

**答案：** 1. $1/2$；2. $3/2$；3. $x\ne\pi/2+k\pi$。

---

## 10.5 三角函数的图像与性质

### 10.5.1 正弦和余弦

| 函数 | 定义域 | 值域 | 最小正周期 | 奇偶性 |
|---|---|---|---|---|
| $\sin x$ | $\mathbb R$ | $[-1,1]$ | $2\pi$ | 奇 |
| $\cos x$ | $\mathbb R$ | $[-1,1]$ | $2\pi$ | 偶 |

正弦在
$$\left[-\frac\pi2+2k\pi,\frac\pi2+2k\pi\right]$$
递增，在相邻的另一半周期递减。余弦可由
$$\cos x=\sin\left(x+\frac\pi2\right)$$
看作正弦图像左移 $\pi/2$。

五点作图法对 $y=\sin x$ 一个周期取：
$$(0,0),
\left(\frac\pi2,1\right),
(\pi,0),
\left(\frac{3\pi}2,-1\right),
(2\pi,0).$$

### 10.5.2 正切函数

$$y=\tan x$$
定义域为
$$x\ne\frac\pi2+k\pi,$$
值域为 $\mathbb R$，最小正周期为 $\pi$，是奇函数；在每个区间
$$\left(-\frac\pi2+k\pi,\frac\pi2+k\pi\right)$$
严格递增。

### 例11【高考题型改编】利用单调性比较大小

比较
$$\sin1,
\\sin1.2$$
（弧度制）。二者都在 $(0,\pi/2)$，正弦递增，故
$$\sin1<\sin1.2.$$
若跨越单调区间，不能只比较角的大小。

### 例12【高考题型改编】求值域

求
$$y=2\sin x-1$$
的值域。由 $-1\le\sin x\le1$，
$$-3\le y\le1.$$

### 例13【强基题型改编】周期判断

函数
$$f(x)=|\sin x|$$
的最小正周期不是 $2\pi$，而是 $\pi$，因为
$$|\sin(x+\pi)|=|-\sin x|=|\sin x|.$$

### 即时训练

1. 写出 $\cos x$ 在 $[0,2\pi]$ 的单调区间。
2. 求 $3-4\cos x$ 的值域。
3. $\tan2x$ 的最小正周期是多少？

**答案：** 1. $[0,\pi]$ 递减，$[\pi,2\pi]$ 递增；2. $[-1,7]$；3. $\pi/2$。

---

## 10.6 $y=A\sin(\omega x+\varphi)+b$ 的图像

设 $A\ne0,\omega\ne0$：

- 振幅为 $|A|$；
- 周期为 $T=2\pi/|\omega|$；
- 中线为 $y=b$；
- 值域为 $[b-|A|,b+|A|]$；
- 相位 $\omega x+\varphi$ 控制水平位置。

写成
$$A\sin\left[\omega\left(x+\frac\varphi\omega\right)\right]+b$$
时，水平平移量为 $-\varphi/\omega$，不能只看 $\varphi$。

### 例14【高考题型改编】参数读图

对
$$y=3\sin\left(2x-\frac\pi3\right)+1,$$
振幅3，周期 $\pi$，中线 $y=1$，值域 $[-2,4]$，相对 $y=3\sin2x$ 向右平移 $\pi/6$。

### 例15【高考题型改编】由最值点恢复解析式

某正弦型函数中线为2，最大值5，最小值 $-1$，故 $|A|=3,b=2$。相邻最大值横坐标相差 $\pi$，故周期 $\pi$，可取 $|\omega|=2$。再代入一个最大值点确定相位。

这里解析式可能有多种等价写法，例如正弦与余弦形式不同但图像相同。

### 例16【强基题型改编】变换顺序

从 $y=\sin x$ 得 $y=\sin(2x+\pi/3)$：

- 若先横向压缩为原来 $1/2$，再左移 $\pi/6$；
- 不能说“左移 $\pi/3$”，因为括号外还有系数2。

### 即时训练

1. 求 $y=-2\cos(3x)+4$ 的振幅、周期和值域。
2. $y=\sin(x-\pi/4)$ 相对 $y=\sin x$ 怎样平移？
3. $y=\sin(4x)$ 在长度多大的区间上完成一个周期？

**答案：** 1. $2,2\pi/3,[2,6]$；2. 右移 $\pi/4$；3. $\pi/2$。

---

## 10.7 和差角公式：旋转合成的代数表达

### 10.7.1 公式

$$\boxed{\cos(\alpha-\beta)=
\cos\alpha\cos\beta+\sin\alpha\sin\beta}.$$
由替换和诱导公式可得
$$\cos(\alpha+\beta)=
\cos\alpha\cos\beta-\sin\alpha\sin\beta,$$
$$\sin(\alpha+\beta)=
\sin\alpha\cos\beta+\cos\alpha\sin\beta,$$
$$\sin(\alpha-\beta)=
\sin\alpha\cos\beta-\cos\alpha\sin\beta.$$

当相关余弦非零时，
$$\tan(\alpha+\beta)=
\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}.$$

### 10.7.2 为什么余弦差公式成立

单位向量
$$u=(\cos\alpha,\sin\alpha),
\quad v=(\cos\beta,\sin\beta)$$
夹角为 $\alpha-\beta$。点积一方面为
$$u\cdot v=\cos\alpha\cos\beta+\sin\alpha\sin\beta,$$
另一方面为
$$|u||v|\cos(\alpha-\beta)=\cos(\alpha-\beta).$$
两者相等即得公式。

### 例17【高考题型改编】求 $15^\circ$ 三角值

$$\sin15^\circ
=\sin(45^\circ-30^\circ)$$
$$=\frac{\sqrt2}{2}\frac{\sqrt3}{2}
-\frac{\sqrt2}{2}\frac12
=\frac{\sqrt6-\sqrt2}{4}.$$

### 例18【强基题型改编】已知两个角的函数值

若 $\alpha,\beta$ 均为锐角，
$$\sin\alpha=\frac35,
\quad\cos\beta=\frac5{13},$$
则
$$\cos\alpha=\frac45,
\quad\sin\beta=\frac{12}{13}.$$
所以
$$\sin(\alpha+\beta)
=\frac35\frac5{13}+\frac45\frac{12}{13}
=\frac{63}{65}.$$
锐角条件用于确定开方后的正号。

### 例19【高联风格】点积看恒等式

$$\cos\alpha\cos\beta+\sin\alpha\sin\beta$$
不是两个无关乘积的偶然组合，而是两个单位方向向量的点积。由柯西不等式立刻有其绝对值不超过1，也解释了它等于某角的余弦。

### 即时训练

1. 求 $\cos75^\circ$。
2. 化简 $\cos(x+\pi/3)$。
3. 已知 $\tan\alpha=1/2,\tan\beta=1/3$，求 $\tan(\alpha+\beta)$。

**答案：** 1. $(\sqrt6-\sqrt2)/4$；2. $(1/2)\cos x-(\sqrt3/2)\sin x$；3. $1$。

---

## 10.8 倍角、半角与降幂

令 $\beta=\alpha$，得到
$$\sin2\alpha=2\sin\alpha\cos\alpha,$$
$$\cos2\alpha=\cos^2\alpha-\sin^2\alpha$$
$$=2\cos^2\alpha-1
=1-2\sin^2\alpha.$$

于是
$$\sin^2\alpha=\frac{1-\cos2\alpha}{2},$$
$$\cos^2\alpha=\frac{1+\cos2\alpha}{2}.$$

半角公式来自把 $2\alpha$ 换成 $\theta$：
$$\sin^2\frac\theta2=\frac{1-\cos\theta}{2},
\qquad
\cos^2\frac\theta2=\frac{1+\cos\theta}{2}.$$
若求 $\sin(\theta/2)$ 本身，还要根据半角所在象限选择正负号。

### 例20【高考题型改编】二次齐次式

化简
$$2\sin^2x+\cos2x.$$
由 $\cos2x=1-2\sin^2x$，原式恒等于1。

### 例21【强基题型改编】由正切求倍角

若 $\tan x=1/3$，则
$$\tan2x=\frac{2\tan x}{1-\tan^2x}
=\frac{2/3}{1-1/9}=\frac34.$$
前提是所涉及正切有定义，且分母不为0。

### 例22【高联风格】三倍角公式

由
$$\cos3x=\cos(2x+x)$$
结合倍角公式可推得
$$\boxed{\cos3x=4\cos^3x-3\cos x}.$$
同理
$$\sin3x=3\sin x-4\sin^3x.$$
这把三角方程与三次多项式联系起来。

### 即时训练

1. 用 $\cos2x$ 表示 $\cos^2x$。
2. 若 $\cos x=3/5$ 且 $x$ 为第四象限角，求 $\sin2x$。
3. 化简 $1-2\sin^2x$。

**答案：** 1. $(1+\cos2x)/2$；2. $-24/25$；3. $\cos2x$。

---

## 10.9 辅助角公式与三角最值

对实数 $a,b$，不全为0，令
$$R=\sqrt{a^2+b^2}.$$
可选 $\varphi$ 使
$$\cos\varphi=\frac aR,
\qquad\sin\varphi=\frac bR,$$
于是
$$\boxed{a\sin x+b\cos x
=R\sin(x+\varphi)}.$$
因此值域为
$$[-R,R].$$

### 例23【高考题型改编】求最值

$$\sin x+\sqrt3\cos x
=2\sin\left(x+\frac\pi3\right).$$
最大值2，最小值 $-2$。

### 例24【高考压轴题型改编】带常数的值域

求
$$y=3\sin x-4\cos x+2$$
的值域。振幅
$$R=\sqrt{3^2+(-4)^2}=5,$$
故
$$-3\le y\le7.$$

### 例25【强基题型改编】角受限时不能直接取满振幅

若 $x\in[0,\pi/6]$，求
$$\sin x+\cos x$$
的范围。

写成
$$\sqrt2\sin\left(x+\frac\pi4\right).$$
此时相位范围为 $[\pi/4,5\pi/12]$，位于正弦递增区间，故
$$1\le\sin x+\cos x
\le\frac{\sqrt6+\sqrt2}{4}.$$
不能无视 $x$ 的限制直接写 $[-\sqrt2,\sqrt2]$。

### 例26【CMO/IMO思想改编】向量投影

$a\sin x+b\cos x$ 可看作向量 $(b,a)$ 与单位向量 $(\cos x,\sin x)$ 的点积。由柯西不等式
$$|a\sin x+b\cos x|
\le\sqrt{a^2+b^2}.$$
等号在两向量同向或反向时取得。辅助角公式和柯西不等式是同一几何事实的两种语言。

### 即时训练

1. 求 $2\sin x-2\cos x$ 的最大值。
2. 求 $1+5\sin x+12\cos x$ 的值域。
3. 辅助角中的 $\varphi$ 是否唯一？

**答案：** 1. $2\sqrt2$；2. $[-12,14]$；3. 模 $2\pi$ 意义下确定，亦可用不同但等价的正弦/余弦形式。

---

## 10.10 三角恒等变换的策略

证明恒等式必须在两边都有定义的公共定义域内进行。常用路线：

1. 从较复杂的一边向较简单的一边化；
2. 统一为正弦、余弦；
3. 统一角度：单角、倍角或和差角；
4. 分式先通分或分子分母同除；
5. 看到平方用 $\sin^2x+\cos^2x=1$；
6. 看到线性组合用辅助角；
7. 不要随意两边平方，以免引入增根。

### 例27【高考题型改编】恒等式证明

证明在有定义处
$$\frac{1-\cos2x}{\sin2x}=\tan x.$$
左边
$$=\frac{2\sin^2x}{2\sin x\cos x}
=\frac{\sin x}{\cos x}=\tan x.$$
约去 $\sin x$ 时要求 $\sin x\ne0$；原分式本身要求 $\sin2x\ne0$，这已包含该条件。

### 例28【强基题型改编】分式齐次化

若 $\sin x+\cos x\ne0$，化简
$$\frac{\sin x-\cos x}{\sin x+\cos x}.$$
当 $\cos x\ne0$ 时可同除以 $\cos x$ 得
$$\frac{\tan x-1}{\tan x+1}.$$
但若 $\cos x=0$，原式可能有定义而变形后的正切无定义。因此这个表达式只在附加条件 $\cos x\ne0$ 下等价。更稳妥的方法是保留正弦余弦形式。

### 例29【高联风格】积化和差的推导

将和差公式相加：
$$\cos(u-v)-\cos(u+v)=2\sin u\sin v.$$
令
$$u=\frac{\alpha+\beta}{2},
\quad v=\frac{\alpha-\beta}{2},$$
得到
$$\cos\beta-\cos\alpha
=2\sin\frac{\alpha+\beta}{2}
\sin\frac{\alpha-\beta}{2}.$$
和差化积、积化和差不必孤立背诵，可从和差角公式推导。

### 即时训练

1. 证明 $\sin(x+y)+\sin(x-y)=2\sin x\cos y$。
2. 化简 $(1-\cos2x)/(1+\cos2x)$。
3. 恒等变换中为什么要关注定义域？

**答案：** 1. 展开相加；2. 在有定义处为 $\tan^2x$；3. 除法、约分、正切化会删去或加入某些点。

---

## 10.11 简单三角方程与解集

### 10.11.1 基本方程

$$\sin x=\sin\alpha$$
的解为
$$x=\alpha+2k\pi
\quad\text{或}\quad
x=\pi-\alpha+2k\pi.$$

$$\cos x=\cos\alpha$$
的解可写成
$$x=2k\pi\pm\alpha.$$

$$\tan x=\tan\alpha$$
的解为
$$x=\alpha+k\pi.$$
其中 $k\in\mathbb Z$。

### 例30【高考题型改编】区间内解方程

解
$$2\sin x=1,
\qquad x\in[0,2\pi].$$
即 $\sin x=1/2$，故
$$x=\frac\pi6,
\quad\frac{5\pi}6.$$

### 例31【高考题型改编】因式分解

解
$$2\sin x\cos x=\sin x.$$
移项：
$$\sin x(2\cos x-1)=0.$$
所以
$$x=k\pi$$
或
$$\cos x=\frac12,
\quad x=2k\pi\pm\frac\pi3.$$

不能一开始同除以 $\sin x$，否则会丢失 $x=k\pi$。

### 例32【强基题型改编】换元方程

解
$$2\cos^2x-3\cos x+1=0.$$
令 $t=\cos x$，且 $t\in[-1,1]$：
$$(2t-1)(t-1)=0.$$
所以
$$\cos x=\frac12
\quad\text{或}\quad
\cos x=1.$$
再分别写出通解。

### 即时训练

1. 解 $\cos x=0$。
2. 在 $[0,2\pi)$ 解 $\tan x=1$。
3. 解 $\sin2x=0$。

**答案：** 1. $x=\pi/2+k\pi$；2. $\pi/4,5\pi/4$；3. $x=k\pi/2$。

---

## 10.12 综合精讲与高级连接

### 例33【高考压轴题型改编】性质、最值与方程合一

设
$$f(x)=\sin2x+\sqrt3\cos2x.$$

（1）化为单一正弦；（2）求最小正周期；（3）求最大值点；（4）解 $f(x)=1$。

$$f(x)=2\sin\left(2x+\frac\pi3\right).$$
周期
$$T=\frac{2\pi}{2}=\pi.$$
最大值2在
$$2x+\frac\pi3=\frac\pi2+2k\pi$$
时取得，即
$$x=\frac\pi{12}+k\pi.$$
方程 $f(x)=1$ 化为
$$\sin\left(2x+\frac\pi3\right)=\frac12,$$
再按正弦方程写两族解。

### 例34【高校强基题型改编】参数最值

求实数 $a$ 的范围，使方程
$$\sin x+\cos x=a$$
有实解。左边值域为 $[-\sqrt2,\sqrt2]$，因此
$$-\sqrt2\le a\le\sqrt2.$$
边界处仍有解，且对应向量同向或反向。

### 例35【全国高中数学联赛风格】正弦乘积恒等式

证明
$$\sin20^\circ\sin40^\circ\sin80^\circ=\frac{\sqrt3}{8}.$$

利用
$$\sin2x=2\sin x\cos x$$
以及
$$\sin3x=4\sin x\sin(60^\circ+x)\sin(60^\circ-x)$$
的等价形式。取 $x=20^\circ$：
$$\sin60^\circ
=4\sin20^\circ\sin80^\circ\sin40^\circ.$$
所以乘积为
$$\frac{\sin60^\circ}{4}=\frac{\sqrt3}{8}.$$

### 例36【CMO/IMO思想改编】复数旋转观点

欧拉公式写作
$$e^{ix}=\cos x+i\sin x.$$
于是
$$e^{i(\alpha+\beta)}=e^{i\alpha}e^{i\beta}.$$
展开右边并比较实部、虚部，就得到余弦和角、正弦和角公式。

高中主线不依赖欧拉公式，但这个观点解释了：三角和角公式本质上是平面旋转相乘的坐标表达。

### 例37【探究题】万能代换

令
$$t=\tan\frac x2.$$
在相关表达式有定义时，
$$\sin x=\frac{2t}{1+t^2},
\qquad
\cos x=\frac{1-t^2}{1+t^2}.$$
推导来自半角关系。它能把许多三角方程化成有理方程，但会遗漏 $x=\pi+2k\pi$ 所对应的“$t$ 无穷大”情形，必须单独检查。

---

## 10.13 方法树与易错清单

### 方法树

1. **任意角求值：** 化同终边角 → 判断象限 → 找参考角。
2. **已知一值求其余：** 平方关系 → 开方 → 象限定号。
3. **图像问题：** 中线、振幅、周期、相位、五点依次确定。
4. **线性组合：** $a\sin x+b\cos x$ → 辅助角或向量投影。
5. **二次式：** 降幂、倍角或令 $t=\sin x/\cos x$。
6. **恒等式：** 统一函数名和角度，从复杂边向简单边。
7. **方程：** 化基本函数 → 写全部周期解 → 按区间筛选。
8. **参数存在性：** 转化为三角表达式的值域问题。

### 高频错误

- 混用角度制与弧度制；
- 把终边相同误认为角相等；
- 开平方后漏掉负号；
- 忘记正切的定义域；
- 把相位 $\varphi$ 直接当平移量；
- 只看频率系数，不取绝对值；
- 辅助角求最值时忽略 $x$ 的限制；
- 解方程同除可能为零的因子，导致漏解；
- 两边平方后不验根；
- 恒等变换约分时扩大定义域；
- 通解漏写 $k\in\mathbb Z$；
- 特殊角数值和象限符号机械混淆。

---

## 10.14 分层习题

### A组　基础巩固（★）

1. 将 $225^\circ$ 化为弧度。
2. 求与 $-11\pi/6$ 同终边且在 $[0,2\pi)$ 内的角。
3. 终边过点 $(-8,-15)$，求三角函数值。
4. 化简 $\sin(2\pi-x)$ 与 $\cos(\pi+x)$。
5. 已知 $\sin x=5/13$ 且 $x$ 在第二象限，求 $\cos x$。
6. 求 $y=4\sin x+3$ 的值域。
7. 求 $y=\cos3x$ 的最小正周期。
8. 求 $\sin75^\circ$。
9. 化简 $1-2\sin^2x$。
10. 在 $[0,2\pi)$ 解 $\sin x=-1/2$。

### B组　综合提高（◆）

11. 已知 $\tan x=2$，求 $(2\sin x+3\cos x)/(\sin x+\cos x)$。
12. 求 $2\sin x+\sqrt5\cos x-1$ 的值域。
13. 求 $y=3\sin(2x-\pi/4)+2$ 的振幅、周期、中线和平移。
14. 证明 $\sin(x+y)+\sin(x-y)=2\sin x\cos y$。
15. 若 $\sin\alpha=3/5,\cos\beta=12/13$ 且均为锐角，求 $\cos(\alpha+\beta)$。
16. 解 $2\cos^2x-\cos x-1=0$。
17. 求 $x\in[0,\pi/3]$ 时 $\sin x+\cos x$ 的范围。
18. 证明 $(1-\cos2x)/\sin2x=\tan x$，并写出公共定义域。

### C组　超越训练（▲/☆）

19. **【强基题型改编】** 求参数 $a$ 的范围，使 $\sin x+\sqrt3\cos x=a$ 有实解。
20. **【高联风格】** 推导 $\cos3x=4\cos^3x-3\cos x$，并据此求 $\cos20^\circ$ 满足的一个三次方程。
21. **【竞赛思想改编】** 证明 $\sin10^\circ\sin50^\circ\sin70^\circ=1/8$。
22. **【向量法】** 用柯西不等式证明 $|a\sin x+b\cos x|\le\sqrt{a^2+b^2}$ 并讨论等号。
23. **【方程与定义域】** 用 $t=\tan(x/2)$ 解一个自选三角方程，并说明需补查哪些角。
24. **【复数思想】** 形式化展开 $(\cos\alpha+i\sin\alpha)(\cos\beta+i\sin\beta)$，比较实部与虚部。

## 提示与答案

1. $5\pi/4$。  
2. $\pi/6$。  
3. $r=17$，故 $\sin=-15/17,\cos=-8/17,\tan=15/8$。  
4. $-\sin x,-\cos x$。  
5. $-12/13$。  
6. $[-1,7]$。  
7. $2\pi/3$。  
8. $(\sqrt6+\sqrt2)/4$。  
9. $\cos2x$。  
10. $7\pi/6,11\pi/6$。  
11. 同除以余弦，得 $(2\tan x+3)/(\tan x+1)=7/3$。  
12. 振幅3，值域 $[-4,2]$。  
13. 振幅3，周期 $\pi$，中线 $y=2$，相对 $\sin2x$ 右移 $\pi/8$。  
14. 展开两个和差角公式相加。  
15. $\cos\alpha=4/5,\sin\beta=5/13$，答案 $33/65$。  
16. 令 $t=\cos x$，得 $t=1$ 或 $t=-1/2$，再写通解。  
17. 相位 $x+\pi/4\in[\pi/4,7\pi/12]$；最大值 $\sqrt2$，最小值1。  
18. 公共定义域为 $\sin2x\ne0$，即 $x\ne k\pi/2$。  
19. $[-2,2]$。  
20. 令 $x=20^\circ$，因 $\cos60^\circ=1/2$，得 $8t^3-6t-1=0$。  
21. 使用 $\sin3x=4\sin x\sin(60^\circ+x)\sin(60^\circ-x)$，取 $x=10^\circ$。  
22. 把表达式看成 $(b,a)\cdot(\cos x,\sin x)$；两向量共线时等号成立。  
23. 需补查 $x=\pi+2k\pi$，并检查代换分母与原方程定义域。  
24. 实部给余弦和角公式，虚部给正弦和角公式。

---

## 章末复盘

### 一条贯穿全章的链

$$\text{旋转}
\longrightarrow
\text{单位圆坐标}
\longrightarrow
\text{正弦、余弦}
\longrightarrow
\text{周期与图像}
\longrightarrow
\text{旋转合成}
\longrightarrow
\text{和差角公式}.$$

### 必查的五个条件

1. 角度还是弧度；
2. 象限与符号；
3. 分母是否为零；
4. 自变量是否受区间限制；
5. 方程是否写全周期解并完成验根。

### 自我检查

- 我能从单位圆推导符号和诱导公式，而不是只背口诀吗？
- 我能解释 $A,\omega,\varphi,b$ 各自改变图像的什么吗？
- 我能从点积推导余弦差角公式吗？
- 我会在辅助角求最值时检查相位范围吗？
- 我会在约分、平方和正切代换后检查定义域与漏解吗？

下一章将把三角函数用于三角形，系统学习正弦定理、余弦定理、面积公式以及解三角形的存在性与多解问题。
