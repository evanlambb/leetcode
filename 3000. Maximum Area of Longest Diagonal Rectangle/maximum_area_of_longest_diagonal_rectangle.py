from typing import List
from math import sqrt

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        diagonal_len = 0
        for rect in dimensions:
            if sqrt(rect[0]**2 + rect[1]**2) == diagonal_len:         
                max_area = max(max_area, rect[0] * rect[1])
            elif sqrt(rect[0]**2 + rect[1]**2) > diagonal_len:
                diagonal_len = sqrt(rect[0]**2 + rect[1]**2)
                max_area = rect[0] * rect[1] 

        return max_area
            
        