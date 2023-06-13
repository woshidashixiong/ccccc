!=和is not运算符的区别？


!=如果两个变量或对象的值不相等，则返回true。

is not是用来检查两个对象是否属于同一内存对象。


li1 = [1,2,3]
li2 = [1,2,3]

li1 != li2
>False

lst1 is not lst2
>True
