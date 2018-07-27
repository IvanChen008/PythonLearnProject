#  函数式编程

"""
    函数是一种內建（Builtin）支持的一种封装，通过把大段的代码拆成函数，通过
    一层一层的函数调用，就可以吧复杂任务分解成简单的任务，这种分解可以称之为
    面向过程的程序设计。函数就是面向过程的程序设计的基本单元。
    但是函数式编程（Functional Programming），虽然也可以归结到面向过程的程
    序设计，但其思想更接近数学计算。
    首相是，计算机和计算的概念。
    在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转
    指令，所以汇编语言是最贴近计算机的语言。
    而计算则是指数学意义上的计算，越是抽象的计算，越远离计算机硬件。
    于是对应到编程语言，越是低级的语言，越贴近计算机，抽象程度越低，执行效率
    越高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低。

    函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数
    没有变量，因此任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数
    我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状
    态不确定，同样的输入，可能得到不同的输出，因此这种函数是有副作用的。
    函数式编程的特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一
    个函数！
    Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不
    是纯函数式编程。
"""
# 高阶函数

'''
    高阶函数英文叫Higher-order function。
    -变量可以指向函数-
    如：求绝对值函数abs，它本身就是这个函数
    >>> abs
    <built-in function abs>
    >>> f = abs
    >>> f
    <built-in function abs>
    >>> f(-10)
    10
    变量本身指向了一个函数，变量f现在已经指向了abs函数本身。直接调用abs()和
    调用变量f()完全相同。
    -函数名也是变量名-
    函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成
    变量，它指向一个计算绝对值的函数！
    在Python内可以把函数名当作变量指向其他的对象，但是实际的代码绝对不能这么
    写，否则会引起混乱，如果要恢复之前的函数，重启Python的交互环境就可以了。
    注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改的abs
    变量指向在其他模块中要生效，要用 import builtins；builtins.abs = 10。
    -传入函数-
    既然变量也可以指向函数，函数的参数也能接收变量，那么一个函数就可以接收另
    一个函数作为参数，这种函数就称之为高阶函数。
        比如：
        def add(x,y,f):
            return f(x)+f(y)
'''
# MapReduce
'''
    Python 内置了map()和reduce()函数。
    “MapReduce: Simplified Data Processing on Large Clusters”==
    ==>http://research.google.com/archive/mapreduce.html
    如果度过Google的这片文章，就能够将map/reduce的概念大概搞明白。
    =map()=
    map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作
    用到序列的每个元素，并把结构作为新的Iterator返回。
    >>> def f(x):
    ...     return x*x
    ...
    >>> r = map(f,[1,2,3,4,5,6,7,8,9])
    >>> list(r)
    [1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>>
    map()传入的第一个参数是f，即函数对象本身。由于结果是一个Iterator,Iterator
    是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
    虽然我们可以写一个循环来完成同样的功能，但是代码的可读性并不很好，不能清楚的
    看明白，所以map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以
    计算简单的运算，还可以计算任意复杂的函数，比如，把这个list所有数字转换为字符
    串，等。
    =reduce()=
    再看看reduce()的用法。reduce把一个函数作用在一个序列上，这个函数必须接收两个
    参数，reduce把结果继续和序列的下一个元素做积累计算，其效果就是:
    >>>reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
    比如如果要把序列[1,3,5,7,9]变成整数13579,reduce就可以排上用场：
    >>> from functools import reduce
    >>> def fn(x,y):
    ...     return x*10+y
    ...
    >>> reduce(fn,[1,3,5,7,9])
    13579
    

    廖雪峰教程的答案：
    1）、
        def normalize(name):
            return name[0].upper()+name[1:].lower()
    2）、
        def prod(L):
            def mul(x,y):
                return x*y
            return reduce(mul,L)
    3）、查看 IteratorAndGenerator.py
        
'''
# filter()
'''
    Python内置的filter()函数过滤序列。
    和map()类似，它接收的参数也是一个函数和一个序列。和map()不同的是，filter()
    把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃
    该元素。
    比如删除偶数：
    >>> def is_odd(n):
    ...     return n%2==1
    ...
    >>> list(filter(is_odd,[1,2,3,5,6,9,10,15]))
    [1, 3, 5, 9, 15]
    >>>
    filter()这个高阶函数的关键在于正确的实现一个“筛选”函数。注意到filter()函数返
    回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要
    用list()函数获得所有结果并返回list。
'''
# sorted() 
'''
    排序也是程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两
    个元素的大小。如果是数字，我们可以直接比较，但是如果是字符串或者两个dict呢？直
    接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
    Python内置的sorted()函数就可以对list进行排序。此外，sorted()函数也是一个高阶
    函数，它还可以接收一个key函数来实现自定义的排序。
    key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比
    原始的list和经过key=abs处理过的list。
    然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素。
    字符串排序的例子：
        默认情况下，对字符串排序，是按照ASCII的大小比较的，由于“Z”<'a'，结果，大写
    字母Z会排在小写字母前面。
    现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码
    大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来
    比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
    >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
    ['about', 'bob', 'Credit', 'Zoo']
    要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
    >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    ['Zoo', 'Credit', 'bob', 'about']
'''
# 返回函数
'''
    -函数作为返回值-
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    我们在外部函数中定义一个外部函数，并且内部函数可以引用外部函数的参数和局部变量，当
    外部函数返回外部函数时，相关参数和变量都保存在返回的函数中，这种称为闭包（Closure）
    的程序结构拥有极大的威力。
    需要注意每次调用外部函数时，每次都会返回一个新的内部函数，即使传入相同的参数。
    -闭包-
    返回的内部函数在其定义内部引用了外部函数的局部变量，所以，当一个外部函数返回了一个
    内部函数后，其内部的局部变量还被新函数引用，所以闭包用起来简单，实现起来可不容易。
    需要注意的是，返回的内部函数并没有立即执行，而是直到调用了f()才执行。
    另外，返回闭包函数是需要牢记，返回函数不要引用任何循环变量，或者后续会发生变化的变量。
    如果一定需要引用循环变量的话，我们可以再创建一个函数，用该函数的参数绑定循环变量当前
    的值，无论该循环变量如何改变，已绑定到函数参数的值不变。
'''
# 匿名函数
'''
    当我们传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。在Python中，
    对匿名函数提供了有限的支持。关键字lambda表示匿名函数，冒号前面的x表示函数参数。匿名
    函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。用匿名函
    数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也
    可以把匿名函数赋值给一个变量，在利用变量来调用该函数。
    同样，也可以把匿名函数作为返回值返回。
'''
# 装饰器
'''
    由于函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用该函数。函数
    对象有一个__name__属性，可以拿到函数的名字。
    假如我们要增强一个函数的功能，但是又不希望修改原函数的定义，这种在代码运行期间动态增
    加功能的方式，称之为“装饰器”（Decorator）。
    本质上，decorator就是一个返回函数的的高阶函数。所以我们要定义一个功能实现的decorator，
    可以定义如下：
    def decor(func):
        def wrapper(*args,**kw):
            pass
            return func(*args,**kw)
        return wrapper

    @decor
    def originFunction():
        pass
    如果现在调用originFunction()函数，不仅会运行函数本身，还会运行函数前一行，把@decor
    放到originFunction()函数的定义处，相当于执行了： originFunction=decor(originFunction)
    由于decor()是一个Decorator，返回一个函数，所以原来的originFunction函数仍然存在，
    只是现在同名的originFunction变量指向了新的函数，于是调用originFunction()将执行新
    函数，即在decor()函数中返回wrapper()函数。
    wrapper()函数的参数定义是(*args,**kw),因此wrapper()函数可以接受任意参数的调用。在wrapper
    函数内，首先打印日志，再紧接着调用原始函数。
    如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。
    def decor(testPram):
        def decorator(func):
            def wrapper(*args,**kw):
                print('%s %s():' % (testPram,func.__name__))
                return func(*args,**kw
            return wrapper
        return decorator
    
    @decor('execute')
    def originFunc():
        pass
    这种三层嵌套的效果相当于是这样的：
    originFunct = decor('execute')(originFunc)
    函数其实首先执行decor('execute')，返回的是decorator函数，再调用返回的函数，参数
    originFunc函数，返回值最终是wrapper 函数。
    以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__
    等属性，但你去看经过的decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
    因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到
    wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
    不需要编写wrapper.__name__ = func.__name__这样的代码，python内置的functools.wraps就是干
    这个事的，所以，一个完整的decorator的写法如下：
    ----------------------
    import functools

    def decor(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('call %s():' % func.__name__)
            return func(*args,**kw)
        return wrapper

    # 针对带参数的decorator：
    def decor(testPram):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('%s %s():' % (testPram,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator
    ----------------------
    import functools 是导入 functools模块。需要记住在定义wrapper()的前面加上@functools.wraps(func)
    即可。

    小结：
        在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，
    而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，
    也可以用类实现。
        decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

'''
# 片函数
'''
    Python的functools模块提供了很多有用的的功能，其中一个就是偏函数（Partial function）。要注意，这里的
    偏函数和数学意义上的偏函数不一样。
    在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
    functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义函数,可以直接用模块创建一个新函数int2
    int2 = functools.partial(int,base=2)
    所以functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
    调用这个新函数会更简单。
    小结：
    当函数的参数个数太多，需要简化的时候，使用functools.partial可以创建一个新的函数，这个新函数可以固定
    住原函数的部分参数，从而在调用时更简单。
'''



'''
    一个函数可以返回一个计算结果，也可以返回一个函数。

    返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
'''