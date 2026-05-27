class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # have we already seen the upper case
        # have we seen the lower case previously
        seenUpper = set()
        seenLower = set()
        counts = [0] * 26
        for c in word:
            ind = ord(c.lower()) - ord('a')
            if c.islower():
                if c.upper() in seenUpper: # we want this to be zero! 
                    counts[ind] = 0 # set it back to zero... 
                if c not in seenLower:
                   seenLower.add(c)

            else:
                # c is uppercase 
                if c.lower() in seenLower and c not in seenUpper:
                    counts[ind] = 1
                    seenUpper.add(c)
                elif c not in seenUpper:
                    seenUpper.add(c)

        return sum(counts)