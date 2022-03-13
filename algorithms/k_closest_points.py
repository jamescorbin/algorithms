from typing import List, Tuple
import heapq

def k_closest_points_origin(points: List[Tuple[int, int]],
                            k: int,
                            dist2 = lambda x: x[0]**2 + x[1]**2,
                            ) -> List[Tuple[int, int]]:
    """
    Remark: handle situation for k > n // 2
    """
    if k > len(points) // 2:
        dist_points = [(-dist2(x), x[0], x[1]) for x in points]
        heapq.heapify(dist_points)
        for i in range(len(points) - k):
            heapq.heappop(dist_points)
        ret = [(x[1], x[2]) for x in dist_points]
    else:
        dist_points = [(dist2(x), x[0], x[1]) for x in points]
        heapq.heapify(dist_points)
        k_closest = []
        for i in range(k):
            w = heapq.heappop(dist_points)
            k_closest.append((w[1], w[2]))
        ret = k_closest
    return ret

def test():
    import numpy as np
    points = np.random.randint(-1000, 1000, (100, 2))
    print(k_closest_points_origin(points, 90))

if __name__=="__main__":
    test()
