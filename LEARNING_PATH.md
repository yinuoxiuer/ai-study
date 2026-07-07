# 学习路线与目录映射

本文件记录从基础编程到大模型论文复现的完整学习路径。左侧是现在的知识目录，括号里保留原始学习顺序，便于追溯旧记录。

## 00 数值计算补充

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `00-numerical-methods/01-hermite-interpolation/` | `numerical_learn` | Hermite 插值、多项式与分段基函数可视化 |

## 01 Python 基础

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `01-python-foundations/00-pycharm-entry-demo/` | 根目录 `main.py` | PyCharm 入口脚本与 `__main__` 结构 |
| `01-python-foundations/01-syntax-variables-operators/` | `day2` | 注释、输出、变量、类型转换、运算符、循环作业 |
| `01-python-foundations/02-control-flow-functions-lists/` | `day3` | 循环、break、函数参数、模块、列表、作用域 |
| `01-python-foundations/03-containers-memory-functions/` | `day4` | 元组、字典、集合、字符串、切片、内存、返回值 |
| `01-python-foundations/04-recursion-oop-intro/` | `day5` | 判空、递归、多值参数、默认参数、OOP 入门 |
| `01-python-foundations/05-oop-exceptions-patterns/` | `day6` | 封装、继承、多态、单例、异常捕获与传递 |
| `01-python-foundations/06-modules-packages-file-io/` | `day7` | 模块、包、导入冲突、文件/目录操作、自定义包 |
| `01-python-foundations/07-data-structures-sorting/` | `day8` | 二叉树、排序、`sort` 与 `sorted` |
| `01-python-foundations/08-copy-regex-modules/` | `day9` | 类型判断、深浅拷贝、正则表达式、模块导入 |

## 02 数据分析与可视化

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `02-data-analysis-visualization/01-jupyter-matplotlib-intro/` | `day10` | Jupyter 基础、Matplotlib 折线图 |
| `02-data-analysis-visualization/02-numpy-matplotlib-basics/` | `day11` | NumPy 数组、广播、切片、统计、Matplotlib 图表 |
| `02-data-analysis-visualization/03-numpy-pandas-eda/` | `day12` | NumPy 读数据、Pandas Series/DataFrame、YouTube/IMDB 数据分析 |
| `02-data-analysis-visualization/04-pandas-time-series-911/` | `day13` | 911 报警数据、时间索引、重采样、分组可视化 |

## 03 传统机器学习

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `03-machine-learning/01-feature-engineering-classification/` | `day14` | DictVectorizer、Count/TF-IDF、标准化、缺失值、分类算法 |
| `03-machine-learning/02-knn-bayes-decision-tree/` | `day15` | KNN、朴素贝叶斯、决策树与树可视化 |
| `03-machine-learning/03-regression-clustering-gradient-descent/` | `day16` | 回归、逻辑回归、梯度下降、聚类 |
| `03-machine-learning/04-ensemble-anomaly-dbscan/` | `day17` | DBSCAN、IQR/Z-score、Isolation Forest、集成学习 |

## 04 深度学习

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `04-deep-learning/01-pytorch-mlp-fashionmnist/` | `day18` | PyTorch 基础、FashionMNIST、MLP、训练/验证/早停 |
| `04-deep-learning/02-mlp-regression-hparam-wide-deep/` | `day19` | MLP 回归、分类、超参数搜索、Wide & Deep |
| `04-deep-learning/03-tensor-autograd-custom-layers/` | `day20` | Tensor、Autograd、数值微分、自定义层 |
| `04-deep-learning/04-cnn-cifar-resnet-transfer/` | `day21` | CNN、SELU、深度可分离卷积、CIFAR-10、ResNet 迁移 |
| `04-deep-learning/05-vgg-resnet-inception-cifar10/` | `day22` | VGG、ResNet、Inception、BatchNorm、AMP、微调 |

## 05 NLP 与序列模型

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/` | `day23` | Embedding、Tokenizer、RNN/LSTM 文本分类与生成 |
| `05-nlp-sequence-models/02-subword-lstm-distributed-training/` | `day24` | BPE 子词、IMDB 情感分类、LSTM、单/多 GPU 对照 |
| `05-nlp-sequence-models/03-seq2seq-attention-translation/` | `day25` | 西英翻译、Encoder/Decoder、Bahdanau Attention、BLEU |
| `05-nlp-sequence-models/04-transformer-machine-translation/` | `day26` | 德英翻译、BPE、Transformer、Noam LR、注意力可视化 |
| `05-nlp-sequence-models/05-relative-position-encoding/` | `day27` | 相对位置编码与多头注意力中的位置项 |

## 06 大模型与论文复现

| 当前目录 | 原目录 | 内容 |
| --- | --- | --- |
| `06-large-models-multimodal-papers/01-glm4-finetuning-experiments/` | `day28` | GLM-4 官方 demo、微调流程、失败原因与环境记录 |
| `06-large-models-multimodal-papers/02-llamafactory-source-study/` | `day29` | LlamaFactory 源码与训练框架学习 |
| `06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/` | `day30` | PEFT 方法对比、GLM-4V-9B 多模态推理 |
| `06-large-models-multimodal-papers/04-detr-object-detection-transformer/` | `day31` | DETR 目标检测、ResNet backbone、Transformer decoder |
| `06-large-models-multimodal-papers/05-deepseek-v3-paper-and-inference/` | `day32` | DeepSeek-V3 论文、MoE/MLA/FP8 要点、推理源码 |

## 主线总结

这条学习路线从“会写 Python”开始，逐步进入“会处理数据”“会训练传统模型”“会搭深度学习训练循环”，再转向 NLP 中的序列建模与注意力机制，最后落到大模型微调、视觉 Transformer 和论文复现。
