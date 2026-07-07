# 2026年01月20日10时32分04秒
# xxx@qq.com
a=5
b=5
print(a is b)
a="hellow"
b="hellow"
print( a is b)
a=554665456884988494848946448986
b=554665456884988494848946448986
print(a is b)
a=(1,2,3,4,5,6)
b=(1,2,3,4,5,6)
print(a is b)
xa=[x for x in range (1000)]
yb=[y for y in range (1000)]
print(xa is yb)
a=5
print(id(a))
del a
b=5
print(id(b))