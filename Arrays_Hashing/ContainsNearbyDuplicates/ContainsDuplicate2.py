from typing import List


class Solution:
    # Questions to ask:
    # 1. What type of elements are going to be given in the input array
    # 2. Can there be more than 1 duplicate elements in the array?
    # 3. what are the max and min value of the integer in the array?
    # 4. Are the numbers within a certain range in the input array?

    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Most commonly used: Hashing technique in a set to hold the unique values and 
        if there are any duplicate values found between the values i the array and the hash set then return true
        '''
        unique_nums = set()

        # iterate through array to store and check if the number exist in set vs array
        for num in nums:
            if num in unique_nums:
                return True
            unique_nums.add(num)
        
        return False

    # Time Complexity -> O(N)
    # Space Complexity -> O(N) 

    ###########################################################################################################################
    # More Difficult version of the question
    # Find duplicate where number constraints in array and numbers are positive:
    # 1 <= nums.length <= 10^5
    # 1 <= nums[i] <= 10^5

    # There are two ways to solve this problem
        # 1. Negative marking
        # 2. Finding cycles in the list using Floyd's Algo

    def neg_marking(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] < 0:
                return index+1
            nums[index] *= -1
        return -1
    
    # Time Complexity -> O(N)
    # Space Complexity -> O(1) 

    def findCyclesFloydAlgo(self, nums: List[int]) -> bool:

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




        