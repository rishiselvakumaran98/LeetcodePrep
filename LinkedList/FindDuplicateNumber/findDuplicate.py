from typing import List

class Solution:
    # There are two ways to solve this problem:
        # 1. Negative Marking
    def findDuplicate_NegativeMarking(self, nums):
        index = 0

        for i in range(len(nums)):
            index = abs(nums[i])

            if (nums[index] < 0):
                return index
            else:
                nums[index] *= -1
        
        return -1
    
        # 2. Fast and slow pointers
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = nums[0]
        fast = nums[nums[0]]

        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow

