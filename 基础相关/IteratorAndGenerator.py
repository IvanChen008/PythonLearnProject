# 2018年7月25日 16:06:33
# 廖雪峰Python 高阶函数 Map、Reduce 第三个练习的答案


# from functools import reduce

# def str2float(s):
#     def char2num(s):
#         digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,'6': 6, '7': 7, '8': 8, '9': 9}
#         return digits[s]
#     def func(x,y):
#         return x*10+y
#     index = s.index('.')
#     # s1 = map(char2num,s[:index-1])
#     # s2 = map(char2num,s[index:]) 
#     return reduce(func,map(char2num,s[:index]))+reduce(func,map(char2num,s[-index:]))*pow(10,index-len(s)+1)

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 2018年7月26日14:23:21
# 廖雪峰Python 高阶函数 闭包的操作调试

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs

# f1,f2,f3 = count()

# def count(): # 
#     def f(j):
#         def g(): # 定义了f函数的返回值函数g
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4): # 循环三次调用三个f函数
#         fs.append(f(i))
#     return fs # 返回一个含有三个闭包函数为内容的列表

# f1,f2,f3=count()
# print(count())
# print(f1())
# print(f1())
# f2()
# f3()


# -*- coding: utf-8 -*-

# 测试:

# def createCounter():
    # def f(j):
    #     def counter():
    #         return j
    #     return counter
    # c=[]
    # for i in range(1,100):
    #     c.append(f(i))
    # return c[]
    # c=0
    # def counter():
    #     nonlocal c
    #     c += 1
    #     return c
    # c=[0]
    # def counter():
    #     c[0] += 1
    #     return c[0]
    
    # return counter

# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')
# ------------------------------
#   装饰器
# ------------------------------
# def log(func):
#     def wrapper(*args,**kw):
#         print('call（ %s ）函数结果:' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
# 
# @log
# def now():
#     print("打印的时间")

# now()
# print(now.__name__)

# # -*- coding: utf-8 -*-
# import time, functools

# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args,**kw):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args,**kw)
#     return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
