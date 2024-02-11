from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we use a heap list to add the elements of nums into it
        # once the len of list gets bigger than k we start to pop from it
        # THis would cause the runtime to be O(N(log(k)))
        heap = []
        for num in nums:
            heapq.heappush(nums, num)
            if len(heap) > k:
                heapq.heappop(nums)
        return heap[0]

    def findKthLargest_QuickSelect(self, nums: List[int], k: int) -> int:
        