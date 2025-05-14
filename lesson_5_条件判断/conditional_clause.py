#示例：字符串的比较
str_a = "abc"
str_b = "xyz"
#==：双等号表示“等于”；=：单等号表示“赋值”
if str_a == str_b:
    print("The 2 strings are equal.")
else:
    print("The 2 strings are not equal.")

#数值型的比较。（比较符号的介绍：>,<,==, !=）
# age = 30
# if age != 18:
#     print("Age is not 18 years old.")
#     # print("Teenager.")
# else:
#     print("Adult.")
#顺便介绍一下自加自减符号：+=, -=


#多个条件的检查（and，or等逻辑关系）


#if-else语句
#if-elif-else结构：
age = 70
if age < 5:
    print("Baby.")
elif 5 <= age < 18:
    print("Student.")
elif 18<=age<30:
    print("Young man.")
elif 30<=age<60:
    print("Middle age.")
else:
    print("Senior.")

#布尔表达式（Boolean expression）
#True or False

'''
if-else的语法：
if [条件表达式]为真：
    执行代码。。。
else:
    执行代码。。。
'''
a = True
b = False

#b虽然是False，b==False是一个正确的判断，即“条件表达式为真”。所以执行if后的代码。
if not b:
    print("b 为真。")
else:
    print("b 为假。")

#引入and, or, not的概念
#and：逻辑“与”。当所有条件都为True的时候，输出结果才为true。否则，结果为false。
#or：逻辑“或”。当任意条件为True，结果就是true。只有所有条件都是false的时候，结果才是false。
#not:逻辑“非”。表示对当前结果“取反”。假设a是true，则not a是false。
c = 1
d = 2
if c == 1 or d == 1:
    print("条件满足")
else:
    print("条件不满足")

#多个if和if-else的比较：


#continue和break的介绍（引入循环控制语句）：


#【练习题】设计一个程序，判断输入的数字是奇数还是偶数。
'''
知识点：
1. input（）的运用
2. 使用int()进行强制类型转换
3. 奇数不能被2除尽；偶数可以。（求余运算。）
'''

# condition_a = 1
# condition_b = 2

# if condition_a == condition_b:
    #if后边的语句被执行的根本原因是if的“条件判断”结果为True。