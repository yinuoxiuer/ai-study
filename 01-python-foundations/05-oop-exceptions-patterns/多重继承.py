# 2026年01月21日17时56分05秒
# xxx@qq.com
class a :
    def test(self):
        print("a test")
    def demo(self):
        print("a demo")
class b:
    def test(self):
        print("b test")
    def demo(self):
        print("b demo")
class c(a,b):#多重继承第一个（最左边）
    pass
if __name__ == '__main__':
    c1=c()
    c1.test()
    c1.demo()
    print(c.__mro__)#查看类的继承顺序