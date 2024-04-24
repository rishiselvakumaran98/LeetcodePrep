class Solution:
    def findRedundantConenction(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)


        def find(n): # if we are given a node n we want to find what its parent is
            p = parent[n] # we want to find the root parent
            # we are going to keep going upwards util we find the root parent
            while p != parent[p]:
                parent[p] = parent[parent[p]] # path compression algo where we set the parent of p to its grand parent
                # we shorten the chain as we go up the link
                p = parent[p]
            # once we reach the root parent then return it
            return p

        def union(n1, n2):
            # to union the nodes we want to find the root parent of the node n1 and n2
            p1, p2 = find(n1), find(n2)
            # return false if the root parents are the same (redundant connection)
            if p1 == p2:
                return False
            # we union them by rank
            if rank[p1] > rank[p2]: # if the rank of p1 is higher than p2 then p1 gets to be the parent of p2
                parent[p2] = p1
                rank[p1] += rank[p2] # update the rank of p1 as it has more children than before 
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            # if we are able to union them together then we return True
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2): # if are not able to union them then they are redundant connection
                return [n1, n2]






