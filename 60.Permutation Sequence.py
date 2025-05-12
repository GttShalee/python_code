#  60.Permutation Sequence.py
from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]  # 数字集合
        k -= 1  
        result = ""

        for i in range(n, 0, -1):
            f = factorial(i - 1)  # (i-1)!
            index = k // f        # 当前位选哪个数
            result += nums.pop(index)  # 选中该数
            k %= f               # 更新k（剩余排列中的第几项）
        
        return result

if __name__ == "__main__":
    solution = Solution()
    n = 3
    k = 3
    result = solution.getPermutation(n, k)
    print(result)