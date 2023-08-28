from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Since we are partitioning all lowercase letters we can use it to construct
        # a palindrome helper method
        def is_palindrome(string):
            l, r = 0, len(string)-1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        subset = []
        def backtrack(i):
            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    subset.append(s[i:j+1])
                    backtrack(j+1)
                    subset.pop()
        backtrack(0)
        return res
    