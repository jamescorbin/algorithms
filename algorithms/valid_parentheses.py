"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        a1, a2 = "(", ")"
        b1, b2 = "[", "]"
        c1, c2 = "{", "}"
        stack = []
        p = 0
        n = len(s)
        ret = True
        if n > 0:
            while (p < n):
                c = s[p]
                if c in (a2, b2, c2):
                    if len(stack) > 0:
                        w = stack[-1]
                        if w == a1 and c == a2:
                            stack.pop()
                        elif w == b1 and c == b2:
                            stack.pop()
                        elif w == c1 and c == c2:
                            stack.pop()
                        else:
                            ret = False
                            break
                    else:
                        ret = False
                        break
                else:
                    stack.append(c)
                p += 1
            if (p == n) and len(stack) == 0:
                ret = True
            else:
                ret = False
        else:
            ret = True
        return ret
