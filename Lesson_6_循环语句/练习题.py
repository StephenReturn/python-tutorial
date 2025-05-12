
#题目1：输出 9*9 乘法口诀表
'''
1x1=1,
2x1=2, 2x2=4,
3x1=3, 3x2=6, 3x3=9,
4x1=4, 4x2=8, 4x3=12, 4x4=16,
5x1=5, 5x2=10,5x3=15,5x4=20, 5x5=25,
'''

#for, range()
#range的语法：range(a,b)：表示一个大于等于a，小于b的范围。
#举例：输出1到5这5个数字，使用for循环。
# for i in range(1,6):
#     print(i)

#简化版的示例：输出5X1到5X5的乘法口诀表：
# for i in range(1,6):
#     print("5x%d=%d" % (i, 5*i), end=', ')

#假如我要输出以下图形：
'''
#
##
###
####
#####
'''
# for i in range(1,6):
#     for j in range(1,i+1):
#         #第一次进入内层循环的时候，j的范围是1到1（range（1,2））
#         #第二次进入内层循环的时候，j的范围是1到2
#         #……
#         #第五次进入内层循环的时候，j的范围是1到5
#         print("#",end='')
#     print("")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%dx%d=%d, " % (i, j, i*j),end='')
#     print("")
    # 上面这句等效于：print("",end='\n')
    #"\n":换行符
#题目2：有四个数字：1、2、3、4，能组成多少个互不相同的三位数？各是多少？
#假设百位数为a，十位数为b，个位数为c
#互不相同：a!=b and a!=c and b!=c
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a != b and a != c and b != c:
#                 print("%d%d%d" % (a,b,c))


#题目3：给定两个变量a和b，交换它们的值。
# a = 2
# b = 3
#
# #temp:临时变量（temporary）
# temp=a
# a=b
# b=temp
# print(a,b)

#题目4：制作一个简单的计算器。要求：
'''
1. 程序为循环状态，等待用户输入。仅当用户输入为q时退出。
2. 给用户4个输入选择（按数字选择），“1加2减3乘4除”
3. 提示“输入第一个数字”，读取第一个数字；第二个数字的读取同理。
4. 显示结果
'''

#
# while True:
#     num1 = input("输入第一个数字：")
#     if num1 == "q":
#         break
#     num2 = input("输入第二个数字：")
#
#     op = input("请选择操作符：1加2减3乘4除:")
#     if op == "1":
#         print("计算结果是：",int(num1) + int(num2))
#     if op == "2":
#         print("计算结果是：",int(num1) - int(num2))
#     if op == "3":
#         print("计算结果是：",int(num1) * int(num2))
#     if op == "4":
#         if int(num2)==0:
#             print("非法输入！除数不能是0！")
#             continue
#         print("计算结果是：",int(num1) / int(num2))

#题目5： 输入一个整数n，判断其是否是质数,并输出判断结果。
'''
知识点：如果一个数只能被2和它本身整除，则这个数是质数。
'''

n = int(input("Please input a number: "))
is_prime=True

for i in range(3,n):
    if n % i == 0:
        is_prime=False

        print("这个数%d不是质数！" % n)
        break
if is_prime:
    print("这个数%d是质数！" % n)
