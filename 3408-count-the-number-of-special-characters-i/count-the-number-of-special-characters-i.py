class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        little = [0] * 26
        big = [0] * 26

        for letter in word:
            if ord('a') <= ord(letter) <= ord('z'):
                little[ord(letter) - ord('a')] += 1
            elif ord('A') <= ord(letter) <= ord('Z'):
                big[ord(letter) - ord('A')] += 1

        count = 0
        for i in range(26):
            if little[i] > 0 and big[i] > 0:
                count += 1

        return count