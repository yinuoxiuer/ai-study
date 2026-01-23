# 2026年01月21日21时49分09秒
# xxx@qq.com
class dog:
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s蹦蹦跳跳" % self.name)
class xiaotianquan(dog):
    def game(self):
        print("%s飞到天上去玩耍" % self.name)
if __name__ == '__main__':
    wangcai = dog("旺财")
    wangcai.game()
    x1 = xiaotianquan("哮天犬")
    x1.game()
class person:
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s和%s一起玩耍" % (self.name,dog.name))
        dog.game()
if __name__ == '__main__':
    zhangsan = person("张三")
    wangcai = dog("旺财")
    zhangsan.game_with_dog(wangcai)
    xiaotianquan = xiaotianquan("哮天犬")
    zhangsan.game_with_dog(xiaotianquan)