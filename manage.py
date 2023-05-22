有的时候我们使用pip下载包的时候，会觉得下载速度十分慢，那是因为在默认情况下，pip使用的国外的源，想要下载速度快点的话，就需要把源换成国内的源。

推荐国内源有以下几种：
阿里云：http://mirrors.aliyun.com/pypi/simple/
豆瓣：http://pypi.douban.com/simple/
清华：https://pypi.tuna.tsinghua.edu.cn/simple/
  
  
查看当前pip源 pip config list
global.index-url='http://pypi.douban.com/simple/'
global.timeout='6000'
global.trusted-host='pypi.douban.com'

永久更改pip源
pip config set global.index-url 源地址

临时跟换
pip install <包名> -i https://mirrors.tools.huawei.com/pypi/simple
