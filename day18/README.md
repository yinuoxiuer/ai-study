# Day 18 AI Study - PyTorch 基础与深度学习入门

本项目包含 AI 学习第 18 天的代码，主要关注 PyTorch 基础知识和深度学习的初步实践。

## 文件说明

### 1. `deep_learning1.ipynb`
- **内容**: 深度学习入门笔记本，使用 FashionMNIST 数据集进行图像分类。
- **功能**:
  - **环境检查**: 检查 PyTorch 及相关库的版本和环境（CUDA/CPU）。
  - **数据处理**: 
    - 加载 FashionMNIST 数据集。
    - 定义数据转换（Transforms），包括 `ToTensor` 和归一化。
    - 提供了可视化单张图片和批量图片的功能。
  - **模型构建**: 
    - 定义了一个包含展平层 (`Flatten`) 和三个全连接层 (`Linear`) 的神经网络 (`NeuralNetwork`)。
    - 使用 ReLU 激活函数。
  - **模型训练**:
    - 定义了交叉熵损失函数 (`CrossEntropyLoss`) 和 SGD 优化器。
    - 实现了带有进度条 (`tqdm`) 的训练循环。
    - 包含模型评估函数，计算损失和准确率。
  - **结果可视化**:
    - 绘制训练过程中的损失 (Loss) 和准确率 (Accuracy) 曲线，对比训练集和验证集的表现。

### 2. `pytorch_test.ipynb`
- **内容**: PyTorch 功能测试与基础神经网络示例。
- **功能**:
  - 定义简单的逻辑回归模型 (`LogisticRegression`)。
  - 定义简单的神经网络模型 (`SimpleNeuralNet`)，用于解决非线性问题（如 XOR 问题）。
  - 包含模型定义、前向传播逻辑以及简单的训练数据准备。

### 3. `main.py`
- **内容**: 默认生成的 Python 示例脚本。

## 环境依赖

运行本项目代码需要安装以下 Python 库：

- torch
- torchvision
- numpy
- pandas
- scikit-learn (sklearn)
- matplotlib
- tqdm
- Pillow (PIL)

## 如何运行

建议使用 Jupyter Notebook 或 VS Code 打开 `.ipynb` 文件进行交互式运行和学习。

1.  首先运行 `deep_learning1.ipynb` 中的环境检查代码，确保 CUDA 或 CPU 可用。
2.  按顺序执行单元格，观察数据加载、模型构建和训练过程。
3.  训练完成后，查看生成的 Loss 和 Accuracy 曲线图。
