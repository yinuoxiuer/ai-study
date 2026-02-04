# Day 14 - 机器学习基础：特征工程与分类算法

本项目旨在通过 Jupyter Notebook 演示机器学习中两个核心环节：**特征工程**和**分类算法**的应用。项目利用 `scikit-learn` 这一强大的机器学习库，展示了从原始数据处理到模型应用准备的全过程。

---

## 核心技术栈

*   **数据处理**: `pandas`, `numpy`
*   **机器学习**: `scikit-learn`
*   **中文分词**: `jieba`
*   **数据可视化**: `matplotlib`

---

## 主要模块与功能

本项目包含两个核心 Notebook 文件：

1.  `特征工程.ipynb`
2.  `机器学习的分类算法.ipynb`

### 1. 特征工程 (`特征工程.ipynb`)

该 Notebook 详细演示了将原始数据转换为可供机器学习模型使用的数值特征的各种技术。

#### 主要内容：

*   **字典特征提取 (`DictVectorizer`)**
    *   **用途**: 将包含键值对的字典列表转换为数值型特征矩阵。通常用于处理类别数据。
    *   **核心语法**:
        ```python
        from sklearn.feature_extraction import DictVectorizer
        dv = DictVectorizer(sparse=False)
        data = dv.fit_transform([{'city': '北京', 'temperature': 100}, ...])
        ```

*   **文本特征提取 (`CountVectorizer` & `TfidfVectorizer`)**
    *   **用途**: 将文本文档集合转换为词频（Count）或 TF-IDF 权重矩阵。
    *   **中文处理**: 对于中文文本，需要先使用 `jieba` 进行分词，并用空格连接，再送入 Vectorizer。
    *   **核心语法**:
        ```python
        import jieba
        from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

        # 中文分词
        text = "我爱北京天安门"
        words = " ".join(jieba.cut(text))

        # 词频统计
        cv = CountVectorizer()
        count_matrix = cv.fit_transform([words])

        # TF-IDF
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform([words])
        ```

*   **数据预处理**
    *   **归一化 (`MinMaxScaler`)**: 将特征缩放到一个给定的范围（通常是 `[0, 1]`）。适用于受距离计算影响的模型。
        ```python
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        normalized_data = scaler.fit_transform(data)
        ```
    *   **标准化 (`StandardScaler`)**: 将特征缩放至均值为 0，方差为 1。适用于大多数机器学习算法。
        ```python
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        standardized_data = scaler.fit_transform(data)
        ```

*   **缺失值处理 (`SimpleImputer`)**
    *   **用途**: 对数据中的缺失值（如 `np.nan`）进行填补。
    *   **核心语法**:
        ```python
        from sklearn.impute import SimpleImputer
        imputer = SimpleImputer(strategy='mean') # 可选 'median', 'most_frequent'
        imputed_data = imputer.fit_transform(data_with_missing_values)
        ```

*   **特征选择与降维**
    *   **低方差过滤 (`VarianceThreshold`)**: 删除方差不满足某个阈值的特征（例如，方差为 0 的特征）。
        ```python
        from sklearn.feature_selection import VarianceThreshold
        selector = VarianceThreshold(threshold=0.0)
        selected_data = selector.fit_transform(data)
        ```
    *   **主成分分析 (`PCA`)**: 一种无监督的线性降维方法，用于在保留大部分信息的前提下减少特征数量。
        ```python
        from sklearn.decomposition import PCA
        # 保留 95% 的信息或降至 2 个主成分
        pca = PCA(n_components=0.95) # or n_components=2
        reduced_data = pca.fit_transform(data)
        ```

### 2. 机器学习的分类算法 (`机器学习的分类算法.ipynb`)

该 Notebook 侧重于数据集的加载、探索和划分，为后续应用分类模型做准备。

#### 主要内容：

*   **数据集加载 (`sklearn.datasets`)**
    *   **小数据集**: `load_iris()` (鸢尾花)
    *   **大数据集**: `fetch_20newsgroups()` (20类新闻)
    *   **核心语法**:
        ```python
        from sklearn.datasets import load_iris, fetch_20newsgroups
        iris = load_iris()
        news = fetch_20newsgroups(subset='all')
        ```

*   **数据集划分 (`train_test_split`)**
    *   **用途**: 将数据集划分为训练集和测试集，用于模型训练和评估。
    *   **核心语法**:
        ```python
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(
            features,
            target,
            test_size=0.25,
            random_state=42
        )
        ```

*   **分类模型（参考）**
    Notebook 中导入了多种经典的分类算法，可基于预处理后的数据进行训练和预测：
    *   `KNeighborsClassifier` (K-近邻)
    *   `MultinomialNB` (朴素贝叶斯)
    *   `DecisionTreeClassifier` (决策树)
    *   `RandomForestClassifier` (随机森林)

---

## 如何运行

1.  确保已安装所有必需的库 (`pip install pandas numpy scikit-learn jieba matplotlib`)。
2.  在 Jupyter Notebook 环境中打开 `.ipynb` 文件。
3.  按顺序执行每个单元格以查看演示结果。
