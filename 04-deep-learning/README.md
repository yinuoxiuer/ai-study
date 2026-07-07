# 深度学习

这一阶段从 PyTorch 基础开始，逐步搭建 MLP、CNN，并在 FashionMNIST 与 CIFAR-10 上练习完整训练流程。

## 学习单元

- `01-pytorch-mlp-fashionmnist/`：PyTorch 环境、FashionMNIST、MLP、训练循环、checkpoint、早停。
- `02-mlp-regression-hparam-wide-deep/`：回归、分类、超参数搜索、Wide & Deep。
- `03-tensor-autograd-custom-layers/`：Tensor 操作、数值微分、Autograd、自定义层。
- `04-cnn-cifar-resnet-transfer/`：CNN、SELU、深度可分离卷积、CIFAR-10、ResNet 迁移学习。
- `05-vgg-resnet-inception-cifar10/`：VGG、ResNet、Inception，从零实现、优化、AMP 与微调。

## 主线

重点是把训练工程闭环跑通：数据集、模型、损失、优化器、验证、保存、日志、复现和结构改进。

## 相关论文

本阶段涉及的 Wide & Deep、SELU、VGG、ResNet、Inception、Inception-ResNet 等论文统一整理在 [论文索引 - 深度学习图像模型](../papers/README.md#deep-learning-papers)。
