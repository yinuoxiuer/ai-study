# 2026年01月17日20时55分16秒
# xxx@qq.com
my_list=["a","b","c"]
# print(my_list.index("bd"))存在异常捕捉后走
my_list[1]=123
print(my_list)
my_list.append("@")
print(my_list)#地址不变，且每次运行的这两个地址不一样
my_list.insert(1,"*")
print(my_list)
my_list.clear()
print(my_list)
del my_list
# print(my_list)不存在，所以打印不了