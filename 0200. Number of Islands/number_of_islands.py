from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        seen = set()

        # at this point, we know how many lands we are looking for, now we just go and find them all... 
        def dfs(r, c):
            if (r, c) in seen:
                return 0
            if grid[r][c] == "0":
                seen.add((r,c))
                return 0 

            # we have now visited this square. 
            seen.add((r, c))
            # we need to check around us now...
            neighbours = [[r, c + 1], [r + 1, c], [r - 1, c], [r, c - 1]]
            for neighbour in neighbours:
                new_row, new_col = neighbour
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                    dfs(new_row, new_col)

            return 1


        for i in range(rows):
            for j in range(cols):
                islands += dfs(i, j)

        return islands