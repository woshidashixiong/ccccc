python 异常捕获里的“坑”

def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

你觉得调用func会返回哪一个值？
实际上不是1，也不是3，即使try里面有异常也不是2

print(func()) # 输出4

原因是，在try…finally…语句中，因为要保证finally能够执行，所以try,except,else里的return无效

在这里需要小心

