# 2026年01月21日12时36分23秒
# xxx@qq.com
# 房子依赖于家具，所以先设计家具
class house_itemm:
    def __init__(self, name, area):
        self.name = name
        self.area = area
    def __str__(self):
        return "%s的面积是%.2f平方米" % (self.name, self.area)
if __name__ == '__main__':
    bed=house_itemm("席梦思", 4)
    chest=house_itemm("衣柜", 2)
    table=house_itemm("餐桌", 1.5)
    print(bed)
    print(chest)
    print(table)
class house_type:
    def __init__(self,house_type,area,item_list):
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.item_list=item_list
    def __str__(self):
        return "%s户型,总面积%.2f平方米,剩余面积%.2f平方米,家具列表:%s" % (self.house_type,self.area,self.free_area,self.item_list)
    def add_item(self,item:house_itemm):#冒号后面是注解
        if item.area>self.free_area:
            print("家具面积过大，无法添加")
            return
        else:
            self.item_list.append(item.name)#也可以放对象
            self.free_area-=item.area
            print("添加%s成功" % item.name)
            print("当前面积为%.2f平方米" % self.free_area)
if __name__ == '__main__':
    my_house=house_type("两室一厅",30,[])
    print(my_house)
    bed = house_itemm("席梦思", 4)
    chest = house_itemm("衣柜", 2)
    table = house_itemm("餐桌", 1.5)
    my_house.add_item(bed)
    my_house.add_item(chest)
    my_house.add_item(table)
    print(my_house)