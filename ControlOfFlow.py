# -----------------
# if语句
# 也许最有名的是if语句
# -----------------
# D:\GitHub\PythonLearnProject>python
# Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = int(input("Please enter an integer:"))
# Please enter an integer:42
# >>> x
# 42
# >>> if x < 0:
# ...     x = 0
# ...     print("Negative changed to zero")
# ... elif x == 0:
# ...     print("Zero")
# ... elif x == 1:
# ...     print('Single')
# ... else:
# ...     print('More')
# ...
# More
# >>>
# 关键字‘elif’是‘else if’的缩写，这个可以有效地避免过深的缩进。
# if...elif...elif...序列用于替代其他语言中的 switch 或 case 语句。
#---------------------
# For语句
#---------------------
# Python 中的for语句和 C 或 Pascal 中的略有不同。
# 通常的循环可能会依据一个等差数值步进过程（如Pascal），或由用户来定义迭代步骤和终止条件（如C），
# Python 的for语句依据任意序列（链表或字符串）中的子项，按它们在序列中的顺序来进行迭代。
# >>> Measure some strings：
# ... words = ['cat','window','defenestrate']
# >>> for w in words:
# ...     print(w,len(w))
# ...
# cat 3
# window 6
# defenestrate 12
# 
# 在迭代过程中修改迭代序列不安全（只有在使用链表这样的可变序列时才会有这样的情况）。
# 如果你想要修改你迭代的序列（例如，复制选择项），你可以迭代它的复本。
# 使用切割标识就可以很方便的做到这一点。