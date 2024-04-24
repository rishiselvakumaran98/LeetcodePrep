class Solution:
    # If we use a brute force approach to solve it we can use recursion
    # However this is not efficient as we keep recursing over similar states
    def climbStairs_bruteForce(self, n):
        def climbStairHelper(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return climbStairHelper(i+1) + climbStairHelper(i+2)
        return climbStairHelper(0)
    
    # We can use Memoization to reduce time complexity or preventing the need to visit repeated states 
    # which reduces the time complexity from O(2^n) to O(n)
    def climbStairs_Memoization(self, n: int) -> int:
        climbArray = [0]*(n+1)
        def climbStairHelper(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if climbArray[i] > 0:
                return climbArray[i]
            climbArray[i] = climbStairHelper(i+1) + climbStairHelper(i+2)
            return climbArray[i]
        return climbStairHelper(0)
    # we can alternatively do this using a DP method as well
    def climbStairs_DP(self, n):
        # used to eliminate an Edge case
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    # We can use an even more efficient way
    # Since are are only interested in the first, second and the next number formed
    # We can essentially use them to find the solution
    def climbStairs_Fib(n):
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first+second
            first = second
            second = third
        return second

        