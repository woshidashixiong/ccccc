
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
