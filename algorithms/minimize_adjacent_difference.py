"""
Rearrange array such that difference
between any two elements is minimized

Solution: rearrange into sinusoid of period frequency 1
"""

from typing import List

def minimize_adjacent_difference(nums: List[int]) -> int:
    nums.sort()
    if len(nums) > 1:
        n = len(nums)
        minimum = nums[0]
        maximum = nums[-1]
        left_arm = [nums[i] for i in range(1, n, 2)
                    if (i != n - 1)]
        right_arm = [nums[i] for i in range(n - 1, 0, -1)
                     if (i % 2 == 0) and (i != n - 1)]
        sinusoid = [minimum] + left_arm + [maximum] + right_arm + [minimum]
        val = float("-inf")
        for i, x in enumerate(sinusoid[:-1]):
            k = (sinusoid[i + 1] - x
                 if sinusoid[i + 1] - x > 0
                 else x - sinusoid[i + 1])
            if k > val:
                val = k
        ret = val
    else:
        ret = 0
    return ret

def test():
    import numpy as np
    nums = np.random.randint(-50, 50, 30)
    print(nums)
    print(minimize_adjacent_difference(nums))

if __name__=="__main__":
    test()

