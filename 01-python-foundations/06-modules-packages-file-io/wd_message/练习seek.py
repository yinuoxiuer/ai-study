# 2026年01月22日21时56分03秒
# xxx@qq.com
import os
def seek_start():
    file=open("file3","r+",encoding="utf-8")
    file.seek(5,0)#汉字是3的整数倍
    text=file.read(5)
    print(text)
def seeek_cur():
    file=open("file3","r+",encoding="utf-8")
    file.seek(0,1)
    text=file.read(3)
    print(text)
def seek_b_cur():
    file=open("file1","rb+")
    file.seek(-10,2)
    b=file.read()
    print(b)
    file.close()
def copy_file():
    file1=open("test.jpg","rb+")
    file2=open("test_copy.jpg","wb+")
    b=file1.read()
    file2.write(b)
    file1.close()
    file2.close()
def modify_file():
    file3=open("test_copy.jpg","rb+")
    file3.seek(10,0)
    c=file3.read(10)
    c_inverted = bytes([255 - x for x in c])
    file3.seek(10, 0)
    file3.write(c_inverted)


if __name__ == '__main__':
    # seek_start()
    # seeek_cur()
    # seek_b_cur()
    # copy_file()
    modify_file()