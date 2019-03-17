"""
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 主要还是递归, 在树的算法中很常见
        # 要罗列好各种情况, 不重不漏
        res = False
        if not pRoot1 or not pRoot2:
            return res
        if pRoot1.val == pRoot2.val:
            res = self.treeContains(pRoot1, pRoot2)
        if not res:
            res = self.treeContains(pRoot1.left, pRoot2)        
        if not res:
            res = self.treeContains(pRoot1.right, pRoot2)

        return res
    
    def treeContains(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        
        return self.treeContains(pRoot1.left, pRoot2.left) and self.treeContains(pRoot1.right, pRoot2.right)
        
        
