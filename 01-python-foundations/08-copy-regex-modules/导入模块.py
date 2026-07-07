# 2026年01月26日08时40分42秒
# xxx@qq.com
# import my_module 默认只能在当前文件夹找
import sys
sys.path.append("module")#相对路径，最低优先级（低于标准库）要高优先级的话把append改为insert
print(sys.path)
print("-"*50)
import my_module
my_module.test1()