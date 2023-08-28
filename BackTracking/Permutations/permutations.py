from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res= []
        def dfs(i, subset):
            # if the len of subset or in this case the index == n
            # then add the subset into the result and then return to backtrack to next state
            if i == n:
                res.append(subset[:])
                return

            for j in range(i, n):
                # we keep swapping the indexes in nums to add unique number
                # into the subset
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1, subset+[nums[i]])
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0, [])
        return res