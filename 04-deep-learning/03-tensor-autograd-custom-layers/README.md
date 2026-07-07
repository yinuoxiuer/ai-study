# Day 20 - PyTorch 基础与自动微分学习笔记

本项目记录了 AI 学习第 20 天的内容，主要聚焦于 PyTorch 的核心数据结构 Tensor 的操作以及自动微分（Autograd）机制的原理与应用。

## 📂 文件说明

### 1. `tensor_learn.ipynb` (Tensor 基础操作)
该 Notebook 涵盖了 PyTorch Tensor 的常用操作，重点探讨了维度变换和内存视图。

*   **Tensor 创建**: 从 List 或 NumPy 数组创建 Tensor。
*   **切片语法**: 深入理解 `t[0:1]` (保留维度) 与 `t[0]` (降维) 的区别。
*   **形状变换 (`view`)**:
    *   学习如何使用 `view()` 重塑张量形状。
    *   理解 `view` 的核心规则：**元素总数必须守恒**。
    *   使用 `-1` 进行自动维度推导。
*   **维度交换 (`permute`)**:
    *   使用 `permute()` 重新排列维度的顺序（例如从 `(Batch, Channel, Height)` 变为 `(Channel, Batch, Height)`）。
*   **原地操作与类型**:
    *   分析了 `sub_` 等原地操作在不同数据类型（Int vs Float）下的行为及报错原因。

### 2. `derivative_approximation.ipynb` (导数与自动微分)
该 Notebook 对比了手动数值微分与 PyTorch 自动微分的实现方式。

*   **数值微分 (Numerical Differentiation)**:
    *   利用极限定义的中心差分公式 $\frac{f(x+\epsilon) - f(x-\epsilon)}{2\epsilon}$ 近似计算导数。
*   **偏导数 (Partial Derivatives)**:
    *   使用 Python `lambda` 闭包技术，通过“固定一个变量，对另一个变量求导”的方法计算多元函数的偏导数。
*   **自动微分 (Autograd)**:
    *   使用 `requires_grad=True` 开启梯度追踪。
    *   构建计算图（Computational Graph）。
    *   使用 `torch.autograd.grad` 计算精确梯度。
    *   理解 `retain_graph=True` 的作用（在多次反向传播时保留计算图）。

## 🚀 关键概念总结

1.  **View vs Reshape**: `view` 返回原数据的视图（共享内存），要求数据在内存中连续；`reshape` 在不连续时会复制数据。
2.  **Permute**: 改变维度的逻辑顺序，常用于图像处理中 `CHW` 与 `HWC` 格式的转换。
3.  **Autograd**: PyTorch 的核心引擎，通过链式法则自动计算梯度，是训练神经网络的基础。

## 🛠️ 运行环境
*   Python 3.x
*   PyTorch
*   NumPy
*   Jupyter Notebook
