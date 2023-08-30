import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Compute the distance and add them into the heap based on that
        dist_heap = []
        for point in points:
            distance = math.sqrt((point[0]**2) + (point[1]**2))
            dist_heap.append([distance, point])
        
        # Heapify the dist_heap
        heapq.heapify(dist_heap)
        rc = []

        for i in range(k):
            dist, point = heapq.heappop(dist_heap)
            rc.append(point)
        
        return rc