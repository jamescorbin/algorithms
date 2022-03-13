from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_width = [0 for i in range(n)]
        stack = []
        for i in range(n):
            h = heights[i]
            start = i
            while stack and h <= heights[stack[-1]]:
                start = stack.pop()
            left_width[i] = ((i - start) + left_width[start])
            stack.append(i)
        right_width = [0 for i in range(n)]
        stack = []
        for i in reversed(range(n)):
            h = heights[i]
            start = i
            while stack and h <= heights[stack[-1]]:
                start = stack.pop()
            right_width[i] = ((start - i) + right_width[start])
            stack.append(i)
        area = [heights[i] * (left_width[i] + right_width[i] + 1)
                for i in range(n)]
        return max(area)
