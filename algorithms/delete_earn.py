"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.
"""

import collections
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        occurences = collections.Counter(nums)
        numssort = sorted(list(occurences.keys()))
        n = len(numssort)
        dp = [0 for i in range(n)]
        p0 = 0
        while (p0 < n):
            t = occurences[numssort[p0]] * numssort[p0]
            if p0 == 0:
                dp[p0] = t
            elif p0 > 0:
                if numssort[p0 - 1] + 1 != numssort[p0]:
                    dp[p0] = dp[p0 - 1] + t
                else:
                    a = dp[p0 - 2] if p0 > 1 else 0
                    dp[p0] = max(dp[p0 - 1], a + t)
            p0 += 1
        return dp[-1]
