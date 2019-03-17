"""用两个栈来实现一个队列，完成队列的Push和Pop操作。 
队列中的元素为int类型。
"""

# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        # 使用两个 list 模拟栈
        # 仅使用 append 和 pop
        self.stack1 = list()
        self.stack2 = list()

    def push(self, node):
        # write code here
        # 入栈放入 stack1
        self.stack1.append(node)

    def pop(self):
        # 出栈从 stack2 出
        # stack2 无元素则一次性从 stack1 提取
        if not self.stack1 and not self.stack2:
            return
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
