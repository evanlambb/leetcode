class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        grid = [matrix[0]]
        grid +=  [['0' for c in range(COLS)] for r in range(ROWS - 1)]
        ans = 0
        
        for c in range(COLS):
            if matrix[0][c] == "1":
                ans = 1
        if ROWS == 1:
            return ans
       
        for r in range(1, ROWS):
            for c in range(COLS):
                top, left, diag = 0, 0, 0
                top = int(grid[r-1][c])
                if c - 1 >= 0:
                    diag = int(grid[r-1][c-1])
                    left = int(grid[r][c-1])
                grid[r][c] = str(min(top, left, diag) + 1) if matrix[r][c] == "1" else "0"
                ans = max(ans, int(grid[r][c]))
        print(grid)
        return ans**2