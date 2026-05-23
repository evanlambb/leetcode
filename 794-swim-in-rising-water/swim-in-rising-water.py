class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m = -1
        locations = [(grid[0][0],0,0)]
        seen = set((0,0))
        while locations:
            h,r,c = heapq.heappop(locations)
            m = max(h, m)
            if r == len(grid) - 1 and c == len(grid[0]) - 1: # we are at the location
                return m
            else:
                dr = [1, -1, 0, 0]
                dc = [0, 0, 1, -1]

                for i in range(4):
                    row = r + dr[i]
                    col = c + dc[i]

                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and (row,col) not in seen: # the square is valid
                        seen.add((row,col))
                        heapq.heappush(locations, (grid[row][col], row, col))
