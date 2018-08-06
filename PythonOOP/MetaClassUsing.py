# type()
'''
    动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
    当Python解释器载入一个模块时，就会依次执行该模块的所有语句，执行结果就是动态创建一个该模块的class对象。
'''
class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s' % name)
'''
>>> from MetaClassUsing import Hello
>>> h = Hello()
>>> h.hello()
Hello,world
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class 'MetaClassUsing.Hello'>
>>>
    type()函数可以查看一个类型或变量的类型，一个class，它的类型就是type，而这个class的一个实例，它的类型
    就是class 这个类型。
    我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
    type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，
    而无需通过【class Hello(object)...】的定义。
    要创建一个class对象，type()函数依次传入3个参数：
        1、class的名称；
        2、继承的父类集合，注意Python支持多继承，如果只有一个父类，别忘了tuple的单元素写法；
        3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
    通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class
    定义的语法，然后调用type()函数创建出class。
    正常情况下，我们都使用 class Xxx... 来定义类，但是type()函数也允许我们动态创建出类来，也就是说，动态语
    言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再
    调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
'''
# metaclass
'''
    除了使用type()动态创建以外，要控制类的创建行为，还可以使用metaclass。
    metaclass，直译为元类，简单的解释就是：当我们定义了类以后，就可以根据这个类创建出实例，所以先定义类，然
    后创建实例。
    但是如果我们想创建出类呢？就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
    连接起来就是，先定义metaclass，就可以创建类，最后创建实例。
    所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
    metaclass是Python面向对象最难理解的，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用的metaclass
    的情况，所以以下内容看不懂也没关系，因为基本上你不会用到。
'''
# 示例
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass = ListMetaclass):
    pass

'''
    当我们传入关键字参数metaclass时，魔术就生效了，它指示python解释器在创建MyList时，要通过ListMetaclass.__new__()
    来创建，在此，我们可以修改类的定义，如加上新的方法，然后返回修改后的定义。
    __new__()方法接收到的参数依次是：
        1、当前准备创建的类的对象；
        2、类的名字；
        3、类继承的父类集合；
        4、类的方法集合；
'''
# 动态修改的意义在哪里？
'''
    直接在MyList定义中写上要添加的属性不是更加简单。正常情况确实该直接写，通过metaclass修改纯属变态。
    但是，总会遇到需要通过metaclass修改类定义的，ORM就是一个典型的例子。
    ORM全称是‘Object Relational Mapping’，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是
    一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
    要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
'''
# 尝试编写一个ORM框架
'''
    编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作
    对应的数据库表User，我们期待他写出这样的代码。

'''


class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)

class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

# 最最最复杂的metaclass
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name=='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model:%s' % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s ==> %s' % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)
# 基类
class Model(dict,metaclass=ModelMetaclass):
    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self,key,value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL:%s' % sql)
        print('ARGS:%s' % str(args))
'''
    当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类
    Model中查找metaclass找到了就使用Model中定义的metaclass的ModelMetaclass来创建User类，也就是说，metaclass可以隐
    式地继承子类，但子类自己却感觉不到。
    在ModelMetaclass中，一共做了几件事：
        1、排除掉对Model类的修改；
        2、在当前类查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中
        删除该Field属性，否则，容易造成运行时错误（实例属性遮盖类的同名属性）；
        3、把表名保存到__table__中，这里简化为表名默认为类名。
    在Model类中，就可以定义各种，操作数据库的方法，比如
    save(),delete(),find(),update()等等。

'''
# 编写功能尝试
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 创建一个实例：
u = User(id = 12345,name = 'Ivan',email='test@orm.org',password='my-pwd')
# 保存到数据库
u.save()

# metaclass是Python中非常具有魔术性的对象，它可以改变类创建时行为，这种强大的功能呢使用起来也务必要小心。