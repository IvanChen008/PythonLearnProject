# 背景
'''
    程序运行的时候，数据都是在内存中的，当程序终止的时候，通常都需要将数据保存到磁盘上，无论是保存到本地磁盘，还是通过网络保存到
    服务器上，最终都会将数据写入磁盘文件。
    而如何定义数据存储格式就是一个大问题。我们可以自定各种保存格式，但是问题来了：存储和读取需要自己实现，JSON还是标准，自己定义
    的格式就是各式各样的了，不能做快速查询，只有把数据全部读取到内存中才能自己遍历，但有时候数据的大小远远超过了内存，根本无法全
    部读入内存。
    为了便于程序和读取数据，而且，能直接通过条件快速查询到指定的数据，就出现了数据库Database这种专门用于集中存储和查询的软件。
    数据库软件诞生的历史非常久远，早在1950年数据库就诞生了，经历了网状数据库，层次数据库，我们现在广泛使用的关系数据库是20世纪70年代
    基于关系模型的基础上诞生的。
    关系模型有一套复杂的数学理论，但是概念上是十分容易理解的。
'''
# NoSQL
'''
    你也许还听说过NoSQL数据库，很多NoSQL宣传其速度和规模远远超过关系数据库，所以很多同学觉得有了NoSQL是否就不需要SQL了，但是千万别
    被忽悠了，连SQL都没明白，怎么可能搞明白NoSQL呢？
    # 数据库类别
    目前广泛使用的关系数据库也就是那么几种：
        Oracle，典型的高富帅
        SQL Server，微软自家的产品，Windows定制款。
        DB2，IBM的产品，听起来高端
        Sybase，曾经是微软的好基友，后来破裂现在很惨
    这些数据库都是不开源而且付费的，最大的好处就是花了钱出了问题可以找厂家解决，不过在Web的世界里，常常需要部署成千上万的数据库服务器，
    当然补鞥呢把大把大把的银子扔给数据库厂家，所以，无论是Google、Facebook,还是国内的BAT，无一例外都选择了免费的开源数据库：
        MySQL，大家都在用，一般错不了
        PostgreSQL，学术气息有点重，其实很不错，但是知名度没有MySQL高
        sqlite，嵌入式数据库，适合桌面和移动应用。
    作为Python开发工程师，选择哪个免费的数据库呢？当然是MySQL。因为MySQL普及率最高，出了错，可以很容易找到解决方法，而且围绕MySQL有
    一大堆监控和运维的工具，安装和使用都很方便。为了能继续后面的学习，需要从MySQL官方网站下载并安装MySQL Community Server 。

'''
# SQLite
'''
    SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身就是C写的，而且体积小，所以经常被集成到各种应用程序中，甚至在iOS和Android
    的app中都可以集成。
    Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
    # 一些概念：
    表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。要操作关系数据库，
    首先需要连接到数据库，一个数据库连接称为Connection；连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后获得执行结果。
    Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。由于SQLite的驱动内置在Python标准库中，
    所以我们可以直接来操作SQLite数据库。
'''
# # 实践一下：
# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute("create table user (id varchar(20) primary key,name varchar(20))")
# cursor.execute('insert into user (id, name) values(\'1\',\'Michael\')')
# cursor.rowcount
# cursor.close()
# conn.commit()
# conn.close()
# # 查询记录：
# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('select * from user where id=?',('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()
'''
    使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心的使用。使用Cursor
    对象执行insert，update，delete语句时，执行结果由rowcount返回影响的函数，就可以拿到执行结果。使用Cursor对象
    执行select语句时，通过fetchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
    如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，比如：
        cursor.execute('select * from user where name=? and pwd=?',('abc','password'))
    SQLite支持常见的标准SQL语句以及几种常见的数据类型。
    小结：
    在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。要确保打开的
    Connection对象和Cursor对象都正确的关闭，否则资源就会泄露。
    如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？可以是
    try:
        pass
    except:
        pass
    finally:
        pass

'''
# # MySQL
# import mysql.connector

# conn = mysql.connector.connect(host='localhost',port='3306',user='root',password='123456',database='test')
# cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s,%s)',['1','Michael'])
# print(cursor.rowcount)

# conn.commit()
# cursor.close()
# print('插入关闭')

# cursor = conn.cursor()
# cursor.execute('select * from user where id = %s',('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# print(cursor.close())
# conn.close()
'''
# 2018年8月16日 16:31:11
# 输出结果：
# +============================
D:\ProgramData\Anaconda3\python.exe G:/Python/MySQLtest.py
1
插入关闭
[('1', 'Michael')]
False

Process finished with exit code 0
# =============================
    由于Python的DB-API定义都是通用的，所以操作MySQL的数据库代码和SQLite类似。
    执行insert等操作后，要调用commit()。
'''
# 使用 SQLAlchemy
'''
    数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，可以用一个
    list表示多行，list的每一个元素是tuple，表示一行记录。Python的DB-API返回的数据结构就是像上面
    这样表示的。但是用tuple表示一行很难看出表的结构，如果把tuple用class实例来表示，就可以更容易
    地看出表的结构。
    SQLAlchemy就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
    是不是很简单？但是转换由谁来做呢？于是ORM框架应运而生。在python中，最有名的ORM框架是SQLAlchemy。
    
    测试一下SQLAlchemy：
    第一=步：导入SQLAlchemy，并初始化DBSession（session:会话）
# ==========================================
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# ==========================================
    以上的代码完成了SQLAlchemy的初始化和具体每个表的class定义。如果有多个表，就继续定义其他class，例如：
    # ===================
    class School(Base):
        __tablename__ = 'school'
        id = ...
        name = ...
    # ===================
    create_engine()用来初始化数据连接。SQLAlchemy用一个字符串表示连接信息。
        ‘数据库类型+数据库驱动名称://用户名:口令@地址：端口/数据库名’
    我们只需要根据需要替换用户名等必要的信息。接下来我们想数据库表中添加一行记录。由于有了ORM，我们向数据库表中添加一行记录，
    可以视为添加一个User对象:
# ===========================================
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
# ===========================================
    最关键是获取session，然后把对象添加到session，最后提交并关闭。DBSession对象可视为当前数据库连接。如何从数据库表中查询数据？
    有了ORM，查询出来的可以不再是tuple，而是User对象。SQLAlchemy提供查询接口如下：
# ===========================================
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
# ===========================================
    ORM其实就是把数据库表的行与对应的对象建立关联，互相转换。由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，而且
    ORM框架也可以提供两个对象之间的一对多、多对多等功能。
    比如：一个User拥有多个Book就可以定义一对多关系。
# ===========================================
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
# ===========================================
    当我们查询一个User对象时，该对象的books属性将返回一个包含若干Book对象的list。
    小结：ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。正确使用ORM的前提是了解关系数据库原理。
'''

