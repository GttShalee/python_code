# 62. Unique Path

import math

class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     result = 0
    #     if m == 1 or n == 1:
    #         result = 1
    #     else:
    #         result += self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    #     return result

# In fact this ia a math problem in combinatorics.
# So we can see that the robot need total n + m - 2 steps to reach the final.
# But it only need n - 1 steps to reach the bottom right bottom.
# So we just caculate the combination of n - 1 steps in n + m - 2 steps.
# The formula is C(n + m - 2, n - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)
        
        # But we can also use the dp to solver this problem
    def dp(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]




solution = Solution()
result = solution.uniquePaths(23, 40)
print(result)