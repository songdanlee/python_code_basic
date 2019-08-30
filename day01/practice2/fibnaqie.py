"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n<=1:
            print(n)
        else:
            a=n-2
            f=0
            b=1
            num = 0
            mid = 0
            for i in range(a+1):
                num = f+b
                f = b
                b = num
            print(num)
s = Solution()
s.Fibonacci(39)