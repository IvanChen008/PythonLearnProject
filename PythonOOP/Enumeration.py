# 定义常量
'''
    定义常量时，为需要定义的枚举类型定义一个class类型，然后，每个常量都是class的唯一实例。Python提供
    了Enum类来实现这个功能。
'''
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name,"=>",member,",",member.value)
'''
    value属性则是自动赋给成员的int常量，默认从1开始计数，如果需要更精确地控制枚举类型，可以从Enum派生出自定义类。

'''
from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0 #Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
'''
    @unique装饰器可以帮助我们检查保证没有重复值。
    访问这些枚举类型可以有若干种方法。
'''
print("%s+++++++++++++++",Month.Feb.value)
day1 = Weekday.Mon
print(day1)
# Weekday.Mon
print(Weekday.Tue)
# Weekday.Tue
print(Weekday['Tue'])
# Weekday.Tue
print(Weekday.Tue.value)
# 2
print(day1 == Weekday.Mon)
# True
print(day1 == Weekday.Tue)
# False
print(Weekday(1))
# Weekday.Mon
print(day1 == Weekday(1))
# True
for name, member in Weekday.__members__.items():
    print(name, '=>', member)
# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat
Weekday(7)
# Traceback (most recent call last):
#   ...
# ValueError: 7 is not a valid Weekday
'''
    我们既可以用成员引用枚举变量，又可以直接根据value的值获得枚举常量。
'''