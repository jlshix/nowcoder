"""输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}
和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        # 一些意外情况
        if not pre and not tin:
            return None
        elif set(pre) != set(tin):
            return None
        
        # 只剩一个节点的时候, 可省略
        if len(pre) == 1 == len(tin):
            return TreeNode(pre[0])
        
        # 先序第一个值为根节点, 在中序中查找位置
        # 借此将二者分别一分为二
        root = pre[0]
        itin = tin.index(root)
        ipre = itin + 1
        lpre, rpre = pre[1:ipre], pre[ipre:]
        ltin, rtin = tin[:itin], tin[itin+1:]
        # 递归构造二叉树
        node = TreeNode(root)
        node.left = self.reConstructBinaryTree(lpre, ltin)
        node.right = self.reConstructBinaryTree(rpre, rtin)
        return node