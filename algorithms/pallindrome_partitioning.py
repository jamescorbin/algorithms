from typing import List

def make_pallindromic_substring_data(s: str) -> List[List[bool]]:
    n = len(s)
    is_pallindrome = [[False for i in range(n)]
                      for j in range(n)]
    for i in range(n):
        is_pallindrome[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_pallindrome[i][i + 1] = True
    for width in range(2, n):
        for i in range(n - width):
            j = width + i
            if s[i] == s[j] and is_pallindrome[i + 1][j - 1]:
                is_pallindrome[i][j] = True
    return is_pallindrome

def recurrsively_build(
        s: str,
        is_pallindrome: List[List[bool]],
        prefix: List[str],
        idx: int) -> List[List[str]]:
    ret = []
    if idx == len(s):
        ret = [prefix]
    else:
        for nxt, is_pall in enumerate(is_pallindrome[idx]):
            if nxt >= idx and is_pall:
                new_prefix = list(prefix) + [s[idx:nxt+1]]
                ret.extend(recurrsively_build(
                                            s,
                                            is_pallindrome,
                                            new_prefix,
                                            nxt + 1))
    return ret

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        O(n**2)
        """
        is_pallindrome = make_pallindromic_substring_data(s)
        ret = recurrsively_build(s,
                                 is_pallindrome,
                                 list(),
                                 0)
        return ret
