# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
# def 关键字用于定义一个函数。
# print_hi 是函数的名称。
# name 是这个函数的一个参数，它是一个变量，当函数被调用时，它将持有传入的值。
# 函数体是缩进的，包含了函数要执行的代码。
# print() 是一个内置函数，用于将文本输出到控制台。
# f'Hi, {name}' 是一个 f-string，它允许你在字符串中嵌入表达式。在这里，它将变量 name 的值插入到字符串中。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
# if __name__ == '__main__': 是一个常见的 Python 结构。
# __name__ 是一个特殊的内置变量，当 Python 解释器读取一个源文件时，它会执行其中的所有代码。
# 当模块被直接运行时，__name__ 的值是 '__main__'。
# 当模块被导入时，__name__ 的值是模块的名称。
# 所以，这个 if 语句块中的代码只有在当前脚本是主程序时才会被执行。
# print_hi('PyCharm') 是对上面定义的 print_hi 函数的调用。
# 'PyCharm' 是传递给 name 参数的参数值。

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
