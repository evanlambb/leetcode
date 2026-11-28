class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        letters = dict()

        for i, c in enumerate(order):
            letters[c] = i

        # returns 1 if w1 < w2, 0 if same, -1 otherwise
        def cmp(w1, w2):
            i = 0

            while i < len(w1) and i < len(w2) and w1[i] == w2[i]:
                i += 1
            if i == len(w1) and i == len(w2):
                return 0
            elif i == len(w1):
                return 1
            elif i == len(w2):
                return -1
            else:
                if letters[w1[i]] < letters[w2[i]]:
                    return 1
                return -1


        for k in range(len(words) -1):
            w1 = words[k]
            w2 = words[k+1]

            if cmp(w1,w2) == -1:
                return False

        return True
                