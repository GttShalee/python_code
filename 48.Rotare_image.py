# 48. Rotate Image
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose which meand  the column become the row
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse which means change the row
        for i in range(len(matrix)):
            matrix[i].reverse()
        
        return matrix
    
# test case
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().rotate(matrix))