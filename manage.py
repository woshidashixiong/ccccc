python获取文件的编码类型

可以使用 `chardet` 模块来获取文件的编码类型。以下是一个示例代码：

```python
import chardet

with open('file.txt', 'rb') as f:
    result = chardet.detect(f.read())

print(result['encoding'])
```

其中，`file.txt` 是要获取编码类型的文件名。`chardet.detect()` 函数会返回一个字典，其中包含了文件编码类型的信息。我们可以通过访问字典的 `encoding` 键来获取文件的编码类型。
