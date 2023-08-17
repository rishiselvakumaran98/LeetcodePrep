class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # first sort the numbers to make it like a two sum sorted input problem

        # Construct a method to pass in a pivot to each of the two points AKA j and then check if nums[i] + nums[j] + nums[k] == 0

        nums.sort()
        result = []

        # Two_sum_sorted method
        def Two_sum_sorted(i):
            l = i+1; r = len(nums)-1
            while(l < r):
                sum_ = nums[l] + nums[i] + nums[r]
                if sum_ < 0:
                    l +=1
                elif sum_ > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip internal duplication within the 
                    while l <r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            Two_sum_sorted(i)
        return result