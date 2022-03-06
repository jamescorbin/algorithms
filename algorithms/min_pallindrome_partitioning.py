from typing import List

def make_pall_indicator(s: str) -> List[List[bool]]:
    n = len(s)
    is_pall = [[False for i in range(n)]
                for j in range(n)]
    for i in range(n):
        is_pall[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_pall[i][i + 1] = True
    for width in range(2, n):
        for i in range(n - width):
            j = i + width
            if s[i] == s[j] and is_pall[i + 1][j - 1]:
                is_pall[i][j] = True
    return is_pall

def search_dp(
            is_pall: List[List[bool]],
            ):
    n = len(is_pall)
    cut = [n for i in range(n)]
    if is_pall[0][n - 1]:
        ret = 0
    else:
        for i in range(n):
            if is_pall[0][i]:
                cut[i] = 0
            else:
                cut[i] = min(cut[j - 1] + 1
                         for j in range(1, i + 1)
                         if is_pall[j][i])
        ret = cut[n - 1]
    return ret


class Solution:
    def minCut(self, s: str) -> int:
        is_pall = make_pall_indicator(s)
        ret = search_dp(is_pall)
        return ret

if __name__=="__main__":
    s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    print(Solution().minCut(s))
