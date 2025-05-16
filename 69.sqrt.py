# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            # 判断 mid 的平方是否是 x 的有效平方根范围
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            # 调整搜索范围：向左半部分查找
            elif mid * mid > x:
                right = mid - 1

# TEST
x = 8
print(Solution().mySqrt(x))