class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        visited = set() # (row, col)
        heap = [] # our MaxHeap
        ROWS, COLS = len(grid), len(grid[0])
        heappush(heap, (-1 * (health - grid[0][0]), 0,0))
        visited.add((0,0))
        while heap:
            h, r, c = heappop(heap)
            h *= -1
            r *= -1
            c *= -1
            if r == ROWS - 1 and c == COLS - 1:
                return True
            dr = [1,-1,0,0]
            dc = [0,0,1,-1]

            for i in range(4):
                row = r + dr[i]
                col = c + dc[i]

                if row >= 0 and col >= 0 and row < ROWS and col < COLS and (row, col) not in visited and h - grid[row][col] > 0:
                    new_h = h - grid[row][col]
                    visited.add((row, col))
                    heappush(heap, (-1 * new_h, -1 * row, -1 * col))
        return False
