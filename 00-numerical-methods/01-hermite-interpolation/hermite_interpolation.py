"""Visualize Hermite interpolation ideas from the numerical methods notes.

The first subplot compares a target function with a cubic Hermite polynomial
constructed from interpolation constraints. The second subplot shows the local
piecewise basis function alpha_k(x), which is useful for understanding why each
node only affects nearby intervals in piecewise Hermite interpolation.
"""
import numpy as np
import matplotlib.pyplot as plt

# 设置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 创建画布，包含左右两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# ==========================================
# 1. 绘制图1中的三次Hermite插值示例 H(x)
# ==========================================
# 设定 x 的范围，稍微超出节点区间以观察趋势
x_val = np.linspace(0, 3, 200)

# 原函数 f(x) = x^(3/2)
f_x = x_val ** (1.5)

# 根据图1计算出的 H(x) 表达式
H_x = -(14 / 225) * x_val ** 3 + (263 / 450) * x_val ** 2 + (233 / 450) * x_val - 1 / 25

# 绘制线条
ax1.plot(x_val, f_x, label='$f(x)=x^{3/2}$', linestyle='--', color='gray')
ax1.plot(x_val, H_x, label='Hermite $H(x)$', color='blue')

# 标记插值节点
nodes_x = [0.25, 1, 2.25]
nodes_y = [0.125, 1, 3.375]
ax1.scatter(nodes_x, nodes_y, color='red', zorder=5, label='插值节点')

ax1.set_title('图1示例：三次Hermite多项式 $H(x)$')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, linestyle=':', alpha=0.6)


# ==========================================
# 2. 绘制图4中的分段基函数 α_k(x)
# ==========================================
def alpha_k(x, x_prev, x_k, x_next):
    """Compute the local Hermite basis alpha_k(x) on two adjacent intervals.

    Values outside [x_prev, x_next] stay at 0, so the plotted curve makes the
    compact support of the basis function visible.
    """
    y = np.zeros_like(x)
    # 左侧区间 [x_{k-1}, x_k]
    mask1 = (x >= x_prev) & (x <= x_k)
    x1 = x[mask1]
    y[mask1] = ((x1 - x_prev) / (x_k - x_prev)) ** 2 * (1 + 2 * (x1 - x_k) / (x_prev - x_k))

    # 右侧区间 [x_k, x_{k+1}]
    mask2 = (x > x_k) & (x <= x_next)
    x2 = x[mask2]
    y[mask2] = ((x2 - x_next) / (x_k - x_next)) ** 2 * (1 + 2 * (x2 - x_k) / (x_next - x_k))
    return y


# 假设节点等距分布：x_{k-1}=0, x_k=1, x_{k+1}=2
x_pw = np.linspace(-0.5, 2.5, 300)
y_alpha = alpha_k(x_pw, 0, 1, 2)

ax2.plot(x_pw, y_alpha, color='purple', linewidth=2, label=r'$\alpha_k(x)$')
ax2.axvline(1, color='gray', linestyle=':', label='当前节点 $x_k$')
ax2.scatter([0, 1, 2], [0, 1, 0], color='red', zorder=5)

ax2.set_title(r'图4：分段插值基函数 $\alpha_k(x)$ 形态')
ax2.set_xlabel('x')
ax2.set_ylabel(r'$\alpha_k(x)$')
ax2.legend()
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()

