class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # If we meet all the three requirements we add a number to the board
        # Then we move tro the next state and keep repeating for numbers 1-9
        # we need to declare data structures that we can dynamically add and use to check if the coordinates exist in O(1) time
        rows, cols, subgrids = defaultdict(set), defaultdict(set), defaultdict(set)
        q = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    subgrids[(r//3, c//3)].add(board[r][c])
                else: # we add the empty spots to the queue to be used later when processing
                    q.append((r,c))

        
        def backtrack():
            if not q:
                return True
            r,c = q.pop()
            b = (r//3, c//3)
            for num in range(1,10):
                num = str(num)
                if num not in rows[r] and num not in cols[c] and num not in subgrids[b]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrids[b].add(num)
                    if backtrack():
                        return True
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    subgrids[b].remove(num)
            q.append((r,c))
            return False
        
        backtrack()
