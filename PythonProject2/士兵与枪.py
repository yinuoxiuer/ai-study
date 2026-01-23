# 2026年01月21日13时18分48秒
# xxx@qq.com
from tkinter import mainloop


class gun:
    def __init__(self,module):
     self.module = module
     self.bullet_count = 0
    def add_bullet(self,count):
        self.bullet_count += count
        print("装填子弹,子弹数为%d"%count)
    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹了")
        else:
            print("发射子弹")
            self.bullet_count -= 1
            print("剩余子弹数%d"%self.bullet_count)
class soldier:
    def __init__(self,name,gun=None):
        self.name = name
        self.gun = gun
    def fire(self):
       if self.gun == None:
           print("没有枪")
           return
       else:
        self.gun.shoot()
if __name__ == '__main__':
  ak47 = gun("AK47")
  ak47.add_bullet(5)
  xusandong = soldier("许三多")
  xusandong.fire()
  xusandong.gun = ak47
  xusandong.fire()




