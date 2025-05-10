#整数型变量int
#浮点型变量（小数）float
#变量的作用域
#函数
#全局变量
#局部变量
#环境变量



#什么是函数：函数就是用一个名称来代替某段特定功能的代码段。
#def: define
#函数的使用需要：1. 函数的定义。2. 函数的调用
#def：函数的定义部分

#缩进
#python通过缩进来表示包含关系
#一个函数内的所有代码都需要缩进
#缩进的层级代表了关系的层级。

#全局变量
workday = "周四"

def sample_function():
    #age是一个局部变量，因为它是在函数内“临时”定义的
    age = 30
    #d: 输出一个整数型变量。d=digital
    print("I'm %d years old" % age)

    height = 1.658648
    #%f = 输出一个浮点数。f=float.系统默认保留6位小数。
    print("I'm %f meters high." % height)
    #%.2f:保留2为小数输出（四舍五入）。
    print("I'm %.2f meters high." % height)

def greetings():
    print("hello world!")


#函数的调用：使用某个特定的函数
#函数的名称可以任意取。但是同一个文件中的函数不能重名。函数名也不可与系统保留关键字冲突
def print_day():
    print(workday)
    #a是一个局部变量，当离开了该函数，a的生命周期也就结束了，因此无法从函数外访问a这个局部变量。
    a = 3
    print(a)














def print_a():
    b = 555
    print(b)

# print_a()

#函数的参数
def greetings_personA_and_personB(a,b):
    print("hello, %s and %s!" % (a,b))


greetings_personA_and_personB("Wang Xi", "Shi Yun")












##变量需要先定义，再使用
# print("hi, %d" % aaa)







'''
#C语言定义一个函数
int void greetings(){
    print("hello")
}

'''