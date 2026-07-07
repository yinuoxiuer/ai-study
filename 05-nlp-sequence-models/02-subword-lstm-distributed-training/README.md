# Day 24: 深度学习进阶 - LSTM 文本处理与分布式训练

本项目包含了第 24 天学习的深度学习相关内容，主要涵盖了基于 LSTM 的文本分类、文本生成以及 PyTorch 分布式训练的实践。

## 项目结构

- **subword_learn.ipynb**: 深入学习子词分词（Subword Tokenization）技术。
  - 使用 `subword-nmt` 工具进行 BPE（Byte Pair Encoding）分词。
  - 在 IMDB 电影评论数据集上进行情感分类任务。
  - 实现了自定义的 `Tokenizer` 和 `LSTM` 模型。
  - 包含完整的训练流程、TensorBoard 可视化、模型保存与早停机制。

- **lstm_generate_learn.ipynb**: 基于字符级的 LSTM 文本生成。
  - 使用莎士比亚作品集（shakespeare.txt）作为训练语料。
  - 实现了“预测下一个字符”的生成模型。
  - 涵盖了字符到索引的映射、数据预处理及模型构建。

- **embedding_lstm_learn.ipynb**: 探索 Embedding 层与 LSTM 的结合使用。
  - 学习如何将离散的单词/子词转换为连续的向量表示。

- **分布式训练示例**:
  - `01-lstm-distributed9-单GPU.ipynb`: 单 GPU 训练基准。
  - `01-lstm-distributed9-多GPU运行效果.ipynb`: 展示多 GPU 分布式训练的配置与运行效果，提升大规模模型训练效率。

## 核心技术点

1. **文本预处理**:
   - 数据清洗（去除 HTML 标签、特殊符号）。
   - BPE 分词技术：解决未登录词（OOV）问题，减小词表大小。
   - 填充（Padding）与截断（Truncation）策略。

2. **模型架构**:
   - **Embedding 层**: 词向量嵌入。
   - **LSTM (Long Short-Term Memory)**: 处理序列数据，解决长距离依赖问题。
   - **双向 LSTM (Bidirectional LSTM)**: 同时利用上下文信息。

3. **训练优化**:
   - **损失函数**: `BCEWithLogitsLoss` (二分类情感分析)。
   - **优化器**: Adam。
   - **回调函数**: 自定义 TensorBoard 可视化、模型检查点保存、早停（Early Stopping）。

4. **分布式计算**:
   - 学习如何利用 PyTorch 的分布式数据并行（DDP）在多 GPU 环境下加速训练。

## 数据集说明

- **IMDB Dataset**: 50,000 条电影评论，用于二分类情感分析。
- **Shakespeare Text**: 莎士比亚作品集，用于字符级文本生成练习。

## 运行环境

- Python 3.12+
- PyTorch
- Pandas, Numpy, Matplotlib, Scikit-learn
- subword-nmt
- TensorBoard
