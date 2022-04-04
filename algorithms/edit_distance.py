import typing

def get_edit_distance(s1: str, s2:str) -> int:
    """
    Hamming distance
    O(n*m) time, O(n) space
    """
    if len(s2) > len(s1):
        s1, s2 = s2, s1
    l1, l2 = len(s1), len(s2)
    memo = [i for i in range(l1 + 1)]
    pmemo = [i for i in range(l1 + 1)]
    for i2 in range(1, l2 + 1):
        pmemo = memo
        memo = [i for i in range(l1 + 1)]
        c2 = s2[i2-1]
        for i1 in range(1, l1 + 1):
            c1 = s1[i1-1]
            if c1 == c2:
                memo[i1] = pmemo[i1 - 1]
            else:
                deletion = pmemo[i1]
                insertion = memo[i1 - 1]
                replacement = pmemo[i1 - 1]
                memo[i1] = 1 + min(
                                    replacement,
                                    deletion,
                                    insertion,)
    return memo[-1]

if __name__=="__main__":
    cases = [
        ("b", "a"),
        ("ba", "a"),
        ("horse", "ros"),]
    for s1, s2 in cases:
        print(s1, s2, get_edit_distance(s1, s2))
