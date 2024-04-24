import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Time: O(n^2 * Log(n))--> We add the points multiple times to the minHeap during BFS it would be (n^2). Then since we pop them from the heap and add it for traversal it would log n
        '''
        # We build an adjancency list consisting of edges between all the points to each other
        # Then we use Prim's algorithm to use Min Spanning tree concept to calculate the minimum cost
        # using a Greedy technique of storing the edges in a Min heap and popping them based on their cost

        '''
        To connect all the edges without forming cycle it will take as n-1 edges -> n=number of vertices or points
        We use a set to keep track of the points visited to avoid cycles
        ### The way prim's algorithm works:
        ### 1. Choose any vertex in the graph
        ### 2. Perform a BFS search on the node where we use a cycle to keep track of visited nodes
        ### 3. Keep a MinHeap (Frontier) to add (dist, (point_x, point_y)) between the nodes
        ### 4. Once the length of the visit sets equals 
        '''

        # First Build the adjacency list of all the points connected to each other from the points
        N = len(points)
        adj_list = {i: [] for i in range(N)} # adj_list consisting of the [cost, point]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                adj_list[i].append([cost, j])
                adj_list[j].append([cost, i])
        
        # Now we perform Prim's Algorithm on the graph
        res = 0
        visited = set()
        minHeap = [[0,0]]
        while len(visited) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neiCost, nei in adj_list[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res