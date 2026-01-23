# 2026年01月16日14时01分05秒
# xxx@qq.com
i=0
a=int(input("please input a number"))
print(bin(a))
while a!=0:
    if a%2!=0:
     i+=1
    a=a>>1
print(i)
