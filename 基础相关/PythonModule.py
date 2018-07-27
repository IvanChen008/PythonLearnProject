# 模块背景介绍
'''
    在计算机程序的开发过程中，随着程序代码越写越多，在一个文件中的代码会越来越长，维护就
    更加困难了。
    为了编写可维护的代码，我们把很多函数分株，分别放到不同的文件里，这样，每个文件包喊得
    代码就相对较少，很多编程语言都采用这种组织代码的方式。在python中，一个.py文件就称之
    为一个模块（Module）。
'''
# 使用模块的好处及注意事项
'''
    使用模块有什么好处？
    最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，
    就可以被其他地方引用。我们编写程序的时候，也经常引用其他模块，包括python内置的模块和
    来自第三方的模块。
    使用模块还可以避免函数名和变量名冲突。相同的名字的函数和变量完全可以分别存在不同的模
    块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但是也要注意尽量，不
    要与内置函数名字冲突。
    你也许还想到，如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了
    按目录来组织模块的方法，称为包（Package）。
    引入包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。
    注意，每一个包目录下面都会有一个__init__.py的文件，这个文件必须存在的，否则，python
    就把这个目录当做普通目录，而不是一个包。这个__init__.py可以是空文件，也可以有Python
    代码，因为__init__.py本身就是一个模块。而它的模块名就是包名。

    注意：自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如系统自带了sys模块，
    自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。

    总结：模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。
    创建自己的模块时，要注意：
        模块名要遵循Python变量命名规范，不要使用中文、特殊字符。
        模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互
    环境执行 import abc ,若成功则说明系统存在此模块。
'''
# 使用模块
'''
    Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用。
    导入
    import sys
    导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。
    当我们在命令行执行一个模块时，Python解释器把一个特殊变量__name__设置为__main__，而如果在
    其他地方导入该模块的时候，这个模块的__name__属性值并不是__main__。

'''
# 作用域
'''
    在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和
    变量我们希望仅仅在模块内部使用，在Python中，是通过_前缀来实现的。
    正常的函数和变量名是公开的(public)，可以被直接引用。类似于__main__这样的变量是特殊变量，也
    可以直接引用，但是有特殊用途。模块定义的文档注释也可以用特殊的变量__doc__访问，我们自己的
    变量一般不要这种变量名；
    类似_xxx和__xxx这样的函数或变量就是非公开的private，不应该被直接引用。之所以我们说，private
    函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制
    访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
    外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''
# 安装第三方模块
'''
    在Python中安装第三方模块，是通过包管理工具pip完成的。Mac和Linux安装pip本身这个步骤就可以
    跳过了。如果你正在使用Windows，确保安装时勾选了pip和Add python.exe to Path。
    一般来说，第三方库都会在Python官方的Pypi.python.org网站注册，要安装一个第三方库，必须先知道
    该库的名称，可以在官网或者pypi上搜索。
'''
# 安装常用模块 
'''
    在使用Python时，我们经常需要用到的很多第三方库，比如，上文提到的Pillow，以及MySQL驱动程序，
    Web框架Flask，科学计算的Numpy等，用pip一个一个装费时费力，还需要考虑兼容性。我们推荐直接使用
    Anaconda,这是一个基于Python数据处理和科学计算平台，他已经内置了许多非常有用的第三方库，我们
    装上Anaconda，就相当于把数十个第三方模块自动安装好了。非常简单易用。
'''
# 模块搜索路劲 
'''
    当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错。
    默认情况，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模
    块的path变量中。
    如果我们要添加自己的搜索目录，有两种方法：
    一是直接修改sys.path，添加要搜索的目录。
    二是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式和设置Path
    环境变量类似，注意只需要添加你自己的搜索路径，Python本身的搜索路径不受影响。
'''
