# Day23 - NLP 深度学习进阶：从 RNN 到 LSTM

本项目是关于自然语言处理（NLP）的深度学习实践，重点涵盖了循环神经网络（RNN）的各种变体及其在文本分类（IMDB 数据集）和文本生成（莎士比亚文集）中的应用。

## 📂 项目结构

### 1. 文本分类实践 (IMDB 数据集)
这些 Notebook 展示了如何使用不同的 RNN 架构处理电影评论的情感分析任务：
*   `embedding_learn.ipynb`: 基础预处理，包括词嵌入（Embedding）、自定义 Tokenizer 实现以及动态填充（Dynamic Padding）逻辑。
*   `simple_rnn_learn.ipynb`: 使用单层单向 RNN 进行情感分类。
*   `two_layer_rnn_learn.ipynb`: 堆叠两层单向 RNN 以提取更深层的特征。
*   `bidirectional_rnn_learn.ipynb`: 实现单层双向 RNN，利用上下文信息提升性能。
*   `two_layer_bidirectional_rnn_learn.ipynb`: 结合了多层和双向结构的复杂 RNN 模型。

### 2. 文本生成实践 (莎士比亚文集)
*   `simple_lstm_generate.ipynb`: 使用字符级 LSTM（Long Short-Term Memory）网络学习莎士比亚的写作风格，并实现自动文本生成。

### 3. 资源文件
*   `shakespeare.txt`: 用于文本生成的原始语料库。
*   `checkpoints/`: 存放训练过程中保存的最佳模型权重（`.ckpt` 文件）。
*   `runs/`: 存放 TensorBoard 训练日志，用于可视化损失函数和准确率曲线。

## 🚀 核心技术点

*   **自定义 Tokenizer**: 实现了单词与 ID 的双向映射，支持特殊标记（`[PAD]`, `[BOS]`, `[EOS]`, `[UNK]`）。
*   **动态填充 (Dynamic Padding)**: 在 `collate_fn` 中根据每个 Batch 的最长句子动态调整长度，显著提升训练效率。
*   **双向 RNN 状态提取**: 学习了如何正确拼接双向 RNN 最后一层的正向和反向隐藏状态（`final_hidden[-2]` 和 `final_hidden[-1]`）。
*   **字符级建模**: 采用“错位对齐”的方法构造输入序列和目标序列，实现预测下一个字符的任务。

## 🛠️ 环境依赖

*   Python 3.x
*   PyTorch
*   TensorFlow (仅用于加载内置数据集)
*   NumPy, Pandas, Matplotlib
*   tqdm, scikit-learn

## 📈 使用说明

1.  确保已下载 `shakespeare.txt` 语料文件。
2.  按照 Notebook 的顺序运行，建议从 `embedding_learn.ipynb` 开始了解数据流。
3.  使用 TensorBoard 查看训练进度：
    ```bash
    tensorboard --logdir=runs
    ```
