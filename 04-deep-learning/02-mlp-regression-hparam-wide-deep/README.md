# Day 19 - 深度学习基础与实践

本项目包含了一系列基于 PyTorch 的深度学习实践代码，涵盖了回归任务、分类任务、模型调优以及 Wide & Deep 模型等内容。

## 文件说明

### 1. 回归任务 (房价预测)
*   **`deep_learn_regression.ipynb`**:
    *   **内容**: 使用加州房价数据集 (California Housing) 进行回归预测。
    *   **核心点**:
        *   数据预处理：StandardScaler 标准化。
        *   模型结构：简单的 MLP (多层感知机)。
        *   训练流程：完整的 Training Loop，包含 Train/Valid 划分。
        *   回调函数：实现了 Early Stopping (早停) 机制。
        *   可视化：绘制 Loss 学习曲线。

*   **`hp_search_learn.ipynb`**:
    *   **内容**: 基于回归任务的超参数搜索 (Hyperparameter Search)。
    *   **核心点**:
        *   演示了如何通过循环遍历不同的学习率 (Learning Rate)。
        *   对比不同超参数下的模型收敛情况。

*   **`wide_deep_learn.ipynb`**:
    *   **内容**: 实现 Wide & Deep 模型架构。
    *   **核心点**:
        *   **Wide 部分**: 线性模型，记忆能力强。
        *   **Deep 部分**: 神经网络，泛化能力强。
        *   **拼接**: 使用 `torch.cat` 将两部分特征融合。

### 2. 分类任务 (FashionMNIST)
*   **`classification_module_dnn.ipynb`**:
    *   **内容**: 使用 FashionMNIST 数据集进行图像分类。
    *   **核心点**:
        *   模型结构：多层全连接网络 (DNN)。
        *   激活函数：ReLU。
        *   初始化：Xavier 初始化。
        *   功能：包含 TensorBoard 支持、模型保存 (Checkpoint)。

*   **`classification_module_dnn_selu.ipynb`**:
    *   **内容**: 改进版分类模型，引入自归一化网络 (SNN)。
    *   **核心点**:
        *   激活函数：**SELU** (Scaled Exponential Linear Unit)。
        *   优势：自带归一化属性，防止梯度消失/爆炸，无需 BatchNorm。

*   **`classification_module_dnn_selu_dropout.ipynb`**:
    *   **内容**: 在 SELU 基础上添加 Dropout。
    *   **核心点**:
        *   Dropout 类型：**AlphaDropout**。
        *   原因：普通的 Dropout 会破坏 SELU 的分布特性，必须使用 AlphaDropout 来保持均值和方差不变。

## 关键技术点总结

1.  **数据处理**:
    *   `Dataset` 和 `DataLoader` 的封装。
    *   `StandardScaler` 数据标准化 (Fit on Train, Transform on All)。

2.  **模型构建**:
    *   `nn.Module` 继承与 `forward` 函数定义。
    *   `nn.Sequential` 容器的使用。
    *   权重初始化 (Xavier Uniform)。

3.  **训练技巧**:
    *   **Early Stopping**: 监控验证集指标，防止过拟合。
    *   **Momentum**: 动量优化器，加速收敛。
    *   **Learning Rate Search**: 简单的网格搜索。

4.  **高级架构**:
    *   **Wide & Deep**: 结合记忆与泛化。
    *   **SNN (SELU + AlphaDropout)**: 深度网络的自归一化方案。

## 运行环境
*   Python 3.x
*   PyTorch
*   Scikit-learn
*   Pandas
*   Matplotlib
*   Torchvision
