
python类变量在多线程下是安全的吗？ /实例变量在多线程下是安全的吗

import threading
import time

class A:
    dic = {}

def aa(i):
    A.dic["vv"] = i
    time.sleep(2)
    print(i,A.dic["vv"])


threads = []

for i in range(3):
    t = threading.Thread(target=aa,args=[i])
    t.start()
    threads.append(t)

for t_obj in threads:
    t_obj.join()



===============================================================================


Python colorlog是一个用于在终端输出彩色日志的Python模块。它可以让你在终端输出带有颜色的日志信息，使得日志信息更加易于阅读和理解。

使用colorlog模块，你可以轻松地将日志信息分为不同的级别，并为每个级别指定不同的颜色。例如，你可以将错误日志信息标记为红色，将警告信息标记为黄色，将调试信息标记为绿色等等。

以下是一个使用Python colorlog模块的示例：

```python
import logging
import colorlog

# 创建一个logger对象
logger = logging.getLogger()

# 创建一个StreamHandler对象
handler = logging.StreamHandler()

# 创建一个ColorFormatter对象
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(message)s',
    log_colors={
        'DEBUG': 'green',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    })

# 将formatter添加到handler中
handler.setFormatter(formatter)

# 将handler添加到logger中
logger.addHandler(handler)

# 设置日志级别为DEBUG
logger.setLevel(logging.DEBUG)

# 输出不同级别的日志信息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

在上面的示例中，我们首先创建了一个logger对象和一个StreamHandler对象。然后，我们创建了一个ColorFormatter对象，并将其添加到handler中。最后，我们将handler添加到logger中，并设置日志级别为DEBUG。

在输出日志信息时，我们可以使用logger对象的不同方法来输出不同级别的日志信息。在这个例子中，我们输出了DEBUG、INFO、WARNING、ERROR和CRITICAL级别的日志信息，并为每个级别指定了不同的颜色。

当我们运行这个程序时，我们将在终端上看到带有颜色的日志信息，使得日志信息更加易于阅读和理解。




===================================================================================================

随机生成一个 100 以内的整数，共有 10 次机会开始游戏，输入猜测的数字。如果猜小了，则提示：猜小了，如果猜大了，则提示：猜大了
猜对了，则提示：猜对了，并且结束游戏，10 次机会用完还没猜对，提示：游戏结束，没有猜到。
import random as rd
 
number = rd.randint(0,100)
for i in range(10):
    choice = int(input("请输入你要猜测的数字："))
    if choice > number:
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print("你猜对了，真棒！")
        print(f'你一共用了{i + 1}次机会')
        break
    print(f'还剩{9 - i}次机会')
else:
    print('游戏结束，你没有猜到')



========================================================================================================
要抓取渲染后的HTML网页，可以使用Selenium的WebDriverWait和ExpectedConditions模块来等待页面加载完成后再获取HTML。




python类变量在多线程下是安全的吗？ /实例变量在多线程下是安全的吗

import threading
import time

class A:
    dic = {}

def aa(i):
    A.dic["vv"] = i
    time.sleep(2)
    print(i,A.dic["vv"])


threads = []

for i in range(3):
    t = threading.Thread(target=aa,args=[i])
    t.start()
    threads.append(t)

for t_obj in threads:
    t_obj.join()



===============================================================================


Python colorlog是一个用于在终端输出彩色日志的Python模块。它可以让你在终端输出带有颜色的日志信息，使得日志信息更加易于阅读和理解。

使用colorlog模块，你可以轻松地将日志信息分为不同的级别，并为每个级别指定不同的颜色。例如，你可以将错误日志信息标记为红色，将警告信息标记为黄色，将调试信息标记为绿色等等。

以下是一个使用Python colorlog模块的示例：

```python
import logging
import colorlog

# 创建一个logger对象
logger = logging.getLogger()

# 创建一个StreamHandler对象
handler = logging.StreamHandler()

# 创建一个ColorFormatter对象
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(message)s',
    log_colors={
        'DEBUG': 'green',
        'INFO': 'white',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    })

# 将formatter添加到handler中
handler.setFormatter(formatter)

# 将handler添加到logger中
logger.addHandler(handler)

# 设置日志级别为DEBUG
logger.setLevel(logging.DEBUG)

# 输出不同级别的日志信息
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

在上面的示例中，我们首先创建了一个logger对象和一个StreamHandler对象。然后，我们创建了一个ColorFormatter对象，并将其添加到handler中。最后，我们将handler添加到logger中，并设置日志级别为DEBUG。

在输出日志信息时，我们可以使用logger对象的不同方法来输出不同级别的日志信息。在这个例子中，我们输出了DEBUG、INFO、WARNING、ERROR和CRITICAL级别的日志信息，并为每个级别指定了不同的颜色。

当我们运行这个程序时，我们将在终端上看到带有颜色的日志信息，使得日志信息更加易于阅读和理解。




===================================================================================================

随机生成一个 100 以内的整数，共有 10 次机会开始游戏，输入猜测的数字。如果猜小了，则提示：猜小了，如果猜大了，则提示：猜大了
猜对了，则提示：猜对了，并且结束游戏，10 次机会用完还没猜对，提示：游戏结束，没有猜到。
import random as rd
 
number = rd.randint(0,100)
for i in range(10):
    choice = int(input("请输入你要猜测的数字："))
    if choice > number:
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print("你猜对了，真棒！")
        print(f'你一共用了{i + 1}次机会')
        break
    print(f'还剩{9 - i}次机会')
else:
    print('游戏结束，你没有猜到')



========================================================================================================
要抓取渲染后的HTML网页，可以使用Selenium的WebDriverWait和ExpectedConditions模块来等待页面加载完成后再获取HTML。


谷歌浏览器历史版本

https://googlechromelabs.github.io/chrome-for-testing/





