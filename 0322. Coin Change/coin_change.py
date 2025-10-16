from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        for i in range(amount + 1):
            dp.append(amount+1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[-1] > amount:
            return -1
        return dp[-1]