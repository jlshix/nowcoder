"""大家都知道斐波那契数列，
现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # 0 1 2 时
        if n == 0:
            return 0
        elif n < 2:
            return 1
        # 初始值与当前计数
        a, b = 1, 1
        current = 2
        # 循环计算
        while current != n:
            a, b = b, a+b
            current += 1
        return b
