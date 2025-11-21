class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # add all of the letters in s1 to a map of sorts, and then iterate through s2 with a sliding window, checking if we have the characters?

        s1_map = {}
        for s in s1:
            if s in s1_map:
                s1_map[s] += 1
            else:
                s1_map[s] = 1

        # We now have a map of all required characters!

        s2_map = {}
        l = r = 0

        if len(s1) > len(s2):
            return False

        while r < len(s1):
            char = s2[r]
            if char in s2_map:
                s2_map[char] += 1
            else:
                s2_map[char] = 1

            r += 1
        r -= 1
        while r < len(s2):
            # check if the maps are equivalent
            if s1_map == s2_map:
                return True
            else:
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1
                r += 1
                if r < len(s2):
                    if s2[r] in s2_map:
                        s2_map[s2[r]] += 1
                    else:
                        s2_map[s2[r]] = 1

        return False