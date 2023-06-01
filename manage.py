python print出一个表格

有时候会有些需求在终端输出表格数据给用户展示，这时候就用到了PrettyTable
非常好用，推荐给大家

from prettytable import PrettyTable

table = PrettyTable(["name","age","score"])
table.add_row(["a","15","90"])
table.add_row(["b","17","100"])
print(table)
'''
输出
+------+-----+-------+
| name | age | score |
+------+-----+-------+
|  a   |  15 |   90  |
|  b   |  17 |  100  |
+------+-----+-------+
'''
