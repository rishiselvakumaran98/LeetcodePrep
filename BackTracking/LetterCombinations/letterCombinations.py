class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterPad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res= []
        stack = []

        def backtrack(i):
            if len(stack) == len(digits):
                res.append("".join(stack[:]))
                return
            
            if i >= len(digits):
                return
            
            for c in letterPad[digits[i]]:
                stack.append(c)
                backtrack(i+1)
                stack.pop()

        backtrack(0)
        return res