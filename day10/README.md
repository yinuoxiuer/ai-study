# Day 10 学习笔记

本目录包含第 10 天的学习代码和笔记，主要涉及 Python 数据可视化库 Matplotlib 的基础使用以及 Jupyter Notebook 的基本操作。

## 文件说明

### 1. 代码文件
*   **`test.py`**: 
    *   一个标准的 Python 脚本。
    *   演示了如何导入 `matplotlib.pyplot`，绘制简单的折线图，并使用 `plt.show()` 显示图像。
*   **`matplotlib.ipynb`**: 
    *   `test.py` 的 Jupyter Notebook 版本。
    *   演示了在 Notebook 环境下进行绘图，图像可直接在单元格下方显示。
*   **`jupyter_test.ipynb`**: 
    *   Jupyter Notebook 的基础练习。
    *   包含变量赋值、运算等基本 Python 操作。
    *   记录了一些学习笔记。

## 学习笔记摘要

### Jupyter Notebook
*   Jupyter 主要用于交互式编程和数据探索。
*   笔记中提到 Jupyter 只能导入 py 文件（通常指作为模块导入时）。

### 工具使用
*   **文件传输**: 提到了 **FinalShell** 和 **WinSCP**，这两个工具常用于在本地 Windows 和远程 Linux 服务器之间传输文件。

## 运行指南

### 运行 Python 脚本
确保已安装 `matplotlib`：
```bash
pip install matplotlib
```
运行脚本：
```bash
python test.py
```

### 运行 Jupyter Notebook
确保已安装 `jupyter` 和 `matplotlib`：
```bash
pip install jupyter matplotlib
```
启动 Jupyter Notebook：
```bash
jupyter notebook
```
然后在浏览器中打开对应的 `.ipynb` 文件运行即可。
