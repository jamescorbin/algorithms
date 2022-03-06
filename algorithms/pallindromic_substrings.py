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


# Driver Code
if __name__ == "__main__":
    str = "abaab"
    n = len(str)
    print(CountPS(str, n))
