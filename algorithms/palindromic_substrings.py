"""
Python3 program to find palindromic
substrings of a string

Returns total number of palindrome
substring of length greater then
equal to 2
"""

def countPS(s: str):
    """
    O(n**2) time complexity, O(n**2) space
    Note all pallindromic substrings also are derivable from this
    """
    n = len(s)
    dp = [[0 for x in range(n)]
          for y in range(n)]
    is_pallidrome = [
        [False for x in range(n)]
         for y in range(n)]
    for i in range(n):
        is_pallindrome[i][i] = True
    for i in range(n - 1):
        if (s[i] == s[i + 1]):
            is_pallindrome[i][i + 1] = True
            dp[i][i + 1] = 1
    for width in range(2, n):
        for i in range(n - width):
            j = width + i
            if (s[i] == s[j] and is_pallindrome[i + 1][j - 1]):
                is_pallindrome[i][j] = True

            if (is_pallindrome[i][j] == True):
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] + 1 - dp[i + 1][j - 1])
            else:
                dp[i][j] = (dp[i][j - 1] +
                            dp[i + 1][j] - dp[i + 1][j - 1])
    return dp[0][n - 1]

class Solution:
    def countSubstrings(self, s: str) -> int:
        # apply Manacher's Algorithm
        s_ext = "|".join([c for c in s])
        radii = [0 for x in s_ext]
        center = 0
        radius = 0
        while center < len(s_ext):
            while (
                    (center - (radius + 1) >= 0)
                    and (center + (radius + 1) < len(s_ext))
                    and (s_ext[center - (radius + 1)] == s_ext[center + (radius + 1)])):
                radius += 1
            radii[center] = radius
            c0 = center
            r0 = radius
            center += 1
            radius = 0
            while (center <= c0 + r0):
                c_max = c0 - (center - c0)
                r_max = r0 - (center - c0)
                if (radii[c_max] < r_max):
                    radii[center] = radii[c_max]
                    center += 1
                elif (radii[c_max] > r_max):
                    radii[center] = r_max
                    center += 1
                else:
                    radius = r_max
                    break
        odds = sum([x // 2 + 1 for x in radii[::2]])
        evens = sum([(x + 1) // 2 for x in radii[1::2]])
        return odds + evens


# Driver Code
if __name__ == "__main__":
    str = "abaab"
    n = len(str)
    print(CountPS(str, n))
