# 论文索引

这里收集仓库中已经复现、拆解或作为方法来源的论文与技术报告。每一行尽量同时连接四类信息：论文原文、官方实现或项目页、本仓库学习单元、本地材料。

## 使用方式

- 从项目找论文：进入对应阶段 README 后，跳到本索引的分类表。
- 从论文找代码：在表格的“仓库学习单元”列进入 notebook、脚本或源码阅读目录。
- 增加新复现：优先补充论文原文链接、官方实现、仓库目录、复现状态和本地 PDF/笔记。

## 总览

| 分类 | 对应仓库阶段 | 重点 |
| --- | --- | --- |
| [深度学习图像模型](#deep-learning-papers) | [`04-deep-learning/`](../04-deep-learning/) | CNN、SELU、VGG、ResNet、Inception、Wide & Deep |
| [NLP 与序列模型](#nlp-sequence-papers) | [`05-nlp-sequence-models/`](../05-nlp-sequence-models/) | RNN/LSTM、BPE、Seq2Seq、Attention、Transformer、相对位置编码 |
| [大模型、多模态与论文复现](#large-model-papers) | [`06-large-models-multimodal-papers/`](../06-large-models-multimodal-papers/) | GLM、LLaMA-Factory、PEFT、GLM-4V、DETR、DeepSeek-V3 |

<a id="deep-learning-papers"></a>

## 深度学习图像模型

| 主题 | 论文 / 技术报告 | 仓库学习单元 | 官方实现 / 项目 | 本地材料 | 复现关系 |
| --- | --- | --- | --- | --- | --- |
| Wide & Deep | [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792) | [`04-deep-learning/02-mlp-regression-hparam-wide-deep/`](../04-deep-learning/02-mlp-regression-hparam-wide-deep/) | [TensorFlow wide_deep tutorial](https://www.tensorflow.org/tutorials/structured_data/wide_deep) | - | 宽深结构思想学习与 notebook 实验 |
| SELU | [Self-Normalizing Neural Networks](https://arxiv.org/abs/1706.02515) | [`04-deep-learning/02-mlp-regression-hparam-wide-deep/`](../04-deep-learning/02-mlp-regression-hparam-wide-deep/), [`04-deep-learning/04-cnn-cifar-resnet-transfer/`](../04-deep-learning/04-cnn-cifar-resnet-transfer/) | - | - | 激活函数对比与训练稳定性观察 |
| Depthwise separable convolution | [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357) | [`04-deep-learning/04-cnn-cifar-resnet-transfer/`](../04-deep-learning/04-cnn-cifar-resnet-transfer/) | - | - | `separable_cnn.ipynb` 中实现深度可分离卷积 |
| VGG | [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556) | [`04-deep-learning/05-vgg-resnet-inception-cifar10/`](../04-deep-learning/05-vgg-resnet-inception-cifar10/) | [torchvision VGG](https://pytorch.org/vision/stable/models/vgg.html) | [`vgg resnet inception论文对比与翻译摘要.pdf`](../05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/vgg%20resnet%20inception%E8%AE%BA%E6%96%87%E5%AF%B9%E6%AF%94%E4%B8%8E%E7%BF%BB%E8%AF%91%E6%91%98%E8%A6%81.pdf) | CIFAR-10 上从零实现、优化和微调 |
| ResNet | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) | [`04-deep-learning/04-cnn-cifar-resnet-transfer/`](../04-deep-learning/04-cnn-cifar-resnet-transfer/), [`04-deep-learning/05-vgg-resnet-inception-cifar10/`](../04-deep-learning/05-vgg-resnet-inception-cifar10/) | [torchvision ResNet](https://pytorch.org/vision/stable/models/resnet.html) | [`vgg resnet inception论文对比与翻译摘要.pdf`](../05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/vgg%20resnet%20inception%E8%AE%BA%E6%96%87%E5%AF%B9%E6%AF%94%E4%B8%8E%E7%BF%BB%E8%AF%91%E6%91%98%E8%A6%81.pdf) | 残差块实现、迁移学习和 CIFAR-10 对比 |
| Inception / GoogLeNet | [Going Deeper with Convolutions](https://arxiv.org/abs/1409.4842) | [`04-deep-learning/05-vgg-resnet-inception-cifar10/`](../04-deep-learning/05-vgg-resnet-inception-cifar10/) | [torchvision GoogLeNet](https://pytorch.org/vision/stable/models/googlenet.html) | [`vgg resnet inception论文对比与翻译摘要.pdf`](../05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/vgg%20resnet%20inception%E8%AE%BA%E6%96%87%E5%AF%B9%E6%AF%94%E4%B8%8E%E7%BF%BB%E8%AF%91%E6%91%98%E8%A6%81.pdf) | 多分支卷积模块实现和 CIFAR-10 实验 |
| Inception-ResNet | [Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning](https://arxiv.org/abs/1602.07261) | [`04-deep-learning/05-vgg-resnet-inception-cifar10/`](../04-deep-learning/05-vgg-resnet-inception-cifar10/) | - | [`vgg resnet inception论文对比与翻译摘要.pdf`](../05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/vgg%20resnet%20inception%E8%AE%BA%E6%96%87%E5%AF%B9%E6%AF%94%E4%B8%8E%E7%BF%BB%E8%AF%91%E6%91%98%E8%A6%81.pdf) | `inception_optimized_resnet_version.ipynb` 中尝试残差化 Inception |

<a id="nlp-sequence-papers"></a>

## NLP 与序列模型

| 主题 | 论文 / 技术报告 | 仓库学习单元 | 官方实现 / 项目 | 本地材料 | 复现关系 |
| --- | --- | --- | --- | --- | --- |
| Word2Vec / Embedding | [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) | [`05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/`](../05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/) | - | - | Embedding 与词向量基础 |
| LSTM | [Long Short-Term Memory](https://www.bioinf.jku.at/publications/older/2604.pdf) | [`05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/`](../05-nlp-sequence-models/01-rnn-lstm-text-classification-generation/), [`05-nlp-sequence-models/02-subword-lstm-distributed-training/`](../05-nlp-sequence-models/02-subword-lstm-distributed-training/) | - | - | 文本分类、字符生成、分布式训练对照 |
| BPE 子词 | [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/abs/1508.07909) | [`05-nlp-sequence-models/02-subword-lstm-distributed-training/`](../05-nlp-sequence-models/02-subword-lstm-distributed-training/), [`05-nlp-sequence-models/04-transformer-machine-translation/`](../05-nlp-sequence-models/04-transformer-machine-translation/) | [rsennrich/subword-nmt](https://github.com/rsennrich/subword-nmt) | - | IMDB/WMT 数据中的子词处理 |
| Seq2Seq | [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) | [`05-nlp-sequence-models/03-seq2seq-attention-translation/`](../05-nlp-sequence-models/03-seq2seq-attention-translation/) | - | - | Encoder/Decoder 翻译基线 |
| Bahdanau Attention | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | [`05-nlp-sequence-models/03-seq2seq-attention-translation/`](../05-nlp-sequence-models/03-seq2seq-attention-translation/) | - | - | 注意力对齐、可视化和 BLEU 评估 |
| Transformer | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | [`05-nlp-sequence-models/04-transformer-machine-translation/`](../05-nlp-sequence-models/04-transformer-machine-translation/) | [annotated-transformer](https://nlp.seas.harvard.edu/annotated-transformer/) | [`transformer论文摘要.pdf`](../05-nlp-sequence-models/04-transformer-machine-translation/transformer%E8%AE%BA%E6%96%87%E6%91%98%E8%A6%81.pdf) | 从数据、模型、训练到推理的完整 notebook |
| 相对位置编码 | [Self-Attention with Relative Position Representations](https://arxiv.org/abs/1803.02155) | [`05-nlp-sequence-models/05-relative-position-encoding/`](../05-nlp-sequence-models/05-relative-position-encoding/) | - | - | 多头注意力中的相对位置项实现 |

<a id="large-model-papers"></a>

## 大模型、多模态与论文复现

| 主题 | 论文 / 技术报告 | 仓库学习单元 | 官方实现 / 项目 | 本地材料 | 复现关系 |
| --- | --- | --- | --- | --- | --- |
| GLM 基础 | [GLM: General Language Model Pretraining with Autoregressive Blank Infilling](https://arxiv.org/abs/2103.10360) | [`06-large-models-multimodal-papers/01-glm4-finetuning-experiments/`](../06-large-models-multimodal-papers/01-glm4-finetuning-experiments/) | [THUDM/GLM-4](https://github.com/THUDM/GLM-4) | - | GLM-4 demo、微调流程和环境问题记录 |
| LLaMA-Factory | [LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models](https://arxiv.org/abs/2403.13372) | [`06-large-models-multimodal-papers/02-llamafactory-source-study/`](../06-large-models-multimodal-papers/02-llamafactory-source-study/) | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | - | 源码结构、训练框架和微调配置学习 |
| LoRA | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | [`06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/`](../06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/) | [microsoft/LoRA](https://github.com/microsoft/LoRA), [huggingface/peft](https://github.com/huggingface/peft) | - | 参数高效微调方法对比 |
| Prefix-Tuning | [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://arxiv.org/abs/2101.00190) | [`06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/`](../06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/) | [huggingface/peft](https://github.com/huggingface/peft) | - | PEFT 方法横向对比 |
| P-Tuning | [GPT Understands, Too](https://arxiv.org/abs/2103.10385) | [`06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/`](../06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/) | [THUDM/P-tuning-v2](https://github.com/THUDM/P-tuning-v2) | - | Prompt/Prefix 类微调方法学习 |
| Adapter | [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751) | [`06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/`](../06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/) | [AdapterHub](https://adapterhub.ml/) | - | Adapter 与 LoRA/Prefix/Frozen 对比 |
| BitFit | [BitFit: Simple Parameter-efficient Fine-tuning for Transformer-based Masked Language-models](https://arxiv.org/abs/2106.10199) | [`06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/`](../06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/) | - | - | 只训练 bias 的 PEFT 基线 |
| GLM-4V / CogVLM2 | [CogVLM2: Visual Language Models for Image and Video Understanding](https://arxiv.org/abs/2408.16500) | [`06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/`](../06-large-models-multimodal-papers/03-peft-and-glm4v-multimodal/) | [THUDM/CogVLM2](https://github.com/THUDM/CogVLM2), [THUDM/GLM-4](https://github.com/THUDM/GLM-4) | - | GLM-4V-9B 多模态推理示例 |
| DETR | [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) | [`06-large-models-multimodal-papers/04-detr-object-detection-transformer/`](../06-large-models-multimodal-papers/04-detr-object-detection-transformer/) | [facebookresearch/detr](https://github.com/facebookresearch/detr) | - | 简化版 DETR 结构实现 |
| DeepSeek-V3 | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | [`06-large-models-multimodal-papers/05-deepseek-v3-paper-and-inference/`](../06-large-models-multimodal-papers/05-deepseek-v3-paper-and-inference/) | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | [`DeepSeek_V3.pdf`](../06-large-models-multimodal-papers/05-deepseek-v3-paper-and-inference/DeepSeek_V3.pdf) | 论文、MoE/MLA/FP8 要点和推理源码学习 |

## 补充规则

新增论文时建议按下面顺序补齐：

1. 论文标题与原文链接，优先 arXiv、OpenReview、会议页或作者主页。
2. 官方代码、模型卡或项目页。
3. 本仓库对应目录、notebook、脚本或本地 PDF。
4. 复现状态：精读、结构实现、训练复现、推理复现、源码阅读等。

传统机器学习阶段目前以算法练习为主，暂不把每个经典算法都强行绑定到原始论文；后续如果开始做论文级复现，可以继续扩展本索引。
