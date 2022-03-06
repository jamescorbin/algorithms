from typing import List

def _merge(left: List[float], right: List[float]):
    ret = []
    lp = 0
    rp = 0
    while (len(left) > lp) and (len(right) > rp):
        x1 = left[lp]
        x2 = right[rp]
        if x1 <= x2:
            nxt = x1
            lp +=1
        else:
            nxt = x2
            rp += 1
        ret.append(nxt)
    if (len(left) > lp):
        ret.extend(left[lp:])
    if (len(right) > rp):
        ret.extend(right[rp:])
    return ret

def merge_sort(arr: List[float]):
    l = len(arr)
    if l > 1:
        ret = _merge(merge_sort(arr[:l//2]), merge_sort(arr[l//2:]))
    else:
        ret = x
    return ret
