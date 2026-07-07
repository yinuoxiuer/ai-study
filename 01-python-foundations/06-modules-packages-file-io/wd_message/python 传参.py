# 2026年01月23日14时52分25秒
# xxx@qq.com
import sys
print(type(sys.argv))
print(sys.argv)
def write_hello(file_path):
    file=open(file_path,"w+",encoding="utf-8")
    file.write(("hello"))
    file.close()
if __name__ == '__main__':
    write_hello(sys.argv[1])

