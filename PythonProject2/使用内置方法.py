class cat:

    def eat(self):
        print("吃吃吃")
    def drink(self):
        print("喝喝喝")
    def  __del__(self):
        print(f"销毁对象")
    def __str__(self):
        return f"这是对象{self.name}"
tom=cat()
tom.eat()
tom.drink()
lazy_cat=cat()
print(tom is lazy_cat)
lazy_cat=cat() #报错，cat()方法没有传参
tom.name="汤姆" #不规范
print(tom.name)
print(tom)
print(lazy_cat)