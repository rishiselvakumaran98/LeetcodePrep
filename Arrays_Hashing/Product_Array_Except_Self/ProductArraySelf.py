class Solution:
    def productExceptSelf(self, nums):
        result_array = [1]*len(nums)
        left = 1
        right = 1
        for i in range(len(nums)):
            j = len(nums)-i-1
            result_array[i] *= left
            left *= nums[i]
            result_array[j] *= right
            right *= nums[j]
        return result_array

