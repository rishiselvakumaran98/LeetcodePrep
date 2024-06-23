class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # We can solve this problem using the idea of finding the first pos
        # diff between gas[i]-cost[i] and seeing if this diff drops below 0
        # if so we would not be able to finish the loop we started

        # A straightforward edge case to check:
        # check if the sum(gas) < sum(cost): if so return -1 as we would not be able to traverse through the gas stations

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1 # We set start to the next index where we want the iteration to start
        return start