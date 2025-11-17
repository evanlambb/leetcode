from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            item = str(len(string)) + "." + string
            ans = ans + item

        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            num = 0
            while s[i].isdigit():
                num *= 10
                num += int(s[i])
                i+= 1
            # the first non-digit character
            ans.append(s[i+1:i+1+num])

            i += num + 1

        return ans
    
s = Solution()
l = ["neet", "code", "loves", "you"]
print(s.decode(s.encode(l)))