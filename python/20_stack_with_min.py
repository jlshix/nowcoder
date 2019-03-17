"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # s1 是普通栈, s2 是最小栈
        self.s1 = []
        self.s2 = []
    
    def push(self, node):
        # write code here
        # 此时 s2 压入的是当前值对应的最小值
        self.s1.append(node)
        if not self.s2 or self.min() > node:
            self.s2.append(node)
        else:
            m = self.min()
            self.s2.append(m)

    def pop(self):
        # write code here
        self.s1.pop()
        self.s2.pop()
    
    def top(self):
        # write code here
        return self.s1[-1]

    def min(self):
        # write code here
        return self.s2[-1]