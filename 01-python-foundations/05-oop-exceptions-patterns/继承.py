# 2026年01月21日16时00分06秒
# xxx@qq.com
class animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("%s正在吃饭" % self.name)
    def sleep(self):
        print("%s正在睡觉" % self.name)
    def drink(self):
        print("%s正在喝水" % self.name)
    def run(self):
        print("%s正在跑步" % self.name)
class dog(animal):
    def __init__(self,name,color):
        super().__init__(name)#继承父类属性
        self.name = name+"覆盖1"
        self.color = color
    def run(self):
        super().run()#调用父类方法
        print("%s正在疯狂奔跑" % self.name)

    def bark(self):
        print("%s正在汪汪叫" % self.name)
class xiaotianquan(dog):
    def __init__(self,name,color,age):
        super().__init__(name,color)
        self.age = age
    def fly(self):
        print("%s的%s岁小天犬正在飞" % (self.color,self.age))
class cat(animal):
    def catch(self):
        print("%s正在抓老鼠" % self.name)





if __name__ == '__main__':
    wangcai = dog("旺财","黄色")
    wangcai.run()
    x1=xiaotianquan("哮天犬","白色",20)
    x1.run()
    x1.fly()