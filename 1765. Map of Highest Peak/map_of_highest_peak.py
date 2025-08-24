from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minutes = 0
        fresh = 0

        q = deque()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c,minutes])
                elif grid[r][c] == 1:
                    fresh += 1

        while q:
            r, c, minutes = q.popleft()
            neighbours = [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]
            for neighbour in neighbours:
                nr, nc = neighbour
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append([nr, nc, minutes + 1])

        if fresh != 0:
            return -1
        return minutes
                