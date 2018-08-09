'''
    如果我们要操作文件、目录，可以在命令下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
    如果要在Python程序中执行这些目录和文件操作，可以使用Python内置的os模块我可以直接调用操作系统提供的
    接口函数。

    环境变量：
    在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看
===========================
>>> import os
>>> os.environ
===========================
    要获取某个环境变量的值，可以调用os.environ.get('key')
'''
# 操作文件和目录
'''
    操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意。查看、创建和删除目录可以这么调用。
===========================
# 查看当前目录的绝对路径
>>> os.path.abspath('.')
'D:\\GitHub\\PythonLearnProject\\IO编程'
>>>
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
>>> os.path.abspath('.')
'D:\\GitHub\\PythonLearnProject\\IO编程'
>>> os.path.join('D:\\GitHub\\PythonLearnProject\\IO编程','testDir')
'D:\\GitHub\\PythonLearnProject\\IO编程\\testDir'
# 然后创建一个目录
>>> os.mkdir('D:\\GitHub\\PythonLearnProject\\IO编程\\testDir')
# 删掉一个目录
>>> os.rmdir('D:\\GitHub\\PythonLearnProject\\IO编程\\testDir')
===========================
    把两个路径合成一个时，不要直接拼字符串，而是要通过os.path.join()函数，这样可以正确处理不同操作系统的路劲分隔符。
    同样的，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一
    部分总是最后级别的目录或文件名。
===========================
>>> os.path.splitext('D:\\GitHub\\PythonLearnProject\\IO编程\\test.txt')
('D:\\GitHub\\PythonLearnProject\\IO编程\\test', '.txt')
>>>
===========================
    os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便。这些合并、拆分路径的函数并不要求目录和文件要真实存在，
    它们只对字符串进行操作。文件操作使用下面的函数。假定当前目录下有一个test.txt文件。
===========================
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')
===========================
    但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
    我们有shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用的函数，它们可以看做是os模块的补充。
    最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码。
===========================
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
[]
>>> os.path.join('D:\\GitHub\\PythonLearnProject\\IO编程','testDir')
'D:\\GitHub\\PythonLearnProject\\IO编程\\testDir'
>>> os.mkdir('D:\\GitHub\\PythonLearnProject\\IO编程\\testDir')
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['testDir']
# 要列出所有的 .py 文件，也只需要一行代码。
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['filereadandwrite.py', 'IO编程.py', 'StringIOandBytesIO.py', '操作文件和目录.py']
===========================
    Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。   
'''