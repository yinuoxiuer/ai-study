# 深度学习代码讲义

这一阶段核心代码主要在 Notebook，`main.py` 多为入口模板或 IDE 生成脚本。重点应放在模型类、训练循环、验证函数、checkpoint 和回调逻辑上。

| 学习单元 | 核心内容 | 语法/库用法 | 优点 | 注意事项 |
| --- | --- | --- | --- | --- |
| `01-pytorch-mlp-fashionmnist/` | FashionMNIST + MLP | `torch.utils.data.Dataset/DataLoader`、`nn.Module`、`CrossEntropyLoss`、SGD、早停 | 从零打通深度学习训练闭环 | 训练/验证模式要切换 `model.train()` / `model.eval()` |
| `02-mlp-regression-hparam-wide-deep/` | MLP 回归、分类、超参数搜索、Wide & Deep | 标准化、训练循环、学习率试验、多输入模型结构 | 能理解调参和结构设计 | 超参数搜索要固定随机种子并记录结果 |
| `03-tensor-autograd-custom-layers/` | Tensor、Autograd、自定义层 | `requires_grad`、反向传播、`nn.Module` 自定义 forward | 理解 PyTorch 的核心计算机制 | 原地操作可能破坏计算图，需谨慎 |
| `04-cnn-cifar-resnet-transfer/` | CNN、SELU、深度可分离卷积、ResNet 迁移 | `Conv2d`、Pooling、Flatten、预训练模型 | 从 MLP 过渡到图像模型 | 图像张量维度通常是 `[N, C, H, W]`，维度错会直接报错 |
| `05-vgg-resnet-inception-cifar10/` | VGG/ResNet/Inception、AMP、BatchNorm、微调 | 残差连接、多分支卷积、混合精度、数据增强 | 接近真实图像分类项目 | CIFAR 数据和 checkpoint 体积大，GitHub 展示时可忽略数据产物 |

## 推荐补充

- 关键训练 Notebook 可以在开头补“实验目的/数据/模型/指标/结论”。
- 如果要把 Notebook 变成工程代码，可拆成 `dataset.py`、`model.py`、`train.py`、`evaluate.py`。
