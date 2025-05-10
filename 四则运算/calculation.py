#python中的加减乘除


'''
加：+
减；-
乘：*
除：/
余：%
整除：//
'''

a = 3
b = 4
add = a+b
print("a+b= %d" % (add))
sub = b-a
print("b-a= %d" % (sub))
multiplex = a*b
print("a * b = %d" % multiplex)
print("a * b =", multiplex)
devide = a/b
print("a/b=", devide)
print("a/b=%d" %devide)
#求余：%
mod = a % b
print("a除以b的余数：", mod)
#整除：//
print("a被b整除：", a//b)


#eval():python的一个系统函数，可以把字符串形式的加减乘除进行运算。
add_string = "3+4"
print(eval(add_string))

#Python是一门动态语言，具有“运行时”机制。
#运行时机制：各个变量到底是什么类型，要到代码跑起来之后才知道。也就是说定义变量的时候，可以不指定它的类型。
#静态语言（C，C#，C++），定义变量的时候必须指明其类型，否则会报错。




#
# name = "Stephen"
# print("Hello %s, this is Jacob." % name)
# print("Hello %s, this is Jacob.", name)



#我在前面双引号字符串输出之后，直接连接逗号后的变量。
# print("a+b=", a+b)
# print("%d %d" % (b, a))
# print(a)






#课后作业：设计一个摄氏度转换为华氏度的小程序。
'''
用户输入一个数字，利用公式进行计算出对应的华氏度，并用print函数输出。
摄氏度转华氏度的公式：
摄氏度×9/5+32=华氏度
知识点：
print（）
四则运算
if-else
'''


