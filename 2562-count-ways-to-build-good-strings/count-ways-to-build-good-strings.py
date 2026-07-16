class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # At each step, you either apply the zero rule or the one rule... 
        # if we get a string that is in the range of low - high, then we add 1 to our count... 
        dp = [0] * (high + 1)
        dp[0] = 1

        for i in range(1, len(dp)):
            dp[i] = (dp[i-zero] if i - zero >= 0 else 0) + (dp[i-one] if i - one >= 0 else 0) % (pow(10,9) + 7)
        count = 0

        for i in range(low, high + 1):
            count += dp[i]
            count %= (pow(10,9) + 7)

        return count