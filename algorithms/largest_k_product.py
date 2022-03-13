import heapq
from typing import List

def largest_k_product(nums: List[int], k: int) -> int:
    """
    Assume nums and k are positive.
    Forgo case k > len(nums) // 2
    """
    heap = nums[:k]
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
    prod = 1
    for num in heap:
        prod *= num
    return prod

def test():
    import numpy as np
    arr = list(np.random.randint(1, 2000, 100))
    print(largest_k_product(arr, 4))

if __name__=="__main__":
    test()

