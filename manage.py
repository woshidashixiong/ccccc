python有列表a和b,结构都如下所示:[[x1,y1,x2,y2]],x1,y1表示矩形的左下角坐标，x2,y2表示矩形右上角坐标,这样的矩形有n多个（大数据量），遍历a中每一个矩形，找出b中与其相交的矩形，输出a中矩形index和b中相交矩形的index，怎样用numpy高效率处理

可以使用numpy中的广播和矩阵运算来高效处理

首先，将a和b转换为numpy数组，方便进行矩阵运算。假设a和b分别为：

```
a = [[x1_1, y1_1, x2_1, y2_1], [x1_2, y1_2, x2_2, y2_2], ...]
b = [[x1_1, y1_1, x2_1, y2_1], [x1_2, y1_2, x2_2, y2_2], ...]
```

则可以使用numpy数组的广播功能，将a和b分别扩展成形状为(n,m,4)的数组，其中n和m分别为a和b的长度，4表示每个矩形有4个坐标值。具体实现如下：

```
import numpy as np

a = np.array(a)
b = np.array(b)

a = np.expand_dims(a, axis=1)
b = np.expand_dims(b, axis=0)

a = np.tile(a, (1, len(b), 1))
b = np.tile(b, (len(a), 1, 1))
```

这样，a和b就可以进行矩阵运算了。接下来，可以使用numpy的逻辑运算和索引功能，找出与每个a矩形相交的b矩形。具体实现如下：

```
overlap = np.logical_and(
    np.logical_and(a[:, :, 0] < b[:, :, 2], a[:, :, 2] > b[:, :, 0]),
    np.logical_and(a[:, :, 1] < b[:, :, 3], a[:, :, 3] > b[:, :, 1])
)

result = np.argwhere(overlap)
```

其中，overlap表示a和b的每个矩形是否相交，result为相交的矩形对的索引。例如，result中的一行表示b中第i个矩形与a中第j个矩形相交。

最后，可以将result中的索引转换为b和a中的矩形索引，输出即可。完整代码如下：

import numpy as np
a = [
    [4,6,7,7],
    [3,3,4,4]
]

b = [
    [9,3,10,4],
    [3,2,5,4],
    [4,6,8,7],
    [3,3,7,7]
]

a = np.array(a)
b = np.array(b)

a = np.expand_dims(a, axis=1)
b = np.expand_dims(b, axis=0)

a = np.tile(a, (1, len(b), 1))
b = np.tile(b, (len(a), 1, 1))

overlap = np.logical_and(
    np.logical_and(a[:, :, 0] < b[:, :, 2], a[:, :, 2] > b[:, :, 0]),
    np.logical_and(a[:, :, 1] < b[:, :, 3], a[:, :, 3] > b[:, :, 1])
)

result = np.argwhere(overlap)

for r in result:
    a_index, b_index = r[0], r[1]
    print("a index: {}, b index: {}".format(a_index, b_index))









