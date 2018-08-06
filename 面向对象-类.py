""" 
Python 是一门面向对象编程（Object Oriented Programming, OOP）的语言，
这里的对象可以看做是由数据（或者说特性）以及一系列可以存取、操作这些数据
的方法所组成的集合。面向对象编程主要有以下特点：

    多态（Polymorphism）：不同类（Class）的对象对同一消息会做出不同的
响应。
    封装（Encapsulation）：对外部世界隐藏对象的工作细节。
    继承（Inheritance）：以已有的类（父类）为基础建立专门的类对象。

在 Python 中，元组、列表和字典等数据类型是对象，函数也是对象。那么，我们
能创建自己的对象吗？答案是肯定的。跟其他 OOP 语言类似，我们使用类来自定义
对象。
 """
# 类和实例
''' 类是一个抽象的概念，我们可以把它理解为具有相同属性和方法的一组对象的
集合，而实例则是一个具体的对象。 
'''
class Animal(object):
    pass

""" Animal 是类名，通常类名的首字母采用大写（如果有多个单词，则每个单词的
  首字母大写），后面紧跟着（object），表示该类是从哪个类继承而来的，所有地
  类都会继承自objec类。
"""
# 创建实例
animal = Animal() # 创建一个实例对象
""" 我们在创建实例的时候，还可以传入一些参数，以初始化对象的属性，为此我们
    需要添加一个__init__ 方法
"""
class AnimalGotName(object):
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("Hello,I am %s" % self.name)
""" 总结：在类中定义了两个方法：__init__和greet。__init__是Python中的特
殊方法(special method),它用于对对象进行初始化，类似于C++中的构造函数；
greet 使我们自定义的方法。
    我们上面定义的两个方法有一个共同点，就是它们的第一个参数都是self，指向
实例本身，也就是说它们是和实例绑定的函数，也就是我们称它们为方法而不是函数
的原因。

注意：在Python中，以双下划线开头，并且以双下划线结尾（即__XXX__）的变量是
特殊变量，特殊变量是可以直接访问的。所以，不要使用__name__这样的变量名。
另外，如果变量名前面只有一个下划线 _ ，表示不要随意访问这个变量，虽然它可
以直接被访问。
"""

# 获取对象信息
""" 我们拿到一个对象实例的时候，我们会需要考查他的类型和方法等。
        第一招：使用type    来获取对象的相应类型
            type（obj）
        第二招：使用isinstance  判断对象是否为制定类型的实例
            isinstance(obj,type)
        第三招：使用hasattr/getattr/setattr
            hasattr(obj,attr)   判断对象是否具有指定属性/方法;
            getattr(obj,attr[,default]) 获取属性/方法的值，要是没有对应
                的属性则返回default的值（前提是设置了default），否则会抛
                出AttributeError异常；
            setattr(obj,attr,value) 设定该属性/方法的值，类似于obj.attr
             = value;
        第四招：使用dir 使用了dir(obj) 可以获取相应对象的所有属性和方法名
        的列表
 """