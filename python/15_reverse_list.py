"""
输入一个链表，反转链表后，输出新链表的表头。
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None
        vals = []
        # 并不是原地, 而是搜集后重新生成
        # TODO 原地
        while pHead:
            vals.append(pHead.val)
            pHead = pHead.next
        head = ListNode(vals[-1])
        p = head
        for val in vals[-2::-1]:
            q = ListNode(val)
            p.next = q
            p = q
        return head

