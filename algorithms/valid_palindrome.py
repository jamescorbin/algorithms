"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

def valid_k_palindrome_edit_distance(s: str, k: int) -> int:
    """
    Time: O(n * n), Space: O(n * n),
    Use edit distance from reversed string.
    k-plaindrome takes at most 2k edits.
    """
    n = len(s)
    s_rev = "".join(reversed([c for c in s]))
    old_memo = [m for m in range(n + 1)]
    memo = [m for m in range(n + 1)]
    for i in range(1, n + 1):
        memo = [m for m in range(n + 1)]
        for j in range(1, n + 1):
            if s[i - 1] == s_rev[j - 1]:
                memo[j] = old_memo[j - 1]
            else:
                memo[j] = 1 + min(
                            memo[j - 1],
                            old_memo[j])
        old_memo = memo
    return memo[-1]

def valid_k_palindrome(s: str, k: int) -> bool:
    return valid_k_palindrome_edit_distance(s, k) <= 2 * k

def valid_k_palindrome_recursive(
        s: str,
        idx_l: int,
        idx_r: int,
        count: int) -> bool:
    """
    K pallindrom problem for small k and
    tighter memory.
    Could be comparable to DP with function cache
    """
    ret = False
    if count < 0:
        ret = False
    else:
        while idx_l < idx_r:
            if s[idx_l] == s[idx_r]:
                idx_l += 1
                idx_r -= 1
            else:
                ret = (ret
                       | check_with_counter(s, idx_l + 1, idx_r, count - 1)
                       | check_with_counter(s, idx_l, idx_r - 1, count - 1))
                break
    if (idx_l >= idx_r) and (count >= 0):
        ret = True
    return ret

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        pl = 0
        pr = n - 1
        count = 1
        return check_with_counter(s, pl, pr, count)

if __name__=="__main__":
    s = "acdcb"
    k = 2
    print(valid_k_palindrome(s, k))



