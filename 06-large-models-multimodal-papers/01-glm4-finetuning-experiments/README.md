# Day 28

本目录包含 GLM-4 相关 demo、微调脚本与实验笔记。

## 目录结构

- `GLM-4/`: 官方仓库源码与 demo
- `glm4微调.ipynb`: 微调尝试与安装命令记录
- `chatglm3_6b_context.ipynb`: 其他模型实验笔记

## 快速开始（微调）

> 仅记录流程要点，具体参数与环境请参考 `GLM-4/finetune_demo/README.md`。

1. 安装依赖（按官方 requirements）
2. 切换到 `GLM-4/finetune_demo` 目录
3. 执行 `finetune.py` 并指定数据与配置

## GLM-4 微调失败原因总结（来自笔记记录）

以下为 `glm4微调.ipynb` 中体现的常见失败原因与修复思路：

- **依赖版本冲突**: `peft` 需要 `0.12.0`，但安装 `bitsandbytes`/其他包可能引入不兼容版本。
- **transformers 版本问题**: 记录中出现 `transformers==4.40.0` 的固定安装，提示高版本可能触发 bug。
- **相对路径找不到**: 未切换到 `GLM-4/finetune_demo` 时，`./AdvertiseGen_fix/` 与 `configs/lora.yaml` 无法解析。
- **缺失依赖**: 记录中手动安装 `ruamel.yaml`，说明 requirements 未完整生效或环境不一致。

## 备注

- 官方文档与环境要求见 `GLM-4/finetune_demo/README.md`。
- 若继续排查，请优先确认 Python 版本、CUDA 环境与 GPU 资源是否满足官方基准。

