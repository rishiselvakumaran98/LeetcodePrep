import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we add into heap with negative values to find the heaviest two stones
        stones = [-1*s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x-y)
        
        return abs(stones[0]) if stones else 0