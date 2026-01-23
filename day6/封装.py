# 2026年01月21日12时15分09秒
# xxx@qq.com
class person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def run(self):
        print(f"运动前体重为:{self.weight}kg")
        self.weight -= 0.5
        print(f"{self.name}正在运动,运动后体重为:{self.weight}kg")
    def eat(self):
        print(f"吃东西前体重为:{self.weight}kg")
        self.weight += 1
        print(f"{self.name}正在吃东西,体重为:{self.weight}kg")
    def __str__(self):
        """只能返回字符串"""
        return f"{self.name}的体重为:{self.weight}kg"

if __name__ == '__main__':
 elephant = person("大象", 80)
 elephant.run()
 print(elephant)