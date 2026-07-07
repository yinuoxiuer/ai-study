# Day 12 - 数据分析学习笔记 (NumPy & Pandas)

本目录包含了第 12 天关于 Python 数据分析的学习代码和练习，主要涵盖了 NumPy 和 Pandas 的基础用法，以及使用 Matplotlib 进行简单的数据可视化。

## 核心内容

### 1. NumPy 基础 (`numpy——learn2.ipynb`, `numpy读数据.ipynb`)
- **数组操作**：掌握了数组的创建 (`arange`, `reshape`)、转置 (`transpose`, `T`, `swapaxes`)。
- **随机数生成**：使用 `np.random.randint` 和 `np.random.randn` 生成测试数据。
- **缺失值处理**：学习了 `np.nan` 的特性（必须为浮点类型）以及如何在数组中赋值。
- **数据读取**：练习使用 `np.loadtxt` 加载 CSV 数据。

### 2. Pandas 基础 (`learn_pandas.ipynb`)
- **数据结构**：
    - **Series**：带索引的一维数组，学习了通过标签和位置进行切片。
    - **DataFrame**：二维表格对象，掌握了从字典、列表创建 DF。
- **索引与切片**：
    - 区分了 `df['col']` (取列) 和 `df.loc['row']` (取行)。
    - 学习了 `.loc` (标签索引) 和 `.iloc` (位置索引) 的规范用法。
- **数据清洗**：
    - **缺失值处理**：使用 `dropna()` 删除空值，`fillna()` 填充空值。
    - **去重统计**：使用 `unique()` 和 `nunique()` 统计唯一值数量。
- **数据排序与应用**：
    - 使用 `sort_values` 按列排序。
    - 使用 `apply` 和 `lambda` 表达式进行批量数据处理。

### 3. 数据可视化练习
- **YouTube 数据分析** (`英国youtube评论数和喜欢数.py`)：
    - 使用 NumPy 加载 YouTube 视频数据。
    - 使用 Matplotlib 绘制散点图 (`plt.scatter`)，观察点赞数与评论数之间的关系。
    - 练习了布尔索引进行数据筛选（如：`t_uk[t_uk[:,1]<=250000]`）。

## 数据文件
- `IMDB-Movie-Data.csv`: 电影数据集，用于练习 Pandas 查询与统计。
- `911.csv`: 紧急救援电话数据集。
- `youtube_video_data/`: 包含美国(US)和英国(GB)的 YouTube 视频统计数据。

## 运行环境
- Python 3.x
- NumPy
- Pandas
- Matplotlib
