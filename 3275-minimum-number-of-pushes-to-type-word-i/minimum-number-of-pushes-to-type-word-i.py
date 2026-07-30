class Solution:
    def minimumPushes(self, word: str) -> int:
        # count the number of distinct numbers 
        # count the occurences of the numbers 
        letters = defaultdict(int)
        for letter in word:
            letters[letter] += 1

        # we then map the most occurences to the first press, then second and third... 
        
        occurances = sorted(letters.values())
        mult = 1
        count = 0
        ans = 0
        for i in range(len(occurances) - 1, -1, -1):
            if count == 8:
                count = 0
                mult += 1
            ans += mult * occurances[i]
            count += 1
        return ans