class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if we get all positive numbers of product is going to keep increasing
        # If we get all negative numbers then the product is going to be 
        # If we get all negatives the sign is alternating
        # Even though we keep looking for the max we still have to keep track of the min
        # This is done to account for the alternating signs and we use the min or max numbers to 
        # We need to by default set the res to max(nums)
        res = max(nums) # 0 -> [-1]
        curMin, curMax = 1,1
        for n in nums:
            if n == 0: # we dont want to mess up our curMin and max product
                curMin, curMax = 1,1
                continue
            temp = n * curMax
            curMax = max(temp, n * curMin, n) # example if currMin or currMax = -1 and n = 8, then we want the max to be set to 8
            curMin = min(temp, n * curMin, n) #[-1, -8] if we multiply we get positive a
            res = max(res, curMax)
        return res
        



             