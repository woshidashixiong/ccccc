题目004：假设你使用的是官方的CPython，说出下面代码的运行结果。

a, b, c, d =1, 1, 1000, 1000
print(a is b, c is d)

def func():
    e = 1000
    f = 1000
    print(e is f, e is d)
    g = 1
    print(g is a)

func()

True False
True False
True

上面代码中a is b的结果是 True 但c is d的结果是 False,这一点的确让人费解。CPython解释器出于性能优化的考虑,把频繁使用的
整数对象用一个叫 small_ints 的对象池缓存起来造成的。 small_ints 缓存的整数值被设定为[-5,256】这个区间,也就是说,在任何引
用这些整数的地方,都不需要重新创建int 对象,而是直接引用缓存池中的对象。如果整数不在该范围内,那么即便两个整数的值相同,
它们也是不同的对象。
