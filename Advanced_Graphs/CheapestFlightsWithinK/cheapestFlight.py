class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # We can solve this problem using bellman-Ford algorithm
        # Since we are given constraint to return the cheapest price from s to d within k stops
        # it would be more challenging to implement djikstra algorithm. Hence we could solve it using bellman ford
        # Tradeoff: If there is a cycle in the graph then bellman ford would not work -> there are no multiple flights between two cities
        # Time-> O(E*k): Usually BFA runs at O(E*V) but since we are given k stops it would O(E*k)
        # Advantage: Can deal with negative weights unlike Djikstra
        prices = [float("inf") for _ in range(n)] # we set the prices as infinity for all the nodes except the starting node
        prices[src] = 0

        # perform the bellman ford Algo for k times
        for i in range(k+1):
            tmpPrices = prices.copy()
            # We go through every single edge
            for s,d,p in flights: # s=src, d=dest, p=price
                # If we cannot reach the source node then we skip
                if prices[s] == float("inf"):
                    continue
                # If we found a new smallest price with current price then we update it (Relaxation)
                if prices[s] + p < tmpPrices[d]: # we could have updated tmpPrices so we use it for reference
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1
                

