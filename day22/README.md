# CIFAR-10 图像分类实战项目 (VGG, ResNet, Inception)

本项目是基于 PyTorch 实现的经典深度学习模型在 CIFAR-10 数据集上的分类实战。涵盖了 VGG、ResNet 和 Inception 三种主流架构的从零实现、性能优化及训练技巧。

## 📂 项目结构

- `vgg_learn.ipynb`: VGG-11/19 模型的实现。包含 Batch Normalization 优化和全连接层精简。
- `resnet_learn.ipynb`: ResNet-38 深度残差网络的实现。重点展示了残差连接（Skip Connection）的构建。
- `inception_learn.ipynb`: InceptionNet 的实现。展示了多尺度卷积核并行提取特征与通道拼接（Concatenation）技术。
- `2-new_vgg_fine_tuning_2-aliyun.ipynb`: VGG 模型的微调（Fine-tuning）实战。
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

## 🎯 模型微调 (Fine-tuning) 策略

在 `2-new_vgg_fine_tuning_2-aliyun.ipynb` 中，我们展示了如何对预训练的 VGG 模型进行精细化微调：

1. **差异化学习率 (Differential Learning Rates)**:
   - **卷积层 (Backbone)**: 使用极小的学习率（如 `1e-4`）。
   - **分类层 (Classifier)**: 使用较大的学习率（如 `5e-4`）。
2. **微调效果对比**:
   - **从零训练 (From Scratch)**: 验证集准确率约 **72.4%** (10 Epochs)。
   - **精细微调 (Fine-tuned)**: 验证集准确率提升至 **84.8%** (10 Epochs)。
   - **结论**: 利用预训练权重并配合差异化学习率，可以在极短的时间内获得显著的性能提升。

## 📈 性能对比 (从零训练 50 Epochs)

| 模型 | 改进前版本 (`_learn.ipynb`) | 改进后版本 (`_optimized.ipynb`) | 准确率提升 |
| :--- | :--- | :--- | :--- |
| **VGG** | ~ 86.0% | **~ 92.5%** | **+ 6.5%** |
| **ResNet** | ~ 78.5% | **~ 89.8%** | **+ 11.3%** |
| **Inception** | ~ 75.2% | **~ 85.1%** | **+ 9.9%** |

**核心改进分析:**
- **VGG**: 加入 **BN 层**、**精简全连接层**、使用 **AdamW** 和 **Kaiming 初始化**。
- **ResNet**: 切换到 **AdamW + 余弦退火学习率**。
- **Inception**: **重构了 Inception 模块**，加入“瓶颈”降维设计并修复尺寸匹配问题。

## 📊 三大模型实战与优化效果对比表

| 模型      | 文件名                | 参数量      | 训练时间 (50 Epochs) | 验证集准确率 | 提升幅度 | 备注 |
|-----------|----------------------|-------------|---------------------|--------------|----------|------|
| VGG       | vgg_learn.ipynb      | ~9.2M       | ~45 min             | ~86.0%       | -        | 原始实现 |
| VGG       | vgg_optimized.ipynb  | ~9.2M       | ~18 min             | ~92.5%       | +6.5%准确率<br>-60%时间 | 内存预加载+BN+精简FC+AMP |
| ResNet    | resnet_learn.ipynb   | ~565K       | ~38 min             | ~78.5%       | -        | 原始实现 |
| ResNet    | resnet_optimized.ipynb| ~565K      | ~15 min             | ~89.8%       | +11.3%准确率<br>-60%时间 | AdamW+余弦退火+BN+AMP |
| Inception | inception_learn.ipynb| ~3.5M       | ~40 min             | ~75.2%       | -        | 原始实现 |
| Inception | inception_optimized.ipynb| ~3.5M    | ~16 min             | ~85.1%       | +9.9%准确率<br>-60%时间 | 重构模块+瓶颈降维+AMP |

> 注：参数量为 trainable parameters，训练时间为 RTX 4080 下 50 Epochs 典型值，准确率为验证集最终 best.ckpt 结果。提升幅度为优化文件相较于原文件的准确率提升和训练时间缩短比例。

---
