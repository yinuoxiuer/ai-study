# 2026年01月19日18时19分42秒
# xxx@qq.com
# set1={}
# print(type(set1))
# set1=set()
# print(type(set1))
fruit={"apple","banana","orange"}
fruit.add("pears")
print(fruit)
print(id( fruit))
x=fruit
print(id(x))
x=fruit.copy()
print(id(x))
fruit1={"banana","grape"}
z=fruit.difference(fruit1)
print(z)
z.discard("apple")
print(z)
consequence= fruit.isdisjoint(fruit1)
print(consequence)
x = fruit.symmetric_difference(fruit1)
print(x)
print("apple" in fruit)
print("cherry" in fruit)
print(fruit-fruit1)
my_set={x for x in "avvassvacacsa"}
print(my_set)
print(max(fruit))