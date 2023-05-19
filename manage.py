#使用%或者format在变量多的时候一不小心就搞乱了位置，还得仔细的检查，用f-string就不用担心这些问题,而且很直观便于阅读理解
# f-string，亦称为格式化字符串常量（formatted string literals），是Python3.6新引入的一种字符串格式化方法
# 主要目的是使格式化字符串的操作更加简便。f-string在形式上是以 f 或 F 修饰符引领的字符串（f’xxx’ 或 F’xxx’），以大括号 {} 标明被替换的字段

name = "xiaotian"
age = 10
print(f"my name is {name},age {age}")
'''
输出
my name is xiaotian,age 10
'''


#  还可以填入表达式或调用函数，Python会求出其结果并填入返回的字符串内：
print(f" 1 + 1 = {1+1}")
'''
输出
 1 + 1 = 2
'''

# f-string还可用于多行字符串
a,b,c = 1,2,3
s = f'''
 a is { a }
 b is { b }
 c is { c }
'''
print(s)
'''
输出
 a is 1
 b is 2
 c is 3
'''
