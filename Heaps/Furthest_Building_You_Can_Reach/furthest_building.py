from collections import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # We max heap to keep track of the largest climb needed for the reaching the next building
        # we then use ladders for those largest climb and then use bricks for the remaining ones
        # this will enable us to tabulate the most optimal solution to the problem
        heap = []

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]

            if diff <= 0:
                continue

            bricks -= diff
            heapq.heappush(heap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)
        
        return len(heights)-1


