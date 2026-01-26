# 2026年01月26日10时35分19秒
# xxx@qq.com
import re
from re import finditer


def simple_match1():
    result=re.match("vc","avc")
    if result:
        print(result.group())
def simple_match2():
    result=re.match("a.","avc")
    if result:
        print(result.group())
def simple_match3():
    result=re.match("[Aac]","avc")
    if result:
        print(result.group())
def simple_match4():
    result=re.match("[0-9]","7avc")
    if result:
        print(result.group())
def simple_match5():
    result=re.match("a\\d","a7vc")
    if result:
        print(result.group())

def simple_match6():
    result = re.match("a\\d", "a7vc")
    if result:
        print(result.group())
def simple_match7():
    result=re.match("[a-z][A-Z]","dHjwiHOIHIOhwqoiavc")
    if result:
        print(result.group())

def simple_match8():
    result = re.match("[1-35-9]", "4HjwiHOIHIOhwqoiavc")
    if result:
        print(result.group())

def regular_name(name):
    result = re.match("[a-zA-z_]\\w*", name)
    if result:
        print("通过")
    else:
        print("失败")

def simple_match10():
    result = re.match("[A-Za-z0-9_]{6}", "12aCa*49")#只是处理前六个
    if result:
        print(result.group())
def simple_match11():
    result = re.match("[A-Za-z0-9_]{8,20}", "12aCa4jd023jd282d02jd82320jd0329")#如果是上一个会被星号打断，现在则是贪婪
    if result:
        print(result.group())
def discrete_email(email):
    result=re.match(r"\w{4,20}@(163|qq|126)\.com$",email) #不转义.的话就会匹配所有字符，美元表示结尾吗，括号成组
    if result:
        print("通过")
    else:
        print("失败")
def split_group1(num):#匹配0到100
    result = re.match(r"[1-9]?\d$|100", num)  # 不转义.的话就会匹配所有字符，美元表示结尾
    if result:
        print("通过")
    else:
        print("失败")
def split_group2(num):#匹配1到99
    result = re.match(r"[1-9]?[1-9]$|[1-9]+0$", num)  # 不转义.的话就会匹配所有字符，美元表示结尾
    if result:
        print("通过")
    else:
        print("失败")
#匹配分组前面的先匹配
def split_group3(num):
    result=re.match(r"([^-]+)-(\d+)", num)
    if result:
        print(result.group(0))
        print(result.group(1))
        print(result.group(2))
    else:
        print("失败")
def data_clear():
    result=re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    if result:
        print("通过")
    else:
        print("失败")

def nickname():
    result = re.match(r"<(?P<name1>[a-zA-Z]*)>\w*</(?P=name1)>", "<html>hh</html>")
    if result:
        print("通过")
    else:
        print("失败")
def search_test():
    result = re.search(r"\d+", "dwnlk12aCa4jd023jd282d02jd82320jd0329")#如果是上一个会被星号打断，现在则是贪婪
    if result:
        print(result.group())
def find_second_match():
    match=re.finditer(r"\d+", "dwnlk12aCa4jd023jd282d02jd82320jd0329")
    next(match)
    second_match=next(match)
    if second_match:
        print(second_match.group())
    #第i次next返回第i个，指针指向下一个
def find_all_match():
    match=re.findall(r"\d+", "dwnlk12aCa4jd023jd282d02jd82320jd0329")
    print(match)
def number_generator(start=0):
    while True:
        yield start#yield类似于断点，这是一个生成器的例子
        start+=1#next相对于取值并且程序执行到下一次yield
def use_sub1():
    result=re.sub(r"\d+",lambda x: str(int(x.group())+100),"djwidjwo456645664")
    print(result)
def use_sub2():
    result=re.sub("orange","apple","orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange",count=5)
    print(result)
#一个findall的问题，如果想提取整体但是有括号就加?:
import re


def use_findall_fixed():
    # 1. 原始字符串
    s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'

    # ---------------- 数据清洗步骤 (保持不变) ----------------
    ret_s = re.sub(r'年|月', r'/', s)
    ret_s = re.sub(r'日', r' ', ret_s)
    ret_s = re.sub(r'时|分', r':', ret_s)
    print(f"清洗后的文本: {ret_s}")

    # ---------------- 核心修复点 ----------------
    # 原来的写法: (0[0-9]|1[0-9]|2[0-4])  <-- findall 会只抓取这里面的内容
    # 现在的写法: (?:0[0-9]|1[0-9]|2[0-4]) <-- 加上 ?: 表示"只分组不捕获"

    regex_str = r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]'

    pattern = re.compile(regex_str)

    ret = pattern.findall(ret_s)
    print(f"最终提取结果: {ret}")
def clear2():
    start="""<div>
<p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
王道码农训练营-WWW.CSKAOYAN.COM
王道码农训练营-WWW.CSKAOYAN.COM
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握 HTTP 协议，熟悉 MVC、MVVM 等概念以及相关 WEB 开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<
br></p>
<p>4、掌握 NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>"""
#赋值号后面的三引号不是注释
    ret=re.sub(r"<[^>]*>|@nbsp;|\n","",start)
    print(ret)
def use_split1():
    result=re.split(" |;","dwdw d180;dh219;d3io fde")
    print(result)
if __name__ == '__main__':
    # simple_match2()
    # simple_match3()
    # simple_match4()
    # simple_match5()
    # simple_match7()
    # simple_match8()
    # regular_name("9j")
    # simple_match9()
    # simple_match10()
    # simple_match11()
    # discrete_email("4489498@qq.com")
    # split_group1("100")
    # split_group2("50")
    # split_group3("010-4849889")
    # data_clear()
    # search_test()
    # find_second_match()
    # find_all_match()
    # gen=number_generator()
    # print(type(gen))
    # print(next(gen))
    # use_sub1()\
    # use_sub2()
    # clear2()
    # use_split1()

