from typing import List

EMPTY = -1

def switch(nums: List[int], val: int, idx: int) -> None:
    n = len(nums)
    if val > n:
        nums[idx] = EMPTY
    elif nums[val - 1] == val:
        pass
    else:
        tmp = nums[val - 1]
        nums[val - 1] = val
        nums[idx] = tmp
        if (tmp > 0) and (tmp < n + 1):
            switch(nums, tmp, idx)

def find_first_missing_positive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        if nums[i] == i + 1:
            pass
        else:
            switch(nums, nums[i], i)
    ret = n + 1
    for idx, j in enumerate(nums):
        if j != idx + 1:
            ret = idx + 1
            break
    return ret

if __name__=="__main__":
    cases = [
            [2, 1, 0],
            [3, 4, -1, 1],
            [3, 4, 6, 1],
            [1, 2, 3, 4, 6, 5],]
    for case in cases:
        print(case, find_first_missing_positive(case))
