函数如下：

def changeInt(number2):
    number2 = number2 + 1
    print("changeInt: number2=",number2)

number1 = 2
changeInt(number1)
print("number:",number1)

打印结果哪项是正确的（ B ）

A changeInt: number2= 3 number: 3
B changeInt: number2= 3 number: 2
C number: 2 changeInt: number2= 2
D number: 2 changeInt: number2= 3


=====================================
Python HummingBird库是一个高效的机器学习库，它可以将训练好的机器学习模型转换为高性能的代码，以便在边缘设备上进行推理。HummingBird库可以将模型转换为多种格式，包括C++、CUDA和ONNX等，这使得它非常适合在嵌入式设备、移动设备和Web应用程序中使用。

HummingBird库的主要特点是其高效性和可扩展性。它使用了一种称为“代码生成”的技术，该技术可以将模型转换为高性能的代码。这些代码可以在边缘设备上运行，从而实现快速的推理。此外，HummingBird库还支持多种硬件加速器，包括GPU、FPGA和ASIC等，这使得它可以在不同类型的设备上进行优化。

HummingBird库还提供了一些高级功能，例如自动微分和模型量化。自动微分是一种将模型转换为可微分函数的技术，这使得它可以使用梯度下降等优化算法进行训练。模型量化是一种将浮点数模型转换为低精度整数模型的技术，这可以减少模型的存储空间和计算量，从而提高推理速度。

HummingBird库的使用非常简单，只需要几行代码就可以将模型转换为高性能代码。以下是一个使用HummingBird库的简单示例：

```python
import hummingbird.ml as hb

# Load a trained PyTorch model
model = torch.load("model.pt")

# Convert the model to a C++ backend
cpp_model = hb.convert(model, "cpp")

# Save the C++ model
cpp_model.save("model.cpp")
```

在这个例子中，我们首先加载了一个训练好的PyTorch模型，然后使用HummingBird库将其转换为C++后端。最后，我们将C++模型保存到磁盘上。

总之，Python HummingBird库是一个非常有用的机器学习库，它可以将训练好的模型转换为高性能的代码，以便在边缘设备上进行推理。它具有高效性、可扩展性和多种硬件加速器支持等特点，可以满足不同场景下的需求。如果您需要将机器学习模型部署到边缘设备上，请考虑使用Python HummingBird库。

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
