"""Supplemental Python syntax examples for the foundation stage.

这些例子不替换原学习代码，只补足原目录里较少覆盖的现代 Python 写法。
每个函数都尽量保持短小，便于单独运行、对照和复习。
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Iterator


@dataclass
class StudentRecord:
    """dataclass 自动生成 __init__、__repr__ 和字段比较等常用方法。

    优点：适合保存结构化数据，少写样板代码。
    注意：它主要表达“数据对象”，复杂业务行为仍应写成普通类方法。
    """

    name: str
    score: int


def use_with_open(path: str) -> str:
    """使用 with 管理文件资源。

    语法点：上下文管理器会在代码块结束时自动关闭文件。
    优点：即使中途抛异常，也能释放文件句柄。
    注意：读取外部文件时仍要处理 FileNotFoundError 等异常。
    """

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def use_enumerate_and_zip(names: list[str], scores: list[int]) -> list[StudentRecord]:
    """把 enumerate 和 zip 组合起来遍历多个序列。

    语法点：enumerate 给出序号，zip 把多个列表按位置打包。
    优点：比手动维护下标更不容易错。
    注意：zip 会按最短序列截断，如果两个列表长度不同，后面的数据会被忽略。
    """

    records: list[StudentRecord] = []
    for index, (name, score) in enumerate(zip(names, scores), start=1):
        print(f"第 {index} 位学生: {name} -> {score}")
        records.append(StudentRecord(name=name, score=score))
    return records


def count_up_to(limit: int) -> Iterator[int]:
    """生成器函数示例。

    语法点：函数中出现 yield 时，调用函数不会立刻执行完整逻辑，而是返回迭代器。
    优点：适合逐个产生大量数据，节省内存。
    注意：生成器只能向前消费，不能像列表一样随意重复索引。
    """

    current = 0
    while current <= limit:
        yield current
        current += 1


def debug_call(func: Callable[..., object]) -> Callable[..., object]:
    """装饰器：在不修改原函数主体的情况下增加调试输出。

    语法点：函数也是对象，可以接收函数并返回新的包装函数。
    优点：适合日志、计时、鉴权等横切逻辑。
    注意：真实项目建议使用 functools.wraps 保留原函数元信息。
    """

    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"调用 {func.__name__}, args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


@debug_call
def add(left: int, right: int) -> int:
    """类型标注示例：说明参数和返回值类型。"""

    return left + right


def classify_score(score: int) -> str:
    """match-case 结构化匹配示例，Python 3.10+ 可用。

    优点：比多层 if/elif 更适合枚举式分支。
    注意：范围判断仍常用 if；match 更擅长精确值、结构和模式。
    """

    match score // 10:
        case 10 | 9:
            return "A"
        case 8:
            return "B"
        case 7:
            return "C"
        case _:
            return "D"


def use_pathlib(root: str) -> list[Path]:
    """pathlib 路径对象示例。

    语法点：Path 用对象方式拼接、判断和遍历路径。
    优点：比手写字符串路径更跨平台、更可读。
    注意：Path 对象传给旧库时，有时需要转成 str。
    """

    root_path = Path(root)
    return [path for path in root_path.iterdir() if path.is_file()]


def build_lookup(records: Iterable[StudentRecord]) -> dict[str, int]:
    """字典推导式示例。

    优点：把“从列表生成映射”的意图写得很紧凑。
    注意：如果 name 重复，后面的分数会覆盖前面的分数。
    """

    return {record.name: record.score for record in records}


if __name__ == "__main__":
    sample_records = use_enumerate_and_zip(["zhangsan", "lisi"], [95, 82])
    print(list(count_up_to(3)))
    print(add(1, 2))
    print(classify_score(88))
    print(build_lookup(sample_records))
