class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build a adjacecncy list of the src -> dst 
        # after building the Adjacency list, sort each of the values in Lex ordering
        adj_list = defaultdict(list)

        for src, dst in tickets:
            adj_list[src].append(dst)
        # Sort through the dict values
        for src in adj_list.keys():
            adj_list[src].sort(reverse=True)
        
        path, visited = set(), set()
        result = []

        def dfs(src):
            while adj_list[src]:
                next_dst = adj_list[src].pop()
                dfs(next_dst)
            result.append(src)
        
        dfs("JFK")
        return result[::-1]

        # Keep a path, visited set
        # Use a output array
        # Perform DFS on the tickets and append it to the output array

        # once we are able to traverse through the cities return the array
