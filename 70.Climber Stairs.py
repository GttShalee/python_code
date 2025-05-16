# @lc app=leetcode id=70 lang=python3
# [70] Climbing Stairs
import math
class Solution:
    # use the pure recursive
    # but it will result time limit exceed
    def climbStairs1(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        # Idea 2 : use dictionary (look-up table) to memorize repeating recursion
        # - The memory start with the base case and recored every recurssion
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]
    
# test
test = Solution()
print(test.climbStairs(3))
print(test.climbStairs(2))