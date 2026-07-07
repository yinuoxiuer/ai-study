# 2026骞?1鏈?6鏃?1鏃?1鍒?4绉?
# xxx@qq.com
import re
def use_greedy():
    des="this is a number 4545-48748948-4896-48648"
    result=re.match(r".+?(\d+)-(\d+)-(\d+)-(\d+)",des)#闂彿鐨勪綔鐢ㄦ槸闈炶椽濠?
    print(result.group(1))
def use_option():
    print(re.match(r"\w*", "djwioqdji", flags=re.A).group())
    print(re.match(r"dj", "Dj", flags=re.I).group())#蹇界暐澶у皬鍐?
    print(re.match(r".*", "Dj\ndwd", flags=re.S).group())#鍖归厤鎹㈣绗?
if __name__ == '__main__':
    # use_greedy()
    # use_option()
    pass
