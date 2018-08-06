class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    一个指示n的阶乘之后跟了几个零
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        for i in range(1,n+1):
            n = n*i
        cot = 0
        if (n%10):
            return 0
        else:
            cot = cot+ 0
            self.trailingZeros(int(n/10))
        return cot
'''
方法一：
很普通的for循环语句：
=====================
a = 1
n = 5
for i in range(1,n+1):
    a = a * i
print(a)
=====================
得到结果：
120

方法二：
采用上篇博文提到的reduce()函数：
=======================
from functools import reduce
n = 5
print(reduce(lambda x,y:x*y,range(1,n+1)))
=======================
得到结果：
    120

方法三：
采用函数的递归：
==================
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return (n*factorial(n-1))

    a = factorial(5)
    print(a)
==================
得到结果：
    120

需要注意的是，函数的递归要有终止机制，否则会一直递归下去。如上个程序中给定了if判断语句来终止循环的进行。
以上三种方式分别采用了不同的方法，第一种是最容易理解的，第二种是最pythonic的，而第三种则是易用性最高的。第三种直接定义一个阶乘函数，随时都可以调用，从而得到不同值。
'''