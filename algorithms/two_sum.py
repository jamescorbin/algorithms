"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

import collections
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums = sorted(list(zip(nums, range(n))))
        p1 = 0
        p2 = n - 1
        ret = None
        while ret is None:
            sm = nums[p1][0] + nums[p2][0]
            if sm > target:
                p2 -= 1
            elif sm < target:
                p1 += 1
            else:
                ret = [nums[p1][1], nums[p2][1]]
        return ret
