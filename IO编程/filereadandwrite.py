'''
    要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标识符。
    如果文件不存在就会，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在。
    如果打开正常，接下来就是调用read()方法读取文件的全部内容，Python把内容读到内存，用一个str对象表示。
    最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且
    操作系统同一时间能打开的文件数量也是有限的。
'''

try:
    f=open('test.txt','r',encoding='utf-8')
    print(f.read())
finally:
    if f:
        f.close()
'''
    由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用，所以，为了保证无论是否出错
    都能正确地关闭文件，我们可以使用try...finally来实现。
    但是由于每次这么写太繁琐了，所以，Python的引入了with语句来自动帮我们调用close()方法。
''' 
with open('test.txt','r',encoding='utf-8') as f:
    print(str(f.read()))
'''
    这种写法和前面的try...finally是一样的，但是代码更简洁，并且不必调用f.close()方法。
    调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆掉了，所以为了保险起见，可以反复
    调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，
    调用readlines()一次读取所有内容并按行返回list。因此根据需要决定怎么调用。
    如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是
    配置文件，调用readlines()最方便。
'''
# for line in f.readlines():
#     print(line.strip())

# file-like Object
'''
    像open()函数返回的这种有个read()方法的对象，在python中统称为file-like object。除了file外，还可以是内存
    的字节流，网络流，自定义流等等。file-like object不要求从特定类继承，只要写个read()方法就行。
    StringIO就是在内存中创建的file-like Object，常常用作临时缓冲。
'''
# 二进制文件
'''
    之前介绍的方法都是读取文本文件，并且UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，
    使用'rb'模式打开文件。
'''
# 字符编码
'''
    要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件。
    遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
    遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略。
'''
# 写文件
'''
    写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符“w”或者“wb”表示写文本文件或写入二进制文件。
    可以反复的调用write()来写入文件，但是必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把
    数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入
    的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以还是用with语句
    更加安全。
'''
# f=open("test.txt",'w')
# f.write('Hello world')
# f.close()
with open('test.txt','w') as f:
    f.write('Hello world!')
'''
    要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。以‘w’模式写入文件时，
    如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾，可以使用‘a’追加（append）
    模式写入。

    Python 中，文件读写通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
'''
