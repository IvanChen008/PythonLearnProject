'''
    在我们同时开发多个应用程序，那这些应用都会共用一个Python，就是安装在系统的Python3。
    但如果我们开发的一个引用需要一个库是新版本，但另一个需要老版本怎么办？

    为了解决这个问题，每个应用可能需要各自拥有一套独立的Python运行环境。virtualenv就是
    用来为一个应用创建一套‘隔离’的python运行环境。
'''
# 步骤
'''
    第一步，创建一个目录
    第二步，创建一个独立的Python运行环境
    命令virtualenv就可以创建一个独立的Python运行环境，我们还可以加上了参数--no-site-packages，
    这样，已经安装到系统Python环境中的所有第三方包都不会复制过来，这样，我们就得到了一个不带任何
    第三方包的‘干净’的Python运行环境。
    新建的Python环境被放到当前目录下的venv目录，有了venv这个python环境，(可以用source进入该环境 Mac、Unix)。
    ==================================
    D:\GitHub\PythonLearnProject>cd VirtualEnvironment\

    D:\GitHub\PythonLearnProject\VirtualEnvironment>venv\Scripts\activate.bat

    (venv) D:\GitHub\PythonLearnProject\VirtualEnvironment>
    ==================================
    在venv环境下，用pip安装的包都被安装到venv这个环境下，系统Python环境不受任何影响。这个环境就是
    单独对项目使用的环境了。

    提供虚拟环境为了解决不同版本的冲突问题。
'''