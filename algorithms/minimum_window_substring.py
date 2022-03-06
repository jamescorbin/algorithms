import collections

def check_is_full(counter: collections.Counter,
                 tcounter: collections.Counter) -> bool:
    is_full = True
    for char, num in tcounter.items():
        if (char in counter) and (num <= counter[char]):
            pass
        else:
            is_full = False
            break
    return is_full

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        tcounter = collections.Counter(t)
        counter = collections.defaultdict(int)
        is_full = False
        deque = collections.deque()
        p = 0
        min_window = n + 1
        min_substring = ""
        while p < n:
            c = s[p]
            if c in tcounter:
                counter[c] += 1
                deque.append((p, c))
                while counter[deque[0][1]] > tcounter[deque[0][1]]:
                    a, b = deque.popleft()
                    counter[b] -= 1
                if not is_full:
                    is_full = check_is_full(counter, tcounter)
            if is_full:
                width = p + 1 - deque[0][0]
                if width < min_window:
                    min_window = width
                    min_substring = s[deque[0][0]: p + 1]
            p += 1
        return min_substring
