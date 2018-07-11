##
##Pyhon 函数、模块、文件操作、异常处理、面向对象编程
##
##
##函数详解
##函数：函数的本质就是功能的封装。使用函数可以大大提高编程的效率与程序的可读性。
##
##作用域
i=10#全局变量
def func():
    j=10#局部变量
print(i)
##print(j)
##函数使用和定义
'''
def 函数名(参数)：
    函数体
'''
def abc():
    print("abc")
##调用函数：函数名()
abc()
# 参数：与外部沟通的接口
# 参数分为形参和实参
# -------------------------
# 模块的导入
import cgi
from cgi import closelog

# 模块的类别
# 1、自带模块
# 2、第三方模块
# 3、自定义模块

# 第三方模块的安装
# 1、pip方式           *（网络安装）
# 2、whl下载安装        *（下载安装）
# 3、直接复制的方式     *（）
# 4、anaconda

# 异常处理
# 异常处理的格式
'''
try:
    pass(程序)
except expression as 异常名称:
    pass（异常处理部分）
'''
try:
    pass
except Exception as err:
    pass