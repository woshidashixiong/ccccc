很多人知道处理时间用datetime，却不知道Pendulum
对于那些在 python 中处理日期时间时会感到沮丧的人来说，Pendulum 很适合你
Pendulum是一个Python日期时间库，它提供了更简单的接口和更好的功能，以便在Python中处理日期和时间。
它是一个开源项目，可以在GitHub上找到它的源代码和文档。
Pendulum提供了许多有用的功能，例如时区支持、日期时间计算、日期时间格式化、日期时间解析等。
它还提供了一些方便的方法来处理日期和时间，例如获取当前日期时间、获取日期时间差等。
Pendulum可以与Python 2.7和Python 3.x一起使用，并且可以在Linux、Mac和Windows上安装和使用。

1. 创建一个Pendulum对象

```python
import pendulum

dt = pendulum.datetime(2021, 9, 30, tz='Asia/Shanghai')
print(dt)
```

输出：

```
2021-09-30T00:00:00+08:00
```

2. 获取当前时间

```python
now = pendulum.now()
print(now)
```

输出：

```
2021-10-01T10:00:00.000000+00:00
```

3. 时区转换

```python
dt = pendulum.datetime(2021, 9, 30, tz='Asia/Shanghai')
dt_utc = dt.in_timezone('UTC')
print(dt_utc)
```

输出：

```
2021-09-29T16:00:00+00:00
```

4. 时间加减

```python
dt = pendulum.datetime(2021, 9, 30, tz='Asia/Shanghai')
dt_plus_one_day = dt.add(days=1)
print(dt_plus_one_day)
```

输出：

```
2021-10-01T00:00:00+08:00
```

5. 时间格式化

```python
dt = pendulum.datetime(2021, 9, 30, tz='Asia/Shanghai')
print(dt.to_iso8601_string())
print(dt.format('YYYY-MM-DD HH:mm:ss'))
```

输出：

```
2021-09-30T00:00:00+08:00
2021-09-30 00:00:00
```

6. 时间差

```python
dt1 = pendulum.datetime(2021, 9, 30, tz='Asia/Shanghai')
dt2 = pendulum.datetime(2021, 10, 1, tz='Asia/Shanghai')
diff = dt2 - dt1
print(diff.in_days())
```

输出：

```
1
```

7. 时间比较

```python
dt1 = pendulum.datetime(2021, 9, 30, tz='Asia/Shanghai')
dt2 = pendulum.datetime(2021, 10, 1, tz='Asia/Shanghai')
print(dt1 < dt2)
print(dt1 == dt2)
```

输出：

```
True
False
```






谷歌浏览器历史版本

https://googlechromelabs.github.io/chrome-for-testing/
