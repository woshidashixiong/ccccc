
=========================================================================================
python多进程的进程池的最大进程数是越多越好吗？


import os,time
import multiprocessing
from multiprocessing import Pool
def work(n):
    print(f"{n} run")
    b = 0
    for i in range(100000):
        b += i
    return b
    

1000个串行work,耗时3.7s

start = time.time()
print("start",start)
for i in range(1000):
    work(i)
end = time.time()
print("end", end,end-start)


1000个并行work, 进程数n跟耗时对比

start = time.time()
print("start", start)
p=Pool(n) #进程池中从无到有创建n个进程,以后一直是这n个进程在执行任务,不填默认为系统cpu核心数 multiprocessing.cpu_count()
res_l=[]
for i in range(1000):
    res=p.apply_async(work,args=(i,))
    res_l.append(res)
p.close()
p.join()
end = time.time()
print("end", end,end-start)

# 串行 3.7
# 1  4.02
# 5  1.15
# 10  1.11
# 20  1.30
# 30  1.64
# 50  2.48
# 100  4.04
# 500  20.49
# 1000  47.89


结论，n的数量并不是越大越好，因为cpu数是固定的，进程开的多cpu也无法被利用，反而开进程的开销大导致效率不减反增，最优值为系统的cpu核心数

============================================================================================================================

python多线程的线程池的最大线程数是越多越好吗？

import os,time
from concurrent.futures import ThreadPoolExecutor
def work(n):
    print(f"{n} run")
    time.sleep(1)
    return n

10w个并行work, 线程数n跟耗时对比

start = time.time()
print("start", start)
threadpool = ThreadPoolExecutor(n) # n控制最大线程数，不是立即开启N个线程，所以此处不消耗时间
res_l=[]
for i in range(100000):
    res= threadpool.submit(work, i)
    res_l.append(res)
threadpool.shutdown(True)
end = time.time()
print("end", end,end-start)


# 5k   21
# 6k   18
# 7k   16
# 8k   14
# 9k   13/13.57/13/13.68
# 1w   12.43/12.34/12.34/12/12
# 2w   10.53/10.67/10.47/10.91
# 3w   12/13/12/13
# 4w   16/16
# 5w   20/22/20
# 10w  /59/64/60/68/57

结论，当并行任务数足够多的时候，线程数并不是越多越好，线程数有一个阈值，该阈值跟电脑性能，任务耗时都有关系，并不是固定的，当前实验阈值1w-3w之间，当开启的线程数超过该阈值，效率反而下降




