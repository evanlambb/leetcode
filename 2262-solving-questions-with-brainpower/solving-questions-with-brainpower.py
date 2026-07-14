class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # we will iterate the array in reverse... 
        dp = [0] * len(questions)
        for i in range(len(questions)-1, -1, -1):
            # iterate the array backwards
            points, brainpower = questions[i][0], questions[i][1]
            dp[i] = max(points + (dp[i + 1 + brainpower] if i + 1 + brainpower < len(questions) else 0), 
                        dp[i+1] if i + 1 < len(questions) else 0)
        return dp[0]