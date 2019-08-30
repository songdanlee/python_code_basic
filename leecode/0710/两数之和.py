from typing import List

class Solution:
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, m in enumerate(nums):
            if dic.get(target - m) is not None:
                return [i, dic.get(target - m)]
            dic[m] = i
