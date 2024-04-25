
Python被严重低估的库decorator，装饰器之神！

这个库可以帮你做什么呢 ？

其实很简单，就是可以帮你更方便地写python装饰器代码，更重要的是，它让 Python 中被装饰器装饰后的方法长得更像装饰前的方法。

有了这个库，再也不用手写那嵌套了一层又一层的装饰器了，看着就糟心

# 下面是一个基本的装饰器deco的写法
from decorator import decorator

@decorator
def deco(func,*args,**kw):
    print("func before my do")
    func(*args,**kw)
    print("func after my do")

@deco
def myfunc():
    print("do my func")

myfunc()

输出如下：

func before my do
do my func
func after my do



# 带参数的装饰器的写法
@decorator
def deco1(func,name=None,*args,**kw):
    print("func before my do",name)
    func(*args,**kw)
    print("func after my do")

@deco1(name="name-1")
def myfunc():
    print("do my func")

myfunc()

输出：

func before my do name-1
do my func
func after my do


怎么样，是不是超级简单，心动不如行动，用起来吧，兄弟！










































