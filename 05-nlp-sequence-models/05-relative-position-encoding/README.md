# day27 相对位置编码学习

## 简介
本目录包含一个用于学习相对位置编码（Relative Position Embedding）的 Jupyter Notebook，演示如何在多头注意力中引入相对位置信息。

## 内容概览
- 相对位置编码模块 `RelativePositionEmbedding`
- 多头注意力模块 `MultiHeadAttention`，在 QK 相关性上叠加相对位置项
- 简单示例与形状检查输出

## 环境依赖
- Python 3.8+（建议）
- PyTorch
- Jupyter Notebook（可选，仅在需要运行 `.ipynb` 时）

## 运行方式
使用 Jupyter 打开并运行 `relative_postition_learn.ipynb`。

如果使用命令行启动 Jupyter：
```bash
jupyter notebook
```

## 核心说明
- 相对位置索引范围为 `[-(max_seq_len-1), ..., 0, ..., +(max_seq_len-1)]`，对应 `2*max_seq_len-1` 个可训练向量。
- 注意力中相对位置项在 QK 点积之后叠加，输出形状为 `(batch_size, num_heads, seq_len, seq_len)`。
- 需要满足 `embed_dim % num_heads == 0`。

## 示例输出
Notebook 中包含以下示例检查：
- 相对位置索引矩阵
- 相对位置参数张量形状
- 相对位置嵌入张量形状

## 备注
- `max_seq_len` 需不小于运行时的 `seq_len`。
- 该示例用于学习与理解，未包含完整的训练或掩码逻辑。

