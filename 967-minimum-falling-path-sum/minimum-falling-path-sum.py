class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        mn = float('inf')
        for r in range(1, ROWS):
            for c in range(COLS):
                consider = []
                if c - 1 >= 0:
                    consider.append(matrix[r-1][c-1])
                if c + 1< COLS: 
                    consider.append(matrix[r-1][c+1])
                consider.append(matrix[r-1][c])
                mn_consider = consider[0]
                for item in consider:
                    mn_consider = min(mn_consider, item)
                matrix[r][c] += mn_consider
        for c in range(COLS):
            mn = min(mn, matrix[ROWS - 1][c])
        return mn