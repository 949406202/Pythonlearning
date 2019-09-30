# -*- coding:utf-8 -*-
#函数调用的时候必须实参顺序一致
def add(name,age):
    return '[%s] 今年 [%d]'%(name,age)
strs = add('zhangsan',15)
print(strs)
#我们在使用关键字函数调用的时候就可以不必须实参顺序一致
def add(age,name):
    return '[%s] 今年 [%d]'%(name,age)
strs = add(name='zhangsan',age=15)#在传参的时候我们指定我们所想要传递的参数名字
print(strs)
#默认值参数
def add(name,age=18):
    return '[%s] 今年 [%d]'%(name,age)
strs = add(name='zhangsan')#在传参的时候如果我们没有指定age的时候，就会使用方法定义的默认值
strs = add('lisi',20)#在传参的时候如果我们指定age的时候，就会使用调用者传递的参数
print(strs)

