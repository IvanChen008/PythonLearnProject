# 面向对象高级编程
'''
    数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。
'''

'''
    正常情况下，当我们定义了一个class，创建了一个class的实例之后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
    通常情况下，我们会将绑定在所有实例的方法直接定义在class中，但动态绑定允许我们在程序运行过程中动态给class加上功能，这在静态
    语言中很难实现。
'''
# 使用 __slots__
'''
    但是，如果我们想要限制实例的属性怎么办呢？只允许某个类型的实例添加特定的属性。为了达到限制的目的，Python允许在定义class的时候，
    定义一个特殊的__slots__变量，来限制该类实例只能添加的属性。
    使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__，这样，
    子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
'''
# 使用@property
'''
    在绑定属性时，如果我们直接把属性暴露出去，虽然写起来简单，但是没办法检查参数，导致可以随意把属性修改了。这就不和逻辑。为了限制
    属性范围，可以通过一个setter()方法来设置这个属性，再通过一个getter()来获取成绩，这样就可以在方法中进行参数检查。
    但是这种设置setter和getter略显复杂，没有直接使用属性那么直接简单。现在就需要一种既可以检查参数，又可以用类似属性这样简单的方式来
    访问类变量的方式，我们可以使用装饰器(decorator)可以给函数动态加上功能的属性，对于类的方法，装饰器一样起作用。Python内置的@property
    装饰器就是负责把一个方法变成属性调用的。
    @property的实现比较复杂，先看看如何使用吧！ 

    @property
    def someproperty(self):
        return self._someproperty
    
    @someproperty.setter
    def someproperty(self,value):
        if not isinstance(value,int):
            raise ValueError('someproperty must be an integer')
        if value < 0 or value > 100:
            raise ValueError('someproperty must between 0~100!')
        self._someproperty = value

    把一个getter方法变成属性，只需要加上@property就可以了，此时@property本身又创建了另一个装饰器@someproperty.setter,负责把一个setter
    方法变成属性赋值，于是我们就拥有了一个可控的属性操作。
    注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。还可以
    定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性。

'''
# 小结：
'''
    @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时，就减少了出错的可能。

'''

# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width must bigger than 0!')
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value < 0:
            raise ValueError('height must bigger than 0!')
        self._height = value
    @property
    def resolution(self):
        return self.height*self.width
        
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# 多重继承
'''
    继承是面向对象编程的一个重要的方式，因为通过继承子类就可以扩展父类的功能。
    通过多重继承，一个子类就可以同时获得多个父类所有功能。
'''
# MinIn
'''
    在设计类的继承关系时，通常，主线都单一继承下来的，如果需要“混入”额外的功能，通过多重继承就可以实现。这种设计通常称之为MixIn
    MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
    Python自带的很多库也使用了MixIn。比如，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，
    这两种模型由ForkingMixIn和TheadingMixIn提供。通过组合我可以创造合适的服务来。
'''

'''
    由于Python允许使用多重继承，因此就是一种常见的设计。只允许单一继承的语言，不能使用MixIn的设计。
'''
# 定制类
'''
    看到类似__slots__这种形如__xxx__的变量或者函数名就要注意了，这些在Python中有特殊用途的。
    除了这些Python的class中含有很多这样的特殊用途的函数，可以帮助我们定制一个类。
'''
# __str__
'''
    我们先定义一个类，
'''
class Student(object):
    def __init__(self,name):
        self.name = name
    
    # 为了打印能好看一些，只需要定义好__str__()方法，返回一个好看的字符串就可以了,不仅好看还可以，看出实例的
    # 内部重要的数据。
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print(Student("TestSomeone"))
# 输出结果
# -------------
# <__main__.Student object at 0x0000018CAF0D3438>
# -------------
'''
# Student object (name: TestSomeone)
'''
'''
    __repr__()是显示变量调用时的内容，返回程序开发者看到的字符串，是针对调试服务的。
'''
# __iter__
'''
    如果一个类想被用于 for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后Python
    的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时推出循环。
'''
# __getitem__()、__setitem__()、__delitem__()
'''
    要变现的像list那样按照下标取出元素，需要实现__getitem__()方法，list有个神奇的切片方法，要针对参数做特殊处理。
    要正确实现一个__getitem__()还是有很多工作要做的。
    此外，如果把对象看做dict,__getitem__()的参数也可能是一个可以做key的object。与之对应的是__setitem__()方法，把对象视作list
    或dict来对集合赋值。最后还有一个__delitem__()方法，用于删除某个元素。
    总之，上面的方法在我们自己定义的类表现得 和python自带的list、tuple、dict没什么区别，这就完全归功于动态语言的“鸭子类型”，
    不需要强制继承某个接口。
'''
# __getattr__()
'''
    正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。为了避免这个无属性的错误，除了加上一个对应缺少的属性外，
    Python还有另一个机制，那就是写一个__getattr__()，动态返回一个属性。
    当调用的属性不存在时，Python的解释器会视图调用__getattr__(self,'someAttr')来尝试获得属性，这样，我们就能获得这个属性的值了。

    注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性。
    此外，注意到任意调用s.abc都会返回None,这是我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，
    抛出AttributeError的错误。

    这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。这种完全动态调用的特性的实际作用就是，可以针对
    完全动态的情况调用。
'''
# __call__()
'''
    一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用，能不能直接在实例本身调用呢，答案当然是肯定的。
    任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
    __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间
    本来就没啥根本的区别。如果你把对象看做函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的这么一来，我们就
    模糊了对象和函数的界限。
    那么，怎么判断一个变量是对象还是函数呢？其实更多的时候，我们需要判断一个对象时否能被调用，能被调用的对象就是一个Callable对象。就是带有
    __call__()的类实例。
    通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
    Python的class允许定许多定制方法，可以让我们非常方便地生成特定的类。
'''