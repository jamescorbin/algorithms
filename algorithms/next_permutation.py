from typing import List

def find_swap(nums: List[int], start_idx: int) -> None:
    idx = start_idx + 1
    min_val, min_idx = nums[idx], idx
    while idx < len(nums):
        if (nums[idx] <= min_val) and (nums[start_idx] < nums[idx]):
            min_val, min_idx = nums[idx], idx
        idx += 1
    nums[start_idx], nums[min_idx] = min_val, nums[start_idx]

def reverse_to_right(nums: List[int], idx: int) -> None:
    n = len(nums)
    idxl = idx + 1
    idxr = n - 1
    while idxl < idxr:
        nums[idxl], nums[idxr] = nums[idxr], nums[idxl]
        idxl += 1
        idxr -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Parse from back find decreasing pair (n, m).
        Take the smaller number of the pair n,
        Find smallest number to the right of it k.
        Swap those n <-> k.
        Then reverse the remaining elements to the right of k.

        E.g.:
        [3, 5, 4, 2, 1] -> [4, 5, 3, 2, 1] -> [4, 1, 2, 3, 5]

        If no decreasing element, swap last non-identical pair:
        [1, 2, 3] -> [1, 3, 2]
        """
        n = len(nums)
        p = n - 2
        while p >= 0 and nums[p] >= nums[p + 1]:
            p -= 1
        if p < 0:
            reverse_to_right(nums, p)
        elif n > 1:
            find_swap(nums, p)
            reverse_to_right(nums, p)

def testing():
    arr = [3, 5, 4, 2, 1]
    print(arr)
    Solution().nextPermutation(arr)
    print(arr)
    arr = [1, 2, 3]
    print(arr)
    Solution().nextPermutation(arr)
    print(arr)
    arr = [2, 2, 3]
    print(arr)
    Solution().nextPermutation(arr)
    print(arr)
    arr = [2]
    print(arr)
    Solution().nextPermutation(arr)
    print(arr)
    arr = [2, 3, 1, 3, 3]
    print(arr)
    Solution().nextPermutation(arr)
    print(arr)

if __name__=="__main__":
    testing()
