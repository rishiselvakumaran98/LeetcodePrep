import heapq
class KthLargest:
    # We use a heap to keep track of the kLargest element
    # Idea is:
    # Initialize a heap with the existing list
    # Assign self.k to k
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        # we need to pop from heap until its size is 
        # what we need to get kLargest from index 0
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        
    
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]