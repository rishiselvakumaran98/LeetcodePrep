from typing import List

class Solution:
    '''
    Time: O(n*2^n) --> Since we are finding a subset state for each of the number in array = 2^n
                        Then we try to add them each to a subset like [1,2] or [2,3] which multiplies by n
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we dont care about the ordering but we do not want to duplicate any subset addition
        res = []

        subset = []
        def dfs(i): # i tells us which element we are currently visiting
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1) # for this recursive call we pass in the filled subset
            # decision to not include nums[i]
            subset.pop()
            dfs(i+1) # for this recursive call we pass in the empty subset

        dfs(0)
        return res


