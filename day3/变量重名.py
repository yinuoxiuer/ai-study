# 2026年01月17日16时19分57秒
# xxx@qq.com
def demo():
    num = 20  # 局部
    print(num)

num=10#全局
demo()
#就近原则
#如果想让里面是全局变量 就用global 变量名 在函数内声明