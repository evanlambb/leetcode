class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = sorted(ransomNote) 
        mag = sorted(magazine)

        if len(ran) > len(mag):
            return False

        i = j = 0
        while i < len(ran):
            if j >= len(mag):
                return False
            if ran[i] < mag[j]: # we are missing a letter.
                return False
            elif ran[i] == mag[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True