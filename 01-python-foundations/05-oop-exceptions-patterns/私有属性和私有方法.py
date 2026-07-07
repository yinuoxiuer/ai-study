# 2026年01月21日15时08分31秒
# xxx@qq.com
class Women:
    def __init__(self, name,age):
        self.name = name
        self.__age = age  # 私有属性
    def __secret(self):
        print('我的年龄是%d' % self.__age)
    def boyfriend(self):
        self.__secret()
if __name__ == '__main__':
    xiaohong = Women('小红', 18)
    xiaohong.boyfriend()
    # xiaohong.secret()
    xiaohong._Women__secret()