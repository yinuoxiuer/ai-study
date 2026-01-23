# 2026年01月17日12时00分45秒
# xxx@qq.com
def test(num):
    print(f"num的地址是{id(num)}")
a=10
print(f"调用函数前a的地址是{id(a)}")
test(a)
print(f"调用函数后a的地址是{id(a)}")
a=20
print(f"重新赋值a的地址是{id(a)}")

def change( numlist):
    print(f"调用函数前numlist的地址是{id(numlist)}")
    numlist[0]=1
    print(f"第一次调用函数后numlist的地址是{id(numlist)}")
    numlist=[1,2,3]
    print(f"第二次调用函数后numlist的地址是{id(numlist)}")
my_list=[10,20,30]

change(my_list)

print(my_list)