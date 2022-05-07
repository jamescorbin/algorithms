"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""
from typing import List

def has_132_pattern(nums: List[int]) -> bool:
    """
    Use stack to build a monotonically decreasing sequence.
    The stack is decreasing from the right.
    The third value bookmarks a smaller element bigger
    less than the top of the stack that has already been
    parsed.

    This method avoids a pitfall like the largest
    element being the last element.
    """
    stack = []
    ret = False
    third_value = float("-inf")
    for num in reversed(nums):
        if num < third_value:
            ret = True
            break
        while (len(stack) > 0) and (stack[-1] < num):
            third_value = stack.pop()
        stack.append(num)
    return ret

def test():
    arrs = [
        [1, 2, 3, 4],
        [3, 1, 4, 2],
        [-1, 3, 2, 0]]
    for nums in arrs:
        print(nums, has_132_pattern(nums))

if __name__=="__main__":
    test()
