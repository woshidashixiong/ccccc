按照题目要求写出对应的装饰器。
要求：有一个通过网络获取数据的函数（可能会因为网络原因出现异常），写一个装饰器让这个函数在出现指定异常时可以重试指定的次数，并在每次重试之前随机延迟一段时间，最长延迟时间可以通过参数进行控制。



from functools import wraps
from random import random
from time import sleep


def retry(*, retry_times=3, max_wait_secs=5, errors=(Exception, )):

    def decorate(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(retry_times):
                try:
                    return func(*args, **kwargs)
                except errors:
                    sleep(random() * max_wait_secs)
            return None

        return wrapper

    return decorate


