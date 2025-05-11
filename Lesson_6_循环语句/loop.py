#input（）的工作原理 --带着看一下系统的函数提示（官方注释）

# a=input("Give me a new number:")

#while循环
'''
语法规则：
while [条件]为真:
    语句。。。
'''

#continue 和 break语句：
'''
continue的作用：跳过这一轮循环，进入下一轮
break的作用：终止当前循环（跳出--break out）。如果还有外层的循环，则代码会直接跳到外层的循环中。
'''
x = 10
while x < 100:
    y = 200
    while y > 0:
        y = y - 50
        print("y=", y)
        if y == 50:
            print("now y is 50!")
            break
    x = x + 10
    print("x=", x)

# while x < 100:
#     x = x + 10
#
#     if x == 30:
#         print("Now x is 30!")
#         continue
#     if x == 60:
#         break
#     print(x)

#for循环 （代入列表——list的概念）



'''
【练习题】用户输入一个数字，利用公式进行计算出对应的华氏度，并用print函数输出。摄氏度转华氏度的公式：摄氏度×9/5+32=华氏度
要求：循环读取，并判断输入是否在0-100之间。如果超出范围，需报错。
当用户输入q，则退出程序。
'''