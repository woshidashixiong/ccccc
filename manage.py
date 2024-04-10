
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
