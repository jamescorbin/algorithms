from typing import List
import heapq

def get_rolling_median(nums: List[int]) -> List[float]:
    lower = []
    middle = []
    upper = []
    results = []
    for i in range(len(nums)):
        if i % 2 == 0:
            if i == 0:
                middle.append(nums[i])
            else:
                lub = heapq.heappop(upper)
                glb = -1 * heapq.heappop(lower)
                x = nums[i]
                if x < glb:
                    heapq.heappush(lower, -1 * x)
                    heapq.heappush(upper, lub)
                    middle.append(glb)
                elif x > lub:
                    heapq.heappush(lower, -1 * glb)
                    heapq.heappush(upper, x)
                    middle.append(lub)
                else:
                    heapq.heappush(lower, -1 * glb)
                    heapq.heappush(upper, lub)
                    middle.append(x)
            results.append(middle[0])
        else:
            x = nums[i]
            x0 = middle.pop()
            if x < x0:
                heapq.heappush(lower, -1 * x)
                heapq.heappush(upper, x0)
            else:
                heapq.heappush(lower, -1 * x0)
                heapq.heappush(upper, x)
            results.append((upper[0] - lower[0]) / 2)
    return results

def test():
    import numpy as np
    nums = list(np.random.randint(-100, 100, 20))
    print(nums)
    print(get_rolling_median(nums))

if __name__=="__main__":
    test()
