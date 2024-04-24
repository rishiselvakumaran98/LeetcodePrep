class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # if the empty list is given or there is no cells in it
        if not heightMap or not heightMap[0]:
            return 0

        # if the len of the board is 3 or less then it means that the board cannot trap rainwater
        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0
        
        # Add the bordering cells around the edges of the board into the heap
        heap = []
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    #mark the heightMap as visited in the board
                    heightMap[i][j] = -1
        
        # Use the heap to perform a BFS search where we pop the smaller heights first from the 
        # heap as levels and then visit the neightbor nodes which has height smaller than the current level
        # if the height is smaller than it means the current cell can trap water and hence we could add the difference
        # to the res variable
        res = 0
        level = 0
        while heap:
            height, x, y = heapq.heappop(heap)
            level = max(level, height)# we take the height that is max at the current moment in the heap

            for r,c in [(-1,0), (0,-1), (1,0), (0,1)]:
                i, j = x+r, y+c
                if 0 <= i < rows and 0 <= j < cols and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    # if the current height is smaller then it could trap water so add it to overall result
                    if heightMap[i][j] < level:
                        res += level-heightMap[i][j]
                    
                    # Mark the coordinate as visited
                    heightMap[i][j] = -1
        return res