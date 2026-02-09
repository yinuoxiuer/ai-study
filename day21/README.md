# Day 21 - 卷积神经网络 (CNN) 进阶与实战

本项目包含了一系列基于 PyTorch 的卷积神经网络（CNN）实战案例，涵盖了从基础 CNN 构建、激活函数对比、深度可分离卷积、到使用 ResNet 进行迁移学习的完整流程。

## 📂 文件说明

### 1. 基础图像分类 (FashionMNIST)
- **`cnn_learn_classification.ipynb`**
  - **任务**: FashionMNIST 服饰图像分类。
  - **模型**: 自定义基础 CNN（2层卷积 + 池化 + 全连接）。
  - **特点**: 实现了完整的训练循环、验证、模型保存（Checkpoint）和早停（Early Stopping）机制。
  - **激活函数**: ReLU。

- **`cnn_learn_classification_selu.ipynb`**
  - **任务**: 同上。
  - **变化**: 将激活函数从 **ReLU** 替换为 **SELU** (Scaled Exponential Linear Unit)，探索不同激活函数对模型收敛的影响。

- **`separable_cnn.ipynb`**
  - **任务**: 同上。
  - **模型**: 实现了 **深度可分离卷积 (Depthwise Separable Convolution)**。
  - **特点**: 相比普通卷积，显著减少了模型参数量，模拟 MobileNet 的核心思想。

### 2. 进阶图像分类 (CIFAR-10)
- **`cifar10_model.ipynb`**
  - **任务**: CIFAR-10 彩色图片分类（Kaggle 竞赛风格）。
  - **数据处理**: 
    - 自定义 `Dataset` 类解析 CSV 标签文件。
    - 实现了训练集、验证集和测试集的划分。
    - 使用了更强的数据增强（随机旋转、水平翻转）。
  - **模型**: 更深层的 CNN 结构，使用了 **BatchNorm2d** 进行归一化，激活函数调整为 **SELU**。
  - **输出**: 生成用于提交的 `submission.csv`。

### 3. 迁移学习与实战 (10 Monkey Species)
- **`10monkeys_test.ipynb`**
  - **任务**: 10 种猴子的细粒度图像分类。
  - **数据加载**: 
    - 使用 `ImageFolder` 加载层级目录数据。
    - **关键修复**: 解决了 `random_split` 导致的数据泄露问题，通过自定义 `TransformedSubset` 类，确保训练集（带增强）和验证集（无增强）使用独立的数据预处理流程。
  - **模型**: 
    - 使用 **ResNet50** (预训练权重 `IMAGENET1K_V2`) 进行迁移学习。
    - 添加了 **Dropout** 层防止过拟合。
  - **优化**: 使用 Adam 优化器，配合早停机制。

## 🧠 核心知识点

1.  **CNN 架构设计**:
    - 卷积层 (`Conv2d`)、池化层 (`MaxPool2d`)、全连接层 (`Linear`) 的组合。
    - **深度可分离卷积**: `Depthwise` + `Pointwise` 卷积的实现。
    - **残差网络 (ResNet)**: 利用预训练模型加速收敛并提高准确率。

2.  **数据处理与增强**:
    - `torchvision.transforms`: Resize, RandomHorizontalFlip, RandomRotation, Normalize, ToTensor。
    - `Dataset` 与 `DataLoader` 的自定义与使用。
    - 防止**数据泄露 (Data Leakage)** 的正确数据集切分方法。

3.  **训练技巧**:
    - **激活函数**: ReLU vs SELU。
    - **正则化**: BatchNorm2d, Dropout。
    - **回调机制**: 保存最佳模型 (Checkpoint), 早停 (Early Stopping)。
    - **可视化**: (注：部分代码中 TensorBoard 相关功能已根据需求移除)。

## 🔧 环境依赖

- Python 3.x
- PyTorch
- Torchvision
- Pandas, Numpy, Matplotlib, Scikit-learn
- Tqdm (进度条)

## 🚀 快速开始

1. 确保已安装所有依赖库。
2. 确保数据集（`data/`, `archive/`, `cifar-10/`）已放置在项目根目录下。
3. 按顺序运行 Jupyter Notebook 单元格即可开始训练。
