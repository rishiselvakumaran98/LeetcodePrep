class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Backtracking -> Generate all possible solutions recursively
        # and we bound them using base conditions for the 
        # Base condition -> check if the len(sublist) == k -> add to the res and then return
        #                -> Pass in a parameter (sum) which is recursively called and added with the current element that we add to the sublist
        #                -> if sum == n: add to the res
        # Remaining parts of the backtrack function
            # setup a for loop for range 1-9
            # recursively call the function with i thats passed
        # Time -> O(n^k)
        res = []
        # helper method that backtrack to generate and bound states
        def backtrack(sublist, x, sum):
            # valid condition
            if len(sublist) == k and sum == n:
                res.append(sublist[:])
                return
            
            if len(sublist) == k or sum > n:
                return
            
            for i in range(x,10):
                sublist.append(i) #[1, 2, 3]
                backtrack(sublist, i+1, sum+i)
                sublist.pop()
        
        backtrack([], 1, 0)
        return res
