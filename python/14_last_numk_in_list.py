"""
输入一个链表，输出该链表中倒数第k个结点。
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 意外情况
        if not head or not k:
            return None
        p = head
        # 从第一个走到第k个走k-1步
        for _ in range(k-1):
            p = p.next
            if not p:
                return None
        q = head
        # 同步前行
        while p.next:
            p = p.next
            q = q.next
        return q