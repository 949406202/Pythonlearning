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
#默认值参数,定义函数的时候尽量将默认参数写在最后
def add(name,age=18):
    return '[%s] 今年 [%d]'%(name,age)
strs = add(name='zhangsan')#在传参的时候如果我们没有指定age的时候，就会使用方法定义的默认值
strs = add('lisi',20)#在传参的时候如果我们指定age的时候，就会使用调用者传递的参数
print(strs)
#不定长参数，他能处理比当初定义时更多的参数,可以传任意长的参数
def add(name,age,*args):
    print("*args = ",*args,",类型是 = ",type(args))
    return '[%s] 今年 [%d] 岁！！！'%(name,age)
strs = add('lisi',20,"足球",'篮球')#在传参的时候我们可以传任意长的参数
print(strs)
#返回多个值的函数
def add():
    return 1,2
x,y = add()
z = add()
print(x,y)
print('类型是',type(z),"，值为 ：",z)
#匿名函数：lambda表达式
num = lambda x,y:x+y
print('x + y =：',num(5,4))#这里5对应x,4对应y
#函数也是一种 数据，因为我们也可以把函数赋值给一个变量
def add(x,y):
    return x + y
f = add
print('函数也是一种数据的 函数赋值给变量 x + y = ',f(1,2))
#  Map函数，相当于分布式和多线程的函数！他会同时进行把集合中的每个元素传到函数体里面分开处理运行，如果map函数的第二
# 个参数是字符串，那么传给 函数的将是一个个的字符，结果作为新的Iterator返回,返回值为：可迭代对象Iterator
lies = ["abc","123","cbcb",'34']
def add(objects):
    print('objects = ',objects)
    return objects
resa = map(add,lies)#add:函数名，lies:集合，这里是python内部把列表转成集合然后传到函数中的
print(resa)
print("resa = ",list(resa))
# Reduce函数，他的不必须传两个参数，第一个是函数，第二个是集合，和Map的传参形式一样，只是功能差异， 返回值为：可迭代对象Iterator
# 作用是 将前一个值与后一个值累计相加 例如想 计算 1+2+3+4+5等于多少  reduce 是把 1+2 =3计算出来，然后拿着
# 3再和3进行计算 3+3 = 6，然后拿着 6和4计算 6+4 =10，然后拿着10和5相加 10+5 = 15
# 总结：是拿着前两个数值之后再与后面的数字进行相加,想用reduce 必须先导入
'''
        reduce(add,[1,2,3,4,5]) == reduce(add(add(add(add(1,2),3),4),5）)
    
'''
from functools import reduce
nums = [1,2,3,4,5]
def add(x,y):
    return x + y
res = reduce(add,nums)
print('res = ',res)
# map和reduce函数的例子 ，计算字符串 '13543' 的阿拉伯数字  13543
def strToint(s):
    def chrToint(chr):
        return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]
    def f(x,y):
        return x *10 + y
    return reduce(f,map(chrToint,s))

res = strToint('13543')
print("map和reduce综合实例：",res)

# filter 函数，作用是将返回为 True的参数放入列表中返回，False的参数自动过滤，这个函数起到了过滤的作用,
# 传递 参数的形式和MAP和reduce一样的 都是传入函数和 将要被分析的数据，返回值为：可迭代对象Iterator
#举例：例如我们想要找出该列表中的所有奇数的 话可以使用 filter来进行编写代码

listsa = [1,2,3,4,5,6,7,8,9]

def add(num):
    if num % 2 == 0:
        return False
    return True

res = filter(add,listsa)
print('listsa = ',listsa)
print("奇数列表 ：",list(res))
# 需求：删除列表中的空字符串的元素
li2 = ["a","","","    ","  bgm   "]
def add(item):
    return item and item.strip()
res = filter(add,li2)
print("res 去空字符串以后留下的为 ：",list(res))
#上面题的解释
a = ""
if a:#空字符串为 假
    print("False")
else:#只要有字符串为 真
    print("True")
# 变量作用域的 问题，全局作用域和 嵌套作用域
# 1.全局作用域
nums = 0
def fn():
    #在这个函数里面可以放回 nums变量但是如果现在这个函数里面修改nums变量的话就需要声明为全局变量
    #例如：
    #global nums
    nums = 30
    print("数字 nums 的值为 %d"%nums)
fn()
print("在外面来进行打印的话就是 ：%d"%nums)
print("如果去掉 global nums，就会是局部的nums和外面的nums没关系！")

# 2.嵌套作用域
nums = 0
def fn():
    a = 30
    print("没有被嵌套修改之前的a变量值：",a)
    def counts():
        #如果我们现在 想在这个函数里面去修改 外面fn函数里面的 a变量的值得话，我们就需要使用nonlocal
        nonlocal a
        a = 50
        print("修改嵌套后的 a变量的值为 ：",a)
    print("调用内部函数counts。。。。。。")
    counts()#在函数内部调用函数
fn()
