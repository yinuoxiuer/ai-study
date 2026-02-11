# CIFAR-10 图像分类实战项目 (VGG, ResNet, Inception)

本项目是基于 PyTorch 实现的经典深度学习模型在 CIFAR-10 数据集上的分类实战。涵盖了 VGG、ResNet 和 Inception 三种主流架构的从零实现、性能优化及训练技巧。

## 📂 项目结构

- `vgg_learn.ipynb`: VGG-11/19 模型的实现。包含 Batch Normalization 优化和全连接层精简。
- `resnet_learn.ipynb`: ResNet-38 深度残差网络的实现。重点展示了残差连接（Skip Connection）的构建。
- `inception_learn.ipynb`: InceptionNet 的实现。展示了多尺度卷积核并行提取特征与通道拼接（Concatenation）技术。
- `cifar-10/`: 数据集目录，包含训练集图片、测试集图片及标签文件。
- `checkpoints/`: 训练过程中保存的最优模型权重（.ckpt 文件）。

## 🚀 核心优化技术

为了在笔记本环境（如 i9 + RTX 4080）下实现极致的训练速度和准确率，本项目实施了以下优化：

1. **内存预加载 (Memory Preloading)**: 针对 CIFAR-10 小数据集，将所有图片一次性加载至 RAM，彻底消除磁盘 I/O 瓶颈，训练速度提升数倍。
2. **批归一化 (Batch Normalization)**: 在所有卷积层后添加 BN 层，加速模型收敛并提高训练稳定性。
3. **分类器精简**: 针对 32x32 小图任务，将原版 VGG 臃肿的 4096 维全连接层缩减至 512 维，有效防止过拟合并减少计算量。
4. **数据增强 (Data Augmentation)**: 采用 `RandomCrop` (带 padding) 和 `RandomHorizontalFlip`，显著提升模型的泛化能力。
5. **混合精度训练 (AMP)**: 利用 PyTorch 自动混合精度技术，在保持准确率的同时大幅降低显存占用并加速计算。
6. **Windows 环境适配**: 针对 Windows 下多进程死锁问题，优化了 `DataLoader` 配置（`num_workers=0`）并限制了单线程运行。

## 📈 性能对比

| 模型 | 改进前版本 (`_learn.ipynb`) | 改进后版本 (`_optimized.ipynb`) | 准确率提升 |
| :--- | :--- | :--- | :--- |
| **VGG** | ~ 86.0% | **~ 92.5%** | **+ 6.5%** |
| **ResNet** | ~ 78.5% | **~ 89.8%** | **+ 11.3%** |
| **Inception** | ~ 75.2% | **~ 85.1%** | **+ 9.9%** |

**核心改进分析:**
- **VGG**: 加入 **BN 层**、**精简全连接层**、使用 **AdamW** 和 **Kaiming 初始化**，解决了训练不稳和过拟合问题。
- **ResNet**: 切换到 **AdamW + 余弦退火学习率**，优化策略更平滑、自适应，收敛效果显著提升。
- **Inception**: **重构了 Inception 模块**，加入“瓶颈”降维设计并修复尺寸匹配问题，使复杂模型得以有效训练。

## 🛠 环境要求

- Python 3.10+
- PyTorch 2.0+ (支持 CUDA)
- Pandas, NumPy, Matplotlib, PIL, tqdm, Scikit-learn

## 📝 使用说明

1. 确保数据存放在 `cifar-10/` 目录下。
2. 根据需求打开对应的 `.ipynb` 文件。
3. 依次运行单元格即可开始训练。模型会自动保存验证集表现最好的权重到 `checkpoints/` 目录。
