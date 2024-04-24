class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # We want to keep two sets pac, atl to keep track of the r,c we visited in ocean grid
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        # we want to setup a dfs function to iterate through a given point recrusively and add it to the given set
        def dfs(r, c, visit, prevHeight):
            # base condition where we dont add any coordinate 
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or heights[r][c] < prevHeight:
                return
            
            visit.add((r,c))
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])

        # Since we start from the corners of the board and add coordinates from row and cols
        # into the 
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        # add the coordinates we added in the atlantic and pacific ocean into the
        res = [] 
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


