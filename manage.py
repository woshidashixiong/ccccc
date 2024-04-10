
======================================================
下面对 strs 和 list 的值输出正确的是( C D )

def changeList(li):
    li.append("end")
    print("list",li)

strs = ["1","2"]
changeList(strs)
print("strs",strs)

A strs [‘1’,‘2’] 
B list [‘1’,‘2’]
C list [‘1’,‘2’,’end’] 
D strs [‘1’,‘2’,’end’]

==========================================================
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(100) # 100 控制最大线程数


def job(i):
    print(f"do job {i}")
    return i

futuers = []
for i in range(10):
    fu = pool.submit(job,i) # i为job函数参数
    futuers.append(fu)

pool.shutdown(True) # True阻塞住等全部线程执行完，再关闭线程池
for fu in futuers:
    # 获取线程返回值，若线程执行异常，则打印线程异常信息
    try:
        result = fu.result()
    except Exception as e:
        print(traceback.format_exc())


=====================================================================
python Queue,multiprocessing.Queue,multiprocessing.Manager().Queue()三种消息队列的区别
import Queue
#用于线程间的消息队列

from multiprocessing import Queue
# 用于子进程间的消息队列

from multiprocessing import Manager,Pool
msg_q = Manager.Queue()
用于进程池pool的进程之间的消息队列，由一个独立的python子进程管理该消息队列

=======================================================================
from datetime import datetime

# 当前时间，字符串格式
s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# logging
import logging
import os

import colorlog

log = logging.getLogger("test")
log.setLevel(logging.DEBUG)

# 终端输出 Info级别 colorlog 为终端输出加上颜色
sh = logging.StreamHandler()
sh_fmt = colorlog.ColoredFormatter("%(log_color)s%(asctime)s %(levelname)s: %(filename)s[%(lineno)d]: %(message)s")
sh.setFormatter(sh_fmt)
sh.setLevel(logging.INFO)
log.addHandler(sh)

# 文件记录 debug级别
file_handler = logging.FileHandler("222.log",mode="w")
file_handler.setLevel(logging.DEBUG)
file_fmt = "%(asctime)s %(levelname)s: %(filename)s[%(lineno)d]: %(message)s"
file_handler.setFormatter(logging.Formatter(file_fmt,datefmt="%Y-%m-%d %H:%M:%S"))

log.addHandler(file_handler)

log.debug("debug")
log.warning("warning")
log.info("info")
log.error("error")





