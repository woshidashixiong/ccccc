运行下面的代码是否会报错，如果报错请说明哪里有什么样的错，如果不报错请说出代码的执行结果。

class A: 
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

obj = A(1)
obj.__value = 2
print(obj.value)
print(obj.__value)
