
说一下`namedtuple`的用法和作用

namedtuple又名具名元组，因为普通元组的局限性，不能为元组的数据进行命名，所以我们并不知道一个元组所要表达的意义，
所以python引入了collections.namedtuple这个工厂函数来构造一个带字段名的元组。

namedtuple能够用来创建类似于元祖的数据类型，除了能够用索引来访问数据，能够迭代，还能够方便的通过属性名来访问数据
能够让我们的代码更加的直观更好维护


from collections import namedtuple
Friend =namedtuple("Friend",['name','age','email'])
f1=Friend('giga',38,'gaga@qq.com')
print(f1)  # Friend(name='giga', age=38, email='gaga@qq.com')
print(f1.age) # 38
print(f1.email) # gaga@qq.com
print(f1[0]) # giga
