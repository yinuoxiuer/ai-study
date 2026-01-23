# 2026年01月16日13时34分51秒
# xxx@qq.com
for i in range(0,10):
    for j in range(0,i+1):
        if(i*j!=0):
            print(i ,"*", j,"=", i * j,end="")
            print(" ",end="")
    print("",end="\n")
