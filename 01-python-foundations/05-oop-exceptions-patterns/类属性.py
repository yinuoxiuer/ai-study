# 2026年01月21日22时16分36秒
# xxx@qq.com
class tool:
    count=0#类属性，也就是类的全局变量
    def __init__(self,name):
        self.name=name
        tool.count+=1
    def __del__(self):#如果统计当前有多少实例
        tool.count-=1
    def func(self):
        print("%s在工作" % self.name)
    @classmethod
    def show_tool_count(cls):
        print(cls.count)
    @staticmethod
    def help():
        print("这是一个工具类，可以创建各种工具")
if __name__ == '__main__':
    tool1=tool("斧头")
    print(tool.count)#这个是推荐写法
    tool2=tool("锤子")
    print(tool2.count)#这个不规范
    del tool1
    print(tool.count)
    tool.show_tool_count()