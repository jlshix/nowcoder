"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if not number:
            return 0
        arr = [1, 2]
        if number > 2:
            for i in range(3, number + 1):
                arr[(i+1)%2] = arr[0] + arr[1]
        return arr[(number+1)%2]