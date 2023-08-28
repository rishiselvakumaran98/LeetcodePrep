from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []
        def dfs(i, total):
            if total == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or total > target:
                return
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])
            subset.pop()

            # skip the duplicates in the array
            j = i
            while j+1 < len(candidates) and candidates[j] == candidates[j+1]:
                j += 1
            dfs(j+1, total)
        
        dfs(0, 0)
        return res