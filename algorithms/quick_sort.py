from typing import List

def quick_sort(arr: List[float]):
    if len(arr) > 0:
        ret = _pivot(arr[0], arr[1:])
    else:
        ret = x
    return ret

def _pivot(arr: List[float], pivot: float):
    ret = []
    if len(arr) > 0:
        left = []
        right = []
        while len(arr) > 0:
            v = arr.pop()
            if v >= pivot:
                right.append(v)
            else:
                left.append(v)
        if len(left) > 0:
            ret = ret + _pivot(left[0], left[1:])
        ret = ret + [pivot]
        if len(right) > 0:
            ret = ret + _pivot(right[0], right[1:])
    else:
        ret = [pivot]
    return ret
