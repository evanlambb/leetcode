class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        l = "abcdefghijklmnopqrstuvwxyz"
        letters_rev = l[::-1]
        letters = dict()
        ans = ""
        for i in range(len(letters_rev)):
            letters[i] = letters_rev[i]

        for word in words:
            s = 0
            for letter in word:
                s += weights[ord(letter) - ord('a')]
            s %= 26
            ans += letters[s]

        return ans