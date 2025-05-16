#使用列表打印人名
#同一类型的变量 or 对象组成的集合。
# names = [] #表明names是一个列表。（C语言当中，这个东西叫做“数组”）
names = ["Alice", "Bob", "Cynthia", "Dell"]#是一个由多个字符串组成的列表

#读取列表中的某个元素：通过索引
# first_name = names[0] #通过方括号加里面的数字来表示提取列表的某一个元素。第一个元素的索引永远是“0”。列表从0开始。
# second_name = names[1]
#n个元素组成的列表，最后一个元素的索引是n-1
# last_name = names[3]
# print(first_name)
# print(second_name)
# print(last_name)

#for循环打印出所有元素；
#通过设定一个临时变量name，在每次循环当中遍历列表Names中的每个元素，并赋值给name
# for name in names:
#     print(name)
#这两句是等效的
# for i in range(0,4):
#     print(i)
# for i in range(0,4):
#     print(names[i])
# for i in [0,1,2,3]:
#     print(names[i])


# 使用列表打印，for循环外加一句print
# Range()函数
#使用range创建数值列表
# num_list = [1,2,3,4,5,6]
# num_list = range(1,7)
# for i in num_list:
#     print(i)
#range(1,7)就等效于[1,2,3,4,5,6]
#列表值的访问:使用索引

#列表长度
print(len(names))
#2个列表的拼接：+号
a = [1,2,3]
b = [4,5,6]
# c = a + b
# print(c)

#典型错误：数组越界
# print(a[2])

#字符串转列表:核心是拆分（split()）
# name_str = "Alice Alice Bob Cathy Alice"
# name_list = name_str.split()#"点语法”。
# print(name_list)

# name_str2 = "Alice,Bob,Cathy"
# name_list2 = name_str2.split(',')
# print(name_list2)
#列表转字符串:语法是"分隔符.join(列表）"
# name_list_to_str = ' '.join(name_list)#name_list = ['Alice', 'Bob', 'Cathy']
# print(name_list_to_str)


#统计某个元素在列表中出现的次数：list.count()
# print(name_list2.count("Alice"))
# #列表的长度：
# print(len(name_list))



names = ["Alice", "Bob", "Cynthia", "Dell"]
#list.remove():去掉列表中的某个元素
# names.remove("Bob")
# print(names)


# list.insert(index, obj):在指定位置插入元素
# names.insert(0,"Stephen")
# print(names)

# list.pop(index=-1):删除(默认从最后一个元素开始往前删除）
# names.pop()
# names.pop()
# print(names)


# list.reverse()：列表反转——排列顺序完全颠倒
# names.reverse()
# print(names)

# list.sort():排序
nums = [1,5,3,6,4,2,10,18]
nums.sort(reverse=True)
print(nums)

#对数字列表进行统计计算（max，min，sum）
print(max(nums))
print(min(nums))
print(sum(nums))

#列表表达式（含平方操作）
#集合的概念
#列表切片
'''
2~4
1到末尾
开头到4
最后3个元素
切片的遍历
'''
# ?names = ["Alice", "Bob", "Cynthia", "Dell"]
print(names[-3:])
#列表的操作：添加、删除
#列表的复制（重要概念：值拷贝、引用拷贝） -- 引申：print(id(var))打印内存地址
#元组：不可变的列表
#元组用圆括号表示
#元组的遍历
#元组的重新赋值（整体改变）