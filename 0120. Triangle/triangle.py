from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        visited = {}
        def dfs(row, ind):
            if (row == len(triangle)):
                return 0
            elif (row, ind) in visited:
                return visited[(row, ind)]
            else:
                s = triangle[row][ind] + min(dfs(row + 1, ind), dfs(row + 1, ind + 1))
                visited[(row, ind)] = s
                return s
        return dfs(0,0) 