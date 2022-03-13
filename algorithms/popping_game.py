from typing import List

def popping_game(nums: List[int]) -> int:
    n = len(nums)
    memo = [[0 for i in range(n)] for j in range(n)]
    for window in range(n):
        for lp in range(n - window):
            rp = lp + window
            rval = nums[rp + 1] if rp + 1 < n else 1
            lval = nums[lp - 1] if lp - 1 > -1 else 1
            for i in range(lp, rp + 1):
                ival = lval * nums[i] * rval
                a = memo[lp][i - 1] if i - 1 >= lp else 0
                b = memo[i + 1][rp] if i + 1 <= rp else 0
                tmp = ival + a + b
                memo[lp][rp] = (tmp
                                if tmp >= memo[lp][rp]
                                else memo[lp][rp])
    return memo[0][n-1]

def test():
    nums = [3, 1, 5, 8]
    print(popping_game(nums))

if __name__=="__main__":
    test()
