1.从本地将文件传输到服务器
scp 【本地文件的路径】 【服务器用户名】@【服务器地址】:【要存放文件的路径】

scp /usr/local/tools/test.png root@192.168.1.1:/usr/local/tools/

2.从本地将文件夹传输到服务器
scp -r 【本地文件的路径】 【服务器用户名】@【服务器地址】:【要存放文件夹的路径】

scp -r /usr/local/tools/test root@192.168.1.1:/usr/local/tools

3.将服务器上的文件传输到本地
scp 【服务器用户名】@【服务器地址】:【服务器上存放文件的路径】 【本地文件的路径】

scp root@192.168.1.1:/usr/local/tools/111.png /usr/local/tools

4.将服务器上的文件夹传输到本地
scp -r 【服务器用户名】@【服务器地址】:【服务器上存放文件的路径】【本地文件的路径】

scp -r root@192.168.1.1:/data/wwwroot/default/test /
