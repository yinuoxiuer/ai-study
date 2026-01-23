# 2026年01月20日21时48分59秒
# xxx@qq.com 属性是特别的，方法是通用的
class person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def run(self):
        print(f"{self.name}在运动")
    def eat(self):
        print(f"{self.name}在吃东西")
daxiang=person("大象",18,3.3)
print(daxiang.age)
daxiang.run()
class animal:
    def __init__(self,name,species,color):
        self.name=name
        self.species=species
        self.color=color
    def see_others(self):
        print("汪汪叫")
    def see_family(self):
        print("摇尾巴")
dahuang=animal("大黄","狗","黄色")
print(dir(dahuang))
print(id(dahuang))
dahuang.color="黑色"
print(id(dahuang))#可变数据类型