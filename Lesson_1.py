#命令行运行python：“开始菜单”
#命令行中，回车键就表示执行当前行的代码。
#表示“包含关系”的符号，一定要成对出现。比如：
#() [] {} "" <>

a = "wang xi"
b = "shi yun"


print("Hello %s and %s!" % (a,b))
print("hello world!")
#%d:digital, 数值型。
#%s:string, 字符串型
# print("I'm %d years old." % age)
custom_input = input() #默认输入的全是字符型
if custom_input == "1":
    age = 30
    print("I'm %d years old" % age)
else:
    age = 20
    print("I'm %d years old" % age)