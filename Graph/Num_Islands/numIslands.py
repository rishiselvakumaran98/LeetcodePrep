from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Runtime: O(mxn)
        Space: O(min(m,n))
        The function numIslands takes a grid of characters representing land ('1') and water ('0') and
        returns the number of distinct islands in the grid.
        
        :param grid: The `grid` parameter is a 2D grid of characters representing land ('1') and water
        ('0'). The goal of the `numIslands` function is to determine the number of islands in the grid,
        where an island is formed by connecting adjacent lands horizontally or vertically
        :type grid: List[List[str]]
        """
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.bfs(r,c,grid)
                    count += 1
        return count
    
    
    def isValid(self, r, c, grid):
        if r < 0 or c  < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
            return False
        return True
    
    def bfs(self, r, c, grid):
        q = deque([(r,c)])
        grid[r][c] = "#"
        while q:
            row, col = q.popleft()
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nr, nc = row+i, col+j
                if self.isValid(nr, nc, grid):
                    grid[nr][nc] = "#"
                    q.append((nr, nc))
        
