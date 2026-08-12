class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS, COLS = len(triangle), len(triangle[-1])
        dp = [[0] * (COLS  + 1) for _ in range(ROWS + 1)]

        row = 0
        for level in triangle:
            for col in range(len(level)):
                dp[row][col] = level[col]

            row += 1

        for row in range(ROWS -1, -1, -1):
            for col in range(COLS -1, -1, -1):
                dp[row][col] = dp[row][col] + min(dp[row+1][col], dp[row+1][col+1])
        return dp[0][0]