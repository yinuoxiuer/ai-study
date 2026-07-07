# Day 17 学习笔记

本项目包含 Day 17 的机器学习算法学习代码，主要使用 Jupyter Notebook 进行演示。

## 文件说明

### 1. dbscan_learn.ipynb (DBSCAN 聚类)
- **内容**: 演示了 DBSCAN (Density-Based Spatial Clustering of Applications with Noise) 聚类算法的使用。
- **主要步骤**:
    - 生成包含噪声的样本数据 (`make_blobs` + 均匀分布噪声)。
    - 使用 `DBSCAN` 进行聚类 (`eps=0.5`, `min_samples=5`)。
    - 识别并分离噪声点 (标签为 -1)。
    - 可视化聚类结果，区分正常点和噪声点。

### 2. median_learn.ipynb (异常值检测)
- **内容**: 演示了两种基于统计学的异常值检测方法。
- **方法一**: 基于四分位数 (IQR)
    - 计算 Q1, Q3 和 IQR。
    - 定义上下界 (`Q1 - 1.5*IQR`, `Q3 + 1.5*IQR`)。
    - 标记超出范围的点为异常值。
- **方法二**: 基于 Z-score (标准分数)
    - 计算平均值和标准差。
    - 计算 Z-score。
    - 标记绝对值大于阈值 (如 3.5) 的点为异常值。

### 3. ensemble_learn.ipynb (集成学习)
- **内容**: 全面介绍了集成学习的各种方法。
- **主要算法**:
    - **Voting (投票法)**:
        - Hard Voting (硬投票): 少数服从多数。
        - Soft Voting (软投票): 基于概率加权。
        - 比较了逻辑回归、SVM 和决策树的单独效果与集成效果。
    - **Bagging (装袋法)**:
        - 使用 `BaggingClassifier` 集成多个决策树。
        - 演示了 `n_jobs=-1` 并行加速的效果。
        - 演示了对特征进行采样 (Random Subspaces)。
    - **Random Forest (随机森林)**:
        - 使用 `RandomForestClassifier`。
        - 介绍了 OOB (Out-of-Bag) 分数评估。
    - **Extra Trees (极端随机树)**:
        - 使用 `ExtraTreesClassifier`。
    - **Boosting (提升法)**:
        - 使用 `AdaBoostClassifier` 进行串行提升训练。

### 4. isolation_forest_learn.ipynb (孤立森林)
- **内容**: 演示了使用孤立森林 (Isolation Forest) 进行异常检测。
- **主要步骤**:
    - 生成随机二维数据。
    - 初始化 `IsolationForest` 模型 (`contamination=0.1`)。
    - 训练模型并预测异常分数。
    - 可视化结果，区分正常点 (1) 和异常点 (-1)。

### 5. main.py
- **内容**: 简单的 Python 示例脚本，包含一个打印问候语的函数。

## 环境要求

- Python 3.x
- Jupyter Notebook
- scikit-learn
- pandas
- numpy
- matplotlib
