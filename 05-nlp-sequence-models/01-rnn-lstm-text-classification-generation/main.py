import os
import sys

# 尝试手动修复路径问题（如果 DLL 找不到）
try:
    import torch
    print(f"PyTorch 版本: {torch.__version__}")
    print(f"CUDA 是否可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"显卡型号: {torch.cuda.get_device_name(0)}")
except ImportError as e:
    print(f"导入失败！错误详情: {e}")
    print("提示：请尝试安装微软 C++ 运行库 (Visual C++ Redistributable)。")