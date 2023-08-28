class Solution:
    """
    We know N queens are going to be placed, we can place each queen by row 
    and each col as we know they cannot be in same row and col

    1. Maintain the column, the row is maintained by using for loop
    2. The diagonal is used by checking 
        - Negative Diagonals --> we are increasing col+=1 and row+=1 --> (r-c)
        - Positive Diagonals --> increasing cols += 1, decreasing row-=1 ==> Can be determined using (r+c)
    3. We keep track of the cols, posDiag, negDiag -> set()

    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # determined -> (r+c)
        negDiag = set() # (r-c)

        res= []

        board = [["."]*n for i in range(n)] # looks like -> [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

        def backtrack(r):
            # we reached the end of the back tracking
            if r == n:
                # each row is going to be a string
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n): # we are iterating col for each row
                # invalid conditions where the queen cannot be placed
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                # valid condition so we add it to the sets to keep track
                col.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)
                # We need to update the board itself
                board[r][c] = "Q"
                
                backtrack(r+1)
                
                # After backtracking we need to clean up the sets for new states generated
                # So we undo all the col addition to the sets
                col.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)
                # We clean the board as well
                board[r][c] = "."

        backtrack(0)
        return res

