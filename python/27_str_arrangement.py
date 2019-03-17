"""输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""

# -*- coding:utf-8 -*-
from itertools import permutations

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        # emmmm 这种写法我也不想的
        return sorted(list(set([''.join(x) for x in permutations(ss, r=len(ss))])))
