# NLP 与序列模型

这一阶段从 RNN/LSTM 过渡到 Seq2Seq、Attention 和 Transformer，重点理解文本序列如何被编码、解码和对齐。

## 学习单元

- `01-rnn-lstm-text-classification-generation/`：Embedding、Tokenizer、RNN/LSTM 文本分类和字符级生成。
- `02-subword-lstm-distributed-training/`：BPE 子词、IMDB 情感分类、LSTM、单 GPU 与多 GPU 训练记录。
- `03-seq2seq-attention-translation/`：西英翻译、GRU Encoder/Decoder、Bahdanau Attention、BLEU。
- `04-transformer-machine-translation/`：德英翻译、BPE、Transformer、Noam 学习率、注意力可视化。
- `05-relative-position-encoding/`：相对位置编码在多头注意力中的实现。

## 主线

先理解“序列状态”如何传递，再理解 Attention 如何显式建模 token 对齐，最后进入 Transformer 的并行注意力结构。

## 相关论文

本阶段涉及的 Word2Vec、LSTM、BPE、Seq2Seq、Bahdanau Attention、Transformer、相对位置编码等论文统一整理在 [论文索引 - NLP 与序列模型](../papers/README.md#nlp-sequence-papers)。
