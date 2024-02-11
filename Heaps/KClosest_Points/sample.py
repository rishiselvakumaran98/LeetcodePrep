from typing import List
import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # we add the distance between the origin and points into a heap
        # and then return the smallest one
        heap = []

        for point in points:
            x,y = point[0], point[1]
            dist = math.sqrt(x**2+y**2) 
            heap.append([dist, point])

        heapq.heapify(heap)
        rc = []
        for _ in range(k):
            dist, point = heapq.heappop(heap)
            rc.append(point)
        return rc
