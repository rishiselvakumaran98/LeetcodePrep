from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # make sure nums is sorted to ensure that we can skip duplicates
        n = len(nums)
        def dfs(i, subset):
            if i == n:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)
            subset.pop()

            # skip duplicates from the nums array
            while i + 1 < n and nums[i] == nums[i+1]:
                i +=1 
            dfs(i+1, subset)
        dfs(0, [])
        return res