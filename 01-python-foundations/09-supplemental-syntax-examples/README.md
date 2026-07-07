# 补充语法示例

这个目录用于补充原始学习记录中没有系统覆盖、但后续写项目很常用的 Python 语法。它不替换原来的 `day` 学习代码，只作为“后补讲义”。

## 文件

- `supplemental_examples.py`

## 覆盖内容

- `with open(...)`：上下文管理，自动关闭文件。
- `enumerate()` / `zip()`：带序号遍历和多序列并行遍历。
- `yield`：生成器，节省内存。
- decorator：装饰器，在不改函数主体时增加额外行为。
- type hints：类型标注，提高可读性和工具提示。
- `dataclass`：减少数据类样板代码。
- `match-case`：结构化分支匹配。
- `pathlib.Path`：更现代的路径处理方式。
- dict comprehension：字典推导式。

## 运行

```powershell
python supplemental_examples.py
```
