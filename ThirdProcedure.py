#this is the first comment
spam = 1    # and this is the second comment
            # ... and now a third!
text = "# This is not a comment because it's inside quotes."
# 以下内容为编译器直接输入学习内容
# >>> 2+2
# 4
# >>> 50 - 5*6
# 20
# >>> (50-5*6)/4
# 5.0
# >>> 8/5   # division always returns a floating point number
# 1.6
# >>> 5**2        # 5 squared
# 25
# >>> 2**7        # 2 to the power of 7
# 128
# >>> width = 20
# >>> height = 5*9
# >>> width*height
# 900
# >>> #浮点数有完整的支持；整数和浮点数的混合计算中，整数会被转换为浮点数：
# ...
# >>> 3*3.75/1.5
# 7.5
# >>> 7.0/2
# 3.5
# 交互模式中，最近一个表达式的辅助给变量 "_"。这样我们就可以把它当作一个桌面计算器，很方便的用于连续计算，例如：
# >>> tax = 12.5/100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_,2)
# 113.06
# >>> 
#################
# 字符串    
# >>> 'spam eggs'   # single quotes
# 'spam eggs'
# >>> 'dosen\'t'    # use \' to escape the single quote ...
# "dosen't"
# >>> "doesn't"     # ... or use double quotes instead
# "doesn't"
# >>> '"Yes," he said.'
# '"Yes," he said.'
# >>> "\"Yes,\" he said."
# '"Yes," he said.'
# >>> '"Isn\'t," she said.'
# '"Isn\'t," she said.'
# >>>
##########
# 交互解释器中，输出的字符串会用引号引起来，特殊字符会用反斜杠转义。
# 虽然和输入看上去不太一样，但是两个字符串是相等的。如果字符串中只有单引号而没有双引号，
# 就用双引号引用，否则用单引号引用。print()函数生成可读性更好的输出，它会省去引号并且打印出转义后的特殊字符。
# >>> '"Isn\'t," she said.'
# '"Isn\'t," she said.'
# >>> print('"Isn\'t," she said.')
# "Isn't," she said.
# >>> s = 'First line.\nSecond line' # \n means newline
# >>> s # without print(), \n is include in the output 
# 'First line.\nSecond line'
# >>> print(s) # with print(), \n produces a new line
# First line.
# Second line
# >>>
### 那么如果你前面滴啊有 \ 的字符被当做特殊字符，你可以使用 原始字符串，方法是在第一个引号前面加上一个r
# >>> print('C:\some\name') # here \n means newline!
# C:\some
# ame
# >>> print(r'C:\some\name') # note the r before the quote"""  """
# C:\some\name
# >>>
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# >>> # 3 times 'un',followed by 'ium'
# ...
# >>> 3 * 'un' + 'ium'
# 'unununium'

# >>> "Py" 'thon'
# 'Python'  # can't concatenate a variable and a string literal
# >>> prefix ='Py'
# >>> prefix 'thon'
#   File "<stdin>", line 1
#     prefix 'thon'
#                 ^
# SyntaxError: invalid syntax
# >>> ('un' * 3) 'ium'
#   File "<stdin>", line 1
#     ('un' * 3) 'ium'
#                    ^
# SyntaxError: invalid syntax
# >>> # 它只用于两个字符串文本，不能用于表达式，如果相连接多个变量或者一个变量一个字符串文本，使用 + 
# >>> prefix + 'thon'
# 'Python'
# >>>
# >>> text = ('Put several strings within parentheses ' 'to have them joined together.')
# >>> text
# 'Put several strings within parentheses to have them joined together.'
# >>>
# >>> word = 'Python'
# >>> word[0]
# 'P'
# >>> word[5]
# 'n'
# >>> word[10]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>>word[-1] # 索引使用负数也可以，这将导致从右边开始计算。但是 -0 就是 0 ,所以不会导致从右边开始计算。
# 'n'
# >>> word[-5]
# 'y'
# >>> word[-6]
# 'P'
# 字符串数组切片，可以让你获得一个子字符串
# >>> word[0:2] # characters from position 0 (included) to 2 (excluded)
# 'Py'
# >>> word[2:5] # characters from position 0 (included) to 2 (excluded)
# 'tho'
# 注意包含起始的字符，不包含末尾的字符
# 这个使得s[:i]+s[i:]永远等于s
# 切片索引有非常有用的默认值；省略的第一个索引默认为零，省略的第二个索引默认为切片的字符串大小。
# >>>  
# >>> word[:2] # character from beginning to position 2 (excluded)
# 'Py'
# >>> word[4:] # character from position 4 (included) to the end
# 'on'
# >>> word[-2:] # character from the second-last (included) to the end
# 'on'
# >>>
#  这个表可以让我们很容易记住切片的工作方式。
#  切片是的索引在连个字符之间，左边第一个字符的索引为0，而长度为n的字符串最后一个字符的右边界索引为n。

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
#  使用过打的索引会导致错误：
# >>> word[41]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
# >>>
# Python字符串是不可以被更改的-它们是 不可变的。因此，赋值给字符串索引的位置会导致错误。
# 因此，给字符串索引位置赋值会导致错误。如果你需要一个不同的字符串，你应该创建一个新的。
# 内置了len(str)函数来返回字符串的长度。
########## 列表 ###########
# python有几个复合数据类型，用于表示其它的值。最通用的就是 list(列表)，
# 它可以写作中括号之间的一列逗号分隔的值。列表的元素不必是同一类型。
# 与字符串（以及其它所有內建的序列类型）一样，列表可以被索引和切片。
# 所有的切片操作都会返回一个包含请求的元素的新列表，就是会返回一个新的（浅拷贝副本）。
# 而且也支持连接这样的操作，但是列表是可变的，它允许修改元素，还可以使用append()方法，在列表的末尾添加新的元素。
# 也可以对切片赋值，此操作可以改变列表的尺寸，或清空它。
# 列表允许嵌套列表（创建一个包含其他列表的列表）。
#