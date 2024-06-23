class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We are starting backwards and we will iterate through the array checking if current NUm < next Num
        # we can store the results into a DP array
        LIS = [1] * (len(nums) + 1)
        
        # We work backwards to set LIS and see if the element following are increasing
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)
            