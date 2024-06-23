class TicTacToe:
    def __init__(self, n) -> None:
        self.board = [["" for _ in range(n)] for _ in range(n)]
        self.n = n
        self.rowSum = [0]*n
        self.colSum = [0]*n
        self.diagSum = 0
        self.revDiagSum = 0
        self.winner = 0
    
    def move(self, player, row, col)->int:
        """
        The method makes a move on the board and returns the winner if the move is a winning move.
        param: player is either 0 or 1
        param: row is the move's row index
        param: col is the move's col index
        @return winner +1 if the first player, -1 if second player and zero otherwise
        """
        if row < 0 or col < 0 or row >= self.n or col >= self.n:
            return Exception("Move board is out of bounds")
        if self.board[row][col] != "":
            return Exception("Move already made in this spot")
        if player not in (0,1):
            return Exception("Invalid player")
        currentMove = 1 if player == 1 else -1
        self.board[row][col] = currentMove
        self.rowSum[row] += currentMove
        self.colSum[col] += currentMove
        if row == col:
            self.diagSum += currentMove
        if row == self.n - col - 1:
            self.revDiagSum += currentMove
        if abs(self.rowSum[row]) == self.n or abs(self.colSum[col]) == self.n or self.diagSum == self.n or self.revDiagSum == self.n:
            self.winner = player
        return 0 if self.winner == 0 else 1
        # currentMove = self.board[row][col]
        # We need to check the row
        # winRow, winCol, winDiag, winRevDiag = True, True, True, True
        # for i in range(self.n):
        #     if self.board[row][i] != currentMove:
        #         winRow = False
        #     if self.board[i][col] != currentMove:
        #         winCol = False
        #     if self.board[i][i] != currentMove:
        #         winDiag = False
        #     if self.board[i][self.n-i-1] != currentMove:
        #         winRevDiag = False
        # if winRow or winCol or winDiag or winRevDiag:
        #     return player
        # return -1
    def getWinner(self)->int:
        return self.winner
    