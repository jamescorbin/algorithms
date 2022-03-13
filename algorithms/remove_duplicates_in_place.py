"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List

def remove_duplicates_1(nums: List[int]) -> int:
    """
    nums is sorted
    """
    if len(nums) > 0:
        slowp = 0
        fastp = slowp + 1
        while fastp < len(nums):
            if nums[fastp] > nums[slowp]:
                slowp += 1
                nums[slowp], nums[fastp] = nums[fastp], nums[slowp]
            fastp += 1
        ret = slowp + 1
    else:
        ret = 0
    return ret

def remove_duplicates(nums: List[int], k: int) -> int:
    """
    nums is sorted, k times
    """
    if len(nums) > 0:
        slowp = 0
        times = 1
        fastp = slowp + 1
        while fastp < len(nums):
            if nums[fastp] == nums[slowp] and times < k:
                slowp += 1
                nums[slowp], nums[fastp] = nums[fastp], nums[slowp]
                times += 1
            elif nums[fastp] > nums[slowp]:
                slowp += 1
                nums[slowp], nums[fastp] = nums[fastp], nums[slowp]
                times = 1
            fastp += 1
        ret = slowp + 1
    else:
        ret = 0
    return ret



def test():
    import numpy as np
    nums = list(np.random.randint(-100, 100, 250))
    nums.sort()
    print(remove_duplicates(nums, 2), nums)

if __name__=="__main__":
    test()
