# NLP 与序列模型代码讲义

这一阶段代码从 RNN/LSTM 逐步过渡到 Seq2Seq Attention 和 Transformer，重点是文本预处理、Tokenizer、序列 padding、mask、训练循环和推理解码。

| 文件/单元 | 语法/库用法 | 例子意图 | 优点 | 注意事项 |
| --- | --- | --- | --- | --- |
| `01-rnn-lstm-text-classification-generation/` | Embedding、RNN、LSTM、Tokenizer、字符级生成 | 文本分类与文本生成入门 | 能理解序列状态传递 | RNN 长序列训练慢，梯度问题明显 |
| `02-subword-lstm-distributed-training/delete_imdb.py` | `os`/文件处理、异常捕获 | 清理或处理 IMDB 数据文件 | 实用脚本化操作 | 删除/改数据脚本运行前应确认路径，避免误操作 |
| `02-subword-lstm-distributed-training/` | BPE、LSTM、单/多 GPU 对比 | 子词分词和分布式训练 | 贴近 NLP 工程 | 多 GPU 需要环境一致，随机性和日志要记录 |
| `03-seq2seq-attention-translation/` | Encoder/Decoder、GRU、Bahdanau Attention、BLEU | 西英翻译实验 | 注意力可视化能帮助理解对齐 | Greedy decoding 简单但不一定最优，后续可加 beam search |
| `04-transformer-machine-translation/data_prepare.py` | `urllib.request`、`gzip`、函数封装、`main()` | 下载并解压 Multi30k 数据 | 脚本结构清晰，便于复用 | 依赖网络；失败时应重试或手动下载 |
| `04-transformer-machine-translation/data_multi30k.py` | 数据准备、BPE、文件写入、异常抛出 | 更完整的数据处理脚本 | 比简单下载脚本更接近训练前处理 | 路径和缓存要说明清楚 |
| `04-transformer-machine-translation/transformer_standalone.py` | `dataclass`、`nn.Module`、多头注意力、mask、Encoder/Decoder、输出对象 | 把 Transformer Notebook 核心实现整理为独立脚本 | 便于阅读模型结构和张量流 | mask 维度、padding、causal mask 是最容易出错的地方 |
| `05-relative-position-encoding/` | 相对位置索引、多头注意力位置项 | 观察 Transformer 位置编码变体 | 能理解绝对/相对位置差异 | 相对位置实现需要非常小心张量 broadcast 维度 |

## Transformer 重点语法说明

- `@dataclass`：用于组织模型输出，让返回值比裸 tuple 更可读。
- `nn.Module`：所有模型层都继承它，参数才能被 PyTorch 注册和优化。
- mask：用大负数屏蔽不该看的 token，softmax 后概率接近 0。
- `forward()`：定义模块调用时的计算路径。
- `torch.matmul()`：完成 QK 相似度和 attention 加权求和。

## 推荐补充

- 在每个翻译实验 README 中记录 BLEU、训练配置、最佳 checkpoint 和失败尝试。
- 对推理函数补输入输出例子，方便以后复现。
