class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        dp = [[0 for _ in range(COLS+1)] for _ in range(ROWS + 1)]
        for r in range(ROWS -1, -1, -1):
            for c in range(COLS -1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r+1][c+1] + 1
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        return dp[0][0] 