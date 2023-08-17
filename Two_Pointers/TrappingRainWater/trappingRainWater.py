from typing import List


class Solution:
    #  UnOptimized but brute force solution
    def trap_UnOptimized(self, height: List[int]) -> int:
        n = len(height)
        maxLeftArray = [0]*n
        maxRightArray = [0]*n
        maxLeft = 0
        maxRight = 0
        minItem = 0
        sum_water = 0
        # we store into the maxleft array
        for i in range(n):
            maxLeftArray[i] = maxLeft
            maxLeft = max(maxLeft,height[i])
        # we store into the maxRight array
        for i in range(n-1, -1, -1):
            maxRightArray[i] = maxRight
            maxRight = max(maxRight, height[i])
        # we store into the minArray
        for i in range(n):
            minItem = min(maxLeftArray[i], maxRightArray[i])
            relativeWater = minItem - height[i]
            sum_water += relativeWater if relativeWater > 0 else 0
        return sum_water
            
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height)-1
        leftMax = height[0]
        rightMax = height[-1]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

