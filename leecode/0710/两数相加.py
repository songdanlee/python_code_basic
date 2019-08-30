# 给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# Definition for singly-linked list.

"""
官方题解
就像你在纸上计算两个数字的和那样，我们首先从最低有效位也就是列表 l1 和 l2 的表头开始相加。
由于每位数字都应当处于 0 .....…9 的范围内，我们计算两个数字的和时可能会出现 “溢出”。例如，5 + 7 = 12。
在这种情况下，我们会将当前位的数值设置为 2，并将进位 carry = 1带入下一次迭代。
进位 carry 必定是 0 或 1，这是因为两个数字相加（考虑到进位）可能出现的最大和为 9 + 9 + 1 = 19。

伪代码如下：

将当前结点初始化为返回列表的哑结点。
将进位 carry 初始化为 0。
将 p 和 q 分别初始化为列表 l1 和 l2 的头部。
遍历列表 l1 和 l2 直至到达它们的尾端。
将 x 设为结点 p 的值。如果 p 已经到达 l1 的末尾，则将其值设置为 0。
将 y 设为结点 q 的值。如果 q 已经到达 l2 的末尾，则将其值设置为 0。
设定 sum = x + y + carry
更新进位的值，carry = sum / 10
创建一个数值为 (sum mod 10)的新结点，并将其设置为当前结点的下一个结点，然后将当前结点前进到下一个结点。
同时，将 p 和 q 前进到下一个结点。
检查 carry = 1 是否成立，如果成立，则向返回列表追加一个含有数字 1 的新结点。
返回哑结点的下一个结点。

链接：https://leetcode-cn.com/problems/two-sum/solution/liang-shu-xiang-jia-by-leetcode/

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
                :param l1:ListNode
                :param l2: ListNode
                :return: ListNode
        """

        carry = 0
        res = ListNode(0)
        pre = res
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)  # tuple (x//y, x%y)
            pre.next = ListNode(val)
            pre = pre.next
        return res.next

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
                :param l1:ListNode
                :param l2: ListNode
                :return: ListNode
        """
        m, n = '', ''
        while l1:
            m, l1 = m + str(l1.val), l1.next  # 把l1(2 -> 4 -> 3)转为对应的 243
        while l2:
            n, l2 = n + str(l2.val), l2.next  # (5 -> 6 -> 4) --> 5,6,4
        # int(m[::-1])# 转为 int 342
        # int(n[::-1]#转为int 465
        # 342  + 465 = 807 相加，转为字符串，逆序，然后每一位转为int，最后转为列表
        return list(map(int, str(int(m[::-1]) + int(n[::-1]))[::-1]))


if __name__ == '__main__':
    sol = Solution()

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l11 = l1.next
    l11.next = ListNode(3)
    l12 = l11.next

    l2 = ListNode(5)
    l2.next = l21 = ListNode(6)
    l21.next = l22 = ListNode(4)

    res = sol.addTwoNumbers(l1, l2)

    while res:
        print(res.val)
        res = res.next
