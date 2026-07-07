# 数据分析与可视化代码讲义

这一阶段的 `.py` 文件主要是 Notebook 之外的小脚本，用于演示 Matplotlib、NumPy/Pandas 数据读取和简单图表。

| 文件 | 语法/库用法 | 例子意图 | 优点 | 注意事项 |
| --- | --- | --- | --- | --- |
| `01-jupyter-matplotlib-intro/test.py` | `import matplotlib.pyplot as plt`、`plt.plot()`、`plt.show()` | 最小折线图 | 快速看到绘图流程 | 脚本运行会弹出窗口；批处理环境可保存为图片 |
| `02-numpy-matplotlib-basics/main.py` | `def`、f-string、入口判断 | PyCharm 模板/入口练习 | 保留脚本运行结构 | 实际分析逻辑主要在 Notebook 中 |
| `03-numpy-pandas-eda/英国youtube评论数和喜欢数.py` | NumPy 读 CSV、数组切片、布尔过滤、Matplotlib 散点图 | 分析评论数和喜欢数关系 | 能练习矩阵列选择和筛选 | NumPy 适合纯数值；混合类型数据更适合 Pandas |
| `03-numpy-pandas-eda/美国youtube 1000多部电影的评论数分布-改进.py` | 直方图、分箱、数据过滤 | 观察评论数分布 | 适合理解数据分布 | 分箱数量会影响图形解读，需要解释选择依据 |
| `03-numpy-pandas-eda/main.py` | 入口模板 | 占位脚本 | 结构统一 | 可把常用数据加载函数抽到这里 |
| `04-pandas-time-series-911/pandas_learn2.py` | `pd.read_csv()`、`to_datetime()`、`set_index()`、`groupby()`、`resample()`、Matplotlib | 911 报警数据时间序列分析 | 非常贴近真实 EDA 流程 | 时间列转换和索引设置是关键；链式操作多时要注意中间结果 |

## 推荐补充

- 数据分析脚本可统一加 `main()`，并把绘图输出保存到 `outputs/`，便于非交互环境复现。
- 对 CSV 路径使用 `pathlib.Path(__file__).parent`，避免从不同工作目录运行时找不到数据。
