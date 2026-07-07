# AI 学习项目

这是一个按学习路线整理的 AI 学习仓库，内容覆盖 Python 编程基础、数据分析、传统机器学习、深度学习、NLP 序列模型、Transformer、大模型微调与论文复现。

原来的 `dayXX` 时间目录已经整理为“知识阶段 + 学习主题”的结构。每个子目录前面的数字只表示学习顺序，目录名表示本阶段真正学习的内容。

## 快速导航

| 阶段 | 目录 | 学习内容 |
| --- | --- | --- |
| 数值计算补充 | `00-numerical-methods/` | Hermite 插值与数值方法可视化 |
| Python 基础 | `01-python-foundations/` | 语法、控制流、函数、容器、OOP、异常、模块、正则、数据结构 |
| 数据分析与可视化 | `02-data-analysis-visualization/` | Jupyter、Matplotlib、NumPy、Pandas、EDA、时间序列分析 |
| 传统机器学习 | `03-machine-learning/` | 特征工程、分类模型、回归、聚类、梯度下降、集成学习、异常检测 |
| 深度学习 | `04-deep-learning/` | PyTorch、Tensor、Autograd、MLP、CNN、CIFAR-10、VGG/ResNet/Inception |
| NLP 与序列模型 | `05-nlp-sequence-models/` | Embedding、RNN、LSTM、BPE、Seq2Seq、Attention、Transformer、相对位置编码 |
| 大模型与论文复现 | `06-large-models-multimodal-papers/` | GLM-4 微调、LlamaFactory、PEFT、GLM-4V、DETR、DeepSeek-V3 |

完整目录映射与学习脉络见 [LEARNING_PATH.md](LEARNING_PATH.md)。

论文复现与方法来源统一收集在 [papers/README.md](papers/README.md)，可以从论文跳到对应学习单元，也可以从项目反查原文、官方实现和本地 PDF。

项目代码、论文索引与 Obsidian 知识库之间的整体关系见 [ARCHITECTURE.md](ARCHITECTURE.md)。

## 仓库阅读方式

1. 先读根目录的 `README.md` 与 `LEARNING_PATH.md`，了解整体学习路径。
2. 进入阶段目录，例如 `04-deep-learning/`，阅读该阶段的 `README.md`。
3. 如果是论文复现或模型结构学习，先查 [论文索引](papers/README.md) 建立“论文 -> 代码 -> 笔记”的对应关系。
4. 再进入具体学习单元，优先打开 `README.md` 和 `.ipynb`，必要时阅读配套 `.py` 脚本。

## 数据、权重与运行产物

本仓库保留了学习过程中产生的数据目录、checkpoint、TensorBoard 日志和部分外部源码仓库，用来呈现完整学习过程。它们通常体积较大，GitHub 上传时建议按需保留：

- 数据集：`cifar-10/`、`FashionMNIST/`、`wmt16/`、`spa-eng/` 等。
- 模型权重：`checkpoints/`、`*.ckpt`。
- 训练日志：`runs/`。
- 外部参考源码：`GLM-4/`、`LlamaFactory/`、DeepSeek-V3 相关源码。

如果只想阅读学习主线，可以优先看 README、Notebook 和核心 Python 脚本；如果要复现实验，再补齐对应数据和依赖。
