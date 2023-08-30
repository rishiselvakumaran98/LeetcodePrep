from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, end, substring):
            # Valid condition where we stop and append the substr
            if open == end == n:
                res.append(substring)
                return
            
            if open < n:
                substring += "("
                backtrack(open+1, end, substring)
                substring = substring[:-1]

            if end < open:
                substring += ")"
                backtrack(open, end+1, substring)
                substring = substring[:-1]
        backtrack(0,0,"")
        return res