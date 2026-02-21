# Day25 Seq2Seq 学习项目

## 项目简介
本目录包含一个基于 PyTorch 的 Seq2Seq 翻译模型练习，使用西班牙语-英语平行语料（`spa-eng/spa.txt`）。包含基础版、改进版和 4 层模型版本的 Notebook，训练日志与模型权重保存在 `runs/` 与 `checkpoints/`。

## 目录结构
- `seq2seq_learn.ipynb`：基础版 Seq2Seq 训练与评估流程。
- `seq2seq_learn_improved.ipynb`：改进版（含断点续训、BLEU 评估、日志绘图）。
- `seq2seq_4layers.ipynb`：4 层模型版本（含多进程/线程设置）。
- `spa-eng/`：平行语料与说明文件。
- `runs/`：TensorBoard 日志。
- `checkpoints/`：模型权重与断点。
- `main.py`：示例脚本（PyCharm 默认模板）。

## 主要流程概览
1. **数据预处理**：Unicode 归一化、清理标点、构建训练/测试集。
2. **词表与分词**：构建 `word2idx/idx2word`，Tokenizer 编码/解码。
3. **模型结构**：Encoder + Bahdanau Attention + Decoder（GRU），Seq2Seq 训练与推理。
4. **训练与评估**：交叉熵损失、早停、TensorBoard 记录，支持 BLEU 评估。

## 快速使用（Notebook）
建议使用 Jupyter 逐单元运行，推荐顺序：
1. 打开 `seq2seq_learn_improved.ipynb` 或 `seq2seq_learn.ipynb`。
2. 依次运行：数据预处理 → 词表 → 模型定义 → 训练 → 评估。
3. 如需查看训练曲线：
   - 直接运行日志绘图单元，或使用 TensorBoard。

## 依赖环境（参考）
- Python 3.x
- numpy, pandas, sklearn
- torch, torchvision（CPU 或 CUDA）
- tqdm, matplotlib
- tensorboard
- nltk（用于 BLEU 评估）

## 断点续训与模型保存
- 权重保存在 `checkpoints/<实验名>/best.ckpt`。
- 改进版中包含断点续训逻辑（恢复 model/optimizer/step/epoch）。

## 日志与评估
- TensorBoard 日志：`runs/<实验名>/`。
- BLEU 评估：Notebook 中提供批量评估函数，输出语料级 BLEU。

## 注意事项
- 数据缓存：`./.cache/lang_pair.npy`。如数据切分异常可删除该缓存重新生成。
- Windows/Jupyter 多进程：4 层模型版本中使用 `spawn` 以避免死锁。
- 若重启内核，需重新加载模型与定义（改进版已提供自动重载逻辑）。

## 说明
本项目为学习实验记录，Notebook 内含详细注释与实验流程。若需进一步整理为脚本，可根据 Notebook 结构拆分模块。

