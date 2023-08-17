from typing import List
class Solution:
    def findDuplicate_Neg_Marking(self, nums: List[int]) -> int:
        # 1. Using Neg Marking
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if (nums[index] < 0):
                return (index + 1)
            else:
                nums[index] *= -1
        return -1
    
    def findDuplicate_Find_Cycle(self, nums: List[int]) -> int:
        # 2. Find cycle using Floyd Algo
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
print(Solution().findDuplicate_Find_Cycle([1,1,2]))