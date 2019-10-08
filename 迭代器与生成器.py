

'''

概念：可以直接用于for循环的对象统称为可迭代对象（Iterable）
     可直接 用于for循环的对象有：list,tuple,dict,set,String等
     注意：可以使用isinstance()函数判断一个对象是否是Iterable对象
'''
from collections import Iterable
#例如查看 list列表是否是一个可迭代对象
print(isinstance(['a','b'],Iterable))
#例如查看 list是否是一个字符串
print(isinstance('sdff',str))

#如果使用for循环来添加元素比较麻烦
li1 = []
for x in range(1,11):
    li1.append(x * x)
print('li1 = ',li1)
#使用列表生成式生成列表
li2 = [x * x for x in range(1,11)]
print('li2 = ',li2)
#使用列表生成式生成列表 for后面添加判断，只有当 判断符合值的时候 才会进行for前面的运算
li3 = [x * x for x in range(1,11) if x % 2 ==0]
print('li3 = ',li3)

#使用双层for生成全排列
li4 = [m + n for m in 'abc' for n in '123']
print('li4 = ',li4)

'''
生成器：一边循环一边推导的机制称为生成器（generator）,我们在循环遍历的时候不断推导后面的值
所有列表数据都是存放在内存中的，受到内存的限制，列表的内容是有限的!

创建生成器：修改列表生成式，将列表的生成式[]改为()
'''
li4 = (x * x for x in range(1,11) if x % 2 ==0)#这就是一个列表生成式

'''
生成器的特点： 可以通过next()函数将得到generator的下一个值
原理：generator保存的是算法，每次调用next()就计算生成器下一个元素的值，直到抛出StopIteration 异常

当所有元素拿出来之后再运行就会报StopIteration 异常
'''
print(next(li4))
print(next(li4))
print(next(li4))
print(next(li4))
'''
推导的算法比较复杂，用列表生成式for循环无法实现的时候可以选择使用函数生成式

如果想要让一个函数变成生成器，只需要将函数的return 改为yield
'''
#普通函数
def func():
    print("aaaaaaaaaaaaa")
    return '哈哈'
strs = func()#普通函数
print('strs = ',strs)
'''
如果函数变成一个生成器函数以后，在每次执行next（）的时候，遇到yield语句返回，如果再次执行next(),会从上次返回的yield语句处继续执行
遇到yield中断，再继续执行没有遇到yield会报错StopIteration
'''
#函数生成器
def funcYield():
    yield 0
    print("aaaaaaaaaaaaa")
    yield 1
    print("bbbbbbbbbbbbbbbbb")
    yield 2
    print("ccccccccccccccccccccc")
    yield 3
    print("ddddddddddddddddddddddddddd")
    yield '哈哈'
strsYield = funcYield()#此时这个函数得到的是一个生成器
print('strsYield = ',type(strsYield))
print('next(strsYield) = ',next(strsYield))#此时函数调用next函数就运行到 yield 0的位置，如果我下面再进行调用的话，就从打印aaaaaaaaaaaaa开始运行
print('next(strsYield) = ',next(strsYield))#此时函数调用next函数就运行到 yield 1的位置，如果我下面再进行调用的话，就从打印bbbbbbbbbbbbbbbbb开始运行

"""
斐波拉契数列，函数版
"""

def func(count):
    index = 0
    x, y = 0, 1
    while index < count:
        print(y)
        x, y = y, x + y
        index += 1
func(5)
print('函数版的结束.......................')
"""
斐波拉契数列，生成器版
"""

def func(count):
    index = 0
    x, y = 0, 1
    while index < count:
        yield y
        x, y = y, x + y
        index += 1
g = func(5)
for i in g:
    print(i)
print('生成器版的结束.......................')
'''
for循环遍历的时候拿不到generator的return的值
'''
def func(count):
    index = 0
    x, y = 0, 1
    while index < count:
        yield y
        x, y = y, x + y
        index += 1
    return '哈哈你好啊！'
g = func(5)
for i in g:
    print(i)
print('for循环遍历没有拿到return的值.......................')
'''
如果想使用循环遍历的时候拿到generator的return的值，必须捕获StopIterator异常
返回值包含在错误的 对象的value属性中
'''
g = func(5)
while 1:
    try:
        ret = next(g)
        print(ret)
    except StopIteration as e:
        print('返回值  = ',e.value)
        break
print('while循环遍历拿到return的值结束.......................')





