# 2026年01月22日11时34分16秒
# xxx@qq.com
import test_exception_module

def exception1():
    while True:
        try:
            num=int(input("请输入数字:"))
            break
        except:
            print("输入错误，请输入整数")

def exception2():
    while True:
        try:
            num=int(input("请输入数字:"))
            print(10/num)
            break
        except ValueError:
            print("输入错误，请输入整数")
        except ZeroDivisionError:
            print("除数不能为0")

def exception3():
    while True:
        try:
            num=int(input("请输入数字:"))
            print(10/num)
            break
        except ValueError:
            print("输入错误，请输入整数")
        except Exception as e:
            print(e)

def exception4():
    while True:
        try:
            num=int(input("请输入数字:"))
            print(10/num)
        except ValueError:
            print("输入错误，请输入整数")
        except Exception as result:
            print("未知错误 %s" % result)
        else:
            print("没有错误")
            break
        finally: #不受return影响
            print("无论是否发生异常，都会执行")

def exception5():
    try:
        test_exception_module.test()
    except Exception as e:
        print("错误信息:", e)
        
        # 使用循环找到 traceback 链表的最后一个节点（最底层的错误源头）
        error_trace = e.__traceback__
        while error_trace.tb_next:
            error_trace = error_trace.tb_next
            
        print("报错文件:", error_trace.tb_frame.f_globals["__file__"])
        print("报错行号:", error_trace.tb_lineno)

exception5()