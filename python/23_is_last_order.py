"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        print('sequence:', sequence)
        if len(sequence) <= 2:
            return True
        length = len(sequence)
        piv = sequence[length-1]
        maxx = minn = sequence[0]
        for i in range(length-1):
            if sequence[i] > maxx:
                maxx = sequence[i]
            elif sequence[i] < minn:
                minn = sequence[i]
            if minn < piv < sequence[i+1]:
                return self.VerifySquenceOfBST(sequence[:i+1]) and self.VerifySquenceOfBST(sequence[i+1:-1])
        if max(sequence[:-1]) < piv or min(sequence[:-1]) > piv:
            return self.VerifySquenceOfBST(sequence[:-1])
        return False


if __name__ == "__main__":
    print(Solution().VerifySquenceOfBST([1, 2, 3, 4, 5]))