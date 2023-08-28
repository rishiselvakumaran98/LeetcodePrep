class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, total):
            # end condition
            if i >= len(candidates) or total > target:
                return
            if total == target:
                copy = subset.copy()
                res.append(copy)
                return
            subset.append(candidates[i])
            dfs(i, total+candidates[i])

            subset.pop()
            dfs(i+1, total)
        dfs(0,0)
        return res