from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we construct a Max Heap where the heaviest stone is at index 0
        stones = [-1*s for s in stones]
        heapq.heapify(stones)

        # we use a loop to make the stones fight each other until there is one left
        while len(stones) > 1:
            y = -1*heapq.heappop(stones)
            x = -1*heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, -1*(y-x))

        # There could be no stones left and in that case we return 0
        return abs(stones[0]) if stones else 0

