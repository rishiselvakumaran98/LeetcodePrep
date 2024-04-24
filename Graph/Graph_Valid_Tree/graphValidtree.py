class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        parents = [i for i in range(n)]
        rank = [1] * (n)

        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[[parents[p]]]
                p = parents[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += p2
            else:
                parents[p1] = p2
                rank[p2] += p1
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return False
        return True


