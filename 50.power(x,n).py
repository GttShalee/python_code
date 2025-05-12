# 50.power(x,n).py
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow1(x, -n)
        elif n % 2 == 0:
            return self.myPow1(x*x, n/2)
        else:
            return x * self.myPow1(x, n-1)
    def myPow2(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result


solution = Solution()
print(solution.myPow1(2.0, 10))
print(solution.myPow2(2.0, 10))

