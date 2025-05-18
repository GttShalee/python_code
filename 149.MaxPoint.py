# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
# return the maximum number of points that lie on the same straight line.
from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        max_points = 0

        for i in range(len(points)):
            slope_count = defaultdict(int)
            overlap = 0
            cur_max = 0
            x1, y1 = points[i]

            for j in range(i+1, len(points)):
                x2, y2 = points[j]

                dx, dy = x2 - x1, y2 - y1

                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                
                g = gcd(dx, dy)
                if g != 0:
                    dx, dy = dx // g, dy // g
                
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                
                slope = (dy, dx)
                slope_count[slope] += 1
                cur_max = max(cur_max, slope_count[slope])

            max_points = max(max_points, cur_max + overlap + 1)

        
        return max_points
        

sol = Solution()
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))