class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                # if its 1 we add it to the fresh count
                if grid[r][c] == 1:
                    fresh += 1
                #  if its 2 then then we add it to q
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for r,c in [(-1,0), (1,0), (0,-1), (0, 1)]:
                    rr, cc = row+r, col+c
                    if rr < 0 or cc < 0 or rr == ROWS or cc == COLS or grid[rr][cc] != 1:
                        continue
                    grid[rr][cc] = 2
                    fresh -= 1
                    q.append((rr,cc))
            time += 1

        return time if fresh == 0 else -1

                