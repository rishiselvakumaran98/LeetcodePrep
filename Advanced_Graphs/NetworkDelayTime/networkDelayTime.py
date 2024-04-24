import collections
import heapq
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build a Adjancency list of all the edges from starting node 
        adj_list = collections.defaultdict(list)
        for u,v,w in times:
            adj_list[u].append((v,w))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            # set to the max between itself and overall weight traversed
            t = max(t, w1)
            for n2, w2 in adj_list[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))
            
        return t if len(visited) == n else -1
