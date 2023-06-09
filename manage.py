在 Flask 中设置接口超时时间可以通过使用装饰器来实现。具体步骤如下：

1. 导入 `signal` 模块：

   ```python
   import signal
   from functools import wraps
   ```

2. 定义一个装饰器函数，用于设置超时时间：

   ```python
   def timeout(seconds=10, error_message='Timeout'):
       def decorator(func):
           def _handle_timeout(signum, frame):
               raise TimeoutError(error_message)
           @wraps(func)
           def wrapper(*args, **kwargs):
               signal.signal(signal.SIGALRM, _handle_timeout)
               signal.alarm(seconds)
               try:
                   result = func(*args, **kwargs)
               finally:
                   signal.alarm(0)
               return result

           return wrapper

       return decorator
   ```

   这个装饰器函数接受两个参数：`seconds` 表示超时时间，`error_message` 表示超时时抛出的异常信息。

3. 在需要设置超时时间的接口函数上使用装饰器：

   ```python
   @app.route('/api/some_endpoint')
   @timeout(seconds=5)
   def some_endpoint():
       # 接口函数的实现
   ```

   在这个例子中，`some_endpoint` 函数的超时时间被设置为 5 秒。

注意：在使用 `signal` 模块时，需要注意操作系统的限制。在windows操作系统中，`signal` 模块可能无法正常工作。
