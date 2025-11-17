from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # it is simple, we will go through each word, map the letters, and then see if we already have that same map in the res
        res = []
        patterns = {} # [0,1,2,3,...,25] : index in res
        # where the list is the letter distrobution and the index is where that pattern is located in the list

        for word in strs:
            letters = []
            for _ in range(26):
                letters.append(0)

            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            if tuple(letters) not in patterns:
                patterns[tuple(letters)] = len(res)
                res.append([])
            res[patterns[tuple(letters)]].append(word)

        return res
