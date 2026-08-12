class Solution:
    def numSquares(self, n: int) -> int:
        num = 1
        squares = []
        while num**2 <= n:
            squares.append(num**2)
            num += 1
        # now i have all of the relevant squares. 
        dp = [float('inf')] * (n + 1) 
        dp[0] = 0
        for i in range(1, n + 1):
            for square in squares:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i-square] + 1)
                else:
                    break
        return dp[-1]