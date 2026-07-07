# 2026年01月23日15时30分06秒
# xxx@qq.com
def read_conf():
    file=open("file6","r+",encoding="utf-8")
    text_inf=file.read()
    print(text_inf)
    print(eval(text_inf))
    file.close()
if __name__ == '__main__':
    read_conf()