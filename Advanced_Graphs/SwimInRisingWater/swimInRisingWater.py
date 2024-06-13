import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # This problem could b a modified version of Djikstra Algorithm 
        # build a adjacency list
        # or the grid is the adjacency list
        minHeap = [(grid[0][0], 0,0)] # (r,c,grid[r][c])
        visited = set()
        total = 0
        N = len(grid)
        while minHeap:
            current_time, r,c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            total = max(current_time, total)
            if (r,c) == (N-1, N-1):
                return total
           
            for R,C in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                # print((R,C))
                if 0 <= R < N and 0 <= C < N and (R,C) not in visited:
                    heapq.heappush(minHeap, (max(current_time, grid[R][C]), R, C))
        return total