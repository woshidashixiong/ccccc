什么是switch语句。如何在Python中创建switch语句？

switch语句是实现多分支选择功能，根据列表值测试变量。

switch语句中的每个值都被称为一个case。

在Python中，没有内置switch函数，但是我们可以创建一个自定义的switch语句。

switch = {
   1: "January",
   2: "February",
   3: "March",
   4: "April"
}
month = int(input())
print(switch.get(month))

> 1
January
