class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        p0 = 0
        p1 = n - 1
        mx = min(height[p0], height[p1]) * (p1 - p0)
        while p1 > p0:
            if height[p0] < height[p1]:
                p0 += 1
            else:
                p1 -= 1
            tmp = min(height[p0], height[p1]) * (p1 - p0)
            if tmp > mx:
                mx = tmp
        return mx
