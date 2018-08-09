# StringIO
'''
    很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO顾名思义就是在内存中读写str。
    要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可。
=========================
>>> f=StringIO()
>>> f
<_io.StringIO object at 0x00000268831D2D38>
>>> f.write("Hello")
5
>>> f.write("   ")
3
>>> f.write("world!")
6
>>> print(f.getvalue())
Hello   world!
>>>
==========================
    getvalue()方法用于获得写入后的str。要读取StringIO，可以用一个str初始化StringIO，然后
    像读文件一样读取。
'''
# BytesIO
'''
    StingIO操作的只能是str，如果要操作二进制数据，就需要用BytesIO。BytesIO实现了在内存中读写bytes，
    我们创建一个BytesIO，然后写入一些bytes。
=============================
>>> from io import BytesIO
>>> f=BytesIO()
>>> f.write('中文'.encode('utf-8'))
6
>>> print(f.getvalue)
<built-in method getvalue of _io.BytesIO object at 0x0000026881578E08>
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'
>>>
=============================
    这里写入的不是str，而是经过UTF-8编码的bytes。和StringIO类似，可以用一个bytes初始化BytesIO，然后
    想读取文件一样读取。
'''
'''
    StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
'''