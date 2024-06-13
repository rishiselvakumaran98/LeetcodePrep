# There are three ways to solve this problem
# The Brute force solution where we use recurrence relation 
# to store the previous sequences in an array and use its value 
# to find the min cost required to climb the stair sequence
# using 1 or 2 steps

class Solution:
    def minCostClimbingStairs_BU(self, cost: List[int]) -> int:
        n = len(cost)
        minimum_cost = [0]*(n+1)
        for i in range(2,n+1): 

            oneStep = minimum_cost[i-1] + cost[i-1]
            twoStep = minimum_cost[i-2] + cost[i-2]
            minimum_cost[i] = min(oneStep, twoStep)
        return minimum_cost[n]

    def minCostClimbingStairs_Memo(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def minimum_cost(i):
            if i <= 1:
                return 0
            if i in memo:
                return memo[i]
            oneStep = minimum_cost(i-1) + cost[i-1]
            twoStep = minimum_cost(i-2) + cost[i-2]
            memo[i] = min(oneStep, twoStep)
            return memo[i]
        return minimum_cost(n)
    
    def minCostClimbingStairs_Optimal(self, cost: List[int]) -> int:
        n = len(cost)
        oneStep = twoStep = 0
        for i in range(2, n+1):
            temp = oneStep
            oneStep = min(oneStep+cost[i-1], twoStep+cost[i-2])
            twoStep = temp
        return oneStep
                    
                    