class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    һ��ָʾn�Ľ׳�֮����˼�����
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
����һ��
����ͨ��forѭ����䣺
=====================
a = 1
n = 5
for i in range(1,n+1):
    a = a * i
print(a)
=====================
�õ������
120

��������
������ƪ�����ᵽ��reduce()������
=======================
from functools import reduce
n = 5
print(reduce(lambda x,y:x*y,range(1,n+1)))
=======================
�õ������
    120

��������
���ú����ĵݹ飺
==================
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return (n*factorial(n-1))

    a = factorial(5)
    print(a)
==================
�õ������
    120

��Ҫע����ǣ������ĵݹ�Ҫ����ֹ���ƣ������һֱ�ݹ���ȥ�����ϸ������и�����if�ж��������ֹѭ���Ľ��С�
�������ַ�ʽ�ֱ�����˲�ͬ�ķ�������һ�������������ģ��ڶ�������pythonic�ģ���������������������ߵġ�������ֱ�Ӷ���һ���׳˺�������ʱ�����Ե��ã��Ӷ��õ���ֵͬ��
'''