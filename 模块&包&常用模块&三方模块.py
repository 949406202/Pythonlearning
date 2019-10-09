

#使用import语句引入标准库中的模块
import sys
import 函数 #导入同包下的  函数.py 模块内容
#注意： 我们以后使用自定义的模块一般使用 from....import语句，他的作用是从某个模块中导入某一个部分，如下
from 函数 import add # 从 函数.py模块 中导入 add方法，（注：如果不在同一个目录 在from 后面需要添加他的路劲）
''' 常用
有的 from 后面的模块写出来的时候会报错，我们需要在前面加个 .  这个点表示 当前目录下,如下
from .函数 import add 
那我们在下面执行的时候就只需要
#add()就可以了
'''
#包含命令行参数的列表
print(sys.argv)
#自动查找所需模块的路劲的列表
print(sys.path)

#使用模块的里面的 函数,变量,类 例如：函数.方法名
#函数.add()

'''
每个 py文件模块都有一个 __name__属性,当其值是‘__main__’时，表明该模块自身在运行，否则是被当做模块引入，此时值为模块的名字
作用：模块就是一个可执行的python文件，一个模块被另一个模块引入，想让模块中的某一程序不执行，我们可以使用__name__属性来使程序隐藏该块代码
当自身执行时在执行该代码块

例如：我们在一个cc.py模块中，我们如果想让cc.py自身执行某一个功能的时候，我们可以使用,如下来进行执行
if __name__ == "__main__":
    在这里写自身运行的时候的一些代码，也就是if里面的代码是给自己py文件使用的
else:
    在这里我们写一些当被当成模块引入的一些功能代码，也就是else里面的代码是给别的模块使用的
'''
print('__name__ = ',__name__)# 在本py文件中__name__ == __main__ 如果当前的py文件被别的py文件引用的时候__name__ 就是当前py文件名

# 注意：我们在开发中定义模块都使用从 if __name__ == "__main__"开始写代码的

if __name__ == "__main__":
    print("我们自己的代码")
else:
    print('别人使用的代码')

'''
包：为了避免模块名冲突，python又引入了按目录来组织模块的方法，称为包（package）
特点：引入包以后，只要顶层的包名，不与别人的冲突，那么所有的模块都不会与此人的冲突
注意：每个包下面都会有一个名为 __init__.py 的文件(也就是说，一旦当前的目录中出现__init__.py说明他是一个包，否则他就是一个目录)
__init__.py 文件的作用：他可以导出的内容(特别说明：需要在__init__.py文件内)

特此说明__init__.py使用方法： 我们之前导包或者模块的时候 我们需要form 包名.模块名 import 方法1，方法2.....
我们有了 __init__.py 文件以后，我们可以把模块在__init__.py 文件里面去写，然后在别的地方需要使用的时候直接引入当前__init__.py的包就可以了
例如 abc 包下面有一个 __init__.py ，一个 a.py,一个 b.py 文件 在外层有一个 xx.py文件需要使用到 a.py和b.py里面的某一个方法

那么我们首先就可以在 __init__.py 文件中写入： from abc.a import a,from abc.b import b
然后我们在 xx.py文件中就可以直接写入：from abc import a方法，b方法
'''
# 例如 form 包名.模块名 import 方法1，方法2.....


'''
在导入的时候如果包和模块都重名的情况下，我们可以使用 as 取别名

from abc.say import say as s1
from bcd.say import say as s2
我们可以使用如上的一种方法来解决
'''

'''
 内建模块：
 
 time 模块
 UTC（世界协调时间），格林尼治时间，世界标准时间，在中国使用UTC+8
 DST(夏令时间)，是一种为了节约能源而人为的规定时间的制度，一般在天亮的夏季将时间提前一小时

    时间的表示方式
    1，时间戳
      以整型或浮点型表示是一个以秒为单位的时间间隔，这个时间基础是1970年1月1日零时开始算
    2，元祖新式
      一种python的数据结构表示，这个元祖有9个整形元素，分别表示不同时间的含义
      yeay(年)
      month(月,1-12)
      day(天,1-31)
      hours(小时,0-23)
      minutes(分,0-59)
      seconds(秒,0-59)
      weekday(星期,0-6,星期一为0)
      Julian day(表示当前日期在本年是第几天，1-366)
      DST flag(夏令时格式，-1 or 0 or 1)0：正常格式，1：夏令时格式，-1：根据当前日期格式来判断 ，一般情况下都使用 0就可以了 
    3，格式化字符串
        %a	本地（locale）简化星期名称
        %A	本地完整星期名称
        %b	本地简化月份名称
        %B	本地完整月份名称
        %c	本地相应的日期和时间表示
        %d	一个月中的第几天（01 - 31）
        %H	一天中的第几个小时（24小时制，00 - 23）
        %I	第几个小时（12小时制，01 - 12）
        %j	一年中的第几天（001 - 366）
        %m	月份（01 - 12）
        %M	分钟数（00 - 59）
        %p	本地am或者pm的相应符
        %S	秒（01 - 61）
        %U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。
        %w	一个星期中的第几天（0 - 6，0是星期天）
        %W	和%U基本相同，不同的是%W以星期一为一个星期的开始。
        %x	本地相应日期
        %X	本地相应时间
        %y	去掉世纪的年份（00 - 99）
        %Y	完整的年份
        %Z	时区的名字（如果不存在为空字符）
        %%	‘%’字符 
'''
import time

#time()返回当前时间戳，浮点类型，无需传参
t1 = time.time()
print(t1)

#gmtime(),将时间戳转化为UTC世界时间元祖形式,接收一个浮点型时间戳为参数，如果不传默认值为当前时间的时间戳,如下两个
t2 = time.gmtime(t1)
t3 = time.gmtime()
print(t2)
print(t3)

#localtime()将时间戳转化为本地时间元祖格式，接收一个浮点型时间戳为参数，如果不传默认值为当前时间的时间戳,如下两个
t4 = time.localtime()
print(t4)

#mktime() 将本地时间元祖转为时间戳，接收一个时间元祖
t5 = time.mktime(t4)
print(t5)

#asctime() 将时间元祖格式转为字符串形式，接收一个时间元祖，默认值为localtime时间的时间元祖

t6 = time.asctime(t4)
print(t6)

#ctime() 将时间戳转为字符串，接收一个时间戳，如果不传默认值为当前时间戳

t7 = time.asctime()
t77 = time.asctime(time.localtime())
print(t7)
print(t77)

# strftime() 将时间元祖以指定的格式转换为字符串形式，接收一个字符串格式串
t8 = time.strftime('%Y-%m-%d %X',time.localtime())
print(t8)

#strptime() 与strftime()相反，将时间字符串转为元祖
t9 = time.strptime('1999-10-01 08:08:08','%Y-%m-%d %X')
print(t9)

#sleep(),延迟一个时间，接收浮点或整型
time.sleep(3)#沉睡3秒再运行

'''
time.clock(): 返回当前程序执行时间，Unix系统始终全部运行时间，而window系统从第二次开始都是以第一次调用此函数的时间戳为基准，而不是以程序
开始时间为基准
如下:
'''
print("开始clock函数")
print(time.clock())
time.sleep(2)
print(time.clock())
time.sleep(2)
print(time.clock())

'''
datetime 基于 time进行了封装，提供了更实用的函数接口，datetime模块的接口更直观更容易调用

datetime模块中的类：

datetime,  同时有时间和日期
timedelta,  主要用于计算时间跨度
time,       只关注时间
date,       只关注日期
tzinfo      时区相关
'''
#获取当前时间
import datetime

t11 = datetime.datetime.now()
print('当前时间是： ',t11)
#获取指定时间
t22 = datetime.datetime(1999,9,8,8,8,8)
print('指定时间是：',t22)

#将时间转为字符串
t33 = t11.strftime('%Y-%m-%d %X')
print('时间字符串 ：',t33)

#将格式化字符串转为datetime对象
t44 = datetime.datetime.strptime(t33,'%Y-%m-%d %X')
print(t44)


'''
一、datetime模块介绍
（一）、datetime模块中包含如下类：
类名	功能说明
date	日期对象,常用的属性有year, month, day
time	时间对象
datetime	日期时间对象,常用的属性有hour, minute, second, microsecond
datetime_CAPI	日期时间对象C语言接口
timedelta	时间间隔，即两个时间点之间的长度
tzinfo	时区信息对象
（二）、datetime模块中包含的常量
常量	功能说明	用法	返回值
MAXYEAR	返回能表示的最大年份	datetime.MAXYEAR	9999
MINYEAR	返回能表示的最小年份	datetime.MINYEAR	1
二、date类
（一）、date对象构成
1、date对象由year年份、month月份及day日期三部分构成：

date（year，month，day)
2、 通过year, month, day三个数据描述符可以进行访问：

>>> a = datetime.date.today()
>>> a
datetime.date(2017, 3, 22)
>>> a.year
2017
>>> a.month
3
>>> a.day
22 
3、当然，你也可以用__getattribute__(...)方法获得上述值：

>>> a.__getattribute__('year')
2017
>>> a.__getattribute__('month')
3
>>> a.__getattribute__('day')
22
 

（二）、date对象中包含的方法与属性
1、用于日期比较大小的方法
方法名	方法说明	用法
__eq__(…)	等于(x==y)	x.__eq__(y)
__ge__(…)	大于等于(x>=y)	x.__ge__(y)
__gt__(…)	大于(x>y)	x.__gt__(y)
__le__(…)	小于等于(x<=y)	x.__le__(y)
__lt__(…)	小于(x	x.__lt__(y)
__ne__(…)	不等于(x!=y)	x.__ne__(y)
以上方法的返回值为True\False 
示例如下：

>>> a=datetime.date(2017,3,1)
>>> b=datetime.date(2017,3,15)
>>> a.__eq__(b)
False
>>> a.__ge__(b)
False
>>> a.__gt__(b)
False
>>> a.__le__(b)
True
>>> a.__lt__(b)
True
>>> a.__ne__(b)
True
2、获得二个日期相差多少天
使用__sub__(...)和__rsub__(...)方法，其实二个方法差不太多，一个是正向操作，一个是反向操作：

方法名	方法说明	用法
__sub__(…)	x - y	x.__sub__(y)
__rsub__(…)	y - x	x.__rsub__(y)
示例如下:

>>> a
datetime.date(2017, 3, 22)
>>> b
datetime.date(2017, 3, 15)
>>> a.__sub__(b)
datetime.timedelta(7)
>>> a.__rsub__(b)
datetime.timedelta(-7)
计算结果的返回值类型为datetime.timedelta, 如果获得整数类型的结果则按下面的方法操作：

>>> a.__sub__(b).days
7
>>> a.__rsub__(b).days
-7
3、ISO标准化日期
如果想要让所使用的日期符合ISO标准，那么使用如下三个方法: 
1).* isocalendar(...)*:返回一个包含三个值的元组，三个值依次为：year年份，week number周数，weekday星期数（周一为1…周日为7)： 
示例如下

>>> a = datetime.date(2017,3,22)
>>> a.isocalendar()
(2017, 12, 3)
>>> a.isocalendar()[0]
2017
>>> a.isocalendar()[1]
12
>>> a.isocalendar()[2]
3


2). isoformat(...): 返回符合ISO 8601标准 (YYYY-MM-DD) 的日期字符串； 
示例如下

>>> a = datetime.date(2017,3,22)
>>> a.isoformat()
'2017-03-22'
3). isoweekday(...): 返回符合ISO标准的指定日期所在的星期数（周一为1…周日为7) 
示例如下：

>>> a = datetime.date(2017,3,22)
>>> a.isoweekday()
3
4).与isoweekday(...)相似的还有一个weekday(...)方法，只不过是weekday(...)方法返回的周一为 0, 周日为 6 
示例如下：

>>> a = datetime.date(2017,3,22)
>>> a.weekday()
2
4、其他方法与属性
1). timetuple(...):该方法为了兼容time.localtime(...)返回一个类型为time.struct_time的数组，但有关时间的部分元素值为0：

>>> a = datetime.date(2017,3,22)
>>> a.timetuple()
time.struct_time(tm_year=2017, tm_mon=3, tm_mday=22, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=81, tm_isdst=-1)
>>> a.timetuple().tm_year
2017
>>> a.timetuple().tm_mon
3
>>> a.timetuple().tm_mday
22
2).toordinal(...)： 返回公元公历开始到现在的天数。公元1年1月1日为1

>>> a = datetime.date(2017,3,22)
>>> a.toordinal()
736410
3). replace(...)：返回一个替换指定日期字段的新date对象。参数3个可选参数，分别为year,month,day。注意替换是产生新对象，不影响原date对象。

>>> a = datetime.date(2017,3,22)
>>> b = a.replace(2017,2,28)
>>> a
datetime.date(2017, 3, 22)
>>> b
datetime.date(2017, 2, 28)
4).resolution：date对象表示日期的最小单位。这里是天。

>>> datetime.date.resolution
datetime.timedelta(1)
5).fromordinal(...)：将Gregorian日历时间转换为date对象；Gregorian Calendar ：一种日历表示方法，类似于我国的农历，西方国家使用比较多。

>>> a = datetime.date(2017,3,22)
>>> b = a.toordinal()
>>> datetime.date.fromordinal(b)
datetime.date(2017, 3, 22)
6).fromtimestamp(...)：根据给定的时间戮，返回一个date对象

>>> time.time()
1490165087.2242179
>>> datetime.date.fromtimestamp(time.time())
datetime.date(2017, 3, 22)
7).today(...)：返回当前日期

>>> datetime.date.today()
datetime.date(2017, 3, 22)
8).max： date类能表示的最大的年、月、日的数值

>>> datetime.date.max
datetime.date(9999, 12, 31)
9).min： date类能表示的最小的年、月、日的数值

>>> datetime.date.min
datetime.date(1, 1, 1)
（三）、日期的字符串输出
1、如果你想将日期对象转化为字符串对象的话，可以用到__format__(...)方法以指定格式进行日期输出：

>>> a = datetime.date(2017,3,22)
>>> a.__format__('%Y-%m-%d')
'2017-03-22'
>>> a.__format__('%Y/%m/%d')
'2017/03/22'
>>> a.__format__('%y/%m/%d')
'17/03/22'
>>> a.__format__('%D')
'03/22/17'
与此方法等价的方法为strftime(...)

>>> a.strftime("%Y%m%d")
'20170322'
关于格式化字符串的相关内容，请查阅本文最后的：附录：python中时间日期格式化符号 
2、如果只是相简单的获得日期的字符串，则使用__str__(...)

>>> a.__str__()
'2017-03-22'
3、如果想要获得ctime样式的格式请使用ctime(...):

>>> a.ctime()
'Wed Mar 22 00:00:00 2017'
三、time类
(一)、time类的数据构成
time类由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成

 time([hour[, minute[, second[, microsecond[, tzinfo]]]]])
相应的，time类中就有上述五个变量来存储应该的值：

>>> a = datetime.time(12,20,59,899)
>>> a
datetime.time(12, 20, 59, 899)
>>> a.hour
12
>>> a.minute
20
>>> a.second
59
>>> a.microsecond
899
>>> a.tzinfo
与date类一样，time类也包含__getattribute__(...)方法可以读取相关属性：

>>> a.__getattribute__('hour')
12
>>> a.__getattribute__('minute')
20
>>> a.__getattribute__('second')
59
（二）、time类中的方法和属性
1、比较时间大小
相关方法包括：__eq__(...), __ge__(...), __gt__(...), __le__(...), __lt__(...)， __ne__(...) 
这里的方法与date类中定义的方法大同小异，使用方法与一样，这里就不过多介绍了，示例如下：

>>> a = datetime.time(12,20,59,899)
>>> b = datetime.time(11,20,59,889)
>>> a.__eq__(b)
False
>>> a.__ne__(b)
True
>>> a.__ge__(b)
True
>>> a.__gt__(b)
True
>>> a.__le__(b)
False
>>> a.__lt__(b)
False
2、__nonzero__(...)
判断时间对象是否非零，返回值为True/False:

>>> a = datetime.time(12,20,59,899)
>>> a.__nonzero__()
True
3、其他属性
1）、max：最大的时间表示数值：

>>> datetime.time.max
datetime.time(23, 59, 59, 999999)
2）、min：最小的时间表示数值

>>> datetime.time.min
datetime.time(0, 0)
3）、resolution：时间间隔单位为分钟

>>> datetime.time.resolution
datetime.timedelta(0, 0, 1)
（三）、时间的字符串输出
1、如果你想将时间对象转化为字符串对象的话，可以用到__format__(...)方法以指定格式进行时间输出：

>>> a = datetime.time(12,20,59,899)
>>> a.__format__('%H:%M:%S')
'12:20:59'
与此方法等价的方法为strftime(...)

>>> a = datetime.time(12,20,59,899)
>>> a.strftime('%H:%M:%S')
'12:20:59'
关于格式化字符串的相关内容，请查阅本文最后的：附录：python中时间日期格式化符号 
2、ISO标准输出 
如果要使输出的时间字符符合ISO标准，请使用isoformat(...):

>>> a = datetime.time(12,20,59,899)
>>> a.isoformat()
'12:20:59.000899'
3、如果只是相简单的获得时间的字符串，则使用__str__(...)

>>> a = datetime.time(12,20,59,899)
>>> a.__str__()
'12:20:59.000899'
四、datetime类
(一)、datetime类的数据构成
datetime类其实是可以看做是date类和time类的合体，其大部分的方法和属性都继承于这二个类，相关的操作方法请参阅，本文上面关于二个类的介绍。其数据构成也是由这二个类所有的属性所组成的。

 datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
（二）、专属于datetime的方法和属性
1、 date(…)：返回datetime对象的日期部分：
>>> a = datetime.datetime.now()
>>> a
datetime.datetime(2017, 3, 22, 16, 9, 33, 494248)
>>> a.date()
datetime.date(2017, 3, 22)
2、time(…)：返回datetime对象的时间部分：
>>> a = datetime.datetime.now()
>>> a
datetime.datetime(2017, 3, 22, 16, 9, 33, 494248)
>>> a.time()
datetime.time(16, 9, 33, 494248)
3、utctimetuple(…)：返回UTC时间元组：
>>> a = datetime.datetime.now()
>>> a
datetime.datetime(2017, 3, 22, 16, 9, 33, 494248)
>>> a.utctimetuple()
time.struct_time(tm_year=2017, tm_mon=3, tm_mday=22, tm_hour=16, tm_min=9, tm_sec=33, tm_wday=2, tm_yday=81, tm_isdst=0)
4、combine(…)：将一个date对象和一个time对象合并生成一个datetime对象：
>>> a = datetime.datetime.now()
>>> a
datetime.datetime(2017, 3, 22, 16, 9, 33, 494248)
>>>datetime.datetime.combine(a.date(),a.time())
datetime.datetime(2017, 3, 22, 16, 9, 33, 494248)
5、now(…)：返回当前日期时间的datetime对象：
>>> a = datetime.datetime.now()
>>> a
datetime.datetime(2017, 3, 22, 16, 9, 33, 
6、utcnow(…):返回当前日期时间的UTC datetime对象：
>>> a = datetime.datetime.utcnow()
>>> a
datetime.datetime(2017, 3, 22, 8, 26, 54, 935242)
7、strptime(…)：根据string, format 2个参数，返回一个对应的datetime对象：
>>> datetime.datetime.strptime('2017-3-22 15:25','%Y-%m-%d %H:%M')
datetime.datetime(2017, 3, 22, 15, 25)
8、utcfromtimestamp(…):UTC时间戳的datetime对象，时间戳值为time.time()：
>>> datetime.datetime.utcfromtimestamp(time.time())
datetime.datetime(2017, 3, 22, 8, 29, 7, 654272)
五、timedelta类
timedelta类是用来计算二个datetime对象的差值的。 
此类中包含如下属性： 
1、days:天数 
2、microseconds：微秒数(>=0 并且 <1秒） 
3、seconds：秒数(>=0 并且 <1天）

六、日期计算实操
1.获取当前日期时间：
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2017, 3, 22, 16, 55, 49, 148233)
>>> today = datetime.date.today()
>>> today
datetime.date(2017, 3, 22)
>>> now.date()
datetime.date(2017, 3, 22)
>>> now.time()
datetime.time(16, 55, 49, 148233)
2.获取上个月第一天和最后一天的日期：
>>> today = datetime.date.today()
>>> today
datetime.date(2017, 3, 22)
>>> mlast_day = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
>>> mlast_day
datetime.date(2017, 2, 28)
>>> mfirst_day = datetime.date(mlast_day.year, mlast_day.month, 1)
>>> mfirst_day
datetime.date(2017, 2, 1)
3.获取时间差
时间差单位为秒

>>> start_time = datetime.datetime.now()
>>> end_time = datetime.datetime.now()
>>> (end_time - start_time).seconds
7
差值不只是可以查看相差多少秒，还可以查看天(days), 秒(seconds), 微秒(microseconds).

4.计算当前时间向后8个小时的时间
>>> d1 = datetime.datetime.now()
>>> d2 = d1 + datetime.timedelta(hours = 8)
>>> d2
datetime.datetime(2017, 3, 23, 1, 10, 37, 182240)
可以计算: 天(days), 小时(hours), 分钟(minutes), 秒(seconds), 微秒(microseconds).

5.计算上周一和周日的日期
today = datetime.date.today()
>>> today
datetime.date(2017, 3, 23)
>>> today_weekday = today.isoweekday()
>>> last_sunday = today - datetime.timedelta(days=today_weekday)
>>> last_monday = last_sunday - datetime.timedelta(days=6)
>>> last_sunday
datetime.date(2017, 3, 19)
>>> last_monday
datetime.date(2017, 3, 13)
6.计算指定日期当月最后一天的日期和本月天数
>>> date = datetime.date(2017,12,20)
>>> def eomonth(date_object):
...     if date_object.month == 12:
...         next_month_first_date = datetime.date(date_object.year+1,1,1)
...     else:
...         next_month_first_date = datetime.date(date_object.year, date_object.month+1, 1)
...     return next_month_first_date - datetime.timedelta(1)
...     
>>> eomonth(date)
datetime.date(2017, 12, 31)
>>> eomonth(date).day
31
7.计算指定日期下个月当天的日期
这里要调用上一项中的函数eomonth(...)

>>> date = datetime.date(2017,12,20)                                            
>>> def edate(date_object):                                                     
...     if date_object.month == 12:                          
...         next_month_date = datetime.date(date_object.year+1, 1,date_object.day)
...     else:
...         next_month_first_day = datetime.date(date_object.year,date_object.month+1,1)
...         if date_object.day > eomonth(last_month_first_day).day:
...             next_month_date = datetime.date(date_object.year,date_object.month+1,eomonth(last_month_first_day).day)
...         else:
...             next_month_date = datetime.date(date_object.year, date_object.month+1, date_object.day)
...     return next_month_date
...
>>> edate(date)
datetime.date(2018, 1, 20)
8.获得本周一至今天的时间段并获得上周对应同一时间段
>>> today = datetime.date.today()
>>> this_monday = today - datetime.timedelta(today.isoweekday()-1)
>>> last_monday = this_monday - datetime.timedelta(7)
>>> last_weekday = today -datetime.timedelta(7)
>>> this_monday
datetime.date(2017, 3, 20)
>>> today
datetime.date(2017, 3, 23)
>>> last_monday
datetime.date(2017, 3, 13)
>>> last_weekday
datetime.date(2017, 3, 16)
附录：python中时间日期格式化符号：
符号	说明
%y	两位数的年份表示（00-99）
%Y	四位数的年份表示（000-9999）
%m	月份（01-12）
%d	月内中的一天（0-31）
%H	24小时制小时数（0-23）
%I	12小时制小时数（01-12）
%M	分钟数（00=59）
%S	秒（00-59）
%a	本地简化星期名称
%A	本地完整星期名称
%b	本地简化的月份名称
%B	本地完整的月份名称
%c	本地相应的日期表示和时间表示
%j	年内的一天（001-366）
%p	本地A.M.或P.M.的等价符
%U	一年中的星期数（00-53）星期天为星期的开始
%w	星期（0-6），星期天为星期的开始
%W	一年中的星期数（00-53）星期一为星期的开始
%x	本地相应的日期表示
%X	本地相应的时间表示
%Z	当前时区的名称
%%	%号本身
'''
#----------------------------------------------------------------------------------
'''
 calendar 模块：
'''
import calendar
#返回2019年 整年的日历
print(calendar.calendar(2019))
print(type(calendar.calendar(2019)))
#返回某年某月的日历，类型为字符串
print(calendar.month(2019,10))
print(type(calendar.month(2019,10)))
#设置日期的第一天：（第一天以星期三开始）
calendar.setfirstweekday(calendar.WEDNESDAY)
cal = calendar.month(2019,10)
print("cal = ",cal)
#返回某个月的第一天和这个月的所有天数
print(calendar.monthrange(2019,10))
#返回某个月以每一周为元素的序列
print(calendar.monthcalendar(2019,10))
#在html中打印某年某月的日历
cal = calendar.HTMLCalendar(calendar.WEDNESDAY)
print(cal.formatmonth(2019,10))
#判断是否为闰年
print(calendar.isleap(2019))
#判断两个年份之间的闰年个数
print(calendar.leapdays(2000,2019))
#----------------------------------------------------------------------------------


