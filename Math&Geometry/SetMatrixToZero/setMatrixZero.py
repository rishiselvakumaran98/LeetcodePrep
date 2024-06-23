class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # check where the 0s are in the matrix, then use those r,c points as reference to set the matrix values to 0
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for r in range(R):
            # check to see if we should set the first col to 0
            if matrix[r][0] == 0:
                is_col = True
            for c in range(1,C):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
            
        # set the matrix cells we marked the left row and top col as zero into 0
        for r in range(1,R):
            for c in range(1,C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        # if the matrix cells in the first cell is 0 then set remaining cells in the cols to 0
        if matrix[0][0] == 0:
            for c in range(C):
                matrix[0][c] = 0
        # if the col is zero then set the remaining cells in the row to 0
        if is_col:
            for r in range(R):
                matrix[r][0] = 0