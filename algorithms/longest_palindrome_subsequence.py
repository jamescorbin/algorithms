class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s = "|".join([c for c in s])
        n = len(s)
        prememo = [1 if j % 2 == 0 else 0 for j in range(n)]
        for window in range(1, n//2 + 1):
            memo = [1 if j % 2 == 0 else 0 for j in range(n)]
            for center in range(window, n-window):
                lp = center - window
                rp = center + window
                if (s[lp] != '|') and (s[lp] == s[rp]):
                    memo[center] = prememo[center] + 2
                else:
                    memo[center] = prememo[center]
                memo[center] = max([
                            memo[center],
                            prememo[center + 1],
                            prememo[center - 1]])
            prememo = memo
        return memo[n//2]

def test():
    sol = Solution()
    s = "bbbab"
    print(sol.longestPalindromeSubseq(s))

if __name__=="__main__":
    test()

