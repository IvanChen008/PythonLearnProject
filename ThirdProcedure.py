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
# >>>
