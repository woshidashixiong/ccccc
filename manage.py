实战面试题：如何读取大文件，内存只有2G,文件有5G

在内存只有2G的情况下，无法一次性将5G的文件读入内存中。
但可以逐行或逐块读取文件内容，处理完后再读取下一行或下一块。
以下是一些读取大文件的方法

1. 逐行读取文件

```python
with open('large_file.txt', 'r') as f:
    for line in f:
        # 处理每一行数据
```

2. 逐块读取文件

```python
with open('large_file.txt', 'r') as f:
    while True:
        chunk = f.read(1024)  # 每次读取1024字节
        if not chunk:
            break
        # 处理每一块数据
```

3. 使用生成器函数逐行读取文件

```python
def read_large_file(file_path):
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line

for line in read_large_file('large_file.txt'):
    # 处理每一行数据
```

以上方法可以有效地减少内存的使用，但是需要注意的是，逐行或逐块读取文件会增加程序的运行时间。如果需要对大文件进行复杂的处理，可以考虑使用多线程或多进程来加速处理过程。
