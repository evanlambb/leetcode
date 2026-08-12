class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # if the letters are the same, we take dp[r+1][c+1]

        # if the letters are different, 

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        sum1 = 0
        sum2 = 0
        print(dp)
        for char in s1:
            sum1 += ord(char)
        for char in s2:
            sum2 += ord(char)
        for i in range(len(s1) + 1):
            dp[i][len(s2)] = sum1
            sum1 -= ord(s1[i]) if i < len(s1) else 0
        for i in range(len(s2) + 1):
            dp[len(s1)][i] = sum2
            sum2 -= ord(s2[i]) if i < len(s2) else 0

        print(dp)

        for r in range(len(s1) -1, -1, -1):
            for c in range(len(s2) - 1, -1, -1):
                if s1[r] == s2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = min(dp[r][c+1] + ord(s2[c]), dp[r+1][c] + ord(s1[r]))
        return dp[0][0]