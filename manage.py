====================================================================================
Python是一种非常流行的编程语言，因为它非常适合数据科学和机器学习。在数据科学和机器学习中，可视化数据是非常重要的一部分，因为它可以帮助我们更好地理解数据。Python有很多可视化库，其中一个非常有用的库是HiPlot。

HiPlot是一个用于交互式高维数据可视化的Python库，它可以帮助我们更好地理解数据并找到数据中的模式。HiPlot可以用于可视化高维数据集，例如深度学习模型的输出、超参数搜索的结果或其他复杂数据集。HiPlot的主要功能包括：

1. 可视化高维数据集：HiPlot可以将高维数据转换为三维空间中的可视化图形，使我们可以更好地理解数据。

2. 交互式探索：HiPlot允许我们交互式地探索数据，例如缩放、旋转和选择数据点。

3. 自定义图形：HiPlot允许我们自定义图形，例如添加标签、颜色和形状。

4. 支持多种数据格式：HiPlot支持多种数据格式，例如JSON、CSV和Pandas DataFrame。

接下来，我们将介绍如何使用HiPlot可视化高维数据集。

安装HiPlot

要使用HiPlot，我们需要先安装它。可以使用pip在命令行中安装HiPlot：

```
pip install hiplot
```

导入HiPlot

在Python中导入HiPlot非常简单：

```python
import hiplot as hip
```

创建HiPlot图形

要创建HiPlot图形，我们需要将数据转换为HiPlot格式。HiPlot格式是一个字典，其中键是数据的名称，值是数据的值。例如，以下是一个包含三个数据点的HiPlot格式数据：

```python
data = [
    {'x': 1, 'y': 2, 'z': 3},
    {'x': 4, 'y': 5, 'z': 6},
    {'x': 7, 'y': 8, 'z': 9}
]
```

要创建HiPlot图形，我们可以使用hip.Experiment类。以下是一个简单的例子：

```python
exp = hip.Experiment()
exp.display_data(data)
```

这将创建一个HiPlot图形，其中x、y和z轴分别表示数据点的x、y和z值。

自定义HiPlot图形

我们可以使用HiPlot的许多选项来自定义HiPlot图形。以下是一些常用的选项：

1. 颜色：我们可以使用颜色选项来为数据点添加颜色。例如，以下是一个将数据点按x值着色的例子：

```python
exp = hip.Experiment()
exp.display_data(data, color='x')
```

2. 标签：我们可以使用标签选项为数据点添加标签。例如，以下是一个将数据点按其索引标记的例子：

```python
exp = hip.Experiment()
exp.display_data(data, label='index')
```

3. 形状：我们可以使用形状选项为数据点添加形状。例如，以下是一个将数据点按其y值形状化的例子：

```python
exp = hip.Experiment()
exp.display_data(data, shape='y')
```

交互式探索HiPlot图形

HiPlot允许我们交互式地探索数据。以下是一些常用的交互式选项：

1. 缩放：我们可以使用鼠标滚轮缩放HiPlot图形。

2. 旋转：我们可以使用鼠标左键旋转HiPlot图形。

3. 选择：我们可以使用鼠标右键选择数据点。

总结

HiPlot是一个非常有用的Python库，它可以帮助我们可视化高维数据集。HiPlot可以用于可视化深度学习模型的输出、超参数搜索的结果或其他复杂数据集。HiPlot的主要功能包括可视化高维数据集、交互式探索、自定义图形和支持多种数据格式。要使用HiPlot，我们需要先安装它，然后将数据转换为HiPlot格式，并使用hip.Experiment类创建HiPlot图形。我们可以使用HiPlot的许多选项来自定义HiPlot图形，并使用鼠标交互式地探索数据。


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




