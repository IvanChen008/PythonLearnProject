'''
    在程序运行的过程中，所有的变量都实在内存中，此时可以随意修改变量，但是程序一旦结束，变量所占用的内存就被操作系统全部回收。
    我们把变量从内存中变成可存储或传输的过程叫做序列化，Python中称为pickling，在其他语言中，也有被称之为，serialization，
    marshalling，flattening等等。
    序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为
    反序列化，也就是unpickling。
    Python提供了pickle模块来实现序列化。
    pickle.dumps()方法把任意的对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接
    把对象序列化后写入一个file-like Object:
=====================================
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()
=====================================
    当我们要把对象从磁盘读到内存是，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法
    从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象。
=====================================
>>> f=open('dump.txt','rb')
>>> d=pickle.load(f)
>>> f.close()
>>> d
{'name': 'ivan', 'age': 20, 'score': 66}
=====================================
    变量的内容又回来了，但是这个变量和原来的变量是没有任何关系的对象，只是数据内容相同而已。Pickle的问题和所有其他编程语言特有的序列化问题一样，
    就是只能用于Python，并且可能不同的版本彼此不兼容，因此，只能用Pickle保存那些不太重要的数据，不能成功的反序列化都不重要的那些。
'''
# JSON
'''
    如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准的格式，如 XML ，JSON是一个非常好的选择，因为JSON表示出来就是一个字符串，
    可以被所有语言读取，也可以方便的存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在web页面读取，非常方便。
    JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
        JSON                Python
        {}                  dict
        []                  list
        "string"            str
        1224.515            int/float
        trur/false          True/False
        null                None
    Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
    将Python对象变成一个JSON：
===================================
>>> import json
>>> d={'name': 'ivan', 'age': 20, 'score': 66}
>>> json.dumps(d)
'{"name": "ivan", "age": 20, "score": 66}'
===================================
    dumps()方法返回一个str，内容就是标准的JSON。类似的dump方法可以直接把JSON写入到一个file-like Object。
    要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化,后者从file-like Object中读取字符串并反序列化：
==================================
>>> json_str='{"name": "ivan", "age": 20, "score": 66}'
>>> json.loads(json_str)
{'name': 'ivan', 'age': 20, 'score': 66}
==================================
    由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确的在Python的str与JSON的字符串之间转换。
    高级用法
    Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用Class表示对象，但是类对象并不是一个可序列化为JSON对象。
    但是如果连class的实例对象都无法序列化为JSON，肯定是不合理的，仔细观察dumps()方法的参数列表，可以发现，除了一个必须的obj参数外，
    dumps()方法还提供了一大堆可选的参数。https://docs.python.org/3/library/json.html#json.dumps
    这些可选的参数就是让我们来定制JSON序列化。在默认的情况下，dumps()方法不知道如何将类实例变为一个JSON对象。可选参数的default就是把任意一个
    对象变为一个可序列化为JSON对象，我们只需要为class专门写一个转换函数，再把函数传进去就可以了。
    因为通常一个class实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__属性的class。同样的入股我们要
    把JSON反序列化为一个class实例，loads()方法首先转换出一个dict对象，然后我们传入object_hook函数负责把dict转换为class实例。
'''
# 小结
'''
    Python语言特定的序列化模块时pickle，但是如果要把序列化搞得更通用、更符合web标准，就可以使用json模块。
    json模块的dumps()和loads()函数是定义的非常好的借口典范。当我们使用时只需要传入一个必须的参数。但是，当默认的是序列化和反序列化机制不满足
    我们的要求时，我们又需要传入更多的参数来定制序列化或反序列化的规则，既做到了借口简单易用，又做到了充分的扩展性和灵活性。
'''