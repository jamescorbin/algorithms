"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""
import timing

class Solution():
    @timing.timing
    def lengthOfLastWord_v1(self, s: str) -> int:
        n = len(s)
        p = n - 1
        strip = False
        cont = True
        count = 0
        while (p >= 0 and cont):
            if s[p] != ' ':
                strip = True
                p -= 1
                count += 1
            elif strip:
                cont = False
            else:
                p -= 1
        return count

    @timing.timing
    def lengthOfLastWord_v2(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

    @timing.timing
    def lengthOfLastWord_v3(self, s: str) -> int:
        n = len(s)
        p = n - 1
        cont = True
        count = 0
        while (p >= 0 and s[p]==' '):
            p -= 1
        while (p >= 0 and cont):
            if s[p] != ' ':
                p -= 1
                count += 1
            else:
                cont = False
        return count



def testCases() -> None:
    tests = [("Hello World", 5),
             ("Hello World  ", 5)]
    sol = Solution()
    for i, (inp, out) in enumerate(tests):
        v = sol.lengthOfLastWord_v1(inp)
        w = v == out
        print(f"{i}, {w}")
        v = sol.lengthOfLastWord_v2(inp)
        w = v == out
        print(f"{i}, {w}")
        v = sol.lengthOfLastWord_v3(inp)
        w = v == out
        print(f"{i}, {w}")

if __name__=="__main__":
    testCases()
