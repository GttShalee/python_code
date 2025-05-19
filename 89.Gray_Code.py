# 89 Gray Code
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        max_num = 1 << n
        return [i ^ (i >> 1) for i in range(max_num)]

# Example usage
if __name__ == "__main__":
    sol = Solution()
    n = 3
    result = sol.grayCode(n)
    print(f"Gray code for n={n}: {result}")