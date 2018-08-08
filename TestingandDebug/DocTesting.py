'''
    如果你经常阅读Python的官方文档，可以看到很多文档都有示例代码。可以把这些示例代码在python的交互环境下输入并执行，
    结果与文档中示例代码显示的一致。
    这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么可
    不可以自动执行写在注释中的这些代码呢？
    当然是可以的，注释是更明确的告诉函数调用者该函数的期望输入和输出。
    并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
    doctest严格按照python交互命令行输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦
    人的输出。
'''
# 文档测试示例
'''

'''
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
'''
    当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。所以，不必担心
    doctest会在非测试环境下执行。
    doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动
    把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。
'''