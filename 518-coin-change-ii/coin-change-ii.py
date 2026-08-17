class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(dp)):
            dp[i][0] = 1

        for i in range(len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] += dp[i-1][j] if i > 0 else 0
                dp[i][j] += dp[i][j-coins[i]] if j - coins[i] >= 0 else 0

        return dp[-1][-1]