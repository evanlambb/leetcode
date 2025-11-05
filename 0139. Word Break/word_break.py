from typing import List

class Solution:
    def __init__(self):
        self.dp = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        elif s in self.dp:
            return self.dp[s]

        for i in range(1, len(s) + 1):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    self.dp[s] = True
                    return True
        self.dp[s] = False
        return False