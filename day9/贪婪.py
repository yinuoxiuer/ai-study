# 2026年01月26日21时51分04秒
# xxx@qq.com
import re
def use_greedy():
    des="this is a number 4545-48748948-4896-48648"
    result=re.match(r".+?(\d+)-(\d+)-(\d+)-(\d+)",des)#问号的作用是非贪婪
    print(result.group(1))
def use_option():
    print(re.match(r"\w*","djwioqdji都叫我i都奇迹",flags=re.A).group())#忽略汉字
    print(re.match(r"dj", "Dj", flags=re.I).group())#忽略大小写
    print(re.match(r".*", "Dj\ndwd", flags=re.S).group())#匹配换行符
if __name__ == '__main__':
    # use_greedy()
    # use_option()
