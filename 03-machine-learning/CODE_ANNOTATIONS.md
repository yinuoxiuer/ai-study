# 传统机器学习代码讲义

这一阶段核心内容主要在 Notebook。`main.py` 多数是入口模板，真正的算法示例在 `.ipynb` 中。

| 学习单元 | 核心 Notebook/脚本 | 语法/库用法 | 优点 | 注意事项 |
| --- | --- | --- | --- | --- |
| `01-feature-engineering-classification/` | `特征工程.ipynb`、`机器学习的分类算法.ipynb` | `DictVectorizer`、`CountVectorizer`、`TfidfVectorizer`、`StandardScaler`、`SimpleImputer`、分类器 API | 系统掌握 scikit-learn 的 `fit/transform/predict` 范式 | 训练集和测试集必须分开 fit，避免数据泄漏 |
| `02-knn-bayes-decision-tree/` | `knn_learn.ipynb`、`bayess_learn.ipynb`、`Decision_Tree.ipynb` | KNN、朴素贝叶斯、决策树、Graphviz 可视化 | 覆盖最典型的传统分类模型 | KNN 对尺度敏感；决策树容易过拟合；贝叶斯依赖条件独立假设 |
| `03-regression-clustering-gradient-descent/` | `regression_learn.ipynb`、`logic_regression_learn.ipynb`、`gradient_down_learn.ipynb`、`cluster _learn.ipynb` | 回归、逻辑回归、梯度下降、聚类 | 从监督学习过渡到无监督学习 | 梯度下降要关注学习率；聚类要先标准化并解释簇含义 |
| `04-ensemble-anomaly-dbscan/` | `dbscan_learn.ipynb`、`median_learn.ipynb`、`isolation_forest_learn.ipynb`、`ensemble_learn.ipynb` | DBSCAN、IQR/Z-score、IsolationForest、Voting/Bagging/RandomForest/Boosting | 体现模型组合和异常检测思路 | 集成模型效果强但解释性下降；异常检测阈值要结合业务 |

## 阅读建议

每个 Notebook 都可以按这条线读：数据加载 -> 特征处理 -> 模型定义 -> 训练/拟合 -> 评估 -> 可视化 -> 结论。
