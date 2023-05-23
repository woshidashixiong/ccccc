python性能分析工具cProfile,推荐给大家

cProfile 是 python 代码调优的一种工具，它能够统计在整个代码执行过程中，每个函数调用的次数和消耗的时间。

# test1.py
import time

def a():
    time.sleep(1)


def b():
    time.sleep(2)


def main():
    a()
    b()
    time.sleep(5)

if __name__ == "__main__":
    # 脚本里使用
    # import cProfile
    # cProfile.run("main()")
    main()
    
两种使用方式

命令行使用
python -m cProfile test1.py (-s ziduan)
脚本里使用
import cProfile
cProfile.run("main()")

输出解释
 9 function calls in 8.027 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.027    8.027 test1.py:1(<module>)
        1    0.000    0.000    8.027    8.027 test1.py:11(main)
        1    0.000    0.000    1.006    1.006 test1.py:3(a)
        1    0.000    0.000    2.006    2.006 test1.py:7(b)
        1    0.000    0.000    8.027    8.027 {built-in method builtins.exec}
        3    8.027    2.676    8.027    2.676 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

共有 9 次函数调用，耗时8.027秒。

ncalls 函数的被调用次数 

tottime 函数总计运行时间，除去函数中调用的函数运行时间 

percall 函数运行一次的平均时间，等于tottime/ncalls 

cumtime 函数总计运行时间，含调用的函数运行时间 

percall 函数运行一次的平均时间，等于cumtime/ncalls 

filename:lineno(function) 函数所在的文件名，函数的行号，函数名
  
  
