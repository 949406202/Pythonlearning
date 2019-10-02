

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