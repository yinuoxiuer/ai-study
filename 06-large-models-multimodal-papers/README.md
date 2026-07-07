# 大模型与论文复现

这一阶段记录大模型工程、微调工具链、多模态模型、目标检测 Transformer 和 DeepSeek-V3 论文/源码学习。

## 学习单元

- `01-glm4-finetuning-experiments/`：GLM-4 demo、微调流程、依赖冲突和失败原因记录。
- `02-llamafactory-source-study/`：LlamaFactory 源码与训练框架学习。
- `03-peft-and-glm4v-multimodal/`：PEFT 方法、LoRA/参数高效微调思路、GLM-4V-9B 多模态推理。
- `04-detr-object-detection-transformer/`：DETR 简化实现，理解目标检测中的 Transformer 查询机制。
- `05-deepseek-v3-paper-and-inference/`：DeepSeek-V3 论文、MoE/MLA/FP8 等要点和推理源码。

## 主线

这一阶段的重点从“训练一个模型”转向“大模型系统如何组织”：源码结构、依赖环境、微调配置、推理入口、论文结构与工程实现之间的对应关系。

## 相关论文

本阶段涉及的 GLM、LLaMA-Factory、PEFT、GLM-4V、DETR、DeepSeek-V3 等论文和官方实现统一整理在 [论文索引 - 大模型、多模态与论文复现](../papers/README.md#large-model-papers)。
