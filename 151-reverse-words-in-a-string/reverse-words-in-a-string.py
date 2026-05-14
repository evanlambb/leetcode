class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        s = ""
        for i in range(len(words) - 1, -1, -1):
            s = s + words[i]
            if i != 0:
                s += " "
        return s