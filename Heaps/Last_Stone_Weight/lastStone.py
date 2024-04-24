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
    
    def lastStoneWeight_Alternative(self, stones: List[int]) -> int:
        # construct a max heap where we pop the first two stones
        # if diff == 0 then skip
        # else add diff into the heap again

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first_stone = -heapq.heappop(heap)
            sec_stone = -heapq.heappop(heap)

            diff = abs(first_stone-sec_stone)
            if diff == 0:
                continue
            heapq.heappush(heap, -diff)
        return -heap[0] if heap else 0