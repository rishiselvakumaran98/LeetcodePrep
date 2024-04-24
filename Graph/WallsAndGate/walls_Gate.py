class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Setup a queue that will hold the positions of the gates
        # we select each gate and from that gate traverse to the neighboring cells and while 
        # traversing we will add the distance relative to gate to the cell min(cell_value, distance)

        q = deque()
        ROWS, COLS = len(rooms), len(rooms[0])
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    # initially populate the queue with their gates
                    q.append((r, c, 0))
        
        while q:
            # get the coordinates of the Room
            row, col, dist = q.popleft()
            for r,c in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                rr, cc = row+r, col+c
                if 0 <= rr < ROWS and 0 <= cc < COLS and rooms[rr][cc] == 2147483647:
                    rooms[rr][cc] = dist + 1
                    q.append((rr,cc, dist+1))