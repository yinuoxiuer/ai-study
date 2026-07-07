# 2026骞?1鏈?6鏃?0鏃?5鍒?9绉?
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
        print("閫氳繃")
    else:
        print("澶辫触")

def simple_match10():
    result = re.match("[A-Za-z0-9_]{6}", "12aCa*49")#鍙槸澶勭悊鍓嶅叚涓?
    if result:
        print(result.group())
def simple_match11():
    result = re.match("[A-Za-z0-9_]{8,20}", "12aCa4jd023jd282d02jd82320jd0329")#濡傛灉鏄笂涓€涓細琚槦鍙锋墦鏂紝鐜板湪鍒欐槸璐┆
    if result:
        print(result.group())
def discrete_email(email):
    result=re.match(r"\w{4,20}@(163|qq|126)\.com$",email) #涓嶈浆涔?鐨勮瘽灏变細鍖归厤鎵€鏈夊瓧绗︼紝缇庡厓琛ㄧず缁撳熬鍚楋紝鎷彿鎴愮粍
    if result:
        print("閫氳繃")
    else:
        print("澶辫触")
def split_group1(num):#鍖归厤0鍒?00
    result = re.match(r"[1-9]?\d$|100", num)  # 涓嶈浆涔?鐨勮瘽灏变細鍖归厤鎵€鏈夊瓧绗︼紝缇庡厓琛ㄧず缁撳熬
    if result:
        print("閫氳繃")
    else:
        print("澶辫触")
def split_group2(num):#鍖归厤1鍒?9
    result = re.match(r"[1-9]?[1-9]$|[1-9]+0$", num)  # 涓嶈浆涔?鐨勮瘽灏变細鍖归厤鎵€鏈夊瓧绗︼紝缇庡厓琛ㄧず缁撳熬
    if result:
        print("閫氳繃")
    else:
        print("澶辫触")
#鍖归厤鍒嗙粍鍓嶉潰鐨勫厛鍖归厤
def split_group3(num):
    result=re.match(r"([^-]+)-(\d+)", num)
    if result:
        print(result.group(0))
        print(result.group(1))
        print(result.group(2))
    else:
        print("澶辫触")
def data_clear():
    result=re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
    if result:
        print("閫氳繃")
    else:
        print("澶辫触")

def nickname():
    result = re.match(r"<(?P<name1>[a-zA-Z]*)>\w*</(?P=name1)>", "<html>hh</html>")
    if result:
        print("閫氳繃")
    else:
        print("澶辫触")
def search_test():
    result = re.search(r"\d+", "dwnlk12aCa4jd023jd282d02jd82320jd0329")#濡傛灉鏄笂涓€涓細琚槦鍙锋墦鏂紝鐜板湪鍒欐槸璐┆
    if result:
        print(result.group())
def find_second_match():
    match=re.finditer(r"\d+", "dwnlk12aCa4jd023jd282d02jd82320jd0329")
    next(match)
    second_match=next(match)
    if second_match:
        print(second_match.group())
    #绗琲娆ext杩斿洖绗琲涓紝鎸囬拡鎸囧悜涓嬩竴涓?
def find_all_match():
    match=re.findall(r"\d+", "dwnlk12aCa4jd023jd282d02jd82320jd0329")
    print(match)
def number_generator(start=0):
    while True:
        yield start#yield绫讳技浜庢柇鐐癸紝杩欐槸涓€涓敓鎴愬櫒鐨勪緥瀛?
        start+=1#next鐩稿浜庡彇鍊煎苟涓旂▼搴忔墽琛屽埌涓嬩竴娆ield
def use_sub1():
    result=re.sub(r"\d+",lambda x: str(int(x.group())+100),"djwidjwo456645664")
    print(result)
def use_sub2():
    result=re.sub("orange","apple","orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange",count=5)
    print(result)
#涓€涓猣indall鐨勯棶棰橈紝濡傛灉鎯虫彁鍙栨暣浣撲絾鏄湁鎷彿灏卞姞?:
import re


def use_findall_fixed():
    # 1. 鍘熷瀛楃涓?
    s = 'hello world, now is 2020/7/20 18:48, now is 2020/7/20 18:48'

    # ---------------- 鏁版嵁娓呮礂姝ラ (淇濇寔涓嶅彉) ----------------
    ret_s = s
    print(f"娓呮礂鍚庣殑鏂囨湰: {ret_s}")

    # ---------------- 鏍稿績淇鐐?----------------
    # 鍘熸潵鐨勫啓娉? (0[0-9]|1[0-9]|2[0-4])  <-- findall 浼氬彧鎶撳彇杩欓噷闈㈢殑鍐呭
    # 鐜板湪鐨勫啓娉? (?:0[0-9]|1[0-9]|2[0-4]) <-- 鍔犱笂 ?: 琛ㄧず"鍙垎缁勪笉鎹曡幏"

    regex_str = r'\d{4}/[01]?[0-9]/[1-3]?[0-9]\s(?:0[0-9]|1[0-9]|2[0-4])\:[0-5][0-9]'

    pattern = re.compile(regex_str)

    ret = pattern.findall(ret_s)
    print(f"鏈€缁堟彁鍙栫粨鏋? {ret}")
def clear2():
    start="""<div>
<p>宀椾綅鑱岃矗锛?/p>
<p>瀹屾垚鎺ㄨ崘绠楁硶銆佹暟鎹粺璁°€佹帴鍙ｃ€佸悗鍙扮瓑鏈嶅姟鍣ㄧ鐩稿叧宸ヤ綔</p>
<p><br></p>
鐜嬮亾鐮佸啘璁粌钀?WWW.CSKAOYAN.COM
鐜嬮亾鐮佸啘璁粌钀?WWW.CSKAOYAN.COM
<p>蹇呭瑕佹眰锛?/p>
<p>鑹ソ鐨勮嚜鎴戦┍鍔ㄥ姏鍜岃亴涓氱礌鍏伙紝宸ヤ綔绉瀬涓诲姩銆佺粨鏋滃鍚?/p>
<p>&nbsp;<br></p>
<p>鎶€鏈姹傦細</p>
<p>1銆佷竴骞翠互涓?Python 寮€鍙戠粡楠岋紝鎺屾彙闈㈠悜瀵硅薄鍒嗘瀽鍜岃璁★紝浜嗚В璁捐妯″紡</p>
<p>2銆佹帉鎻?HTTP 鍗忚锛岀啛鎮?MVC銆丮VVM 绛夋蹇典互鍙婄浉鍏?WEB 寮€鍙戞鏋?/p>
<p>3銆佹帉鎻″叧绯绘暟鎹簱寮€鍙戣璁★紝鎺屾彙 SQL锛岀啛缁冧娇鐢?MySQL/PostgreSQL 涓殑涓€绉?
br></p>
<p>4銆佹帉鎻?NoSQL銆丮Q锛岀啛缁冧娇鐢ㄥ搴旀妧鏈В鍐虫柟妗?/p>
<p>5銆佺啛鎮?Javascript/CSS/HTML5锛孞Query銆丷eact銆乂ue.js</p>
<p>&nbsp;<br></p>
<p>鍔犲垎椤癸細</p>
<p>澶ф暟鎹紝鏁扮悊缁熻锛屾満鍣ㄥ涔狅紝sklearn锛岄珮鎬ц兘锛屽ぇ骞跺彂銆?/p>
</div>"""
#璧嬪€煎彿鍚庨潰鐨勪笁寮曞彿涓嶆槸娉ㄩ噴
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
    pass
