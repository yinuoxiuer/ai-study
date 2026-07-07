# 2026年01月21日20时25分29秒
# xxx@qq.com
class parent:
    def __init__(self,height):
        self.height=height

class son1(parent):
    def __init__(self,age,*args):
     self.age=age
     super().__init__(*args)

class son2(parent):
    def __init__(self,score,*args):
        self.score=score
        super().__init__(*args)

class grandson(son1,son2):
    def __init__(self,name,*args):
        self.name=name
        super().__init__(*args)
if __name__ == '__main__':
 xiaoming=grandson("小明",18,99.5,175)
 print(xiaoming.name)
 print(xiaoming.score)
 print(xiaoming.age)
 print(xiaoming.height)
 print(grandson.__mro__)