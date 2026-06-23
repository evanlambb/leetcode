class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0] * (len(obstacleGrid[0]) + 1) for _ in range(len(obstacleGrid) + 1)]
        dp[len(obstacleGrid)][len(obstacleGrid[0]) - 1] = 1
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1] if obstacleGrid[r][c] == 0 else 0
        return dp[0][0]