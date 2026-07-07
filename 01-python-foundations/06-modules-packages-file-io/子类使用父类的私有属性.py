class A:
    def __init__(self):
        self.__age = 18
    def base_age(self):
         print(self.__age)
class B(A):
     def get_age(self):
         self.base_age()
zhangsan = B()
zhangsan.get_age()