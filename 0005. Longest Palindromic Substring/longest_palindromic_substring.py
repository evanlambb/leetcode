class Solution:
    def checkPalindrome(self, s: str, l: int, r: int, res: str, resLen: int):
        while(l >= 0 and r < len(s) and s[l] == s[r]):
            if (r - l + 1) > resLen:
                resLen = r - l + 1
                res = s[l:r+1]
            l -= 1
            r += 1
        return resLen, res

    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # check the odd
            l, r = i, i
            resLen, res = self.checkPalindrome(s, l, r, res, resLen)

            l, r = i, i + 1
            resLen, res = self.checkPalindrome(s, l, r, res, resLen)

        return res        