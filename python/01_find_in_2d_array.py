"""在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 空时不含
        if not array:
            return False
        # 获得行列数
        row,col = len(array), len(array[0])
        # 从第一行最后一列开始查找
        i, j = 0, col - 1
        # 设立边界条件
        while i < row and j >= 0:
            # 小则往下, 大则往左
            if array[i][j] < target:
                i += 1
            elif array[i][j] > target:
                j -= 1
            else:
                return True
        return False

