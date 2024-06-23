class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowVisited, colVisited, subGrid = defaultdict(set), defaultdict(set), defaultdict(set)
        ROWS, COLS = len(board), len(board[0])
        # prepopulate the Visited sets with the existing cell values
        for r in range(ROWS):
            for c in range(COLS):
                cell = board[r][c]
                if cell != ".":
                    box_value = (r//3)*3 + (c//3)
                    rowVisited[r].add(cell)
                    colVisited[c].add(cell)
                    subGrid[box_value].add(cell)


        def isValid(r, c, value):
            box_value = (r//3)*3 + c//3
            return value not in rowVisited[r] and value not in colVisited[c] and value not in subGrid[box_value]

        def solve(r, c):
            # Goal: If we reach the end of row or col then we return back from the function call
            # we check only for roww as row -1 as we are incrementing it below and need to prevent 
            # index outofbounds exception
            if r == ROWS-1 and c == COLS:
                return True
            # If we simpily reached end of col then we increment the row to move to the next
            elif c == COLS:
                c = 0
                r += 1
            # if the current grid is already filled then move to the next state
            if board[r][c] != ".":
                return solve(r,c+1)
            box_value = (r//3)*3 + c//3
            # We Make the choice to add the coordinate into the board
            
            for value in range(1, ROWS+1):
                # we check if the particular value can be placed in the cell
                value = str(value)
                if isValid(r, c, value):
                    board[r][c] = value
                    rowVisited[r].add(value)
                    colVisited[c].add(value)
                    subGrid[box_value].add(value)
                
                    if solve(r,c+1):
                        return True

                    # backtrack on the solution
                    board[r][c] = "."
                    rowVisited[r].remove(value)
                    colVisited[c].remove(value)
                    subGrid[box_value].remove(value)

            return False
        solve(0,0)






