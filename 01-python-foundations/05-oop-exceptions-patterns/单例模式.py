# 2026年01月22日10时04分05秒
# xxx@qq.com
class Musicplayer:
    instance=None
    init_flag = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance



    def __init__(self,name):
        if Musicplayer.init_flag==False:
            print("初始化播放器")
            self.name=name
            Musicplayer.init_flag = True
        else:
            print("播放器已经创建")


if __name__ == '__main__':
    mp1=Musicplayer("七里香")
    mp2=Musicplayer("稻香")
    print(id(mp1))
    print(id(mp2))
    print(mp1.name)
    print(mp2.name)
