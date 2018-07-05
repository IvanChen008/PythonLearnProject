# -----------------
# if语句
# 也许最有名的是if语句
# -----------------
# D:\GitHub\PythonLearnProject>python
# Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = int(input("Please enter an integer:"))
# Please enter an integer:42
# >>> x
# 42
# >>> if x < 0:
# ...     x = 0
# ...     print("Negative changed to zero")
# ... elif x == 0:
# ...     print("Zero")
# ... elif x == 1:
# ...     print('Single')
# ... else:
# ...     print('More')
# ...
# More
# >>>
# 关键字‘elif’是‘else if’的缩写，这个可以有效地避免过深的缩进。
# if...elif...elif...序列用于替代其他语言中的 switch 或 case 语句。
#---------------------
# For语句
#---------------------
# Python 中的for语句和 C 或 Pascal 中的略有不同。
# 通常的循环可能会依据一个等差数值步进过程（如Pascal），或由用户来定义迭代步骤和终止条件（如C），
# Python 的for语句依据任意序列（链表或字符串）中的子项，按它们在序列中的顺序来进行迭代。
# >>> Measure some strings：
# ... words = ['cat','window','defenestrate']
# >>> for w in words:
# ...     print(w,len(w))
# ...
# cat 3
# window 6
# defenestrate 12
# 
# 在迭代过程中修改迭代序列不安全（只有在使用链表这样的可变序列时才会有这样的情况）。
# 如果你想要修改你迭代的序列（例如，复制选择项），你可以迭代它的复本。
# 使用切割标识就可以很方便的做到这一点。
#
#-----------------
# range()函数：产生一个数值序列，生成一个等差级数链表。
#-----------------
# >>> for i in range(5):
# ...     print(i)
# ...
# 0
# 1
# 2
# 3
# 4
# >>>range(5,10)
# range(5, 10)
# >>> for i in range(5,10):
# ...     print(i)
# ...
# 5
# 6
# 7
# 8
# 9
# >>> range(0,10,3)
# range(0, 10, 3)
# >>> for i in range(0,10,3):
# ...     print(i)
# ...
# 0
# 3
# 6
# 9
# >>> range(-10,-100,-30)
# range(-10, -100, -30)
# >>> for i in range(-10,-100,-30):
# ...     print(i)
# ...
# -10
# -40
# -70
# >>>
# 需要迭代链表索引的话，可以如下结合使用 range() 和 len()
# >>> a = ['Mary','had','a','little','lamb']
# >>> for i in range(len(a)):
# ...     print(i,a[i])
# ...
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb
# >>>
# 但是这种场合可以方便的使用 enumerate()
# >>> print(range(10))
# range(0, 10)
# >>>
#----------------
# range()函数返回的对象有时表现为它是一个列表，但事实上他并不是。当你迭代它时，
# 它是能够返回一个期望的序列的连续项对象；但实质上，他又不是真正的构造列表。
# 我们把它称为 可迭代的。即适合作为那些期望从某些东西中获得连续项直到结束的函数或结构的一个目标。
# 我们已经见过的for语句就是这样一个迭代器。list()函数是另外一个（迭代器），它从可迭代（对象）中创建列表。
#----------------
# >>> list(range(5))
# [0, 1, 2, 3, 4]
# >>>
#-----------------------------------------------------
# >>> for n in range(2,10):
# ...     for x in range(2,n):
# ...             if n % x == 0:
# ...                     print(n,"equals",x,'*',n//x)
# ...                     break
# ...     else:
# ...             print(n,'is a prime number')
# ...
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3
# >>>
# break 语句和C中的类似，用于跳出最近的一级for或while循环。
# 循环可以有一个 else 子句；它在循环迭代完整个列表（对于for）
# 或执行条件为false（对于while）时执行，但是循环被break中止的情况下不会执行。
# 
# Tips：
#       与循环一起使用时，else 子句与try语句的 else 子句比与if语句的else子句具有更多的共同点：
#       try语句的else子句在未出现异常时运行，循环的else子句在未出现break时运行。
#-----------------
# continue 语句是从C语言借鉴过来的，他表示循环继续执行下一次迭代。
#-----------------
# >>> for num in range(2,10):
# ...     if num % 2 == 0:
# ...             print("Found an even number:",num)
# ...             continue
# ...     print("Found a number",num)
# ...
# Found an even number: 2
# Found a number 3
# Found an even number: 4
# Found a number 5
# Found an even number: 6
# Found a number 7
# Found an even number: 8
# Found a number 9
# >>>
#----------------
# pass语句
#----------------
#>>> while True:
# ...     pass
# ...
# >>> class MyEmptyClass:
# ...     pass
# ...
# pass 语句什么也不做。它用于那些语法上必须要有什么语句，但程序什么也不做的场合。
# 通常用于创建最小结构的类。
# 另一方面，pass 可以在创建新代码的时候用来做函数或控制体的占位符。可以让我们在更加抽象的级别上思考。