# DETR模型简介

本项目实现了DETR（Detection Transformer）目标检测模型的简化版本，基于PyTorch和Torchvision。

## 主要内容
- 使用ResNet-50作为特征提取骨干网络。
- 通过1x1卷积将特征维度从2048降至256。
- 利用Transformer结构进行目标检测。
- 分类器输出类别（COCO数据集91类+1背景）。
- 边界框回归器输出目标框的坐标。
- 位置编码采用可学习的行/列嵌入。

## 代码结构
- `DETR`类：继承自`nn.Module`，包含骨干网络、卷积降维、Transformer、分类器、边界框回归器、位置编码等。
- `forward`方法：输入图片，经过特征提取、降维、位置编码、Transformer处理，输出分类和边界框。

## 快速开始
1. 安装依赖：
   - `torch`
   - `torchvision`
2. 运行`detr.ipynb`，可测试模型的前向推理。

## 输入输出说明
- 输入：尺寸为`(1, 3, 800, 1200)`的图片张量。
- 输出：
  - 分类结果`logits`，形状为`(100, 1, 92)`。
  - 边界框`bboxes`，形状为`(100, 1, 4)`。

## 参考
- [DETR论文](https://arxiv.org/abs/2005.12872)
- [PyTorch官方文档](https://pytorch.org/)

---
如需进一步使用或训练，请参考原论文和官方实现。
