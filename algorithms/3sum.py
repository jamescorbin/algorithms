from typing import List, Tuple, Set
import collections

def find_2sum(nums: List[int], target: int) -> Set[Tuple[int]]:
    """
    O(n) time, O(n) space
    """
    indexer = collections.defaultdict(list)
    for i, x in enumerate(nums):
        indexer[x].append(i)
    ret = set()
    for psumm, idxs in indexer.items():
        if psumm >= target:
            if target - psumm in indexer:
                if psumm == target - psumm:
                    if len(idxs) > 1:
                        ret.add((target - psumm, psumm))
                else:
                    ret.add((target - psumm, psumm))
    return ret

def find_3sum(nums: List[int], target: int) -> Set[Tuple[int]]:
    """
    Find unique triplets (x0, x1, x2) where x0 <= x1 <= x2
        such that x0 + x1 + x2 = target
    O(n2) time, O(1) space
    """
    n = len(nums)
    nums.sort()
    p0 = 0
    ret = set()
    while p0 < n - 2:
        x0 = nums[p0]
        p2 = n - 1
        p1 = p0 + 1
        while (p1 < p2):
            while (p1 < p2) and (x0 + nums[p1] + nums[p2] < target):
                p1 += 1
            if (x0 + nums[p1] + nums[p2] == target) and (p1 != p2):
                ret.add((x0, nums[p1], nums[p2]))
            p2 -= 1
        p0 += 1
    return ret

def find_3sum_sorted(nums: List[int], target: int,
                     start_idx: int=0) -> Set[Tuple[int]]:
    """
    find_3sum without calling sort
        and an start index argument
        which is used for find_4sum_const_space
    """
    n = len(nums)
    p0 = start_idx
    ret = set()
    while p0 < n - 2:
        x0 = nums[p0]
        p2 = n - 1
        p1 = p0 + 1
        while (p1 < p2):
            while (p1 < p2) and (x0 + nums[p1] + nums[p2] < target):
                p1 += 1
            if (x0 + nums[p1] + nums[p2] == target) and (p1 != p2):
                ret.add((x0, nums[p1], nums[p2]))
            p2 -= 1
        p0 += 1
    return ret

def find_4sum_const_space(nums: List[int],
                          target: int,
                          ) -> Set[Tuple[int]]:
    """
    O(n3) time, O(1) space
    """
    ret = set()
    nums = nums.sort()
    for i in range(nums):
        ret = ret | find_3sum_sorted(nums, target - nums[i], i + 1)
    return ret

def find_4sum_fast(nums: List[int],
                   target: int,
                   ) -> Set[Tuple[int]]:
    """
    O(n2) time, O(n) space
    """
    n = len(nums)
    indexer = collections.defaultdict(list)
    for i in range(n - 1):
        for j in range(i + 1, n):
            indexer[nums[i] + nums[j]].append((i, j))
    ret = set()
    for psumm, idxs in indexer.items():
        if psumm >= target:
            if target - psumm in indexer:
                idxs2 = indexer[target - psumm]
                for pair1 in idxs:
                    for pair2 in idxs2:
                        nset = set([pair1[0], pair1[1], pair2[0], pair2[1]])
                        if len(nset) == 4:
                            group = sorted([nums[w] for w in nset])
                            ret.add(group)
    return ret


if __name__=="__main__":
    import random
    nums = [random.randint(-20, 20) for i in range(30)]
    target = random.randint(-20, 20)
    print(nums)
    print(target)
    print(find_3sum(nums, target))



