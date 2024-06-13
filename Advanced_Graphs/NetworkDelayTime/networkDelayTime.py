import collections
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Summary of Djikstra Algorithm:
        # We can implement Djikstra Algo to solve this problem -> Shortest path greedy approach to solve this
        # WE implement a BFS approach and use a MinHeap (Priority-Queue) to iterate over the nodes with shortest path
        # We visit nodes that are right next to our frontier
        # MinHeap can get us the min value to traverse to the next node (Adding into account the sum of paths from each level iteration)
        # In minHeap we store the values as (Path, node) -> path: weight to get to that node
        # We start by initializing the heap to heap = [(0, 1)] -> Starting from 1 to get to 1
        # We pop the node from heap, and look at all its neighbor nodes
        # Time complexity -> E = V^2 (Due to bidirectional edges). Since we use a minHeap -> O(E*log(V^2)) -> 2*E*Log(V) -> O(E*log(v))
        # Space Complexity -> E ()
        """

        # We keep a adjaceny List to store the source nodes to their neighboring nodes
        edges = defaultdict(list)
        for u,v, w in times:
            edges[u].append((v,w))
        
        # Initialize the minheap to the first node
        minHeap = [(0, k)] # (0,k) will be the first node
        # We keep a visited set to make sure we dont visit the nodes again or form a cycle
        visited = set()
        res = 0
        while minHeap: # while out minheap is non-empty
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited: # if we already visited the node then just pop the next element
                continue
            visited.add(n1)
            res = max(res, w1)

            # We now go through all the neighbors and add them to the minHeap and their current weight 
            for neighbor, w2 in edges[n1]:
                if neighbor not in visited:
                    heapq.heappush(minHeap, (w1+w2, neighbor))
            
        return res if len(visited) == n else -1