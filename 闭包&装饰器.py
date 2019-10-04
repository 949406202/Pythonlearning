

'''
闭包概念：第一在函数内部的函数，并且使用外层函数的变量，
他是函数里面包含函数，然后将函数返回赋值给一个变量，这个变量就代表闭包也就是一个内部函数！
例如：
'''
a = 10
def func():
    b = 20
    def funcIner():
        c = 30
        return b
    return funcIner
f2 = func()
print('闭包产生的值 ： ',f2())

'''
装饰器：他是一个闭包，把一个函数作为一个参数然后返回一个替代版函数，本质上就是一个返回函数的函数！
例如：简单装饰器，在不修改原函数的情况下 打印aaaaaa之前我想打印一串*****************
'''
def func():
    print("aaaaaaaaaaaaaaaaaaa")
def warning(f):
    def inners():#返回的这个函数就是替代版本
        print("*****************************")
        f()
    return inners
#调用
d = warning(func)
d()#相当于调用了inner函数
func = warning(func)
func()#等同上面的调用

'''
复杂的装饰器：带参数的
'''
def funcs(a,b):
    return a + b

def warpper(f):
    def inner(a,b):
        if a < 0:
            a = 1
        if b < 0:
            b = 1
        return f(a,b)
    return inner
funcs = warpper(funcs)
print('装饰器带参数使用  = ',funcs(-3,5))

'''
使用@符号来调用装饰器

'''
def warpper(f):
    def inner(a,b):
        if a < 0:
            a = 1
        if b < 0:
            b = 1
        return f(a,b)
    return inner

@warpper # 相当于 funcs = warpper(funcs)
def funcs(a,b):
    return a + b

print('使用@符号的装饰器结果 ：',funcs(2,3))

'''
通用装饰器

'''
def warpper(f):
    def inner(*args,**kwargs):
        #在这增加我们想增加的功能
        print("这是增加新功能的地方！")
        res = f(*args,**kwargs)
        #在这如果有想修改返回值得，就可以在和进行修改
        return res
    return inner

@warpper
def func(name):
    return name+'说这个失误有点大！'

print('通用装饰器返回结果 ：',func('张飒'))

'''
装饰器带参数

'''

def warpper(count = 3):#相当于 @warpper(5) 传值
    def deco(f):#传的函数 func
        def inner(*args,**kwargs):#func(counts) 具体函数传的值在这
            for x in range(count):
                f(*args,**kwargs)
        return inner
    return deco

@warpper(5)#如果这里传值，warpper就使用这里传的值，如果不传就使用默认值3
def func(counts):
    print("heihei"+str(counts))

#调用函数
func(4)

'''
装饰器的使用，计算程序运行时间
'''
import time

def timer(f):
    def inner(*args,**kwargs):
        time1 = time.time()
        res = f(*args,**kwargs)
        time2 = time.time()
        print("运行时间为:  %f"%(time2-time1))
    return inner

@timer
def fun():
    print("aaaaaaaaaaaaaaaa")
    time.sleep(2)
    print("bbbbbbbbbbbbbbbbbbbbbbbbb")

fun()

'''
使用map将10000分10个1000同时进行
'''
listnumber = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
lisa = []
def fornumber(x):
    for i in range(x):
        print("第 [ ",i," ]个数")
        lisa.append(i)
    return lisa

res = map(fornumber,listnumber)
time1 = time.time()
print(time1)
print("res = ",list(res))
time2 = time.time()
print(time2-time1)
'''
多个装饰器的执行顺序
'''
def timer1(f):
    print("in timer1")
    def inner1(*args,**kwargs):
        print("in inner1")
        res = f(*args,**kwargs)
        print("exit inner1")
        return res
    print("exit timer1")
    return inner1
def timer2(f):
    print("in timer2")
    def inner2(*args,**kwargs):
        print("in inner2")
        res = f(*args,**kwargs)
        print("exit inner2")
        return res
    print("exit timer2")
    return inner2
def timer3(f):
    print("in timer3")
    def inner3(*args,**kwargs):
        print("in inner3")
        res = f(*args,**kwargs)
        print("exit inner3")
        return res
    print("exit timer3")
    return inner3

@timer1
@timer2
@timer3
def func(a,b):
    print("a + b :",(a+b))

func(1,2)
'''
装饰器 应用场景： 1.函数的调用次数，2.缓存，3.参数，结果检查，4.日志，5.统计，6.权限管理 ，7.重试（例如链接数据库，连续重新链接）
'''
def timer4(f):
    print("in timer4")
    index = 0#这个变量在闭包中，就相当于一直存放在内存中
    def inner4(*args,**kwargs):
        print("in inner4")
        nonlocal index#申请访问上一层的变量
        index += 1
        res = f(*args,**kwargs)
        print("exit inner4")
        print("执行第 %d 次执行方法"%index)
        return res
    print("exit timer4")
    return inner4

@timer4
def func(a,b):
    return a + b

res = func(2,3)
print('测试方法的执行次数   res = ',res)
res = func(2,3)
print('测试方法的执行次数   res = ',res)

'''
装饰器：一个模拟链接数据库的函数，链接失败之后重新链接

链接3次，每次链接失败中间停隔 0 秒,报任何错误都让其执行捕获
'''
import random
def retry(count = 3,wait = 0,exceptions= (Exception,)):
    def wraning(f):
        def inner(*args,**kwargs):
            for i in range(count):
                try:
                    print("--------------------------------------")
                    res = f(*args,**kwargs)
                except exceptions as e:#所有的异常都捕获！！
                    time.sleep(wait)#如果报了任何的错误都让其沉睡 wait 秒
                    print("进入了except...................")
                    continue
                else:
                    return res
        return inner
    return wraning

@retry(5)
def connetSQL(ip,port,dbName,password):
    num = random.choice([1,2,3,4])
    print("*******************",num)
    if num <= 2:
        10/0


connetSQL("",'','','')










