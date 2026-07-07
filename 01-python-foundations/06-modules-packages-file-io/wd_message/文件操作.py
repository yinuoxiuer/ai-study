# 2026年01月22日20时59分22秒
# xxx@qq.com
def open_read():
   file=open("file1","r",encoding="utf-8")
   text=file.read()
   print(text)
   file.close()
def open_rw():
   file=open("file3","r+",encoding="utf-8")
   text=file.read()
   print(text)
   file.write("read write")
   file.close()
def open_write():
   file=open("file3","w",encoding="utf-8")
   file.write("study hard")
def open_append():
   file=open("file3","a",encoding="utf-8")
   file.write("hello world")
def use_raedline():
   file=open("file3")
   while True:
       text=file.readline()
       if not text:#最后是一个空字符串
           break
       print(text)
   file.close()

if __name__ == '__main__':
    # open_read()
    # open_rw()
    # open_write()
    # open_append()
    use_raedline()