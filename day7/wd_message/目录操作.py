# 2026年01月23日12时03分58秒
# xxx@qq.com
import os
from time import strftime
from time import gmtime

def use_rename():
    os.rename("file3","file33")#绝对路径容易出错,双反斜杠用于转义
    os.rename("D:\\PythonProject3\\wd_message\\file33","D:\\PythonProject3\\wd_message\\file3")
def use_dir():
    file_list=os.listdir(".")
    print(file_list)
def change_dir():
    print(os.getcwd())
    os.chdir("dir2")
    print(os.getcwd())
def scan_dir(cur_path,width):
    file_list=os.listdir(cur_path)
    for file in file_list:
        new_path=cur_path+"\\"+file
        print(" "*width+file)
        if os.path.isdir(new_path):
            scan_dir(new_path,width+4)
def use_stat(file_path):
    file_info=os.stat(file_path)
    # 转换时间
    gm_time=gmtime(file_info.st_mtime)
    time_str=strftime("%Y-%m-%d %H:%M:%S", gm_time)
    # 修正：补全 format 参数和括号
    print('size:{}, uid:{}, mode:{:x}, mtime:{}'.format(
        file_info.st_size, 
        file_info.st_uid, 
        file_info.st_mode, 
        time_str
    ))

if __name__ == '__main__':
    # use_dir()
    # os.mkdir("dir2")
    # os.rmdir("dir1")
    # print(os.getcwd())
    # os.chdir("dir2")
    # file4=open("file4","w")
    # change_dir()
    # scan_dir(".",0)
    use_stat("file1")