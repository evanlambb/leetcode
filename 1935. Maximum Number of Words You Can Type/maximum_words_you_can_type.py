class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        letters = {}
        for i in range(len(brokenLetters)):
            if brokenLetters[i] not in letters:
                letters[brokenLetters[i]] = 1



        words = text.split()

        word_count = 0
        for word in words:
            for letter in word:
                if letter in letters:
                    word_count -= 1
                    break

            word_count += 1

        return word_count
