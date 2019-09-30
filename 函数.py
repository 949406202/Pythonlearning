# -*- coding:utf-8 -*-
#函数调用的时候必须实参顺序一致
def add(name,age):
    return '[%s] 今年 [%d]'%(name,age)
strs = add('zhangsan',15)
print(strs)
#我们在使用关键字函数调用的时候就可以不必须实参顺序一致
def add(age,name):
    return '[%s] 今年 [%d]'%(name,age)
strs = add(name='zhangsan',age=15)
print(strs)

