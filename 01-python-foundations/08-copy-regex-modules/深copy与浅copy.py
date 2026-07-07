# 2026年01月25日19时06分47秒
# xxx@qq.com
import  copy
def shallow_copy1():
    a=[1,2,3]
    b=a.copy()
    b[0]=5
    print(a)
    print(b)
def shallow_copycopy2():
    c=[1,2,3]
    d=copy.copy(c)
    print(id(c))
    print(id(d))
def use_copy_test1():
    a=[1,2]
    b=[3,4]
    c=[a,b]
    d=copy.copy(c)
    print(id(c))
    print(id(d))
    a[0]=5
    print(c)
    print(d)
    print("-"*50)
    print(id(a),id(b))
    print(id(c[0]),id(c[1]))
    print(id(d[0]),id(d[1]))
def use_deep_copy():
        a = [1, 2]
        b = [3, 4]
        c = [a, b]
        d = copy.deepcopy(c)
        print(id(c))
        print(id(d))
        a[0] = 5
        print(c)
        print(d)
        print("-" * 50)
        print(id(a), id(b))
        print(id(c[0]), id(c[1]))
        print(id(d[0]), id(d[1]))
class Student:
    def __init__(self,name,time):
        self.name=name
        self.time=time
        self.equipment=["鞋子","衣服","裤子"]
def use_copy_own_object():
        old=Student("小王",18)
        new=copy.deepcopy(old)
        new.time=20
        new.equipment.append("帽子")
        print(old.time)
        print(old.equipment)

if __name__ == '__main__':
     # use_deep_copy()
      use_copy_own_object()
