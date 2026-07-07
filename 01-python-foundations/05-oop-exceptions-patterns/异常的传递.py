# 2026年01月22日13时31分52秒
# xxx@qq.com
def demo1():
    num=int(input("请输入数字:"))
    return num
def demo2():
    num2=demo1()
    print("demo2")
    return num2
try:
    print(demo2())
except Exception as resultc:
    print("出现异常 %s"% resultc)