python获取当前系统用户名和主机名

获取用户名
import getpass
print(getpass.getuser())
# 输出 root

import os
print(os.getlogin())
# 输入root


获取主机名
import platform
print(platform.node())
# 输出 DESKTOP-LU87hD6
    
