# 2026年01月20日20时30分59秒
# xxx@qq.com
import sys
sys.setrecursionlimit(100000)
def print_info(num):
    if num > 0:
        print_info(num-1)
        print(num)
# print_info(5)
def sum_num(num):
   if num>1:
       return num+sum_num(num-1)
   else:
       return 1
# print(sum_num(10))
def step(num):
    if num>2:
        return step(num-1)+step(num-2)
    elif num==1:
        return 1
    elif num==2:
        return 2
for i in range(1,100000):
    print(step(i))