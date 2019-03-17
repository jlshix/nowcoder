"""
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # p q 分别指向 1 2
        p, q = pHead1, pHead2
        # head 为合并后的
        head = ListNode(0)
        # 保留标记
        r = head
        # 都还有时前进
        while p and q:
            # 添加节点并各自前进
            if p.val < q.val:
                head.next = ListNode(p.val)
                p = p.next
                head = head.next
            elif p.val > q.val:
                head.next = ListNode(q.val)
                q = q.next
                head = head.next
            else:
                head.next = ListNode(p.val)
                head.next.next = ListNode(q.val)
                p, q = p.next, q.next
                head = head.next.next
        # 一方耗尽后, 接上另一方
        if not p:
            head.next = q
        if not q:
            head.next = p
        # 返回的是不含头结点的
        return r.next
