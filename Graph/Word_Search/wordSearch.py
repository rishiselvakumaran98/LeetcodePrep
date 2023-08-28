from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Time: O(n * m * dfs -> len(word) -> 4^len(word) as we call dfs 4 times)
        Space: 
        We solve this using backtracking where we visit the neighboring nodes up, down, right, left to check if the word matches
        '''
        ROWS, COLS = len(board), len(board[0])
        path = set() # use a set to make sure we dont revisit the same rows and cols

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 
                or r >= ROWS or c >= COLS 
                or word[i] != board[r][c] 
                or (r,c) in path):  # all theses are invalid conditions
                return False
            
            path.add((r,c))
            # we need to find our target word one single time
            res = (dfs(r+1, c, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1)
                    )
            path.remove((r,c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False
         

