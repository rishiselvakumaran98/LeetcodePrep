'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas 
and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead 
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Ex:

Input: piles = [3,6,7,11], h = 8
Output: 4

'''

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the length of piles will always be <= h
        # brute force solution would be to use all the numbers 1...11 (until max number of banana in a pile)
        # then check if the piles[i]/number for each pile adds upto <= h

        # we can do binary search algorithm to reduce time to O(log(n) * p)
        l = 0
        r = max(piles)
        result = 2**31
        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                result = min(result, k)
                # we still want to find the best k which is min
                r = k-1
            else:
                l = k+1
        return result