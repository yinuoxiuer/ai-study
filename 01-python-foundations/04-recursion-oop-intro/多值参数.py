# 2026年01月20日19时13分27秒
# xxx@qq.com
def demo2(*args,**kwargs):
    print(f"这是demo2函数{args}")
    print(f"这是demo2函数{kwargs}")





def demo (num,*args,**kwargs):
    print(num)
    print( args)
    print( kwargs)
    demo2(*args,**kwargs)#这里的*是解包
demo(1,2,4,5,3,name='xiaoming',age=18)