# 2026年01月19日21时37分24秒
# xxx@qq.com
list1=[1,2,3]
list2=[1,2,3]
print(list1==list2)
print(id(list1))
print(id(list2))
print(list1 is list2)
a=(1,2,3)
b=("a","b","c")
print(list(zip(a,b)))
print(dict(zip(a,b)))
seasons=["Spring","Summer","Autumn","Winter"]
print(list(enumerate(seasons)))
my_dict=dict(enumerate(seasons))
print({k:v for v,k in my_dict.items()})
