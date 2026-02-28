# Day30 课程笔记与实验

本目录包含两个 Jupyter Notebook：一个是 GLM-4V-9B 多模态推理示例，另一个是参数高效微调（PEFT）方法的学习与对比实验。内容以教学/学习为主，侧重流程与方法理解。

## 目录结构

```
./
  glm_4v_9b.ipynb
  PEFT（Parameter_Efficient_Fine_Tuning_讲解.ipynb
```

## Notebook 说明

### 1) `glm_4v_9b.ipynb`

- 目的：调用 `THUDM/glm-4v-9b` 进行图像描述推理，并记录模型参数量与结构要点。
- 主要步骤：
  - 克隆 GLM-4 仓库并安装依赖。
  - 加载 `GLM-4V-9B` 模型与分词器，使用 `apply_chat_template` 做图像+文本输入。
  - 执行 `generate` 生成图像描述。
  - 计算总参数量，并补充模型结构与注意力机制说明。
- 运行要点：Notebook 首行注明需要 A100 级别显存环境；建议在 Colab A100 上运行。

### 2) `PEFT（Parameter_Efficient_Fine_Tuning_讲解.ipynb`

- 目的：在 SST-2 二分类任务上，对比多种参数高效微调方法。
- 数据与预处理：
  - 通过 `datasets` 读取本地 `sst2` parquet 文件。
  - 使用 `bert-base-uncased` 分词器进行编码。
- 训练评估：
  - 统一训练函数与验证函数，支持早停与余弦学习率调度。
  - 记录并绘制多种方法的验证准确率曲线。
- 覆盖方法：
  - 冻结特征提取（Frozen）
  - 全量微调（Fully Fine-tuning）
  - BitFit（仅更新 bias）
  - P-Tuning / Prefix Tuning / P-Tuning v2
  - LoRA
  - Adapter Tuning

## 运行环境与依赖

以下为 Notebook 中使用到的主要依赖，版本以 Notebook 为准：

- Python 3.x
- PyTorch
- Transformers
- Datasets (`datasets==2.20.0`)
- 其他：tqdm、matplotlib、numpy、PIL 等

## 数据准备（SST-2）

`PEFT（Parameter_Efficient_Fine_Tuning_讲解.ipynb` 读取本地数据，默认路径为：

```
./sst2/data/train-00000-of-00001.parquet
./sst2/data/validation-00000-of-00001.parquet
```

请确保 `sst2` 目录位于项目根目录下。

## 使用建议

- 如果在本地运行，请确认显存与依赖版本满足要求；大模型推理建议使用 Colab A100。
- Notebook 中包含较多教学性质的文字说明，可按需要裁剪或整理成课程笔记。

## 可能的后续整理方向

- 将训练流程抽成可复用脚本或配置化实验。
- 补充不同 PEFT 方法的超参对比与训练曲线截图。
- 为 GLM-4V-9B 推理示例添加更多输入样例与可视化输出。
