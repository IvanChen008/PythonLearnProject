'''
    常用的内置模块：
        datetime是Python处理日期和时间的标准库。
        collections是Python内建的一个集合模块，提供了许多有用的集合类。
        base64是一种用64个字符来表示任意二进制数据的方法。
        struct是Python提供来解决bytes和其他二进制数据类型的转换。准确地讲，Python没有专门处理字节的数据类型。
        但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来
        处理字节，以及字节和int，float的转换。
        hashlib:Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
        hmac:通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值，Hmac算法：Keyed-Hashing for Message Authentication。
        它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5
        还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。Python自带的hmac模块实现了标准的Hmac算法。
        itertools:Python内建模块itertools提供了非常有用的用于操作迭代对象的函数。
        contextlib有一些其他decorator，便于我们编写更简洁的代码。
        urllib提供了一系列用于操作URL的功能。
        XML：虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。
        HTMLParser:python提供了HtmlParser来非常方便地解析HTML。
'''