"""
操作给定的二叉树，将其变换为源二叉树的镜像
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        # 特殊情况与停止条件
        if not root:
            return None
        if not root.left and not root.right:
            return root
        # 递归反转
        root.left, root.right = self.Mirror(root.right), self.Mirror(root.left)
        return root