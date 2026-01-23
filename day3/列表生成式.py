# 2026年01月17日22时59分20秒
# xxx@qq.com
generate_list=[j for i in range(10) for j in range(i)]
print(generate_list)
generate_list=[[col*row for col in range (10)] for row in range (10)]
print(generate_list)
generate_list1=[j for x in generate_list for j in x]
print(generate_list1)
generate_list2=[x for x in range(10) if x%2==0]
print(generate_list2)
generate_list3 =[x if x%2==0 else x**2 for x in range(10)]
print(generate_list3)