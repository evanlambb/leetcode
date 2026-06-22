class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = [0] * 26
        for letter in text:
            counts[ord(letter) - ord('a')] += 1
        return min(counts[0], counts[1], counts[11] // 2, counts[13], counts[14] // 2)