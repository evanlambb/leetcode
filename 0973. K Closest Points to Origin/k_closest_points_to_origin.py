from typing import List
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # base case, everything is included:
        if k >= len(points):
            return points

        # can i just implement a custom sort?
        return sorted(points, key = lambda p: sqrt(p[0]**2 + p[1]**2))[:k]