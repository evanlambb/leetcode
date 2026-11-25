class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        c1, c2 = 0,0
        while True:
            if c1 < len(word1) and c2 < len(word2):
                ans += word1[c1] + word2[c2]
                c1 += 1
                c2 += 1
            elif c1 < len(word1):
                ans += word1[c1:]
                break
            else:
                ans += word2[c2:]
                break

        return ans