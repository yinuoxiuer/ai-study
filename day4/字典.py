# 2026年01月18日20时10分31秒
# xxx@qq.com
# xiaoming_dict = {
#     'name': '小明',
#     'age': 18,
#     'height': 1.75,
#     'is_male': True,
#     'hobbies': ['football', 'swimming', 'programming'],
#     'address': {
#         'province': '北京',
#         'city': '北京'
#     }
# }
# print(id(xiaoming_dict))
# xiaoming_dict["father"]="god"
#
# print(xiaoming_dict["father"])
# print(id(xiaoming_dict))
# print(xiaoming_dict.pop("name"))
# print(xiaoming_dict)
# temp_dict = {"name":"小王", "age": 19}
# xiaoming_dict.update(temp_dict)
# for i in xiaoming_dict:
#     print(f"{i} : {xiaoming_dict[i]}")
#     print("",end="\n")
#     print(i , xiaoming_dict[i])
# for k in xiaoming_dict.items():
#         print(k)
# for k,v in xiaoming_dict.items():
#     print(f"{k},{v}")
test_dict={1:1,2:2,3:3}
print(id(test_dict))
test_dict={1:1,2:2,3:3}
print(id(test_dict))
test_dict.setdefault("name","小明")#对已经存在的key及其value不做修改
print(test_dict)
test_dict["age"]=18
print(test_dict)