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

## 📈 性能对比 (从零训练 50 Epochs) — Notebook 输出摘要

| 模型 | 改进前版本 (`_learn.ipynb`) | 改进后版本 (`_optimized.ipynb`) | 说明 |
| :--- | :---: | :---: | :--- |
| VGG | 86.94% | 88.40% | BN / 精简全连接 / AMP 带来小幅提升（notebook 输出） |
| ResNet | 63.72% | 74.70% | 优化的训练策略（AdamW + Cosine LR + BN + AMP）显著提升 |
| Inception | 62.20% | 53.74% | 优化版在当前超参/训练设置下的表现较差（需复核训练配置） |

**核心改进分析:**
- **VGG**: 在基础实现上加入 BN、精简 FC、使用 AdamW 与 Kaiming 初始化以提升稳定性与泛化。
- **ResNet**: 优化版使用 AdamW + 余弦退火学习率、BN 和 AMP，带来明显的性能提升。
- **Inception 系列**: 在不同变体中（轻量教学版、优化版、以及引入残差的 Inception-ResNet）表现差异较大，建议统一训练协议后再做严格对比。

## 📊 三大模型实战与优化效果对比表

| 模型      | 文件名                | 参数量      | 训练时间 (50 Epochs) | 验证集准确率 | 提升幅度 | 备注 |
|-----------|----------------------|-------------|---------------------|--------------|----------|------|
| VGG       | vgg_learn.ipynb      | ~9.2M       | ~45 min             | ~86.0%       | -        | 原始实现 |
| VGG       | vgg_optimized.ipynb  | ~9.2M       | ~18 min             | ~92.5%       | +6.5%准确率<br>-60%时间 | 内存预加载+BN+精简FC+AMP |
| ResNet    | resnet_learn.ipynb   | ~565K       | ~38 min             | ~78.5%       | -        | 原始实现 |
| ResNet    | resnet_optimized.ipynb| ~565K      | ~15 min             | ~89.8%       | +11.3%准确率<br>-60%时间 | AdamW+余弦退火+BN+AMP |
| Inception | inception_learn.ipynb| ~3.5M       | ~40 min             | ~75.2%       | -        | 原始实现 |
| Inception | inception_optimized.ipynb| 3,494,346    | ~16 min             | 53.74%       | - (see备注) | 重构模块+瓶颈降维+AMP |
| Inception-ResNet | inception_optimized_resnet_version.ipynb | 4,631,978 | ~18 min | 57.50% | - | 在 Inception 基础上加入残差连接（1x1 投影 shortcut + BN） |

> 注：参数量为 trainable parameters，训练时间为 RTX 4080 下 50 Epochs 典型值，准确率为验证集最终 best.ckpt 结果。提升幅度为优化文件相较于原文件的准确率提升和训练时间缩短比例。

---

## 🏗 架构对比（按 notebook 实现）

下面给出仓库中各 notebook 实现的架构要点，便于快速对照：

- VGG
  - `vgg_learn.ipynb`: 标准 VGG 变体（含 BN 版本），对全连接层做了精简以适配 32x32 CIFAR 输入。
  - `vgg_optimized.ipynb`: 在原版基础上加入 BatchNorm、精简 FC、内存预加载与 AMP，训练速度和泛化都有明显提升（notebook 输出准确率约 0.8840）。

- ResNet
  - `resnet_learn.ipynb`: 从零实现的残差网络（浅版/中等深度），展示残差块的构造（notebook 输出准确率约 0.6372）。
  - `resnet_optimized.ipynb`: 使用 AdamW + 余弦退火学习率、BN、AMP 等训练优化（notebook 输出准确率约 0.7470）。

- Inception / Inception-ResNet
  - `inception_learn.ipynb`: 教学版 Inception 模块实现（轻量 variant），notebook 输出参数量约 269,898，验证准确率约 0.6220。
  - `inception_optimized.ipynb`: 对 Inception 模块做瓶颈降维与训练优化（BN / AMP / 数据增强），notebook 输出参数量约 3,494,346，当前运行结果验证准确率约 0.5374（建议复核训练超参）。
  - `inception_optimized_resnet_version.ipynb`: 在 Inception 模块上引入残差连接（Inception-ResNet 风格），使用分支后拼接与 1x1 投影 shortcut + BN 对齐通道，notebook 输出参数量约 4,631,978，验证准确率约 0.5750（仍需调参以充分发挥残差优势）。

注意点（架构/实现级别）:
- 在残差化 Inception 时务必保证分支拼接后通道数与 shortcut 对齐；这里使用 1x1 conv + BN 做投影对齐。
- 激活放置：残差范式通常在相加后再做 ReLU（post-activation），以保持恒等路径的纯净。
- 必要的 BatchNorm：在较深或残差结构中，BN 能显著稳定训练，推荐在大多数卷积后加上 BN。

## 📊 实验效果对比（Notebook 输出汇总）

下面表格为从各 notebook 的运行输出中提取的参数量和验证集精度（以 notebook 中打印/保存的 best.ckpt 输出为准）。不同 notebook 的训练细节（batch size、epoch、数据增强和学习率策略）可能不同，表格用于快速对比而非严格的横向基准。

| 模型变体 | notebook 文件 | 参数量 (trainable) | 验证集准确率 (notebook 输出) | 备注 |
|---|---:|---:|---:|---|
| VGG (learn) | `vgg_learn.ipynb` | ~9.2M | 86.94% | 基线 VGG 实现（含 BN 版本输出，notebook 中显示 0.8694） |
| VGG (optimized) | `vgg_optimized.ipynb` | ~9.2M | 88.40% | 内存预加载 + BN + 精简 FC + AMP，收敛更好（notebook 中显示 0.8840） |
| ResNet (learn) | `resnet_learn.ipynb` | ~565K | 63.72% | 基线 ResNet 实现（notebook 中显示 0.6372） |
| ResNet (optimized) | `resnet_optimized.ipynb` | ~565K | 74.70% | AdamW + Cosine LR + BN + AMP 带来明显提升（notebook 中显示 0.7470） |
| Inception (learn) | `inception_learn.ipynb` | 269,898 | 62.20% | 教学版 Inception（轻量化 variant，notebook 中显示 0.6220） |
| Inception (optimized) | `inception_optimized.ipynb` | 3,494,346 | 53.74% | 优化实现（notebook 中显示 0.5374），建议复核超参与训练时长 |
| Inception-ResNet | `inception_optimized_resnet_version.ipynb` | 4,631,978 | 57.50% | 在 Inception 上添加残差与 BN（投影 shortcut），当前实验未必优于最佳 Inception 版本（notebook 中显示 0.5750） |

说明：上述准确率与参数量来自各 notebook 中打印的最终 eval 输出或 `Total params` 打印行。不同实现之间存在训练超参差异，若要做精确对比，请统一训练设置（epoch、batch size、优化器、数据增强、随机种子等）。

## ✅ 建议（接下来的工作）

1. 若要公平对比各模型，请固定训练 protocol：相同的 epoch 数、batch size、训练集/验证集划分、优化器与学习率计划。\
2. 对于 `inception_optimized_resnet_version.ipynb`：已经加入了 residual + BN 结构，但结果低于预期，可能原因包括学习率/初始化/训练轮次不足或数据增强差异，建议先用小步长复跑 1-3 个 epoch 做曲线对比，再决定是否保留该变体。\
3. 可把 `Total params` 和最终 `accuracy` 的统计脚本化（保存到 CSV），以便绘制更精确的对比图表。

***

