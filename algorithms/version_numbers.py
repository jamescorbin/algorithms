
from typing import Tuple, List

def standardize(s: str) -> Tuple[int, int, int]:
    t = s.split(".")
    if len(t) == 3:
        ret = (int(t[0]), int(t[1]), int(t[2]))
    elif len(t) == 2:
        ret = (int(t[0]), int(t[1]), 0)
    elif len(t) == 1:
        ret = (int(t[0]), 0, 0)
    return ret

def sort_version_numbers(version1: str, version2: str) -> int:
    ver1 = standardize(version1)
    ver2 = standardize(version2)
    if ver1 > ver2:
        ret = 1
    elif ver2 > ver1:
        ret = -1
    else:
        ret = 0
    return ret

