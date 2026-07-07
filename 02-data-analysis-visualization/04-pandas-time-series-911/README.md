# Day 13 - Pandas 911 数据分析项目

本项目是使用 Pandas 和 Matplotlib 对美国 911 报警电话数据进行的一次实践分析。项目主要展示了如何利用 Pandas 处理时间序列数据，并进行数据可视化。

## 项目文件

- `911.csv`: 项目所用的原始数据集，包含了报警电话的各种信息（如时间、地点、标题、描述等）。
- `pandas_learn2.ipynb`: 核心分析代码所在的 Jupyter Notebook 文件。
- `pandas_learn2.py`: 由 Notebook 导出的 Python 脚本文件。
- `README.md`: 本说明文件。

## 分析步骤

代码 `pandas_learn2.ipynb` 中主要完成了以下几个步骤：

1.  **数据加载**: 使用 `pd.read_csv()` 读取 `911.csv` 文件。

2.  **数据清洗与预处理**:
    - 将 `timeStamp` 列从字符串格式转换为 Pandas 的 `datetime` 时间类型，这是进行时间序列分析的基础。
    - 将 `timeStamp` 列设置为 DataFrame 的索引，方便后续按时间进行重采样（`resample`）。

3.  **特征工程**:
    - 从 `title` 列（例如 `"EMS: BACK PAIN/INJURY"`）中提取出报警的**主分类**（如 `EMS`, `Fire`, `Traffic`）。
    - 创建一个名为 `cate` 的新列来存储这些分类信息。

4.  **数据分析与可视化**:
    - 使用 `df.groupby('cate')` 对数据按报警分类进行分组。
    - 对每个分类的数据，使用 `resample('M')` 按**月**进行降采样，并使用 `.count()` 统计每月的报警次数。
    - 使用 Matplotlib 循环绘制每个分类的月度报警次数趋势图，并将它们呈现在同一张图表中，方便对比。
    - 对图表进行了美化，包括设置画布大小、添加图例、标题、坐标轴标签和旋转X轴刻度标签，以提高可读性。

## 如何运行

1.  确保你已经安装了 `pandas`, `matplotlib`, 和 `numpy` 库。
2.  打开 `pandas_learn2.ipynb` 文件。
3.  按顺序执行 Notebook 中的代码单元格。
4.  最终的图表将会在 Notebook 中直接显示出来。

## 关键 Bug 修复记录

在开发过程中，遇到了图表无法显示（`<Figure size ... with 0 Axes>`）的问题。原因及修复方法如下：

- **问题**: 在为 DataFrame 添加 `cate` 列时，由于索引不匹配，导致整列被赋值为 `NaN`（空值）。这使得 `groupby('cate')` 无法产生任何分组，绘图的 `for` 循环从未执行。
- **修复**: 将 `df["cate"] = pd.DataFrame(...)` 的复杂赋值方式，修改为更直接、更安全的 `df["cate"] = cate_list`，从而保证了分类数据被正确添加。
