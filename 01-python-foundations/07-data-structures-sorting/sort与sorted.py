# 2026年01月25日11时49分47秒
# xxx@qq.com
from operator import itemgetter,attrgetter
my_list="can you see it It is None".split()
print(my_list)
print(sorted(my_list))#默认排序根据ascii码排序
print(sorted(my_list,key=str.lower))
def change_lower(strname: str):
    return strname.lower()
print(sorted(my_list,key=change_lower))
print(my_list)
my_list.sort()
print(my_list)
students_tuples=[("zhangsan",18,"D"),("lisi",19,"C"),("wangwu",17,"B"),("zhaoliu",16,"A")]
print(sorted(students_tuples,key=lambda x:x[1]))
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def __repr__(self):
        return repr((self.name,self.age,self.grade))
if __name__ == '__main__':
    student1=Student("zhangsan",18,"D")
    print(student1)
    students=[Student("zhangsan",18,"D"),Student("lisi",19,"C"),Student("wangwu",17,"B"),Student("zhaoliu",16,"A")]
    print(sorted(students,key=lambda x:x.grade))
    print(sorted(students_tuples,key=itemgetter(0,1)))
    print(sorted(students,key=attrgetter("name")))
    print(sorted(students_tuples,key= lambda x:(x[0],x[1])))
    print(sorted(students, key=attrgetter("name","age")))
    print(sorted(students, key=attrgetter("name", "age"),reverse= True))
    print(sorted(students_tuples, key=lambda x: (x[0], -x[1])))#对第二个元素进行降序，因为是数字
    data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
    # 按照第0个元素（颜色）排序
    # 结果中，虽然两个 blue 排在一起了，但在原列表中先出现的 ('blue', 1) 依然排在 ('blue', 2) 前面
    print(sorted(data, key=itemgetter(0)))
    my_dict={"li":["A",50],"zhang":["F",60],"wang":["C",70],"zhao":["B",80]}
    for i in my_dict.items():
        print(i)
    print(sorted(my_dict.items(),key=lambda x:x[1][1]))
    game_result=[{"name":"zhangsan","score":100,"level":"A"},{"name":"lisi","score":90,"level":"B"},{"name":"wangwu","score":80,"level":"C"},{"name":"zhaoliu","score":70,"level":"D"}]
    print(sorted(game_result,key=lambda x:x["score"]))
    print(sorted(game_result, key=itemgetter("score", "level")))