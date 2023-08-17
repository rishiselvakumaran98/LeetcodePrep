class Solution:
    '''
        More optimized solution:
        Time: O(n)
        Space: O(n)
    '''
    def longestConsecutive(self,nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        unique_set = set(nums)
        longest = 1
        for num in nums:
            if num-1 not in unique_set:
                next_num = num+1
                while next_num in unique_set:
                    next_num += 1
                longest = max(longest, next_num-num)
        return longest
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
        Most brute force method to do it
        Time: O(nlogn) for sorting using TimSort 
        Space: O(n) for sorting in worst case
    '''
    def longestConsecutiveBF(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        current = 1
        longest = 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                current += 1
            elif nums[i+1]-nums[i] == 0:
                continue
            else:
                current = 1
            longest = max(longest, current)
                
        return longest
    '''
    
    '''