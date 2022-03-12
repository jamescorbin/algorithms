from typing import List, Optional

def search(arr: List[int],
           target: int,
           lp: int,
           rp: int) -> int:
    """
    If not found, return smallest index of value or last element
    """
    mp = (rp - lp) // 2 + lp
    if lp == rp:
        ret = lp
    elif arr[mp] == target:
        ret = mp
    elif arr[mp] < target:
        ret = search(arr, target, mp + 1, rp)
    else:
        ret = search(arr, target, lp, mp)
    return ret


def test_search():
    import numpy as np
    arr = sorted(np.random.randint(-100, 100, 100))
    print(arr)
    idx = search(arr, -101, 0, 99)
    val = arr[idx] if (idx >= 0) and (idx < len(arr)) else "miss"
    print(idx, val)

if __name__=="__main__":
    test_search()

