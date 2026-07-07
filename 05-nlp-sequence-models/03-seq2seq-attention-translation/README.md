# Day25 Seq2Seq 翻译实验记录

## 项目概览
本目录是一个西班牙语到英语的 Seq2Seq + Bahdanau Attention 学习项目，核心语料为 `spa-eng/spa.txt`。当前主要实验都在 Notebook 中完成，训练日志在 `runs/`，模型权重在 `checkpoints/`。

## Day25 文件说明（按用途）
- `seq2seq_learn.ipynb`：基础版训练/推理/BLEU 评估，作为对照基线。
- `seq2seq_learn_improved.ipynb`：引入更多工程化改造（保存、重载、评估流程）。
- `seq2seq_learn_improved_optimize.ipynb`：继续调参与优化，含 BLEU-4（200 样本）评估单元。
- `seq2seq_4layers.ipynb`：4 层网络结构尝试，偏结构与训练策略试验。
- `seq2seq_learn_final_fourlayers.ipynb`：当前最终版，已打通训练、保存、自动加载与翻译评估。
- `checkpoints/`：各实验权重目录（含旧命名与新规范命名）。
- `runs/`：TensorBoard 日志目录，和实验名一一对应。
- `outputs/`：文本导出目录（当前文件存在但为空）。
- `spa-eng/`：数据与说明文件（`_about.txt` 记录数据来源与许可）。
- `.cache/`：预处理缓存（`lang_pair.npy`）。
- `aliyun/`、`.idea/`：环境/IDE 相关目录。

## 模型与训练主线
1. 数据预处理：Unicode 归一化、标点切分、非法字符清洗。
2. 词表构建：`word2idx/idx2word` + `Tokenizer` 编解码。
3. 模型结构：`Encoder(GRU)` + `BahdanauAttention` + `Decoder(GRU)`。
4. 训练流程：交叉熵（带 padding mask）+ 周期验证 + 早停 + TensorBoard。
5. 推理评估：逐词解码（greedy）+ 注意力可视化 + 语料级 BLEU。

## 实验结果对照（来自各 Notebook 输出）
> 说明：下面是仓库里已保存输出单元中的结果，不同 Notebook 的样本量不完全一致。

| Notebook | 评估口径 | 输出结果 |
|---|---|---|
| `seq2seq_learn.ipynb` | 测试集 BLEU（100 样本） | `0.1272` |
| `seq2seq_learn_improved.ipynb` | 测试集 BLEU（100 样本） | `0.0003` |
| `seq2seq_learn_improved_optimize.ipynb` | BLEU-4（200 样本） | `0.0013` |
| `seq2seq_learn_final_fourlayers.ipynb` | 测试集 BLEU（100 样本） | `0.3605` |

## 为什么 `final` 版本当前效果最好
在当前仓库已记录结果里，`seq2seq_learn_final_fourlayers.ipynb` 的 BLEU（100 样本）最高，主要来自“结构 + 训练稳定性 + 工程一致性”三方面同时改进：

1. 训练更稳：学习率降到 `2e-4`（对比早期常见 `1e-3`），并保留 `dropout=0.3`。
2. 梯度更可控：在 `loss.backward()` 后、`optimizer.step()` 前做 `clip_grad_norm_`（`max_grad_norm=1.0`），显式抑制 RNN 梯度爆炸。
3. 深层结构生效：统一使用 `encoder_num_layers=4` 与 `decoder_num_layers=4`，并在加载时自动从 checkpoint 推断层数，避免“模型层数和权重不匹配”导致的加载失败或隐式退化。
4. 保存/加载链路更完整：
   - 保存命名规范：`best_e{enc}_d{dec}_s{step}_{timestamp}.ckpt`
   - 指针文件：`best.latest.txt` 用于精确定位本次实验最新 best
   - 加载逻辑：优先读取 marker，再回退匹配 `best_*.ckpt`，与旧版 `best.ckpt` 共存不冲突。
5. 可视化反馈更直接：训练后立即绘制 loss 曲线，便于及时判断是否收敛。

## 新旧模型不冲突的约定
- 每次训练使用唯一实验名：`translate-seq2seq-e{enc}-d{dec}-{timestamp}`。
- 同一实验目录内保留多个 best 快照，`best.latest.txt` 指向当前推荐加载文件。
- 老目录中的 `best.ckpt` 仍可回退加载，但不会覆盖新命名权重。

## 推荐使用方式
1. 首选运行 `seq2seq_learn_final_fourlayers.ipynb` 进行训练与翻译。
2. 训练完成后查看：
   - loss 曲线（Notebook 内 matplotlib 输出）
   - TensorBoard：`runs/<exp_name>/`
   - 权重目录：`checkpoints/<exp_name>/`
3. 翻译推理时优先使用 `best.latest.txt` 对应的 checkpoint。

## 已知限制
- BLEU 评估包含随机抽样（如 100 样本），单次结果会波动。
- `seq2seq_learn_improved_optimize.ipynb` 使用 200 样本 BLEU-4，不能与 100 样本结果做严格横向等价比较。
- 当前项目以 Notebook 实验为主，尚未拆分为标准化脚本训练框架。

