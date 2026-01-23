# 2026年01月22日14时44分50秒
# xxx@qq.com
def input_password():
    while True:
        pwd=input("请输入密码:")
        if len(pwd)>=6:
            return pwd
        else:
           raise Exception("密码长度不够")
try:
    print(input_password())
except Exception as e:
    print(e)
try:
    assert 1 == 2, "发生异常" #相当于if not 1==1: raise AssertionError("发生异常")
except Exception as e:
    print(e)
